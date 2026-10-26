# Hope Akmenos — E001/A01 character design sheet: final owner approval

**Date:** 2026-10-26. **Campaign:** The Wastes. **Subject / sheet:** `WASTES-HOPE-AKMENOS-DS-001`. **State:** `WASTES-HOPE-AKMENOS-A01` (organic introduction-era baseline). **Final decision:** `OWNER_APPROVED`, v1 three-page visual reference.

## Explicit approval and scope

The owner approved the full three-page assembled sheet in chat (“Yes, approved.”, 2026-10-26), **after** explicitly resolving the former equipment-continuity concern as a side-file *anatomical labeling* error rather than an illustration fault. This is approval of the **exact unchanged assembled page pixels** listed below, not retroactive approval of all appearances/variants. Front, paired side profiles, rear and face are supported as the E001 organic baseline, and the separate face/front/side/back anchor approvals remain in their own history. Do not transpose late cybernetics (anatomical left arm/leg and horn), E088 restoration, or E101 right Hand of the Voice into E001.

**Correct side-panel semantics (anatomical, not sheet position):**
- Viewer-left panel: Hope's **anatomical RIGHT** side, character faces right (→), tools/holster visible on the correct right hip.
- Viewer-right panel: Hope's **anatomical LEFT** side, character faces left (←).
- All previously alleged tool-holster inconsistencies are cleared; `IRV-0003` was closed as a filenames/metadata correction. No image mirroring or redesign was needed.

## Actual repository readback and technical checks

On 2026-10-26 the connected workspace listed the following exact repository files under `illustrations/references/`. Each was **read back from the repository's binary endpoint**, with its returned byte count and SHA-256 matched to the previously verified session export; the first PNG bytes carry a 1024×1024 RGB IHDR and an embedded `iCCP` chunk. The earlier session technical checks decoded the complete export as RGB PNG, 1024×1024 with a 588-byte profile described as `sRGB built-in`. The original owner-uploaded RGBA anchors used during assembly were untagged; their RGB values were treated as sRGB when generating the final tagged exports, as documented in the assembly report, rather than assuming their original profile was proven.

| Exact verified repository asset | Bytes | SHA-256 |
| --- | ---: | --- |
| `illustrations/references/Hope_Akmenos_E001_DesignSheet_v1_Page1_FrontBack_1024_sRGB.png` | 1,495,240 | `93f41a7b2611e886e7cc9a45c3eb64285f5250f03868c6fdb4623f54dba8167c` |
| `illustrations/references/Hope_Akmenos_E001_DesignSheet_v1_Page2_Sides_1024_sRGB.png` | 1,210,327 | `485b3304f3a2d75081824a4e9bb841e8d75fbdba5771225fd21fe49151eb59f3` |
| `illustrations/references/Hope_Akmenos_E001_DesignSheet_v1_Page3_Face_1024_sRGB.png` | 1,569,185 | `f5d27f58ff0085d046ee591b28bafa191c46884013df9f0a5ac8007cda212f47` |
| `illustrations/references/Hope_Akmenos_E001_Side_AnatomicalRight_v2_1024_sRGB.png` | 1,026,617 | `0bcb718afb0c25ea771fd44b3484f6e1226e2e23d1bd88204709c75eacb58212` |
| `illustrations/references/Hope_Akmenos_E001_Side_AnatomicalLeft_v2_1024_sRGB.png` | 1,023,879 | `dfa8d85404a930338ad9c3231d3e1ef6a0917612833dbe916ea8ee6f838b1c8c` |
| `illustrations/references/Hope_Akmenos_E001_Side_Paired_Overview_v1_1024_sRGB.png` | 1,210,329 | `edd84d7146f2bd685eed8319cc647ecfa92767eb003b141a1d8aaf2e61050bee` |
| `illustrations/references/Hope_Akmenos_E001_Back_v1_1024_sRGB.png` | 1,258,514 | `11569e4e231a46d5b858191067fbf6bc3ec7d0cbe341675aae833763ee33fdb8` |
| `illustrations/references/Hope_Akmenos_E001_Face_v1_1024_sRGB.png` | 1,569,186 | `1ef34cf6f619757df4e51e0f12a151965f1ed3381506af1b1c06c65667d3c91d` |
| `illustrations/references/Hope_Akmenos_E001_Front_v1_PanelsRemoved_1024_sRGB.png` | 1,244,152 | `8c19629c99f5111bc56735473d9024d31a6a289f4cd6961b4d428bad48a960e1` |

The associated `illustrations/references/hope-e001-manifest-corrected.json` was present and read. **Its pre-approval `AWAITING_OWNER` fields must be superseded by the present final decision;** update the manifest's decision and repository-registration metadata while leaving input filenames, hashes, pixel semantics and historical notes intact.

## Decision and release handling

`FACE_APPROVED`, `FRONT_APPROVED`, `SIDE_APPROVED`, `BACK_APPROVED`, and completed three-page v1 sheet `OWNER_APPROVED` are now supported for E001/A01. This approval indicates the internally registered reference package, **not** an assertion of website publication or commit/push of the present text edits.

See also [assembly manifest/history](ILLUSTRATION_HOPE_E001_SHEET_ASSEMBLY_2026-10-26.md), [side export and naming report](ILLUSTRATION_HOPE_E001_SIDE_TECHNICAL_GATE_2026-10-25.md), [subject reference](../project/ILLUSTRATION_HOPE_AKMENOS_REFERENCE.md) and [sheet registry](../project/ILLUSTRATION_CHARACTER_DESIGN_SHEETS.md).
