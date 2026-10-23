# E104 — complete Parakeet/Qwen comparison (2026-10-23)

> **The Wastes · corrected S1E104 — I Blew A Dragon For THIS · played campaign session.** [Source-first dossier](../episodes/E104.md). **Text-only research, no audio listening, human reference transcript, verified speaker map or accuracy ranking.** Both full exports read in consecutive recording-clock windows through their final speech, postgame and outro. No new ASR run or source edit.

## Input inventory and access

Research began on clean local **main**, HEAD **`bf0c95f75607484ba934f78eb221c708d9516a1f`**, repository **`frankysan/There-Will-Be-Dungeons-Transcripts`**. Direct filesystem supplied both complete SRTs and editing support. **InfinityDB OAuth Probe** independently reported the same repository, branch, HEAD and zero visible changes. Connected **GitHub** supplied prior-episode context from `episodes/E103.md` pinned to that exact commit; no default-branch revision was silently substituted. Local ignored media was available only through direct access. No private archive was consulted or uploaded.

| Exact input path / filename-derived label | Access / association | Cues | First start | Last end | Normalized tokens |
| --- | --- | ---: | --- | --- | ---: |
| [sources/The Wastes S1E104. I Blew A Dragon For THIS.parakeet.processed.srt](../sources/The%20Wastes%20S1E104.%20I%20Blew%20A%20Dragon%20For%20THIS.parakeet.processed.srt) — processed Parakeet | Direct checkout at starting HEAD; primary export | 3,063 | 00:00:10.080 | 02:57:02.960 | 26,633 |
| [sources/The Wastes S1E104. I Blew A Dragon For THIS.qwen-q8.canary-ctc.nemotron.srt](../sources/The%20Wastes%20S1E104.%20I%20Blew%20A%20Dragon%20For%20THIS.qwen-q8.canary-ctc.nemotron.srt) — Qwen Q8 / Canary CTC / Nemotron | Direct checkout at starting HEAD; independent recognition export by filename | 5,426 | 00:00:10.000 | 02:57:02.780 | 27,229 |

**SHA-256, measured from local bytes:**

- Parakeet: `49c82590fca8f47b9166da3b4fcbe56af1912b38121595dda461209286031b1c`.
- Qwen: `ead1b6ceea17f16bbc6670faba7256335220c8c624e220bafb8b8b100ff08086`.
- Matching local basename: **`local/The Wastes S1E104. I Blew A Dragon For THIS.mp3`**, **170,421,577 bytes**, **02:57:03.000** container duration measured with `ffprobe`; SHA-256 **`45467c3b0873f7ba2addd0abff72253064696e26ba168ac27e64d6c2f2dc0178`**. **Filename and duration association only**: these measurements do not prove which audio bytes produced either ASR export. MP3 tags supplied no title, album, track or date. Audio was not played.

No additional E104 raw/alternate-model export was found among the source files or matching local basenames. Model/pipeline names above are **filename inferences**, not verified build/run metadata. Decoding flags, VAD settings, model versions, hardware and run durations are unknown. The corrected archive identity is exact; **original publisher ID/title and recording/publication day remain unverified**, rather than inferred by arithmetic from another episode.

## Measurement and reproducibility

Extract chronological SRT cue bodies; remove numeric cue indices, timing lines and optional `(speaker N)` decorations; join text, lowercase, delete straight/curly apostrophes to join contractions, replace non-Unicode-letter/digit characters with whitespace, and split into tokens. Both inputs were checked by the existing parser/measurement functions in [the comparison-backfill implementation](../experiments/asr_backfill_2026_10_23.py). Its `tokens` function uses Unicode `isalpha`/`isdigit`, and its **exact arbitrary-width bit-vector Levenshtein** uses unit insertion, deletion and substitution costs, without timing buckets, anchors or approximate cutoffs. An independently written local bit-vector calculation reproduced the result and passed **500 seeded short-sequence checks against rolling-row dynamic programming**. The repository implementation independently returned the same full-export totals and distance.

**Parakeet → Qwen: 2,686 ordered word edits / 26,633 primary Parakeet tokens = 10.09% text disagreement.** Qwen has **596 more normalized tokens**; that difference is not a count of confirmed omitted speech. **This is not audio-grounded WER, transcript accuracy, confirmed hallucinations or evidence that one recognizer is better.** Shared aligner/diarizer labels do not provide independent speaker verification.

To reproduce only the measurements, from the repository root (no ASR, writes or backfill regeneration):

```python
from pathlib import Path
from runpy import run_path

helpers = run_path("experiments/asr_backfill_2026_10_23.py")
paths = sorted(Path("sources").glob("The Wastes S1E104.*.srt"))
runs = [helpers["read"](path.resolve()) for path in paths]
for stats, _, words in runs:
    print(stats["path"], stats["cues"], stats["last_end_ms"], len(words))
edits = helpers["distance"](runs[0][2], runs[1][2])
print(edits, len(runs[0][2]), 100 * edits / len(runs[0][2]))
```

The global distance ignores speaker tags and does not validate diarization. Numeric source speakers must be mapped within this episode; **Kristen and Kyle explicitly say they have swapped computers/accounts (~00:10–00:11)**. Account names and reused character slips are unsafe speaker evidence. SRT intervals are cue-level, not word-level timing. The leading ten seconds and any non-speech gaps were not audio-checked.

## High-risk text comparisons and interpretation

| Recording clock | Specific source evidence / disagreement | Safe treatment |
| --- | --- | --- |
| 00:04–00:06 | Both have **sloppy but acceptable** and the patron's apology; segmentation places the phrase at different cue starts | Patron accepts station fire; no tested Hand-power restoration |
| 00:07:50–00:08:05 | Parakeet reduces the recognition to **Cinderborn**; Qwen supplies **Omnium Cinderborn**; subsequent both use Omnom/Amnom/Nam Nam variants | Match prior **Omnom Cinderborn** contextually; his physical survival is distinct from his testimony of Razak Val's fall |
| 00:15:43–00:16:35 | Crowd interjection is garbled: Parakeet **“you feel see me why” / “i knew it”**, Qwen **“You're still not” / “I'm not”**; craftsman **“better” / “Battered”** | Do not create a named official, insult or house affiliation from these uncertain lines |
| 00:25:50–00:27:15 | Both show **Celibus/Cullivus Stump's animated corpse**; Qwen explicitly retains **“He's a zombie”** while Parakeet lacks that short sentence | Undead appearance is supported by the surrounding scene in both; exact omitted/added wording needs listening |
| 00:33–00:37:30 | Both open Asmodeus-addressed gate without summoning him; Qwen preserves **“not Pharrell, Doctor Spider”**, while Parakeet compresses the correction | Dr. Spider, not Vorel, follows Hope; **Spatulo and Steerious's two tieflings cross**; destination unseen |
| 00:53:15–00:53:30; 01:15–01:24 | Calls vary **“some ga feet a blazar” / “Sunge Feinablazar”** before separate **Sunga, Fina, Blazar** machine labels | Keep provisional divisions and names; no separate settled spell/faction name |
| 01:12–01:18 | Battle appears to send escorts down, but one small boat is visibly alongside at 02:03 and used later | Record losses without inventing two permanent escort destructions or a new replacement vessel |
| 01:30–01:33 | Acid breath and acid damage are explicit; both later contain GM **“lightning breath”** wording | One acid attack; no silent new lightning power or second attack |
| 01:48–01:54 | Both retain **9**, deity spelling **O-L-I-D-A-M-M-A-R-A**, requested moon removal and GM's post-break confirmation; stray **Hope** in returning party list | Squirts causes the intervention; **Stanley/Vorel**, not absent Hope, Feather Fall from disappearing mech; damage remains |
| 01:57–02:17 | Admiral variants **Walls / Boobin Walls / Booben walls / Wallace**; crew says overboard, then dead | Separate reported death from recovered body; do not merge with earlier Captain Meart/Myard |
| 02:16–02:28 | Both **Snatch**, fruit instructions and wrong first attempt; Parakeet's **“baby head”** contrasts with Qwen **“baby hand”** at 02:28 | Recognize established back-hand mutation, not a new infant head; retain raw alternatives |
| 02:34–02:43 | Both show party/case escape; Qwen identifies destroyed ship **The Great Angelashi**, Parakeet renders **“the flashy”** | Same named main ship, destroyed by tentacles; Snatch's rescue was intended, then not depicted |
| 02:45–02:54:50 | Both have performed **Lesser Restoration**, framed window, corrected ritual, **ten orcs** and ship entering closing gate | Sam recovers; arrival still withheld. Fruit-gathering declarations precede final luck-roll inventory |
| 02:55–02:57:02 | Qwen preserves extra connective outro words, both end **“So we did it”** after network sign-off | Full transcript ending included; no audio validation of placement or wording |

## Review boundaries

See the [dossier's custody table](../episodes/E104.md#custody-and-open-checks-at-cutoff) and [review queue](../project/REVIEW_QUEUE.md). The later [June-publication bonus](../episodes/BONUS-2020-06.md) discusses an **unused mecha-piloting alternative**; E104 instead directly depicts **Squirts's Divine Intervention**. Neither source proves the moon's destination. Hope's two saved residents are not the orcs on the separate planar airship. **Main ship destruction is resolved; arrival after the second portal is not.** No original SRT/MP3 changed, no canonical speech correction, commit, push or new ASR processing performed.
