"""Reproduce the bounded three-export intake; no audio or transcript edits.

Run from the repository root: python experiments/qwen_canary_intake_2026_10_22.py
Uses the existing dependency-free parser and time-aware alignment.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from asr_alignment import align
from asr_evidence import TOKEN, Word, normalized
from audit_sources import audit_srt
from build_transcripts import clock, parse_srt

PAIRS = [
    ('BONUS-2019-03', 'Bonus 2019-03 - March 2019 The Year One Q&A!',
     'Bonus 2019-03 - March 2019 The Year One Q&A!'),
    ('BONUS-2019-04', 'Bonus 2019-04 - April 2019',
     'Bonus 2019-04 - Bonus Show 01 - The First and Last (April 2019 )'),
    ('E039', 'The Wastes S1E039. Taking up arms', 'The Wastes S1E039. Taking up arms'),
]
SUFFIX = '.qwen-q8.canary-ctc.nemotron.srt'
STEM = 'QWEN_CANARY_INTAKE_2026-10-22'


def read(path):
    cues = parse_srt(path)
    words = []
    for c in cues:
        for m in TOKEN.finditer(c.text):
            words.append(Word(f'w{len(words)}', m.group(), normalized(m.group())[0],
                              str(c.idx), m.start(), m.end(), c.start, c.end, 'cue', c.speaker))
    stat = audit_srt(path)
    stat['normalized_words'] = len(words)
    stat['speaker_cue_counts'] = dict(Counter(c.speaker for c in cues))
    stat['opening_text'] = ' '.join(c.text for c in cues[:5])
    stat['closing_text'] = ' '.join(c.text for c in cues[-5:])
    return stat, words


def main():
    result = {'date': '2026-10-22', 'audio_verified': False,
              'scope': 'Only the three explicit source pairs in the reproduction script.',
              'configuration_evidence': 'Owner reports Qwen Q8 + Canary CTC + Nemotron; filenames agree. '
              'Model/build versions, VAD, chunking, decoding, post-processing and runtime unconfirmed.',
              'method': 'Unicode lexical tokens excluding leading speaker labels; existing time-aware '
              'alignment with 2000 ms drift, 192-token cap, 30000 ms fallback buckets. '
              'Cue intervals are not word timestamps. Parakeet sources are processed, so differences '
              'can include recognition and processing. No same-episode Q8 without Canary is available '
              'for these pairs; aligner text preservation cannot be isolated.', 'episodes': []}
    rows = []
    sections = []
    for episode, new_stem, old_stem in PAIRS:
        paths = [ROOT / 'sources' / (old_stem + '.parakeet.processed.srt'),
                 ROOT / 'sources' / (new_stem + SUFFIX)]
        snapshots = [hashlib.sha256(p.read_bytes()).hexdigest() for p in paths]
        (a, aw), (b, bw) = [read(p) for p in paths]
        ops, stats = align(aw, bw)
        assert [w.id for _, aa, _, _ in ops for w in aa] == [w.id for w in aw]
        assert [w.id for _, _, bb, _ in ops for w in bb] == [w.id for w in bw]
        groups = []
        for kind, aa, bb, notes in ops:
            key = (kind, bool(aa), bool(bb), tuple(notes))
            if groups and groups[-1][0] == key:
                groups[-1][1].extend(aa)
                groups[-1][2].extend(bb)
            else:
                groups.append((key, list(aa), list(bb)))
        candidates = []
        for (kind, _, _, notes), aa, bb in groups:
            if kind == 'agreement' and not notes:
                continue
            ws = aa + bb
            candidates.append({'classification': kind, 'notes': list(notes),
                               'start_ms': min(w.start_ms for w in ws),
                               'end_ms': max(w.end_ms for w in ws),
                               'parakeet': ' '.join(w.text for w in aa),
                               'qwen': ' '.join(w.text for w in bb),
                               'parakeet_cue_ids': list(dict.fromkeys(w.segment_id for w in aa)),
                               'qwen_cue_ids': list(dict.fromkeys(w.segment_id for w in bb))})
        item = {'episode': episode, 'pairing_evidence': 'Filename/title and corresponding opening '
                'text; original audio hashes and full recording equivalence not verified.',
                'parakeet': a, 'qwen': b, 'alignment_stats': stats,
                'candidate_groups': len(candidates),
                'classifications': dict(Counter(c['classification'] for c in candidates)),
                'candidates': candidates}
        result['episodes'].append(item)
        for label, s in [('Parakeet processed', a), ('Qwen Q8 + Canary + Nemotron', b)]:
            rows.append(f"| {episode} | {label} | {s['cues']:,} | {s['normalized_words']:,} | "
                        f"{s['nonpositive_duration_cues']} | {s['overlap_pairs']} | {s['last_cue_end']} |")
        examples = []
        for side in ['qwen', 'parakeet']:
            other = 'parakeet' if side == 'qwen' else 'qwen'
            unilateral = [c for c in candidates if c[side] and not c[other]]
            examples.extend(sorted(unilateral, key=lambda c: len(c[side].split()), reverse=True)[:2])
        sections.append(f"\n## {episode}\n\n{len(candidates):,} candidate groups; "
                        f"{stats['fallback_blocks']} bounded fallback blocks. These are review hypotheses.\n")
        for c in examples:
            sections.append(f"\n- **{clock(c['start_ms'])}–{clock(c['end_ms'])}**: "
                            f"Parakeet: `{c['parakeet'] or '(no aligned words)'}`; "
                            f"Qwen: `{c['qwen'] or '(no aligned words)'}`.\n")
        assert snapshots == [hashlib.sha256(p.read_bytes()).hexdigest() for p in paths]
    out = ROOT / 'reports'
    (out / (STEM + '.json')).write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    md = '# Qwen Q8 + Canary CTC + Nemotron: first intake — 2026-10-22\n\n'
    md += '**Status:** Export structure and model disagreement only; no listening, audio-grounded '
    md += 'accuracy measurement, new ASR execution, or canonical transcript edits.\n\n'
    md += result['configuration_evidence'] + '\n\n' + result['method'] + '\n\n'
    md += 'The two alphabetical bonus exports and the additional E039 export were present at intake. '
    md += 'April has different source basenames; its opening introduction corresponds in both exports. '
    md += 'Pairing is provisional from filenames/content, not verified audio identity.\n\n'
    md += '| Recording | Source | Cues | Normalized words | Nonpositive durations | Adjacent overlaps | Last cue end |\n'
    md += '|---|---|---:|---:|---:|---:|---|\n' + '\n'.join(rows) + '\n'
    md += ''.join(sections)
    md += '\n## Reproduction and interpretation\n\n'
    md += '`python experiments/qwen_canary_intake_2026_10_22.py` regenerates this report and the '
    md += '[JSON](QWEN_CANARY_INTAKE_2026-10-22.json), including every candidate, cue references and source SHA-256. '
    md += 'Both sides retain every lexical token through alignment; all six source hashes were unchanged after analysis. '
    md += 'Neither word counts nor candidate counts measure accuracy. Speaker IDs are local to each run. '
    md += 'Overlaps can be simultaneous speech; valid cues do not establish accurate alignment.\n\n'
    md += 'Listen to the examples above, plus randomly selected agreed passages, before accepting wording. '
    md += 'Check introductions and endings against audio for dropped speech or music hallucinations. '
    md += 'Obtain exact settings/runtime before treating these as a reproducible production configuration. '
    md += 'A same-audio Q8 export without Canary is still needed to isolate alignment effects.\n'
    (out / (STEM + '.md')).write_text(md, encoding='utf-8')
    for item in result['episodes']:
        print(item['episode'], json.dumps({k: item[k] for k in ['alignment_stats', 'candidate_groups', 'classifications']}))
        for label in ['parakeet', 'qwen']:
            print(label, json.dumps({k: item[label][k] for k in ['cues', 'normalized_words', 'nonpositive_duration_cues', 'overlap_pairs', 'last_cue_end']}))


if __name__ == '__main__':
    main()
