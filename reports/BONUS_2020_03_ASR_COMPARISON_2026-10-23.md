# March 2020 public-release bonus: two-ASR comparison (2026-10-23)

> Text-only comparison of **two unchanged ASR-produced SRT exports for one ~35m37s cast Q&A**; **not audio verification**. [Research dossier](../episodes/BONUS-2020-03.md).

## Inputs and reproducible normalization

| File | Source label is filename inference only | SRT cues | Final cue end | Normalized word tokens |
| --- | --- | ---: | --- | ---: |
| [Parakeet processed](../sources/Bonus%202020-03%20-%20March%202020.parakeet.processed.srt) | Parakeet processed, exact build/settings unknown | **712** | **00:35:37.410** | **6,674** |
| [Qwen Q8/Canary CTC/Nemotron-labelled](../sources/Bonus%202020-03%20-%20March%202020.qwen-q8.canary-ctc.nemotron.srt) | Model/pipeline components named by export, exact builds unknown | **1,088** | **00:35:37.220** | **6,906** |

Parse SRT cues in order; discard cue numbers and timecodes; remove `(speaker N)` decorations; concatenate transcribed content, lowercase, strip apostrophes (joining contractions), substitute whitespace for non-Unicode-letter/digit punctuation and tokenize on whitespace. Full-episode **unit-cost ordered word-token Levenshtein** gives **523 edits / 6,674 Parakeet tokens = 7.84% inter-ASR text difference** (includes host framing/outro). **This is NOT word error rate against audio**, independently confirmed omission/hallucination, a model ranking or speaker-diarization accuracy. **No audio or handouts checked, model binaries/decoding/VAD/segment details and performance timings unavailable.** Sources not modified.

## Source-dependent risks

| Approx. clock | Stable conclusion, or uncertainty requiring listening |
| --- | --- |
| **00:00–00:50** | Scott hosts a fan Q&A and says **supporters hear it one week before public listeners**; no independently verified exact recording or release day. The **March 2020 label is filename/publication convention**, not spoken date at start. |
| **~00:50–04:10** | Character deathmatch and E081 dissent/PvP **were hypothetical, not played**. Beau says he **intentionally seeded a possible party-splitting future** but the PCs chose shared sacrifice. |
| **~04:30–05:10** | Both exports support **Weir / Kitobalpraith as original campaign setting/figure**, **Sigil and Planescape as published D&D**, and **Far Realm connection described only as an allusion**. Qwen sometimes renders **Kitobalpraith as “Kotal Preth”**, Parakeet as “Kitobel Prayet”; **neither variant should replace canonical project spelling based on ASR**. |
| **~05:10–07:10** | The GM's borrowed planes/Manual of the Planes/TSR framework helps production attribution, **not proof every published setting rule applies unchanged in Wastes**. Some confusion in quoted cosmology analogies; no new played world hopping. |
| **~08:20–09:15** | **M-sports poster started as a joke, game/mechanics developed after players became interested**. Neither source implies tournament victory was staged or false. |
| **~10:00–19:10** | Cast prefers collaborative flexible rulings; Beau admits **missed triggers and imperfect spell status tracking**; E093 **Vorel grating/movement** discussed as table ruling. **Not external RAW adjudication nor retcon.** |
| **~19:35–20:50** | Jon: **Stanley remains changed after death** and doubtful about returning home. Amid joking about Diontalus, **Parakeet says “just in a cat”** while **Qwen says “just in a capsule”** at ~20:37–20:45. **Cannot claim either object is canon, or that Diontalus is conclusively alive/dead**; inspect audio and original E0xx crystal reports. |
| **~21:00–27:40** | Beau: **resurrection depended on player effort and Sigil's options**, not globally guaranteed. Players discuss listener attachment to Nothing/Squirts and possibility of not pursuing resurrection. **No unseen cure or contract release**. |
| **~27:40–32:05** | Returning to Earth, **Nash's family, Stanley's reluctance, Hope godhood and Lady of Pain final boss** are conditional/joking scenarios. **Don't register as upcoming plot or foreknowledge**. |
| **~32:05–34:08** | **Vorel's desire to check kingdom and Golden Sands** is a player expectation, **not a completed return**; GM says **no solo Vorel episode planned**, however appealing the idea. |

## Decisions and reproduction limits

The **Q&A is supplementary testimony** whose stable GM intent should be placed in the bonus dossier and pointed to from applicable **Sigil, M-sports, Stanley and broader world interpretation**. **Do not produce a fictional time-step** between E093 and E094 or replace E094's actual Knight Commander encounter with speculative endgame choices. Preserve the **Diontalus cat/capsule split as an audio-review item**.

The filenames do not contain verified ASR model versions, quantization execution metadata, exact commands, device usage, decode speed, media checksums or manual speaker mapping. Comparing recognizers by token edit distance gives no reliable ground truth without hearing the audio. [Review queue](../project/REVIEW_QUEUE.md) · [model test log](../project/MODEL_TESTS.md).
