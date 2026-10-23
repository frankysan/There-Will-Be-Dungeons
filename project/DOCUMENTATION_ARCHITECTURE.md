# Documentation architecture — layered first and second arc consolidation

**Status:** Adopted for the first consolidation pass (2026-10-21); **Phases A–D implemented as first structural editorial passes**; audio verification and expanded secondary-entity review remain pending. **Scope:** *The Wastes* through corrected **E081**, including the two completed documented arc endings and separately indexed cast Q&As. A second consolidation after E081 applied the original four-layer model to the entire E055–E081 arc. This reorganizes **documentation**, not the source transcripts or the game world. The plan deliberately distinguishes what already exists from later migration tasks.

## Why the structure changes

The first research pass added episode-group appendices to `world/*.md` and the root README as new processed SRTs were reviewed. This preserves a valuable investigation trail but makes it hard to follow a person's life, a place's history, or the main story without reading repeated—and sometimes superseded—status updates. A reader should not have to reconcile the E048 report that Angelashi had died with her **directly observed survival in E054**, or confuse an E049 character's beliefs with the GM's post-arc explanation of Buttons' motivation.

Our goal is **one clear reader-facing account per purpose**, with linked evidence and without deleting the working research.

## Four document layers

| Layer | Primary purpose | Canonical location | Source/status rule |
|---|---|---|---|
| **1. Sources and research** | Keep machine transcripts, per-episode notes, Q&A reports, provenance, transcription experiments, original unresolved questions and the trail of editorial judgments | `sources/`, `episodes/E###.md`, `episodes/BONUS-*.md`, `reports/`, `research/legacy/` | Episode dossiers are **source-first research**, **not** finalized reader transcripts or a canonical encyclopedia. Historical snapshots are frozen, not active authorities |
| **2. World reference** | Answer **who/what/where**, with stable identities, concise subject-focused descriptions, status, relevant relationships and episode provenance | `world/` | Subject pages should reflect **the declared spoiler horizon**, cite episodes/Q&A, and separate witnessed events, GM exposition, claims, open identity questions and later revelations |
| **3. Narrative** | Offer a coherent, enjoyable **story-first account**, by arc and point of view, without repeating every investigatory caveat | `narrative/ARC_ONE.md`, `ARC_TWO.md` and the ongoing `ARC_THREE.md` | **A synthesis, not an audio-verified transcript.** No dialogue invented or quoted without confirmation. Explain later revelations as later revelations; reference dossiers for timestamps |
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

- **Immediate reader entry points**: repository [README](../README.md), [narrative index](../narrative/README.md), [Arc One](../narrative/ARC_ONE.md), [world index](../world/README.md).
- **Episode-specific research entry point**: `episodes/E###.md`, with `episodes/BONUS-2019-03.md` under its own namespace. Keep time-code tables and doubts here even if a world fact is later resolved.
- **World reference status**: `world/CHARACTERS.md` and `world/PLACES.md` are now **subject indexes** linked to `world/characters/` (10 profiles) and `world/places/` (5 major profiles). Their **former full append-only content is frozen** in `research/legacy/2026-10-21/WORLD_CHARACTERS.md` and `WORLD_PLACES.md`. **Phase C completed as a first pass**: `world/WORLD.md` is now the thematic world reference and `CHRONOLOGY.md` the unified E000–E081 event timeline. Their pre-rewrite details are preserved at `research/legacy/2026-10-22/WORLD_HISTORY.md` and `WORLD_CHRONOLOGY.md`. **Phase D implemented**: the active `CONSISTENCY_LEDGER.md` distinguishes open source questions from accepted decisions and later-episode resolutions; `project/REVIEW_QUEUE.md` is prioritized. Both full original records are preserved as `research/legacy/2026-10-22/WORLD_CONSISTENCY_LEDGER.md` and `PROJECT_REVIEW_QUEUE.md`, without audio verification.
- **Historical long-form README inventories** are copied into `research/legacy/2026-10-21/` before replacing their index pages. They are historical research snapshots; the new indexes and arc narrative are the preferred reading experience. Git history retains every original text revision.
- `world/entities.json` is **not** a synchronized canon catalog for every researched character yet; do not fill in aliases or biographies automatically from narrative synthesis.

## Target structure after further migration

```text
README.md                         Short project landing / navigation
narrative/
  README.md                       Narrative guide and spoiler horizons
  ARC_ONE.md                     Continuous first-arc history (E000–E054)
  ARC_TWO.md                     Completed second-arc story (E055–E081)
  ARC_THREE.md                    Initial, ongoing third-arc story (E082–E091)
  [future arc chapters]           Later arcs by played chronology
world/
  README.md                       Reference navigation, source tiers
  CHARACTERS.md                   Compact character index / overview
  characters/                     Focused linked character profiles (phased)
  PLACES.md                       Compact geography index
  places/                         Focused linked locations (phased)
  WORLD.md                        Thematic history, society, technology, magic
  CHRONOLOGY.md                   One unified timeline, separate historic claims
  CONSISTENCY_LEDGER.md           Active disagreements + resolution links
episodes/
  E000.md ... E054.md             Per-episode source-first research dossiers
  BONUS-2019-03.md                Q&A evidence; never E055
project/                          Decisions, guide, workflow, review queue, numbering
reports/                          Research and source comparison
research/legacy/                  Preserved original append-only research snapshots
sources/                          Immutable audio/ASR/reference material
```

This is a **target**, not a claim that every suggested subject subdirectory exists now. Prefer **stable, descriptive slugs** for added profiles. A single reference index must point to each profile, not duplicate a full biography.

## Reference-entry contract (next pass)

For a character/place/organization/artifact, use this consistent order:
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
| **A — architecture and first narrative** | Write this policy, a coherent [Arc One narrative](../narrative/ARC_ONE.md), a narrative index, brief root/world navigation, and frozen former index snapshots; mark remaining compendia transitional | Reader can follow E000–E054 without consulting every research appendix; every chapter links to supporting dossiers; no source files overwritten |
| **B — people and geography** | Consolidate **characters** and **places** by entity, starting with four PCs, Buttons, P0D, Angelashi, Tietkalla, Dusthill, Slavetown, Black Mine and Château Weir | Each has one usable reference entry; updates reference it rather than append duplicate episode paragraphs; no lost names/uncertainties |
| **C — thematic world and unified chronology** | Reorganize `WORLD.md` by history/politics/society/magic/technology; replace chronological additive blocks in `CHRONOLOGY.md` with a single linked timeline; archive originals | Time-of-knowledge, branch events, one-shots and claims remain distinguishable; repeated text demonstrably reduced |
| **D — editorial backlog and cleanup** | Split resolved decisions out of outstanding checks, ensure old backlinks/anchor links resolve, review provenance, reconcile remaining entities | No known broken local links; no source drift; targeted repository tests pass when code/generated files are modified |

## Post-E081 — second arc close and ongoing maintenance

The [second-arc consolidation report](../reports/SECOND_ARC_CONSOLIDATION_2026-10-22.md) applies the four-layer contract to **E055–E081**: a flowing [Arc Two narrative](../narrative/ARC_TWO.md), one compact [chronology](../world/CHRONOLOGY.md), thematic [world reference](../world/WORLD.md), [characters](../world/CHARACTERS.md) and [places](../world/PLACES.md), [current open questions](../world/CONSISTENCY_LEDGER.md), and a [prioritized audio queue](REVIEW_QUEUE.md). Full pre-rewrite copies are indexed in [research/legacy/2026-10-22](../research/legacy/2026-10-22/README.md).

**New arc practice:** The [initial Arc Three narrative](../narrative/ARC_THREE.md) covers **E082–E091 only** and is organized as connected story movements, not an episode-by-episode append-only file. Because this arc remains ongoing, **future chapters may be added or earlier chapters revised only when enough source-grounded connected developments justify them**. Do not use the title to assert a literal third in-world year; avoid projecting the arc's eventual ending. On an individual recording, update **that dossier and materially affected subject profiles** first. Extend the chronology compactly and open a stable issue only when needed. Do **not** append each episode's summary to all three world indexes, add a new chronology appendix for the same events, or keep a permanent one-episode review table once its details have an archived source. After a substantial arc has ended, consolidate the narrative as **one readable whole**, preserving a re-linked frozen copy beforehand.

**Preservation and integrity:** Every new snapshot's links must be rebased to remain usable from its archive directory; the unchanged historical text should remain findable. Distinguish *played* outcomes, **GM-declared cutoff status**, and unreliable **NPC/creator retrospective testimony**. **Consolidation is not audio verification**. Document-only edits must receive Markdown/link validation; any local code or generated-file changes also require the relevant passing tests.

### Safety of the migration

Before replacing any major source-linked working document: **save a frozen copy under `research/legacy/`**, verify new counterpart contains appropriate cross-references, check all relative links (and inbound anchors where practical), and report which portions remain unverified or unmigrated. Do not delete episode dossiers, overwrite raw SRTs, retroactively change the cast's words, or make narrative pages responsible for live continuity bookkeeping.

**Validation:** For document-only changes, validate Markdown structure, relative links and index consistency; run any applicable documentation tests available. If later work modifies **local code or generated files**, run the required relevant test suites before claiming completion.
