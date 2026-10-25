# Illustration subject-reference template

**Purpose:** Copy the subject section below into
[the appearance register](ILLUSTRATION_REFERENCES.md), or a separately linked
subject file when the record grows. Replace placeholders with supported
information; mark unknowns explicitly and omit irrelevant fields.

Use [the illustration guide](ILLUSTRATION_GUIDE.md) for the shared visual
style. These are production records outside the in-universe world articles;
episode references and uncertainty belong here.

## Subject: <campaign and name>

| Field | Entry |
| --- | --- |
| Subject ID | <campaign-qualified stable ID> |
| Kind | <character, creature, place, item, vehicle, event, other> |
| Canonical reference | <relative link to subject page or category index> |
| Aliases | <source-supported aliases; do not merge uncertain identities> |
| Record version / updated | <version and date> |
| Researched scope | <episodes/scenes actually reviewed; identify gaps> |
| Record status | <evidence-only, working design, selected reference, superseded> |
| Art-direction version | <guide version> |
| Review basis | <sources read/viewed/listened to; existing reports reused> |
| Last applicable state | <state ID and story cutoff, or unknown> |

### Recognition and stable features

Write a concise, drawable description of the subject's defining silhouette,
proportions, visible features, material character and distinctive motifs.
Identify which features are stable only within a particular form or era.

| Feature | Description | Evidence IDs | Status / limits |
| --- | --- | --- | --- |
| <feature> | <specific visual instruction or unknown> | <source IDs> | <supported, claim, inference, artistic choice; verification limits> |

### Appearance-state timeline

| State ID | Applies in story | First description / later revelation | Change and boundary | Evidence |
| --- | --- | --- | --- | --- |
| <campaign-subject-A01> | <scene/interval; unknown boundaries explicit> | <episode/time and source role> | <baseline, temporary state, transformation, restoration, etc.> | <source IDs> |

State IDs remain stable when a boundary is corrected. Record that correction
in the change log; do not erase the earlier evidence. Release order and
story time may differ.

### State: <state ID and descriptive label>

- **Applicable scene/interval:** <supported start/end and excluded eras>.
- **Baseline and differences:** <named baseline, additions, removals,
  replacements, damage, repairs or temporary effects>.
- **Complete drawable description:** <standalone description including
  relevant stable features; do not rely on unexplained "same as before">.
- **Colors and materials:** <intrinsic colors versus scene illumination;
  identify required hues and open design choices>.
- **Scale and orientation:** <known measurements/relative sizes, uncertain
  dimensions, left/right and spatial relationships>.
- **Visible equipment / custody / condition:** <distinguish ownership,
  availability and what is actually in the scene>.
- **Must preserve:** <identity features and era-specific requirements>.
- **Must not appear yet / no longer present:** <source-supported exclusions>.
- **Unknowns:** <details requiring evidence or an explicitly artistic choice>.
- **Supporting evidence:** <source IDs and role/confidence limitations>.
- **Selected reference images:** <links/IDs, exact applicable state,
  reference scope, selection status and approval attribution if any>.
- **Visual continuity with earlier illustrations:** <which actual images
  have been inspected, persistent traits to retain, relevant source-supported
  differences for this state, and details to exclude/revert>.

Repeat this state section only for genuinely distinct appearances. Track
small scene-specific variations without manufacturing new permanent states.

### Evidence register

| ID | Supported visual detail | Exact source and locator | Role | Verification and temporal limits |
| --- | --- | --- | --- | --- |
| <S01> | <what this source actually supports> | <episode/dossier, source filename/version, approximate time or cues, handout/page/image as applicable> | <played scene, GM/cast commentary, character claim, creator document, fan art, etc.> | <audio listened to? image viewed? inherited report only? exact era? conflict?> |

Link the original source where available and identify any reliance on a
prior dossier or report. Do not fabricate cue numbers, source versions or
exact timestamps. A handout's observed date is not its fictional-era date.
If citing **D&D Beyond character-sheet JSON**, label it
`final-sheet-snapshot` / `campaign_end`, with source filename,
JSON path and optional hash. Record its actual character-specific
text versus generic rules-library definitions. It may support a
**terminal appearance or candidate spelling**, not when an item was
acquired, a location visited, an NPC first met or an early outfit worn.

### Character-sheet cross-entity leads (when applicable)

| Sheet / JSON field | Referenced character, NPC, item or place | Sheet-time evidence | Needed story-time corroboration | Disposition |
| --- | --- | --- | --- | --- |
| <sources/json/file.json, JSON path, optional hash> | <name, candidate alias and entity type> | <final-campaign reference only; custom entry/inventory/other> | <episode scene or creator source to locate; no retroactive assumption> | <candidate, supported in specific era, rejected, unresolved> |

Include only relevant **campaign-specific** leads from the subject's
campaign. Do not replicate complete JSON payloads, boilerplate, account
identifiers or late-campaign spoilers in early reader-facing content.
A terminal sheet can suggest where to look, but is not a visual
timeline; preserve source-specific spelling and status rather than
silently converting all references to accepted canon.

### Artistic decisions

| ID | Open feature and chosen treatment | Applies to | Status / rationale | Date and revision |
| --- | --- | --- | --- | --- |
| <D01> | <feature absent from known descriptions; proposed visual choice> | <state(s) or illustration> | <proposed, selected working choice, owner-approved, superseded; supporting references if any> | <date and record version> |

Do not record a source-established feature as an artistic decision. If
later evidence contradicts a choice, retain the historical entry, revise
the active design and identify affected illustrations.

### Conflicts and unresolved questions

| Question | Conflicting or missing evidence | Treatment for now | Next bounded check |
| --- | --- | --- | --- |
| <question> | <source IDs and exact difference or gap> | <omit, leave open, provisional rendering, label subjective> | <specific passage/image or research task> |

### Recurring-character design sheet (when applicable)

For named characters recurring or expected to appear in at least two
illustrations, link the [design-sheet approval ledger](ILLUSTRATION_CHARACTER_DESIGN_SHEETS.md).
Research documents the **introduction-era written design brief**, while
sheet imagery and owner approval are separate generation/review steps. No
new scene/portrait/group illustration of a recurring character may bypass
this gate, even when the evidence record is drawable.

| Field | Record |
| --- | --- |
| Recurrence | <recurring, expected across multiple pictures, or genuinely one-off; basis> |
| Baseline design brief | <supported era/state ID, silhouette, front/profile/back, anatomy, face and expressions, posture, orientation> |
| Clothes, props and palette | <visible outfit and equipment for baseline state; intrinsic colors and materials; explicit artistic decisions> |
| Source vs interpretation | <evidence IDs and verification; creator/player intent, fan art and campaign-end JSON separately identified; unknowns/conflicts> |
| Sheet ID and version | <stable campaign-qualified DS identifier, version, story-state coverage> |
| Image / technical checks | <real verified PNG page paths, each 1024x1024 sRGB, style/source checks, actual visual inspection> |
| Approval / scope | <sheet-needed, research-blocked, drafting, awaiting-owner-review, owner-approved, revision-needed, superseded; explicit owner/date or none> |
| Variants and approved deltas | <linked state-specific pages/approved written changes, what to carry forward/change/exclude> |
| Previous art impact | <image IDs checked, IRV review flags and superseded designs if relevant> |

A player-created illustration is a *design-intent source*, not itself an
approved new project sheet. Approval is version- and state-specific and
must not be inferred from a separately selected world-page illustration.

### Existing-art continuity inventory

Before each new image, locate **all previous project illustrations of the
subject** across story states and inspect the actual images when accessible.
This is separate from deciding whether the subject is researched.

| Image ID / path | Depicted story state and location | Status and source role | Stable features to retain | State-specific details not transferable | Access / review |
| --- | --- | --- | --- | --- | --- |
| <existing asset ID and verified path> | <subject IDs, era, location state> | <owner-selected, approved model sheet, draft, fan/art reference, superseded> | <persistent recognized design> | <early/late equipment, damage, attire, environment> | <actually viewed? any restrictions or errors?> |

For each new illustration, document a **carry forward / change / exclude**
matrix based on the selected image lineage and the target appearance
state. Record the image references **actually supplied** to the generator,
not just the ones inspected or cited. Preserve prior files and IDs rather
than overwriting them. If critical selected art is inaccessible or
contradicts newly discovered evidence, resolve the blocker or record it
as an explicit open continuity issue; an old generated image is not
proof of canon.

### Illustration records

| ID / output | Scene and state IDs | Guide / subject versions | Prompt and reference record | Status / review |
| --- | --- | --- | --- | --- |
| <ID and real output link when created> | <exact event moment and state for every recurring subject> | <versions used> | <exact prompt/edit instructions and supplied image references, linked if long> | <draft, selected, revised, superseded; reviewer/date and remaining issues> |

Keep a source-evidence review distinct from a visual style review. No image
is implied to exist merely because a prompt or planned filename is listed.

### Existing-illustration revision flags

Whenever new evidence, contextual understanding, or an image comparison
reveals a potentially inaccurate **existing illustration**, make or
update the corresponding entry in
[ILLUSTRATION_REVISION_QUEUE.md](ILLUSTRATION_REVISION_QUEUE.md). Keep the
actual asset unchanged pending the appropriate review. Refer to the
depicted **story-time state**, not merely the latest known character or
item appearance. An artistic design choice contradicted by newer research
is reviewable even when the old illustration was selected.

| IRV issue | Affected image/version and depicted state | Finding, confidence and evidence | Proposed action / owner decision | Resolution or replacement |
| --- | --- | --- | --- | --- |
| <IRV-#### link> | <image ID/path; subject and location states> | <what changes in understanding, actual pixels inspected or not> | <review/edit/regenerate/annotate/no-reuse and decision status> | <open, approved exception or new asset ID> |

If source research needed to decide the issue is still missing, link
a separate `IRQ-` entry. These two queues are distinct, and resolution
of the research question does not silently approve a new illustration.
Preserve the original image ID, owner selection and provenance history.

### Change log

| Date / version | Change | Evidence or artistic basis | Affected states / illustrations |
| --- | --- | --- | --- |
| <date / version> | <new detail, corrected boundary or changed choice> | <source IDs or design decision> | <IDs, including images needing revision> |
