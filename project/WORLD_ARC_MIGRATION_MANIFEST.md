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

