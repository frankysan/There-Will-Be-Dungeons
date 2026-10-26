# Nash Maggard — E001 side-profile deterministic normalization (2026-10-26)

**Campaign/subject:** The Wastes / `WASTES-NASH-MAGGARD`. **Request:** owner asked for an updated E001 paired side reference using the established E000/A01 costume/front anchor. The request label `E001` does not by itself establish a new appearance state: treat as a candidate continuation of A01 pending story-scope confirmation. **Result:** technical exports prepared locally; **visual owner approval of these exact exports and repository asset registration remain pending**.

## Source and non-generative corrections

- The user supplied the *already cleaned and geometrically corrected* side-pair `Nash_Maggard_E001_Side_References_Final(1).png` (1536 × 1024, RGBA with alpha 255 everywhere, untagged PNG); SHA-256 `747efa2e36356f3a4f48dc107f4da61b25140c40d1289008df6ea34d7e17fa0b`; 2,722,049 bytes.
- The source used for this procedure is **not** a fresh image-generation result. Earlier free-form regenerations changed Nash's features and were rejected; **do not regenerate or repaint to normalize**.
- Source left panel: character's anatomical **RIGHT**, looking image-right (→); seeing right eye, staff in right hand. Source right panel: anatomical **LEFT**, looking image-left (←); damaged red left eye and left-hip satchel. Staff bears Freedom, a transverse iron nail. These are the existing source-image facts to preserve, not a reason to relabel/mirror character pixels.
- The canonical `CHARACTER_SHEET.md` and `CHARACTER_SHEET_PROMPTS.md` in the active workspace **already contain the corrected anatomical orientation convention** (from the Hope E001 audit). No redundant direction reversal or template change was made.

## Technical exports (session files, not registered repository assets)

| Filename | SHA-256 | Bytes | Treatment |
| --- | --- | ---: | --- |
| `Nash_Maggard_E001_Side_Paired_v1_1024_sRGB.png` | `01fb8ddb8d9403a535042c917cd72a3bbc7a644b334ce17348df805058f40035` | 831018 | Whole 1536×1024 source uniformly fitted to a 1024×683 region within a 1024-square neutral canvas, y=170; background-only top/bottom extension. |
| `Nash_Maggard_E001_Side_AnatomicalRight_FacingRight_v1_1024_sRGB.png` | `3a980dceb11365052985b699a0e388fad9f9a0a4b6622818ac489cce53c428b5` | 891606 | Exact original left-half crop x=[0,768), padded 128 px each side; no scaling or mirroring. |
| `Nash_Maggard_E001_Side_AnatomicalLeft_FacingLeft_v1_1024_sRGB.png` | `21ee5101e709c597b04cdf61655f2d085e6166b8aa1ef5bf1bc015f2e4bd37b0` | 921862 | Exact original right-half crop x=[768,1536), padded 128 px each side; no scaling or mirroring. |

All three files were re-opened and validated as **1024×1024 RGB PNG with embedded "sRGB built-in" ICC profile**. Because the supplied original is **untagged**, the source RGB interpretation as sRGB is an explicit assumption, **not verified historical colorimetry**. The two full-resolution single-profile crops passed exact RGB pixel comparison against the corresponding source half in their central 768×1024 regions. The paired export's central 1024×683 rectangle passed exact comparison against the deterministic Lanczos-resized source. No character pixels were cropped, painted, mirrored, or independently regenerated.

A manifest and checked ZIP package were created in the working session alongside the PNGs. Session files are **not automatically repository files**. Do **not** mark `SIDE_APPROVED` for this **new E001 candidate**, do not replace the older already owner-approved `illustrations/references/Nash_Maggard_Side_v2_HoodUp_1024_sRGB.png`, and do not claim a new asset is registered merely because a proposed path appears here.

## Decision/status and remaining action

1. **Candidate normalized / technical gate PASS.** All three local exports meet file format/dimension/ICC checks. The left/right source artwork is preserved.
2. **Visual approval PENDING.** User's instruction to proceed with technical cleanup is not treated as explicit owner visual acceptance for these exact derivatives.
3. **Repository registration PENDING.** After owner visual approval, upload exact PNG bytes as *new*, non-overwriting paths under `illustrations/references/`, then read them back to independently verify SHA-256, dimensions, image pixels, and embedded profile. Connected text-edit tools cannot currently ingest session image file paths directly as PNG bytes.
4. **Existing approvals remain unchanged:** Nash E000/A01 face/front/hood-up side/back anchors retain their repository-approved status, and the existing composite remains awaiting owner review. This report records a *separate E001 candidate*, not a supersession.

**Source documents:** [Nash appearance reference](../project/ILLUSTRATION_NASH_MAGGARD_REFERENCE.md), [design-sheet ledger](../project/ILLUSTRATION_CHARACTER_DESIGN_SHEETS.md), [canonical workflow](../.agents/skills/twbd-illustration-generate/CHARACTER_SHEET.md), [paired-side template](../.agents/skills/twbd-illustration-generate/CHARACTER_SHEET_PROMPTS.md), [house style](../project/ILLUSTRATION_GUIDE.md).
