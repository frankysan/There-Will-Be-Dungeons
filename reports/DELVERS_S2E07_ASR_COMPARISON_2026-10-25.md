# Delvers S2E07 — The Devils Eggs: exact complete-export ASR comparison (2026-10-25)

**Source-identity follow-up, 2026-10-27:** The [S2E07–S2E03 batch check](DELVERS_S2E07_S2E03_SOURCE_IDENTITY_2026-10-27.md#s2e07) verifies both complete local exports against their recorded Git blobs after CRLF-to-LF conversion only, and verifies both source paths in the recorded source commit. Raw bytes differ in line endings. This independently confirms local content correspondence with the originally pinned source revision. Earlier provenance statements remain dated history. Prior interpretive coverage, inter-ASR measurements, played cutoff and audio status are unchanged.

**Episode:** Played Delvers S2E07, on Gemholm and in the offshore underwater laboratory. [Source dossier](../delvers/episodes/S2E07.md) · [Delvers queue](../delvers/REVIEW_QUEUE.md). At start local MCP `main` was **clean** at `bba3e150ed807966cd540e0c0c29218037f77c80`; both GitHub exports pinned to same ref. Original publisher/recording date, MP3 alignment and same source-audio bytes **not independently checked**.

| Filename-labelled ASR export (runtime/options NOT established) | Source | Pinned Git blob | Cues | Normalized words | Last cue end |
| --- | --- | --- | ---: | ---: | --- |
| Parakeet processed | [P](../sources/Delvers%20S2E07.%20The%20Devils%20Eggs.parakeet.processed.srt) | `21e24394085960a57a51eb383397545353c50845` | 2,476 | 22,664 | 02:48:24.250 |
| Qwen Q8/Canary CTC/Nemotron labelled | [Q](../sources/Delvers%20S2E07.%20The%20Devils%20Eggs.qwen-q8.canary-ctc.nemotron.srt) | `2834696fe3564ce583a6f1aaa30b3c6548dd23ac` | 3,961 | 22,617 | 02:48:23.980 |

**Global exact ordered unit-cost Levenshtein word edit distance: 1,520 / 22,664 = 6.71% textual disagreement.** Q contains **47 fewer normalized words**; ends **0.270 seconds before P**. **NOT WER**, model accuracy or validated omissions/hallucinations.

**Method:** Parse all numbered SRT cues, omit index/timestamp lines and optional `(speaker N)` markers. Join chronological utterances; Unicode letter/digit normalization with lowercasing, straight/curly apostrophe removal (joins contractions), other punctuation replaced by whitespace. Word-token lists compared via two-row dynamic-programming **±2,300-token diagonal band**. Identical **24-word leading** and **2-word trailing** segments removed mathematically without changing distance. Computed **1,520 < 2,300** proves no optimal path can exit band; this is exact global edit distance, not time-alignment candidates. **Every P 10-minute source-clock window 00:00–02:48** read chronologically; full Q parsed for metric, but secondary semantic reading only selected windows (~12–18, 28–32, 42–47, 53–59, 75–82, 87–94, 111–120, 135–142, 143–152, 152–165 min). **No sound listened**, original shared Discord diary/map images not read and no model command/run config or reference transcript available.

| Approx. recording clock | Comparison evidence and priority |
| --- | --- |
| **~00:14–00:19** | **Key painted by Mack with Evelyn's magical paints (#2)** actually opens workshop. Magical permanence and item name not checked against spell-specific rules. |
| **~00:30–00:45** | **Hank Tom and Caleb diaries** describe gem sliver, suspicious drinks, infection symptoms. NPC log spelling/attribution **Hank Tom, Caleb, Ambermoor** worth checking against **GM image**; only text read in ASR. |
| **~00:56–01:02** | Ambermoor diary starts `chaos gems` whose substance sounds `kage/chaos phage`, and **Koh's claw + failed CON 10** leads to internally moving egg; compare original written diary and audio. |
| **~01:10–01:21** | **Compelled Duel** physically attracts fleeing slaad via **table GM house adjudication**; **Balmer** swimsuit name label; creature regenerates earlier wounds. Koh's **natural-20 medicine** extracts larva, **crushes under hoof**; not cured by healing spell alone. |
| **~01:28–01:35** | Ambermoor's diary references **weaponization, kingdom/vampire faction sale, distilled chaos phage, Destin transforming into green and Neko as perfect-subject**. All are written **NPC claims**; cannot assert buyer contact or complete creature development beyond scenes. |
| **~01:40–02:00** | Eve drives crab #2, rescues **#3 key from burned Destin house** despite external bump from large unidentified creature. **Church larva visibly disappears under Evelyn's Lesser Restoration**, but does not prove all stages curable. |
| **~02:12–02:28** | Koh swims hidden underwater escape tunnel; alarm on main door **actually triggered** by Evelyn while Koh infiltrates. **Black slaad in tank** and four sample syringes; note evolving nomenclature with `chaos gems` and infected drinks. |
| **~02:28–02:40** | **Ambermoor knocked out nonlethally** after double natural-20 offhand psychic strike, **not killed**; bind/gag with sash, strip components and crab key. Evelyn casts **Lesser Restoration on black slaad, fails to change it**, then kills sedated specimen labelled **Neko**. |
| **~02:40–02:48** | **Two remaining large slaadi disappear from view, not confirmed eliminated**; special chaos gems **consumed/dissolved into reagents** by GM explanation; **three Delvers and prisoner stop at Krandal farm**, **Mack and Church continue to guild**, **briefcase NOT yet handed over**. Dragon-slayer teaser is production, not played. |

**Next action:** listen to targeted MP3 portions *after* confirming seek offset, and inspect GM diary/map assets if available; avoid changing source subtitle data as editorial “fix.” [Next Delvers source S2E08](../delvers/SOURCE_INVENTORY.md).
