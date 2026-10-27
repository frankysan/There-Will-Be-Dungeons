# Wastes cleanup — Phase 0 narrative navigation and compatibility census, batch 04

**Batch ID:** `20261027T173923+0100-phase0-narrative-04`. **Started:** 2026-10-27 17:39:23 +01:00 (Europe/Stockholm). **State:** structural reads complete; pending owner decision on two compatibility stubs.  
**Workspace/revision:** local workspace MCP repository `There Will Be Dungeons Transcripts/`, `main`, initial HEAD `313993bc94c45e16772d538321649a7e832a901b`, initial Git status clean.

## Approval and scope

The user invoked `$twbd-wastes-cleanup`; the [progress checkpoint](../project/WASTES_CLEANUP_PROGRESS.md) explicitly selects the three outstanding narrative navigation/compatibility files for this bounded read-only Phase 0 batch. **D-045** authorizes the approved eleven-arc boundary structure; it does not establish passage accuracy or permit unpreserved rewrites. This batch performs **no navigation edits, story rewrites, renames, deletions or other canon changes**.

**Protected sources:** All current `narrative/` contents, `sources/`, other campaigns, archives, unpublished media and all unrelated working-tree changes. The only authorized mutations are this journal and its linked tracking records: `project/WASTES_CLEANUP_PROGRESS.md` and `project/WASTES_CLEANUP_MANIFEST.md`.

**Access limitations:** Direct host-local checkout is not mounted in this runtime; the local workspace MCP can read line-numbered text and make guarded edits, but does not provide a byte-exact SHA-256 or a general-purpose local shell. Hash baselines, automated Markdownlint and substantive preservation/rewrites are **not performed**. The HEAD is a revision label, not a measured working-byte hash.

## Ordered operations

| ID | Target | Required output | Status |
| --- | --- | --- | --- |
| CENSUS-07 | `narrative/README.md` | Complete line census, headings, existing six-arc navigation/notes, links/anchors, approval and stale-label flags | **Complete: 80/80 lines, structural only** |
| CENSUS-08 | `narrative/SEASON_TWO.md` | Complete line census, compatibility behavior, link targets, stale status | **Complete: 3/3 lines, content correction held** |
| CENSUS-09 | `narrative/SEASON_THREE.md` | Complete line census, compatibility behavior, link targets, stale status | **Complete: 4/4 lines, content correction held** |
| CONTROL-04 | Journal, manifest, progress | Capture results and remaining Phase 0 baseline work, reconcile status/readbacks | **Complete: checkpoint writes and targeted readbacks verified** |

Earlier [batch 01](WASTES_CLEANUP_PHASE0_NARRATIVE_2026-10-27.md), [batch 02](WASTES_CLEANUP_PHASE0_NARRATIVE_02_2026-10-27.md) and [batch 03](WASTES_CLEANUP_PHASE0_NARRATIVE_03_2026-10-27.md) covered six of the nine `narrative/` paths structurally. **This batch** targets the three remaining paths; a structural read of all nine would still **not** close the comprehensive Phase 0 baseline, which requires working-byte hashes, paragraph/source trace, incoming links/anchors, `world/`, and active project controls.

## Results, tests and recovery

### Completed structural reads

All three source files were read through their reported last numbered line with no gaps or parser issues. This was a read-only inventory; no titles, story text, links, status notices or redirects were changed.

| File | Lines | Read chunks | Headings | Markdown links | Distinct target strings | Footnote definitions | Unresolved footnote IDs | State |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `narrative/README.md` | 80/80 | 2 | 4 | 59 | 41 | 6 | 0 | **Structurally inventoried** |
| `narrative/SEASON_TWO.md` | 3/3 | 1 | 1 | 2 | 2 | 0 | 0 | **Structurally inventoried; content update approval required** |
| `narrative/SEASON_THREE.md` | 4/4 | 1 | 1 | 1 | 1 | 0 | 0 | **Structurally inventoried; content update approval required** |

**Guide / `narrative/README.md`:** The main headings are (line 1) “The Wastes — story guide,” (line 7) “Five completed Season One arcs,” (line 19) “Arc Six — Seasons Two and Three (COMPLETE: campaign finale),” and (line 23) “Notes.” Line 5 correctly says the **eleven-arc division is approved but not implemented** and links D-045/the crosswalk. Lines 9–21 and the subsequent source/notes material still describe the **actually available six old reader files**, which is accurate as a compatibility/transition presentation rather than a withdrawal of eleven-arc approval. Six footnote definitions have matching references; 59 Markdown links were detected (41 distinct strings), without checking their existence or inbound anchors. The guide retains legacy editorial name forms including “Tietkalla” and “Principle” in historical/current prose; treat these as **referent-specific migration leads**, not a blanket replacement instruction. The long “Notes” section contains past dated structure/horizon explanations, which should not automatically be rewritten as if they were new narrative.

**`narrative/SEASON_TWO.md`:** A three-line compatibility stub titled “Redirect — Arc Six (Seasons Two–Three).” Its links target `ARC_SIX.md` and `../episodes/S2E12.md`. It correctly distinguishes the S2E12 season ending from the longer continuing story, but still says “currently reviewed Season Three continuation,” a pre-final-completion formulation. Its target `ARC_SIX.md` is the **currently available** narrative file, so do not prematurely link to nonexistent Arc 10/11 files.

**`narrative/SEASON_THREE.md`:** A four-line compatibility stub with a link to `ARC_SIX.md`. Its body claims only the Season Three **opening** has been reviewed and “the arc has not ended.” **This is stale and contradicted by the owner-accepted completed campaign at S3E18**, independently reflected in `narrative/README.md` and D-045. It should be corrected only after explicit approval for the specific compatibility content update.

### Approval stop gate and recovery

**Pending owner approval:** A compatibility-status update to **both `narrative/SEASON_TWO.md` and `narrative/SEASON_THREE.md`** that (a) acknowledges that played Wastes ended with S3E18, (b) recognizes D-045's adopted eleven-arc boundaries without claiming new files exist, and (c) preserves legacy filenames and valid links to the existing `ARC_SIX.md` until new Arc 10/11 pages have been migrated and validated. Alternative: postpone both edits, leaving stale status text visible, until rollout; this is not the recommended option. **The owner has approved the eleven arcs, not explicitly the text of these redirect updates. Stop here and request a decision rather than proceed to another content edit.** The guide requires no immediate edit to record this batch.

**Remaining Phase 0 despite all nine narrative files being structurally read:** byte-exact local working-copy SHA-256, paragraph fingerprints, inline/outgoing target existence, **incoming** links and anchors, episode/scene/footnote claim coverage and evidence horizons, active project controls, and comprehensive `world/` enumeration. No full structural acceptance, factual review or audio verification is asserted. No execution environment was available for Markdownlint, `git diff --check` or checksum commands. Previous six narrative file structural measurements remain in their earlier batch reports and were not resampled.

**Next exact action:** Ask the owner to approve or decline the scoped two-redirect text correction. If approved, first confirm current HEAD, target bytes and preservation requirements; make a bounded edit with readback and crosslink validation, then resume the wider Phase 0 baseline. Do not silently skip this pending content decision.

**Checkpoint validation and concurrent work:** At the final status inspection, the local workspace still reported `main` HEAD `313993bc94c45e16772d538321649a7e832a901b`. Only three paths belong to this Wastes batch: new `reports/WASTES_CLEANUP_PHASE0_NARRATIVE_04_2026-10-27.md`, modified `project/WASTES_CLEANUP_PROGRESS.md` and modified `project/WASTES_CLEANUP_MANIFEST.md`. Concurrent Delvers files and archives appeared as other working-tree changes; **no Delvers target was edited by this batch**. All three Wastes tracking documents were read back (the progress pointer in smaller ranges after one broad-range request was blocked). No files under `narrative/` were changed. No commit, push or full test execution.