# Delvers — documentation plan

**Prepared 2026-10-24.** Delvers seasons 1–3 will use the same four editorial layers as Wastes, with independent continuity and a declared spoiler horizon on every reference or narrative page. This plan allocates future paths; it does not claim the uncreated pages below already exist.

## Campaign layers and locations

| Layer | Location | Purpose and creation point |
| --- | --- | --- |
| Campaign entry and source register | `delvers/README.md`, `delvers/SOURCE_INVENTORY.md` | Available now: navigation, exact archive identities, source availability and limits |
| Episode research | `delvers/episodes/S1E01.md`, then the actual season-qualified IDs | Create after a complete bounded recording review; preserve its final cutoff and evidence questions |
| ASR comparisons | `reports/DELVERS_S1E01_ASR_COMPARISON_YYYY-MM-DD.md` and equivalent verified IDs | Link complete-input metrics, high-risk differences and listening questions from the dossier; qualify by campaign and season |
| World portal and subject indexes | `delvers/world/README.md`, `CHARACTERS.md`, `PLACES.md`, `WORLD.md` | Begin with sourced people, geography and setting from the first researched episode; add indexes when needed for discovery |
| Subject profiles | `delvers/world/characters/<slug>.md`, `places/<slug>.md`, `items/<slug>.md`, `factions/<slug>.md` | One substantial source-linked account per subject; multiple indexes may link to it |
| Additional reference categories | `delvers/world/ANTAGONISTS.md`, `ITEMS_AND_ARTIFACTS.md`, `FACTIONS_AND_POWERS.md`, `HISTORICAL_EVENTS.md` | Expand to Wastes-scale navigation as researched subjects warrant each category |
| Chronology and continuity | `delvers/world/CHRONOLOGY.md`, `delvers/world/CONSISTENCY_LEDGER.md` | Start with the first sourced events/issues; separate archive order, story time, beliefs, later revelations and actual cutoff status |
| Story-first narrative | `delvers/narrative/README.md`, then descriptively named arc files | Begin when researched scenes support connected prose; keep arcs flexible until their boundaries are demonstrated |
| Editorial controls | `delvers/REVIEW_QUEUE.md`; future `delvers/DECISIONS.md` | Open source/listening tasks now; add a decision register when Delvers-specific spelling or identity resolutions exist |
| Shared standards and experiment history | `project/` | Reuse workflow, numbering, editorial guide, page contract and model log; qualify every Delvers entry by campaign and season |

All Delvers world paths in this table are relative to `delvers/world/` where abbreviated. **World and narrative directories are deferred until there is researched content to put in them.** They are not empty templates to be filled from episode titles or another campaign.

## First episode and subsequent passes

1. When Delvers research starts, review **S1E01 — How Much Is Potato** through the final speech/outro, using both exact exports in the [source inventory](SOURCE_INVENTORY.md). Verify matching recording identity and any transcript truncation or advertising offsets.
2. Establish GM, performers and characters from the actual recording rather than importing Wastes roles. Record the episode type, cast-to-character mapping, starting premise, places, actions, custody changes and final unresolved situation with timestamps and confidence.
3. Create the source-first dossier and campaign-qualified comparison report. Measure the established complete-export word-token distance, naming the reference denominator; distinguish ASR disagreement from accuracy and keep unlistened wording provisional.
4. Create only the world pages supported by that episode, using the [shared page contract](../project/WORLD_REFERENCE_PAGE_TEMPLATE.md) with Delvers links. Begin its chronology and continuity issues where evidence warrants them. Keep handout statements attributed and separate from what was actually played.
5. Add story-first synthesis when enough researched scenes form a useful narrative. Preserve uncertainty and source links without duplicating the dossier in every subject page.
6. Update the Delvers index and queue with the researched horizon, source status and next verified entry. Log any ASR experiment in the shared model log under an explicit Delvers ID. Run Markdown, relative-link and source-preservation checks before reporting completion.

## Season and story boundaries

Research season 1 before season 2, retaining **S2E00 — Cassius at the Guild** before S2E01 in archive order. Its classification remains open until the recording is reviewed. Continue to season 3 using its actual IDs. Neither an E00 label nor the final available filename proves episode type, story chronology or fictional closure.

Do not assign one story arc per season in advance, reuse Wastes arc numbers or impose eight chapters on an ongoing story. Once a Delvers arc has ended, follow the shared policy for a coherent consolidation and roughly eight main chapters where meaningful, preserving a linked historical snapshot before a major rewrite.

## Continuity and provenance contract

- Campaign + season + episode form the source identity. `Delvers S1E01` is not `Wastes E001`, `Inverse S1E01` or `Delvers S2E01`.
- Every world and narrative page states its researched spoiler horizon. Later handouts, previews, Q&As and episodes cannot silently supply earlier character knowledge.
- Separate observed/GM-adjudicated action, NPC/character claims, jokes, unchosen plans and later creator commentary. Track item custody, deaths/survival, locations, private knowledge, promises and completed actions.
- Keep written spelling authority distinct from spoken-word verification and identity matching. The guild guide's in-world bylines do not establish real-world authorship.
- Keep original SRTs and MP3s unchanged. Private handouts and Discord archives remain local; link to the existing provenance register rather than copying private source material into Git.
- Use stable subject slugs and a single primary page per subject. Indexes summarize and navigate; dossiers retain the detailed time-coded investigation.

## Completion criteria for the first research slice

A complete first slice has a full-recording S1E01 dossier, a documented two-export comparison or explicit source limitation, only evidence-supported reference additions, the actual episode cutoff, unresolved listening questions and a verified S1E02 pointer. Narrative coverage is stated honestly if not yet useful. Source availability, text research and audio verification remain separate statuses.

[Campaign index](README.md) · [Source inventory](SOURCE_INVENTORY.md) · [Review queue](REVIEW_QUEUE.md)
