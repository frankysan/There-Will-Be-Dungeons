# Hope Akmenos E001/A01 — deterministic character design sheet candidate

**Date:** 2026-10-26. **Sheet:** `WASTES-HOPE-AKMENOS-DS-001`. **Updated 2026-10-26:** `ASSEMBLED_CANDIDATE / AWAITING_OWNER_SHEET_REVIEW / REGISTRATION_PENDING / LATERALITY_LABELS_CORRECTED`. Not `OWNER_APPROVED`.

## Sources actually used

The four images were **directly attached by the owner** to the assembly request, and their decoded RGB pixels were inspected. Uploaded copies were 1024×1024 **opaque RGBA with no embedded ICC metadata**; the attached copies are not binary-identical to separately documented prior repository originals. Conversion to RGB assumes the presented RGB values use the sRGB color space, consistent with previously approved sRGB-normalized anchors; do not misstate the untagged copies as color-profile-verified.

| Source | Attached filename | SHA-256 of actual session copy |
| --- | --- | --- |
| Front | `Hope_Akmenos_E001_Front_v1_PanelsRemoved_1024_sRGB(3).png` | `f48999946a8a35272551bbc4d2aec1e8cecf0d2538c8623d5bbba0b1b7094781` |
| Paired sides | `Hope_Akmenos_E001_Side_Paired_Overview_v1_1024_sRGB(1).png` | `9e7763b7b9f26456c9cb734d4d94df73a9c6b237a10a3c419bd92d3cd892da00` |
| Back | `Hope_Akmenos_E001_Back_v1_1024_sRGB.png` | `87fed3ac2a7d25c2bf1f09681ebd472474b078d5754cbb309da61506547e884a` |
| Face | `Hope_Akmenos_E001_Face_v1_1024_sRGB(3).png` | `0e73ceb2935a290a03ddf8eefce34210600930b044730ba1ec869c765b915c75` |

The owner had previously visually accepted the side pair and full-body rear drawing. The original rear generation `1b7c8137-ddcc-42ea-9c55-5d7c622c7864` was a 1254-square, untagged PNG, and the separately normalized 1024-square tagged derivative had been verified in the chat as SHA-256 `11569e4e231a46d5b858191067fbf6bc3ec7d0cbe341675aae833763ee33fdb8`, **but no repository upload/readback is established**. Preserve `BACK_VISUAL_APPROVED / BACK_REGISTRATION_PENDING`.

## Assembly layout and checks

Created **three independently legible text-free 1024-square pages**, rather than shrinking all four full-body views into one illegible four-column sheet. All contents were assembled non-generatively using supplied source pixels:

1. **Page 1** front + back, side by side, native-size figures, no changes to anatomy/costume/props. Front cropped/translated horizontally -290px, back translated +270px horizontally and +11px vertically; empty background-only pixels are smoothly blended across x499–529. Character silhouettes/tail tips are all preserved, and the boots align at similar height.
2. **Page 2** paired anatomical profiles: **left panel is Hope's RIGHT side, facing viewer-right (→)**; **right panel is Hope's LEFT side, facing viewer-left (←)**. Same full drawing and geometry as submitted; no mirroring or scaling.
3. **Page 3** enlarged owner-accepted face reference, same submitted drawing and geometry.

All **saved final files** independently re-opened and verified: PNG format, RGB, 1024×1024 pixels, 588-byte ICC with profile description `sRGB built-in`, no text, no decorative frames or truncation. A ZIP and machine-readable per-file manifest were created in the ChatGPT session but **not registered into the repository**.

| Session page (not a repository asset) | Bytes | SHA-256 |
| --- | ---: | --- |
| `Hope_Akmenos_E001_DesignSheet_v1_Page1_FrontBack_1024_sRGB.png` | 1,495,240 | `93f41a7b2611e886e7cc9a45c3eb64285f5250f03868c6fdb4623f54dba8167c` |
| `Hope_Akmenos_E001_DesignSheet_v1_Page2_Sides_1024_sRGB.png` | 1,210,327 | `485b3304f3a2d75081824a4e9bb841e8d75fbdba5771225fd21fe49151eb59f3` |
| `Hope_Akmenos_E001_DesignSheet_v1_Page3_Face_1024_sRGB.png` | 1,569,185 | `f5d27f58ff0085d046ee591b28bafa191c46884013df9f0a5ac8007cda212f47` |

## Review blocker and next action

**`IRV-0003` resolved as anatomical file-naming error on 2026-10-26:** The owner clarified that Hope's tool holster is consistently on the **anatomical right**, and the original split file names had left and right **reversed**. Byte-identical, correctly named v2 individual profiles and a corrected JSON manifest were prepared in the session; see [side technical report](ILLUSTRATION_HOPE_E001_SIDE_TECHNICAL_GATE_2026-10-25.md). Page 2 is visually valid unchanged and its existing hash remains authoritative. **No image-content correction or reassembly required.**

**Next:** owner reviews and separately approves/rejects the three assembled pages. Exact chosen final PNG bytes, corrected individual profile files and corrected manifest must be registered under `illustrations/references/` (or another documented destination), with repository **readback** of hashes, dimensions, ICC, and correct anatomical names. Only after the final owner approval and binary registration promote the complete sheet to `OWNER_APPROVED`. Previously approved face/front remain unaffected.
