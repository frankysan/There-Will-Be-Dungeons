# Stanley Billings E001 two-page sheet — explicit final visual approval

**Date:** 2026-10-25. **Campaign:** The Wastes. **Subject:** `WASTES-STANLEY-BILLINGS`. **Sheet ID:** `WASTES-STANLEY-BILLINGS-DS-001`. **Appearance state:** `WASTES-STANLEY-BILLINGS-A01`, E001.

**Historical 2026-10-25 production status: `VISUAL_APPROVED / REGISTRATION_PENDING`, NOT yet `OWNER_APPROVED` at that checkpoint.** This note remains a record of the original visual-approval event. **Anatomical side labels corrected 2026-10-26**, with no changes to sheet pixels. The current repo has registered candidate files; resolving the separate completed-sheet registration state is not required for this filename correction. In the immediately preceding sheet review, the owner was shown the completed turnaround PNG and facial reference PNG, then explicitly answered **“Yes, approved.”** This accepts the **exact two-page layout**, not merely its individual anchor views. Retain the approved visuals; no re-generation or costume/face revision is authorized.

## Approved assembled candidate (session assets, not yet confirmed in project repository)

| Page | Proposed repository path | Exact session candidate SHA-256 | Verified |
| --- | --- | --- | --- |
| 1 — four body views | `illustrations/references/Stanley_Billings_E001_Sheet_01_Turnaround_1024_sRGB.png` | `c476e8d2f7063f7e2588166d91464d245e329aab03baee40ca52436f3834d04b` | 345,442 bytes; 1024×1024 RGB PNG, sRGB ICC 588 bytes |
| 2 — full-size facial reference | `illustrations/references/Stanley_Billings_E001_Sheet_02_Face_1024_sRGB.png` | `8360a6e3720e8df495819a1e7338b1557feccbe162a436082cdf70323354b128` | 1,305,953 bytes; 1024×1024 RGB PNG, sRGB ICC 588 bytes |

**Page 1:** deterministic composition from the actual supplied front, rear, and approved paired profiles. Upper left = front; upper right = back; **lower left = Stanley's anatomical RIGHT side facing image-right (→)**; **lower right = anatomical LEFT side facing image-left (←)**. This corrects the previous reversed anatomical-side labels without changing the already-approved composite image; see [2026-10-26 side correction](ILLUSTRATION_STANLEY_E001_SIDE_LATERALITY_CORRECTION_2026-10-26.md). The views were proportionally resized, retaining body/equipment rather than reinventing the character. Neutral background, no image text or decorative labels. The rear is largely coat-covered; the hidden rapier is acceptable under the earlier owner decision.

**Page 2:** user-supplied approved close-up shown at full 1024×1024; image-pixel comparison against that attached face file passed, despite differing PNG byte encoding. Do not claim this exact page has the old repository face anchor's SHA-256 (`3c315ea76096eb4253ba8504a0209e48fe00fc3dfab3d691d8d22e97630d1e4d`); it does not.

## Checks and registration gate

- **PASS:** Both exact session files re-opened and decoded as 1024×1024 RGB PNG; 588-byte embedded ICC describes **sRGB built-in**.
- **PASS:** Exact local SHA-256 values and sizes rechecked; assembled page 1 visually inspected.
- **PASS:** Explicit owner approval of the two **combined** pages, separate from anchor approvals.
- **PENDING:** The two exact composed PNGs must be placed at the paths above. The available workspace PNG create/chunk API requires encoded base64; a session `/mnt/data` filename cannot be passed as a file object. No successful repository upload has been demonstrated for these assembled files.
- **PENDING:** After upload, re-read both repository files and compare exact SHA-256, bytes, 1024×1024 dimensions, PNG signature and sRGB ICC. Update ledger and subject status to `OWNER_APPROVED` **only then**, preserving this visual decision.
- **Existing back reference caution:** repository entry `Stanley_Billings_E001_Back_v1_1024_sRGB.png.png` currently reports **1254×1254 PNG IHDR** despite its name. A **new session-only, separately verified normalization** was prepared as `Stanley_Billings_E001_Back_v2_1024_sRGB.png` (**1,009,023 bytes, SHA-256 `d3d3d1d658c01a089f5fd2b6485ac01d85ccdcfcd1bb4ee3a39e98b988d112c7`, RGB 1024×1024, 588-byte sRGB ICC**). Source was 1254×1254 RGBA with fully opaque alpha and no ICC; sRGB is an **assumption** for the input, not a proven source profile. This is a proportionally Lanczos-resized exact-artwork derivative with no new design features. **Upload and read back this new anchor too**, then confirm the existing rear visual approval against the derivative before `BACK_APPROVED`.
- **Testing:** full project tests not run; no executable code changed, only this approval/provenance report.

Companion session manifest: `Stanley_Billings_E001_Sheet_Manifest.json` (contains the exact page hashes and current registration state). Session copies are not durable repository registration.

**Next action:** register the two exact approved page PNGs and resolve any remaining individual back technical gate; verify repository readback; then promote the *completed* E001/A01 sheet to `OWNER_APPROVED` without requesting another visual decision unless the pixels change.
