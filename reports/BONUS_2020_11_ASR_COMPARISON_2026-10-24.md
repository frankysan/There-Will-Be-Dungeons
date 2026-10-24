# November 2020 bonus — complete-export ASR comparison, 2026-10-24

**BONUS-2020-11 · out-of-game cast Q&A**, mainly *The Wastes* through **E123**, not a numbered played episode. [Dossier](../episodes/BONUS-2020-11.md) · [Parakeet][p] · [Qwen-labelled][q]. Both complete texts read; **no listening, source correction, ASR rerun or benchmarking**.

## Identity, access and dates

Initially clean direct checkout **`main`, HEAD `ee72b957c26492c6a08ae965e63e0f4214259bc1`**. Connected workspace repository-prefixed Git status returned the **same branch/HEAD and zero visible changes**; GitHub supplied the numbering policy at that **explicit commit**. Episode evidence, ignored audio and the retained catalogue snapshot were read locally. No remote tracked bytes substituted for local-only evidence.

Catalogue original **`TWBD Bonus from 11-01-2020`**, listed public release **9 November 2020**, owner-normalized **`Bonus 2020-11 - November 2020`**. Closing speech says **going up today / tonight on November first**. These are **distinct evidence classes**; supporter timing is a spoken claim, with year from metadata, not a verified upload/recording timestamp. E123's conversation/candy events are a **content association**, not independent recording-date proof.

| Exact basename under `sources/` | Bytes | Cues | Normalized tokens | First cue start | Final cue end |
| --- | ---: | ---: | ---: | --- | --- |
| `Bonus 2020-11 - November 2020.parakeet.processed.srt` | 57,779 | 584 | 5,393 | 00:00:05.840 | 00:30:14.460 |
| `Bonus 2020-11 - November 2020.qwen-q8.canary-ctc.nemotron.srt` | 74,688 | 897 | 5,549 | 00:00:05.680 | 00:30:14.140 |

Only these two bonus exports were located in the episode-prefix inventory. Pipeline labels come **from filenames**, not verified historical model/build/aligner/diarizer settings or exact acoustic inputs.

SHA-256:

```text
Parakeet 65703c5a7c5243c609078dc26e3fd67c6adba5c853c2b6bcac04ee7e54dc2d10
Qwen     709fb3fd5344d6c05db44ba4c32c0fd5dc4c9a428410f0ded29035b1d4221484
MP3      a208c064b1ab69adb1a14e73c12ab607502538e02822c07aa646ff86a492c8eb
```

Matching-named local audio **`local/Bonus 2020-11 - November 2020.mp3`**, **29,569,351 bytes**, ffprobe duration **1,819.735878 seconds (00:30:19.736)**. SRTs end **5.276 / 5.596 seconds before** that endpoint. The untranscribed tail was **not listened to or classified as silence**. Filename/time association does not prove these bytes were the original ASR input. Audio was not uploaded; private raw materials unchanged/unpublished.

Both inputs have **zero nonpositive-duration cues**. Primary has zero adjacent overlaps; secondary has **one 1-ms overlap at cues 821–822, 00:27:45.099**. Structural checks do not certify words/speakers.

## Method, measurements and coverage

Prepared the exact pair with **`tools/prepare_episode.py --id BONUS-2020-11`**, fresh output **`local/episode-analysis/BONUS-2020-11`**, default ten-minute windows and candidate alignment. Parser joins cue content after speaker-decoration removal. Shared normalization lowercases, deletes straight/curly apostrophes, replaces non-Unicode-letter/digit characters with spaces and splits into tokens. Existing unbounded bit-vector implementation computes **exact unit-cost ordered word Levenshtein over both complete sequences**.

**434 edits / 5,393 primary Parakeet tokens = 8.0474689412201% inter-ASR text disagreement (8.05% rounded).** Direction/reference denominator **Parakeet → Qwen**; Qwen **+156 tokens**. **Not WER, accuracy or proof that extra text is correct.**

Time-aware alignment separately produces **326 candidate groups**: **148 conflicting recognition, 160 possible omission, 18 uncertain segmentation**. These labels/counts are **unverified review heuristics**, distinct from exact edit operations. SRT clocks are cue intervals, not word timings.

**Both exports read completely**, in **00:00–00:10, 00:10–00:20, 00:20–00:30 and final 00:30–00:30:14** batches, all **four windows per export**, including opening/supporter context and final website/farewell. No unseen secondary windows are represented as reviewed.

**Targeted supplementary E114 check only:** In `The Wastes S1E114. I hope that's a baby.parakeet.processed.srt`, cues **2453, 2476–2477**, and corresponding `qwen-q8.canary-ctc.nemotron.srt`, cues **4147, 4182**, the texts identify the newborn as a boy near **02:36:27**, and give **two girls and two boys near 02:38:07–02:38:12**. These narrow passages contextualize the bonus's uncertain recall/possible Nash Junior assignment. **No full E114 reread, fresh E114 distance or audio check**. Exact supplementary source paths/hashes are retained in the local checkpoint; [E114 dossier](../episodes/E114.md) and [existing comparison](E114_ASR_COMPARISON_2026-10-23.md) retain their original research scope.

## Substantive differences and interpretation hazards

| Recording | Readings / hazard | Treatment |
| --- | --- | --- |
| ~00:00:41 | Listener-question fragments **Nash / Nash slash Gas / Gas** | Context is Nash/Scott's appetite; do not create a new character from Qwen's recognition. |
| ~00:02:24–00:05:08 | Listener presumes Nash's time travel explains Stanley's family; Scott's King Arthur analogy is qualified | Question premise/metaphor is not a demonstrated cause or new title. Jon says current blame is not aimed at Nash. |
| ~00:05–00:06 | Question calls Diontalus **lowly**, Kyle condenses dragon death | Jon pushes back; no downgrade of archfey capability, erasure of rescue/healing or new death scene. |
| ~00:11:50–00:12:53 | Parakeet vague **picked up** / **lord**; Qwen **picked up in Tietkala** / **lore** | GM's retrospective growth discussion, not a new pickup scene or canonical rank; align wording against audio. |
| ~00:13–00:16 | Same-level/stat switch, restricted knowledge, patron/played form explanation | Historical player model, not new sheet verification, a regained form or proof scythe losses can never be cured. |
| ~00:17:57 | Parakeet **codie / foleying**, Qwen **co DM / folding** | Production/co-DM joke in context, not formal role reassignment or an in-world craft. |
| ~00:19:38 | Parakeet **`i don't find it super good`**, Qwen **`I find it super good`** | **Negation difference can reverse evaluation**. Surrounding praise does not verify the exact words; no audio-grounded preference quote selected. |
| ~00:24:53–00:25:22 | Parakeet's hypothetical Pipe speech fragment **`my father was a think he handled things`**; Qwen **`my father was a bit reckless. I don't think he handled things`** | Imagined future characterization, not a performed Nash/child spell or actual personality change. |
| ~00:25:57–00:27:04 | Both show uncertain child-gender recall, Jon's **Nash Junior girl** suggestion and apparent acceptance; Qwen has a fuller Jon line | Preserve **earlier E114 two-girls/two-boys text**. Later creator discussion may propose an individual assignment; no updated handout, individual naming-map verification or retconned birth scene claimed. |
| ~00:27:25–00:28:18 | Kyle's counterfactual boots; cast says feet remain and suggests retrieving them | **No crafting/recovery**. Do not add boots to inventory, new bonuses, remains custody transfer or a completed memorial. |
| ~00:28:37–00:29:32 | Temptation, resistance and early society-at-any-cost mindset | Jon's account of interiority, no actual reunion/godhood. Scott's lovers joke is not a romance revelation. |
| ~00:29:32–00:30:14 | Both explicitly **November first**, after same-day upload/supporter wording | Keep spoken supporter-date claim separate from catalogue **November 9** public release; year inferred from original label/context, not spoken here. |

## Follow-through

The dossier, model log, bonus queue and materially affected profiles/ledger preserve **retrospective attribution**, the **E114 child-count distinction**, and **unperformed boots/spinoff/reunion**. No played chronology/narrative advancement; main research remains **E124**, latest played dossier **E123**. No new performed Vorel title or Nash spell phrase found.

Next available bonus pair is **January 2021**; no December 2020 bonus source found in the local source-prefix inventory. Verify **date/supporter context, gender intent, class-switch wording, negation, track identity and remains proposal** through listening/creator notes as needed. Music licensing/current site contents were not researched; no audio fidelity judgment is made.

**Validation:** All **13 changed Markdown files** read back; **1,404 link references** checked with no missing local targets. `git diff --check` passes. `npm run lint:markdown` checks **345 maintained files** and fails on **8 pre-existing violations**, versus the **10-violation baseline**; expanding the Hope/Vorel profiles removes their former trailing consecutive blank lines. Same-library/config comparison with the **initial pinned revision** finds **zero introduced violations** and both new core files lint-clean. Both bonus SRTs, local MP3 and two supplementary E114 SRT hashes are unchanged. Git shows **no original source/media, played chronology or narrative changes**.

**Concurrent Git change:** During final verification, the checkout advanced externally to **`04e37872b5c868f5f473f271c257e959cecb5c1e` (`Bonus 2020-11`)**, containing the 13-file research update. At the final check, **this report's validation note and Angelashi's spoiler-scope clarification remain local modifications**. The research agent issued **no commit, push or remote-write command**; initial revision/provenance above is retained rather than silently rebased.

[p]: ../sources/Bonus%202020-11%20-%20November%202020.parakeet.processed.srt
[q]: ../sources/Bonus%202020-11%20-%20November%202020.qwen-q8.canary-ctc.nemotron.srt
