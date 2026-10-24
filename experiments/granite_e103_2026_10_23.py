"""Reproduce E103 Granite/Parakeet/Qwen measurements without ASR or source edits."""
from itertools import combinations
from pathlib import Path
import hashlib
import json
import random
import re
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from asr_backfill_2026_10_23 import distance, read, tokens
from asr_alignment import align
from build_transcripts import parse_srt


def simple_distance(a, b):
    row = list(range(len(b) + 1))
    for i, x in enumerate(a, 1):
        new = [i]
        for j, y in enumerate(b, 1):
            new.append(min(row[j] + 1, new[-1] + 1, row[j-1] + (x != y)))
        row = new
    return row[-1]


def main():
    rng = random.Random(103)
    for _ in range(200):
        a = [rng.choice('abcd') for _ in range(rng.randrange(35))]
        b = [rng.choice('abcd') for _ in range(rng.randrange(35))]
        assert distance(a, b) == simple_distance(a, b)
    paths = {name: next((ROOT / 'sources').glob('The Wastes S1E103. *.' + suffix))
             for name, suffix in [('parakeet', 'parakeet.processed.srt'),
                                  ('qwen', 'qwen-q8.canary-ctc.nemotron.srt'),
                                  ('granite', 'granite-plus-q4.canary-ctc.nemotron.srt')]}
    loaded = {k: read(p) for k, p in paths.items()}
    result: dict[str, Any] = dict(date='2026-10-23', episode='The Wastes S1E103', audio_verified=False,
                  new_asr_execution=False, model_metadata='Filename labels only; builds, settings, runtime and hardware unknown.',
                  method='Chronological cue text; strip speaker labels; lowercase; delete apostrophes; split on non-Unicode-alphanumeric characters; exact ordered unit-cost word Levenshtein. Not audio WER.',
                  distance_validation='200 seeded random sequence pairs checked against scalar dynamic programming.',
                  sources={k: v[0] for k, v in loaded.items()}, pairs={}, windows=[])
    audio = next((ROOT / 'local').glob('The Wastes S1E103. *.mp3'))
    result['available_audio'] = dict(path=audio.relative_to(ROOT).as_posix(),
                                     bytes=audio.stat().st_size,
                                     sha256=hashlib.sha256(audio.read_bytes()).hexdigest(),
                                     association='Matching archive ID/title only; export input hashes unavailable; not listened to.')
    for a, b in combinations(paths, 2):
        aa, aw, at = loaded[a]
        bb, bw, bt = loaded[b]
        edits = distance(at, bt)
        ops, stats = align(aw, bw)
        assert [w.id for _, x, _, _ in ops for w in x] == [w.id for w in aw]
        assert [w.id for _, _, x, _ in ops for w in x] == [w.id for w in bw]
        groups = []
        for kind, x, y, notes in ops:
            key = kind, bool(x), bool(y), tuple(notes)
            if groups and groups[-1][0] == key:
                groups[-1][1].extend(x)
                groups[-1][2].extend(y)
            else:
                groups.append((key, list(x), list(y)))
        candidates = []
        for (kind, _, _, notes), x, y in groups:
            if kind == 'agreement' and not notes:
                continue
            candidates.append(dict(classification=kind, diagnostics=list(notes),
                                   start_ms=min(w.start_ms for w in x+y),
                                   end_ms=max(w.end_ms for w in x+y),
                                   texts={a: ' '.join(w.text for w in x), b: ' '.join(w.text for w in y)},
                                   cue_ids={a: list(dict.fromkeys(w.segment_id for w in x)),
                                            b: list(dict.fromkeys(w.segment_id for w in y))}))
        result['pairs'][a+'_'+b] = dict(edits=edits, denominator=len(at), rate=edits/len(at),
                                       denominator_model=a, alignment_statistics=stats,
                                       candidate_groups=len(candidates))
    cues = {k: parse_srt(p) for k, p in paths.items()}
    # Sensitivity analysis only: retain the delivered export for headline metrics.
    # These patterns remove visible annotation syntax, never repetitions or speech.
    speaker_artifact = re.compile(r'Speaker\s+\d+')
    t_artifact = re.compile(r'\[?T:\s*(?:\d+\]?)?')
    def clean(text):
        return t_artifact.sub('', speaker_artifact.sub('', text))
    gc = cues['granite']
    cleaned = tokens(' '.join(clean(c.text) for c in gc))
    annotation_sensitivity: dict[str, Any] = dict(
        method='Analysis-only removal of case-sensitive Speaker N and optional-bracket T: number markers, including incomplete T: fragments. No number/URL spelling conversion or repetition removal; original sources unchanged.',
        speaker_marker_occurrences=sum(len(speaker_artifact.findall(c.text)) for c in gc),
        t_marker_occurrences=sum(len(t_artifact.findall(c.text)) for c in gc),
        t_marker_cue_ids=[c.idx for c in gc if t_artifact.search(c.text)],
        unknown_speaker_cue_ids=[c.idx for c in gc if c.speaker == 'Unknown'],
        cleaned_normalized_tokens=len(cleaned),
        pairs={k: dict(edits=distance(loaded[k][2], cleaned),
                       denominator=len(loaded[k][2]),
                       rate=distance(loaded[k][2], cleaned)/len(loaded[k][2]))
               for k in ('parakeet', 'qwen')},
        repeated_i_cues=[c.idx for c in gc if 8590000 <= c.start < 8622000
                          and clean(c.text).strip() == 'I'])
    result['annotation_sensitivity'] = annotation_sensitivity
    for start in range(0, max(v[0]['last_end_ms'] for v in loaded.values()), 600000):
        text = {k: ' '.join(c.text for c in cc if start <= c.start < start+600000)
                for k, cc in cues.items()}
        result['windows'].append(dict(start_ms=start, end_ms=start+600000,
                                       token_counts={k: len(tokens(t)) for k, t in text.items()}))
    passages = {
        'opening': {'parakeet': (0, 90000), 'qwen': (0, 90000), 'granite': (0, 90000)},
        'room_entry': {'parakeet': (215000, 305000), 'qwen': (215000, 305000), 'granite': (215000, 305000)},
        'guardian_expiry': {'parakeet': (3030000, 3076000), 'qwen': (3030000, 3076000), 'granite': (3030000, 3076000)},
        'nonlethal_intent': {'parakeet': (5790000, 5840000), 'qwen': (5790000, 5840000), 'granite': (5790000, 5840000)},
        'timing_anchor': {'parakeet': (6030000, 6050000), 'qwen': (6030000, 6050000), 'granite': (6030000, 6050000)},
        'weather': {'parakeet': (6690000, 6755000), 'qwen': (6690000, 6755000), 'granite': (6690000, 6755000)},
        'ending': {'parakeet': (9660000, 9856000), 'qwen': (9660000, 9856000), 'granite': (9660000, 9856000)},
    }
    for label, span in {'two_weapons': (3330000, 3380000),
                        'grapple': (5030000, 5090000),
                        'sacred_flame_artifacts': (4450000, 4495000),
                        'repetition': (8580000, 8640000),
                        'alternative_reactions': (5980000, 6020000)}.items():
        passages[label] = {k: span for k in paths}
    result['selected_passages'] = {
        label: {k: [dict(cue_id=c.idx, start_ms=c.start, end_ms=c.end,
                        speaker=c.speaker, text=c.text) for c in cues[k] if start <= c.start < end]
                for k, (start, end) in spans.items()}
        for label, spans in passages.items()}
    for k, p in paths.items():
        assert hashlib.sha256(p.read_bytes()).hexdigest() == loaded[k][0]['sha256']
    target = ROOT / 'reports/GRANITE_E103_METRICS_2026-10-23.json'
    target.write_text(json.dumps(result, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    print(json.dumps(dict(sources={k: dict(cues=v['cues'], tokens=v['normalized_tokens'])
                                    for k, v in result['sources'].items()},
                          pairs=result['pairs'],
                          sensitivity={k: v for k, v in result['annotation_sensitivity'].items()
                                       if not isinstance(v, list)},
                          repeated_i_cues=len(result['annotation_sensitivity']['repeated_i_cues'])), indent=2))


if __name__ == '__main__':
    main()
