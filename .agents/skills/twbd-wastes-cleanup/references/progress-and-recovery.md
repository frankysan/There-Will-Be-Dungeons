# Durable progress and recovery

## Repository records: one authority for each state

- **[Wastes cleanup tasks](../../../../project/WASTES_CLEANUP_TASKS.md):** the **only** task checklist, progress state and resume action. Stable `WCL-###` headings never get reused or renumbered; record exact targets, approval basis, evidence and limits in the same task entry.
- **`project/WASTES_CLEANUP_MANIFEST.md`:** artifact lifecycle, preservation and compatibility only, not batch completion.
- **`project/WASTES_CLEANUP_CHANGELOG.md`:** significant milestones/owner decisions only, not a second per-task log.
- **`project/WASTES_CLEANUP_PROGRESS.md`:** compatibility redirect to the tasks; never append a new status there.
- **`project/DECISIONS.md`:** authority and approvals. `project/REVIEW_QUEUE.md` and `world/CONSISTENCY_LEDGER.md` retain *evidence issue IDs*, not cleanup task checkboxes.
- **`research/legacy/`:** one-time exact major-rewrite originals and byte-preserved old manifest/changelog/progress history.

If records disagree, reconcile actual bytes and decisions, never unsupported success claims. Use `reports/` only for independently useful research, not routine batch paperwork.

## Recover and coordinate an adaptive WCL cohort

1. Inspect live Git status/HEAD and the register's next actionable WCL ID.
   A named user task takes precedence. Evaluate its dependencies and a
   **lookahead set** of related eligible siblings or same-source tasks
   according to [the cleanup skill's D-082 adaptive batching contract](../SKILL.md).
   Default to the largest manageable, dependency-safe cohort instead of
   stopping at four files or one task by habit.
   An older unchecked deferred/conditional task is not automatically next.
2. Record a compact **selected exact path set, task ID set and dependency/
   operation plan** in the existing WCL/census records. A four-file anchor
   may gain other related pending paths after preflight; do not silently
   expand or claim unexamined work. Do not create another batch record. The same source may support multiple IDs, but each retains its
   own acceptance condition; parents close only after required children and
   the parent exit gate are actually satisfied.
3. Preflight the union of unique input sizes, source windows, link/fragment
   density, edit risk, validation work and tool-output cost **before** loading
   all files. Group small related tasks and split large/conflicting ones;
   reserve room for edits, checks and checkpointing. This is an approximate
   context budget, not a claimed exact token count.
4. Checkpoint each finished **file's evidence and validations** as the cohort
   proceeds; mark each WCL checkbox independently after all of that task's
   outputs pass. Prefer a **single task-register update per coherent cohort**
   where practical. If interrupted, compare actual persisted bytes and
   resume only unfinished IDs or operations, retaining completed work. Do **not** rerun the whole group.
5. At close, read back only changed WCL entries, update the register's one
   next-action pointer, and run bounded remaining checks. The manifest changes
   only for actual artifact dispositions; the milestone log only for meaningful
   decisions or changes. Never append progress in the old redirect or create
   a parallel "completed batch" ledger.

## Grouped world census: per-file recovery contract (D-082, 2026-11-01)

For read-only structural audits, record related files as per-file subrecords
under their selected WCL task IDs or the continuing world census, with no
per-batch report. Preflight live Git state, file sizes, evidence overlap,
source and link density, and approval/tool limits. The new D-082 defaults
prefer roughly **10–15 short, 5–8 medium, or 1–3 large related files**, with
**800–1,500 source lines when practical**, instead of a routine four-file
cohort. These are not quotas; choose fewer for dense or difficult work, and
do not add unrelated files merely to fill a number. The October 27 small
batch pilot is historical guidance, not the current selection limit.

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

**Checkpoint each completed file in its existing WCL/census record**, not a
new file: mark its per-file review level only after actual full line coverage,
provenance and the applicable checks, with missing validations explicit.
The parent WCL checkbox remains unchecked until the complete selected task
scope passes. One cohort may close multiple independently evidenced WCL IDs.
If the tool times out, do not mark in-flight work complete. On resume compare
Git status and source input, retain evidenced completed files, recheck any changed
input, and resume the first `reading` or `unknown` record from its last verified
line. If a file grew unexpectedly or has complex semantic ambiguity, split the
remaining batch and document the revised path list; do not claim unprocessed
files as complete. A required **unapproved substantive edit stops the entire
cleanup batch** under the skill's owner-approval gate; never process a different
file as a workaround. Read-only investigation can document the blocked choice.

At close, check off **each independently verified WCL task**, reconcile full
census counts and unique paths, read back only changed entries and check Git
scope. Do not rerun every already passed file check as a final monolithic audit. Update the manifest only for actual file dispositions; never mirror task completion in progress. Do not create PRE_ copies for routine control edits. If interrupted, reconcile the task against persisted evidence without repeating finished reads. Count world
first-pass coverage per completed **unique path**; do not change the original
134-file worklist's `listed_only` directory-baseline states. Missing hashes,
source/fact/audio verification, incoming/backlink checks or lint remain explicitly
pending and are never implied by a batch completion label.

## Per-task evidence and milestone recording

Record the action, affected files, source/approval, observed result, test scope and limits under **each affected `WCL-###`**, even when several share one source read. For major rewrites, link the **one** SHA-verified pre-edit original and source/paragraph trace. For a census, retain actual per-file evidence in the task or a linked continuing census. A meaningful milestone/owner decision may also get **one brief changelog row referring to the task ID**. Incremental validation, ordinary typo fixes and routine checkoffs do not receive duplicate change entries.

Original-audio verification must name the recording source, actual listened clock interval and verifier; two ASR outputs are not audio verification. Historical record URLs, evidence report paths and approved archive hashes remain retained as evidence.

For D-085/WCL-197 legacy-page retirement, run the **read-only exact-target** `tools.wastes_reference_diagnostics` with repeated `--alias-target world/.../old-name.md`, explicit `--domain` for `world`, `episodes`, `narrative`, `wastes`, `project`, `reports` and **`research`**, and bounded `--max-files`, `--max-bytes` and `--max-links` high enough to cover each domain. Prefer separate domain runs to one capped whole-repository scan; check `LIMIT` lines and restricted-file exclusions, not just a zero match count. The alias mode resolves ordinary inline Markdown links, conservatively treats Markdown reference-style definitions (including potentially unused definitions) as link candidates, and parses HTML `<a href>` destinations to the exact file. It distinguishes `research/legacy/` backlinks from maintained navigation; literal filename/code text alone is not a hyperlink. It does **not** validate the browser's rendered reference-definition usage, every HTML form, external/bookmark URLs or native GitHub behavior. **Never delete an old compatibility page while immutable archived links still depend on it** unless a separately approved, proven-preserving solution covers those links. If the MCP server lacks deletion, retain the candidate, record the blocker under WCL-197, and do not use a test/script/Git commit as a backdoor deletion mechanism.

## Transport-safe check checkpoints

After each successful targeted validation, record its status and coverage
limit once under the **relevant WCL ID**. At final handoff read back only
the modified task entries and use a scoped Git check, never a second
multi-file verification sweep.
Limit concurrent checks, summarize large render/diff results inside the tool
call, and never emit full HTML or base64 data as a diagnostic. If the tool
request itself exceeds a call budget, break it into separate small calls.

After a stream interruption, the **last operation is unconfirmed**, not
automatically rolled back. On the next call: (1) inspect only the current
Git status/target; (2) compare persisted results with each task's last confirmed
checkpoint; (3) resume the first unverified action in the selected cohort;
(4) mark a genuinely
unrunnable test as pending, not passed. Reuse previously verified archive
hashes instead of reopening large protected snapshots. Avoid repeating
passed lint, link checks or major rewrites solely to produce a final summary.

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
4. **Apply one bounded operation.** Read back the changed output and update the corresponding WCL task with the result needed for recovery. Record a
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
6. **Close each selected task independently.** Verify each deliverable and its own checks; update only its checkbox/evidence and set one next-action pointer. Update the manifest only if an artifact's disposition/compatibility changed, and the changelog only for a material milestone/decision. Never update the progress redirect per batch. Reconcile interrupted writes before moving on.

## Recovery decisions

| Observation | Next action |
| --- | --- |
| Intent exists; file has pre-edit hash | Check archive/prerequisites; perform only the pending operation. |
| File matches recorded post-edit hash | Retain output; resume its first missing validation or control update. |
| Output differs after timeout | Compare against preserved original and intended change. Record completed, partial or unapplied outcome; reconcile narrow remainder before retrying. |
| Input changed since checkpoint | Preserve new work, assess dependent operations, invalidate only affected evidence and rebuild that slice's prerequisites. Preserve baseline/history. |
| Required major-rewrite baseline missing/hash mismatch | Stop the major rewrite; recover verifiable exact original bytes or record a blocker. Routine guarded copyedits and read-only work do not require a full-file baseline. |
| Check fails/tool unavailable | Record exact scope/failure. Fix introduced problems where possible; keep missing checks pending and avoid falsely advancing acceptance. |
| Task-register update interrupted | Inspect each selected ID against persisted artifacts; restore only missing task-state edits, keeping unverified IDs unchecked. |
| Routine unambiguous spelling/grammar/display correction | Apply under standing D-047 owner permission after guarded source-hash/archive checks; verify exact delta and preserve quotes, aliases, URLs, referents and uncertainty. No per-edit approval request. |
| Substantive or ambiguous change has no explicit approval | **Stop before that edit**, persist the exact choice and evidence, request approval/clarification and do not substitute other substantive cleanup edits. Resume after decision is recorded. |

After repeated failure, change approach or reduce the slice instead of blindly
repeating a call. Preserve failures and recovery outcomes. A batch is complete
only when its scoped outputs/checks are accounted for and **each selected WCL task's** evidence agrees;
the phase may still remain incomplete.
