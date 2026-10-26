# Nash E000 character-design-sheet assembly — draft for final owner review

**Date:** 2026-10-25. **Subject ID:** `WASTES-NASH-MAGGARD`. **Sheet ID:** `WASTES-NASH-MAGGARD-DS-001`. **Appearance state:** `WASTES-NASH-MAGGARD-A01` (E000). **Current status:** `SHEET_LAYOUT_DRAFT / AWAITING_OWNER_REVIEW`. This records a completed **candidate layout**, not final owner approval or publication of a sheet.

## Exact reviewed source assets

All four reference files were already accepted by the owner and registered in `illustrations/references/`. Their local working copies were rehashed immediately before assembly and **all matched the previously recorded repository hashes**.

| View | Workspace reference | SHA-256 |
| --- | --- | --- |
| Face | `illustrations/references/wastes_nash-maggard_e001_sheet-02-face_v01.png` | `93e82eff061afd08611d0e6cf4fe8dfd11058ed94985c8c10a9d42140947cb71` |
| Front | `illustrations/references/wastes_nash-maggard_e001_front_v01.png` | `cc60727f08492be9bf54c43da5c6de9694fbd1c89f95840521396f033ecf58d0` |
| Side (two hood-up profiles) | `illustrations/references/Nash_Maggard_Side_v2_HoodUp_1024_sRGB.png` | `4a7bb1f07755a047f2ce430deb6d01e935db0b771b71d9a9fa1bb61a336337d5` |
| Back | `illustrations/references/Nash_Maggard_Back_v1_1024_sRGB.png` | `9f348f34ac86dd79f33cd9c59342b04c6d2267a99d908c8eea528b11c99f95d1` |

All source PNGs were programmatically inspected and contain an embedded ICC profile; each is an 8-bit RGB 1024 × 1024 image. Approval is restricted to the visual state established in Nash's [written reference](../project/ILLUSTRATION_NASH_MAGGARD_REFERENCE.md). Nash's left red/sightless eye, bald scarred head, rusty raised hood, covering bandages, flat clothed crotch silhouette, satchel and **Freedom as an ordinary old nail pierced crosswise through the staff's top** must remain consistent. These source choices include artistic reconstructions; the composition itself is not new transcript evidence.

## Draft produced in this session

| Page | Session-only output path | SHA-256 | Checked properties |
| --- | --- | --- | --- |
| 1 — full-body turnaround | `/mnt/data/Nash_Maggard_E000_Sheet_01_Turnaround_1024_sRGB.png` | `3e7c0383d5222d54327927bcac967a9d9d54d6582003354d4312e33de325209b` | 1024 × 1024, RGB PNG, embedded sRGB ICC; **814,363 bytes** |
| 2 — facial studies | `/mnt/data/Nash_Maggard_E000_Sheet_02_Face_1024_sRGB.png` | `93e82eff061afd08611d0e6cf4fe8dfd11058ed94985c8c10a9d42140947cb71` | 1024 × 1024, RGB PNG, embedded sRGB ICC; **1,866,988 bytes**; **byte-for-byte copy of approved face anchor** |

Companion, non-image artifacts (session-only): `/mnt/data/Nash_Maggard_E000_Sheet_Manifest.json` and `/mnt/data/Nash_Maggard_E000_Character_Design_Sheet_Draft.zip` (both PNGs plus manifest). The ZIP was tested for entry integrity. Exact creator source hashes and selected output hashes are preserved in the JSON manifest.

**Page 1:** Four full-body panels, **front top-left, back top-right, left-facing side bottom-left and right-facing side bottom-right**. All four derive from the existing accepted anchor pixels. The front and back are not mirrored; the side panels were clipped from the accepted two-profile original without swapping identity sides. Their figures were proportionally reduced to **477 pixels in height** (source canvas basis) so no staff, hood, cape, boots, nail or satchel is cropped. No character elements were re-generated or newly painted. A neutral, subtly shaded studio background holds all figures on one page. Non-subject original studio backdrops were replaced with a deterministic matte: **OpenCV GrabCut** foreground masks seeded by existing artwork colors, alpha edges feathered, and source crops resized with Lanczos. Manual removal of one unrelated grey-background mask false positive at upper-left of the right-side source crop; no artwork feature was removed. No text, invented gear, logos or numeric/stat labels.

**Page 2:** The previously approved complete multi-part face reference copied **unchanged and without recompression**; maintaining its full-size facial and eye details is preferable to shrinking it to fit the four-body layout.

**Actual checks:** Every output PNG was opened, verified as **1024 × 1024 RGB** with a nonempty embedded ICC profile, and passed PIL structural decode checks. Page 1 was visually viewed at full output size after the final matte revision to confirm that **no visible square crop backgrounds, clipped limbs/staffs, flipped views, overpainting or labels** remain. Page 2 has exactly the same SHA-256 as the original approved face reference. The matte process is a **layout/compositing operation**, not an assertion that source graphics contain true transparent layers. The rendering source script `/mnt/data/assemble_nash_sheet.py` is currently a **session-only working script**, not an installed reusable character-sheet skill or committed repository tool.

## Approval and repository gates

- **Current approval:** `FACE_APPROVED`, `FRONT_APPROVED`, `SIDE_APPROVED`, `BACK_APPROVED` remain valid for their exact registered source assets. **Combined sheet page 1 has not yet been accepted** by the owner. Page 2 is a byte-identical approved face reference, but selection as part of the **complete two-page sheet** still awaits final confirmation.
- **Current file locations:** these two combined-sheet **outputs exist in the session container**, **not confirmed as files in the repository**. Do not turn session paths into `illustrations/` claims until the exact files are placed in the project workspace and read back via the binary reader.
- **Suggested eventual workspace filenames (not created there):** `illustrations/references/Nash_Maggard_E000_Sheet_01_Turnaround_1024_sRGB.png` and `illustrations/references/wastes_nash-maggard_e001_sheet-02-face_v01.png`.
- **To finalize:** (1) owner reviews the actual page 1 layout and page 2 as a pair, recording approval or actionable corrections; (2) copy/register the exact approved candidate PNGs (or a new version with fresh hashes) into the repository; (3) binary-read each repository output and verify SHA-256, dimensions and ICC; (4) update the sheet ledger to `OWNER_APPROVED` for this precise E000/A01 2-page version and scope. Preserve the existing individual anchors and superseded attempts unchanged.
- **Editorial gate remains independent:** use transcript-backed state variants for later appearances and do not treat a design-sheet composition as a canon verification event. Any new inconsistency triggers the existing `IRV-` review process rather than silent replacement.

**No full sheet was declared approved or published as part of this assembly pass.**
