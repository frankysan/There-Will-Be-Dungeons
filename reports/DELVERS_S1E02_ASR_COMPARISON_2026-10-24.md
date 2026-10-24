# Delvers S1E02 — ASR comparison (2026-10-24)

**Scope:** complete **Delvers S1E02 — Agreeable Meatball** Parakeet processed and independent Qwen/Canary CTC/Nemotron-labelled SRT exports, both retrieved from private GitHub commit `e908edb7b1b05207e6de2c281af72fb0f0415f8e`. Labels derive from filenames, not independently established inference configuration. Primary text read chronologically through closing network outro; the complete Qwen text was processed for the metric and manually inspected at opening and selected high-risk scenes, **not independently interpreted in every interval**. No audio played; identical audio input/clock alignment not established.

| Export | SRT source | Blob SHA | Cues | Final cue end | Normalized tokens |
| --- | --- | --- | ---: | --- | ---: |
| P (reference) | [`Delvers S1E02. Agreeable Meatball.parakeet.processed.srt`](../sources/Delvers%20S1E02.%20Agreeable%20Meatball.parakeet.processed.srt) | `d44dff08c13fe79b7d2c492dff4a47b43ece9825` | 2,520 | 02:52:12.010 | 22,273 |
| Q | [`Delvers S1E02. Agreeable Meatball.qwen-q8.canary-ctc.nemotron.srt`](../sources/Delvers%20S1E02.%20Agreeable%20Meatball.qwen-q8.canary-ctc.nemotron.srt) | `31516a81dbb8caf1f9b5bb35911df95173adc151` | 4,229 | 02:52:12.000 | 22,324 |

## Exact text-only distance

**1,803 ordered word-token edits / 22,273 P-reference tokens = 8.10% inter-ASR disagreement.** Both entire exports were parsed by SRT cue block, excluding cue numbers/timelines, stripping `(speaker N)` labels, joining spoken text, lowercasing, deleting straight/curly apostrophes, replacing non-Unicode-letter/digit runs with spaces, and tokenizing. An exact unit-cost Levenshtein recurrence was evaluated with a **4,465-token diagonal band** (20% of the longer sequence), stripping **27 common-prefix** and **3 common-suffix** tokens first. The resulting distance is below the band limit, so no optimal path can lie outside the permitted band; the distance is exact. This was computed in the connected JavaScript runtime, **not claimed as a run of `tools/prepare_episode.py`**. Edit count is not WER, recognition accuracy, or verified deletions/hallucinations.

## High-risk cross-export windows (SRT clocks)

| Window | Text evidence and next check |
| --- | --- |
| ~00:01:30–00:02:00 | **P `ko` vs Q `Kyle`** in the dramatic recap interview. The next speaker recounts their experiences as Koh; Q's name is likely misattributed. Audio needed for exact word and staging |
| ~00:07:09–00:11:46 | Both exports agree on the prospective 500-gold **moon cultist** posting, three issued waters and **25-gold silver purchase**; no accepted cultist job or performed ritual |
| ~00:19:08–00:25:42 | Both support House/Crush/Armada and **Studwell**, who allegedly broke his back squatting. `Cord/Corn/Kord`, `House/How`, `Crush/Krash` are orthographic hypotheses. Evelyn persuades Crush to provide a **second potion**, despite an unsuccessful attempted slap |
| ~00:45:20–00:52:40 | Both identify the first attacker as a **Shadow**, vulnerable to radiance and weak in sun. Krandal actually destroys it with Sacred Flame; this is not the same as Studwell |
| ~01:01:40–01:15:25 | Both support **ten laps**, a strength-draining hit on Koh, Shadows defeated with cooperation, and the **first** basin cleansed with Koh's issued holy water; initial Sacred Flame roll/check is corrected from attack to Dexterity save |
| ~01:32:50–01:38:00 | Both explicitly have **Koh stab Krandal**, eight damage, rather than attacking the Shadow; Krandal goes down and Evelyn heals him. Do not silently turn friendly fire into a successful monster attack |
| ~01:45:59–01:54:28 | Evelyn goes down, fails a death saving throw, and is revived. Koh deploys drift-globe daylight; it weakens Shadows but is **not itself narrated as immediate damage**. Evelyn smites the final Shadow |
| ~02:17:00–02:20:15 | Kettlebell initially appears to drop Krandal; **Relentless Endurance** is then applied to remain at one HP. Preserve that correction rather than an uncorrected unconsciousness |
| ~02:30:00–02:44:30 | Both support Koh's killing hit on Studwell, Sultan's rescue by the second strength potion, Koh ringing the bell and Evelyn pouring the final holy water. At ~02:37:01 P `ko spyros` vs Q `Kospiodos`; the approved **Koh Spiros** is written-source backed, not sound-verified |
| ~02:44:20–02:50:40 | GM identifies **Sultan's Sash of Strongman** with the Rope of Climbing behavior; Koh physically retrieves it but discusses shared equipment. Guild pay is **300 gold total** and is divisible by three; no selection of the next mission. Paid award is distinct from off-air XP promised |

## Limits and review handoff

No listening, waveform comparison, diarization verification, or MP3 alignment was performed. The matching local MP3 was previously inventoried, but source equivalence and exact seek offsets were not reverified. Full-export measurements do not license full Qwen semantic coverage: **targeted cross-reading only**. Disputed names and contract terms remain provisional pending audio/written source corroboration. Preserve original ASR files unchanged; use the [episode dossier](../delvers/episodes/S1E02.md) and [Delvers review queue](../delvers/REVIEW_QUEUE.md) for keyed follow-ups. Do not infer any shared continuity with Wastes or Inverse.
