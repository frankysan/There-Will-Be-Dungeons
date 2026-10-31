---
name: twbd-wastes-cleanup
description: Progressively execute or resume The Wastes completed-campaign cleanup plan in bounded, related multi-file batches, with recoverable evidence and a compact, continuously maintained change and decision history rather than per-task backups or reports. Use for Wastes narrative consolidation, world cleanup, inventory, and campaign integration under that plan; not routine episode intake or other campaigns.
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

## Resume and choose a slice

Read [progress and recovery](references/progress-and-recovery.md) before cleanup
mutations. Maintain recoverable operation states in existing controls; do not create
new reports or snapshots solely because another small operation or turn began.
Apply the repository-wide baseline/reporting economy policy (D-052 in AGENTS.md).

1. Inspect HEAD, staged/unstaged changes and untracked files. Preserve unrelated
   work. Read `project/WASTES_CLEANUP_TASKS.md` **first**; its unchecked stable
   `WCL-###` items and current next-action pointer govern work. The old
   `WASTES_CLEANUP_PROGRESS.md` is only a redirect. Read manifest dispositions
   only when file creation, preservation, path compatibility or disposition is
   relevant; the old full history is preserved under `research/legacy/`.
2. Reconcile incomplete operations against actual bytes, hashes, archives and
   check results. A timed-out call has an unknown outcome until inspected. Never
   blindly repeat it, overwrite partial work or regenerate a baseline over edits.
3. Reuse valid artifacts. HEAD advancing alone does not invalidate them: inspect
   changed inputs/dependencies and recheck only affected work. A validation-only
   resume does not trigger transcript rereading or another rewrite.
4. Select the explicit next eligible unchecked `WCL-###` task; split it into
   further stable child task IDs if it describes multiple independently verifiable
   deliverables. An existing historical `Batch ###` number is evidence, **never**
   a new task ID. For read-only Phase 0 world censuses,
   **prefer one related multi-file batch** after size/complexity preflight, rather
   than one administrative checkpoint per short article. Use the approved limits
   below; keep complex registers and large narrative/scene transformations in
   separate controlled slices. Never merge unrelated editorial decisions.
5. Record the intended paths, approval basis and per-file operation states **in
   that task's entry** (or a linked evidence worklist for a long census).
   Perform and read back each bounded operation, record actual checks and limits,
   then check **that one task** off only when its acceptance criteria pass.
   Update the manifest **only** if an artifact's disposition/compatibility changed;
   update the milestone changelog **only** for a meaningful milestone or decision.
   Do not append a second progress or per-batch recap. On interruption recover
   the first unverified file/state without rerunning completed work.

### Bounded multi-file audit selection (owner approved 2026-10-27)

For a **structural read-only inventory**, choose files by theme and source
relationship (e.g. items and related technology, or several creature profiles),
not simply because they sort next. Start with the earliest unread eligible path;
preflight line counts, scope, dependency/claim density and source horizons before
fixing an ordered target list. Do not mark a worklist entry as read until its
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
At task close, update **one checkbox and its evidence/limits**, read that task
back and inspect Git status. Change the manifest only for actual disposition
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
   for, close the one WCL task and give a concise status. Extra independent
   audits belong to separately scoped tasks, not an ever-expanding final
   verification block. If one check is expensive or unreliable, isolate it,
   explain its limitation and leave that gate explicitly open rather than
   risking all completed work.

## Validate and hand off

Before a major rewrite/restructure verify one exact SHA-256-checked working-copy
baseline for that coherent effort; reuse it for subsequent repairs. Ordinary
bounded edits need no extra archive. After each meaningful operation read back
the output, **record the result once in its WCL task entry**, and update only
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

Advance only evidenced lifecycle stages; check off the **single WCL task** when
validated and set the next action there. Update the manifest only for a real
artifact disposition, not as another progress log. Checkpoint **in place** after meaningful slices, before expensive calls where recovery requires it, and immediately on recoverable errors; no standalone report is required per slice. End a turn with completed
scope, actual validation, unresolved decisions/errors and checkpoint path. Do not
commit, push, publish or launch background cleanup without explicit authorization.
Do not mark the campaign complete because a batch or time allowance ended.
