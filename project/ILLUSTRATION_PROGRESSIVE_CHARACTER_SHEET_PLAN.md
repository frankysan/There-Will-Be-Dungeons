# Progressive character-design-sheet workflow — implementation plan

**Date:** 2026-10-25. **Status:** Recorded workflow proposal, **not yet an implemented skill or a successful illustration**. **First pilot:** Nash Maggard (`WASTES-NASH-MAGGARD-DS-001`, E000/`WASTES-NASH-MAGGARD-A01`). **Purpose:** Establish a reproducible, source-faithful character appearance through small, reviewable visual anchors rather than asking an image model to invent an entire populated design sheet in one request.

This is a planned **reusable character-sheet skill** which will complement, not replace, the existing [subject research skill](../.agents/skills/twbd-illustration-research/SKILL.md), [illustration generation skill](../.agents/skills/twbd-illustration-generate/SKILL.md), [style guide v0.6 / style lock v2](ILLUSTRATION_GUIDE.md), [sheet-first approval policy and ledger](ILLUSTRATION_CHARACTER_DESIGN_SHEETS.md), [written subject template](ILLUSTRATION_SUBJECT_TEMPLATE.md), [appearance register](ILLUSTRATION_REFERENCES.md) and [existing-art revision queue](ILLUSTRATION_REVISION_QUEUE.md). Those established source, chronology, rights, style and **1024 × 1024 PNG/sRGB** gates remain authoritative. This plan proposes finer-grained steps and additional records; **do not treat it as an authorization to render without passing existing gates**.

## Rationale and decision

Two initial [Nash design-sheet attempts](../reports/ILLUSTRATION_NASH_MAGGARD_DESIGN_SHEET_ATTEMPTS_2026-10-25.md) failed: they defaulted to a generic fantasy fighter/ranger, invented bows, swords and shields, overlooked Nash's eye/facial damage and staff/satchel, added extensive text, and returned **1536 × 1024** images rather than the project's **1024 × 1024** square. Generating a fully annotated sheet from scratch is therefore **not the default workflow**. Reduce the number of identity, clothing, viewpoint, layout and equipment decisions per generation. First lock an expressive face, then a complete front silhouette, then profile/side, then back, then assemble clean sheet pages from accepted visual anchors.

**Prefer controlled, non-generative compositing for final layout** when true accepted anchor pixels can be placed without distorting proportions; image-to-image assembly may be used only if exact identity is visibly preserved. Neither approach exempts the *final saved page* from the actual PNG/sRGB/dimension and continuity checks.

## Phase order and gates

| Phase | Draft output | Prerequisite | Acceptance / next step |
| --- | --- | --- | --- |
| 0. Research/design brief | Integrated written design specification only | Campaign/entity and time-specific evidence, existing art review | `BRIEF_READY`: sourced features, uncertainties, decisions and exclusions clear |
| 1. Face | Single neutral head/bust anchor | `BRIEF_READY` | Human review; record `FACE_APPROVED` before advancing |
| 2. Front | One neutral front full-body anchor | Approved face, same story-state reference | Human review; record `FRONT_APPROVED` |
| 3. Side/profile | One neutral side full-body anchor | Approved face and front | Human review; record `SIDE_APPROVED` |
| 4. Back | One neutral back full-body anchor | Approved front and side; same outfit and orientation | Human review; record `BACK_APPROVED` |
| 5. Layout | One or two text-free reference pages, each separate square PNG | All four approved anchors | Compare complete pages with anchors; `AWAITING_OWNER_REVIEW` |
| 6. Final approval | Versioned selected model sheet and registered applicable states | Technical, style, fidelity and human final review | **Explicit owner** approval of exact assets/version/state scope only; `OWNER_APPROVED` |

The primary default order is **face → front → side → back → complete sheet**. If the back is more important for a particular character, the human reviewer may explicitly change the side/back order; do not silently omit an essential view. Head-only creatures, nonhuman bodies or transformative forms may require an equivalent set of meaningful views, while preserving separate state IDs. This plan concerns **recurring characters**, not all places/vehicles.

A failed or rejected anchor is replaced **at its own phase**. Previously approved earlier anchors remain stable unless new evidence or a documented design decision invalidates them. Do not auto-run the entire series; each approved anchor becomes the actual next-stage visual reference after inspection and documented acceptance. **Anchor approval for progression is distinct from final owner approval of the whole character sheet**. Never mark a candidate as approved just because an automated checker reports PASS or because it was generated.

## Fixed inputs, uncertainty and prompt construction

**Phase 0 must freeze a versioned brief** with: `campaign`, `subject_id`, `sheet_id`, `state_id`, applicable story interval/cutoff, sourced mandatory traits and evidence IDs/verification, prohibited later-era traits, missing evidence/conflicts, creator/player/fan artwork provenance and permissions, provisional artistic choices with design-decision IDs, known asymmetric features (subject's left/right), intrinsic palette versus lighting, visible outfit and actual scene equipment versus inventory. Campaign-end D&D Beyond exports are **late snapshots**, not first-appearance evidence. If essential identity is unresearched, follow the research skill and persist an `IRQ-` blocker before generating.

Freeze an **identity lock** once the face is accepted. Record its version, specific features, eye/skin treatment, face proportions, whether a hood hides features, and any deliberately provisional side/orientation choice. Freeze a **silhouette/outfit lock** when the front is accepted: garment pieces, scale/build, palette, staff/prop designs, carried strap path, boots and sided details. Side/back phases must carry forward these locks rather than re-inventing a costume. Any material change makes a new version and triggers re-review of dependent anchors.

Every image-generation/edit request must combine, **in this order and without silently dropping sections**:

1. **Identity block:** exact campaign/subject, story state/cutoff, and unambiguous task as a *single reference view*, not a multi-panel character sheet.
2. **Sourced positive constraints:** visible physical traits, face/eyes/scars, clothing/gear only when established for the time.
3. **Provisional visual decisions:** selected palette/outfit/hair/hood/body details clearly labeled as artistic, not new narrative canon. Only selected carry-forward choices, never other-era details.
4. **Named phase/composition:** exactly one bust, front, strict profile or rear figure, neutral stance/background, full figure not cropped when relevant.
5. **Continuity anchors and exclusions:** specific accepted prior files/versions, what to retain/change/exclude, prohibition of genre-default equipment and later-state features; no added text/layout.
6. **The entire, verbatim immutable fixed style prompt block** from the generation skill's section 3B, including the **single 1024 × 1024, 1:1 PNG/sRGB** requirement; use square options in the renderer too. Do not replace this block with 'same style as before'.

For **every attempt**, preserve the **actual submitted prompt** and renderer options when exposed; don't infer that an internal or adapted tool definitely received the intended prompt. Differentiate a written *intended brief* from an *observed actual prompt*. Actual image-reference conditioning is strongly preferred; record reference pixels/IDs actually provided to the model separately from images merely inspected in research or described in text. If an indispensable reference cannot be inspected or made usable in a way that preserves critical identity, stop or explicitly record a blocked-access limitation; do not falsely claim image-conditioned consistency.

All anchor canvases, rejected trials, and final pages follow the project-square style convention; renders that return a wrong format/ratio or image with incidental captions, labels, stats, decorative borders, watermarks or extra gear are **not compliant project assets**. Do not simply stretch/crop to conceal failure.

## Phase-specific prompt tasks and approval checklist

### 1. Face close-up — identity lock

**Task template (prefix to the invariant style block):** 'One close-up/bust portrait of [subject] in [state]. Establish the face and eyes only. [Mandatory face details]. [Provisional hood/hair/skin-color choices]. Neutral simple background, single face clearly visible. No weapons or extra characters. Preserve [exact creator-intent details if supported] without backdating inferred era details. Exclude [later forms/equipment, generic heroic beauty, text or labels].'

**Accept only if:** recognizable non-generic identity, all source-required facial damage/features visible, correct eye count/functional contrast, no invented later traits; shadows/hood do not erase the face; project style lock and technical gates pass. A second small expression variant may be added after the primary face anchor is accepted, not used to avoid deciding the primary face. Any arbitrary left/right eye placement is recorded **as an artistic choice** until verified.

### 2. Front full-body — costume/silhouette lock

**Task template:** 'One complete, front-facing neutral standing character, head-to-boots, of [subject/state]. Use the approved face image [ID/version] as the exact face/eye/skin identity reference. Preserve [face lock]. Show [mandatory clothes/boots/props], with provisional [outfit/palette decisions]. Keep the entire figure readable, no other views/labels/layout, no invented swords, bows, shields, packs or magic gear. [Specific exclusions].'

**Accept only if:** face is consistent with the accepted face image, silhouette and anatomy are distinctive and plausible, staff/satchel/boots match applicable evidence, clothing and palette can be reproduced, no automatic RPG loadout or extra anatomy, full feet/head shown, style and format passes. Freeze the costume/gear/sided design decisions on acceptance.

### 3. Side/profile full-body — dimensional continuity

**Task template:** 'One strict [subject-side left/right] full-length side/profile neutral view of [subject/state], keeping the *same person and same actual garments* as [approved face and front anchor IDs]. Preserve proportions, head/eye treatment, hood edge, sleeve/boot structure, satchel strap, staff dimensions and all asymmetries. No added gear, no multi-view layout or text.'

**Accept only if:** profile head/silhouette is recognizably the same character, visual height/body ratios and clothing layering match the front, strap and carried items connect plausibly, side choice is logged, no mirroring/flip mistakes or design additions, style and format pass.

### 4. Back full-body — rear construction continuity

**Task template:** 'One strict full-length rear view of the same [subject/state] from [approved face/front/side IDs]. Show consistent back of hood/cape, garment seams, boots, strap/satchel, and carried staff where visible. No invented backpack, extra weapons or insignia, no text or multiple views.'

**Accept only if:** cape/hood and costume construction reconcile with approved front and side; satchel strap and carried objects are consistent; no unexpected new weapons/gear/body changes or mirrored asymmetry; style, dimensions and sRGB verified.

### 5. Final sheet — assemble instead of re-invent

**Default:** **two text-free 1024 × 1024 pages** when a single page crowds details:

- **Page 1:** front, side/profile and back at comparable full-body scale, with no labels or frames.
- **Page 2:** approved face close-up and selected expression(s), optional exact staff/satchel details and small unlabeled palette swatches, only where legible and genuinely useful.

A single page may be used if all views remain readable. Use approved **actual anchor images** as inputs or for deterministic placement; avoid freehand re-generation of their faces, outfits and proportions. If assembly must be rendered generatively, request **layout-only reuse of approved anchor designs** and recheck every detail. Companion Markdown contains panel identity, colors, sources, approval and ambiguity; the image pixels contain no narrative text, logos or decorative sheet typography. Each page has its own verified width/height, color handling, version and review.

**Accept only if:** no face or costume drift, matched size/orientation, correct image count and usable view detail, nothing added, no text, both page(s) technically pass. Mark a technically compliant layout **draft / awaiting owner review** until the owner explicitly accepts the exact page(s), version and story scope.

## Record schema and suggested skill interface

**Proposed skill name, not installed yet:** `twbd-character-sheet` (e.g. `$twbd-character-sheet Wastes "Nash Maggard" E000`). Subcommands/variants may include `plan`, `face`, `front`, `side`, `back`, `finalize`, `status` or `continue <sheet-id>`; names are provisional until implementation. **Resume from persisted state rather than redoing approved work.**

Suggested record fields:

```yaml
campaign: ...
subject_id: ...
sheet_id: ...
state_id: ...
story_scope: ...
source_reference_version: ...
style_guide_version: ...
mandatory_traits: []       # evidence IDs / verification recorded separately
explicit_exclusions: []
provisional_design_choices: []
accepted_identity_lock: {}  # face features, eye placement, version
accepted_outfit_lock: {}    # garment, silhouette, props, palette
anchor_images:              # each: stage, ID, exact path, version, approval
  face: null
  front: null
  side: null
  back: null
final_pages: []             # each page status and verified image identity
reference_inputs: []        # inspected versus truly passed to renderer
attempt_log: []             # prompt, settings, result, checks, reason
owner_approval: null        # only explicit owner decision, scope and date
next_step: ...
```

Track a compact per-anchor `carry_forward / change_later / exclude` matrix; do not silently copy unverified design decisions into new canon. Retain all former versions and source provenance when revising. Keep source research in the subject reference; maintain sheet and phase status in [the design-sheet ledger](ILLUSTRATION_CHARACTER_DESIGN_SHEETS.md); place attempts and actual prompts in a bounded dated report; place **specific pre-existing-image issues** in the `IRV-` ledger, and missing source research in `IRQ-` (approval waiting alone is **not** an `IRQ-` problem).

Suggested internal progression statuses: `BRIEF_READY`, `FACE_DRAFTING`, `FACE_APPROVED`, `FRONT_DRAFTING`, `FRONT_APPROVED`, `SIDE_DRAFTING`, `SIDE_APPROVED`, `BACK_DRAFTING`, `BACK_APPROVED`, `SHEET_LAYOUT_DRAFTING`, `AWAITING_OWNER_REVIEW`, `OWNER_APPROVED`, `REVISION_NEEDED`, `SUPERSEDED`. A rejected attempt retains its own failure reason but does **not** advance the stage. Missing research sets the independent `research-blocked` flag; missing owner approval is not a research failure. No automatic promotion by generation or metadata validation.

## Technical and operational hard gates

- **Before any render:** integrated state-correct research; known source/image provenance and access; appropriate approved previous-stage anchor; complete phase-specific prompt with **verbatim immutable style block**; explicit square request, 1024 pixels where tool supports it; ability to inspect and validate final image bytes. If these are missing, **stop** and record why.
- **After every render:** inspect actual pixels for facial and prop fidelity, no invented or temporally impossible details, approved identity/style continuity, text-free composition, and output technical attributes. Verify real **1024 × 1024 PNG and sRGB** in the saved file, not the prompt/tool claim. A non-square render is a failed attempt, not a usable intermediate asset for project selection; any safe correction requires separate inspection and provenance.
- **Acceptance:** the anchor may advance only after its review outcome is explicitly recorded, preferably with owner feedback at identity/silhouette checkpoints; *final sheet approval* requires an explicit owner statement covering actual files/version and temporal scope. Never assume the owner approved a draft from a request to generate one.
- **Failure handling:** log failed candidates, exact observed issue, and focused retry instructions. Do not stack multiple independent corrections in one iteration when it is possible to isolate the highest-impact failure. If the same stage repeatedly hallucinates a ranger/warrior costume, simplify to a closer crop, stronger identity reference or image editing rather than asking for a more elaborate sheet. Do not overwrite existing art or approvals.
- **Versioning:** if a change to an accepted face is made, revalidate dependent front/side/back/layout; changes to outfit revalidate side/back/layout. Preserve the old anchors and approvals, flag specific affected existing images when new evidence requires review.
- **Permissions and scopes:** do not publish/redistribute original creator/fan images without established rights. Selected references may retain separate rights status from generated assets. The rendered model sheet is a **visual production reference** and never transcript/source proof.
- **Validation:** inspect changed documentation links and Markdown; run focused tests/lint when an appropriate project check runner is available. Report `PASS`, `FAIL` or `NOT RUN` honestly; an InfinityDB-specific check tool is not a TWBD documentation check.

## Nash pilot: next actionable work (no generation included in this plan)

**Current:** E000/A01 written brief [v0.4](ILLUSTRATION_NASH_MAGGARD_REFERENCE.md) integrated; the [latest face-render review](../reports/ILLUSTRATION_NASH_FACE_DIRECTION_2026-10-25.md) establishes the **preferred working style** (bald, extensive stylized old burns, wraps over scalp/face, rust hood), **not an approved anchor**. The preferred session PNG was 1254 × 1254 without embedded ICC, so it cannot be selected as compliant without a distinct verified asset; sheet `WASTES-NASH-MAGGARD-DS-001` is **drafting, no valid PNG or owner approval**. Earlier generic ranger/fighter attempts are documented and rejected. **Staff identity correction (2026-10-25):** Scott's depicted hooked/pointed staff tip is specifically an **old nail**, called **“Freedom” by Nash in E018**. The later first-person account associates it with escaping the Solar Mines; do not equate it with the **different gun named Freedom in E014**. The E000 staff is narrated but the nail's attachment in that exact scene is a **provisional backward application** of E018 evidence, not direct opening narration. Later E073 shows the staff **broken**, with its nail-bearing portion retained as arcane focus. Preserve each state rather than assuming all later staff/finials are interchangeable.

**Next:** implement the reusable skill's minimal `plan/face/status` phases; explicitly use Scott's hooded sketch and colored image as **player-art intention**, not proof of an E000 costume. Produce **one technically compliant standalone face close-up** (not another automatic full-sheet redraw), using **house style lock v2** and the owner-preferred adult-animation simplification: bald/almost hairless head, deep old contracted burn-like scarring, irregular raised lesions, concealment bandages crossing the scalp and parts of face, no luxuriant beard or dangling head hair, two visibly differentiated eyes: **his own LEFT is the red, sightless/dormant eye** (viewer-right from directly in front), and his right is the seeing eye. The left-red placement is an **owner-fixed continuity choice, not source-verified anatomical laterality**. Depict **subdued early red** rather than the later E089+ intense glow. Under a provisionally rust-brown hood, maintain enough facial visibility to show pockmarks, scars, blisters and pustules. **Owner's interpretation of Scott's orange circles is damaged skin from heavy Solar Mines radiation, not decorative garment spots**, and wraps/bandages primarily **conceal his severe disfigurement**, not protect like armor or medical equipment. These material/intent readings are artistic hypotheses, not independently verified episode detail. Show no swords, bows, shields, ranger gear, armor loadout or on-image text. Request owner feedback after actual 1024-square, sRGB and style/source verification; only then proceed to front → side → back → final page(s). **Owner-added full-body anatomy detail (2026-10-25):** Nash's clothed trousers/drapery must be **flat in front with no genital bulge** (D09; reported early-episode dialogue, precise source not verified yet). **Two first front-view trials** generated multiview annotated sheets instead of a single front figure and omitted the staff; both remain drafts, not approved anchors. See [front attempt report](../reports/ILLUSTRATION_NASH_FRONT_ATTEMPTS_2026-10-25.md). Future front attempts must request a **single full-length figure without insets, text, rear view or panels**, avoiding the phrase 'character sheet' in the visual prompt. **For the later full-body and staff-detail anchors**, explicitly render a **plain worn staff tipped with an ordinary old metal nail “Freedom”**, small enough to remain an identifiable *nail* rather than a forged fantasy pick, axe, curved weapon blade, or jeweled finial; its attachment mechanism and exact shape remain artistic choices. The nail is not required in the **face-only** render. Do not retroactively depict the E098 Skyblinder bird ornament on the E000 staff. Companion Markdown identifies the nail/name; never print “Freedom” on the image.

**2026-10-25 asset-registration update:** The owner added two images to `illustrations/references/`. The existing preferred face-study file `Nash_Maggard_Face_v1.png` is **1254 × 1254 RGB with no embedded color profile** (SHA-256 `8fbb2e8ce113826c89b85cc461af8f3ba3eaa41cbfc435462e4395b0efdc025b`), so still **not `FACE_APPROVED`**. The `Nash_Maggard_Front_v1.png` asset is **1024 × 1024 RGB PNG, embedded sRGB ICC**, SHA-256 `cc60727f08492be9bf54c43da5c6de9694fbd1c89f95840521396f033ecf58d0`, matching the user's accepted previous export: **`FRONT_APPROVED` for E000/A01**. The *complete sheet* remains drafting. Before side/back production under this strict progressive workflow, normalize/register a distinct compliant face variant and secure face-anchor approval. See [front attempt/verification record](../reports/ILLUSTRATION_NASH_FRONT_ATTEMPTS_2026-10-25.md).

**2026-10-25 face-normalization update:** A copy of the repo's original
1254-square `Nash_Maggard_Face_v1.png` was resized without cropping to a
separate **1024 × 1024 sRGB-tagged PNG** at the *session-only* path
`/mnt/data/Nash_Maggard_Face_v1_1024_sRGB.png`, SHA-256
`93e82eff061afd08611d0e6cf4fe8dfd11058ed94985c8c10a9d42140947cb71`.
This export passed metadata and visual inspection; its untagged source
colors were *assumed sRGB*. It has **not** been confirmed in the project
repo and has **not** received explicit `FACE_APPROVED` acceptance.
See [face-direction normalization record](../reports/ILLUSTRATION_NASH_FACE_DIRECTION_2026-10-25.md#normalized-candidate-prepared--2026-10-25).

**2026-10-25 subsequent approval/side-image update:** The user explicitly approved the normalized face anchor, now independently verified at `illustrations/references/Nash_Maggard_Face_v1_1024_sRGB.png` (checksum matches its existing conversion record). **`FACE_APPROVED` and `FRONT_APPROVED` are now registered.** The newly generated double-profile side study (ID `3f64de82-7f19-46cf-8c63-858f1eafc7ae`) also received positive owner feedback (“Yes.”). A **1024-square sRGB** side derivative has been prepared and checked but is not yet in the repository: `/mnt/data/Nash_Maggard_Side_v1_1024_sRGB.png` (SHA-256 `86fe9b11dbd4c07c6164e2a47a23b4525b7c93df2afaeda597790d67ea3e73d6`). Record **SIDE VISUAL ACCEPTED**, pending repository copy/hash validation for `SIDE_APPROVED`. Both sides have the hood down, while front shows hood up; preserve this as a documented presentation difference, not a change of identity. See [side-figure review](../reports/ILLUSTRATION_NASH_SIDE_ANCHOR_2026-10-25.md). Final sheet remains drafting; back view not yet produced.

**2026-10-25 corrected side-image and MCP attempt:** The owner rejected the previous right-side nail continuity and requested the hood up. The revised *two-profile hood-up* visual was **explicitly accepted** (generation `6b8dfa98-c6f0-411e-8911-3eb201d8929d`). Derived `/mnt/data/Nash_Maggard_Side_v2_HoodUp_1024_sRGB.png` is **1024-square ICC-tagged PNG**, SHA-256 `4a7bb1f07755a047f2ce430deb6d01e935db0b771b71d9a9fa1bb61a336337d5`. The MCP chunked uploader accepted the start but requires base64, and current connected tools cannot pass raw generated container file bytes as an image reference; **the upload was aborted without creating a repository asset**. Side approval remains **visual acceptance pending repository hash verification**, while face and front remain approved. [Detailed report](../reports/ILLUSTRATION_NASH_SIDE_ANCHOR_2026-10-25.md).

**2026-10-25 verified side / accepted back update:** The previously missing corrected hood-up side PNG has been **registered** at `illustrations/references/Nash_Maggard_Side_v2_HoodUp_1024_sRGB.png`: 1024-square RGB PNG with embedded ICC, SHA-256 `4a7bb1f07755a047f2ce430deb6d01e935db0b771b71d9a9fa1bb61a336337d5`. It is the owner-accepted visual: record **`SIDE_APPROVED`** (historical failed MCP upload remains part of the audit). The owner also explicitly approved the generated single hood-up back view `9e58bbe1-cbd2-478a-9c34-1c65bf87fd50`. A separate **1024-square RGB PNG with embedded 588-byte sRGB ICC**, `/mnt/data/Nash_Maggard_Back_v1_1024_sRGB.png`, SHA-256 `9f348f34ac86dd79f33cd9c59342b04c6d2267a99d908c8eea528b11c99f95d1`, passed visual and technical checks, but is not yet registered in the repository. Mark **`BACK_VISUAL_APPROVED / BACK_REGISTRATION_PENDING`**, and after file/hash validation **`BACK_APPROVED`**. [Report](../reports/ILLUSTRATION_NASH_BACK_ANCHOR_2026-10-25.md). The complete sheet remains drafting.

**2026-10-25 back registration and final assembly gate:** The user-added back PNG `illustrations/references/Nash_Maggard_Back_v1_1024_sRGB.png` now matches the accepted normalized back export **exactly**: SHA-256 `9f348f34ac86dd79f33cd9c59342b04c6d2267a99d908c8eea528b11c99f95d1`, 1024 × 1024 RGB PNG with embedded `iCCP` profile. Record **`BACK_APPROVED`**, along with already recorded **`FACE_APPROVED`**, **`FRONT_APPROVED`**, **`SIDE_APPROVED`**. The character's *input anchors are complete*, but the **combined character sheet is not**. Next create text-free composite page(s) from approved images only; check no proportions, staff nail direction, eye laterality, cloak/strap or color continuity changes; produce compliant 1024-square ICC-tagged PNGs and obtain separate owner approval. [Back verification report](../reports/ILLUSTRATION_NASH_BACK_ANCHOR_2026-10-25.md).

**Do not generate or implement new skills as a side effect of merely recording or reviewing the plan.** This document remains a durable handoff for explicit generation requests.
