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
2. **Visual reference PNG**: neutral full-body **front, paired anatomical left/right profiles (recommended), and back**
   views with matched proportions and scale. A single profile is acceptable when deliberately selected, but always record both anatomical side and facing direction; when the 1024-square space
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
| The Wastes / [Stanley Billings](ILLUSTRATION_STANLEY_BILLINGS_REFERENCE.md) | `WASTES-STANLEY-BILLINGS-DS-001` · E001/A01 baseline (written appearance reference v0.6) | **FINAL SHEET VISUALLY APPROVED / REPOSITORY REGISTRATION PENDING** — On 2026-10-25 the owner explicitly approved the two assembled, text-free 1024×1024 sRGB pages: four-view turnaround (SHA-256 `c476e8d2f7063f7e2588166d91464d245e329aab03baee40ca52436f3834d04b`) and full-size face (SHA-256 `8360a6e3720e8df495819a1e7338b1557feccbe162a436082cdf70323354b128`). **Do not mark `OWNER_APPROVED` yet**: the exact composite files are session-only and require repository upload/readback; rear anchor's misleading `_1024_` filename currently has a 1254-square IHDR, and a newly prepared compliant v2 derivative (session-only, SHA-256 `d3d3d1d658c01a089f5fd2b6485ac01d85ccdcfcd1bb4ee3a39e98b988d112c7`) still requires repository registration/readback. Existing `FACE_APPROVED`, `FRONT_APPROVED`, `SIDE_APPROVED` remain in effect. **SIDE LATERALITY CORRECTION (2026-10-26):** The old individual side filenames had Stanley's anatomical LEFT/RIGHT reversed. Approved paired illustration is unchanged: **image-left figure faces right (→) = anatomical RIGHT**; **image-right figure faces left (←) = anatomical LEFT**. Current byte-identical, repository SHA-256-verified v2 anchors are [`AnatomicalRight_Side`](../illustrations/references/Stanley_Billings_E001_AnatomicalRight_Side_v2_1024_sRGB.png) and [`AnatomicalLeft_Side`](../illustrations/references/Stanley_Billings_E001_AnatomicalLeft_Side_v2_1024_sRGB.png); original v1 names retained as aliases/provenance. [Correction audit](../reports/ILLUSTRATION_STANLEY_E001_SIDE_LATERALITY_CORRECTION_2026-10-26.md) / [`IRV-0004`](ILLUSTRATION_REVISION_QUEUE.md#irv-0004--stanley-e001-anatomical-profile-filenames-reversed). No art change or additional owner visual review needed for side anchors. [Final visual approval + technical gate report](../reports/ILLUSTRATION_STANLEY_E001_SHEET_FINAL_VISUAL_APPROVAL_2026-10-25.md), [face](../reports/ILLUSTRATION_STANLEY_E001_FACE_ANCHOR_2026-10-25.md), [front](../reports/ILLUSTRATION_STANLEY_E001_FRONT_ANCHOR_2026-10-25.md), [paired sides](../reports/ILLUSTRATION_STANLEY_E001_SIDE_APPROVAL_2026-10-25.md). | Upload **exact approved pages** to `illustrations/references/`, verify SHA-256, dimensions and embedded sRGB ICC by readback; register/read back prepared back v2 derivative separately, then promote the composite to `OWNER_APPROVED` with approval already recorded. Preserve prior rejected candidates and historical reports; no further generative redesign or new visual approval is needed unless the artwork changes. E023 groomed moustache/goatee and later moustache-free appearances remain independent story variants. |
| The Wastes / [Nash Maggard](ILLUSTRATION_NASH_MAGGARD_REFERENCE.md) | `WASTES-NASH-MAGGARD-DS-001` (reserved for E000/A01 baseline, written draft v0.11) | **drafting complete sheet**; [approved normalized E000 face anchor](../illustrations/references/Nash_Maggard_Face_v1_1024_sRGB.png) follows the [owner-preferred bald/bandaged adult-animation art direction](../reports/ILLUSTRATION_NASH_FACE_DIRECTION_2026-10-25.md); [written E000/A01 design-sheet brief](ILLUSTRATION_NASH_MAGGARD_REFERENCE.md#e000a01-character-design-sheet-brief--draft-v011-2026-10-25) integrated; [two nonconforming render attempts rejected](../reports/ILLUSTRATION_NASH_MAGGARD_DESIGN_SHEET_ATTEMPTS_2026-10-25.md); **FRONT_APPROVED** for owner-selected, repository-verified [`Nash_Maggard_Front_v1.png`](../illustrations/references/Nash_Maggard_Front_v1.png), **1024-square, sRGB-tagged**, exact SHA-256 matches validated derivative; original [`Nash_Maggard_Face_v1.png`](../illustrations/references/Nash_Maggard_Face_v1.png) remains untagged, but normalized [`Nash_Maggard_Face_v1_1024_sRGB.png`](../illustrations/references/Nash_Maggard_Face_v1_1024_sRGB.png) is **repo-verified and `FACE_APPROVED`** by owner; **SIDE_APPROVED:** corrected hood-up side v2 PNG verified in repo (1024-square sRGB; [side verification](../reports/ILLUSTRATION_NASH_SIDE_ANCHOR_2026-10-25.md)); **BACK_APPROVED:** rear 1024-square sRGB export now registered, hash-verified and owner-approved ([back report](../reports/ILLUSTRATION_NASH_BACK_ANCHOR_2026-10-25.md)); old hood-down pair superseded due to nail discontinuity; **two-page, text-free composite generated from approved anchors and technically inspected** ([assembly report](../reports/ILLUSTRATION_NASH_E000_SHEET_ASSEMBLY_2026-10-25.md)); **complete sheet `AWAITING_OWNER_REVIEW`, not approved** | Next production step: **All four anchor views are owner-approved, in-repository and hash-verified**. The two-page, text-free sheet candidate was **assembled and checked locally**; next have owner review [page 1 and page 2](../reports/ILLUSTRATION_NASH_E000_SHEET_ASSEMBLY_2026-10-25.md), then register the exact PNGs in `illustrations/references/`, verify hashes, and **only then mark the complete sheet `OWNER_APPROVED`**. Preserve **house style v2**: bald/no long hair, substantial but **stylized healed-burn facial scarring**, concealing head/face wraps, red/sightless eye on Nash's **left**, organic blister/pustule remnants, rather than generic rugged beard or photoreal gore; later full-body/prop anchors must show **Freedom as an actual nail hammered transversely through the upper wooden shaft**, with head and point sticking out of opposite sides—not a tip ornament or fantasy hook, disclosed in E018 and provisionally applicable to E000; verify 1024-square PNG/sRGB and continuity before front/side/back or owner approval |
| The Wastes / [Vorel Rasvim Kurik](ILLUSTRATION_VOREL_REFERENCE.md) | `WASTES-VOREL-DS-001` · E000/E001/A01, [written v0.2 appearance research](ILLUSTRATION_VOREL_REFERENCE.md) | **PLAN APPROVED / FACE VISUALLY ACCEPTED / REGISTRATION PENDING**. The owner accepted the single-panel, text-free E001 portrait (generation `90016a5a-8a10-4983-bbe5-4d7d5863121e`) on 2026-10-26. A conforming **1024×1024 sRGB PNG** was prepared and independently checked (SHA-256 `d4b9dcbd54cf14f65dff5ef1cfafc2761d7254578a9ba4467636383dfac253d5`), but it is session-only; **not repository-registered / not yet `FACE_APPROVED`**. [Face audit](../reports/ILLUSTRATION_VOREL_E001_FACE_ACCEPTANCE_2026-10-26.md). Seven-foot unclothed muscular lizardfolk: **E001 player-confirmed golden scales**, GM-described **bronze-gold** (E017), particularly craggy back/upper head versus smoother chest. Long thick tapering tail and short fan-shaped occipital frill are owner-approved **provisional design choices**; early yellow eye color remains unverified. **No E053 prismatic color change or embedded Eye** in E001. | Next: Transfer the **exact owner-accepted, normalized face PNG** to `illustrations/references/` and read back its SHA-256, dimensions and embedded sRGB ICC; then mark `FACE_APPROVED`. Next phase is **single full-body front** referencing the actual accepted face image, followed by paired anatomical profiles, back and assembled sheets. Gold/bronze base is sourced; exact palette treatment remains open. |
| The Wastes / [Hope Akmenos](ILLUSTRATION_HOPE_AKMENOS_REFERENCE.md) | `WASTES-HOPE-AKMENOS-DS-001` · E001/A01 organic baseline (written reference v0.2) | **FACE_APPROVED** — owner's approved darker-maroon E001 face is [repository-registered](../illustrations/references/Hope_Akmenos_E001_Face_v1_1024_sRGB.png); binary readback verified **1,569,186 bytes**, 1024×1024 PNG/sRGB, SHA-256 `1ef34cf6f619757df4e51e0f12a151965f1ed3381506af1b1c06c65667d3c91d`. See [face acceptance and export audit](../reports/ILLUSTRATION_HOPE_E001_FACE_ACCEPTANCE_2026-10-25.md). [First FRONT attempt F01](../reports/ILLUSTRATION_HOPE_E001_FRONT_ATTEMPTS_2026-10-25.md) has now been **non-generatively salvaged by removing surrounding detail panels**, preserving its central full-body figure: see [panel-removal/validation report](../reports/ILLUSTRATION_HOPE_E001_FRONT_PANEL_SALVAGE_2026-10-25.md). **FRONT_APPROVED**: the owner accepted the exact [single-figure panel-free front](../illustrations/references/Hope_Akmenos_E001_Front_v1_PanelsRemoved_1024_sRGB.png). Its repository copy was read back and hash-verified: **1,244,152 bytes**, RGB PNG **1024 × 1024**, embedded **sRGB built-in** ICC, SHA-256 `8c19629c99f5111bc56735473d9024d31a6a289f4cd6961b4d428bad48a960e1`; see [acceptance and technical report](../reports/ILLUSTRATION_HOPE_E001_FRONT_PANEL_SALVAGE_2026-10-25.md). Pose remains slightly three-quarter with Hope's right hand on hip, a **deliberate owner-accepted exception** to strictly orthographic neutrality. The historical two-failure circuit breaker still prohibits simply repeating unconditioned generative attempts. E001 source establishes optimistic horned tiefling mechanic and workwear context; late-sheet maroon/purple/gold fields and existing Scott Johnson/Ron Tang/Casey Boyd drawings are **candidates**, not an approved early model. Exact height 5 ft 6 in (sheet) vs 5 ft 8 in (wiki) conflicts; hairstyle/horn shape are unselected. **Both original arms/legs and horns must be organic before E037–E038**. | **SIDE_APPROVED / REPOSITORY VERIFIED (2026-10-26; anatomical filenames corrected):** Owner accepted the E001 paired side drawing (generation `4b05d728-921f-4fdf-bba7-33fbc12db0d9`). Original is 1536×1024 **without ICC**, therefore not production-compliant. Three original session exports (paired 1024-square overview; full-size anatomical left and right 1024-square pages) passed PNG/RGB/sRGB ICC/dimensions/hash validation; their chosen corrected binaries are **now in `illustrations/references/` and SHA-256 verified by independent readback** on 2026-10-26. Exact checks and hashes: [side technical gate](../reports/ILLUSTRATION_HOPE_E001_SIDE_TECHNICAL_GATE_2026-10-25.md). **2026-10-26 owner correction:** The tool holster is consistently on Hope's anatomical RIGHT. The split-file **left/right names**, not the artwork, were reversed: right-facing (→) profile = anatomical RIGHT; left-facing (←) = anatomical LEFT. [`IRV-0003`](ILLUSTRATION_REVISION_QUEUE.md#irv-0003--hope-e001-side-views-anatomical-leftright-filenames-reversed-not-a-holster-error) is **resolved** as a label/metadata error. Byte-identical, corrected repository-verified names are `Hope_Akmenos_E001_Side_AnatomicalRight_v2_1024_sRGB.png` (old `Side_Left_v1` pixels) and `Hope_Akmenos_E001_Side_AnatomicalLeft_v2_1024_sRGB.png` (old `Side_Right_v1` pixels); hashes in the side technical report. The paired sheet art and all three assembled-page hashes remain unchanged. **BACK_APPROVED / REPOSITORY VERIFIED** — owner also accepted rear generation `1b7c8137-ddcc-42ea-9c55-5d7c622c7864`; the normalized 1024-square sRGB-tagged rear derivative was subsequently registered and its SHA-256 verified by repository readback. **THREE-PAGE DETERMINISTIC SHEET v1 `OWNER_APPROVED` on 2026-10-26** from owner-supplied front, paired sides, back and face: [assembly and checks](../reports/ILLUSTRATION_HOPE_E001_SHEET_ASSEMBLY_2026-10-26.md). All three pages passed 1024-square PNG/ICC inspection, and their **exact SHA-256 hashes were verified by binary readback from `illustrations/references/`** on 2026-10-26. The earlier IRV-0003 concern was **resolved without visual edits**, by correcting anatomical filename labels and the companion manifest. The owner **separately approved the three-page assembled sheet** on 2026-10-26; `SIDE_APPROVED`, `BACK_APPROVED` and completed-sheet **`OWNER_APPROVED`** are now recorded in the [final approval report](../reports/ILLUSTRATION_HOPE_E001_SHEET_FINAL_APPROVAL_2026-10-26.md). Scope is only E001/A01; future variants require independent research/design approval. The two approved face/front anchors are retained. Do not backdate later **LEFT** arm/leg/horn prostheses, forearm rocket, queen attire or **RIGHT** Hand of the Voice. **E088/A05 variant now needs a separate organic-restoration design:** new natural left arm and leg, no gun-bearing prosthetics, **older scars persist**, original inert body remains behind; E088 borrowed tunic/trousers differ from later black/gold tailoring and E089 practical armor. Kristen's ~5 ft 6 in spoken estimate agrees with the sheet; fan-wiki 5 ft 8 in is secondary/conflicting. Exact post-resurrection horn shape remains unverified. Early SRT sweep and horn-fitting verification remain research priorities, with unconfirmed features labeled choices. |

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
