# Nash Maggard — E000 side/profile anchor review (2026-10-25)

**Subject:** `WASTES-NASH-MAGGARD`; **sheet:** `WASTES-NASH-MAGGARD-DS-001`; **applicable appearance:** `WASTES-NASH-MAGGARD-A01` / E000.

## Owner's decision and rendered study

- **Owner feedback:** “Yes.” immediately following the displayed side/profile turnaround render on 2026-10-25. Record as **SIDE VISUAL DESIGN ACCEPTED** for this **paired opposing-profile image**, not as approval of any final multi-view character sheet. Do not turn “Yes” into source-evidence or confirmation that the image is already stored in the repository.
- **Generation ID:** `3f64de82-7f19-46cf-8c63-858f1eafc7ae`; initial session file `/mnt/data/a_clean_studio_like_character_concept_turnaround.png`.
- **Composition:** Two complete, facing-opposite profile figures on a neutral background, one looking left and one looking right. This is an **accepted paired-side study** even though the original proposed phase requested one single profile view. No text labels. Both figures carry a staff with an **old iron nail passing horizontally through its upper wooden section**; rust-red ragged cloak, partially lowered hood, scarred nearly bald head, head/face and forearm bandaging, muted travel garments, boots and worn satchel remain recognizable.
- **Visual continuity cautions:** Unlike the owner-approved **hood-up** front view, both profiles present **hood down / scalp exposed**. Treat that as a *hood configuration variation*, not an unexplained change to Nash's hair, scars or standard costume. A strict same-outfit/same-pose turnaround must either reconcile the hood for the back view or include an explicit reference note. Facing-opposite profiles may mirror details; do not assume lesions, satchel shoulder, red **LEFT** eye, or nail head/point should simply be reflected when creating a back or story illustration. Where not directly seen, follow the explicit written left/right decisions and approved front anchor, not model guesses.
- **Existing reference:** The owner's approved front anchor `illustrations/references/wastes_nash-maggard_e001_front_v01.png` is the master for the outfit and proportions. The face anchor `illustrations/references/wastes_nash-maggard_e001_sheet-02-face_v01.png` was **explicitly owner-approved**, is present in the repo, and its SHA-256 `93e82eff061afd08611d0e6cf4fe8dfd11058ed94985c8c10a9d42140947cb71` and 1024-square embedded ICC profile were independently checked. The register now records **`FACE_APPROVED`**, separate from the side-view decision.

## Original and separate technical export

| Asset | SHA-256 | Inspection | Status |
| --- | --- | --- | --- |
| Session original `/mnt/data/a_clean_studio_like_character_concept_turnaround.png` | `47bdbd58bda90384e5d04055fa02b52452df1f20f7929d1ed2aa2e5247e2aa26` | 1254 × 1254, RGB PNG, **no embedded ICC profile** | **Owner accepted the appearance**, **not** production-size-compliant |
| Derived `/mnt/data/Nash_Maggard_Side_v1_1024_sRGB.png` | `86fe9b11dbd4c07c6164e2a47a23b4525b7c93df2afaeda597790d67ea3e73d6` | 1024 × 1024 RGB PNG, embedded **588-byte sRGB ICC profile**; **1,565,273 bytes**; generated with full-image Lanczos resize, **no crop/mirror/painting** | Meets pixel-size and tagged-color-file requirements; **not yet verified in project workspace** |

The original untagged source RGB was **assumed** to represent sRGB when exporting. Tagging the derivative does not prove the generator's original color intent. Session paths are not automatically canonical repository paths. The generated-image tool's metadata exposed an empty prompt field, so exact prompt delivery and source-image conditioning cannot be reconstructed from that metadata.

**Next asset placement:** copy or upload the derived PNG **without overwriting any existing file** to `illustrations/references/Nash_Maggard_Side_v1_1024_sRGB.png`, check its full-file SHA-256 against `86fe9b11dbd4c07c6164e2a47a23b4525b7c93df2afaeda597790d67ea3e73d6`, and explicitly bind owner visual acceptance to that content-verified file. At that point record `SIDE_APPROVED` in the sheet ledger. Until then, stage status is **SIDE VISUAL ACCEPTED / FILE REGISTRATION PENDING**, not `SIDE_APPROVED`.

## Corrections and final owner selection — hood-up v2

After viewing the first side profile pair, the owner observed that in the
right-hand profile **Freedom appeared beside the staff rather than physically
passing through its wood**. That discrepancy invalidates the earlier
`SIDE VISUAL ACCEPTED` status for the first generated render; it is retained
only as a historical draft. A first correction was generated on 2026-10-25
(`gen_id=8f73c57f-7969-4d0e-a48a-d5b8b25f2b05`;
`/mnt/data/scarred_wanderer_profile_turnaround.png`).
The owner then requested **hood up on both profiles**, matching the
previously approved front anchor.

The revised two-profile **hood-up** render (`gen_id=6b8dfa98-c6f0-411e-8911-3eb201d8929d`;
original session file `/mnt/data/wounded_hooded_wanderer_turnaround.png`)
was displayed and **explicitly accepted** by the owner: “Yes, I accept this
one. See if you can use the MCP server to write the PNG now.”

For future artwork, this is the **preferred side/profile visual reference**.
Both figures wear the rust-red hood up; their staff nails appear driven
transversely through the *upper wooden shaft*, with nail head and point
protruding on opposite sides. Keep the original owner-approved front design
and correct left/red eye orientation; do not treat opposite-facing profiles
as freely interchangeable mirrors for anatomical or gear sidedness.

### Verified technical export for selected v2

| Artifact | SHA-256 | Inspection |
| --- | --- | --- |
| Selected original `/mnt/data/wounded_hooded_wanderer_turnaround.png` | `3129ab7695221fce5306012daa53ea50455d1031d324c91ceb4327c3ecef17f5` | Actual **1254 × 1254 RGB PNG**, **2,164,445 bytes**, unprofiled |
| Session derivative `/mnt/data/Nash_Maggard_Side_v2_HoodUp_1024_sRGB.png` | `4a7bb1f07755a047f2ce430deb6d01e935db0b771b71d9a9fa1bb61a336337d5` | Actual **1024 × 1024 RGB PNG**, **1,412,227 bytes**, embedded **588-byte sRGB ICC**, resized with Lanczos without cropping or altering composition |

The source was untagged, so the conversion **assumes original RGB
represents sRGB**; this is not retrospective proof of generator colorimetry.
The normalized PNG was visually opened and inspected for both full-body
figures, intact hoods and nails. Original and output checksums were
computed directly from local image bytes.

### MCP upload attempt and blocked handoff

The connected local workspace exposes `create_workspace_png` and a
chunked `begin_workspace_png_upload` /
`append_workspace_png_upload` /
`finish_workspace_png_upload` workflow. **All require image bytes supplied
as an explicit base64 string**, not a session container pathname,
generated-image file ID or `source_file_ref`.

- Target: `illustrations/references/Nash_Maggard_Side_v2_HoodUp_1024_sRGB.png`.
- Upload beginning accepted by MCP with `total_bytes=1412227`,
  `upload_id=9c4942994eee41efb0b3b55930d91f29`.
- The generated file's binary is available in the local container, but
  the current connected tool interface offers **no direct container-file /
  generated-file-ID to MCP base64 bridging operation**. Do not pretend
  the file was delivered merely because the upload was initialized.
- The empty upload session was **explicitly aborted**, and the MCP server
  confirmed `PNG upload aborted`. **No PNG was written to the repository.**

**Current stage: owner-approved visual design, technically validated
session export, awaiting file registration. Not yet formally
`SIDE_APPROVED` in the repository.** Copy the verified derivative using a
supported file bridge or user-side upload to the exact workspace path,
read its full-file SHA-256 back via MCP and ensure the ICC/dimensions
match, then set `SIDE_APPROVED`. The old hood-down v1 remains
superseded for the intended baseline; do not overwrite other files.
The final multi-view character model sheet remains unapproved.

## Subsequent repository registration check — 2026-10-25

The previously missing corrected image is **now present** at
`illustrations/references/Nash_Maggard_Side_v2_HoodUp_1024_sRGB.png`.
A fresh MCP binary read confirmed **1,412,227 bytes**, SHA-256
`4a7bb1f07755a047f2ce430deb6d01e935db0b771b71d9a9fa1bb61a336337d5`,
**1024 × 1024**, 8-bit RGB PNG and an embedded `iCCP` chunk.
That is identical to the owner-accepted hood-up v2 export. **Record
`SIDE_APPROVED` for E000/A01**. The earlier unsuccessful upload attempt
above remains historical and was not retroactively successful.

The rear view was subsequently rendered and accepted by the owner; see
[back-anchor inspection and export](ILLUSTRATION_NASH_BACK_ANCHOR_2026-10-25.md).
Its registration is a separate step from this side-view approval.

