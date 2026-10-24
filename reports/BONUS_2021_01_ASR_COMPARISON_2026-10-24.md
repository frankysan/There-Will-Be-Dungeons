# BONUS-2021-01 — January 2021 ASR comparison (2026-10-24)

**Scope:** two complete subtitle exports of the cast's **January 2021 bonus**, a Q&A rather than new campaign play. Sources read at pinned private GitHub HEAD `226fb0e4760ea42df0b4134375bd5ad8163cf6c9`; the same HEAD was observed in the connected workspace before editing. The owner-normalized January basename represents the **public-publication month**; the actual recording and original public-release day were not independently verified.

| Filename-inferred pipeline | Exact source | Git blob SHA | Cues | Last end | Word tokens |
| --- | --- | --- | ---: | --- | ---: |
| Processed Parakeet (reference) | [`Bonus 2021-01 - January 2021.parakeet.processed.srt`](../sources/Bonus%202021-01%20-%20January%202021.parakeet.processed.srt) | `29b5a4d9f2ac8368666947d61605cfcf3aaaca2d` | 563 | 00:29:28.040 | **5,346** |
| Qwen Q8/Canary CTC/Nemotron-labelled | [`Bonus 2021-01 - January 2021.qwen-q8.canary-ctc.nemotron.srt`](../sources/Bonus%202021-01%20-%20January%202021.qwen-q8.canary-ctc.nemotron.srt) | `b9a26c0a966b30258f7d8a3a690ac50e71df86cc` | 835 | 00:29:36.400 | **5,430** |

## Full-export word comparison

**330 unit-cost ordered word-token edits / 5,346 primary tokens = 6.17% text disagreement**; Qwen has **84 more normalized tokens** than Parakeet. The exact metric processes **all cues in both exports**: split SRT cue blocks; discard numbers/timing; remove optional `(speaker N)` tags; join cue text; lowercase; remove straight/curly apostrophes; replace non-Unicode-letter-and-digit runs with whitespace; then split into ordered words. Levenshtein insertions, deletions and substitutions each cost one. A **700-token diagonal band** was used for the exact dynamic program; because the optimum found (330) is **below 700**, it cannot exit the band and is exactly the unconstrained ordered distance. No audio-verified alignment is claimed.

The complete Parakeet stream was editorially read in successive recording-clock portions, the Qwen export was read through its closing extra reaction, and selected evidence-bearing parallel passages were compared. The measure is **not WER, transcription accuracy, a proven omission/hallucination count or source fidelity**. Neither the labelled pipeline settings nor identical input-audio bytes were independently verified. `tools/prepare_episode.py` was **not executed**.

## Focused parallel-text issues

| SRT-clock window | Observation and verification boundary |
| --- | --- |
| ~00:00:06–00:00:47 | Both exports identify one bonus being recorded/presented and **another promised next week**, to cover a **missed December** instalment. No recording or publication day can be inferred from `today` or `next week` without independent evidence |
| ~00:03:07–00:05:38 | Both contain Kyle's reference to a **poltergeist**, while earlier played S1E02 uses the name **Studwell** for the invisible/strength-draining foe. This is an out-of-game creature-category clarification, not a new monster encounter. Kyle's skeletal minotaur is hypothetical |
| ~00:05:38–00:09:49 | Both support **not intentionally based on Colossus** and Scott's **newly improvised** maternal source of Krandal's accent, absent warrior father, potato upbringing and possible half-orc cultural variation. Do not claim those details were previously played or officially fixed in setting |
| ~00:09:49–00:12:32 | Both have **Baffo** vital to Jon's *planned*, unperformed Inverse finale, **Garpoon** as a desired return, and uncertain **Hackloman** in a separate Wastes-world one-shot reference. References to an arena or reusable characters are counterfactual, not proof Inverse and Wastes share reality |
| ~00:12:32–00:14:22 | Both contain the **equal-level last-person-standing** thought experiment: Vorel, Nash, Stanley and Squirts mentioned as hypothetical victors. Several jokes/different nickname renderings are present; no canonical duel/power result |
| ~00:14:22–00:15:15 | Kristen directly supports Hope's **continuing desire to undo the Scorching**, *conditional on access to time travel*. This is a cast characterization statement, not in-world action |
| ~00:15:15–00:18:10 | Both support Kyle's **grick identification** of Koh's S1E01 fissure sighting and the **unused** possibility that it could capture/drag him. Keep the earlier actual safe escape separate |
| ~00:18:10–00:22:49 | Both support **XP not milestones**, a planned twelve-episode Delvers shape, and the group's agreed **level-one start**. No already-completed season ending or foreordained fixed character progression follows |
| ~00:22:49–00:26:29 | Both present currently **Kyle-run initiative for production speed**, a suggested **popcorn method** and proposed automation. **Neither alternative is adopted** |
| ~00:26:29–end | Current **Discord sheet-link suggestions** versus an **unbuilt third-party campaign viewer**; Qwen's last cue **00:29:32.800–00:29:36.400** contains repeated `Oh` after Parakeet ends **00:29:28.040**. Listen before labeling audio presence, intentional speech, missed content or export artifact |

## Input integrity and follow-up

Original sources were read, not edited. Initial workspace status had **two unrelated changes** (`world/characters/stanley-billings.md` modified and a Stanley legacy draft untracked), which this work deliberately preserves. No audio listening, waveform comparison, timing-offset calibration, diarization verification or ASR rerun. The highest-value narrow checks are the ~00:07:49–00:09:49 live character conception, ~00:11:34 `Hackloman` entity, ~00:14:22 Hope's conditional intent and ~00:29:24 onward Qwen extra tail; see [episode dossier](../episodes/BONUS-2021-01.md) and [review queue](../project/REVIEW_QUEUE.md).

The content is predominantly **Delvers-related behind-the-scenes discussion**, with separate remarks on **Inverse and Wastes**. None should be integrated into the chronology as a played session. **Next verified bonus pair:** [February 2021 Parakeet](../sources/Bonus%202021-02%20-%20February%202021.parakeet.processed.srt) and [Qwen](../sources/Bonus%202021-02%20-%20February%202021.qwen-q8.canary-ctc.nemotron.srt).
