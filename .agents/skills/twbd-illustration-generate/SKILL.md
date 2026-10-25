---
name: twbd-illustration-generate
description: Generate source-faithful, visually congruent illustrations for researched TWBD entities and specific story moments across separate campaigns. Before drawing, find and inspect existing illustrations of each subject, reuse stable visual identity while applying scene-time/state changes, and maintain the same 1024x1024 graphic-novel style. When a subject or required state is unresearched, do NOT generate—record the missing work in the dedicated illustration research queue and inform the requester.
---

# TWBD illustration generation — research-gated, style-locked

## Trigger and absolute invariants

Invoke for requests such as `$twbd-illustration-generate Wastes Fate 4 at E006`,
`$twbd-illustration-generate Delvers Koh Spiros at S1E10`, or
`$twbd-illustration-generate Wastes E066 scene: the tyrannosaur crushes Fate 4`.
This skill **produces visual art only for entities whose required appearances
have already been researched and integrated**. It does not research subjects
from scratch and must not fabricate their canonical look.

**Three non-negotiable contracts:**

1. **Identical output dimensions and style — an enforceable gate, not a
   preference:** **Every new render or edit attempt**, including previews,
   revisions, variants, multi-view sheets, location panoramas and proposed
   world-page images, must be directed to the same **1024 × 1024-pixel square
   (1:1), PNG, sRGB** output and must use the **verbatim fixed style block**
   from section 3B and the [current illustration guide](../../../project/ILLUSTRATION_GUIDE.md#fixed-production-canvas-and-style-lock-v03).
   Do not change aspect ratio by subject type, user wording such as 'aerial',
   'wide' or 'panoramic', tool defaults, or an existing image's proportions.
   If a renderer disregards the request, its result is **noncompliant**, not an
   approved exception. Follow the required pre-call and post-call gates below.
2. **No research, no image:** Before calling **any** image generator or
   creating/editing a draft, determine the complete set of important depicted
   subjects and verify usable **campaign-qualified, time-correct, integrated
   appearance references for all of them**. If **any** subject fails,
   **do not generate any part of the illustration**. Record all blockers in
   [ILLUSTRATION_RESEARCH_QUEUE.md](../../../project/ILLUSTRATION_RESEARCH_QUEUE.md)
   and tell the invoker. Research happens through the separate
   [subject-research skill](../twbd-illustration-research/SKILL.md).
   **No fallback to generic fantasy stereotypes, arbitrary character designs,
   a random fan portrait, or an unsupported generated mock-up.**

3. **Existing-image continuity is mandatory:** Find and inspect existing
   project illustrations of each subject before generation. Preserve stable
   identifying designs, and apply the researched time- and location-specific
   changes rather than copying another era's appearance. If an essential
   selected visual reference is inaccessible, stop and report the problem.
   An older image never overrules documented story evidence.

A requested image containing both a researched character and an
unresearched item, location, creature or companion **blocks the entire
composition**. Do not draw just the researched character unless the user
explicitly makes a new, smaller request and that new request passes its own
preflight. Queue write failures are also hard stops.

## 0. Identify the requested picture before doing anything visual

1. Resolve the **campaign/continuity**, depicted moment and spoiler cutoff,
   intended viewpoint (objective, subjective vision, retrospective account),
   desired type (portrait, exterior, interior, scene, map-like place, reference
   sheet), required visible entities, and any explicit details from the
   request. If exact season/episode is absent, use a supported bounded
   appearance only where unambiguous; never silently choose a later form.
2. Inspect current Git status and the relevant project file revision where
   available; preserve unrelated modifications. Read
   [style guide](../../../project/ILLUSTRATION_GUIDE.md),
   [appearance register](../../../project/ILLUSTRATION_REFERENCES.md),
   [subject template](../../../project/ILLUSTRATION_SUBJECT_TEMPLATE.md),
   [research queue](../../../project/ILLUSTRATION_RESEARCH_QUEUE.md),
   [existing-art revision queue](../../../project/ILLUSTRATION_REVISION_QUEUE.md),
   and applicable named subject records, source/image provenance and relevant
   story chronology. Prefer active references over older pilot/style-study
   versions. If repository access is unavailable, do not treat memory alone
   as proof that a specific appearance state is cleared.
3. Build a *preflight inventory* of **every specific subject needed in the
   frame**, each with a campaign-qualified ID, the scene-relevant state ID,
   reference file/version, and required/excluded identifying features.
   Include: named characters, creatures, vehicles, signature equipment,
   recognizably depicted artifacts and locations, relevant factions/insignia,
   and the event itself if the request is a specific named/historical event.
   A state-changing building, costume, injury or transformation counts as
   a distinct required *state*, not necessarily a new entity.
4. Incidental anonymous scenery (plain sky, soil, generic vegetation) does
   not require independent subject research unless its identity or unique
   lore is important. **Never evade a research gate by relabeling a known
   entity as 'generic' background or by borrowing another campaign's design.**

## 1. Mandatory preflight: decide READY or BLOCKED

For **every** inventory item, verify **all**:

- **Identity:** A real, indexed, campaign-qualified appearance record exists;
  shared names between Wastes/Inverse/Delvers are not interchangeable.
- **Evidence:** A source-linked recognition baseline and documented visual
  features exist; their verification class is explicit. A generic `world/`
  biography, ASR keyword hit, unintegrated audit, wiki fan art or
  generated picture alone does **not** count as researched.
- **Story-time fit:** A state or source-supported state applicability matches
  the exact scene/cutoff, including equipment, changing location state,
  injury, damage, transformation or destruction. Do not transpose a late
  portrait into an early scene. Historical revelations need correct story
  time, not just revelation episode.
- **Drawable completeness:** Defining silhouette/anatomy/geometry, any
  source-mandated color/material/markings, relevant possessions, exclusions,
  and time-specific changes are concrete enough for the requested camera
  view. Significant contradictions and crucial missing design-sheet evidence
  requiring further research are blockers. **An ordinary undecided detail**
  may be filled by an *explicitly provisional artistic choice* if doing so
  cannot override source evidence or resolve a material contradiction.
- **Reference integrity:** Resolve stable IDs, working links and relevant
  versions. A stylistic trial is not a selected canonical appearance sheet.
  Audio verification and owner art approval are **not required** when the
  documented ASR-based record is sufficiently drawable for a *provisional*
  image; preserve that status and do not promote it to verified canon.

**Decision:**

- `READY` only if **all** required subjects pass for **this** scene.
- `BLOCKED` on one or more failures or unavailable essential references.
  **STOP before any image-generation/editing/preview tool call.** Execute
  section 2 and end the invocation. Do not continue into prompt creation,
  style tests or visual drafts. If a seemingly minor detail actually governs
  identity, make it a research blocker rather than guessing.

## 2. BLOCKED path — durable queue first, user notification second

1. Collect **all** missing/insufficient entities in the requested image,
   not merely the first. For each, record: campaign, stable ID or provisional
   name, type, requested scene/state/spoiler cutoff, specific missing visual
   evidence or unresolved conflict, existing references actually checked,
   next bounded subject-research action, and the **blocked image request**.
2. Open [the dedicated queue](../../../project/ILLUSTRATION_RESEARCH_QUEUE.md)
   and check for an existing item with the same **campaign + subject +
   scene/state + research gap**. Append this request/date to the existing
   entry, or assign the next unused `IRQ-####` ID and add a `queued` entry
   with its exact missing work. If access to a critical image/source is
   blocked, mark `blocked-access` rather than claiming the entity has never
   been studied. **Do not use the general episode REVIEW_QUEUE as a substitute.**
3. Save via an available *non-destructive* repository edit (guarded patch,
   local file edit or permitted workspace write); read back changed entries
   and confirm persistence. Do not commit/push or overwrite unrelated work.
   If the write fails, **remain BLOCKED**, report the failure and present
   the intended entries for manual recording; never claim they were saved.
4. Tell the invoker **no image was generated**, list each pending subject,
   missing state/detail and queue ID if actually saved, link the queue, and
   propose the precise `$twbd-illustration-research ...` follow-up(s).
   Do not start that research automatically inside this generation run;
   future research is an independent step. Once integrated, a **new**
   generation invocation rechecks the whole composition. Clearing a queue
   entry never silently resumes generation or schedules background work.

**Failure examples:** a researched E006 Fate 4 and an unresearched named
rider still block a joint image; an E006 reference does not clear an E028
patched-roof scene unless that state is integrated; a Delvers subject
cannot inherit the look of a similarly named Wastes creature. These are
preflight examples, **not** new queued requests and not authorization to
create example art.

## 3. READY path — preserve visual lineage, then build the brief

### 3A. Mandatory existing-illustration continuity pass

Complete this **before composing a prompt**, for **every recognizable
depicted subject**. Being researched is not the same as being visually
unrepresented: check both.

1. **Find existing artwork:** From the appearance register and subject
   records, locate production-image IDs and actual images in the repository's
   `illustrations/` tree, referenced `world/` pages and linked production
   reports. Include the same subject across **all documented appearance
   states**, not only images named for the requested episode. Keep separate
   any archive/fan illustrations and superseded experiments. Search by
   campaign-qualified ID, names and relevant aliases; do not equate
   another campaign's similarly named entity with the subject.
2. **Inspect the image, not just its filename or caption:** Open the actual
   viewable pixels wherever available, alongside its record, provenance,
   selection status, applied state(s), date/story placement, revision and
   known errors. Distinguish **owner-selected** project depictions,
   owner-approved model sheets, provisional drafts, superseded images,
   fan interpretations and creator source handouts. Record which files were
   truly viewed and which could not be inspected.
3. **Choose visual anchors by applicability and authority:** First prefer a
   compatible **approved or selected same-state** depiction/model sheet.
   Next use selected depictions of adjacent states for *persistent*
   identity features only. Older or later images may help recognize the
   subject but must be filtered through the full state timeline. A
   production depiction can establish a **working artistic convention**
   (such as otherwise unspecified paint) when explicitly selected for
   reuse; it is never new evidence of show canon. Drafts, fan art and
   unrelated-epoch pictures have no automatic authority. New source
   evidence supersedes a conflicting artistic choice **even in approved
   older art**; flag existing affected assets for review.
4. **Build a state-aware continuity matrix** in the visual brief:
   - **Carry forward:** stable silhouette, proportions, facial structure,
     distinctive markings, persistent palette/material choices and
     orientation/asymmetry that apply through this story interval.
   - **Change for this depiction:** explicitly sourced or chosen alterations
     between the anchor's state and target (growth/aging, new clothes,
     equipment, injury/scars, transformation, vehicle damage/repair,
     place architecture, occupancy, weathering or location-specific dirt).
   - **Exclude/revert:** later features not yet obtained, lost/removed gear,
     unrepaired damage at an earlier point, temporary effects that have
     ended, and details unique to another location/illumination/viewpoint.
   - **Unresolved:** significant disagreements, image provenance gaps,
     physical differences the source does not explain or speculative
     fixes. Decide whether it is safe to leave those off-frame, use an
     explicit provisional artistic treatment, or **BLOCK** for additional
     source research/access.
5. **Location, viewpoint and temporal reasoning:** Environmental lighting,
   color casts, pose, framing, dampness, dust, mud and shadows may change
   without changing the subject's intrinsic colors or design. A location
   itself may acquire physical changes, damage or repairs; use its matching
   location-state reference. Characters can change costume/gear or carry
   temporary grime without becoming different people. Reuse consistent
   anatomy/geometry even when new composition or camera angle differs.
   Flashbacks and prequels use **story-time** appearance, not the later
   published image's outfit or present-day condition. When multiple
   entities appear, pin every entity and the setting to compatible
   simultaneous states.
6. **Use real anchors in generation when supported:** Provide the relevant
   previously selected image(s) as actual visual references to the image
   generation/editing workflow, with **precise instructions to retain only
   their persistent features and apply target-state changes**. When an
   image cannot be passed to the renderer, do not claim that it was;
   preserve a precise written cross-image comparison and note the
   limitation. If the continuity-critical selected image cannot even be
   inspected and its features are not adequately documented, treat it as
   a `blocked-access` continuity gap (section 2), not a green light to
   guess. Do not modify existing selected assets to obtain a new scene.

**Review existing-art flags before reuse.** Read
[ILLUSTRATION_REVISION_QUEUE.md](../../../project/ILLUSTRATION_REVISION_QUEUE.md)
for each visual anchor's open issues. Check issue evidence and **target
story-state applicability**; omit flagged features rather than copying
them into a new render. If this pass reveals an additional mismatch,
new contextual limitation or source conflict, create/update an `IRV-`
entry with affected image ID/path, severity, verification, state and
proposed review/edit/regeneration action. Cross-link affected subject
records; preserve selected assets and owner decisions. Deduplicate.
Differences expected from era, location, weather, camera, costume or
repair **are not automatically errors**. If the mismatch leaves the
**requested** subject insufficiently researched, also create an `IRQ-`
blocker and stop. Unrelated outdated drafts need not block new work.

**Example — Fate 4:** The owner-selected E006 garage illustration
`WASTES-FATE4-ILL-001` anchors the *completed unveiling* vehicle
`WASTES-FATE4-A01` and garage `WASTES-JIMSTERS-GARAGE-A03`.
Use its recognizable vehicle styling as a **working illustration reference**,
not as a technical plan or confirmation of canonical paint. The earlier
E001 build `WASTES-FATE4-A00A` cannot silently inherit the completed
metal dragon-skull front and roof equipment; later `A06` needs the
raptor-hide roof patch and relevant damage despite the intact E006 image.
The garage's E001 construction setting is a different state from the
E006 unveiling setting. Preserve the persistent vehicle identity without
freezing every scene to the same appearance.

### 3B. Construct the state-correct visual brief

For each pictured subject, pin its state ID and reference **version**; if
any of these prove unavailable during briefing, **return to BLOCKED**.
Build a short explicit brief with:

1. Campaign, subject(s), exact scene and spoiler cutoff, objective versus
   subjective visual viewpoint and consistent scale/spatial relationships.
2. **Non-negotiable identity details** from appearance records, including
   required colors, anatomy, silhouette, materials, visible gear and
   exclusions. Keep left/right from the subject's perspective. Separate
   installed equipment from portable supplies; no future costume or repair
   appears early.
3. Source-provenance references *outside* the actual generation prompt and
   a list of **provisional artistic gap-filling decisions** with subject,
   scene and revision. Evidence always outranks the artistic choice.
4. The **verbatim invariant style recipe below**, project-square frame,
   composition, lighting, one primary bright accent and optional second
   accent **across the whole image** (unless established colors require an
   explicit exception), and simple negative space where needed.
5. **Visual-lineage anchors:** Include the selected prior illustrations actually
   viewed, their story-state IDs and review status, and the explicit list of
   details to **carry forward, change or exclude**. Distinguish images examined
   from reference pixels actually supplied to the renderer. Do not present
   unrelated-era, fan, draft or superseded art as an approved model sheet.

### Fixed style prompt block — include unchanged in every generation/edit prompt

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

Treat this prompt block as an **immutable style lock** (v1) introduced
in guide v0.3 and retained unchanged in v0.4. Changes require a deliberate *project-wide style revision* with a
new version, not improvisation for a particular character, medium or
image. The style guide's detailed rules take precedence if a conflict is
found; report and version any correction. An individual scene's mood,
weather, lighting and palette must not turn the style into photorealism,
anime, watercolor, 3-D render or a different comic style. Prior vehicle
style experiments are **not** an owner-approved universal anchor.

### 3C. Hard pre-call style-and-canvas gate — run for every invocation

This gate is **mandatory even for drafts, retries, image edits, revisions,
panoramas, establishing shots, reference sheets and supposedly temporary
previews**. Passing the source-research `READY` gate alone is insufficient.

1. **Load the current guide** and paste the full **unchanged** section 3B
   fixed style prompt block into the **actual image generation/edit request**.
   Describing it merely as "same style as before", "graphic novel" or a
   summary is **not compliance**. Preserve the fixed ink, line weight,
   stylization, flat/cel shadows, muted pastel treatment, limited accents,
   restrained detail and no lettering/borders. A visual reference may help
   retain **subject identity** but must not silently replace the house style.
2. **Set the canvas in both prompt and tool settings:** request square
   aspect ratio **1:1** and **1024 × 1024** wherever the tool permits, and
   explicitly state both in the prompt. Never use tool options suggesting
   16:9, 4:3, portrait or free aspect ratio for this project. If a tool
   supports only square aspect ratio rather than explicit pixels, request
   square and follow with **real output validation/normalization**.
3. **Compose *inside* the square:** Aerial establishing shots, large
   landscapes, groups and long vehicles must retain the entire pertinent
   scene through camera distance, depth, smaller subjects and/or deliberate
   negative space, **not** by widening the file. Multi-view sheets tile all
   views within the square. No cropping of canonical details or stretching
   geometry to force a fit.
4. **Resolve conflicts explicitly:** An incompatible requested output ratio
   or radically different art style is **not permission** to waive a
   collection-wide rule. If faithful square/style treatment would defeat an
   explicit essential user constraint, stop and report the conflict; a
   deliberate updated guide/version or distinct non-project illustration
   request is needed to depart from it.
5. **Check completion capability before generating:** Ensure a practical
   way exists to read **actual output image bytes/dimensions**, correct
   unexpected dimensions without distortion (prefer a square re-render;
   alternatively fit in a square sRGB PNG without losing features), and
   validate the final asset. If that path is unavailable, disclose the
   constraint and **do not create or present a noncompliant deliverable as
   project illustration**. No speculative file path or claim that a tool
   option guarantees size.

**Pass/fail checkpoint**: `source-ready AND style-block-in-prompt AND
square-request AND preservation-of-scene-in-square AND validation-path`.
Do not invoke generation or editing with any of these fields missing.

## 4. Generate, normalize and compare — only after READY

1. **Generate with the actual mandatory configuration.** Use the fixed
   style prompt block unchanged and explicitly select square 1:1, requesting
   1024x1024 when supported by the tool. The picture's viewpoint (including
   an aerial panorama) changes how much of the subject is drawn **within**
   that square, not the canvas dimensions. For each new variant, retry or
   edit, **repeat the pre-call gate**; do not inherit unspecified tool settings
   from the prior render.
2. **Inspect real image bytes after every render, before acceptance.** Decode
   the returned image/file and verify both pixel dimensions are **1024**
   (not merely that the prompt said 1024), its encoded format is **PNG**,
   and the final color is **sRGB**. Use image metadata plus a reliable decoder
   or image library; if a color profile is missing/unknown, perform and verify
   a controlled sRGB conversion when possible, otherwise mark sRGB **not
   verified**. A matching filename, claimed tool size or thumbnail alone
   cannot pass this gate. Record raw width/height/format/profile result.
3. **Normalize or reject nonconforming output without distorting evidence.**
   Preferred: rerender or edit with square framing and the unchanged style
   block. If correction tools are available, proportionally fit the entire
   image **inside** an exact 1024x1024 sRGB PNG using intentional
   background/negative space; preserve all scene-defining elements and
   recognizable anatomy. **Never crop canonical features, nonuniformly
   stretch, or silently letterbox a final image with awkward padding.**
   Inspect corrected composition and decode/verify the **final saved bytes**
   again. If required correction, export or actual-dimension verification
   cannot be performed, the image is **INVALID FOR PROJECT USE**—no catalog
   entry as accepted artwork, no world-page embed, no claim of completion.
4. **Perform a separate visual style gate**, not just a prose assertion.
   Inspect the actual pixels against the current guide's fixed recipe:
   bold dark varying contours, finer interior inks, recognizably slightly
   cartoon-stylized forms, matte muted-pastel broad areas, controlled
   cel-shaded shapes, restrained hatching/detail, one primary and at most
   one supporting vivid accent (unless source-established colors demand
   more), and no incidental text/frames/watermarks. Compare with selected
   style-compatible references when available; do **not** let fan art,
   reference photographs, or an older off-style generated image override
   the house style. A style-mismatched render fails regardless of its size.
5. **Perform the distinct lore/time/continuity gate** using section 3A's
   actual subject references and each depicted story state. Check stable
   anatomy, geometry, colors and props, appearance changes, setting and
   exact scene/cutoff independently of the style check. A source-critical
   feature cannot be excused as an artistic simplification.
6. **Correct or quarantine, never silently accept.** New edits must use
   the same square canvas + verbatim style block and pass **all three**
   post-render gates (technical format/size/color, visual style, source and
   story-time). Keep original outputs identifiable but label nonconforming
   renders as `invalid-output` or `noncompliant-study`, not as usable
   draft/selected project assets. For pre-existing owner-selected but
   technically nonconforming images, **retain the selection history** and
   record the technical defect for review rather than silently overwriting
   the image or retroactively claiming valid production dimensions.
7. **Save only a verified deliverable and update the production record.**
   Before embedding in `world/` or claiming a repo asset exists, verify the
   exact saved file's path, dimensions, PNG/sRGB encoding and repository
   presence/readback. For every version record the **original render**
   dimensions and format, any transformation and correction method, **final
   verified** pixel size/format/color profile, art-direction version,
   subject/state IDs, verbatim prompt and reference use, actual visual
   inspection, style and lore review outcomes, image IDs and approval
   status, using [the subject template](../../../project/ILLUSTRATION_SUBJECT_TEMPLATE.md).
   No missing-file Markdown embeds, invented metadata, false test passes,
   or automatic owner approval.
6. **Post-generation consistency audit:** Compare the candidate and prior
   illustrated states to the latest evidence, including every visible
   recurring subject, significant prop and scene location. For a new
   source conflict, a newly understood historical context, missing
   defining feature, unexpected persistent-design drift, or deliberate
   continuity deviation, create/update and cross-link an `IRV-` review
   flag for **each affected existing or newly generated image**. Distinguish
   an actual discrepancy from story-appropriate change and avoid asserting
   image inspection when pixels were unavailable. Indicate whether only
   an annotated review, local edit, or complete regeneration is warranted.
   The discovery of a bad prior selected image does **not** authorize
   overwriting or replacing it; flag for owner review and preserve its ID.
7. Preserve image source/copyright provenance per
   [image asset policy](../../../project/IMAGE_ASSETS.md). The owner may
   later mark a model sheet or illustration **owner-approved**; generation
   itself grants no such status. Publish/share outside the repository only
   when media rights are clear.

## 5. Bounded validation and response

**Revision-flag check:** In both READY and BLOCKED paths, report whether
the existing-art impact scan found any affected illustrations, give
`IRV-` IDs and statuses for flags actually persisted, and distinguish
newly identified issues from pre-existing ones. Verify the ledger's
entries and subject cross-links by reading them back. Flagging alone
does **not** authorize a replacement render or alter a selected image.

- **BLOCKED:** Confirm queue entries were written/read back; no image
  generator was invoked; report subjects, scene-specific blockers, IDs,
  queue path and exact research actions. If the queue could not be
  persisted, disclose that blocker and do not generate.
- **READY and generated:** Record a distinct outcome for each mandatory
  gate: `research_time_state=PASS`, `style_prompt_included=PASS`,
  `requested_square_1024=PASS`, `actual_final_png_1024x1024=PASS`,
  `final_srgb=PASS`, `visual_style=PASS`, and
  `source_continuity=PASS`. Mark any unknown verification `UNVERIFIED`,
  never `PASS`; if any are `FAIL` or `UNVERIFIED`, the deliverable is
  **not accepted for project use**. Cite the exact inspected/re-read image
  and its location rather than a hypothesized output path.
- **Regression examples (enforced outcomes):** A 1672x941 Dusthill aerial
  that otherwise looks right is `FAIL: actual_final_png_1024x1024` until
  **correctly recomposed or converted and reverified**; choosing it for a
  world page is not a waiver. A perfectly sized 1024x1024 image rendered
  photorealistically or with heavily saturated, painterly gradients is
  `FAIL: visual_style`. A technically correct graphic-novel image with
  a missing era-defining feature is `FAIL: source_continuity`. Only an
  image satisfying **all** gates may be cataloged as a conforming candidate
  or used in a `/world` page.
- **Fail-closed reporting:** If generation itself cannot deliver a square,
  validated, style-matched artifact, report the attempted source image
  and why it failed, any safe correction actually completed, and the
  remaining limitation. Do not claim the project illustration is finished,
  generate unrelated substitutes, fabricate successful validation, or leave
  broken image links. Run only relevant local checks, avoid full corpus
  rescans, and never alter original transcript SRTs, audio or archived
  source images.

**Keep the research and illustration functions separate:** the research
skill builds source-linked appearance knowledge; this skill either uses
already integrated knowledge to generate consistent art or records why
it must not generate yet.
