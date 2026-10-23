# E106 — complete Parakeet/Qwen ASR comparison (2026-10-23)

> **The Wastes · corrected S1E106 — I Took An Arrow Thru The Brain · Arc Five played session.** [Source-first dossier](../episodes/E106.md). **Text-only full-export comparison**; no audio listening, manual reference transcript, ASR rerun or verified speaker identities. The two story threads, credits and final cue were examined in bounded recording-clock sections. Different ASR output is not corroborated live audio.

## Input inventory / source identity

At the start of this research the workspace MCP reported **clean main**, HEAD **`ae01d18892e434a65e8cbc258dec31aec6f408c1`**, repository **There Will Be Dungeons Transcripts**. The original SRTs were read completely using the permitted workspace binary reader in successive 65,536-byte base64 blocks; these local bytes were not written back. The archive-owner local publication catalogue identifies **TWBD 108, 8 June 2020**, corrected S1E106; this catalogue was available in the preceding review and its date has **not** been independently cross-verified against publisher metadata. The host calls this the Sunday **7 June** show and says the prior week was missed; the recording clock cannot certify an actual capture date.

| Exact filename / inferred pipeline | Cues | First start | Last end | Normalized word tokens |
| --- | ---: | --- | --- | ---: |
| [The Wastes S1E106. I Took An Arrow Thru The Brain.parakeet.processed.srt](../sources/The%20Wastes%20S1E106.%20I%20Took%20An%20Arrow%20Thru%20The%20Brain.parakeet.processed.srt) — **primary processed Parakeet** | **2,490** | **00:00:08.720** | **02:40:30.030** | **21,909** |
| [The Wastes S1E106. I Took An Arrow Thru The Brain.qwen-q8.canary-ctc.nemotron.srt](../sources/The%20Wastes%20S1E106.%20I%20Took%20An%20Arrow%20Thru%20The%20Brain.qwen-q8.canary-ctc.nemotron.srt) — **Qwen Q8/Canary CTC/Nemotron by basename** | **3,921** | **00:00:01.280** | **02:40:29.280** | **22,064** |

**SHA-256 (reported by MCP binary reader):**
- Parakeet `a5390487bae6b978996a00b0c0973392d48f98f0452fa68bc6ab232d3024cceb`
- Qwen `65a8bf89b0c55a4159fc36ad33d02c789001208c160f24f85f257d1cb8de13dc`

No source MP3 was listened to or correlated by hash with these SRTs. The **model names, precision, alignment and diarizer** here are strictly inferred from filenames; model builds, decoder/VAD flags, diarization accuracy, run environment, processing times and actual hardware are **unknown**. There is no independent provenance demonstration that both recognizers operated on byte-for-byte identical audio.

## Calculation

Parse each complete SRT into chronological cue bodies; discard numeric indices, timing rows and optional `(speaker N)` prefixes; join words and normalize by **lowercasing, deleting both straight and curly apostrophes, replacing other non-Unicode-letter/digit characters with whitespace and splitting into word tokens**. The same full-export, arbitrary-width bit-parallel **ordered Levenshtein distance**, with equal costs for deletion, insertion and substitution, is used as for E105. Speaker labels and timestamps are **excluded from the lexical metric**, not validated by it.

**Parakeet → Qwen: 1,885 ordered word edits / 21,909 primary tokens = 8.60% text disagreement.** Qwen contains **155 more normalized words**. This is **not WER**, a claim that Parakeet omitted 155 audible words, a word-accuracy estimate, or proof that either is preferable. No staged/truncated alignment estimate was substituted for the exact whole-episode metric.

## Story-critical recognition and interpretation checks

| Clock | Sources and risk | Source-safe interpretation |
| --- | --- | --- |
| ~00:00–00:03; 02:39–02:40:30 | Qwen begins ~7.4 s earlier, while both exports contain an **orphaned “I've aged pretty well”** or similar line after credits, matching the Principle's earlier phrase. | Neither trailing cue should be accepted as a new played post-credit revelation; determine audio and cue placement. |
| ~00:10–00:19 | **Jalver/Javer** is in the audience; Stanley's **Enthralling Performance** uses five selected targets. | Identify targets and save results separately; the performed speech does not itself prove that every observer was charmed. |
| ~00:19–00:26 | Both depict **Stanley locating a medallion in an unexpected boot**, opening chest, **actual gauntlet with purple veins**, and transfer to Tobacho through golem. | Key search settled **in play** but **who placed it** is not. Fist physically delivered, **Hand absent**. |
| ~00:26–00:35 | Tobacho probes gauntlet's teeth/membrane and missing inner item; Stanley's **32/19 Deception** checks differ from ordinary truthful disclosure. | Tobacho does not receive Hope's **Hand of the Voice**; claim that team never knew its absence is a **lie**. No direct Sigil–Earth portal offered. |
| ~00:35–00:40 | Advertised bounty has **10 million**, **another 10 million**, **50 million** with conditions involving Hope, right arm, death; exact tier grammar prone to compression. | Preserve the announced numbers and qualifiers; **not** a completed bounty or a verified universal contract. Item-debt waiver may not settle Nash's unrelated harbor claim. |
| ~00:44–00:49 | **Mangler** offers to pursue Hope; gas-mask guide **Badass T** repeatedly stabs him before response. | Observed violent death by guide; not a party-agreed kill or actual capture of Hope. |
| ~00:57–01:04 | **52 Pinocchio Street (?)**, frog vendor recognizes party inconsistently, and owner is **alive** when he consents to basement portal use. | E105 vendor absence was a holiday. Check street spelling, consent and exact address. |
| ~01:05–01:15 | Long phonetic **Dwarvish poem**, standing on head, bulb-shaped **dizzle/dwizzle dink** eaten in proper sequence; portal opens. | Ritual is **performed**, not merely instructed. Stanley retains Badass T's notebook. No normalized canonical poem until handout/audio checking. |
| ~01:14–01:20 | Guide exits with bloody knife, refuses direct answer about frog vendor; crew later **fires at the original portal**. | Seller's murder **strongly implied, but body and direct killing not depicted**. No reusable direct Earth gate, no Earth arrival. |
| ~01:21–01:39 | Hope's entry with **Spatulo, Steerious and two refugees**; Brett calls metal-bodied **Principle “Vladimir”**; attack on Principal City described verbally. | The casino is her **E104 Gate destination**; city attack is **reported**, not seen in this section. Refugees alive on arrival. |
| ~01:36–01:56 | Brett/Principle-generated **illusory Earth history**: pre-Scorching tiefling exploitation, dragon strikes, lizardfolk defenders, young Vladimir, **CHIDS**, and **Lich Project** pods. | Attribute history claims to **the Principle and Brett**, even when vividly visualized; distinguish reenactment from independently witnessed time travel. Soul consumption **100 humans/day** and claimed ancient age are **testimony**. |
| ~01:55–01:59 | Term **Eye of the Voice** is explicitly a second desired relic; spelling of suggested future Earth rendezvous **Carvutican/Car Vatican** fluctuates. | Do not merge with **Eye of Groxl**, which Vorel already possesses. Hope's next intended destination is **Tobacho**, not an already performed audience. |
| ~01:59–02:10 | **Spatulo** (ASR variants Spitulo/Spitulo) threatens Hope's claim, Steerious strikes twice (11, 10), he surrenders. | No death from those sword strokes; **execution occurs later in the lab**. |
| ~02:09–02:22 | Dr. Spider's **Mental Prison** hits for **41 psychic damage** despite successful Intelligence save; Spatulo **dies**, then brain jar/speaker with *Speak with Dead* and **Blood Skunk's 18-to-hit arrow**. | Spell is cause of death; **arrow is into preserved already-dead brain**; after arrow the speaker still answers. “Tobacho weakness” was a false plea; envy of Lady of Pain is corpse testimony, not omniscient fact. |
| ~02:23–02:32 | Steerious **admits losing track of two rescued tieflings**; Hope's evil recharge heats/scorches ring, opens Gate; **four** characters walk into Sigil street. | Refugees **do not enter**; no reunion with other party or Tobacho meeting. |
| ~02:32–02:40 | Improbability vessel reaches **paired asteroids**, Stanley statue, outside hamburger factory, oversized tower interior and **Nash wall-face speaking “Junior.”** | New location **not Earth**; giant face speaks but **is not identified as Nash's father**. This is the real played cliffhanger; final stray cue is not a resolution. |

## Review and provenance limits

High-priority listening includes **gauntlet/key actual custody**, exact bounty language, item-debt waiver, frog vendor's inferred death, full phonetic ritual sequence, **status of two rescued refugees**, illusion versus physically played action, Dr. Spider's lethal *Mental Prison*, postmortem arrow and Qwen/Parakeet closing displaced dialogue. Keep original SRTs immutable and record any future listening verification by precise cue/time. **No MP3 was opened, no speaker diarization was verified, no source was edited, and no ASR was rerun.** The [episode dossier](../episodes/E106.md) and [review queue](../project/REVIEW_QUEUE.md) carry the continuity cutoff and pending tasks.

**Next intended release/archive entry:** [Bonus 2020-06 — June cast Q&A](../episodes/BONUS-2020-06.md) (**previously analyzed**, out-of-game commentary; [ASR comparison](BONUS_2020_06_ASR_COMPARISON_2026-10-23.md)). **Next unresearched corrected-numbered recording:** [The Wastes S1E107 — The Handshaking Algorithm (Parakeet)](../sources/The%20Wastes%20S1E107.%20The%20Handshaking%20Algorithm.parakeet.processed.srt) and [Qwen](../sources/The%20Wastes%20S1E107.%20The%20Handshaking%20Algorithm.qwen-q8.canary-ctc.nemotron.srt), present but **unread**. The publication catalogue describes a Jon-run side story; classify it separately from the original party when analyzed.
