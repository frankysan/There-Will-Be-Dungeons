# Illustration style and continuity guide

**Version:** 0.6, 2026-10-25. **Scope:** Characters, creatures, places, vehicles,
items, events and other illustrated subjects across The Wastes, Inverse and
Delvers. Shared art direction does not imply shared fictional continuity.

**Owner's initial direction:** Comic-book / graphic-novel illustration, heavy
line art, slight cartoon stylization, muted pastel colors, and one or two bright
accent colors per illustration. Respect the show's descriptions and maintain
written, time-specific instructions for recurring subjects.

The core direction above is owner-supplied. **On 2026-10-25 the owner selected
a stronger modern adult-animation / stylized graphic-novel direction** after
viewing the [latest Nash face study](../reports/ILLUSTRATION_NASH_FACE_DIRECTION_2026-10-25.md).
This confirms a **project-wide rendering direction**, not approval of a
specific production PNG, Nash's final face anchor or a complete model sheet.
Earlier vehicle studies remain unapproved trials. The same recognizable
ink, matte color and simplification principles must work for all subjects
without copying Nash's anatomy, disfigurement or personal palette.

[Subject template](ILLUSTRATION_SUBJECT_TEMPLATE.md) ·
[Recurring-character design sheets](ILLUSTRATION_CHARACTER_DESIGN_SHEETS.md) ·
[Canonical phased design-sheet workflow](../.agents/skills/twbd-illustration-generate/CHARACTER_SHEET.md) ·
[Appearance references](ILLUSTRATION_REFERENCES.md) ·
[Illustration research queue](ILLUSTRATION_RESEARCH_QUEUE.md) ·
[Illustration revision queue](ILLUSTRATION_REVISION_QUEUE.md) ·
[Editorial standards](EDITORIAL_GUIDE.md) · [Image provenance](IMAGE_ASSETS.md)

## Visual language

| Element | Working instruction |
| --- | --- |
| Ink | **Bold, smooth, confident dark-ink contours** with pronounced line-weight hierarchy, selective finer facial/structural marks and readable strong silhouettes; avoid uniformly scratchy micro-detail. |
| Stylization | **Modern adult-animation-inspired graphic-novel stylization:** expressive, slightly exaggerated yet recognizable features; deliberately simplified graphic planes and shapes instead of painterly realism. Adult dramatic seriousness, not childish caricature or rubbery anatomy. Respect sourced age, size, anatomy, disfigurement and uniqueness. |
| Color | Use muted pastel base colors and restrained neutrals, with one or two saturated accent hues across the whole illustration. Bright accents remain selective. |
| Shadows | Favor a few broad, clean **cel-shaded graphic shadow masses** with simple highlights; dramatic shadow remains possible but may not obscure essential identification or sourced abnormalities. Avoid photographic skin shading or muddy render effects. |
| Texture | **Sparse, controlled texture** and limited ink hatching only where identity or materials benefit; render burn scarring, worn cloth, wood, metal and weather with *designed shapes* first, not photographic pores, procedural grit or intricate random noise. |
| Detail | Prioritize **shape readability and characterful defining features** over realism. Use intentional silhouette and a few distinctive detail clusters; simplify the rest. Severe wounds or disfigurement can be visibly substantial without photographic gore, fresh tissue detail or gratuitous realism. Do not beautify or erase source-required damage. |
| Composition | Use a clear focal point, readable action and purposeful negative space. Portraits, object studies, environments and event scenes share the same ink and color treatment. |
| Tone | Maintain a distinctly **adult narrative tone**. Stylization permits dramatic, eerie, melancholy and funny scenes without turning tragic events or severe injury into slapstick, cuteness or sensationalized gore. |

**Reference calibration:** The last [Nash E000 face-direction study](../reports/ILLUSTRATION_NASH_FACE_DIRECTION_2026-10-25.md)
was positively received for *stylistic treatment*: broad clean
animation-like shapes, ink-heavy edges, controlled cel shading, dull
rust/grey fabric, expressive asymmetry and readable but non-photographic
old damage. Its burnt face, bandage placement, baldness and left red
sightless eye are **character-specific**, not a universal character
preset. Its actual session PNG was **1254 × 1254 with no embedded ICC**:
use it as **directional art feedback only**, not a technically compliant
or automatically approved reference asset. Avoid direct copying of
an identifiable television show's copyrighted character design;
"modern adult animation" describes broad craft, not a request to
imitate any specific studio.

Default to a standalone illustration. Panels, captions, speech balloons and
lettering are composition choices for a specific brief, not requirements of
the style. Avoid incidental lettering and watermarks in generation prompts.

## Fixed production canvas and style lock (v0.6 — art style recipe v2)

**All canonical newly generated illustrations, variants and multi-view model
sheets use exactly 1024 × 1024 pixels (1:1 square), exported as PNG in sRGB.**
This is a project production convention, not a historical property of the
existing two early Fate 4 previews or archived fan artwork. It applies to
characters, creatures, vehicles, places, artifacts and events alike. Adapt
composition **inside** the square, using purposeful negative space for tall
figures and broad vistas; never change aspect ratio for a subject type.
Previews, selected variants and edits must obey the same canvas before
entering the project illustration catalog.

The **shared style lock v2** combines the visual-language table above into
the same mandatory recipe for *every* generated image: modern
**adult-animation-influenced graphic-novel** shapes, bold variable dark-ink
outer contours, economical expressive interior marks, simplified yet
physically recognizable anatomy and solid silhouettes, broad matte muted
pastel/earth/neutral colors, purposeful negative space and deliberate
flat cel-shaded shadows. Use texture/hatching *sparingly* and only where
defining materials or identity; avoid photoreal modeling, hyper-detailed
skin, glossy digital painting or crowded visual micro-noise. For severe
injury or disfigurement, show source-required severity through clear
*stylized* scars and altered shape rather than gratuitous anatomical gore.
No incidental text, frames, logos or watermarks. Use **one main and at most
one supporting saturated accent across the entire image**, except where
show-established colors necessarily require more. Color, anatomy and
identity evidence always outrank this discretionary palette limit.

Keep this **v2** fixed style recipe and master dimensions **identical for every
production prompt**. The authoritative verbatim renderer block now lives in
[the generation skill, section 3B](../.agents/skills/twbd-illustration-generate/SKILL.md),
updated with this owner-selected direction. Do not reuse the retired v1
block from an older saved report. Subject-specific features, era, composition, setting,
lighting and chosen pastel/accent hues may vary, but not the underlying ink,
shape, shading or texture treatment. Use selected, versioned project-owned
references when available; earlier style trials are not owner-approved
anchors. An image that visibly drifts from the style lock is a draft needing
revision, not a selected reference. Image-model output may vary despite
identical instructions, so inspect and compare with the existing catalog.

**Research is a hard prerequisite, not a generation stage.** Before producing
*any* draft, check a campaign-qualified, time-specific, integrated appearance
record for **every** named or visually distinctive depicted subject. A missing
record, missing required state or material unresolved feature means **no image
is generated**. Log each blocker in the separate
[illustration research queue](ILLUSTRATION_RESEARCH_QUEUE.md), report it to
the requester and use the subject-research workflow first. Incidental
anonymous set dressing is not an entity unless it carries a specific lore
identity. If the queue cannot be saved, stop rather than silently proceeding.

For a completed image, verify its **actual pixel dimensions**, not only the
requested size. If a generator returns another ratio/size, safely adapt
within the same square canvas without cropping or stretching evidence-bearing
features, or withhold it as an invalid output. Preserve exact prompt,
style-guide version, subject IDs/state versions, references, output identity,
review status and any corrections in a production record.

## Established-character orthographic continuity (2026-10-25 clarification)

A selected front view is a **visual specification**, not a suggestion for a new character. For side/back turnarounds, require a reference-conditioned transformation of the **actual approved pixels** and keep the positive owner-approved outfit/identity lock. A text mention of a reference file or a verbal comparison does not prove the image renderer received the file. When the tool cannot verifiably accept the reference, **stop and switch to an explicitly controlled image-editing, artist-assisted or manual geometry/layout workflow** rather than repeatedly regenerating generic variants. Review outputs against the reference for exact garment color/cut, props, side-specific attachment, anatomy and sheathed-equipment construction.

Avoid feeding the generation model a long list of rejected accessories, textures or colors—even negative statements can surface those features in auto-composed prompts. Keep forbidden-feature names in a separate **validation** checklist and use short **positive renderer instructions** that describe only the intended existing design. Where the actual generation-request description is visible, check it against the approved reference before rendering; if it contains incompatible additions, the **prompt itself is wrong** and the run should not proceed. Once a specific fault recurs twice using the same rendering strategy, institute a method-change stop, not an unlimited retry cycle. The authoritative gates and stage statuses are in [the progressive character-sheet workflow](../.agents/skills/twbd-illustration-generate/CHARACTER_SHEET.md#1a-existing-anchor-turnaround-gate--no-text-only-character-reinvention).

## Palette and lighting

Select a small family of dusty rose, sage, pale blue, sand, lavender or similar
muted pastels as appropriate to the subject. Pair these with warm or cool
neutrals and dark ink. These are palette options, not mandatory colors for
every image. Exact swatches remain unselected until a visual trial.

Choose one main saturated accent and, when useful, one supporting accent.
Count accent hues across the complete composition, including lighting and
effects, rather than assigning two new accents to each subject.

**Described subject colors take priority over palette economy.** Preserve
recognizable skin, scales, hair, clothing, markings, materials and light
effects when the show establishes their color. Do not bleach or recolor them
to fit the palette, or turn an unspecified feature into a supposed canonical
color. If several required bright colors coexist, document the exception and
control emphasis through area, value, background and framing.

Record a subject's underlying colors separately from scene lighting. Reuse
them across images unless a sourced change or an explicitly recorded working
design revision explains the difference. A magical glow in one scene does
not establish permanent luminescence.

## Source fidelity and design choices

Use the [editorial source standards](EDITORIAL_GUIDE.md) and the
[existing image-reference policy](IMAGE_ASSETS.md). A polished drawing does
not make its contents established show lore.

For each appearance detail, record two independent things:

| Field | What to record |
| --- | --- |
| Evidence role | Played description, GM/cast clarification, character claim, creator design document, fan interpretation, inference, or artistic choice. |
| Verification | Exact source and version, approximate timestamp/cues where available, whether the passage was listened to, and any unresolved conflict. |

A GM statement read only in ASR remains transcription-provisional; its speaker
role does not make the wording audio-verified. Two agreeing ASR exports are
not two independent accounts of the fictional event.

- Preserve explicit descriptions over generic fantasy conventions, stock
  creature designs or assumptions based on a name or game statistic.
- Distinguish a character's claim, vision, disguise or hypothetical future
  from an objective view of the world. Label a subjective event illustration
  accordingly in its production record and caption when needed.
- Use dated creator designs within their supported scope. Fan art is an
  interpretation; campaign-end sheets and undated portraits do not establish
  introduction-time appearances.
- For entity research, check available **campaign-matched D&D Beyond sheet JSON**
  for character-specific names and leads to NPCs, places, items and other
  characters. The files are **final-campaign snapshots**: hair, eyes, age,
  equipment, spells, titles, custom notes and inventory do not establish
  when those details were first true, worn or known. Cross-reference actual
  played scenes before adding earlier appearance requirements; ignore
  generic embedded D&D rules text as in-world evidence. Preserve compact
  JSON-field provenance outside reader-facing world prose and respect
  the requested spoiler cutoff.
- Leave unspecified features open. When rendering requires a choice, record
  it as an artistic decision with its own status and revision history.
- Preserve conflicting descriptions. Seek the relevant passage or use a
  composition that leaves the disputed feature unresolved.
- A generated image may become a selected production reference; it never
  becomes evidence of what was said in the show.

## Appearance continuity

Give each subject a campaign-qualified identity and each distinct appearance
a stable state ID. Separate recurring physical features from costumes,
equipment, temporary conditions, transformations and scene-specific effects.

Record both **when the appearance applies in the story** and **when its
supporting detail was first described or learned**. Later revelation is not
automatically physical change. A flashback, retrospective Q&A or historical
prequel can describe an earlier state without changing release order.

Use precise scene boundaries when known; write "start unknown" or "end
unresearched" when they are not. Do not stretch an introduction-state record
across an entire arc merely because later appearances have not been reviewed.

Preserve earlier states when adding later ones. Record changes as explicit
deltas from a named baseline, with a usable complete description for the
selected state. Temporary forms, disguises and alternate versions must stay
distinguishable; a reversion does not create a new permanent feature.

Record left and right from the subject's perspective. Do not mirror scars,
missing limbs, heraldry, asymmetric equipment or a location's established
layout. Treat a current inventory as distinct from what is visibly worn or
carried in a particular scene.

## Apply the reference to different subjects

| Subject | Required visual continuity |
| --- | --- |
| Characters | Face, age/build, skin or scales, hair, anatomy, posture, markings, clothing, equipment and relevant visible changes. Use sourced behavioral traits for gesture without inventing hidden motives. |
| Creatures | Distinctive anatomy, proportions, movement, surface texture and markings; distinguish an individual from species-wide traits and transformed people from an unrelated species. |
| Places | Geography, skyline, landmarks, architecture, materials, relative scale, established spatial relationships, inhabited condition and changes over time. An evocative view is not an exact map of unspecified geography. |
| Items and vehicles | Shape, scale, construction, materials, markings, mechanisms, damage, repairs and upgrades. Track the object's appearance separately from custody and actual scene presence. |
| Events | Exact narrative moment, participants, their valid appearance states, location state, positions and visible effects. Do not combine incompatible moments or reveal later knowledge in an earlier scene. |
| Factions and other subjects | Record visible symbols, insignia and material culture only where supported. A member's design does not automatically establish a universal uniform. |

## Visual congruity with existing illustrations across story states

**Existing illustrations must be consulted for every recurring depicted
subject**, even when the written appearance record already passes the
research gate. Find the subject's complete production-image lineage in
the appearance register, dedicated reference pages, `illustrations/` assets
and linked `world/` illustrations. Inspect the **actual images** and their
recorded story-state IDs, scope, approval status and known fidelity errors.
Do not infer visual content from a filename, assume inaccessible images
have been examined or borrow a similarly named subject from another
campaign. Selected project depictions carry continuity weight as
**artistic references**, never as independent evidence of the show.

**Resolve the exact story moment first.** Choose a same-state selected
or owner-approved depiction when available; otherwise use nearby states
to preserve **permanent identity features only**, and apply the documented
state changes. An earlier outfit, intact roof, installed machine part or
healthy limb must not persist into a later scene after its alteration;
later scars, equipment, decorations, rebuilds and transformations must
not be backdated into an earlier one. Source-supported changes supersede
the design shown in older selected art. Preserve the earlier image and
flag the conflict for review rather than silently rewriting visual history.

Each new illustration brief must explicitly separate:

- **Carry forward:** stable face, body structure, subject scale, markings,
  construction, orientation and selected long-lived artistic choices
  (including unspecified base colors) supported for the targeted period.
- **Change:** source-supported damage, repair, age, clothing, carried
  objects, transformation and location changes, plus scene-specific
  weather, lighting, dust, mud or pose. Intrinsic colors should not drift
  simply because the illumination changes.
- **Exclude or revert:** details present only in a different era, costume,
  location, dream, flashback, temporary effect or superseded design.
- **Open:** conflicts and gaps; distinguish safe provisional choices from
  true missing research or inaccessible indispensable imagery. For a
  blocking gap, follow the dedicated research queue and **do not render**.

Treat locations as subjects with their own appearance states: a recurring
room can acquire damage, furniture, changed occupants and new lighting;
its established walls and openings cannot freely change position. In a
scene with multiple recognizable subjects, choose a **mutually compatible
set of temporal states** for characters, their gear, vehicles, objects and
the setting.

Pass relevant selected images as **actual image inputs** when the renderer
allows. Supply explicit instructions on which features to retain and which
target-state differences to apply. Otherwise describe and record the visual
comparison, state that the images were not passed to the renderer, and
do not pretend the output was directly image-conditioned. If a necessary
selected reference cannot be inspected and its distinguishing features
are not already documented, treat it as a continuity/access blocker,
rather than inventing a new design. Compare the output against all
relevant selected images **after** generation as a separate visual-lineage
review from show-source accuracy and shared style compliance.

**Working example — Fate 4:** The owner-selected E006 garage portrait
`WASTES-FATE4-ILL-001` represents completed Fate 4 `A01` and garage
`A03`. It may establish a recognizable *working artistic treatment*
for later views, but its exact paint and proportions are not canon.
The earlier E001 construction state `WASTES-FATE4-A00A` must not
automatically inherit completed skull-front and roof fittings. The
later E028 `A06` needs the raptor-hide roof patch. A change in exterior
sunlight alone does not justify repainting the same vehicle. Track
garage changes using its own state record rather than copying the
E006 background into every other scene.

## Illustration brief and record

Build each brief from the same components:

1. Campaign, subject IDs, exact scene or story interval, spoiler cutoff and
   objective versus subjective viewpoint.
2. This guide's version and the selected written appearance-state versions.
3. Full required appearance, scale and materials; explicit changes from
   baseline; relevant details that must remain absent at this point.
4. Composition, viewpoint, gesture, setting, lighting, pastel base palette
   and chosen accent hues.
5. Source references and image references, each labeled by role. Keep
   evidence notes outside the image-generation prompt when they would add
   confusing visual instructions.
6. Open details and the artistic decisions made to resolve them for this
   image. Save the exact generation/edit prompt and relevant tool metadata
   when actually available; do not invent a seed or hidden configuration.
7. Output identifier/path when available, draft or selected status, review
   notes and a link to any revision it replaces.

A reference image complements the written description. For image edits,
supply the appropriate selected reference alongside explicit instructions to
retain stable features. Do not rely on an earlier prompt or image remaining
in conversation memory.

### Mandatory recurring-character design sheet

**Before making any new scene, portrait or group illustration depicting a
recurring character (or one reasonably expected to recur across two or more
illustrations), first create and obtain explicit owner approval of a character
design sheet.** This includes identifiable recurring NPCs and companions;
anonymous set dressing and truly isolated one-off characters are exempt.
When a character later becomes recurring, halt *future* scene illustrations
until the sheet exists; do not retroactively invalidate older selected art.

Follow the [design-sheet specification and approval ledger](ILLUSTRATION_CHARACTER_DESIGN_SHEETS.md).
The **active operational workflow** is [the progressive character-sheet
procedure](../.agents/skills/twbd-illustration-generate/CHARACTER_SHEET.md),
installed as a companion inside `twbd-illustration-generate`. The [original
pilot plan](ILLUSTRATION_PROGRESSIVE_CHARACTER_SHEET_PLAN.md) is historical
rationale and detailed Nash test data, **not competing live instructions**.
Research creates the source-integrated, story-era written brief. Then,
subject to distinct owner and technical approval gates, generation proceeds
**one anchor at a time**: face close-up → front full figure → side/profile →
back full figure. Finally **assemble** approved *actual image pixels* into
one or two readable text-free **1024 × 1024 sRGB PNG** pages; do not make a
single new generation call to redraw all views. Retain text labels,
provenance, palette notes and uncertain choices in the **written companion**,
not on the image. Final sheet approval **must be separate** from each
individual anchor approval, and the exact PNGs must be hash-verified in the
project repository. A trial drawing, player artwork, a selected scene illustration,
or a generated unreviewed sheet is **not** an approved character model sheet.

An approved baseline records long-lived identity traits, not an immutable
outfit or final-campaign build. Significant story-time changes use documented
variants or an explicitly approved written delta tied to a stable state ID;
never backdate late gear, scars, transformations or terminal JSON details.
Source-supported corrections supersede artistic assumptions and require
review flags on affected older images. The sheet itself is a production
reference, not independent evidence of what happened in the show. **Missing
source research** goes in the `IRQ-` queue; **a missing/unapproved sheet after
research** is tracked in the sheet ledger and blocks scene generation until
approval. Creating a sheet draft remains permitted when its research is ready.

## Flagging existing illustrations when research or context changes

Both [illustration research](../.agents/skills/twbd-illustration-research/SKILL.md)
and [illustration generation](../.agents/skills/twbd-illustration-generate/SKILL.md)
must review **existing art affected by new visual evidence**, newly
clarified story-time/location context, or a discovered conflict with
earlier art. Inspect the actual image whenever possible and compare its
**depicted state** against the new finding. Include selected images,
drafts, archived trials and other scenes featuring the affected subject.
A discovery about an earlier appearance may require revisiting an older
image even when it was found in a later transcript. Changes due to time,
location, damage, repair, costume, lighting and camera angle are not
automatically errors.

Create or update a durable `IRV-####` entry in the separate
[illustration revision and consistency queue](ILLUSTRATION_REVISION_QUEUE.md).
Record image IDs/paths, selection/approval status, the relevant story
states, expected versus depicted feature, evidence and verification,
severity, suggested review/edit/regeneration and any owner decision.
Link the flag from the subject's production record. A report that only
mentions a possible problem without a persisted issue is **incomplete**.
A source-backed contradiction can supersede an artistic choice but
never licenses automatic replacement of owner-selected artwork.

Use [ILLUSTRATION_RESEARCH_QUEUE.md](ILLUSTRATION_RESEARCH_QUEUE.md)
for **missing source research blocking a new image** and the `IRV-`
queue for **existing art needing review/correction**. A single problem
may require both entries, but their closure is independent. Do not
regenerate every flagged image: use `review-only`, `annotate`, `edit`,
`regenerate` or `archive/no-reuse` based on actual visual impact.
Keep old versions and attribution; resolving a flag requires a
documented review or verified replacement and an appropriate decision.

## Review and maintenance

Before selecting an illustration, check fidelity to the evidence, correct
story state, recognizable identity, proportions/anatomy, left/right
consistency, required colors, scale, scene participants and spoiler limits.
Check the **style v2** ink hierarchy, simplified adult-animation-inspired
shapes, restrained matte palette, broad cel shading and limited accents as
a separate art-direction review. A scene may be dramatic, weathered or dark
without returning to photoreal textures or grotesque procedural detail.

Record the outcome honestly as draft, selected working reference, revised
or superseded. Use "owner-approved" only following actual owner approval;
routine drafting and reversible refinement can proceed without a new
permission step. **Exception:** recurring-character scene illustrations
require a separately owner-approved, applicable design sheet first;
creating the sheet draft does not itself require prior approval.

When subsequent episode research locates a visual description, add or
revise the subject's evidence and state record. Check earlier artistic
decisions against the new evidence and note which existing illustrations
need correction. Preserve prior records and images; do not silently replace
a design or rewrite source transcripts.

The production records live outside ordinary reader-facing world prose.
Link them from appropriate indexes or source footnotes without interrupting
the in-universe narrative or adding sections after Current status. Start
with the [shared appearance register](ILLUSTRATION_REFERENCES.md), keeping
campaigns visibly separate; split growing subject records into linked
files when warranted.

## Initial implementation and next work

The [reusable template](ILLUSTRATION_SUBJECT_TEMPLATE.md) and the
[active Fate 4 subject reference](ILLUSTRATION_FATE4_REFERENCE.md) establish
the written method. The original [v0.2 introduction pilot](ILLUSTRATION_FATE4_PILOT_0_2.md)
is preserved, and the [transcript audit](../reports/FATE_4_TRANSCRIPT_AUDIT_2026-10-25.md)
now supplies time-specific appearance changes through selected E066 scenes.
These are ASR-based findings, **not** audio or direct source-image verification.

The first [two-pass vehicle style study](../reports/ILLUSTRATION_STYLE_STUDY_2026-10-25.md)
has been generated and visually reviewed by the assistant. Its second pass
uses stronger contours, simpler mechanical detail and broader flat color
areas, bringing it closer to the requested direction. Neither pass is an
owner-approved style or a definitive Fate 4 design. The report preserves
both exact prompts, output identifiers and provisional appearance choices.

The original Fate 4 style previews lacked transcript-described solar
panels and the dragon-skull front, so they are **rendering studies only**,
not accurate selected continuity sheets. Next: directly inspect the source
images and their applicable era, resolve remaining scene-specific details,
and develop a revised multi-view Fate 4 study. **The Nash E000 face studies
have now provided the owner-preferred project-wide graphic direction**, as
recorded in [the bounded visual report](../reports/ILLUSTRATION_NASH_FACE_DIRECTION_2026-10-25.md).
Their head/face decisions and technical production compliance are still
unapproved. Extend the cleaner, slightly cartoony style equally to other
characters, creatures, vehicles, locations and items, respecting each
subject's material properties and episode-supported details.
Update [the backlog](BACKLOG.md#illustration-style-and-continuity-2026-10-25)
as those tasks are completed.
