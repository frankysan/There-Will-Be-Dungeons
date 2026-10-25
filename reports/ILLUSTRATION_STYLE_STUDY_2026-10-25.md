# Illustration style study — Fate 4

**Date:** 2026-10-25. **Study:** WASTES-FATE4-STYLE-001.
**Status:** Two generated previews, visually reviewed by the assistant;
second rendering is the closer style candidate, with no owner acceptance
or production-reference selection implied.

[Style guide](../project/ILLUSTRATION_GUIDE.md) ·
[Subject record](../project/ILLUSTRATION_REFERENCES.md#wastes-fate-4) ·
[Follow-up tasks](../project/BACKLOG.md#illustration-style-and-continuity-2026-10-25)

## Purpose and evidence boundary

Test heavy comic-book / graphic-novel line art, slight cartoon stylization,
muted pastel color and selective bright accents in a neutral exterior
vehicle illustration. This is not a literal scene, a technical drawing,
or a definitive Fate 4 appearance.

Both passes use guide version **0.1** and subject-record version **0.1**
as their written starting point. The supported broad form is the existing
dossier's modified RV on monster-truck wheels. No original audio or SRT
was reviewed for this trial, and the source design images remained
inaccessible through the connector. They were not supplied to imagegen.

The original sources and their outstanding era/version questions remain
as recorded in the subject register. Generated details do not settle them.

## Outputs and execution

| Pass | Output identifier returned by imagegen | Input | Status |
| --- | --- | --- | --- |
| 001-A | `exec-40e97d90-e604-4591-8055-751734679f00.png` | Exact text prompt below; no input image | Initial preview, retained for comparison. |
| 001-B | `exec-78722942-caa5-48a0-9fb4-7a6c06dbb0f1.png` | 001-A as the sole edit reference; exact edit prompt below | Revised preview; assistant's closer style candidate. |

**Tool:** Built-in `image_gen.imagegen`, not CLI/API fallback.
**Settings:** `transparent_background=false` in both calls.
The second call used `referenced_image_paths` for the local 001-A output;
no original show/fan artwork was used as an image input.
Both returned PNGs are **1536 × 1024, RGB**, checked by reading their
image metadata and verifying file integrity. The tool did not expose
a seed, exact model identifier or additional quality settings.

These output identifiers refer to the previews displayed in the ChatGPT
conversation. They are not relative repository asset paths, and no binary
image was imported into this repository as a selected production asset.

## Provisional design choices

| ID | Choice introduced for this study | Evidence boundary |
| --- | --- | --- |
| D01 | A boxy cab-over RV body, simple side door/windows, two axles and four tires. | Broad RV/monster-wheel concept comes from the written evidence; exact body, layout and wheel count are study choices. |
| D02 | Warm ivory and dusty sage body, blue-gray windows, charcoal running gear, coral-red stripe/details. | Palette exploration only; not established Fate 4 paint colors. Small amber vehicle lamps appear in both outputs as another localized bright hue. |
| D03 | Plain off-white paper and a small dusty ground patch in a front three-quarter view. | Neutral presentation, not a claim about the unveiling's exact setting or camera view. |
| D04 | Light wear, exposed lifted suspension and simplified mechanical construction. | Visual interpretation of a modified vehicle; not a technical specification or evidence of a particular repair or damage event. |
| D05 | Generated roof fittings and rails, a rolled awning, mirrors, vents and bumper details. | Incidental generated interpretation, not sourced inventory or accepted accessories. Do not backfill these into episode documentation. |

The editing instruction preserves the trial's vehicle interpretation to
isolate the rendering change. That preservation does not endorse its
incidental features as canon.

## Assistant visual review

**001-A:** Recognizable RV identity and oversized wheel silhouette; muted
ivory/sage base with coral emphasis. Dense suspension, tire detailing,
fine scratches and nuanced shading pull it toward detailed vehicle
concept art rather than the intended simpler graphic-novel treatment.

**001-B:** Much stronger contour weight, broader color areas, cleaner
tire shapes and fewer scratches. These changes better match the requested
heavy-line, slightly cartoony direction. The same overall vehicle
interpretation and palette remain recognizable.

**Limits:** The image still contains considerable suspension detail and
uses earthy sage/ivory more than a broad pastel palette. Small amber lamps
introduce a second localized accent alongside coral; the requested single
accent hue was therefore not perfectly followed, although two accent hues
fit the owner's overall direction. This one vehicle study does not test
faces, expressions, creature anatomy or complex environments.

No further automatic iteration was made: the second preview is a concrete
candidate for the owner's style feedback. Neither rendering is an
owner-approved house style, canonical vehicle design or selected
continuity reference.

## Exact first-pass prompt

```text
Use case: illustration-story.
Asset type: preview-only visual style study, one standalone landscape illustration, approximately 3:2.
Primary request: Establish a comic-book / graphic-novel illustration style with heavy expressive ink, slight cartoon stylization, muted pastel colors, and one bright accent hue. Make this read as a hand-drawn ink-and-color illustration, with a strong recognizable silhouette.
Subject: A heavily modified recreational vehicle on monster-truck wheels, based only on a broad written description. For this provisional concept, use a long boxy RV body with a cab, simple side windows and a side door, lifted high on two axles and four enormous deep-tread tires. It must remain clearly an RV rather than an armored truck. The precise body model, paint and engineering details are creative choices for this study.
Composition/framing: A front three-quarter exterior view showing the full vehicle, enough margin around it, a clear view of the raised chassis and oversized wheels. No people. A very simple warm off-white paper backdrop with a small patch of pale dusty ground and a grounded cast shadow; no identifiable story location.
Style/medium: Bold near-black outer contours, varied line weight, thinner selective interior lines, solid ink shadow shapes, flat muted color areas and two or three clear cel-shaded values. Slightly exaggerated wheel proportions and lively confident drawing, but not a miniature toy or chibi design. Restrained hatching and subtle print texture; clean readable shapes at thumbnail scale.
Color palette: Warm ivory and dusty sage body panels, muted blue-gray windows and metal, charcoal tires and shadows. One saturated coral-red accent as a narrow horizontal body stripe and a small matching detail. Use this single bright hue sparingly across the entire image. These colors are provisional art direction, not established character or vehicle lore.
Lighting/mood: Soft directional daylight, readable materials, an adventurous and resourceful feeling. Only light everyday surface wear; no battle damage.
Constraints: No guns, turrets, rockets, skulls, fantasy ornaments, magical glow, extra vehicles, elaborate scenery, diagrams, inset views, panels, labels, lettering, logos, signatures or watermarks. Do not render photorealistically, as a 3D model, or with airbrushed painterly gradients. No visible text.
```

## Exact edit prompt

```text
Use case: style-transfer.
Edit the previous RV style-study illustration. Change the rendering style only; preserve the same vehicle interpretation, its long RV silhouette, cab-over body, two axles and four large tires, window and door arrangement, camera angle, overall framing, plain paper background, ivory and sage body colors, blue-gray windows and coral-red stripe. Do not add or remove vehicle accessories or introduce people, lettering or story scenery.
Make it clearly a slightly cartoony graphic-novel drawing: substantially bolder black exterior contours, strong varied ink line weight, simpler interior lines and much broader flat shapes. Reduce small mechanical and surface detail by about half, especially tire tread, suspension, grilles and body scratches, while keeping the main structural forms readable. Use flat muted pastel fills and a few deliberate solid shadow shapes rather than many finely modeled values. Keep the restrained coral-red accent and the existing limited palette. Reduce grungy weathering to a few purposeful ink marks. The result should be expressive, confident and easily readable at small size, not photorealistic, a 3D render, a miniature toy or a highly detailed technical illustration. No text, labels, panels, logos, signatures or watermarks.
```

## Next work

Retain the source-image inspection and era/version checks as open tasks.
Use feedback on 001-B to refine line weight, stylization, palette and
detail density. A later character study should test expression and
proportion once a bounded, sourced appearance reference exists.

If a preview is selected for production, record that selection and
its applicable appearance state, export it to the intended project
asset location, and link the real saved file. The current preview
does not silently become the recurring vehicle's model sheet.
