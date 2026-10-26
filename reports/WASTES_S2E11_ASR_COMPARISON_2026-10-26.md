# Wastes S2E11 — exact full-export ASR comparison (2026-10-26)

**Played episode:** *The Wastes* **S2E11 — Flesh Sauce**. [Timestamped primary dossier](../episodes/S2E11.md). Two independently labeled processed SRTs; **no original audio listened to or reference transcript provided**.

**Source/provenance:** Entire files fetched from GitHub default branch, Git blob P `cb3b41861d514f7effb0fd141c6f51f8c3652d75`, Q `751cb795be11e08c89da932b624068fbbe5f6cf7`. Connected local workspace **Git status was blocked twice**, so initial checkout HEAD and whole-local-bytes identity with GitHub remain unverified. Model/pipeline names **inferred from filenames** (not run logs); no invented hardware, flags or timestamps.

| Independent source | Git blob | SRT cues | Normalized words | Last cue end | Text characters |
| --- | --- | ---: | ---: | --- | ---: |
| [Parakeet processed](../sources/The%20Wastes%20S2E11.%20Flesh%20Sauce.parakeet.processed.srt) | `cb3b41861d514f7effb0fd141c6f51f8c3652d75` | **2,211** | **19,603** | **02:28:23.230** | **205,266** |
| [Qwen Q8 / Canary CTC / Nemotron](../sources/The%20Wastes%20S2E11.%20Flesh%20Sauce.qwen-q8.canary-ctc.nemotron.srt) | `751cb795be11e08c89da932b624068fbbe5f6cf7` | **3,808** | **20,032** | **02:28:24.700** | **287,482** |

**Reproducible method:** parse entire chronological SRT content; omit cue ordinals/timing; strip optional `(speaker N)` tags; join spoken cue text; lowercase; remove straight/curly apostrophes (join contractions); replace all but Unicode letters/digits with spaces and split into normalized words. Calculate **ordered unit-cost global word Levenshtein distance** (insert, delete, substitute=1) P→Q via two-row dynamic-programming **diagonal band ±4,000**. **2,137 edits** lie strictly below the band width and therefore give the **exact unrestricted global optimum**. **2,137 / 19,603 = 10.90% INTER-ASR TEXT DISAGREEMENT**, Qwen **429 more normalized tokens**. **NOT word error rate (WER), omission/hallucination count, model accuracy, or proof one variant is correct.**

## Text-only review priorities

| Recording window | Specific question; don't infer unplayed resolution |
| --- | --- |
| **~00:03–00:09** | Vorel's lizardfolk-king **fantasy only**, Tungsten immediately freed of visual pull by Union; Stanley **actually resists charm with natural 20 / 22** to start entry. |
| **~00:21–00:30** | Stanley's **illusory peaceful parents/family** not a true future flashback; two **distinct lich voices**, whose names are read variously **Egnails/Maggot Lord; Archeloft/Obtuserizer**. Verify names from audio or handout. |
| **~00:33–00:40** | “Kill switch” **explicitly speculation** by liches, and their **phylactery re-formation outside prison claim** is an offered escape scheme **not enacted**. |
| **~00:44–00:48** | Creature self-label **“Zach Soksy Sacks”** Q vs **“Zach soaxy sax”** P, high risk of ASR fabrication/phonetic splitting. “Nameless creator/emotion made matter” is creature testimony only. |
| **~01:26–01:30** | Nash has **pre-existing *Light* vegetable peeling on forehead** despite old S2E10 skull lantern; Union actually blindfolds captive Stanley but cannot immediately break charm. |
| **~01:41–01:49** | Hope cuts eye wall **with dagger + Hand cold**, telepathic screams for **37 and 28 psychic damage** on failed saves; **Union unconscious**, no instant death. Timing/order of saves vs deaths needs listening. |
| **~02:02–02:06** | **PRIVATE Hope–Voice dialogue**, ***Finger of Death* considered only, NOT cast**, Voice says **another portion of its power atop prison** (not confirmed Eye of Voice), and instructs Hope to **sing**. |
| **~02:07–02:16** | Hope, Nash, Tungsten sing, Stanley resumes and **uses guitar with familiar written song**; GM awards inspiration. **Creature dissolves and all tentacles/captives fall**, Vorel frees, Union stabilized. Song is NOT a magical casting by Nash. |
| **~02:22–02:27** | **Nash visibly removes ONE ring from bound corpse, then ACTUALLY WEARS IT**, senses release/data stream. Still **no verified new spell use/teleport**. Party bluffs liches it's a mere wedding band, lies successful (~24), **lich confrontation begins but no rounds finished**. |

**Review coverage:** Entire Parakeet primary read chronologically (approx. 00:00–00:17; 00:17–00:42; 00:42–01:07; 01:07–01:32; 01:32–01:57; 01:57–02:22; 02:22–02:28:23). Complete Qwen file parsed and compared computationally; **selected independent Qwen excerpts** at ~00:00–00:04, ~00:26–00:39, ~00:43–00:48, ~01:25–01:29, ~02:03–02:18 and ~02:19–02:25. **NOT entire Qwen editorial read. No original audio listened.** No media/transcripts modified. Next verified played source: [S2E12 — Dust to Dust](../sources/The%20Wastes%20S2E12.%20Dust%20to%20Dust.parakeet.processed.srt).
