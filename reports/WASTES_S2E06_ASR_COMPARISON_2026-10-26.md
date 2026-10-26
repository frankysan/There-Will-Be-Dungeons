# The Wastes S2E06 — Schrödinger's Nash: two-ASR comparison (2026-10-26)

[Full timestamped episode dossier](../episodes/S2E06.md). **Played Wastes S2E06**, normalized input basename `The Wastes S2E06. Schrödinger's Nash`. Full primary read through 02:49:18; complete independent secondary processed for metric and selected windows read. **No audio listening or human ground-truth transcript.**

| Input | Git blob SHA (remote) | Subtitle cues | Final end | Normalized words |
| --- | --- | ---: | --- | ---: |
| [Parakeet processed](../sources/The%20Wastes%20S2E06.%20Schr%C3%B6dinger's%20Nash.parakeet.processed.srt) | `7a209ba83fd9489af0554fe119537079b5a13d2c` | **2,873** | **02:49:18.720** | **25,791** |
| [Qwen Q8/Canary CTC/Nemotron-labelled](../sources/The%20Wastes%20S2E06.%20Schr%C3%B6dinger's%20Nash.qwen-q8.canary-ctc.nemotron.srt) | `4672c92fa908db6e9d123b37b7de9b87f9e92808` | **5,052** | **02:49:18.380** | **26,683** |

**Exact ordered normalized-word edit distance = 2,965 / 25,791 = 11.50% inter-ASR TEXT disagreement — NOT WER.** Secondary has **892 more tokens**, which says nothing by itself about accuracy.

**Reproducible method:** Chronologically concatenate only SRT cue speech; exclude cue numbers/timestamps and `(speaker N)` labels; lowercase, remove straight and curly apostrophes, replace non-Unicode letters/digits with whitespace and split; compute unit-cost ordered word Levenshtein (insert/delete/substitute = 1). Two-row DP used an approximately **±4,500-word diagonal band**; minimum **2,965 < 4,500** ensures no better path can have left the band, so it equals the global distance. The measured number is **textual model disagreement** and **cannot establish which output is accurate or which words were omitted/hallucinated**.

**Provenance:** Initial local checkout `main` HEAD `a1ca34cef5adf3419c9ec8a8bef056404b77a151` was clean. GitHub could not resolve that exact HEAD and thus source data came from GitHub default-branch immutable blob IDs above. Local first cue lines were consistent; **entire workspace/source blob byte identity was not verified**. Pipeline names are **labels inferred from filenames**, not authenticated runtime commands/settings. Research used full Parakeet text and selected Qwen verification windows rather than a complete second editorial read.

## Material text-only verification priorities

| Recording clock | Risk and editorial decision |
| --- | --- |
| **~00:11–00:21** | Nash's improvised rhyme for ***Reduce*** on Vorel is **existing NSP-013**, not a new finding. Actual shrinkage and gate-handle operation must not be mistaken for unlocking dial magically. |
| **~00:35–01:08** | **Tungsten Wheel's signed employment contract** (bank teller at 10 gold/week), signed teller ledger and small key found at desk **confirm past work**, but not whereabouts, alive/dead status or future employment. “Tapioca / iron / plow” are separate clue words, with untranslated Dwarvish elsewhere. |
| **~01:08–01:25** | A fresh ooze **actually sets Stanley's Wisdom to 3**, after separate Nash intelligence/dexterity losses in S2E05. Ooze is killed; **WIS stays 3**. ***Healing Word* restores nine HP/back discomfort only**, not Wisdom. |
| **~01:40–01:56** | Key number **724**, obtained from Tungsten's desk, opens matching deposit box. Hope reads **coordinates** from parchment, **not their destination**. Bank initial loot estimate **13,365 gold-equivalent**, revised surviving **12,968**, plus discussed **4,322 each** are not a settled individual inventory ledger. |
| **~02:00–02:31** | Masked marauders named **Green Vale / Greenveil**, leader **Stink Eye** (phonetic) and killed lookout **Flamar/Flemar**. Stanley's crowd-clearing ***Fireball/Destructive Wave*** and Vorel's leader kill, Hope's disguise and dragon-Nash's acid breath/impact need kept separate. Dragon transformation is **performed**, not cure. |
| **~02:28–02:45** | Three surrendering orcs **Tuk/Ruk/Lok (?)** actually accepted by Stanley as crew, entered on ship map; original raiding group mostly dead. They report caged prisoners and **Hope actually frees Badass T and the locals**. Do not record a rescued Tungsten. |
| **~02:44–02:49:18** | GM uses **adult black dragon INT 14** for transformed Nash. **Nash's underlying INT 3/DEX 3 and Stanley WIS 3 remain unresolved** at cutoff. No restored normal form, off-asteroid voyage or visited coordinate destination. |

**Review limits:** No source audio, GM handouts, player sheets, original subtitle diarization or character spell lists checked. ASR uncertainties include president Golka, bank staff names, key reading “seven to four,” dwarf love-letter writers, marauder names and survivors' names. No claim of verified speaker separation or corrected transcript. **Next source independently identified as Wastes S2E07 “Brace for Impact,” unresearched.**