# Durable progress and recovery

## Repository records: one authority for each state

- **[Wastes cleanup tasks](../../../../project/WASTES_CLEANUP_TASKS.md):** the **only** task checklist, progress state and resume action. Stable `WCL-###` headings never get reused or renumbered; record exact targets, approval basis, evidence and limits in the same task entry.
- **`project/WASTES_CLEANUP_MANIFEST.md`:** artifact lifecycle, preservation and compatibility only, not batch completion.
- **`project/WASTES_CLEANUP_CHANGELOG.md`:** significant milestones/owner decisions only, not a second per-task log.
- **`project/WASTES_CLEANUP_PROGRESS.md`:** compatibility redirect to the tasks; never append a new status there.
- **`project/DECISIONS.md`:** authority and approvals. `project/REVIEW_QUEUE.md` and `world/CONSISTENCY_LEDGER.md` retain *evidence issue IDs*, not cleanup task checkboxes.
- **`research/legacy/`:** one-time exact major-rewrite originals and byte-preserved old manifest/changelog/progress history.

If records disagree, reconcile actual bytes and decisions, never unsupported success claims. Use `reports/` only for independently useful research, not routine batch paperwork.

## Resume from the indexed task list

1. Inspect the live HEAD and working tree. Read the register's next unchecked `WCL-###` and its acceptance criteria; inspect relevant artifacts.
2. Save bounded path/operation intent, source/owner authority, checks and recovery state **once in that task**. For many independent files split into child task IDs or link one per-file census; keep older batch IDs as historical evidence labels only.
3. Reconcile timeouts using current file contents; pending or unverified operations remain unchecked. Never regenerate an already verified baseline.
4. Check off the one task when fully evidenced, attach actual tests/limits and set the next action **there**. Change the manifest only when a file's disposition changed; append a changelog row only for a genuine milestone, decision or significant blocker.
5. Do not mirror completion in progress, duplicate long descriptions in three records, create fresh report snapshots per task, or falsely mark a whole phase complete from sample checks.

## Grouped world census: per-file recovery contract (owner approved 2026-10-27)

For Phase 0 **read-only structural audits**, record related files as **per-file subrecords under one WCL task**, or a linked continuing census when the list is extensive, **without a report per group**. Before the first full read, inspect live Git status and
candidate sizes, then persist an ordered path list and estimated line budget. Default to a 4–6-file pilot (roughly 300 lines) for the next
batch; subsequent choices follow the skill's short/medium/large grouping envelopes.
Never treat a numeric target as a reason to add an unrelated or complex file.

Create one **file record per planned path**, with:

- Stable ID, exact path, anticipated and observed length, source horizon, original
  baseline/HEAD and any known concurrent changes; state `queued`, `reading`,
  `complete`, `blocked` or `unknown` (and last confirmed numbered line).
- Structural inventory: numbered-line coverage without gaps, headings, tables,
  footnotes/review markers, ordinary Markdown links; count internal-world links
  whose target paths match the baseline separately from outside-world **unchecked**
  links. Record a parse/verification error explicitly rather than silently omitting.
- Domain purpose, evidence class and date cutoff, approved D-044/D-045 editorial
  leads, open issues, actual checks and precise **not-run** validation limits.
- Any owner approval needed before a **material content edit**. Read-only
  structural completion is not `fact-reviewed`, `audio-verified` or accepted.

**Checkpoint after each file in the existing record**, not in a new file:
update its status to `complete` only following full line coverage and saved
findings; persist the next file and any error.
If the tool times out, do not mark in-flight work complete. On resume compare
Git status and source input, retain evidenced completed files, recheck any changed
input, and resume the first `reading` or `unknown` record from its last verified
line. If a file grew unexpectedly or has complex semantic ambiguity, split the
remaining batch and document the revised path list; do not claim unprocessed
files as complete. A required **unapproved substantive edit stops the entire
cleanup batch** under the skill's owner-approval gate; never process a different
file as a workaround. Read-only investigation can document the blocked choice.

At close, mark **only verified WCL file subrecords/tasks** complete, read back that task and check Git scope. Update the manifest only for actual file dispositions; never mirror task completion in progress. Do not create PRE_ copies for routine control edits. If interrupted, reconcile the task against persisted evidence without repeating finished reads. Count world
first-pass coverage per completed **unique path**; do not change the original
134-file worklist's `listed_only` directory-baseline states. Missing hashes,
source/fact/audio verification, incoming/backlink checks or lint remain explicitly
pending and are never implied by a batch completion label.

## Single-task evidence and milestone recording

Record the action, affected files, source/approval, observed result, test scope and limits under the active `WCL-###`. For major rewrites, link the **one** SHA-verified pre-edit original and source/paragraph trace. For a census, retain actual per-file evidence in the task or a linked continuing census. A meaningful milestone/owner decision may also get **one brief changelog row referring to the task ID**. Incremental validation, ordinary typo fixes and routine checkoffs do not receive duplicate change entries.

Original-audio verification must name the recording source, actual listened clock interval and verifier; two ASR outputs are not audio verification. Historical record URLs, evidence report paths and approved archive hashes remain retained as evidence.

## Operation protocol

1. **Classify the edit permission, then write intent.** Straightforward
   non-semantic spelling, grammar, punctuation and display-name corrections
   are authorized by standing owner decision **D-047 (2026-10-28)** and do
   **not** need individual approval. Check each referent, preserve aliases,
   historical quotes, filenames/links and uncertain facts; avoid blind
   replacement. For any **material/ambiguous** change, identify an explicit
   owner decision/current request. If absent, **stop before that edit** and
   request clarification instead of substituting unrelated substantive work.
   Otherwise record D-047 or explicit approval provenance, affected paths, prerequisites and next action in the active WCL task. Input hashes
   are mandatory for preserved major-rewrite baselines and hash-pinned accepted
   editions, optional for ordinary corrections. For census chunks, record the
   ordered worklist and bounds without generating a new report.
2. **Preserve once before a major transformation.** For an extensive rewrite,
   consolidation, reordering or destructive replacement, preserve the exact
   current working-copy bytes of each affected document **once per coherent
   rewrite effort**, preferably under `research/legacy/`, with original path,
   timestamp, SHA-256 and purpose. Read back and verify the baseline; HEAD
   cannot substitute for uncommitted working-copy bytes. Reuse that baseline
   across subsequent small chapters/repairs; do not back up progress/manifest
   files or create `PRE_<batch>` copies for ordinary updates. A later *distinct*
   substantial rewrite of a materially changed file warrants a new baseline.
   For minor changes or audits, use Git diff/guarded readback without an archive.
   Missing or mismatched required **major-rewrite** preservation stops that
   rewrite, not unrelated read-only tasks.
3. **Recheck the precondition.** Immediately before editing, ensure the target
   still matches its expected hash; reconcile intervening changes instead of
   overwriting them or treating an outdated archive as their backup.
4. **Apply one bounded operation.** Read back the changed output and update the single WCL task with the result needed for recovery. Record a
   post-edit SHA-256 for accepted/version-pinned or major rewritten documents,
   but do not require a new hash, backup or report for every minor edit. Where
   supported, write active controls atomically; a leftover temporary file is
   not a completed checkpoint.
5. **Validate actual bytes.** Advance only supported page lifecycle stages:
   not-inventoried → inventoried → outlined → archived → edited →
   structurally-validated → fact-reviewed → accepted. Mark functional registers
   retained-exception. For new pages record confirmed prior absence and archival
   stage inapplicable; never fabricate an original. Audio review is separate,
   not required for every ASR-provisional editorial acceptance. Record actual
   acceptance criteria and reviewer.
6. **Close the task once.** Verify its defined deliverable and actual checks; update that checkbox, evidence and next action. Update the manifest only if an artifact's disposition/compatibility changed, and the changelog only for a material milestone/decision. Never update the progress redirect per batch. Reconcile interrupted writes before moving on.

## Recovery decisions

| Observation | Next action |
| --- | --- |
| Intent exists; file has pre-edit hash | Check archive/prerequisites; perform only the pending operation. |
| File matches recorded post-edit hash | Retain output; resume its first missing validation or control update. |
| Output differs after timeout | Compare against preserved original and intended change. Record completed, partial or unapplied outcome; reconcile narrow remainder before retrying. |
| Input changed since checkpoint | Preserve new work, assess dependent operations, invalidate only affected evidence and rebuild that slice's prerequisites. Preserve baseline/history. |
| Required major-rewrite baseline missing/hash mismatch | Stop the major rewrite; recover verifiable exact original bytes or record a blocker. Routine guarded copyedits and read-only work do not require a full-file baseline. |
| Check fails/tool unavailable | Record exact scope/failure. Fix introduced problems where possible; keep missing checks pending and avoid falsely advancing acceptance. |
| Task-register update interrupted | Reconstruct actual source state, then apply only the missing task edit. Keep unchecked until validated. |
| Routine unambiguous spelling/grammar/display correction | Apply under standing D-047 owner permission after guarded source-hash/archive checks; verify exact delta and preserve quotes, aliases, URLs, referents and uncertainty. No per-edit approval request. |
| Substantive or ambiguous change has no explicit approval | **Stop before that edit**, persist the exact choice and evidence, request approval/clarification and do not substitute other substantive cleanup edits. Resume after decision is recorded. |

After repeated failure, change approach or reduce the slice instead of blindly
repeating a call. Preserve failures and recovery outcomes. A batch is complete
only when its scoped outputs/checks are accounted for and its WCL task evidence agrees;
the phase may still remain incomplete.
