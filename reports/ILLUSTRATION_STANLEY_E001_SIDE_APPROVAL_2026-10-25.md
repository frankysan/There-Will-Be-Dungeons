# Stanley Billings — E001 paired side-profile visual approval (2026-10-25)

**Campaign:** The Wastes. **Character:** `WASTES-STANLEY-BILLINGS`. **State:** `WASTES-STANLEY-BILLINGS-A01` (E001). **Design-sheet ID:** `WASTES-STANLEY-BILLINGS-DS-001`.

**Status:** `SIDE_VISUAL_ACCEPTED / SIDE_REGISTRATION_PENDING` for **both** anatomical side profiles, as a **single explicitly owner-approved paired image**. Existing `FACE_APPROVED` and `FRONT_APPROVED` remain valid. `SIDE_APPROVED` is **not yet reached**: source and derivatives must still be placed in `illustrations/references/` and byte/hash/profile checked through the repository. `BACK_DRAFTING` and final-sheet `OWNER_APPROVED` have **not** started.

## Context and explicit owner decision

After S01–S07 off-model or unverified editing attempts (see [side attempt history](ILLUSTRATION_STANLEY_E001_SIDE_ATTEMPTS_2026-10-25.md)), the owner switched to **directly attaching the approved front PNG in a separate image-edit request**. The owner then supplied the resulting *two-profile image* in this conversation and specifically confirmed **“Yes, approved.”** This is approval of the **visible two-panel image**, not a retroactive approval of rejected S01–S07 or an assertion that the image generator's internal source reference, prompt and edit lineage are technically available to inspect. **Input-conditioned renderer provenance remains unverified; source material and owner approval of the outcome are explicit.**

The owner-requested orientations and approved composition are:
- **Left panel:** Stanley's **anatomical left** side, facing **viewer's right (→)**, with the **left-hip fully sheathed rapier** conspicuous.
- **Right panel:** Stanley's **anatomical right** side, facing **viewer's left (←)**, with rapier partially occluded by his body/coat as expected for a sword physically attached to his left hip.
- The two figures maintain comparable scale and complete hair-to-boots framing on a neutral background. Their silhouettes, brown hair/pointed ears, curled moustache and goatee, practical weathered brown coat, **plain muted olive/dark-umber vest**, off-white shirt, dark trousers, brown belt and tall buckled boots are visibly consistent with the approved E001 front. Bare hands and a single sheathed weapon are retained. The figures retain mild stylistic perspective in the boots but owner approved the visual result. This is an **owner-selected artistic design convention**, not a newly discovered podcast description.

## Submitted original, not technically normalized

- **Uploaded user image:** `Elven Rapier Duelist Turnaround(1).png` (this is the accepted owner-provided image in the chat, **not yet a repository reference**).
- Independently opened locally through Pillow: **1254 × 1254 RGBA PNG**, **2,558,033 bytes**; SHA-256 **`e5097b02cddd4dbc00239c261b53e785733dc9eee95dc7bc68d3d680845869b5`**.
- Entire alpha channel is opaque (255). **No embedded ICC profile**. For subsequent sRGB tagging the source is treated as **assumed sRGB**, not proven sRGB. Preserve this original PNG separately if archiving raw owner-approved art.

## Prepared normalized production exports — current chat session, NOT yet in repository

The approved image was proportionally LANCZOS-resized from 1254² to 1024² without cropping either figure and embedded a **588-byte Pillow/ImageCms sRGB ICC profile**. For individually usable full-body side anchors, the exact original left/right pixel halves were additionally cut at the **1254-pixel midpoint**, resized to **490 × 980 without stretching or mirroring**, and centered on 1024² with only the neutral image-edge background extended around them. These are **deterministic crops/reformats** of the approved paired source, not separate generative redrawing; only the paired arrangement itself received explicit user visual approval in this turn. Both derived images have been opened/visually inspected; no clipping of the face, feet, coat or rapier visible.

| Intended repo path (pending upload) | Content and technical verification | SHA-256 of exact prepared export |
| --- | --- | --- |
| `illustrations/references/Stanley_Billings_E001_Both_Sides_v1_1024_sRGB.png` | Owner-approved pair, RGB 1024×1024, sRGB ICC 588 bytes, **1,130,779 bytes** | `1163cc16f5ed34f1b2d7a8016330a5253cd03f2fbef7bd2037d490effc626b9a` |
| `illustrations/references/Stanley_Billings_E001_Left_Side_v1_1024_sRGB.png` | Anatomical left / facing right, RGB 1024×1024, sRGB ICC 588 bytes, **574,210 bytes** | `c685ace99abf4e51fbae4b77d887dab8de8a9835d51e4f64de95c679f57c14eb` |
| `illustrations/references/Stanley_Billings_E001_Right_Side_v1_1024_sRGB.png` | Anatomical right / facing left, RGB 1024×1024, sRGB ICC 588 bytes, **548,196 bytes** | `09f65c7e94b15c4e671093ebc00f3f5325341399a94760fb0a84f58552c2b4fe` |

**Caution:** The accepted pair is the primary visual approval; the two individual square extractions retain its artwork, and their registration as individual side anchors is conditional on readback and normal review. Do not say that the side assets are already in the repository merely because download links exist in this chat.

## Next stage / exact registration gate

1. Owner places all three exports in `illustrations/references/`, preserving the filenames above and the previously approved E001 front/face.
2. Verify each repo file's byte count, SHA-256, PNG IHDR and actual sRGB ICC profile through the connected workspace reader. If all match, record the **paired** side approval as `SIDE_APPROVED`, and register both individual side pixel-derivatives as accompanying left/right anchors, provided no new layout artifacts are found.
3. Proceed on a **separate explicit stage invocation** to a **single complete orthographic rear view** using the exact approved front/side references, unchanged brown coat/vest/collar/cuff/boots and actual physical left-hip rapier placement. Do **not** simply mirror a profile or accidentally change the sword's hip, and do not mark `BACK_APPROVED` without separate owner approval and repository verification.
4. The final assembled sheet remains pending independent review and registration.

**Checks:** Supplied original file metadata and checksum PASS. All three converted session exports PNG/1024-square/sRGB ICC/byte-count/checksum PASS. Paired and individual views opened/visually reviewed PASS. Repository readback NOT RUN (images not uploaded yet). TWBD lint/tests NOT RUN (repository-only text documentation change; no relevant test runner available). No source facts changed; no other subject images modified.
