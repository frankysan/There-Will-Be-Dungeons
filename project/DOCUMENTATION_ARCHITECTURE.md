# Documentation architecture — layered arc consolidation

**Status:** The four-layer editorial architecture was adopted 2026-10-21, consolidated through E081 and expanded again **2026-10-23** into a subject-centered encyclopedia with dedicated characters, places, artifacts, factions, antagonists and historical-event studies. **Current researched Wastes Season One horizon: E128, its finale and the close of Arc Five**, with E107–E109 independently placed as an earlier historical prequel, E127 a separate one-off and bonuses as commentary. Audio verification and secondary-entity review remain pending. This reorganizes **documentation**, not the source transcripts or the in-world canon.

## Why the structure changes

The first research pass added episode-group appendices to `world/*.md` and the root README as new processed SRTs were reviewed. This preserves a valuable investigation trail but makes it hard to follow a person's life, a place's history, or the main story without reading repeated—and sometimes superseded—status updates. A reader should not have to reconcile the E048 report that Angelashi had died with her **directly observed survival in E054**, or confuse an E049 character's beliefs with the GM's post-arc explanation of Buttons' motivation.

Our goal is **one clear reader-facing account per purpose**, with linked evidence and without deleting the working research.

## Four document layers

| Layer | Primary purpose | Canonical location | Source/status rule |
|---|---|---|---|
| **1. Sources and research** | Keep machine transcripts, per-episode notes, Q&A reports, provenance, transcription experiments, original unresolved questions and the trail of editorial judgments | `sources/`, `episodes/E###.md`, `episodes/BONUS-*.md`, `reports/`, `research/legacy/` | Episode dossiers are **source-first research**, **not** finalized reader transcripts or a canonical encyclopedia. Historical snapshots are frozen, not active authorities |
| **2. World reference** | Answer **who/what/where**, with stable identities, concise subject-focused descriptions, status, relevant relationships and episode provenance | `world/` | Subject pages should reflect **the declared spoiler horizon**, cite episodes/Q&A, and separate witnessed events, GM exposition, claims, open identity questions and later revelations |
| **3. Narrative** | Offer a coherent, enjoyable **story-first account**, by arc and point of view, without repeating every investigatory caveat | `narrative/ARC_ONE.md` through `ARC_FIVE.md`, all five Season One arcs completed in eight main chapters; Arc Four and Arc Five share E101's in-recording boundary | **A synthesis, not an audio-verified transcript.** No dialogue invented or quoted without confirmation. Explain later revelations as later revelations; reference dossiers for timestamps |
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
- **World reference status**: `world/README.md` now exposes seven reader-oriented categories; `CHARACTERS.md`, `PLACES.md` and `WORLD.md` are concise indexes/thematic overviews, linking to detailed profiles in `world/characters/`, `world/places/` and `world/technology/`. Antagonists, artifacts, factions and historical events have their own topical indexes; `CHRONOLOGY.md` retains the **single episode-ordered E000–E128 Season One main-party timeline** (with E127 separately classified). The longer E118-era working versions of the three rewritten files are frozen in [the 2026-10-22 research archive](../research/legacy/2026-10-22/README.md), with links rebased. Earlier compendia remain in `research/legacy/2026-10-21/`; the E081-era history, chronology, ledger and review-queue archival snapshots are also retained. Nothing here implies audio verification.
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
  ARC_ONE.md ... ARC_FIVE.md      All five Season One arcs completed, eight chapters each
world/
  README.md                       Seven top-level subject categories
  CHARACTERS.md                   People and allies index
  ANTAGONISTS.md                  Role-based rivals/antagonists index
  PLACES.md                       Location directory
  ITEMS_AND_ARTIFACTS.md          Relics and extraordinary devices
  HISTORICAL_EVENTS.md            Major events and historical studies
  FACTIONS_AND_POWERS.md          Organizations and contested powers
  WORLD.md                        Thematic world systems; no episode recaps
  CHRONOLOGY.md                   Detailed E000–E124 time-of-knowledge timeline
  CONSISTENCY_LEDGER.md           Open disputes and source-cutoff resolutions
  characters/                     One primary biography per substantial person
  places/                         One primary page per substantial location
  technology/                     Artifact and device studies
  HISTORY_*.md                    Focused event and ancient-history studies
episodes/
  E000.md ... E124.md             Source-first dossiers (with exceptions)
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

**Planned larger cleanup (2026-10-24):** [World reference cleanup — arc-structured histories](WORLD_ARC_CLEANUP_PLAN.md) proposes reorganizing **material within the existing canonical subject pages** into concise, ordered Arc One–Five sections, starting with a read-only full inventory and a small preservation-verified pilot. The [Phase 0 manifest and pilot checkpoint](WORLD_ARC_MIGRATION_MANIFEST.md) inventory **85 world Markdown files** and document **completed Nash, Elhandar and Mask of Eltanfawr pilots**, each with pre-edit archives and bounded link checks. **Other world subjects remain unmigrated**, and the full repository-wide fragment scan/automated checks have not run. It keeps existing slugs, source tiers and the global chronology intact, and is separate from the [creatures/monsters category proposal](WORLD_CREATURES_PLAN.md).

Large recurring collections may have a **separate linked subject register** rather than expanding the biography: [Nash's spellcasting phrases and rhymes](../world/characters/nash-spellcasting-phrases.md) owns that collection, with a short link from his profile and the character index. Keep source/cue provenance, confidence and distinct spoiler horizons on the register; do not duplicate its entries across reference and narrative pages.

**Binding presentation directive for reader-facing `/world` documents:** [World narrative style](WORLD_NARRATIVE_STYLE.md). Use [the world-reference template](WORLD_REFERENCE_PAGE_TEMPLATE.md) for the article structure. **Main text must be in-universe and narrative-focused**, rather than recounting transcription work or episodic research. This applies to people, places, organizations, artifacts, historical studies and the thematic world guide.

1. **Introduction first:** Describe the subject broadly **as initially encountered**, without foreshadowing later deaths, discoveries or ownership transfers. Do not put episode numbers or ASR/citation-quality labels in an opening metadata banner.
2. **Development by arc:** Follow material developments chronologically in readable story prose. `Arc One` etc. are acceptable navigation headings, **but no episode-number ranges in headings or paragraphs**.
3. **Optional enduring relationships and mechanisms:** Describe in-world relationships and powers naturally; preserve the difference between performed acts and characters' claims or beliefs. Keep source-level mechanics in notes where possible.
4. **Current status last:** Finish with the latest **in-world** condition, whereabouts and open narrative questions. **This remains the final substantive heading** even when footnote definitions follow it; focused historical studies may instead end with **Lasting legacy**.
5. **Evidence in Markdown footnotes:** Put **episode IDs/times/dossier links, ASR uncertainties, alternative name spellings, audio-verification state, editorial comments, Q&A provenance, reviewed mechanics and unresolved source conflicts** in `[^note]` definitions at the bottom, referenced close to the supported prose. **No separate Sources/Notes heading after Current status**. Preserve enough citations and nuanced sourcing; removing a qualifier from the prose must not promote uncertain testimony into objective truth.
6. **Maintain links and exceptions:** Keep canonical slugs, aliases, inbound anchors and prior episode cutoffs. Purpose-built **[Nash phrase](../world/characters/nash-spellcasting-phrases.md) and [Vorel titles](../world/characters/vorel-titles.md) registers** retain episode/cue/source tables in their bodies; source-keyed chronology, consistency ledger, technical schemas, indexes and compatibility stubs may likewise keep functional metadata. The ordinary biographies and event studies **are not exempt** merely because they currently cite episodes inline.

**Character biographies have a separate editorial emphasis (D-038):** they explain **personality, motivations, relationships, beliefs/allegiances, attributes, revelations and lasting change**, rather than retelling episode events. For major recurring characters, aim for **reasonably balanced prose across substantively important arcs**, using a flexible **150–300-word starting range** per meaningful arc and reviewing sections above about **twice the median** of similarly important sections. This is a prompt to remove duplicated battle/travel summaries and deepen supported character analysis—not a quota or justification to pad minor arcs. The [world narrative style guide](WORLD_NARRATIVE_STYLE.md) and [character page template](WORLD_REFERENCE_PAGE_TEMPLATE.md) supply acceptance criteria. Keep historic and unverified motivations qualified rather than inventing interior thoughts.

**Domain-adapted focus and balance (D-039):** The character-first principle is now a **subject-first rule throughout ordinary `world/` reference pages**. Places emphasize physical/social identity and transformation; artifacts emphasize characteristics, custody, actual versus alleged powers and status; factions emphasize aims, organization, alliances and shifts in authority; historical events emphasize causes and lasting legacy; thematic pages emphasize systems and competing explanations. Evaluate **relative balance among comparably significant sections**, shortening duplicate scene recaps before essential subject-level information. The **character-specific 150–300 words** is not a universal target. A historical-event study may end in `## Lasting legacy` instead of `## Current status`. Follow [the domain-specific guidance](WORLD_NARRATIVE_STYLE.md) and [reference template](WORLD_REFERENCE_PAGE_TEMPLATE.md), maintaining the same footnote/source discipline.

**Rollout status:** Nash has completed D-037 and D-038, and **Elhandar has completed D-037 and its D-039 place-focused balance review**; [the migration manifest](WORLD_ARC_MIGRATION_MANIFEST.md) records preservation and validation. Eltanfawr still needs its pending D-037 presentation pass with D-039 artifact focus included. This does not imply that other world subjects already comply. These rules are adopted for subsequent edits and do not claim that all existing pages already comply.

## Migration sequence and acceptance criteria

| Phase | Actions | Done when |
|---|---|---|
| **A — architecture and first narrative** | Write this policy, coherent [Arc One](../narrative/ARC_ONE.md) and [Arc Two](../narrative/ARC_TWO.md) narratives, a narrative index, brief root/world navigation, and frozen former index snapshots; mark remaining compendia transitional | Reader can follow E000–E054 without consulting every research appendix; every chapter links to supporting dossiers; no source files overwritten |
| **B — people and geography** | Consolidate **characters** and **places** by entity, starting with four PCs, Buttons, P0D, Angelashi, Tietkalla, Dusthill, Slavetown, Black Mine and Château Weir | Each has one usable reference entry; updates reference it rather than append duplicate episode paragraphs; no lost names/uncertainties |
| **C — thematic world and unified chronology** | Reorganize `WORLD.md` by history/politics/society/magic/technology; replace chronological additive blocks in `CHRONOLOGY.md` with a single linked timeline; archive originals | Time-of-knowledge, branch events, one-shots and claims remain distinguishable; repeated text demonstrably reduced |
| **D — editorial backlog and cleanup** | Split resolved decisions out of outstanding checks, ensure old backlinks/anchor links resolve, review provenance, reconcile remaining entities | No known broken local links; no source drift; targeted repository tests pass when code/generated files are modified |

## Post-E081 — third arc close and ongoing maintenance

The [third-arc consolidation report](../reports/THIRD_ARC_CONSOLIDATION_2026-10-22.md) applies the four-layer contract to **E055–E081**: a flowing [Arc Three narrative](../narrative/ARC_THREE.md), one compact [chronology](../world/CHRONOLOGY.md), thematic [world reference](../world/WORLD.md), [characters](../world/CHARACTERS.md) and [places](../world/PLACES.md), [current open questions](../world/CONSISTENCY_LEDGER.md), and a [prioritized audio queue](REVIEW_QUEUE.md). Full pre-rewrite copies are indexed in [research/legacy/2026-10-22](../research/legacy/2026-10-22/README.md).

**New arc practice:** The [Arc Four narrative](../narrative/ARC_FOUR.md) now covers **E082 through Hope's actual departure in E101** and is classified as **completed at that in-recording boundary**. [Arc Five](../narrative/ARC_FIVE.md) **begins in the remainder of the same E101**, not E102. E101 is indexed in both narratives but remains **one source-first dossier**; the [2026-10-23 narrative consolidation](../reports/NARRATIVE_CHAPTER_BALANCE_2026-10-23.md) reshapes completed Arcs One–Four into eight main chapters each, with frozen, relinked copies of the changed narratives. Arc Four's narrative rewrite is complete; source listening and consolidation of other reference documents remain separate work. All five completed Season One narratives remain ASR-provisional. **Arc Five's owner-confirmed ending is E128**; do not infer Season Two events or assert a literal third in-world year from arc labels. On an individual recording, update **that dossier and materially affected subject profiles** first. Extend the chronology compactly and open a stable issue only when needed. Do **not** append each episode's summary to all three world indexes, add a new chronology appendix for the same events, or keep a permanent one-episode review table once its details have an archived source. After a substantial arc has ended, consolidate the narrative as **one readable whole**, preserving a re-linked frozen copy beforehand. Aim for **about eight main chapters** in completed arcs, following meaningful story turns; prologues, epilogues and source notes are outside that count. Ongoing arcs may grow without that constraint until their ending is known.

**Arc Five consolidation (2026-10-24):** [Eight-chapter narrative](../narrative/ARC_FIVE.md) and [audit](../reports/ARC_FIVE_CONSOLIDATION_2026-10-24.md) now close the **fifth and final Season One arc at E128**. Each of the 24 regular-story E101–E128 episode dossiers is linked; the historical E107–E109 prequel and E127 one-off are separate. **Exception to the preferred archival workflow:** no exact frozen copy of the dirty, 62-heading pre-consolidation working tree was saved before the edit; this is openly recorded in the audit. Do not mark that preservation gate as satisfied, and continue to use the episode dossiers for detailed evidence.

**Preservation and integrity:** Every new snapshot's links must be rebased to remain usable from its archive directory; the unchanged historical text should remain findable. Distinguish *played* outcomes, **GM-declared cutoff status**, and unreliable **NPC/creator retrospective testimony**. **Consolidation is not audio verification**. Document-only edits must receive Markdown/link validation; any local code or generated-file changes also require the relevant passing tests.

### Safety of the migration

Before replacing any major source-linked working document: **save a frozen copy under `research/legacy/`**, verify new counterpart contains appropriate cross-references, check all relative links (and inbound anchors where practical), and report which portions remain unverified or unmigrated. Do not delete episode dossiers, overwrite raw SRTs, retroactively change the cast's words, or make narrative pages responsible for live continuity bookkeeping.

**Validation:** For document-only changes, validate Markdown structure, relative links and index consistency; run any applicable documentation tests available. If later work modifies **local code or generated files**, run the required relevant test suites before claiming completion.
