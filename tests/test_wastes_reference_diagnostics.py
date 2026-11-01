"""Focused synthetic regression tests for the bounded Wastes reference diagnostic."""
import tempfile
import unittest
from pathlib import Path

from tools.wastes_reference_diagnostics import heading_ids, scan


class ReferenceDiagnosticsTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "world" / "characters").mkdir(parents=True)

    def put(self, relative, body):
        p = self.root / relative
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(body, encoding="utf-8")
        return p

    def test_valid_links_fragments_notes_and_status(self):
        self.put("world/characters/hope.md",
                 "# Hope\n\n## Current status\n\nSafe.[^e]\n\n[^e]: Evidence.\n")
        self.put("world/README.md", "# World\n\n[Hope](characters/hope.md#current-status)\n")
        result = scan(self.root)
        self.assertEqual(result["links_checked"], 1)
        self.assertEqual(result["findings"], [])
        self.assertTrue(result["complete_within_limits"])

    def test_missing_link_and_fragment_are_distinct(self):
        self.put("world/README.md", "# Main\n\n[Missing](missing.md)\n\n"
                 "[Not a heading](characters/a.md#vanished)\n")
        self.put("world/characters/a.md", "# A\n\n## Current status\n\nAlive.\n")
        kinds = [x["kind"] for x in scan(self.root)["findings"]]
        self.assertIn("missing_link_target", kinds)
        self.assertIn("fragment_candidate", kinds)

    def test_missing_and_orphan_footnotes(self):
        self.put("world/README.md", "# Source\n\nUnknown[^missing].\n\n[^unused]: Not cited.\n")
        kinds = [x["kind"] for x in scan(self.root)["findings"]]
        self.assertIn("missing_footnote_definition", kinds)
        self.assertIn("unused_footnote_definition", kinds)

    def test_name_and_status_are_advisories(self):
        self.put("world/characters/test.md", "# Kervalon\n\nThe Principle visits.\n")
        findings = scan(self.root)["findings"]
        self.assertTrue(any(x["kind"] == "missing_final_status" for x in findings))
        self.assertTrue(any(x["kind"] == "canonical_name_candidate" for x in findings))
        self.assertTrue(all(x["level"] == "review" for x in findings))

    def test_duplicate_heading_slugs(self):
        self.assertEqual(heading_ids("# Name\n\n## Tally\n\n## Tally\n"),
                         {"name", "tally", "tally-1"})

    def test_restricted_pages_never_scanned(self):
        self.put("world/characters/bok-bok.md", "# Restricted\n\n[^ghost]: Note.\n")
        self.put("world/README.md", "# Index\n\n[Go](characters/bok-bok.md#missing)\n")
        result = scan(self.root)
        self.assertEqual(result["files_discovered"], 2)
        self.assertEqual(result["files_scanned"], 1)
        self.assertTrue(any("Capability-restricted" in item for item in result["limits"]))
        self.assertTrue(any(x["kind"] == "restricted_fragment_target" for x in result["findings"]))
        self.assertFalse(any(x["kind"] == "unused_footnote_definition" for x in result["findings"]))

    def test_bounds_are_reported_and_no_files_are_modified(self):
        p = self.put("world/README.md", "# Intro\n\n[one](a.md) [two](b.md)\n")
        before = p.read_bytes()
        result = scan(self.root, max_links=1)
        self.assertEqual(result["links_checked"], 1)
        self.assertEqual(result["links_skipped"], 1)
        self.assertFalse(result["complete_within_limits"])
        self.assertEqual(p.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
