"""Reproduce E002–E005 export comparisons without ASR execution or source edits.

Run from the repository root: python experiments/asr_backfill_2026_10_23.py
Only the dated JSON evidence is regenerated; editorial reports stay separate.
"""
from collections import Counter
from pathlib import Path
import hashlib
import json
import re
import sys
from typing import Any
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from asr_alignment import align
from asr_evidence import TOKEN, Word, normalized
from asr_metrics import distance, tokens
from audit_sources import audit_srt
from build_transcripts import parse_srt

EPISODES = ('E002', 'E003', 'E004', 'E005')


def coverage_register():
    """Inventory dossiers, dedicated reports and explicitly scoped prior work."""
    previous = {
        'E000': ('MULTIPASS_PILOT_2026-10-21.md', 'Full raw-export pilot; processed-pair report absent'),
        'E001': ('MULTIPASS_PILOT_2026-10-21.md', 'Full raw-export pilot plus targeted work; processed-pair report absent'),
        'E039': ('QWEN_CANARY_INTAKE_2026-10-22.md', 'Full-export intake; dedicated report absent'),
        'BONUS-2019-03': ('QWEN_CANARY_INTAKE_2026-10-22.md', 'Full-export intake; dedicated report absent'),
        'BONUS-2019-04': ('QWEN_CANARY_INTAKE_2026-10-22.md', 'Full-export intake; dedicated report absent'),
    }
    rows, counts = [], Counter()
    dossiers = sorted((ROOT / 'episodes').glob('*.md')) + sorted((ROOT / 'inverse/episodes').glob('*.md'))
    for dossier in dossiers:
        key = dossier.stem
        inverse = dossier.parent.parent.name == 'inverse'
        if inverse:
            match = re.fullmatch(r'S(\d+)E(\d+)', key)
            if match is None:
                raise ValueError(f'Invalid Inverse episode ID: {key}')
            season, episode = match.groups()
            prefix = f'Inverse S{int(season)}E{int(episode)}. '
            report_key = 'INVERSE_' + key
            identity = 'Inverse ' + key
        else:
            prefix = ('Bonus ' + key[6:] + ' - ' if key.startswith('BONUS-') else
                      'The Wastes S1' + key + (' ' if key == 'E013.5' else '. '))
            report_key = key.replace('-', '_')
            identity = key if key.startswith('BONUS-') else 'Wastes S1' + key
        a = sorted((ROOT / 'sources').glob(prefix + '*.parakeet.processed.srt'))
        b = sorted((ROOT / 'sources').glob(prefix + '*.qwen-q8.canary-ctc.nemotron.srt'))
        # Alternate-copy exports are listed as such, never treated as additional episodes.
        sources = f'{len(a)} Parakeet / {len(b)} Qwen'
        reports = sorted((ROOT / 'reports').glob(report_key + '_ASR_COMPARISON_*.md'))
        if reports:
            status = 'Dedicated report'
            evidence = ' · '.join(f'[{p.stem.rsplit("_", 1)[-1]}]({quote(p.name)})' for p in reports)
        elif key in previous and not inverse:
            status = 'Prior comparison'
            report, note = previous[key]
            evidence = f'[{note}]({report})'
        elif a and b:
            status, evidence = 'Ready', 'Existing exports; comparison pending'
        else:
            status, evidence = 'Needs export', 'Independent Qwen export unavailable in sources/'
        counts[status] += 1
        link = '../' + dossier.relative_to(ROOT).as_posix()
        rows.append(f'| [{identity}]({link}) | {sources} | {status} | {evidence} |')
    text = '# ASR comparison coverage — analyzed episodes (2026-10-23)\n\n'
    text += ('Inventory of all **119 existing dossiers** in `episodes/` and `inverse/episodes/`; '
             'source availability is limited to the repository `sources/` directory. '
             'Unanalyzed recordings are outside this backlog. Each row represents one corrected '
             'archive identity; alternate copies are not independent episodes.\n\n')
    text += (f"**{counts['Dedicated report']} dedicated reports**; "
             f"**{counts['Prior comparison']} prior comparisons**; "
             f"**{counts['Ready']} ready pairs**; "
             f"**{counts['Needs export']} recordings need another export**.\n\n")
    text += ('A dedicated report is a documentation-coverage status, not an audit of its methodology '
             'or proof of audio verification. Earlier raw-export pilots and the three-export intake '
             'are kept visible rather than misclassified as never compared. Pair availability '
             'does not verify common audio hashes or recording offsets. The supplemental E013.5 '
             'and December 2019 bonus each have alternate-copy pairs requiring separate handling.\n\n'
             'This pass adds **Wastes S1E002–E005**. Continue with **Wastes S1E006**, then '
             'chronological ready entries; keep Inverse, bonuses and the E043 standalone adventure '
             'within their own continuity/type. E076–E083 require an independent export before '
             'a two-ASR comparison can be computed. No missing export was generated in this pass.\n\n'
             '[Reproduction script](../experiments/asr_backfill_2026_10_23.py) · '
             '[E002–E005 metrics and complete candidate evidence](ASR_BACKFILL_2026-10-23.json) · '
             '[Review queue](../project/REVIEW_QUEUE.md).\n\n'
             '| Analyzed recording | Available processed-pair exports | Comparison status | Report / next action |\n'
             '| --- | --- | --- | --- |\n')
    (ROOT / 'reports/ASR_COMPARISON_COVERAGE_2026-10-23.md').write_text(
        text + '\n'.join(rows) + '\n', encoding='utf-8')
    print('Coverage:', dict(counts), flush=True)


def read(path):
    cues = parse_srt(path)
    if cues != sorted(cues, key=lambda c: c.start):
        raise ValueError(f'Nonchronological cues: {path.name}')
    words = []
    for cue in cues:
        for match in TOKEN.finditer(cue.text):
            words.append(Word(f'w{len(words)}', match.group(), normalized(match.group())[0],
                              str(cue.idx), match.start(), match.end(), cue.start, cue.end,
                              'cue', cue.speaker))
    stats = audit_srt(path)
    lexical = tokens(' '.join(c.text for c in cues))
    stats.update(path=path.relative_to(ROOT).as_posix(), normalized_tokens=len(lexical),
                 first_start_ms=cues[0].start, last_end_ms=max(c.end for c in cues),
                 opening_text=' '.join(c.text for c in cues[:5]),
                 closing_text=' '.join(c.text for c in cues[-5:]))
    return stats, words, lexical


def compare_episode(episode):
    primary, = (ROOT / 'sources').glob(f'The Wastes S1{episode}. *.parakeet.processed.srt')
    alternative = primary.with_name(primary.name.replace('.parakeet.processed.srt',
                                                         '.qwen-q8.canary-ctc.nemotron.srt'))
    a, aw, at = read(primary)
    b, bw, bt = read(alternative)
    edits = distance(at, bt)
    operations, statistics = align(aw, bw)
    assert [w.id for _, aa, _, _ in operations for w in aa] == [w.id for w in aw]
    assert [w.id for _, _, bb, _ in operations for w in bb] == [w.id for w in bw]
    groups = []
    for kind, aa, bb, notes in operations:
        key = kind, bool(aa), bool(bb), tuple(notes)
        if groups and groups[-1][0] == key:
            groups[-1][1].extend(aa)
            groups[-1][2].extend(bb)
        else:
            groups.append((key, list(aa), list(bb)))
    candidates = []
    for (kind, _, _, notes), aa, bb in groups:
        if kind == 'agreement' and not notes:
            continue
        candidates.append(dict(classification=kind, diagnostics=list(notes),
                               start_ms=min(w.start_ms for w in aa + bb),
                               end_ms=max(w.end_ms for w in aa + bb),
                               parakeet=' '.join(w.text for w in aa),
                               qwen=' '.join(w.text for w in bb),
                               parakeet_cue_ids=list(dict.fromkeys(w.segment_id for w in aa)),
                               qwen_cue_ids=list(dict.fromkeys(w.segment_id for w in bb))))
    for path, stats in ((primary, a), (alternative, b)):
        assert hashlib.sha256(path.read_bytes()).hexdigest() == stats['sha256']
    return dict(episode=episode, parakeet=a, qwen=b, edits=edits,
                denominator=a['normalized_tokens'], disagreement_rate=edits / len(at),
                alignment_statistics=statistics, candidate_groups=len(candidates),
                classifications=dict(Counter(c['classification'] for c in candidates)),
                candidates=candidates)


def main():
    result: dict[str, Any] = dict(date='2026-10-23', audio_verified=False, new_asr_execution=False,
                  scope=list(EPISODES), access='Direct local checkout; portable paths and SHA-256 below.',
                  pairing='Corrected archive ID, title and corresponding introductory text; original '
                          'audio identity and recording-clock equivalence remain unverified.',
                  method='Parse every SRT cue through the final cue; remove leading speaker decoration, '
                         'join text, lowercase, delete straight/curly apostrophes, replace everything '
                         'except Unicode letters/digits with spaces. Exact ordered unit-cost word '
                         'Levenshtein / processed Parakeet token count. Not audio-grounded WER.',
                  candidate_method='Separate existing time-aware alignment: 2000 ms drift, 192-token '
                                   'cap, 30000 ms fallback. Cue intervals, never synthetic word times. '
                                   'Alignment lexical normalization retains apostrophes and uses NFKC; '
                                   'candidate counts are not the global distance.',
                  configuration='Pipeline labels inferred from filenames only; build, settings, '
                                'runtime, audio hashes and hardware not established.', episodes=[])
    for episode in EPISODES:
        item = compare_episode(episode)
        result['episodes'].append(item)
        print(episode, item['edits'], item['denominator'],
              f"{item['disagreement_rate']:.2%}", item['candidate_groups'], flush=True)
    target = ROOT / 'reports' / 'ASR_BACKFILL_2026-10-23.json'
    target.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    coverage_register()


if __name__ == '__main__':
    main()
