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

*No open illustration issues remain as of the owner-confirmed Hope E001 labeling correction on 2026-10-26.*

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

### IRV-0004 — Stanley E001 anatomical profile filenames reversed

- **Status / severity / type:** `resolved` / `minor` / `visual-lineage` (incorrect anatomical labels and filenames; no pixel or character-design change).
- **Opened and resolved:** 2026-10-26, following direct user request to apply the same left/right naming correction made for Hope Akmenos.
- **Campaign / subject / state:** The Wastes, `WASTES-STANLEY-BILLINGS-A01`, sheet `WASTES-STANLEY-BILLINGS-DS-001`.
- **Affected assets:** Owner-approved paired PNG `wastes_stanley-billings_e001_side-paired_v01.png`; two mislabeled extracted v1 files; associated four-view sheet `wastes_stanley-billings_e001_sheet-01-turnaround_v01.png`; written side/assembly metadata. Original binaries all preserved.
- **Cause:** Legacy turnaround instructions incorrectly labeled the figure facing image-right (→) as anatomical LEFT and figure facing image-left (←) as anatomical RIGHT. Correct orientations are the reverse: **viewer-left figure = anatomical RIGHT**, **viewer-right figure = anatomical LEFT**.
- **Resolution:** Created two additional **byte-identical** correctly named v2 PNGs **in the repository**, verified by original/new binary readback: `wastes_stanley-billings_e001_side-right_v02.png` = historical `Left_Side_v1` (574,210 bytes, SHA-256 `c685ace99abf4e51fbae4b77d887dab8de8a9835d51e4f64de95c679f57c14eb`), `wastes_stanley-billings_e001_side-left_v02.png` = historical `Right_Side_v1` (548,196 bytes, SHA-256 `09f65c7e94b15c4e671093ebc00f3f5325341399a94760fb0a84f58552c2b4fe`). Both preserve the previous 1024-square RGB PNG and sRGB ICC tagging.
- **Impact / approval:** No mirroring, resizing, redrawing, reassembly, or new sheet visual approval required. The prior `SIDE_APPROVED` stays valid for the same images. The previously approved E001 four-view composite remains byte-identical; its panel-side descriptions have been corrected in the written records. This issue does not itself change the separate full-sheet registration/approval state.
- **Provenance and exact checks:** [2026-10-26 correction report](../reports/ILLUSTRATION_STANLEY_E001_SIDE_LATERALITY_CORRECTION_2026-10-26.md), [historical approval with corrigendum](../reports/ILLUSTRATION_STANLEY_E001_SIDE_APPROVAL_2026-10-25.md) and [sheet manifest](../illustrations/references/wastes_stanley-billings_e001_manifest.json).


### IRV-0003 — Hope E001 side views: anatomical LEFT/RIGHT filenames reversed (not a holster error)

- **Status / type:** `resolved` / `visual-lineage` (naming/metadata only; alleged image-content defect **disproven**).
- **Opened:** 2026-10-25; **resolved by owner clarification:** 2026-10-26.
- **Subject:** The Wastes, `WASTES-HOPE-AKMENOS-A01` / `WASTES-HOPE-AKMENOS-DS-001`.
- **Historical concern:** Prior audit incorrectly said the tool holster moved from Hope's anatomical right hip to her left between front/back and a side view. The initial paired render `4b05d728-921f-4fdf-bba7-33fbc12db0d9` and split 1024-square derivatives were owner-visually-accepted; none were repository-registered.
- **Confirmed resolution:** The owner states that the holster is correctly located on **Hope's anatomical RIGHT hip in all images**. The *file names*, not the art, were reversed: profile facing right (→), holster near-visible, depicts anatomical **RIGHT**, and the profile facing left (←) depicts anatomical **LEFT**. The earlier generic generation templates had this directional convention reversed as well.
- **Action:** Preserve source art and all historical original files and hashes; **do not** mirror, regenerate or swap the two image contents. Versioned corrected split filenames were created non-destructively as `wastes_hope-akmenos_e001_side-right_v02.png` (byte-identical to formerly named `Side_Left_v1`, SHA-256 `0bcb718afb0c25ea771fd44b3484f6e1226e2e23d1bd88204709c75eacb58212`) and `wastes_hope-akmenos_e001_side-left_v02.png` (byte-identical to formerly named `Side_Right_v1`, SHA-256 `dfa8d85404a930338ad9c3231d3e1ef6a0917612833dbe916ea8ee6f838b1c8c`). All are session files; no repository PNG registration is implied.
- **Assembled sheet effect:** No redraw or reassembly required. Page 2 remains anatomically **RIGHT on left panel**, **LEFT on right panel**. Three page images and their existing hashes are unchanged; correct the companion written specification and machine manifest only. The pending separate final-sheet owner review and repository-readback gates remain.
- **Prevention:** Corrected [side-profile orientation convention](../.agents/skills/twbd-illustration-generate/CHARACTER_SHEET.md) and [reusable paired-side prompt](../.agents/skills/twbd-illustration-generate/CHARACTER_SHEET_PROMPTS.md). Historical other-character left/right filename conventions should be individually verified, not silently assumed.
- **Evidence:** Explicit owner correction in chat (2026-10-26) plus previously inspected source PNGs. [Side technical report](../reports/ILLUSTRATION_HOPE_E001_SIDE_TECHNICAL_GATE_2026-10-25.md); [assembly report](../reports/ILLUSTRATION_HOPE_E001_SHEET_ASSEMBLY_2026-10-26.md).


### IRV-0002 — E001 Dusthill aerial versus newly found map

- **Status / severity / type:** `closed-superseded` / `major` / `new-context` (older first aerial only); its original map comparison remains provisional, but its incorrect 1672 × 941 canvas is confirmed.
- **Date:** 2026-10-25.
- **Subject/state:** The Wastes, `WASTES-DUSTHILL-A01` opening settlement.
- **Affected image:** Owner-selected generated aerial view, `gen_id=5549267f-4eb6-4d62-aa21-d5897f33e272`; not yet stored in the repository or embedded in its world page. **Technical production issue (2026-10-25):** The generation output metadata reports **1672 × 941**, a landscape aspect ratio that **fails** the mandatory `1024 × 1024`, square PNG production gate regardless of map fidelity. Preserve the owner's selection history, but do **not** publish or classify this source render as a conforming project asset unless it is safely recomposed/normalized to square and the final PNG/sRGB bytes are verified.
- **Observed issue:** Illustration represents hidden red-rock village, huts, water outlet and cave farms, but omits a clearly distinct gathering circle and other mapped locations (school, Hillmaster hut, barracks, trading post), while positions of farms and garage are interpretive.
- **Evidence:** Direct pixel inspection of `local/images-wiki/maps/Dusthill.webp` (formerly `DVJ4V1JVwAErBl-.webp`), SHA-256 `141731587b065a5271a6814c2d1cfd264f8b8a0a86b3fdbe41219266ef7bc5ce`; [revised subject reference](ILLUSTRATION_DUSTHILL_REFERENCE.md#newly-inspected-dusthill-plan-2026-10-25). Map provenance/era and scale unverified. On 2026-10-25 the project owner recalled that it probably originated with the GM but could not confirm authorship (`owner-recollection`, not a verified credit); E001 geography ASR-based, audio not listened.
- **Applicability:** Map may show another era or schematic approximation; aerial view cannot depict every detail. This is **not a confirmed contradiction**.
- **Action:** The owner requested and selected a new map-informed E001 aerial. Preserve the older source image and IRV history; do not reuse the old non-square render. Map date/provenance research remains outstanding and applies independently to the *new* selected interpretation.
- **Owner action:** After pausing the first image for map research, the owner requested a replacement E001 aerial and expressly selected it for Dusthill's `/world` page on 2026-10-25. New image working ID: `WASTES-DUSTHILL-ILL-001`, generation `e373f801-a918-41cc-aa32-e42323be4900`.
- **Resolution:** **Closed as superseded**, not corrected in place. Replacement `WASTES-DUSTHILL-ILL-001` (`illustrations/wastes/dusthill-e001-aerial-establishing.png`) was verified in the connected repository with exact SHA-256 `9b978f2c3fb02598279656baef39e7bb3d7bdfc5efa7163de536480aa60e71bf`, PNG dimensions 1024 × 1024, and an embedded ICC profile, then linked on `world/places/dusthill.md` with a provenance note. The first landscape image remains superseded; neither map-authorship verification nor hosted deployment is implied.
- **History:** 2026-10-25 — added on direct map inspection; later that day the user selected a map-informed replacement. Old image retained as superseded; no automatic file overwrite.

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

