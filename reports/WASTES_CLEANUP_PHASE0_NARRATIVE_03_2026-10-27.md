# Wastes cleanup — Phase 0 narrative structural census, batch 03

**Batch ID:** `20261027T172725+0100-phase0-narrative-03`. **Started:** 2026-10-27 17:27:25 +01:00 (Europe/Stockholm). **State:** Completed Phase 0 structural batch 03; journal, manifest and progress pointer synchronized and read back.  
**Workspace:** `There Will Be Dungeons Transcripts/` through local workspace MCP. **Branch:** `main`. **Starting HEAD:** `45b5556d17a01267e1962f6494cda703e615a3af`; starting Git working tree reported clean.

## Authority and scope

- The user invoked `$twbd-wastes-cleanup` to resume the next bounded Phase 0 census, as specified in [the progress pointer](../project/WASTES_CLEANUP_PROGRESS.md). **D-045** approves the eleven-arc division, **not** unsourced textual claims or unpreserved rewrites.
- **Read-only source files, in order:** `narrative/ARC_FIVE.md` followed by `narrative/ARC_SIX.md`. Protect every narrative source file, `sources/`, raw media, historical records, other campaigns and concurrent changes from edits.
- **Writable controls only:** this batch journal, `project/WASTES_CLEANUP_MANIFEST.md`, and `project/WASTES_CLEANUP_PROGRESS.md`; no content, navigation, paths, or arc-boundary changes.
- The directly mounted repository filesystem is unavailable in this session; workspace MCP can read numbered text lines, but does not supply exact working-copy SHA-256 or general-purpose shell execution. Hash and source archive operations remain pending and must precede any substantive rewrite. Do not substitute an unchecked GitHub revision for the current working copy.

## Ordered, recoverable operations

| ID | Target | Prerequisite and proposed output | State |
| --- | --- | --- | --- |
| CENSUS-05 | `narrative/ARC_FIVE.md` | Consecutive line-numbered reads through EOF; headings, sections, approximate prose/paragraphs, footnotes and reference issues | **Completed structural read: 177/177 lines** |
| CENSUS-06 | `narrative/ARC_SIX.md` | Bounded line-numbered reads through EOF; identify seasonal divisions and section density without rewrites | **Complete: 813/813 numbered lines** |
| CONTROL-03 | Journal, manifest, progress pointer | Persist actual measurements, next path, limitations and Git status; read back | **Complete: all three control files updated/read back** |

Earlier [batch 01](WASTES_CLEANUP_PHASE0_NARRATIVE_2026-10-27.md) inventoried Arcs One and Two; [batch 02](WASTES_CLEANUP_PHASE0_NARRATIVE_02_2026-10-27.md) inventoried Three and Four. Initial coverage **4 of 9** `narrative/` files. After this batch, the expected remaining paths (if both operations complete) are `narrative/README.md`, `narrative/SEASON_TWO.md`, and `narrative/SEASON_THREE.md`.

## Results, validation and recovery

**CENSUS-05 completed (Arc Five only):** `narrative/ARC_FIVE.md` read **177/177** numbered lines in three consecutive chunks, with no gaps. Eight main story chapters, **approximately 3,154** story-body words and **48** paragraph blocks; `## Notes` begins on line 117 and contains **29 footnote definitions**. All observed 58 footnote identifier mentions resolve to a definition. 43 Markdown links were detected (34 distinct target strings), **not checked for file/anchor existence**. Historical/old editorial name forms such as `Principle` and `Tietkalla` remain and require referent-specific inspection in the eventual migration, without changing these source bytes.

**CENSUS-06 completed (Arc Six):** The full **813/813 numbered lines** of **narrative/ARC_SIX.md** were read in fourteen consecutive nonoverlapping ranges, from 1–60 through 781–813. No missing ranges or line-parsing gaps were found. The document contains two long narrative season sections, followed by a separate research-status section beginning at line 807.

| Existing division | Start line | Third-level subsections | Approx. words* | Paragraph blocks |
| --- | ---: | ---: | ---: | ---: |
| Season Two — A Vessel for Hope | 7 | 14 | 7,548 | 96 |
| Season Three — The continuing Arc Six | 201 | 24 | 24,623 | 302 |
| Research status and source audits (metadata, not story) | 807 | 0 | About 956 | 3 |

Main narrative total: **approximately 32,171 body words and 398 paragraph blocks** across 38 third-level subsections, many of them episode-led rather than reader-facing chapters. There are **67 Markdown links (54 distinct target strings)**, **no numbered/labelled Markdown footnote definitions or markers**, and a separate source-status apparatus. None of these link destinations or anchors was checked, and the absence of footnote markers does not mean the sources are verified.

**Arc Six migration lead:** The approved new **Arc 10** is Season Two S2E01–S2E12 plus S3E01–S3E03; new **Arc 11** begins with S3E04 and ends at the played S3E18 finale. The old season heading at line 201 is **not** an approved arc boundary. The last S3E03 narrative subsection, “Gifts before war,” starts at line 275 and runs through 283. The next subsection, “A final evening, and the work of being alive,” begins at **line 285** and contains the played S3E04 augmentation/celebration material. This reading is corroborated by the dossiers **episodes/S3E03.md** and **episodes/S3E04.md**. Treat it as a strong future **passage-mapping candidate**, not as a substitute for exact line/paragraph/source-cue trace. S3E019 is nonplayed cast testimony, not a continuation after the S3E18 conclusion.

**Arc Five migration lead:** Old Arc Five supplies new **Arc 08** (the remainder of E101 plus E102–E114, excluding the historical E107–E109) and **Arc 09** (E115–E126 and E128, excluding E127). The existing Chapter IV, “A forest in the stars” (line 41), and its endnote links collectively cover **E114–E118**, so that current chapter spans the new E114/E115 boundary. Its section heading must **not** be used as an automatic splice point; map individual paragraphs and note claims before migration. E101 is shared with the existing Arc Four/new Arc 07 at Hope’s departure, without duplicating played action.

**Name-migration flags:** Old Arc Five has reader-facing “Principle” and “Tietkalla” occurrences. Arc Six's raw literal sweep found about 146 “Principle,” 3 “Kervalon,” 2 “Tietkalla” and 1 “Ornath”; these figures include mixed prose, link and source contexts and are *not* referent-reviewed corrections. D-044 authorizes canonical editorial spellings, **not** wholesale editing of quoted text, source transcripts, legacy links or ambiguous references.

*Approximate word count uses a rough Unicode token heuristic after stripping common Markdown decorations and link destinations. This is not an audio-grounded transcript word count.*

### Validation and lifecycle

**Completed:** full-range numbered-line reads, heading/section counts, heuristic story-body words and paragraph-block counts, existing Arc Five note-reference-definition matches (29 definitions; no missing marker IDs), markdown link inventory counts, and a first boundary comparison with relevant episode dossiers. Both documents are **structurally inventoried only**, not archived, rewritten, fact-reviewed or accepted.

**Not performed:** working-byte SHA-256, paragraph/content hashes, archived originals, full scene-to-dossier paragraph traces, source timestamp matching, incoming links and anchors, link target existence, editorial accuracy/audio verification, executable Markdownlint and Git diff --check. The local workspace MCP exposes no general-purpose shell. These remain prerequisites/limits, not passing results. No original narrative or SRT material was edited.

**Next action:** After synchronizing and verifying the manifest/progress pointer, inventory the three remaining **narrative navigation/compatibility files** in a bounded Phase 0 batch: narrative/README.md, narrative/SEASON_TWO.md, narrative/SEASON_THREE.md. Before any substantive rewrite, obtain byte-exact working-copy hashes, map source paragraphs/claims and links, and archive existing originals. Do not repeat these two source reads unless the inputs change or coverage needs targeted follow-up. Do not re-request owner approval for the eleven-arc boundary structure D-045.