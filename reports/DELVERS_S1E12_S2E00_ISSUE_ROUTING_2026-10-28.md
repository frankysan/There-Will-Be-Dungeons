# Delvers S1E12/S2E00 — review routing and classification-status reconciliation

The Season One finale and Academy cutaway now use review-task subjects consistent with the ledger. Sixteen already existing global IDs are centrally visible, while thirteen historical dossier labels retain explicit mappings. One stale ledger clause now reflects the cutaway's already-completed text classification; no new interpretation, issue resolution or listening is claimed.

## Scope, identity and baseline

**Date:** 2026-10-28. **Local baseline:** `main`, HEAD `56c0029a89d3f624a17ba36c3cf00ce77cb47ff3`, with prior Delvers routing repairs and unrelated Wastes work present. This batch preserves current working copies, including uncommitted changes, and creates no commit.

- **S1E12 — End Friends:** played session; Season One/first-arc finale.
- **S2E00 — Cassius at the Guild:** narrated in-universe Academy cutaway, without a played party session. Its existing text classification places it during the Season One kuo-toa operation, before S1E12 in story time. Its archive ID remains S2E00.

Authority is the owner's continuation instruction and the [episode-analysis skill](../.agents/skills/twbd-episode-analysis/SKILL.md) for narrow metadata/routing maintenance. [Exact originals](../research/legacy/2026-10-28/delvers-s1e12-s2e00-issue-routing/README.md), hashes and rebased reading copies precede edits. The [routing record](../research/legacy/2026-10-28/delvers-s1e12-s2e00-issue-routing/routing.json) preserves old/new blocks, original rows, mappings and the single ledger replacement.

## S1E12 — historical labels mapped to ten existing ledger subjects

The ledger already has 001–010: arc boundary, equipment, prisoner transport, interrogation, First Sons/warning, summoning plate, roper ecology, aid, guild decisions/property and Snake Island offer. The dossier previously had only seven review rows. Existing ledger 008–010 now have matching dossier tasks; they are not newly allocated issues.

| Historical dossier label | Retained targets | Current route |
| --- | --- | --- |
| DEL-S1E12-001 | Rest/equipment/sword; cart restraint; date/offset | DEL-S1E12-002, DEL-S1E12-003 plus episode-wide source gate |
| DEL-S1E12-002 | First Sons names/roles, frogman and warning evidence | DEL-S1E12-005 |
| DEL-S1E12-003 | Names/deity, interrogation magic and circlet use | DEL-S1E12-004 |
| DEL-S1E12-004 | Noble Hollow, ritual/threat, disk and interrupted summoning | DEL-S1E12-001, DEL-S1E12-006 |
| DEL-S1E12-005 | Roper/brood/spells/cultist; Marek/Faelan/Norman outcomes | DEL-S1E12-005, DEL-S1E12-007, DEL-S1E12-008, DEL-S1E12-009 |
| DEL-S1E12-006 | Guild outcomes, promised tower, offer and arc ending | DEL-S1E12-001, DEL-S1E12-009, DEL-S1E12-010 |
| DEL-S1E12-007 | MP3/ASR clock, speaker, date and house-rule verification | Episode-wide source gate |

The unkeyed source gate retains all former general provenance checks and opening date/clock targets. Current 007 follows the already existing roper/piercer subject. The gate does not create an issue ID or silently discard the older meaning.

Retained boundaries include the narrow temple/ritual questions, swallowed cultist with survival unshown, separate aid to Faelan and Norman, no presumed universal survival, promised rather than transferred tower, unperformed trial/rehabilitation, and Snake Island offer without acceptance or travel. These are existing review subjects, not new source findings.

## S2E00 — historical labels mapped to existing cutaway subjects

Ledger 001–005 cover narrated placement, Academy request/custody, inspection/resources, private judgment/knowledge and source-tail difference. Existing dossier 006 remains the recording/speaker/date provenance task.

| Historical dossier label | Retained targets | Current route |
| --- | --- | --- |
| DEL-S2E00-001 | Opening/type/placement, theatre and Aegis pronunciation | DEL-S2E00-001, DEL-S2E00-002 |
| DEL-S2E00-002 | Board names/ranks and Carrie's horn/shaft custody | DEL-S2E00-002, DEL-S2E00-004 |
| DEL-S2E00-003 | History/phonetic names, selector, Cassius opinions and private knowledge | DEL-S2E00-004 |
| DEL-S2E00-004 | Sponsorship/inspection/resources; condition and place names | DEL-S2E00-003, DEL-S2E00-004 |
| DEL-S2E00-005 | Next-week-finale statement, tail difference and terminal Oh | DEL-S2E00-001, DEL-S2E00-005 |
| DEL-S2E00-006 | Original recording, voice/date and narrated-versus-party distinction | DEL-S2E00-006 |

All written-name candidates, the horn/shaft return-custody gap, withheld funding, proposed inspection, private wife disclosure and unexplained condition remain qualified. The existing 22.120-second final-cue difference is retained, not recomputed or diagnosed. Text classification is complete; spoken wording, audio offsets, voices, dates and written authority remain unresolved.

## Single stale ledger clause

`DEL-S1E12-010` still said the S2E00 type/chronological position was not reviewed. That is inconsistent with the existing [S2E00 implications](../delvers/episodes/S2E00.md#canon-and-chronology-implications) and completed [DEL-PREP-006 record](../delvers/REVIEW_QUEUE.md#completed-text-classification-check).

Only that source-status clause changes: it now points to the recorded narrated-cutaway classification, retains archive S2E00, and explicitly keeps audio/provenance questions open. The Snake Island offer, first-arc ending and all other text in that row remain unchanged. Every other ledger row is unchanged. This synchronization neither newly classifies the recording nor closes DEL-S1E12-010 or a cutaway listening question.

## Preservation and validation

Both dossier source/story/continuity prefixes before their review headings retain their exact bytes and original newline formats. Existing headings and inventory destinations remain. Their obsolete onward-research pointers now distinguish the already-classified cutaway and already-researched S2E01 from current verification; no new intake or immediate story-time continuation is inferred.

The [central queue](../delvers/REVIEW_QUEUE.md#s1e12-listening-and-continuity-targets) gains matching ten/six task tables and the finale source gate. All 76 previous issue-table rows, including completed DEL-PREP-006, remain verbatim; sixteen existing global IDs yield 92 unique central rows. [Manifest](../project/DELVERS_CLEANUP_MANIFEST.md) receives an append-only checkpoint. Earlier routing repairs and ordinary world/narrative pages remain intact.

[Checkpoint](../project/DELVERS_S1E12_S2E00_ISSUE_ROUTING_2026-10-28.json) records per-member key sets, historical mappings, source gate, prefix preservation, exact ledger replacement, archive/protected hashes, queue-row agreement, links, targeted Markdownlint and scoped whitespace checks. Its final status distinguishes completed from pending checks.

Completed structural results: five exact originals verified; both dossier prefixes byte-identical; thirteen historical dossier labels mapped to sixteen existing global IDs. All 76 prior central rows remain verbatim, with 92 unique rows after the repair. Fourteen of the fifteen relevant ledger rows are unchanged; the remaining row differs only in its specified classification-status clause. All other ledger text and 143 protected Delvers files are unchanged. All 33 new local links/anchors resolve, and 730 archival link destinations retain their targets after rebasing. Guarded reconstruction, table widths and scoped whitespace checks pass. A concurrent Wastes character-index change is recorded and left untouched.

Targeted Markdownlint checked six maintained files: five have zero violations; the ledger has one **pre-existing MD009 at line 182**, a single trailing space. Independent lint of the exact archived ledger and current ledger returns the identical line/rule/detail; that line is unchanged by this batch. No lint violation is introduced, and the unrelated baseline line is retained. The archive README also has zero violations. Thus lint is recorded with a baseline exception, not as an all-files pass.

No fresh SRT reading, audio listening, ASR metric, rulebook/map/handout/sheet inspection, fictional chronology determination or evidence resolution occurs. Listening remains deferred by owner. Rendered-site interaction, later-episode review and a whole-repository/campaign-wide audit are not performed. Further maintenance requires a concrete discrepancy. No commit, push or publication is performed.
