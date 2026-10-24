"""Regression tests for wiki-supported reader editions.

Run: python -m unittest discover -s tests -p 'test_reader_editions.py'
"""
from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "reader_build", ROOT / "tools" / "build_reader_editions.py"
)
assert SPEC and SPEC.loader
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)

TRANSCRIPT_SPEC = importlib.util.spec_from_file_location(
    "transcript_build", ROOT / "tools" / "build_transcripts.py"
)
assert TRANSCRIPT_SPEC and TRANSCRIPT_SPEC.loader
transcript_module = importlib.util.module_from_spec(TRANSCRIPT_SPEC)
sys.modules[TRANSCRIPT_SPEC.name] = transcript_module
TRANSCRIPT_SPEC.loader.exec_module(transcript_module)


class ReaderEditTests(unittest.TestCase):
    def test_readable_renderer_uses_markdownlint_blank_line_spacing(self):
        cues = [
            transcript_module.Cue(1, 0, 1000, "speaker 0", "First line."),
            transcript_module.Cue(2, 600_000, 601_000, "speaker 1", "Second section."),
        ]
        output = transcript_module.render_markdown("E000", cues)
        self.assertNotIn("\n\n\n", output)
        self.assertIn(
            "**Listener-verified ending:** “Now” is the final spoken word; the remainder is music. "
            "Do not extend spoken-word timings into the outro.\n\n"
            "## 00:00:00–00:10:00\n\n",
            output,
        )
        self.assertIn(
            "**Scott** *[00:00:00]*: First line.\n\n"
            "## 00:10:00–00:20:00\n\n"
            "**Beau** *[timestamp unreliable; source SRT says 00:13:20]*: Second section.",
            output,
        )
        self.assertTrue(output.endswith("\n"))

    def test_reader_renderer_normalizes_excess_blank_lines(self):
        source = (
            "# E000 — Introductions\n\n"
            "> **Status: machine-generated readable draft — not a verified transcript.**\n \t\n\n"
            "## 00:00:00–00:10:00\n\n"
            "**Kristen** *[00:00:00]*: Hope.\n"
        )
        output, _ = module.render_reader("E000", source)
        self.assertNotIn("\n\n\n", output)
        self.assertNotIn(" \t\n", output)
        self.assertIn(
            "no new dialogue has been inserted.\n\n"
            "## 00:00:00–00:10:00\n\n"
            "**Kristen** *[00:00:00]*: Hope.",
            output,
        )

    def test_checked_in_reader_drafts_are_reproducible(self):
        for ep in module.EPISODES:
            with self.subTest(episode=ep):
                original = (ROOT / "transcripts" / f"{ep}.readable-draft.md").read_text(encoding="utf-8")
                reader, log = module.render_reader(ep, original)
                checked = (ROOT / "transcripts" / f"{ep}.reader-draft.md").read_text(encoding="utf-8")
                ledger = json.loads((ROOT / "transcripts" / f"{ep}.reader-edits.json").read_text(encoding="utf-8"))
                self.assertEqual(checked, reader)
                self.assertEqual(ledger, log)

    def test_ambiguous_phonetics_remain_unmodified(self):
        original = (ROOT / "transcripts" / "E001.readable-draft.md").read_text(encoding="utf-8")
        output, _ = module.render_reader("E001", original)
        self.assertIn("Orifi or Orify?", original)
        self.assertIn("Orifi or Orify?", output)

    def test_changes_only_to_turns_and_metadata(self):
        for ep in module.EPISODES:
            original = (ROOT / "transcripts" / f"{ep}.readable-draft.md").read_text(encoding="utf-8")
            output, log = module.render_reader(ep, original)
            source_turns = [line for line in original.splitlines() if module.TURN.fullmatch(line)]
            result_turns = [line for line in output.splitlines() if module.TURN.fullmatch(line)]
            with self.subTest(episode=ep):
                self.assertEqual(len(source_turns), len(result_turns))
                for before, after in zip(source_turns, result_turns):
                    start = module.TURN.fullmatch(before)
                    end = module.TURN.fullmatch(after)
                    assert start and end
                    self.assertEqual(start.group(2), end.group(2))
                self.assertEqual(sum(log["counts"].values()), len(log["edits"]))
                self.assertTrue(all(change["source_url"].startswith("https://twbd.fandom.com/")
                                    for change in log["edits"]))


if __name__ == "__main__":
    unittest.main()
