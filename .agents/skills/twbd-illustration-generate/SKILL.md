---
name: twbd-illustration-generate
description: Generate consistent, source-faithful illustrations for researched entities and specific story moments in There Will Be Dungeons (The Wastes, Inverse, Delvers and other separately identified adventures). Require integrated subject appearance research first; when a subject or required state is unresearched, do NOT generate any image—record a blocker in the dedicated illustration research queue and inform the requester. All project illustrations share one fixed 1024x1024-pixel square canvas and graphic-novel style.
---

# TWBD illustration generation — research-gated, style-locked

## Trigger and absolute invariants

Invoke for requests such as `$twbd-illustration-generate Wastes Fate 4 at E006`,
`$twbd-illustration-generate Delvers Koh Spiros at S1E10`, or
`$twbd-illustration-generate Wastes E066 scene: the tyrannosaur crushes Fate 4`.
This skill **produces visual art only for entities whose required appearances
have already been researched and integrated**. It does not research subjects
from scratch and must not fabricate their canonical look.

**Two non-negotiable contracts:**

1. **Identical output dimensions and style:** Each canonical image—portrait,
   creature study, vehicle, location, event scene, multi-view sheet, variant,
   edited version or draft submitted as project art—must be **1024 × 1024
   pixels**, square (1:1), **PNG, sRGB**, with the shared style lock from
   [illustration guide v0.3](../../../project/ILLUSTRATION_GUIDE.md#fixed-production-canvas-and-style-lock-v03).
   NEVER silently switch to landscape, portrait or a different pixel size.
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
   [research queue](../../../project/ILLUSTRATION_RESEARCH_QUEUE.md), and
   applicable named subject records, source/image provenance and relevant
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

## 3. READY path — construct a source-faithful visual brief

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
5. Selected previously reviewed/appropriate project reference images when
   actually available. Do not use a fan image whose provenance, depiction
   era or reuse restrictions make it inappropriate, and never assume an
   archived image is owner-approved simply because it exists.

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

Treat this prompt block as an **immutable style lock** (v1) tied to guide
v0.3. Changes require a deliberate *project-wide style revision* with a
new version, not improvisation for a particular character, medium or
image. The style guide's detailed rules take precedence if a conflict is
found; report and version any correction. An individual scene's mood,
weather, lighting and palette must not turn the style into photorealism,
anime, watercolor, 3-D render or a different comic style. Prior vehicle
style experiments are **not** an owner-approved universal anchor.

## 4. Generate, normalize and compare — only after READY

1. Use the image-generation/editing capability available for the request.
   Explicitly request **square 1024x1024**. For a tall figure, use vertical
   composition **within the square**; for a broad location, retain the square
   and widen the depicted field instead of changing the canvas.
   Multi-view model sheets tile views **inside one 1024x1024 canvas**;
   producing several distinct variants yields several **individually
   square** images.
2. Check the **actual output dimensions** and exported format. An output
   does not enter the project illustration catalog or count as complete if
   its final canonical PNG is not exactly 1024x1024. If tooling permits,
   conform an off-size output using a non-distorting fit inside a square
   canvas with matched neutral background—**never stretch or crop away
   relevant features**. If exact sizing/export cannot be verified or
   corrected, report the image as incomplete/invalid rather than claiming
   an accepted asset. Do not fabricate output file paths or image metadata.
3. Visually inspect every candidate against **the same style lock** and
   appropriate selected project-owned references, if any: weight of ink,
   pastel balance, limited accent hues, restrained texture and shadows,
   anatomy, scale and recognizable features. Check the selected historical
   states and exclusions **separately** from visual style. No 'close enough'
   acceptance for a source-critical missing feature.
4. If corrections are required, create a **new versioned edit** on the same
   1024x1024 square, retaining the subject/state references and style lock.
   Recheck dimensions and lore fidelity after each edit. A candidate may be
   retained as a labeled draft with known issues but not marked selected;
   do not overwrite the old image or silently redesign recurring features.
5. Add a production record in the subject appearance file(s) or linked
   register, using [the subject template](../../../project/ILLUSTRATION_SUBJECT_TEMPLATE.md):
   image/version ID, true output path or identifier, 1024x1024 PNG check,
   guide/style-lock version, entity IDs/appearance-state IDs and versions,
   exact prompt/edit instructions, images actually provided as references,
   artistic decisions, source-fidelity review, style review, author/reviewer
   and selection/approval status. Record unknown metadata as unknown; no
   invented random seed, model version, license or approval.
6. Preserve image source/copyright provenance per
   [image asset policy](../../../project/IMAGE_ASSETS.md). The owner may
   later mark a model sheet or illustration **owner-approved**; generation
   itself grants no such status. Publish/share outside the repository only
   when media rights are clear.

## 5. Bounded validation and response

- **BLOCKED:** Confirm queue entries were written/read back; no image
  generator was invoked; report subjects, scene-specific blockers, IDs,
  queue path and exact research actions. If the queue could not be
  persisted, disclose that blocker and do not generate.
- **READY and generated:** Confirm every subject's appearance state,
  invariant prompt style block, actual 1024x1024 output size, no accidental
  exclusions/spoilers, stable image ID/path and linked production record.
  Report what was visually inspected, whether dimensions were technically
  checked, review outcome and what remains provisional.
- If source or tooling access is limited, be explicit; do not pretend
  the illustration passed its size/style review or that a record was
  persisted. Run only relevant local checks, avoid full corpus rescans,
  and never alter original transcript SRTs, audio or archived source images.

**Keep the research and illustration functions separate:** the research
skill builds source-linked appearance knowledge; this skill either uses
already integrated knowledge to generate consistent art or records why
it must not generate yet.
