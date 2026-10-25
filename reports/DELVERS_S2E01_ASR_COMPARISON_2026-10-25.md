# Delvers S2E01 — Very Snakey: complete ASR comparison (2026-10-25)

**Identity:** Played **Season Two Episode One**, explicitly announced at host opening, following season-one arc finale [S1E12](../delvers/episodes/S1E12.md) and separately archived in-universe S2E00 cutaway. **Cold opening plays after two lost weeks on Snake Island**, then reconstructs island expedition in disconnected memories; *not* a complete chronological journey played on-air. Pinned connected clean Git `main` and private GitHub ref `181342d2540927c2411e37e1115df480eff3c51f`. No audio listened, source SRT-to-MP3 clocks/sheets/handout verified or pipeline run settings checked.

| Export | Exact file | Git blob SHA | Cues | Last cue end | Normalized words |
| --- | --- | --- | ---: | --- | ---: |
| Primary Parakeet processed | [P](../sources/Delvers%20S2E01.%20Very%20Snakey.parakeet.processed.srt) | `37a4785e5be816a49c3ac60fd55e26ae29546fc8` | **2,531** | **02:52:36.220** | **22,859** |
| Secondary Qwen Q8/Canary CTC/Nemotron-labelled | [Q](../sources/Delvers%20S2E01.%20Very%20Snakey.qwen-q8.canary-ctc.nemotron.srt) | `47e86b06ebeceb6e799ec46b6d65fda1343aae13` | **4,026** | **02:52:35.880** | **22,953** |

**Complete-export textual disagreement: 1,749 edits / 22,859 primary words = 7.65%**. Qwen has **94 extra normalized words** and ends **0.340 sec earlier** by SRT cue timestamp. **Not WER, audio-verified accuracy, confirmed missed speech, hallucination or cue-by-cue alignments.**

Method: tokenize all SRT cue bodies in time order, ignoring indices/timecodes and removing `(speaker N)`, Unicode lowercase, delete curly/straight apostrophes without spaces, replace other nonletters/digits by spaces, split. Unit-cost ordered **Levenshtein** two-row dynamic programming **4,000-token diagonal band**. Result 1,749 below band; any path leaving band must already cost ≥4,000 insertions/deletions, so the global optimum is exact. Both whole exports parsed for distance; primary read chronologically and Qwen **targeted excerpts** read for high-impact events, **not an independent entire Qwen semantic reread**.

## High-risk source review

| Approx. clock | Disagreement / reading boundaries |
| --- | --- |
| ~00:00–00:29 | Cold open after **two weeks away from Atomer**; quests are memory shards (Staff of the Python, **Princess Hissia/Isia**, snake queen necklace/ring, false golden idol, ridden serpents, venom). **1,000 gp each paid**, guild inspects items; **Cassius removes apparent curses**, objects return following morning. **No proof full Snake Island story, marriages, snake idols retrieved or forgotten events objectively validated**. |
| ~00:33–00:41 | Satyr **Chuck Abnaz/Nasty** with three colleagues identifies **Cloven Brotherhood** as Koh's forgery associates, helped wife's medical payments then threatens fee/return to crime. Wife still asleep, daughter alive; no observed assault. |
| ~00:43–01:01 | Rianu/Rhianu Keeves still alive and unresponsive. **6 HP Cure Wounds** restores bedsores, not consciousness. Unusual **Revivify on living target** causes faint **“Kalizar/Calizar”**, not successful resurrection; exact word unknown. |
| ~01:08–01:16 / ~01:35–01:46 | Parent letter **Lord and Lady Blackwater**, gold-on-black B family crest, physician **Ripart/Rippard**, goggles detect **Lestai/Lastai goddess mark**. What happened **two years ago** is told privately to Margaret but **narration skips it**. |
| ~01:17–01:34 | Koh now **buys Ring of Feather Falling for 2,000 gp**; guild upgrades board/map. Party **registers White Wedding/Hooper ghost assignment, 530 gp, tomorrow evening**. Do not treat Silver Slayer rank as upgraded player rank or ghost already expelled. |
| ~01:48–02:51 | Krandal **receives physical tower deed and visits** farmland near Noble Hollow, sea hag and minotaur skeleton fight. Koh beheads minotaur skeletal body but **skull remains talking and is buried**, rather than destroyed. Evelyn's Lay on Hands **restores 20 HP to fallen Krandal**; hag eventually killed via Evelyn's hammer and Krandal spectral face mace, disgorges fish/eels. Land renamed **Potato Grove**, no crops yet; cauldron spotted not taken. |
| Final | Memory of priest-like normal snake and cooking pyre is **unresolved recollection**, not confirmation party was eaten. Out-of-game announcement of upcoming guest **Bo Schwartz / Bo Sharts?** is not in-world and not a confirmed scene in S2E01. |

## Outstanding evidence

See [dossier listening keys](../delvers/episodes/S2E01.md). **Both complete exports analyzed quantitatively, only full primary chronologically read**, selected secondary corroborated. Original audio, map and price list not inspected, old death/undead conditions only text-level adjudications. Original `sources/` files unchanged.

[Dossier](../delvers/episodes/S2E01.md) · [Delvers review queue](../delvers/REVIEW_QUEUE.md).
