# BONUS-2021-02 — February 2021 archive bonus ASR comparison (2026-10-25)

**Content classification:** Out-of-game cast Q&A, not played campaign material. **Date discrepancy:** the owner-normalized archived basename uses February 2021 as the **public-publication-month category**, but the spoken host welcome says this is **the second of two January 2021 bonus episodes**. The preceding [BONUS-2021-01](../episodes/BONUS-2021-01.md) likewise anticipates a second instalment. Preserve the owner-normalized February source identity and do not infer recording/early release/public publication day solely from the dialogue.

**Revisions:** Both complete source files fetched from private `frankysan/There-Will-Be-Dungeons-Transcripts` at `6d0d427f662d920bbe01a29309d4e00294c6371c`, matching the initially clean connected workspace's `main` HEAD.

| Filename-inferred pipeline | Exact source file | Git blob SHA | Cues | Final cue end | Word tokens |
| --- | --- | --- | ---: | --- | ---: |
| Parakeet processed (reference) | [`Bonus 2021-02 - February 2021.parakeet.processed.srt`](../sources/Bonus%202021-02%20-%20February%202021.parakeet.processed.srt) | `234477733f16d54546793171ff641c168b7121e1` | **636** | **00:33:10.869** | **6,001** |
| Qwen Q8 / Canary CTC / Nemotron-labelled | [`Bonus 2021-02 - February 2021.qwen-q8.canary-ctc.nemotron.srt`](../sources/Bonus%202021-02%20-%20February%202021.qwen-q8.canary-ctc.nemotron.srt) | `1499845b8def09f1d156ce3b1fb940628b1d42d7` | **924** | **00:33:11.240** | **6,116** |

## Exact full-export ordered-text disagreement

**397 token edits / 6,001 primary tokens = 6.62%.** Qwen has **115 more normalized words**. This is **inter-export text disagreement**, not word error rate, ASR accuracy, a confirmed audio omission or hallucination percentage. The 0.371-second difference in final subtitle endpoints does **not** demonstrate source audio identity or seek alignment.

For both complete SRT files: split numbered cue blocks; discard cue indexes and timing headers; join utterance text in cue order; strip optional `(speaker N)` tags; lowercase; remove apostrophes `'` and `’` (so contractions join); replace runs of all other characters except Unicode letters/digits with spaces; tokenize on whitespace. Calculate **unit-cost ordered word Levenshtein insertions, deletions and substitutions**. A rolling-row dynamic program with **900-token diagonal band** found distance **397**, strictly below band width; a lower-cost unrestricted path could not exit the band, establishing an **exact optimum**. Common ending suffix comprised three normalized tokens; there was no identical prefix. The code did not create/rewrite transcripts, and `tools/prepare_episode.py` was **not executed**.

**Research coverage:** The complete processed Parakeet SRT was read sequentially from welcome through its final farewell. The **entire Qwen source** was tokenized for the metric, with additional selected passages read at the start, guest-player discussion, subclass response, Nash/Solar Mines, Groxl and closing theology; Qwen **was not independently close-read throughout**. The audio was **not listened to**, local MP3 copy/duration **not opened or measured**, original ASR model settings and matching input audio hashes **not verified**, speaker diarization **not audio-verified**.

## Cross-source, claim-sensitive windows

| SRT clock | Finding / why listening matters |
| --- | --- |
| 00:00–00:01 | Both exports support **“two in January … second of those two”** while normalized files say `February 2021`. Public-release/recording date is **open**; changing canonical archive numbering from dialogue alone would recreate prior source-identity hazards |
| ~00:01–00:07 | Other RPG systems (Star Wars, The Expanse etc.), Starfinder/Pathfinder adaptations, audio formats, streaming rights, and proprietary sounds are *hypothetical*. No campaign launch or licensing/legal opinion is established |
| ~00:07–00:09 | Listener's **coloring-book proposal** discussed. Fan/possible commercial variants distinguished; no actual product approval, license or concrete release |
| ~00:08–00:11 | The cast recognizes a “missing voice,” is open to **Beau's possible return or guests**, and Kyle says Veggie Sticks **could have been played by a guest**. This is not evidence that he actually was guest-voiced, or of any confirmed future participant |
| ~00:11–00:15 | Scott consciously **preplans as Krandal** more than as Nash; Kristen plans front-line space control, Jon reconciles tactics and character-limited knowledge. GM appreciates rapid turn flow. These are creator-method statements, not fictional actions |
| ~00:15–00:21 | Imagined Thanksgiving dishes expose Stanley's scarcity-minded attraction to **clean water and available food**, Nash's indiscriminate eating, Vorel's imagined gravy and Hope's possible mashed potatoes. Keep a hypothetical dinner separate from played Wastes food inventory |
| ~00:21–00:23 | Jon mentions a *Tasha's* subclass **for Koh**, not Stanley. A proposed Stanley rogue dip is only a possibility; possible Hope Artificer arm solution is audience speculation. Compare S1E05 for later actually-played Koh developments |
| ~00:23–00:25 | Scott expresses worry about Nash as the **center of Solar Mines/Time Bar/multiple Nash foreshadowing**, but explicitly lacks knowledge of Beau's planned outcome. Do **not** transform it into a canonical secret ending or player request that changed Beau's story |
| ~00:25–00:26 | “principal's deal” in both ASRs is likely **Prince of Deals**; check audible title. Jon reports Stanley feels sad but still struggles upward; no new bargain in this bonus |
| ~00:26–00:28 | **Groxl/Grozil/Grosil** ASR variants, old-friend mystery and White Tower separation: Kyle discusses Vorel's uncertainties, rather than confirming divine truth, future meeting or permanent separation. Mastermind's pursuit/assassins are imagined future reactions |
| ~00:28–00:33 | Deity discussion contrasts Wastes Fishbird with **Pelor** and mythological pantheons. Scott enjoys exploring Krandal's religion but relationship still developing. Opinions on Greek/Egyptian/Norse/Roman cosmologies **do not introduce those religions into Delvers canon**. Both transcripts reach final farewell |

## Research follow-up

Highest priority listening: date characterization **00:00–00:00:40**; `Prince of Deals` **~00:25:30**; Groxl/voice/Mastermind **~00:26–00:28**; guest/player future **~00:08–00:11**; actual ending **~00:33:10**. Always check SRT-to-audio offsets first. No direct edits to Wastes or Delvers fictional chronology should derive from this **discussion-only** source.

[Full bonus dossier](../episodes/BONUS-2021-02.md) · [Shared review queue](../project/REVIEW_QUEUE.md).
