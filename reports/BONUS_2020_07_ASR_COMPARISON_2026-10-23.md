# BONUS 2020-07 — July-publication bonus (the delayed June Q&A): whole-export ASR comparison, 2026-10-23

> **Out-of-game retrospective Q&A, not a Wastes played episode.** [Bonus dossier](../episodes/BONUS-2020-07.md) · [processed Parakeet source](../sources/Bonus%202020-07%20-%20July%202020.parakeet.processed.srt) · [Qwen-labelled source](../sources/Bonus%202020-07%20-%20July%202020.qwen-q8.canary-ctc.nemotron.srt). **No audio listening, ASR reruns or original SRT edits.** The owner filenames use a **July public-release** category even though Scott calls the episode a **late June bonus** in the opening; neither labels the exact recording date.

## Pinned source inventory

Initial connected workspace state: **clean `main`, HEAD `139ae823108a12ad44c8b8787d1fc4b343f9c768`**. Full transcripts were fetched read-only using the connected GitHub `fetch_file` action at that same explicit commit, reaching both outros. The workspace binary reader independently returned **Parakeet file size 71,383 bytes and SHA-256 `711533b2e0748190bdc13264fa81820b96d6c0577402966f6238ea3ed8316cef`** for the opening chunk's source identity. The tabulated **Git blob SHAs** are **not SHA-256**; characters are the length of each fetched UTF-8 text string, **not bytes**. These do **not** establish audio-file mastering, exact model/runtime versions, or run timings.

| Exact SRT / label inferred from filename | Retrieved text characters | Parsed cues | First start | Last end | Normalized words | Git blob SHA |
| --- | ---: | ---: | --- | --- | ---: | --- |
| [Bonus 2020-07 - July 2020.parakeet.processed.srt](../sources/Bonus%202020-07%20-%20July%202020.parakeet.processed.srt) — processed Parakeet primary | **67,862** | **731** | **00:00:00.560** | **00:37:20.470** | **6,693** | `0ffe5802563bd36af52561ff2adc6d5a87a0b0ca` |
| [Bonus 2020-07 - July 2020.qwen-q8.canary-ctc.nemotron.srt](../sources/Bonus%202020-07%20-%20July%202020.qwen-q8.canary-ctc.nemotron.srt) — Qwen Q8/Canary CTC/Nemotron-labelled | **92,168** | **1,195** | **00:00:00.050** | **00:37:20.160** | **6,928** | `e1b4351be3c7318ec025892b8afcabfe4cae4526` |

## Reproducible exact method and comparison result

For each **entire SRT**, concatenate only chronological cue text, excluding cue indices/timecode rows, and strip optional `(speaker N)` tags. Lowercase, **remove straight/curly apostrophes** to retain joined contractions, replace other non-Unicode-letter/digit characters with spaces, and tokenize on whitespace. Compare these ordered word sequences using **full unit-cost Levenshtein** (insert, delete, substitute cost one) with the same exact arbitrary-width bit-vector method used in preceding episode reports.

**Primary Parakeet → Qwen: 611 ordered-word edits / 6,693 Parakeet normalized tokens = 9.128940684% ≈ 9.13% text disagreement.** Qwen's normalized token count is **235 higher**, but this is **not** a measured audio omission, hallucination count, model accuracy, confidence, transcription WER or proof of which export is correct. Speaker boundaries, acoustics, model options, quantization and pipeline stage provenance are **filename-derived/unverified**.

## Important phrase/meaning checks

| Recording-clock window | Risk for documentary accuracy | Editorial treatment pending listening |
| --- | --- | --- |
| ~00:00–00:30 | Both exports preserve **July bonus, technically “for June,” delayed to have everyone**; punctuation around host's self-correction varies. | **Keep the official archive ID BONUS-2020-07**, but distinguish **host-stated content-month June** from published-month July and unknown recording date. |
| ~00:40–03:45 | Hell description includes Beau's **homebrew/canon** distinction and a question about the main cast, Hope's henchmen and **Dunebreaker guard**. | This is **out-of-game advice and a hypothetical future battle**, not observed cosmological law or a crossover. |
| ~03:45–14:55 | Multiple speakers discuss possible GMing, **Edge of the Empire**, beginner kits, finding groups and scheduling. | **Personal preference/practical advice** in 2020, not a new campaign, table obligation or modern guide verified today. |
| ~14:55–16:20 | Parakeet garbles **“delicious Sam squid”**; Qwen has **“delicious sand squids”**, referring to Dipshit's possible ancestry. | **Jon says he does not think Dipshit originated them**; no invented family tree or biological genealogy. |
| ~16:30–19:10 | Dragon-metal heart, “green dragon” in listener question versus cast's correction **Nash is black dragon**, partial scales and Beau's deliberate refusal to disclose why body accepts the implant. | Keep accepted black-dragon status and cause **unknown**; suggested anatomy/regeneration or race change **did not happen**. |
| ~23:00–25:15 | Stanley's ***Vicious Mockery*** prior knowledge; fast joking list **Toyota Stump, Lady Despair, Nuts Phenom, Brill Darrow** and speaker ownership. | **Prior skill knowledge** from Jon, **pseudonyms/audio uncertain**; no new alternate characters introduced. |
| ~25:15–27:40 | Jon discusses **Nothing in Inverse**, then unreturned **Stanley artifact/elf side** plans. | Independent campaign commentary and **possible future plot, not a consummated action**. |
| ~27:40–30:10 | Scott's “**the Feeler**” comic concept, empathic pain, and Solar Mines impact on Nash's physical appearance. | Creator-provided **inspiration**, not an in-world entity, confirmed historical flashback or imposed character ability. |
| ~30:10–31:45 | Beau discusses **individual-scale/prismatic pixel animations**, conditional on finding a teacher; Parakeet has “skills” for “scales” in places. | **Hypothetical mastery requiring training**, not immediate magical signage or a documented new spell. |
| ~31:45–37:20 | Jokes about Stanley and Hope's partners, including a supposed orc guard **immediately acknowledged as invented**, and Scott's **Angelashi-first-relationship / Nash fidelity explanation**. | Do **not** certify a partner tally or publish invented jokes as plot. Retain attribution to Scott rather than new in-play scene. |

## Listening queue and next pointer

Highest-value verification: intro ~00:00–00:20; **sand squid** ~14:55–16:20; Nash body ~16:20–19:15; remembered alter egos ~23:15–25:00; Nothing/Stanley planned elf side ~25:10–27:45; **Feeler** ~27:45–30:10; per-scale conditional rules ~30:05–31:45; deliberately retracted joke, partner labels and Nash/Angelashi self-description ~32:00–37:00. Last cues end within **0.31 seconds** of each other and do not independently prove a cut outro. Read both in full as text, **not audio validated**.

**Next already verified main-story source** remains [E111 — Squirts Into The Night](../sources/The%20Wastes%20S1E111.%20Squirts%20Into%20The%20Night.parakeet.processed.srt) and [Qwen](../sources/The%20Wastes%20S1E111.%20Squirts%20Into%20The%20Night.qwen-q8.canary-ctc.nemotron.srt), not reviewed in this pass. [Bonus dossier](../episodes/BONUS-2020-07.md) · [active review queue](../project/REVIEW_QUEUE.md).
