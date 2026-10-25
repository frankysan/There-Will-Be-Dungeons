# Nash Maggard design-sheet draft attempts — 2026-10-25

**Subject:** `WASTES-NASH-MAGGARD`. **Sheet ID:** `WASTES-NASH-MAGGARD-DS-001`.
**Target:** baseline `WASTES-NASH-MAGGARD-A01`, E000 introduction only.
**Outcome:** **No valid PNG delivered to the repository; no approved character
design sheet.** Preserve these two noncompliant outputs as rejected studies
outside the project illustration catalog; never cite them as approved visual
references. The source-linked [written specification](../project/ILLUSTRATION_NASH_MAGGARD_REFERENCE.md#e000a01-character-design-sheet-brief--draft-v01-2026-10-25)
was integrated separately, before generation.

## Input evidence actually reviewed

- E000 processed subtitle lines 285–479 (scene approximately
  00:03:49–00:06:47) directly read; source **not audio-verified**.
  E000 establishes facial scars, tumors, pitted/cratered skin, **two
  different eyes** (one seeing, one sightless/dormant and burning),
  one worn boot, **a staff** and threadbare shoulder satchel.
- Read actual pixels of Scott Johnson's player-created
  `local/images-wiki/scott-johnson-art/Nash_-_Scott_Johnson.webp`
  (SHA-256 `107993f8f6eb5fefceb2a7fabe91530b00c4cb24b72c2fe4d8a7a74a926fd3dc`)
  and `Scott_Johnson-Nash_Maggard.webp`
  (SHA-256 `a5adb03a7a935eb18664e8d6c9d4a8d074c6388e19189b715b6db4eafee22cad`).
  These show a hood/cape, broad boots, staff with hooked/pick tip,
  layered outfit and an intentionally obscured face. They are undated
  player-created **design-intent references**, not E000 costume evidence.
- [Illustration guide v0.5](../project/ILLUSTRATION_GUIDE.md) and the
  [character-sheet protocol](../project/ILLUSTRATION_CHARACTER_DESIGN_SHEETS.md).
  No source-art image was positively confirmed as an actual
  image-conditioning input to the generator. It was inspected in the
  research interface, but should not be recorded as a guaranteed
  reference image supplied to rendering.

## Rejected outputs (not repository assets)

| Attempt | Generation ID / local chat-session file | Actual technical check | Visual/source compliance |
| --- | --- | --- | --- |
| 1 | `aba81b5b-b8d2-4c98-8ab3-edd421a8aed3`; `/mnt/data/a_detailed_character_design_sheet_illustration_on.png`; SHA-256 `f866a5a178016bfdd04f9562c5b3e772cf8b465ab8b23c01af770d9d6cb9a519` | **1536 × 1024**, RGB PNG, no embedded ICC profile; square-size **FAIL**, sRGB **UNVERIFIED** | Conventional brown-haired ranger, bow/quiver, sword, many invented equipment/biography details and plentiful text. No distinctive Nash lesions/two-eye contrast, staff or Scott-inspired hooded identity. **FAIL** |
| 2 | `1a84d554-b1d7-4fa6-b548-c3bad198483f`; `/mnt/data/a_detailed_character_design_sheet_illustration_ed.png`; SHA-256 `dae5f90647eb0ae2314d59394c2084b79f560c2029078b15cbd829780b7d4266` | **1536 × 1024**, RGB PNG, no embedded ICC profile; square-size **FAIL**, sRGB **UNVERIFIED** | Conventional swordsman/fighter with blue cloak, sword, shield, and invented side items, printed text, and generic nearly unscarred face. It does not depict E000 Nash. **FAIL** |

Both attempts were visually inspected. Their generation metadata recorded
no usable actual prompt text (empty `prompt` field). Therefore compliance
with the **verbatim fixed style block** cannot be established and **must not
be marked PASS**. The generated pages also violate the no-incidental-text
rule. Neither output was cropped/resized to disguise the issue, uploaded to
`illustrations/`, chosen for a `world/` page, approved, or designated a
candidate production model sheet.

## Target visual brief for the next controlled rendering

A **single 1024 × 1024-square, sRGB PNG** with a neutral uncluttered
background and **matched front, side and back full-body views** of one
visually consistent adult human man. E000 Nash is scarred, pitted and
tumor-marked, with the same clearly recognizable facial proportions in
every view; two eyes, one apparently sighted and one sightless/dormant
(without post-E089 supernatural bright red styling). He carries a worn
walking staff and a threadbare shoulder satchel and wears visibly worn
boots. Use Scott's rust-brown deep hood and cape, grey layered costume,
olive/sand cloth, broad brown boots and restrained orange accents only
as **D01–D05 provisional artistic choices** in the written reference:
the hood casts a shadow but does not erase the damaged face, especially
in an enlarged face inset. Staff tip may subtly suggest Scott's hooked
sketch, **not** the later white bird ornament. No bow, arrows, sword,
shield, heroic knight armor, giant backpack, wolf insignia, unrelated
pendant, extra arm, dragon form or terminal gear. No added titles, labels,
logos, notes, frames or watermark **inside the image**; maintain written
labels and source evidence in the companion Markdown document.

**Mandatory unmodified style lock for the actual renderer prompt:**

> A single 1024 x 1024 pixel square illustration, rendered in the same
> cohesive graphic-novel / comic-book style used across the There Will Be
> Dungeons illustration collection: bold, confident dark-ink outer contours
> with deliberate variation in line weight; finer expressive interior
> linework; slightly cartoon-stylized but physically recognizable forms;
> readable silhouettes and purposeful negative space; broad matte muted
> pastel color areas, restrained neutrals, clear simple cel-shaded shadow
> shapes and only sparse intentional ink hatching or print-like texture.
> Detail is focused on identity-defining anatomy, objects and story features,
> not incidental visual noise. Use at most one main and one supporting vivid
> accent color across the **entire image**, except where source-established
> colors require otherwise. Preserve source-specified colors exactly rather
> than recoloring them to fit the palette. No added captions, speech bubbles,
> lettering, decorative borders, logos, signatures or watermarks unless the
> requested scene explicitly requires an in-world marking.

This is a **planned brief**, not an assertion that this block was used
verbatim in the two rejected render requests. Before retrying, verify the
actual renderer has accepted the entire prompt and the desired canvas
options. If this cannot be assured, do not promote its output as a project
illustration. If a rendered output is nonsquare, off-style, invented, or
fails face/eye/equipment fidelity, quarantine it and keep the sheet
unapproved.

## State and next step

- Written E000/A01 baseline: integrated and **provisional**.
- Sheet `WASTES-NASH-MAGGARD-DS-001`: **drafting**, technically and
  narratively noncompliant attempts rejected, **no asset in project**.
- **No owner-approved image**; recurring-character scenes featuring
  Nash remain blocked at the *design approval* gate (not necessarily
  the source-research gate).
- Next controlled task: generate a faithful, validated, correctly sized
  model sheet using a renderer capable of explicit prompt, verified
  square output and actual Scott reference image-conditioning; request
  owner acceptance only after all pre-/post-render checks pass.
