# Wastes S2E10 — Full-export inter-ASR comparison (2026-10-26)

**Episode:** Played *Wastes* Season Two S2E10 **“Big Mouthful of Carpet”**; [source-first dossier](../episodes/S2E10.md). The original audio was NOT listened to, and no manually corrected transcript exists for WER/accuracy testing.

**Evidence & provenance:** Workspace MCP `main` HEAD `4d6728c1ebc9c743871f7bf0983af3297188a45c` started clean; exact normalized source names found, both local opening cues checked. Whole transcripts read from GitHub default-branch Git blobs listed below; full local-vs-remote byte equivalence not independently established. Labels below are filename-derived rather than checked model execution metadata; no run hardware, model build or configuration asserted.

| Full independent source | Git blob SHA | Cues | Normalized words | Last SRT end | Text characters |
| --- | --- | ---: | ---: | --- | ---: |
| [Parakeet processed](../sources/The%20Wastes%20S2E10.%20Big%20Mouthful%20of%20Carpet.parakeet.processed.srt) | `533a0ff4e5249187879e514881236f89f9a0d67d` | **2,522** | **22,582** | **02:31:17.870** | **233,836** |
| [Qwen Q8 / Canary CTC / Nemotron](../sources/The%20Wastes%20S2E10.%20Big%20Mouthful%20of%20Carpet.qwen-q8.canary-ctc.nemotron.srt) | `9ac7b639440dd496b4d7a0f37a60c1104f448af4` | **4,368** | **23,234** | **02:31:17.640** | **329,249** |

**Exact method:** Parse entire chronological SRT cue speech; omit cue ordinal/timing lines and optional `(speaker N)` decorations. Concatenate text, lowercase, remove straight/curly apostrophes (joining contractions), replace everything other than Unicode letters and digits with spaces, and split into normalized words. Compute unit-cost **global ordered word Levenshtein edit distance** (insert/delete/substitute) P→Q with two-row dynamic programming and diagonal ±5,000 band; **2,472** is strictly less than width, hence equal to unrestricted global optimum. Parakeet is the denominator: **2,472 / 22,582 = 10.95% inter-ASR text disagreement**, Qwen has **652 additional normalized word tokens**. **NOT WER, an omission/hallucination count, audio accuracy or proof of one model's superiority.**

## Targeted listening priorities (NOT audio verified)

| Approx. recording time | High-impact review |
| --- | --- |
| **~00:08–00:11** | Whether dragon transformation is heart-activated magic suppressed while Nash's fused-DNA underwear flight persists; Tungsten's rumor of collector ring also operating prison dais. Do not turn proposed ring into acquired item. |
| **~00:29–00:35** | Bandaged corpse described jokingly as similar to Nash/mummy; **finger actually transferred to Nash's pocket**, unlike unverified corpse identities. |
| **~00:45–00:50** | **Old *Light* peeling physically transferred to skull's eye socket** as lantern; no fresh cast, later precise skull ownership at end unresolved. |
| **~01:12–01:20; ~01:39–01:50** | Multiple **animated carpets** restrain/smother Nash and Stanley; Vorel and Hope help free, later all slain. Potentially mislabeled number/locations of rugs due maps not visible. |
| **~01:22:50–01:23:20** | Earlier **Corpse Slayer Dagger returned from Vorel TO STANLEY** by explicit player confirmation; Stanley then uses it against rug ~01:47. |
| **~01:24:40–01:25:50** | **Private** Hand-of-Voice ruling: 2d8 cold on Hope's weapon remains active, later applied to magical dagger attacks. Do not impute party-shared secret. |
| **~01:30–01:32** | Nash *proposes* **Chromatic Orb**, then immediately remembers anti-magic **before declaration/resolution**; no slot spent and no Nash rhyme. |
| **~01:51–01:57; ~02:10** | Tungsten's **speculative** living-carpet explanation and specimen shards in Hope/Union/Tungsten storage; Nash's decorative sandals **acquired and bagged**, no tested magic. |
| **~02:18–02:29** | **Telepathic invitation** from eastern eye/tentacle area (source not independently identified); **two OTHER voices** from reanimated seated corpses actually warn of soul loss. **Tungsten pulled toward it and grappled**, Vorel **fails INT save 7, drops rope and actually enters**, Hope fails to hold tail. Do not claim escape, resolution, collected ring, corpse attacks or eye identity. |

**Coverage:** Entire Parakeet read in chronological blocks through outro; entire independent Qwen export parsed for counts and exact global comparison, selected Qwen segments independently inspected covering intro, carpet choice/assault, dagger return, Hand interaction, specimen acquisition, sandals, and final mental intrusion. **This is not a complete second editorial review and no original audio was auditioned**. No raw SRT edited. [Next episode source](../sources/The%20Wastes%20S2E11.%20Flesh%20Sauce.parakeet.processed.srt) independently inventoried; not analyzed.
