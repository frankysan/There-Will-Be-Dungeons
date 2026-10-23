# April 2020 bonus — dual-ASR text comparison (2026-10-23)

> Source-first comparison of two machine-transcribed exports, **not audio listening**, verified ground-truth WER or model-accuracy ranking. [April 2020 research dossier](../episodes/BONUS-2020-04.md). Original source SRTs were read only.

## Inputs and repeatable normalization

| SRT input | Filename-implied pipeline | Cues | Last timestamp | Normalized word tokens |
| --- | --- | ---: | --- | ---: |
| [Parakeet processed](../sources/Bonus%202020-04%20-%20April%202020.parakeet.processed.srt) | Parakeet processed; build/decoder unknown | **815** | **00:40:05.740** | **7,038** |
| [Qwen Q8/Canary CTC/Nemotron-labelled](../sources/Bonus%202020-04%20-%20April%202020.qwen-q8.canary-ctc.nemotron.srt) | Components per filename; builds/options unknown | **1,395** | **00:40:05.540** | **7,315** |

Parse chronological SRT cues, omit indices, timestamps and `(speaker N)` tags, concatenate text, lowercase, remove apostrophes (so contractions join), replace all characters not Unicode letters/digits with whitespace and tokenize. Apply **unit-cost ordered Levenshtein at the word-token level over the entire transcript**, without guessing spoken references from one system. **850 edits / 7,038 Parakeet tokens = 12.08% inter-ASR difference**. This **does not measure error against speech**, hallucination or missed words. Qwen has **277 more normalized tokens**, which cannot by itself demonstrate Parakeet omitted speech; possible segmentation/repetitions/different lexical readings must be audio checked. No audio/hash, manual reference, model build, VAD/decoding settings, device or execution benchmarks collected.

## Case-based editorial findings

| Window | Shared signal, divergence and required caution |
| --- | --- |
| **~00:40–03:50** | Pandemic/isolation remote D&D tooling—**Discord, optional Roll20/Fantasy Grounds, D&D Beyond, virtual dice**. **Period-specific advice, not a binding record of every show's actual tool**. |
| **03:50–05:35** | Beau directly identifies **Walnut as a human male**, initially envisioned small and weak and perhaps one day a priest. Other cast pictured him as gnome. Some discussion of what **Vorel/Nash later did to help Walnut with curing/healing**, but E094 stops earlier: **do not backdate**. Order name varies across ASR (“Pelagric/Palatric”); check audio/handout. |
| **~06:30–19:40** | Imaginary screen adaptation choices: **Michael Wincott as Nash voice, Tom Hiddleston/Loki visual inspiration for Stanley, Patrick Warburton for Vorel, Jennifer Hale/Evangeline Lilly for Hope**, alongside more ironic casting. **No actual movie/adaptation deal and no new player-character transformations**. |
| **~19:45–23:15** | Real-world magic-item wishes (portal device, Diplomacy, immovable rod, bag, Hope robotic arm, Nash thermal flying underwear); **not transferred to campaign**. |
| **23:15–24:45** | Possible community-art book, character iteration drawings, M-sports minigame. **Production brainstorm, no publication**. |
| **24:45–26:20** | **Vorel's chest still contains inert remnant of the singular Eye of Groxl**, with **sunken/craterlike scar** in player mental picture; GM says **artifact remnants don't simply decay like flesh**. Neither proof Eye works nor proof separate eye was implanted after E081 loss. Compare main-scene E081/E082 descriptions, source recording and owner-confirmed singular artifact decision. |
| **26:20–28:55** | **Future Nash iterations** recalled; a hivemind copy **may remain if the Kervalon hive survived destruction**, a **conditional conjecture**, not established surviving extra PC/alternate future. |
| **28:55–32:15** | Beau explicitly **intended a moral-tone contrast** between bitter Earth and more diverse Sigil. **White Tower's order designed as genuinely good-aligned**, Tietkalla and a few Earth paladin groups (**Order of Paxus led by Melgor**, spelling uncertain) excepted. Do not infer every particular paladin is trustworthy or whole city safe. |
| **34:05–37:15** | **First hundred episodes** favourite-arc question: lizardfolk clans, early Tietkalla, vampire plot and rocket escape; character relationships. **Not an extra main episode, does not fix corrected chronology index.** |
| **37:15–39:25** | Current cliffhanger: **Nash and a demonic entity seemingly occupy the same teleport destination after concentration ends**. Beau says he'd premarked space in GM layer and did not force it; **the actual aftermath is unknown and may occur after E094**. Do not write a settled hybrid or death, and don't assign a specific unresearched episode number. |
| **39:25–40:05** | Qwen: host appears to say early-access listeners getting bonus **“April fifth”**; Parakeet loses **“April”** (“which is to say fifth”), leaving **date ambiguity**. **Not audio verified, not proof of public-release day or exact recording day**. Parakeet final isolated cue at ~40:01 apparently repeats **“we saw an opportunity [to] upgrade Nash's look”** from ~26:20; Qwen doesn't clearly retain this on the tail. **Check whether closing sting, edit bleed or hallucination; don't declare omission**. |

## Preservation and future verification

No original transcript edited; source comparison only. Model versions, command lines, quantization/runtime details, hardware, exact source audio identity and speaker diarization ground truth are unavailable. Track **Walnut human/male** and **Eye remnant** as later GM/cast exposition; keep **Nash/demon collision** and **April fifth** as audio/listening priorities and **future numbered-episode cross-checks**. [Review queue](../project/REVIEW_QUEUE.md).
