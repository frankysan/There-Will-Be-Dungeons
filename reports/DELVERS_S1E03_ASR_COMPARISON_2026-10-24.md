# Delvers S1E03 — recovered-source ASR comparison (2026-10-24)

**Source-identity follow-up, 2026-10-27:** The [S1E07–S1E03 batch check](DELVERS_S1E07_S1E03_SOURCE_IDENTITY_2026-10-27.md#s1e03) verifies all comparison inputs listed in the historical report against their recorded Git blobs after CRLF-to-LF conversion only, and verifies their exact historical source paths in the recorded source commit. Raw bytes differ in line endings. This independently confirms local content correspondence with the originally pinned source revision. Earlier provenance statements remain dated history. Prior interpretive coverage, inter-ASR measurements, played cutoff and audio status are unchanged.

**Identity correction completed for text:** This is the comparison of the **actual S1E03 — Raw End Of Joke Stick** exports whose filenames contain **`(corrected)`**. Both older **uncorrected** S1E03-labelled files are **S1E04** and remain unchanged. Their former **7.65%** metric stays in [S1E04's report](DELVERS_S1E04_ASR_COMPARISON_2026-10-24.md). [Source identity audit](DELVERS_S1E03_SOURCE_IDENTITY_2026-10-24.md) · [Real S1E03 dossier](../delvers/episodes/S1E03.md).

| Export | Exact file under `sources/` | Blob SHA | Cues | Final SRT end | Normalized tokens |
| --- | --- | --- | ---: | --- | ---: |
| Parakeet processed (P) | [corrected Parakeet](../sources/Delvers%20S1E03.%20Raw%20End%20Of%20Joke%20Stick%20%28corrected%29.parakeet.processed.srt) | `f7a2823f5b2ad8e048a324c2a05d9789cbcf5506` | **2,401** | 02:49:33.070 | **22,025** |
| Qwen Q4/Canary CTC/Nemotron | [corrected Q4](../sources/Delvers%20S1E03.%20Raw%20End%20Of%20Joke%20Stick%20%28corrected%29.qwen-q4.canary-ctc.nemotron.srt) | `bd0e0373989511d9045eec74ecc06f3325a896da` | **3,777** | 02:49:32.730 | **22,002** |
| Qwen Q8/Canary CTC/Nemotron | [corrected Q8](../sources/Delvers%20S1E03.%20Raw%20End%20Of%20Joke%20Stick%20%28corrected%29.qwen-q8.canary-ctc.nemotron.srt) | `da85b4f44a0d397c64670dc3fac2397e343bf34c` | **3,995** | 02:49:32.730 | **22,056** |

**Revision:** All three complete SRT source contents retrieved from the connected GitHub repository `frankysan/There-Will-Be-Dungeons-Transcripts` at commit `4c94049d48e45d4ac589f038d593619c9d2bf068`, consistent with the initial workspace HEAD. The MP3 `local/Delvers S1E03. Raw End Of Joke Stick (corrected).mp3` is present by filename, but workspace binary reading returned **access denied**. MP3 contents, exact synchronization, model settings, and matching input audio hashes were **not** independently verified.

## Exact full-export word-distance calculation

| Comparison | Unit-cost word edits | Reference tokens | Inter-export disagreement |
| --- | ---: | ---: | ---: |
| **P vs Qwen Q8** | **1,627** | **22,025** (P) | **7.39%** |
| **P vs Qwen Q4** | **1,659** | **22,025** (P) | **7.53%** |

Method: split all SRT cue blocks, exclude cue numbers and timecode headers, concatenate text following each header, remove `(speaker N)` decorations, lowercase, remove straight and curly apostrophes, replace characters other than Unicode letters and digits with spaces, then tokenize on whitespace. Calculate ordered **Levenshtein insert/delete/substitute distance, unit cost 1**. Common exact prefix (15 tokens) and suffix (2 tokens) excluded before dynamic programming, within a **2,600-token diagonal band**. Both returned distances are strictly **below** that band, proving the constrained optimal path cannot have crossed its boundary; both measurements are exact for these normalized token streams. No `tools/prepare_episode.py` run, no audio verification and no time-aware alignment is claimed. These numbers are **not WER, ASR accuracy, verified omissions or hallucination counts**. Q4 and Q8 are filename-inferred pipeline names.

## Evidence-bearing listening targets

| SRT clock | Context, disputed details and action |
| --- | --- |
| ~00:00–00:03 | Syndicated dairy/sports adverts before program opening may shift seek positions relative to other audio downloads |
| ~00:08–00:13 | Koh's wife seems `Anthela/Anathela`; six-year-old daughter **Penelope**; bedridden wife, exhausted fortune and the guild-healer **cover story** are supported by primary context. Verify spelling/nanny naming with audio or written source |
| ~00:13–00:17 | Rat-person guild night acquisitions clerk **Jimmy** is actually encountered, resolving S1E02's unidentified rat-like figure |
| ~00:27–00:36 | Koh **apologizes to Krandal** for last mission's friendly fire; Cassius explicitly assigns **sighting only, no killing required**. Do not invent accepted reward for extra gricks |
| ~00:38–00:52 | Cart companions `Demetrios Dimontino`, `Fidra Norgoth`, `Didi`; moon-cult god **imprisoned beyond moon** is NPC belief, not verified cosmology; no death of this session's humanoid |
| ~00:56–01:03 | A **wooded thrush Yuri** is revived from abandoned trapper cart and pocketed by Krandal. His fate after S1E03 remains unverified |
| ~01:19–01:26 | Two **hippogriffs** are encountered, but deterred/avoided without combat |
| ~01:45–01:56 | **Veggie Sticks** introduces himself and claims he knows all in his woods, a boast S1E04 later retracts; he **permits passage** and remains at rim |
| ~01:59–02:24 | Krandal finds **crypt-like black goo** in fountain; Evelyn finds carved symbols and **old Elvish tablet**. Only **'sky people'** provisionally deciphered. Abandoned Sacred Flame target replaced by harmless Thaumaturgy bush shake |
| ~02:25–02:30 | **Evelyn kills the first played grick**, following Koh's strike; Krandal takes nine HP from the initial tentacles. Later statement of four kills across S1E03–S1E04 counts Evelyn's kill, not an invented additional prior kill |
| ~02:34–02:47 | Koh's **enchanted climbing sash is still ascending** with ordinary rope attached, Evelyn has not escaped with tablet, extra gricks closing; S1E04 begins with recap of this very cutoff |

## Coverage and next checks

The **complete Parakeet source** was read sequentially from advertising to final network outro; the **entire Q4 and Q8 content** was parsed for metrics, with selected context compared. This does not mean complete independent close reading of each Qwen utterance. Audio unverified; Qwen punctuation/variant wording cannot establish exact names or audio fidelity. Original ASR and MP3 bytes were not modified.

The recovery eliminates the artificial S1E02-to-S1E04 source gap: **S1E03 now supplies the played grick assignment, journey, family revelation, Veggie Sticks encounter and first grick kill**; [S1E04](../delvers/episodes/S1E04.md) owns the remaining combat, escape and guild payment. Continue with [review queue](../delvers/REVIEW_QUEUE.md).
