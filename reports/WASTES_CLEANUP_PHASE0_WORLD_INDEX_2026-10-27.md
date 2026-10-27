# Wastes cleanup — Phase 0 world indexes, batch 06

**Date:** 2026-10-27 (Europe/Stockholm). **Status:** Intent recorded, bounded read-only census pending. **Checkout:** `main` at `a0a347b2e33ca9a4e4c561d259b472798d0b9d45`, initial working tree clean.

## Governing scope and approval

The owner invoked `$twbd-wastes-cleanup` to resume the [recorded next Phase 0 slice](../project/WASTES_CLEANUP_PROGRESS.md). D-045 approves the eleven-arc narrative boundaries, but not new world-canon assertions or unsourced text changes. This batch authorizes **read-only inventory only**, plus metadata updates to this journal and the Wastes progress/manifest controls. No world prose, original sources, story text, redirects, schema, paths or slugs will be changed. If a necessary content edit lacks explicit approval, record the proposed change and **stop for owner decision**.

Use [batch 05's 134-file worklist](../project/WASTES_CLEANUP_WORLD_WORKLIST_2026-10-27.json) as the bounded directory baseline, not as proof of per-page inventory completion. The worklist belongs to an earlier `main` revision; current HEAD has advanced. Root `world/` still includes both intended files, and this batch must read their current full contents to account for possible revisions. Do not alter historical worklist states, original transcripts, episodes, narrative arcs, audio or other campaigns.

The live local workspace MCP offers numbered-line reads and guarded text-file edits for controls, but no general-purpose shell or exact working-copy SHA-256 for text files. Working-copy checksums, byte-for-byte preservation snapshots, all-file backlink audits and full markdownlint remain pending; do not assert passing results.

## Ordered operations

| ID | Target | Planned evidence | Status |
| --- | --- | --- | --- |
| WORLD-INDEX-01 | `world/ANTAGONISTS.md` | Full consecutive numbered-line read; heading purpose, actual horizon, source/status notes, subject and external links, footnotes and unresolved targets | **Complete: 32/32 lines, structural only** |
| WORLD-INDEX-02 | `world/CHARACTERS.md` | Same; distinguish navigation/subject index from biographies and detect unresolved duplicated or stale coverage | **Complete: 65/65 lines, structural only** |
| WORLD-CHECK-06 | Batch journal, [manifest](../project/WASTES_CLEANUP_MANIFEST.md) and [progress pointer](../project/WASTES_CLEANUP_PROGRESS.md) | Save observed facts and lifecycle limits; verify readbacks and final repository status | **Complete: Wastes controls read back; Git status checked** |

**Exact next action:** Read `world/ANTAGONISTS.md` in numbered, consecutive chunks until its reported EOF; capture counts and diagnostic excerpts. Then read `world/CHARACTERS.md`, compare link destinations against the stored world-path worklist, and checkpoint. File-existence checks do not establish backlinks, headings, provenance or narrative truth.

## Observations and bounded checks

**WORLD-INDEX-01 and WORLD-INDEX-02 completed (read-only structural inventory).** Both files were read in a single uninterrupted consecutive numbered-line range. No parsing gaps were detected.

| Source file | Read coverage | Heading lines | Table lines | Approx. total words* | Prose words* | Markdown links | Footnote IDs |
| --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |
| `world/ANTAGONISTS.md` | **32/32** | 1, 5, 24 | 16 | 1,031 | 249 | 39 (35 distinct targets) | None |
| `world/CHARACTERS.md` | **65/65** | 1, 5, 16, 22, 38, 55, 63 | 31 | 1,375 | 563 | 74 (70 distinct targets) | None |

*Approximate Unicode-token word counts after removing common Markdown delimiters and link destination syntax, **not** audio/transcript word counts. “Prose” excludes table lines and headings; these indexes intentionally contain most informational text inside tables. Narrative-style chapter/footnote requirements do **not** apply mechanically to such specialist indexes.

### `world/ANTAGONISTS.md`

- **Purpose and horizon:** Role-based index distinguishing recurring threats from ambiguous intermediaries. Its opening line 3 explicitly covers the **played campaign through S3E18**, and says S3E019 is nonplayed cast Q&A; it also states that processed ASR/dossiers, **not independent audio listening**, supply the evidence.
- **Sections:** “Recurring threats and political adversaries” (line 5); “Dangerous or ambiguous intermediaries” (line 24). Reader-facing cast/status claims are interspersed in compact table rows; no Markdown footnote identifiers/definitions exist. This is an **index exception**, not evidence that full sourcing is complete.
- **Coverage and evidence caution:** The Principal/Vladimir entry at line 12 addresses S3E16–S3E18, lunar copies, Nash successor and unresolved final duplicate; the antagonist roles of Diontalus, Monsoon Cabbage, Brett/Asmodeus, Worldbreaker and Soulbroker each have distinct reported or witnessed outcomes. This inventory **does not verify those interpretations against audio or full dossiers**. The role index warns that an adversary label is not a moral or metaphysical certainty.
- **Approved spelling / stable paths:** Some reader-facing “Principle” and “Tietkalla” labels remain, including the principal antagonist link `characters/the-principle.md`. Owner-approved D-044 uses **The Principal** and **T'ietkalla** for unambiguous referents. Correct labels during a source/identity-aware targeted change; **do not rename the legacy filename or perform blanket source replacements**. Raw counts: six “Principle” and four “Tietkalla” literal occurrences (referents not individually adjudicated in this pass).

### `world/CHARACTERS.md`

- **Purpose and horizon:** Main directory for protagonists, companions, family, guests, rulers and witnesses; opening line 3 explicitly marks the **complete played campaign through S3E18** and excludes S3E019 from played action. Profiles remain ASR-provisional absent particular higher-grade evidence.
- **Sections:** protagonists (line 5), new Season Three companions/key survivors (16), long-running companions/family/allies (22), later companions and individual paths (38), major opponents/rulers/witnesses (55), reading policy (63). The player-vs-character and single-subject-profile distinction is already explicit. This is an **index/register exception**, not material for forced arc-biography formatting.
- **Name and testimony flags:** Stanley is identified as **Valiir Or'Nath** with owner-confirmed poem provenance, consistent with the existing decision. The profile link for **The Principal** still visibly says “The Principle / Vladimir” (line 59) while preserving filename `the-principle.md`. The index describes Nash as “Engineered son of the Principle” in line 9; source-ledger accounts contain conflicting/symbolic parentage and manipulated-dream claims, so **verify what S3E18 physically establishes about manufacture versus asserted parentage before changing that wording**. Do not promote a retrospective/planned explanation or interested character testimony to settled biological descent. Raw text contains three “Principle,” one “Tietkalla” and one “T'ietkalla” literal forms.
- **Retrospective boundary:** Later guest/Chance/Eddie material explicitly labels **S3E019 GM retrospective** rather than a newly played rescue or action, and the E107–E109 Dunebreaker prequel is correctly treated as historical rather than a chronological sequel. No new episode or person is invented by this inventory.

### Target-path check

The existing [134-file machine worklist](../project/WASTES_CLEANUP_WORLD_WORKLIST_2026-10-27.json) was re-read fully (615 numbered lines), parsed as JSON and used as a membership baseline. Relative Markdown link targets were normalized against each source path; result:

| Index | All Markdown links | Link occurrences resolving to listed `world/` files | Missing listed-world targets | Out-of-world links (not validated) |
| --- | ---: | ---: | ---: | ---: |
| `ANTAGONISTS.md` | 39 | 28 | **0** | 11 |
| `CHARACTERS.md` | 74 | 58 | **0** | 16 |
| **Total** | **113** | **86** | **0** | **27** |

The 27 outside-world link occurrences point to episode, project or historical research paths. Their existence, source-accuracy and incoming links/anchors have **not** been checked. Neither index has fragment identifiers in these Markdown links. This check does **not** validate the linked profiles' prose, audio, source cues, other directories, or inbound backlinks.

### Lifecycle, validation and preservation

- Both pages reached only **read-only structural inventory** (heading, table, rough words, note-marker, link and declared horizon inspection). They are **not** source-claim reviewed, audio-verified, accepted or structurally validated with full automated checks.
- No original `world/`, `narrative/`, `sources/`, `episodes/` or legacy/archive content was edited; no names, slugs, story scenes, profile claims or links were replaced.
- The earlier [world worklist](../project/WASTES_CLEANUP_WORLD_WORKLIST_2026-10-27.json) still lists all **134** items as `listed_only` because it records a **directory baseline**, not a progressively overwritten page-state register. This journal separately records the structural reads of these two indexes, bringing the total to **six structurally read world files** (including README, WORLD, ENTITY_SCHEMA, entities JSON); **128 files remain without this first-pass full read**.
- **Unperformed:** byte-exact working-tree SHA-256, archival copies (not required for a read-only survey), per-claim source window mapping, audio listening, full target/backlink/anchor scanning, Markdownlint, `git diff --check`, comprehensive project and episode inventory. Nothing is to be marked as passing.

**WORLD-CHECK-06 validated:** The [Wastes manifest](../project/WASTES_CLEANUP_MANIFEST.md) (batch 06 entry at line 103) and [progress pointer](../project/WASTES_CLEANUP_PROGRESS.md) (batch 06 entry at line 29) were updated and read back successfully. Final checkout remained `main` HEAD `a0a347b2e33ca9a4e4c561d259b472798d0b9d45`. Wastes-owned edits in status are this new report and the two control updates; concurrent Delvers edits and archives were left untouched. No narrative/world/source content edits, commits, pushes or full lint/test runs occurred. D-044 already authorizes canonical names but does **not** demand performing a source-replacing bulk rename as part of this inventory. New content changes outside that decision require explicit owner approval.

**Next exact slice after checkpoint:** Verify HEAD and present worklist, then carry out a separately journaled **read-only `world/CHRONOLOGY.md` structural census** (large technical chronological register). Preserve source clocks and record heading/date-episode structure, links, and its technical-index exception. Do not co-migrate the much larger `world/CONSISTENCY_LEDGER.md` in the same bounded slice.