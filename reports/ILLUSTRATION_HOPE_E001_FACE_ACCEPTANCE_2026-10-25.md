# Hope Akmenos — E001 face approval and export audit (2026-10-25)

**Scope:** Wastes / `WASTES-HOPE-AKMENOS`, first-appearance `A01` (E001), reserved sheet `WASTES-HOPE-AKMENOS-DS-001`. **Stage:** `FACE`; **status: owner accepted / compliant exported derivative / repository registration pending**. Earlier [first face attempt](ILLUSTRATION_HOPE_E001_FACE_ATTEMPT_2026-10-25.md) superseded visually by the dark-maroon correction, not deleted.

## Owner selection and lineage

1. Initial portrait: generation `3a3acc3f-2bf2-4082-b8ad-3146450a638c`, `/mnt/data/a_clean_character_sheet_portrait_illustration_on.png` (first attempt report). Owner requested **darker skin** because the design brief specifies **deep maroon**; **original lighter skin version was not approved**.
2. Revised *darker maroon* face: generation ID `dbc90a81-77e9-42e5-9cbf-d51f4b53f693`, session original `/mnt/data/darker_maroon_tiefling_steampunk_portrait.png`. Owner response: **“Yes, accepted.”** This is the **visually approved E001 face identity**, not an accepted whole character sheet or full-body outfit.
3. Revised-source byte audit: **PNG**, RGB, **1254 × 1254**, **2,403,880 bytes**, SHA-256 `c268845518412187063fb06c1181bf7cfa12a85eee78da83701543ac7357cdef`. No embedded ICC profile / sRGB tag in Pillow metadata. The original **fails technical export criteria**; do not upload it as if it were a compliant canonical `1024_sRGB` image.
4. Prepared proportionally downscaled version, session file `/mnt/data/Hope_Akmenos_E001_Face_v1_1024_sRGB.png`, target future repo path `illustrations/references/Hope_Akmenos_E001_Face_v1_1024_sRGB.png`. **PNG**, RGB, **1024 × 1024**, **1,569,186 bytes**, SHA-256 `1ef34cf6f619757df4e51e0f12a151965f1ed3381506af1b1c06c65667d3c91d`. PIL Image.Resampling.LANCZOS downscale of accepted square (no crop, no aspect distortion, no generative additions). Embedded verified **588-byte sRGB built-in ICC** (`iCCP` PNG chunk; `ImageCms.getProfileName`: `sRGB built-in`). Untagged source RGB was **assumed sRGB** for profile assignment, not measured or proven. PNG decoded and visually inspected again at 1024 square; same face/hair/horns/accessories/skin shade preserved. The export file itself is not a new generative redesign.
5. The accepted visual rendering and its compliant derivative are **session-only** as of this report. The workspace PNG API accepts base64 bytes but not source paths or generated session file IDs; no verified byte-transfer bridge from this image file to that API was available in this invocation. **No PNG uploaded, no repository image readback performed, so no `FACE_APPROVED` status claimed yet.** Await registration of the *exact hash-listed derivative*, with independent inspection of the registered file.

## Visual/content review

| Gate | Verdict | Evidence / qualification |
| --- | --- | --- |
| E001 organic tiefling face / two horns | PASS | Two intact textured organic horns, both attached to head; pointed ears; no later metallic horn or implants |
| Identity and palette | PASS (owner design selection) | Owner accepted revised visibly **dark maroon** skin; purple hair, gold eyes and warm confident expression. These colors derive originally from a **later** character JSON and remain provisional *early-story evidence* despite being **locked for this approved artistic face**. |
| E001 continuity | PASS for visible area | No left mechanical body modification, later Hand, queen crown, mirror-restoration marks, advanced weapons. Full limbs and tail are **outside a bust** and must still be checked at front stage. |
| Costume / prop chronology | OWNER-ACCEPTED DESIGN CHOICE, E001 WEAR UNVERIFIED | Brass-rimmed goggles, utility vest and a small necklace appear. They are plausible engineer/character-note visual choices, but episode-one wear and exact keepsake identity are unverified. Do not present as spoken E001 canon. Full-body outfit construction is still pending owner selection. |
| General TWBD v2 art direction | PASS, with minor style watch | Bold variable dark outlines, stylized expressive anatomy, graphic shadow masses, subdued neutrals, readable silhouette, neutral background, mature look. **Some fine hatching/texture is denser than the style guide's preferred restraint**; do not extrapolate it into exaggerated gritty/photoreal shading or claim exact pixel comparison with Nash/Stanley anchor images in this invocation. |
| Single portrait / no lettering / square | PASS | One head-and-shoulders figure, neutral background, no inscriptions or watermark. |
| Original pixel dimensions and color tag | FAIL | Original 1254 square, untagged |
| Normalized PNG 1024 × 1024 / decoded RGB / ICC tag | PASS | Actual saved bytes inspected, PNG `IHDR` + `iCCP` + `IEND`, profile name checked |
| Preservation across normalization | PASS | Same framing/proportions; image visually checked. Diagnostic 1024→1254 round-trip mean channel difference ~1.03/255 (resampling only, not a claim of identical pixels). |
| Repository registration and byte-for-byte readback | NOT DONE | Must upload exact SHA `1ef34cf6…`; record verified dimensions/profile/SHA before `FACE_APPROVED`. |
| Full character sheet approval | NOT APPLICABLE | Front, paired sides, back, assembled pages remain pending |

**Next action:** upload the verified 1024-square sRGB PNG at the target repository path **without overwriting any prior accepted file**; read it back and match the full SHA-256, byte count, PNG dimensions, embedded ICC sRGB profile. Then update stage to `FACE_APPROVED` and use that **actual registered PNG** as the visual reference/attachment for `$twbd-illustration-generate Wastes "Hope Akmenos" E001 design-sheet front`.

**Checks at original acceptance:** PNG decode, IHDR, ICC identity, dimensions, SHA-256 and visual derivative check **PASS** for exported file. Subsequent repository registration readback is documented below; no TWBD code/test suite run.

## Registration completed — subsequent readback, 2026-10-25

The previously missing file now exists at [`illustrations/references/Hope_Akmenos_E001_Face_v1_1024_sRGB.png`](../illustrations/references/Hope_Akmenos_E001_Face_v1_1024_sRGB.png). Connected repository binary read verified MIME `image/png`, **1,569,186 bytes**, SHA-256 **`1ef34cf6f619757df4e51e0f12a151965f1ed3381506af1b1c06c65667d3c91d`**, matching exact visually accepted normalized session output; PNG IHDR is 1024×1024 RGB and `iCCP` is present. Session file was reopened, decoded and the embedded ICC inspected as `sRGB built-in` (588 bytes). The exact reference was visually inspected: deep-maroon skin; two organic ram horns; purple swept-back gathered hair, amber-gold eyes, pointed ears, goggles on crown; white collared shirt, weathered dark utility vest and small round pendant. **FACE_APPROVED** for E001/A01 only. This status supersedes the original report's `REGISTRATION_PENDING` statements; preserve their original chronology. **FRONT is now eligible but remains a separate owner review.**
