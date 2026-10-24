# E122 — complete-export ASR comparison, 2026-10-24

**The Wastes · corrected S1E122 · That's Ghost Water · played session**, original catalogue **TWBD 124**, dated **19 October 2020** in the retained owner-spreadsheet snapshot. Recording date unverified. [Dossier](../episodes/E122.md) · [Parakeet][p] · [Qwen-labelled][q]. **Text-only ASR evidence; no listening, new ASR run, source correction or hardware/runtime benchmark.**

## Input identity and access

The direct checkout began clean on **`main`, HEAD `45212948d0d88a3bcc9292810b465cd27cb3eaea`**. The connected workspace's repository-prefixed Git status independently returned the **same branch, HEAD and zero visible changes**. GitHub successfully supplied the numbering policy at that **explicit commit**. Episode evidence was read locally, including ignored material; remote tracked files were not substituted for local sources. GitHub cannot establish ignored-audio identity.

Exact input basenames below are under `sources/`. Only these **two E122 SRTs** were located there; no raw/third-model export was found in that episode-prefix inventory. Pipeline names are **inferred from filenames**, not verified run metadata.

| Export / exact basename | Bytes | Cues | Normalized tokens | First cue start | Last cue end |
| --- | ---: | ---: | ---: | --- | --- |
| `The Wastes S1E122. That's Ghost Water.parakeet.processed.srt` | 247,716 | 2,527 | 22,653 | 00:00:13.280 | 02:40:10.050 |
| `The Wastes S1E122. That's Ghost Water.qwen-q8.canary-ctc.nemotron.srt` | 333,000 | 4,114 | 22,879 | 00:00:13.280 | 02:40:09.790 |

SHA-256:

```text
Parakeet fce5a4c952131637a9657a4272786ad43761137cbf2398ca04e4f26ccfaf7f52
Qwen     304e6854cb0b997b8dd7bafb2ee5693075bd02d1a52027c9290f626f08d43ebb
```

Both parsed exports have **zero nonpositive-duration cues and zero adjacent overlapping cue pairs**. This is structural evidence, not acoustic coverage validation.

The matching-named local audio copy is **`local/The Wastes S1E122. That's Ghost Water.mp3`**, **153,873,298 bytes**, ffprobe duration **9,588.732567 seconds (02:39:48.733)**. Parakeet/Qwen end **21.317 / 21.057 seconds later**. This mismatch is an **open audio-copy/clock question**, not proof of invented outro speech, known clock offset or use of a different input. No historical ASR-input audio hash/run manifest was established. Audio was neither played nor uploaded.

Local-copy SHA-256: `4a0979e1f22e751eb0924c898be5d2bfa5f75c64c373fc5e72263db7a4dc54db` (does not identify the historical ASR inputs).

The retained local spreadsheet snapshot maps this episode to **TWBD 124**, and E123 to **TWBD 125: No Floating Forks**. Its catalogue dates are metadata, not verified recording dates. Private materials were not copied into tracked output.

## Exact metric and preparation

Used the repository's `tools/prepare_episode.py` with the exact source pair, ID **E122**, default ten-minute windows and output **`local/episode-analysis/E122`**. Its parsed cue content removes speaker decorations before joining text. Shared `asr_metrics` normalization lowercases, deletes straight/curly apostrophes, replaces every non-Unicode-letter/digit with whitespace and splits into tokens. The distance is **exact ordered unit-cost word Levenshtein over the complete sequences**, using the existing unbounded bit-vector implementation; candidate alignment is a separate calculation.

**1,755 edits / 22,653 primary Parakeet tokens = 7.747318235995232% inter-ASR text disagreement (7.75% rounded).** Direction/reference denominator: **Parakeet → Qwen**. Qwen has **226 more normalized tokens**. Neither the extra tokens nor the disagreement establishes which recognizer is correct. **This is not WER or measured recognition accuracy.**

The separate time-aware alignment produced **1,463 candidate groups**: **674 conflicting recognition, 750 possible omission and 39 uncertain segmentation**. Those labels are **unverified heuristics**, not confirmed errors or additional edits in the exact metric. SRT intervals are cue timings, not word timings.

## Editorial coverage

**Every primary cue was read**, in recording-clock batches **00:00–00:30, 00:30–01:00, 01:00–01:30, 01:30–02:00, 02:00–02:25 and 02:25 through final 02:40:10 speech/outro**. This covers all **17 generated primary windows**, including the two final cues after 02:40.

Qwen was **fully parsed for the complete-export metric**, with editorial readings selected at **00:18–00:39, 00:40–00:56:48, 01:35–01:39, 01:56–01:57:42, 02:10:12–02:13:30, 02:29–02:32 and 02:35 through final outro**. **Other secondary windows were not read throughout**, so this report does not claim full interpretive coverage of Qwen or an exhaustive discrepancy audit. Preparation outputs and the private phase checkpoint retain exact source hashes and reviewed ranges.

## High-risk differences and shared traps

| Recording window | Readings / hazard | Safe treatment and listening task |
| --- | --- | --- |
| ~00:21 | Parakeet **`elves of elhendar`**, Qwen **`elves of Elrond`** | Existing archive **Elhandar** is editorial orthography, not audio verification; do not create an unrelated setting from Qwen's reading. |
| ~00:22:51–00:24:26 | Parakeet **`rubistic trianglosphere` / `rubistic triangulosphere`**, Qwen **`robustic trianglosphere` / `rubistic trianglosphere`** | Device name remains provisional. Both describe fabrication then melting/sealing; **none has occurred**. |
| ~00:33:15–00:33:40 | Both produce unclear **`that she's you`** amid the mother's negative answer | Agreement does not settle meaning. Retain emotional negative maternity response without declaring Nash literally the mother. |
| ~00:34:37–00:36:54 | Parakeet **`dragons s ou l`**, later **`dragonsons`**, and **`produce their own dragons`**; Qwen **`Dragon Sons`** and **`produce their own dragon sons`** | Preserve cult/group wording alternatives. Human engineering, Clench and donor ancestry are **the dragon's claims**, not independently tested origin facts. |
| ~00:33:59–00:42:22 | Son **`yoshular` / `yosha lar`** versus **`Yshilar` / `Yoshalar`**; mother **`kaz de jere`** versus **`Cas de Gurey`** | Retain E121 alternatives too. No canonical name selected by recognizer majority or sound similarity. |
| ~00:55–00:56 | Parakeet **`and willing creature`**; Qwen **`An unwilling creature`**; both garble the resilient-sphere spell name | Check original cue and item rules against audio/handout; item has explicit one-minute, three-charge, movable/no-concentration rulings. Hope's extended imprisonment is attributed separately to Diontalus. |
| ~01:57 | Both render very little of the private headphone-off disclosure beyond **`you hear`** | Later Vorel says **giggling**, but neither text certifies the missing acoustic detail. No reconstructed private dialogue. |
| ~02:11–02:13 | Male custodian **`tomsilar bear`** versus **`Tom Cilabert`**; female **`aluneva`** versus **`Eluneva`** | Keep names provisional rather than equating them with an established elf. |
| ~02:30:58–02:31:24 | GM rhyme: **`you think i only know said but i actually know mage hand`** versus **`You think I only know sand? But I actually know mage hand`** | Do not repair `said` to `sand` or attribute the original wording to Scott. *Mage Hand* is **withdrawn as unsuccessful** under the GM's ruling. |
| ~02:35:49–02:36:04 | Hope's Nash impression **`yes the time box Nash don't eat the bottom`** versus **`Nev, the time bomb, Nash. The time bomb. Don't eat the bonbons`** | Necklace impersonation during play fight, **not a genuine time traveler or a Nash spell incantation**. |
| ~02:36:18–02:36:24 | Qwen adds a separate **“It's my turn / No, that's not your turn”** exchange absent from Parakeet's merged turn check | Possible overlap/recognition difference; no supported change to the ultimate jaw-opening action. |
| ~02:38–02:40 | Both finish with candy forced toward Nash's mouth/face, **next-time swallowing question**, then the network outro | Full transcript end read. Do not canonize ingestion, magical candy effects or a later completed rest; reconcile final clocks with the shorter local MP3. |

## Publication and remaining checks

Wrote the **local E122 dossier, comparison and model-log entry**, advanced the main research pointer to **verified E123 — No Floating Forks**, and reconciled the materially changed continuity, narrative and subject pages. E122 remains **ASR-provisional**. Vorel receives **no newly located title**; the Nash phrase register distinguishes the **GM-supplied failed-cast rhyme**.

Audio priorities are the **device/group/dragon/custodian names, mother's reply, wand rules, spike and burial, untranscribed private sound, failed casting wording and candy cutoff**. Exact input provenance and the approximately **21-second endpoint mismatch** remain open. No original SRT/MP3 changes, commit or push are implied.

**Validation:** All **26 changed Markdown files** read back; **2,119 link references** checked with **no missing local targets**. `git diff --check` passes. `npm run lint:markdown` checks **340 files** and still fails on **10 pre-existing violations**, versus **12 before this work**; terminal-newline fixes in the two expanded heart/dragon pages remove two old violations. Comparison against `HEAD` with the same installed Markdownlint library/config finds **zero introduced violations**, and the **two new core documents are lint-clean**. Both E122 SRT hashes and the local MP3 hash remain unchanged; Git shows **no original source/media edits**. Work remains **local and uncommitted** on the original branch/HEAD.

[p]: ../sources/The%20Wastes%20S1E122.%20That's%20Ghost%20Water.parakeet.processed.srt
[q]: ../sources/The%20Wastes%20S1E122.%20That's%20Ghost%20Water.qwen-q8.canary-ctc.nemotron.srt
