# Hope Akmenos — E001 front-view attempts and method stop (2026-10-25)

**Request:** `$twbd-illustration-generate Wastes "Hope Akmenos" E001 design-sheet front`. **Stage:** `DESIGN_SHEET / FRONT`. **Outcome:** `FRONT_DRAFTING / FRONT_METHOD_BLOCKED` after two repeated composition failures with the same tool approach. **No front owner approval, technical export or repository registration claimed**. The pre-existing `FACE_APPROVED` anchor is preserved.

## Preflight / face gate resolved

- Campaign/subject/state: The Wastes / `WASTES-HOPE-AKMENOS` / `WASTES-HOPE-AKMENOS-A01` E001 organic Dusthill mechanic; candidate sheet `WASTES-HOPE-AKMENOS-DS-001`.
- **Canonical approved face:** `illustrations/references/Hope_Akmenos_E001_Face_v1_1024_sRGB.png`; now actually present in connected repository. Binary readback: **1,569,186 bytes**, SHA-256 `1ef34cf6f619757df4e51e0f12a151965f1ed3381506af1b1c06c65667d3c91d`, 1024 × 1024 RGB PNG with iCCP. Identical SHA and length to the accepted normalised session file, which was decoded and embedded profile inspected: 588-byte ICC `sRGB built-in`. The user accepted the darker-maroon face in the conversation. The earlier registration-pending status is superseded: **FACE_APPROVED**.
- The actual face pixels were opened/visually inspected in this invocation. Locked traits: dark maroon skin, amber/gold eyes, freckles, large intact organic brown ram-like horns curling out and inward at tips, purple gathered/swept-back hair with loose facial strands, pointed ears, brass-rimmed dual goggles resting above forehead, open-collared cream work shirt, dark utilitarian vest with brown shoulder straps/brass buckle details, small circular brass pendant, adult-animation-influenced inked/cel-shaded style. All are owner-selected baseline *art choices*, not independently verified E001 spoken palette/costume canon.
- Front-only additional design proposals: two fully organic arms/hands and legs, practical brown utility trousers and tall strapped brown boots, compact accessible tool belt, one dark maroon tail, plain neutral background, no E033 rocket, later mechanical-left prostheses, post-resurrection scarring, Tietkalla royal styling or Hand of Voice. Exact front outfit, props, equipment handedness and tail are not yet owner approved.

## Required output

One **single neutral full-body strict front view** (head, horns, boots and tail unobstructed), no face insets, rear/side panels, close-up panels, labels, borders or lettering. Original face actual pixels should be supplied as source to a controlled image-to-image or edit call. Match fixed `SKILL.md` §3B v2 style verbatim and project 1024 × 1024 sRGB PNG. Record whether image pixels were **actually fed to generator**, not merely seen by assistant or present in a previous chat.

## Two rejected candidates — material repeat

| ID | Session preview | Bytes / SHA-256 | Review |
| --- | --- | --- | --- |
| F01 generation `cd5dd474-2a91-44cf-abba-d0b912e25dd4` | `/mnt/data/a_clean_character_concept_turnaround_style_illustr.png` | 2,649,270; `0bfbecb5a0ea8f4bd8224820c519604d2b9ed9195703a524073e471a5228bb60` | **REJECT:** one central standing full-body figure **plus** numerous independent enlarged face, back, shirt, tool, hair/boot panels and rectangular borders. Character is posed rather than strictly orthographic neutral. |
| F02 generation `8b8f82c8-6089-46d0-9bef-d8e0c8333f7b` | `/mnt/data/a_clean_studio_character_concept_illustration_on_a.png` | 2,480,909; `a603b0c6e6ccf090b97015edfcb799e183e5e3eae346b535965e1795fd87a3d8` | **REJECT:** one large full-body figure **plus** enlarged face portrait and miniature rear full-body inset. Non-neutral bent arm/hand-on-hip and modest head angle. |

Both outputs are original **1254 × 1254 RGB PNGs**, **no embedded ICC**, so also fail mandatory 1024 sRGB delivery even if the owner later wanted them as stand-alone studies. The generation metadata for both returned `edit_op: null`, `parent_gen_id: null`, `prompt: ""`. The user-facing tool elaborations showed **unrequested multi-view/panel composition** in both attempts. The generator's final internal prompt and whether accepted face pixels were actually reference-conditioned were **not verifiable**. **Do not claim these results were actual image edits of the canonical face.** The visual resemblance is not sufficient to prove input identity.

## Circuit breaker and next controlled method

The project-wide **two material failures** rule is triggered. **STOP this unverified/unconditioned image-generation strategy; do not issue a third similar render, text-only retry or 'negative prompt' expansion.** Preserve both drafts as historical failures but do not add to `illustrations/references/`, promote approval, normalize as a supposed production front, or use the drafts as side/back anchors.

**Recommended distinct workflow:** initiate a fresh image-edit request with the **owner directly attaching** the exact repo-verified accepted face PNG (`Hope_Akmenos_E001_Face_v1_1024_sRGB.png`) to the *same request*. Request **a single head-to-boots strict orthographic neutral front view of the character in that supplied image**. Avoid `design-sheet`, `turnaround`, `panel`, `close-up`, `front and back` keywords in model-facing composition; these phrases triggered extra panels. Attach only the approved face, not either rejected multi-view draft. Use positive wardrobe descriptors from the proposed E001 brief and append **exact fixed v2 style block** from generation skill. If tool input/reference transmission cannot be established, switch to a verifiably controlled editor/illustrator-assisted route before another image. Do not state success from `edit_op:null` alone.

Only after a **single suitable front** is actually reviewed/accepted, and a separate **1024-square sRGB PNG is exported, visually checked, uploaded and hash read back**, mark `FRONT_APPROVED`. Until then this remains **FRONT_METHOD_BLOCKED** (front is not approved). **FACE_APPROVED remains in force**.

**Source authority:** [Hope appearance record](../project/ILLUSTRATION_HOPE_AKMENOS_REFERENCE.md), [E001 plan](ILLUSTRATION_HOPE_E001_SHEET_PLAN_2026-10-25.md), [face acceptance and SHA/ICC verification](ILLUSTRATION_HOPE_E001_FACE_ACCEPTANCE_2026-10-25.md), [canonical sheet workflow](../.agents/skills/twbd-illustration-generate/CHARACTER_SHEET.md), [reusable owner-attachment prompts](../.agents/skills/twbd-illustration-generate/CHARACTER_SHEET_PROMPTS.md).

**Checks:** Actual face SHA/profile/repo readback **PASS**; F01/F02 single-view composition **FAIL**; candidate dimensions/ICC **FAIL**; FRONT approval and repo publication **NOT DONE**. No unrelated content edited or source suite run.
