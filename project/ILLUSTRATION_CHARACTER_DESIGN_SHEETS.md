# Recurring-character design sheets

**Established:** 2026-10-25. **Scope:** Recurring named characters likely to
appear in multiple project illustrations, across The Wastes, Inverse and Delvers.
This is a visual-production protocol, **not** a new source of story canon.
Follow the [style and continuity guide](ILLUSTRATION_GUIDE.md), the
[progressive-anchor character-sheet implementation plan](ILLUSTRATION_PROGRESSIVE_CHARACTER_SHEET_PLAN.md),
[appearance register](ILLUSTRATION_REFERENCES.md), the
[subject template](ILLUSTRATION_SUBJECT_TEMPLATE.md), and
[image rights policy](IMAGE_ASSETS.md). Keep the campaigns separate.

## Sheet-first gate

An identifiable character who already recurs, or is reasonably expected to
appear in **two or more planned illustrations**, needs a **character design
sheet before any new scene/portrait/group illustration featuring that character**.
This includes recurring NPCs and companions; it does not include incidental,
anonymous figures. If a previously one-off character becomes recurring, pause
further scene illustration until a sheet has been approved. Do not invent a
recurrence prediction merely to block a truly isolated one-off illustration.
This policy is prospective: existing selected illustrations are preserved, not
retroactively invalidated solely because no sheet existed when they were made.

For a scene illustration, check an **owner-approved baseline design sheet**
and, when applicable, an approved or explicitly reconciled appearance-state
variant for **each recurring character in the image**. A provisional, generated,
artist-supplied or merely selected reference is not automatically an approved
sheet. A character's sheet may be created as an initial *draft* only after the
normal integrated, time-specific source-research gate passes; approval is a
**separate subsequent decision**. Do not use a sheet's missing approval as a
reason to bypass research or generate a generic character. A requested
design-sheet illustration is exempt only from the requirement to already
possess an approved design sheet, not from source research, art style, image
technical verification, or reference inspection.

**Missing source research:** Log an `IRQ-####` blocker in
[ILLUSTRATION_RESEARCH_QUEUE.md](ILLUSTRATION_RESEARCH_QUEUE.md) and stop before
any image generation. **Research is complete but no approved sheet:** log/update
the subject's entry in this registry as `sheet-needed`, `drafting` or
`awaiting-owner-review`. Do **not** misuse the source-research queue as an
art-approval queue. No scene render until sheet approval is recorded. If a
required approved sheet exists but cannot be inspected or its defining features
are not recorded, stop and report the access/continuity blocker. Failed writes
must be disclosed; never claim an approval or persistent status that was not
saved.

## Design-sheet contents

Every sheet has **two linked artifacts**:

1. **Structured written character design specification**, saved in the
   character's integrated appearance reference (or a linked dedicated file).
   Record campaign and ID, source/version/verification, introduction-era
   baseline, story applicability, proportions and silhouette, face, hair,
   skin/markings/scars, expression range, posture, left/right asymmetry,
   standard visible clothes and equipment, swatches/underlying colors,
   material textures, mandatory features/exclusions, alternative forms,
   uncertainty and explicitly chosen artistic interpretations. Record exact
   image-source provenance and distinguish creator/player intent, fan art,
   final-campaign JSON and played narration. D&D Beyond JSON is a
   **campaign-end snapshot**; never backdate its traits or items.
2. **Visual reference PNG**: neutral full-body **front, profile and back**
   views with matched proportions and scale; when the 1024-square space
   permits, an enlarged three-quarter face, expression details, key equipment
   close-up and compact color swatches. Use consistent facial anatomy and
   clothing details from view to view; do not mirror asymmetric features.
   The full sheet must be one **1024 × 1024, sRGB PNG** using the project-wide
   immutable graphic-novel style prompt. Keep labels, citations and annotations
   in the **companion written specification**, not on the image; the
   no-incidental-text/no-decorative-frames style rule remains in force.
   If every useful view cannot fit legibly, create **multiple separately
   validated square pages** under the same sheet ID/version; do not widen
   the canvas, crop defining traits or shrink every figure beyond use.

Show-specific descriptions take precedence over artistic choices. Original
creator/player artwork (for example Scott Johnson's Nash designs) is a
high-value **intent reference** with its own source role, never proof of when
an undated feature existed. Existing project art may anchor established
artistic decisions but cannot override a contradicted episode description.
Record conflicts, never blend incompatible versions to hide uncertainty.

## Chronology and variants

The **baseline** must be the earliest sufficiently researched appearance, not
the character's final character-sheet build. Keep persistent identity separate
from period-specific clothing, gear, bodily changes, injuries, magical forms,
disguises and lighting. Each major source-supported change gets a linked
**variant** with its applicable stable appearance-state ID and explicit
`carry forward / change / exclude` instructions. Reuse an approved baseline
for unchanged features; do not draw a late variant into an earlier flashback.
Minor ephemeral mud, posture or lighting can be documented in the scene brief
rather than requiring another sheet. A major transformed form may need a
separate sheet page or approved variant before repeated use.

A baseline's **approval does not approve all future appearance variants**.
Approve significant variant imagery individually, or document an explicit
owner-approved written variation that can be reliably rendered using the
baseline sheet. An artistic/design-only update increments the sheet version;
a supported change to historical appearance states also updates the
source-linked subject reference. Never silently replace an approved version.

## Identifiers, files and approval ledger

Use stable, campaign-qualified IDs (example:
`WASTES-NASH-MAGGARD-DS-001`) and state IDs already recorded in the subject
reference. Prefer verified paths such as
`illustrations/wastes/nash-maggard-design-sheet-a01.png`; a suggested filename
is **not** an assertion that the asset exists. A sheet entry records:

| Field | Required record |
| --- | --- |
| Character and campaign | Stable subject ID and link to written reference |
| Sheet ID, version, state | Stable `-DS-###`, version/date, introduction/baseline state or variant, valid story interval |
| Asset(s) | Verified path(s) and original/actual 1024-square PNG sRGB checks; no imaginary links |
| Research inputs | Evidence IDs, transcript and image sources, exact guide/reference versions, known conflicts |
| Design and continuity | Source-mandated traits vs artistic choices, viewpoint/asymmetry, known state changes, excluded late traits |
| Generation provenance | Exact prompt, reference images actually inspected vs supplied to renderer, output identity, inspection results |
| Decision | `sheet-needed`, `research-blocked`, `drafting`, `awaiting-owner-review`, `owner-approved`, `revision-needed`, or `superseded` |
| Approval | **Explicit owner approval**, date, sheet version/file ID(s), accepted state scope and conditions; never infer approval from generation, a world-page image selection or a player's drawing |
| Impacts | Affected previously created illustrations and `IRV-####` issue links as necessary; preserve old art and prior sheet versions |

### Initial candidate

| Campaign / character | Sheet ID | Current state | Next action |
| --- | --- | --- | --- |
| The Wastes / [Nash Maggard](ILLUSTRATION_NASH_MAGGARD_REFERENCE.md) | `WASTES-NASH-MAGGARD-DS-001` (reserved for E000/A01 baseline, written draft v0.10) | **drafting complete sheet**; [approved normalized E000 face anchor](../illustrations/references/Nash_Maggard_Face_v1_1024_sRGB.png) follows the [owner-preferred bald/bandaged adult-animation art direction](../reports/ILLUSTRATION_NASH_FACE_DIRECTION_2026-10-25.md); [written E000/A01 design-sheet brief](ILLUSTRATION_NASH_MAGGARD_REFERENCE.md#e000a01-character-design-sheet-brief--draft-v010-2026-10-25) integrated; [two nonconforming render attempts rejected](../reports/ILLUSTRATION_NASH_MAGGARD_DESIGN_SHEET_ATTEMPTS_2026-10-25.md); **FRONT_APPROVED** for owner-selected, repository-verified [`Nash_Maggard_Front_v1.png`](../illustrations/references/Nash_Maggard_Front_v1.png), **1024-square, sRGB-tagged**, exact SHA-256 matches validated derivative; original [`Nash_Maggard_Face_v1.png`](../illustrations/references/Nash_Maggard_Face_v1.png) remains untagged, but normalized [`Nash_Maggard_Face_v1_1024_sRGB.png`](../illustrations/references/Nash_Maggard_Face_v1_1024_sRGB.png) is **repo-verified and `FACE_APPROVED`** by owner; **SIDE_APPROVED:** corrected hood-up side v2 PNG verified in repo (1024-square sRGB; [side verification](../reports/ILLUSTRATION_NASH_SIDE_ANCHOR_2026-10-25.md)); **BACK_APPROVED:** rear 1024-square sRGB export now registered, hash-verified and owner-approved ([back report](../reports/ILLUSTRATION_NASH_BACK_ANCHOR_2026-10-25.md)); old hood-down pair superseded due to nail discontinuity; **complete multi-view sheet remains unapproved** | Next production step: **All four anchor views are owner-approved, in-repository and hash-verified**. Next compose final text-free one- or two-page sheet from the actual accepted face, front, side and back images; review consistency, size and sRGB before separately requesting complete-sheet owner approval. Preserve **house style v2**: bald/no long hair, substantial but **stylized healed-burn facial scarring**, concealing head/face wraps, red/sightless eye on Nash's **left**, organic blister/pustule remnants, rather than generic rugged beard or photoreal gore; later full-body/prop anchors must show **Freedom as an actual nail hammered transversely through the upper wooden shaft**, with head and point sticking out of opposite sides—not a tip ornament or fantasy hook, disclosed in E018 and provisionally applicable to E000; verify 1024-square PNG/sRGB and continuity before front/side/back or owner approval |

Do not confuse this example candidate with a complete register of recurring
characters. Add others when their recurrence and scene-illustration need are
established; maintain their entries here and cross-link their subject records.
If an approved sheet later conflicts with a meaningful finding, update the
source reference, mark `revision-needed`, create/link specific `IRV-` entries
for *existing* affected images and sheets, and ask the owner to review a new
version. Differences legitimately caused by time or form are not defects.
**Never** silently regenerate, overwrite, revoke approval or re-embed assets.

## Workflow handoff

`$twbd-illustration-research` determines recurrence, gathers visual evidence,
documents the initial state, identifies outstanding unknowns and prepares a
**design-sheet brief** within the integrated subject reference. It checks
existing illustrations for conflicts and records `IRV-` findings, but
**does not generate or approve** any sheet.

`$twbd-illustration-generate` first distinguishes **design sheet** from
**scene illustration**. For an eligible sheet request it uses the integrated
research, creates and validates a multi-view sheet, records a draft and obtains
**explicit owner review** before changing status to `owner-approved`.
For a scene request, it requires the applicable approved sheet(s), checks
versions and states, uses their **actual pixels as visual inputs when possible**,
and compares the output to the written references and existing art. If a
necessary sheet is absent, it stops, records the need here, and gives the
requester the exact next sheet request. Generating a sheet never
automatically resumes a previously blocked scene.
