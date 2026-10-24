# E126 — Parakeet/Qwen full-export ASR comparison (2026-10-24)

> **The Wastes · corrected S1E126 — Musical Shredding Damage.** [Episode dossier](../episodes/E126.md). Both complete UTF-8 SRT texts fetched from pinned GitHub commit `d9ff8e10a2092b81b8b985f9d7f110fcc868e2e4`, matching the initially clean connected workspace. All primary recording windows examined for a provisional scene sequence through credits; Qwen independently read for selected pivotal scenes, **not full interpretive Qwen coverage**. No original-audio playback, MP3 waveform equality test, ASR execution or source-file changes.

## Inventory and exact comparison

| Full-export source / filename-inferred pipeline | Git blob SHA (source revision fingerprint) | Cues | Last cue end | Normalized word tokens |
| --- | --- | ---: | --- | ---: |
| [Parakeet processed](../sources/The%20Wastes%20S1E126.%20Musical%20Shredding%20Damage.parakeet.processed.srt) | `b422fe6ed51d2f5c81e6edcb260fdd80631d00a4` | **2,704** | **02:44:10.080** | **24,448** |
| [Qwen Q8/Canary CTC/Nemotron-labelled](../sources/The%20Wastes%20S1E126.%20Musical%20Shredding%20Damage.qwen-q8.canary-ctc.nemotron.srt) | `10a5f8f7943b68cc8711c032e1bdc892a8d378d5` | **4,486** | **02:44:09.810** | **24,882** |

**Exact ordered unit-cost word Levenshtein: 2,375 edits / 24,448 Parakeet tokens = 9.71% inter-ASR textual disagreement** (secondary **+434 tokens**). Full SRT cue texts concatenated in chronological order; indices and time lines omitted, optional `(speaker N)` labels removed, lowercase conversion, straight/curly apostrophes deleted to join contractions, non-Unicode-letter/digit characters converted to spaces, and split into words. An exact furthest-reaching diagonal dynamic-programming computation used substitution/insertion/deletion cost 1, match cost 0. These figures **are not word error rate, accuracy, verified omissions or hallucinations**. Git SHA is Git object fingerprint, **not a claimed file SHA-256**. File sizes above were not independently byte-hashed via local read. Filename-inferred model labels do not establish historical model versions, diarizer settings or shared acoustic input. The repository's `tools/prepare_episode.py` was **not run**.

## Important disagreements and listening targets

| Recording clock | Transcript readings and high-stakes evidence | Conservative conclusion |
| --- | --- | --- |
| ~00:03–00:14 | Both exports present the protected post-impact room and wounded harbor tieflings brought into the villa, but speaker spelling varies | Household **survived first impact**; unspecified elves reportedly transported refugees; exact delivery magic unobserved |
| ~00:28–00:39 | Mask named approximately **Elton IV** in Parakeet, **Eltanfawr** in Qwen; future Prime name variants. Both describe the villa as a spelljammer, dime-size shrinking and **four-night attunement** | Stanley **dons mask**, learns potential capabilities, attempts lift but has **not attuned or flown** |
| ~00:51–01:06 | Reusable beauty-bomb and costume gag precedes apparent shifting of rubble; causal relation not proven | The bomb **operates**, sunlight/route appears and Vorel **scouts outside**, but do not claim dance caused escape |
| ~01:14–01:22 | Both SRTs distinctly report **one tiefling dies immediately**, then **several more** in second tumbling; adult bodies shield children | Deaths occurred; no total count or household death; avoid treating GM-hit-count as mortality count |
| ~01:25–01:30 | Qwen renders **Henitar Grape**, Parakeet more often **Henatar**; both depict the guitar defeating Diontalus, hostile castle crashing into Elhandar | Diontalus is **motionless**, not confirmed dead; station damage severe, ultimate total loss unknown |
| ~01:45–02:03 | Hope casts a close-in **Teleport that fails**, apparently due anti-teleport field; later guitar-induced compulsive aggression, orb defenses and stun | Spell attempted/expended, no movement; Hope and Vorel turn on each other under effect, not by conscious allegiance |
| ~02:21–02:23 | Both exports preserve Nash's **performed Shield couplet** while a dragon; Parakeet `going to bounce`, Qwen `gonna bounce`; attribution to Nash supported | Keep [existing NSP-012](../world/characters/nash-spellcasting-phrases.md) provisional; no duplicate and no audio-confirmed exact quote |
| ~02:29–02:42 | Stanley's **Telekinesis** wrests floating guitar, uncontrolled Fireball absorbed; two **acid breaths** bypass spheres, disk fails and enemy falls | **Henatar limp in desert at cutoff**; no witnessed interrogation, binding, final killing or permanent guitar custody |

**New original-audio checks** should focus on ~00:28–00:39 names/Prime terminology, ~01:15–01:22 casualties, ~01:25–01:30 Diontalus state and antagonist spelling, ~01:45–01:48 teleport obstruction, ~02:21–02:23 Shield phrase, ~02:30–02:42 guitar transfer and final battle outcome. No dialogue was independently audio-verified. Exact next Wastes S1 source **E127** is expected but its basename has **not** been checked here.
