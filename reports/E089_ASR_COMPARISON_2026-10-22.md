# E089 — It has an umbrella in it: dual-ASR comparison (2026-10-22)

> Two transcriptions of **the same ~2 h 51 m 40 s recording**, compared as text; **no audio listening, reference transcription, new model inference, or SRT edits**. [Episode dossier](../episodes/E089.md).

## Sources and quantitative disagreement

| Source | SRT cues | Final displayed cue (approx.) | Normalized word tokens |
| --- | ---: | --- | ---: |
| [Parakeet processed](../sources/The%20Wastes%20S1E089.%20It%20has%20an%20umbrella%20in%20it.parakeet.processed.srt) | **2,728** | **02:51:35.96** | **23,424** |
| [Qwen Q8 / Canary CTC / Nemotron-labelled](../sources/The%20Wastes%20S1E089.%20It%20has%20an%20umbrella%20in%20it.qwen-q8.canary-ctc.nemotron.srt) | **4,485** | **02:51:39.56** | **23,652** |

**Method:** extract full ordered SRT cue text, strip literal `(speaker N)` decorations, lowercase, strip apostrophes/punctuation while retaining Unicode letters and digits, collapse whitespace, then compute unit-cost word-token Levenshtein distance across both complete versions including recap/outro. **1,747 minimum word edits / 23,424 first-export tokens = 7.46% normalized *inter-ASR text difference*.** **NOT audio-grounded WER**, nor a ranking, verified omission/hallucination count, accurate diarization measure or proof that caption counts measure speech coverage. Model builds, exact inference options, recording hashes, performance times/hardware, reference audio and source sheet crosschecks are not provided.

## Evidence requiring listening

| Approx. position | Source issue / safe boundary |
| --- | --- |
| **00:02–00:19** | **E088's eight-day skip now actually passed**, Nash fully human-shaped with eye/old scars and clothes; bird pecks Stanley and escapes after Vorel's thrown pitcher. **No bird-spy cause proved**. |
| **00:22–00:28** | **M Sports Weekly article** says Kanja was **found hanged/burned** with some inner residents dead, **Harmonium investigating**. **This is a newspaper report**, not eyewitness murder recording or proof **Mind Master/Crimson Moon** carried out the threatened act. |
| **00:35–00:53** | Rickshaw driver **Fanbo/Fambo Joe**, **Dangly Dozen**, **Bronze Gymnasium**, future Friday performance *not actually attended*. Driver gets **1gp +20 silver pieces** per spoken payment: check whether a silver/copper recognition error before deciding accounting. |
| **00:55–01:08** | Street frog vendor asserts no portal **ownership** but control/stewardship of **location knowledge**. Nash's **Solar Mines radioactive-material/heat “solar” deception** and unsupported suspicion Principle purchased energy; character testimony, not external proof. |
| **01:08–01:39** | **Portal Regulatory Agency of Sigil**, staff **Duerto/Dueto**, assistant **Fax/Faks** (illithid BMF competitor), search system **Echo (?)**, **one indexed stable portal to Earth**, **steward Tobacho Fleur/Tobacco Fleur (?) based in Hive**. Crucial **name spelling unresolved across ASR**; no coordinates/key or crossing, only alleged steward. Separate “same shard” world and spelljammer speculation do not automatically mean Earth is a different plane. |
| **~01:19–01:30** | Halfling official requires **armed escort around Hope solely because tiefling**; explicit **institutional discriminatory claim**, not proof Hope threatens staff. Supervisor apologizes. |
| **01:40–02:06** | Stanley seriously proposes **not returning to dangerous Earth**; Hope's royal duty, Nash's family, Vorel's relationships/unfinished commitments cited. **No decision to remain**. **Pig's Foot/Big Foot** restaurant, poutine and cola, **20gp** meal, **1.5gp** return rickshaw. |
| **02:07–02:23** | **Stanley actually recovers Scully**, Hope's original pistol, in E082 dead-body room. **Recovered spectrometer**, not 1,400gp display model. Glow reads Hope's and Stanley's **Infernal/Abyssal names, Weir destiny, proprietor and reward if found**, with highly uncertain **secondary Stanley name Valier Or Noth (?)**. Compare audio, character notes and previous Weir labels before normalizing. |
| **02:22–02:35** | **Nash's novelty device unfolds into umbrella and is named Barbara**. A purple temporary portal **appears during repeated use**, leading to a hot dark enclosed area with oily many-legged creatures; **no reliable reactivation mechanism or realm identified**; group does not cross, Nash retrieves item as door vanishes. |
| **02:37–02:51** | **Java/Jarva the Carver** says Rat King's rats killed and stripped prior scavenger gang; corpses/destruction observed but claim of identity/motive NPC-only. **Vorel bribes 7gp +2gp**, is told second pistol sold to **Fedor (?)**, apparent associate of **same Tobacho Fleur**. **No actual Hive visit, gun recovery or Earth exit**. |

## Documentation decisions

1. Change **Nash's current morphology from incomplete heart to complete humanoid**, *at E089*, while retaining E088's planned-but-not-completed cutoff.
2. Treat Kanja's death as **contemporaneous press report** plus Harmonium inquiry; don't state the earlier threat is conclusive proof of murderer.
3. Upgrade **Earth return** from generic portal hypothesis to **one official record and alleged Hive steward**, not a found exit. Keep specific **Tobacho Fleur** and **Fedor** spellings provisional.
4. Mark **Scully recovered**, second pistol missing but traced to steward's network via ratfolk witness. Ethereal spectrometer **actually recovered, active**, confirms persistent **Weir inscription** yet does not conclusively adjudicate soul contract.
5. Distinguish **Barbara mechanical umbrella** from its coincident purple portal, and **Nash only briefly puts head through** rather than the party traveling to a named plane.
6. E089 ends with **surface-vs-sewer route discussion for Hive**, not a chosen infiltration or encounter.

**Next single episode:** [E090 — The smell of strawberries and sadness](../sources/The%20Wastes%20S1E090.%20The%20smell%20of%20strawberries%20and%20sadness.parakeet.processed.srt). [Review queue](../project/REVIEW_QUEUE.md) · [model-test log](../project/MODEL_TESTS.md).
