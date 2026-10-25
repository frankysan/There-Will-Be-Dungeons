# Illustration research queue

**Established:** 2026-10-25. **Purpose:** Track source research that must be
completed **before** a requested TWBD illustration can be generated. This
is a dedicated **illustration preflight blocker ledger**, not the general
[episode/listening review queue](REVIEW_QUEUE.md), and not a list of
future art suggestions.

[Illustration guide](ILLUSTRATION_GUIDE.md) ·
[Subject appearance register](ILLUSTRATION_REFERENCES.md) ·
[Subject research skill](../.agents/skills/twbd-illustration-research/SKILL.md).
The separate generation skill installs at
`.agents/skills/twbd-illustration-generate/SKILL.md`.

## Hard-stop rule

**No preview, draft, reference sheet, edit, partial composition or final image
may be generated for a requested illustration when any required depicted
entity lacks a usable, integrated, time-specific appearance reference.**
First collect *all* missing or insufficiently researched entities, write or
update their entries in this ledger, verify the write succeeded, then tell
the requester which items are blocked and exactly what research is needed.
If the ledger cannot be written, **still do not generate**; report the
write failure and provide the proposed queue entries without falsely
claiming they were saved.

An entity is *ready for the requested depiction* only if the
[appearance register](ILLUSTRATION_REFERENCES.md) links an actual subject
record containing an identity/recognition baseline, source-linked visual
evidence, the required appearance state or justified state applicability,
and a drawable description with explicit must-preserve and must-not-appear
constraints for the requested story moment. ASR-provisional evidence can
qualify **if honestly labeled** and not so uncertain that the intended
defining features must be invented. Owner approval of an art design is
**not** a prerequisite for a first provisional draft; nor can an older
generated image substitute for missing research.

Count named/identifiable characters, creatures, places, vehicles, artifacts,
significant props and any specifically illustrated historical event as
required subjects. The requested main subject always counts. Generic,
non-distinctive scenery or incidental anonymous figures are not separate
subjects unless their visual identity or lore matters. Do not evade the
rule by renaming a known entity as generic scenery.

Missing reference, missing **relevant story state**, unresolved identity,
a material source contradiction, and inaccessible crucial source
documentation are all valid blocker reasons. A general `world/` biography,
fan art, an unintegrated transcript audit, a candidate design, or an
unrelated later-era appearance **does not by itself clear the gate**.

## Open requests

*No open requests.*

Each new active entry uses the structure below and the next unused,
monotonically increasing `IRQ-####` ID. Deduplicate by **campaign + stable
subject ID (or unresolved name) + required scene/state + specific research
gap**, and append additional blocked illustration IDs and request dates to
the existing entry rather than cloning it.

<!-- Queue entry structure (not a real request).
### IRQ-XXXX — <campaign> / <subject or provisional name>
- **Status:** queued | researching | blocked-access | resolved | cancelled
- **Opened / updated:** YYYY-MM-DD
- **Campaign / subject:** <campaign-qualified ID or unresolved name, aliases>
- **Blocked request(s):** <requested illustration ID/description, date, spoiler cutoff>
- **Needed scene/state:** <episode, narrative time, transformation, condition>
- **Missing or insufficient:** <specific visual features/state/source checks>
- **Evidence checked:** <links to existing subject record or "none", what was inspected>
- **Research action:** Run $twbd-illustration-research for <subject, exact scope>.
- **Resolution:** <source-backed reference path, state ID and version when ready;
  otherwise "pending">
- **History:** <append dated changes, do not erase prior requests>
-->

## Resolution and recheck

Research is completed by the **separate research skill**, which must
integrate its source-supported result in a dedicated subject appearance
record and index. The generation skill is not permitted to improvise
research in-place merely to bypass the queue. When that work is finished,
recheck the **specific illustration's** scene and every depicted subject;
change the relevant entry to `resolved`, recording the reference path,
state/version and verification status. Re-evaluate a previously blocked
request on a **new invocation**—a queue resolution is not an instruction
to create images automatically.

Preserve the history of resolved entries under `## Resolved requests`,
with their stable `IRQ-` IDs. A later contradiction may reopen the same
specific gap or create a new one if materially different. Distinguish
research clearance from **artistic selection**, which is reviewed
separately after generation.

## Resolved requests

### IRQ-0001 — The Wastes / Jimster's garage, Dusthill

- **Status:** resolved
- **Opened / updated:** 2026-10-25
- **Campaign / subject:** The Wastes; Jimster's garage/workshop in Dusthill (place; stable ID `WASTES-JIMSTERS-GARAGE`; names refer to the same documented working facility).
- **Blocked request(s):** 2026-10-25 — `$twbd-illustration-generate Wastes Fate 4 inside Jimster's garage in Dusthill, no people`; intended 1024 × 1024 illustration, no visible people; requested story-time cutoff not specified.
- **Needed scene/state:** The garage interior with Fate 4 physically present. Distinguish E067's retrospective pre-modification RV (`WASTES-FATE4-A00`), E001's last-monster-wheel construction (`A00A`), and the still-unfinished E005 build (`A00B`) from the completed E006 vehicle (`A01`); establish which is actually depicted inside the garage rather than presuming the unveiling occurred indoors.
- **Original research gap (now addressed):** No indexed, integrated **appearance reference for Jimster's garage** existed when the illustration was requested. Research the garage's supported spatial layout, workshop/entrance geometry and scale sufficient to contain the relevant RV, doors and surroundings, furnishings, tools, lighting and any unique visual features. Record which features are genuinely described and which must remain artistic choices. Resolve or explicitly separate the garage/workshop terminology and the requested vehicle's time/state before illustration.
- **Evidence checked:** [Dusthill world entry](../world/places/dusthill.md) notes a garage but does not describe its appearance. [E001 dossier](../episodes/E001.md) mentions a mechanical workshop; [E006 dossier](../episodes/E006.md) places the Bok Bok scene in Jimster's garage; [E067 dossier](../episodes/E067.md) locates a pre-modification Fate 4 in Jimster's garage during Hope's subjective interlude. [Fate 4 appearance reference](ILLUSTRATION_FATE4_REFERENCE.md#appearance-state-timeline) already covers vehicle states `A00`, `A00A`, `A00B`, and `A01`, but cannot substitute for a researched setting. These are existing dossier/reference findings, not a new primary transcript or audio audit.
- **Research performed:** Bounded E001/E005/E006/E067 direct transcript review, with targeted second-ASR comparisons in E001/E006/E067; four garage states integrated. No audio verification or selected model sheet.
- **Resolution:** 2026-10-25 — [garage reference v0.1](ILLUSTRATION_JIMSTERS_GARAGE_REFERENCE.md) integrated into the [appearance index](ILLUSTRATION_REFERENCES.md#wastes-jimsters-garage-in-dusthill). The recommended no-people composition is E001 garage `WASTES-JIMSTERS-GARAGE-A01` with Fate 4 `WASTES-FATE4-A00A`. Exact floorplan/connection of entrances is still a provisional artistic choice; the historical scene includes people, but the requested image excludes them. Any new generation request must recheck the references and select a depicted moment.
- **History:** 2026-10-25 — original illustration preflight blocked because the garage lacked research; Fate 4 already had a provisional state reference. The garage research was subsequently integrated and this queue item resolved. No image generated as part of research.

