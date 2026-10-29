# Durable progress and recovery

## Repository records

Create these only when executing cleanup, after inspecting existing records:

- `project/WASTES_CLEANUP_PROGRESS.md`: short resume pointer with phase/gates,
  active batch link, remaining work and the exact next action.
- **One ongoing Wastes cleanup change/recovery log:** prefer the existing
  `project/WASTES_CLEANUP_PROGRESS.md` and relevant manifest entries, with
  dated, concise append/update entries. Reuse existing evidence reports by link.
  Do **not** create a new `reports/` file merely to record a batch, chapter,
  retry, checkpoint or routine status. A separate report is warranted only for
  substantial independently useful research, a new comparison or a milestone
  review that cannot be captured succinctly in the existing records.
- `project/WASTES_CLEANUP_MANIFEST.md`: canonical page lifecycle and links to
  batch evidence. Preserve prior checkpoints and preliminary-planning history.
- Phase 0 may use `project/WASTES_CLEANUP_BASELINE.json` for a reproducible
  inventory, but **do not confuse inventory metadata with full-text backup**.
  Before a major rewrite/restructure, preserve each affected document's exact
  working-copy contents once per coherent rewrite effort, with original-path and
  SHA-256 metadata. Reuse verified baselines throughout that effort; capture a
  new one only for a distinct later substantial rewrite from a changed state.
  Routine edits, progress/manifest updates, and read-only audits require **no
  individual full-content snapshots**.

Resolve links from each record's directory. Do not copy private raw source
content or image binaries into journals; record permitted provenance and findings.
The manifest owns disposition; the decisions ledger owns owner approvals; the
progress file holds the current pointer **and concise continuing workstream log**.
Existing detailed reports remain referenced evidence, not a mandatory new output.
If records disagree, reconcile actual bytes; a newer completion claim alone is
not authority. If a required state record cannot be saved, stop dependent edits.

## Progress pointer

Record last saved time, selected repository root, HEAD and initial Git changes,
each phase's gate state, active batch path, pending decisions with approval
references, and ordered remaining work. **For each planned edit, record either
the standing D-047 minor-editorial permission or the specific owner approval;
mark an unapproved substantive/ambiguous change `approval-required`.**
The next action names the file, operation and prerequisite check, not merely
"continue Phase 0". An unresolved **substantive** approval-required edit is
a stop state, not an invitation to select unrelated material changes. Routine
unambiguous spelling, grammar and tiny display fixes are **not** stop states.
Link completed batches without copying their details. Future work remains
planned, not completed.

## Grouped world census: per-file recovery contract (owner approved 2026-10-27)

For Phase 0 **read-only structural audits**, record several related world files
in the existing progress/manifest or a continuing journal, **without a new
report file per group**. Before the first full read, inspect live Git status and
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

At close, **aggregate only validated file records** into one manifest checkpoint
and one progress-pointer/update-log entry; read back changed controls and check
final Git scope. Do not duplicate the entire controls as PRE_ archives. If interrupted between the journal and either control,
reconcile the missing record without repeating completed reads. Count world
first-pass coverage per completed **unique path**; do not change the original
134-file worklist's `listed_only` directory-baseline states. Missing hashes,
source/fact/audio verification, incoming/backlink checks or lint remain explicitly
pending and are never implied by a batch completion label.

## Continuing change/recovery log

Append or update a **concise entry in the existing workstream record** when a
meaningful edit, decision, completed audit group, validation milestone or blocker
changes the project state. A typical entry records **date, affected paths, change,
reason/source or owner decision, observed result, checks/limits and next action**.
Include hashes when needed to pin an accepted draft, preserve a major-rewrite
baseline, or distinguish competing versions; no full-file attachment is required.

For a **major rewrite/restructure**, also link the one-time preserved
working-copy baseline and its hash, the scene/paragraph coverage disposition,
and any compatibility-link or evidence review. For a grouped read-only census,
retain per-file coverage/status and remaining paths, but keep detailed notes
within the same record, not a new per-file report. After a timeout or ambiguous
write, persist only the state needed to recover without repeating completed
work. Use `not assessed`, `not run` and `pending` honestly.

Separate enduring analysis can still be documented in `reports/` when it adds
independent research value; link it instead of copying it into each log.

Source verification records include episode, absolute recording clock/cues,
source identity/hashes, actual action (comparison/listening/handout inspection),
verifier/date, affected articles, interpretation change and limits. Name listened
windows; partial listening is not full-episode verification. Retain competing
testimony and existing issue keys.

## Operation protocol

1. **Classify the edit permission, then write intent.** Straightforward
   non-semantic spelling, grammar, punctuation and display-name corrections
   are authorized by standing owner decision **D-047 (2026-10-28)** and do
   **not** need individual approval. Check each referent, preserve aliases,
   historical quotes, filenames/links and uncertain facts; avoid blind
   replacement. For any **material/ambiguous** change, identify an explicit
   owner decision/current request. If absent, **stop before that edit** and
   request clarification instead of substituting unrelated substantive work.
   Otherwise record D-047 or explicit approval provenance, affected paths,
   prerequisites and next action in the existing workstream record. Input hashes
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
4. **Apply one bounded operation.** Read back the changed output and update its
   result in the existing progress/change log as needed for recovery. Record a
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
6. **Synchronize controls in place.** Record meaningful intra-batch recovery
   states as needed, then update relevant manifest disposition and current
   progress pointer **once at grouped-batch close**. Verify changed records
   and links; do not preserve another full-text copy of either control just
   because it was updated. Reconcile any interrupted write on resume and
   persist urgent blockers promptly.

## Recovery decisions

| Observation | Next action |
| --- | --- |
| Intent exists; file has pre-edit hash | Check archive/prerequisites; perform only the pending operation. |
| File matches recorded post-edit hash | Retain output; resume its first missing validation or control update. |
| Output differs after timeout | Compare against preserved original and intended change. Record completed, partial or unapplied outcome; reconcile narrow remainder before retrying. |
| Input changed since checkpoint | Preserve new work, assess dependent operations, invalidate only affected evidence and rebuild that slice's prerequisites. Preserve baseline/history. |
| Required major-rewrite baseline missing/hash mismatch | Stop the major rewrite; recover verifiable exact original bytes or record a blocker. Routine guarded copyedits and read-only work do not require a full-file baseline. |
| Check fails/tool unavailable | Record exact scope/failure. Fix introduced problems where possible; keep missing checks pending and avoid falsely advancing acceptance. |
| Manifest/pointer write interrupted | Reconstruct from journal and actual artifacts; apply only missing control updates. |
| Routine unambiguous spelling/grammar/display correction | Apply under standing D-047 owner permission after guarded source-hash/archive checks; verify exact delta and preserve quotes, aliases, URLs, referents and uncertainty. No per-edit approval request. |
| Substantive or ambiguous change has no explicit approval | **Stop before that edit**, persist the exact choice and evidence, request approval/clarification and do not substitute other substantive cleanup edits. Resume after decision is recorded. |

After repeated failure, change approach or reduce the slice instead of blindly
repeating a call. Preserve failures and recovery outcomes. A batch is complete
only when its scoped outputs/checks are accounted for and manifest/pointer agree;
the phase may still remain incomplete.
