# Stanley Billings E001 — anatomical left/right profile filename correction

**Date:** 2026-10-26. **Campaign/state:** The Wastes, `WASTES-STANLEY-BILLINGS-A01`; sheet `WASTES-STANLEY-BILLINGS-DS-001`.
**Status:** `SIDE_APPROVED` retained; original side drawings remain owner approved. Metadata/filenames corrected and repository readback verified. No redraw, image flip, cropping or re-encoding.

## Finding and correct anatomy

A review of the actual [paired side illustration](../illustrations/references/wastes_stanley-billings_e001_side-paired_v01.png) and [approved front](../illustrations/references/wastes_stanley-billings_e001_front_v01.png), prompted by the owner's request to apply the same correction made for Hope Akmenos, shows the old individual left/right filenames follow the former **reversed orientation convention**. The corrected conventions in [the canonical turnaround workflow](../.agents/skills/twbd-illustration-generate/CHARACTER_SHEET.md) are:

- **Left image panel:** character faces image-right (→); camera observes the character's **anatomical RIGHT** side.
- **Right image panel:** character faces image-left (←); camera observes the character's **anatomical LEFT** side.
- Image position (left/right *panel*) and Stanley's anatomical side (right/left *profile*) are independent. Verify body-facing direction and defining asymmetries rather than trusting previous names.

The front reference puts the single sheathed rapier on **Stanley's anatomical LEFT hip** (right side of the front image). The two profile drawings and four-view assembled image are retained exactly as previously owner-approved. This update corrects **side identification metadata only**; it does not assert a new sword design, move a sheath, or re-evaluate the artist's rendering of partially occluded equipment. The historical side approval had labeled the left panel anatomical left and right panel anatomical right and must now be read with this corrigendum.

## Deterministic corrected repository assets

The exact files were copied byte-for-byte inside the connected repository using original binary PNG chunks and a new-version name. The original v1 files remain present and immutable. The binary reader confirmed matching **SHA-256 and size** for each original/alias; retained sRGB-tagged 1024×1024 RGB PNG content is therefore identical and continues to pass prior technical verification.

| Correct v2 file under `illustrations/references/` | Legacy mislabeled v1 source | Bytes | SHA-256 |
| --- | --- | ---: | --- |
| `Stanley_Billings_E001_AnatomicalRight_Side_v2_1024_sRGB.png` | `Stanley_Billings_E001_Left_Side_v1_1024_sRGB.png` | 574,210 | `c685ace99abf4e51fbae4b77d887dab8de8a9835d51e4f64de95c679f57c14eb` |
| `Stanley_Billings_E001_AnatomicalLeft_Side_v2_1024_sRGB.png` | `Stanley_Billings_E001_Right_Side_v1_1024_sRGB.png` | 548,196 | `09f65c7e94b15c4e671093ebc00f3f5325341399a94760fb0a84f58552c2b4fe` |

The [original paired PNG](../illustrations/references/wastes_stanley-billings_e001_side-paired_v01.png) is unchanged (SHA-256 `1163cc16f5ed34f1b2d7a8016330a5253cd03f2fbef7bd2037d490effc626b9a`). The existing [four-view assembled sheet](../illustrations/references/wastes_stanley-billings_e001_sheet-01-turnaround_v01.png) is also **not changed** by a metadata-only filename correction; old four-view layout positioning is unaffected.

## Approval and provenance

The owner's prior explicit acceptance of the two-profile image remains in effect. The user's 2026-10-26 message specifically requests this same anatomical-side **renaming fix for Stanley**, as was applied to Hope. This does **not** by itself approve a different generated image or affect any later story appearance. The report and sheet manifest identify the corrected v2 files as current anatomical-side references; do not use the old mislabeled v1 filenames as anatomical truth. Other historical occurrences of the old convention in earlier reports remain documented and are superseded by this dated corrigendum.

**Sheet status:** This correction preserves the previous final-sheet visual approval; independent final assembled-sheet repository promotion is a separate workflow gate from renaming the side anchors. See [final sheet visual approval](ILLUSTRATION_STANLEY_E001_SHEET_FINAL_VISUAL_APPROVAL_2026-10-25.md). No additional image generation is authorized by this correction.
