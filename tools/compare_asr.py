#!/usr/bin/env python3
"""Compare exported recognition evidence; never rewrite a published transcript."""
from __future__ import annotations

import argparse
from bisect import bisect_left, bisect_right
from collections import Counter
from itertools import combinations
import json
from pathlib import Path
import time

from asr_alignment import align, bounds
from asr_evidence import digest, interval, load_manifest, number

SCHEMA = 1


def write_json(path, data):
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False, allow_nan=False) + '\n',
                    encoding='utf-8', newline='\n')


def selected(run, start, end):
    # Unknown timing remains evidence and is never dropped as out of scope.
    return [w for w in run.words if w.start_ms is None or w.end_ms is None
            or max(w.start_ms, w.end_ms) >= start and min(w.start_ms, w.end_ms) < end]


def source_entry(run, words, role='aligned'):
    return {'run_id': run.id, 'role': role, 'word_ids': [w.id for w in words],
            'lexical_text': ' '.join(w.text for w in words),
            'segment_ids': list(dict.fromkeys(w.segment_id for w in words)),
            'timing_precision': sorted({w.timing for w in words}),
            'speaker_labels': list(dict.fromkeys(w.speaker for w in words)),
            'word_confidences': [w.confidence for w in words]}


def candidate(episode, participants, kind, evidence, scope=None):
    words = [w for _, ws in participants for w in ws]
    start, end = bounds(words)
    if scope is not None and start is not None and end is not None:
        start, end = max(start, scope[0]), min(end, scope[1])
        if end < start:
            start, end = scope
    sources = [source_entry(r, ws) for r, ws in participants]
    identity = {'episode': episode, 'audio': participants[0][0].audio, 'kind': kind, 'scope': scope,
                'evidence': evidence,
                'sources': [{'run': r.id, 'metadata': r.metadata,
                             'words': [(w.id, w.text, w.start_ms, w.end_ms, w.timing) for w in ws]}
                            for r, ws in participants]}
    return {'id': 'd-' + digest(identity)[:20], 'episode': episode,
            'start_ms': start, 'end_ms': end, 'classification': kind,
            'diagnostics': evidence, 'sources': sources,
            'priority': 'high' if kind in ('possible_omission', 'possible_hallucination', 'boundary_anomaly') else 'medium',
            'status': 'unreviewed', 'audio_verified': False}


def anomalies(run):
    findings = []
    seen_segments = set()
    previous = None
    for w in run.words:
        if w.timing in ('cue', 'segment'):
            if w.segment_id in seen_segments:
                continue
            seen_segments.add(w.segment_id)
        notes = []
        kind = 'boundary_anomaly'
        if w.start_ms is None or w.end_ms is None:
            notes.append('Missing timing; no word timestamps inferred')
            kind = 'uncertain_segmentation'
        else:
            if w.end_ms <= w.start_ms:
                notes.append('Inverted or zero duration; source values preserved')
            if min(w.start_ms, w.end_ms) < run.coverage_ms[0] or max(w.start_ms, w.end_ms) > run.coverage_ms[1]:
                notes.append('Timestamp outside declared run coverage')
            if previous and previous.end_ms is not None and w.start_ms < previous.end_ms:
                notes.append('Overlap or backward timestamp; simultaneous speech is possible')
                if (w.timing == previous.timing == 'word' and w.norm == previous.norm
                        and w.speaker == previous.speaker
                        and abs(w.start_ms - previous.start_ms) <= 40
                        and abs(w.end_ms - previous.end_ms) <= 40):
                    notes.append('Near-identical repeated word intervals: possible boundary duplicate, not deleted')
        if notes:
            ws = [previous, w] if previous and any('Overlap' in n for n in notes) else [w]
            findings.append(candidate(run.episode, [(run, ws)], kind, notes))
        previous = w
    for seg in run.segments:
        if seg.get('word_text_mismatch'):
            findings.append(candidate(run.episode, [(run, [w for w in run.words if w.segment_id == seg['id']])],
                                      'uncertain_segmentation',
                                      ['Detailed words disagree with segment text; both preserved', seg['id']]))
    return findings


def compare(runs, primary, drift_ms=2000, max_tokens=192, window_ms=30000, comparison_coverage_ms=None):
    if len({r.episode for r in runs}) != 1 or len({digest(r.audio) for r in runs}) != 1:
        raise ValueError('All runs must refer to the same episode and audio identity')
    records, pairs = [], []
    if comparison_coverage_ms is not None:
        interval(comparison_coverage_ms, 'comparison_coverage_ms')
        if comparison_coverage_ms[1] > runs[0].audio['duration_ms']:
            raise ValueError('Comparison coverage exceeds audio duration')
    for run in runs:
        for rec in anomalies(run):
            scope = comparison_coverage_ms
            in_scope = scope is None or rec['start_ms'] is None
            if not in_scope and scope is not None:
                in_scope = (rec['end_ms'] >= scope[0] and rec['start_ms'] <= scope[1]
                            or scope[0] <= run.coverage_ms[1] <= scope[1] and rec['end_ms'] > run.coverage_ms[1]
                            or scope[0] <= run.coverage_ms[0] <= scope[1] and rec['start_ms'] < run.coverage_ms[0])
            if in_scope:
                records.append(rec)
    for a, b in combinations(runs, 2):
        start = max(a.coverage_ms[0], b.coverage_ms[0])
        end = min(a.coverage_ms[1], b.coverage_ms[1])
        if comparison_coverage_ms is not None:
            start = max(start, comparison_coverage_ms[0])
            end = min(end, comparison_coverage_ms[1])
        if start >= end:
            pairs.append({'runs': [a.id, b.id], 'coverage_ms': None, 'note': 'No common coverage; not compared'})
            continue
        aw, bw = selected(a, start, end), selected(b, start, end)
        ops, stats = align(aw, bw, drift_ms, max_tokens, window_ms)
        groups = []
        for kind, aa, bb, notes in ops:
            notes = list(notes)
            if any(w.timing == 'unknown' for w in aa + bb):
                notes.append('Unknown timing: textual alignment only')
            if any(w.start_ms is not None and w.end_ms is not None and
                   (w.start_ms < start or w.end_ms > end) for w in aa + bb):
                notes.append('Source interval crosses comparison coverage boundary; wording not clipped')
            if kind == 'agreement' and notes:
                kind = 'uncertain_segmentation'
            key = (kind, bool(aa), bool(bb), tuple(notes))
            if groups and groups[-1][0] == key:
                groups[-1][1].extend(aa)
                groups[-1][2].extend(bb)
            else:
                groups.append((key, list(aa), list(bb)))
        agreements = []
        for (kind, _, _, notes), aa, bb in groups:
            if kind == 'agreement':
                agreements.append({'a_word_ids': [w.id for w in aa], 'b_word_ids': [w.id for w in bb]})
                continue
            evidence = list(notes)
            if kind == 'possible_omission':
                missing = b.id if aa else a.id
                evidence.append(f'Speech appears in one pass only; possible omission in {missing} or insertion in the other pass')
            elif kind == 'uncertain_segmentation':
                evidence.append('Concatenation-equivalent words or uncertain alignment boundaries; retain both forms')
            if any(w.timing in ('cue', 'segment') for w in aa + bb):
                evidence.append('Interval includes coarse cue/segment timing, not measured word timing')
            record = candidate(a.episode, [(a, aa), (b, bb)], kind, evidence, [start, end])
            records.append(record)
            if kind == 'possible_omission':
                # A separate suspicion needs more than disagreement or minority count.
                present_run, present = (a, aa) if aa else (b, bb)
                lo, hi = bounds(present)
                probs = [w.confidence for w in present if w.confidence is not None]
                if lo is not None:
                    segs = {w.segment_id for w in present}
                    probs += [t['p'] for s in present_run.segments if s['id'] in segs for t in s['tokens']
                              if t['p'] is not None and t['start_ms'] is not None and t['end_ms'] is not None
                              and t['start_ms'] < hi and t['end_ms'] > lo]
                if probs and sum(probs) / len(probs) < .5:
                    records.append(candidate(a.episode, [(a, aa), (b, bb)], 'possible_hallucination',
                                             ['Unilateral text with mean available probability below 0.5; uncalibrated heuristic',
                                              f'Related omission candidate: {record["id"]}'], [start, end]))
        pairs.append({'runs': [a.id, b.id], 'coverage_ms': [start, end],
                      'word_counts': [len(aw), len(bw)], 'statistics': stats,
                      'agreement_word_pairs': sum(len(x['a_word_ids']) for x in agreements),
                      'agreements': agreements})
    # Extra passes are contextual evidence, not votes. Index once per run.
    indexes = {}
    for run in runs:
        timed = sorted((w for w in run.words if w.start_ms is not None), key=lambda w: w.start_ms)
        indexes[run.id] = (timed, [w.start_ms for w in timed],
                           max((abs(w.end_ms-w.start_ms) for w in timed if w.end_ms is not None), default=0))
    for record in records:
        covered = {s['run_id'] for s in record['sources']}
        lo, hi = record['start_ms'], record['end_ms']
        for run in runs:
            if run.id in covered:
                continue
            timed, starts, width = indexes[run.id]
            ws = [] if lo is None else [w for w in timed[bisect_left(starts, lo-width):bisect_right(starts, hi)]
                                       if w.end_ms is not None and max(w.start_ms, w.end_ms) >= lo]
            role = 'context_only' if lo is not None and lo < run.coverage_ms[1] and hi >= run.coverage_ms[0] else 'not_covered_or_untimed'
            record['sources'].append(source_entry(run, ws, role))
    records.sort(key=lambda r: (r['start_ms'] is None, r['start_ms'] or 0, r['id']))
    return {'schema_version': SCHEMA, 'episode': runs[0].episode, 'audio': runs[0].audio,
            'primary': primary, 'status': 'experimental-unverified',
            'algorithm': {'version': 1, 'drift_ms': drift_ms, 'max_tokens': max_tokens, 'window_ms': window_ms,
                          'comparison_coverage_ms': comparison_coverage_ms},
            'runs': [r.export() for r in runs], 'pairs': pairs, 'disagreements': records,
            'counts': dict(Counter(r['classification'] for r in records))}


def reconcile(report, ledger=None):
    ledger = ledger or {'schema_version': 1, 'decisions': []}
    if ledger.get('schema_version') != 1 or not isinstance(ledger.get('decisions'), list):
        raise ValueError('Invalid decision ledger')
    known = {r['id']: r for r in report['disagreements']}
    decisions, seen = [], set()
    for entry in ledger['decisions']:
        key = entry['disagreement_id']
        if key not in known or key in seen:
            raise ValueError('Unknown or duplicate disagreement decision; never silently migrate annotations')
        seen.add(key)
        if entry.get('action') not in ('accept', 'reject', 'defer'):
            raise ValueError('Decision action must be accept, reject, or defer')
        if not all(isinstance(entry.get(k), str) and entry[k].strip() for k in ('reviewer', 'date', 'evidence')):
            raise ValueError('Decision requires reviewer, date, and evidence')
        if type(entry.get('audio_verified')) is not bool:
            raise ValueError('audio_verified must be explicit boolean')
        if entry['audio_verified'] and not entry.get('audio_evidence'):
            raise ValueError('Audio verification requires audio_evidence')
        if entry['action'] != 'defer' and entry.get('candidate_run_id') not in {
                s['run_id'] for s in known[key]['sources'] if s['role'] == 'aligned'}:
            raise ValueError('Accepted/rejected candidate must be an aligned source run')
        decisions.append(dict(entry))
        known[key]['status'] = entry['action']
        known[key]['audio_verified'] = entry['audio_verified']
        known[key]['review_decision'] = dict(entry)
    primary = next(r for r in report['runs'] if r['id'] == report['primary'])
    return {'schema_version': SCHEMA, 'episode': report['episode'], 'primary': primary['id'],
            'primary_source_sha256': primary['source']['sha256'],
            'base_segments': primary['segments'], 'base_word_ids': [w['id'] for w in primary['words']],
            'alternatives': report['disagreements'], 'decisions': decisions,
            'publication_ready': False, 'automatic_text_changes': [],
            'note': 'Accepted choices are review overlays only; no speech inserted, removed, or published.'}


def make_jobs(report, before_ms=2000, after_ms=2000, merge_gap_ms=1000, max_job_ms=120000,
              suggestion=None):
    for name, value in [('before_ms', before_ms), ('after_ms', after_ms), ('merge_gap_ms', merge_gap_ms)]:
        if number(value, name) < 0:
            raise ValueError('Padding and merge gap must be nonnegative')
    if number(max_job_ms, 'max_job_ms') <= 0:
        raise ValueError('max_job_ms must be positive')
    duration = report['audio']['duration_ms']
    spans, unlocated = [], []
    for rec in report['disagreements']:
        if rec['status'] in ('accept', 'reject') and rec['audio_verified']:
            continue
        if rec['start_ms'] is None or rec['end_ms'] is None:
            unlocated.append(rec['id'])
            continue
        lo = max(0, min(duration, rec['start_ms'] - before_ms))
        hi = max(0, min(duration, rec['end_ms'] + after_ms))
        if hi <= lo:
            unlocated.append(rec['id'])
            continue
        # Split pathological/very long uncertain regions instead of launching a whole episode.
        while lo < hi:
            edge = min(hi, lo + max_job_ms)
            spans.append((lo, edge, rec['id'], rec['classification']))
            lo = edge
    merged = []
    for lo, hi, key, reason in sorted(spans):
        if merged and lo <= merged[-1]['end_ms'] + merge_gap_ms and max(hi, merged[-1]['end_ms']) - merged[-1]['start_ms'] <= max_job_ms:
            job = merged[-1]
            job['end_ms'] = max(job['end_ms'], hi)
            job['disagreement_ids'] = sorted(set(job['disagreement_ids'] + [key]))
            job['reasons'] = sorted(set(job['reasons'] + [reason]))
        else:
            merged.append({'start_ms': lo, 'end_ms': hi, 'disagreement_ids': [key], 'reasons': [reason]})
    for job in merged:
        job.update({'episode': report['episode'], 'audio': report['audio'],
                    'context_before_ms': before_ms, 'context_after_ms': after_ms,
                    'suggested_configuration': suggestion or {'model': 'Qwen3-ASR 1.7B', 'quantization': 'Q8',
                                                               'settings': {'purpose': 'independent targeted evidence'}},
                    'status': 'pending', 'timestamp_origin': 'episode'})
        job['id'] = 'j-' + digest(job)[:20]
    return {'schema_version': SCHEMA, 'jobs': merged, 'unlocated_disagreement_ids': unlocated,
            'note': 'Jobs are proposals. Split or clamped jobs may have less context; review before execution.'}


def stamp(ms):
    if ms is None:
        return 'unknown'
    seconds = ms / 1000
    return f'{int(seconds//3600):02}:{int(seconds%3600//60):02}:{seconds%60:06.3f}'


def markdown(report):
    lines = [f'# {report["episode"]} ASR comparison', '',
             'Experimental review candidates, not verified omissions or accuracy scores.', '',
             'SRT words carry whole cue intervals. Speaker labels are local to each run. '
             'Original segments, word timing and token probabilities are in comparison.json.', '',
             f'Primary: `{report["primary"]}`. Classifications: `{report["counts"]}`.', '']
    for run in report['runs']:
        lines.append(f'- `{run["id"]}`: {run["metadata"]["model"]}; coverage {run["coverage_ms"]} ms; '
                     f'source `{run["source"]["name"]}`, SHA-256 `{run["source"]["sha256"]}`.')
    for rec in report['disagreements']:
        lines += ['', f'## {rec["id"]} — {stamp(rec["start_ms"])}–{stamp(rec["end_ms"])}', '',
                  f'{rec["classification"]}; priority {rec["priority"]}; status {rec["status"]}; '
                  f'audio verified: {rec["audio_verified"]}.', '',
                  'Diagnostics: ' + '; '.join(rec['diagnostics']), '']
        for src in rec['sources']:
            # Escape Markdown metacharacters in transcript evidence.
            text = src['lexical_text'].replace('\\', '\\\\')
            for char in '*_[]<>`':
                text = text.replace(char, '\\' + char)
            lines.append(f'- {src["run_id"]} ({src["role"]}; {", ".join(src["timing_precision"]) or "no words"}): {text or "[no corresponding words]"}')
    return '\n'.join(lines) + '\n'


def validate_report(report):
    if report.get('schema_version') != 1:
        raise ValueError('Unsupported report schema')
    ids = [r['id'] for r in report['disagreements']]
    if len(set(ids)) != len(ids):
        raise ValueError('Duplicate candidate identifiers')
    runs = {r['id']: r for r in report['runs']}
    words = {key: {w['id'] for w in run['words']} for key, run in runs.items()}
    if report['primary'] not in runs:
        raise ValueError('Unknown primary')
    categories = {'possible_omission', 'conflicting_recognition', 'possible_hallucination',
                  'boundary_anomaly', 'uncertain_segmentation'}
    for run in runs.values():
        interval(run['coverage_ms'], 'run coverage')
        if len(words[run['id']]) != len(run['words']):
            raise ValueError('Duplicate source word identifiers')
        segments = {s['id'] for s in run['segments']}
        for word in run['words']:
            for key in ('start_ms', 'end_ms'):
                number(word[key], key, True)
            if word['timing'] not in ('word', 'cue', 'segment', 'unknown'):
                raise ValueError('Unknown timing precision')
            if word['segment_id'] not in segments:
                raise ValueError('Broken segment reference')
    for rec in report['disagreements']:
        if (rec['classification'] not in categories or rec['status'] not in ('unreviewed', 'accept', 'reject', 'defer')
                or type(rec['audio_verified']) is not bool):
            raise ValueError('Invalid classification or review status')
        if rec['audio_verified'] and not rec.get('review_decision', {}).get('audio_evidence'):
            raise ValueError('Audio-verified records require reviewer evidence')
        for key in ('start_ms', 'end_ms'):
            number(rec[key], key, True)
        for src in rec['sources']:
            if src['run_id'] not in words or not set(src['word_ids']) <= words[src['run_id']]:
                raise ValueError('Broken source references')
    for pair in report['pairs']:
        if pair['coverage_ms'] is not None:
            interval(pair['coverage_ms'], 'pair coverage')
    # Also rejects NaN in arbitrary metadata/evidence on serialization.
    json.dumps(report, allow_nan=False)


def run_comparison(manifest, out, decisions=None, **options):
    started = time.perf_counter()
    data, runs = load_manifest(manifest)
    report = compare(runs, data['primary'], comparison_coverage_ms=data.get('comparison_coverage_ms'), **options)
    provisional = reconcile(report, decisions)
    jobs = make_jobs(report, **data.get('job_options', {}))
    validate_report(report)
    # New directories only: never overwrite evidence or existing review edits.
    out.mkdir(parents=True, exist_ok=False)
    write_json(out/'comparison.json', report)
    (out/'comparison.md').write_text(markdown(report), encoding='utf-8', newline='\n')
    write_json(out/'jobs.json', jobs)
    write_json(out/'reconciliation.json', provisional)
    write_json(out/'decisions.json', decisions or {'schema_version': 1, 'decisions': []})
    summary = {'episode': data['episode'], 'counts': report['counts'],
               'runs': [{'id': r.id, 'words': len(r.words), 'coverage_ms': r.coverage_ms,
                         'source': r.source, 'metadata': r.metadata} for r in runs],
               'pairs': [{k: v for k, v in pair.items() if k != 'agreements'} for pair in report['pairs']],
               'jobs': len(jobs['jobs']), 'unlocated': len(jobs['unlocated_disagreement_ids']),
               'elapsed_seconds': round(time.perf_counter()-started, 3),
               'audio_verified': False, 'algorithm': report['algorithm']}
    write_json(out/'summary.json', summary)
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manifest', type=Path)
    parser.add_argument('--out', required=True, type=Path, help='New directory, never overwritten')
    parser.add_argument('--decisions', type=Path)
    parser.add_argument('--drift-ms', type=int, default=2000)
    parser.add_argument('--max-tokens', type=int, default=192)
    parser.add_argument('--window-ms', type=int, default=30000)
    args = parser.parse_args()
    try:
        ledger = json.loads(args.decisions.read_text(encoding='utf-8')) if args.decisions else None
        result = run_comparison(args.manifest, args.out, ledger, drift_ms=args.drift_ms,
                                max_tokens=args.max_tokens, window_ms=args.window_ms)
    except (ValueError, KeyError, TypeError, OSError) as exc:
        parser.exit(2, f'Comparison failed: {exc}\n')
    print(json.dumps({k: result[k] for k in ('episode', 'counts', 'jobs', 'elapsed_seconds')}))


if __name__ == '__main__':
    main()
