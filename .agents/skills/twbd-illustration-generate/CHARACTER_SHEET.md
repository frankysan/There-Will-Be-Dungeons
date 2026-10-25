# Canonical recurring-character design-sheet workflow

**Status:** Active production procedure for `twbd-illustration-generate` `DESIGN_SHEET` requests, 2026-10-25. Read alongside [SKILL.md](SKILL.md), particularly the exact **section 3B immutable style block**, [research skill](../twbd-illustration-research/SKILL.md), [style guide v0.6](../../../project/ILLUSTRATION_GUIDE.md), [character-sheet registry](../../../project/ILLUSTRATION_CHARACTER_DESIGN_SHEETS.md), [appearance register](../../../project/ILLUSTRATION_REFERENCES.md), and [image assets policy](../../../project/IMAGE_ASSETS.md). This document is an **operational companion to the installed generation skill**, not a separately installed `twbd-character-sheet` skill.

## Supported stage requests and dispatch

Invoke through the installed generation skill with an explicit character-sheet mode and stage, for example:

- `$twbd-illustration-generate Wastes "Stanley Billings" E001 design-sheet plan`
- `$twbd-illustration-generate Wastes "Stanley Billings" E001 design-sheet face`
- `$twbd-illustration-generate Wastes "Stanley Billings" E001 design-sheet front`
- `$twbd-illustration-generate Wastes "Stanley Billings" E001 design-sheet side`
- `$twbd-illustration-generate Wastes "Stanley Billings" E001 design-sheet back`
- `$twbd-illustration-generate Wastes "Stanley Billings" E001 design-sheet assemble`
- `$twbd-illustration-generate Wastes "Stanley Billings" E001 design-sheet status`

`plan`, `status`, `face`, `front`, `side`, `back`, `assemble`, `review`, `register`, `revise`, `continue` are **natural-language stage selectors**, not a promised command-line executable. `continue` resumes the first pending stage using **persisted records**; a terse “proceed” in the active character-sheet workflow completes **at most one logical stage** unless the owner explicitly requests more. Merely recording a plan does not authorize generation. `assemble` does not authorize changing any final approval flag.

## 0. Research and story-state contract (always first)

1. Record Git status; inspect existing subject references and sheet ledger. Identify **campaign-qualified subject ID**, `sheet_id`, `state_id`, first relevant episode and story/spoiler cutoff. Do not merge character identity between campaigns, or reuse story-era variants without explicit applicability.
2. Use `twbd-illustration-research` for the **written, integrated evidence brief**. Require source IDs, episode/time locators and verification classes; differentiate GM narration, character claims, retrospective bonus, player artwork, later-scene observations, final D&D Beyond JSON and artistic assumptions. **End-of-campaign JSON is not first-appearance evidence.** If research is too weak to depict a material identity trait, queue a specific `IRQ-` blocker and stop.
3. Before drawing, inspect actual existing creator art, accepted images, rejected attempts and same-subject appearances. Record inspection/access gaps and rights. Freeze a versioned baseline: mandatory `S` sourced facts, owner-selected provisional `D` artistic decisions, time-limited exclusions, main palette, anatomy/asymmetries from **character's own left/right**, clothes, props, carried versus merely owned equipment, and identity/silhouette constraints.
4. Reserve/update the named candidate in [sheet ledger](../../../project/ILLUSTRATION_CHARACTER_DESIGN_SHEETS.md). A missing sheet requiring approval is a **sheet workflow gate**; only missing source research gets an `IRQ-` entry. Existing artwork affected by genuine contradictory evidence goes to the `IRV-` revision queue. Do not silently rewrite approved art.

## 1. Anchor production sequence

| Stage | Default image task | Prerequisite | What the owner approves |
| --- | --- | --- | --- |
| `BRIEF_READY` | Source-linked written identity/appearance brief only | Subject research passes | Readiness and provisional design choices; **no image yet** |
| `FACE` | **One** neutral close-up/bust with identifying eyes, hair, scars and expression | `BRIEF_READY` | Identity lock; exact accepted picture |
| `FRONT` | **One** neutral, complete front full-body figure, head to boots | `FACE_APPROVED` | Face carry-forward, proportions, garments, props and palette |
| `SIDE` | **One** strict full-body profile; *two opposite profiles only if explicitly requested/accepted* | `FRONT_APPROVED` | Dimensional continuity, item attachments and left/right details |
| `BACK` | **One** complete rear full-body view | `SIDE_APPROVED` | Rear garment construction, hood, carried straps, boots and props |
| `ASSEMBLE` | **One or two** text-free pages, composed from approved **actual source pixels** | All four anchors approved | Whether the **final arrangement**, not just inputs, is acceptable |
| `OWNER_APPROVED` | Register exact final sheet version, pages and story scope | Final pages technically and repository verified **and** explicit approval | Final completed model-sheet package |

Every anchor has independent stages: `*_DRAFTING` → `*_VISUAL_ACCEPTED` → `*_REGISTRATION_PENDING` → `*_APPROVED`. A user approving how a render **looks** does not prove its eventual export is sRGB/1024 or present in the repo. A prior stage can remain `*_APPROVED` when unrelated later candidates fail. Historical sequences that advanced out of order are allowed as **documented exceptions**, not general shortcuts. The final sheet's `OWNER_APPROVED` is **separate from all four anchor approvals**.

### Stage-specific visual briefs

**Face:** “Exactly one bust/face reference, no multi-panel sheet, full face identifiable, one neutral background, no weapons, no annotations.” Preserve documented eye/asymmetry and severe or subtle defining traits. A later expression add-on must not replace the primary identity anchor without review.

**Front:** “Exactly one completely visible front-facing figure, head and feet in frame, no rear/side/insets/palette strips/labels.” Carry the **approved face file as an actual reference where supported**; if renderer cannot accept it, disclose limitation. Reuse proportion, hood/head, fabric, accessory and staff designs, and avoid default medieval-fighter gear/extra weapons. Freeze silhouette/outfit palette decisions after acceptance.

**Side:** “One strict full-body left or right profile of same character and actual costume.” Compare to the approved front and written locks. If opposite-facing pair is explicitly chosen, **audit each individually**: avoid simply flipping a damaged left eye, satchel sidedness, staff nail head/point, shoulder or gear. Floating nail beside staff, mirrored scarring and changed hood state are hard continuity faults unless justified/reviewed.

**Back:** “One full rear view head-to-boot of precisely the same outfit and equipment, same hood-up/down configuration.” Reconcile cape folds, straps, bags, gloves, boots and prop attachment geometry with front and sides. No new inscriptions or backpacks.

**Assemble:** Default two text-free 1024-square pages when a single sheet would shrink features: first page front, side(s) and back at **comparable actual figure heights**; second page high-resolution approved face/expression reference and essential tiny objects. **Prefer deterministic layout using exact approved pixels**, not a generative redraw. Matte/scale images only without cropping/warping defining body, staff or boots; inspect actual mask edges and the output image after compositing. No panel labels, statblocks, written descriptions or decorative borders. Put all explanation in Markdown/manifest, not in the image.

**Phase-specific prompt recipe:** (1) subject/campaign/state/episode cutoff; (2) sourced mandatory visible facts; (3) provisional design decisions and exclusions; (4) exactly **one stage-specific composition**, not “make an elaborate character sheet”; (5) filenames/hashes of approved **actual image references** and what was truly passed to renderer; (6) append **verbatim current full style lock** in generation `SKILL.md` section 3B, **no modifications/shortening**. Request a **single 1024 × 1024 square PNG in sRGB**. Keep the actual tool prompt/settings and source conditioning metadata if available. If not, label `actual_prompt=unavailable` or `refs_sent=not verified`, not as a factual claim.

## 2. Review and retry rules

Review source fidelity, facial recognition, correct eye side, anatomical proportions, acquired gear chronology, garment/cape/hood consistency, staff/prop physical construction from *every* view, straps/satchels, hands/feet, no floating/duplicated/mirrored objects, no later-story details, no labels and house style v2. Compare the **actual pixels**, not just file name or text description.

If a candidate fails, record exact defect and the generated-image reference; keep approved earlier anchor unmodified. Retry **only the failing stage/region**, preferably using image edit with prior accepted art where available. Multi-view prompts hallucinating extra inset figures should be reduced to one figure. Do not extrapolate from a corrected single detail that all other details are still right. A style study is not automatically an identity anchor.

## 3. Physical-image quality, color and publication

**Technical hard gate:** inspect saved file bytes, not requested renderer settings: PNG signature, **1024 × 1024 IHDR**, decoded pixels and **actual sRGB tagging**, color mode, exact SHA-256 and bytes. An `iCCP` chunk proves embedded ICC but not by itself which profile: inspect ICC description where possible. A renderer may return 1254 or 1536 despite being asked for 1024. Treat original as **noncompliant**, preserve it, create a *separate* versioned conforming 1024 PNG with proper aspect ratio and an embedded sRGB ICC using a reliable image processor. No aggressive crop, stretch or false claim that untagged input’s color space is proven; log any **sRGB assumption** and inspect derivative after conversion.

**File registration:** Session `/mnt/data/` files, generated ChatGPT file IDs and image preview refs are **not repository assets**. Place separate files under `illustrations/references/` without overwriting approved artwork. The workspace MCP's current PNG create/chunk APIs accept **base64 PNG data**, not local file paths/ChatGPT IDs; if no supported bridge from session bytes to the MCP argument exists, do not attempt an empty upload. Provide an independently verified PNG and record `REGISTRATION_PENDING`. After upload by whichever means, **read back exact repo file SHA-256, dimensions and profile** before promoting to `*_APPROVED`. A ZIP link that fails to download does not invalidate a PNG; provide verified direct PNG alternatives.

**Rights/provenance:** Archive/player/GM/fan reference images may have reuse restrictions distinct from generated assets. Preserve filenames, source and rights decisions; never silently redistribute raw art or replace an older accepted file. The assembled sheet is a *production design reference*, not source canon.

## 4. Persisted manifest / state record

At every stage save or update the sheet ledger, subject file and a bounded report; prefer a **machine-readable versioned manifest** where applicable, and cross-link rather than duplicate conflicting long status paragraphs. Persist real facts only:

```yaml
schema_version: 1
campaign: ...
subject_id: ...
sheet_id: ...
state_id: ...
story_scope: { from: ..., until: ..., spoiler_cutoff: ... }
research: { reference_path: ..., version: ..., evidence_ids: [] }
style: { guide_version: 0.6, lock_version: v2 }
owner_design_choices: []
source_exclusions: []
identity_lock: { version: ..., subject_left_right: ... }
outfit_lock: { version: ..., garments: ..., accessories: ... }
anchors:
  face: { status: ..., path: ..., sha256: ..., owner_decision: ..., color_profile: ... }
  front: { status: ..., path: ..., sha256: ..., owner_decision: ..., color_profile: ... }
  side: { status: ..., path: ..., sha256: ..., owner_decision: ..., color_profile: ... }
  back: { status: ..., path: ..., sha256: ..., owner_decision: ..., color_profile: ... }
final_pages: [{ path: ..., sha256: ..., owner_approved: false }]
attempt_log: [{ phase: ..., intended_prompt: ..., actual_prompt: ..., references_inspected: [], references_sent_to_renderer: [], settings: ..., outcome: ..., error: ... }]
owner_final_approval: null
next_step: ...
```

Do not write invented values to a manifest. Keep `story time` and `disclosure time` separate. Retain exact archive/asset provenance; when an approved identity or costume changes, re-review its dependent front/side/back/page assets and any affected scene images, add relevant `IRV-` entries and version the new sheet rather than overwriting the old.

## 5. Final completion gate and pilot example

Only set `OWNER_APPROVED` after **the combined final page(s)** are actually shown to and explicitly approved by the owner, their exact files are **registered and hash-verified in the repository**, and the approval record binds sheet ID/version/campaign/story state/time coverage and source hashes. Prior visual approval of face/front/side/back alone is **insufficient**.

Nash pilot: [progressive plan](../../../project/ILLUSTRATION_PROGRESSIVE_CHARACTER_SHEET_PLAN.md), [actual compositing report](../../../reports/ILLUSTRATION_NASH_E000_SHEET_ASSEMBLY_2026-10-25.md), and [ledger](../../../project/ILLUSTRATION_CHARACTER_DESIGN_SHEETS.md). Four anchors are owner-approved and repo-verified, while the two-page composite is `AWAITING_OWNER_REVIEW` and its session-only outputs have not been registered. A fresh character must **not** inherit Nash's bald disfigured head, red-left eye, rust cloak, concealment wraps or nail-tipped staff as generic design choices.

Do not claim full completion without evidence. Report checks as `PASS`, `FAIL` or `NOT RUN` and keep unrelated edits untouched. A connected InfinityDB-only check runner is **not** a TWBD suite.
