---
name: twbd-illustration-research
description: Research source-grounded visual references for a named There Will Be Dungeons entity (character, creature, place, item, vehicle, event or faction), across its appearances and changes in story time. Use for requests like "$twbd-illustration-research Wastes Fate 4", illustration-reference backfills, visual continuity audits and accurate subject sheets. Do not use for image generation or unrelated fantasy concept art.
---

# TWBD illustration research — entity-first appearance history

## Trigger and deliverables

Given **one named entity**, determine its campaign and identity, locate visual evidence in the transcripts and creator/archived references, and produce a **drawable, source-linked appearance record with time-specific states**. Research across relevant episodes, not merely the next episode. Honor any requested story interval or spoiler cutoff; otherwise search the available campaign corpus in resumable passes and identify unreviewed gaps. This skill researches appearance; it **does not generate or approve images**.

Examples: `$twbd-illustration-research Wastes "Fate 4"`; `$twbd-illustration-research Delvers "Koh Spiros" through S1E10`; `$twbd-illustration-research Wastes Tietkalla at first appearance`.

Consult [illustration guide](../../../project/ILLUSTRATION_GUIDE.md), [subject-reference template](../../../project/ILLUSTRATION_SUBJECT_TEMPLATE.md), [appearance register](../../../project/ILLUSTRATION_REFERENCES.md), [editorial guide](../../../project/EDITORIAL_GUIDE.md), [image provenance](../../../project/IMAGE_ASSETS.md), [external references](../../../project/EXTERNAL_REFERENCES.md), and campaign-specific indexes, chronology, world pages, source inventories and review queues as applicable.

**Worked example:** [Fate 4 transcript audit](../../../reports/FATE_4_TRANSCRIPT_AUDIT_2026-10-25.md) and [search manifest](../../../reports/FATE_4_TRANSCRIPT_AUDIT_2026-10-25.json). This is an exemplar of research method, not a universal feature list. Its saved findings awaited appearance-register integration at the time of the audit.

Keep The Wastes, Inverse, Delvers, and other adventures in separate continuities. Distinguish the entity from impersonators, lookalikes, transformations, derivative objects, and other entities with similar names.

## 0. Identity, access and resume

1. Inspect branch/HEAD, Git status, relevant existing appearance records and audit checkpoints. Preserve unrelated edits and all source SRTs, audio and images. Identify whether a connector exposes the live worktree, a pinned GitHub revision or an older snapshot; never silently mix them. The workspace MCP may expose the repository under `There Will Be Dungeons Transcripts/`.
2. Establish campaign, stable campaign-qualified subject ID, kind, established spelling, aliases/ASR variants, namesake ambiguities, first appearance and requested spoiler cutoff. Check the entity's world page, episode dossiers, spelling ledger and prior art.
3. Inventory exact source paths and versions: primary and independent ASR, audio (if accessible), creator handouts, maps, image files, dossiers and past reports. An image file's existence is **not** evidence that it has been visually inspected.
4. Reuse recorded searches and prior checkpoints. Record source fingerprints/commit, which episodes were screened, which windows were actually read, what remains open and the first incomplete phase before doing new work.

## A. Broad entity-centered source search

1. Search relevant episode dossiers and known scenes, then **transcript text** across the campaign's selected corpus. Build queries from proper name, titles, aliases, phonetic ASR variants, common nouns and local context. Catch descriptions using pronouns or generic labels without the entity's name.
2. Join adjacent SRT cues and examine nearby context. Search visual terms suited to the subject: build, color, size, clothing, scars, markings, anatomy, gear, weapons, surfaces, materials, shape, movement, doors, windows, landmarks, arrangement, damage, repair, transformation and illumination. Search both feature descriptors and event verbs.
3. Distinguish search candidates from confirmed references. Explicitly log rejected matches (wrong person/vehicle, homophone, metaphor, hypothetical, future plan, unrelated scene). Fate/Faith/Feet and Four/For/4 yielded false hits in the Fate 4 pilot.
4. Prioritize first appearance and origin, high-density descriptions, creator sheets, equipment transitions, injuries/damage/repairs, transformations, end state, and later recollections. Search bonus Q&As and flashbacks as **retrospective sources**, not as additional played events.
5. For large corpora use bounded parsing/search and save a dated manifest, ideally `reports/ILLUSTRATION_<CAMPAIGN>_<ENTITY>_AUDIT_<date>.json`, with schema version, ref/hashes, exact filenames, search terms, files screened, candidates/cue windows and semantic-review status. Store disposable intermediate data under ignored `local/`. A parsed corpus is not fully semantically reviewed or audio-verified; report omissions in coverage.

## B. Read and verify actual scene evidence

Read complete relevant scene windows before accepting any keyword hit. For each material finding record a stable evidence ID `S01`, `S02`, etc., exact source path and version, episode/time/cue/page, source role, feature, applicable story time, disclosure time, verification level and uncertainty.

Keep **evidence role** separate from **verification**: played GM narration/action; character claim or subjective memory; player joke or hypothesis; cast/GM retrospective clarification; creator design; fan wiki/art; inference; artistic choice. Mark ASR-only, independent ASR text corroboration, actually listened-to interval, directly inspected image, or inherited earlier dossier. Two ASR exports are not audio verification. A creator sheet may represent a different era; final-campaign character sheets and fan art do not prove first-appearance designs. Note provenance and reuse rights of all image leads.

Distinguish **permanent appearance** from visible carried/worn equipment, stored inventory, installed components, temporary transformations, illusions, lighting, condition and scene effects. Capabilities influence plausible poses/actions but need not be visually apparent. A fictional object mentioned as owned is not necessarily present in the frame. Do not infer standard fantasy anatomy or exact color merely from game statistics or a creature name.

Compare alternative ASR on consequential ambiguities (color, dimension, number, anatomy, left/right, negation, identity, possession, change). Retain disputes and targeted audio-listening tasks. Never invent listening, cue locators, timestamps, measured dimensions, colors or image-inspection results. Record false positives and excluded proposals with evidence rather than simply deleting them.

**Fate 4 cautionary example:** the E006 description includes a fabricated metal dragon-skull front, roof solar panels, rear ladder and exterior combat rails in addition to enormous tires. Earlier trial illustrations omitted defining features. A weapon-filled front seating area does **not** imply a mounted turret. The E028 raptor-hide roof patch is not metal, and the E057 interceptor's colors/chained tires and a bonus's hypothetical mounted gun do **not** describe Fate 4. Consult the linked audit for exact evidence rather than reusing these facts for other vehicles.

## C. Build appearance states and design constraints

Follow the subject template; retain existing IDs, evidence and historical decisions.

1. Create a concise **recognition baseline** covering defining silhouette, proportions, motifs, intrinsic colors/materials and source-supported distinctive features. Mark unspecified features openly.
2. Define stable, campaign-qualified state IDs (`<SUBJECT-ID>-A01`, `A02`, etc.) for genuinely distinct appearances: introduction, origin revealed later, equipment change, major injury, disguise, repair, destruction, restoration, and other supported transformations. Track **when true in story** separately from **when learned**. Use `start unknown` and `end unresearched` rather than stretching a state across unknown periods.
3. For each state write a **complete drawable description**, baseline and deltas, colors/materials versus lighting, scale/orientation (left/right from subject perspective), visible accessories versus custody, required exclusions at that point, unknown choices and evidence IDs. Minor ephemeral changes may remain scene notes rather than new permanent states.
4. Separate supported facts (`S`) from creative gap-filling choices (`D`) and existing images/production references. A generated image never establishes source canon. Preserve prior choices, note when new evidence contradicts them, and list which earlier images/prompts need revision. **Owner-approved** requires actual approval.
5. Subject checks: characters—face, age/build, expression, clothing, wounds and worn gear; creatures—individual versus species anatomy, scale and movement; places—geography, landmarks, architecture, spatial relationships and temporal condition; items/vehicles—construction, openings, scale, mechanisms and repairs; events—exact moment, participants and each one's applicable state, location and spoiler cutoff; factions—insignia versus non-universal clothing.

## D. Persist audit and active appearance reference

For a substantial search, publish a dated `reports/ILLUSTRATION_<CAMPAIGN>_<ENTITY>_AUDIT_<date>.md` with scope and pinned source identities, search methodology, **files screened versus passages read/listened**, grouped evidence, state chronology, rejected leads, unresolved contradictions, image provenance and explicit next checks. Link any machine-readable search manifest.

**Mandatory integration gate:** update `project/ILLUSTRATION_REFERENCES.md` or an indexed dedicated subject file with the evidence IDs, recognition baseline, complete supported states, conflicts, artistic decisions, existing illustration impact list and change log. The search report alone is **not** an integrated/finished reference. Preserve pre-existing state IDs and records; fix relevant source mistakes in separately bounded edits or log a precise correction task if unsafe to do now.

**Research-queue handoff:** Before completing an entity requested through
[the illustration research queue](../../../project/ILLUSTRATION_RESEARCH_QUEUE.md),
inspect its matching `IRQ-####` entry and required scene/state. Update that
entry to `resolved` **only after** the needed time-specific appearance
evidence and drawable description are integrated in the register; record the
active reference path, state/version and outstanding nonblocking limits.
If research is still incomplete, leave the entry `queued`, `researching`
or `blocked-access` with its exact next check. Completing research **never
automatically generates** a previously blocked illustration; a new
generation invocation must recheck *all* depicted subjects.

Keep production evidence outside reader-facing, in-universe `world/` prose. Cross-link through indexes/footnotes without adding ASR uncertainties, timestamps or research boilerplate to narrative text.

At the end of each phase persist a resumable checkpoint: campaign/entity ID, source revision, searched inventory, reviewed windows, files written, completed phase, pending integration/validation and **one next step**. Prefer `local/illustration-research/<campaign>-<entity>/` for local-only progress, otherwise a short clearly provisional report section. Do not claim a checkpoint was saved if a write failed. On continuation, resume the first incomplete phase instead of restarting the corpus sweep.

## E. Targeted validation and outcome

Read back edited sections, inspect final Git status and ensure no original source media/SRT was changed. Check stable IDs, story-state boundaries, evidence role versus verification wording, real relative links, register index and Markdown tables. Where a suitable project runner exists, lint **only changed maintained Markdown**, for example `npm run lint:markdown -- --files <changed-paths>`. Run only relevant tests; report editorial verification and automated checks independently as **passed / failed / not run**, without invented success claims. Do not run InfinityDB-only check tools against this repository. Do not silently commit, push or overwrite unrelated edits.

Report: entity/campaign; source ref; screened versus context-read versus listened coverage; strongest drawable requirements and changes; files written; active register integrated or pending; remaining contradictions and exact next check. An incomplete session ends with a durable phase checkpoint if writing is supported, not a claim of full research.
