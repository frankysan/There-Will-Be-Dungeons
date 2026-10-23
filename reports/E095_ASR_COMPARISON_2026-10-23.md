# E095 — A Cloudy Day: dual-ASR comparison (2026-10-23)

> **No audio listening or independently verified reference.** Text-only comparison of [Parakeet processed](../sources/The%20Wastes%20S1E095.%20A%20Cloudy%20Day.parakeet.processed.srt) and [Qwen Q8/Canary CTC/Nemotron-labelled](../sources/The%20Wastes%20S1E095.%20A%20Cloudy%20Day.qwen-q8.canary-ctc.nemotron.srt) exports. [E095 source-first dossier](../episodes/E095.md).

## Input and method

| Export | SRT cues | Last cue end | Normalized word tokens |
| --- | ---: | --- | ---: |
| Parakeet processed | **2,242** | **02:42:51.790** | **19,182** |
| Qwen Q8/Canary CTC/Nemotron-labelled | **3,632** | **02:42:51.460** | **19,276** |

Parse SRT cues chronologically; discard numbers, timestamps and `(speaker N)` labels; join spoken cue lines; lowercase; remove apostrophes (joining contractions); replace non-Unicode-letter/digit characters with whitespace; split to tokens. Full-episode **unit-cost ordered word-token Levenshtein = 1,339 edits / 19,182 Parakeet words = 6.98% inter-ASR disagreement**. This is **NOT ground-truth WER, measured omissions/hallucinations, a model ranking or independent diarization validation**. Neither model rerun, no audio listened, original transcripts unchanged. Model exact builds, media hashes, hardware/quantization, VAD and command-line decoding settings not known.

## Source-sensitive story and evidence boundaries

| Window | Confirmed-as-ASR account, competing wording and rule |
| --- | --- |
| **00:00–00:04** | Host explicitly calls this **Sunday March 15, 2020**; independent original recording/publication metadata not checked. Recap covers **E094**, no new E094 scene. |
| **00:05–00:29** | Eight private Constitution rolls each. **Hope rests unaffected**; Stanley/Nash/Vorel are **ill and not granted full long rest**. Nash's **poison-like hot diarrhea into a separate storage chest** deals **6 fire damage**, lock/key, not the Fist chest; **Lesser Restoration temporarily lowers stages** only. |
| **00:39–00:51** | Qwen seems to spell Knight Commander **“Alentris”**, Parakeet **“Lentris”**, player characters did not have this name at E094. **Four reported dead overnight**; she suspects Hope due to E094 demon-camp mouth-caster dust, **not independently proved cause**. **Stanley persuades her (22) to leave Hope in his custody** for cure mission, **future trial reserved**. |
| **00:52–01:08** | Ancient elf high cleric **Crudmund Hordweld/Hordveld (?)** is ill/blind. He remembers **Battle of Rabidal Ridge** and **“Incubatrix” undead curse-virus** as historical parallel; names heavily ASR dependent, allegation **NPC hypothesis**, not virus specimen or independently established etiology. |
| **01:09–01:18** | **Sir Daniel** asks to desert/escape to wife and child **Clarice (?)**; **Stanley refuses until everyone cured**, no desertion. A clash of swords on another level **audible, not seen or adjudicated**. |
| **01:19–01:58** | Black library clouds opaque/unusual, **Dispel Magic doesn't visibly clear**, man with **bleeding eyes dies and becomes dark cloud**, observed; no support every cloud has one person. |
| **02:00–02:04** | **Hope hears mental voice in cloud**, with repeated “bring us the Fist” and **“new master”**; do not attribute to a certain besieger or claim the others overhear. She remains **symptom-free in the moment**. |
| **02:12–02:28** | **Musings of Hordweld**, discovered “**cure to shale disease**” with **cradling/rocking, Celestial incantation and broth**; earlier cleric said **“Incubatrix”**. Distinction matters: **wrong-title/other-disease risk**, and only incomplete physical rocking tried. **No one cured yet**. Multiple Dimension Door scrolls used; inventory requires count audit. |
| **02:30–02:38** | Cleric worse, **bleeding from eyes**, says **Walnut may read sacred words**, **lamb preferred and chicken acceptable**; **Vorel and Gregor begin cooking chicken broth**, Stanley/Nash seek Walnut and Hope remains library. **No completed ritual**. |
| **02:38–02:42** | Outro addresses contemporary illness/isolation, discusses in-session drawing of Nash's chest incident, not extra campaign action. **Final isolated Parakeet cue at 02:42:48 repeats “if you need anything just yell Walnut”**, which isn't proof it was spoken there without audio check. |

## Pending checks and provenance

- **The plague is played and dangerous, but its source remains unproved.** Hope E094 alignment-altering dust, GM historical tiefling carrier analogy, her apparent immunity and malicious inner voice make a strong hypothesis; avoid stating the causal chain as independently witnessed.
- **“Incubatrix” versus “shale disease” is a material apparent mismatch, not a spelling to normalize away**. Do not claim perfect cure has been found or that simple cuddling/broth (without Celestial) cures.
- **Alentris/Hordweld/Rabidal/Clarice/Denise** and stage/roll details require audio review.
- **Walnut remains a human male on the later April bonus GM statement**, but E095 does **not** yet show him performing the cure. **Hope isn't with the other three at endpoint**, and they have not performed Fist retrieval or demon/Nash merger.
