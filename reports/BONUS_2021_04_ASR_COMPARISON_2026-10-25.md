# Bonus 2021-04 — April 2021: ASR comparison (2026-10-25)

**Source type:** Out-of-game bonus Q&A, primarily retrospective discussion of **Delvers Season One** with minor Wastes/cast/media remarks. **Not** a Delvers played episode, nor proof of future Season Two actions. Owner-normalized archive `Bonus 2021-04 - April 2021`, spoken month/year not explicitly given in greeting. Exact source revision: clean connected workspace/GitHub `main` **`035844d77a97f739cdedf681dadea45d4840c15e`**. Two complete exports reviewed textually to sign-off, **no original MP3 listened**, recording day, publication day, precise audio/SRT offsets and model-run settings unverified.

| Export | Exact source | Git blob | Cues | Final cue end | Normalized words |
| --- | --- | --- | ---: | --- | ---: |
| Parakeet processed (primary) | [P](../sources/Bonus%202021-04%20-%20April%202021.parakeet.processed.srt) | `a4254c48ca8c68c871958736aa992a9bd4f62b0e` | **740** | **00:38:54.320** | **7,067** |
| Qwen Q8 / Canary CTC / Nemotron-labelled | [Q](../sources/Bonus%202021-04%20-%20April%202021.qwen-q8.canary-ctc.nemotron.srt) | `d28d07b6f122ccf070d73d8bfd569ff7ae48be5a` | **1,078** | **00:38:54.150** | **7,220** |

## Exact normalized whole-export comparison

**479 unit-cost ordered-word Levenshtein edits / 7,067 primary Parakeet word tokens = 6.78% inter-ASR textual disagreement**, **not WER, transcription accuracy, audio-verified omissions or hallucinations**. Qwen has **153 more normalized words**; final cue ends **0.170 seconds before** Parakeet. This metric **does not pair cues by clock or diarized speaker**.

Method: parse entire SRTs, remove cue indices and timecodes, strip optional `(speaker N)` decorators, join bodies in order, Unicode lowercase, **remove straight/curly apostrophes without adding a space**, replace other nonletter/nondigit spans by spaces, tokenize. Compute unit-cost insert/delete/substitute dynamic programming with **1,300-word diagonal band**. Returned distance **479, strictly below band width**, so any alignment leaving band must cost >= 1,300 and cannot beat it: **global optimum exact**, not extrapolated. Both complete P/Q exports were semantically inspected in chronological 4-minute sections, with detailed primary and cross-source Qwen review. Source SRTs unchanged.

## Text-only source risks

| Approximate recording clock | What differs or remains uncertain |
| --- | --- |
| ~00:00–00:04 | Names `Splenderbelt/Splunderbelt/Splendo`, `Grinkeeper/Grimkeeper/Greenkeeper`, `Koh/Co`. Retrospective intent behind surnames and hiding high-born backgrounds is well supported, but **does not tell PCs a new secret**. |
| ~00:04–00:08 | Cockatrice scar **healed** by accumulated magical healing per GM. **12-episode season structure** is production intent, not a universal rule requiring all arcs to end in 12. |
| ~00:08–00:14 | Upcoming **Bronze Ball** and Snake Island described as future/enthusiastic; **no scenario outcome**. **Same lake system**, not identical lake, is explicit Kyle claim; alternate pit passages **not party-discovered**. |
| ~00:14–00:20 | `Ouroboros` speculative other RPG setting, `The Last God` media, `Big Bleeper Bloops` preferred NPC and `Bach/Bok-Bok` comparison are **speaker-attributed and partly proper-name provisional**, not evidence of shared fictional continuity. |
| ~00:22–00:27 | Kyle's **unvisited hidden Skull Keep basement and alchemy lab**, grick-site tablet missed, and hypothetical casualties from choosing other wells are **unplayed branches**. Cast says **Greatsword of Wounding given back to Broadside**; record as **retrospective custody correction** without inventing in-game time of handing it over. |
| ~00:27–00:31 | Potential guest appearance is an **invitation, not scheduled event**; avoid importing sensitive personal discussion into in-universe canon. |
| ~00:31–00:38:54 | Krandal’s less overt zeal, Koh’s low-Charisma adaptation and discarded **Phantom rogue** plan, Evelyn’s former **~16** concept changed to **~18** and unperfect school record are creator-development perspectives. **No Phantom level, cured wife, farm, promised future event or confirmed age of 16 in played story**. |

## Recommended audio checks

See [dossier review keys](../episodes/BONUS-2021-04.md): speaker identity near ~00:01–00:04 and ~00:25–00:27, Skull Keep hidden room wording, the Greatsword handover, proper-name variants, Evelyn's revised age, season-two previews, and original episode-relative clock. No local transcription runner was used and no audio-level correctness has been established.

[Bonus dossier](../episodes/BONUS-2021-04.md) · [project queue](../project/REVIEW_QUEUE.md).
