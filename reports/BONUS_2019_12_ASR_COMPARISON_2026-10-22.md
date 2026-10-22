# December 2019 bonus — four-export ASR comparison (2026-10-22)

> **Scope:** Four repository SRT exports of the same **December-publication 2019 bonus Q&A**. The files represent **two audio copies** (standard, alternate with an extra commercial pre-roll) and **two labelled recognition/processing pipelines**, **not four independent performances or human-confirmed reference transcripts**. **No audio was listened to, no SRT edited, and no manual WER/reference transcript exists.** All comparison results are computed against *other ASR output*, not ground truth. Follow [transcription experiment policy](../project/WORKFLOW.md) and [multi-pass notes](MULTIPASS_PIPELINE.md).

## Inputs and structural results

| Input (under `sources/`) | Label derived from filename, not run metadata | SRT cues | Approximate first/end cue (clock) | Approximate normalized word count |
| --- | --- | ---: | --- | ---: |
| [Standard Parakeet](../sources/Bonus%202019-12%20-%20December%202019.parakeet.processed.srt) | Parakeet, processed; model/build/settings **not specified in source** | **645** | 00:00:07.2–00:34:19.6 | **5,992** |
| [Standard Qwen](../sources/Bonus%202019-12%20-%20December%202019.qwen-q8.canary-ctc.nemotron.srt) | Qwen Q8, Canary CTC, Nemotron per filename; exact build/settings **unrecorded here** | **967** | 00:00:00.1–00:34:27.8 | **6,075** |
| [Alternate Parakeet](../sources/Bonus%202019-12%20-%20December%202019%20%28alternate%20copy%29.parakeet.processed.srt) | Parakeet, processed, alternate copy | **647** | 00:00:01.6–00:35:19.8 | **6,151** (includes commercials) |
| [Alternate Qwen](../sources/Bonus%202019-12%20-%20December%202019%20%28alternate%20copy%29.qwen-q8.canary-ctc.nemotron.srt) | Qwen Q8, Canary CTC, Nemotron per filename, alternate copy | **988** | 00:00:01.7–00:35:19.5 | **6,210** (includes commercials) |

**Method:** Parse numbered SRT cues, read start/end times and combine text while removing `(speaker N)` decorations. Whitespace- and punctuation-normalized tokens provide **automated text-only edit distance**, with case folded and apostrophes removed. Cue segmentation and alignment are deliberately **not** treated as word accuracy. A separate file's speaker numbers are **not mapped** to the same performer IDs. No exact configuration, reference-audio checksum, model invocation, GPU/runtime, audio decoding parameters or post-processing version was supplied, so **do not invent them**.

The standard copy starts with the actual host introduction. The alternate adds approximately **one minute of ads** from **Undeniably Dairy** and **Priceline**, followed by the same bonus conversation; it **does not provide another distinct Q&A**. The spoken-show start is approximately **00:00:07.2** (standard Parakeet), **00:00:00.1** (standard Qwen), **00:01:07.4** (alternate Parakeet) and **00:01:00.3** (alternate Qwen). The roughly seven-second difference between Qwen and Parakeet onset timestamps within each audio copy is **alignment/export behavior to review**, not evidence of seven seconds missing from the conversation. Compare windows by **spoken content**, not raw timestamps alone. Advertising is distribution content, not 2019 story or dependable original publication evidence.

## Quantitative text-only agreement

Calculated from the **actual conversation onward**, trimming the alternate's leading ads. Unit is **minimum word-token Levenshtein substitutions/insertions/deletions divided by the first named export's token count**, rounded. This is an **inter-ASR disagreement rate, not WER, ASR accuracy, or verified omission/hallucination frequency**.

| Pair | Normalized conversation tokens | Word edit operations | First-export-relative disagreement |
| --- | --- | ---: | ---: |
| Standard **Parakeet vs Qwen** | 5,710 / 5,795 | **338** | **5.92%** |
| Alternate **Parakeet vs Qwen** | 5,705 / 5,781 | **342** | **5.99%** |
| Standard vs alternate **Parakeet** | 5,710 / 5,705 | **168** | **2.94%** |
| Standard vs alternate **Qwen** | 5,795 / 5,781 | **150** | **2.59%** |

Different punctuation, proper-name tokenization, contractions, ad truncation, dialogue repetition and segment boundaries can all affect these numbers. The higher number of Qwen cues is **not evidence it recognized more speech**. A full audio-verified transcription is required to measure actual deletions, insertions, substitutions, timestamps, word alignment, attribution or genuine model hallucinations.

## High-impact comparison candidates — *not* resolved by model vote

| Standard recording, approximate | Source disagreement or recognition risk | Treatment / future listening action |
| --- | --- | --- |
| **00:03–00:04** | Both versions recognize an **angel/technology hybrid** made for the old laboratory, but Qwen renders the location as **“cedus or cedus”** while the established world term is **CHIDS**. | Note **Beau's handmade experimental angel design** as GM creative commentary. Check pronunciation and whether a specific angel/stat block is identified; do **not** change the transcript to a guessed proper noun. |
| **00:04–00:06** | The GM calls Hope/Stanley's appearances **petitioners** and says their souls were **interrupted en route to the Weir**. Soulbroker name is transcribed variably (e.g. Parakeet **“kitobel pray”**, Qwen elsewhere **“Kotobalprith / Cotobal Price”**). | Use the extant **Catoblepraithe/Catobelpraithe** unresolved-spelling ledger. The creator's statement is stronger retrospective setting testimony than a Sigil NPC's opinion, **but it is still not a performed resurrection**. |
| **00:07–00:09** | Cast describes all four entering the beam and Beau's **unexpected decision/adjudication**. Minor wording and alignment vary; no independent recorded afterlife event is described. | Retain the actual E081 sacrifice and GM death declaration; note **no off-mic preset agreement** and **on-the-fly roll/save math** as post-episode production explanation. |
| **00:15–00:18** | Elf's name near discussion of unstable regeneration appears as **“saranthalos” (Parakeet)** or **“Ceranthelos/Ceranthelas” (Qwen)**. It refers to the already documented **Cerinthala-like elf context**, but exact spoken name needs audio checking. | Preserve **Beau's conditional elf-restoration explanation** and beam disintegration caveat as retrospective setting statement, **not a universal all-elves regeneration rule**. Cross-check [E074–E081](../episodes/E074.md). |
| **00:18–00:21** | Both models largely agree on **lost non-dragon-metal possessions**, surviving **Nash's dragon heart** and **Vorel's ruptured Eye of Groxl**, plus discussion of **Château Weir's time cost / Nobiery journey**. | Item exception does **not** mean all lost dragon-metal gear was found; claim about Eye remains **one owner-confirmed Groxl item**, not new dragon metal. The trip timing is **retrospective estimation**, not an exact universal exchange rate. |
| **00:21–00:26** | **Quizquaz**, **Dolo Popio**, **Andreeste**, **Tietkalla** and **Soulbroker** are sometimes split, transformed or approximated (e.g. **“Quiz Quads,” “Delapopio,” “Andriasta,” “Tietala”**). | Use previously researched display spellings and alias ledger, **not majority-voted canonical names**. Beau says Dolo Popio was engaged to remove Hope to facilitate Andreeste's claim and a Weir-court dispute existed, but **the fall of Tietkalla is asked as a hypothetical, not observed**. |
| **00:25–00:30** | Vorel's sacrifice of the Eye is variously heard as **“Grojil,” “Grozil,” “Groguil”**; name of the trickster priest approximates **Kidigree**. The Q&A explicitly explores whether Nash is a person *with* a heart or a heart *with* a person. | **Groxl** is the **owner-confirmed written form** of the same Eye; priest spelling still pending. Nash's immortality and the God Killer's target are **deliberately unanswered**, not settled by this bonus. |
| **00:30–00:33** | **Data core** allegedly delivered to an **elven scoutmaster at Dusthill**, whose name the cast themselves do not firmly recall. Player mentions **Melgor** as a possible acting authority and Beau speculates about Hope's mother/parents. | Log as **retrospective player recollection and GM uncertainty**, not a new on-camera item transfer or a confirmed succession/parental fate. Confirm against original scene before altering custody records. |
| **00:34 / tail** | Standard Qwen includes **a short “O'er hill and dale”** after the sign-off; it is not reliably represented in the other three exports and may be an audio tail or recognition artifact. | **Audio-review tail**; do not assert a verified final spoken line or hallucination. |

## Source-quality decision

- **Reference for episode chronology:** use the **standard (non-alternate) copy** because its clock is free of the additional ad minute; quote **approximate recording offsets** and distinguish Qwen/Parakeet onset.
- **Research approach:** consult **both recognizers** at names, negation, fate claims, character decisions, comedic asides and claims about cosmology. Keep the same canonical display convention from the [editorial guide](../project/EDITORIAL_GUIDE.md), but **never silently rewrite original ASR**.
- **Not demonstrated:** either ASR pipeline's superiority, a numeric WER, confirmed exact character/noun spellings from audio, objective Sigil law, a new game scene, an actual resurrection or Tietkalla falling.
- **Next test:** listen to the source audio at the critical windows above (including alternate ad boundary and standard-Qwen tail), preserve exact speaker identity per file, log accepted/rejected readings and optionally create a **manual audio-grounded reference** with both disputed and control regions. The comparison is **not a replacement for the existing multi-pass workflow**.

[Bonus dossier](../episodes/BONUS-2019-12.md) · [Review queue](../project/REVIEW_QUEUE.md) · [Audio experiment guidance](../project/MODEL_TESTS.md).
