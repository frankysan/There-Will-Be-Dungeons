# The Wastes — completed-campaign consolidation and cleanup plan

**Prepared:** 2026-10-27. **Status:** **Eleven-arc organization approved by the owner (D-045); actual migration pending**. Preliminary repository audit only: no narrative rewrite, full page census, audio verification or migration has yet been completed under this plan. **Story horizon:** The played campaign ends at [S3E18](../episodes/S3E18.md). [S3E019](../episodes/S3E019.md) is a separate post-campaign cast roundtable/Q&A, not an additional played chapter. All transcript-based findings retain their existing ASR-provisional limits.

This plan extends, rather than replaces, the ongoing [Wastes world arc cleanup](WORLD_ARC_CLEANUP_PLAN.md) and uses lessons from the [Delvers campaign cleanup](DELVERS_CAMPAIGN_CLEANUP_PLAN.md), [migration manifest](DELVERS_CLEANUP_MANIFEST.md) and [narrative chapter maps](DELVERS_NARRATIVE_CHAPTER_MAPS.md). Operational trackers: [Wastes manifest](WASTES_CLEANUP_MANIFEST.md) · [proposed chapter maps](WASTES_NARRATIVE_CHAPTER_MAPS.md) · [editorial guide](EDITORIAL_GUIDE.md) · [world style](WORLD_NARRATIVE_STYLE.md) · [reader-first presentation standard (D-048)](READER_FIRST_PRESENTATION.md) · [decisions](DECISIONS.md).

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

## 3. Narrative architecture — eleven arcs approved; migration pending

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
5. **Bounded execution and acceptance:** Group related short pages when safe; preserve exact working-copy originals and inbound anchors before substantial reordering. For each article/index compare before/after **section hierarchy, unique subject claims, footnote markers and definitions, link destinations/fragment targets, canonical aliases, chronology and last actual observation**. When tools are available run changed-file Markdownlint, link/anchor and whitespace checks; never report unrun checks as passed. Log `D-048 planned → archived → presentation-migrated → structurally-validated → accepted` (or `retained-exception`) in the [manifest](WASTES_CLEANUP_MANIFEST.md), linked to the existing per-file inventory rather than claiming the whole world complete.

**Wastes-specific dependencies:** Eleven-arc migration D-045 remains separately provenance-gated; do not pre-emptively rename arc links or index a chapter path that does not exist. Races D-046 is planned, not published; any new index/page must follow D-048 when authorized and sourced. The root archive's recently revised portals are **examples/preservation baselines**, not targets for automatic replacement. Preserve S3E18 played ending versus S3E019 commentary and prequel/one-shot chronology.

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

Phases 3–5 can proceed in carefully scoped linked batches. Keep detailed report checkpoints (old/new source horizons, edits, hashes, links, test results, reviewer limits) as Delvers does. Run changed-file Markdownlint, link/anchor checks and diff whitespace checks when local tooling is available; distinguish performed checks from merely recommended checks. Do not run the full test suite unnecessarily.

### Bounded multi-file cleanup batches (owner approved 2026-10-27)

**Phase 0 read-only structural inventory** should normally review *several related
short world files per batch*, rather than opening and closing a report for each
small article. Group by domain/source relationships, inspect actual lengths and
complexity before selecting an ordered set, and preserve individual per-file
findings under **one batch journal**. Recommended planning envelopes:

| Source type | Typical grouping | Total source-line guide |
| --- | --- | --- |
| Short articles (~15–50 lines) | 4–8 related files | ~300 lines |
| Medium articles (~50–150 lines) | 2–4 related files | ~350 lines |
| Large articles (~150–300 lines) | 1–2 when safe | ~400 lines |
| Registers / complicated source material / more than 300 lines | One file or bounded chunks | Standalone checkpoint |

These are **adaptive guides**, not minimum throughput. Prefer fewer files when
contention, density, uncertain provenance or cross-reference complexity demand
it. For the **first grouped pilot (Batch 15)** aim for **4–6 related world files,
roughly 300 lines combined**. Begin candidate preflight at
`world/ITEMS_AND_ARTIFACTS.md`; name additional related unread paths and their
line counts in the pilot journal **before full reading**. Do not count preflight
as completed structural review.

Every chosen file needs its own operation ID, actual numbered-line coverage,
source horizon, link split (listed-world vs outside-world unchecked), notes,
footnotes, approved name/arc crosswalk leads, clear unperformed validation and
recoverable `queued/reading/complete/blocked/unknown` status. Checkpoint the
journal **after each file**, then perform **one** guarded manifest update and
**one** progress-pointer update at batch close, followed by readback and Git
status. On timeout recover completed files and resume only unconfirmed work.
A pending unapproved substantive edit **stops the entire batch**, and the agent
must not jump to another file to avoid asking the owner. See the
[cleanup skill](../.agents/skills/twbd-wastes-cleanup/SKILL.md) and its
[recovery instructions](../.agents/skills/twbd-wastes-cleanup/references/progress-and-recovery.md).

**Coverage accounting remains per world file, not per batch.** The
134-unique-path `WASTES_CLEANUP_WORLD_WORKLIST_2026-10-27.json` remains a
`listed_only` directory snapshot; it must not be rewritten to claim fact/auditory
approval. At the Batch 14 checkpoint, **14 of 134** world files have full first-pass
structural reads and **120 remain**. This batching change does not itself audit
another world file, advance the phase or authorize content changes.

## 8. Additional improvements to track

1. Create an **entity-and-relationship graph**: stable IDs, canonical names/aliases, first/last observation, kinship, membership, item custody and connected histories. Extend beyond the `entities.json` E000/E001 pilot.
2. Perform a **campaign-resolution sweep**: distinguish closed outcomes, missing observations, contested claims and intentional hooks (including the apparent second Nash after the finale).
3. Extract stale/historical per-episode notes from active ledgers/queues to preserved archives, while retaining durable current questions and original issue keys.
4. Complete **Vorel's title register** with the roundtable retrospective; resume **Nash's spell-phrase register** beyond the earlier E111 keyword-pass ceiling with exact source support.
5. Build a **cartographic crosswalk** for the owner-held Known Wastes v3 map and other artifacts; record labels, edition, source, regional inclusion and uncertainty, without inventing precision or distribution rights.
6. Introduce automated **coverage/index diagnostics** for canonical name drift, missing final states, broken footnotes, unresolved alias pointers and uncited high-impact claims. Tool checks are aids to editorial review, not proof of canon.
7. Separate **episode publication/recording order, fictional chronology, and when a fact became known**, with Dunebreaker and retrospective bonuses as explicit exceptions.
8. Add **D-048 reader-first checks** to the page census and presentation diagnostics: index section order, first-screen project metadata, subject-page research apparatus, reachable footnotes, intentional source-first exceptions and optional artwork. Track **needs-migration versus accepted** rather than treating existing Wastes portals or completed spelling fixes as proof of full compliance.

## 9. First implementation slice and scope record

This planning slice records the preliminary audit, proposal and owner-confirmed naming corrections. It **does not claim** to have completed Phase 0's exhaustive page-by-page machine manifest, conducted new transcript/audio comparisons, rewritten an arc, created new race subject articles, reconciled the full active ledger or run repository-wide tests.

**Current Phase 0 census pointer (recorded 2026-10-27):** Resume Phase 0 using the owner-approved bounded multi-file audit workflow above. At the Batch 14 checkpoint, 9/9 narrative files have received initial structural reads and 14/134 world files have received first-pass structural reads; byte hashes, source-to-claim/paragraph maps, inbound links and complete validation remain unfinished. **Batch 15** starts with a size/complexity preflight of `world/ITEMS_AND_ARTIFACTS.md` plus related unread files, selects and journals approximately 4–6 paths within ~300 combined lines, then performs a read-only pilot with per-file checkpoints. **D-045 already approves the eleven arc boundaries**; scene-level provenance, preservation/compatibility checks and any separately undecided substantive edits remain gated. Do not start a narrative rewrite from this planning pointer or claim the multi-file pilot has already occurred.

**New concurrent presentation obligation (2026-10-28):** At the next live census checkpoint, add D-048 reader-first page-purpose/disposition fields to the existing inventory before approving a page's presentation. Carry this through Phase 4 subject pages and Phase 6 overview/index integration; section 6A above and the [D-048 standard](READER_FIRST_PRESENTATION.md) are planning rules, not evidence that any current source page has been consolidated. The N1-P3 name-normalization checkpoints in the manifest remain separate completed text-edit batches.
