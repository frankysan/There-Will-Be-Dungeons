"""Synthetic, audio-free regression tests for resumable episode preparation."""
from pathlib import Path
import json
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))

from asr_metrics import distance, tokens
from prepare_episode import prepare


PRIMARY = """1
00:00:01,000 --> 00:00:02,000
(speaker 0) I'm here.

2
00:00:02,000 --> 00:00:03,000
(speaker 1) Never.

3
00:01:01,000 --> 00:01:03,000
(speaker 0) The dragon sings.
"""
SECONDARY = """1
00:00:01,000 --> 00:00:02,000
(speaker 0) I am here.

2
00:00:02,000 --> 00:00:03,000
(speaker 1) Never.

3
00:01:01,000 --> 00:01:03,000
(speaker 0) The dragon sings.
"""


class PrepareEpisodeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.folder = Path(self.tmp.name)
        self.primary = self.folder / "test.parakeet.processed.srt"
        self.secondary = self.folder / "test.qwen.srt"
        self.out = self.folder / "prepared"
        self.primary.write_text(PRIMARY, encoding="utf-8")
        self.secondary.write_text(SECONDARY, encoding="utf-8")

    def test_pair_produces_exact_metric_complete_windows_and_candidates(self):
        before_a = self.primary.read_bytes()
        before_b = self.secondary.read_bytes()
        record, cached = prepare(
            "E999", self.primary, self.out, self.secondary, window_minutes=1,
            review_limit=10,
        )
        self.assertFalse(cached)
        self.assertEqual(record["sources"][0]["cue_count"], 3)
        self.assertEqual(record["sources"][1]["cue_count"], 3)
        self.assertEqual(record["sources"][0]["normalized_token_count"], 6)
        self.assertEqual(record["metric"]["ordered_word_edits"], 2)
        self.assertEqual(record["metric"]["primary_normalized_tokens"], 6)
        self.assertEqual(record["metric"]["is_wer"], False)
        self.assertEqual(len(record["windows"]), 2)
        self.assertEqual(sum(w["cue_count"] for w in record["windows"]), 3)
        self.assertIsNotNone(record["alignment_statistics"])
        self.assertGreater(record["candidate_count"], 0)
        self.assertTrue(all(not c["audio_verified"] for c in
                            json.loads((self.out / "candidates.json").read_text(encoding="utf-8"))))
        self.assertIn("cue 1", (self.out / record["windows"][0]["file"]).read_text(encoding="utf-8"))
        self.assertIn("cue 3", (self.out / record["windows"][1]["file"]).read_text(encoding="utf-8"))
        self.assertEqual(before_a, self.primary.read_bytes())
        self.assertEqual(before_b, self.secondary.read_bytes())
        self.assertEqual(json.loads((self.out / "summary.json").read_text(encoding="utf-8")), record)

    def test_exact_existing_preparation_reused_but_changed_input_rejected(self):
        first, reused = prepare("E999", self.primary, self.out, self.secondary)
        self.assertFalse(reused)
        again, reused = prepare("E999", self.primary, self.out, self.secondary)
        self.assertTrue(reused)
        self.assertEqual(first, again)
        self.secondary.write_text(SECONDARY.replace("Never.", "No."), encoding="utf-8")
        with self.assertRaises(FileExistsError):
            prepare("E999", self.primary, self.out, self.secondary)

    def test_partial_generated_artifacts_are_not_silently_accepted(self):
        prepare("E999", self.primary, self.out, self.secondary)
        (self.out / "summary.md").unlink()
        with self.assertRaises(FileExistsError):
            prepare("E999", self.primary, self.out, self.secondary)

    def test_single_export_and_no_alignment_mode(self):
        record, _ = prepare("Delvers-S1E01", self.primary, self.out)
        self.assertIsNone(record["metric"])
        self.assertIsNone(record["candidate_count"])
        self.assertFalse((self.out / "candidates.json").exists())
        other_out = self.folder / "no-alignment"
        pair, _ = prepare("E999", self.primary, other_out, self.secondary, do_alignment=False)
        self.assertEqual(pair["metric"]["ordered_word_edits"], 2)
        self.assertIsNone(pair["alignment_statistics"])

    def test_reject_duplicate_or_nonchronological_sources(self):
        with self.assertRaises(ValueError):
            prepare("E999", self.primary, self.out, self.primary)
        bad = self.folder / "bad.srt"
        bad.write_text(PRIMARY.replace("00:01:01,000", "00:00:00,500"), encoding="utf-8")
        with self.assertRaises(ValueError):
            prepare("E999", bad, self.out)
        with self.assertRaises(ValueError):
            prepare("E999", self.primary, self.folder)

    def test_metric_preserves_report_normalization(self):
        self.assertEqual(
            tokens("Don't, don’t — C4N-D13; Élf_2!"),
            ["dont", "dont", "c4n", "d13", "élf", "2"],
        )
        self.assertEqual(distance(["im", "here"], ["i", "am", "here"]), 2)


if __name__ == "__main__":
    unittest.main()
