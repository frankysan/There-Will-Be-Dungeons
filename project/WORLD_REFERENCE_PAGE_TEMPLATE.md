# World reference page template

**Purpose:** A compact, **in-universe and narrative-focused** subject page in `world/characters/`, `world/places/`, `world/technology/` or a major event study in `world/`. **The governing presentation rule is [World narrative style](WORLD_NARRATIVE_STYLE.md): put episode IDs, ASR uncertainty, source links and editor notes in footnotes, not the main prose.** Use this template as a checklist, not a demand for empty headings. [Documentation architecture](DOCUMENTATION_ARCHITECTURE.md) · [World portal](../world/README.md).

## Recommended structure

```markdown
# Preferred display name — short in-world description

## Introduction

Describe the subject's nature, role and condition at its first
appearance, without revealing later discoveries or final outcomes.
Let the relevant sources appear in footnotes, not in the prose.[^intro]

## Development by arc

### Arc One — the early journey

Tell the material developments in a connected, in-universe account.
Include only arcs in which the subject meaningfully appears.[^early]

### Arc Five — the later struggle

Preserve what the characters believed and learned at each point.
Attribute uncertain in-world claims naturally; move source/ASR
disagreement, episode numbers and research commentary to notes.[^late]

## Relationships and abilities (optional)

Add only lasting information not already clear from the story.

## Current status

Describe the last known condition, location, relationships and
unresolved in-world fate. This is the last narrative section.[^status]

[^intro]: [Introduction dossier](../../episodes/E001.md).
    Page research horizon and source quality may be recorded here.
[^early]: [Supporting episode](../../episodes/E027.md).
[^late]: [Later episode](../../episodes/E126.md).
    Record exact ASR alternatives and provenance where necessary.
[^status]: [Final researched appearance](../../episodes/E128.md).
    Link unresolved research to the consistency ledger/review queue.
```

**These episode links illustrate footnote placement, not a required episode range for every subject.** The `## Current status` heading must remain the **last substantive heading**; footnote definitions may follow it without another heading. Keep in-text arc labels as navigation, but no `E###` references or review terminology in the main text. For the full rules and register exceptions, see [World narrative style](WORLD_NARRATIVE_STYLE.md).

## Canon and sourcing rules

1. **Reference scope:** This is *The Wastes*. *Inverse* and the E043 one-shot are independent unless a source explicitly establishes a shared continuity. E107–E109 are a **same-world historical prequel**, not the current Arc Five.
2. **One main subject page:** Category indexes link to the page and offer a brief description; don't append E### recaps to `CHARACTERS.md`, `PLACES.md`, `WORLD.md`, or the root world portal.
3. **Introduction → arcs → current status:** The first section describes the subject as originally encountered, with **no future spoilers or research apparatus**. Narrate chronological arc changes as in-world events; keep the **latest status as the last substantive section**, with supporting episode cutoffs in footnotes. Earlier false beliefs and later revelations both remain visible in proper narrative order.
4. **Source tier:** Directly played event; GM statement to players; GM/cast retrospective; in-character testimony; private handout/vision; processed ASR only; owner- or cast-confirmed orthography; external wiki reference. Preserve this classification **in footnotes**; in the narrative, distinguish witnessed actions from what characters *say, believe or promise*. Never elevate testimony or an unplayed plan into an observed event.
5. **Identity:** Distinguish actor/performance from fictional person, individuals from claimed aliases, singular artifacts from ASR misspellings. Use curated forms such as **Diontalus**, **Eye of Groxl** and **Eltanfawr** in the main narrative where established by owner decisions. Put uncertain alternate spellings and `(?)` markers **in notes**, or describe an unnamed subject naturally until evidence supports naming it.
6. **Distinct agents:** When separate supernatural characters occupy the same body, give each a primary profile and distinguish whose acts, memories and motives are observed. Stanley and Diontalus have separate canonical pages; the former combined-page URL remains a short compatibility page linking to both.
7. **Items:** Acquisition, transfers, loss, charges, attunement, power *read-out* and **actually demonstrated power** have different evidence thresholds. Distinguish the Hand, Eye of Voice, Eye of Groxl, Fist gauntlet, CHIDS portal device and Traversal Drive.
8. **Cross-links:** Link major **in-world subjects naturally** in the prose. Put episode dossiers, source reports, editorial decisions and review queues **in footnotes** linked relative to the page's directory. Maintain stable links and inbound anchors when changing slugs. Don't copy source transcript text into the encyclopedia.
9. **Archival:** Before shortening an established, long-lived index, preserve its pre-edit working research in `research/legacy/` with source links **rebased**. Historical snapshots are not parallel authorities; source transcriptions remain untouched.
10. **Check before completion:** Validate the introduction-time viewpoint, ordered relevant arcs and final current status. Search **the main text and headings** for E-numbers, ASR/GM/player terminology, editorial qualifiers, uncertain `(?)` spellings and episode/source links; move research metadata to relevant footnotes. Verify that **every note reference has a definition**, no orphan definitions exist, source links and inbound anchors survive, and real chronology/knowledge boundaries remain accurate. Run available Markdownlint/link/repository checks where possible; never claim audio verification without listening.

## Category ownership

- `world/CHARACTERS.md`: people; `world/ANTAGONISTS.md`: a *role-based index* linking the same people, not duplicated pages.
- `world/PLACES.md`: places (including mobile locations), with major sites under `world/places/`.
- `world/ITEMS_AND_ARTIFACTS.md`: relics, weapons, devices and identified technologies, with substantial subjects under `world/technology/`.
- `world/HISTORICAL_EVENTS.md`: major event index and focused historical studies. `CHRONOLOGY.md` retains the unique, episode-ordered reference timeline.
- `world/FACTIONS_AND_POWERS.md`: organizations and disputed powers.
- `world/WORLD.md`: stable thematic context and uncertain cosmology, *not* the story-by-episode chronology.
