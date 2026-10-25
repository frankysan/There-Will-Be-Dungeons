# Reusable character-sheet production prompts and turnaround playbook

**Status:** Active reusable companion to [the canonical character-sheet workflow](CHARACTER_SHEET.md), [the generation skill](SKILL.md), and [the illustration style guide](../../../project/ILLUSTRATION_GUIDE.md). Applies to **all campaigns and characters**; never import Stanley's costume, Nash's injuries or another character's anatomy into a new subject.

**Why this exists:** The [Stanley E001 paired-profile pilot](../../../reports/ILLUSTRATION_STANLEY_E001_SIDE_APPROVAL_2026-10-25.md) succeeded visually only after the **owner attached the approved front PNG directly to a separate image-edit request**, asked for **both anatomical side profiles**, and approved the resulting image. Several earlier prose-only generations repeatedly altered the established costume; displaying the reference to the assistant or mentioning its path had not established actual renderer conditioning ([failed attempts](../../../reports/ILLUSTRATION_STANLEY_E001_SIDE_ATTEMPTS_2026-10-25.md)). The successful image's internal editing lineage was **not available for independent verification**, so do not claim a guaranteed technical solution. The reliable lesson is **the owner's actual source-file attachment + a simple, positive, specific view-change request + independent visual approval**, not a magical prompt string.

## Quick-start checklist for any new character

1. Resolve `CAMPAIGN`, `CHARACTER`, `STORY_STATE` and spoiler cutoff. Read the integrated, evidence-backed appearance reference, sheet registry and sources. Separate story-confirmed traits from accepted artistic choices; no research, no image.
2. Set up IDs and stage reports. Work one stage at a time: **brief → face → full-body front → paired anatomical sides (recommended default) → full-body back → deterministic sheet assembly → separately approved final sheets**. Do not produce the entire reference suite in one generative call.
3. Obtain explicit visual owner approval for **the exact face and front** and register verified 1024-square sRGB PNGs with SHA-256 before rotating the figure.
4. For **side or back edits**, make the approved front (and optionally the approved face/side) a **direct image attachment in the same editing request**. A text filename, repo read, embedding in the assistant's notes, image shown in a prior response or renderer resemblance does **not** prove image input was passed. If the available editor cannot accept the supplied source image, **STOP**; do not substitute unanchored text-to-image.
5. Request **both true anatomical side profiles in one view** by default because a pair makes mirrored equipment/anatomy mistakes and costume drift easier to detect. A single side remains valid if explicitly requested or if an established asymmetric design requires staged handling. Only the viewpoint should change. See [paired profile copy template](#template-c--paired-side-profiles-recommended-default).
6. Inspect the actual pixels against the **exact approved source**, including color/materials, silhouette and handedness. Reject visual drift before technical normalization. A repeated failure using one method triggers the [circuit breaker](CHARACTER_SHEET.md#1a-existing-anchor-turnaround-gate--no-text-only-character-reinvention); stop after two similar failures and **change the input method**, not the volume of negative prompting.
7. After explicit approval, normalize without cropping figures or stretching proportions to **1024 × 1024 PNG with actual sRGB tagging**. For a paired sheet, **preserve the approved pair** and optionally make **two deterministic, non-mirrored crops** for separate anchors. Check every derivative visually. Treat an untagged generator output as **assumed** sRGB only when appropriately justified; do not claim the input was tagged.
8. Save new versioned images under `illustrations/references/` or a documented image directory. **Read back** PNG signature, IHDR, ICC/sRGB description, dimensions, byte count and SHA-256. Log exact approved original, transformations, resulting hashes, source refs, prompt/input mode, owner decision and story scope. Do not mark `*_APPROVED` until the exact registered export is verified.
9. Back uses the *actual approved front and side images* and a **single true rear view**. Assemble the finished sheet by composing **approved exact pixels**, not regenerated copies. Explicitly present final pages and obtain a **separate** owner decision before `OWNER_APPROVED`.

### Operational preflight record (fill only actual observations)

```yaml
character: <campaign-qualified subject ID>
state: <story-state ID>
stage: <FACE|FRONT|PAIRED_SIDES|BACK|ASSEMBLE>
approved_reference_files: [{path: ..., sha256: ..., approval_status: ...}]
source_attached_in_current_edit_request: <yes|no|unverified>
editor_mode: <image_edit|reference_conditioned|manual|unverified>
input_conditioning_provenance: <verified|unverified>
actual_prompt: <captured verbatim|unavailable>
requested_view: <front|left_and_right|back>
output_candidate: <file / generation ID>
visual_decision: <pending|rejected|owner_accepted>
export_verification: <pending|pass|fail>
repo_registration: <pending|sha256_verified>
```

If metadata reports `edit_op:null` / `parent_gen_id:null`, that **does not prove an image input was consumed**. It also does not disprove everything about a visually plausible candidate. Record the actual interface contract, owner attachment and available lineage honestly. **Never substitute a hypothetical input link or image hash.**

## Prompt template conventions

- Replace every bracketed field or template placeholder (such as `[CHARACTER]`, `[STORY_STATE]` and `[ASYMMETRIC FEATURE]`) with subject-specific details from the **approved actual image** and integrated reference. Never replace them by inventing canon.
- Attach the required PNG(s) **to the same request**. Do not include rejected candidates as source inputs. Start a fresh image edit request when the client cannot bind previous tool/image outputs reliably.
- Prompt **positively**: describe the approved garment, face and equipment, and what to change in viewpoint. Keep prior failure terms and negative inventories in a **separate QA checklist**, not the model-facing request where they may be mistaken for desired attributes.
- Preserve the attached image as the visual authority. The current mandatory house style is the **exact immutable block in [SKILL.md §3B](SKILL.md#fixed-style-prompt-block--include-unchanged-in-every-generationedit-prompt)**. Before issuing each actual generate/edit call, **append that full block unchanged**; the compact templates below are the *subject/view-specific prefix*. If copying into a client outside this project, paste the full block from SKILL.md after the template. The source file, not this page, owns style-version updates.
- Generate **one candidate per stage for review**. A 1024-square target may be ignored by the renderer: validate the real output, then make a separate versioned compliant derivative **only after visual approval**.

## Template A — first face (source-led concept)

**Attachment:** relevant *authorized* creator/concept art, when rights and era suitability permit, otherwise no visual asset; this stage can establish its own first anchor.

```text
[CAMPAIGN], [CHARACTER], [STORY_STATE] — FACE reference.

Create exactly ONE neutral head-and-shoulders portrait in the approved project style.
Story-established features: [VERIFIED EARLY-STATE PHYSICAL FEATURES].
Provisional owner-selected features (if needed): [ARTISTIC CHOICES CLEARLY NOT CANON].
Expression and palette: [SUPPORTED OR APPROVED CHOICE].
One figure, one simple neutral background, no typography or additional panels.

Request one 1024×1024 sRGB PNG candidate. Present the face for approval;
do not infer that generating it approves it.
[APPEND VERBATIM STYLE LOCK V2 FROM SKILL.MD §3B]
```

After the owner accepts the actual face image: conform/tag, visually inspect, register exact SHA, read back, then `FACE_APPROVED`.

## Template B — front body from approved face

**Attachment:** the **exact approved face PNG** (prefer direct image attachment).

```text
[CAMPAIGN], [CHARACTER], [STORY_STATE] — FRONT character anchor.
Edit/use the attached approved FACE as the visual identity reference.
Create exactly ONE neutral full-body, strictly front-facing view, from hair to
boot soles. This is the same character, not a newly invented design.

Preserve: [APPROVED FACE, HAIR, ASYMMETRIES, COMPLEXION].
Full-body costume and props, supported by the integrated brief:
[POSITIVE, SPECIFIC AND PROVISIONAL-CHOICE-LABELED OUTFIT/PROP LOCK].
[SUBJECT-ANATOMICAL LEFT/RIGHT EQUIPMENT POSITIONS].

One figure on a plain neutral background, no labels, extra insets or other views.
Produce one 1024×1024 sRGB PNG candidate for explicit owner approval.
[APPEND VERBATIM STYLE LOCK V2 FROM SKILL.MD §3B]
```

The accepted front becomes the **costume/silhouette authority** for SIDE and BACK after registry verification. Never backdate later accessories into this baseline.

## Template C — paired side profiles (recommended default)

**Attachment REQUIRED:** the **exact approved full-body FRONT PNG**, directly attached **to this image-edit request**. Optionally attach an approved separate face as a second actual image reference if the tool supports it. Avoid attaching the rejected render attempts.

```text
[CAMPAIGN], [CHARACTER], [STORY_STATE] — TWO ANATOMICAL SIDE PROFILES.

Edit the ATTACHED APPROVED FULL-BODY FRONT PNG itself. Rotate the camera
around the SAME character and costume. This is a VIEWPOINT TRANSFORMATION,
not a redesign, recreation from a text description, or simple mirroring.

Exactly TWO standing head-to-boots figures, neutral, equally scaled:

LEFT PANEL: camera views the CHARACTER'S ANATOMICAL LEFT side;
             character faces the RIGHT edge of the canvas (→).
RIGHT PANEL: camera views the CHARACTER'S ANATOMICAL RIGHT side;
             character faces the LEFT edge of the canvas (←).

Keep the attached figure's face, hairstyle, body proportions, costume
construction, existing colors/materials, seams, pockets, cuffs, closures,
boots, hands and [EXACT APPROVED EQUIPMENT] the same.
[POSITIVE SHORT OUTFIT/IDENTITY LOCK FROM FRONT — NO NEW FANTASY DETAILS].
[ASYMMETRIC FEATURE] remains on the CHARACTER'S [LEFT|RIGHT] side
in BOTH views, with appropriate visibility/occlusion from the opposite side.
A carried blade remains in the same physical scabbard if the front shows
it sheathed. These are TWO REAL CAMERA VIEWS, NOT FLIPPED COPIES.

Neutral background, full figures, even spacing, no text, decoration,
additional views, inset faces or equipment panels.
One square 1024×1024 sRGB PNG candidate for owner review.
Use the actual attached image as your source. If the editor cannot accept
the source as an image input, REPORT THAT AND DO NOT GENERATE AN UNLINKED
TEXT-TO-IMAGE SUBSTITUTE.
[APPEND VERBATIM STYLE LOCK V2 FROM SKILL.MD §3B]
```

**Orientation audit before approval:** Left anatomical side = camera on character's left, figure facing viewer-right; right anatomical side = camera on character's right, figure facing viewer-left. **Direction alone does not prove anatomy or handedness**: check asymmetric accessories/marks. Never mirror the whole drawing to produce a second side. For a subject lacking a conventional face/anatomical left/right, explicitly substitute the researched creature/object orientation and record how determined.

**Visual QA off-prompt checklist:** compare both figures to the actual registered front; check facial identity and hair length; coat/armor/clothing cut and color, patterns/ornament, hand covering, added or missing straps/pouches, boot geometry and attachment sidedness; continuous sword/sheath/staff/tool structure; no new unsupported gear; no cutoff or swapped view. Treat unintended changes as revisions, not “minor variety.”

**Export:** Keep the user-approved **paired** image as authoritative. Only after approval, normalize it and optionally split the **actual paired pixels** into separate left and right 1024-square PNGs. Preserve each figure's scale, proportion and entire silhouette with neutral padding; no flipping, regeneration, aggressive stretching or new accessory construction. These are **derivative reference files** linked back to the exact paired source, each independently inspected and hashed.

## Template D — rear view after paired sides approved

**Attachment REQUIRED:** approved FRONT and approved paired SIDE reference files, direct image attachments if the tool can accept both.

```text
[CAMPAIGN], [CHARACTER], [STORY_STATE] — STRICT FULL-BODY BACK VIEW.

Edit/reconstruct the exact SAME already-approved character shown in the
attached FRONT and BOTH SIDE reference images. Camera directly behind:
one neutral full-body orthographic rear view, hair to boot soles.

Keep the established proportions, hair length, collar, garment hem/splits,
seams, cuffs, pockets, belt/straps, boot heights and equipment physical
construction. Keep [ANATOMICAL LEFT/RIGHT MARKS OR PROPS] on the same
physical side. Reconstruct only back-facing geometry not shown in front;
the front/side source images are authoritative.

Exactly ONE rear-facing standing figure, neutral background, no labels,
extra views or decoration. One 1024×1024 sRGB PNG candidate for review.
If actual input images cannot be passed to the editing tool, STOP.
[APPEND VERBATIM STYLE LOCK V2 FROM SKILL.MD §3B]
```

Do not mark `BACK_APPROVED` until exact owner approval and repository PNG/profile/hash verification.

## Template E — final composite (not generative)

**Inputs:** all **owner-approved and repository-verified** face/front/paired sides/back; do not reconstruct them by prompting another image model.

```text
[CAMPAIGN], [CHARACTER], [STORY_STATE] — ASSEMBLE.
Compose the actual approved source pixels deterministically into one or
more text-free 1024×1024 sRGB PNG sheet pages.

Preserve full-body scale across front, both anatomical sides and back.
If all four full bodies become illegible, use multiple square pages;
keep a separate face/detail page if useful. Keep every image's original
outfit, handedness, physical equipment, style and colors unchanged.
No newly generated people, equipment, captions or annotation panels.

Inspect actual assembled output, check exact source SHA references,
and present the final page(s) for a NEW, EXPLICIT owner approval.
Do not mark OWNER_APPROVED until pages are registered and hash-verified.
```

## Example records — not universal character canon

- **Stanley Billings / Wastes E001:** [approved face/front descriptions](../../../project/ILLUSTRATION_STANLEY_BILLINGS_REFERENCE.md) and [owner-accepted paired side profiles](../../../reports/ILLUSTRATION_STANLEY_E001_SIDE_APPROVAL_2026-10-25.md). The correct design happens to have a plain olive/dark-umber vest, brown coat and **left-hip sheathed rapier**. These are Stanley-only artistic locks. The accepted pair was owner-approved but the prepared registered-asset checks were still **pending as recorded**; do not retroactively mark `SIDE_APPROVED` without actual file readback.
- **Nash Maggard / Wastes E000:** [sheet workflow precedent](../../../reports/ILLUSTRATION_NASH_E000_SHEET_ASSEMBLY_2026-10-25.md). Nash's scars, wraps, hood, red sightless eye and staff nail are likewise Nash-only.

## Failure modes that must not return

1. Unanchored text-only image regeneration after a front/face was already accepted; merely mentioning the filename or pasting an image in *a different* assistant tool result is inadequate.
2. Using rejected-render details in the positive generative prompt (“red patterned vest,” “new pouches,” etc.) while intending to forbid them. Keep these in **QA only**.
3. Ambiguous “left profile” naming without both **camera side** and **facing direction**, mirroring asymmetrical equipment, or changing anatomical left/right based on image position.
4. Treating successful visual approval as proof of physical exact-file registration, ICC compliance or internal reference-conditioning provenance.
5. Assembling a new generative multiview picture instead of composing already approved exact anchor pixels, or treating a front/side approval as final-sheet approval.

**Source of truth:** [canonical sequence and technical gates](CHARACTER_SHEET.md) and the [immutable style block](SKILL.md#fixed-style-prompt-block--include-unchanged-in-every-generationedit-prompt). Keep this playbook updated whenever the workflow genuinely improves.
