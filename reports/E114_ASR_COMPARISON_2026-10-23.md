# E114 — full-export ASR comparison (2026-10-23)

[Episode dossier](../episodes/E114.md). **The Wastes S1E114 — I hope that's a baby** is a played Arc Five main-party session. Both existing exports were read through the final network outro. **1,981 exact ordered normalized word edits / 22,701 Parakeet tokens = 8.73% inter-model text disagreement.** Qwen has **418 more tokens**; this is not a confirmed omission count, WER, or an accuracy ranking. **No audio listening or ASR rerun occurred.**

## Input inventory and access

Research began with a **clean local `main`** at `162bd714fe77b9632de913bc716f50eb0ac53d49`. Direct filesystem reads supplied the transcripts, ignored MP3, Git state and edits. The **workspace MCP Git status** independently reported the same repository, branch, commit and zero visible changes. **GitHub** supplied the numbering-policy introduction at that explicit commit, confirming the owner-column-I archive convention; it was not used to substitute remote SRTs for local sources. No unresolved revision difference was found between those identities; this does not establish the newest remote branch tip.

| Input / filename label | Exact repository-relative path | Cues | First start | Last end | Normalized tokens |
| --- | --- | ---: | --- | --- | ---: |
| Processed Parakeet, primary | [The Wastes S1E114. I hope that's a baby.parakeet.processed.srt][p] | 2,542 | 00:00:10.080 | 02:42:02.720 | 22,701 |
| Qwen Q8 / Canary CTC / Nemotron | [The Wastes S1E114. I hope that's a baby.qwen-q8.canary-ctc.nemotron.srt][q] | 4,288 | 00:00:02.720 | 02:42:02.340 | 23,119 |

Both sources were available in full. No additional E114 raw/alternate ASR export was located beside these files. Model, quantization, aligner and diarizer labels are **inferred from filenames**; model builds, actual run configuration, hardware and runtime remain unverified.

| Input | Raw bytes | SHA-256 of local file bytes |
| --- | ---: | --- |
| Parakeet SRT | 248,975 | `ea4c0fa8ae7070c57c4dd06dc9872f0a7fc2cc3428a19f2dd74366c011c839b8` |
| Qwen SRT | 343,964 | `b0a605282686f2829464ce87f585da97ccbde143182e233c6af21c11af89c7e0` |
| Matching local MP3 | 156,135,241 | `52e1121cfad197a3624c7c870f1bdf9db826871e9f42328f2f031be45e9019ac` |

The audio copy is **`local/The Wastes S1E114. I hope that's a baby.mp3`**, associated by exact archive basename. **ffprobe reports 9,730.104 seconds (02:42:10.104)**. This fingerprints the available copy. Historical ASR-run metadata was unavailable, so the exact input bytes used to generate these exports remain unverified. The roughly seven-second interval after the final text cue was not listened to. See the [machine-readable measurements](E114_ASR_COMPARISON_2026-10-23.json).

The owner-catalogue attribution **TWBD 116 / August 10, 2020** is retained from the pinned [E113 dossier](../episodes/E113.md); the original spreadsheet was not independently reopened, and a recording date is not established by that publication metadata. E115's exact two filenames were checked locally; no publisher number was extrapolated.

## Exact metric and reading method

1. Parse chronological SRT cue content, discarding cue indices and timing lines; remove optional `(speaker N)` decorations and join cue text.
2. Lowercase; delete straight and curly apostrophes, joining contractions; replace every other character except Unicode letters and digits with whitespace, then split into tokens. Punctuation and speaker IDs are not words.
3. Compute **unrestricted, ordered, unit-cost word Levenshtein distance** between both complete sequences, using a Myers bit-vector recurrence with Python arbitrary-precision integers and one pattern bit per whole word. This is not the repository's heuristic time-anchored candidate count or a bag-of-words difference.
4. Validate the recurrence against scalar dynamic programming on **1,000 deterministic random sequence pairs**, in both directions, including empty sequences. Additional checks cross 64/128/256-bit lengths; identity sequences give zero and shifted sequences give two. The complete reversed-direction calculation also gives **1,981**. Divide by **22,701 primary Parakeet tokens**, not Qwen's count or their average.

For full text reading, recording-clock ten-minute chunks represented both exports using shared lexical text once and explicit **P/Q alternatives** for differing words, retaining all lexical content through the outro. Matching capitalization/punctuation was folded only in that reading display, **not used to replace either source file**. High-risk windows were reread directly with original cue IDs and speaker decorations. One-minute display boundaries can create apparent end/start differences; those are not evidence of missing speech. No text was reconciled into a canonical transcript.

## Concrete disagreements and listening targets

| Recording clock | Parallel-export evidence / risk | Interpretation retained pending listening |
| --- | --- | --- |
| 00:00:02.720–00:00:14 | Q cue 1 puts `Hello, everyone.` at 02.720–10.720; P begins the greeting at 10.080 | Opening cue alignment differs; do not infer extra greeting speech or an audio-copy offset from this alone |
| ~00:10–00:15; 00:24–00:27 | **Philanthalar / Philanthula / philanthlear**, **Lyrielle / Liriel / lirael**, garbled surname **Korlani/Quarlani (?)**, **Doctor Evany/Vani/Avigne (?)** | Provisional names, with separate characters for the greeter, new PC and other doctor; no global numeric-speaker mapping |
| ~00:37–00:41 | **Solania** and **Toesalt / To Salt / Towsalt**, “the Tremendous”; uncertain projection wording following surface blast | Crew estimates are not a census; pirate employer and connection to explosion unknown |
| ~00:41–00:44 | Angelashi's private changeling disclosure; P `new` versus Q `no` in the line-of-sight rules answer; actual Animate Objects attempt then private failure | GM explicitly says living forms are not objects; no successful animation or genetic scan |
| ~00:47–00:53 | P/Q preserve the GM's **“lifeless” → “unconscious”** self-correction for Bok Bok; **Shield** and **Wall of Force** are separate actions | Bok Bok survives; Shield is not an established air seal; doctor's Wall of Force is the effective barrier |
| ~01:24–01:26 | **Pill offered by Mage Hand**, then refused; UI hit points and table corrections differ from superficial reading | No Vorel consumption or fresh pill exhaustion; no completed long rest inferred from his wording |
| ~01:40–01:42 | Declared move toward archer is rewound due to existing grapple | Keep the final adjudicated action against Fluffy, rather than record both incompatible positions |
| ~01:55:15–01:55:38 | P `there once was a hell / lettuce` versus Q `There once was a vagina. Whatever the / hell that is.` across speaker turns; main Larry/hairy/Carrie limerick broadly agrees | Preserve interruption and uncertain preamble; successful Performance, not casting or actual baby naming |
| ~02:08:15–02:08:32 | Both give **`just because you think it's a toot it will actually be a boot`**, with different cue/speaker boundaries nearby | Nash's nonmagical labor poem; lexical agreement is not audio verification |
| ~02:12–02:16 | P **`you're not charmed`**, Q **`you're now charmed`** (~02:13); discussion and ensuing narration show intended entry into mouth | Record the GM-adjudicated Command and Stanley killing Fluffy before entry, not an unperformed swallowing or settled general rules interpretation |
| ~02:25–02:34 | Cloudkill comes down tube; Stanley's Telekinesis rescue, concentration loss and named doctor overboard | Unknown fog caster; Vorel rescued, attempted elf rescue fails; no invented survivor count or universal off-ship death declaration |
| ~02:34–02:40 | Early fourth-child description switches **she/he**; Q **`Oh, sorry`** where P lacks apology; final narration explicitly gives **two girls, two boys** | Four living children; do not assign all individual sexes/forms or names; Angelashi transforms, Nash's ancestry remains a disputed assertion |
| ~02:41–02:42 | Network tag splits `frogpants` / `com` across slightly different cue boundaries | Both reach final speech/outro; final cue times are not certified audio speech boundaries |

## Decision and next scope

The provisional episode result is **four living changeling children and Angelashi's visible revelation**, alongside **Fluffy's death and the ship's successful escape with significant elven losses**. **No Elhandar arrival, Squirts resurrection, confirmed Principle death, or settled Nash ancestry**. The [dossier](../episodes/E114.md), [continuity ledger](../world/CONSISTENCY_LEDGER.md) and [review queue](../project/REVIEW_QUEUE.md) carry the same distinctions. The two labor poems are classified separately from spells in [Nash's register](../world/characters/nash-spellcasting-phrases.md#related-wording-and-non-casting-performances).

Next verified source pair: **The Wastes S1E115 — The Forest for The Trees**, [Parakeet](../sources/The%20Wastes%20S1E115.%20The%20Forest%20for%20The%20Trees.parakeet.processed.srt) / [Qwen](../sources/The%20Wastes%20S1E115.%20The%20Forest%20for%20The%20Trees.qwen-q8.canary-ctc.nemotron.srt). Files are nonempty; no E115 content is analyzed here. Original SRT/MP3 files remain untouched.

## Documentation validation

**20 changed/new Markdown files pass Markdownlint with the repository configuration; 60 new/changed local link targets and anchors resolve.** The measurement JSON parses and agrees with the recorded counts. `git diff --check` passes. Source SRT and matching MP3 SHA-256 fingerprints are unchanged after editing; no original media/transcript path appears in Git changes.

The full **`npm run lint:markdown`** command checks **256 maintained Markdown files** and reports **two MD012 blank-line violations in the untouched E113 comparison report, lines 34–35**. The same two violations are reproduced directly from that file's **initial HEAD contents**; they are pre-existing, and the file was left unchanged. The runner covers all Markdown directories changed in this pass. These checks do not constitute audio verification. Work remains **local and uncommitted**.

[p]: ../sources/The%20Wastes%20S1E114.%20I%20hope%20that%27s%20a%20baby.parakeet.processed.srt
[q]: ../sources/The%20Wastes%20S1E114.%20I%20hope%20that%27s%20a%20baby.qwen-q8.canary-ctc.nemotron.srt
