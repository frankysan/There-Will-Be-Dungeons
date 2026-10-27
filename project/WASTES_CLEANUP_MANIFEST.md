# The Wastes — completed-campaign cleanup migration manifest

**Initialized:** 2026-10-27. **Status:** **Preliminary planning inventory only; eleven-arc boundaries now owner-approved by D-045, implementation pending**. An exhaustive up-to-date file-by-file, hash-and-inbound-link census, source-claim review and migration log have **not** been performed. Based on a read-only inspection of GitHub `main` at **`c0b2a8317a1865922211920c62ae69b1a6661254`**, except where separately indicated. Do not confuse inspected paths with an accepted complete inventory.

[Campaign plan](WASTES_CAMPAIGN_CLEANUP_PLAN.md) · [proposed arc crosswalk](WASTES_NARRATIVE_CHAPTER_MAPS.md) · [existing world-arc manifest](WORLD_ARC_MIGRATION_MANIFEST.md) · [Delvers method](DELVERS_CLEANUP_MANIFEST.md).

## 1. Inventory method and states

**Required complete census:** all maintained files in `narrative/`, `world/` (including directories and `entities.json`), Wastes episode/navigation/control files, active `project/` policy and review files, and affected reference/report paths. Do not silently count separately scoped `delvers/` or `inverse/` content as Wastes canon. Preserve out-of-game bonuses, one-offs, early prequel and raw source inventories as distinct classes.

Future machine manifest fields per file:
- `path`, `type`, `canonical_subject_id`, `legacy_aliases`, `sha256` / blob SHA, `baseline_commit`, `source_horizon`, `last_direct_observation`.
- Page headings, prose word and paragraph counts per section, footnote/reference counts, note diagnostics, source episode IDs, inbound links and anchor references, related entities, dependencies.
- `problem_flags` (stale endpoint, research apparatus in narrative, duplicate scene/subject, unsupported identity merge, named-entity orthography, missing source, broken link, wrong classification), priority and proposed disposition.
- `archive_path`, exact preservation hash, migrated paragraph/claim trace, new canonical path or compatibility alias, review evidence and test outcome.
- Lifecycle: **not-inventoried → inventoried → outlined → archived → edited → structurally-validated → fact-reviewed → accepted**. Do not conflate a structural check with factual/audio approval. A genuine exempt register should be marked **retained-exception**, not "rewritten."

The earlier [world arc migration manifest](WORLD_ARC_MIGRATION_MANIFEST.md) records **85 world Markdown files at its 2026-10-24 baseline** and later scoped pilots; this is **not** today's number and must not be copied into the new total. The new observed subdirectories contain 46 character-related pages, 19 place pages, 32 creature pages and 21 technology pages. They include specialized registers and must be classified individually.

## 2. Immediate priority / risk register

| Path or group | Observed issue or task | Priority | Proposed disposition | Current state |
| --- | --- | --- | --- | --- |
| `narrative/ARC_SIX.md` | ~205k characters, 814 lines, thirty played episodes; season-oriented additive blocks and uneven weight | **P0** | Preserve; full scene/paragraph map; use as stress-test for proposed Arc 10/11 | Inspected, **not migrated** |
| `narrative/ARC_ONE.md`–`ARC_FIVE.md` | Each ~24–29k characters; current arcs cross several natural story changes, many run around 27 episodes | **P0** | Per-scene crosswalk into proposed Arc 01–09; balanced chapter pilots and old-path compatibility | Inspected, **not migrated** |
| `narrative/README.md` | Correct campaign endpoint at S3E18; current six-arc reading order | **P1** | Only change after owner decides arc structure | Inspected |
| `narrative/SEASON_TWO.md`, `SEASON_THREE.md` | Legacy redirects to current Arc Six; one stub retains "arc has not ended" | **P1** | Preserve target compatibility; reconcile obsolete status with concluded campaign | Inspected |
| Root `README.md` | Several "latest researched" pointers still reference S3E15, despite concluded campaign | **P0** | Separate navigation/horizon pass, avoiding mass edits of historical research notes | Inspected |
| `world/WORLD.md` | Declares researched horizon E124 while current Wastes ends S3E18 | **P0** | Reassess global setting/systems synthesis and ending states | Inspected |
| `world/PLACES.md` | S3E15 horizon and episode-recap material among place summaries | **P1** | Retarget directory after place-by-place inventory, reconcile map names | Inspected |
| `world/FACTIONS_AND_POWERS.md` | S3E15 horizon; early/late faction fates and the Principal require review | **P1** | Subject-led faction directory; missing standalone candidates audit | Inspected |
| `world/ITEMS_AND_ARTIFACTS.md` | S3E15 horizon; changing object custody and effects after finale | **P1** | Inventory/custody study and final status corrections | Inspected |
| `world/HISTORICAL_EVENTS.md` | Only declares E128 horizon; later campaign changed world and public institutions | **P1** | Integrate witnessed turning points and separate disputed ancient history | Inspected |
| `world/CHRONOLOGY.md` | ~186k-character detailed source-keyed timeline; already reaches S3E18 | **P1** | Keep chronological technical exception, detect duplicate event clocks/old boundaries | Inspected |
| `world/CONSISTENCY_LEDGER.md` | ~312k characters, many dated cutoffs and active naming question `names.principle` now superseded by owner-confirmed orthography | **P0** | Close *spelling-only* uncertainty, preserve plot/identity questions; archive obsolete episode updates after claim comparison | Inspected |
| `project/REVIEW_QUEUE.md` | ~293k characters; historic research material, old "next" pointers and valid high-priority listening windows mixed | **P1** | Distill open issue keys and check completion, preserve old queue versions | Inspected |
| `world/CHARACTERS.md` and `world/characters/` | 46 files observed; mixed finished profiles, specialist registers, and research-era structures | **P1** | Last-state audit, characterization-focused rewriting, correct names and preserve exception registers | Directory inspected only |
| `world/places/` | 19 files observed; many have no post-Season-One final state | **P1** | Place-specific status, culture, geography, provenance | Directory inspected only |
| `world/creatures/` and `CREATURES_AND_MONSTERS.md` | 32 files observed; avoid equating intelligent persons with unintelligent beasts | **P1** | Follow creature taxonomy and separate race/individual concepts | Directory inspected only |
| `world/technology/` | 21 files observed; may omit important objects or final holder/status changes | **P1** | Artifact and technology inventory/chain-of-custody review | Directory inspected only |
| `world/RACES.md`, `world/races/` | **Proposed new domain, files not created by this planning change** | **P0** | Define schema/entry structure then implement source-backed racial profiles | Planned |
| `world/ENTITY_SCHEMA.md`, `world/entities.json` | JSON version 1 pilot seed limited to E000/E001 | **P1** | Controlled expanded taxonomy, stable entity IDs, canonical display names, old aliases and relationships | Inspected |
| `project/DOCUMENTATION_ARCHITECTURE.md` | Still presents Wastes at Season One horizon and current five/six-arc structure | **P1** | Reconcile when new structure is selected, retain historical architecture decision context | Inspected |
| `project/EDITORIAL_GUIDE.md` and `DECISIONS.md` | Need binding map-spelling decisions and planned scope cross-references | **P0** | Add owner naming rule and proposal status without changing source-evidence tier | Targeted documentation update |
| `reports/WASTES_KNOWN_MAP_ORTHOGRAPHY_2026-10-27.md` | Earlier analysis treated Principal as only map-preferred; Khaervilon not registered | **P0** | Record explicit owner canon decision and old-name aliases | Targeted documentation update |
| `episodes/S3E019.md` | Finale roundtable supplies retrospective context, unused GM prep and titles | **P1** | Nonplayed source reference only; no extra story arc | Inspected |

**Note:** `Khaervilon`, `The Principal`, `T'ietkalla` and `Or'Nath` are now *editorial canonical spellings* for clear referents; legacy file paths are intentional compatibility. Do not reclassify old source text as "corrected" or split one entity because an alias remains visible.

## 3. Domain-wide discovery leads (not certified missing entries)

| Category | High-value audit leads | Distinguishing check |
| --- | --- | --- |
| **Races** | Lizardfolk, Tieflings, Lactids, Harlequinari; possible elves, dwarves, orcs, illithids, pixies | Culture/species vs individual biography vs creature encounter; no unsupported universal attributes |
| **Places** | Planet Nash, Pentel Weiss, elven Mars sites, region-labeled map locations, Solar Mines subdivisions | Standalone location vs existing place section; map inscription date/extent unverified |
| **Characters** | Badass T, omitted minor allies/adversaries, reunions, family/final status | Last **actual** appearance vs secondhand reports |
| **Factions** | Council of Earthly Defenders, Council of Faces, Umbilical Order, Arcanum Universalis | Independent organization vs office/cult vs individual; played vs unused GM designs |
| **Events / history** | Elhandar disaster, Solar Mines war, Worldbreaker banishment, Earth restoration, old dragon-war accounts | Played outcome vs NPC testimony and creator hindsight |
| **Artifacts / technology** | Important early equipment, moving items and their final holders, late spells/technical devices | Possession, demonstrated effect, claim and potential planned use kept separate |
| **Specialist registers** | Vorel's full title list; Nash's improvised casting phrases beyond E111 | In-session quotation vs retrospective memory vs non-spell poem |

Before opening a new page, search the directory, source-keyed chronology, relevant episodes and naming aliases. Record `missing`, `underindexed`, `covered in existing page`, `potential duplicate`, or `not enough evidence`.

## 4. Initial verification queue candidates

Use existing [review queue](REVIEW_QUEUE.md) keys and [ledger](../world/CONSISTENCY_LEDGER.md). High-impact clusters: pact E022–E024; deaths and coronation E048–E054; Sira/CHIDS E066/E079–E081; divergent party E101–E116; vessel/prison S2E01–S3E03; final state S3E12–S3E18; nonplayed Round Up S3E019. Also inspect E000–E001 cosmological claims and targeted new Discord handouts. These are **leads**, not fresh validated errors or an exhaustive order-of-work.

## 5. Named-entity migration checklist (planning, not bulk rewrite)

| Canonical display | Legacy display/search alias | Stable path examples | Basis | Action |
| --- | --- | --- | --- | --- |
| **The Principal** | the Principle | `world/characters/the-principle.md` | Owner-approved Known Wastes map | Main prose migration pending; preserve one character ID and old path |\n| **Principal City** | Principle City | `world/PLACES.md` (index; dedicated page subject to evidence review) | City referred to in episodes; spelling follows owner-confirmed title, **not independently verified as a map-printed city label** | Normalize unambiguous live editorial compound; keep historical aliases and evidence classes distinct. [Audit](../reports/PRINCIPAL_RELATED_NAMES_AUDIT_2026-10-27.md) |\n| **The Principal's Lands** | Principle's Lands | `world/PLACES.md`, map register | Directly printed on the Known Wastes map | Keep distinct from Principal City's limits; do not invent coordinates or area identity |
| **Khaervilon** | Kervalon | `world/places/kervalon.md` | Owner-confirmed Known Wastes map | Main prose migration pending; preserve location ID and old path |
| **T'ietkalla** | Tietkalla, ASR alternatives | `world/places/tietkalla.md` | Known Wastes map and owner's canonical policy | Main prose migration pending; keep same place/kingdom identity |
| **Moag Ferhain** | ASR alternatives | existing chronology/name entries | Known Wastes map corroboration | Confirm exact entity locations before new page |
| **Ubere Mtaris** | ASR alternatives | existing indexes | Known Wastes map corroboration | Treat as labeled geography; scope uncertain |
| **Valiir Or'Nath** / **Stanley Billings** | historic Ornath-style surname; Stanley remains familiar name | `world/characters/stanley-billings.md` | Jon's poem and owner identity confirmation | One character with two supported names |
| **Delit Or'Nath** / **Villa Or'Nath** | Delit Ornath, Villa Ornath | `world/places/villa-ornath.md` | Owner-confirmed shared family spelling | Keep path and aliases; harmonize later prose |

A label's existence on an in-world map does not prove the party visited that location, that its name was known to them earlier or that the real-world illustration may be redistributed.

## 6. Preservation and completion tracking

For each bounded implementation batch:
1. Archive exact old bytes with hashes before any substantial rewrite and record paths in this manifest.
2. Record scene/page claims, old/new paragraphs, last-observation horizons and relevant original episode links.
3. Apply canonical names to newly authored prose and verified editorial replacements, **never** silently normalize `sources/`, historical quotations or old handout text.
4. Validate notes, links, inbound anchors and compatible slugs, compare source coverage, then run changed-file Markdownlint/diff checks as available.
5. Mark separate statuses for **structurally validated**, **fact reviewed**, **audio listened** and **accepted**; do not infer one from another.

**Planning checkpoint (2026-10-27):** This manifest records issues and scoped measurements only. Full census and machine-readable page-level baseline, archived originals for narrative rewrites, new Races pages, accepted arc boundaries and final integration remain **unstarted**.
