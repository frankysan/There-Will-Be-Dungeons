# The Wastes — completed-campaign consolidation and cleanup plan

**Prepared:** 2026-10-27. **Current status (2026-10-30):** The eleven-arc edition and reader navigation are integrated; the source/link and bounded rendered-Markdown audits are complete under [D-078](DECISIONS.md)'s explicit browser-verification deferral. [D-079](DECISIONS.md) authorizes the subsequent narrative editorial cleanup, Git integration and publication/deployment workflow without per-chapter permission checks. **This document retains its October 27 preliminary observations as a historical planning baseline, not as assertions that migration is still pending.** The project is currently **private**. The immediate private-repository publication milestone was achieved by [merged PR #6](https://github.com/frankysan/There-Will-Be-Dungeons-Transcripts/pull/6) on 2026-10-30; no separate public website is required or deployed for this stage. Any later public-facing deployment must have a deliberately selected destination and distributable scope, without exposing the whole private research archive by default ([D-080](DECISIONS.md)). **Story horizon:** The played campaign ends at [S3E18](../episodes/S3E18.md). [S3E019](../episodes/S3E019.md) is a separate post-campaign cast roundtable/Q&A, not an additional played chapter. All transcript-based findings retain their existing ASR-provisional limits. **Active workflow (2026-10-31):** the [indexed task register](WASTES_CLEANUP_TASKS.md) alone owns completion checkboxes and the next action. Earlier planning pointers below remain historical, not live instructions.

This plan extends, rather than replaces, the [Wastes world arc cleanup](WORLD_ARC_CLEANUP_PLAN.md) and uses [Delvers methodology](DELVERS_CAMPAIGN_CLEANUP_PLAN.md). **Authoritative active tracker:** [Wastes cleanup tasks](WASTES_CLEANUP_TASKS.md). Supporting records: [artifact dispositions](WASTES_CLEANUP_MANIFEST.md) · [dated milestones](WASTES_CLEANUP_CHANGELOG.md) · [approved arc crosswalk](WASTES_NARRATIVE_CHAPTER_MAPS.md) · [editorial guide](EDITORIAL_GUIDE.md) · [world style](WORLD_NARRATIVE_STYLE.md) · [D-048 standard](READER_FIRST_PRESENTATION.md) · [owner decisions](DECISIONS.md).

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
- **D-048 reader-first consolidation:** audit and align active Wastes README/overview/index pages and ordinary world subject articles to story → setting/lore → history → closing project notes (indexes), or in-universe subject history → Current status/Lasting legacy → source footnotes (articles). Preserve newly owner-reworked entry points; remove front-loaded ASR, status and production apparatus without losing provenance or restoring removed image embeds.

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

## 3. Narrative architecture — eleven arcs integrated; historical design constraints

Use the [owner-approved eleven-arc crosswalk](WASTES_NARRATIVE_CHAPTER_MAPS.md) as the implementation baseline (D-045). The accepted episode/scene boundaries follow resolution, shifts of location, character choice and dramatic transition rather than recording/season labels. The detailed chapter beats, placement of supplemental E013.5 scenes, titles and source-footnote assignments still require traceable verification; **do not change an accepted arc boundary without a fresh owner decision**.

Particular safeguards:
- `E000` is the introductory source; count it openly, not as an unlabelled played session.
- `E013.5` belongs at its *fictional* point in the first arc, independent of release order.
- `E043` and `E127` are separate one-offs; `E107`–`E109` are the earlier-period Dunebreaker prequel; maintain separate access and historical placement.
- `E101` transitions within one recording at Hope's departure; one dossier supports both sides. Do not duplicate the scene.
- `S2E12` is a season ending, not necessarily a dramatic arc boundary; a proposed arc continues through `S3E03`.
- `S3E019` is nonplayed testimony and cannot extend the Wastes narrative.

**Decision governance:** **D-045 approves the eleven-arc episode boundaries; D-049 (owner-approved policy A, 2026-10-28) fixes `narrative/ARC_01.md`–`ARC_11.md` as the future canonical filenames and requires all six original word-form arc files to remain byte-preserved, readable at their existing paths.** D-042/D-043 remain historical records of the completed six-arc implementation, including continuity across the Season Two finale, not authority to retain six arcs in the final migration. Do not update canonical reading navigation or rewrite existing arc files until archived originals, source-to-scene coverage and compatibility links are validated. Retain all six legacy arc filenames as permanently readable, unchanged historical first-edition files; keep both seasonal compatibility stubs, and switch public Wastes/narrative/world navigation only after all eleven new arcs are independently accepted, with a visible legacy-edition section.

**Approval and editorial autonomy (D-047/D-048):** D-048 already authorizes the **reader-first presentation standard** throughout the project; D-047 authorizes unambiguous minor spelling, formatting and non-semantic copyedits without per-edit approval. These are not new owner approval gates. **Substantive or ambiguous changes**—scene/narrative rewrites, newly adjudicated canon, race schema/classification decisions, changes to accepted arc boundaries, identity merges, renames/deletions, source quotation changes or meaningful source-evidence reinterpretation—still require explicit applicable approval and bounded preservation. Stop and document a genuine unapproved substantive dependency instead of circumventing it with unrelated work; read-only planning remains permissible. See [the cleanup skill](../.agents/skills/twbd-wastes-cleanup/SKILL.md) and [D-048 rules](READER_FIRST_PRESENTATION.md).

### Rebalancing method

1. Capture immutable pre-edit originals and hashes; enumerate headings, prose paragraphs, episode/dossier links, footnotes and incoming links.
2. Build a source-to-scene-to-chapter map, including multi-episode threads and endings. Identify unique scenes, testimony, private knowledge and unresolved outcomes.
3. Pilot one short and one dense proposed arc before applying a global chapter budget.
4. Use the existing **roughly 350–450 in-universe words per narrative chapter** as a *diagnostic*, not a target requiring padding. Typically six to nine chapters where narratively justified; measure per chapter, not per episode.
5. Preserve character agency, causal connections, necessary emotional aftermath, interesting small scenes and pivotal consequences. Relegate detailed combat order and exhaustive numerical mechanics to dossiers when prose does not need them.
6. Compare transformed text with old paragraphs and relevant evidence notes; trace every relocation or deletion of unique content. Revalidate cross-chapter knowledge boundaries and source footnotes.

The numeric arc filename policy is **approved as D-049**, but the new paths have **not** been created or published. Do not point world/subject histories at nonexistent new arcs. Complete the source-backed eleven-arc pages and verify compatibility, then migrate all reader-facing navigation together; substantive story rewriting still requires separate approval.

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

## 6A. D-048 reader-first consolidation — required during Wastes cleanup (2026-10-28)

**Decision and status:** The owner reworked the archive's README/index entry points and removed displayed illustrations from [Dusthill](../world/places/dusthill.md) and [Fate 4](../world/technology/fate-4.md). Treat these as **current editorial direction**, not permission to restore imagery or replace recently revised prose. [D-048 presentation standard](READER_FIRST_PRESENTATION.md) applies now; **page-by-page convergence remains to be inventoried, migrated and validated**. The completed small canonical-name corrections in the [Wastes manifest](WASTES_CLEANUP_MANIFEST.md) do not by themselves satisfy this structural/presentation pass.

**Integrate into Phase 0, Phase 4 and Phase 6 rather than launching an unrelated rewrite:**

1. **Reader-entry and index inventory (Phase 0):** Assess `README.md`, `wastes/README.md`, `narrative/README.md`, `world/README.md`, `world/CHARACTERS.md`, `ANTAGONISTS.md`, `CREATURES_AND_MONSTERS.md`, `PLACES.md`, `ITEMS_AND_ARTIFACTS.md`, `FACTIONS_AND_POWERS.md`, `HISTORICAL_EVENTS.md`, `WORLD.md`, and their relevant history/subject directories. Distinguish the shared root portal (coordination with other campaigns) from Wastes-only content. Record each page's **purpose, active-vs-historical status, reader-first compliance, metadata above the narrative, research footnotes, legacy anchors/links, artwork embed state, exceptions, and migration priority**. Do not call a 2026-10-28 owner-reworked page deficient merely because it differs from a generic template.
2. **Navigation/overview treatment (Phase 4 / integration):** Lead with a short accessible in-world description; put story/arc reading routes, world/characters/places/lore, and history/turning points **before** research provenance, verification limits, project decisions, indexes of files and production metadata. Place the latter in **`## Sources and project notes` at the bottom**. Present reader-friendly subjects/relationships, not ASR confidence and episode IDs as the principal index columns. Keep navigation complete and the root/other-campaign boundaries intact. If an index has a legitimate reference-register role, identify its exception instead of deleting essential data.
3. **Ordinary world subjects (Phase 4):** Consolidate the material into **subject identity/introduction → relevant change and historical development → latest known in-world status or lasting legacy**. Preserve source-aware scene chronology and character-specific personality/relationships. Move raw episode numbers, transcript/run comparisons, verification status, editorial asides and illustration-production detail into **linked Markdown footnotes**, leaving natural *in-world* attributed doubt in the story. Do not turn a place, object, person or race article into a second full arc recap.
4. **Artwork and evidence boundaries:** **Never re-add** the owner-removed Fate 4 or Dusthill image embeds by following old templates. Review now-unreferenced `[^illustration]` notes as **provenance maintenance**, not a reason to display an image or erase approved production history. Other imagery is optional and requires intentional page-level selection, rights/source checks and separation from fact evidence. Raw ASR, episode evidence dossiers, source catalogs, specialist registers, consistency ledgers, and technical schemas remain purpose-built **evidence-first exceptions**; don't force their diagnostic body fields into fiction.
5. **Bounded execution and acceptance:** Group related short pages when safe; preserve exact current working-copy originals and inbound anchors before substantial reordering. Compare section hierarchy, unique claims, footnotes, links/fragments, canonical aliases, chronology and last observation. Record **task acceptance and validation once against a WCL ID** in the [task register](WASTES_CLEANUP_TASKS.md), not three batch recaps. Update the [manifest](WASTES_CLEANUP_MANIFEST.md) only for artifact disposition/compatibility and the changelog only for a significant milestone/decision. Run targeted lint, rendered-link and diff checks when available, without claiming unrun tests.

**Wastes-specific dependencies (updated from initial planning):** The eleven-arc edition is already integrated privately ([WCL-002](WASTES_CLEANUP_TASKS.md#wcl-002)); the two-article Races and entity-v2 pilot is also in place ([WCL-009](WASTES_CLEANUP_TASKS.md#wcl-009)–[WCL-011](WASTES_CLEANUP_TASKS.md#wcl-011)), but further peoples remain open. Do not rewrite stable legacy arc routes or claim public deployment. The root archive's revised portals are preservation baselines, not automatic replacement targets. Keep S3E18 played ending distinct from S3E019 commentary and prequel/one-shot chronology.

**D-048 presentation scope is owner-approved; D-047 minor corrections may be applied directly.** Escalate genuine ambiguous canon, material narrative/structural changes, path/anchor removals, authorial quote changes, or new taxonomy decisions under their existing approval rules.

## 7. Phases and acceptance gates

| Phase | Deliverable | Exit gate |
| --- | --- | --- |
| **0 — Detailed baseline** | Current full `/narrative`, `/world`, controls and research-link census, per-page manifest, old text hashes, section/paragraph lengths, incoming links, aliases, duplicate/coverage flags; **D-048 page-purpose, first-screen, reader-vs-research-content, illustration embed and footnote/last-section findings** | Every in-scope page has purpose, priority, reader-first disposition, treatment and source horizon; check historic baseline vs current HEAD |
| **1 — Arc decision** | Eleven-arc scenario with episode/scene/chapter crosswalk, coverage map, comparative reading-weight estimates and alternatives | Boundaries justified; known one-offs/prequel/E101 handled; explicit owner decision before changing canonical structure |
| **2 — Narrative rollout** | Pre-edit archives, bounded chapter pilots, then all accepted arcs, compatible aliases | Unique scenes, causal sequence, source footnotes and in-world knowledge preserved; chapter length assessed, not mechanically imposed |
| **3 — Races + discovery** | Approved new index, template/schema updates, evidence-backed starter entries and world omission register | Intelligence/personhood/classification respected, no duplicate biographies, all sources linked |
| **4 — World rollout** | Domain-focused small batches of people, places, items, factions, races, creatures, events and history, with last-state checks **and D-048 narrative-first presentation/footnote consolidation** | Each ordinary article finishes in in-world current status/legacy with supporting footnotes, retains subject facts and provenance/links, and has preserved original bytes or an explicitly justified exception |
| **5 — Research verification** | Focused source/handout/audio checks against existing open issue keys | No falsely resolved ambiguity; competing testimony and planned events remain distinguished |
| **6 — Campaign integration** | Navigation, timeline, ledger, queue, entity names, full terminal statuses, stable links and final validation; **D-048 reader-first checks of root/Wastes portals and all active subject indexes** | Story/world/lore/history precede final Sources and project notes; no stale *active* completion text or known broken maintained links; every page has a presentation disposition (accepted, pending, retained-exception) and unresolved questions remain visible |

Phases 3–5 can proceed in carefully scoped linked batches. **Record progress and validation in one WCL checkbox entry** rather than parallel progress/manifest/changelog summaries. Reports remain for independently useful source research. Run scoped Markdownlint, link/anchor and whitespace checks where available; distinguish performed checks from recommended checks. Do not run the full test suite unnecessarily.

### Adaptive, multi-file cleanup cohorts (D-082, owner approved 2026-11-01)

The owner explicitly replaced the former highly conservative review cadence with
**larger, adaptive batches**, to reduce repetitive reads, validations and
task-register edits while keeping the per-file evidence contract. The
2026-10-27 **4–8 short / 2–4 medium / 1–2 large file** and **300–400 line**
pilots are superseded **for active selection**, but remain historical context;
the older Batch 15 plan is not a live next-action pointer. The [cleanup
skill](../.agents/skills/twbd-wastes-cleanup/SKILL.md) governs execution,
[recovery instructions](../.agents/skills/twbd-wastes-cleanup/references/progress-and-recovery.md)
govern interruption, and the [WCL task register](WASTES_CLEANUP_TASKS.md)
owns statuses and the next action.

| Source/work type | Typical compatible files or tasks per execution |
| --- | --- |
| Short character, creature and technology articles | **10–15 files** |
| Medium world-reference or narrative articles | **5–8 files** |
| Large biographies, source-dense registers or long documents | **1–3 files**, with internal checkpoints as needed |
| Several low-risk related editorial WCL tasks | Group if common evidence, approvals and validations permit |

For ordinary light-to-medium review, plan **about 800–1,500 combined source
lines when practical**, not as a target to fill: a batch of 10 tiny pages
may total fewer, and a very long technical register may need its own
chunked audit. Preflight current line counts/bytes, provenance, link/footnote
density, dependencies, approvals and context/tool limits. Start with the
authoritative WCL anchor; a small lookahead may add related eligible
**pending** files or independent tasks when the **exact chosen paths and
WCL IDs** are recorded. The existing anchor's named files remain required.
No speculative source expansion or checkbox completion from a preflight.

Read and validate in **bounded waves**, not one huge response. Store
**individual** source horizons, D-048 dispositions, link/fragment counts
and limits, footnotes, hashes, incoming samples and caveats in the
[146-path current world census](WASTES_WORLD_FILE_CENSUS.json) or owning
WCL entry. Check off each WCL task **independently** only after all its
required outputs have been read back and validated. At the end of a
coherent batch, reconcile census totals and update **one** next-action
pointer in the task register; avoid appending duplicate manifest,
changelog and progress reports. On an interrupted operation or a blocked
check, retain verified per-file work, leave incomplete acceptance pending,
and resume only the uncertain part. Any renderer or safety limit must be
recorded literally and must not be bypassed.

**This is an efficiency decision, not relaxed verification or added
substantive authorization.** Preserve one exact baseline before a major
rewrite (D-052), original source/ASR and episode knowledge boundaries,
D-048 reader-first distinctions, owner D-081 boundaries and D-078's
browser deferral. Do not infer audio validation, native-browser pass,
canon certainty, commits, public deployment or publication. Coverage
remains per **unique current file**, not per batch. The immutable
2026-10-27 134-file worklist records a historical baseline; live counts
come only from the current census.

## 8. Additional improvements to track

1. Create an **entity-and-relationship graph**: stable IDs, canonical names/aliases, first/last observation, kinship, membership, item custody and connected histories. Extend beyond the `entities.json` E000/E001 pilot.
2. Perform a **campaign-resolution sweep**: distinguish closed outcomes, missing observations, contested claims and intentional hooks (including the apparent second Nash after the finale).
3. Extract stale/historical per-episode notes from active ledgers/queues to preserved archives, while retaining durable current questions and original issue keys.
4. Complete **Vorel's title register** with the roundtable retrospective; resume **Nash's spell-phrase register** beyond the earlier E111 keyword-pass ceiling with exact source support.
5. Build a **cartographic crosswalk** for the owner-held Known Wastes v3 map and other artifacts; record labels, edition, source, regional inclusion and uncertainty, without inventing precision or distribution rights.
6. Introduce automated **coverage/index diagnostics** for canonical name drift, missing final states, broken footnotes, unresolved alias pointers and uncited high-impact claims. Tool checks are aids to editorial review, not proof of canon.
7. Separate **episode publication/recording order, fictional chronology, and when a fact became known**, with Dunebreaker and retrospective bonuses as explicit exceptions.
8. Add **D-048 reader-first checks** to the page census and presentation diagnostics: index section order, first-screen project metadata, subject-page research apparatus, reachable footnotes, intentional source-first exceptions and optional artwork. Track **needs-migration versus accepted** rather than treating existing Wastes portals or completed spelling fixes as proof of full compliance.

## 9. Historical first implementation slice and scope record (2026-10-27)

This planning slice records the preliminary audit, proposal and owner-confirmed naming corrections. It **does not claim** to have completed Phase 0's exhaustive page-by-page machine manifest, conducted new transcript/audio comparisons, rewritten an arc, created new race subject articles, reconciled the full active ledger or run repository-wide tests.

**Historical Phase 0 census pointer (2026-10-27, superseded):** The original 9/9 narrative and 14/134 world listed/read counts describe the initial audit, **not** current remaining work. The old proposed Batch 15 pilot is archival planning evidence; resume using the latest unchecked [WCL task](WASTES_CLEANUP_TASKS.md), especially [WCL-029](WASTES_CLEANUP_TASKS.md#wcl-029) and [WCL-013](WASTES_CLEANUP_TASKS.md#wcl-013), without repeating old work.

**Reader-first presentation obligation (D-048; ongoing):** Track actual per-page D-048 findings, approved exceptions and validations through [WCL-013](WASTES_CLEANUP_TASKS.md#wcl-013), [WCL-031](WASTES_CLEANUP_TASKS.md#wcl-031) and [WCL-039](WASTES_CLEANUP_TASKS.md#wcl-039), not the prior N1-P3 or batch-specific tracker prose.
