# Wastes cleanup — Phase 0 factions and powers index, batch 10

**Date:** 2026-10-27 (Europe/Stockholm). **Status:** Batch 10 complete; journal, manifest and progress checkpoint read back and Git status verified. **Checkout:** `There Will Be Dungeons Transcripts`, branch `main`, initial HEAD `ad80d071af89a968a25d186415b94cdb1a1b2df4`. Initial visible status: **five Wastes-only control changes** (added batch-07/08/09 journals, modified cleanup manifest and progress pointer); no restricted entries reported.

## Scope and approval

The user's "Proceed" continues `$twbd-wastes-cleanup` at the exact recorded next Phase 0 slice: **read-only structural inspection of `world/FACTIONS_AND_POWERS.md`**, and metadata-only report/manifest/progress updates. The eleven-arc structure **D-045** is owner-approved but not migrated. Written spellings **D-044** (The Principal, Principal City, Khaervilon, T'ietkalla, Moag Ferhain and Or'Nath family names) remain binding for new editorial text, without blind source changes. Any **unapproved substantive lore, taxonomy, structural, text/slug rewrite or other edit** requires stopping before that edit and requesting owner direction. Do not silently resolve contested institutions or turn a retrospective plan into played history.

Preserve all existing Git changes, world/source/episode/narrative content, stable paths, raw media and archived research; do not commit or push.

## Ordered operations

| ID | Operation | State |
| --- | --- | --- |
| FACTIONS-10-01 | Full numbered-line read of present 23-line index; categorize headings, subject/index entries, played/source horizon and named-entity migration leads | **Complete: 23/23 numbered lines; one H1, 15 entries** |
| FACTIONS-10-02 | Count ordinary Markdown links; check local `world/` link membership in historical 134-path world worklist; identify untested out-of-world targets/anchors | **Complete: 31 internal occurrences/27 destinations listed; 13 others unverified** |
| FACTIONS-10-03 | Save evidence here, update the Wastes manifest and progress with a guarded change, read back, verify final Git status | **Complete: three records read back; Git scope verified** |

## Findings and validation

### FACTIONS-10-01 — scope and structure

**Full numbered-line read:** current `world/FACTIONS_AND_POWERS.md` comprises **23/23 lines**, one level-one title, **17 table lines** (header + separator + **15 faction/power entries**, lines 7–21), no Markdown footnote references/definitions and no explicit `[[review-needed:...]]` markers. The file is a functional **thematic index of factions, institutions and supernatural power claimants**; its rows mix concrete organizations with coalition/war-time snapshots, individual representatives and cosmological claims. This is not a dedicated institutional-history page census or permission to merge organizations with a single person. **Observed** acts and **attributed testimony** must remain distinguished.

**Stale research horizon, not a trivial date edit:** line 3 states “spoilers through researched **S3E15**,” even though the **played campaign ended S3E18**. Content includes S3E05–09 Solar Mines snapshots, S3E12–15 dramatic developments, unfinished ambitions and “not yet” status labels valid only at those individual episodes' source cutoffs. **There is no S3E18 entry in this index.** A source-backed final institutional-status audit must check S3E16–S3E18 before changing the top-level horizon, marking warfare resolved, inventing the continued existence/disappearance of organizations or recasting time-of-knowledge. S3E019 cast roundtable is **nonplayed retrospective** and can clarify intended unused designs but must not be treated as witnessed action (particularly Council of Faces, Principal City, Council of Earthly Defenders and the Principal's later fates).

**Canonical orthography and crosswalk:** three literal `Principle` occurrences and three `Tietkalla` occurrences remain, while the first faction name already reads **The Principal's regime**. D-044 confirms **The Principal**, **T'ietkalla**, **Khaervilon**, **Moag Ferhain**, **Principal City** and the Or'Nath family forms for editorial referents; legacy filename `characters/the-principle.md` and `places/tietkalla.md` remain intentionally compatible. One `Arc Six` link (line 15) points to the still-existing legacy narrative, not a validated future Arc 11 target. Under owner-approved **D-045**, the eleven-arc structure is an implementation dependency; **do not rewrite link targets or old historical descriptions before the new arc navigation exists**. All these items are editorial migration *candidates*, not edits made in batch 10.

### FACTIONS-10-02 — bounded link membership

**44** ordinary Markdown link occurrences: **31 internal-world** references to **27 distinct paths**, each path present in the unchanged **134-item, sorted/deduplicated valid-JSON historical world directory worklist**; **zero missing listed-world destinations**. External-to-world occurrences comprise **12 episode dossier links (11 distinct targets)** and **one** `../narrative/ARC_SIX.md` compatibility link; their actual targets, content, incoming anchors and citation accuracy were **not** checked. No fragment markers were found in this page's ordinary inline links; syntax counting is **not** comprehensive Markdown parsing or a repository-wide link test. Worklist page states remain `listed_only`, by design.

### Preservation and evidence limits

No `world/`, `narrative/`, `episodes/`, `sources/`, legacy archives, canonical entity records, slugs or other campaigns changed. No substantive lore/canon or article-creation decisions made. **Not run:** byte-exact source SHA-256, preservation archive (unnecessary for read-only census), fact/claim-vs-episode validation, original-audio listening, comprehensive backlink/anchor and external-to-world link validation, Markdownlint and `git diff --check`. This page is **first-pass structurally read only**, not fact-reviewed/audio-verified/accepted. First-pass fully read world files: **10/134**, with **124 remaining**.

## Resume pointer

**FACTIONS-10-03 verified:** the new batch-10 journal, Wastes manifest (111 lines) and progress pointer (37 lines) were read back with matching evidence and next step. Final observed Git status: branch `main`, HEAD `ad80d071af89a968a25d186415b94cdb1a1b2df4`, **six Wastes metadata changes only** (four added batch-07 through batch-10 reports and two modified progress/manifest controls), zero restricted entries reported. No world, narrative, episodes, raw sources or other campaign content edited; no commit or push. **Next separately scoped read-only batch:** `world/HISTORICAL_EVENTS.md` (the next unread root-world file shown in the directory listing). If a material edit becomes necessary and lacks explicit approval, record the hold and stop instead of choosing another edit.
