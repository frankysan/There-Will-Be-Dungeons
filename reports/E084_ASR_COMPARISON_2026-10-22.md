# E084 — Select Your Champion: two-ASR source comparison (2026-10-22)

> **Scope:** the **same corrected Wastes episode E084**, processed by two named ASR pipelines. This is **machine-to-machine comparison only**, **not** an audio-verified reference, quality ranking, omission count or corrected subtitle. **No audio listening or new model execution occurred**; preserve both existing SRTs unchanged. [Episode dossier](../episodes/E084.md) · [Model tests](../project/MODEL_TESTS.md).

## Inputs and reproducible text comparison

| Repository source | Claimed model/pipeline in filename | Cues | First cue | Last cue near | Normalized text tokens |
| --- | --- | ---: | --- | --- | ---: |
| [Parakeet processed](../sources/The%20Wastes%20S1E084.%20Select%20Your%20Champion.parakeet.processed.srt) | Parakeet, processed; **exact run options not supplied** | **2,765** | 00:00:09.6 | 02:52:16.7 | **24,435** |
| [Qwen Q8 / Canary CTC / Nemotron](../sources/The%20Wastes%20S1E084.%20Select%20Your%20Champion.qwen-q8.canary-ctc.nemotron.srt) | Qwen Q8 / Canary CTC / Nemotron per filename; **exact run options not supplied** | **4,709** | 00:00:09.6 | 02:52:21.7 | **24,725** |

**Method:** Extract SRT cue text, strip `(speaker N)` (speaker numbers are model-specific, **not independently diarized people**), lowercase, remove apostrophes and punctuation, condense whitespace and compare sequential word tokens by **minimum Levenshtein edit distance** (substitutions + deletions + insertions). The calculated **1,887 edit operations / 24,435 Parakeet tokens = 7.72%** is a **first-export-relative inter-ASR disagreement rate**. Not a word error rate against audio: some disagreements may result from punctuation normalization, model segmentation, morphological choices and actual omissions, but **none are attributed to a recognizer without listening**. Cue counts differ greatly but **do not prove Qwen covered more audio**. No run timings, model build hashes, decoding parameters, source audio hashes or machine benchmarks for these specific files are present; do not invent them.

## High-value audio-review locations

| Standard episode offset | ASR divergence / risk | Present editorial handling |
| --- | --- | --- |
| **~00:28–00:39** | Champion author called **Kenja/Kanja/Kanja-like**. Cleric called **Kidigree/Kidagri**. Potion is called “forget-me powder”; text frequently scrambles “sick,” “six sticks,” numerical quantity. | The **scheme** is clear: misdirect competitors with sickness needles and rig Vorel's pairings to humiliate the champion. **Do not infer confirmed medicine formula or total device count**. |
| **~01:02–01:10** | Fixer name **Pelvis** and alias **Ebon/Eben Skulker** broadly align; note **private meeting** and unclear exact identity. | Keep these as provisional spelling but establish Pelvis's earlier fixer relationship as GM-narrated context, not proof the rest of the party knew the job. |
| **~01:18–01:34** | Magical-contact street **Castamere/Castlemere Lane**, target **Stevius Ronkly**, Hive drop address **Belshamer Lane**. The **kidnap target's faction is Parakeet “Godsmen” vs Qwen “Guardsmen”**. | **Do not choose a faction** until heard or verified against character handouts. Both models indicate **kidnap, take to Abyss, 7-day deadline, 1-hour portal return limit**. All are an **offered/accepted job**, not performed abduction. |
| **~01:22–01:24** | Nash's appendage descriptions include old finger, arm, foot. | **Second grasping hand/forearm and foot** after the second E083/E084 overnight rest; avoid saying whole body or restored spellcasting. |
| **~01:43–02:00** | Squirts' forehead **Ioun/“a yewn” stone**, magical scan and swallowing; indefinite invisibility out-of-combat discussion is uncertain. | Guards **deny her entry**; she later enters through priest's side access. Beau gives an **acknowledged provisional table ruling**, not a stable rules text or audio-certified item ID. |
| **~02:01–02:07** | **Royce Colosseum** vs **Royce Gymnasium**; **Bland, Kung/Kong, Rubles/Rubbles**, announcers; new **4,000-gold donation**. | Don't silently merge venue spelling or invent total paid prize. Organizer says only **three characters available** for qualifiers. |
| **~02:08–02:24** | Opponent **Randorf/Randolph**, later called **Randuish**; gnome physically sickened after Squirts' needle jab. | **Vorel actually wins** using Kung; opponent's sickness/sabotage is visible. Some spoken damage arithmetic is corrected during play. |
| **~02:24–02:43** | Nash's opponent board name **Farcred/Farfrid** versus self-introduction **Greteigs (?)**, potentially **multiple names or ASR/model confusion**. | Distinguish a **single elderly female orc using Bland**, visibly defeated by Nash's **Rubles**. **Do not canonically identify her** with an unverified spelling. |
| **~02:43–02:49** | Rival kenku **Bockip/Bakit/Bocket/Bockit**, variants in both files. | **Double forfeit** when both kenku wait for the other to choose a move; no advancement asserted. |

## Editorial decision and next test

Both models support the **episode-level causal events**: book theft, checked unconscious halfling, deliberate sickness sabotage, Nothing's secret portal conversation, Nash's regrowth, **Vorel and Nash wins** and **Nothing's double timeout**. The **Godsmen/Guardsmen discrepancy** is a concrete example why the text cannot be mechanically merged by model vote. The characters' and locations' names remain indexed by provisional aliases so searches can find them, without declaring source-verified official spellings.

**Next verification:** listen to **01:29–01:33** for the target/faction/addresses, **01:00–01:10** for Pelvis and Nothing's epithet, **00:29–00:37** for the priest and champion names, **01:46–02:10** for security and rules exceptions, **02:08–02:24** for the needle and gnome name, and **02:41–02:50** for competitor identity and forfeit outcome. Record audio-grounded speaker IDs and corrections in the review queue; never overwrite original source transcriptions silently.

**Reproducibility limit:** these observations derive from repository SRTs already present. They cannot be replayed as ASR inference without source audio, exact model version, settings, hardware information, pipeline command and outputs; file names alone supply only pipeline labels. See the [ASR comparison workflow](MULTIPASS_PIPELINE.md) for procedures.

[Episode](../episodes/E084.md) · [Review queue](../project/REVIEW_QUEUE.md).
