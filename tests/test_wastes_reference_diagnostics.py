"""Focused synthetic regression tests for the bounded Wastes reference diagnostic."""
import tempfile
import unittest
from pathlib import Path

from tools.wastes_reference_diagnostics import audit_alias_backlinks, heading_ids, scan


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

    def test_episode_domain_checks_links_without_rewriting_evidence(self):
        self.put("world/characters/stanley.md",
                 "# Stanley\n\n## Current status\n\nAlive.\n")
        episode = self.put("episodes/E063.md",
                           "# Episode\n\n[Stanley](../world/characters/stanley.md#current-status)\n"
                           "[Old alias](../world/characters/stanley-diontalus.md)\n")
        before = episode.read_bytes()
        result = scan(self.root, domains=("world", "episodes"))
        self.assertEqual(result["files_scanned"], 2)
        self.assertEqual(result["links_checked"], 2)
        self.assertEqual([x["kind"] for x in result["findings"]], ["missing_link_target"])
        self.assertEqual(episode.read_bytes(), before)

    def test_alias_audit_counts_preserved_historical_and_live_backlinks(self):
        self.put("world/characters/stanley-diontalus.md", "# Old alias\n")
        old = self.put("research/legacy/characters.md",
                       "# Snapshot\n\n[Joint](../../world/characters/stanley-diontalus.md)\n")
        live = self.put("project/PLAN.md",
                        "# Plan\n\n[Legacy](../world/characters/stanley-diontalus.md)\n"
                        "Literal `stanley-diontalus.md` is not a link.\n")
        before = (old.read_bytes(), live.read_bytes())
        audit = audit_alias_backlinks(
            self.root, ("world/characters/stanley-diontalus.md",),
            ("world", "research", "project"))
        self.assertEqual(audit["matches_found"], 2)
        self.assertEqual(audit["by_domain"], {"project": 1, "research": 1})
        self.assertEqual(audit["matches"][0]["line"], 3)
        self.assertEqual(sum(bool(m["historical"]) for m in audit["matches"]), 1)
        self.assertEqual((old.read_bytes(), live.read_bytes()), before)

    def test_alias_audit_reference_definitions_and_html_href(self):
        self.put("world/technology/mask-of-elton-iv.md", "# Historical alias\n")
        self.put("world/technology/mask-of-eltanfawr.md", "# Canonical\n")
        page = self.put(
            "project/PLAN.md",
            "# Plan\n\n[Old mask][mask]\n\n"
            "[mask]: ../world/technology/mask-of-elton-iv.md\n"
            "<a href='../world/technology/mask-of-elton-iv.md#old'>Historical</a>\n"
            "[New mask](../world/technology/mask-of-eltanfawr.md)\n"
            "Literal \`mask-of-elton-iv.md\` is not a link.\n",
        )
        before = page.read_bytes()
        result = audit_alias_backlinks(
            self.root, ("world/technology/mask-of-elton-iv.md",),
            ("project", "world"))
        self.assertEqual(result["matches_found"], 2)
        self.assertEqual(
            [x["kind"] for x in result["matches"]],
            ["reference_definition", "html_href"],
        )
        self.assertEqual([x["line"] for x in result["matches"]], [5, 6])
        self.assertEqual(result["by_domain"], {"project": 2})
        self.assertEqual(page.read_bytes(), before)

    def test_alias_audit_excludes_restricted_source_pages(self):
        self.put("world/characters/stanley-diontalus.md", "# Old alias\n")
        self.put("world/CONSISTENCY_LEDGER.md",
                 "[Old](characters/stanley-diontalus.md)\n")
        audit = audit_alias_backlinks(
            self.root, ("world/characters/stanley-diontalus.md",), ("world",))
        self.assertEqual(audit["matches_found"], 0)
        self.assertTrue(any("Restricted pages excluded" in v for v in audit["limits"]))
        self.assertFalse(audit["complete_within_limits"])

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
