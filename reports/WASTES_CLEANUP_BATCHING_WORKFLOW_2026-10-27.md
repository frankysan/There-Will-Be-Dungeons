# Wastes cleanup — approved multi-file batching workflow update

**Date:** 2026-10-27 (Europe/Stockholm). **Scope:** owner explicitly agreed to grouped bounded audits after Batch 14. **Status:** workflow change implemented, read back and checkpointed; Batch 15 pilot not started. **Baseline:** local MCP checkout `There Will Be Dungeons Transcripts`, `main` at `ad80d071af89a968a25d186415b94cdb1a1b2df4`, ten prior Wastes-only metadata changes (eight reports plus two controls), no restricted entries reported.

## Approved change and protected scope

Update the Wastes cleanup skill's normal-batch selection, recovery instructions, cleanup campaign plan and active Wastes progress/manifest checkpoint to use **related multi-file structural-audit batches**. Do not modify any `world/`, `episodes/`, `sources/`, `narrative/`, legacy, media or other-campaign contents; do not mark 134-file worklist `listed_only` states as fact-reviewed or restructure arcs in this workflow change. No commit or push.

The user explicitly approved the recommendation to group approximately 4–6 files in the **next pilot** with around **300 numbered source lines**, using a single journal, per-file findings, and one consolidated administrative checkpoint, while keeping the approval stop gate. Subject and size determine later groups; large or complex indexes remain standalone. The current **14/134** first-pass world inventory is unchanged by this workflow-only update.

## Required controls

- **Before the group:** verify Git HEAD/status, recover an interrupted active batch, inspect actual candidate sizes and relationships, choose an **ordered, explicit target list**, exclusions, input evidence and per-file line budget; record the planned file paths *before* a substantial read.
- **Normal envelopes:** short (about 15–50 lines) 4–8 files / 300 total; medium (about 50–150) 2–4 / roughly 350; large (150–300) 1–2 / roughly 400; complex registers or over 300 lines **one separate batch**. Treat budgets as safety guides, not quotas.
- **During the group:** per-file operation IDs and durable `queued|reading|complete|blocked|unknown` states, own numbered-line coverage, links, internal-world match, external unchecked, footnotes, source horizon, alias/canon leads, evidence limitations and status; checkpoint the journal after each completed file. Do not invent completed line reads or tests.
- **Interruption:** retain completed file observations; reconcile `reading` or `unknown` from live source and last confirmed line, continue only incomplete work. If an unapproved material edit is required, **stop entire cleanup batch**, record exact issue, do not bypass by choosing another file.
- **After the group:** perform guarded manifest/progress updates once for the group, read back all three records and final Git status; file count is the number of individually completed first-pass files, not number of batches. Never rewrite the preserved original 134-path directory inventory.

## Specific next step after this workflow change

Next checkpoint is **Batch 15 pilot**, beginning with a size/purpose preflight of `world/ITEMS_AND_ARTIFACTS.md` and nearby unread, thematically related world pages. Choose 4–6 short/medium pages within a roughly 300-line working budget, record their full ordered paths and a **separate Phase 0 pilot journal before reading all file contents**. Revert to a smaller batch if input length/density justifies it. This document is **not** an audit of any of those world pages.

## Validation and recovery

**Implemented and verified in the local MCP working tree:**

- Updated `.agents/skills/twbd-wastes-cleanup/SKILL.md` to choose bounded related multi-file read-only audits with explicit preflight, per-file journal evidence, adaptive size limits, recovery, owner stop gate; refreshed its D-045 arc-decision wording.
- Updated `.agents/skills/twbd-wastes-cleanup/references/progress-and-recovery.md` with individual file state/line coverage, completion and resume rules, and once-per-batch manifest/progress synchronization.
- Updated `project/WASTES_CAMPAIGN_CLEANUP_PLAN.md` with grouped-budget table, Batch 15 pilot scope, and accurate existing D-045 approval.
- Updated `project/WASTES_CLEANUP_MANIFEST.md` with an explicit owner-approved workflow checkpoint; updated `project/WASTES_CLEANUP_PROGRESS.md` with the latest precise next action and consistent Phase 0 **14/134** world read count.
- Read back the altered skill, recovery instructions, plan, manifest, progress and this journal through the local workspace MCP. Verified the final Git scope: `main` unchanged HEAD `ad80d071af89a968a25d186415b94cdb1a1b2df4`, **14 visible Wastes-only changes** (nine added reports, including this journal, plus five modified controlling documents), **no restricted entries reported**. No `world/`, `narrative/`, `episodes/`, `sources/` or other campaign files modified; no commits or pushes.

**Limitations:** Git diff whitespace tests, markdownlint, source/audio/fact validation, byte-exact hash checks and world-link surveys **were not performed** for this metadata-only workflow change; MCP readback and Git-scope checks are not substitutes. Earlier pending verification work remains pending. **Next action:** Batch 15 candidate-size and thematic preflight, followed by an explicitly ordered 4–6-file read-only pilot (about 300 source lines), *not* a content rewrite.
