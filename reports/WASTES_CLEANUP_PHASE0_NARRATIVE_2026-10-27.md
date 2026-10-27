# Wastes cleanup — Phase 0 narrative baseline, batch 20261027-phase0-narrative-01

**Date:** 2026-10-27 (Europe/Stockholm). **State:** Planned; read-only inventory in progress. **Working branch:** `main`; baseline HEAD `02b1bf56aae3e5e3ec9a3b474559f3c45631ebe7`.

## Authorization and protected sources

The owner has explicitly accepted **eleven narrative arcs** on 2026-10-27, recorded in [D-045](../project/DECISIONS.md). This is structural approval, **not** an assertion that chapter prose has already been checked or migrated. The current invocation authorizes the next bounded *non-destructive* Phase 0 census. No story-document rewrites, changes to raw transcripts, renames, deletions or changes to approved arc boundaries are part of this batch.

Initial Git status: clean at `02b1bf56aae3e5e3ec9a3b474559f3c45631ebe7`. **Concurrent change noticed after read:** unrelated untracked `project/DELVERS_CREATURE_FACTION_INVENTORY.json`; preserve it. Main work remains the Wastes only.

## Planned scope and intent

- Ordered narrative inventory from local workspace: `ARC_ONE.md`, `ARC_TWO.md`, `ARC_THREE.md`, `ARC_FOUR.md`, `ARC_FIVE.md`, `ARC_SIX.md`, `README.md`, `SEASON_TWO.md`, `SEASON_THREE.md` (nine files). Sorting here is by narrative role, not literal directory order.
- **This slice:** `narrative/ARC_ONE.md` and `narrative/ARC_TWO.md`; read text without modifying it, measure supported structure and source links, flag what requires later scene/canon review.
- **Remaining:** seven other narrative files; all `world/` reference pages, controls, cross-repository inbound link census and complete source-to-scene coverage mapping. None should be claimed complete.
- The local workspace MCP provides line-numbered text reads and guarded edits, **not** byte-exact local SHA-256 or a general purpose shell. Record working-copy hashes as **not available** for this batch; a future local-capable pass must fill the required hash field before any substantive rewrite. No archive backup is required before this read-only census.
- `reports/wastes-cleanup/` is not an existing writable directory under current workspace MCP restrictions (file creation requires a tracked parent); this standalone journal uses the established `reports/` directory instead.

| Operation | Input | Approval | State |
| --- | --- | --- | --- |
| CENSUS-01 | `narrative/ARC_ONE.md` | Read-only Phase 0 | Pending |
| CENSUS-02 | `narrative/ARC_TWO.md` | Read-only Phase 0 | Pending |
| CONTROL-01 | Journal, [progress pointer](../project/WASTES_CLEANUP_PROGRESS.md), [manifest](../project/WASTES_CLEANUP_MANIFEST.md) | Required checkpoint metadata | In progress |

## Results — first structural census slice

The original `narrative/` files were read from the local workspace through their complete reported line ranges (no skipped line-numbered rows or range gaps). This is a **structural inventory only**, not a paragraph-by-paragraph scene/claim mapping or factual endorsement. Footnote episode links were not promoted to direct played-scene coverage.

| Source file | Read range | Main story sections | Approx. body words* | Main-body paragraph blocks | Footnote definitions | Notes begin | Lifecycle |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- |
| `narrative/ARC_ONE.md` | 1–145 / 145 | Prologue + I–VIII | 3,137 | 43 | 15 | line 109 | **Inventoried (structural only)** |
| `narrative/ARC_TWO.md` | 1–152 / 152 | I–VIII + Epilogue | 2,933 | 40 | 18 | line 103 | **Inventoried (structural only)** |

\*Word count is a text-only heuristic over chapter/prologue/epilogue body lines with Markdown decorations and link targets removed; it is **not** exact rendered prose or source-word count, and excludes the Notes section.

### Existing `ARC_ONE.md`: section spans and word estimates

| Start line | Section | Approx. words | Blocks |
| ---: | --- | ---: | ---: |
| 5 | Prologue — A world that survived the dragons | 150 | 2 |
| 11 | I. Beneath Dusthill — The broken waterworks | 365 | 5 |
| 23 | II. Leaving Dusthill — Captives and a home on wheels | 369 | 5 |
| 35 | III. The buried laboratory — A race to escape | 370 | 5 |
| 47 | IV. Slavetown — Freedom with limits | 368 | 5 |
| 59 | V. A city in flames — Murders and the mine deed | 385 | 5 |
| 71 | VI. The Black Mine — The descent | 371 | 5 |
| 83 | VII. Château Weir — The price of a soul | 379 | 5 |
| 95 | VIII. Heroes of the Wastes — The way out | 380 | 6 |

**Crosswalk lead (not scene coverage verified):** Existing Arc One spans E000–E026, including supplemental E013.5; approved future Arc 01 covers E000–E009 and Arc 02 covers E010–E026. The early Dusthill/laboratory sections and later Slavetown/Mine/Weir sections suggest a practical boundary near current Chapters III/IV, but **do not reassign a section until its actual paragraphs and notes are mapped**. The exact fictional placement of E013.5 remains an explicit review point.

### Existing `ARC_TWO.md`: section spans and word estimates

| Start line | Section | Approx. words | Blocks |
| ---: | --- | ---: | ---: |
| 5 | I. The road from the Liberators — A challenge and a pledge | 360 | 5 |
| 17 | II. Two voices — Stanley and Diontalus | 369 | 5 |
| 29 | III. Trashburg — The promises beneath the keep | 357 | 5 |
| 41 | IV. The deal collapses — Hope rebuilt and the pit below | 356 | 5 |
| 53 | V. An older kingdom — The books beneath the city | 375 | 5 |
| 65 | VI. The price of betrayal — P0D, the Gem and the petrified throne | 354 | 4 |
| 75 | VII. Through the beast — The Eye of Groxl and the last road to the keep | 353 | 4 |
| 85 | VIII. The crown — A queen and a city still in ruins | 361 | 5 |
| 97 | Epilogue — A kingdom to rebuild | 48 | 2 |

**Crosswalk lead (not scene coverage verified):** Existing Arc Two covers E027–E054, excluding standalone E043; approved new Arc 03 covers E027–E040, new Arc 04 covers E041–E054 excluding E043. The proposed transition falls around the Pit/cavern material within the later part of existing Chapter IV and the early Chapter V area; **no exact intra-section paragraph boundary is yet demonstrated**. An episode ID appearing in an endnote, especially E043/E055, is not proof that the narrative directly depicts a scene from that recording.

### What this slice did and did not verify

- **Completed:** files' reported line-range completeness, headings/section starts, body paragraph-block and approximate word counts, footnote-definition counts, initial old-to-approved-arc association, protected/no-edit scope.
- **Unassessed:** working-copy byte-exact SHA-256; paragraph/content hashes; actual source-to-scene/footnote mapping; heading anchors and incoming backlinks; qualitative chapter balance; episode-era/private knowledge; last direct observation and cause/effect accuracy. Mark these **pending**, not passed.
- **Validation:** no executable shell or local hash/lint utility offered by this MCP. This is a structural readback; Markdownlint, link/anchor validation, original audio listening and editorial accuracy checks are **not run**. The two narrative source files have not been edited.

### Recovery and next exact action

**CENSUS-01 and CENSUS-02: completed as structural inventory only.** Next work: Phase 0 read-only census of `narrative/ARC_THREE.md` and `ARC_FOUR.md`, or obtain a direct local runner first to capture missing hashes when available. Build paragraph-level source mapping only after baseline completeness. Owner's approval of eleven arcs is recorded in [D-045](../project/DECISIONS.md); an unapproved change to those boundaries still triggers the approval stop gate. Preserve the untracked Delvers inventory and every unrelated change.

**Concurrent workspace change at final validation:** local `main` HEAD advanced from the original `02b1bf56aae3e5e3ec9a3b474559f3c45631ebe7` to `e0d80b8c5bd553f85911e186f74e498482b0cd33` while this batch was in progress; unrelated Delvers modifications/untracked archival files also appeared. The latest status lists no changes to the two narrative source files; however, no commit-by-commit comparison or byte-identical hash audit was performed. **Before relying on these measurements for a rewrite, verify that those source inputs still match the recorded census snapshot.** This batch did not modify or intentionally stage/commit any Delvers work.
