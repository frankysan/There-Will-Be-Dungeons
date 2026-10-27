# The Wastes — completed-campaign consolidation and cleanup plan

**Prepared:** 2026-10-27. **Status:** Planning baseline and preliminary repository audit; no narrative split, canon rewrite, full page census, audio verification or migration has yet been completed under this plan. **Story horizon:** The played campaign ends at [S3E18](../episodes/S3E18.md). [S3E019](../episodes/S3E019.md) is a separate post-campaign cast roundtable/Q&A, not an additional played chapter. All transcript-based findings retain their existing ASR-provisional limits.

This plan extends, rather than replaces, the ongoing [Wastes world arc cleanup](WORLD_ARC_CLEANUP_PLAN.md) and uses lessons from the [Delvers campaign cleanup](DELVERS_CAMPAIGN_CLEANUP_PLAN.md), [migration manifest](DELVERS_CLEANUP_MANIFEST.md) and [narrative chapter maps](DELVERS_NARRATIVE_CHAPTER_MAPS.md). Operational trackers: [Wastes manifest](WASTES_CLEANUP_MANIFEST.md) · [proposed chapter maps](WASTES_NARRATIVE_CHAPTER_MAPS.md) · [editorial guide](EDITORIAL_GUIDE.md) · [world style](WORLD_NARRATIVE_STYLE.md) · [decisions](DECISIONS.md).

## 1. Goal, scope and exclusions

Publish a coherent, source-linked **finished reading experience** for all of The Wastes: relatively short story-led narratives; a complete, subject-focused world encyclopedia; compatible navigation; and concise, actionable open evidence questions. Retain the full investigative record.

In scope:
- Reconsider the six existing `narrative/ARC_*.md` documents as a possible **10–20 played/introductory episodes per arc** structure, crossing season boundaries when warranted.
- Compare chapter reading weight and rebalance narrative prose (particularly the overgrown sixth arc), with a scene/paragraph coverage record before edits.
- Inventory `world/` for omissions in people, places, creatures, artifacts, events, historical background, factions, systems and **intelligent races**. Create the **Races** domain after its classification and source template are agreed.
- Review all existing world subject pages against their domain-specific prose contracts, current status, source notes, relationships, links and coverage horizon.
- Triage episodes and nonplayed retrospectives for bounded second research passes and original-audio/handout checks.
- Integrate authoritative new written spellings, preserve legacy aliases, and prevent speculative creator preparations from turning into played history.
- Reconcile the root and campaign navigation, chronology, entity index, decision history, active review queue and consistency ledger.

Out of scope for the planning phase: editing generated `sources/` transcripts; inferring audio-verification from two ASR systems; deleting provenance; committing private source image binaries; automatically renaming stable slugs; declaring contested lore settled; or rewriting the campaign merely because an episode's latest dossier reports a newer cutoff. Other campaigns remain separate realities.

## 2. Evidence-backed preliminary audit

The initial read-only repository inspection found:

| Subject | Current observation | Implication |
| --- | --- | --- |
| Narrative | `ARC_ONE`–`ARC_FIVE` are approximately 24–29k characters each; `ARC_SIX.md` is approximately **205k characters / 814 lines**, covering 12 Season Two and 18 played Season Three episodes | Arc Six is much larger; do not solve only by arbitrary word deletion |
| Existing divisions | Arcs One–Three span roughly 27 played/intro entries apiece; existing Arc Six spans 30; E101 is a shared in-recording boundary | Evaluate the **whole six-arc arrangement**, not just Arc Six |
| World subject files | Inspected directory listings contain **46** `world/characters/` entries (including specialist registers), **19** `places/`, **32** `creatures/`, **21** `technology/` | Significant coverage, but counts alone do not establish completeness or page quality |
| Active controls | `world/CONSISTENCY_LEDGER.md` approximately **312k characters** and `project/REVIEW_QUEUE.md` approximately **293k characters** | Separate actionable open questions from historical episode research without loss |
| Stale coverage | Root `README.md` still refers to S3E15 as latest in places; `world/WORLD.md` says E124; `PLACES.md`, `FACTIONS_AND_POWERS.md`, `ITEMS_AND_ARTIFACTS.md` indicate S3E15 | Reconcile *current* reading horizon with final S3E18; retain historical cutoff labels only in dated evidence |
| Names | Map/Discord material confirms owner-approved spellings; some working prose still uses previous forms | Centralize canonical orthography and manage a reviewed migration, not silent transcript edits |
| Entity index | `world/entities.json` is explicitly `pilot-seed`, primarily E000/E001 | Design a broader stable-ID coverage and relationship register |
| Creator retrospective | S3E019 discusses CHIDS design, unused Principal City/western dungeon, cast plans and alternative outcomes | Store as **retrospective and unused prep**, never played world history |

These measurements are **sampling/inspection findings**, not an exhaustive per-file manifest, word-count benchmark, link scan, or validation report. The pre-existing 85-page World Phase 0 inventory was recorded **before** subsequent creature and other page creation and must not be treated as a current full inventory.

## 3. Narrative architecture — proposed, not adopted

Use the [eleven-arc working crosswalk](WASTES_NARRATIVE_CHAPTER_MAPS.md) as a hypothesis. Boundaries should follow resolution, shifts of location, character choice and dramatic transition rather than recording/season labels. Eleven arcs, each approximately 10–20 entries, give the likely best reading balance; however, a scene-map review may alter titles or split points.

Particular safeguards:
- `E000` is the introductory source; count it openly, not as an unlabelled played session.
- `E013.5` belongs at its *fictional* point in the first arc, independent of release order.
- `E043` and `E127` are separate one-offs; `E107`–`E109` are the earlier-period Dunebreaker prequel; maintain separate access and historical placement.
- `E101` transitions within one recording at Hope's departure; one dossier supports both sides. Do not duplicate the scene.
- `S2E12` is a season ending, not necessarily a dramatic arc boundary; a proposed arc continues through `S3E03`.
- `S3E019` is nonplayed testimony and cannot extend the Wastes narrative.

**Decision governance:** D-042/D-043 record owner-approved continuity and the current canonical Arc Six arrangement. The new eleven-arc organization is **proposed for evaluation**, not yet an adopted replacement. On approval, write an explicit superseding decision, update navigation and retain old arc filenames as redirects or historical copies after assessing backlinks.

**Mandatory approval checkpoint:** Before *any* proposed cleanup edit that lacks a clear, applicable owner approval, stop the batch and request clarification/approval, identifying the exact change, affected files and evidence. A cleanup invocation or planning document does **not** imply acceptance of new arc boundaries, narrative rewrites, Races schema/content, canon judgments, renames, deletions or other undecided changes. Record the hold and preserve the current files; **do not continue with a different edit to bypass the unresolved decision**. Read-only investigation and preparing the decision package are permissible. Resume only upon explicit approval, and do not ask again for an already recorded authorization. See [the cleanup skill](../.agents/skills/twbd-wastes-cleanup/SKILL.md).

### Rebalancing method

1. Capture immutable pre-edit originals and hashes; enumerate headings, prose paragraphs, episode/dossier links, footnotes and incoming links.
2. Build a source-to-scene-to-chapter map, including multi-episode threads and endings. Identify unique scenes, testimony, private knowledge and unresolved outcomes.
3. Pilot one short and one dense proposed arc before applying a global chapter budget.
4. Use the existing **roughly 350–450 in-universe words per narrative chapter** as a *diagnostic*, not a target requiring padding. Typically six to nine chapters where narratively justified; measure per chapter, not per episode.
5. Preserve character agency, causal connections, necessary emotional aftermath, interesting small scenes and pivotal consequences. Relegate detailed combat order and exhaustive numerical mechanics to dossiers when prose does not need them.
6. Compare transformed text with old paragraphs and relevant evidence notes; trace every relocation or deletion of unique content. Revalidate cross-chapter knowledge boundaries and source footnotes.

Do not automatically map new arc IDs into subject histories until arc numbering is approved. A stable numeric file scheme (e.g. `ARC_01.md`–`ARC_11.md`) is an option, not an enacted path change.

## 4. World taxonomy, missing subjects and Races domain

The owner has requested a **Races** domain for intelligent peoples, complementing Characters (individuals), Creatures (non-intelligent creatures and monstrous forms), Factions (organized groups) and Places (locations). Provisional structure:
- `world/RACES.md`: compact index.
- `world/races/`: subject pages using the same source-footnoted, in-universe presentation, introduction → development → current status/lasting legacy contract.
- `world/ENTITY_SCHEMA.md` and future `entities.json`: extend allowed types to include a race/culture entity with stable ID, aliases and relationships, without breaking existing IDs.

**Initial candidates:** Lizardfolk, Tieflings, Lactids, Harlequinari; then assess elves, dwarves, orcs, illithids, pixies and other demonstrated intelligent peoples. A race entry should describe supported appearance, social structure, culture, habitat, historical relations and known members. It should not repeat Vorel's biography, Hope's character growth or one NPC's battle log. Avoid assuming a universal racial quality from one specimen, one homebrew player character or unsourced rulebook defaults. Harlequinari are explicitly a custom concept in episode research; never impose unsupported standard-D&D mechanics.

**Discovery targets, not certified omissions:** Planet Nash, Pentel Weiss, Mars settlements, minor Solar Mines facilities, Badass T and other late recurring individuals, the Council of Earthly Defenders, Council of Faces, Umbilical Order, Arcanum Universalis, the fall of Elhandar, Worldbreaker's banishment, Earth's restoration, item custody and older lost histories. Determine whether each is missing, underindexed, merged appropriately with another entry or adequately covered in the existing thematic reference before creating a duplicate.

**Creator-retrospective boundary:** The S3E019 account of Principal City, its three spires, underground Lactids, a western dungeon and unrealized railway is background on **unused preparation**. It does not establish a played visit, observed geography or survival of the Arcanum Universalis. Keep retrospective-only facts identifiable in footnotes or a distinct unused-material register.

## 5. Canonical naming and link compatibility

**Owner confirmation, 2026-10-27:** **The Principal** is canonical; **the Principle** is an incorrect earlier editorial/ASR form. **Principal City** (not *Principle City*) follows the ruler's canonical name; it is distinct from the map-printed **Principal's Lands**, and the city name has not independently been confirmed as a label on that particular map. [Targeted compound and related-entity audit](../reports/PRINCIPAL_RELATED_NAMES_AUDIT_2026-10-27.md). **Khaervilon** is canonical; **Kervalon** is an incorrect earlier form. The map also gives authoritative **T'ietkalla**, **Moag Ferhain**, **Ubere Mtaris** and **The Principal's Lands** (subject to the actual labels documented in the [map register](../reports/WASTES_KNOWN_MAP_ORTHOGRAPHY_2026-10-27.md)). A separate Jon-authored document and owner confirmation establish **Valiir Or'Nath** as Stanley Billings's original elven name, **Delit Or'Nath** as his father's name and **Villa Or'Nath** as the home.

Use canonical spellings in **all newly authored editorial prose**. During the cleanup, review and replace wrong *editorial* spellings in reader-facing documents where the referent is unambiguous, preserving original recording words, directly quoted historical source passages, title strings, historic frozen reports, source hashes, links and stable legacy file paths (e.g. `world/characters/the-principle.md`, `world/places/kervalon.md`, `world/places/tietkalla.md`, `world/places/villa-ornath.md`). These paths and legacy name strings are **aliases/compatibility**, not assertions that they remain correct display names. Preserve referent identity and document redirects if any file paths are later renamed. A written spelling decision does not independently verify how a performer pronounced the name.

Maintain [Editorial guide](EDITORIAL_GUIDE.md), [written-map report](../reports/WASTES_KNOWN_MAP_ORTHOGRAPHY_2026-10-27.md) and [decisions](DECISIONS.md) as authoritative spelling-policy entrypoints. Old contradictory *active* recommendations must be retired; older historical records remain unchanged and identified as superseded.

## 6. World article and source-review standards

Apply [D-037–D-040](DECISIONS.md), [World narrative style](WORLD_NARRATIVE_STYLE.md) and [reference template](WORLD_REFERENCE_PAGE_TEMPLATE.md):
- In-world main prose; no episode IDs, research-state banners, ASR timings or editor commentary in ordinary subject narrative.
- Introduce the subject at first encounter; follow **meaningful** changes, knowledge states and relationships; end in **Current status** (or **Lasting legacy** for historical studies). Do not back-project finale revelations.
- Different domain lens for individuals, peoples, places, factions, items, creatures and events. Characters emphasize temperament, motivation, changing bonds and agency. Do not substitute chronological combat recaps.
- Footnote substantive claims with source dossiers, source windows, original handouts, alternative spellings and explicit unverified limits. Preserve specialty registers (e.g. Nash's spell phrases, Vorel's titles), source-keyed chronology and operational ledgers as functional exceptions.
- Separate direct scene observation, GM exposition, NPC claim, player recollection, possible future, creator unused prep, and original-audio-verified wording.
- Compare every reference article's final condition and last actual observation; a character merely mentioned in the finale did not necessarily appear in it.

**Second-pass triage:** Prioritize significant identity, contract, chronology, custody or ending questions where listening or a recovered handout may materially change the account. Initial windows include E000–E001 prologue; E022–E024 pact; E048–E054 deaths/coronation; E066/E079–E081 CHIDS; E101–E116 split timelines; S2E01–S3E03 early space voyage; S3E12–S3E18 finale; and S3E019 retrospective wording. These are *candidates* from the existing [Wastes review queue](REVIEW_QUEUE.md) and [ledger](../world/CONSISTENCY_LEDGER.md), **not** an order to reanalyze every episode. Merge tasks into existing issue keys rather than inventing parallel backlogs.

For every completed check record episode, absolute audio time/cues, source identity and hashes, actual action taken (ASR comparison, listening, handout inspection), who verified it, date, affected articles, old/new interpretation, and limits. Inter-ASR text disagreement is **not WER or audio confirmation**.

## 7. Phases and acceptance gates

| Phase | Deliverable | Exit gate |
| --- | --- | --- |
| **0 — Detailed baseline** | Current full `/narrative`, `/world`, controls and research-link census, per-page manifest, old text hashes, section/paragraph lengths, incoming links, aliases, duplicate/coverage flags | Every in-scope page has purpose, priority, treatment and source horizon; check historic baseline vs current HEAD |
| **1 — Arc decision** | Eleven-arc scenario with episode/scene/chapter crosswalk, coverage map, comparative reading-weight estimates and alternatives | Boundaries justified; known one-offs/prequel/E101 handled; explicit owner decision before changing canonical structure |
| **2 — Narrative rollout** | Pre-edit archives, bounded chapter pilots, then all accepted arcs, compatible aliases | Unique scenes, causal sequence, source footnotes and in-world knowledge preserved; chapter length assessed, not mechanically imposed |
| **3 — Races + discovery** | Approved new index, template/schema updates, evidence-backed starter entries and world omission register | Intelligence/personhood/classification respected, no duplicate biographies, all sources linked |
| **4 — World rollout** | Domain-focused small batches of people, places, items, factions, races, creatures, events and history, with last-state checks | Each article passes its domain contract and provenance/links; previous bytes preserved |
| **5 — Research verification** | Focused source/handout/audio checks against existing open issue keys | No falsely resolved ambiguity; competing testimony and planned events remain distinguished |
| **6 — Campaign integration** | Navigation, timeline, ledger, queue, entity names, full terminal statuses, stable links and final validation | No stale *active* completion text, no known broken maintained links, all pages disposed as accepted/archive/exempt and unresolved questions visible |

Phases 3–5 can proceed in carefully scoped linked batches. Keep detailed report checkpoints (old/new source horizons, edits, hashes, links, test results, reviewer limits) as Delvers does. Run changed-file Markdownlint, link/anchor checks and diff whitespace checks when local tooling is available; distinguish performed checks from merely recommended checks. Do not run the full test suite unnecessarily.

## 8. Additional improvements to track

1. Create an **entity-and-relationship graph**: stable IDs, canonical names/aliases, first/last observation, kinship, membership, item custody and connected histories. Extend beyond the `entities.json` E000/E001 pilot.
2. Perform a **campaign-resolution sweep**: distinguish closed outcomes, missing observations, contested claims and intentional hooks (including the apparent second Nash after the finale).
3. Extract stale/historical per-episode notes from active ledgers/queues to preserved archives, while retaining durable current questions and original issue keys.
4. Complete **Vorel's title register** with the roundtable retrospective; resume **Nash's spell-phrase register** beyond the earlier E111 keyword-pass ceiling with exact source support.
5. Build a **cartographic crosswalk** for the owner-held Known Wastes v3 map and other artifacts; record labels, edition, source, regional inclusion and uncertainty, without inventing precision or distribution rights.
6. Introduce automated **coverage/index diagnostics** for canonical name drift, missing final states, broken footnotes, unresolved alias pointers and uncited high-impact claims. Tool checks are aids to editorial review, not proof of canon.
7. Separate **episode publication/recording order, fictional chronology, and when a fact became known**, with Dunebreaker and retrospective bonuses as explicit exceptions.

## 9. First implementation slice and scope record

This planning slice records the preliminary audit, proposal and owner-confirmed naming corrections. It **does not claim** to have completed Phase 0's exhaustive page-by-page machine manifest, conducted new transcript/audio comparisons, rewritten an arc, created new race subject articles, reconciled the full active ledger or run repository-wide tests.

**Next action:** Generate a complete current file/hash/link/paragraph baseline; construct a per-scene map for `ARC_SIX.md` plus an earlier arc; test whether eleven segments produce satisfying narrative closures; obtain the owner's explicit arc-boundary decision; and then implement a bounded preservation-verified rewrite pilot.
