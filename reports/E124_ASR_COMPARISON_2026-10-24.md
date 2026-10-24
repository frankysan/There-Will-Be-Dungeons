# E124 ASR comparison — 2026-10-24

**The Wastes · corrected S1E124 — Bow To The Fish Bird · played session.** Original catalogue **TWBD 126**, owner catalogue date **2020-11-09**; recording date unverified. [Dossier](../episodes/E124.md) · [Research queue](../project/REVIEW_QUEUE.md). **ASR-only, not audio-verified**; original sources unchanged.

## Inputs, access and review scope

Direct checkout began clean on `main`, HEAD **`0c8b32e68f79b18668433f911c052a48ea18a56e`**, matching connected workspace status. GitHub numbering policy was read at that **explicit ref**; remote access does not expose ignored local audio. Direct filesystem supplied the exact exports, matching-named MP3 and retained owner catalogue snapshot. No raw private messages were used or published.

| Filename-derived label | Exact source | Bytes | Cues | Normalized words | Final end |
| --- | --- | --- | --- | --- | --- |
| Parakeet processed | [The Wastes S1E124. Bow To The Fish Bird.parakeet.processed.srt][p] | 200,380 | 2,033 | 18,550 | 02:28:52.120 |
| Qwen Q8 / Canary CTC / Nemotron | [The Wastes S1E124. Bow To The Fish Bird.qwen-q8.canary-ctc.nemotron.srt][q] | 271,649 | 3,326 | 18,742 | 02:28:51.780 |

Both begin **00:00:08.640**. Labels are **inferred from filenames**, not verified model/run settings, independent acoustic inputs or measured performance. **Every primary cue was read through the outro** in fifteen ten-minute windows, with a narrow boundary reread. Secondary was **fully parsed for the metric**, with selected editorial windows **00:22–00:29, 00:36:30–00:39:42, 00:50–01:10, 01:21–01:34 and 02:10–02:25:42** read. **No complete secondary interpretive review is claimed**.

A **targeted prior-source check only** read E115 naming cues: [Parakeet](../sources/The%20Wastes%20S1E115.%20The%20Forest%20for%20The%20Trees.parakeet.processed.srt) **1635–1639**, [Qwen-labelled](../sources/The%20Wastes%20S1E115.%20The%20Forest%20for%20The%20Trees.qwen-q8.canary-ctc.nemotron.srt) **2610–2624**, ~01:51:19–01:51:35. Both explicitly identify the baby-form boy and name him Junior; this is preserved alongside E124's later daughter assignment. **No complete new E115 review or metric is claimed**. Supplementary source hashes and exact windows retained in the local checkpoint.

SHA-256:

- Parakeet: `3f2379333effa2f8e778c3bb6ada22bc4c55d12692a31794b6dfab8ebaab209a`.
- Qwen-labelled: `d5b27a54782daa8f1e5e0707efcb4473a26cdd2e0a79cb4ca4d4bdb53f1d1161`.
- Matching ignored `local/The Wastes S1E124. Bow To The Fish Bird.mp3`: **143,050,897 bytes**, SHA-256 `cc02c9e61dedf5046eac0edf47d464bd10aadecadfa2dfdd626048fb3b3bc991`, ffprobe duration **8,912.332500 seconds (02:28:32.333)**. Primary/secondary endpoints are **19.788 / 19.448 seconds later**. **Historical ASR input/copy identity and clock relationship remain unverified**; no listening or claimed constant alignment correction.

## Reproducible whole-export measurement

`tools/prepare_episode.py` prepared both complete exports in ignored `local/episode-analysis/E124`, reusing `build_transcripts.parse_srt` and the exact shared `asr_metrics` implementation. Extract chronological cue content without indices/timing or optional speaker decorations; lowercase, delete straight/curly apostrophes, split on non-Unicode letters/digits. Compute **unit-cost ordered word-level Levenshtein over the full sequences**, with the primary as denominator.

**1,529 edits / 18,550 primary normalized words = 8.2425876011% (8.24%) text disagreement.** Secondary has **192 more words**. **This is not WER, accuracy, confirmed omissions, or a ranking of either model.** Neither majority agreement nor word-count advantage establishes truth.

The separate time-aware alignment produced **1,245 candidate hypotheses**: **612 conflicting recognition**, **595 possible omission**, **38 uncertain segmentation**. These are not the global edit count or audio-adjudicated classifications. Both exports have **zero nonpositive cue durations**. Primary has no adjacent overlap; secondary cues **523/524** overlap by **1 millisecond**, at **00:19:15.959–00:19:15.960** (`all buoyant.` / `And she she kicks up...`). This is a file-timing observation, not proof of overlapping speech. SRT cue intervals are **not word timings**.

## Material wording and evidence risks

| Recording clock | Primary / secondary reading or shared risk | Editorial consequence |
| --- | --- | --- |
| ~00:23–00:28 | Husband `Lelu/Leilu` versus `Lelou/Lilu`; Fishbird/Malhya forms vary. | Retain alternatives; Emenil's widowhood/reverend/persecution account is testimony, not a newly observed death or an author-confirmed name. |
| ~00:28:04–00:28:38 | `barrow saurus` / `Barosaurus`; `cheater dian tallus` / `Cheetah, Dian Talos` (candidate IDs d00210–d00212; primary 434–435, secondary 674). | Preserve title variants and self-recital status; earlier list explicitly skipped. Keeper of Stories is an existing title. |
| ~00:50–00:55 | Both depict two disappearances and return; “permanent banishment” followed by actual restoration. | No death/resurrection; Stanley and Nash lack the intervening dialogue and do not see one another in the void. |
| ~00:59–01:04 | `Groxl/Grojil` versus `Gergil/Grosjean`; both have ambiguous “the one he slew ... he ... unmaker.” Both expressly cure Diontalus's debuffs. | One Eye of Groxl; divine lore remains attributed/antecedent unresolved. Actual cure resolves E123 drain, without inventing final stat values. |
| ~01:07:25 | Primary `faerun`, secondary `Favron` (d00496; primary 889, secondary 1454). | Unnamed engineer last near an uncertain world; no confirmed Faerûn import, engineer identity or present location. |
| ~01:23; ~01:43 onward | `Amanthalodar/Amenthalodar/Amantha Lodar`; core `Cadulate/Cadgilet`. | Working names only; promised Slack spelling was not examined. High Elf's political/theological history remains his account. |
| ~01:26–01:28; ~01:42–01:45 | Both explicitly use **Bok Bok and Squirts** for the household roster. | Agreement does not resolve the conflict with Squirts's E111 disintegration/E115 memorial. No revival played; Chunks substitution is not silently accepted. |
| ~01:32:06–01:32:25 | Both retain the bonus decision: Nash Junior female/daughter. | Main-session confirmation of the later assignment; **E115 ~01:51:19–01:51:35 named the baby-form boy Junior**. Preserve both episode-era assignments and E114's birth count; no in-story transformation depicted. |
| ~02:15–02:18 | Undoing phrase `care laundry me he jaju my heistita` / `Care, laundry, meji, jajul, my histita`; d01140 samples the final-word conflict. | Hope-only Voice claim, twice refused killing order; phrase neither performed nor validated. Do not repair pseudo-language or treat it as Nash casting. |
| ~02:23:55–02:25:34 | Primary `if he does not if he dies` / secondary `if he does not, he dies` have punctuation/segmentation ambiguity; both threaten station, agree own court and end with request/“yes.” | Preserve conditional coercion; no newly witnessed death. Agreement and promised aid are shown, physical departure and assistance are not. |
| ~02:25:34–02:28:52 | Social-victory congratulations, hiatus discussion, toilet-world joke and outro. | No additional adventure, time jump or household roster correction from the “baby Chunks” credit. Local audio ends before both export clocks. |

## Decision and listening queue

Use **ASR-provisional documentation** for the complete primary account, with the material second-export readings above. Prioritize **Eye/unmaker antecedent, explicit cure, Squirts/Chunks roster, private undoing phrase and final accord**, then uncertain names/titles and child mapping. Establish the audio-copy relationship before mapping these SRT clocks to precise listening windows. No original transcript reconciliation, ASR rerun, audio review or performance evaluation occurred.

**Next source verified:** Wastes **S1E125 — A Case of Malpractice**, both exact exports present/nonempty and not analyzed. Main continuity remains at **E124's negotiated scene cut**.

[p]: ../sources/The%20Wastes%20S1E124.%20Bow%20To%20The%20Fish%20Bird.parakeet.processed.srt
[q]: ../sources/The%20Wastes%20S1E124.%20Bow%20To%20The%20Fish%20Bird.qwen-q8.canary-ctc.nemotron.srt
