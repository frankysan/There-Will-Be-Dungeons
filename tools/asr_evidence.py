"""Lossless lexical evidence with explicit word/cue/unknown timing precision."""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
import hashlib
import json
import math
from pathlib import Path, PureWindowsPath
import re
import unicodedata

from build_transcripts import parse_srt

TOKEN = re.compile(r"[^\W_]+(?:['’][^\W_]+)*", re.UNICODE)


def normalized(text):
    return [m.group().lower().replace('’', "'") for m in TOKEN.finditer(unicodedata.normalize('NFKC', text))]


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                                     allow_nan=False).encode()).hexdigest()


def number(value, name, nullable=False):
    if nullable and value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f'{name} must be a finite number')
    return value


def interval(value, name):
    if not isinstance(value, list) or len(value) != 2:
        raise ValueError(f'{name} must be [start_ms, end_ms]')
    a, b = [number(v, name) for v in value]
    if a < 0 or b <= a:
        raise ValueError(f'{name} must have 0 <= start < end')
    return a, b


@dataclass
class Word:
    id: str
    text: str
    norm: str
    segment_id: str
    char_start: int
    char_end: int
    start_ms: float | None
    end_ms: float | None
    timing: str  # word, cue, segment, unknown; cue intervals are NOT word timings
    speaker: str | None = None
    confidence: float | None = None
    source_word_index: int | None = None


@dataclass
class Run:
    id: str
    episode: str
    audio: dict
    coverage_ms: list
    metadata: dict
    source: dict
    words: list[Word] = field(default_factory=list)
    segments: list[dict] = field(default_factory=list)

    def export(self):
        return asdict(self)


def safe_metadata(value):
    """Prevent accidental propagation of workstation paths from manifests."""
    if isinstance(value, dict):
        for item in value.values():
            safe_metadata(item)
    elif isinstance(value, list):
        for item in value:
            safe_metadata(item)
    elif isinstance(value, str) and (re.search(r'[A-Za-z]:[\\/]|\\\\', value)
                                   or value.startswith('/')):
        raise ValueError('Use portable labels, not absolute paths, in metadata')


def load_run(spec, base, episode, audio):
    required = ('id', 'path', 'format', 'coverage_ms', 'model', 'version',
                'quantization', 'settings', 'processing_seconds')
    if any(key not in spec for key in required):
        raise ValueError(f'Run requires {required}; use null for unknown metadata')
    if not re.fullmatch(r'[A-Za-z0-9_.-]+', spec['id']):
        raise ValueError('Run id must be a portable identifier')
    if not isinstance(spec['settings'], dict):
        raise ValueError('settings must be an object')
    for key in ('model', 'version', 'quantization'):
        if spec[key] is not None and not isinstance(spec[key], str):
            raise ValueError(f'{key} must be a string or null')
    if spec.get('audio_id', audio['id']) != audio['id'] or spec.get('audio_sha256', audio.get('sha256')) != audio.get('sha256'):
        raise ValueError('Run declares a different audio identity')
    coverage = list(interval(spec['coverage_ms'], 'coverage_ms'))
    if coverage[1] > audio['duration_ms']:
        raise ValueError('coverage exceeds audio duration')
    elapsed = number(spec['processing_seconds'], 'processing_seconds', True)
    if elapsed is not None and elapsed < 0:
        raise ValueError('processing_seconds cannot be negative')
    offset = number(spec.get('timestamp_offset_ms', 0), 'timestamp_offset_ms')
    meta = {k: spec[k] for k in required if k not in ('id', 'path', 'format', 'coverage_ms')}
    meta.update({k: spec[k] for k in ('provenance_note', 'parent_disagreement_ids') if k in spec})
    meta['timestamp_offset_ms'] = offset
    safe_metadata(meta)
    path = base / spec['path']
    raw = path.read_bytes()
    run = Run(spec['id'], episode, audio, coverage, meta,
              {'name': path.name, 'sha256': hashlib.sha256(raw).hexdigest(), 'format': spec['format']})

    def times(obj):
        offsets = obj.get('offsets', {})
        a = number(offsets.get('from'), 'offset from', True)
        b = number(offsets.get('to'), 'offset to', True)
        return (a + offset if a is not None else None,
                b + offset if b is not None else None)

    def add(text, sid, a, b, precision, speaker, confidence=None, source_word_index=None):
        if not isinstance(text, str):
            raise ValueError('Recognition text must be a string')
        confidence = number(confidence, 'confidence', True)
        if confidence is not None and not 0 <= confidence <= 1:
            raise ValueError('Confidence must be in [0, 1]')
        for m in TOKEN.finditer(text):
            run.words.append(Word(f'w{len(run.words)}', m.group(), ''.join(normalized(m.group())),
                                  sid, m.start(), m.end(), a, b,
                                  precision if a is not None and b is not None else 'unknown',
                                  speaker, confidence, source_word_index))

    if spec['format'] == 'srt':
        for index, cue in enumerate(parse_srt(path)):
            sid = f's{index}'
            a, b = cue.start + offset, cue.end + offset
            run.segments.append({'id': sid, 'source_cue': cue.idx, 'text': cue.text,
                                 'start_ms': a, 'end_ms': b, 'speaker': cue.speaker,
                                 'tokens': []})
            add(cue.text, sid, a, b, 'cue', cue.speaker)
    elif spec['format'] == 'crispasr-json':
        data = json.loads(raw)
        if not isinstance(data.get('transcription'), list):
            raise ValueError('CrispASR JSON requires a transcription array')
        # Read only public model basename, never embedded paths or arbitrary metadata.
        model = data.get('crispasr', {}).get('model')
        run.source['embedded_model_name'] = PureWindowsPath(model).name if model else None
        for index, seg in enumerate(data['transcription']):
            sid = f's{index}'
            a, b = times(seg)
            text = seg['text']
            if not isinstance(text, str):
                raise ValueError('Segment text must be a string')
            tokens = []
            for token in seg.get('tokens', []):
                ta, tb = times(token)
                p = number(token.get('p'), 'token probability', True)
                if p is not None and not 0 <= p <= 1:
                    raise ValueError('Token probability must be in [0, 1]')
                tokens.append({'text': token['text'], 'p': p, 'start_ms': ta, 'end_ms': tb})
            run.segments.append({'id': sid, 'text': text, 'start_ms': a, 'end_ms': b,
                                 'speaker': seg.get('speaker'), 'tokens': tokens})
            if seg.get('words'):
                first_word = len(run.words)
                for word_index, word in enumerate(seg['words']):
                    wa, wb = times(word)
                    add(word['text'], sid, wa, wb, 'word', word.get('speaker', seg.get('speaker')),
                        word.get('p'), word_index)
                # Never silently discard words in segment text if a detailed list disagrees.
                lexical = [w.norm for w in run.words[first_word:]]
                if lexical != normalized(text):
                    run.segments[-1]['word_text_mismatch'] = True
            else:
                add(text, sid, a, b, 'segment', seg.get('speaker'))
    else:
        raise ValueError(f"Unsupported format: {spec['format']}")
    return run


def load_manifest(path):
    data = json.loads(path.read_text(encoding='utf-8'))
    if data.get('schema_version') != 1 or not isinstance(data.get('episode'), str):
        raise ValueError('Manifest requires schema_version 1 and episode')
    audio = data['audio']
    if not isinstance(audio.get('id'), str) or not audio['id']:
        raise ValueError('Audio requires a nonempty id')
    if number(audio.get('duration_ms'), 'audio duration') <= 0:
        raise ValueError('Audio duration must be positive')
    if audio.get('sha256') is not None and not re.fullmatch(r'[0-9a-f]{64}', audio['sha256']):
        raise ValueError('Audio SHA-256 must be lowercase hexadecimal or null')
    if not isinstance(audio.get('identity_evidence'), str):
        raise ValueError('State how audio identity was established')
    safe_metadata(audio)
    runs = [load_run(s, path.parent, data['episode'], audio) for s in data['runs']]
    if len(runs) < 2 or len({r.id for r in runs}) != len(runs):
        raise ValueError('At least two uniquely named recognition runs required')
    if data['primary'] not in {r.id for r in runs}:
        raise ValueError('Primary must identify one run')
    return data, runs
