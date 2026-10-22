# January 2020 bonus — two-export ASR comparison (2026-10-22)

> **Two machine transcripts, one roughly 33½-minute bonus recording. No audio verification, reference WER, new model run or source SRT editing.** The [research dossier](../episodes/BONUS-2020-01.md) uses both exports, and **retrospective GM explanation is not contemporaneous E085 scene knowledge**.

## Inventory and technical method

| File under `sources/` | Filename-indicated pipeline, **not verified run metadata** | SRT cues | First cue / end | Casefolded normalized words |
| --- | --- | ---: | --- | ---: |
| [Parakeet processed](../sources/Bonus%202020-01%20-%20January%202020.parakeet.processed.srt) | Parakeet processed; exact version, decoder and options **unknown** | **666** | **00:00:03.0 / 00:33:28.6** | **6,105** |
| [Qwen Q8 + Canary CTC + Nemotron](../sources/Bonus%202020-01%20-%20January%202020.qwen-q8.canary-ctc.nemotron.srt) | Qwen Q8/Canary CTC/Nemotron per filename; exact versions/options **unknown** | **1,064** | **00:00:03.0 / 00:33:28.3** | **6,242** |

**Method:** parse cue starts/ends, concatenate text, strip `(speaker N)` decorations (not a speaker mapping), lowercase, remove apostrophes and punctuation, normalize whitespace, then calculate unit-cost **word-token Levenshtein distance** over the full texts (including ads/outro). Result: **434 edit operations / 6,105 Parakeet tokens = 7.11% first-export-relative text disagreement**. This is **not speech-to-text WER, proof of omissions or hallucinations, or evidence one recognizer is better**. Cue count alone is not coverage. Output-speaker IDs are not independently assigned to performers. Neither machine run's hardware, performance, model build, recording checksum, chunk strategy, VAD, decoding parameters or commands is present; **do not invent them**.

Both files start with modern **Chromebook** and **Priceline** ads; the actual bonus introduction begins at roughly **01:07**, shifting all substantive Q&A time offsets by that pre-roll. These advertisements **cannot date the original conversation**. The host explicitly says this is **the December 2019 bonus**, explaining that non-supporters may hear it **in January**. The owner's/publication normalization nevertheless assigns **BONUS-2020-01** to the **January 2020 public-release file**; the precise recording/member-release/public-release dates remain **unverified**. Do not silently rename the source to a 2019-12 file or conflate it with the separate [BONUS-2019-12](../episodes/BONUS-2019-12.md).

## High-impact comparisons and verification windows

| Approx. file clock | Issue observed in exports | Safe treatment until audio checked |
| --- | --- | --- |
| **~01:07** | Host names “December 2019”, then says heard “into January”; both ASRs broadly concur. | **Spoken bonus title vs normalized publication month are independent metadata**, with unknown exact release date. |
| **~02:00–03:10** | **Steel Heaven / Steel God / Principle / Chromianity**, “is Sigil that heaven?” | **No yes/no answer from Beau**. Do not merge the Principle's religion with Sigil or the Weir. Verify the exact religion spelling from a non-ASR source if canonical display needed. |
| **~04:55–05:45** | Beau explicitly calls E085's womanlike enforcement the **Lady of Pain**, names Royce champion **Ventro** and describes M-fighting's relative safety. | This is **GM retrospective identification**, not the unannounced apparition self-identifying in E085. Same title is **local Royce title**, not Kanja's overall BMF crown. |
| **~06:00–09:00** | Nash regenerating toward his **previous body**, Scott expecting **existing defects**, and the GM's **player agency** assurance. | **Strong creator forecast**, not proof a full human body, fixed old defects, permanent youth or working dragon shape has already been achieved. |
| **~09:15–12:00** | Jon describes Nothing's **internal voice and remembered-speech kenku curse**. Qwen contains an apparent internally contradictory phrase “there's no curse on the kengku”, while nearby context affirms a curse; Parakeet has different disfluent words at the same point. | **Don't quote the contradictory ASR phrase as doctrine.** Treat the stable explanation as **Jon's character interpretation**, not official D&D-universal rules. Listen before inferring who imposed the curse. |
| **~12:00–15:10** | Whether Hope/Stanley are revived and resume opposing the **Principle**; hypothetical **Weir-bound soul void**. | Players **cannot know**, GM says **“probably”** to a void-like experience. No played revival, suffering, time return or actual contract closure. |
| **~15:15–17:50** | **Diontalus/Dian Talus** (several ASR variants); confusion whether **Vorel or the Principle** proposed space-launch. | Vorel **wanted space disposal**, Principle's stated original plan was **imprisonment in crystal for study**. **Current crystal/soul location unverified**. Player-operated Twitter persona is **external roleplay, not in-story contact**. |
| **~18:00–19:10** | Vorel's imagined burning of city, possible party involvement in Nothing's **Pelvis** commission. | **Speculation**, not enacted arson, contract sharing, travel or kidnapping. |
| **~19:15–21:50** | Nash's blocked spells vs missing spell components; hints “someone” or “something” **externally negated** his effects. | GM explicitly says **Nash functionally retains former magical powers**. Exact Sigil-specific suppression rule is **intentionally not told**; don't infer divinity-exclusive mechanism or permanent impairment. |
| **~24:15–26:25** | Beau suggests turning custom marionette fighting into **cards, dice, hero sheets, perhaps a product**. | **Proposed future publication only**, not an actual published game or new match mechanics. |
| **~29:30–32:20** | Vorel's **potential contracts**, lemon farming and future celebrity in Sigil. | **Plans and jokes**; E085 sponsorships explicitly unsigned, no committed trip to merchants or time jump. |

## Decision and next verification

Use both transcripts to triangulate **episode-level meaning**, preserving uncertain proper names and role attribution. Explicit creator statements (Ventro's likely name, **Lady of Pain**, external cause of Nash's failed spells) may strengthen the world reference as **later GM testimony**, while the played-event documents continue to say **what the characters witnessed in E085**.

First audio listen: **01:07 title, 04:55–05:45 Lady/Ventro, 06:50–09:00 regrowth, 09:15–11:20 kenku curse wording, 15:30–17:10 Diontalus vs space-launch, 19:30–21:40 spell suppression**. Compare a few control regions as well as disputes, log audio-grounded speaker/time and exact accepted wordings, and preserve untouched raw export snapshots. No superiority claim, token error percentage against audio, or transcript correction is warranted from this report.

[Bonus dossier](../episodes/BONUS-2020-01.md) · [Prior monthly bonus](../episodes/BONUS-2019-12.md) · [Review queue](../project/REVIEW_QUEUE.md) · [Model tests](../project/MODEL_TESTS.md).
