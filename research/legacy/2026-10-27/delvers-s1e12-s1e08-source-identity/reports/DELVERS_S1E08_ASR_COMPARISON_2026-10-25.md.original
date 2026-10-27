# Delvers S1E08 — Need any help down there: ASR comparison (2026-10-25)

**Scope:** Played *Delvers* S1E08 including sponsor/edited recap, southwestern-well descent, underground dungeon, First Sons cooperation, temple-floor breakthrough, well passage sealing and unresolved gelatinous cube. Source at private `frankysan/There-Will-Be-Dungeons-Transcripts` pinned revision `6f36aecd601641ecea798e75be0024a1b64021e5`, matching the initially clean connected workspace `main` HEAD. No raw MP3 listened or audio equivalence verified.

| Filename-inferred pipeline | Complete SRT | Git blob SHA | Cues | Last cue | Normalized word tokens |
| --- | --- | --- | ---: | --- | ---: |
| Primary, processed Parakeet | [S1E08 Parakeet](../sources/Delvers%20S1E08.%20Need%20any%20help%20down%20there.parakeet.processed.srt) | `c33726511bd66309d593ecd9cc61d7b5dde4e24b` | **2,131** | **02:25:14.070** | **18,846** |
| Secondary, Qwen Q8/Canary CTC/Nemotron-labelled | [S1E08 Qwen](../sources/Delvers%20S1E08.%20Need%20any%20help%20down%20there.qwen-q8.canary-ctc.nemotron.srt) | `339b0a578cf1141b84639aec2580c5b41c73d21f` | **3,526** | **02:25:13.720** | **18,897** |

## Exact normalized whole-export measurement

**1,565 unit-cost ordered word edits / 18,846 Parakeet tokens = 8.30% inter-ASR textual disagreement**. Qwen has **51 additional normalized tokens**; final cue ends **0.350 seconds earlier**. This result is **not WER, transcription accuracy, an audio-certified omission or hallucination**, and subtitle-end agreement cannot prove a common input audio.

Method: Split all cues; discard cue numbers/timing; remove optional `(speaker N)` decorators; join all speech in chronological order; lowercase; remove straight/curly apostrophes; substitute any run of characters other than Unicode letters/digits with whitespace; split into words. Compute exact **insertion/deletion/substitution Levenshtein distance with unit cost** between full ordered token sequences. A two-row dynamic program with **2,000-word diagonal band** returned **1,565 edits**, strictly below the band boundary, proving the globally optimal path remains within it. **This is not cue-wise or time-aware WER**. Applied to source bytes at the pinned revision; no local `tools/prepare_episode.py` run.

**Interpretive coverage:** Parakeet export read chronologically in five bounded recording intervals through final network outro. Both full exports parsed for complete metric. Qwen selectively close-read for Brigand Patrol, Primordial speech, First Sons member names and ruin identity, armory/horn damage, sealing plan/aftermath and final threat. Qwen **not fully independently close-read** throughout; original audio, shared map, handout and historical D&D sheets **not checked**. Character/place spelling and map topology remain text-only.

## High-impact cross-source and interpretation checks

| Approximate SRT clock | Finding and transcription/research limit |
| --- | --- |
| ~00:03–00:20 | The recapped well oversight is superseded by **played descent**. `Dominic Reese` is supported in both transcripts, but spellings of fellow patrol members are phonetic; another squad's apparent Fireball at a different well **cannot establish safe water**. Concrete is still a single bag carried in this sequence. |
| ~00:24–00:33 | GM **corrects accidental six-foot rust juveniles to six-inch** in the dialogue. The stirge pouch produces eight stirges; Koh alone loses five HP in summarized combat. Apparent transcription of juvenile species and numbers must retain the GM's immediate correction. |
| ~00:33–00:43 | Qwen and Parakeet both present imperfect, heavily stylized creature/Primordial utterances; **do not invent exact translated warning**. Table discussion of Krandal's Primordial/Minotaur proficiency is partly improvised out-of-character backstory. Qwen contains unusually repeated phonetic `rrrr...` in this passage, making raw length/cue alignment particularly hazardous. |
| ~00:49–01:02 | Qwen `Edgar Boonefellow` / P `Edgar boonfellow`, `Norman Green` and `Faelan/Faelen Ianya` remain audio-provisional. First Sons Brotherhood **physically present**, three members; ruin is **similar to** previously explored forest structure, not definitely the same physical dungeon. A nonviolent claim dispute is settled by yielding the immediate exploration. |
| ~01:03–01:25 | First attempted platform crossing **triggers opening**; later lowering weight and jumping succeeds. Koh's shortbow arrow **pins needle button**; abandoned/submitted items in out-of-character duplicate-sheet cleanup must not be silently turned into in-world inventory loss. Bag of concrete **moves across** but not consumed here. |
| ~01:26–01:36 | Eight stone-metal rune shafts, six puzzle stations; Qwen says psychic `spears` and identifies **Horn of Blasting**. Evelyn blows it; **19 thunder damage to Evelyn and Krandal**, temporary deafness; Koh uses Psionic Whispers. Small crack shown on horn, **no destruction**; short rest follows. |
| ~01:45–02:03 | Six pressure pads activated with combined group weight **physically open floor of Pelor's temple**, not teleportation. Brother Maynard later witnesses disruption. Need map/audio check for the exact structure and any additional temple consequences, not documented here. |
| ~02:06–02:14 | Explicit GM montage declares **rock and concrete seals completed** with both groups; no water-potability result. The rock-eater **is not shown killed or sealed inside the well-side area**. Koh **has not retrieved the climbing sash** when he talks about a future surface trip. Two spear shafts are spare but offered transfer **not shown conclusively accepted**. |
| ~02:15–02:25 | Piercers hang above natural cavern. Evelyn investigates abnormal hovering stones with a javelin; **gelatinous cube is revealed in narrow passage at cutoff**. No subsequent combat/damage, reward or resolved monster identity beyond cube; network sign-off follows. |

## Priority listening

First establish MP3/SRT seek alignment, then inspect ~00:04 (other squad/member names); ~00:17–00:19 (Dominic/Hiroshi/Yolana); ~00:33–00:39 (stone being/Primordial); ~00:49–00:57 (First Sons names); ~01:26–01:35 (horn/psychic shafts); ~01:55–02:03 (pressure plates and temple); ~02:08–02:14 (rock-concrete and sash); ~02:20–02:24 (cube reveal). Check original Discord map for route/platform layout and guild roster before canonizing spellings. **Source SRTs and MP3s unmodified.**

[Full dossier](../delvers/episodes/S1E08.md) · [Delvers queue](../delvers/REVIEW_QUEUE.md).
