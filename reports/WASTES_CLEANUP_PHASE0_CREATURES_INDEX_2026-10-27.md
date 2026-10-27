# Wastes cleanup — Phase 0 creatures index, batch 09

**Date:** 2026-10-27 (Europe/Stockholm). **Status:** CREATURE-09-01/02/03 completed; saved and read back. **Repository:** `There Will Be Dungeons Transcripts`, `main` HEAD `ad80d071af89a968a25d186415b94cdb1a1b2df4`. **Initial visible working changes:** prior batch-07/08 reports added, Wastes manifest and progress modified; four visible Git entries; no restricted entries reported.

## Scope, authority, and preservation

Owner asked to proceed with `$twbd-wastes-cleanup` at the exact next [progress pointer](../project/WASTES_CLEANUP_PROGRESS.md). This batch performs **read-only structural inspection of `world/CREATURES_AND_MONSTERS.md`**, and may update **only this journal** and the Wastes cleanup manifest/progress metadata. D-045 already approves the **11-arc boundaries**; the migration is pending. D-044 already approves **The Principal, Principal City, Khaervilon, T'ietkalla** and other canonical written names. That does not authorize blind changes to source recordings, direct quotations, legacy filenames or other lore. Before any edit outside these explicitly allowed metadata operations, **stop and request owner approval**. Preserve concurrent work, stable IDs/paths, creature personhood distinctions, sources, historical archives, narrative and other campaigns. No commit, push or content reclassification.

## Ordered operations

| ID | Target and operation | State |
| --- | --- | --- |
| CREATURE-09-01 | Read all consecutive numbered lines of the 44-line creature index; classify purpose, headings, table entries, direct episode horizon, specialty-note status and name/taxonomy leads | **Complete: 44/44 lines** |
| CREATURE-09-02 | Enumerate ordinary Markdown links and footnote references; compare internal-world path targets to unchanged 134-file world worklist; explicitly delimit unchecked out-of-world targets | **Complete: 37/37 in-world links present in worklist; 13 outside-world unverified** |
| CREATURE-09-03 | Save observed findings here, synchronize Wastes manifest/progress and read back, then verify final live Git status | **Complete: controls read back and Git status checked** |

## Results and validation

**CREATURE-09-01 — structural read:** `world/CREATURES_AND_MONSTERS.md` has **44/44 numbered lines**, one H1, 36 pipe-table lines (header, separator and **34 entries**), and **one footnote definition** (`[^scope]`, line 44) referenced once from line 3. Of the 34 entries, **32** have dedicated `world/creatures/` links, whereas **mind fluffs** and **Slow Peters** (lines 7–8) have inline direct dossier links from S3E03/S3E05 and lack dedicated subject pages in this index. This is an *index and category-policy exception*, not a 34-article source review. The explanation deliberately distinguishes non-intelligent creatures/monstrous forms from reasoning NPCs, and retains P0D, Squirts, Henitar/Henatar Grape, the imprisoned black dragon and named companions within character contexts. Do not automatically reclassify people as beasts. The footnote's “compiled within Wastes E128 research horizon” describes older thematic compilation; newer Season Three rows extend selective index content without making every 32 older subject pages S3E18-complete. No audio listening or article-by-article final status audit occurred.

**CREATURE-09-02 — scoped link check:** **50** inline Markdown link occurrences: **37 distinct internal-world paths**, all matching paths in the unchanged, valid-JSON, **134-file `world/` directory worklist** (32 creature pages, three indexes, two character pages), with **zero missing listed-world targets**. The other **13** link occurrences point outside `world/` (episode dossiers, source-review reports and project policy) and were **not checked**. No fragment targets in these ordinary links. This was a lexical, single-page link scan, not a full repository backlinks/anchors or source-accuracy check.

**Approved spelling leads (not modified):** prose line 3 says `Tietkalla` (approved **T'ietkalla**); lines 16 and 20 contain `Kervalon` (approved **Khaervilon**). These are unambiguous apparent editorial candidates but they were *not replaced during the read-only census*; original source/quotes and stable slugs remain protected. Species classification, missing pages for two inline entries, and season-final status of individual articles are **not implicitly approved changes**. The 11-arc D-045 decision remains in force; no arc structure affected.

**Validation limits:** No byte-exact working-copy hash, pre-edit preservation archive (not needed for this read-only task), detailed page claim/source comparison, audio listening, full markdownlint, `git diff --check`, inbound-link scan, fragment parser or external-to-world destination test was run. This page has received a **first-pass structural review only**. World first-pass full reads now **9/134**; **125 remain**.

## Recovery pointer

**CREATURE-09-03 verified:** This report, manifest (109 lines), and progress pointer (35 lines) were read back with matching batch-09 evidence. Final observed Git status: branch `main`, HEAD `ad80d071af89a968a25d186415b94cdb1a1b2df4`, five Wastes-only metadata changes (three added reports from batches 07–09 and the two updated controls), no restricted entries; no commit or push. **Next separate read-only batch:** `world/FACTIONS_AND_POWERS.md` root index, after verifying the current checkout. Any material taxonomic or canonical-content edit not clearly approved requires the mandatory stop/owner decision.
