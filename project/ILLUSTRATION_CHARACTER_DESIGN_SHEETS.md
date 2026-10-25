# Recurring-character design sheets

**Established:** 2026-10-25. **Scope:** Recurring named characters likely to
appear in multiple project illustrations, across The Wastes, Inverse and Delvers.
This is a visual-production protocol, **not** a new source of story canon.
Follow the [style and continuity guide](ILLUSTRATION_GUIDE.md), the
[active canonical character-sheet workflow](../.agents/skills/twbd-illustration-generate/CHARACTER_SHEET.md),
    [reusable prompts and attached-image playbook](../.agents/skills/twbd-illustration-generate/CHARACTER_SHEET_PROMPTS.md),
[historical progressive pilot plan](ILLUSTRATION_PROGRESSIVE_CHARACTER_SHEET_PLAN.md),
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
   Each completed page must be **1024 × 1024, sRGB PNG** following the project-wide
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
| Decision | **Per-anchor:** `*_DRAFTING`, `*_VISUAL_ACCEPTED`, `*_REGISTRATION_PENDING`, `*_APPROVED`; **combined sheet:** `sheet-needed`, `research-blocked`, `drafting`, `AWAITING_OWNER_REVIEW`, `OWNER_APPROVED`, `REVISION_NEEDED`, or `SUPERSEDED` — see [canonical workflow](../.agents/skills/twbd-illustration-generate/CHARACTER_SHEET.md) |
| Approval | **Explicit owner approval**, date, sheet version/file ID(s), accepted state scope and conditions; never infer approval from generation, a world-page image selection or a player's drawing |
| Impacts | Affected previously created illustrations and `IRV-####` issue links as necessary; preserve old art and prior sheet versions |

### Initial candidate

| Campaign / character | Sheet ID | Current state | Next action |
| --- | --- | --- | --- |
| The Wastes / [Stanley Billings](ILLUSTRATION_STANLEY_BILLINGS_REFERENCE.md) | `WASTES-STANLEY-BILLINGS-DS-001` (reserved; E001/A01 written reference **v0.6**, E023/A01B evidence-backed handlebar/goatee style) | **FACE_APPROVED** ([E001 face report](../reports/ILLUSTRATION_STANLEY_E001_FACE_ANCHOR_2026-10-25.md); [original plan](../reports/ILLUSTRATION_STANLEY_E001_SHEET_PLAN_2026-10-25.md)): owner accepted generation `cd259553-dace-43fb-9038-34946497674f` and requested continuation after receiving normalized PNG; the 1024×1024 sRGB derivative is now [in the repository](../illustrations/references/Stanley_Billings_E001_Face_v1_1024_sRGB.png), read back, and **hash-matched** (SHA-256 `3c315ea76096eb4253ba8504a0209e48fe00fc3dfab3d691d8d22e97630d1e4d`, ICC 588-byte sRGB); separate historic repo v0 face and sheet retained, not auto-approved; E023 Jon-played haircut confirms **curled Western moustache + small goatee + swept brown hair with shaved sides**, March 2019 Jon-approved Audie Norman facial-haired design **unmatched to exact file**, Diontalus E045 removes facial hair; E060 explicitly lacks moustache; separate S2E03 Unbreakable Majesty and S3 bare-mouth variant; **FACE_APPROVED and FRONT_APPROVED** ([front anchor registered with exact hash](../reports/ILLUSTRATION_STANLEY_E001_FRONT_ANCHOR_2026-10-25.md); two prior [rejected multiview attempts](../reports/ILLUSTRATION_STANLEY_E001_FRONT_ATTEMPTS_2026-10-25.md)). **SIDE_VISUAL_ACCEPTED / SIDE_REGISTRATION_PENDING** for both E001/A01 anatomical sides ([owner-approved paired image and exact derivative export plan](../reports/ILLUSTRATION_STANLEY_E001_SIDE_APPROVAL_2026-10-25.md)); the earlier [side attempts and root-cause report](../reports/ILLUSTRATION_STANLEY_E001_SIDE_ATTEMPTS_2026-10-25.md) remains historical; three subject-profile drafts (S01/S03/S04) rejected for recurrent **red brocade, gold piping, extra arm guards/pouches and sheathing inconsistencies**, with one earlier correction-call error (S02). New attempts `d1d70c6e-470a-4ed5-9bb2-dbeef2efb498` and `34ac72c6-b14c-4c90-a117-0583e2d32dce` are untagged 1254-square and not accepted. Approved face/front unchanged; back and complete sheet not approved | Owner accepted single front generation `fc3ab615-2c66-48b9-afb1-0b88fcbb0a43`. Its 1024×1024 ICC-tagged sRGB derivative [has been placed in repository](../illustrations/references/Stanley_Billings_E001_Front_v1_1024_sRGB.png), read back with exact SHA-256 `95b535fe5ccdc19ebde882d3725f24dd228da661288abfddf8a6fce75c1a8b0f`, and **FRONT_APPROVED**. **Next action: owner should place the three separately verified 1024-square sRGB PNGs (paired, anatomical left, anatomical right) at their exact paths in the [side approval report](../reports/ILLUSTRATION_STANLEY_E001_SIDE_APPROVAL_2026-10-25.md). Verify repository hashes, and only then mark `SIDE_APPROVED` and proceed to the separate BACK stage.** Historical caution: do not retry the same generative method solely because the user invokes the stage again. First switch to a **verifiably reference-conditioned edit of the exact approved front/face image** (or controlled manual orthographic construction), check the positive request description before rendering, and use a separate forbidden-feature QA checklist. All three rendered profile drafts are noncompliant **1254-square/untagged** and have invalid costume/rapier details; one correction call failed. See [full S01–S07 attempt history](../reports/ILLUSTRATION_STANLEY_E001_SIDE_ATTEMPTS_2026-10-25.md); S06 and S07 also produced outputs with no verified edit lineage (`edit_op:null` / `parent_gen_id:null`) despite approved local front-asset availability. They are rejected, and the reference-input capability gate remains blocked. The S05 attempted approved-pixel handoff showed the image in tool output but the generator still returned `edit_op:null` / `parent_gen_id:null` with an invented pouch and no verified edit/reference lineage; S05 is rejected as well. Requires explicit true image-input editing rather than contextual display. Existing generator request descriptions themselves included rejected details, while actual image conditioning was unverified; **stop rather than generate another unconditioned fantasy duelist**. Follow the new [turnaround gate](../.agents/skills/twbd-illustration-generate/CHARACTER_SHEET.md#1a-existing-anchor-turnaround-gate--no-text-only-character-reinvention). Owner's explicit paired-profile visual approval is now recorded; **repository byte/hash/profile readback of the paired file and two independent crops is still required for `SIDE_APPROVED`**. E023 groomed and later moustache-free Unbreakable Majesty states remain separate. No Stanley scene art or completed model sheet approved. |
| The Wastes / [Nash Maggard](ILLUSTRATION_NASH_MAGGARD_REFERENCE.md) | `WASTES-NASH-MAGGARD-DS-001` (reserved for E000/A01 baseline, written draft v0.11) | **drafting complete sheet**; [approved normalized E000 face anchor](../illustrations/references/Nash_Maggard_Face_v1_1024_sRGB.png) follows the [owner-preferred bald/bandaged adult-animation art direction](../reports/ILLUSTRATION_NASH_FACE_DIRECTION_2026-10-25.md); [written E000/A01 design-sheet brief](ILLUSTRATION_NASH_MAGGARD_REFERENCE.md#e000a01-character-design-sheet-brief--draft-v011-2026-10-25) integrated; [two nonconforming render attempts rejected](../reports/ILLUSTRATION_NASH_MAGGARD_DESIGN_SHEET_ATTEMPTS_2026-10-25.md); **FRONT_APPROVED** for owner-selected, repository-verified [`Nash_Maggard_Front_v1.png`](../illustrations/references/Nash_Maggard_Front_v1.png), **1024-square, sRGB-tagged**, exact SHA-256 matches validated derivative; original [`Nash_Maggard_Face_v1.png`](../illustrations/references/Nash_Maggard_Face_v1.png) remains untagged, but normalized [`Nash_Maggard_Face_v1_1024_sRGB.png`](../illustrations/references/Nash_Maggard_Face_v1_1024_sRGB.png) is **repo-verified and `FACE_APPROVED`** by owner; **SIDE_APPROVED:** corrected hood-up side v2 PNG verified in repo (1024-square sRGB; [side verification](../reports/ILLUSTRATION_NASH_SIDE_ANCHOR_2026-10-25.md)); **BACK_APPROVED:** rear 1024-square sRGB export now registered, hash-verified and owner-approved ([back report](../reports/ILLUSTRATION_NASH_BACK_ANCHOR_2026-10-25.md)); old hood-down pair superseded due to nail discontinuity; **two-page, text-free composite generated from approved anchors and technically inspected** ([assembly report](../reports/ILLUSTRATION_NASH_E000_SHEET_ASSEMBLY_2026-10-25.md)); **complete sheet `AWAITING_OWNER_REVIEW`, not approved** | Next production step: **All four anchor views are owner-approved, in-repository and hash-verified**. The two-page, text-free sheet candidate was **assembled and checked locally**; next have owner review [page 1 and page 2](../reports/ILLUSTRATION_NASH_E000_SHEET_ASSEMBLY_2026-10-25.md), then register the exact PNGs in `illustrations/references/`, verify hashes, and **only then mark the complete sheet `OWNER_APPROVED`**. Preserve **house style v2**: bald/no long hair, substantial but **stylized healed-burn facial scarring**, concealing head/face wraps, red/sightless eye on Nash's **left**, organic blister/pustule remnants, rather than generic rugged beard or photoreal gore; later full-body/prop anchors must show **Freedom as an actual nail hammered transversely through the upper wooden shaft**, with head and point sticking out of opposite sides—not a tip ornament or fantasy hook, disclosed in E018 and provisionally applicable to E000; verify 1024-square PNG/sRGB and continuity before front/side/back or owner approval |

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

`$twbd-illustration-generate` distinguishes **design sheet** from **scene**.
For a design-sheet request it follows the [canonical phased workflow](../.agents/skills/twbd-illustration-generate/CHARACTER_SHEET.md): research brief →
face → front → side → back → **deterministic assembled sheet**. Each image
gets separate owner visual acceptance, technical export and repository
readback/hash checks before stage approval. An accepted source portrait,
full-body figure, or assembled layout **does not automatically approve the
entire multi-view sheet**; the actual final page(s) need separate explicit
owner approval and verified repository registration.
For a scene request, it requires the applicable approved sheet(s), checks
versions and states, uses their **actual pixels as visual inputs when possible**,
and compares the output to the written references and existing art. If a
necessary sheet is absent, it stops, records the need here, and gives the
requester the exact next sheet request. Generating a sheet never
automatically resumes a previously blocked scene.
