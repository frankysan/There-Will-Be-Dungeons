# Durable progress and recovery

## Repository records

Create these only when executing cleanup, after inspecting existing records:

- `project/WASTES_CLEANUP_PROGRESS.md`: short resume pointer with phase/gates,
  active batch link, remaining work and the exact next action.
- `reports/wastes-cleanup/<batch-id>.md`: detailed batch journal. Use a unique
  timestamp plus subject slug, e.g. `20261027T140000Z-phase0-narrative-census`.
  Reuse the same ID on resume. Use actual timestamps and record the timezone.
- `project/WASTES_CLEANUP_MANIFEST.md`: canonical page lifecycle and links to
  batch evidence. Preserve prior checkpoints and preliminary-planning history.
- Phase 0 may use `project/WASTES_CLEANUP_BASELINE.json` for the full machine
  inventory described by the manifest. Inspect any existing schema first. Save
  chunk coverage and remaining paths; never replace the original baseline with a
  post-edit scan. Store later snapshots separately.

Resolve links from each record's directory. Do not copy private raw source
content or image binaries into journals; record permitted provenance and findings.
The manifest owns disposition; the journal owns operation evidence and recovery;
the progress file is a pointer. If they disagree, reconcile actual bytes and
evidence. A newer completion claim alone is not authority. If a record cannot be
saved, stop dependent edits.

## Progress pointer

Record last saved time, selected repository root, HEAD and initial Git changes,
each phase's gate state, active batch path, pending decisions with approval
references, and ordered remaining work. The next action names the file, operation
and prerequisite check, not merely "continue Phase 0". Link completed batches
without copying their details. Future work remains planned, not completed.

## Batch journal template

Use these sections before mutation; fill observations as they become available.
Use `not assessed`, `not run`, `pending` or `inapplicable` when truthful.

| Section | Required fields |
| --- | --- |
| Identity/scope | ID, phase, start/update times, goal, exact allowed paths, protected/excluded paths, baseline HEAD, pre-existing staged/unstaged/untracked changes. |
| Inputs/decisions | Governing policies, accepted structure and approval provenance; input paths/hashes, source class/horizon, actual last observation and existing issue keys. Metadata-only work may have no story horizon. |
| Planned operations | Ordered IDs/dependencies, intended transformation, pre-edit hash or confirmed absence for creation, archive destination, expected evidence, current operation state. |
| Preservation | Exact-original path/hash/readback comparison; separate rebased reading-copy path/hash/link checks. Archive controls before substantial shortening too. |
| Coverage/interpretation | Old paragraph/scene IDs tied to baseline hash, destination chapter/paragraph, retained/relocated/summarized/archived disposition and rationale; old/new interpretation, affected articles and knowledge boundaries. For census chunks record enumerated/processed/remaining paths. |
| Results | Operation start/end or interruption time, actual paths/post-edit hashes, readback observations, lifecycle reached, deviations and outstanding work. |
| Validation | Command/check, file scope and hashes checked, time, exit/outcome, diagnostics or report link, baseline vs introduced failures. Separate structural/factual/audio/acceptance results. |
| Recovery/handoff | Last confirmed operation, pending intent, error/unknown outcome, retry condition, exact next action, manifest/pointer synchronization and final Git scope. |

Source verification records include episode, absolute recording clock/cues,
source identity/hashes, actual action (comparison/listening/handout inspection),
verifier/date, affected articles, interpretation change and limits. Name listened
windows; partial listening is not full-episode verification. Retain competing
testimony and existing issue keys.

## Operation protocol

1. **Write intent first.** Persist operation ID, input hashes, affected paths,
   prerequisites and next action before a long call or edit. For a census chunk,
   save its ordered worklist and bounds before scanning.
2. **Preserve before replacing.** Copy actual working-copy bytes to
   `research/legacy/<date>/wastes-cleanup/<batch-id>/<repo-path>.original`.
   Read back and compare SHA-256 with the pre-edit file. HEAD is not a substitute
   for the working copy. Keep `.original` immutable. If useful, create a separate
   readable `.md` copy with rebased relative links, distinct hash and link checks.
   Preservation failure prevents rewriting that file.
3. **Recheck the precondition.** Immediately before editing, ensure the target
   still matches its expected hash; reconcile intervening changes instead of
   overwriting them or treating an outdated archive as their backup.
4. **Apply one bounded operation.** Read back output, record actual post-edit
   hash/outcome and save the journal before continuing. Where supported, write
   progress records through a temporary sibling followed by rename/replace so a
   torn write leaves the prior checkpoint intact. An orphan temporary file is
   not a completed checkpoint.
5. **Validate actual bytes.** Advance only supported page lifecycle stages:
   not-inventoried → inventoried → outlined → archived → edited →
   structurally-validated → fact-reviewed → accepted. Mark functional registers
   retained-exception. For new pages record confirmed prior absence and archival
   stage inapplicable; never fabricate an original. Audio review is separate,
   not required for every ASR-provisional editorial acceptance. Record actual
   acceptance criteria and reviewer.
6. **Synchronize controls.** Save evidence first, then relevant manifest
   disposition and progress pointer. Track/read back these writes and cross-links.
   An interruption between them requires reconciliation on resume.

## Recovery decisions

| Observation | Next action |
| --- | --- |
| Intent exists; file has pre-edit hash | Check archive/prerequisites; perform only the pending operation. |
| File matches recorded post-edit hash | Retain output; resume its first missing validation or control update. |
| Output differs after timeout | Compare against preserved original and intended change. Record completed, partial or unapplied outcome; reconcile narrow remainder before retrying. |
| Input changed since checkpoint | Preserve new work, assess dependent operations, invalidate only affected evidence and rebuild that slice's prerequisites. Preserve baseline/history. |
| Archive missing/hash mismatch | Stop that page's rewrite. Recover a verifiable actual original or record blocker and choose independent work. Never claim rewritten text as the old original. |
| Check fails/tool unavailable | Record exact scope/failure. Fix introduced problems where possible; keep missing checks pending and avoid falsely advancing acceptance. |
| Manifest/pointer write interrupted | Reconstruct from journal and actual artifacts; apply only missing control updates. |
| Owner decision pending | Link reviewable package and exact decision; preserve canonical structure and continue independent eligible work. |

After repeated failure, change approach or reduce the slice instead of blindly
repeating a call. Preserve failures and recovery outcomes. A batch is complete
only when its scoped outputs/checks are accounted for and manifest/pointer agree;
the phase may still remain incomplete.
