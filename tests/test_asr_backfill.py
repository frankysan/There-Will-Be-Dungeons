"""Check exact whole-export metric independently of candidate alignment."""
import importlib.util
import itertools
from pathlib import Path
import random
import unittest

spec = importlib.util.spec_from_file_location('backfill', Path(__file__).resolve().parents[1] /
                                            'experiments/asr_backfill_2026_10_23.py')
backfill = importlib.util.module_from_spec(spec)
spec.loader.exec_module(backfill)


def oracle(a, b):
    row = list(range(len(b) + 1))
    for i, left in enumerate(a, 1):
        new = [i]
        for j, right in enumerate(b, 1):
            new.append(min(row[j] + 1, new[-1] + 1, row[j - 1] + (left != right)))
        row = new
    return row[-1]


class ExactComparisonTests(unittest.TestCase):
    def test_exhaustive_small_sequences(self):
        seqs = [p for n in range(5) for p in itertools.product(('hi', 'yes'), repeat=n)]
        for a in seqs:
            for b in seqs:
                self.assertEqual(backfill.distance(a, b), oracle(a, b), (a, b))

    def test_long_repetitions_and_order(self):
        rng = random.Random(23)
        for _ in range(100):
            a = rng.choices(('hi', 'yes', 'no', 'name'), k=rng.randrange(40, 160))
            b = rng.choices(('hi', 'yes', 'no', 'name'), k=rng.randrange(40, 160))
            self.assertEqual(backfill.distance(a, b), oracle(a, b))
        self.assertEqual(backfill.distance(['a'] * 300, ['a'] * 250), 50)
        self.assertEqual(backfill.distance(['yes', 'no'], ['no', 'yes']), 2)

    def test_report_normalization(self):
        self.assertEqual(backfill.tokens("Don't, don’t — C4N-D13; Élf_2! hi hi"),
                         ['dont', 'dont', 'c4n', 'd13', 'élf', '2', 'hi', 'hi'])


if __name__ == '__main__':
    unittest.main()
