# BONUS-2020-09 — full-export ASR comparison (2026-10-23)

[September 2020 bonus dossier](../episodes/BONUS-2020-09.md). **Out-of-game Wastes cast Q&A**, not a played episode. Both exports were read fully, including the Qwen-only ending cue. **638 exact ordered normalized word edits / 6,481 primary Parakeet tokens = 9.84% text disagreement**. Qwen has **240 more tokens**; neither figure measures correctness, confirmed omissions or WER. **No listening, new ASR execution or transcript correction.**

## Access, revision and source inventory

Research began on **clean local `main`, HEAD `f0b4db7a5bf0a80652e4c0d55fab1bdb8adac2ae`**. Direct filesystem access supplied complete current SRTs, local-only MP3 and retained provenance manifest. **Workspace MCP Git status independently matched repository, branch, HEAD and zero visible changes**, with zero restricted entries omitted. Connected GitHub read capabilities were discovered; no remote source copy was needed for evidence absent locally, and no remote revision was substituted. The current remote branch tip was not refreshed. All edits are local and uncommitted.

| Exact source / inferred pipeline | Cues | First start | Last end | Normalized tokens | Bytes |
| --- | ---: | --- | --- | ---: | ---: |
| [Bonus 2020-09 - September 2020.parakeet.processed.srt][p] — processed Parakeet, primary | 697 | 00:00:04.240 | 00:36:42.690 | 6,481 | 68,696 |
| [Bonus 2020-09 - September 2020.qwen-q8.canary-ctc.nemotron.srt][q] — Qwen Q8 / Canary CTC / Nemotron | 1,102 | 00:00:04.240 | 00:36:47.920 | 6,721 | 90,968 |

Model/pipeline labels are **inferred from filenames**. Actual model builds, hardware, run flags, diarizer configuration and recognition runtime are unknown. No additional same-basename raw/alternate export was found in `sources/`; no independent third pass was generated. Matching introduction, topic sequence and farewell support pairing; the historical recognizers' exact input-audio bytes remain unverified.

| Input | SHA-256 of original local bytes |
| --- | --- |
| Parakeet SRT | `c305a2dd650e43a4f45a0d9d5fa9017fdd8797182b8a8918022279b00f304af8` |
| Qwen SRT | `8767a265d407715e1a8bb708747f717d237ee552e3de1b72788985e40ee1f283` |
| Matching local MP3 | `865dad334e99c4facf0d5499ea2a818ed97c042259373c7809f84116790fc355` |

**Audio association:** `local/Bonus 2020-09 - September 2020.mp3`, **35,738,032 bytes**, ffprobe duration **2,205.278438 seconds (00:36:45.278438)**. Hash and size match the retained **`local/bonus-identification-2026-10-22/rename-manifest.json`** entry: original `010.bonus_twbd_Sept_2020.mp3`, owner-sheet row **143**, publisher title **`TWBD Bonus 9-15-2020`**, [archived publisher URL](https://shows.acast.com/there-will-be-dungeons/episodes/6501086309d52c00124340e6). Historical correlations **0.97515 / 0.98064** were inspected, **not rerun**. No audio or linked source was downloaded or uploaded. This is provenance evidence, **not listening verification**.

The filename is a **public-publication-month label**. Scott's description of early supporter access and his “today” Solar Mines recollection do not supply an exact recording day. E117 contains a matching retelling; **neither publication order nor this content association establishes recording order relative to E118**. [Machine-readable measurements](BONUS_2020_09_ASR_COMPARISON_2026-10-23.json).

## Reproducible metric and coverage

1. Parse each entire SRT into chronological cues using `tools/build_transcripts.py::parse_srt`, removing cue indices, timing lines and leading speaker decorations; join cue text. Both files were checked to be in start-time order.
2. Use `experiments/asr_backfill_2026_10_23.py::tokens`: lowercase, delete straight and curly apostrophes, replace every character other than Unicode letters/digits with whitespace, then split. Contractions are joined; no name normalization or editorial repair is applied.
3. Use that module's **exact unrestricted unit-cost ordered word Levenshtein** `distance`, an arbitrary-width Myers bit-vector recurrence. No time buckets, anchors or band limits affect this distance. It was checked against scalar dynamic programming on **1,000 deterministic random token pairs** with seed **202009**, lengths 0–24 over a three-token alphabet, in both directions. Full-sequence reverse calculation also returns **638**.
4. Direction **Parakeet → Qwen**; denominator **6,481 Parakeet tokens**. **638 / 6,481 × 100 = 9.8441598519%**, rounded **9.84%**. The **Qwen-only trailing two words are included**. Alignment/candidate counts are not this metric. This pass neither benchmarks recognition performance nor identifies a more accurate model.

Both complete lexical exports were read in **00:00–00:08, 00:08–00:16, 00:16–00:24, 00:24–00:32 and 00:32–end recording-clock chunks**, with small opening passages reread after output truncation. Adjacent same-speaker cues were grouped only for the reading display; words were not reconciled. Critical windows were reread with original cue IDs. Parakeet ends after the farewell; Qwen adds a separate final cue. Numeric labels are **episode-local**: contextual answers support **0 Scott, 1 Kristen, 2 Beau, 3 Jon, 4 Kyle**, but some short turns are split/merged differently and Qwen's tail has **Unknown** attribution.

## High-risk text differences and listening queue

| Clock / cues | Export evidence | Treatment |
| --- | --- | --- |
| ~00:47–01:29; P 17–30 / Q 26–45 | P `truncatedversion`, `solar minds`, broken transition; Q `truncated version`, `Solar Minds Tech`, fuller transition | Scott says the fuller uprising account was not told; E117 content association only, no completed missing history or proved date |
| ~03:19–03:24; P 65–67 / Q 98–102 | P `i didn't hook up with any`; Q `Stanley didn't hook up with anyone`; speaker splits differ in nearby Beau/Jon exchange | Denial and player/character distinction; no new romance, no imported speaker mapping |
| ~04:14–05:39; P 86–110 / Q 130–171 | P `brint` and lost addict wording; Q `Brent, the fixable addict`; `dying tallus` / `Dian Talus` | Victim/substance wording needs listening; Jon playing Diontalus is not Stanley choosing his murders or killing the archfey |
| ~05:42–05:52; P 113–115 / Q 175–180 | P garbles Vorel's knowledge clause; Q `Burrell would know what a lion is` after doubting lions exist | Continuity banter; do not establish universal presence/absence of lions |
| ~06:35–07:19; P 129–141 / Q 209–234 | Both retain unused Squirts inspiration; Q has additional reaction words; `Flynn` unclear in both | Forgotten option, not performed reroll or proof of survival; preserve E111 death |
| ~10:52–11:22; P 207–214 / Q 336–346 | P `bach bach`, `fate for`, `slave down`; Q `Bachbach`, `Fate Four`, `Slave Town`; both `Lizard King` | Kyle's retrospective consequences; established Bok Bok/Fate 4/Slavetown referents, no new title or first-use backdating |
| ~12:15–12:54; P 226–239 / Q 365–391 | P `something he could control`; Q `not something he could control`; Q also clearer that party did not witness forced joining | **Meaningful negation/knowledge risk**. Beau's surrounding explicit forced-joining account supports attributed discussion, not invented shared knowledge |
| ~18:09–18:28; P 345–350 / Q 556–565 | Initial `forty eight` / `48`, then explicit `4d6` and total below 70; six/seven hesitation | Qualified reconstruction of roll method; no 48-die system or audited original stats |
| ~19:47–19:56; P 374–375 / Q 597–602 | P `serious that's standard array`; Q `serious. This was standard array` after minotaur answer | Standard-array minotaur answer; precise name wording unresolved, do not silently repair a quotation |
| ~22:00–22:30; P 411–419 / Q 664–679 | Both ask immunity then Kyle says resistance; P truncates `home`, Q `homebrew` | Distinguish Kyle's correction and Beau's homebrew shrapnel description from official rules or new powers |
| ~31:41–32:22; P 599–608 / Q 933–951 | P `Henry henrikson`, Q `Skunk Henrikson`; P `not the holiday`, Q `not the the harlequinari` | Scott's red-blood description clear; **membership/nonmembership clause unresolved**, not a new identity claim |
| ~34:09–34:40; P 643–651 / Q 1006–1023 | P `sabriel liriel of course`; Q `Sabriel, Lyriel, and Horison` | Kristen's book/name/Ariel inspiration; no verified literary titles or new canonical spelling |
| ~35:30–35:38; P 670–672 / Q 1061–1066 | P `gruntled` / Q `disgruntled` in employee joke | Opposed joke wording; no factual source for VHS-cover anecdote, no lore consequence |
| ~35:49; P 677 / Q 1072 | P `character is just red`; Q `character is just rad` | Likely praise context; do not turn this into Lyrielle's skin/clothing color |
| 00:36:44.800–00:36:47.920; Q 1102 only | Q **`Holy God.`**, Unknown speaker; no Parakeet counterpart | Starts within the MP3's last half-second but **ends 2.641562 seconds past its measured duration**. Could involve recognition/timing or copy mismatch; listen to the actual ending before any verdict |

The Qwen ending anomaly does **not** prove a longer underlying recording, audible speech, absent Parakeet speech or hallucination. The file association is supported by retained provenance; an exact historical ASR-input hash is unavailable. Both models' cue times remain coarse source timings, not verified word-level alignment.

## Documentation follow-through and validation

The [dossier](../episodes/BONUS-2020-09.md), [review queue](../project/REVIEW_QUEUE.md), [model log](../project/MODEL_TESTS.md), root navigation and affected existing subject pages record **creator interpretation and unplayed alternatives**. No main-event chronology or narrative chapter is advanced. Vorel's existing **Lizard King** recollection is indexed as retrospective; no new Nash casting phrase is added. Latest played research stays **E118**; next main source **S1E119 — Put Out The Fish Fire** and next monthly bonus **BONUS-2020-10** both have verified nonempty Parakeet/Qwen pairs.

**Validation:** All **14 Markdown files changed by this bonus pass pass Markdownlint** with the repository configuration, including both new documents. The **101 new/changed relative link targets and anchors resolve**; table-column/duplicate-heading checks pass after repairing one pre-existing missing cell in the touched review queue. Three pre-existing excess-blank-line violations were cleaned in touched subject pages. Comparison JSON parses and agrees with source measurements; both SRT hashes and the MP3 hash/size are unchanged. `git diff --check` passes. Markdown/link checks do not verify audio or recording dates.

The final full **`npm run lint:markdown`** snapshot checks **309 maintained files** and exits **1** with **eight pre-existing MD012 violations in seven untouched files**: E113's comparison (34–35), `world/CHARACTERS.md` (57), `world/PLACES.md` (59), `world/WORLD.md` (49), Hope's profile (65), the Stanley/Diontalus navigation page (10), and Vorel's profile (67). All eight were independently reproduced from initial HEAD contents. These are distinct from the passing changed-file checks; the inventory grew as concurrent research files appeared.

**Concurrent work:** An independent **E119 dossier, comparison and Dilenoria profile appeared during validation**. They were left untouched and excluded from this bonus pass's changed-file claims. E118/E119 pointers above describe this pass's established main-story boundary; separate work may advance it. The initial clean state and pinned HEAD remain documented, without claiming the final checkout contains only this task's edits. No commit or push was made by this pass.

[p]: ../sources/Bonus%202020-09%20-%20September%202020.parakeet.processed.srt
[q]: ../sources/Bonus%202020-09%20-%20September%202020.qwen-q8.canary-ctc.nemotron.srt
