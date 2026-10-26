# Hope Akmenos E001/A01 — side-view acceptance, technical exports, and continuity review

**Date:** 2026-10-25. **Sheet:** `WASTES-HOPE-AKMENOS-DS-001`. **Updated 2026-10-26:** `SIDE_VISUAL_ACCEPTED / SIDE_REGISTRATION_PENDING / LATERALITY_LABELS_CORRECTED`. Owner confirmed the holster is consistent across views and the two split **file labels** had been reversed. Not yet `SIDE_APPROVED` (repository binary readback pending) or a completed approved sheet.

## Owner action and original output

The owner explicitly accepted the displayed two-figure side-view design in chat, and then required the artwork to satisfy the project constraints. The exact original generated PNG was directly inspected in the session at `/mnt/data/a_clean_character_design_sheet_turnaround_illust.png` (not a repository asset). Original SHA-256: `c469672f025c5bb24a02c7e7500d92b1c2ddc2b3aff1a60f9398257dd816aabc`.

**Technical fail of the original:** RGB PNG, **1536 × 1024**, **no ICC/sRGB tag**. The original cannot be registered as a compliant 1024-square production asset despite visual acceptance. Generation ID: `4b05d728-921f-4fdf-bba7-33fbc12db0d9`. Returned `edit_op:null`, `parent_gen_id:null`: owner provided an approved front image in the request, but the tool's reference-conditioning lineage is **unverified**. The internal actual prompt and exact style-lock use are not independently established.

## Deterministic 1024-square derivatives

Produced without new character drawing, mirroring, garment edits, warping, or clipping any complete figure. Technical checks performed on **saved bytes**: PNG signature/format, RGB mode, exact 1024 × 1024 dimensions, 588-byte embedded `sRGB built-in` ICC description and SHA-256. The original untagged RGB values were **assumed** to be sRGB when explicitly attaching the standard profile; this is an honest working assumption, not proof of the generator's true color space.

| Session file (NOT in repository) | Bytes | SHA-256 | Method |
| --- | ---: | --- | --- |
| `Hope_Akmenos_E001_Side_Paired_Overview_v1_1024_sRGB.png` | 1,210,329 | `edd84d7146f2bd685eed8319cc647ecfa92767eb003b141a1d8aaf2e61050bee` | Remove empty outer margins, preserve both full silhouettes, isotropically resize into square |
| `Hope_Akmenos_E001_Side_Left_v1_1024_sRGB.png` | 1,026,617 | `0bcb718afb0c25ea771fd44b3484f6e1226e2e23d1bd88204709c75eacb58212` | Actual left-panel pixels at original figure scale; neutral backdrop extension |
| `Hope_Akmenos_E001_Side_Right_v1_1024_sRGB.png` | 1,023,879 | `dfa8d85404a930338ad9c3231d3e1ef6a0917612833dbe916ea8ee6f838b1c8c` | Actual right-panel pixels at original figure scale; neutral backdrop extension |

All three saved exports were opened and visually inspected. No arbitrary filenames in this document establish repository assets. **Next binary step:** upload exact chosen PNG(s) to `illustrations/references/` and independently read back their hashes, size and ICC; the MCP image uploader accepts base64 payloads, not paths from ChatGPT's session container. Until then record `REGISTRATION_PENDING`.

## Visual fidelity and independent gate

**2026-10-26 owner correction (supersedes prior suspicion):** The holster stays on **Hope's anatomical RIGHT hip** in the approved front, back and both sides. The prior issue was the anatomical LEFT/RIGHT label applied to the separate PNGs; the actual right-facing (→), holster-near profile depicts Hope's **anatomical RIGHT** side, and the left-facing (←) profile depicts her **anatomical LEFT**. `IRV-0003` was resolved as a labeling error, **not** an image-design defect. Neither the paired art nor the composed three-page sheet needs mirroring, redrawing or recomposition. Corrected **session-only, byte-identical** names:

- `Hope_Akmenos_E001_Side_AnatomicalRight_v2_1024_sRGB.png` = original `Side_Left_v1` bytes, SHA-256 `0bcb718afb0c25ea771fd44b3484f6e1226e2e23d1bd88204709c75eacb58212`.
- `Hope_Akmenos_E001_Side_AnatomicalLeft_v2_1024_sRGB.png` = original `Side_Right_v1` bytes, SHA-256 `dfa8d85404a930338ad9c3231d3e1ef6a0917612833dbe916ea8ee6f838b1c8c`.

Historical v1 hashes/filenames above are retained as generation/export provenance; do **not** relabel those old source files in place.

**Current safe handoff:** Face and front stay `*_APPROVED`; sides are owner-accepted with correctly named, technically verified session exports, and no equipment-continuity blocker remains. **Registration/readback of the exact side files remains pending.** The back has subsequently received separate owner visual approval and session technical normalization; it too awaits repo registration. Three assembled 1024-square sheet pages are awaiting separate owner approval and repo registration. Do not declare `SIDE_APPROVED`, `BACK_APPROVED`, or `OWNER_APPROVED` prematurely.
