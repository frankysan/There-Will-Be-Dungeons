# World reference page template

**Purpose:** A compact, source-linked *subject* page in `world/characters/`, `world/places/`, `world/technology/` or a major event study in `world/`. Use this as an editorial checklist, not a requirement to paste empty headings into every page. [Documentation architecture](DOCUMENTATION_ARCHITECTURE.md) · [World portal](../world/README.md).

## Recommended structure

```markdown
# Preferred display name — short distinguishing description

**Identity/type:** ... **Aliases:** ... (status and source).
**Spoilers:** ... **Evidence quality:** Processed ASR, not audio-verified
unless specific evidence has been independently checked.

## Overview

Two or three paragraphs: what is this subject and why does it matter?
State the last demonstrated condition (and as-of episode), not just an
early-arc snapshot. Use links to other subjects, not repeated biographies.

## Development and observed events

### Early history or introduction
Timeline of 3–6 meaningful milestones, with episode links.

### Major change or current state
Later observations that revise earlier beliefs, clearly dated.

## Relationships, locations, powers or ownership

For people: relationships/organizations; for locations: sub-sites and
visitors; for artifacts: acquisition, custody, observed uses and stated
mechanical limitations; for events: participants, causes and aftermath.
Separate direct evidence from claimed mechanisms.

## Conflicting accounts and open questions

A short list or paragraph: witnesses, interpretations, disputed names,
unknown final states. Link to the existing consistency ledger and
review queue, avoiding a parallel unsynchronized issue tracker.

## Evidence and related reading

Specific episode dossiers, cast/GM bonuses when relevant, orthography
decisions and neighboring world subjects.
```

## Canon and sourcing rules

1. **Reference scope:** This is *The Wastes*. *Inverse* and the E043 one-shot are independent unless a source explicitly establishes a shared continuity. E107–E109 are a **same-world historical prequel**, not the current Arc Five.
2. **One main subject page:** Category indexes link to the page and offer a brief description; don't append E### recaps to `CHARACTERS.md`, `PLACES.md`, `WORLD.md`, or the root world portal.
3. **Spoiler horizon and time-of-knowledge:** When the party first **believed** Angelashi dead E048 but **freed her alive** E054, preserve both observations with their source cutoff. E081's declaration of the party's death and their E082 return likewise coexist.
4. **Source tier:** Directly played event; GM statement to players; GM/cast retrospective; in-character testimony; private handout/vision; processed ASR only; owner- or cast-confirmed orthography; external wiki reference. Never elevate testimony or an unplayed GM plan into an observed event.
5. **Identity:** Distinguish actor/performance from fictional person, individuals from claimed aliases, singular artifacts from ASR misspellings. **Diontalus** and **Eye of Groxl** follow recorded owner spelling decisions. Unconfirmed names retain '(?)' and alternative forms.
6. **Distinct agents:** When separate supernatural characters occupy the same body, give each a primary profile and distinguish whose acts, memories and motives are observed. Stanley and Diontalus have separate profiles despite the legacy Stanley URL slug.
7. **Items:** Acquisition, transfers, loss, charges, attunement, power *read-out* and **actually demonstrated power** have different evidence thresholds. Distinguish the Hand, Eye of Voice, Eye of Groxl, Fist gauntlet, CHIDS portal device and Traversal Drive.
8. **Cross-links:** Link first occurrences of related major subjects and episode dossiers using paths relative to the **new file's own directory**. Update inbound links when changing a slug. Don't copy source transcript text into the encyclopedia.
9. **Archival:** Before shortening an established, long-lived index, preserve its pre-edit working research in `research/legacy/` with source links **rebased**. Historical snapshots are not parallel authorities; source transcriptions remain untouched.
10. **Check before completion:** Local Markdown links, duplicate slugs, headings, stale horizon/status language, affected Markdown lint and repository canonical checks when available. Never claim external audio verification without listening.

## Category ownership

- `world/CHARACTERS.md`: people; `world/ANTAGONISTS.md`: a *role-based index* linking the same people, not duplicated pages.
- `world/PLACES.md`: places (including mobile locations), with major sites under `world/places/`.
- `world/ITEMS_AND_ARTIFACTS.md`: relics, weapons, devices and identified technologies, with substantial subjects under `world/technology/`.
- `world/HISTORICAL_EVENTS.md`: major event index and focused historical studies. `CHRONOLOGY.md` retains the unique, episode-ordered reference timeline.
- `world/FACTIONS_AND_POWERS.md`: organizations and disputed powers.
- `world/WORLD.md`: stable thematic context and uncertain cosmology, *not* the story-by-episode chronology.
