# Delvers S1E07/S1E08 — review-key routing reconciliation

S1E07 and S1E08 reused existing review IDs for different subjects than their consistency-ledger entries. Both dossiers and the central queue now follow the unchanged ledger subjects, with provenance questions retained under existing S1E07-009 and S1E08-007. All sixteen existing keys and historical review targets remain open.

## Scope and baseline

**Date:** 2026-10-28. **Local baseline:** clean `main`, HEAD `56c0029a89d3f624a17ba36c3cf00ce77cb47ff3`. The checkout advanced after the S1E06 repair; this run uses the current committed files. No commit is created here.

The owner instructed continuation of the demonstrated two-episode routing repairs. This follows the [episode-analysis skill](../.agents/skills/twbd-episode-analysis/SKILL.md) for narrow documentation/metadata maintenance: no repeated source intake, new ASR calculation, listening or story interpretation is required. The [ledger](../delvers/world/CONSISTENCY_LEDGER.md) remains unchanged.

[Exact originals and rebased reading copies](../research/legacy/2026-10-28/delvers-s1e07-s1e08-issue-routing/README.md) preserve the two dossiers, central queue and cleanup manifest. The [routing record](../research/legacy/2026-10-28/delvers-s1e07-s1e08-issue-routing/routing.json) retains old/new blocks, tails, task rows and explicit mappings. Historical labels are not retroactively treated as if they always had their new subjects.

## S1E07 historical-to-current crosswalk

The ledger subjects 001–008 are siblings/globe, psionic training/hilt, purchased equipment, school/bag/ball, cockatrice/wedding/earnings, ecological hypotheses, southwestern encounters/items and well safety/cutoff. Existing 009 retains source-copy, map, assignment, written-name and sheet verification.

| Historical dossier label | Retained target | Current key(s) |
| --- | --- | --- |
| DEL-S1E07-001 | Broscale/globe testimony and mental-subtitle training | DEL-S1E07-001, DEL-S1E07-002 |
| DEL-S1E07-002 | Cockatrice, Battersby wedding and radiant rings | DEL-S1E07-005 |
| DEL-S1E07-003 | Margaret, school, bag and planned ball | DEL-S1E07-004 |
| DEL-S1E07-004 | Psi Blast; companies/maps; predator/larva theory | DEL-S1E07-002, DEL-S1E07-009, DEL-S1E07-006 |
| DEL-S1E07-005 | Rust trail, Shmorth, extra barrel and origin limit | DEL-S1E07-007 |
| DEL-S1E07-006 | Hilt/psychic progression; equipment; rust identification | DEL-S1E07-002, DEL-S1E07-003, DEL-S1E07-007 |
| DEL-S1E07-007 | Stirge, Bruno, kill and healing | DEL-S1E07-007 |
| DEL-S1E07-008 | Antenna/buckles/sample; water, patrol and concrete | DEL-S1E07-007, DEL-S1E07-008 |
| DEL-S1E07-009 | Copy/clock, map, written names and sheets | DEL-S1E07-009 |

Grouped targets preserve the mental-subtitle and unused Psi Blast details, hilt destruction versus blade persistence, Life Stealing/Corpse Slayer distinction, hammer recovery, ordinary javelins, scale-mail corrosion and unchanged Koh armor AC. Wedding/earnings limits, Bruno's survival, specimen/custody uncertainty and the uninspected-well cutoff remain intact. The historical Dawn Globe rules-comparison request remains uncompleted; no fresh rulebook comparison is claimed. Ledger questions such as the retained circlet and ambiguous 580-gold allocation are now explicitly visible under their existing subjects.

## S1E08 historical-to-current crosswalk

The ledger subjects 001–006 are breach/seal, First Sons cooperation, temple damage, horn/shafts, sash/ropes/equipment, and the rock creature/deeper cavern/cliffhanger. Existing 007 retains source-copy/clock and naming provenance, including the former 001 city/other-team spelling targets. It is not a new issue ID.

| Historical dossier label | Retained target | Current key(s) |
| --- | --- | --- |
| DEL-S1E08-001 | City, Darma/Dominic/Hiroshi/Yolana and other-team naming | DEL-S1E08-007 |
| DEL-S1E08-002 | Breach, seal geometry and untested water | DEL-S1E08-001 |
| DEL-S1E08-003 | Rock-creature dialect/warning and language backstory | DEL-S1E08-006 |
| DEL-S1E08-004 | First Sons names, claim dispute and puzzle participants | DEL-S1E08-002 |
| DEL-S1E08-005 | Horn/shafts, platforms and armor custody | DEL-S1E08-004, DEL-S1E08-003, DEL-S1E08-005 |
| DEL-S1E08-006 | Temple damage; seal; sash; deeper cavern/cube | DEL-S1E08-003, DEL-S1E08-001, DEL-S1E08-005, DEL-S1E08-006 |
| DEL-S1E08-007 | Audio-copy/clock and pipeline provenance | DEL-S1E08-007 |

The new grouping preserves all earlier naming targets without merging the other-well teams with the First Sons. It retains the rock-creature geometry and backstory limits, eight shafts/six platforms, 19 thunder damage/deafness/crack, spare-shaft uncertainty, sheet/map/audio verification gate, armor custody, completed concrete use, unretrieved sash and no cube fight at cutoff. Temple repair, safe water, final inventory and future rewards remain unestablished.

## Changed files and preserved boundaries

- [S1E07 dossier](../delvers/episodes/S1E07.md#listening--provenance-follow-up): nine current review tasks and an explicitly historical S1E08 onward pointer.
- [S1E08 dossier](../delvers/episodes/S1E08.md#targeted-listening-and-research-queue): seven current tasks and an explicitly historical S1E09 onward pointer. The inventory destination remains available.
- [Central queue](../delvers/REVIEW_QUEUE.md#s1e07-listening-and-continuity-targets): matching nine/seven task tables and dated reconciliation note. The 36 prior issue-table rows remain verbatim; sixteen existing IDs become centrally visible, yielding 52 unique rows without new global IDs.
- [Cleanup manifest](../project/DELVERS_CLEANUP_MANIFEST.md): append-only checkpoint.

Both dossier prefixes before their review headings retain their exact bytes: source inventories, scene evidence, ASR figures, interpretation boundaries and episode cutoffs are unchanged. Existing headings, original newline formats, ledger rows and all ordinary world/narrative material are retained. All sixteen original label meanings are mapped, including targets split across several current subjects. No issue is allocated or resolved.

## Validation and remaining work

The [checkpoint](../project/DELVERS_S1E07_S1E08_ISSUE_ROUTING_2026-10-28.json) records each member separately: archived hashes, prefix/key preservation, dossier/queue row agreement, crosswalk completeness, central-row counts, protected files, links, targeted Markdownlint and scoped whitespace checks. Its final status distinguishes completed checks from pending ones.

Completed results: four exact originals verified; both story/source prefixes byte-identical; all sixteen existing dossier keys and target mappings retained; fourteen ledger rows unchanged; all 36 prior central task rows verbatim, with 52 unique rows after adding the sixteen existing tasks. All 144 protected Delvers files and three other protected control records remain unchanged. The 31 new local links/anchors resolve, and 673 archived link destinations retain their targets after rebasing. Task-table widths and scoped tracked/new-file whitespace checks pass. Markdownlint reports zero violations across five maintained files and the archive README. Three added blank EOF lines found during validation were removed only from the new tails/append; preserved prefixes remain unchanged.

This is **played-session Delvers S1E07/S1E08 documentation, routing only**. Clock ranges come from existing dossier/ledger targets and evidence maps; no new SRT window is interpreted or MP3 seek calibrated. No ASR metric is recalculated, recording heard, original map/handout/sheet inspected or source issue closed. Listening remains deferred by owner. Rendered-site interaction and a whole-repository audit are not performed.

The demonstrated S1E07/S1E08 repairs are complete only after validation passes. Later episodes are not reviewed or certified by this batch; further maintenance requires a concrete discrepancy. Main-campaign intake remains complete at S3E12. No commit, push or publication is performed.
