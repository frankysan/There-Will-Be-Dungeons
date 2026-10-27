# Delvers S1E06 — The Tower: whole-export ASR comparison (2026-10-25)

**Source-identity follow-up, 2026-10-27:** The [S1E07–S1E03 batch check](DELVERS_S1E07_S1E03_SOURCE_IDENTITY_2026-10-27.md#s1e06) verifies all comparison inputs listed in the historical report against their recorded Git blobs after CRLF-to-LF conversion only, and verifies their exact historical source paths in the recorded source commit. Raw bytes differ in line endings. This independently confirms local content correspondence with the originally pinned source revision. Earlier provenance statements remain dated history. Prior interpretive coverage, inter-ASR measurements, played cutoff and audio status are unchanged.

**Identity:** Played **Delvers S1E06 — The Tower**, distinct from S1E05 *Maximum Montage* and S1E07. Original spreadsheet lists S1E06 with publication around **2021-02-14**. The opening broadcasts a **new Saturday live schedule**, which does not date the fictional castle excursion or identify the exact podcast-publication day.

**Inputs:** Two complete SRT exports from private GitHub `frankysan/There-Will-Be-Dungeons-Transcripts` at commit `24b2c62932b64fc280c7f67eb31a0177306e094e`, matching the initially **clean** connected workspace `main` HEAD.

| Filename-inferred pipeline | Exact source | Blob SHA | Cues | Last SRT end | Word tokens |
| --- | --- | --- | ---: | --- | ---: |
| Processed Parakeet (primary) | [`Delvers S1E06. The Tower.parakeet.processed.srt`](../sources/Delvers%20S1E06.%20The%20Tower.parakeet.processed.srt) | `484ee2a69200d9d398d5ec22ba262336cca91c60` | **2,677** | **03:03:03.760** | **23,887** |
| Qwen Q8 / Canary CTC / Nemotron-labelled | [`Delvers S1E06. The Tower.qwen-q8.canary-ctc.nemotron.srt`](../sources/Delvers%20S1E06.%20The%20Tower.qwen-q8.canary-ctc.nemotron.srt) | `aebb3ad8a139653da4011296f3dffc3c764c46e9` | **4,266** | **03:03:03.340** | **23,890** |

## Exact full-export word comparison

**1,475 Levenshtein word edits / 23,887 Parakeet primary tokens = 6.17% inter-export disagreement.** The Qwen export contains **three more** normalized tokens overall. This is **not word error rate, comparative accuracy, audio-verified omissions or hallucinations**.

Procedure: extract every SRT cue in order, omit indices and timecodes, concatenate cue speech, strip optional `(speaker N)`, lowercase, remove straight and curly apostrophes, replace all characters except Unicode letters/digits by whitespace, tokenize on whitespace; compute ordered unit-cost insertions, deletions and substitutions. A rolling-row dynamic program bounded to a **3,000-token diagonal band** produced distance **1,475**. Because every path leaving that band would cost at least 3,000 (more than this candidate), the result is the **unrestricted exact optimum** for these normalized sequences. **11-token identical prefix** and **1-token identical suffix** excluded before DP. This comparison does not use timestamps as anchors.

**Research coverage:** The entire Parakeet stream was read chronologically through 03:03:03 in bounded ~35-minute intervals. Complete Qwen content was tokenized for exact distance; Qwen selectively read for the client/keep name, handed-out jars, badge ceremony, servants' attack, and **Dawnless Dunes** prophecy. This is not a claim of independent close reading of every Qwen cue, sound verification, or performed `tools/prepare_episode.py` run. No audio was accessed; no MP3 and SRT timing alignment, hash of underlying audio, speaker diarization or ASR inference settings were verified.

## Focused inter-source and editorial checks

| Approximate Parakeet SRT clock | Grounded finding / remaining verification |
| --- | --- |
| 00:00–00:03 | **Saturday schedule** and missed following weekend are broadcast business; guild montage recap and new rogue tools are not newly played shopping scenes |
| ~00:05–00:09 | **Bronze orientation and library key.** Cassius slips and calls the client `Mickels/Mikkels` (a farm name), **immediately corrects himself to Withers**. Don't manufacture a Mickels relative/dual owner. Foreword by `Impossible Diamonds` is read from new guide, not verified from the actual PDF |
| ~00:14–00:22 | **Helena Clearstone** supplies **two holy-water containers**, one whole container required after defeating the skull; **not another nonholy-water item**. Qwen cleanly supports her name where Parakeet is messy. Bronze **unnumbered chimera-shield** badges replace wood discs; don't backdate to S1E05's approval |
| ~00:25–00:34 | `Alexandre / Alexander Vanderbuck Withers`, owner of `Enzo Keep`; earlier bronze group missing, mirrors warned against, guild contract **350** with **up to 500 extra each** for preserving furniture. Client testimony about being rightful owner and family genealogy is not independently proven |
| ~00:55–01:06 | Skeletal carpenter repairs chair, **screams and attacks when spoken to**; Evelyn destroys it. Maid tries to open door and Koh braces it with a dagger; gardener and repair staff later ignore unprovoked movement |
| ~01:10–01:33 | First direct flameskull aggression comes after Evelyn's exploratory stone-door joystick ringing; broken stained-glass window, **Fireball**, Koh's failed climbing-sash dive and fall (5 + 5), Evelyn takes 12 fire damage, valuable upholstery burns |
| ~01:54–02:14 | Master's desk contains **three unrotted handout pages**: familiar glyphs, stone-door diagram and lever instructions. P and Q text support the **up–left–up–down–right then inward press** solution (not circle-the-joystick); incorrect attempt invites skull/Flaming Sphere; Krandal's ten-gallon water apparently douses sphere, party escapes through steam |
| ~02:14–02:36 | **Enzo Vanderbuck Withers**, apparently mirror-bound head of a decapitated body, claims a failed necromantic immortality spell made the skull his split consciousness and animated servants. No independent historical proof or actual handout/mirror examination. Koh hides identity of person he wishes to heal, Evelyn says **she seeks someone**. Enzo glosses rune `sky people` and `Dawnless Dunes`, calls the latter's underground **heart** awakening and predicts visible consequences **within a year**. **Qwen supports “Dawnless Dunes,” not `Dauntless`; earlier Parakeet near ~02:30 varies**. Do not assert prophecy as settled canon |
| ~02:40–02:56 | Distinguish **Koh's** psychic Soul Knife damage from nonmagical shortbow piercing (resisted), **Krandal's** Sacred Flame and Spiritual Weapon, Evelyn's Sacred Weapon/Compelled Duel, and enemy's Shield/Blur/Flaming Sphere. No proof initial rooftop damage was unresisted piercing |
| ~02:56–03:03 | Koh's Soul Knife kills the skull; catches it; **Evelyn pours one of two full holy-water jars**. Two **orange garnets** recovered and bagged by Koh. Mirror dims but is not removed/destroyed; servants cease moving. Return approx 7:30 PM. After later inspection the GM says **roughly 400 bonus gold** on top of guild's previously stated mission fee, without reiterating explicit per-member units. No shown level-up, XP adjudicated **off-air** |

## Source limitations and next actions

Open audio/listening priorities: owner's names **Alexandre Vanderbuck Withers / Enzo Withers**, exact founder portrait, **Helena**, **Belsuna**, **Dawnless Dunes**, mystery skull's pronouncements, whether the ending bonus was **400 each**, and which enchanted orders are delivered at mission start. Published handouts for adventuring-tier guild guide and castle symbols are **described in scene but were not read**. No SRT or MP3 was edited.

[Full source-first dossier](../delvers/episodes/S1E06.md) · [Delvers queue](../delvers/REVIEW_QUEUE.md).
