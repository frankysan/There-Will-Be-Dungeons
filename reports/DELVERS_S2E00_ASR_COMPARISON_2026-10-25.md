# Delvers S2E00 — Cassius at the Guild: complete ASR comparison (2026-10-25)

**Source-identity follow-up, 2026-10-27:** The [S2E02–S2E00 batch check](DELVERS_S2E02_S2E00_SOURCE_IDENTITY_2026-10-27.md#s2e00) verifies both complete local exports against their recorded Git blobs after CRLF-to-LF conversion only, and verifies both source paths in the recorded source commit. Raw bytes differ in line endings. This independently confirms local content correspondence with the originally pinned source revision. Earlier provenance statements remain dated history. Prior interpretive coverage, inter-ASR measurements, played cutoff and audio status are unchanged.

**Archive type/placement:** The owner-normalized archive labels this **S2E00**, but both recordings narrate an **in-universe guild-academy cutaway** while the Darkest Delvers are at the kuo-toa village and announce **next week's S1 finale**. **Do not renumber the archive item** or place the academy hearing after S1E12 simply because its ID begins S2. It is **not an interactive player session or retrospective Q&A**. Provenance: private `frankysan/There-Will-Be-Dungeons-Transcripts` at exact repository/workspace `main` HEAD **`5a024d072e3a5a65d7e0bc15675b1bed9ce9459d`**, fetched Git blobs as below.

| Export / file-label pipeline | Exact source | Git blob | Complete cues | Last cue end | Normalized tokens |
| --- | --- | --- | ---: | --- | ---: |
| Parakeet processed | [P](../sources/Delvers%20S2E00.%20Cassius%20at%20the%20Guild.parakeet.processed.srt) | `105b185598848ff09e8df3183d9a1804544e9493` | **173** | **00:10:36.380** | **1,451** |
| Qwen Q8 / Canary CTC / Nemotron-labelled | [Q](../sources/Delvers%20S2E00.%20Cassius%20at%20the%20Guild.qwen-q8.canary-ctc.nemotron.srt) | `4fccc6a466ffaabbf8a73263aaef0acd1e94dda2` | **220** | **00:10:58.500** | **1,456** |

## Whole-export metric

**80 exact ordered word-level Levenshtein edits / 1,451 Parakeet normalized tokens = 5.51% inter-ASR textual disagreement**. Qwen includes **5 more normalized tokens**, and last SRT cue ends **22.120 seconds later** than Parakeet. These are **textual and clock differences, not WER, accuracy, verified omissions or hallucinations**. Both full exports were read in order through the end; **original audio was not listened to**, nor were timestamps aligned to the local MP3. Filename pipeline labels do not independently prove settings or same recording bytes.

Method: parse **every SRT cue**, discard cue indexes and timing, strip `(speaker N)`, join speech in order; Unicode lowercase, remove straight/curly apostrophes without replacement, change all non-letter/digit runs into whitespace and split. Compute full exact unit-cost insert/delete/substitute **Levenshtein distance** using a two-row dynamic-programming matrix (no banded approximation). Result **80**. Both source Git blob IDs are recorded above; no source files modified.

## Notable transcript disagreements and source interpretation

| Approximate clock | Supported distinction / follow-up |
| --- | --- |
| ~00:00–00:02 | **Aegis/Eegis** name differs, established working name in campaign is Aegis. Academy auditorium **Radiant Lance Theatre** supported across both. `Numilari/New Malarie` finance-governors, `Ivorn/Iphorn the Just` and Keld guildmaster remain ASR-phonetic and should not be hardened into canonical spelling. |
| ~00:03–00:05 | Board hears evidence including **Horn of Blasting** and **psychic spear shafts**, presented by Carrie. The board's claim about ancient elf defenses, reports of hook horrors being extinct/a related group, and “ancient evil” awakening are **statements/beliefs** rather than new independent physical proof. |
| ~00:06–00:09 | City history: Proudface temple, an uncertain final battle, Class V Oni incursion and a behir in “thirty-four”; names `Loran/Loren`, `Strongfair/Stormfair`, `Temwater` unclear. `Tumin Maximus` apparently **hand-selected Delvers**, divination elder asserts they are chosen. **Cassius's negative descriptions of Krandal/Koh/Evelyn are his opinion**, not episode-play adjudications. The **board's mention of Cassius's “condition” cannot support diagnosing him**. |
| ~00:08–00:10 | Board **denies** gold-rank funding and announces **Selenar Everbloom's forthcoming inspection**. The Bronze Ball/Withers donations are **future and past statements** rather than money handed over. All of these events occur **before the S1E12 finale**, despite S2E00 ID. |
| ~00:10–end | **Final cue difference: Parakeet 00:10:36.380 versus Qwen 00:10:58.500**. Qwen includes isolated **“Oh”** after season-two cast/guest teaser. The 22.120-second tail could reflect variant silence/audio/outro handling or spurious ASR; **no audio proof to choose between explanations**. |

## Remaining verification

Listening windows DEL-S2E00-001–006 are enumerated in the [dossier](../delvers/episodes/S2E00.md). The next owner-normalized archive item is [S2E01 — Very Snakey](../delvers/SOURCE_INVENTORY.md); no S2E01 narrative has been inspected here. Original MP3 source, speaker voices and written guild names unverified, and **no project linter or tests run**.

[Episode dossier](../delvers/episodes/S2E00.md) · [review queue](../delvers/REVIEW_QUEUE.md).
