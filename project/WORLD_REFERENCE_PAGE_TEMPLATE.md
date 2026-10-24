# World reference page template

**Purpose:** A compact, source-linked *subject* page in `world/characters/`, `world/places/`, `world/technology/` or a major event study in `world/`. Use this as an editorial checklist, not a requirement to paste empty headings into every page. [Documentation architecture](DOCUMENTATION_ARCHITECTURE.md) · [World portal](../world/README.md).

## Recommended structure

```markdown
# Preferred display name — short distinguishing description

**Identity/type:** ... **Aliases:** ... (status and source).
**Spoilers:** ... **Evidence quality:** Processed ASR, not audio-verified
unless specific evidence has been independently checked.

## Introduction — at first appearance

Two or three concise paragraphs: the subject's broad nature, role and
condition as presented when first encountered (cite the episode). Describe
**then-current** location, relationships, known powers or ownership without
giving away later revelations, deaths, betrayals or changes of custody.
The page-level spoiler-horizon label above may identify the last researched
episode; it is NOT a summary of that ending.

## Development by arc

### Arc One — ... (E###–E###)
Meaningful changes in played order, with supporting episode links.

### Arc Two — ... (E###–E###)
Include only arcs where this subject actually develops. Add later arcs as
relevant, placing disclosures where learned, not at the earlier event date.
Historical prequels and bonus commentary are separately identified.

## Relationships, locations, powers or ownership (optional)

Enduring relationships, ownership/ability distinctions and cross-links
that aren't already conveyed by the arc summaries. Keep this section
before the final status, or omit it for simple/short entries.

## Current status — end of Season One (E128)

The **final substantive section** states the latest directly demonstrated
condition as known at the researched cutoff; if the subject last appears
earlier, name that episode and distinguish "last seen" from confirmed
later survival/death. Include current location, relationships, custody,
known abilities and remaining disputes only where relevant. Summarize
open questions here, linking the consistency ledger and review queue;
provide source dossier and related-page links here and inline above.
**Do not put another story section after current status.**
```

## Canon and sourcing rules

1. **Reference scope:** This is *The Wastes*. *Inverse* and the E043 one-shot are independent unless a source explicitly establishes a shared continuity. E107–E109 are a **same-world historical prequel**, not the current Arc Five.
2. **One main subject page:** Category indexes link to the page and offer a brief description; don't append E### recaps to `CHARACTERS.md`, `PLACES.md`, `WORLD.md`, or the root world portal.
3. **Introduction → arcs → current status:** The first section describes the subject and condition **at initial introduction**, even when the metadata spoiler horizon is later. Arc sections reveal changes **when learned**. The **last substantive section reports the latest observed state**, including unresolved questions. When the party first **believed** Angelashi dead E048 but **freed her alive** E054, preserve both observations in chronological order. E081's declaration of the party's death and their E082 return likewise coexist.
4. **Source tier:** Directly played event; GM statement to players; GM/cast retrospective; in-character testimony; private handout/vision; processed ASR only; owner- or cast-confirmed orthography; external wiki reference. Never elevate testimony or an unplayed GM plan into an observed event.
5. **Identity:** Distinguish actor/performance from fictional person, individuals from claimed aliases, singular artifacts from ASR misspellings. **Diontalus** and **Eye of Groxl** follow recorded owner spelling decisions. Unconfirmed names retain '(?)' and alternative forms.
6. **Distinct agents:** When separate supernatural characters occupy the same body, give each a primary profile and distinguish whose acts, memories and motives are observed. Stanley and Diontalus have separate canonical pages; the former combined-page URL remains a short compatibility page linking to both.
7. **Items:** Acquisition, transfers, loss, charges, attunement, power *read-out* and **actually demonstrated power** have different evidence thresholds. Distinguish the Hand, Eye of Voice, Eye of Groxl, Fist gauntlet, CHIDS portal device and Traversal Drive.
8. **Cross-links:** Link first occurrences of related major subjects and episode dossiers using paths relative to the **new file's own directory**. Update inbound links when changing a slug. Don't copy source transcript text into the encyclopedia.
9. **Archival:** Before shortening an established, long-lived index, preserve its pre-edit working research in `research/legacy/` with source links **rebased**. Historical snapshots are not parallel authorities; source transcriptions remain untouched.
10. **Check before completion:** Validate that **the opening description is introduction-time accurate and does not reveal future outcomes**, all materially relevant arcs appear in proper order, **current status is the final substantive section**, and its claims match latest played evidence. Also check local Markdown links, duplicate slugs, preserved anchors, stale horizon/status language, affected Markdown lint and repository canonical checks when available. Never claim external audio verification without listening.

## Category ownership

- `world/CHARACTERS.md`: people; `world/ANTAGONISTS.md`: a *role-based index* linking the same people, not duplicated pages.
- `world/PLACES.md`: places (including mobile locations), with major sites under `world/places/`.
- `world/ITEMS_AND_ARTIFACTS.md`: relics, weapons, devices and identified technologies, with substantial subjects under `world/technology/`.
- `world/HISTORICAL_EVENTS.md`: major event index and focused historical studies. `CHRONOLOGY.md` retains the unique, episode-ordered reference timeline.
- `world/FACTIONS_AND_POWERS.md`: organizations and disputed powers.
- `world/WORLD.md`: stable thematic context and uncertain cosmology, *not* the story-by-episode chronology.
