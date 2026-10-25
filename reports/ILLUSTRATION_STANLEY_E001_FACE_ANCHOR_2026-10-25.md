# Stanley Billings — E001 face acceptance and normalization (2026-10-25)

**Campaign:** The Wastes. **Subject:** `WASTES-STANLEY-BILLINGS`. **Appearance:** `WASTES-STANLEY-BILLINGS-A01` (E001). **Sheet:** `WASTES-STANLEY-BILLINGS-DS-001`. **Stage:** FACE, **status: `FACE_APPROVED` as of 2026-10-25** (owner accepted portrait, then requested continuation after seeing normalized file; exact export placed in repository and verified). The *complete character sheet* is not approved.

## Owner visual decision and image identity

- Following the explicit `$twbd-illustration-generate Wastes "Stanley Billings" E001 design-sheet face` invocation, the image generator produced the **single bust image** `cd259553-dace-43fb-9038-34946497674f`, exposed as `/mnt/data/charismatic_half_elf_rogue_portrait.png` and an equivalent generated-session path.
- Owner response: **“Accepted.”** The acceptance is for the **visibly presented E001 face portrait**, not automatically the older, differently hashed repository `Stanley_Billings_Face_v0.png` or the unfinished `Stanley_Billings_Sheet_v0.png`. No full-body garment design, later-state face, assembled sheet or other unseen file is thereby approved.
- Source image was independently inspected/decoded: **1254 × 1254 RGB PNG**, **2,030,441 bytes**, SHA-256 `ee8fa92d76d75bac328b7861b695e62e3f24f172889645f4a09a575b1dc3dcdb`, **no embedded ICC profile**. Noncompliant as a published production anchor until normalized.

## Accepted face design — provisional artistic lock for E001/A01

The accepted face portrait displays **adult male half-elf**, medium/dark **wavy swept-back brown hair with loose strands**, noticeable pointed ears, **warm light-tan complexion**, **brown eyes**, thick dark brows, angular cheekbones and jaw, a modestly upturned/curl-tipped **moustache** and small **goatee** with short jaw stubble. His expression is composed, self-assured and persuasive. Visible clothing: **earth-brown high/lapelled practical coat**, muted charcoal/olive vest and open-collared off-white shirt, against an unobtrusive neutral background.

These exact face/hair/eye/skin/color/moustache choices are **owner-accepted visual interpretations** for the early-story E001 model, **not transcript-confirmed E001 descriptions**. Jon's E023 barber specification supplies useful later chronology but does **not** prove that the exact curls/side-cut are present at the opening. The E045 Diontalus-controlled face, E060 no-moustache appearance and much later Unbreakable Majesty silver-eyed face are **distinct states** and must not be silently copied back or treated as contradictions.

**Continuity checklist for the next FRONT anchor:** same face, eye color and nose/jaw structure; same wavy brown hair silhouette, moustache/goatee pattern, tan skin and ears; carry forward the visible **brown outer coat, muted dark vest and off-white open collar**, then resolve the **full-body garment construction, working pockets and rapier hip** as new owner-reviewed front-view design decisions. Do not introduce capes, later formal outfits, goggles merely from fan art, elaborate armor, late equipment, a default lute, silver eyes or an extra figure. Style: approved shared **adult-animation-influenced graphic-novel style lock v2**.

## Normalized candidate for repository registration

- Saved session-only output: `/mnt/data/Stanley_Billings_E001_Face_v1_1024_sRGB.png`
- Intended **new** repo path (not created in this step): `illustrations/references/Stanley_Billings_E001_Face_v1_1024_sRGB.png`
- Proportionally resized without crop or distortion from the **owner-accepted generator original** using Pillow LANCZOS, 1254-square → **1024 × 1024**. Output **RGB PNG**, **1,305,953 bytes**, SHA-256 `3c315ea76096eb4253ba8504a0209e48fe00fc3dfab3d691d8d22e97630d1e4d`.
- Embedded **588-byte sRGB ICC profile**, description **“sRGB built-in”** (Pillow ImageCms). Original was **untagged**; input color was **assumed sRGB**, not proven by the image's original metadata. Normalized output pixels were subsequently visually inspected; recognizability and cropped composition match the accepted source, with no observed new errors.
- **Registration verified on continuation:** the owner placed `illustrations/references/Stanley_Billings_E001_Face_v1_1024_sRGB.png` into the repository and said “Proceed” after being shown the normalized direct PNG. The MCP binary reader independently returned **1,305,953 bytes**, SHA-256 `3c315ea76096eb4253ba8504a0209e48fe00fc3dfab3d691d8d22e97630d1e4d`, matching the independently opened and inspected session export byte-for-byte. Its PNG header gives **1024 × 1024 RGB** and an ICC chunk; the byte-identical session copy's 588-byte embedded profile was parsed as **sRGB built-in**. This is owner acceptance of the normalized continuation by placement/instruction, **not a verbatim owner declaration of the SHA-256**. Accordingly the FACE anchor is `FACE_APPROVED`; never overwrite prior v0 files. The prior MCP upload limitations remain historical.

## Next single action

The E001 face anchor is now `FACE_APPROVED`, owner accepted and repository-verified. The next logical phase is a **single full-body front figure** using the exact face reference, with separate visual acceptance and repository verification before `FRONT_APPROVED`. Follow the progressive sheet workflow; the completed sheet still requires independent approval.

**Audit:** Original accepted source and normalized PNG inspected in available session environment. This report is documentation-only; no TWBD test suite run; unrelated worktree changes left untouched. [Design-sheet plan](ILLUSTRATION_STANLEY_E001_SHEET_PLAN_2026-10-25.md) · [integrated reference](../project/ILLUSTRATION_STANLEY_BILLINGS_REFERENCE.md) · [sheet ledger](../project/ILLUSTRATION_CHARACTER_DESIGN_SHEETS.md).
