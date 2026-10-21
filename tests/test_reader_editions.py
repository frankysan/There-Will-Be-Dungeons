"""Regression tests for wiki-supported reader editions.

Run: python -m unittest discover -s tests -p 'test_reader_editions.py'
"""
from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "reader_build", ROOT / "tools" / "build_reader_editions.py"
)
assert SPEC and SPEC.loader
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


class ReaderEditTests(unittest.TestCase):
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
