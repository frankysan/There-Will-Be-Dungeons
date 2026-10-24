# Documentation architecture — layered arc consolidation

**Status:** The four-layer editorial architecture was adopted 2026-10-21, consolidated through E081 and expanded again **2026-10-23** into a subject-centered encyclopedia with dedicated characters, places, artifacts, factions, antagonists and historical-event studies. **Current researched Wastes horizon: E118**, with E107–E109 independently placed as an earlier historical prequel and bonuses as commentary. Audio verification and secondary-entity review remain pending. This reorganizes **documentation**, not the source transcripts or the in-world canon.

## Why the structure changes

The first research pass added episode-group appendices to `world/*.md` and the root README as new processed SRTs were reviewed. This preserves a valuable investigation trail but makes it hard to follow a person's life, a place's history, or the main story without reading repeated—and sometimes superseded—status updates. A reader should not have to reconcile the E048 report that Angelashi had died with her **directly observed survival in E054**, or confuse an E049 character's beliefs with the GM's post-arc explanation of Buttons' motivation.

Our goal is **one clear reader-facing account per purpose**, with linked evidence and without deleting the working research.

## Four document layers

| Layer | Primary purpose | Canonical location | Source/status rule |
|---|---|---|---|
| **1. Sources and research** | Keep machine transcripts, per-episode notes, Q&A reports, provenance, transcription experiments, original unresolved questions and the trail of editorial judgments | `sources/`, `episodes/E###.md`, `episodes/BONUS-*.md`, `reports/`, `research/legacy/` | Episode dossiers are **source-first research**, **not** finalized reader transcripts or a canonical encyclopedia. Historical snapshots are frozen, not active authorities |
| **2. World reference** | Answer **who/what/where**, with stable identities, concise subject-focused descriptions, status, relevant relationships and episode provenance | `world/` | Subject pages should reflect **the declared spoiler horizon**, cite episodes/Q&A, and separate witnessed events, GM exposition, claims, open identity questions and later revelations |
| **3. Narrative** | Offer a coherent, enjoyable **story-first account**, by arc and point of view, without repeating every investigatory caveat | `narrative/ARC_ONE.md`, `ARC_TWO.md`, `ARC_THREE.md` and `ARC_FOUR.md` (completed at E101's departure) and ongoing `ARC_FIVE.md` | **A synthesis, not an audio-verified transcript.** No dialogue invented or quoted without confirmation. Explain later revelations as later revelations; reference dossiers for timestamps |
| **4. Editorial controls** | Decisions, workflow, source-tier policy, unresolved checks, numbering crosswalk and the consolidation migration plan | `project/` | `DECISIONS.md` for explicit resolutions, `REVIEW_QUEUE.md` for *open* checks, `EDITORIAL_GUIDE.md` for style; decisions never rewrite historical source files |

**Reader's authority order:** source recordings/audio (when actually listened to) and verified scene evidence, carefully identified GM/cast statements, processed episode SRT with uncertainty, supporting cast-written spellings, owner-confirmed editorial decisions, externally sourced fan references as lower-tier corroboration. For **orthography** an owner-confirmed spelling can be authoritative without verifying **spoken wording** or unrelated identities.

## Separation of clocks and evidence

1. **Release/archive order ≠ story time.** Corrected Wastes **E043** is a holiday one-shot and not in the main narrative; original publisher **55** is `BONUS-2019-03`, **not corrected E055**. E013.5 was released between E013/E014 but includes an **earlier in-world scene**.
2. **Played at the episode's cutoff ≠ known after subsequent revelations.** E048 directly rescues **Tedna and Bok Bok**; E050 kills **Tedna**; E054 directly finds **Angelashi alive**, despite an earlier report of her death. Preserve the original episode stopping points.
3. **Character testimony ≠ narrator-confirmed fact.** Treat Kefeli, Monsoon, Nobiery, Buttons, and others as speakers with possibly conflicting motives. Describe **GM-confirmed mechanics/events** separately from world-history assertions.
4. **Q&A retrospective intent ≠ scene knowledge or alternate plot.** Beau's Year One Q&A revelation that **Buttons loved Stanley** and intended to remove Diontalus via the Arcanum belongs to an attributed later commentary paragraph, not an E049 speech the characters heard.
5. **Future or unchosen material ≠ historical event.** Three-month downtime, magic-item purchases, unchosen chrome or pixie routes, vehicle upgrades and the next Jon-run mini-adventure are plans until played and sourced.
6. **Names have explicit provenance.** **Diontalus** is creator/owner accepted, **Eye of Groxl** owner-confirmed as the **one item** behind ASR `Grojil/Groxel`, and **Tietkalla** has contextual cast-written support. **Angelashi/Angel Ashi**, Nobiery and other disputed forms remain documented rather than silently normalized in source files.

## Canonical pages, transitional pages and archives

- **Immediate reader entry points**: repository [README](../README.md), [narrative index](../narrative/README.md), [Arc One](../narrative/ARC_ONE.md) and [Arc Two](../narrative/ARC_TWO.md), [world index](../world/README.md).
- **Episode-specific research entry point**: `episodes/E###.md`, with `episodes/BONUS-2019-03.md` under its own namespace. Keep time-code tables and doubts here even if a world fact is later resolved.
- **World reference status**: `world/README.md` now exposes seven reader-oriented categories; `CHARACTERS.md`, `PLACES.md` and `WORLD.md` are concise indexes/thematic overviews, linking to detailed profiles in `world/characters/`, `world/places/` and `world/technology/`. Antagonists, artifacts, factions and historical events have their own topical indexes; `CHRONOLOGY.md` retains the **single episode-ordered E000–E122 timeline**. The longer E118-era working versions of the three rewritten files are frozen in [the 2026-10-22 research archive](../research/legacy/2026-10-22/README.md), with links rebased. Earlier compendia remain in `research/legacy/2026-10-21/`; the E081-era history, chronology, ledger and review-queue archival snapshots are also retained. Nothing here implies audio verification.
- **Historical long-form README inventories** are copied into `research/legacy/2026-10-21/` before replacing their index pages. They are historical research snapshots; the new indexes and arc narrative are the preferred reading experience. Git history retains every original text revision.
- `world/entities.json` is **not** a synchronized canon catalog for every researched character yet; do not fill in aliases or biographies automatically from narrative synthesis.

## Current structure and expansion pattern

### Independent campaigns

The top-level `episodes/E###.md`, `world/` and `narrative/` conventions describe **The Wastes**. [Inverse](../inverse/README.md) and [Delvers](../delvers/README.md) are independent campaigns in their own realities; shared standards do not imply shared continuity.

**Delvers research, 2026-10-24:** its [documentation plan](../delvers/DOCUMENTATION_PLAN.md) applies the same four layers within `delvers/`: season-qualified episode dossiers, a subject-centered world reference with chronology and consistency ledger, story-first narrative arcs, and campaign-specific review controls. Its [source inventory](../delvers/SOURCE_INVENTORY.md) covers 37 available entries across seasons 1–3, including S2E00. **S1E01 now has a complete dual-ASR dossier, first supported world/reference pages and a narrative; the other 36 entries remain inventoried only.** Create further pages as played evidence supports them, rather than populating them from titles or handouts. Campaign-qualified comparison reports remain in shared `reports/`; the [Delvers queue](../delvers/REVIEW_QUEUE.md) owns its next episode, **S1E02**, without changing the Wastes pointer. Retain separate spoiler horizons, identities and source provenance throughout. Audio verification and the premiere's MP3/SRT clock mismatch remain open.

### Existing Wastes layout

```text
README.md                         Project navigation and research horizon
narrative/
  README.md                       Story-first entry point
  ARC_ONE.md ... ARC_FIVE.md      Completed arcs and ongoing Arc Five
world/
  README.md                       Seven top-level subject categories
  CHARACTERS.md                   People and allies index
  ANTAGONISTS.md                  Role-based rivals/antagonists index
  PLACES.md                       Location directory
  ITEMS_AND_ARTIFACTS.md          Relics and extraordinary devices
  HISTORICAL_EVENTS.md            Major events and historical studies
  FACTIONS_AND_POWERS.md          Organizations and contested powers
  WORLD.md                        Thematic world systems; no episode recaps
  CHRONOLOGY.md                   Detailed E000–E122 time-of-knowledge timeline
  CONSISTENCY_LEDGER.md           Open disputes and source-cutoff resolutions
  characters/                     One primary biography per substantial person
  places/                         One primary page per substantial location
  technology/                     Artifact and device studies
  HISTORY_*.md                    Focused event and ancient-history studies
episodes/
  E000.md ... E122.md             Source-first dossiers (with exceptions)
  BONUS-*.md                      Cast commentary, never played episodes
project/
  WORLD_REFERENCE_PAGE_TEMPLATE.md Editorial contract for all world pages
  DECISIONS.md, REVIEW_QUEUE.md   Accepted names and unresolved checks
reports/                          ASR and research comparison
research/legacy/                  Preserved, rebased historic working research
sources/                          Original/processed transcription material
```

Prefer **stable descriptive slugs**. A subject has one authoritative page and can be linked from several category indexes. **Stanley and Diontalus are distinct pages**: `world/characters/stanley-billings.md` is the canonical Stanley biography; `world/characters/diontalus.md` owns the archfey's agency, crimes and unresolved E059 crystal fate; `world/characters/stanley-diontalus.md` is only a backward-compatible navigation page; index entries should not duplicate the biography. New categories should be introduced only when they solve an actual navigation problem.

## Reference-entry contract

Large recurring collections may have a **separate linked subject register** rather than expanding the biography: [Nash's spellcasting phrases and rhymes](../world/characters/nash-spellcasting-phrases.md) owns that collection, with a short link from his profile and the character index. Keep source/cue provenance, confidence and distinct spoiler horizons on the register; do not duplicate its entries across reference and narrative pages.

Use [WORLD_REFERENCE_PAGE_TEMPLATE.md](WORLD_REFERENCE_PAGE_TEMPLATE.md) as the maintained page contract for people, places, organizations, artifacts and historical events. For a character/place/organization/artifact, use this consistent order:

1. **Name and aliases** (orthography/source and stable identity; no invented official title).
2. **Overview** in two or three concise paragraphs reflecting the specified spoiler horizon.
3. **Chronological development** as short linked milestones, **not** every transcript table row.
4. **Relationships and relevant mechanisms/ownership** with demonstrated-versus-claimed distinctions.
5. **Outstanding disputes** only where still unresolved, linking `CONSISTENCY_LEDGER.md` and `REVIEW_QUEUE.md`.
6. **Evidence links** to episode dossiers, the Q&A and appropriate cast-written/provenance decisions.

Narrative prose should not contain long repeated `source evidence status` disclaimers every sentence. Use one conspicuous **source-quality notice** per chapter, then subtle qualifications such as “Monsoon claimed” or “the group believed” where required.

## Migration sequence and acceptance criteria

| Phase | Actions | Done when |
|---|---|---|
| **A — architecture and first narrative** | Write this policy, coherent [Arc One](../narrative/ARC_ONE.md) and [Arc Two](../narrative/ARC_TWO.md) narratives, a narrative index, brief root/world navigation, and frozen former index snapshots; mark remaining compendia transitional | Reader can follow E000–E054 without consulting every research appendix; every chapter links to supporting dossiers; no source files overwritten |
| **B — people and geography** | Consolidate **characters** and **places** by entity, starting with four PCs, Buttons, P0D, Angelashi, Tietkalla, Dusthill, Slavetown, Black Mine and Château Weir | Each has one usable reference entry; updates reference it rather than append duplicate episode paragraphs; no lost names/uncertainties |
| **C — thematic world and unified chronology** | Reorganize `WORLD.md` by history/politics/society/magic/technology; replace chronological additive blocks in `CHRONOLOGY.md` with a single linked timeline; archive originals | Time-of-knowledge, branch events, one-shots and claims remain distinguishable; repeated text demonstrably reduced |
| **D — editorial backlog and cleanup** | Split resolved decisions out of outstanding checks, ensure old backlinks/anchor links resolve, review provenance, reconcile remaining entities | No known broken local links; no source drift; targeted repository tests pass when code/generated files are modified |

## Post-E081 — third arc close and ongoing maintenance

The [third-arc consolidation report](../reports/THIRD_ARC_CONSOLIDATION_2026-10-22.md) applies the four-layer contract to **E055–E081**: a flowing [Arc Three narrative](../narrative/ARC_THREE.md), one compact [chronology](../world/CHRONOLOGY.md), thematic [world reference](../world/WORLD.md), [characters](../world/CHARACTERS.md) and [places](../world/PLACES.md), [current open questions](../world/CONSISTENCY_LEDGER.md), and a [prioritized audio queue](REVIEW_QUEUE.md). Full pre-rewrite copies are indexed in [research/legacy/2026-10-22](../research/legacy/2026-10-22/README.md).

**New arc practice:** The [Arc Four narrative](../narrative/ARC_FOUR.md) now covers **E082 through Hope's actual departure in E101** and is classified as **completed at that in-recording boundary**. [Arc Five](../narrative/ARC_FIVE.md) **begins in the remainder of the same E101**, not E102. E101 is indexed in both narratives but remains **one source-first dossier**; the [2026-10-23 narrative consolidation](../reports/NARRATIVE_CHAPTER_BALANCE_2026-10-23.md) reshapes completed Arcs One–Four into eight main chapters each, with frozen, relinked copies of the changed narratives. Arc Four's narrative rewrite is complete; source listening and consolidation of other reference documents remain separate work. Both narratives are ASR-provisional. Do not use the title to assert a literal third in-world year; avoid projecting the arc's eventual ending. On an individual recording, update **that dossier and materially affected subject profiles** first. Extend the chronology compactly and open a stable issue only when needed. Do **not** append each episode's summary to all three world indexes, add a new chronology appendix for the same events, or keep a permanent one-episode review table once its details have an archived source. After a substantial arc has ended, consolidate the narrative as **one readable whole**, preserving a re-linked frozen copy beforehand. Aim for **about eight main chapters** in completed arcs, following meaningful story turns; prologues, epilogues and source notes are outside that count. Ongoing arcs may grow without that constraint until their ending is known.

**Preservation and integrity:** Every new snapshot's links must be rebased to remain usable from its archive directory; the unchanged historical text should remain findable. Distinguish *played* outcomes, **GM-declared cutoff status**, and unreliable **NPC/creator retrospective testimony**. **Consolidation is not audio verification**. Document-only edits must receive Markdown/link validation; any local code or generated-file changes also require the relevant passing tests.

### Safety of the migration

Before replacing any major source-linked working document: **save a frozen copy under `research/legacy/`**, verify new counterpart contains appropriate cross-references, check all relative links (and inbound anchors where practical), and report which portions remain unverified or unmigrated. Do not delete episode dossiers, overwrite raw SRTs, retroactively change the cast's words, or make narrative pages responsible for live continuity bookkeeping.

**Validation:** For document-only changes, validate Markdown structure, relative links and index consistency; run any applicable documentation tests available. If later work modifies **local code or generated files**, run the required relevant test suites before claiming completion.
