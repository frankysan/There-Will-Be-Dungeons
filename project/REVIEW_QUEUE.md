# Review queue — pilot

These are **outstanding checks**, not completed corrections. References give approximate positions in the original episode audio.

| Priority | Episode / time | Concern | Suggested action |
|---|---|---|---|
| High | E000 00:13:07–00:13:28 | “Now” is the last word; processed Parakeet cue is placed at 13:20–13:28 while raw ends by 13:11 | Retimestamp final word from audio; exclude musical tail |
| High | E001 00:00–00:13 | Baseline/chunked Parakeet recognize `no m h` in intro; default VAD misses `hello everybody` while baseline and padded VAD capture it | Listen for genuine speech versus music/noise; verify opening greeting |
| High | E001 01:23–01:42 | Five Parakeet runs disagree on short conversational speech; chunked runs substitute `i guess` for other runs' greetings to Kyle; turning LCS dedup off changes nothing | Verify turn-by-turn dialogue and overlap against original audio |
| High | E001 02:17–03:08 | Variants differ in `yeah`, `you're sweating`, `armpit`, `finality`; 700 ms VAD duplicates near-simultaneous `if` | Listen and build a verified transcription regression sample |
| Medium | E001 04:13–08:45 | Variants disagree around reactions, false starts and the Dusthill setting narration; `Dusill` and concatenated words recur | Compare audio and external spelling references without overwriting raw output |
| Medium | E001 10:00 boundary | Both 30 s chunked runs timestamp their final word to 10:00.800, beyond the requested 600 s window | Check chunk-alignment timestamp clamping |
| High | E001 00:47:00–00:48:00 | Listener-confirmed Cohere omission; Parakeet/Qwen cover more speech | Verify Parakeet wording against audio; add passage to ASR regression suite |
| High | E001 01:55:00–01:56:00 | Second listener-confirmed Cohere omission | Verify Parakeet wording against audio; add regression sample |
| High | E001 throughout, notably 00:58, 01:17 and 02:31 | Sixth diarization cluster is Scott doing a voice | Check short boundaries; use `Scott` in final draft but preserve cue provenance |
| High | E000 00:03:49–00:07:18; E001 01:09 | Nash family name transcribed Maggard/Magard/Maghard | Wiki spelling **Nash Maggard** documented; verify individual audio wording |
| High | E000 00:11:41–00:13:11 | Vorel name and longer name; Verithica/Caegro uncertain | Wiki confirms written **Vorel Rasvim Kurik**; listen to introduction for phonetics and other geographic names |
| Medium | E001 00:15:31–00:15:43 | Tiefling's personal name Orifi/Orify uncertain; “Hope” confirmed as desired name | Wiki supports **Oriphi “Hope” Akmenos**; retain original ASR naming exchange until listening review |
| Medium | E001 00:18:03 and 00:41:27 | Gimster/Gymster; Shun T and related spellings | Later-episode wiki summary supports **Jimster** and **Shun'ti Stoutbarrel**; verify early audio and avoid retroactive surname insertion |
| Medium | E001 00:16:13 and 00:42:15–00:42:44 | Tavern mentioned in player dialogue; DM later states there is no tavern | Treat as discrepancy/scene revision; do not canonize a tavern |
| Medium | E001 03:01–03:02 | Dramatic ending includes a gun, light, a skull wall; precise actor and actions require careful review | Confirm detailed sequence before definitive scene summary |
| Medium | E001 entire | Post-processed Parakeet transcript has changed cue boundaries and text relative to separate raw run | Sample-check against raw and source audio; identify systematic changes |
| High | E001 00:23:21 and 01:51:13 | Q4/Q8 recognize different amounts of conversational speech, including a possible Scottish-accent aside | Listen to audio, determine which extra words are genuine |
| High | E001 02:13:40 | Q8 includes an additional phrase absent from Q4 (`voodoo and the steeple and the antenna`) | Verify with audio; do not insert into canonical transcript automatically |
| Medium | E001 throughout | Q4 and Q4+Canary yield identical words but 924 word-level speaker-ID differences | Compare selected turn boundaries against audio; keep diarization correction independent of aligner choice |
| Medium | E001 Q4/Q8 raw | Q4 without Canary has 56 invalid durations; Q8 raw has 64, while Q4+Canary has zero | Validate Q8+Canary only if Q8 wins lexical accuracy comparison |
| Medium | E000 00:04 and 00:07 | Q4 `Nash Magard` versus Q8 `Nash Maggard` | Wiki supports **Nash Maggard**; retain all original model outputs |
| Medium | All future episodes | More voice acting may split individuals into additional diarizer IDs | Track per-episode aliases only; never map an ID globally |

## Resolution format

When a question is settled, record `resolution`, `evidence/audio checked`, `correction applied`, and `date`, then transfer spelling resolution into `world/CONSISTENCY_LEDGER.md` and the episode-specific correction log.

For full settings, measures, and evidence qualifications, see the [Parakeet segmentation benchmark](../reports/PARAKEET_SEGMENTATION_2026-10-21.md).
