# E090 — The smell of strawberries and sadness: two-ASR comparison (2026-10-22)

> **Text-only comparison of two machine transcripts of the same ~02:49:50 episode; no audio listening.** [E090 researched dossier](../episodes/E090.md). Source SRTs unmodified. No independently verified words, diarization, actual run settings or model quality ranking.

## Source inventory and comparison

| Pipeline named in SRT filename | Caption cues | Approx. final end | Normalized word tokens |
| --- | ---: | --- | ---: |
| [Parakeet processed](../sources/The%20Wastes%20S1E090.%20The%20smell%20of%20strawberries%20and%20sadness.parakeet.processed.srt) | **2,650** | **02:49:50.14** | **23,453** |
| [Qwen Q8/Canary CTC/Nemotron-labelled](../sources/The%20Wastes%20S1E090.%20The%20smell%20of%20strawberries%20and%20sadness.qwen-q8.canary-ctc.nemotron.srt) | **4,294** | **02:49:50.00** | **23,635** |

Method: extract all SRT text in cue order, strip `(speaker N)` decorations, lowercase, strip apostrophes/punctuation while preserving Unicode letter/digit sequences, collapse whitespace. **Unit-cost whole-sequence word Levenshtein = 1,903 operations / 23,453 first-export tokens = 8.11% normalized inter-ASR text disagreement.** This is **NOT WER against audio, a transcript accuracy measurement, a verified omission/hallucination total, a measure of audio time coverage or a model ranking**. Cues differ because of segmentation. The scripts, decoding parameters, model versions, media hashes, hardware, timing and manually verified reference words are unavailable.

## Material comparative findings

| Clock | What both transcripts support, and where listening matters |
| --- | --- |
| **00:03–00:11** | **Ratfolk Java/Jarver corrects “Tabasco Joe” toward Tobacho Fleur**; Vorel proposes but party **rejects one-hour, single-person shrinking route through the Dark Below**, choosing surface transportation. Names vary more than meaning. |
| **00:15–00:25** | **Lohar** commissions **four matching leather gang outfits for 50gp each**, skulls, spikes and concealed **toe-spike boots**. A **two-day crafting/delivery interval** is agreed and later fulfilled; **no visibly spoken payment**. Do not debit 200gp as an actual payment without source. |
| **00:27–00:37** | Beau explicitly tells Scott **Nash's earlier thermal underwear fused into DNA**, leaving **armpit vent/cooling control and fly speed 10**, to be formally entered as feat eventually. **Active GM adjudication, not mere foreshadowing**. Hope's rumors go nowhere; Stanley's library sources estimate huge overcrowded Hive and border checkpoints; **Fax/Faks fails to attend Vorel's BMF coaching**, Tubbs 9K cannot locate him. |
| **00:37–00:47** | Four gang outfits **actually delivered, worn and dirtied with Prestidigitation**. In-character names **Lady Despair, Toyota Stump, Brildaro, Nuts Phenom** vary later. Rickshaw lady **takes 1gp fare** and departs at Harmonium cordon. |
| **00:54–01:06** | **Harmonium Captain Sir Unindra/Unidra (?) of Fifty-Seventh Legion** at gallows/cages. Stanley's persuasion and Nash's intimidation permit **entry but officer bars future exit**, with **hanging threatened for prior attempted leaver**. **No actual execution, liberation, guard fight, escape or portal crossing** shown. |
| **01:08–01:21** | Tout pushes **Daddy Long Legs**, a seedy club; Hope reconsiders and enters, **1gp admission demand waived**. Weapons checked; **Hope retains unrecognized Scully** until later explicit gift to Tobacho. |
| **~01:29–01:41** | Nash describes unhappy **tiefling dancer as smelling “strawberries and sadness,”** theme/title. Hope interviews hooded **red tiefling, scarred face, skull-etched gold teeth, calls himself Spatulo/Spatula (?)**, who gives **frog vendor/alleyway directions to Tobacho cantina**. The later reaction proves he is **not an agreed ally of dragon**. |
| **01:54–02:05** | Nash **chases/tackles and threatens a smaller passerby with flaming hand** without killing him; party reunites and travels to central Hive. **No further undertaking to rescue dancer completed**. |
| **02:08–02:16** | **Frog-on-a-stick vendor** indicates alley toward **burgundy steel door**; attendant lets “Lady Despair” group in. **Tobacho Fleur** physically appears as **very large *blue* dragon, not black dragon** despite one table prompt confusing colors; wears **monocle and beret** and has stone-golem old-Draconic translator. |
| **02:23–02:37** | **Jelver/Jolver (?)** introduces party, calls false names out, charges **50gp appointment actually paid**. Audience gift: **Hope hands Scully to Stanley, who *gives it to dragon*, accepted via goblin beneath couch**. This is a critical **post-E089 inventory reversal**; do not assert Scully remained with Hope. |
| **02:39–02:47** | Tobacho calls **Earth cursed**, **offers knowledge/location/means of access only after party retrieves an unspecified object** using their prowess. **Jelver's private briefing occurs next session**, not during this one. **No artifact identity/key or portal address** given. |
| **02:45–02:49** | **Hope mentions Spatulo in closing**, dragon responds hostilely, stone golem calls him an **“infidel” disrupting business**, with bounty suggested for delivering him alive. **No apprehension or contract acceptance** performed. |

## Interpretation decisions

1. Treat **E090 physical appearance of Tobacho as a blue dragon** as in-scene, but **his claim of controlling stable Earth portal** as party's conditional NPC promise (agency E089 identified a steward, not publicly inspectable door).
2. **Scully is actually relinquished**. Scully's E089 recovery is historically correct; Hope's E090 cutoff is **no longer holding Scully**, and *Mulder* is separately still missing.
3. **No key, coordinates, artifact specification, item recovery, Earth exit or exit permission** at cutoff; offer and private passage only.
4. Keep **Harmonium coercive entrance checkpoint / death-sentence threat** separate from actual sentence or execution. Use the captain's 57th Legion and name with uncertainty.
5. Record GM's **10-foot hover and DNA-fused cooling underwear** as **new real character ruling**, even though formal feat entry is promised rather than verified.
6. Keep **four outfits physically delivered but 50gp each only quoted**, and count **50gp appointment and 1gp rickshaw as paid**.
7. **Spatulo is a potentially dangerous political/business rival to Tobacho**, as the dragon calls him an infidel; the prior directions do not establish friendship or safe sponsorship.

**Next bounded slice:** [E091 — Going on a heist](../sources/The%20Wastes%20S1E091.%20Going%20on%20a%20heist.parakeet.processed.srt), the exact source filename confirmed in repository tree. **Do not advance story from February bonus's reference to E091 recording**, and keep unclear character/NPC names open for audio listening. [Review queue](../project/REVIEW_QUEUE.md) · [Model test log](../project/MODEL_TESTS.md).
