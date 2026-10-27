---
name: twbd-wastes-cleanup
description: Progressively execute or resume The Wastes completed-campaign cleanup plan in small, evidence-preserving batches, with durable progress records that survive timeouts and errors. Use for Wastes narrative consolidation, world cleanup, inventory, and campaign integration under that plan; not routine episode intake or other campaigns.
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

- `project/WASTES_CAMPAIGN_CLEANUP_PLAN.md`: scope, phases and acceptance gates.
- `project/WASTES_CLEANUP_MANIFEST.md`: inventory, lifecycle and migration record.
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
mutations. Recording is part of each operation, not an end-of-turn task.

1. Inspect HEAD, staged/unstaged changes and untracked files. Preserve unrelated
   work. Read `project/WASTES_CLEANUP_PROGRESS.md` if present, its active batch
   journal and relevant manifest entries. Missing progress files mean initialize
   records, not assume the campaign is untouched.
2. Reconcile incomplete operations against actual bytes, hashes, archives and
   check results. A timed-out call has an unknown outcome until inspected. Never
   blindly repeat it, overwrite partial work or regenerate a baseline over edits.
3. Reuse valid artifacts. HEAD advancing alone does not invalidate them: inspect
   changed inputs/dependencies and recheck only affected work. A validation-only
   resume does not trigger transcript rereading or another rewrite.
4. Select the earliest unmet eligible gate. Normally take one major page, one
   chapter pilot, a bounded census chunk, or at most three small subject pages,
   plus necessary control updates. A full census can span checkpointed chunks.
5. Persist intent, perform the slice, validate and checkpoint using the recovery
   protocol. Continue only within the requested scope and remaining capacity.

### Mandatory owner-approval stop gate

Before **each proposed cleanup edit**, identify the approval authorizing its
exact scope (current user request or an explicit, still-applicable recorded owner
decision). The general `$twbd-wastes-cleanup` invocation, a draft plan, a
suggested chapter crosswalk, and a recorded *proposal* do **not** by themselves
approve an undecided rewrite, renumbering, new taxonomy, canon assertion, file
move, deletion, or other material change.

If the next required edit is **not explicitly approved**, or its approved scope
is ambiguous, **STOP the cleanup batch before modifying that target and ask the
owner for clarification/approval**. Present the exact files/subjects affected,
the proposed edit and alternatives, its evidence, and the relevant unresolved
decision. Record the blocked operation and pending approval in the journal,
manifest and progress pointer when those records exist; a metadata-only record
of the hold is not permission to make the substantive edit. **Do not sidestep
the hold by choosing a different cleanup edit or silently skipping ahead.**
Resume only after an explicit decision; do not re-request an approval already
recorded and still applicable. Read-only investigation needed to explain the
choice is allowed, provided it changes no unapproved content.

## Phases and exit evidence

Use the live campaign plan's phases and gates. Phase completion and individual
page lifecycle are separate; an accepted pilot does not complete its domain.

| Phase | Work and completion evidence |
| --- | --- |
| 0 — Detailed baseline | Enumerate current narrative/world files, Wastes episodes/navigation/controls, active policies and affected reports. Save scope, exclusions, sorted worklist and remaining paths before chunking. Capture working-copy hashes, headings, paragraphs, prose counts, notes, episode links, inbound links/anchors, aliases and coverage flags. Assess purpose, horizon, last actual observation, priority and treatment per file; mark unknowns explicitly. Reconcile earlier accepted pages individually. Close only after all in-scope files and semantic fields are accounted for. |
| 1 — Arc decision | Map existing paragraphs/scenes to candidate chapters. Stress-test Arc Six and an earlier arc, compare closures, alternatives and reading weight. Keep six arcs canonical until explicit owner adoption supersedes D-042/D-043. Eleven arcs and numeric filenames remain proposals. Save a reviewable package; record approval source and exact adopted boundaries before structural changes. |
| 2 — Narrative rollout | After adoption, archive originals, pilot a short and a dense accepted arc, then roll out bounded chapters/arcs. Trace each substantial old paragraph to retained, relocated, summarized or archived content with rationale. Preserve unique scenes, agency, emotional consequences, causality, private knowledge and source notes. Track navigation/anchor/subject-label dependencies as one coordinated change set. |
| 3 — Races and discovery | Search existing subjects, aliases, chronology and dossiers before declaring omissions. Record missing, underindexed, covered, potential duplicate or insufficient evidence. Prepare classification/template/schema proposal and establish the plan's agreement gate before rollout. Preserve stable entity IDs; distinguish peoples, individuals, factions and creatures. Create only evidence-backed entries. |
| 4 — World rollout | Review a subject against its domain contract, actual first/last observation and final supported condition. Preserve prior bytes and claim trace. Retain specialist-register and technical-index exceptions; do not duplicate biographies by arc or turn indexes into stories. |
| 5 — Research verification | Reuse existing review-queue/ledger issue keys. Prioritize consequential identity, contract, chronology, custody or ending questions. Consult dossiers first and perform only focused ASR/handout/listening work needed. Record actual actions and competing interpretations; never resolve doubt merely to close a batch. |
| 6 — Integration | Reconcile root/world/narrative navigation, chronology, entity aliases/relationships, queues and ledger. Archive obsolete controls before shortening; retain issue keys and unresolved questions. Verify terminal file dispositions, compatibility links, actual horizons and maintained anchors. Completion requires every applicable gate and explicit evidence limits. |

Phases 3–5 may proceed in linked batches only within **already-approved**
scopes and satisfied dependencies. Read-only inventory, comparison and discovery
may prepare an approval decision, but any pending **unapproved edit** invokes
the mandatory stop gate above; do not continue to another edit instead.

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
- Narrative chapters use roughly 350–450 prose words as a diagnostic. Major
  biography sections have separate 150–300-word guidance. Compare meaningful
  sections within the domain; no padding, invented motives or lost developments
  for a quota. Other world domains have no universal word budget.
- Separate observed events, GM exposition, NPC claims, private knowledge,
  retrospectives and unused plans. ASR agreement/disagreement is neither accuracy
  nor audio verification. A finale mention is not a final direct appearance.

## Validate and hand off

Before substantial editing verify the exact working-copy archive and record its
SHA-256. After every bounded operation read back the output, record actual hash
and outcome, and persist remaining tasks before continuing.

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

Advance only evidenced lifecycle stages, synchronize the manifest and progress
pointer, and state the exact next action. Checkpoint after each slice, before
expensive calls and immediately on recoverable errors. End a turn with completed
scope, actual validation, unresolved decisions/errors and checkpoint path. Do not
commit, push, publish or launch background cleanup without explicit authorization.
Do not mark the campaign complete because a batch or time allowance ended.
