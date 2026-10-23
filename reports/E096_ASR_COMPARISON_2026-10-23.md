# E096 — You hold the soup: dual-ASR comparison (2026-10-23)

> **Text-only comparison, no audio listening or ground-truth transcript.** [Episode research dossier](../episodes/E096.md) · [Parakeet](../sources/The%20Wastes%20S1E096.%20You%20hold%20the%20soup.parakeet.processed.srt) · [Qwen Q8/Canary CTC/Nemotron-labelled](../sources/The%20Wastes%20S1E096.%20You%20hold%20the%20soup.qwen-q8.canary-ctc.nemotron.srt).

## Input inventory and method

| Export | SRT cues | Last timestamp | Normalized word tokens |
| --- | ---: | --- | ---: |
| Parakeet processed | **2,437** | **02:44:05.070** | **21,679** |
| Qwen Q8/Canary CTC/Nemotron-labelled | **4,160** | **02:44:04.920** | **21,930** |

Remove SRT ID/timecode and `(speaker N)` labels, concatenate cues in chronological order, lowercase, delete apostrophes (contractions join), replace all non-Unicode-letter/digit with whitespace and split. Full-transcript **unit-cost ordered word-level Levenshtein = 1,698 operations / 21,679 Parakeet tokens = 7.83% inter-ASR text disagreement**. **Not audio-grounded WER, verified hallucination/omission count, model benchmark, diarization validation or sound-word correctness**. No listening, reruns, recording hash, VAD/decoding params, model build or device timings available. Original SRTs unchanged.

## Critical distinctions by source segment

| Approx. position | Stable source-supported event and remaining uncertainty |
| --- | --- |
| **00:03–00:16** | **Vorel/Gregor complete actual broth**, Walnut gives **phonetic Celestial**, **Stanley rocks/recites and broth poured across Alentris's face**. **A black cloud turns blue-white/dissipates**, commander visibly **cured**. **E095 “shale” vs “Incubatrix” title mismatch still remains in manuscript**, but **this ritual demonstrably works against the episode's plague**. |
| **00:16–00:36** | **Alentris then cures Stanley** with same action; **Stanley and Alentris have consensual romantic/sexual intimacy**, not merely an offer. **Walnut cures Vorel**, including black-cloud release. The young human-male status is also explicitly GM-confirmed in later April 2020 bonus. |
| **00:36–00:53** | **Walnut cures Nash when broth actually added**; initially shaky, later confident after Nash encourages him. Stanley is away with Alentris when **Nash starts leading further cures**, including one guard. **No claim all cured this early**; later montage handles remainder. |
| **01:13–01:29** | Hope **still in lower library** (E095 cutoff intact), hears **unidentified deep voice** say letting everyone die would have enabled them to meet; threatens temporary lawful-good protection. **Hope refuses because of friends**. Restricted **compendium seen but barred**, law text **Executus** suggests severe religious repentance instead of execution. **No spell/alignment reversal, religious conversion, compendium retrieval or demon defeat**. Hope **returns upstairs during E096**. |
| **01:29–01:51** | Full commander name audible approximately **“Alentris Vayne”** (alternates across recognizers); **Stanley defends Hope, high Persuasion 31**. She mentions ~**dozen** losses, versus four known at E095's earlier report—avoid treating as contradiction or resurrecting dead. **Captain Waltz** reports future replacement ship **near White Tower noon tomorrow**; this is **message/intent, not confirmed bookable or arrived transport**. **Original Captain Meart wasn't observed dead**. |
| **01:44–02:01** | Alentris suggests **bridge to Mount Celestia may give judgment to return four to Earth** but **no outcome guaranteed**, and **proposes to give stolen pendant key to Walnut and send separately**, **not played physical transfer**. Stanley agrees in principle to promise before Euphemius after consulting friends. **Hijack and Divine transfer proposed**, not done. |
| **~02:01–02:08** | **Hope's return is witnessed**, **Alentris/knights kneel to thank her**. Further **Stanley/Alentris assist**, and **GM explicitly declares White Tower remaining inhabitants cured** after hours of rites. **Black clouds' persistence after this has not been explicitly re-observed or removed**. |
| **02:14–02:23** | Stanley apologizes to Vorel and seeks companions' **informed agreement** about Mt Celestia plan. **Hope shares mental voice revelation with companions** for first time; demon identity uncertain. No final binding vote/oath shown. |
| **02:24–02:39** | **Restricted library compendium** (possibly demons) still behind **a lever-operated gate requiring cleric/commander authorization**; **Vorel, Nash and Hope convince Walnut to follow them down** by confusion; no actual permission in hand, lever pulled, tome opened or demon found. **Stanley stays separate**. |

## Listening priorities and scope controls

- **Alentris/Elentris Vayne spelling**, names of ships/captains **Waltz/Meart**, order **Obsidian White/Wight**; maintain provisional orthography.
- Specific in-game **broth poured vs drunk** corrects E095's uncertainty, **all remaining members cured**, not restoration of casualties.
- The **“shale disease” versus “Incubatrix”** wording should be audio and original-note checked; **ritual efficacy is verified within played ASR story despite title mismatch**.
- **E094 captured-bishop Fist/key separation persists**; **key-to-Walnut is future conditional plan, not inventory change**.
- **Hope inner voice claims plague plan**, but the exact speaker/source of infection and a possible hidden demon remain unknown.
- **E097 after this cutoff**, not used to preempt the restricted-library consequences.
