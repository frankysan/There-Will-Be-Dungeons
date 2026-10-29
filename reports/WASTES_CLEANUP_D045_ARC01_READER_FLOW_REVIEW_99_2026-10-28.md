# Wastes Cleanup — Batch 99: Arc 01 reader-flow and source-fidelity review

**Date:** 2026-10-28. **Status:** read-only review; no story editing or publication.

## Current repository and access

Opening: `main`, HEAD `571d1d372906a99d1cb79fe565007f929e025351`, **10 pre-existing changed paths**, zero restricted. No local checkout at standard mounts. Authenticated workspace MCP worked intermittently, but repeatedly rejected certain file reads and long report writes. Next-priority GitHub retrieved E009 and E013.5 dossiers. **Its committed Arc01 is pre-Batch98; it must not stand in for the live modified file.** When reads resumed, MCP independently confirmed current `narrative/ARC_01.md` **15,875 bytes / SHA-256 `ca7e951972048351cb4a8b7482bbc1c32aff19243a87d9a704f887b31bbc0548`**, identical to the Batch98 post-edit baseline. No narrative, original arcs, navigation, episode/world or season file was edited in this batch.

## Chapter III chronology and surrounding story

**PASS (E006 dossier):** Nash directly verifies Dusthill's water at the surface; Vorel captures a goblin; Stanley has his separate confrontation with Aaron; afterward the captive identifies himself as Bok Bok; the following morning comes Shun'ti's public meeting, Wilma's accusation and Nash's visions. A smaller council, Zorenthelas's speaker-attributed Elhandar beliefs, the talking wrench and Fate 4 presentation follow. The party gives **C4N-D13's data core to Zorenthelas with a request for Elhandar**, without claiming delivery, proven significance or permanent custody. The E005 engine status is separate from E006's surface proof.

**PASS (reader flow):** Chapters I–II cover the Hillmaster, river, ruined settlement and Peter's claims; Chapter III leads from the raided town to departure; IV continues the rescue pursuit and identifies E007's beetles without backdating the E006 mystery. V holds Nash/Stanley's E008 underground experience separate from later-released E013.5 Hope/Vorel dialogue set during their separation. VI ends at E009's escape, unresolved guest-gnome fate and approaching convoy; E010 belongs to the next arc. Chapter III's approximately **477 prose words** are near a diagnostic 350–450 target and do not justify arbitrary compression.

## Additional findings — not authorized edits

- **Medium, potentially important:** [E008 dossier](../episodes/E008.md), about 00:06–00:10, records **Nash's private vision** before meeting the guest gnomes, including contrasting unidentified appeals and Solar Mines imagery. The draft opens Chapter V at the gnomes and leaves this separate scene out. A small source-backed addition could preserve his experience and future character motivations, but must leave the voices' identity, truth and private knowledge unresolved. **Requires specific owner approval; do not insert automatically.**
- **Low–medium, optional:** [E009 dossier](../episodes/E009.md) distinguishes portable-hole cloth, rods/immovable-rod puzzle, a staff revealed by the tree, and specific actions in saving Chance. Chapter VI summarizes the rescue and portable cloth but does not track every item's custody. Review relevance to subsequent story before expansion; do **not** invent permanent ownership.
- **PASS, supplemental status:** [E013.5 dossier](../episodes/E013.5.md) confirms Hope and Vorel's discussion was released later but set in the E008–E009 separation. The time-travel plan and dragon/star traditions are beliefs and goals, not proven cosmology. Stanley's retrospective suggestion that the gnomes did not make it out is not evidence of their deaths; E009 GM commentary specifically does not declare them dead.

**Result:** No newly confirmed chronology or custody contradiction in the repaired Chapter III or checked neighboring transitions. These are possible additions, not corrections already approved by Batch98. Chapter lengths are diagnostics, not quotas. Existing six-arc edition and public links remain protected.

## Validation, lifecycle and next decision

The **current live Arc01 byte-size/SHA were rechecked** after workspace reads recovered. Batch98 already checked the exact bounded Chapter III change, all six headings, seven paired footnotes and nineteen unchanged Markdown links; those are *carried-forward* checks, not freshly rerun. Original recordings were not listened to; there was no complete Markdown render, lint or broad test run. Existing early source paragraph identities (17/17) establish traceability, **not** proof that every dossier scene is represented. Draft status remains **unpublished, provisionally source-reviewed, not finally accepted**.

**Recommendation:** The owner may accept the concise draft provisionally with these optional details deferred, or explicitly approve a narrow Chapter V Nash-only scene and/or consequential E009 item/agency expansion. Do not request the already completed Batch98 correction again; do not edit other arcs or public navigation.

## Recovery and checkpoint

Source and data findings were first preserved in a standalone Markdown/git patch fallback because repeated MCP create/read requests were rejected by safety checks. No GitHub write was attempted. Once authenticated workspace operations resumed, the live Arc01 hash was verified and this **same report** was created in small guarded, readback-friendly pieces. Archive exact live tracker working copies before appending the Batch99 checkpoint, then read back and confirm Git scope. This review does not authorize stage, commit or push.

**Next batch:** a specific owner decision on two possible prose additions, or on provisional acceptance of the compact revised Arc01; continue the eleven-arc migration only within the approved scope and D-049 compatibility policy.
