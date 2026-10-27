# Wastes completed-campaign cleanup — progress and resume pointer

**Updated:** 2026-10-27 (Europe/Stockholm). **Repository:** `There Will Be Dungeons Transcripts`, branch `main`, initial HEAD `02b1bf56aae3e5e3ec9a3b474559f3c45631ebe7`.

**Structure approval:** [D-045](DECISIONS.md) — owner accepted eleven-arc crosswalk on 2026-10-27. Current `ARC_ONE`–`ARC_SIX` documents still exist and are **unmigrated**. Approved boundaries are not a validated scene map. Other unapproved content/canon edits require a separate approval checkpoint.

## Gates

| Phase | State | Evidence |
| --- | --- | --- |
| 0 — Detailed baseline | **In progress; six legacy arc files structurally inventoried (6 of 9 narrative files)** | [Batch 01](../reports/WASTES_CLEANUP_PHASE0_NARRATIVE_2026-10-27.md) · [Batch 02](../reports/WASTES_CLEANUP_PHASE0_NARRATIVE_02_2026-10-27.md) · [Batch 03](../reports/WASTES_CLEANUP_PHASE0_NARRATIVE_03_2026-10-27.md) · [manifest](WASTES_CLEANUP_MANIFEST.md) |
| 1 — Arc decision | **Structure approved D-045; coverage validation pending** | [Owner-approved crosswalk](WASTES_NARRATIVE_CHAPTER_MAPS.md) |
| 2 — Narrative rollout | Not begun | Requires Phase 0 census, source-to-scene trace and pre-edit archives |
| 3 — Races and discovery | Not begun | D-046 requests domain; detailed implementation/entries not implicitly approved |
| 4 — World rollout | Not begun | Domain/page-by-page review required |
| 5 — Research verification | Not begun under this cleanup | Existing episode research remains available |
| 6 — Campaign integration | Not begun | Depends on migrated and reviewed content |

**Prior checkpoint (batch 02; superseded by latest checkpoint below):** [Batch 01](../reports/WASTES_CLEANUP_PHASE0_NARRATIVE_2026-10-27.md) inventoried `narrative/ARC_ONE.md` and `ARC_TWO.md`; [Batch 02](../reports/WASTES_CLEANUP_PHASE0_NARRATIVE_02_2026-10-27.md) inventoried `narrative/ARC_THREE.md` and `ARC_FOUR.md` at initial HEAD `5531bd660d0b465f2f658b961f17eccbc33fde56`. All four source files were read completely without gaps, **not rewritten**. **Next exact action:** Confirm live Git HEAD/status, then begin bounded, read-only structural census of `narrative/ARC_FIVE.md`; inventory `ARC_SIX.md` in separate controlled chunks, given its size. Remaining narrative after batch 02: `ARC_FIVE.md`, `ARC_SIX.md`, `README.md`, `SEASON_TWO.md`, `SEASON_THREE.md` (**5 of 9**). Entire `world/` and cross-repository inbound-link census remain pending. Byte-exact hashes, paragraph-level source mapping, last direct observations, footnote targets and inbound anchors are **not complete for any file**.

**Latest completed slice — Batch 03 (2026-10-27):** [Journal](../reports/WASTES_CLEANUP_PHASE0_NARRATIVE_03_2026-10-27.md). Existing `narrative/ARC_FIVE.md` (177/177 lines) and `narrative/ARC_SIX.md` (813/813 lines) were fully structurally inventoried **without changing story content**. All six legacy arc files have now received an initial structural read (**6 of 9 narrative files**). Arc Five Chapter IV straddles the accepted E114/E115 boundary; Arc Six's accepted Arc 10/11 split begins at S3E04 (line 285 section), **not** the Season Three heading. Source-to-scene mapping, byte hashes, and incoming links remain pending. **Next exact action:** Verify Git status, then inventory `narrative/README.md`, `narrative/SEASON_TWO.md`, and `narrative/SEASON_THREE.md` in the next read-only Phase 0 batch. Thereafter complete the wider world/controls and link/hash baseline before story migration.

**Preservation:** No source or narrative prose modified. Byte-exact local SHA-256 and executable local lint/check runner are not provided by this MCP; hashes and automated checks remain pending until a suitable local runner is available. Preserve other campaign changes and untracked files.
