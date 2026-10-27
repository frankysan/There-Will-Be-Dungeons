# Delvers S1E11 — No More Fish: ASR comparison (2026-10-25)

**Source-identity follow-up, 2026-10-27:** The [S1E12–S1E08 batch check](DELVERS_S1E12_S1E08_SOURCE_IDENTITY_2026-10-27.md#s1e11) verifies both complete local exports against their recorded Git blobs after CRLF-to-LF conversion only, and verifies both source paths in the recorded source commit. Raw bytes differ in line endings. This independently confirms local content correspondence with the originally pinned source revision. Earlier provenance statements remain dated history. Prior interpretive coverage, inter-ASR measurements, played cutoff and audio status are unchanged.

**Type:** Played Delvers S1E11. Source identity from [owner-normalized inventory](../delvers/SOURCE_INVENTORY.md), with first in-world scene continuing **living fish ritualist bound below the lake** in S1E10 and final in-world scene **three prisoners leaving kuo-toa village on horses**, prior to reaching guild. Initial connected workspace `main` HEAD and pinned private GitHub sources at **`d2763e5d2f3998286aecc27c42e42db9b835bb8c`**; checkout initially had **7 unrelated Fate-4 illustration/backlog/E057 edits**, untouched. **No original audio listened**, seek offsets, source-audio identity or model settings checked.

| Export (filename-derived pipeline) | Source | Blob SHA | Cues | Last end | Normalized tokens |
| --- | --- | --- | ---: | --- | ---: |
| Primary Parakeet processed | [SRT](../sources/Delvers%20S1E11.%20No%20More%20Fish.parakeet.processed.srt) | `5bdbbd397aeca078a0bc51251f80b3ca8100ede5` | **2,487** | **02:48:24.480** | **22,331** |
| Secondary Qwen Q8/Canary CTC/Nemotron-labelled | [SRT](../sources/Delvers%20S1E11.%20No%20More%20Fish.qwen-q8.canary-ctc.nemotron.srt) | `98fe8e3dd3ee5224298e2091ea5be3231b3a72af` | **4,023** | **02:48:23.800** | **22,480** |

## Complete-export textual metric

**1,874 ordered word edits / 22,331 Parakeet words = 8.39%** *inter-ASR textual disagreement*, not **WER**, accuracy or an audio-verified hallucination/omission. Qwen has **149 additional normalized word tokens**, final cue **0.680 seconds earlier**. Independent input audio files and SRT timing offset **not verified**.

Method: Parse all cue bodies, discard indices/timing, remove `(speaker N)` decorators, join in order. Unicode lowercase; drop straight/curly apostrophes without replacement; collapse all non-letter/digit runs to spaces, tokenize. Two-row, unit-cost (insert/delete/substitute) full ordered word **Levenshtein** with **3,500-token diagonal band**; returned **1,874**, strictly below bandwidth. Thus any path outside the band would cost at least 3,500 edits and cannot improve on this global optimum. Not a time/cue-paired WER.

**Scope:** Primary Parakeet content examined chronologically through opening recap, deep-cave search, fog/Water Breathing, village, darkmantle-hatted collector, combat, prisoner stabilization and closing sign-off. Full Qwen export processed for measurement; Qwen excerpt close-reading **selected** around geometry, Wand of Secrets, monster descriptions, staff exchange, party's confrontation, damage and outro, **not a complete semantic Qwen re-reading**. MP3 audio, map images, guild handouts, sheet versions and underlying pipeline parameters **not inspected**. Source SRTs unchanged.

## High-impact cross-source interpretation issues

| Parakeet SRT clock | Supported / unverified |
| --- | --- |
| ~00:03–00:14 | Both render **Dawnless Dunes carving**, small black-sludge-dripping opening and **Wand of Secrets** identified by Koh from captive's old stone-metal wand. Wand points to a quarter stone-metal **gear-edged disc** with missing gear; Evelyn extracts. **Who held slime sample** unclear by speaker attribution. Do not assert 4 pieces/door purpose as proven. |
| ~00:22–00:50 | Floating **beaked brain with barbed tendrils** feeding on stirges **unnamed in played speech**; **Koh's final psychic strike kills it**. This matches common monster art intuitions but neither model independently identifies official species. Evelyn physically pries beak apart and party extracts halves; no submission to guild yet. |
| ~00:54–01:08 | **Hook-horror-headed fountain**, **Krandal's old smoke/fog bottle** causes heavy obscurity when unstoppered, then is sealed and carried. Farther **tooth-faced portal** glimpsed only, not opened. Party returns underwater and **surfaces near expiry**; no drowning. |
| ~01:16–01:27 | **Conch-shell staff is actually given to trader**, then passed to threatening **darkmantle-cowl mounted leader who departs for bullywug camp**. The staff is **not** collected by the Delvers as quest payment. Village does not independently endorse leader's intimidation. |
| ~01:33–01:43 | Caster's address **“Cole/Coal”** (possibly warrior), fighter's **“Marek/Marik?”** (possibly caster), and guild-recognized **“Broadside”** are **not safely disambiguated as 3 names for 3 distinct individuals**. Koh's opening psychic sneak strike is **natural-20, explicitly nonlethal, 33 psychic**, caster collapses and stays alive. Potion pocketed during theft is retrieved. |
| ~01:48–02:28 | Aid +5 max/current HP to each; Krandal Spiritual Weapon appears **spectral face-mace**, later strikes and **drops plate-armored fighter**, **not an adjudicated kill**. Broadside's appearance emerges when magical facial alteration fades after stripping gear. Krandal stabilizes and then heals fighter before Koh **knocks him unconscious nonlethally again**. Shield's **teeth motif matches distant subterranean stone door**, relevance unknown. |
| ~02:33–02:46 | **Glepo Ma sends warning** himself to bullywug camp and actually enters water; report not received by friends yet. He compensates Delvers with **gear crank + pouch estimated 1,000 gp**, chosen by Koh; wooden shield and old shovel remain. Party leaves **fighter's heavy plate** but carries **toothed shield, sword, ordinary caster's mace**; ties/gags **three living captives**. Evelyn drinks standard healing potion before riding. |
| ~02:46–02:48 | **In-world cutoff:** party **starts on horseback** toward guild, **does not arrive** or learn future outcome. Out-of-game show host remarks explicitly defer decisions to next episode. Title S1E12 *End Friends* is no evidence of friends dying/ending here. |

## Listening priorities

Align original MP3/SRT first, then inspect ~00:04 collector of black ooze; ~00:07 wand identification; ~00:09 disc and gear; ~00:27–00:49 creature ID; ~00:56 fog bottle and ~01:05 temple-like gate; ~01:20–01:27 mounted collector and staff custody; ~01:33–01:51 two attackers' names and guild gear; ~02:26–02:32 **Broadside** reveal and medical stabilization; ~02:33–02:46 gold/crank/warning/captive horses; final ending. No audio-backed accuracy claims.

[Episode dossier](../delvers/episodes/S1E11.md) · [Delvers queue](../delvers/REVIEW_QUEUE.md).
