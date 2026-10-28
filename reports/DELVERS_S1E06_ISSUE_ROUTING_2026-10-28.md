# Delvers S1E06 — review-key routing reconciliation

The S1E06 dossier and consistency ledger reused the same issue IDs for different subjects. Current dossier and central-queue instructions now follow the unchanged ledger subjects 001–008; existing 009 retains source-copy, clock and handout checks. No issue is allocated or resolved, and no source or story claim is newly interpreted.

## Baseline and authority

**2026-10-28:** local `main`, HEAD `59e327f283b0f1357e7eab733dab99323e9aff4e`, with prior Delvers acceptance work and concurrent Wastes changes present. The owner instructed continuation; this is an independent, demonstrated tracking discrepancy after the bounded presentation pass. The [episode-analysis skill](../.agents/skills/twbd-episode-analysis/SKILL.md) permits narrow metadata/validation work to update only affected documentation without repeating full source intake.

The [ledger](../delvers/world/CONSISTENCY_LEDGER.md) is retained unchanged. Its S1E06 subjects are bronze/key/guide, holy water, flame encounters/furniture, Enzo identity/fate, inscription/prophecy, private motives, rewards/custody/level, and the missing prior bronze adventurers. The dossier's old review list instead used 004 for fire, 005 for the lever diagram, 006 for combined Enzo/prophecy/illness, 007 for private motives and 008 for combined final outcomes. An unqualified key therefore selected different questions on different pages.

## Historical-to-current crosswalk

The mapping is an explicit current routing migration, not a claim these IDs always had the same meaning. [Exact pre-edit lists](../research/legacy/2026-10-28/delvers-s1e06-issue-routing/README.md) remain authoritative for historical references. The [machine-readable mapping](../research/legacy/2026-10-28/delvers-s1e06-issue-routing/routing.json) preserves the original block, replacement rows and tail change.

| Historical dossier label | Retained review target | Current key(s) |
| --- | --- | --- |
| DEL-S1E06-001 | Bronze orientation, guide/names and pickups | DEL-S1E06-001 |
| DEL-S1E06-002 | Holy-water issue and use | DEL-S1E06-002 |
| DEL-S1E06-003 | Servants, furniture and post-skull cessation | DEL-S1E06-003 |
| DEL-S1E06-004 | Separate Fireball/window damage and Flaming Sphere/steam | DEL-S1E06-003 |
| DEL-S1E06-005 | Unexamined lever diagram, code and mistaken circular action | DEL-S1E06-009 |
| DEL-S1E06-006 | Enzo/kinship; inscription/forecast; loved one's condition | DEL-S1E06-004, DEL-S1E06-005, DEL-S1E06-006 |
| DEL-S1E06-007 | Evelyn's unnamed person and Koh's undisclosed wife | DEL-S1E06-006 |
| DEL-S1E06-008 | Final skull kill; water; garnets/rewards/dagger; mirror/staff | DEL-S1E06-003, DEL-S1E06-002, DEL-S1E06-007, DEL-S1E06-004 |
| DEL-S1E06-009 | Audio-copy/seek and handout/guide provenance | DEL-S1E06-009 |

Ledger key 008 already concerns the previous missing bronze adventurers. It now has a matching current review target, using the existing dossier's client report, Enzo testimony and later report to Cassius; no bodies, gear recovery or fate is newly established. The former diagram target remains open under existing provenance key 009 rather than being overwritten by the prophecy subject. All original numbers, injury amounts, holy-water accounting, private-disclosure limits, reward-allocation uncertainty and diagram actions remain review targets.

## Changed scope and preservation

- [S1E06 dossier](../delvers/episodes/S1E06.md#bounded-verification-queue): review-task block replaced; all preceding source, evidence-map and continuity material preserved byte-for-byte. Its obsolete next-intake label is explicitly historical; the same S1E07 source destination remains available and no new main-campaign intake is queued.
- [Central queue](../delvers/REVIEW_QUEUE.md#s1e06-listening-and-continuity-targets): nine existing S1E06 keys become centrally visible, taking issue-table rows from 27 to 36 without allocating new global IDs. Existing task rows remain verbatim. The lifecycle also links the [completed bounded D-048 acceptance](DELVERS_D048_ACCEPTANCE_03_2026-10-28.md); it does not imply factual or whole-world acceptance.
- [Cleanup manifest](../project/DELVERS_CLEANUP_MANIFEST.md): append-only checkpoint. Exact originals, hashes and rebased reading copies are archived before editing.

Read-only inspection of S1E07 and S1E08 review-key lists against their ledger rows also found subject collisions. Those dossiers are unchanged. They are the next bounded routing slice; this report neither migrates their labels nor claims a campaign-wide key audit.

## Validation and limits

[Checkpoint](../project/DELVERS_S1E06_ISSUE_ROUTING_2026-10-28.json) records original/protected hashes, preserved dossier prefix, ledger/other-task preservation, nine-key correspondence, central-row counts, guarded-edit reconstruction, local links, targeted Markdownlint and scoped whitespace checks. Final status there distinguishes completed checks from pending work.

Completed results: three exact originals verified; the dossier prefix is byte-identical and its original LF format is retained. All nine dossier/queue tasks match, all 27 pre-existing central task rows remain verbatim, and the central table now has 36 unique existing-key rows. The ledger and 145 other protected Delvers files are unchanged. All 26 new local link/anchor occurrences resolve; 661 archival link destinations retain their original targets after rebasing. Table widths, existing headings and scoped whitespace checks pass. Markdownlint reports zero violations in four maintained files and the archive README. Concurrent Wastes edits are recorded separately and left untouched.

This is **Delvers S1E06, played-session documentation, metadata/routing only**. SRT clocks are retained or grouped from existing dossier/ledger windows, not freshly located or calibrated MP3 seeks. No new transcript interpretation, original recording/handout review, ASR metric or listening verification is performed. Existing comparison figures and source-identity findings are unchanged. All evidence questions remain open; listening is deferred by owner. No commit, push or publication is performed.
