# World arc cleanup — Phase 0 inventory and migration manifest

**Date:** 2026-10-24. **Status:** All 85 `world/**/*.md` page outlines and length metadata read from the **connected dirty worktree**. **Migration not started.** Preparation for the [arc-structured cleanup](WORLD_ARC_CLEANUP_PLAN.md) with the agreed **introduction-time description → arc developments → latest status last** contract in [the page template](WORLD_REFERENCE_PAGE_TEMPLATE.md). This is a planning document, **not a canon source or exhaustive link-validation report**.

## Workspace and coverage baseline

- Git `main`, HEAD **`d9ff8e10a2092b81b8b985f9d7f110fcc868e2e4`**. **44 pre-existing visible changes** at the start of Phase 0, including staged, unstaged, combined (`MM`/`AM`) and untracked files. Do **not** reset, stage, or reconstitute a "clean" state over them. Working files may differ materially from this HEAD.
- Complete Markdown directory census using constrained `list_workspace` followed by permitted `read_workspace_file`: **42 character entries** (including 2 registers and 1 compatibility page), **18 places**, **11 technology/artifacts**, **14 top-level `.md` files**: **85 Markdown files**. `world/entities.json` is the **86th non-directory entry** and is outside this textual migration. The actual *creatures* category is only a separate proposed plan; `world/creatures/` does **not** currently exist in this inventory.
- Each Markdown file was opened for its outline and total line count; root `CONSISTENCY_LEDGER.md` has **572 lines** and was read for heading extraction with a 320-line viewport, **not inspected in its entirety**. The two longest registers were read through their ends for structural classification. Other inspected files were at or below their read limits. Line counts below are **read-time metadata**, not post-cleanup byte counts or hashes.
- Scoped searches across all **86 files** in `world/` found **zero literal links containing `nash-maggard.md#`, `elhandar.md#` or `mask-of-elton-iv.md#`**. An episode-scope search of 150 files also found zero `nash-maggard.md#`; a narrative-scope search of six files found zero `mask-of-elton-iv.md#`. A repository-root search is **truncated after 1,204 files / 33,814,992 bytes** and **must not be considered exhaustive**. No general Markdown link/fragment validator was run. Existing specialized register links to other anchored documents are recorded below.
- **Do not overwrite or shorten a single subject page yet.** An exact **working-tree pre-edit snapshot** must be created under `research/legacy/`, its links rebased and its contents read back before the corresponding replacement. **No such snapshots or local validation commands were created/run during this inventory.** If archival access is denied, defer that migration rather than repeat the earlier Arc Five preservation exception.

## Migration legend

**P1** = pilot or high-impact multi-arc rewrite; **P2** = later substantive arc/chronology cleanup; **P3** = compact single-arc page, handle opportunistically; **KEEP** = index, ledger, register, compatibility/redirect or technical reference where arc-biography template does not apply. `I→A→S` means *introduction-time overview → development by relevant arcs → current/last-observed status at end*. Skip empty arcs; append retrospective comments as attributed evidence **before** final status. **Do not move status of a later season into the opening prose**.

## Characters — 42 files (including two source registers and one compatibility page)

| File under `world/characters/` | Lines | Class | Proposed bounded action |
| --- | ---: | --- | --- |
| `alvert.md` | 15 | P3 | Single-appearance profile; check introduction and last-observed, no empty arcs |
| `angelashi.md` | 49 | P2 | Reorder Arc Two–Five developments, introduction before E128 Mars departure |
| `blood-skunk-hendrickson.md` | 15 | P3 | Arc Five introduction/acts; bonus separate |
| `bok-bok.md` | 41 | P2 | Chronological development, Squirts/Chunks conflict remains open |
| `buttons.md` | 21 | P2 | Year One Q&A revelation belongs after initial played history |
| `cerinthala.md` | 47 | P2 | Order E072–E075; avoid opening with disappearance outcome |
| `charles-dickens.md` | 13 | P3 | One-off context and last-observed |
| `dilenoria.md` | 25 | P2 | Introduction as pupil → betrayal/revealed agency in Arc Five |
| `diontalus.md` | 71 | P1 | Possession, extraction, separate archfey actions and E128 revival in correct arc sequence |
| `diptak.md` | 9 | P3 | Compact Razak Val chronology |
| `dr-spider.md` | 21 | P2 | Arc Five role vs E127 standalone professor; preserve separate identities |
| `emenil.md` | 27 | P2 | Introduction/Harbor ties → E123/E124 lake sequence |
| `follow-sira-rorf.md` | 45 | P2 | **Grouped profile**: retain distinct Follow/Sira/Rorf persons, later outcomes after early descriptions |
| `general-carthax.md` | 9 | P3 | Arc Five opponent; death/capture correctness |
| `henitar-grape.md` | 21 | P2 | E125 introduction, E126 fall, E128 execution **after surrender** |
| `hope-akmenos.md` | 91 | P1 | Five-arc biography; E101 split; Voice-private vs shared knowledge; status at end |
| `imprisoned-black-dragon.md` | 23 | P2 | E121 encounter → E122 death/heart, distinguish testimony vs seen |
| `kefeli.md` | 7 | P3 | Short earlier-arc appearance |
| `lyrielle.md` | 43 | P2 | E114 first introduction → birth/help → E128 Mars evacuation, commentary separate |
| `malhya.md` | 23 | P2 | Arc Five lake manifestation; observed healing vs cosmological testimony |
| `monsoon-cabbage.md` | 17 | P3 | Initial actions then E055 later reporting; do not confuse hearsay with observation |
| `nash-maggard.md` | 89 | **P1 PILOT** | Five-arc outline; **E126/E128 top insertions moved into Arc Five**, final rest/level 13 last |
| `nash-spellcasting-phrases.md` | 226 | **KEEP register** | Keep source-indexed identifiers; do not force biography or break NSP references |
| `nobieri.md` | 25 | P2 | First encounter before E123/124 updates; attributed ancient claims |
| `nothing.md` | 59 | P2 | Arc Four E084–E088 timeline; Q&A commentary outside played sequence |
| `omnom-cinderborn.md` | 25 | P2 | Earlier introduction → return E118 → E121 actual death |
| `orp.md` | 15 | P2 | Current death is **currently at top**; move to end after E014/E059/E062 sequence (not a redirect) |
| `p0d.md` | 15 | P3 | Death and spirit-afterlife cutoff order |
| `quizquaz.md` | 9 | P3 | Compact minor character |
| `soulbroker.md` | 27 | P2 | Early compact encounter/bargain → E128 claimed history and **witnessed** sky rift |
| `squirts.md` | 101 | P1 | Many reverse updates E084–E128; E111 death and E125 separate Hell body; E128 name conflict |
| `stanley-billings.md` | 95 | P1 | Split five-arc development correctly, E126/E128 from top to last arc, Diontalus separate |
| `stanley-diontalus.md` | 9 | **KEEP compatibility** | Preserve this file and its inbound links; canonical profiles remain separate |
| `steerious-business.md` | 11 | P3 | One-off appearance and Arc Five employer/role |
| `tedna.md` | 11 | P3 | Arc Two fate, later alternate Tedna not same individual |
| `the-principle.md` | 23 | P2 | Early reports vs visible appearances; Soulbroker's E128 claims after prior events |
| `the-voice.md` | 17 | P2 | Arc Four/Five relationship and E124 refused order, distinguish Hand and Eye |
| `tobacho-fleur.md` | 13 | P3 | Arc Four/Five contracts, present statements vs verified power |
| `tungsten-wheel.md` | 9 | P3 | Arc Five engineer **named but not located**, do not imply contacted |
| `tylander-sullivan.md` | 7 | P3 | Compact earlier-arc source |
| `vorel-titles.md` | 177 | **KEEP register** | Keep source-indexed title/epithet claims and identifiers; not five-arc biography |
| `vorel.md` | 95 | P1 | Five-arc chronology, no invented “king of space” conferral; title register separate |

## Places — 18 files

| File under `world/places/` | Lines | Class | Proposed bounded action |
| --- | ---: | --- | --- |
| `black-mine.md` | 21 | P2 | Introductory setting → lower depths, ending condition last |
| `chateau-weir.md` | 27 | P2 | First visit → interpretations/bonus after played encounter |
| `chids.md` | 89 | P2 | Already chronological E070–E081; compress episode-heading sprawl, preserve Drive cutoff |
| `dunebreaker.md` | 59 | P2 | **Historical prequel** E107–E109 in own chronological sequence, not Arc Five |
| `dusthill.md` | 25 | P2 | First visit then E059 return; initial mistaken state preserved |
| `elhandar.md` | 95 | **P1 PILOT** | Reverse E128→E116 heading run → initial station/biodome → Arc Five developments → current wreck/evacuation last |
| `gray-waste-and-pandemonium.md` | 27 | P2 | Arc Five travel in played order; separate locations kept distinct |
| `kaiser-casino.md` | 11 | P3 | Arc Five introduction and later encounters |
| `kervalon.md` | 64 | P2 | E065–E081 subsite chronology; avoid duplicating CHIDS |
| `leopold-facility.md` | 11 | P3 | Short place reference |
| `razak-val.md` | 50 | P2 | Arc Three introduction, Great Fang transfer and threat in sequence |
| `sigil.md` | 197 | **P1** | Large E083–E116 headings out of order; **high impact, after pilot** |
| `slavetown.md` | 27 | P2 | Initial coercion → later E058/59 accounts |
| `solar-mines.md` | 13 | P3 | Stable subject and source links |
| `the-harbor.md` | 39 | P2 | E117 founding → E123/124 → crash/deaths E126 → Mars departure E128 |
| `tietkalla.md` | 77 | P1 | Arc One/Two/Three/Five shifts, Hope's separate return and Carthax assault |
| `villa-ornath.md` | 29 | P2 | First home E115 → E118 study → E125 crash → E126 spelljammer → E128 cutoff |
| `white-tower.md` | 19 | P2 | Arc Four entry/siege → E101 in-recording departure |

## Technology and artifacts — 11 files

| File under `world/technology/` | Lines | Class | Proposed bounded action |
| --- | ---: | --- | --- |
| `book-of-adjacencies.md` | 17 | P2 | Discovery E118 and later notes, book's claims remain claims |
| `diontalus-ocarina.md` | 9 | P3 | Arc Five given, no proved activation |
| `eye-of-groxl.md` | 19 | P2 | Initial physical discovery/powers then later Malhya statements |
| `gem-of-tides.md` | 9 | P3 | Compact custody/source |
| `hand-of-the-voice.md` | 17 | P2 | Hand vs Eye/Fist, time-of-knowledge and later unperformed ring proposal |
| `henatar-guitar.md` | 15 | P2 | E126 temporary seizure → E128 Stanley's possession/benign strum |
| `mask-of-elton-iv.md` | 13 | **P1 PILOT** | Introduced E118, controls attempted E126, **never attuned/flown as of E128** |
| `nash-dragon-heart.md` | 35 | P2 | Manufactured implanted vs separate natural heart → Mars custody |
| `noble-speeder.md` | 27 | P2 | E123 use, E125 escape and E128 added set/ownership |
| `portal-device.md` | 47 | P2 | Arc Three constructed device behavior, one storyline vs planned uses |
| `traversal-drive.md` | 13 | P3 | Arc Three operation and status |

## Top-level world files — 14 Markdown files

| File under `world/` | Lines | Class | Treatment |
| --- | ---: | --- | --- |
| `ANTAGONISTS.md` | 28 | **KEEP index** | Short role-based links only; no duplicated antagonist history |
| `CHARACTERS.md` | 60 | **KEEP index** | Links to canonical profiles, categories; optional later browse-by-arc |
| `CHRONOLOGY.md` | 239 | **KEEP chronology** | Already split by arcs; single source-aware world event timeline |
| `CONSISTENCY_LEDGER.md` | 572 | **KEEP ledger** | Preserve issue IDs/status and E101 boundary; **separate audit** for stale headings/duplicates |
| `ENTITY_SCHEMA.md` | 17 | **KEEP technical** | Machine schema; no narrative rewrite |
| `FACTIONS_AND_POWERS.md` | 17 | **KEEP index** | Cross-links to organizations/powers without arc copies |
| `HISTORICAL_EVENTS.md` | 32 | **KEEP index** | Links to time-aware event studies |
| `HISTORY_ANCIENT_CATASTROPHE.md` | 17 | P2 | Study, not arc biography; sort testimony/recorded changes without false dating |
| `HISTORY_CHIDS_DRIVE.md` | 21 | P2 | Focused cross-arc event study, source-order rather than forced five arcs |
| `HISTORY_TIETKALLA.md` | 25 | P2 | Before-party history → later city changes chronologically |
| `ITEMS_AND_ARTIFACTS.md` | 33 | **KEEP index** | Short artifact links, not duplicates |
| `PLACES.md` | 59 | **KEEP index** | Short location links; avoid second chronology |
| `README.md` | 35 | **KEEP portal** | Seven existing categories; optional browse-by-arc crosswalk |
| `WORLD.md` | 52 | **KEEP thematic** | Setting systems and competing cosmology; not episode recaps |

## Pilot dependency and link/archival checklist

| Pilot | Current structure | Required preservation & source test | Planned first/last sections |
| --- | --- | --- | --- |
| [Nash](../world/characters/nash-maggard.md) | 89 lines, ten H2 headings, two **E128/E126 blocks prepended before first-appearance identity** | Archive **actual 89-line dirty-working copy**; map existing headings/inbound anchors, validate intro from E000/E001 as appropriate (not inferred from one heading), reconcile family/heart and source-indexed [rhyme register](../world/characters/nash-spellcasting-phrases.md) | **Introduction — at first appearance** → meaningful Arcs One–Five → **Current status at E128** |
| [Elhandar](../world/places/elhandar.md) | 95 lines, 15 H2 headings, **reverse E128 down to E116** before basic station description | Archive **actual 95-line dirty-working copy**; validate first real Elhandar scene from episode dossier, E125 collision vs E126 survival vs E128 refugee exodus | **Introduction — at first appearance** → Arc Five station/forest → **Wreckage + departing survivors at E128** |
| [Mask](../world/technology/mask-of-elton-iv.md) | 13 lines, 1 H2 section | Archive exact current working copy; verify E118 introduction/attributes vs E126 attempt; preserve ability/readout vs actually demonstrated effects | **Introduction — at discovery** → Arc Five tests → **Not fully attuned at E128** |

**Link observations:** Existing links *inside* two specialized registers target **other documents' fragments**, and must be retained/checkable: `nash-spellcasting-phrases.md` links to `project/EDITORIAL_GUIDE.md#nashs-spellcasting-phrases-and-rhymes-2026-10-23` and `project/REVIEW_QUEUE.md#nashs-spellcasting-phrase-register`; `vorel-titles.md` links to `reports/VOREL_TITLE_AUDIT_2026-10-23.md#source-windows-and-export-inventory`. No claim is made that these existing fragments were validated. `stanley-diontalus.md` is a **working, deliberately retained compatibility page**; repository-wide search found multiple inbound citations to it, including old episode dossiers. Do not remove it.

**Open Phase 0 gates before pilot:** (a) full repository-wide inbound link and anchor audit using an appropriate local runner, or a clearly documented narrower per-file check; (b) working-copy frozen snapshots with **relative links rebased**, verified via readback; (c) baseline diff scope and affected Markdown lint/test capability; (d) per-paragraph source mapping for pilot. The first migration must be bounded to **one file at a time**. **No subject pages were modified to produce this manifest.**

## Phase 1 pilot checkpoint — Nash Maggard (2026-10-24)

**Status: Nash profile reorganized and editorially checked; Elhandar and Mask of Elton IV not yet modified.** The original Phase 0 inventory above is retained as a **historical baseline**; between Phase 0 and this pilot the owner committed prior work, so the pilot's initial worktree was **clean at HEAD `15f229105a4a9d1f28586a9a030a762b0ab3d93f`**, rather than the earlier 44-change worktree. The pilot intentionally created only the Nash page edit and one archive, plus checkpoint documentation.

- **Exact working-copy freeze before editing:** [Nash pre-arc-reorganization archive](../research/legacy/NASH_MAGGARD_BEFORE_WORLD_ARC_CLEANUP_2026-10-24.md), **89 source lines** (23,920 text characters before link rebasing), created **before** replacing the original file. Archive content is identical except Markdown relative link destinations are **rebased for `research/legacy/`**. The archive was read back and matched the expected rebased text **exactly**. **80 link occurrences / 65 unique original destinations** were preserved. This is a pre-edit snapshot of the current, formerly clean worktree; it does not supersede older archives.
- **Primary initial-evidence check:** [E000 introduction](../episodes/E000.md) and [reader-edited transcription](../transcripts/E000.reader-draft.md) at ~00:03:49–00:07:00 show a scarred staff-carrying survivor leaving the Solar Mines/Blood Canyons, one impaired eye, regret and tentative hope. That **initial characterization** forms the opening; later dragon form, later families, E128 execution and finale status are **not front-loaded**.
- **Rewrite:** [Nash profile](../world/characters/nash-maggard.md), now **106 lines** (26,971 Markdown characters; **longer than before** by ~13%, because the first pilot prioritizes **faithful relocation plus a new introduction/current-status frame**, not aggressive shortening). Exactly five chronological `### Arc One–Five` sections, correct **E101 split** at Hope's departure; separate **Enduring relationships** and **creator/GM commentary**; the **final `##` section is E128 current status**. E125 unknown-after-impact, E126 enemy limp, E128 death are not collapsed; Ruby still unbuilt and the natural/engineered hearts distinct; NSP identifiers still use the existing phrase register. All **65 distinct old linked destinations** remain.
- **Relative link checks:** current page **92 relative link occurrences / 68 unique normalized destinations**; archived page **80 / 65**. The three new unique destinations are existing introductory/context records. Directory listings covering **all 150 episode files, 42 character entries, 18 place files, 11 technologies, 6 narrative pages, 98 reports, 19 pre-existing 2026-10-22 research archives and 19 project files** confirm referenced filenames exist. Four references to `world/` root entries were checked by direct read. No missing relative file targets in these checks. Inbound search for literal `nash-maggard.md#` found none in **all 86 world entries, 150 episode files and six narrative files**; project search only matched the manifest's literal audit text. This is **scoped target/anchor validation**, not a full repository-wide Markdown fragment crawler.
- **Readback:** new biography read back **character-for-character identical as a Unicode text string** to the authored replacement, with the intended final heading and all five arcs. No original episode transcripts, model exports or other world subject entries edited. **General Markdownlint/test suites were not run**: the connected tool supports bounded read/search/write and Git status, not arbitrary check commands.
- **Final worktree check:** Git status shows **10 visible changes**. These include five files from this Nash pilot/checkpoint (the Nash page, its frozen archive, this manifest, the cleanup plan, and the documentation architecture) plus **five unrelated documentation changes** (`README.md`, `narrative/ARC_FIVE.md`, `narrative/ARC_FOUR.md`, `narrative/README.md`, and `world/CHRONOLOGY.md`) that appeared after the pilot began and were **not edited by this pass**. Preserve them and do not reset or stage anything indiscriminately.

**Next:** Pilot **Elhandar** as a **separate** bounded page rewrite only after its own exact working-copy snapshot, introductory episode audit, inbound-link checks and readback. Then perform Mask of Elton IV likewise. Later review whether Nash's length should be reduced through dossier links without losing meaningful arc milestones; do not undo this preservation baseline.

## Phase 1 pilot checkpoint — Elhandar (2026-10-24)

**Status: Elhandar reorganized and the working-copy archive verified.** Nash and Elhandar pilots are complete; **Mask of Elton IV has not yet been migrated**. The prior pilot/Phase 0 sections remain historical baselines.

- **Pre-edit worktree:** `main` at `9fa7f81b75349324108d47e39980d53ddfca1e0b`, with **zero visible Git changes** before work. The owner's Nash pilot and other prior changes were already committed between turns. No existing unrelated changes were modified.
- **Freeze before edit:** [Elhandar pre-reorganization archive](../research/legacy/ELHANDAR_BEFORE_WORLD_ARC_CLEANUP_2026-10-24.md) preserves the **entire current 95-line page (22,316 characters before link rebasing)**. All **35 Markdown relative-link occurrences** were rebased for the `research/legacy/` location (archive length 22,409 characters); link target round-trip assertions succeeded. The archive was read back and **matched the rebased text character-for-character before rewriting**.
- **First encounter checked:** [E115 dossier](../episodes/E115.md) describes the **actual first physical docking at Elhandar**: a technological cylinder and living forest sphere, Rainbow Road, Admiral Chrysorius, the High Elf's welcome, working elven facilities and lakeside cottage. [E114](../episodes/E114.md) ends *before* docking. The introductory section now describes **that functioning refuge and initial knowledge only**, without announcing its later destruction. Names and ancient cosmological statements remain provisional or attributed.
- **Rewrite:** [Elhandar](../world/places/elhandar.md) is **120 lines / 26,083 text characters** (+~17% versus old; preservation-first pilot, not an aggressive shortening pass). Its structure is **introduction (E115)** → **one Arc Five development section (E115–E128) with five thematic chronological subphases** → **current status (E128) as final section**. All **15 original topical/episode sections' narrative paragraphs remain intact**, simply moved into played order with thematic grouping and a concise opening/latest-state frame. E125 ending at impact, E126 household survival and refugee deaths, and E128 rescue/heart recovery/Mars-bound departure remain distinguished. The **natural heart** is explicitly different from Nash's implanted engine; Ruby remains unbuilt and Mars arrival unobserved. No fictitious Arc One–Four Elhandar visits were added.
- **Preservation and link checks:** All **33 distinct original normalized relative link targets** remain in the revised page. The new page has **46 relative link occurrences / 37 unique normalized targets**. Readback of the new page matched authored text exactly. Scoped searches for literal `elhandar.md#` returned **no matches in 86 `world/` entries, 150 `episodes/` files or six narrative documents**; a project-scope match was audit text rather than an inbound anchor. Several high-value links (E115, E126, category/Harbor/chronology, E115 ASR report, review queue) were confirmed via direct read. **Validation is partial:** large directory listings were capped/denied, direct reads of the two E115 SRT sources were workspace-denied and a concurrent E128 file read was blocked by a tool check; those are not evidence of missing files. Original SRT links were **preserved unchanged**. The full repository-wide link/fragment crawler, general Markdownlint and source checks **have not been run**.
- **Worktree after subject edit and archive, before checkpoint documentation:** only two visible changes, the new archival Markdown file and `world/places/elhandar.md`. No transcript, `world/CHRONOLOGY.md`, or other subject file edited by this pilot; no commit/push.
- **Next pilot:** [Mask of Elton IV](../world/technology/mask-of-elton-iv.md), with its own pre-edit freeze, E118 introductory evidence, bounded source/link checks and final E128 not-yet-attuned status. Keep the same one-page-per-slice workflow. Consider **later condensation** of Nash/Elhandar profiles after the preservation-first structure is validated across all three types; do not sacrifice episode knowledge boundaries to shorten them.

## Phase 1 pilot checkpoint — Mask of Eltanfawr (2026-10-24)

**Status: artifact pilot completed. All three Phase 1 reference types (Nash, Elhandar, mask) have received preservation-first migrations.** Former status statements higher in this manifest describe the *earlier checkpoints* and are retained as historical audit entries.

- **Initial worktree:** clean `main` at `ef427ae1e978c27af1243f9e510d08057f74c564`. Exact source at [legacy mask slug](../world/technology/mask-of-elton-iv.md): **13 lines / 2,347 text characters** before modification. [Frozen original](../research/legacy/MASK_OF_ELTANFAWR_PRE_ARC_REORGANIZATION_2026-10-24.md) was created **first**, with all **nine relative Markdown link occurrences** correctly rebased from `world/technology/` to `research/legacy/`. Round-trip target comparisons had **zero errors**, and archive readback matched the rebased original **exactly**.
- **New owner spelling decision:** [D-036](DECISIONS.md) documents **Eltanfawr** as **owner-selected preferred orthography**, not audio-verified pronunciation. The single artifact has [canonical page](../world/technology/mask-of-eltanfawr.md), and [old Elton-IV slug](../world/technology/mask-of-elton-iv.md) is a **small compatibility reference** for existing inbound links/aliases, not a second item. Historic E118/E126 dossiers and ASR exports have **not** been modified.
- **Story-first page:** The canonical reference starts with Stanley's **E118 discovery** of an obsidian jeweled mask in his father's secret study, plus *Peer into Plurality* as **untested GM-described mechanics**; Arc Five development records **E126 actual wearing and failed lift command**, with purported vessel controls, and **E128 still incomplete attunement**. **Final H2 heading is “Current status — end of Season One (E128)”**. Stanley still has the mask; no completed spelljammer flight, shrinking or tested d20 effect. The distinct **four successful rests** versus **four consecutive nights** wordings remain an open source-check issue.
- **Cross-references updated:** Artifact index, world portal, Villa Ornath, Stanley/Hope, Book of Adjacencies, Arc Five narrative, thematic world overview and consistency ledger use the canonical display spelling/target where appropriate, while transcript-era names are preserved as source aliases. Original old-slug inbound links still resolve to the compatibility page.
- **Editorial and bounded validation:** Canonical page and compatibility page created/read back; key file targets (both mask pages, E118/E126/E128 dossiers, two relevant comparison reports, Book, Villa, Stanley, artifact index, ledger, review queue) were directly checked and **all responded**. Scoped `world/` search before migration found six references to the old mask slug and **zero literal `mask-of-elton-iv.md#` fragment references**; these were **not a full repository-wide crawl**. **Markdownlint, link/fragment crawler, original audio verification, and general tests have not been run.** No source transcripts changed and no commit/push. At the **final status inspection**, 33 visible worktree changes were present. A separate concurrent narrative-editing workflow has modified or created `narrative/ARC_ONE.md`–`ARC_FIVE.md`, narrative tooling scripts and `research/legacy/2026-10-24/` snapshots; those files are **not part of this mask pilot** (apart from this pilot's two targeted Eltanfawr spelling replacements in `narrative/ARC_FIVE.md`). **Do not attribute the entire 33-file status to the mask or reset those changes.** Targeted spelling consistency additionally touched `world/CHRONOLOGY.md` and `world/places/elhandar.md` after the initial checkpoint.
- **Next:** Phase 2 should address recurring core-character profiles in bounded one-page steps after per-page preservation and link scans; give priority to **Hope, Stanley, Vorel and Diontalus**. A later editorial refinement may consolidate overlong Nash and Elhandar copies without removing their evidence.

## New presentation gate for subsequent `/world` migrations (2026-10-24)

**Directive [D-037](DECISIONS.md):** The archive owner now requires the **main text** in ordinary world-reference pages to read as **in-universe narrative**, with no visible episode numbers, ASR alternatives, timing, editor disclaimers or research caveats. Cite and explain those details through **Markdown footnotes** adjacent to the supported story passages, with all note definitions after the **final substantive Current status section**. See [World narrative style](WORLD_NARRATIVE_STYLE.md) and [revised template](WORLD_REFERENCE_PAGE_TEMPLATE.md). In-world uncertainty and competing character accounts remain naturally attributed within the story; provenance and reconciliation issues belong in notes.

**Migration status:** Phase 1's **Nash, Elhandar and Eltanfawr** pilots were completed under the *earlier structural contract* and are **not yet compliant with this newer presentation rule**. Preserve their work and frozen source copies; schedule bounded second passes to move source apparatus to footnotes while retaining all relevant arc facts. The first future Phase 2 character migration (Hope, then other major characters) should implement the new style **from the start**. Keep **Nash's spellcasting-phrase register** and **Vorel's title register** in their existing source-indexed research form, along with functional indexes, technical schema and chronology/consistency records as applicable. Do not blanket-convert specialist registers.

**New acceptance check:** in the main prose and headings, zero episode-ID/range citations, ASR labels, question-mark spelling variants or out-of-world review notes; all crucial research/provenance claims remain traceable through **valid footnote markers and definitions**, and the **latest status remains the last narrative heading**. This checkpoint is a **plan/policy update**, not evidence that any world subject article has already received its second pass.

## Phase 2 presentation checkpoint — Nash Maggard (2026-10-24)

**Status:** [Nash Maggard](../world/characters/nash-maggard.md) is the **first of the three previously structured pilot pages to receive the D-037 in-universe narrative/footnote second pass**. [Elhandar](../world/places/elhandar.md) and [Mask of Eltanfawr](../world/technology/mask-of-eltanfawr.md) have **not** received this pass. No other world subject pages were edited in this task.

- **Before-edit worktree:** initial `main` HEAD `440d2f23ea5932d23a6aa8106994c5386bc49d54` with **12 visible pre-existing unrelated changes** (arc narrative balancing and its archives, `rebalance_narratives.py`, an existing manifest change). Those changes were left untouched. A concurrent external commit changed HEAD during the work; after Nash's edit the status was **two visible files from this pass**, the Nash page and its new archive, before this manifest checkpoint. Do not reset other workflows.
- **Working-copy archive:** [Nash before in-universe presentation pass](../research/legacy/NASH_MAGGARD_PRE_IN_UNIVERSE_PASS_2026-10-24.md) created **before** replacement. The source page was **106 numbered lines / 26,971 characters**. All **92 relative Markdown link occurrences / 68 unique targets** were rebased from `world/characters/` to `research/legacy/`; every round-trip destination was checked. Archive readback matched every **nonterminal content character and line**; the workspace write/read interface normalized away one terminal **empty line**, leaving **105 nonblank/content lines** rather than the initial 106 numbered lines. **No substantive content or link was lost**. This exact trailing whitespace difference is explicitly recorded rather than claiming byte-for-byte identity.
- **New narrative:** Rewritten biography now **23,817 characters**, with **14,320 characters of connected in-world main narrative** followed by 26 grouped Markdown source footnotes. Introduction represents Nash's original Solar Mines/Dusthill portrayal, followed by **five ordered arc subsections**, an enduring-relationships/abilities section and **`## Current status` as last substantive H2**. Crucial E125 crash uncertainty, E126 Henatar still alive, E128 execution after surrender, P0D/Squirts deaths, Hope's departure/reunion, Elhandar family evacuation, divergent infant-name/gender descriptions, natural-vs-engineered hearts and alleged Nash origins remain distinguished. Main prose contains **no `E###` identifiers, ASR labels, `GM`/player research terms or `(?)` spelling markers**.
- **Provenance and validation:** The new page read back **character-for-character**, 26 footnote references match **26 unique definitions**, with **zero missing/orphan notes**; **all 68 previous distinct normalized link destinations are preserved** and the **nine new destinations were checked by direct file read and found**. The general directory listing only returned the first 50 episode filenames, so its negative results for later-numbered episode files **are listing-limit artifacts, not broken links**. The earlier first pilot had checked old destinations. No full repository-wide fragment crawl, Markdownlint or general test runner was available through the connected workspace; **these checks have not been run**. Original transcriptions/episode dossiers remain unchanged, as do [Nash's spellcasting register](../world/characters/nash-spellcasting-phrases.md) and all other world subject pages. No commit or push performed.
- **Next:** Continue the presentation second passes **one page per turn**: **Elhandar**, then **Eltanfawr**. Preserve each page's **current** working copy before edits, even though earlier first-pilot archives also exist. Only after those three are complete should the Phase 2 core-character backlog (Hope, Stanley, Vorel, Diontalus) proceed under the updated style.

## Phase 2 presentation checkpoint — Elhandar (2026-10-24)

**Status:** [Elhandar](../world/places/elhandar.md) has completed its **D-037 in-universe narrative and footnote second pass**. Nash was completed previously; **Eltanfawr remains the one outstanding second-pass pilot**. This work modified no other world subject page.

- **Pre-edit baseline and archive:** `main` HEAD `cc7f039b233992f4c6ac5084ad6ef0017f4916ab` with **zero visible working-tree changes** before the pass. The then-current 26,103-character working page was confirmed against the pinned GitHub source and archived **before editing** as [Elhandar pre-in-universe pass](../research/legacy/ELHANDAR_PRE_IN_UNIVERSE_PASS_2026-10-24.md). All **46 relative link occurrences** were rebased without target changes. An independent binary readback proved the archive **byte-for-byte identical to the intended rebased copy** (SHA-256 `8d99cce78952a309382c0ab027edad84c04eb911addc96385f548049346ab085`, 26,360 bytes). A few large connector text reads were blocked, so pinned GitHub content was used **only after** clean Git-status confirmation.
- **Presentation rewrite:** Elhandar now opens as a real, working orbital forest sanctuary, then narrates its Arc Five history through **five story-focused internal subsections**: first days, Harbor/study, expedition/heart, audience/siege, wreck/departure. Its **final substantive heading is `## Current status`**, describing the fallen station, surviving ships and unresolved Mars arrival without out-of-universe interruption. The in-universe main prose contains **no E### identifiers, ASR/GM/player/transcript labels, speculative-spelling markers or episode ranges**. Witnessed events, participant testimony and plans are kept distinct. The two heart types are not conflated; Ruby remains unbuilt, and the giant burrower is not defeated.
- **Sources and checks:** The page uses **23 named Markdown footnotes**, with **23 references, no missing definitions and no unused definitions**. All **37 unique original link destinations were retained**; one additional internal artifact link points to the existing canonical [Mask of Eltanfawr](../world/technology/mask-of-eltanfawr.md). Readback via the workspace binary source verified the final heading, prose checks and note structure after replacement; the final minor wording adjustment (“Whether they have reached Mars safely remains unknown”) keeps the last section in-world. Previous E115 source-model exports remain cited in the notes without reprocessing.
- **Validation scope:** Bounded structural checks and link-set preservation completed. Full repository-wide broken-link/fragment scan, Markdownlint, canonical docs tests and independent audio listening **were not run**; don't claim those are green. No original episode/transcript/source document was modified and no commit/push occurred.
- **Next:** Process **Mask of Eltanfawr** as the **third presentation pass**, in a separately bounded turn with a fresh exact working-copy archive, footnotes and source checks; then begin Phase 2 major characters.

## D-038 character-biography balance and focus checkpoint (2026-10-24)

**Policy update only — no character page rewritten in this checkpoint.** The owner requested **more balanced prose across character arcs**, with greater attention to **personality, attributes, motives, relationships, allegiances, revelations and lasting change** than to a sequence of events. [D-038](DECISIONS.md) is now reflected in the [world narrative directive](WORLD_NARRATIVE_STYLE.md), [template](WORLD_REFERENCE_PAGE_TEMPLATE.md), [editorial guide](EDITORIAL_GUIDE.md) and [cleanup plan](WORLD_ARC_CLEANUP_PLAN.md). This is a **character-page requirement**, not a mandate to give place, item, chronology or specialist-register pages equal-length arc entries.

**Observed example — Nash current biography:** From the clean committed `world/characters/nash-maggard.md` read at `84e837296a7e4f3fb31b1c9f45bc0a16d37030f6`, simple prose-token counts excluding Markdown headings and footnote definitions give **Arc One ~78, Two ~131, Three ~243, Four ~175, Five ~1,051 words** (substantive-arc median ~175). These are approximate planning metrics, **not a semantic completeness test**. Arc Five is roughly six times the median, with much event-led battle/travel recounting. It is a **high-priority future rebalancing candidate**, but **do not rewrite Nash merely to hit an arbitrary quota or erase significant family/identity/reconciliation developments**. Source evidence in footnotes and existing archives must be retained.

**New acceptance criteria per major character:** record approximate **main-prose word counts by meaningful arc before and after**, excluding headings/footnotes; note whether a disproportionate arc (roughly >2× the median of comparable substantive arcs) has a justified cluster of **distinct character transformations**. In each major arc, identify supported **initial state → pressures/relationships/revelations → changed state**, with event summaries retained only when essential to those changes. Verify the main text remains in-universe, intro-time focused, chronological, with **current status last** and cited claims/uncertainties in valid footnotes. Preserve source links, disputed knowledge, aliases and agent distinctions. **Short arcs with little meaningful involvement do not require padding.**

**Rollout:** Apply D-038 to the next major biography (Hope, Stanley, Vorel, Diontalus) **from its first edit**. Schedule Nash's separate character-centered balance pass with a fresh pre-edit archive and one-file scope. Finish Eltanfawr's pending second presentation pass under D-037; **do not force artifact histories into character word-count proportions**.

## D-039 all-domain subject focus and proportionality checkpoint (2026-10-24)

**Policy update only — no `/world` subject pages rewritten here.** The archive owner extended the character-biography subject-focus principle to **all ordinary world-reference domains** while retaining different criteria for each. The [world narrative directive](WORLD_NARRATIVE_STYLE.md) and [template](WORLD_REFERENCE_PAGE_TEMPLATE.md) now specify the primary questions for **places, artifacts/technology, factions and institutions, historical events, thematic world studies**, and possible future creature pages; [D-039](DECISIONS.md) records the decision. Indexes, specialist registers, schemas, source chronologies, ledgers and redirects remain purpose-based exceptions.

**Migration acceptance for every ordinary subject page:** Record (1) the **domain-specific defining qualities** introduced without future spoilers; (2) meaningful changes by arc or thematic phase; (3) its latest condition, custody, reach, aftermath or legacy; (4) its **balance review**—whether disproportionately long sections explain truly major subject changes or merely replay scene chronology; (5) the retained provenance/links, source-tier boundaries and evidence footnotes. The character **150–300-word soft planning range does not apply** to places, technologies, factions or event/thematic studies. Short one-arc entries should remain short; no padding or empty arcs.

**Pending follow-up choices:** Nash needs its D-038 character-focused arc balance review. [Elhandar](../world/places/elhandar.md) has completed D-037 presentation but may need a **D-039 place-centered balance review**, emphasizing lived qualities of the station and its transformation rather than the party's full mountain expedition. [Mask of Eltanfawr](../world/technology/mask-of-eltanfawr.md) has a structural pilot and still needs its D-037 in-universe presentation pass; apply D-039 artifact focus in that same bounded task, emphasizing the mask's nature, custody, abilities and incomplete attunement rather than Stanley's surrounding travels. Other domains should follow the [Phase 3–4 cleanup plan](WORLD_ARC_CLEANUP_PLAN.md) with one large subject page per pass, verified working-copy snapshots and actual checks when available. No source transcripts or world canonical articles were modified for this policy checkpoint.

## D-038 Nash character-focused rebalancing — 2026-10-24

**Status: completed for [Nash Maggard](../world/characters/nash-maggard.md) only.** This is the implementation of D-038 after the prior D-037 in-universe presentation pass, not a new transcript review. At the beginning, `main` was clean at `e908edb7b1b05207e6de2c281af72fb0f0415f8e`. No other `/world` subject entries or source documents were edited.

- **Exact pre-edit working-copy preservation:** [Nash before character-focused rebalance](../research/legacy/NASH_MAGGARD_PRE_CHARACTER_FOCUS_2026-10-24.md). The 23,998-byte current biography was saved **before** the edit with all **111 relative Markdown link occurrences** correctly rebased; the archive was read back through the binary workspace interface, **byte-identical** to the expected rebased content (SHA-256 `6abaa0c03bd0076bdcac20acf54a3d3778f28627d6d5260aba488d1faca34902`). The earlier second-pass archive remains untouched.
- **Editorial changes:** Nash's biography now emphasizes a **solitary survivor developing loyalties**, P0D's loss and his attachment to Angelashi, anticipation of fatherhood, willingness to share the CHIDS beam, changing body and continuity of identity, the responsibilities and tenderness of family life, uncertain dragon-heart origins, and his conflicting **protective and lethal choices** (including the killing of surrendered Henatar). Retold travel, incidental battles and magic-by-magic sequences were substantially reduced; no additional psychological facts were invented.
- **Arc-length checkpoint (approximate main-prose words, excluding headings, link syntax and footnote references):**
  
  | Arc | Before | After |
  | --- | ---: | ---: |
  | One | 80 | **143** |
  | Two | 133 | **171** |
  | Three | 248 | **203** |
  | Four | 180 | **172** |
  | Five | 1,052 | **328** |

  Substantive-arc median after the revision: **172 words**; longest arc is **1.91×** the median (was ~5.8×). Arc Five remains longest for good reason: reunion with Angelashi, four children, Hope's return, revelation concerning Nash's manufactured nature, lethal choice at the station wreck and the painful Mars separation. No equal-length padding was used.
- **Source integrity:** All **77 original distinct Markdown link destinations** from the working copy were retained. The **26 named Markdown footnotes and their definitions were left unchanged**; there are **26 corresponding main-prose markers, no missing or orphan definitions**. The introduction still represents the first encounter, all five arcs remain sequential, and **Current status** is the last substantive heading. Main prose has **no E### identifiers, ASR/GM/player terminology or uncertain-spelling markers**. Final binary readback verified the revised document (SHA-256 `e2ea2f33640dddb990aea6df4bccfed317caa5781450211f05fe58e8454cb880`, 19,857 bytes).
- **Checks not performed:** No full repository-wide link/fragment crawl, Markdownlint, source tests or original-audio listening was available through the connected workspace. These are **not claimed as passing**. No commit or push was performed. Other profiles, including Elhandar and Eltanfawr, remain for their own subject-focused review.

**Next:** Resume the existing one-page-at-a-time world plan. Eltanfawr's in-universe artifact-focused second pass is still pending; Elhandar may later receive a separate place-focused proportionality review. Major-character passes (Hope, Stanley, Vorel, Diontalus) should follow this character study approach and each require their own preservation and citation checks.





