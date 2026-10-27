# Delvers S2E12 — The Bell of The Ball: exact complete-export ASR comparison (2026-10-25)

**Source-identity follow-up, 2026-10-27:** The [S2E12–S2E08 batch check](DELVERS_S2E12_S2E08_SOURCE_IDENTITY_2026-10-27.md#s2e12) verifies both complete local exports against their recorded Git blobs after CRLF-to-LF conversion only, and verifies both source paths in the recorded source commit. Raw bytes differ in line endings. This independently confirms local content correspondence with the originally pinned source revision. Earlier provenance statements remain dated history. Prior interpretive coverage, inter-ASR measurements, played cutoff and audio status are unchanged.

**Identity:** [Delvers S2E12 — The Bell of The Ball](../delvers/episodes/S2E12.md), **played Season Two and second-arc finale** (owner confirmation). Main finale cliffhanger **active Hereditary Drone open under ballroom, possessed/compelled elves enter pit, Wildfire and Withers both fall into underground opening**, no true-Khalazar defeat. [Delvers queue](../delvers/REVIEW_QUEUE.md).

**Source provenance:** MCP `main` initially HEAD `2dcbb98eaf12484e91225dacdf60d0a81f092a60` with **two unrelated existing illustration-doc edits**; **both P/Q exports fetched from GitHub at exactly that matching commit**, local first-cue snippets checked separately. Published/recording date, original audio bytes/offset and pipeline runtime settings/compute performance **NOT verified**.

| Label from filename only | Source | Git blob SHA | SRT cues | Unicode normalized words | Last cue |
| --- | --- | --- | ---: | ---: | --- |
| Parakeet processed | [P](../sources/Delvers%20S2E12.%20The%20Bell%20of%20The%20Ball.parakeet.processed.srt) | `a9b7f9d5cbba70c4f4ccfa2d95704de2e399739a` | **2,727** | **24,975** | **03:01:28.240** |
| Qwen Q8 / Canary CTC / Nemotron-labelled | [Q](../sources/Delvers%20S2E12.%20The%20Bell%20of%20The%20Ball.qwen-q8.canary-ctc.nemotron.srt) | `e2b59b51a2b184dc476e6e68e29de6ec85246af0` | **4,245** | **24,995** | **03:01:28.300** |

**Exact ordered unit-cost word edit Levenshtein distance = 1,620 / 24,975 = 6.49% inter-ASR textual disagreement**. Q has **20 more normalized words**, and final cue ends **0.060 seconds later**. **NOT WER/accuracy, not proven hallucination/omission and not a validated winner.** Full primary P manually narrative-reviewed through complete outro/last line, complete Q parsed for metric and selected Q windows compared; no audio.

**Algorithm:** Chronological SRT cue parsing, remove cue IDs/time lines/`(speaker N)`, lowercase, delete straight/curly apostrophes to join contractions, other non-Unicode-letter-or-number glyphs replace with spaces, tokenize. Strip **57 identical prefix tokens, 0 suffix**, then two-row dynamic programming with **±2,400 token-index diagonal band**; optimum **1,620 < band** certifies globally exact edit distance (outside band would require more than 2,400 insertions/deletions). **P reviewed in contiguous ~ten-minute recording clock windows 0–181:28**, Q entire parsed but only independent selected windows (0–8, 65–81, 89–103, 108–123, 123–137, 137–150, 150–166, 166–179, 179–181.5) checked; some Q segments visibly excerpt-clipped. No audio, handouts, map art, original model log or runtime benchmarks checked.

| Clock | Specific high-risk disagreement / human listening target |
| --- | --- |
| **~00–30** | Ball begins this episode; **Anthela really receives Dagger of Venom and Driftglobe**, Koh coat-checks Cape of Mountebank, **no actual sale of dragon skull**. |
| **~30–68** | Evelyn uses hidden hammer bag, **Krandal keeps face maces after coat check**, mysterious Mr. Goodwine potato-spirit proposal is **NOT a paid deal**. Fallen guild memorial names audio-needed. |
| **~72–96** | **Cassius's magical speech triggers Wisdom save/compelled smiles**, but exact spell/relationship to later drone **unidentified**; silver heroes publicly acknowledged at ball. |
| **~97–112** | Evelyn **actually changes Lady Blackwood dress but retains hair up** and meets **Gentleman Cavalier Traveler**, blonde and no facial hair, masks/cane/sword; never supplies actual name despite question. |
| **~104–122** | Snake Island **Princess Hissia** identifies herself as Krandal's romantic beloved and giver of snake staff/armor; Krandal's own memory fragments remain unreliable. **Ribbon physically given to Traveler**; princess and traveler both new live appearances. |
| **~123–139** | Maestro possessed with Khalazar voice, Selenar mouth accuses Withers; **Withers says he hired Broscales/opened doors**; exactly what contract/door needs original speech check. Khalazar body not directly observed. |
| **~139–156** | Physical Drone **emerges through ballroom floor**, roper transports compulsively arriving elves, hook horrors block doors, Evelyn given **unidentified diamond-heart handle** by Lady Vestal. **Wildfire AND Withers fall into separate hole**, neither death confirmed. |
| **~156–172** | Koh saves Mack/Church, Krandal Zoltar, Evelyn and GCT teleport/hack through gricks/darkmantles. **Evelyn learns 3-HP hand-squeeze Lay-on-Hands**, not just usual slap. |
| **~172–181:28** | Water cube drains to tunnels; **Carrie's fireball bracelet expended**, but rock doesn't collapse. **~25 ballroom tables** block hole, **drone continues and elf subjects still digging**. GM mentions Season Three in **three months in-world** but **NOT played**, Wastes plans production-only. |

**Pending verification:** original audio for named entities, item mechanics, magical speech and possessed Withers testimony, exact GCT curse provenance and royal snake memory, affected guest fate. Source SRTs and MP3 untouched.
