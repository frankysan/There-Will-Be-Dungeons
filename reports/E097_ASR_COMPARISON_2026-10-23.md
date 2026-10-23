# E097 — Walnut, go away: dual-ASR comparison (2026-10-23)

> **No audio listened to; no reference transcript or audio-ground-truth WER.** [E097 dossier](../episodes/E097.md) · [Parakeet](../sources/The%20Wastes%20S1E097.%20Walnut%2C%20go%20away..parakeet.processed.srt) · [Qwen Q8/Canary CTC/Nemotron-labelled](../sources/The%20Wastes%20S1E097.%20Walnut%2C%20go%20away..qwen-q8.canary-ctc.nemotron.srt).

| Source | Cues | Final cue end | Normalized words |
| --- | ---: | --- | ---: |
| Parakeet processed | **2,494** | **02:37:51.730** | **20,811** |
| Qwen Q8/Canary CTC/Nemotron-labelled | **4,068** | **02:37:51.520** | **20,996** |

**Method:** Extract chronological SRT cue text; strip indices/timecodes and `(speaker N)` tags; lowercase; remove apostrophes (joining contractions); replace non-Unicode-letter/digit characters with whitespace and split into tokens. Run **unit-cost ordered full-episode word Levenshtein**: **1,519 token edits / 20,811 Parakeet tokens = 7.30% inter-ASR disagreement**. This is **NOT verified errors against speech, model quality ranking, validated omissions/hallucinations or speaker attribution**. Audio, exact source file hashes, model builds, commands, VAD/decoding settings, ground truth and hardware timings are not available for the comparison; no original SRT altered.

## Main distinctions and audio-review checks

| Window | What the source says / don't infer |
| --- | --- |
| **00:03–00:15** | The black stair cloud **has dissipated**. Three PCs **physically force barred gate with 25 combined strength**, breaking restraint; **Enlarge not actually cast** and **Walnut absent** at first. |
| **00:14–00:38** | **Hope actually removes and reads handwritten Monstrous Compendium** behind gate; **doesn't find named Carthax/Ulvert**. Generic **Asmodeus, Orcus** entries are not identity of hostile voice. Vorel's church-relic manuscript **doesn't identify Zorander's Fist**, merely stories of other artifacts; Nash's commander journal is mundane. |
| **00:38–01:08** | **Vorel awakens Walnut in his room and brings him to library**, rather than Walnut coming along at previous E096 cutoff. Walnut says **Fist brought to tower ~one week ago** and claims strength of mountain, lethal touch, haunting; he stresses this is **rumor**, not demonstrated magic. **Kidigree as god of clowns/Limbo** is his imperfect religious knowledge, not validated sourcebook identity. |
| **01:09–01:29** | **Four PCs and Walnut talk privately** after waking Stanley. Vorel considers **opening Fist chest to expose demon**; not performed. **Stanley resists gambling the tower to fulfill Tobacho's deal**; Hope asks not to touch glove. No permanent group accord. |
| **~01:32** | **Hope privately hears disembodied voice “today ... we meet”**. No observed demon/appearance or confirmation of time promised. |
| **~01:34–02:10** | Hope/Stanley make stew, Nash assists; other defenders join breakfast. **Knight Commander Vayne receives ovation**, one knight says **she recently arrived with Fist**; does **not prove she is impersonator, disease-instigator or demon**. Potential “Tedna”/Nash locked-latrine chest side jokes not new relic custody. |
| **02:10–02:13** | Walnut dismissed for private party concerns. Alentris's proposed **key-to-Walnut handoff has NOT happened**; timing of her appointment raises party questions only. **Hope repeats the voice warning and requests she not touch the relic**. |
| **02:14–02:23** | **Knight Commander publicly rescinds the earlier execution sentence**, not simply stays it. Reports **Knight Commander Thayle (?)** near Mt Celestia Great Road border and **pegasi-riding celestial reinforcements expected this evening**, not yet witnessed. Plans gate battle for Fist collection, **not executed**. |
| **02:23–02:30** | **Stanley proposes safer roof rendezvous and Dimension Door messenger transit**, which **Alentris accepts** in place of gate opening. Still **only plan**, no observed arrival/transfer; **Captain Waltz's separate replacement airship isn't declared canceled**. |
| **02:30–02:34** | Alentris describes local farm hamlet restoring after siege and a **good place to raise children**; dialogue is a romantic potential, **not confirmed pregnancy, parenthood, residence or future engagement**. |

## Publication and continuity decisions

The earlier **E096 replacement-airship option is superseded as the commander's publicly chosen E097 strategy** by word of the **celestial pegasi escort**, while the private Tobacho/Waltz transport **is still due by its sender's claim and neither arrived nor demonstrably canceled**. The **formal rescinding of death sentence is new** and must supersede E094/E096 provisional stays. The **library gate really was lifted and broken**, and **Hope actually accessed the compendium, then left it behind**, resolving E096's future-only library plan. The **voice's promised meeting remains unfulfilled** by E097 cutoff, and the artifact stays in its **unopened chest** with key **not physically passed to Walnut**.

No audio verification or original file edits. Preserve uncertainties of spelling, speaker mapping, divine lore and exact plan provenance in [review queue](../project/REVIEW_QUEUE.md).
