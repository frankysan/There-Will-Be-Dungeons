# Gibbering mouther and mushroom-pit spider — targeted source review

**Date:** 2026-10-25. **Campaign:** The Wastes, Season One. **Candidates:** WSC-015 and WSC-016. **Result:** Both support bounded creature articles. [Candidate search](WASTES_S1_CREATURE_SEARCH_2026-10-24.md) · [Machine-readable evidence inventory](MOUTHER_AND_SPIDER_SOURCE_REVIEW_2026-10-25.json).

## Scope and method

Examined **seven selected primary Parakeet windows** and **nine selected Qwen windows** across E009 and E044 to resolve anatomy, creature identity and outcome. The four full export files were parsed for routing, cue metadata and SHA-256 fingerprints. **That parsing is not full interpretive review.** The windows below define manual-reading scope; cross-reading covers selected overlapping passages only. No original audio was heard, no full-export disagreement metric was computed and no source export was edited. Model/pipeline labels are inferred from filenames; subtitle intervals are not word timings.

Initial keyword/context discovery located additional nearby references. The E009 primary window at 02:31:35–02:33:35 and the 02:50:40–02:59:40 window are deliberately bounded to the text actually read; no intervening uninterrupted episode coverage is claimed. The complete parsed cue cache remains local at `local/creature-search/mouther-spider-2026-10-25/sources.json`.

## WSC-015 — gibbering mouther

| Passage | Supported finding | Boundary |
| --- | --- | --- |
| E009 ~02:17–02:23:38 | Pink/red fleshy mass drops from ceiling, blocks the exit, bears eyes and mouths, moves by gripping with teeth, disrupts concentration and spits a blinding flash. | A shouted “scientists” suggestion is not proven origin. The later illustration is not the basis for these anatomical claims. |
| ~02:30:50–02:33:35 | The name **gibbering mouther** is explicitly supplied; surrounding dough-like ground traps Chance's feet. | Qwen also renders nearby “mouther” as “mauler” before the full name. No external stat block is imported merely because the GM mentions a monster manual. |
| ~02:51–02:58 | Chance is bitten unconscious and partly assimilated. Stanley casts Cure Wounds; Chance wakes inside the flesh and struggles to breathe. Nash's fire removes enough mass for him to pull free. | Initial spoken “dead” is immediately qualified as not outright killed. No completed assimilation, resurrection or permanent guest-character death occurs here. |
| ~02:58:28–02:59:18; ~03:00:45 | Eddie's arrow strikes several eyes; the body turns grey, hardens and becomes motionless. The later primary passage calls it dead. | Not a petrification effect attributed to another creature. The later facility collapse is separate from this already completed defeat. |

**Important text disagreement:** Parakeet explicitly says the gibbering becomes silent; Qwen emits a long repeated syllable string across the same post-hardening interval. Preserve that difference for listening. The repeated ASR text is not evidence that the motionless creature survived or started another conversation. Likewise, a Fireball/Fire Bolt naming correction occurs in the primary rules exchange before the final fire hit; describe fire in prose rather than inventing a third-level spell expenditure from later shorthand. The two exports support the principal physical sequence, but agreement does not establish audio accuracy.

## WSC-016 — mushroom-pit spider

| Passage | Supported finding | Boundary |
| --- | --- | --- |
| E044 ~01:53:43–01:57:20 | Apparent moving ceiling resolves into a gigantic spider whose skin becomes dark blue-green; eight legs enclose the people beneath it and block escape. | “Invisibility” and “phased into existence” describe its appearance in the scene, not a verified standard phase-spider species or planar mechanism. |
| ~01:55–01:56; ~02:04 | A foot and then the falling body break mushrooms, releasing green particulate that causes severe sneezing. | Mushroom disturbance causes the clouds; no intrinsic spider spore attack is established. |
| ~02:02:15–02:06:15 | Vorel cuts through the legs with Mawstorm; the spider loses support, grabs unsuccessfully and falls. Its curled corpse is subsequently seen in the pit. | The kill is explicit. An early recap places Hope/Vorel under it, but the later narration corrects toward Nash/Stanley and explicitly puts Hope safely at a distance. Avoid assigning everyone the same position. |
| ~02:06–02:09:30 | A small bag is recovered beside the corpse; Vorel gathers severed, meaty legs as provisions. | The bag is not established as the spider's property. The narrator frames feeding on mushrooms as a guess, not witnessed ecology. Do not fix an inventory count from the initial four severed legs when subsequent taking/carrying is discussed. |

An isolated/interjected “another spider” wording during the bag retrieval does not, in this selected context, establish a second played attack or kill. No new combat follows that line; listening is needed to classify it. The article describes the one confirmed large attacker and its corpse. It is not automatically one of the earlier Dusthill spiders, a CHIDS brain-backed spider or a member of a confirmed broader population.

## Reviewed windows and fingerprints

- [E009 / Parakeet](../sources/The%20Wastes%20S1E009.%20Surfacing.parakeet.processed.srt): 5239 cues; last end 03:16:12; SHA-256 `2b218b1132c7c2d4e0e36f88b8e98628c119775e73107d00ad75bfd580552c73`.
- [E009 / Qwen](../sources/The%20Wastes%20S1E009.%20Surfacing.qwen-q8.canary-ctc.nemotron.srt): 6194 cues; last end 03:16:12; SHA-256 `e01ece14ea78f68750243b6eab0bddbbf6f59d487af30090a1eaeb51df257a2f`.
- [E044 / Parakeet](../sources/The%20Wastes%20S1E044.%20Poke%20it%20with%20your%20Mage%20Hand.parakeet.processed.srt): 2772 cues; last end 02:51:08; SHA-256 `0e95ae8d8432256fea649532c9d91ba9240ec02edf5cafe7326d06a9ad5d1054`.
- [E044 / Qwen](../sources/The%20Wastes%20S1E044.%20Poke%20it%20with%20your%20Mage%20Hand.qwen-q8.canary-ctc.nemotron.srt): 4631 cues; last end 02:51:08; SHA-256 `a14bc5f6f6ec707036b9170069ed62c2bd95e4884157c684cb663e140cfc1137`.

| Episode / export | Recording window | Cue range inspected |
| --- | --- | --- |
| E009 / Parakeet | 02:16:20–02:23:55 | 3574–3784 |
| E009 / Parakeet | 02:31:35–02:33:35 | 4009–4063 |
| E009 / Parakeet | 02:50:40–02:59:40 | 4512–4802 |
| E009 / Parakeet | 02:30:50–02:31:35 | 3988–4009 |
| E009 / Parakeet | 03:00:25–03:01:00 | 4821–4844 |
| E009 / Qwen | 02:16:50–02:19:25 | 4228–4320 |
| E009 / Qwen | 02:23:00–02:23:40 | 4448–4466 |
| E009 / Qwen | 02:30:50–02:31:20 | 4696–4713 |
| E009 / Qwen | 02:51:10–02:53:50 | 5357–5435 |
| E009 / Qwen | 02:57:25–02:59:20 | 5593–5661 |
| E044 / Parakeet | 01:53:10–01:57:45 | 1803–1885 |
| E044 / Parakeet | 02:02:10–02:09:30 | 1956–2090 |
| E044 / Qwen | 01:53:40–01:57:20 | 2986–3099 |
| E044 / Qwen | 02:02:35–02:04:40 | 3252–3315 |
| E044 / Qwen | 02:06:05–02:06:45 | 3364–3384 |
| E044 / Qwen | 02:08:00–02:09:25 | 3418–3462 |

Overlapping windows are retained as actually read, not counted as independent corroboration. These selected checks do not establish complete coverage of either recording or an ASR accuracy measurement.

## Integration and next work

Created [Gibbering mouther](../world/creatures/gibbering-mouther.md) and [Mushroom-pit spider](../world/creatures/mushroom-pit-spider.md), linked both in the creature index and marked WSC-015/WSC-016 published. Narrowly amended E009's combat/outcome summary and E044's appearance, death and provisioning sequence; neither dossier is relabeled as a fresh full dual-export review. Both reference pages use in-universe subject-focused prose, source footnotes and Current status last.

Next are WSC-017 pale tentacled cavern organism and WSC-018 river headache creatures for focused review. The latter requires a specific creature/NPC boundary check before publication. Campaign research pointers, original transcripts and media remain unchanged.

**Existing asset limitation:** E009's unchanged illustration link to `../sources/images/Scott_Johnson_-_Gibbering_Mouther.webp` is already present in HEAD, but the local `sources/images/` directory is absent. The illustration was not used as creature evidence, and this pass does not recreate or remove it. Newly added article/source links are checked separately from this pre-existing missing target.
