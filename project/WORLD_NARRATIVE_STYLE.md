# World-reference narrative style directive

**Status:** Archive-owner directive adopted 2026-10-24. **Scope:** Reader-facing prose throughout `world/`, particularly canonical character, place, artifact, faction and event histories. Read with [the world-reference template](WORLD_REFERENCE_PAGE_TEMPLATE.md), [documentation architecture](DOCUMENTATION_ARCHITECTURE.md) and [arc cleanup plan](WORLD_ARC_CLEANUP_PLAN.md). This directive governs **presentation**, not which sources count as evidence, and does not retroactively claim that existing pages already comply.

**Project-wide companion rule (D-048, 2026-10-28):** The owner’s reader-first index/overview revisions extend this hierarchy to **README portals and indexes across Wastes, Delvers, Inverse, one-shots and bonus material**. Navigation pages show story, setting, lore and history first; project methodology, verification and illustration-production notes belong in their closing `Sources and project notes` section. Ordinary in-universe subject pages continue to keep their **Current status / Lasting legacy** section last and source apparatus in footnotes, not an extra metadata section. Do not automatically re-add the illustration embeds recently removed from Fate 4 and Dusthill. Purpose-built sources and technical registers are not forced into in-universe prose. [Full standard](READER_FIRST_PRESENTATION.md).

## 1. Default: an in-universe, narrative-focused main text

Write as an account of the **fictional world and its inhabitants**, in a fluent, coherent third-person narrative. Describe subjects **as first encountered**, then what happened through relevant arcs, then their **latest known in-world status at the end**. Prefer a continuous account of material developments over a series of transcript-processing notes or mechanics logs. Historical accounts may use the appropriate past tense; the latest-state section describes where the story leaves the subject.

**Do not put these in the main narrative**, including its opening metadata, subsection headings and closing status paragraphs:

- Corrected **episode identifiers** such as `E118`, recording clocks, cue identifiers, recording/publication dates, transcript basenames or URLs to episode research dossiers as visible link text.
- ASR/model names and disagreements, speculative spellings with `(?)` or transcription alternatives, listening priorities, confidence grades or repeated “audio not verified” warnings.
- Out-of-universe framing such as “the GM says,” “the player rolled,” “this episode ends,” “the party gains level 13,” source review instructions, or statements about how the archive was edited. Retain essential fictional consequences in ordinary prose rather than deleting them.
- Proposed-but-unplayed events written as completed history; a character's private knowledge presented as common knowledge; owner/creator retrospective plans presented as in-world facts.

**The arc labels may remain as an organizational aid** (`### Arc Five — The fall of Elhandar`), because readers asked to browse entries by arc. **Do not put episode ranges in the headings.** In-world temporal descriptions are welcome (“after the crash,” “during the siege,” “when the ships departed”). Avoid treating the five arc labels as literal in-world calendars.

Keep natural uncertainty where the **characters themselves** lack reliable knowledge: “The Soulbroker claimed the Principle had betrayed him,” “The others believed Angelashi dead,” “The villa was said to be capable of spaceflight.” These are meaningful parts of the story, not ASR uncertainty, and **must remain in the narrative**. Do not invent an objective fact, motive, quote, spelling or scene to make the narrative smoother.

### Character biographies — personality and development first

**For `world/characters/` biographies, use a character-focused lens distinct from the plot-led [arc narratives](../narrative/README.md).** The primary questions are **who this person is, what drives them, whom they trust or oppose, how they respond to hardship, and what changes about them**. Focus on:

- **Personality, disposition and contradictions:** temperament, habits, values, fears, strengths, weaknesses and characteristic choices, supported by what the character does or says.
- **Motivations, beliefs and allegiances:** ambitions, obligations, loyalties, faith, bargains, factions and changes in worldview; distinguish an internal motive inferred from behavior from one actually disclosed.
- **Relationships and agency:** friendships, family, rivalries, romances, betrayals, reconciliations, influence and how those bonds evolve. Preserve distinct agency (notably Stanley versus Diontalus).
- **Attributes and growth:** defining physical or magical traits, capabilities, limitations and identity revelations, especially when they affect choices or self-understanding. Avoid combat move-by-move summaries and out-of-world stat blocks.
- **Lasting transitions:** revelations, moral decisions, transformations, losses, acquired responsibility and changed circumstances; events serve as **illustrations and causes** of these developments, not as the organizing goal.

An arc section should explain **how the character enters the arc, what tests or reshapes them, and how they emerge**, rather than retelling all the places visited and enemies defeated. Mention a battle, quest or discovery only when it reveals an enduring trait, changes a relationship/allegiance, or materially alters the person's circumstances. The complete event sequence belongs in the [arc narrative](../narrative/README.md), episode dossiers and the [chronology](../world/CHRONOLOGY.md). If a paragraph would fit unchanged in a generic session recap, reconsider its relevance to the character.

**Balance the prose across substantive character arcs.** Following the recent [arc narrative prose balancing guidance](EDITORIAL_GUIDE.md), begin with a **soft planning range around 150–300 main-prose words per developed arc** for major recurring characters, excluding headings, footnotes and citations. This is **not a mandatory minimum or maximum**: a briefly appearing character, an arc without meaningful growth, or a genuinely pivotal transformation can warrant less or more. Compare sections of **similar character importance**; if one substantial arc exceeds roughly **twice the median** of the other substantial arc sections, review it for plot recap, repetition and opportunities to emphasize character change instead. **Do not pad short sections, erase major developments or invent personality traits to equalize counts.** Longer coverage should be justified by multiple distinct, source-supported changes, not more action scenes.

An enduring **Relationships and abilities** section is optional for cross-arc synthesis, **not a substitute for tracking relationship and personality changes where they happen**. Across the whole article, the **Introduction and Current status are naturally briefer** than the developed arc sections; they need not match their length. Neither the optional relationships section nor one exceptionally event-heavy arc should overshadow the person's defining developments elsewhere. Avoid repeating the same facts in every arc, the enduring section and Current status. Footnotes can carry detailed action provenance and retrospective interpretations without turning the main text into a research report.

### Other world domains — describe the subject, not a second plot summary

**Apply the same subject-first approach to all ordinary `/world` reference articles**, adapted to what makes each domain useful. Arc headings provide a chronology of **changes to the subject**, not a requirement to retell every scene involving it. Each substantive section should explain the subject's **starting nature or condition, meaningful changes and lasting significance**. Draw the connecting events from the [arc narratives](../narrative/README.md) through footnotes rather than duplicating the full journey.

| Domain | Main-prose focus | Prefer over scene-by-scene recap |
| --- | --- | --- |
| **Places and settlements** (`world/places/`) | Geography, physical character, atmosphere, inhabitants, customs, institutions, everyday function, political control, dangers and the way those features change; distinguish what a place was at introduction from its latest condition | The place's role as refuge, threat, home, stronghold or ruin, and the causes and consequences of changes in its society, leadership or landscape. Mention visits and battles only insofar as they **alter the place** |
| **Items, artifacts and technology** (`world/technology/`) | Physical nature, origins when known, purpose, stated versus **demonstrated** capabilities, limitations, attunement, custody, damage, transformations and symbolic importance | How the object is understood and used, what changes its owner or function, and why it matters. An owner's travel itinerary, combat rounds or every mention of the object normally belongs elsewhere |
| **Factions, institutions and supernatural powers** (`world/FACTIONS_AND_POWERS.md` and substantive subject pages) | Identity, aims, beliefs, membership, leadership, organization, alliances, rivals, resources, reach, methods and changes in influence | Political, ideological and relational shifts. Separate a faction's **declared goals** from its witnessed behavior; do not treat one member's action or an interested speaker's claim as settled institutional policy |
| **Historical events and eras** (`world/HISTORY_*.md` and substantial studies) | Causes and context, central agents, turning points, competing interpretations, direct consequences and lasting legacy | Why the event happened, what fundamentally changed and what remains disputed—not a second chronological log of every participant action. The [chronology](../world/CHRONOLOGY.md) already handles the detailed sequence |
| **Thematic setting and cosmology** (`world/WORLD.md` and narrative thematic studies) | How societies, magic, technology, geography, belief and power structures operate; competing accounts and changes in what is understood about them | Coherent explanations of world systems and lived consequences, with distinct levels of certainty. Avoid treating revelations in a single encounter as universal laws or duplicating arc plots |
| **Creatures and monsters** (`world/creatures/` in each campaign) | Appearance, ecology or origin when supported, behavior, abilities, relationships to habitats/peoples, and meaningful changes in the creature or monstrous form | The creature's distinguishing traits and significance, with encounters as illustrations rather than a combat log or invented species-wide rules. Primarily non-intelligent creatures; talking, reasoning NPCs retain character biographies. Follow the [shared category policy](WORLD_CREATURES_PLAN.md) for Wastes and Delvers |

**Balance is domain-relative, not one global word budget.** For major places, institutions, long-lived artifacts and historical subjects, review whether one arc or thematic phase dominates because it recaps many scenes instead of explaining major changes. Compare **sections of similar significance within that subject**: a paragraph or two may be enough for one minor appearance, while the founding or destruction of a city, a change of faction leadership, or the revelation of an artifact's function may justify more. The character-profile **150–300 word range does not apply to these domains**. For very short, single-arc entries, a concise introduction, one development section and current status may be sufficient; **do not invent empty arcs or pad for symmetry**.

**Domain-specific end sections:** Current status means the **present known condition** of a place; custody and operational state for an artifact; leadership, loyalties and reach for a faction; **aftermath or enduring legacy** for an event; and the latest supported understanding of a setting phenomenon. The last substantive section remains `## Current status` for standard subject pages, or `## Lasting legacy` for a focused historical event when that is the clearer in-world meaning. In either case, footnotes follow without a new sources heading. State uncertainty naturally where witnesses disagree or the fate is unknown.

**Across every domain, ask:** Does this passage teach the reader something characteristic about **this subject**, beyond the fact that a scene happened nearby? Are claims distinguished from demonstrations, and does the treatment explain **what changed and why it matters**? Reduce duplicated journeys and battle detail first; **keep** events that genuinely establish a location's destruction, a power's limit, a faction's allegiance, an artifact's transfer or an event's legacy. This principle is an editorial lens, not permission to discard unique evidence.

## 2. Put research and verification in Markdown footnotes

Attach **Markdown footnote markers** near the sentence or paragraph they support. At the **bottom of the file**, place corresponding footnote definitions using the existing arc-narrative convention (`[^key]: ...`, with subsequent indented lines if necessary). Footnote definitions **do not form another narrative chapter**; the final substantive `##` heading remains **Current status** on ordinary pages (or **Lasting legacy** for focused historical studies). Do **not** append a `## Sources` or `## Notes` section after Current status on standard subject pages.

Put the following in the relevant footnotes:

- The exact episode dossier, relevant clock/cues where important, and research/report links.
- **ASR uncertainties**, source contradictions, variant spellings, provenance, editorial naming decisions and **whether audio was actually heard**. Owner-confirmed display spellings are used naturally in the prose; list source-specific alternatives here rather than peppering text with question marks.
- Unresolved source conflicts and editorial cautions, linked to the [consistency ledger](../world/CONSISTENCY_LEDGER.md) or [review queue](REVIEW_QUEUE.md).
- GM mechanics and numbers or out-of-game milestones **when they matter for provenance**, and retrospective cast/creator comments properly identified as commentary.
- Page-wide researched-source horizon and verification limitations (prefer a short **single opening footnote marker**, rather than repeated warnings).

**Use one focused footnote for a meaningful paragraph or event**, not one note per sentence if a nearby marker covers the same evidence. Use stable, descriptive note IDs (for example, `[^nash-introduction]`, `[^nash-arc-five]`, `[^nash-status]`), not fragile sequential renumbering. Include direct relative links to canonical episode dossiers and reports. Preserve existing source references when moving them out of the main text; **do not remove provenance to make prose cleaner**.

## 3. Example of the intended separation

The following is a formatting example, not new campaign evidence:

```markdown
# Mask of Eltanfawr

## Introduction

Stanley found a dark jeweled mask among his father's possessions
in the hidden study of Villa Or'Nath. Its first described power
suggested that a wearer could alter the course of chance, but
Stanley did not yet put that power to use.[^mask-discovery]

## Development by arc

### Arc Five — The hidden vessel

After Elhandar fell, Stanley learned that the mask could command
the cottage itself. He donned it, but the house would not rise
at his request.[^mask-controls]

## Current status

The mask remains in Stanley's possession. He has not completed
its attunement, and the villa has yet to fly.[^mask-status]

[^mask-discovery]: [E118](../../episodes/E118.md).
    The processed ASR contains "Elton IV"/"Eltenvor"; the archive
    owner chose **Eltanfawr** as the preferred display spelling.

[^mask-controls]: [E126](../../episodes/E126.md).
    The described four-night requirement and the earlier four-rest
    item readout have not been reconciled.

[^mask-status]: [E128](../../episodes/E128.md).
    Source-level status, not audio-verified.
```

The illustrative example does **not** replace the source dossiers or the mask's actual reference page. When implementing on a real page, recheck all facts and retain any critical qualifications in either the naturally attributed prose or a note.

## 4. Exceptions: purpose-built research or navigation documents

**Explicit specialist-register exceptions:** [Nash's spellcasting phrases](../world/characters/nash-spellcasting-phrases.md) and [Vorel's titles](../world/characters/vorel-titles.md) remain **source-indexed registers**. Keep their episode numbers, exact wording, cue ranges, confidence/evidence fields and comparison data **in the main tables** because that is their function. Other future specialist registers may use the same exception **only when deliberately identified as such**.

**Structural exceptions:** `world/CONSISTENCY_LEDGER.md`, `world/CHRONOLOGY.md` (the source-keyed reference timeline), `world/ENTITY_SCHEMA.md`, `world/entities.json`, compact navigation indexes and compatibility/redirect stubs may retain the editorial metadata and links needed to do their jobs. Index summaries should still be readable and avoid gratuitous ASR qualifiers. Focused history studies and the thematic `world/WORLD.md` **default to the narrative rule** unless a clearly delimited evidence table genuinely requires technical/source fields.

**Do not blanket-exempt all `world/` files merely because they currently contain E-numbers.** Classify each file by purpose, record a new exception in the [migration manifest](WORLD_ARC_MIGRATION_MANIFEST.md) if necessary, and keep one canonical subject page. The existence of a compatibility alias does not create a second canonical identity.

## 5. Migration and acceptance checks

For each existing article, preserve an exact **pre-edit working-copy archive** with correctly rebased links before substantial rewriting. Use one page or a very small bounded batch at a time. Reorder by **introduction → chronological arc development → current status last**, retain established identities/relationships and in-world uncertainty, and move research apparatus to **complete, reachable footnotes**.

Before claiming completion, check:

1. Main text (including headings and any opening metadata) has **no E### citations, ASR qualifiers, episode timing or editorial review language**. All essential evidence moved to correctly referenced footnotes.
2. Every `[^key]` reference has its definition; no orphan definitions; footnote links resolve. **Current status is the final substantive section** even though the definitions follow it.
3. All arc-relevant events and their **knowledge boundaries** remain accurate; disputed names and source conflicts remain documented in footnotes and appropriate central registers.
4. Existing canonical subject links, redirects and inbound anchors survive migration. Run applicable Markdownlint/document-link tests when available, and state clearly if not run.
5. Specialist registers and technical indexes have **not been forced into narrative prose** or deprived of the detailed source data on which they depend.

**Rollout:** Apply this style immediately to new ordinary world-reference writing. Existing articles receive bounded, preserved presentation and subject-focus passes under their own campaign’s cleanup plan. **Migration progress, outstanding subjects and acceptance results belong in the campaign’s plan and manifest**, not in this shared writing rule. The same contract applies to Delvers and Wastes; declaring the standard does not certify that every existing page meets it. Campaign-specific taxonomy, narrative boundaries and unresolved canon decisions remain in that campaign’s process.

## Delvers world and narrative

**Owner-directed extension, 2026-10-24:** This revised direction also governs `delvers/world/` and `delvers/narrative/`. Apply D-037's in-universe prose and footnotes, D-038's character focus and D-039's domain-specific subject focus to Delvers reference articles. Introduce each subject as first encountered, follow meaningful chronological phases, and finish with **Current status** (or **Lasting legacy** for a historical study). Use Delvers phases rather than importing Wastes arc numbers or boundaries. Preserve natural attribution of claims and private knowledge; put episode IDs, clocks, spelling alternatives, source horizon and verification limits in footnotes. Keep Delvers continuity and evidence independent of Wastes and Inverse.

Delvers narratives remain **plot-led connected stories**, while reference pages explain their own subjects. **Completed-campaign application, 2026-10-28:** use the three primary arc accounts in the [narrative reading order](../delvers/narrative/README.md#primary-reading-order) and their implemented [chapter maps](DELVERS_NARRATIVE_CHAPTER_MAPS.md). The [First jobs study](../delvers/narrative/FIRST_JOBS.md) and other earlier detailed studies remain historical versions at their established paths; they are not an ongoing primary narrative or additional chapters after the first-arc synthesis. Follow the [editorial guide](EDITORIAL_GUIDE.md) for presentation and proportional reading weight. Do not pad scenes, invent transitions or impose Wastes arc boundaries or a fixed chapter count. Declare each reference article’s actual researched horizon in a source note, even when its last direct observation predates the Delvers finale. Campaign completion does not resolve uncertain testimony, identities or unperformed events.

Navigation indexes, source-keyed chronology, consistency ledger and deliberately identified specialist registers retain the metadata required for their purpose. Do not exempt thematic `WORLD.md` or ordinary profiles merely because their older versions contain research apparatus. Future writing follows this policy immediately. The [Delvers migration record](../reports/DELVERS_STYLE_EXTENSION_2026-10-24.md) records the bounded existing-page pass and exact working-copy preservation; this does not claim later episodes or audio have been researched.
