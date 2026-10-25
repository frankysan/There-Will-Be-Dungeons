# Nash Maggard — iterative face direction and project-style pivot (2026-10-25)

**Subject:** `WASTES-NASH-MAGGARD`. **Sheet:** `WASTES-NASH-MAGGARD-DS-001`.
**State:** `WASTES-NASH-MAGGARD-A01` (E000 introduction).
**Review status:** **OWNER-PREFERRED VISUAL DIRECTION, NOT AN APPROVED FACE ANCHOR OR APPROVED COMPLETE SHEET.**
Source research/ASR verification remains as recorded in
[the Nash reference](../project/ILLUSTRATION_NASH_MAGGARD_REFERENCE.md).
This report records **what was actually generated**, user feedback and
independently inspected technical properties. It is not confirmation that
the generation tool used the exact intended prompt or reference pixels.

## Iteration evidence and decisions

| Sequence | Session-generated file / image generation ID | User review and what changed |
| --- | --- | --- |
| A. Initial hooded face | `scarred_hooded_wanderer.png`; `54606a49-a599-44d3-91e6-098c1252f68c` | User: 'not bad at all'; however long dark head hair and full beard made it read too much as a rugged, infected wanderer, not a substantially burned character. |
| B. Head-wrapping variant | `a_detailed_illustrated_concept_art_style_compilati.png`; `833b7adc-fdd1-4aa7-ac22-bc5a77fc95cb` | User requested bandages covering the head as well. Multiple faces and close-ups appeared, with hood and facial wraps; still substantial dark hair. |
| C. Hairless, stronger burns | `scarred_hooded_survivor_portrait.png`; `1660d2d7-99c9-4877-8bea-1dab0af3ecc7` | User asked for little/no hair and a face more like a severe-burn survivor; next requested more extensive damage. Kept too much smooth/healthy face and beard for the desired severity. |
| Blocked stronger-burn attempt | No delivered image file | The generation request was blocked; **no image exists** from this attempt. This is not a reason to invent a successful render or to disguise a nonconforming result as an approved asset. |
| D. Stylized adult-animation direction (preferred) | `a_detailed_comic_graphic_novel_style_character_she.png`; `ea839199-8236-43a3-bc39-e9d01e7fbee2` | User explicitly: **'Yes, that is a very good direction.'** Preferred blend of more cartoony/modern adult-animation shapes with bold ink, severe but non-graphic healed burn scarring, asymmetrical face, bald scalp, concealing wraps, rust hood and differentiated eyes. This approves the **design direction**, not the file as a production/scene anchor. |

The exact tool metadata `prompt` field for the generation records was
empty, so complete actual submitted prompt text and use of external
reference-image conditioning are **not verified**. Conversation-visible
briefs and older Scott Johnson art are **research references**; do not
claim their pixels were directly provided to the renderer. The preferred
study shows a large bust, smaller frontal/profile/hooded studies and
eye details. **That is a conceptual art study**, not evidence that a
finished multiview character sheet has passed the progressive anchor
workflow. A standalone face anchor and separately approved full-body
views are still needed.

## Exact files inspected in the current session

The following files were present at the session's `/mnt/data/` paths
and checked programmatically. These session paths are **not verified
repository paths or guaranteed persistent project image assets**.
All four had **1254 × 1254** RGB PNG pixels and **no embedded ICC profile**;
their actual square ratio passes, but the required **1024 × 1024 size
fails** and **sRGB profile is not verified**.

| Session filename | SHA-256 |
| --- | --- |
| `scarred_hooded_wanderer.png` | `0c7ad70191c15b6510cd6694048307d8d5c46329bafdf0df1eeeaba9c4cde858` |
| `a_detailed_illustrated_concept_art_style_compilati.png` | `e7717890368b1dc1b741a1ad91f773bede5436523a5d22b7fc7dfbc55d5b3ff4` |
| `scarred_hooded_survivor_portrait.png` | `fc57cd1c879ddcbbe9a1820f97d9478c5214b870dfa5df20341ea66230329bf5` |
| `a_detailed_comic_graphic_novel_style_character_she.png` | `8fbb2e8ce113826c89b85cc461af8f3ba3eaa41cbfc435462e4395b0efdc025b` |

No file was newly uploaded into the project `illustrations/` catalog,
selected as a reader-facing world image, technically normalized or marked
as an approved face anchor. If the chosen artwork is later imported,
preserve its exact original identity and record *new* converted-file hashes,
actual 1024-square dimensions, verified sRGB handling and explicit owner
acceptance of that particular version. Do not relabel the original as
compliant. Avoid silent cropping or inaccurate resizing.

## Visual findings to carry forward for Nash

- **Head and facial hair:** E000 visual design uses **a bald/almost
  hairless head**; avoid long hair framing the face. Sparse facial
  stubble is acceptable but a thick intact beard or a handsome healthy
  head of hair is not part of the preferred direction. The campaign-end
  JSON says `hair: "Gone"` but **does not time-stamp first hair loss** or
  specify hair or beard color. Therefore early baldness is an
  **owner-directed continuity interpretation**, not verified E000 dialogue.
- **Burn appearance:** Severe **old burn-like contracted scar masses,
  uneven healed skin planes, mottled/cratered texture and selected
  raised blister/pustule remnants**. More extensive damage than the
  earlier near-miss faces; use boldly outlined, flattened stylized
  shapes rather than close photoreal gore, fresh wounds, exposed tissue
  or proliferating orange decorative circles. The JSON terminal state
  says `skin: "Burned and disfigured."`; E000 already describes
  scars, pitting and tumors. Their exact source/chronology remains
  qualified in the written subject reference.
- **Eyes and asymmetry:** Red, damaged/sightless eye on **Nash's own
  LEFT** (viewer-right when front-facing), with subtler E000 treatment
  than later E089 glow. His RIGHT eye is sighted; no lateral mirroring.
  Do not confuse a visual red iris with a permanently intense laser glow.
- **Concealment:** Rough pale-grey fabric/bandages visibly wrap over
  the bald scalp, forehead and parts of the face, nose/cheeks and neck,
  intentionally masking damage without completely hiding the
  source-important eye and scars. Primary implied purpose is
  **concealment of disfigurement**, not armor or a clinical
  protective mask (owner interpretation).
- **Silhouette/palette:** Threadbare deep **rust/umber hood** over muted
  greys and dirty off-white wrappings, bold dark-ink outer contours,
  carefully simplified shapes, broad matte/cel-shaded planes, restrained
  texture; keep a serious, weathered expression. No generic heroic
  beard/hair, handsome ranger look or unrequested equipment.
- **Further phases:** Once a technically conforming and reviewed
  **face anchor** is accepted for progression, extend the same
  head/eye/wrapping language consistently to front, side and back
  figures. The full-figure staff has the **old nail “Freedom”** at its
  tip based on later E018 testimony, not a fantasy axe or E098 bird
  finial. No props are needed in face-only tests.

## Project-wide decision versus subject canon

The owner likes the **modern adult-animation / graphic-novel
stylization** achieved here: simplified readable forms, expressive
but not childish anatomy, heavy clean variable ink contours,
flat-matte muted pastel/earthy regions, selective cel-shadowing and
minimal microtexture. Apply **this level of stylization as the general
house direction**, adapting it to creatures, places, objects, vehicles
and events without making all subjects look like Nash or introducing
burned flesh where none exists. Keep the project's limited bright
accents and format rules. Preserve source fidelity and chronology
as constraints independent from style.

## Normalized candidate prepared — 2026-10-25

The original owner-preferred face artwork is preserved unchanged in the repository as
`illustrations/references/Nash_Maggard_Face_v1.png` (SHA-256
`8fbb2e8ce113826c89b85cc461af8f3ba3eaa41cbfc435462e4395b0efdc025b`).
A **separate session export**, `/mnt/data/Nash_Maggard_Face_v1_1024_sRGB.png`,
was generated directly from matching original bytes with aspect-preserving
Lanczos downsampling, **no cropping, mirroring, content retouching or added art**.
Verified output: **1024 × 1024, RGB PNG**, embedded **588-byte sRGB ICC
profile** (`sRGB built-in`), **1,866,988 bytes**, SHA-256
`93e82eff061afd08611d0e6cf4fe8dfd11058ed94985c8c10a9d42140947cb71`.
The resulting image was **visually inspected**, retaining all of the face,
red left eye, bandages, rust hood and small angle/eye reference views.
The original was untagged, so the sRGB export **assumes its RGB channel
values were intended as sRGB**; a tag cannot retroactively verify the
original source color space.

**Status: technically conforming export, not yet a repository asset or
`FACE_APPROVED`.** The exported session PNG must be placed in a new,
non-overwriting workspace path such as
`illustrations/references/Nash_Maggard_Face_v1_1024_sRGB.png`, and its
full-file SHA-256 reverified there; the original v1 PNG stays unmodified.
Owner's previous favorable response approved the artistic *direction*,
not necessarily this exact normalized file/version as the formal face
identity anchor. Request explicit acceptance once the copy is accessible.

## Face anchor approved and repository identity checked (2026-10-25)

After the normalization handoff, the user explicitly answered **“Yes, it's approved.”** for the proposed 1024-square E000 face anchor. A subsequent workspace read confirmed `illustrations/references/Nash_Maggard_Face_v1_1024_sRGB.png`, full-file SHA-256 `93e82eff061afd08611d0e6cf4fe8dfd11058ed94985c8c10a9d42140947cb71`, 1024 × 1024 PNG with embedded ICC. The hash matches the originally inspected derivative. **Record `FACE_APPROVED` for this exact E000/A01 reference.** The original untagged 1254-square `Nash_Maggard_Face_v1.png` remains a preserved source study. Neither the face approval nor the separate front approval approves the eventual complete sheet.

**Do not mistake 'good direction' for 'owner-approved model sheet'.**
Keep `WASTES-NASH-MAGGARD-DS-001` in `drafting` until an actual
technically conforming anchor and final sheet have separately cleared
their approval stages.
