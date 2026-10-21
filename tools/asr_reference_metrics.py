#!/usr/bin/env python3
"""Exact WER components for short, explicitly audio-verified reference samples."""
import argparse
import json
from pathlib import Path

from asr_evidence import normalized, interval


def error_rates(reference, hypothesis, max_cells=4_000_000):
    ref, hyp = normalized(reference), normalized(hypothesis)
    if len(ref) * len(hyp) > max_cells:
        raise ValueError('Reference sample too large; split into manually bounded samples')
    # State: (edits, substitutions, deletions, insertions). Linear memory.
    prev = [(j, 0, 0, j) for j in range(len(hyp)+1)]
    for i, word in enumerate(ref, 1):
        row = [(i, 0, i, 0)]
        for j, other in enumerate(hyp, 1):
            c, s, d, ins = prev[j-1]
            diag = (c + (word != other), s + (word != other), d, ins)
            c, s, d, ins = prev[j]
            delete = (c+1, s, d+1, ins)
            c, s, d, ins = row[j-1]
            insert = (c+1, s, d, ins+1)
            row.append(min((diag, delete, insert), key=lambda x: x[0]))
        prev = row
    edits, substitutions, deletions, insertions = prev[-1]
    return {'reference_words': len(ref), 'hypothesis_words': len(hyp),
            'substitutions': substitutions, 'deletions': deletions, 'insertions': insertions,
            'wer': edits/len(ref) if ref else None,
            'substitution_rate': substitutions/len(ref) if ref else None,
            'deletion_rate': deletions/len(ref) if ref else None,
            'insertion_rate': insertions/len(ref) if ref else None,
            'normalization': 'NFKC, Unicode lexical words, lowercase, straight apostrophe; repetitions retained',
            'tie_break': 'diagonal, deletion, insertion; ambiguous edit decompositions can differ'}


def evaluate(data):
    if data.get('schema_version') != 1 or data.get('audio_verified') is not True:
        raise ValueError('Metrics require a schema_version 1 audio-verified reference')
    for key in ('reviewer', 'evidence', 'episode', 'audio_id', 'reference_text'):
        if not isinstance(data.get(key), str) or not data[key].strip():
            raise ValueError(f'Reference requires {key}')
    interval(data['coverage_ms'], 'reference coverage')
    if not isinstance(data.get('hypotheses'), dict) or not data['hypotheses']:
        raise ValueError('Hypotheses must map run IDs to texts for the identical sample')
    return {'reference': {k: v for k, v in data.items() if k != 'hypotheses'},
            'metrics': {k: error_rates(data['reference_text'], v) for k, v in data['hypotheses'].items()}}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('reference', type=Path)
    args = parser.parse_args()
    print(json.dumps(evaluate(json.loads(args.reference.read_text(encoding='utf-8'))), indent=2))
