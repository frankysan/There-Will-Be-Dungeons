# Delvers S3E03 — Thank You For The Deposit: exact ASR comparison (2026-10-25)

**Source-identity follow-up, 2026-10-27:** The [S3E04–S3E01 batch check](DELVERS_S3E04_S3E01_SOURCE_IDENTITY_2026-10-27.md#s3e03) verifies both complete local exports against their recorded Git blobs after CRLF-to-LF conversion only, and verifies both source paths in the recorded source commit. Raw bytes differ in line endings. This independently confirms local content correspondence with the originally pinned source revision. Earlier provenance statements remain dated history. Prior interpretive coverage, inter-ASR measurements, played cutoff and audio status are unchanged.

**Campaign/episode:** [Delvers S3E03 — Thank You For The Deposit](../delvers/episodes/S3E03.md), played Season Three. Host introduces episode as **weekend of 2021-08-21**, not independently checked publication date. Guest **Bo Schwartz** performs new halfling bard/journalist Dumbledwark. **Actual cutoff**: reporter obtains **C4 licence** and **steals warlock's tome**; guild promise of grounding relief is **future**, dungeon **NOT entered**.

**Repository/source provenance:** Initial clean local MCP `main` at **`351c80f93c4eba3a62296f92e8c146fd6719336e`** (no visible changes). GitHub accepted **same pinned commit** and supplied **both complete SRT files at that exact ref**. Audio copies inventoried locally but **not listened to**; no cast-posted city map, newspaper handout, character sheet, publication metadata, audio fingerprint or verified inference-config/runtime/hardware examined. Inferred pipeline labels derived **solely from source basenames**, NOT independently verified model settings.

| Export | Relative source | Blob SHA at pinned commit | Complete cues | Words | Final end |
| --- | --- | --- | ---: | ---: | --- |
| P / Parakeet processed | [P](../sources/Delvers%20S3E03.%20Thank%20You%20For%20The%20Deposit.parakeet.processed.srt) | `34d39fae8c959f417f3731d4fafd8beeb0375ba6` | 2,425 | 22,254 | 02:25:29.470 |
| Q / Qwen Q8–Canary CTC–Nemotron | [Q](../sources/Delvers%20S3E03.%20Thank%20You%20For%20The%20Deposit.qwen-q8.canary-ctc.nemotron.srt) | `5d4ba1d8e1cb7bb2bd85443d378dcd7f644267e7` | 4,129 | 22,574 | 02:25:28.670 |

**Exact complete-export unit-cost Levenshtein word distance = 2,052 / 22,254 = 9.22% ordered inter-ASR textual disagreement.** Q has **320 more Unicode-normalized tokens** and ends **0.800 sec earlier**. **NOT WER, measured transcription accuracy, or known omissions/hallucinations.** No one-to-one word timestamp alignment or per-model omissions asserted.

**Reproducible method:** Extract complete chronological SRT cue speech; remove cue index/timestamp and `(speaker N)` marker; join cue lines; lowercase and delete curly/straight apostrophes to join contractions; replace non-Unicode-letter/digit characters with space; split into word tokens. **100 identical prefix tokens / 3 suffix** removed for performance only. Two-row DP unit-cost insert/delete/substitute **±3,600 token-index diagonal** produced **2,052**, strictly below band, which ensures exact global optimum; a narrower **±2,000 band also returned 2,052 but could not certify optimality** and was NOT used for final exact claim. Identical algorithm to previous dossiers. All primary Parakeet source interpreted in sequential clock windows **0–28, 28–56, 56–84, 84–112, 112–145:29**, including last spoken profanity after network ident. Complete Q processed for metric; Q independently inspected selected excerpts **0–8, 8–13, 35–42, 44–56, 75–85, 88–99, 111–120, 122–140, 127–134, 136–145.5 min** (partial output clipped; no complete interpretive Q reading). No audio.

| Clock | High-risk independent listening focus |
| --- | --- |
| **~00:00–00:14** | Bo/Beau performer spelling; Dumbledwark of Raisinbunch, editor Chroma / staff names; **supposed paid-informant prophecy**, not authenticated, and C4 missing Silver deaths/claimed total six. |
| **~00:14–00:32** | Koh's refusal to discuss charges, reporter's **insight that details withheld** not guilt revelation, and **Koh photo actually taken**. |
| **~00:32–00:56** | Centaur Allspice carriage fares; Lady Vestal drains fountain as class-photo distraction; **Evelyn already in Loran base**, no actual re-enacted door unlocking; her Cassius belief/Selenar rumor are not proof. Reporter **forgot Evelyn photo**. |
| **~00:56–01:14** | Gleepo Ma **actively sells harvested farm potatoes** (no quantified revenue); reporter actually commissions **gilded potato** and gives Krandal; snake worker and farm map imagery uninspected. |
| **~01:14–01:41** | **Krandal voluntary signed Zone of Truth and actual bank-theft disclosure** to journalist, no verified Cassius causal link; refusal to recruit Koh to similar session; Krandal **photo taken**. |
| **~01:41–01:48** | Reporter does **not** cast Speak with Animals, but **does deposit feces in Krandal's compost box**; no downstream crop result. |
| **~01:48–02:03** | Jimmy the Soup implies bribe but no accepted payment; Zoltar acting guildmaster in Cassius office; Dumbledwark **detects magical Warlock's Tome in stacked crates**, not yet acquired. |
| **~02:03–02:17** | Zoltar **accuses Delvers/Cassius of ball disaster**, claims Cassius magically entrapped and eventually **admits economic interest in not defeating Khalazar**. Attribute testimony and distinguish coercive inference from observed reality. |
| **~02:17–02:23:49** | **C4 LICENCE actually handed to reporter**, **warlock's tome stolen by Sleight of Hand 20**, Zoltar promises **tomorrow** grounding relief and agrees reporter to chaperone. **No Delvers notification nor C4 entry this session**. |

**Editorial caution:** The “two light/one shadow” verse is a supposed guild informant prophecy quoted by newsroom, not verified canonical cosmology. Zoltar's self-incriminating profit statement is actually spoken and he agrees to exploit PR, but his claims of Cassius confinement and Delvers-caused catastrophe are **not independent verification**. New journalist's theft custody is firm; “mysterious tome from Cassius's office” does **not** establish Cassius owned it.

**Status:** Text-only evidence; no original MP3 listening; independent Q-window selection not entire second narrative; no source media changed. [Next Delvers S3E04](../delvers/SOURCE_INVENTORY.md).
