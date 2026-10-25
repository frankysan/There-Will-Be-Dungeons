# Illustration revision and consistency queue

**Established:** 2026-10-25. **Purpose:** Durable, cross-subject review of
**existing TWBD illustrations** that may be visually inconsistent, no longer
source-faithful, or outdated by newly researched context. This is distinct
from [the illustration research queue](ILLUSTRATION_RESEARCH_QUEUE.md), which
blocks **new generation because an entity/state lacks enough research**.
Both [entity research](../.agents/skills/twbd-illustration-research/SKILL.md)
and [illustration generation](../.agents/skills/twbd-illustration-generate/SKILL.md)
must consult and maintain this queue.

[Style and continuity guide](ILLUSTRATION_GUIDE.md) ·
[appearance register](ILLUSTRATION_REFERENCES.md) ·
[subject template](ILLUSTRATION_SUBJECT_TEMPLATE.md).

## Flagging contract

On each meaningful **new visual finding** (including research discoveries,
newly interpreted chronological/contextual evidence, creator references,
and corrected descriptions) or **new image comparison**, identify which
previously created illustrations may be affected. Search the relevant
subject records, image IDs, production inventory, illustrations directory,
world-page embeds and other recognizable entities/locations in those
compositions. Cross-reference the images' **own depicted story states**,
not the date the image was generated or the later episode that revealed an
earlier feature. A newly discovered fact about the E006 unveiling can
invalidate an E006 image even if the source was found years later.

Flag only a specific **evidence-supported discrepancy**, a plausible
**review-needed uncertainty** tied to actual new context, or a verifiable
**production/style issue**. Differences legitimately caused by age,
costume, injury, transformation, temporary effect, damage, repair,
lighting, viewpoint, atmosphere or **story/location time** are **not**
automatically inconsistencies. A source-verified color/silhouette feature
and a previously owner-selected but unsupported artistic choice have
different authority. Earlier generated art, fan art and source handouts
are not new transcript evidence.

**Both skills must write an issue even when the existing illustration
was once selected/approved.** Selection affects the approval workflow,
not the correctness of source evidence. Never silently delete, overwrite,
replace, unpublish or regenerate selected images, change image links,
declare an issue resolved or revoke owner approval. Preserve original
asset IDs, version history and provenance. Owner-directed replacement or
approval is handled separately.

## Classification and impact

Use these fields on every real item:

- **Finding type:** `source-contradiction`, `new-context`,
  `state-placement`, `visual-lineage`, `style-or-dimensions`,
  or `asset-provenance`. Use a concrete explanation, not just the label.
- **Evidence confidence:** `confirmed` (directly checked source/image
  and applicable state), `provisional` (e.g. ASR-only or inherited audit),
  or `investigate` (plausible signal, not yet checked). Record separately
  what was **actually viewed/listened to**. Do not classify an ASR
  transcript as audio-verified.
- **Severity:** `critical` (wrong entity, timeline, or major defining
  feature that makes the scene misleading); `major` (material
  mismatch in character/setting, equipment, repairs or proportions);
  `minor` (local detail or limited style drift); `informational`
  (new supporting context requiring no apparent visual change).
- **Status:** `needs-review`, `needs-research`,
  `regeneration-recommended`, `edit-recommended`,
  `accepted-exception`, `resolved`, or `closed-superseded`.
  A finding should not be marked confirmed merely because a reviewer
  recommended regeneration.
- **Recommended action:** `review-only`, `edit`, `regenerate`,
  `annotate`, `archive/no-reuse`, or `no-change`, with rationale
  and explicit decision state. A minor contextual addition need not
  trigger full regeneration.

Track the **affected image ID(s) and exact paths**, their status (draft,
selected, owner-approved, superseded), depicted campaign/subject/state(s),
scene and location, and whether the discrepancy actually appears in frame.
A fact about the inside of a vehicle does **not** invalidate an exterior
drawing when the interior is not visible. Describe the old depicted feature,
the new supported requirement, scene applicability, affected regions, and
what must remain consistent with other versions. Include linked evidence,
source version/time/role, discovered date and any relevant unresolved
alternative explanation.

## Create/update procedure for both skills

1. **Before writing:** Read the open and closed ledgers plus the subject's
   illustration records; identify the actual asset(s), their depiction
   states, selection status and any existing issue. Do not claim to have
   inspected pixels when only Markdown references were read.
2. **Deduplicate:** Use a stable ID `IRV-0001`, `IRV-0002`, …,
   and match **affected image ID or image group + issue/feature +
   applicable scene/state**. One issue may list multiple images affected
   by the *same* finding, but track each separately if correction needs,
   priority or review outcome differ. Append new evidence/history to the
   same issue instead of creating redundant flags.
3. **Record the problem and the next action:** Use the entry template
   below. Separate what is established from an artistic preference,
   what can safely be carried forward, and what needs a new render.
   **Flag first; do not automatically generate or edit.**
4. **Cross-link:** Add a concise dated flag with the `IRV-` ID to each
   affected image's production/subject reference record. Link the queue,
   note impact on the affected state, and preserve old selected image
   versions. If a source finding affects several subject images, inspect
   all pertinent records.
5. **Generation gate:** When creating new art, inspect all **open**
   flags on selected visual anchors. Do not copy flagged details. Reuse
   unaffected features if the scene is sufficiently researched. If the
   flagged contradiction makes a subject's required target depiction
   underspecified, open/update the separate `IRQ-` research blocker
   and **stop generation** until that source question is resolved.
   Do not conflate a request to review existing art with a blanket block
   on unrelated illustration work.
6. **Resolution:** After researched correction or owner decision,
   retain the previous asset, record replacement/edit image ID and
   path (if any), visual/source review results, and exact owner action
   if applicable. A generated candidate is not automatically the new
   selected image. Mark `resolved` only after the appropriate change,
   annotation or accepted exception is verified; if superseded work
   was already excluded from use, `closed-superseded` can be appropriate.
   Never retroactively erase the discrepancy.

If the ledger or links cannot be written, report the **unsaved flag and
affected image** explicitly; do not falsely say it was recorded. A failed
queue write does not authorize modifying or silently using flawed art.

## Open illustration findings

*No open entries yet; add a real item only when supported by evidence or
a concrete visual-continuity review.*

<!-- Real entry structure; use next unused IRV-####.
### IRV-XXXX — <short problem / subject and state>
- **Status / severity / type:** needs-review | major | new-context
- **Opened / updated:** YYYY-MM-DD
- **Campaign / subject(s) / state(s):** IDs and scene/location time
- **Affected image(s):** ID; repository path; selected/draft/approved status
- **Visible issue:** specifically what appears or is omitted in the frame
- **Source and verification:** evidence references, episode/clock/version;
  actual pixels viewed? audio listened? confidence provisional/confirmed?
- **Applicability and exceptions:** why the issue affects this state;
  alternative interpretation; expected era/location differences
- **Action:** review-only | edit | regenerate | annotate | archive/no-reuse
- **Carry / change / exclude:** stable features versus needed correction
- **Owner action / decision:** pending, or exact explicit approval
- **Research dependency:** IRQ-#### if source is insufficient, else none
- **Resolution / replacement:** pending, or old/new image IDs and links
- **History:** dated evidence, review, updates, recheck results
-->

## Closed and superseded findings

### IRV-0001 — Fate 4 early style previews lack defining unveiling features

- **Status / severity / type:** `closed-superseded` / `major` /
  `source-contradiction`.
- **Opened / updated:** 2026-10-25.
- **Campaign / subject(s) / state(s):** Wastes / `WASTES-FATE4`, original
  introduction `WASTES-FATE4-A01` at the E006 unveiling.
- **Affected image(s):** `WASTES-FATE4-STYLE-001-A` and
  `WASTES-FATE4-STYLE-001-B`; earlier **unselected style trials**, not
  owner-selected production models. Their precise repository image paths
  are not established by this ledger; see the
  [style study](../reports/ILLUSTRATION_STYLE_STUDY_2026-10-25.md)
  and [subject reference](ILLUSTRATION_FATE4_REFERENCE.md).
- **Visible issue:** Earlier documented style previews omitted the
  E006-defining **metal dragon-skull front and solar panels**, and did not
  correctly convey the purposeful exterior combat handholds.
- **Source and verification:** [E006-based Fate 4 audit](../reports/FATE_4_TRANSCRIPT_AUDIT_2026-10-25.md)
  and [active appearance reference](ILLUSTRATION_FATE4_REFERENCE.md).
  This initial queue entry records a **prior written visual comparison**;
  the actual pixels were **not independently reopened** when this ledger
  was created. Spoken details are ASR-supported, **not audio-verified**;
  treat the comparison's confidence as `provisional`.
- **Applicability and exceptions:** These exclusions are wrong for the
  completed E006 A01 state, but need not apply to the unfinished E001
  vehicle A00A. Do not backdate completed fittings into construction.
- **Action:** `archive/no-reuse`; no regeneration required for already
  superseded experimental trials unless a future request specifically
  selects or restores them.
- **Carry / change / exclude:** Style trial may inform linework exploration;
  complete E006 model must add the researched front/roof/rails. Do not
  treat trial paint as established canon.
- **Owner action / decision:** Neither early image was selected; the owner
  later selected a different [E006 scene depiction](../world/technology/fate-4.md).
  This does **not** establish approval of exact vehicle geometry.
- **Research dependency:** None for this already documented issue.
- **Resolution / replacement:** **Closed as superseded**, not silently
  repaired. Later page image `WASTES-FATE4-ILL-001` is a distinct
  owner-selected scene, not an edited copy of the early previews.
- **History:** 2026-10-25 — inconsistency previously noted in subject
  documentation; indexed here for future visual-impact checks. No
  new image generated, overwritten or automatically selected.

