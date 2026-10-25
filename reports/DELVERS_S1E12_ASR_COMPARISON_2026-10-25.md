# Delvers S1E12 — End Friends: complete-export ASR comparison (2026-10-25)

**Identity:** Delvers S1E12 — *End Friends*, explicitly **Season One finale** in both opening and sign-off. Owner separately marks **end of first story arc**. Audio not listened, MP3–SRT seek alignment, original map/handouts, recording date and run configurations unverified. **Git provenance caveat:** Connected workspace `main` clean HEAD **89df0a269f956b7572ca905c7202d03bba466b46**, but GitHub API returned **404 for that commit ref**; full source exports read via GitHub `main` by exact pathname with individual verified Git blob IDs. **Workspace/GitHub byte-level identity not verified**, do not claim same commit.

| Export (filename-derived labels only) | Source | Git blob SHA | Cue count | Last cue end | Normalized tokens |
| --- | --- | --- | ---: | --- | ---: |
| Parakeet processed, reference | [SRT](../sources/Delvers%20S1E12.%20End%20Friends.parakeet.processed.srt) | `f56f8043dcc87edf0d1378ecbd8ea9a51f82d892` | **2,777** | **03:06:05.310** | **24,536** |
| Qwen Q8/Canary CTC/Nemotron-labelled | [SRT](../sources/Delvers%20S1E12.%20End%20Friends.qwen-q8.canary-ctc.nemotron.srt) | `f93f47b1269c66bc6e120fb67188a58ef0aa2f19` | **4,485** | **03:06:04.960** | **24,634** |

## Exact complete ordered-word edit distance

**2,017 / 24,536 = 8.22% inter-ASR textual disagreement**, **not WER**, independent accuracy, transcript completeness, omission, hallucination or audio-verified error count. The secondary has **98 more** normalized tokens, and final cue ends **0.350 seconds earlier** than primary.

Normalization: parse complete SRT cue bodies and concatenate chronological text; strip indices, timecodes and optional `(speaker N)` decorations; Unicode lowercasing, remove straight and curly apostrophes without space, substitute non-Unicode-letter/digit runs with whitespace, then split tokens. Standard unit-cost Levenshtein insertion, deletion, substitution calculated by two-row **3,000-token diagonal-banded dynamic programming**. Returned optimum 2,017 is **strictly less than 3,000**, so any alignment venturing outside band would require at least 3,000 insertions/deletions; hence computed result is **exact global ordered word distance**. This is not time-aware speaker/cue WER.

Primary content read chronologically in recording-clock blocks from opening to full sign-off. Entire Qwen export parsed for the numeric comparison; **selected Qwen portions close-read** for season identification, character and captive transitions, guild interrogation, ritual defeat, saving the enemies, aftermath and Snake Island hook. No full independent Qwen narrative pass or original audio verification; no local `prepare_episode.py`, generic lint or pipeline tests run. Original sources unedited.

## High-risk semantics/disagreements for later listening

| Time | Issue and conservative conclusion |
| --- | --- |
| ~00:00–00:18 | Both state **Season One finale** and playing a **short rest / re-equipping armor** at fish village before setting out. Evelyn's **Greatsword of Wounding** identified; previous S1E11 “sword” now more specifically named. Important not to claim party still without armor while at guild. |
| ~00:19–00:47 | **Boonefellow** is rescued alive by straw-hatted bullywug and returned to guild with **all three prisoners** by carriage. **Norman Green not proven dead**, **Faelan abducted**. Village fish footprints suggest messenger presence but don't independently confirm delivered warning. |
| ~00:54–01:13 | Caster name **Cheet/Cheat**, also **Mary/Merry**: Q renders “Cheet” and deity “Wejoss” (presumably **Wee Jas**), P “Cheat/Ouija”. Guild researcher surname P **“Marrick Gideoms”** versus Q **“Merrick Gideon's”**—do not impose confident permanent orthography without audio/source notes. **Zone of Truth** does not force response, and asserted “dream/compulsion” still interpreted alongside guild finding. |
| ~01:08–01:20 | Ritual requires **high elf sacrifice, faith of devoted priests, summoning disk**, midnight at **Noble Hollow**. Cheet's prediction city will be assaulted by “beast of the lake” is **her statement**, not completed outcome. Her own motivation “just see what happens” partly self-serving. |
| ~01:28–02:02 | Underworld invocation sound **“Orgothel Argir Urun Ractus...”** significantly garbled across outputs; do not canonize a proper divine/summoned name. **Evelyn nonlethally knocks out Marek**, stone gear-disk **shatters**, intended rite ends. Identical workmanship of older quarter-disc now actually **GM-recognized**, but no literal assembly. |
| ~02:04–02:51 | Giant **roper** emerges as existing mother of piercers beneath collapsing Noble Hollow; **not proven to be summoned lake beast**. Krandal forces drop twice, heals **Solburn**; Koh's eye arrow wounds, Evelyn's javelin at brood-hole kills roper. **One unnamed cultist is swallowed**. Evelyn heals **Faelan and Norman**, they both live. |
| ~02:51–03:06 | Four-day debrief at Zone of Truth **clears Delvers and Broadside/Solburn**, but **Marek trial and Cheet rehabilitation are prospective**, no sentences administered. **Extra guild cash unavailable** owing to northern vampire war; **old tower deed promised, not delivered**. Final Snake Island visitor offers **new quest with buckets of coins/snakes**, no acceptance played. Host confirms break/new season plans, not in-world scene. |

[Source-first S1E12 dossier](../delvers/episodes/S1E12.md) · [Delvers listening queue](../delvers/REVIEW_QUEUE.md).