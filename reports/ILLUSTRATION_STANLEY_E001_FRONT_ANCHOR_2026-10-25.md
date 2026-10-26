# Stanley Billings — E001 front-view approval and normalization (2026-10-25)

**Campaign:** The Wastes. **Subject:** `WASTES-STANLEY-BILLINGS`. **Appearance state:** `WASTES-STANLEY-BILLINGS-A01`, E001. **Design sheet:** `WASTES-STANLEY-BILLINGS-DS-001`.

**Status:** `FRONT_APPROVED` as of 2026-10-25, following explicit visual owner approval, owner placement in repository and exact binary hash/PNG identity verification. **Face remains `FACE_APPROVED`** (see [face report](ILLUSTRATION_STANLEY_E001_FACE_ANCHOR_2026-10-25.md)). Profile, back, and complete sheet remain unapproved.

## Accepted generation

- User explicitly invoked `$twbd-illustration-generate Wastes "Stanley Billings" E001 design-sheet front`. A **single complete front-standing, head-to-boots** figure was generated, with no sheet labels/insets. **Generation ID:** `fc3ab615-2c66-48b9-afb1-0b88fcbb0a43`.
- **Original generator file:** `/mnt/data/confident_half_elf_swordsman.png` (session file; not a repository asset). Source metadata independently inspected on 2026-10-25: **1254 × 1254 RGB PNG**, **1,749,378 bytes**, SHA-256 `9917ae7f9e4be51b42f1415bcd3a3e27a1bbf8d38231adc4abdb6b3809bc68d0`, **no embedded color profile**.
- **Owner decision:** “Approved.” This explicitly approves the visible composition and its visual choices. It does not prove that the original untagged PNG fulfills the technical publication gate.
- The portrait visibly corresponds to the owner-approved E001 face identity: brown swept-back, wavy hair, conspicuous half-elf ears, thick eyebrows, warm tan skin, brown eyes, curled moustache, narrow goatee, composed/dignified expression. Minor 3D-to-2D view/scale simplifications are part of the accepted illustrated identity. The full neutral figure has a front-oriented torso and visible head-to-boots outline.

## Locked full-body artistic decisions for E001/A01

**These are owner-selected *artistic production choices*, not newly verified E001 transcript descriptions.** The E001 text establishes a coat with a usable pocket, plus a rapier drawn later underground; E023 facial grooming is a **later** appearance clue.

- **Outfit:** A brown, worn **long, open-front, knee-to-mid-calf coat** with broad folded lapels, raised/turned-down collar, deep side-panel lines, small cuff adjustment tabs and a visible low outer pocket on Stanley's **right side** (viewer left). His coat opens over an **olive/dark-umber five-button vest**, **soft off-white open-collared shirt**, dark tobacco-grey trousers, a plain brown leather waist belt with rectangular brass buckle, and dark brown tall boots with small outer ankle straps/buckles. Matte, dust-muted materials with minimal brass accent and no bright saturated trim.
- **Pose:** Standing upright and almost fully frontal, feet slightly apart, **Stanley's right hand** (viewer left) slipped into the pocket region near the hip, **left hand** (viewer right) relaxed beside his body. This is a studio reference pose, not literal reenactment of his E001 left-hand food-concealment motion; the required coat pockets remain feasible.
- **Rapier:** A single plain, sheathed **rapier at Stanley's own left hip** (viewer right), the guard visible beside the left edge of the vest and just above the waist belt. A slim dark scabbard descends toward the calf, with a restrained brass/tan swept ring-guard and brown grip. Its exact hardware, carry side and scabbard attachment are *artistic decisions*, not source-confirmed. Keep the grip/guard and scabbard physically connected in the future profile and back render. No second sword, gun, shield, backpack, lute, ornate magical book or campaign-end magical objects.
- **Continuity checkpoints for profile/back:** Keep coat lapel/collar proportions, lower hem/split, pocket elevation, cuff-tab shapes, vest front/coat overlap, waist-belt thickness and central buckle, same boot heights and straps, and subject-left rapier/sheath arrangement. Avoid mirroring left/right. The accepted face, moustache and goatee remain separate from Diontalus's E045 and later silver-eyed, moustache-free states.
- **Render treatment:** Same modern adult-animation-inspired ink-heavy graphic-novel style lock v2, matte earthy tones and broad cel shading. Neutral warm-grey background; **no captions or other written labels**.

## Technical normalization and verified repository registration

- **Prepared session PNG:** `/mnt/data/Stanley_Billings_E001_Front_v1_1024_sRGB.png`.
- **Registered repository filename:** `illustrations/references/wastes_stanley-billings_e001_front_v01.png`. The file was confirmed at this exact path in the connected repository. Do not overwrite the exploratory Stanley sheet, accepted face, or any previous version.
- **Method:** Proportional Pillow LANCZOS resize of the accepted **1254 × 1254** source to **1024 × 1024** RGB; no aspect-ratio distortion or crop; embedded Pillow ImageCms built-in sRGB ICC (**588 bytes**, profile description `sRGB built-in`); PNG optimized.
- **Verified normalized file:** **1024 × 1024**, RGB, sRGB-tagged PNG, **1,067,778 bytes**, SHA-256 **`95b535fe5ccdc19ebde882d3725f24dd228da661288abfddf8a6fce75c1a8b0f`**. Pixel inspection after conversion: full body, hair, hands, rapier and boots remain in frame with no evident crop or continuity-breaking resize. Since the original was untagged, source color space was **assumed sRGB** rather than measured.
- **Repository verification on side-stage continuation:** The connected MCP binary reader returned **1,067,778 bytes** and exact SHA-256 **`95b535fe5ccdc19ebde882d3725f24dd228da661288abfddf8a6fce75c1a8b0f`**, matching the visually inspected, 1024 × 1024, sRGB-tagged session derivative byte-for-byte. The file header confirms 1024-square RGB PNG and embedded ICC. Owner explicitly approved the visible single-front render and subsequently placed its normalized derivative in the exact repository path. Mark **`FRONT_APPROVED`** for this hash, without implying that owner recited the checksum. Full sheet, profile and back still need independent approvals.

## Follow-up and verification

1. **Completed:** repository registration and exact checksum/technical comparison, `FRONT_APPROVED`.
2. **Current stage:** `$twbd-illustration-generate Wastes "Stanley Billings" E001 design-sheet side` — produce **one** strict, full-length **subject-left profile** of the exact outfit, with rapier on subject-left hip, and seek separate approval.
3. Later: back view, deterministic composition, and **distinct final-sheet owner approval**.

The two previously rejected multi-view candidates remain rejected and are documented in [front attempt report](ILLUSTRATION_STANLEY_E001_FRONT_ATTEMPTS_2026-10-25.md). No previously selected art was altered, no new canon was inferred from generated pixels. Local image metadata and pixel inspections: **PASS**. Repository asset registration: **PASS, hash-matched on 2026-10-25**. TWBD test/lint suite: **NOT RUN** (local MCP provides no TWBD-targeted check runner).
