# Reader-first presentation standard — project-wide

**Owner directive D-048 · effective 2026-10-28.** The archive's current reader portals are the pattern to follow for **all campaigns and new or revised reader-facing material**, not merely The Wastes. Lead with **the story, the fictional world, its people, lore and history**. Relegate project-specific maintenance, production, transcription, provenance detail and internal process to a **closing section or Markdown footnotes**. This standard governs presentation and information hierarchy; it does not change what is canon, which audio was checked or the separation of campaign continuities.

**Primary examples reviewed:** [archive landing page](../README.md), [Wastes campaign portal](../wastes/README.md), [Wastes world portal](../world/README.md), [Delvers campaign portal](../delvers/README.md), [Fate 4 reference](../world/technology/fate-4.md), and [Dusthill reference](../world/places/dusthill.md). The recently removed illustration embeds on the last two pages **must not be restored automatically**.

## 1. Reader-facing navigation: README files, directories, overviews and indexes

Order content by what a visitor wants to explore, using headings suited to the page:

1. **Title and an inviting in-world or story-focused introduction.** Identify the fictional setting, subject or character(s) and why the material is interesting. The first screen should not be a build log, an ASR disclaimer, a status ledger or a production notice.
2. **Story and reading routes first.** Present campaigns, arcs, chapters or accessible narrative sequences with short story-oriented descriptions. Keep campaign worlds distinct. Do not present a release-catalogue or publication order as in-world chronology.
3. **World, characters, places, cultures, creatures, objects, factions and lore next.** Index entries should answer who or what they are and why they matter; use navigation tables or lists where they help browsing. Prefer the subject's role and history over performer, transcript IDs, editorial status or research counts as headline fields.
4. **History, turning points, connections and consequences.** Offer history/cosmology links and meaningful paths deeper into the setting. Preserve actual story outcomes and the distinction between fact, report, belief and unperformed plan.
5. **Sources and project notes at the bottom**, normally under `## Sources and project notes` (or an equally clear last section). Collect research provenance, episode/ASR status, listening caveats, maintenance state, cleanup plans, index compatibility, number crosswalks, illustration production and other out-of-world guidance there. Keep links to the source evidence available, rather than deleting it for readability.

**Navigation exceptions:** A pure transcript index, technical index, evidence inventory, citation register or contributor-facing workflow document may put its functional data first; its purpose must be explicit. Even then, avoid needless out-of-world clutter in the opening and keep cross-campaign routing accurate. Do not rename stable URLs or alter link destinations solely to reformat a portal.

## 2. Subject pages and thematic reference writing

For ordinary characters, places, technology, creatures, groups, historical events and setting studies, follow [the narrative style directive](WORLD_NARRATIVE_STYLE.md) and [reference template](WORLD_REFERENCE_PAGE_TEMPLATE.md):

- **Main prose is in-world and subject-first**: introduction as initially known, important development and meaningful changes, then current in-world status or historical legacy. The subject's story and nature take precedence over a process/report chronology.
- **In-world uncertainty stays visible** (for example, “she believed,” “he claimed,” or competing histories). Do not disguise actual character knowledge limitations as a smooth objective narrator's certainty.
- **Research/production apparatus goes into referenced Markdown footnotes at the bottom**: episode IDs and clocks, ASR alternatives, source links, confidence and listening limits, editorial decision provenance and illustration-production details. Cite close to the associated assertion, and keep every footnote reference paired with a definition.
- `## Current status` (or `## Lasting legacy` for event studies) is the **last substantive in-world heading**; footnote definitions follow it, not a new research heading. For **overview/index pages**, in contrast, the project-information section comes last because that is their reader navigation contract.
- **Visuals are optional**, never a prerequisite or substitute for canon prose. Do not reintroduce removed image embeds or automatically place illustrations in indexes/subject pages. When an image is intentionally selected for reader display, keep its artistic nature and rights/source limits clear; maintain generation, approval and appearance-production records in `project/` and appropriately cited notes, not in the opening story. Do not infer that removing an embed deletes its asset or cancels its production history.

## 3. Scope and important exceptions

This standard applies across the repository's **Wastes, Delvers, Inverse, one-shot and bonus reading routes** and to future reader-facing pages. It also applies to introductory material for narrative and world directories. Independent campaigns retain independent canon; an in-universe explanation for one is never silently imported into another.

**Source-first/evidence-first exceptions are intentional:** episode dossiers, transcripts, processed ASR, audio comparisons, research reports, review queues, decision logs, metadata schemas, technical instructions, specialist phrase/title registers, and source-keyed chronologies or ledgers retain the details required to establish evidence and operate the archive. They must not be rewritten as fictional prose or stripped of provenance. A bonus Q&A index still distinguishes commentary from played events.

For mixed-purpose documents, **split the reader-facing explanation from the research apparatus** rather than sacrificing either. Do not create a new story fact, canon name/identity, audio-verification claim, invented quotation, speaker attribution, completed action, or false chronological ordering while moving text.

## 4. Rollout and acceptance

- **Immediately** use this structure for every new reader-facing page and each page revised during ongoing cleanup, including non-Wastes campaigns.
- **Existing pages are not automatically certified compliant.** Inventory them in bounded, reviewable groups; preserve pre-edit working copies for substantive rewrites and use guarded edits; avoid rewriting the whole archive as one giant batch. Do not disturb recently user-reworked indexes merely to apply a generic template.
- **Check hierarchy:** A reader reaches story/world/history before archive mechanics. Overview/index pages place project detail at the bottom; ordinary subject pages put research detail in referenced footnotes and finish their narrative with current status/legacy.
- **Check integrity:** canonical display names, legacy paths, anchor links, source citations/footnotes, spoiler and knowledge horizons, nuanced testimony, original images and rights constraints. Do not claim links or tests pass if not checked.
- **Handle illustration cleanup accurately:** Fate 4 and Dusthill currently have no illustration embeds. Do not restore them by automation. Any retained illustration-only footnotes that are no longer cited should be reviewed separately during a bounded cleanup; don't delete project provenance or invent an inline display to make them visible.
- **Authorizations:** D-048 explicitly establishes this **presentation direction** across the project. D-047 continues to authorize routine small editorial corrections without repeat approval. This is **not** permission to rewrite story beats, move scenes, change approved arc boundaries, adjudicate ambiguous lore, perform bulk deletions or rename files without the existing substantive approval/provenance safeguards.

**Related standards:** [editorial guide](EDITORIAL_GUIDE.md), [documentation architecture](DOCUMENTATION_ARCHITECTURE.md), [world narrative style](WORLD_NARRATIVE_STYLE.md), [world-reference template](WORLD_REFERENCE_PAGE_TEMPLATE.md), [image assets/provenance](IMAGE_ASSETS.md), [owner decisions](DECISIONS.md). Historical index reorganization evidence remains in [the 2026-10-28 checkpoint](READER_INDEX_REORGANIZATION_2026-10-28.json); it is not a new content authority.
