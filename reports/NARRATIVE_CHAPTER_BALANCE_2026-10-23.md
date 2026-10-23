# Narrative chapter consolidation — 2026-10-23

The completed Wastes narrative pages now each have **eight main chapters**. Their existing arc boundaries remain intact. Prologues, epilogues and source notes are outside the count; **Arc Five remains ongoing** and is unchanged. Chapter count is a reading convention, not a claim of equal story duration or equal word count.

## Layout changes

| Narrative | Before | After | Editorial change |
| --- | --- | --- | --- |
| [Arc One](../narrative/ARC_ONE.md) | 3 main chapters | 8 | Divide the existing Dusthill, Slavetown and Black Mine prose at changes in setting and purpose; retain all story paragraphs and the prologue |
| [Arc Two](../narrative/ARC_TWO.md) | 5 main chapters | 8 | Separate the departure, Diontalus joining and Trashburg arrival, then distinguish the pit journey from the ancient kingdom; retain all story paragraphs and retrospective epilogue |
| [Arc Three](../narrative/ARC_THREE.md) | 8 main chapters | 8 | Unchanged |
| [Arc Four](../narrative/ARC_FOUR.md) | Accumulated scene chapters, numbered through XLI with a missing XXXIX, plus later unnumbered sections | 8 | Rewrite the completed arc as a connected whole, reducing about 26,200 words to about 3,100; remove repeated episode cutoffs and duplicated status recaps from the active narrative |
| [Arc Five](../narrative/ARC_FIVE.md) | Ongoing opening | Unchanged | Continue to grow until its story boundary is established |

Arc Four's chapters follow arrival in Sigil, the tournament, the reunion, Tobacho's bargain, the failed infiltration, the plague and cure, the rooftop battle, and Hope's departure. Every main chapter links to its supporting episode dossiers. The rewrite retains the difference between NPC testimony, private knowledge, proposed plans and completed actions. In particular:

- Hope and Stanley return through mirrors while their old bodies remain; Nash's casting resumes through a GM correction, and his body finishes regrowing later.
- Kanja's reported death does not identify a murderer. Nothing's separate abduction commission is not shown completed.
- Hope is rejected by White Tower, accepts the besiegers' coerced alignment change and later discloses it. The successful cure does not resolve the conflicting disease names or identify its sender.
- Stanley and Alentris become lovers; the death sentence is rescinded. The proposed celestial transfer does not become a completed delivery.
- The chest, gauntlet and severed Hand remain distinct. Vorel opens the box; Hope binds the Hand to herself; Vorel returns the separate gauntlet to the chest.
- The siege ends, but the Blood War and the return to Earth remain unresolved. Hope's departure at approximately 01:57–01:59 in E101 closes Arc Four; the remainder of E101 begins Arc Five.

This is an editorial consolidation of existing research, **not a new source study or audio verification**. Detailed source uncertainties and earlier episode-cutoff states remain in the dossiers and archived narrative.

## Preservation and navigation

Before editing, the three changed narrative pages were saved under [research/legacy/2026-10-23](../research/legacy/2026-10-23/README.md), with relative links rebased for that directory:

- [Arc One before chapter balancing](../research/legacy/2026-10-23/ARC_ONE_PRE_CHAPTER_BALANCE.md)
- [Arc Two before chapter balancing](../research/legacy/2026-10-23/ARC_TWO_PRE_CHAPTER_BALANCE.md)
- [Arc Four before chapter balancing](../research/legacy/2026-10-23/ARC_FOUR_PRE_CHAPTER_BALANCE.md)

Update the [story guide](../narrative/README.md) with the chapter counts and the [documentation architecture](../project/DOCUMENTATION_ARCHITECTURE.md) with the completed narrative pass and an approximate eight-chapter convention. Reference-page consolidation and source listening remain separate work. No narrative files are renamed. Existing frozen narrative snapshots, episode dossiers and source artifacts remain unchanged; the archive index gains links to the new copies.

## Validation

- `npm run lint:markdown`: **216 maintained Markdown files, zero violations**. Explicit Markdownlint of the three new snapshots and their archive index: **four files, zero violations**. `git diff --check` passes.
- Compare **6,204 current relative file/fragment links** against **6,057** in the starting revision: **no new failures**. The same **17 pre-existing failures** remain outside this change.
- All four completed arcs contain **eight numbered main chapters**. Arc Three and the ongoing Arc Five are unchanged.
- All **15 Arc One** and **27 Arc Two** story/notice paragraphs are retained verbatim; headings, source-link layout and archival navigation change.
- Git object-hash comparison confirms **602 pre-existing tracked source, transcript and archive files unchanged**, excluding the deliberately extended archive index. The three new snapshots reproduce their original narrative text apart from rebased link destinations.
- Review Arc Four's ending and the story guide against the E101 shared boundary: Hope's completed departure ends Arc Four, and the later casino material stays in Arc Five. The rewritten narrative links to every dossier from E082 through E101.

Changes remain local and uncommitted. No new listening or canonical transcript edits were performed.
