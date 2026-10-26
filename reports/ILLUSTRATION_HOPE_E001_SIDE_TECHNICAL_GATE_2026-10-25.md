# Hope Akmenos E001/A01 — side-view acceptance, technical exports, and continuity review

**Date:** 2026-10-25. **Sheet:** `WASTES-HOPE-AKMENOS-DS-001`. **Status:** `SIDE_VISUAL_ACCEPTED / SIDE_REGISTRATION_PENDING / CONTINUITY_REVIEW_NEEDED`; NOT `SIDE_APPROVED` or a complete approved sheet.

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

The accepted front shows the substantial tools/tool holster on **Hope's anatomical RIGHT hip** (viewer's left), and a trailing cloth sash on **her anatomical LEFT** (viewer's right). The **left-facing-right** profile in the generated pair displays the prominent tool rig on its near-visible side, while the **right-facing-left** profile does not comparably show it; this suggests the asymmetric gear may have switched sides. This is an **image-inspection concern**, not newly discovered narrative canon: refer to `IRV-0003` and compare against the actual repository-approved front before a final side continuity pass. The exact 1024-square derivatives faithfully preserve the accepted art, including this potential problem; resizing and tagging **do not cure it**. Do not quietly reinterpret acceptance as a waiver or silently edit the rig without recording a design decision.

**Current safe handoff:** Face and front stay `*_APPROVED`. Side visuals are owner-accepted, with physical-image technical exports verified **in session** but not repository-registered; anatomical-side equipment continuity remains to be reconciled. Do **not** start or mark the back stage as approved based on a premature `SIDE_APPROVED` assertion, and do not declare the whole sheet `OWNER_APPROVED`.
