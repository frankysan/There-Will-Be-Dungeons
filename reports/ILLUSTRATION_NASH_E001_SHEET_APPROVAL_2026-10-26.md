# Nash Maggard — E001 four-view design-sheet visual approval (2026-10-26)

**Subject:** The Wastes / `WASTES-NASH-MAGGARD`. **Baseline state:** A01 costume/character identity, requested as E001. **Sheet identifier:** `WASTES-NASH-MAGGARD-DS-001` with this E001 image as a new, independent candidate; do not silently replace the approved E000 references or previously assembled E000 pages.

## Owner visual decision

The owner replied **"Approved."** to the **specific four-view design-sheet image** shown in the preceding conversation, generated as `/mnt/data/weathered_hooded_wanderer_turnaround.png` (`gen_id=a4a1c9d8-1d33-4fa9-8539-a79f32cdda49`). Thus its **appearance and composition are visually accepted**, and do **not** need another artistic approval merely because the export is normalized without a visible redesign.

- Upper-left: anatomical RIGHT side, facing image-right (→); upper-right: front.
- Lower-left: back; lower-right: anatomical LEFT side, facing image-left (←).
- Identity/outfit audit: ragged rust-red hood and cloak, wrapped hands/legs, layered gray clothing, worn boots, left red/sightless eye, left-hip bag, right-hand staff with the iron nail `Freedom` through the wooden shaft. No lettering, watermark, prop panels or decorative captions.
- This is an **approved visual exception to the preferred deterministic sheet-assembly method**, because the selected image was generated as a four-view layout. It is **not** proved to be a pixel-exact layout of the already approved front, sides and back. Its art approval does not rewrite approvals or SHA-256 hashes of the original anchors. Keep this provenance transparent rather than implying source pixels were pasted unchanged.

## Technical image audit and conforming derivative

| Artifact | Dimensions | Color profile | SHA-256 | Bytes |
| --- | --- | --- | --- | ---: |
| Owner-approved original `weathered_hooded_wanderer_turnaround.png` (conversation-only) | 1254 × 1254 RGB PNG | no ICC profile | `b115feffd2bcb5078872e50f0c7f0e4e758217b9a7b0c4f57995c3661103f062` | 1,921,673 |
| Normalized `Nash_Maggard_E001_Design_Sheet_v1_1024_sRGB.png` (conversation-only) | **1024 × 1024 RGB PNG** | embedded 588-byte **"sRGB built-in"** ICC | `fd64c349b2d0d8c643530fee62ca559e6e5e2e85587a5cd3c0eedbcb58b4cdbd` | 1,202,634 |

- Transformation: full-image **uniform Lanczos downsample** 1254×1254 → 1024×1024, **no crop, no mirror, no new generative call, and no addition/removal of any artwork**. The normalized image was decoded and visually inspected.
- The source's original RGB colorimetry is **unknown** because it was untagged. Export presumes sRGB and embeds the appropriate profile; do not claim this proves original encoding.
- A JSON manifest and ZIP containing the PNG/manifest are available as conversation artifacts, not repository files.

## Stage/status

- **New E001 sheet: `FINAL_SHEET_VISUALLY_ACCEPTED / REPOSITORY_REGISTRATION_PENDING`.** Technical export validated. The owner's "Approved" explicitly applies to the presented four-view image; no further redundant visual approval is required for a faithful technical normalization.
- **Do not mark `OWNER_APPROVED` in the canonical registry** until the **exact derivative PNG** is transferred to `illustrations/references/wastes_nash-maggard_e001_sheet-four-view_v01.png` and independently read back to verify SHA-256, PNG size and ICC tag.
- The local workspace MCP accepts source text edits and PNG base64 uploads but cannot directly import `/mnt/data/` session files by path. **No PNG has been uploaded into the repository through this audit.**
- The existing E000/A01 `FACE_APPROVED`, `FRONT_APPROVED`, `SIDE_APPROVED`, `BACK_APPROVED`, and its separate two-page `AWAITING_OWNER_REVIEW` composite remain unaffected. The previously prepared E001 paired-side anchors and separately owner-approved E001 rear have their own independent registration status.
- Treat E001 as the user-requested episode label tied to A01 design continuity pending a deliberate story-state entry; it is **not evidence of new costume/scarring chronology**.

**Related:** [Nash character reference](../project/ILLUSTRATION_NASH_MAGGARD_REFERENCE.md) · [Nash E001 paired sides](ILLUSTRATION_NASH_E001_SIDE_NORMALIZATION_2026-10-26.md) · [canonical sheet protocol](../.agents/skills/twbd-illustration-generate/CHARACTER_SHEET.md) · [sheet ledger](../project/ILLUSTRATION_CHARACTER_DESIGN_SHEETS.md).
