---
name: twbd-illustration-research
description: Research source-grounded visual references and prepare written character design-sheet briefs for recurring TWBD characters, alongside other creatures, places, items, vehicles, events and factions across changing story appearances. Cross-reference campaign-end D&D Beyond character-sheet JSON for canonical spelling and leads to characters, items, locations and NPCs, but never backdate final-sheet appearance or inventory. Keep evidence and state chronology distinct, and flag existing art that needs review. No image generation.
---

# TWBD illustration research — entity-first appearance history

## Trigger and deliverables

Given **one named entity**, determine its campaign and identity, locate visual evidence in the transcripts and creator/archived references, and produce a **drawable, source-linked appearance record with time-specific states**. Research across relevant episodes, not merely the next episode. Honor any requested story interval or spoiler cutoff; otherwise search the available campaign corpus in resumable passes and identify unreviewed gaps. This skill researches appearance; it **does not generate or approve images**.

Examples: `$twbd-illustration-research Wastes "Fate 4"`; `$twbd-illustration-research Delvers "Koh Spiros" through S1E10`; `$twbd-illustration-research Wastes Tietkalla at first appearance`.

Consult [illustration guide](../../../project/ILLUSTRATION_GUIDE.md), [recurring-character design-sheet specification](../../../project/ILLUSTRATION_CHARACTER_DESIGN_SHEETS.md), [subject-reference template](../../../project/ILLUSTRATION_SUBJECT_TEMPLATE.md), [appearance register](../../../project/ILLUSTRATION_REFERENCES.md), [illustration revision queue](../../../project/ILLUSTRATION_REVISION_QUEUE.md), [editorial guide](../../../project/EDITORIAL_GUIDE.md), [image provenance](../../../project/IMAGE_ASSETS.md), [external references](../../../project/EXTERNAL_REFERENCES.md), and campaign-specific indexes, chronology, world pages, source inventories and review queues as applicable.

**Worked example:** [Fate 4 transcript audit](../../../reports/FATE_4_TRANSCRIPT_AUDIT_2026-10-25.md) and [search manifest](../../../reports/FATE_4_TRANSCRIPT_AUDIT_2026-10-25.json). This is an exemplar of research method, not a universal feature list. Its saved findings awaited appearance-register integration at the time of the audit.

Keep The Wastes, Inverse, Delvers, and other adventures in separate continuities. Distinguish the entity from impersonators, lookalikes, transformations, derivative objects, and other entities with similar names.

## 0. Identity, access and resume

1. Inspect branch/HEAD, Git status, relevant existing appearance records and audit checkpoints. Preserve unrelated edits and all source SRTs, audio and images. Identify whether a connector exposes the live worktree, a pinned GitHub revision or an older snapshot; never silently mix them. The workspace MCP may expose the repository under `There Will Be Dungeons Transcripts/`.
2. Establish campaign, stable campaign-qualified subject ID, kind, established spelling, aliases/ASR variants, namesake ambiguities, first appearance and requested spoiler cutoff. Check the entity's world page, episode dossiers, spelling ledger and prior art.
3. Inventory exact source paths and versions: primary and independent ASR, audio (if accessible), creator handouts, maps, image files, dossiers, **available D&D Beyond character-sheet JSON exports**, and past reports. **For The Wastes location research, inspect the current private `local/images-wiki/maps/` collection and its filename/hash registry in `project/IMAGE_ASSETS.md`; do not rely on legacy opaque map filenames under `sources/images/`. As of 2026-10-25 the owner recalls all six maps are likely GM-originated, but that remains an unverified attribution and does not authenticate each map's story-era applicability. Distinguish Dusthill's surface plan from the separate caverns diagram; distinguish annotated from unannotated regional maps.** An image file's existence is **not** evidence that it has been visually inspected. Treat character-sheet JSON as an **end-of-campaign snapshot**, not as the opening-era build or inventory. Check `sources/json/` as a **mixed-campaign source directory** and discover additional exports dynamically; assign each sheet to a campaign from established character identity and project references, **not merely from its folder or filename**.
4. Reuse recorded searches and prior checkpoints. Record source fingerprints/commit, which episodes were screened, which windows were actually read, what remains open and the first incomplete phase before doing new work.

## 0A. Character-sheet JSON cross-reference — campaign-end only

**Mandatory when relevant exports are available, even for a requested
item, location, NPC or creature rather than a player character.** First
inventory the exports in the shared `sources/json/` directory, identify
the represented character and **campaign for each**, then read all
relevant sheets from the requested **same campaign** as an additional
structured source of identifiers, orthography and *candidate*
connections. Example Wastes exports include:

- `sources/json/hope-akmenos.json`
- `sources/json/nash-maggard.json`
- `sources/json/stanley-billings.json`
- `sources/json/vorel.json`

These filenames are **examples, not an exhaustive or campaign-defining
inventory**. The same `sources/json/` directory also contains Wastes and
Delvers exports with numbered filenames; discover new ones at each run.
Determine subject identity and campaign before cross-referencing (a
matching name or shared directory is insufficient). If two JSON exports
refer to the **same character-sheet ID**, recognize them as potentially
duplicate or different snapshots, compare hashes and actual metadata,
retain both source identities where relevant, and avoid double-counting
as independent corroboration. If sheet access is unavailable, note it.
**All currently supplied character sheets represent their characters at
the end of their respective campaigns, per the archive owner.** Never
assume that a Delvers sheet describes a Wastes character or that any
sheet supplies a historical revision merely from its filename.

1. Parse **actual JSON structure**, rather than searching only the top-
   level `data.name`. Exports may be minified as **one very large line**;
   use bounded programmatic JSON parsing or structured extraction when
   available, avoiding enormous raw tool outputs. If access is truncated
   or only a fragment was read, report **partial coverage**, not a
   full-sheet review. Prioritize character-entered names, descriptions,
   custom/background notes, explicit custom features, named item
   definitions, inventory/equipment, custom actions, spell labels and
   meaningful entity mentions in text fields. In common D&D Beyond
   exports, `data.name`, `data.hair`, `data.eyes`, `data.skin`,
   `data.height`, `data.weight` and inventory/description fields may
   be informative; inspect the **actual keys and populated values**.
   For the main character, these may describe their **late appearance**.
   For items, NPCs, places and other characters mentioned inside *any*
   relevant sheet, record candidate associations with the owning PC.
2. Separate **campaign-specific material** from embedded SRD/class,
   species, subclass, feat, spell or background **boilerplate** (often
   nested under `definition.description`, sometimes HTML). Generic
   rules examples, default equipment lists and stock lore do **not**
   establish that a named NPC, item or location appeared in this show.
   Differentiate *sheet owner entered a claim*, *named item actually
   listed in a final inventory*, *generic D&D rules text* and *inference*.
   An avatar, species portrait or decorative image is **not automatically
   a faithful likeness** of the actual-play character.
3. Treat final-sheet names and spellings as **strong candidates for
   canonical orthography**, especially when they are custom names,
   while recording source spellings, aliases, source field/JSON path and
   ambiguity. Compare them against episode wording, the project's
   canonical spelling ledger, creator materials and relevant other
   sources. A name found in an inventory or note is not sufficient to
   equate two similarly named characters or to prove who possessed an
   item in an earlier scene.
4. **Never backdate.** A final-sheet hair/eye/skin description, level,
   species/class option, feature, magic item, spell, condition,
   relationship, title, character name or equipment entry **does not
   establish its introduction appearance, acquisition episode, earlier
   ownership, earliest ability, or whether it was visibly worn**.
   Avoid reconstructing early builds by subtracting levels or guessing
   gear chronology. Only an independently timestamped episode or
   authoritative historical source can anchor when a feature first
   applies. Keep separate `campaign_end` **source time**,
   `story_applicability=unknown` until corroborated, and the episode
   where it was first narrated or discovered. A later description
   may confirm a stable feature, but that stability itself needs evidence.
5. For each visually relevant extracted lead, capture a compact
   **pointer**, not a huge JSON dump: campaign, owning sheet filename,
   observed source revision/hash when available, JSON path or key,
   short paraphrased value, entity type (PC/NPC/item/place/other),
   relationship, `final-sheet-snapshot` source role, uncertainty
   and targeted episode/source cross-check. Follow that lead into
   transcript windows and existing subject records **before** treating
   it as a visual requirement. Exclude unrelated account identifiers,
   usernames, session/account secrets, boilerplate and irrelevant
   mechanics from maintained documentation.
6. Respect the requested story cutoff and avoid exposing late-campaign
   spoilers in earlier-episode user-facing illustrations or narrative.
   Place terminal-state facts in research notes/late-state sections with
   appropriate spoiler scope. Do not automatically create extra subject
   pages, `IRQ-` blockers or `IRV-` art-revision flags for every string
   in the sheet: only when a meaningful verified visual issue/research
   dependency exists. In particular, a difference between a final
   sheet and an early illustration **is not an inconsistency without
   evidence that the feature applied in the illustrated era**.

**Evidence ranking:** Actual-play scene narration/audio and
time-correct creator material determine what belonged in a pictured
scene; the exported character sheet corroborates a terminal build and
provides high-value spelling and research leads. It cannot itself
establish an earlier scene's physical condition. Record conflicts
rather than silently overriding the transcript or an applicable
historical source.

## A. Broad entity-centered source search

1. Search relevant episode dossiers and known scenes, use **candidate names, aliases and connections from same-campaign final-sheet JSON** (section 0A), then search **transcript text** across the campaign's selected corpus. Build queries from proper names, titles, aliases, phonetic ASR variants, common nouns and local context. Catch descriptions using pronouns or generic labels without the entity's name. A JSON hit is a search lead, not an episode match.
2. Join adjacent SRT cues and examine nearby context. Search visual terms suited to the subject: build, color, size, clothing, scars, markings, anatomy, gear, weapons, surfaces, materials, shape, movement, doors, windows, landmarks, arrangement, damage, repair, transformation and illumination. Search both feature descriptors and event verbs.
3. Distinguish search candidates from confirmed references. Explicitly log rejected matches (wrong person/vehicle, homophone, metaphor, hypothetical, future plan, unrelated scene). Fate/Faith/Feet and Four/For/4 yielded false hits in the Fate 4 pilot.
4. Prioritize first appearance and origin, high-density descriptions, creator sheets, equipment transitions, injuries/damage/repairs, transformations, end state, and later recollections. Search bonus Q&As and flashbacks as **retrospective sources**, not as additional played events.
5. For large corpora use bounded parsing/search and save a dated manifest, ideally `reports/ILLUSTRATION_<CAMPAIGN>_<ENTITY>_AUDIT_<date>.json`, with schema version, ref/hashes, exact filenames, search terms, files screened, candidates/cue windows and semantic-review status. Store disposable intermediate data under ignored `local/`. A parsed corpus is not fully semantically reviewed or audio-verified; report omissions in coverage.

## B. Read and verify actual scene evidence

Read complete relevant scene windows before accepting any keyword hit. For each material finding record a stable evidence ID `S01`, `S02`, etc., exact source path and version, episode/time/cue/page, source role, feature, applicable story time, disclosure time, verification level and uncertainty.

Keep **evidence role** separate from **verification**: played GM narration/action; character claim or subjective memory; player joke or hypothesis; cast/GM retrospective clarification; creator design; **final D&D Beyond sheet JSON snapshot (custom entry versus generic rules text)**; fan wiki/art; inference; artistic choice. Mark ASR-only, independent ASR text corroboration, actually listened-to interval, directly inspected image, or inherited earlier dossier. Two ASR exports are not audio verification. A creator sheet may represent a different era; final-campaign character sheets and fan art do not prove first-appearance designs. Note provenance and reuse rights of all image leads.

Distinguish **permanent appearance** from visible carried/worn equipment, stored inventory, installed components, temporary transformations, illusions, lighting, condition and scene effects. Capabilities influence plausible poses/actions but need not be visually apparent. A fictional object mentioned as owned is not necessarily present in the frame. Do not infer standard fantasy anatomy or exact color merely from game statistics or a creature name.

Compare alternative ASR on consequential ambiguities (color, dimension, number, anatomy, left/right, negation, identity, possession, change). Retain disputes and targeted audio-listening tasks. Never invent listening, cue locators, timestamps, measured dimensions, colors or image-inspection results. Record false positives and excluded proposals with evidence rather than simply deleting them.

**Fate 4 cautionary example:** the E006 description includes a fabricated metal dragon-skull front, roof solar panels, rear ladder and exterior combat rails in addition to enormous tires. Earlier trial illustrations omitted defining features. A weapon-filled front seating area does **not** imply a mounted turret. The E028 raptor-hide roof patch is not metal, and the E057 interceptor's colors/chained tires and a bonus's hypothetical mounted gun do **not** describe Fate 4. Consult the linked audit for exact evidence rather than reusing these facts for other vehicles.

## C. Build appearance states and design constraints

Follow the subject template; retain existing IDs, evidence and historical decisions.

1. Create a concise **recognition baseline** covering defining silhouette, proportions, motifs, intrinsic colors/materials and source-supported distinctive features. Mark unspecified features openly.
2. Define stable, campaign-qualified state IDs (`<SUBJECT-ID>-A01`, `A02`, etc.) for genuinely distinct appearances: introduction, origin revealed later, equipment change, major injury, disguise, repair, destruction, restoration, and other supported transformations. Track **when true in story** separately from **when learned**. Use `start unknown` and `end unresearched` rather than stretching a state across unknown periods.
3. For each state write a **complete drawable description**, baseline and deltas, colors/materials versus lighting, scale/orientation (left/right from subject perspective), visible accessories versus custody, required exclusions at that point, unknown choices and evidence IDs. Minor ephemeral changes may remain scene notes rather than new permanent states.
4. Separate supported facts (`S`) from creative gap-filling choices (`D`) and existing images/production references. A generated image never establishes source canon. Preserve prior choices, note when new evidence contradicts them, and list which earlier images/prompts need revision. **Owner-approved** requires actual approval. For each meaningful visual discovery, perform the mandatory existing-image impact scan in section D; a note buried in prose is not a persisted revision flag.
5. Subject checks: characters—face, age/build, expression, clothing, wounds and worn gear; creatures—individual versus species anatomy, scale and movement; places—geography, landmarks, architecture, spatial relationships and temporal condition; items/vehicles—construction, openings, scale, mechanisms and repairs; events—exact moment, participants and each one's applicable state, location and spoiler cutoff; factions—insignia versus non-universal clothing.
6. **Recurring characters:** Decide whether this identifiable character already appears, or is reasonably expected to appear, in at least two project illustrations. Record the basis; do not presume a one-off is recurring without reason. For recurring characters, include a *draw-ready written design-sheet brief* linked to the approved-sheet registry: earliest supported baseline state; full-body front/profile/back, characteristic silhouette, facial structure and expressions, build, visible dress/gear, intrinsic palette, markings and subject-side asymmetry; explicit source-vs-artistic decisions; and source-backed chronology of later variants. Refer to player/creator artwork as intent with its provenance and time limits. Use final-campaign JSON only for late-state evidence or research leads. This brief is not an image or owner approval.

### C1. Sheet-first handoff for recurring characters

Research creates **the written specification** for a recurring character,
not an illustrated design sheet. Consult and update the subject's entry in
[ILLUSTRATION_CHARACTER_DESIGN_SHEETS.md](../../../project/ILLUSTRATION_CHARACTER_DESIGN_SHEETS.md):
`research-blocked` when key features/states are unsupported, or
`sheet-needed` when enough research is integrated to start a provisional
baseline sheet. Link any pre-existing sheet candidate and state IDs; do not
claim it is owner-approved merely because it exists or a player drew it.
Research clearance permits a **design-sheet draft** under the generation
skill, not a scene illustration of a recurring character. Scene work must
await explicit sheet approval, with separate state-variant coverage.

When new material contradicts a sheet or existing scene, add the actual
**impacted image IDs** to the existing-art review process in section D.
Do not label a legitimate evolution (scar, gear, disguise, etc.) an error.
Never automatically redraw or replace the sheet. Preserve both underlying
show evidence and the original artistic decision/version.

## D. Check existing illustrations and flag revision impacts

**Mandatory visual-impact pass after every new or corrected material finding,
even if no new image is being requested.** Inspect the subject's image
inventory, selected world-page depictions, earlier draft/selected/superseded
images, actual image pixels when accessible, and illustrations in which
the entity appears beside other researched subjects. Compare the new
information against **each image's story-time state and visible composition**
rather than the source's recording/publishing date or the object's last
known form. Separate stable traits from worn gear, temporary appearance,
damage, repairs, lighting, location, and changes in viewpoint. A new
historical revelation may require re-evaluating an image from an earlier
episode; it is not automatically a later physical change.

For each potentially affected image decide: **unchanged**, **review
needed**, **correction/edit candidate**, **regeneration recommended**, or
**already superseded**. Do not call an image inconsistent if it legitimately
depicts a different time/location or if the newly discovered detail would
not be visible. Log uncertain leads as `investigate`, never as a confirmed
error. Distinguish source role and actual verification (e.g. ASR-only,
creator handout actually seen, direct image pixel review, audio listened).
Existing owner-selected art is still subject to review if new evidence
conflicts with it; selection is not canon proof.

When a concrete mismatch or relevant new context is found, **create or
update an `IRV-####` item in**
[ILLUSTRATION_REVISION_QUEUE.md](../../../project/ILLUSTRATION_REVISION_QUEUE.md).
Deduplicate by **image ID(s) + issue/feature + affected story state**, record
source links/evidence, date, confidence, severity, image version/selection
status, affected region, expected versus depicted detail, proposed action
(review, edit, regenerate, annotate or archive), and follow-up/owner
decision. Cross-link every affected image's production/subject record
and preserve the old image. **Never automatically regenerate, overwrite,
replace links, revoke an approval or close a flag.** If essential
appearance evidence itself is missing, also record an independent `IRQ-`
research blocker; the two queues answer different questions. If writing
a flag fails, report it as unsaved instead of implying it was persisted.

The original Fate 4 style trials are a worked case: the pre-audit E006
studies omitted defining skull/solar details; they are already
superseded and require a documented **no-reuse flag**, not automatic
regeneration. An E001 construction image lacking those same later
fittings would **not** be in error merely because an E006 study needs
them.

## E. Persist audit and active appearance reference

For a substantial search, publish a dated `reports/ILLUSTRATION_<CAMPAIGN>_<ENTITY>_AUDIT_<date>.md` with scope and pinned source identities, search methodology, **files screened versus passages read/listened**, grouped evidence, state chronology, rejected leads, unresolved contradictions, image provenance and explicit next checks. Link any machine-readable search manifest.

**Mandatory integration gate:** update `project/ILLUSTRATION_REFERENCES.md` or an indexed dedicated subject file with the evidence IDs, recognition baseline, complete supported states, conflicts, artistic decisions, existing illustration impact list and change log. For recurring characters, also integrate the **design-sheet brief**, sheet registry link/status and relevant state variants; research completion is **not** sheet approval. The search report alone is **not** an integrated/finished reference. Preserve pre-existing state IDs and records; fix relevant source mistakes in separately bounded edits or log a precise correction task if unsafe to do now.

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

## F. Targeted validation and outcome

Read back edited sections, inspect final Git status and ensure no original source media/SRT was changed. Check stable IDs, story-state boundaries, evidence role versus verification wording, real relative links, register index and Markdown tables. Where a suitable project runner exists, lint **only changed maintained Markdown**, for example `npm run lint:markdown -- --files <changed-paths>`. Run only relevant tests; report editorial verification and automated checks independently as **passed / failed / not run**, without invented success claims. Do not run InfinityDB-only check tools against this repository. Do not silently commit, push or overwrite unrelated edits.

Report: entity/campaign; source ref; recurring-character status and written design-sheet readiness/approval gap where applicable; available character-sheet JSON files actually examined (or access gap), candidate cross-entity spellings/references with terminal-state labels, screened versus context-read versus listened coverage; strongest drawable requirements and changes; files written; active register integrated or pending; existing illustrations checked and any persisted `IRV-####` flags (or explicitly none); remaining contradictions and exact next check. An incomplete session ends with a durable phase checkpoint if writing is supported, not a claim of full research.
