# Delvers — completed-campaign cleanup plan

**Prepared:** 2026-10-26. **Status:** Programme underway: 107-file structural baseline, navigation reconciliation, three-arc chapter maps and preserved Season One consolidation pilot completed. Claim-level acceptance across the remaining pages and later narrative/world rewrites remain pending. See the [migration manifest](DELVERS_CLEANUP_MANIFEST.md) for the bounded checkpoint. The campaign is concluded through [S3E12](../delvers/episodes/S3E12.md). This plan covers the Delvers namespace, especially [narrative](../delvers/narrative/README.md) and [world](../delvers/world/README.md), with supporting navigation, chronology and editorial controls.

## 1. Intended result

Give Delvers a coherent, finished reading experience: three connected arc narratives and a subject-centered world reference that follows people, places and objects from introduction through their last supported state. Readers should be able to follow the story without encountering the archive's incremental research history in every paragraph.

Use the existing [world and narrative style directive](WORLD_NARRATIVE_STYLE.md), [reference template](WORLD_REFERENCE_PAGE_TEMPLATE.md), [editorial guide](EDITORIAL_GUIDE.md) and [documentation architecture](DOCUMENTATION_ARCHITECTURE.md). This plan supplements the [Delvers documentation plan](../delvers/DOCUMENTATION_PLAN.md), whose initial-research milestones remain historically useful but whose onward-work language needs reconciliation.

Campaign completion permits full-campaign synthesis. It does not make every ASR spelling certain, establish an unshown event, or turn text research into listening verification. Retain Delvers' separate reality and continuity throughout.

## 2. Initial checkout inventory and findings

The filesystem inventory on 2026-10-26 contains:

| Layer | Markdown files | Planning implication |
| --- | ---: | --- |
| Episode dossiers | 37 | S1E01–S1E12, S2E00–S2E12 and S3E01–S3E12 are present; audit research limits rather than restart an assumed episode backlog |
| Narrative | 8 | Three arc/season syntheses, four earlier Season One studies and one portal need an explicit canonical reading route |
| World: characters | 35 | Prioritize recurring subjects and identity/relationship continuity |
| World: places | 27 | Review geography, institutions and event-like pages currently filed as places |
| World: items | 20 | Reconcile custody, demonstrated powers and final condition |
| World: creatures | 6 | Preserve the distinction between creature references and reasoning named characters |
| World: root documents | 7 | Portal, character/place/creature indexes, setting essay, chronology and consistency ledger have different editorial purposes |
| World total | 95 | Classify every page before migration; these counts do not measure quality or researched completeness |

Representative inspection establishes the following starting problems, not an exhaustive content audit:

- [Season One](../delvers/narrative/SEASON_ONE_ARC.md) already has eight numbered chapters, alongside four older detailed studies. Their relationship needs a durable reader-facing policy.
- [Season Two](../delvers/narrative/SEASON_TWO.md) has 21 second-level sections; [Season Three](../delvers/narrative/SEASON_THREE.md) has no second-level chapter headings despite its extensive accumulated prose. Both need structure and proportionality review.
- [Koh's biography](../delvers/world/characters/koh-spiros.md) includes reverse episode updates, visible source identifiers and detailed action recaps. It is a useful pilot for restoring chronological, character-focused prose.
- The [campaign portal](../delvers/README.md) mixes finale coverage with earlier onward-research pointers and obsolete coverage summaries. The documentation plan still includes an earlier “next unresearched” milestone. Reconcile current instructions while retaining explicitly dated history.
- [The public guild reckoning](../delvers/world/places/guild-public-reckoning-s3e10.md) needs a classification decision: a historical event may be better served by an event article linked from the guild's institutional history. Its current path alone does not justify a move.
- The finale dossier explicitly limits its audio review and local/remote source-byte verification. Preserve those limits and route consequential questions to the review queue.

No full claim-by-claim audit, global link check, main-prose balance measurement or audio review is claimed by this inventory.

## 3. Story boundaries and knowledge

| Segment | Coverage | Editorial treatment |
| --- | --- | --- |
| First arc | S1E01–S1E12 | Completed arc; preserve the established first-arc title unless deliberately changed |
| Academy cutaway | S2E00 | Keep its archive ID; place its narrated events alongside the Season One kuo-toa mission, with exact placement qualified by evidence |
| Second arc | S2E01–S2E12 | Ends at the Bronze Ball catastrophe; immediate aftermath belongs to the third arc |
| Third arc | S3E01–S3E12 | Includes the three-month transition, final expedition, Khalazar's defeat and the one-year epilogue |
| Final invitation and sealed letter | S3E12 closing scene | Invitation is shown; wedding is not performed. Letter remains unopened; do not supply its contents or manufacture a fourth arc |
| Handouts and bonuses | Individually classified | Attribute setting claims and retrospective commentary; do not silently insert them as played history |

Track when something happened, when it was learned and who knew it. Give hallucinations and visions their narrative place without treating their apparent events as ordinary physical history. Preserve testimony as testimony, including the aboleth's claims. Later outcomes must not overwrite the historically correct cutoff in an earlier episode dossier.

## 4. Narrative consolidation

Use one primary narrative per confirmed arc, retaining the existing paths during the first pass. Keep the existing titles as working titles; do not mechanically rename files or choose new campaign branding during cleanup.

1. Build an episode-to-scene outline for all three arcs, including the Academy cutaway and epilogue. Check completeness against dossiers, the chronology and the four older Season One studies. Record unique material before condensing anything.
2. Measure main story prose per section, excluding headings, navigation and complete footnote definitions, including their continuation lines. Raw file word counts are unsuitable because some notes contain extensive research summaries.
3. Draft chapter maps before rewriting. The Delvers documentation plan already allows roughly eight main chapters for a completed arc where meaningful. Retain Season One's eight as the starting point; assess approximately eight for Two and Three against actual turning points. Do not split or pad merely to match a number.
4. Use comparable reading weight across substantive chapters. The shared guide's roughly 400-word chapter convention is a planning reference for the proposed completed-arc treatment; confirm that it fits Delvers before treating 350–450 words as a rollout target. Preserve supported events and character decisions over numerical symmetry.
5. Rewrite as connected, plot-led, in-universe prose. Remove repeated cutoff warnings, emphatic “ACTUALLY” bookkeeping, scene-by-scene combat mechanics and duplicated explanations. Preserve consequential choices, rescues, losses, revelations and naturally attributed uncertainty.
6. Keep epilogues proportionate and distinguish the played one-year outcomes from the invitation and unresolved letter. Ending the campaign does not require resolving every fictional mystery.

Archive exact working-copy originals and provide rebased reading copies before substantial edits. The four earlier Season One studies should eventually be presented as historical detailed versions rather than competing canonical chapters. Decide their final archive/navigation treatment only after checking for unique content and inbound links; retain compatibility links if relocated.

## 5. World-reference consolidation

Keep one canonical page per subject. Use introduction-time description, chronological development through relevant Delvers arcs, optional enduring reference material and final **Current status**. A historical-event study may end with **Lasting legacy**. Avoid empty arc sections for subjects with no meaningful change.

| Domain | Editorial questions |
| --- | --- |
| Characters | What drives this person? How do loyalties, relationships, identity and choices change? Which scenes demonstrate those changes? |
| Places | What is the place like, who lives or governs there, and how do its purpose, condition and society change? |
| Items | What is it, what has it demonstrably done, who holds it, and what is its final known condition? |
| Factions and institutions | What are their aims, leadership, methods and alliances? What changes institutionally rather than merely happening nearby? |
| Creatures | What appearance, behavior, habitat and abilities are supported? Is this an individual observation or a justified general trait? |
| Setting and history | What explains the world's systems or a historical transformation? Which accounts remain attributed or disputed? |

Major biographies may use the shared flexible 150–300 words per substantive arc as a diagnostic starting point. Other domains need subject-relative balance. Do not shorten a pivotal transformation merely because a quieter arc is brief.

Move episode IDs, clocks, source links, spelling alternatives and verification commentary into complete Markdown footnotes. Keep uncertainty experienced by the characters in the prose. Notes should support claims rather than repeat an entire dossier or finale recap on every page.

Preserve functional exceptions: navigation indexes, source-keyed chronology and the consistency ledger retain the evidence fields their work requires. The thematic `WORLD.md` receives a prose review. Assess missing item/faction/history navigation against existing substantive content before creating indexes; do not add empty categories for symmetry.

## 6. Work sequence and completion gates

| Phase | Bounded deliverable | Exit gate |
| --- | --- | --- |
| 0 — Full audit | Page-level manifest for all 95 world files, eight narratives and campaign control documents; section/prose measurements; inbound links; source horizons; exception and duplication inventory | Every file has an intended disposition and priority; sampled findings above replaced or supplemented by page-level evidence |
| 1 — Editorial foundations | Reconcile current completion language in portals, documentation plan and review queue; establish chapter maps and archival layout | No active instruction points to another main-campaign episode; historical milestones clearly dated; source and listening limits preserved |
| 2 — Narrative pilots | Archive and consolidate one arc at a time, starting with Season One; compare the finished approach before applying it to Two and Three | Scene coverage accounted for; no fabricated transitions; chapter balance assessed; historical versions reachable |
| 3 — World pilots | Koh; guild institution; three-urn artifact account; one short place or creature page | Each treatment satisfies its own subject focus, chronological order, footnotes and last-known state; pilot findings recorded before scaling |
| 4 — World rollout | Small linked batches: core PCs/families; guild and rivals; places; artifacts; remaining characters/creatures; setting/history | Each batch has preserved originals, claim checks, links and a recorded acceptance result |
| 5 — Campaign integration | Cross-check narratives, chronology, ledger, indexes and final states across the whole campaign | Contradictions resolved or explicitly queued; no stale current-status claims; canonical reading route and archive links verified |

The guild pilot may remain within its current place path initially. Classification changes, renamed slugs and new index categories need evidence from Phase 0 and an inbound-link plan, rather than a bulk directory reorganization.

The future manifest should record: path, page purpose, canonical subject/alias, researched horizon and last direct observation, applicable arcs, main-prose measurements, problems, proposed treatment, archive/hash location, dependencies, status, validation and unresolved review items. Use explicit states such as **inventoried**, **outlined**, **archived**, **rewritten**, **validated** and **accepted**. “Rewritten” alone does not mean complete.

## 7. Verification work alongside editing

Use the [Delvers consistency ledger](../delvers/world/CONSISTENCY_LEDGER.md) and [review queue](../delvers/REVIEW_QUEUE.md) as the canonical issue registers. Close the sequential main-campaign intake route while retaining unresolved listening and identity tasks.

Prioritize questions that can change identities, chronology or final status: Anthela/Anathala spelling and authority; Khalazar's visionary history; Shaolin Nym and other ancestral identities; the urn contents/custody sequence; the red shard's unshown return; rescue headcounts; Darmah's condition during escape; and the invitation's groom name and GCT signature. Link to existing issues before allocating duplicates.

For the finale and any similarly limited dossier, verify full source identity where needed before relying on exact wording. Retain separate fields for source availability, text research, selected comparison windows, complete narrative reading and actual listening. ASR agreement or disagreement supplies review leads, not accuracy or permission to resolve a name silently.

Most prose cleanup can proceed with unresolved details carefully bounded in footnotes. Pause a specific identity merge, decisive factual rewrite or claimed resolution when its required evidence is missing; continue independent editorial work.

## 8. Preservation and acceptance

Before each substantial rewrite, capture exact pre-edit working-copy bytes under `research/legacy/`, hash the originals and create appropriately rebased reading copies. Preserve source SRT/MP3 files and unrelated working-tree changes. Record every move, alias and unique passage retained elsewhere.

For each bounded batch:

- Compare against the pre-edit text and underlying dossiers for lost developments, false certainty and knowledge leakage.
- Check introduction-time viewpoint, chronological development, subject focus and final-state placement. Confirm that an earlier last observation is not invented into a finale appearance.
- Verify footnote references/definitions, relative links and incoming anchors; link checks must ignore fenced illustrative Markdown. Preserve old targets through updated links or compatibility stubs when moving content.
- Run changed-file Markdownlint using `npm run lint:markdown -- --files <changed Markdown paths>` and `git diff --check`. Run applicable repository checks when available; record baseline failures separately.
- Read each resulting article as a reader, including its rendered footnotes when a preview is available. Report what was actually checked; a structural check does not establish factual accuracy.

The programme is complete when every in-scope page has an accepted disposition, all three narratives form a coherent reading route, reference articles satisfy their domain contract, obsolete active instructions are gone, preserved versions remain reachable and open evidence questions remain visible in the appropriate registers. No commit, push or publication is part of this planning pass.

## 9. Recommended first implementation slice

The first implementation slice has produced the structural manifest and prose measurements, reconciled campaign control documents, outlined all three narratives and consolidated Season One with preservation. The [chapter maps](DELVERS_NARRATIVE_CHAPTER_MAPS.md) and [checkpoint](DELVERS_CLEANUP_MANIFEST.md#first-implementation-checkpoint) record the result and limits. Full claim-level horizon and final-state review remains part of the page batches; the structural scan does not replace it.

Next, complete the old-section-to-new-chapter coverage checklist for Season Two and consolidate that arc against its dossiers. Season Three needs a deliberate decision about the final expedition's chapter weight. The world pilots remain bounded by their own acceptance gates; no world subject has been rewritten in this first slice.
