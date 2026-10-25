# August 2021 bonus — complete-export Parakeet vs Qwen Q8 comparison (2026-10-25)

**Identity:** [BONUS-2021-08 — August 2021 supporter Q&A](../episodes/BONUS-2021-08.md), owner-normalized source `Bonus 2021-08 - August 2021`. **Out-of-game post-Delvers-S2E12 discussion**, not a played campaign session; actual recording/publishing day unverified. [Wastes/cross-campaign queue](../project/REVIEW_QUEUE.md).

**Provenance:** MCP workspace `main` initially **clean** HEAD `1701b3789a536e9197540e497f2ed92cea24a58a`. Both source exports actually fetched at **that exact Git commit**, and initial Parakeet lines independently checked with MCP reader. No known evidence of file changes between revisions. Original MP3, publisher metadata, Discord images and run-metadata/settings unchecked.

| Filename model/pipeline label (not verified runtime flags) | Exact SRT source | Git blob SHA | Cues | Lowercase Unicode normalized words | Final timestamp |
| --- | --- | --- | ---: | ---: | --- |
| Parakeet processed | [P](../sources/Bonus%202021-08%20-%20August%202021.parakeet.processed.srt) | `3da1823da02abe4f8aa034e5f354dbda0435549b` | **621** | **5,991** | **00:31:28.860** |
| Qwen Q8 / Canary CTC / Nemotron-labelled | [Q](../sources/Bonus%202021-08%20-%20August%202021.qwen-q8.canary-ctc.nemotron.srt) | `cfdf2ffa58f56c000ccc288c345b9de960c0e2bc` | **936** | **6,095** | **00:31:28.620** |

**Exact full-export word-level unit-cost ordered Levenshtein: 353 / 5,991 = 5.89% textual disagreement**, **NOT word error rate (WER), model accuracy, confirmed omission/hallucination or audio truth**. Q has **104 more normalized words**, ending **0.240 seconds earlier**.

**Exact method:** Parse **all** chronological SRT cues, exclude cue index/timestamp lines and `(speaker N)` decorations, concatenate texts, lowercase, remove apostrophes `'`/`’` to join contractions, tokenize runs of Unicode letters/digits; all other punctuation separated. Strip **57 identical prefix tokens and 23 suffix tokens**; two-row exact Levenshtein DP inside **±900 token-index diagonal band**, optimum **353 <900** certifies global exact route does not leave band. Full primary text read in **0–5, 5–10, 10–15, 15–20, 20–25, 25–30, 30–31:28** min recording-clock groups. Complete Q file parsed for metric, independent Q **0–4, 6–11, 17–22, 22–27, 27–31:28** min groups text-reviewed, NOT full independent narrative read. Original audio not listened to.

| Clock window | High-value independent comparison / listening sensitivity |
| --- | --- |
| **00–05** | Host calls **recent S2E12 finale** completed but does **not explicitly date recording August**. Guest **Garrett** wanted elf hunter, **Brian** requested Oceans Eleven heist; Kyle says dragon battle truncated due to guest roleplay and scheduling, not secret deliberate Brotherhood hair bait. |
| **~05–11** | Scott explains Krandal's **unspent farm gold due to fear of bad soil/death/commitment before first harvest**. Three-month skip and hypothetical later upgrades **not actual history**. Modern-school clique description **hypothetical**. |
| **~14–18** | Cast's virtual multiplayer TWBD tabletop software suggestion is **proposal**, not actual program; digital character sheet vs physical mini desire out-of-game. Koh **possible only indirect paperwork support to Blackwood robbery**, no named perpetrator verified. |
| **~18–22** | Dragon battle **compressed**, possible future live battle **wish**, not replayed; comparison of Bo's introspective Wastes/Stanley role with Kyle's compact Delvers show is subjective creative preference. |
| **~22–24** | **Critical GM-secret**: performers **take off headphones** and Kyle tells audience **S2E10 Khalazar shade mechanical Mummy Lord CR15 with full stats**; cast **did not hear** and no character knows. Verbatim source must be audio verified before quotation/absolute stat-sheet fidelity. |
| **~24–29** | **Psychic rogue** class choice (Jon), GM organic improvisation and strange underground sound hook, coma-wife biography worked into plot. Story focus not predetermined; aspirations of untraceable attacks **not actual assassinations**. |
| **~29–31:28** | **Pelor god of agriculture** acknowledges compatible farm pursuit; cleric “god change” is **speculative alternate path**, not an event. Sponsor-question sign-off and next-month intent, no actual played scene. |

**Major limitations and next tests:** Original MP3/handouts/Discord and timestamps not verified, no audio-checked accuracy, no authorial confirmation of exact vocal proper-name spellings or speaker turns. If audio review available, sample **22–24 min GM confession first**, then **16–18 min Koh forgery** and **8–11/29–30 min farm deity**. SRT files unchanged. [Next bonus September 2021](../sources/Bonus%202021-09%20-%20September%202021.parakeet.processed.srt) verified in source corpus but not yet researched.
