# Wastes Batch 82 — D-045 approved eleven-arc crosswalk versus live Places routes

**Date:** 2026-10-28. **Status:** bounded **READ-ONLY** navigation/crosswalk audit COMPLETE; narrative migration and route replacement **NOT** performed. **Authority:** D-045 owner-approved arc boundary baseline; D-047 stop before substantive/new scene placement; D-048 reader-first/navigation preservation. No source edits, archive, commit, push, unapproved story reconstruction or source-audio claims.

## Live access and repository preflight

- Re-evaluated full priority hierarchy at start of batch: direct local checkout absent from `/local`, `/mnt/data/There Will Be Dungeons Transcripts`, `/workspace/There Will Be Dungeons Transcripts` and `/workspaces/There Will Be Dungeons Transcripts`; Keycloak-authenticated repository **MCP available**. GitHub, Git-generated patches and ZIP fallback unnecessary. Check from first tier again on later file access/failure.
- Repository `There Will Be Dungeons Transcripts`, `main` HEAD **`fb65b9fb636f10674ea769b832b1dd5b89aba925`**, **11 existing visible working-tree changes / 0 restricted entries**, comprising Batch 78–81 place source, reports and archives plus trackers. Left intact, no reset/staging/commit/push.
- Working `world/PLACES.md` **89 LF lines / 19,904 bytes**, SHA-256 **`a3367d1ce294131af8f42ec84bca12ce894fce6e696ef4eb8a309a1ec2518934`**, as completed in Batch 81. Current route table L50–59 (six legacy route rows including historical prequel) was read but **not changed**. No pre-edit archive is necessary for this read-only batch. Future source mutation must create a **new, exact then-current** archive and independent SHA/size match first.

## Confirmed published narrative versus owner-approved D-045 crosswalk

Read `project/WASTES_NARRATIVE_CHAPTER_MAPS.md` L1–32 and L145–187, `project/WASTES_CAMPAIGN_CLEANUP_PLAN.md` L42–65 and L102–114, `project/DECISIONS.md` D-045/D-047, `narrative/README.md`, `wastes/README.md`, the openings of all six published arc narratives and the `ARC_FIVE.md` / `ARC_SIX.md` endings. The source chapter maps call themselves **preliminary beats**, while their **eleven numbered arc boundaries are owner-approved**.

| Current published file, observed source | Current file bytes / SHA-256 | D-045 destination arcs (approved boundaries) | Implication |
| --- | --- | --- | --- |
| `narrative/ARC_ONE.md` — E000–E026 incl. supplemental E013.5 | 24,216 / `956c0a4a6314fc09aee7f985bd7c95a6c9c6274ee958cfb0eaec557e11b39e7a` | **01** E000–E009; **02** E010–E026 | Split the established Dusthill/Slavetown journey with verified scene coverage; place E013.5 in story time |
| `narrative/ARC_TWO.md` — E027–E054, E043 one-off excluded | 25,058 / `7893a77a9f77ab94bd79e316abeb8d2c32f5c489f3ab8c7f8acb5318687c5f38` | **03** E027–E040; **04** E041–E054 except E043 | Split route to T'ietkalla from coronation, without importing one-off |
| `narrative/ARC_THREE.md` — E055–E081 | 28,792 / `730c17ee5ed78d8aca1c0f716bc8bb766b39289a6fbe97aeaf447877ad7cbca7` | **05** E055–E066; **06** E067–E081 | Separate government/Razak Val/Fate 4 from Khaervilon/CHIDS |
| `narrative/ARC_FOUR.md` — E082–E101 up through Hope's departure | 24,569 / `428f5e930d4d2e55de3f77f98d0809e9e6db6f3e526d75a4672c9b82be095a39` | **07** E082–E101 through Hope's departure | Same dramatic source boundary; only ID/title/navigation and chapter coverage changes, **not** a wholesale two-way split |
| `narrative/ARC_FIVE.md` — remainder of E101–E128 (E107–E109 historic, E127 one-off excluded) | 28,734 / `a2dfb834af74f8ad73c95332156ee19419614c30df2d305d53482734f26c8284` | **08** rest E101, E102–E106, E110–E114; **09** E115–E126, E128 | Must preserve inside-recording E101 split; distinguish historical Dunebreaker and E127; **E128 actually ends Season One** |
| `narrative/ARC_SIX.md` — S2E01–S2E12 plus S3E01–S3E18 | 206,128 / `44e8b30073d3d95a93b449783de11c7cafac1e74473c2ea082ce7e68b1ee541d` | **10** S2E01–S2E12 plus S3E01–S3E03; **11** S3E04–S3E18 | Break across the **S3E03/S3E04** transition, not at S2 season boundary; retain finale and out-of-game S3E019 distinction |

All **six** current arc paths exist and are readable, and `narrative/README.md` and `wastes/README.md` link the **actually published six**. `narrative/SEASON_TWO.md` / `SEASON_THREE.md` are current compatibility stubs to `ARC_SIX.md` and already state the eleven-arc replacement is **not yet implemented**. Candidate `ARC_SEVEN.md`–`ARC_ELEVEN.md` do **not** exist under these specific names. A planned `ARC_01.md` naming scheme is only a proposal, **not an enacted route**. Do not invent, publish or link to eleven files before choosing exact names and creating/validating the actual reading copies.

D-045 special cases: **E000** is introductory, **E013.5** is a separate supplemental story-time insert, **E043/E127** are standalone one-offs, **E107–E109** are historical *Dunebreaker*, **E101** has a single shared recording with two scene blocks but one unique dossier, **S2E12** is only a season ending, **S3E019** is nonplayed post-campaign cast Q&A. The approved row counts total **155 arc entries / 154 distinct source IDs** due solely to shared E101, rather than duplicated play. The preliminary chapter beats and exact E013.5 placement are **not** audited/approved scene mappings.

## Specific current `world/PLACES.md` route issues — OPEN, no edits

1. **Existing route labels refer only to published legacy Arcs One–Five**, plus historic Dunebreaker; **the published legacy Arc Six is entirely absent** from its L52–59 table. The Wastes root/season story guides already provide working routes to all six arcs. A draft eleven-row replacement would misrepresent nonexistent final chapter links.
2. The legacy table's L58 label says **“Arc Five through E126”**, whereas the **published `narrative/ARC_FIVE.md`, `narrative/README.md`, `episodes/E128.md` and D-045 consistently establish E128** as its actual endpoint, with E127 excluded. This is an unambiguous **stale route label** needing correction when the route table is coordinated. Existing route prose also ends its listed place chain at Elhandar; it should not be treated as an exhaustive route through E128.
3. The place directory now independently covers the S3E18 Moon facility and Mars Feywild platform, but **none of the older route labels should be retroactively renamed Arc 11** until new narrative content and navigation are ready.
4. The old Arc Four (E082–E101 split at Hope) already matches the **new Arc 07 source boundary**. Treat it as an ID/content compatibility migration, not a fresh story-time cut.
5. Root `wastes/README.md` and `narrative/README.md` explicitly describe the six published reading pages and note the future eleven-arc structure. Those are **accurate transitional statements**. Do not call them wrong or rewrite them prematurely.

## Reader-first eleven-route **draft map**, NOT approved active navigation

These location trails are **candidate orientation summaries only**, assembled from the owner-approved crosswalk's preliminary chapter beats and the current narrative/dossier coverage. They are **not new witnessed scene records, a surveyed map or final route-cell wording**:

| Approved arc | Existing evidence/approved transformation | Candidate geographic orientation for future route table |
| --- | --- | --- |
| **01 — Beginnings in Dusthill** | E000–E009 | Dusthill → waterworks → Leopold ruins → road toward Slavetown |
| **02 — Chains and Bargains** | E010–E026 | Slavetown → Black Mine → Château Weir → Liberators' refuge |
| **03 — Road to a Lost Kingdom** | E027–E040 | Golden Land → Trashburg and route toward T'ietkalla |
| **04 — The Crown of T'ietkalla** | E041–E054, except E043 | T'ietkalla's subterranean routes → keep → coronation |
| **05 — Kings and Consequences** | E055–E066 | T'ietkalla → Razak Val → Fate 4's loss / search |
| **06 — Beneath the World** | E067–E081 | Khaervilon → CHIDS → Traversal Drive |
| **07 — The City of Doors** | E082–Hope's E101 departure | Sigil → Outlands → White Tower |
| **08 — Separate Paths** | rest E101, E102–E106, E110–E114 | White Tower, infernal/other-plane and T'ietkalla strands (**parallel**, not direct route arrows) |
| **09 — The Fall of Elhandar** | E115–E126 and E128 | Elhandar → Earth/Villa Or'Nath → the Burrow's arrival |
| **10 — Across the Stars** | S2E01–S3E03 | Villa Or'Nath / Fate Six → Mars → Planet Nash → Pentel Weiss → Mars recovery |
| **11 — The Last War** | S3E04–S3E18 | Mars → Solar Mines and canyon → Moon facility → Planet Nash → diverging T'ietkalla, Razak Val, Mars/Feywild farewells |
| **Separate historical prequel** | E107–E109 | Dunebreaker; earlier fictional era, not main-arc present |

**Do not use unqualified route arrows as proof of sequential physical travel, identical sites, seen destinations or shared party locations.** E101 multiple viewpoints, E107–109 publication interruption, characters' disparate S3E18 departures and the unclear late second Nash all require provenance. The present route table's explanatory caution remains valid.

## Integration dependency and next bounded task

**No `world/PLACES.md`, narrative, root portal, season redirects, arc chapter or archived source bytes were changed in Batch 82.** Under D-045 and the cleanup plan, the eleven-arc route-table integration is **deferred until** (a) exact new file names plus compatibility policy, (b) old paragraph/scene/footnote crosswalk to new chapters, especially E101 and S2E12/S3E03, (c) source-based preliminary chapter-beat review, (d) new reading files written and verified, and (e) coordinated narrative/root/Wastes/world-index navigation updates. A standalone Places table flip now would create reader-visible claims of eleven accessible chapters that do not exist. An isolated E126→E128 legacy-label correction is supported and can be handled under D-047 as a separately archived minor change if the old table will persist during the phased migration, but **was not performed here**.

**Next Batch 83:** Build a bounded **read-only paragraph/episode/source-link crosswalk pilot**, starting with the heavy legacy `narrative/ARC_SIX.md` into approved target Arcs 10 and 11, using the approved S3E03/S3E04 boundary and monitoring old links and scene evidence. Do not rewrite or split narrative without full preservation, coverage tracking and any required specific approval. Prefer one precise arc/chapter segment per batch over a global 206k-byte rewrite. Continue to preserve all concurrent working changes.

**Validation still unrun:** GFM rendering/clickable Markdown footnotes, Markdownlint, whitespace diff, complete backlink census, 11-arc scene/paragraph audit, original audio listening and whole-project tests. This report is a navigation/crosswalk inventory only, not a certified complete migration map.
