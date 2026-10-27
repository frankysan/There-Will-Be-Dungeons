# Wastes cleanup — Phase 0 historical-events index, batch 11

**Date:** 2026-10-27 (Europe/Stockholm). **Status:** HISTORY-11-01/02/03 completed; records read back and Git scope verified. **Repository:** `There Will Be Dungeons Transcripts`, branch `main`, initial HEAD `ad80d071af89a968a25d186415b94cdb1a1b2df4`. Initial working tree: **six visible Wastes-only metadata changes** from batches 07–10 (four added reports and modified manifest/progress), zero restricted entries reported.

## Authority, bounded scope and stop gate

Owner instructed `$twbd-wastes-cleanup` to continue from recorded [progress](../project/WASTES_CLEANUP_PROGRESS.md). This batch permits **read-only structural census of `world/HISTORICAL_EVENTS.md`** and **metadata-only records** (this journal, Wastes cleanup manifest/progress). **D-045 approves the 11-arc proposal** but does not authorize an unsourced historical-page, narrative or link rewrite. **D-044** approves canonical editorial spellings (**The Principal, Principal City, Khaervilon, T'ietkalla, Moag Ferhain and related Or'Nath names**), with protection for direct testimony, originals, stable filename slugs and ambiguous referents. If a needed *substantive or undecided* content edit is not already approved, document exact proposal, **stop before applying it and ask owner**, rather than silently substituting another edit. No commits, pushes, source/episode/archive/other-campaign changes. Preserve existing/concurrent work.

## Bounded operations

| ID | Operation | State |
| --- | --- | --- |
| HISTORY-11-01 | Read 32/32 numbered lines, classify index rows, temporal/episode horizon, ancient vs played vs retrospective claims and chronology exceptions | **Complete: 32/32 consecutive lines; three headings and 17 event entries** |
| HISTORY-11-02 | Inventory lexical Markdown links/footnotes and compare internal-world path targets to original unchanged 134-file world worklist | **Complete: 19 internal-world links to 16 listed paths; 23 out-of-world links unverified** |
| HISTORY-11-03 | Write verified observations and limitations here, guarded checkpoint to manifest and progress, read back records and final Git status | **Complete: three records read back; Git status verified** |

## Findings and limits

### HISTORY-11-01 — full numbered structural read and temporal integrity

The entire `world/HISTORICAL_EVENTS.md` was read, **32/32 consecutive numbered lines** with no gaps; the index has **three Markdown headings** (one H1, two H2), **21 pipe-table lines** and **17 named event entries**. Section 1 contains **five ancient/retrospective history entries** (lines 9–13), and section 2 contains **twelve in-campaign turning points** (lines 19–30). The index explicitly declares an **E128 / Season One-ending research cutoff** at line 3; it does **not** claim knowledge through the full S2 and S3 campaigns, and contains **no S3E18 mention**. That cutoff must remain accurate until the index has been source-led extended, not mechanically changed to a later episode.

**Important evidence boundaries preserved:** the ancient Scorching is not securely dated and incorporates partly competing accounts; the Pristine-to-Slavetown transition incorporates GM background; the Solar Mines uprising is retrospective Nash testimony/character memory, **not played flashback**; the **Dunebreaker E107–E109 prequel takes place before E001 in fiction even though released between E106 and E110**. In the played-event table, water restoration, contracts, coronation, casualties and Elhandar exodus have scope/custody limits. The E081 deaths are explicitly reversed by later E082 appearance, and E128 descriptions **do not** assert that Earth has already been completely healed or the Ruby installed.

**Structural chronology leads, no edit:** line 30's **E120 Elhandar hunt/abduction** row appears *after* lines 28–29's **E125–E128 exodus/season ending** despite this being a turning-point chronology. Reordering it is an editorial-navigation proposal rather than a fact correction; review chronology, backlinks and section semantics before moving any rows. Line 24 still labels E101 Hope's departure as the **Arc Four → Arc Five** split and links legacy `ARC_FOUR.md`/`ARC_FIVE.md`, which are existing targets under the old six-arc navigation. The owner has accepted **D-045 eleven arcs** with a mid-E101 split, but new links/boundaries have not been deployed; do not redirect links to nonexistent new arc files or silently rewrite historical arc titles.

**Canonical spelling leads, not corrected in this batch:** five literal `Tietkalla` occurrences correspond to the now owner-approved **T'ietkalla** form, and one `Principle` occurrence refers to owner-approved **The Principal**. `Khaervilon`/`Kervalon` do not appear. Legacy file slugs (e.g. `HISTORY_TIETKALLA.md`) are intentionally preserved; each visible referent must be examined before the appropriate editorial pass. The continuity-exception footer distinguishes **E013.5's earlier-in-fiction scene**, **E043's unrelated holiday one-shot**, **nonplayed bonus Q&As**, and **Inverse as its own separate continuity**; none may be collapsed into ordinary Wastes chronology.

### HISTORY-11-02 — internal world link path check

The lexical ordinary Markdown-link scan found **42 occurrences**: **19** within `world/` to **16 distinct path targets**; all 16 targets match exact entries in the read-back, parsed, unchanged **134-file world directory worklist** (zero missing within that limited set). The other **23** links are **18 episode dossier references** (16 distinct episode destinations), **four legacy narrative arc/index links** (three distinct destinations) and **one separate Inverse continuity link**. Those 23 targets and their contents were **not checked**. No fragment links, `[^...]` footnote references/definitions or `[[review-needed:...]]` markers appeared within this page's scanned syntax. Worklist entries remain `listed_only`, as directory coverage is not content approval. No AST-style Markdown parsing, link-anchor/inbound backlink or external link verification was performed.

### Preservation and validation limitations

**Unchanged:** `world/HISTORICAL_EVENTS.md`, all other world/narrative/episodes/source/legacy/Inverse files, spelling displays, old arc links, stable identifiers and taxonomy. **Unperformed:** byte-exact source SHA-256, source-cue audit, ASR-to-audio checks, original audio listening, complete chronology ordering/source validation, incoming/outgoing anchor and 23 out-of-world link targets, Markdownlint and `git diff --check`. This is a **structural first pass**, not acceptance or source verification. With batches 05–10, the total fully structurally read world files is now **11/134**, leaving **123** outstanding.

## Recovery pointer

**HISTORY-11-03 verified:** the batch-11 report (39 lines), Wastes cleanup manifest (113 lines) and progress pointer (39 lines) were read back with consistent scope/findings and next operation. Final observed Git status: `main` HEAD `ad80d071af89a968a25d186415b94cdb1a1b2df4`; **seven visible Wastes-only metadata changes**, five added reports from batches 07–11 and two modified controls; **zero restricted entries** reported. No world/episode/narrative/source, stable slugs or other-campaign content edited; no commit or push. **Next separately journaled read-only slice:** `world/HISTORY_ANCIENT_CATASTROPHE.md`, after confirming current controls; do not initiate a scene rewrite or unapproved content change. Preserve the Dunebreaker earlier-in-world placement, intra-E101 split and **E043's separate holiday one-off**. Nonplayed bonus or Inverse cannot be counted as ancient Wastes action.
