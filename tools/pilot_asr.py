#!/usr/bin/env python3
"""Reproduce only the existing two-episode export comparison; never launch ASR."""
import argparse
import json
from pathlib import Path

from compare_asr import run_comparison, write_json
from audit_sources import sha256

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True, help='New directory for bounded export pilots')
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=False)
    summaries = {}
    examples = {}
    for name in ('E000-full', 'E001-full', 'E001-opening'):
        summaries[name] = run_comparison(ROOT/'experiments/multipass'/f'{name}.json', args.out/name)
        print(name, summaries[name]['counts'], summaries[name]['elapsed_seconds'])
        report = json.loads((args.out/name/'comparison.json').read_text(encoding='utf-8'))
        chosen = report['disagreements'][:5]
        if name == 'E001-opening':
            for rec in report['disagreements']:
                pair = {s['run_id'] for s in rec['sources'] if s['role'] == 'aligned'}
                if ('possible boundary duplicate' in str(rec['diagnostics'])
                        or rec['classification'] == 'boundary_anomaly' and rec['end_ms'] > 600000
                        or rec['start_ms'] is not None and 99500 <= rec['start_ms'] <= 103000
                        and pair == {'E001-baseline', 'E001-chunk30-overlap3'}):
                    chosen.append(rec)
        examples[name] = {'comparison_sha256': sha256(args.out/name/'comparison.json'),
                          'selection': 'First five records, plus opening greeting/duplicate/overrun examples; not exhaustive',
                          'records': chosen}
    write_json(args.out/'pilot-summary.json', summaries)
    write_json(args.out/'pilot-evidence.json', {
        'schema_version': 1, 'audio_verified': False, 'summaries': summaries,
        'tool_sha256': {p.name: sha256(p) for p in sorted((ROOT/'tools').glob('*asr*.py'))},
        'examples': examples})


if __name__ == '__main__':
    main()
