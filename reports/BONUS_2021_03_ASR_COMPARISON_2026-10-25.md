# Bonus 2021-03 — March 2021: exact ASR export comparison (2026-10-25)

**Identity/type:** The archive owner's monthly label is `Bonus 2021-03 - March 2021`, explicitly called **March 2021** in both transcripts' opening. **Out-of-game Q&A**, not played Wastes or Delvers content. Private GitHub repository `frankysan/There-Will-Be-Dungeons-Transcripts`, revision **`d3fda6963cb7536bfaf0869354beb24f43db86f9`**, aligned with initially clean connected workspace `main` HEAD. Audio **not listened to**, MP3/SRT offset, real recording date, original source-audio byte identity and model-run metadata **not independently verified**.

| Export (pipeline inferred from filename only) | Exact source | Git blob SHA | SRT cues | Last end | Normalized tokens |
| --- | --- | --- | ---: | --- | ---: |
| Processed Parakeet (primary) | [SRT](../sources/Bonus%202021-03%20-%20March%202021.parakeet.processed.srt) | `8f57baebf73db15de2bdb352802aca0a07c5e486` | **607** | **00:30:52.150** | **5,646** |
| Qwen Q8 / Canary CTC / Nemotron-labelled | [SRT](../sources/Bonus%202021-03%20-%20March%202021.qwen-q8.canary-ctc.nemotron.srt) | `51a575c1babf61855590469a16bd01a6d202855f` | **890** | **00:30:51.880** | **5,734** |

## Exact normalized word-edit distance

**312 edits / 5,646 primary words = 5.53% inter-ASR textual disagreement**. Qwen contains **88 more normalized tokens**, with last cue end **0.270 seconds earlier** than primary. This measure is **not WER, transcription accuracy, a hallucination count, an omission count or evidence of which output is right**.

Method: parse **all cue bodies** from both complete SRT exports, remove indexes/timing and optional `(speaker N)` decorations; join speech in order; lowercase, remove straight/curly apostrophes without spaces; replace any run other than Unicode letters/digits with a space; split on whitespace. Compare full ordered token streams using **unit-cost (substitution, insertion, deletion) Levenshtein** with 2-row DP and a **1,500-token diagonal band**. Because the 312-edit solution is **strictly inside/less than the 1,500-token width**, any path wandering outside the band would require at least 1,500 insertions/deletions and cannot be shorter: the result equals the **global exact** ordered distance. No cue/time alignment or audio correction is inferred.

**Interpretive coverage:** Parakeet was read chronologically from first words to sign-off; both exports parsed completely for numeric result; secondary **selectively close-read** at intro/calendar, Delvers player-character inspiration, guild gear, suggested module, Vorel barbarian-path clarification, critical-hit/initiative house rules, and hypothetical PvP tournament. Not an independent complete Qwen editorial pass. No source media edited, audio listened, clip seek calibration, source PDFs/handouts inspected, provider run settings checked, local `prepare_episode.py` run, or testing/lint run.

## High-risk text differences and listening targets

| Window | Assessment / interpretation risk |
| --- | --- |
| ~00:00–00:02 | First question appears Parakeet as **“when not in coded”**, Qwen as **“when not in COVID”**. Pandemic context favors latter, **not audio-proven**; “Nerdtacular” convention name likewise varies. March 2021 host label agrees across exports; **publication day still unknown**. |
| ~00:02–00:05 | Several speakers imagine **themselves** as fantasy classes/races; ASR provides no reliable diarization for individual assignments. Only attribute when introduced by name (e.g., Kristen's halfling). Do not convert to player-character classes. |
| ~00:05–00:09 | **Scott/Krandal**, **Jon/Koh**, **Kristen/Evelyn** design motivations follow cast mentions, but game names vary; Parakeet `Immortals Phoenix rising` vs identifiable title `Immortals Fenyx Rising`, and anime list **Cardcaptor / Escaflowne** punctuation unresolved. Jon's daughter-name anecdote is **creator biography**, not a retconned Delvers event. |
| ~00:09–00:14 | `bugman` blacksmith story explicitly DM's **improvisation**, not proof the smith was a bugman. Shared-item custodianship is distinct from legal/played equipment ownership; guild's **Soul Knife**, **climbing sash** and **drift globe** are different possessions. |
| ~00:13–00:17 | Question about **painting at Skull Keep** is not proof any item collected, destroyed or magical effect undone. Cast **describe** supporter report-card PDFs and partly imagined guild handbooks, not verified document text or a scheduled campaign module. |
| ~00:17–00:19 | A listener incorrectly assumes Kyle's Wastes barbarian was **Berserker**; Kyle corrects to **“Path of Storms”** and fire effects. Preserve this contrast instead of reporting Berserker as fact. |
| ~00:21–00:24 | House-rule **critical** requires initial natural 20, then **second modified d20 normal hit vs AC**; bosses may suffer alternative severe plot effect, and a gelatinous cube/ghost may lack anatomy for instant kill. **Initiative preset to 10 or precomputed only when not consequential**; explicit rolls when timing matters. These are **speaker's explanatory intent**, not proof every prior scene adjudicated exactly as described. |
| ~00:24–00:30 | Acquisitions Incorporated is **not a Delvers source Kyle says he used**; PvP bracket purely imaginary, not actually played. No “Nash versus Stanley” combat/rebalance or new character canon. |
| ~00:30–end | Closing supporter Q&A invitation agrees across sources; actual next recording day unverified. Owner's **April 2021 bonus** pair is inventoried, but host's “next month” is still a future-plan statement in this March recording. |

## Outstanding verification

Listen to source audio in the above bounded windows; verify publication month/day and audio-duration offset, speaker mapping for self-insert choices, full player-name/campaign references, exact guild guide PDF and competing title spellings. Preserve model outputs and report any audio-verified changes with clip times and verified speaker, not model-vote corrections.

[Source-first dossier](../episodes/BONUS-2021-03.md) · [Research queue](../project/REVIEW_QUEUE.md).
