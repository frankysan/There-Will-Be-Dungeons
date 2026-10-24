# Delvers — revised world and narrative presentation

**Date:** 2026-10-24. **Scope:** Apply the owner's revised `/world` and `/narrative` direction to the equivalent Delvers layers, using existing research through **Delvers S1E02**. This is a presentation pass, not new episode analysis or audio verification. [Binding application](../project/WORLD_NARRATIVE_STYLE.md#delvers-world-and-narrative).

## Preservation and existing changes

The worktree already contained S1E02 research, narrative and reference additions, alongside unrelated Wastes/editorial changes. These were preserved. Before rewriting, all 14 existing Delvers world/narrative Markdown files and its documentation plan were archived from their **working-copy bytes**, including those additions.

The [archive](../research/legacy/2026-10-24/delvers-pre-style/README.md) contains 15 exact `.md.original` snapshots plus adjacent Markdown reading copies with relative links rebased to their original live targets. Its [manifest](../research/legacy/2026-10-24/delvers-pre-style/manifest.json) records independent SHA-256 hashes for both forms. Originals and reading copies were read back before live edits; the exact snapshots preserve the original line endings and bytes. The historical drafts retain superseded cutoffs and research wording deliberately.

## Applied presentation

| Layer | Changes |
| --- | --- |
| Three character biographies | Character-focused descriptions of disposition, choices, mutual care, relationships and abilities; chronological first-job and crypt phases; current status last; source and mechanics detail moved into descriptive footnotes |
| Guild, farm cave and drift globe | Subject-specific identity, function, physical condition, institutional practice, custody and demonstrated versus explained powers; current status last |
| Thematic world guide | In-universe explanation of guild employment, the world below and sanctuary devotion, with attributed testimony and source notes |
| First jobs narrative | Retained connected story and the existing crypt chapter; removed opening research banner and the mid-story transcript aside; added source notes for the premiere chapters |
| Navigation | Narrative index now describes both completed jobs; world portal links both dossiers and the style policy; place index replaces the obsolete unvisited-crypt entry with the researched sanctuary outcome |
| Governing documentation | Shared style directive, editorial guide, architecture and Delvers documentation plan explicitly adopt the same presentation across both campaigns, with independent continuity |

The cave page retains **S1E01 as its last direct observation**; other revised articles use supported S1E02 developments. The second assignment supersedes the old assertion that the crypt is unvisited or that the first overnight rest has not occurred. No later rest, strength restoration, globe recharge or third-job selection is invented. Koh's sash retrieval remains distinct from permanent exclusive ownership. House's explanation of Studwell remains testimony.

No Wastes arc numbers, eight-chapter requirement or minimum word count are imposed on this ongoing opening narrative. Existing short scenes are not padded. Functional character/place indexes, chronology, ledger and research queues retain their source metadata and specialized purpose. The chronology, ledger, character index, episode dossiers, ASR reports, sources and media were not rewritten by this pass.

## Validation

- **Preservation:** all 15 exact-original hashes and all 15 rebased-reading-copy hashes match the archive manifest.
- **Presentation:** seven ordinary reference articles and both narrative pages pass checks for source apparatus outside the main prose and complete, unique footnote definitions. All seven reference articles finish with `Current status` as their final substantive section.
- **Links:** 433 scoped relative links checked, covering outgoing links from changed pages and archive reading copies, plus repository Markdown links into changed targets; **zero missing paths or fragments**. Fenced formatting examples are excluded. This is not a repository-wide link audit.
- **Focused Markdownlint:** all 16 changed maintained Markdown files pass with **zero violations**.
- **Full Markdownlint:** **371 maintained files, 29 violations**, the same pre-existing violations as the pre-edit baseline of 370 files. Existing failures remain in Wastes/project/report files; no repository-wide clean result is implied. The new migration report accounts for the extra maintained file; research archives are outside the maintained lint set.
- **Whitespace:** `git diff --check` passes.

Validation checks presentation and internal source links, not accuracy against audio. Original recordings, transcripts and source research retain their existing verification status.
