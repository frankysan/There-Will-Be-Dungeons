# Wastes S2E03 — two-ASR comparison (2026-10-26)

[Episode dossier](../episodes/S2E03.md). Played **The Wastes S2E03 — Enemy Mine**; full Parakeet processed and Qwen-labelled sources available. Initial workspace branch `main`, clean HEAD **`101d4fdd8038f0519282917bb50b111643a784bf`**, **same ref GitHub resolved**. First 12 local transcript lines matched the remotely fetched contents; whole-file local byte equivalence **not proven**. Remote **Git blob hashes**, not local checksums:

| Export / linked input | Blob SHA | Cue count | Last end timestamp | Normalized words | Source characters |
| --- | --- | ---: | --- | ---: | ---: |
| [Parakeet processed](../sources/The%20Wastes%20S2E03.%20Enemy%20Mine.parakeet.processed.srt) | `ae29cdbebe60c34eef421f52c8aba467e50a08b6` | **2,193** | **02:24:58.920** | **19,757** | 206,240 |
| [Qwen Q8/Canary CTC/Nemotron-labelled](../sources/The%20Wastes%20S2E03.%20Enemy%20Mine.qwen-q8.canary-ctc.nemotron.srt) | `6d815c47b5efb1fa6c36adc7a040ac244761ce67` | **3,341** | **02:24:58.620** | **19,975** | 265,571 |

**Exact normalized ordered word Levenshtein distance: 1,770 / 19,757 = 8.96% inter-ASR TEXT disagreement (NOT WER).** Qwen has 218 more normalized tokens. Computation used all chronological SRT cue text, excluded cue IDs/timing, removed `(speaker N)`, lowercase, stripped straight/curly apostrophes, replaced other non-Unicode-letter/digit characters with spaces, then split. A two-row unit-cost DP with a ±2,900-token diagonal band found **1,770 edits**, strictly inside the bound, ensuring an exact global minimum (any better path also fits within that band). This is **model disagreement, not measured accuracy, audio omission, confirmed hallucination, or correct diarization**.

**Review scope:** Entire primary read in successive ~8-minute clock bins from first content to final network outro. Entire Qwen processed for metric, Qwen **selected** ~00:19–00:40, ~01:03–01:32 and ~02:00–02:24 examined independently for critical interpretation; no audio, full-file local equivalence, cast roster, item card, VTT or official handout check. ASR models/pipelines are labels inferred from filenames rather than verified runtime configs.

## Most consequential text-only findings / listening priorities

| Recording window | Source disagreement or caution |
| --- | --- |
| **00:05–00:24** | Names and ranks **Sumarslanar / Sumaslanar**, birdfolk **Gale/Jilier Critelskop**, Hargomoon, elves; Vorel's repeated **“greatest of all the time Vorels you may meet”** not a new formal title. **Monsoon spotted privately by Stanley**, only later public. |
| **00:25–00:41** | **Future Nash travelling through adjacencies** is Amanthalodar's testimony, not flashback. Hope attributes Solar Mines to **Tungsten “diary”** where S2E02 physically displayed a letter; needs document check. Tarrasque/cure are separate missions. |
| **00:42–01:05** | **Nash's Solar Mines testimony**: breeding, medical slavery, Slow Peters, solar-grid mineral processing, Emperor With No Name, secret extraction. Neither model can independently verify his memories, current facility or leader. |
| **01:05–01:22** | Council revises lizardfolk count to **75**; around **300 elves / 5 giants / 64 birdfolk / 50 Liberators**, 15 dropships, ~20 vehicles. **10,000 goblins CONDITIONAL on Bok Bok deposing Goblin King**. Monsoon and Nobieri volunteer personally; exhausted tieflings **not conscripted**. |
| **01:22–01:30** | Stanley's **34 persuasion** wins council's acceptance of potentially recruiting **Diontalus**, not an actual appearance. **Tarrasque** identified by Elhandari as a corrupted World Breaker; versioned D&D stat chat is out of game. |
| **01:30–02:06** | Many divergent proper nouns for potential allies and armaments (**Eddie and Sira/Sarah**, Jimster, Kervalon) and provisional force positions. **Mold Earth tunneling discussed, not cast**; proposed recruitment and scouting are not completed operations. |
| **~02:05–02:15** | Elhandari new office **Selle / Selili / Sililli Prime (?)** and tree's privately spoken **Nash must die** warning; followed by performed transformation, **Unbreakable Majesty** early **feat (not level 14)**. Qwen and Parakeet agree meaning but orthography and precise sacred language need listening. |
| **~02:15–02:19** | Guardian's office **Belekun / Balelikun**, name **Yunyon / Union Weal / Wheel** unstable. **She claims Tungsten Wheel is her uncle**, does not establish marriage/family history independently. Guardian physically assigned but no travel begun. |
| **02:19–02:24:59** | Narrator suggests Blast Belly Rock as possible next episode; **not an actual visit**. Clean network outro, unlike previous S2E02's post-outro duplicated furniture cue. |

**Preservation:** Source SRTs unchanged. **No original audio heard, no ground-truth transcription score.**
