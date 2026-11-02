---
name: twbd-wastes-cleanup
description: Execute the indexed WCL task register for The Wastes cleanup, selecting dependency-safe groups of related unfinished tasks through adaptive context, source, and verification budgeting. Check off each task independently with recoverable evidence; keep other project records concise. Use for Wastes narrative, world, reference and integration cleanup; not routine episode intake or other campaigns.
---

# Wastes campaign cleanup

Carry out the repository's cleanup plan one recoverable slice at a time. Creating
this skill does not execute the cleanup. When invoked to work, complete the next
eligible slice and document it within the user's requested scope. A request to
resume means reconcile persisted work before doing more.

## Repository and authority

Use the current checkout if it contains `project/WASTES_CAMPAIGN_CLEANUP_PLAN.md`.
The usual checkout is
`C:/Users/Franky/Documents/GitHub/There Will Be Dungeons Transcripts`.
Resolve repository paths below against that root; never write progress into the
installed skill folder. Read applicable `AGENTS.md` and included instructions.
Here shell commands use `rtk`; use `rtk proxy` for unsupported executables.
PowerShell cmdlets require `powershell -NoProfile -Command`, not direct execution
through `rtk proxy`.

At first use read the current controlling documents:

- `project/WASTES_CLEANUP_TASKS.md`: **the sole authoritative indexed checkbox task list, task states and next action**.
- `project/WASTES_CAMPAIGN_CLEANUP_PLAN.md`: historic scope, phases and acceptance gates.
- `project/WASTES_CLEANUP_MANIFEST.md`: **artifact dispositions and compatibility only**, not task status.
- `project/WASTES_CLEANUP_CHANGELOG.md`: significant milestones/decisions only, not batch recaps.
- `project/WASTES_NARRATIVE_CHAPTER_MAPS.md`: proposed crosswalk and exceptions.
- `project/DECISIONS.md`: applicable accepted/superseding decisions, especially
  D-037–D-044 and later Wastes cleanup decisions.

For earlier page work consult `project/WORLD_ARC_CLEANUP_PLAN.md` and
`project/WORLD_ARC_MIGRATION_MANIFEST.md`. Their Season One limits, counts and
next pointers are historical; preserve useful archival/style rules without
imposing obsolete scope on the completed campaign. Follow later explicit owner
decisions; do not silently resolve a genuine conflict by choosing a convenient
plan paragraph. The Delvers cleanup manifest is a method example, not canon.

For prose read `project/EDITORIAL_GUIDE.md`,
`project/WORLD_NARRATIVE_STYLE.md` and
`project/WORLD_REFERENCE_PAGE_TEMPLATE.md`. For taxonomy also read
`project/WORLD_CREATURES_PLAN.md` and `world/ENTITY_SCHEMA.md`.

## Select work from the WCL task register

Read [progress and recovery](references/progress-and-recovery.md) before
mutations. Follow D-052 backup/reporting economy. **The authoritative work
queue is `project/WASTES_CLEANUP_TASKS.md`, not numeric historical batches,
the old phase-plan "next" sentences, or manifest/changelog pointers.**

1. **Refresh live state and task statuses.** Inspect HEAD and working-tree
   changes, then read the task-register introduction, the explicit
   **Current next action**, the relevant WCL entries and their parent/child
   dependencies. Preserve other people's edits and reconcile incomplete work
   against actual bytes, checks, archives and source horizons. A timed-out
   operation has unknown outcome until read back.
2. **Establish the anchor task.** If the owner names a task, use that scope.
   Otherwise start from the register's current next actionable WCL ID, *not*
   the lowest-numbered unchecked entry: older tasks may be deliberately
   deferred, conditional, blocked or dependent on another review. If its
   status is stale, reconcile and correct the pointer with evidence; do not
   silently skip a genuinely blocked requested edit. A parent workstream is
   not independently complete while required children remain unchecked.
3. **Look ahead for related eligible tasks.** Inspect a small number of nearby
   child/sibling tasks and other open WCL IDs sharing the **same article,
   evidence windows, dependency chain or one coherent edit/validation pass**.
   Check that all have satisfied prerequisites, applicable authorization and
   individually testable acceptance criteria. Keep unrelated campaigns,
   approvals and contested canon decisions separate. Open inventory candidates
   are investigations, not automatic permission to author missing pages.
4. **Preflight cost before selecting a cohort.** Inspect metadata and small
   slices rather than loading all candidate articles and whole historical
   archives. Estimate unique source bytes/lines, primary episodes or evidence
   windows, files and incoming links to edit, expected output, validation
   effort, risk of conflicting work, and source/approval uncertainty. Use the
   **D-082 adaptive batching rules below**. Prefer the largest coherent,
   dependency-safe ordered cohort that can be fully reviewed and validated;
   retain a single focused task for genuinely dense or gated work. Do not group merely
   because several checkboxes are adjacent in the register.
5. **Execute in dependency order.** Keep an open task's requirements, selected
   paths, evidence and recovery checkpoint sufficiently detailed for safe
   continuation, without an extra batch journal. Perform bounded operations,
   readback and checks; mark each WCL independently only when its own scope
   passes. **At completion, compact its entry to one short outcome paragraph**
   retaining the checkbox, parent/dependencies, key evidence links and any
   essential limits. Detailed raw validation, source windows and hashes belong
   in source files, the per-file census, existing review records, the one-time
   major-rewrite archive and Git history—not repeated in every checked task.
   Never compact an incomplete task into a falsely resolved one. Recover the
   first unfinished action after interruption.
6. **Close and select the next task.** Reconcile the parent only when its
   defined exit gate and required children are evidenced. Set **Current next
   action** to the next eligible unchecked WCL ID based on dependencies and
   priority; this need not be numerically adjacent. Read back task changes
   and inspect Git status. Update the manifest only for actual file
   dispositions/compatibility, and the changelog only for meaningful
   milestones/decisions. Never maintain a parallel progress log.

### Adaptive, context-safe grouping of multiple WCL tasks (D-082)

**Default: select the largest coherent, dependency-safe cohort that can actually
finish and be validated.** Do not limit a normal interaction to four files or
one WCL task merely out of habit. Start from the authoritative next-action
WCL ID, preflight a small lookahead of eligible related tasks/paths, and
bundle their shared reads, edits and validation when the combined scope is
manageable. Every file retains its own source horizon and validation result;
every WCL checkbox retains its own acceptance gate. A larger invocation does
**not** make an incomplete task complete.

| Work type | Typical candidate group | Planning notes |
| --- | --- | --- |
| Short character, creature or technology profiles | **10–15 related files** | Usually uncomplicated structure; group by relationships and actual sizes |
| Medium reference/reader articles | **5–8 related files** | Favor a common source or link neighborhood |
| Large or dense source documents | **1–3 files** | Use numbered chunks and checkpoints; one very dense register may still stand alone |
| Compatible low-risk editorial WCL tasks | **Several tasks together** | Preserve substantive approvals, exact file ownership and independent acceptance |
| Blocked browser, disallowed tool, contested canon or unapproved task | **Do not combine to evade the gate** | Record the blocker; safely complete independent already authorized work only when it does not depend on the blocked action |

**Typical source-line envelope:** Aim for roughly **800–1,500 combined
source lines** on ordinary light-to-medium inventory cohorts *when practical*.
This is a guide to reduce repetitive overhead, not a target to pad: ten tiny
profiles may be 250 lines, and a single dense register may be 1,000 lines
read in chunks. Adapt downward for large paragraphs, many source claims,
many link targets/footnotes, rendering limits, slow tools, source ambiguity,
or overlapping work. Counts and line lengths are not a token meter.

**Preflight and processing budget:**

1. Inspect file metadata, actual line counts/bytes and a few introductory
   slices before committing to the cohort. Estimate the **union of new
   evidence**, expected link and footnote validation, output/result size,
   source provenance, prerequisites and approval risk. Record the **exact
   selected paths and WCL IDs** in their existing task/census records;
   an expandable anchor is not a license to check unseen files.
2. Work in **bounded waves** (usually 1–3 tool calls per wave, with compact
   in-tool summaries). Read full contents of each selected file in numbered
   chunks; do not forward all file bodies, full rendered HTML, raw diffs or
   archives into conversation context. Around **30,000 characters of dense
   source text in a single response** is a warning to reduce *that response
   or wave*, **not** a hard ceiling on the whole recoverably checkpointed
   cohort. Reserve capacity for interpretation, guarded changes and checks.
3. Capture one individually attributable record per file: current hash/size,
   fully read line coverage, source horizon and uncertainty, presentation
   classification, local-link and fragment validation limits, footnotes,
   image embeds, incoming examples and any failed/not-run checks. Keep
   working validation distinctions (renderer first-100, independent target
   existence, native-browser deferred) instead of promoting a partial check
   to a pass. Use the live census for file dispositions and the WCL task
   register for task completion; **no new batch report**.
4. Checkpoint finished **per-file evidence** incrementally so a stream error
   or oversized response never invalidates other finished work. Run scoped
   checks by file or small group; **update the task register once per
   coherent batch when possible**, checking off each independently
   completed WCL ID and advancing one next-action pointer. If an ID
   requires several files and only some pass, leave that checkbox open
   with a recoverable exact subset and blockers.
5. Reconsider group size after every checkpoint. Shrink, split or stop
   for tool safety restrictions, actual context pressure, mismatched source,
   missing authorization, incompatible edits or genuine canon ambiguity.
   Never circumvent a blocked tool with alternate instructions. Avoid
   repeatedly running whole-cohort final checks; verify only new or
   uncertain deltas and the aggregate census/task consistency at close.

The historical WCL-044–049 sequencing and old October 27 small-file pilot
remain examples of dependency and source caution, **not live numeric batch
limits**. This D-082 strategy changes execution economy, not D-048,
D-052, D-078, D-081, canonical/audio, public/private or Git permissions.

### Live multi-file audit selection (D-082 supersedes October 27 pilot)

For a structural read-only census, use the **larger adaptive cohorts above**
instead of the historical **4–8 short / 2–4 medium / 1–2 large files**
and **300–400 combined source lines**. That 2026-10-27 guidance and
Batch 15 pilot remain historical method evidence only. Start with the
controlling WCL anchor, then choose other **eligible, related, pending**
paths or WCL siblings after preflighting sizes, dependencies and source
density; do not automatically group by alphabetical adjacency. Name exact
chosen paths and WCL IDs before reading. When the anchor names four files,
all four remain required, but additional compatible paths may be included
under the owner-approved D-082 cohort procedure **after their scope is
explicitly recorded and their independent evidence will be retained**.

Use the current `project/WASTES_WORLD_FILE_CENSUS.json` as one per-path
evidence store, retaining current source hash, actual line coverage,
provenance, headings, incoming examples, footnotes/images, link and
fragment coverage, and distinct `queued | reading | complete | blocked |
unknown` verification states. Record renderer 100-link limits or safety
blocks exactly, rather than replacing them with file-existence passes.
If interrupted, retain completed per-file dispositions and resume only
the first unknown/pending record after rereading Git status. Check off a
WCL task only when **all of its selected required outputs** meet its
documented exit criteria; unfinished work stays open, even if another
WCL in the same invocation is completed. At cohort close, update the one
task-register next-action pointer and validate census counts/unique paths.
Do not generate an extra task journal, per-batch reports or redundant
snapshots.

**Fresh access preflight at every file-access batch:** Before the first read or
write of each bounded group of files, each resumed work slice and each batch
checkpoint, re-evaluate the complete `AGENTS.md` priority **from step 1**:
local filesystem → workspace MCP → GitHub → Git patch → ZIP. Select the first
currently viable, revision-correct method; stop checking lower-priority routes
once one can perform the operation. **Do this even when the prior batch succeeded
and nothing has failed.** Never carry forward an old MCP outage or access-denied
finding: if local files are unavailable, probe MCP again at the next batch so
service recovery is detected automatically.

**Required-write fallback:** On a failed task-register, required artifact-disposition, evidence or source
operation, inspect whether the operation partially persisted and **restart the
same full priority check at step 1**, rather than assuming a previously failed
route is still unavailable or silently omitting the write. Safely retry or use
the first viable route; do not overwrite newer local or uncommitted work with a
stale remote tree. Verify results and distinguish applied changes from Git
patches or ZIP bundles requiring manual application. If no method can apply a
required edit, retain an explicit reconciliation checkpoint and report it as
pending, never completed. All owner-approval gates still apply.

### Editorial autonomy and mandatory substantive owner-approval gate

**Owner clarification (D-047, 2026-10-28): Small edits and spelling changes do
not require individual approval.** Proceed autonomously with bounded,
unambiguous, non-substantive corrections in maintained editorial text: typos,
punctuation, grammar, clearly established canonical spellings (D-044), and
straightforward reader-facing labels. A batch of small independent fixes is
allowed; do not turn that into a broad unreviewed rewrite. Classify each
occurrence by referent, preserve old slugs, aliases, direct source quotations,
source-facing reports and raw ASR/audio, link targets, footnote IDs, provenance,
episode knowledge cutoffs and all evidentiary uncertainty. Before edits, check
live Git state and record exact paths/intent; preserve a full original **only before a major rewrite/restructure when a suitable baseline is not already held**. For minor edits, rely on guarded changes, Git diff and readback to validate actual deltas. Record the
standing owner permission as **D-047 / editorial-minor** rather than seeking
fresh approval for every obvious typo. Do not re-open completed historical
approval gates just because older reports still describe them.

**Substantive or ambiguous changes still require explicit owner approval:**
rewriting or relocating scenes, arc/file restructuring, new taxonomy, canon or
identity adjudication, disputed name referents, altered factual interpretation,
chronology, endings, source quotations, renamed files or link destinations,
deletions, and any correction that could change meaning or evidence status.
The general `$twbd-wastes-cleanup` invocation, a draft plan, a proposed
crosswalk, or the minor-edit permission does not authorize those changes.

If the next necessary edit **requires approval** and that approval is missing
or unclear, **STOP before editing that target and request the owner's
decision**, identifying affected files, proposed alternatives and evidence.
Record the blocker against the active WCL task; do not bypass a genuine
substantive gate by changing other content instead. Read-only investigation
to characterize the decision is allowed. Do not request approval again when
it is already recorded and applicable.

## Optional bounded reference diagnostics (WCL-115)

The repository provides a **read-only, heuristic** helper at
`tools/wastes_reference_diagnostics.py` with focused regression tests at
`tests/test_wastes_reference_diagnostics.py`. Run through the authorized
workspace `run_script` module `tools.wastes_reference_diagnostics` (or
`python -m tools.wastes_reference_diagnostics` locally), optionally selecting
`--domain world --domain narrative --domain wastes --max-links 18000`.
`--sample-per-kind` controls short actionable console samples; `--json`
provides structured findings and can exceed bounded remote output.

The tool checks **simple inline local Markdown links**, approximate heading
fragments, footnote reference/definition pairing, missing final-status headings,
curated canonical-spelling aliases and potential stale high-impact finale
assertions. It does not fully parse reference-style/nested Markdown, verify
external bookmarks, perform native GitHub/interactive click-through, listen to
audio or decide canon. Findings are **review candidates**, not automatic
corrections; historical six-word-form arc prose remains excluded from active
name warnings. The previously safety-restricted
`world/CONSISTENCY_LEDGER.md` and `world/characters/bok-bok.md` are expressly
**excluded from file-content scanning**, including fragment target reads; leave
their existing validation tasks blocked until legitimately authorized. Do not
use other scripts to circumvent these restrictions. Always retain normal
per-file renderer/lint/source validation and the WCL-103 browser gap. Route
meaningful corrections to their owning tasks (notably WCL-195/WCL-197 naming,
WCL-040 source claims, and WCL-116 disposition), without silently rewriting
historical or disputed evidence.

## Phases and exit evidence

Use the live campaign plan's phases and gates. Phase completion and individual
page lifecycle are separate; an accepted pilot does not complete its domain.

| Phase | Work and completion evidence |
| --- | --- |
| 0 — Detailed baseline | Enumerate current narrative/world files, Wastes episodes/navigation/controls, active policies and affected reports. Save scope, exclusions, sorted worklist and remaining paths before chunking. Capture working-copy hashes, headings, paragraphs, prose counts, notes, episode links, inbound links/anchors, aliases and coverage flags. Assess purpose, horizon, last actual observation, priority and treatment per file; mark unknowns explicitly. Reconcile earlier accepted pages individually. Close only after all in-scope files and semantic fields are accounted for. |
| 1 — Arc decision | The owner approved the eleven-arc episode-boundary crosswalk in D-045. Map existing paragraphs/scenes to the approved arcs, stress-test closures and reading weight, then verify coverage; this does not by itself authorize narrative rewrites, new filenames or link migrations. D-042/D-043 record historical six-arc practice, not the final plan. Preserve approval provenance and any unresolved scene-level decisions before structural changes. |
| 2 — Narrative rollout | After adoption, archive originals, pilot a short and a dense accepted arc, then roll out bounded chapters/arcs. Trace each substantial old paragraph to retained, relocated, summarized or archived content with rationale. Preserve unique scenes, agency, emotional consequences, causality, private knowledge and source notes. Track navigation/anchor/subject-label dependencies as one coordinated change set. |
| 3 — Races and discovery | Search existing subjects, aliases, chronology and dossiers before declaring omissions. Record missing, underindexed, covered, potential duplicate or insufficient evidence. Prepare classification/template/schema proposal and establish the plan's agreement gate before rollout. Preserve stable entity IDs; distinguish peoples, individuals, factions and creatures. Create only evidence-backed entries. |
| 4 — World rollout | Review a subject against its domain contract, actual first/last observation and final supported condition. Preserve prior bytes and claim trace. Retain specialist-register and technical-index exceptions; do not duplicate biographies by arc or turn indexes into stories. |
| 5 — Research verification | Reuse existing review-queue/ledger issue keys. Prioritize consequential identity, contract, chronology, custody or ending questions. Consult dossiers first and perform only focused ASR/handout/listening work needed. Record actual actions and competing interpretations; never resolve doubt merely to close a batch. |
| 6 — Integration | Reconcile root/world/narrative navigation, chronology, entity aliases/relationships, queues and ledger. Archive obsolete controls before shortening; retain issue keys and unresolved questions. Verify terminal file dispositions, compatibility links, actual horizons and maintained anchors. Completion requires every applicable gate and explicit evidence limits. |

Phases 3–5 may proceed in linked batches within **D-047 autonomous
minor-editorial scope**, any other explicitly approved substantive scope, and
satisfied dependencies. Read-only inventory, comparison and discovery may
prepare new material decisions; only a **substantive/ambiguous edit needing
approval** invokes the stop gate above. Routine, unambiguous spelling or
small non-semantic fixes do **not** create an approval hold.

## Evidence and editorial invariants

- Played endpoint: S3E18. S3E019 is nonplayed roundtable testimony; retrospective
  recollections and unused creator preparation remain identifiable. Principal City
  preparation does not establish a played visit or surviving institution. Keep
  Wastes, Delvers, Inverse and independent one-offs separate.
- E000 is introductory; place E013.5 in fictional time. E043/E127 are one-offs;
  E107–E109 are the Dunebreaker historical prequel. Split E101 at Hope's departure
  without duplicating its scene or counting its dossier twice. Season boundaries
  alone do not create arcs. Verify proposed counts against the numbering index.
- New prose uses current canonical orthography: The Principal, Principal City,
  Khaervilon, T'ietkalla and Or'Nath forms, following current naming decisions and
  map/handout registers. Preserve legacy slugs, historical quotes, source-derived
  titles, frozen reports and raw `sources/` bytes. Review replacements by referent;
  never perform repository-wide blind replacement.
- Keep one canonical subject identity and distinct agency for Stanley/Diontalus.
  Preserve distinctions among hearts, Hand/Fist, Eyes and other documented entities.
  Apply older world-plan regression examples at their stated cutoff; a Season One
  condition is not automatically the campaign's final state.
- Main prose is in-world and subject-focused: introduction-time perspective,
  meaningful chronological changes, Current status last (Lasting legacy for
  suitable history studies). Put source IDs, clocks, research horizons and ASR
  limits in complete footnotes. Keep natural in-world attribution and uncertainty.
- **Future drafted or rebalanced narrative chapters** use roughly **400–600 main-prose words** as a **soft diagnostic** (D-069); event-heavy chapters may require more room for important scenes, agency and consequences. Quiet chapters may be shorter. Do **not** retroactively trim protected editions. Major biography sections retain separate **150–300-word** guidance. Compare meaningful sections within the domain; no padding, invented motives or lost developments for a quota. Other world domains have no universal word budget.
- Separate observed events, GM exposition, NPC claims, private knowledge,
  retrospectives and unused plans. ASR agreement/disagreement is neither accuracy
  nor audio verification. A finale mention is not a final direct appearance.

## Stream-safe verification and recovery

Use **small, bounded, recoverable checks** to reduce large-response or long-call
stream failures. This is a transport-risk mitigation, **not** evidence of a
confirmed transport root cause.

1. **Check incrementally:** Validate each changed file close to its edit and
   record the actual result/limits under its WCL task immediately. At final
   handoff check only unresolved gates, the concise task readback and Git
   status/diff; **do not rerun all previously passed checks**.
2. **Bound calls and output:** Prefer one focused test or 1–3 short independent
   calls at a time, rather than a broad parallel fan-out. Use short numbered
   ranges for source reading. For binary files, request only small metadata
   chunks when size/SHA-256 suffice. Never forward full rendered HTML, large
   binary/base64 payloads, massive diffs or entire legacy reports as results.
   Count link/anchor statuses within the call and return **only counts,
   exceptions and precise failures**. Avoid a single script with dozens of
   nested tool calls, even if each response is small.
   **Workspace MCP path contract:** `search_workspace(path=...)` requires an
   existing **directory** (e.g. the repository's `project` or `world` root),
   never a specific `.md`/`.json` file; use `read_workspace_file` for exact
   file content and numbered, bounded reads for local matches. A
   `path_not_directory` rejection is an input-validation error, not proof of
   an underlying stream failure or a failed repository write. Correct the
   argument rather than retrying the same invalid call.
3. **Do not revalidate immutable archives repeatedly:** Verify an exact
   preservation copy once (size + SHA-256), record the result and reuse it until
   its bytes or relevant inputs change. Archived historical files above
   renderer limits are not missing merely because HTML preview cannot inspect
   them; note that limit separately from the verified file hash.
4. **Handle transport errors as unknown outcomes:** On `Error in input stream`,
   message-stream loss, timeout or interrupted verification, do **not** infer
   that a write or check failed, and do not blindly repeat the last batch.
   Reconnect with **one small read-only Git status or target readback**, verify
   whether the last operation persisted, then resume **only incomplete checks**.
   Record any genuinely unverified check as pending. Do not create a backup,
   change task status, or redo a major rewrite merely because delivery failed.
5. **Prioritize useful stopping points:** Once required checks are accounted
   for, close each verified WCL task in the selected cohort and give a concise status. Extra independent
   audits belong to separately scoped tasks, not an ever-expanding final
   verification block. If one check is expensive or unreliable, isolate it,
   explain its limitation and leave that gate explicitly open rather than
   risking all completed work.

## Validate and hand off

Before a major rewrite/restructure verify one exact SHA-256-checked working-copy
baseline for that coherent effort; reuse it for subsequent repairs. Ordinary
bounded edits need no extra archive. After each meaningful operation read back
the output, **record its result once in the corresponding WCL task entry**, and update only
actual artifact dispositions or significant milestone decisions where applicable.
Do not generate new per-batch reports or duplicate snapshots.

Review domain focus, claim coverage, knowledge boundaries, actual source horizon
and final status. Check footnote references/definitions, relative links, incoming
anchors, compatibility pages and rebased archive reading copies. Link checks
must ignore fenced illustrative Markdown. Distinguish baseline failures from
introduced diagnostics.

Use available tooling with explicit changed-file scope, for example:

```powershell
rtk proxy node scripts/lint-markdown.mjs --files world/characters/vorel.md
rtk git diff --check -- world/characters/vorel.md
```

Include every maintained file changed by the actual slice. The repository linter
excludes installed skills and historical archive roots; check those separately
when needed. Record commands, scope, exit codes, diagnostics and evidence paths.
Unavailable or timed-out checks remain unrun/unknown. Run code tests when tools
change, not as an editorial ritual. Passing tooling does not establish facts.

Advance only evidenced lifecycle stages; check off **each individually validated
WCL task** in the selected cohort and set the next eligible action in the
register introduction. Update the manifest only for a real
artifact disposition, not as another progress log. Checkpoint **in place** after meaningful slices, before expensive calls where recovery requires it, and immediately on recoverable errors; no standalone report is required per slice. End a turn with completed
scope, actual validation, unresolved decisions/errors and checkpoint path. Do not
commit, push, publish or launch background cleanup without explicit authorization.
Do not mark the campaign complete because a batch or time allowance ended.
