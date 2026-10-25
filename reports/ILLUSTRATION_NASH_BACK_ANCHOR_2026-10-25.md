# Nash Maggard — E000 back-view anchor, approved visual and export

**Date:** 2026-10-25. **Subject:** `WASTES-NASH-MAGGARD`; **sheet:** `WASTES-NASH-MAGGARD-DS-001`; **story state:** `WASTES-NASH-MAGGARD-A01` / E000.

## Visual selection and provenance

- Owner explicitly approved the single full-figure rear-view render in the conversation: **“Yes, accepted.”** This selection applies to the image shown, not a complete character design sheet.
- Image generation ID: `9e58bbe1-cbd2-478a-9c34-1c65bf87fd50`. Original generated session file: `/mnt/data/tattered_hooded_wanderer_with_staff.png`. The tool-provided generated-image metadata did not contain a replayable prompt; actual image conditioning is not independently verified.
- **Full-body back view:** Nash stands with his **rust/umber hood raised**, ragged layered cape with irregular frayed hem, wrapped arms and lower legs, worn boots, a threadbare satchel resting near his **left hip** and its strap diagonally across the cloak from the **right shoulder area**, and staff in the **right hand**. The staff’s actual old nail **Freedom** visibly passes *horizontally through the wood near its top*, with head and point visible on opposite sides; no later Skyblinder bird ornament, spearhead or ornamental cap.
- The neutral grey studio-like background is not a story location. Character identity, outfit, hood-up configuration and staff construction were inspected in the normalized export and found visually consistent with the user-accepted front/hood-up side direction. Side-specific strap/gear placement should be checked again when assembling a unified sheet; visual approval is not independent episode proof.
- Rights/source distinctions remain per [Nash’s written reference](../project/ILLUSTRATION_NASH_MAGGARD_REFERENCE.md) and [illustration style v0.6](../project/ILLUSTRATION_GUIDE.md). Baldness, burn details, eye laterality and costume are partly owner-directed art choices; this back view does not establish otherwise.

## Original and normalized PNG inspection

| Asset | Dimensions, format and color | SHA-256 |
| --- | --- | --- |
| Session original: `/mnt/data/tattered_hooded_wanderer_with_staff.png` | **1254 × 1254**, RGB PNG, **no embedded ICC profile**; **1,919,244 bytes** | `4df22d0e7d35268457621ad774e381c8e6710da09b73d7e9ee661e519a7a31f3` |
| Prepared non-destructive export: `/mnt/data/Nash_Maggard_Back_v1_1024_sRGB.png` | **1024 × 1024**, RGB PNG, **588-byte embedded sRGB ICC profile** (`sRGB built-in`), **1,222,125 bytes** | `9f348f34ac86dd79f33cd9c59342b04c6d2267a99d908c8eea528b11c99f95d1` |

Conversion: separate PNG exported with Pillow's **Lanczos** downsampling from the original entire square; **no crop, mirror, repaint, retouch or overwrite**. Because the original had no color profile, it was **assumed** that its RGB sample values represented sRGB before tagging the exported derivative; this does *not* establish the generator's actual colorimetry. The derivative’s dimensions, embedded profile and preserved whole-figure composition were checked by opening the saved file and inspecting its image data. A ZIP alternative `/mnt/data/Nash_Maggard_Back_v1_1024_sRGB.zip` was created and checked for ZIP integrity.

## Repository registration gate

**Owner-approved visual design + technically compliant session export does not equal a file registered in the project repo.** Expected destination:

`illustrations/references/Nash_Maggard_Back_v1_1024_sRGB.png`

At the time of this report, repository asset listing contained the accepted face and front images and the **hood-up side v2** image, but **not** the back export. The current MCP create/upload commands accept base64 image data and do not accept a generated image's local path or file ID directly. Do not initialize a new empty upload or falsely record a completed upload. Copy/upload this exact PNG through an available supported path, then read back the workspace binary header + SHA-256 and confirm it matches the value above. After that, record **`BACK_APPROVED`** for this exact `A01` version.

**Current status:** `BACK_VISUAL_APPROVED` (owner) + local PNG technical checks passed; **`BACK_REGISTRATION_PENDING`**. Previously, **`FACE_APPROVED`** and **`FRONT_APPROVED`** were established. The side v2 was approved by the owner; its repository contents have now been read and matched its expected SHA-256 `4a7bb1f07755a047f2ce430deb6d01e935db0b771b71d9a9fa1bb61a336337d5` (1024 × 1024 RGB PNG with embedded ICC), so **`SIDE_APPROVED`** is now supported. The **complete multi-view sheet** remains drafting, not approved.

## Next design-sheet step

Once the back file is registered and verified, assemble **text-free** page(s) from the four accepted anchors rather than re-inventing them: comparable front/side/back views on page 1, face close-up and optional detail panels on page 2 if needed. Preserve all original anchor versions and source research; a sheet needs its own technical checks and separate final owner acceptance before general scene-illustration reuse. Do not introduce a mismatched eye side or nail geometry in the assembly.

## Subsequent repository registration — 2026-10-25

The owner placed `illustrations/references/Nash_Maggard_Back_v1_1024_sRGB.png`
in the repository during this work. A fresh read of its workspace binary
confirmed **1,222,125 bytes**, **1024 × 1024**, **8-bit RGB PNG**, an
embedded `iCCP` color-profile chunk named `ICC Profile`, and full-file
SHA-256 `9f348f34ac86dd79f33cd9c59342b04c6d2267a99d908c8eea528b11c99f95d1`.
The hash is **exactly identical** to the saved inspected owner-accepted
sRGB-tagged derivative. Therefore **`BACK_APPROVED`** is now recorded
for this specific E000/A01 back reference. Earlier pending-registration
language in this report documents the previous state, not the current
one. The complete model sheet is **still not approved**: all four input
anchors are approved, but layout pages still need assembly, visual and
technical checks, and separate explicit owner approval.
