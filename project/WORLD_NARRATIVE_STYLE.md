# World-reference narrative style directive

**Status:** Archive-owner directive adopted 2026-10-24. **Scope:** Reader-facing prose throughout `world/`, particularly canonical character, place, artifact, faction and event histories. Read with [the world-reference template](WORLD_REFERENCE_PAGE_TEMPLATE.md), [documentation architecture](DOCUMENTATION_ARCHITECTURE.md) and [arc cleanup plan](WORLD_ARC_CLEANUP_PLAN.md). This directive governs **presentation**, not which sources count as evidence, and does not retroactively claim that existing pages already comply.

## 1. Default: an in-universe, narrative-focused main text

Write as an account of the **fictional world and its inhabitants**, in a fluent, coherent third-person narrative. Describe subjects **as first encountered**, then what happened through relevant arcs, then their **latest known in-world status at the end**. Prefer a continuous account of material developments over a series of transcript-processing notes or mechanics logs. Historical accounts may use the appropriate past tense; the latest-state section describes where the story leaves the subject.

**Do not put these in the main narrative**, including its opening metadata, subsection headings and closing status paragraphs:

- Corrected **episode identifiers** such as `E118`, recording clocks, cue identifiers, recording/publication dates, transcript basenames or URLs to episode research dossiers as visible link text.
- ASR/model names and disagreements, speculative spellings with `(?)` or transcription alternatives, listening priorities, confidence grades or repeated “audio not verified” warnings.
- Out-of-universe framing such as “the GM says,” “the player rolled,” “this episode ends,” “the party gains level 13,” source review instructions, or statements about how the archive was edited. Retain essential fictional consequences in ordinary prose rather than deleting them.
- Proposed-but-unplayed events written as completed history; a character's private knowledge presented as common knowledge; owner/creator retrospective plans presented as in-world facts.

**The arc labels may remain as an organizational aid** (`### Arc Five — The fall of Elhandar`), because readers asked to browse entries by arc. **Do not put episode ranges in the headings.** In-world temporal descriptions are welcome (“after the crash,” “during the siege,” “when the ships departed”). Avoid treating the five arc labels as literal in-world calendars.

Keep natural uncertainty where the **characters themselves** lack reliable knowledge: “The Soulbroker claimed the Principle had betrayed him,” “The others believed Angelashi dead,” “The villa was said to be capable of spaceflight.” These are meaningful parts of the story, not ASR uncertainty, and **must remain in the narrative**. Do not invent an objective fact, motive, quote, spelling or scene to make the narrative smoother.

## 2. Put research and verification in Markdown footnotes

Attach **Markdown footnote markers** near the sentence or paragraph they support. At the **bottom of the file**, place corresponding footnote definitions using the existing arc-narrative convention (`[^key]: ...`, with subsequent indented lines if necessary). Footnote definitions **do not form another narrative chapter**; the final substantive `##` heading remains **Current status**. Do **not** append a `## Sources` or `## Notes` section after Current status on standard subject pages.

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
in the hidden study of Villa Ornath. Its first described power
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

**Rollout:** Apply this style to **future** `world/` writing immediately, and to **existing subject pages during the planned arc-based cleanup**. The already migrated Nash, Elhandar and Eltanfawr pages now require a **second presentation pass**; their chronology, source archives and previous editorial work remain useful. This directive does not itself assert that those pages have been rewritten into this new style.
