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
   **adaptive batching rules below**. Choose a small ordered cohort; it may
   contain one task if the anchor itself is extensive. Do not group merely
   because several checkboxes are adjacent in the register.
5. **Execute in dependency order.** Record a compact intent and selected IDs
   in their existing task entries (no extra batch journal), then perform each
   bounded operation, its readback and necessary tests. Check off **each WCL
   independently** once that task's outcome is proved. If the work is
   interrupted, leave only unverified or blocked IDs unchecked and recover
   from the first incomplete step without repeating verified reads/edits.
6. **Close and select the next task.** Reconcile the parent only when its
   defined exit gate and required children are evidenced. Set **Current next
   action** to the next eligible unchecked WCL ID based on dependencies and
   priority; this need not be numerically adjacent. Read back task changes
   and inspect Git status. Update the manifest only for actual file
   dispositions/compatibility, and the changelog only for meaningful
   milestones/decisions. Never maintain a parallel progress log.

### Adaptive, context-safe grouping of multiple tasks

**Default: consider a cohort every time**, but prefer a useful finished
subset to a large unfinished batch. Make an explicit **group-or-split**
judgment at the beginning and reconsider after each completed task.

| Work type | Usual grouping decision |
| --- | --- |
| Several small read-only checks on the same file/source | Group 2–6 short tasks if their evidence and acceptance checks overlap; share source reads |
| Bounded independent copyedits/cross-links | Group about 2–4 low-risk tasks if approval, change set and validations are compatible |
| One large biography/technical register, source-heavy audio check, contested canon, schema migration or major rewrite | Prefer one focused task, or a few ordered *stages of the same task*; plan a new slice before expanding |
| Prerequisite → dependent task (such as [WCL-044](../../../project/WASTES_CLEANUP_TASKS.md#wcl-044) → [WCL-045](../../../project/WASTES_CLEANUP_TASKS.md#wcl-045) → [WCL-046](../../../project/WASTES_CLEANUP_TASKS.md#wcl-046)) | May share one research pass, **but close each separately and do not start the dependent edit/decision until prerequisite evidence is real** |
| Browser-deferred, conditional public-release or unapproved substantive task | Not eligible for opportunistic grouping; retain the gate and request an owner decision where genuinely required |

**Context and response budget (heuristic, not a precise token meter):**

- Estimate the **union** of newly needed evidence, not the sum of repeated
  references. Prefer small numbered-line windows and distilled findings over
  copying whole articles into context. A large WCL record is not a mandate to
  reread every historical batch.
- Keep the next slice comfortably within the remaining context. Reserve
  substantial room for comparing evidence, making guarded edits, checking
  output, updating task status and explaining limitations. As a conservative
  fallback, treat roughly **30,000 characters of newly read dense source text**
  as a *preflight split warning*, **not a quota**; one large article may need
  consecutive bounded reads and persisted subrecords. If the source is dense,
  ambiguous or tool outputs are large, split sooner. Never claim an exact
  remaining-token count without supporting instrumentation.
- Limit verification fan-out to **1–3 small calls**, summarize responses
  inside tools, and avoid forwarding full rendered HTML, massive diffs,
  base64 text or repeated archived source. Keep independent validations
  incremental, not one high-cost final sweep.
- If a task develops new source uncertainties, incompatible edits, failing
  checks or a required substantive owner decision, **shrink or stop the
  cohort**. Preserve completed tasks, record the precise blocker in its
  WCL entry, and do not pick unrelated substantive work merely to evade it.
- If one task is too large, record a *checkpointed internal stage* within
  that ID or register a new independently verifiable child ID; **do not
  tick the checkbox until its full exit criteria are satisfied**. Parent
  checkboxes are gates, not summaries of a sample.
- Example: a read-only review may efficiently cover WCL-044–046 with a
  shared Nash article inventory **only if** heading/anchor findings and
  historical cutoffs are actually completed before recording the structural
  disposition. Independently dense Hope/Vorel/Stanley biographies (WCL-047–049)
  should normally be separate source-reading slices.

### Bounded multi-file audit selection (owner approved 2026-10-27)

For a **structural read-only inventory**, choose files by theme and source
relationship (e.g. items and related technology, or several creature profiles),
not simply because they sort next. Within the chosen eligible WCL task(s),
start with the specified prerequisite paths and select other related unread
files only if the adaptive source and context preflight allows it.
Preflight line counts, scope, dependency/claim density and source horizons before
fixing the ordered targets. Do not mark a worklist entry as read until its
actual full numbered-line census and findings are recorded.

| Complexity | Preferred grouping | Total source-line planning envelope |
| --- | --- | --- |
| Short subject files (roughly 15–50 lines) | 4–8 related files | Around 300 lines |
| Medium subject files (roughly 50–150 lines) | 2–4 related files | Around 350 lines |
| Large subject files (roughly 150–300 lines) | 1–2 where tractable | Around 400 lines |
| Complex technical registers or files above 300 lines | One standalone file or checkpointed chunks | Separate batch |

These envelopes are **guidelines, not quotas**. Split early if dense links, source
uncertainty, conflicting canon, tool limits or a necessary approval decision makes
a grouping unsafe. The historic **Batch 15** pilot instruction is retained only as historical
method guidance, **not a live next-action pointer**. Use the next unchecked
WCL task and name the actual selected paths before reading them in full.
Grouping does not permit more substantive edits.

The active **WCL task entry**, or an evidence-bearing linked census record when
one task needs many per-file subrecords, retains them without a per-batch report:
path,
ordered operation ID, actual line coverage/size, purpose and source horizon,
headings/notes/links (in-world listed versus out-of-world unchecked), D-044/D-045
migration leads, verification limits and `queued | reading | complete | blocked |
unknown` state. After each fully processed file, save a recovery checkpoint.
An interrupted or ambiguous operation must be reconciled from actual data before
resuming; retain completed per-file work and never infer results for unread files.
At cohort close, update **each completed task's checkbox and distinct evidence/limits**,
read back only the changed WCL entries and inspect Git status. Change the manifest only for actual disposition
changes; the progress compatibility redirect must not be updated per batch. Keep the preserved 134-file
world directory worklist as a `listed_only` baseline; track first-pass completion
in separate evidence records. See [progress and recovery](references/progress-and-recovery.md).

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
