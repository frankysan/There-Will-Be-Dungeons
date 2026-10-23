# Initial model tests (supplied by archive owner)

## 2026-10-23: comparison backfill for analyzed Wastes S1E002–E005

The [coverage register](../reports/ASR_COMPARISON_COVERAGE_2026-10-23.md) inventories
119 analyzed dossiers: 26 have dedicated reports after this pass, five have
earlier pilot/intake comparisons, 80 are ready with existing export pairs, and
eight (E076–E083) lack an independent Qwen export in `sources/`.

This bounded pass compares complete processed Parakeet and Qwen Q8 / Canary CTC /
Nemotron-labelled exports for four played sessions. The labels come from filenames;
exact builds, settings, inference runtime, hardware and original audio hashes are
unconfirmed. No recognizer was run and no audio was listened to.

| Recording | Exact word edits | Parakeet denominator | Disagreement | Report |
| --- | ---: | ---: | ---: | --- |
| Wastes S1E002 | 2,897 | 27,096 | 10.69% | [Spiders](../reports/E002_ASR_COMPARISON_2026-10-23.md) |
| Wastes S1E003 | 3,266 | 32,144 | 10.16% | [Soft Head Returns](../reports/E003_ASR_COMPARISON_2026-10-23.md) |
| Wastes S1E004 | 2,604 | 26,934 | 9.67% | [The Oil Demon](../reports/E004_ASR_COMPARISON_2026-10-23.md) |
| Wastes S1E005 | 2,855 | 27,354 | 10.44% | [Goblincide](../reports/E005_ASR_COMPARISON_2026-10-23.md) |

These are exact ordered word-level Levenshtein distances relative to processed
Parakeet, not audio-grounded WER or model rankings. Normalization removes speaker
decorations, lowercases, deletes straight/curly apostrophes, replaces everything
except Unicode letters/digits with whitespace, then splits. Every cue through
each outro is included. Separate time-aware candidate counts are 2,244 / 2,627 /
2,063 / 2,119 with zero fallback blocks; they use a different lexical normalization
and are not the global metric. The E005 sign-off is present in both exports but
shifted in time, demonstrating why unilateral alignment is not proven omission.

The [reproduction script](../experiments/asr_backfill_2026_10_23.py) writes
[complete candidate evidence and SHA-256](../reports/ASR_BACKFILL_2026-10-23.json).
Its exact bit-vector metric is checked against independent dynamic programming
on exhaustive small and seeded longer/repeated sequences. All eight input hashes
were unchanged after computation. Reports contain selected contextual text checks;
they do not claim full manual cue review or verified wording. Next backfill: E006.

## 2026-10-22: first Qwen Q8 + Canary CTC + Nemotron batch intake

[Reproducible intake report](../reports/QWEN_CANARY_INTAKE_2026-10-22.md) and
[complete candidate evidence](../reports/QWEN_CANARY_INTAKE_2026-10-22.json) compare
the March and April 2019 bonus exports plus the additional E039 export with their
existing processed Parakeet counterparts. All three Qwen SRTs parse and have
zero nonpositive cue durations; adjacent overlaps are 3 / 3 / 0 respectively.
Time-aware alignment produces 2,245 / 357 / 1,623 candidate groups without bounded
fallback. Counts describe disagreement, not audio-verified errors or omissions.

The owner identifies the new configuration as Qwen Q8 + Canary CTC + Nemotron;
exact builds, VAD/chunking, decoding, post-processing and runtime remain
unconfirmed. These recordings have no same-audio Q8-without-Canary control, so
this intake does not establish alignment-only text preservation. April's
different basenames were paired using the matching opening introduction; audio
hash identity has not been verified. Source hashes were unchanged after analysis.
No recognizer was executed, no listening was performed and no transcript wording
was accepted. The report supplies timed review examples in both directions.

These results describe **the user's actual local Subtitle Edit tests**, not generic benchmark claims. The real-time factors were approximate relative comparisons rather than standardized throughput measurements.

| Engine | Configuration as reported | Observations |
|---|---|---|
| Cohere Transcribe | `cohere-transcribe` + `Nemotron-3-Diarization.q8_0` + built-in aligner | Substantial speech omissions, **listener-confirmed** |
| Parakeet TDT 1.1B | `parakeet-tdt-1.1b` + `Nemotron-3-Diarization.q8_0` + built-in aligner | Strong current coverage/speed candidate; raw no-postprocessing SRTs additionally provided |
| Qwen3-ASR 1.7B F16 | `qwen3-asr-1.7b-f16` + `Nemotron-3-Diarization.q8_0` + `qwen3-forced-aligner-0.6b-q8_0` | Reported 7–8× slower than the fast alternatives; tested on E000 |
| Qwen3-ASR 1.7B Q8 | `qwen3-asr-1.7b-q8_0` + `Nemotron-3-Diarization.q8_0` + `qwen3-forced-aligner-0.6b-q8_0` | Reported 2–3× slower; valuable independent comparison |
| ARK | Configuration not recorded | Speaker identification failed; this does not, on its own, establish recognition accuracy |

## Comparison limitations

The Cohere and Qwen files supplied for this pilot are post-processed. Some speaker names were replaced globally by find-and-replace, preserving each engine's assignments but changing their labels. The additional Parakeet no-postprocessing files came from a **new run**, so differences cannot be ascribed exclusively to the post-processing module.

The originals are retained in `sources/`; **do not rank word accuracy solely by similarity to another model**. Only a verified reference or actual listening can establish correctness.

## 2026-10-21: additional Qwen raw-output variants

Six Qwen SRTs (Q4, Q4 + Canary CTC, and Q8, for E000 and E001) were added unmodified to `sources/`. [Detailed comparison](../reports/QWEN_VARIANTS_2026-10-21.md) and [machine-readable metrics](../reports/QWEN_VARIANTS.json) record the results. The `q4.raw.srt` filename does **not** prove no aligner was used; it only distinguishes the no-Canary export from the Canary variant.

**Findings:** Q4 + Canary preserves all Q4 text exactly while eliminating all E001 nonpositive cue durations (56 → 0). It also changes E001 speaker attribution for 924/32,007 tokens because cue boundaries and labels change. Q4 and Q8 recognition differ by 1,070 word edits in E001 and 17 in E000. These are disagreements, not an accuracy ranking.

Next experimental priority: audio-verified Q4/Q8/Parakeet discrepancies, plus a Q8 + Canary alignment run if Q8 is favored.

## 2026-10-21: E001 Parakeet segmentation experiments

[Full five-run benchmark with transcript comparisons and audio-review targets](../reports/PARAKEET_SEGMENTATION_2026-10-21.md). CrispASR 0.8.43, Parakeet TDT 1.1B GGUF, English, Radeon RX 9070 via Vulkan, 600 seconds of the same E001 audio. The following are **machine-output comparisons, not audio-verified WER**.

| Run | Time / speed | Words | Finding |
|---|---:|---:|---|
| Full audio, no VAD | 15.75 s / 38.1× | 1,701 | Preserves the opening greeting; provisional baseline |
| Default Silero VAD | 13.33 s / 45.0× | 1,699 | Misses candidate `hello everybody`, captures other possible brief remarks |
| VAD with 700 ms padding | 12.96 s / 46.3× | 1,699 | Recovers greeting; nearly merges VAD regions; near-same-time duplicate `if` |
| 30 s chunks + 3 s overlap, LCS auto | 15.77 s / 38.0× | 1,692 | Some better phrases, but possible lost greetings around 01:40 |
| Same chunks, LCS off | 14.96 s / 40.1× | 1,692 | **JSON and SRT are byte-identical** to LCS auto |

Stop optimizing segmentation based solely on model-to-model agreement. Listen to the timestamped review samples before revising the model choice. No existing source SRTs or transcript drafts were changed in this test.

## 2026-10-21: reproducible multi-pass export comparison

[Implementation](../reports/MULTIPASS_PIPELINE.md) and
[measured pilot with machine-readable evidence](../reports/MULTIPASS_PILOT_2026-10-21.md).
The new standard-library tooling compares full E000/E001 Parakeet/Qwen Q8 SRTs
and the five 600-second Parakeet JSON runs against each other and the opening of
the full Qwen export. Explicit common coverage prevents the rest of a full
episode being labelled missing from a short run. Original wording, source hashes,
cue/word timing precision, probabilities and configuration uncertainty survive.

The local export pilot produces structured disagreement reports, padded job
proposals and provisional reconciliation with no automatic text changes. It
rediscovers the `hi`/`kyle` versus `i guess` discrepancy, the 03:08 near-same-time
`if if`, and timestamps beyond the requested 600 seconds. These are not new
listener-verified findings. C1/C2 remain byte-identical historical experiments.

The installed CrispASR help was inspected for the optional single-job adapter;
the adapter's bounded argument construction and hash rejection are tested.
E000/E001 original audio was not found in the expected local locations, so no new
recognizer run or listening verification was performed. No model/configuration
was promoted on the basis of these comparison counts.

## 2026-10-21: first real bounded third pass

After the original E000/E001 MP3s became available, both matched the existing
manifest hashes. [Real execution and import evidence](../reports/TARGETED_VERIFICATION_2026-10-21.md)
records one Parakeet TDT 1.1B run on E001 01:14.760–01:44.400: 29.640 s of
mono 16 kHz PCM, CrispASR 0.8.43 / eb633d90, Vulkan, English, no explicit
VAD/chunking. Extraction took 0.816 s; the ASR process including startup took
2.850 s. The 101-word result includes `hi kyle hi hi`, while the historical
chunked versions contain `i guess`. This remains an unreviewed alternative.

The clipped run is the same recognizer family with a different window, not a
new independent-model vote. Import retained all six historical runs, all fifteen
prior alignments and all 971 candidate IDs, adding 56 pairwise review records.
The portable export removes only an embedded private model path and preserves
the entire transcription array. No audio-based wording decision, WER claim or
canonical transcript update follows from this run alone.

## 2026-10-21: two-process CrispASR throughput observation

[Full observation, limitations and controlled follow-up](../reports/ASR_CONCURRENCY_2026-10-21.md). The owner ran **two CrispASR instances concurrently** and reported near-full 32 GB system RAM, ~8.5 GB/16 GB VRAM, GPU copy/compute peaks around 25%, virtually no drive activity, and approximately **6–7 minutes completion time per episode** without obvious slowdown. This is a provisional throughput observation; episode durations/settings and sequential control timings are not yet recorded. It does **not** measure ASR accuracy.

## 2026-10-22: December 2019 bonus — two ASR pipelines across two audio copies

[Four-export source inventory, exact comparison method and case review](../reports/BONUS_2019_12_ASR_COMPARISON_2026-10-22.md) accompanies [the retrospective bonus dossier](../episodes/BONUS-2019-12.md). The repository has **standard and alternate-copy Parakeet processed SRTs** (645/647 cues) and **Qwen Q8 + Canary CTC + Nemotron-labelled SRTs** (967/988 cues). The alternate audio has a **roughly one-minute ad pre-roll** absent from the standard copy; compare **spoken-show content** after trimming the ads and accounting for ~7-second differing model caption onset.

For conversation-only normalized word-token Levenshtein differences: standard Parakeet versus Qwen **338 edit operations / 5.92%** first-export-relative disagreement; alternate Parakeet versus Qwen **342 / 5.99%**. Same-pipeline standard versus alternate outputs differ by **168 / 2.94%** Parakeet and **150 / 2.59%** Qwen. These are **cross-transcript text distances**, **not audio-grounded WER, verified omission counts, verified hallucinations or model ranking**. Different cue totals do not establish superior coverage. **No model was run in this review**; exact model build, configuration, hardware, processing time and original audio hash are **not provided** and must not be invented.

The report flags **CHIDS/Cedus**, Soulbroker spellings, Cerinthala-like elf, **Dolo Popio/Andreeste**, **Eye of Groxl's God Killer title**, and an unmatched Qwen outro tail for audio review. Canon display convention **Groxl** comes from the owner, not model voting; **no raw SRT, generated transcript or glossary was changed**. A listener-verified reference is still needed before applying speech-level corrections.

## 2026-10-22: E084 — two complete ASR exports for one story episode

[Episode research](../episodes/E084.md) references [the two-model discrepancy report](../reports/E084_ASR_COMPARISON_2026-10-22.md). Repository sources: **Parakeet processed** (**2,765** cues; ~**24,435** normalized text tokens; final cue near **02:52:16.7**) and **Qwen Q8 + Canary CTC + Nemotron-labelled** (**4,709** cues; ~**24,725** tokens; last near **02:52:21.7**), both starting ~**00:00:09.6**. Whole-file normalized word-token **Levenshtein distance = 1,887 edit operations / 24,435 first-export words = 7.72% inter-ASR disagreement**, **not** WER or demonstrated ASR accuracy. The file pair shares the played narrative; model-label metadata cannot supply run commands, settings, word timestamps or verified speaker identities.

Material disagreement: the person whom Nothing is commissioned to kidnap belongs to **“Godsmen” in Parakeet** but **“Guardsmen” in Qwen**. Other contested words include **Stevius Ronkly**, **Castamere/Castlemere Lane**, priest/champion names, **Randorf/Randolph**, **Bockip/Bakit**, venue naming and the needle/potion details. Only **audio/primary notes** can resolve such differences; model voting would create false authority. The dossier documents **played outcomes that both drafts support** (Vorel/Nash first-round wins, Nothing double forfeit, observed opponent sabotage) while keeping proper names provisional. **Neither recognizer was rerun, no audio was checked, and neither source SRT was changed**.

## 2026-10-22: E085 two-export intake and retrospective case checks

[Full comparison report](../reports/E085_ASR_COMPARISON_2026-10-22.md) · [story evidence dossier](../episodes/E085.md). Source Parakeet processed **2,855 cues / 24,683 punctuation-stripped words** and Qwen Q8/Canary CTC/Nemotron-labelled **4,883 cues / 25,001 punctuation-stripped words**, both for E085 (~**02:45:55** including outro). The compared streams contain identical general episode events; a whole-episode normalized **word-token Levenshtein distance of 2,009 operations / 24,683 first-export tokens = 8.14%** is a **machine-to-machine disagreement ratio**, **not WER, verified omission/hallucination tally or recognizer accuracy ranking**. Cue boundaries and initial caption offsets differ; neither proves missing audio. No audio, original run commands, model versions/builds, inference timing, hardware config, or human word references are provided here; **no new inference was run**.

Important human review candidates are **Ventro (Royce champion) vs Kanja/Kenja (overall champion)**, **Minno/Minnow** and **Kidigree/Kidagri** spellings, the Lady-like **green woman-shaped apparition** without a stated identity, Nash's **externally negated magic** alongside successful Squirts casting, **Nash's successful save against Squirts' needle**, and payment narration (**1gp wages +20gp tips vs stated balance 20**). Both models agree on **Vorel defeating Nash and Ventro at the qualifier**, **Ventro vanishing**, and **two attackers entering the sleeping room**, none of which establishes ultimate BMF victory, resurrection or next episode's fight resolution. All original SRT bytes remain unchanged.

## 2026-10-22: January 2020 bonus two-ASR comparison and metadata anomaly

[Report and reproducible normalized-word comparison](../reports/BONUS_2020_01_ASR_COMPARISON_2026-10-22.md) · [source-first Q&A dossier](../episodes/BONUS-2020-01.md). Two exports of **one** ~33½-minute recording: **Parakeet processed 666 cues / 6,105 tokens**, **Qwen Q8 + Canary CTC + Nemotron-labelled 1,064 cues / 6,242 tokens**. Whole-episode (including ads) casefolded punctuation-stripped **word Levenshtein distance is 434 token edits**, **7.11% of first-export token count**. This is **inter-ASR text disagreement, not WER against audio**. No model runs, audio listening, verified deletions/hallucinations, reference words or validated speaker map. Different caption counts or one transcript's punctuation do not identify a winner; exact inference settings, software versions, GPU/hardware and source hash remain unknown.

Both files include roughly a **one-minute advertisement pre-roll** before the host explicitly calls this the **“December 2019” bonus** while noting non-members may hear it in **January**. The owner-normalized filename **“Bonus 2020-01 - January 2020”** is a **public-release archive month**, not a fresh story or a proven exact recording date. Important audio checks: **Steel Heaven/Chromianity name** (deliberate GM non-answer); **Beau later identifies E085's green apparition as Lady of Pain and names Ventro**; **rest-based Nash regeneration and external spell negation without disclosed Sigil mechanism**; **Jon's kenku curse/internal voice versus a contradictory Qwen phrase**; and **Principle's Diontalus crystal custody vs Vorel's suggested space launch**. Source SRTs remain **unchanged**, and the spoken Q&A does not add an E085 played scene.

## 2026-10-22: E086 two-ASR review — night assassins and spell keys

[Full report](../reports/E086_ASR_COMPARISON_2026-10-22.md) · [E086 dossier](../episodes/E086.md). Two original exports **not modified**, ~**02:54:46** each: **Parakeet processed: 2,807 SRT cues / 24,647 normalized tokens; Qwen Q8/Canary CTC/Nemotron-labelled: 4,770 cues / 24,984 normalized tokens**. Both contain the same episode, with subtitle segmentation differing. Normalized casefold/punctuation-stripped, full-episode **word-token Levenshtein = 1,946 edits / 24,647 first-export words = 7.90% inter-ASR disagreement**. **Not WER, audio-verified errors, model ranking, speaker identification, omission or hallucination count.** No audio listening, new model execution, exact inference settings, build versions, hardware/runtime, audio hash or independent word-level reference available.

High-impact audio/primary-sheet checks: **Order of the Crimson Moon** privately known to Nothing vs later group deciphering, **Heart of Kazdin/Kaz Desiray** spell description says **acid while GM narrates fire**, **young lizardfolk apparently dead then revived/stabilized with Spare the Dying and seen fleeing** (not a permanent homicide), **Arcane Spice 200gp one-day offer revoked before payment**, **20gp red cape price waived to free**, **spell keys 500gp per school / proposed 12×50 gp financing** and official Sigil anti-doping rules. Reconcile **Nash's prior 25,000gp in Tietkalla vault** with 21gp on-hand, and the out-of-character GM explanation of **the Lady's magical dampening field**, without backdating secrets to earlier scenes. Future checks **must compare actual audio or character sheets**, not blindly merge ASR.

## 2026-10-22: E087 dual-export ASR text audit — championship, test substitution and actual prize

[Full comparison report](../reports/E087_ASR_COMPARISON_2026-10-22.md) · [E087 dossier](../episodes/E087.md). Same ~**02:55:52** recording, **Parakeet processed 2,899 cues / 25,296 normalized words**, **Qwen Q8/Canary CTC/Nemotron-labelled 4,718 cues / 25,537 words**. Compute ordered-casefolded punctuation/apostrophe-stripped word-token Levenshtein: **1,675 edits**, **6.62% of first export's words**. **Text-only inter-ASR disagreement**; **not audio-verified WER, quality ranking, reliable omitted words/hallucinations, or verified speaker diarization**. No source audio played, model rerun, versions, hardware speeds, VAD details or reference transcript supplied; original SRTs **unchanged**.

High-value audio/primary-note checks: Mind Master full name, **dark-haired female companion's eyes recognized from Crimson Moon ninja**, actual **Kidigree urine substitution** (strong played evidence of cheating), **Tubbs 9K urine positive but no observed tampering**, **Vorel Kung defeats Mind Master then Kanja**, priest disc depicts **miniature staff within Kanja apparent body**, **actual 5,000gp prize and Kung trophy paid**, and **600gp to Nothing / 500gp to Nash / 100gp to Bill** accounting. At E087 cutoff **party departs toward temple**; **no priest meeting or resurrection**, **no purchased spell key or inn ownership**. Later repeated audio passes should specifically test names and exact spoken mechanics; do not use model majority vote or infer unplayed outcomes.

## 2026-10-22: E088 dual-ASR review — resurrection and corrected Sigil magic model

[Detailed two-export comparison](../reports/E088_ASR_COMPARISON_2026-10-22.md) · [source-first episode dossier](../episodes/E088.md). One ~**02:50:31** E088 recording, **Parakeet processed 2,618 cues / 23,066 normalized words** and **Qwen Q8/Canary CTC/Nemotron-labelled 4,105 cues / 23,127 normalized words**. Ordered casefold/apostrophe-and-punctuation-stripped whole-episode **word-token Levenshtein = 1,362 edits**, **5.90% first-export-relative text disagreement**, **NOT an audio-grounded WER, accuracy score, model ranking, or verified omission/hallucination count**. No audio listening, rerun, original inference arguments, model build/runtime configuration, audio hash, verified diarization or reference transcription supplied. Original SRTs untouched.

**Must-review correction:** E085–E087 document spells failing and a Sigil spell-key vendor, and the January 2020 bonus frames external suppression. **In E088 Beau explicitly says blanket Sigil-wide magic negation was a DM error and doesn't apply within Sigil; Nash actually casts Fire Bolt without a key.** Preserve what was played *then* but **mark its former rules explanation superseded now**, including in retrospective world profiles and prose. Other high-value passages: **Jon/Stanley's and Kristen/Hope's separate played choices to leave a void**, original corpses still strapped in mirrors room, organic Hope without implants, **Mind Master accompanied by Crimson Moon figures threatening Kanja over 100,000gp**, **Infernal mark “Stanley Billings” seen on neck**, **distinct spectrometer 100/700/1,400gp quotes**, **Vorel actually pays 1,250gp for pro BMF machine + Nash skull focus**, **30gp formal outfits actually delivered**, and the **not fully established eight-day Nash rest**. Next verification should prioritize actual listening at **00:35–00:39** for exact correction wording, and **00:19–00:30** for return mechanics, before any non-ASR canonical claim.

## 2026-10-22: E089 two-ASR text-only audit — Eight-day regrowth, Hive steward, recovered Scully

[Full report](../reports/E089_ASR_COMPARISON_2026-10-22.md) · [E089 episode dossier](../episodes/E089.md). The same ~**02:51:40** recording yielded **Parakeet processed 2,728 SRT cues / 23,424 normalized words** and **Qwen Q8/Canary CTC/Nemotron-labelled 4,485 cues / 23,652 words**. Casefolded punctuation/apostrophe-stripped whole-file **word-token Levenshtein = 1,747 edits / 23,424 first-export words = 7.46% text disagreement**. **Not audio-verified WER, actual deletion/hallucination accuracy, true diarization, or relative model ranking**. No audio listening, new model run, hardware/run timing, precise build/options, input hash or human-verbatim word reference. Original SRT untouched.

Audio/handout follow-ups: **E089 explicitly completes the eight-day skip and full Nash bodily regrowth**; **M Sports Weekly reports Kanja murdered, Harmonium investigating, not identified assailant**; **Duerto + Fax agency's record of stable Earth portal, steward Tobacho Fleur (?) in Hive** with **no exact door/key**; **Hope recovers original Scully**, while **Java/Jarva says second gun sold to Fedor/Tobacho network** for **7+2gp bribe**; **recovered ethereal spectrometer** reads Infernal/Abyssal **Weir destiny, proprietor/reward and alternate Stanley name** (spellings uncertain); **Barbara umbrella** appears temporally linked to **purple portal** to unknown dark many-legged location, **no full traversal**. Verify **rickshaw fare/tip stated as 1gp +20sp**, **two frogs cost 50sp**, **20gp restaurant and 1.5gp return rickshaw**, before updating canonical cash registers; avoid treating suspected Principle purchase of mined radioactivity as verified fact.

**Decision:** no ranking of ASR models; keep proper names provisional and prioritize **exact audio** at **~01:32–01:37** for Earth steward and **~02:23–02:48** for soul inscription/second gun agent, and **~00:24** for news attribution. No original transcription corrected.

## 2026-10-22: February 2020 bonus two-ASR comparison — retrospective commentary, not game audio

[Bonus dossier](../episodes/BONUS-2020-02.md) · [comparison report](../reports/BONUS_2020_02_ASR_COMPARISON_2026-10-22.md). Both sources describe the same **~34:01** cast Q&A: **Parakeet processed 674 cues / 6,322 normalized words**; **Qwen Q8/Canary CTC/Nemotron-labelled 1,042 cues / 6,457 normalized words**. Lowercase/remove apostrophes and punctuation (preserve Unicode letters/digits) then compute full ordered word-token Levenshtein: **459 edits, 7.26% of Parakeet word count**. **Inter-ASR text disagreement only**, no audio-reference WER, no verified omissions/hallucinations, no relative quality ranking. No new model passes, build/config/time metrics, audio listening or verified source recordings; original SRTs untouched.

Major audio-name checks: **host describes January/early February 2020 despite February file**; **E091 recorded “tonight”**; **Hack Loman** backup PC (never played); **Solar Mines' player-described “micro sun”**, **Slow Peters already documented E073 as fire elementals**, GM withheld **Nash's parentage** and **possible dragon hybrid child**; **Groxl** canon spelling vs several ASR phonetic guesses; **Jon intentionally silent Diontalus during three-month gap** with hypothetical never-spoken “told you so”; **unplayed Archibald, Scrumptious, high-elf fencer Fochirolass (?) and Buster Balls McBuster** concepts. Audio priority: **~18–24 min and 28–33 min**, original fighter design file desirable if available. Strictly **out-of-game commentary after E089**, not source for adding played campaign developments.

## 2026-10-22: E090 dual-export ASR analysis — Hive entry, Scully gift, Tobacho's condition

[Two-export report](../reports/E090_ASR_COMPARISON_2026-10-22.md) · [E090 source-first dossier](../episodes/E090.md). Same ~**02:49:50** episode, **Parakeet 2,650 cues / 23,453 normalized words** and **Qwen Q8/Canary CTC/Nemotron-labelled 4,294 cues / 23,635 normalized words**. Strip `(speaker N)`, casefold, remove apostrophes and punctuation but keep Unicode letters/digits, then compute ordered **word-token Levenshtein: 1,903 edits / 23,453 = 8.11% inter-ASR transcript disagreement**. **Not audio WER or a ranking, known error/hallucination count or evidence of verified omissions.** No new model runs, audio listening, primary handout verification, decoding settings/model versions, hardware/timing or human reference transcript; original SRTs untouched.

Review priorities: **00:27–00:31 GM reveals Nash's DNA-fused thermal underwear and active fly 10/cooling** (not simply future suggested feat); **00:54–01:05 Harmonium commander's name, caged escaped prisoner and no witnessed execution**; **~01:37 Spatulo clue, later Dragon hostility**; **~02:14 blue vs black dragon explicitly settles on blue**, **~02:27 50gp appointment actually paid**, **~02:37–02:40 Scully is actually gifted/removed by goblin** (post-E089 item status reversal); **~02:40–02:49 promised Earth-portal location/access is *conditional* on an unknown retrieval task; cutoff is before briefing**. Four Lohar outfits at 50gp each **are delivered but the cash transfer is not voiced**; do not silently debit 200gp. Next bounded story source [E091](../sources/The%20Wastes%20S1E091.%20Going%20on%20a%20heist.parakeet.processed.srt).

## 2026-10-23: E091 two-ASR source comparison — troll test, captive bishop and White Tower heist

[Report](../reports/E091_ASR_COMPARISON_2026-10-23.md) · [episode dossier](../episodes/E091.md). **Parakeet processed 2,506 cues / 21,829 normalized tokens / ending 02:46:29.49**; **Qwen Q8/Canary CTC/Nemotron-labelled 4,188 cues / 22,021 normalized tokens / ending 02:46:29.18**. Lowercase, remove speaker labels and apostrophes (join contractions), strip other punctuation, then ordered word-token Levenshtein gives **1,736 edits / 21,829 = 7.95% inter-ASR textual disagreement**. **Not WER, independently verified accuracy, omissions, hallucinations or model ranking**. No audio listening, rerun, checked model build/settings, media hashes or human reference words. Neither SRT altered.

Story-critical listening: **conjured but damaging trial (Stanley down/stabilized and healed, all wounded restored)**, names **Zorander's Fist / Drethiel / Euphemius / Obsidian White / Stevius Ritley / Butar Thrun / Eulonis**, charmed bishop's **White Tower custody and key** as testimony, **airship and scrolls only promised**, **Shatter +2 actually loaned to Vorel**, sealed Lohar and Hive writs not redeemed, **level 10 out of character**. No heist, Fist possession or Earth crossing before E091 ends.

## 2026-10-23: E092 dual-export comparison — real key theft, delivered gear, airship hangar

[Full comparison](../reports/E092_ASR_COMPARISON_2026-10-23.md) · [E092 dossier](../episodes/E092.md). **Parakeet: 2,546 cues, 22,086 normalized words, end 02:44:03.320**; **Qwen Q8/Canary CTC/Nemotron-labelled: 4,306 cues, 22,268 words, end 02:44:03.260**. Strip cue IDs/timestamps and `(speaker N)`, lowercase, remove apostrophes, split on non-Unicode-alphanumeric characters and use ordered word-token Levenshtein: **1,674 edits / 22,086 = 7.58% inter-ASR disagreement**. **Not audio-verified WER, omissions, hallucinations, quality ranking, or verified diarization.** Neither audio listened nor model rerun; model build/decoding args/hardware timing/source hash/reference transcription not obtained. Original SRTs unchanged.

**Story-critical checks:** Tobacho sealed writ **actually accepted**; Lohar priest robes **actually delivered**, temporary disguises; **Stanley steals authentic pendant and high cleric wears fake**, **Hope briefly detained then released by Stanley's Modify Memory** (save adjudication needs listening); **8 Dimension Door and 4 Reverse Gravity scrolls, ring, +2 dagger, both Fox and Scully and bullets physically delivered**, **Smokey's belt absent**; **Fox versus earlier Mulder** and dagger-recipient differences remain flagged. **Nash charges ring with 3×L1 + 1×L2 Chromatic Orbs**. **Ship hangar reached and vessel toured; no departure**. Improvised elephant captain name uncertain.

## 2026-10-23: E093 — dual ASR text disagreement during Outlands airship flight

[Comparison report](../reports/E093_ASR_COMPARISON_2026-10-23.md) · [E093 dossier](../episodes/E093.md). **Parakeet: 2,833 SRT cues, 24,570 normalized words, final 02:54:05.840**. **Qwen Q8/Canary CTC/Nemotron-labelled: 4,839 cues, 25,045 words, final 02:54:05.740**. Lowercase, drop SRT IDs/times and `(speaker N)`, delete apostrophes, tokenize Unicode letters/digits, ordered word-level Levenshtein **2,139 edit operations / 24,570 Parakeet tokens = 8.71% inter-ASR disagreement**. **Not human-corrected WER, omission/hallucination totals or model quality**; no audio was listened to and no decoding runs/hardware benchmarks were performed. Exact pipeline settings/media fingerprints unavailable. Original sources unmodified.

**Critical evidence boundaries:** Vessel **Traveler's Twin** named and actually launched through Sigil portal into Outlands; **Mind Master procures ship (NPC claim), gives Vorel Amulet of Health, but Stanley actually wears it**; captain **hands over sending stone** and **Stanley sees White Tower siege with telescope**, not Fist contents. **Nash uses young black dragon form/acid breath**, rescues Hope after fall, she rides him and shoots Scully (accidental **18 friendly fire** to Nash, **31 critical damage** to flyer); **Stanley polymorphs one wyvern into rat** (no witnessed ground impact); **Vorel kills wyvern belowdecks with Shatter, suffering poison/injuries**. **Ship smokes/descends** at cutoff, no recorded crash or Fist capture. Captain spelling/gift intent/combat rule details require audio checking.

## 2026-10-23: E094 dual-ASR comparison — White Tower ward, conditional bargains and disputed artifact custody

[Full E094 comparison](../reports/E094_ASR_COMPARISON_2026-10-23.md) · [provisional dossier](../episodes/E094.md). **Parakeet: 2,386 cues, 21,574 normalized words, final 02:42:42.330**. **Qwen Q8/Canary CTC/Nemotron-labelled: 3,729 cues, 21,699 normalized words, final 02:42:42.280**. Lowercase, remove SRT time/cue IDs and `(speaker N)`, remove apostrophes, split text into Unicode-letter/digit words, full ordered **word-level Levenshtein = 1,324 edits / 21,574 = 6.14% inter-ASR disagreement**. **Not audio-verified word-error rate, measured recognition accuracy, omissions, hallucinations or diarization quality.** Audio not listened to, neither recognition pipeline rerun; build/settings/hardware timing/source media hashes unavailable. Original exports not altered.

**Editorial finding:** E093 ship **descending** becomes E094 **crash/bad landing beyond ridge with captain alive, one-week repair estimate**. Paired **Dimension Door** brings **Stanley/Nash/Vorel inside White Tower**, **Hope ward-rejected for 4 necrotic and 49 falling damage**, alive and in demon/devil camp; **Ulvert (?) bargain and magical temporary lawful-good alignment change played**, bringing Hope inside later. **Nash's ball confiscated by Walnut and returned**. **Knight Commander actually sentences party to death, then grants stay of execution**; **hexagonal Fist chest visible but unopened**, stolen **pendant key held briefly then returned to Stanley, finally placed in his bag**. **Separate gold Euphemius totem transfer unclear**, **unidentified final mind voice**. Requires targeted audio review. **No Fist or Earth transit at cutoff.**

## 2026-10-23: March 2020 public-release bonus — two-ASR source-first retrospective comparison

[Research dossier](../episodes/BONUS-2020-03.md) · [reproducible text comparison](../reports/BONUS_2020_03_ASR_COMPARISON_2026-10-23.md). **Parakeet processed: 712 SRT cues, 6,674 normalized words, end 00:35:37.410**; **Qwen Q8/Canary CTC/Nemotron-labelled: 1,088 cues, 6,906 normalized words, end 00:35:37.220**. Remove SRT indices and timing, speaker labels `(speaker N)`, lowercase, delete apostrophes, split on non-Unicode-letter/digit characters, full ordered word-token Levenshtein **523 edits / 6,674 Parakeet tokens = 7.84% inter-ASR disagreement**. **This is not measured audio WER, model ranking, speaker verification or confirmed omissions/hallucinations.** Original source files unchanged; audio not listened to; no ASR rerun, build/settings/VAD/source hashes or hardware timing available.

**Important source distinctions:** Beau explicitly calls the **Weir and Kitobol Prith/Kitobalpraith (spelling to verify)** his campaign's original creations; published **Planescape/Sigil and Far Realm** are source/inspirational material, **not proof Weir = Far Realm**. **M-sports poster preceded the developed game** as production history. **E081 shared sacrifice over possible PvP**, **Sigil's resurrection resources**, and Jon's **Stanley psychologically changed by death** are retrospective, **not new E093/E094 scenes**. **Disputed Diontalus aside at ~20:37**: Parakeet hears **“cat”**, Qwen **“capsule”**; neither confirmed canon. Hypothetical Hope godhood, Lady of Pain boss and possible solo Vorel show are unplayed/jokes. No new fictional story chronology row.

## 2026-10-23: April 2020 bonus — two-ASR comparison, Eye remnant and later-story spoiler

[April bonus dossier](../episodes/BONUS-2020-04.md) · [detailed comparison](../reports/BONUS_2020_04_ASR_COMPARISON_2026-10-23.md). Two unchanged machine SRTs: **Parakeet processed 815 cues / 7,038 normalized words / final 00:40:05.740**; **Qwen Q8/Canary CTC/Nemotron-labelled 1,395 cues / 7,315 words / final 00:40:05.540**. Strip cue IDs/times and speaker labels, lowercase, delete apostrophes, tokenize by Unicode letters/digits, run **ordered unit-cost full-transcript Levenshtein: 850 word operations / 7,038 = 12.08% inter-ASR difference**. This is **NOT audio-verified WER, omissions, hallucinations, source quality or diarization**. No audio listened or new recognition run performed; decoding/VAD parameters, exact builds, media fingerprints and runtimes unknown. Sources left untouched.

**High-impact source distinctions:** **Walnut is human male** (Beau explicitly says); **Eye of Groxl inactive/destroyed inner presence but physical remnant persists in Vorel's chest**, GM says artifact does not conventionally rot. **Moral contrast of Earth and Sigil intentional**; good defenders do not make entire Sigil safe. **Hivemind-connected future Nash conditional survival**; **bonus discusses the now-sourced [E098](../episodes/E098.md) finale**: Nash's Enlarge ends Banishment, returning the enemy into Nash's occupied dragon square; no adjudicated aftermath and not an E094 scene. **Host may say “April fifth” in Qwen** where Parakeet has only “fifth”; this is a suggested **member-access** date, not independently verified public or recording day. **Both SRTs contain ~40:01–40:05 art/design callback line** following the farewell, not a Qwen omission; its actual audible status/placement requires listening. E098's April 5, 2020 intro and announced immediate subsequent bonus recording support a same-session link, without externally verified release timing. Avoid backdating future events and place high-value listening checks in review queue.

## 2026-10-23: E095 — White Tower epidemic and two-ASR comparison

[E095 dossier](../episodes/E095.md) · [comparative report](../reports/E095_ASR_COMPARISON_2026-10-23.md). **Parakeet: 2,242 cues, 19,182 normalized words, end 02:42:51.790**; **Qwen Q8/Canary CTC/Nemotron-labelled: 3,632 cues, 19,276 words, end 02:42:51.460**. Strip cue/timecode, `(speaker N)`, lowercase, remove apostrophes, tokenize as Unicode letters/digits; **ordered unit-cost full word-token Levenshtein = 1,339 edits / 19,182 = 6.98% inter-ASR disagreement**. **Not audio-ground-truth word-error rate, validated hallucinations/omissions, diarization or model accuracy**. No audio listened to or models rerun; exact source audio, hashes, runtime/build options and hardware not available; originals unchanged.

**Evidence decisions:** E095 **Hope symptom-free, Stanley/Nash/Vorel feverish and unrested**; **Commander Alentris reports four defenders dead**, accuses Hope of introducing disease after E094 dust, but **no independently verified transmission mechanism**. **Hordweld remembers Incubatrix undead curse virus** vs journal **“cure to shale disease”**, a material **possible wrong-ritual mismatch**. **One dying library man visibly becomes black cloud**; **Hope walks into cloud and hears unidentified coercive voice**, not confirmed source of pathogen. **Lesser Restoration reduces stages, doesn't cure**; **Walnut not yet reciting incantation, broth still being prepared**. **Hope separated in library**, others upstairs. **Nash 6 fire damage in distinct toilet chest** never confuse with hexagonal relic chest. Review title/spell/stages by listening.

## 2026-10-23: E101 — one recording ends Arc Three and starts Arc Four

[E101 dossier](../episodes/E101.md) · [full-export two-ASR comparison](../reports/E101_ASR_COMPARISON_2026-10-23.md). Clean initial connected workspace and tracked GitHub `main` at **`4ad532a1e4c871b78645731f0977770137ac11fc`**. **Parakeet 2,736 cues / 24,605 normalized words / last end 02:49:58.210**; **Qwen Q8/Canary CTC/Nemotron-labelled 4,521 cues / 24,969 words / last end 02:49:58.760**. Whole-export SRT cue body concatenation, dropping index/time/speaker labels, lowercasing, deleting apostrophes, Unicode letter/digit word tokenization; **exact ordered word Levenshtein 1,973 / 24,605 = 8.02% inter-ASR disagreement**. **NOT audio WER, reference correctness, verified omissions or hallucinations**; filename model names not independently confirmed; no audio, source hash, model build/config, VAD or runtime benchmark measured. Provisional proper nouns: Zygast, Muglep, Plains of Antipathy, Carthax, Ulvert, Spatulo; timestamped audio-check queue in report.

**User-confirmed story structure:** Corrected **E101 is both Arc Three finale and Arc Four opener**, boundary Hope's **decision to go alone ~01:44 and completed portal exit ~01:58**; do not place all E101 into one arc. Played breakthroughs: **Stanley nat-20 death save**, rescues Alentris; Hope **attaches Hand of the Voice after severing right hand**, gains powers/cursed appearance, GM patron **restores Eye of Groxl to Vorel**, **Finger of Death raises demon**; demons **actually withdraw** when coalition ends. **Hope leaves through infernal portal with Spatulo**; gauntlet **locked in chest**, medallion **returned to Stanley**. New arc: **Hope visits Kaiser Casino**, host **claims to be Asmodeus (“Brett”)**, no formal pact yet; former companions regroup/rest. **No source transcripts changed or audio verified.**

## 2026-10-23: E100 — Fist opened midair, private message and connected-ASR comparison

[E100 dossier](../episodes/E100.md) · [full-recording comparison](../reports/E100_ASR_COMPARISON_2026-10-23.md). Sources from GitHub `main` at **`4a4425af75d3d815deed3c328a994f6007e3c643`** matched initial clean connected checkout: **Parakeet processed 3,584 cues / 31,018 normalized words / final 03:29:43.460**, **Qwen Q8/Canary CTC/Nemotron-labelled 6,247 cues / 31,599 words / final 03:29:43.480**. Drop SRT cue/time/speaker headers, lowercase, delete apostrophes, Unicode letter/digit word tokens; **exact complete ordered word Levenshtein 3,045 / 31,018 = 9.82% inter-ASR disagreement** (implementation checked against 180 short DP examples, all matched). **NOT reference WER, actual correctness, verified omissions or hallucinations**. No audio listened; build/model/decoding/VAD/hardware/timings unknown; SRTs untouched. Both contain a post-credits toe-related callback, audible status not checked.

**Played evidence:** Stanley **saves falling Alentris** and finds Fist chest intact; Nash loses dragon form and **attached headless demon separates**, no proven lingering permanent changes. **Three airships** and rival chest-seeking party arrive, including hooded mage **Spatulo (?)**, whom only Hope recognizes from E090; exact affiliation unknown. Minotaur **knocks Alentris unconscious, temporarily takes closed chest**. Nash **Hastes Vorel** and later **Thunder Steps himself/Hope to ground**. After a further Fire Storm **Stanley and Alentris become unconscious**; **Vorel removes stolen key from Stanley, activates lock, opens chest and physically claims gauntlet with severed hand inside** but does not wear it. **Hope alone receives a private call**, separate from **Vorel's GM-described dark whispers**. E100 title refers to a giant flier's brain matter after Hope's lethal shots; moon remains unexplained.

## 2026-10-23: E099 — White Tower chest falls and wild-magic moon

[E099 dossier](../episodes/E099.md) · [full-export comparison](../reports/E099_ASR_COMPARISON_2026-10-23.md). **Parakeet 2,846 cues / 24,379 normalized words / last cue 02:51:50.210**, **Qwen Q8/Canary CTC/Nemotron-labelled 4,903 cues / 24,778 words / last cue 02:51:00.370**. Remove cue indices/timing and speaker tags, join text, lowercase, remove apostrophes and tokenize on non-Unicode letters/digits; **exact complete ordered word Levenshtein 2,591 / 24,379 = 10.63% inter-ASR disagreement**. **NOT speech-reference WER, verified omissions/hallucinations or model accuracy**; no audio listening or recognition benchmark, model builds/decoding/VAD/hardware unknown. **Comparison caveat:** Parakeet has later-era ad pre-roll absent in Qwen and the end clocks differ by ~50s, so exact edits include possible audio-edition differences. Source SRTs unchanged; blob SHAs and revision logged in report.

**Research decisions:** Nash **survives E098 conjoinment** and **decapitates** the attached demon without removing its body. His GM-controlled magical aftermath brings a belief of drowning in **a picture of a lake** (not future death), four enlarged nearby creatures, substance-location knowledge (not acquisition), and **actual sudden night with a close city-bearing moon**. Celestial commander **Thayle (?) actually takes closed Fist chest**; Vorel's **Mass Suggestion**-driven kick dismounts her, Stanley **Feather Falls** her and chest lands on roof. **Alentris later takes chest back and flies**, but a hostile archer kills Pegasus: **Alentris and the still-closed chest fall off roof, fates unknown**. Distinguish **Thayle's slowed earlier fall, Stanley/Vorel's separately protected later fall and Alentris's unresolved final fall**. No Fist delivery, Earth return or audio verification.

## 2026-10-23: E098 — White Tower roof battle, new items and return from Banishment

[E098 dossier](../episodes/E098.md) · [full-episode two-ASR report](../reports/E098_ASR_COMPARISON_2026-10-23.md). **Parakeet: 2,782 cues / 24,563 normalized words / final 02:51:08.359**; **Qwen Q8/Canary CTC/Nemotron-labelled: 4,752 cues / 24,875 words / final 02:51:07.720**. Extract all SRT cue text, strip index/timing and `(speaker N)` tags, lowercase, join contractions by removing apostrophes, split on non-Unicode-letter/digit characters; **exact full-episode unit-cost ordered word Levenshtein = 1,907 / 24,563 = 7.76% inter-ASR disagreement**. Exact bit-vector computation checked against dynamic-programming results for 200 random short token pairs. **No audio heard, no human-reference WER, no confirmed omissions/hallucinations**; filenames alone suggest model/pipeline labels. No model-build, VAD, decoding or hardware performance metadata verified. Original ASR files unchanged.

**Key research decisions:** **Captain Waltz says ship following pegasi** (not a witnessed interception); **Stanley transfers eight Reverse Gravity scrolls to Nash**; all four receive new blacksmith items/healing potions; **Nash learns functioning but unused White Tower teleportation sigils** and GM-assigned Tietkalla/unknown-Earth destinations, with required special reagents still missing. **Main gate opens and roof ascent really occurs by two Dimension Doors and Hope's broom**, not the proposed Reverse Gravity. **Two winged enemies are slammed to death with Telekinesis; celestial pegasi approach**, but **Fist remains in closed chest with Alentris**. **Nash's new Enlarge on Vorel ends Banishment and returns enemy into Nash's dragon-occupied space**; fate explicitly deferred. Listening targets: Skyblinder/Corpse Slayer labels, Tietkalla variants, Thayle/Alentris orthography and exact overlap outcome.

## 2026-10-23: E097 — restricted compendium and celestial roof plan

[E097 dossier](../episodes/E097.md) · [dual-ASR report](../reports/E097_ASR_COMPARISON_2026-10-23.md). **Parakeet 2,494 cues / 20,811 normalized tokens / final 02:37:51.730**; **Qwen Q8/Canary CTC/Nemotron-labelled 4,068 cues / 20,996 tokens / final 02:37:51.520**. SRT indices/times and `(speaker N)` excluded, lowercase, apostrophes removed, Unicode-letter/digit word split; **unit-cost ordered word Levenshtein 1,519 edits / 20,811 = 7.30% inter-ASR disagreement**. **Not audio-grounded WER or recognized omissions/hallucinations**; no audio listening, command reruns, model builds, decoding/VAD or performance benchmarking.

**Research decisions:** Library gate **actually lifted**, **Walnut fetched later**, generic fiend compendium **doesn't name antagonist**, book left behind. **Alentris's death sentence formally revoked** and **celestial pegasi escort only expected**. **Roof Dimension Door plan accepted**, not performed; Waltz ship unconfirmed rather than canceled. **Hope hears meeting threat without demon appearing**, key still not given to Walnut. Source spellings Thayle, Alentris, relic legendary abilities and Kidigree/Limbo need audio review.

## 2026-10-23: E096 — cured plague and unperformed airship hijack

[Source-first E096 dossier](../episodes/E096.md) · [comparison report](../reports/E096_ASR_COMPARISON_2026-10-23.md). **Parakeet: 2,437 cues / 21,679 normalized words / final 02:44:05.070**; **Qwen Q8/Canary CTC/Nemotron-labelled: 4,160 cues / 21,930 normalized words / final 02:44:04.920**. Strip SRT cue IDs/times and `(speaker N)`, lowercase, remove apostrophes, split on non-Unicode-letter/digit; **unit-cost full-transcript ordered word Levenshtein = 1,698 / 21,679 = 7.83% inter-ASR difference**. **Not audio-reference WER or measured omissions/hallucinations/model quality**. No audio/listening, command-line reruns, source hashes, model builds or runtime/decoding/VAD/device benchmark data. Original SRTs unchanged.

**High-value clarifications:** E095 journal **“shale disease” cure demonstrably works** with **cradling + Celestial phonetics + broth poured**, and all **remaining** inhabitants treated (deaths beforehand cannot be reversed). **Stanley and Alentris Vayne form a relationship**. Hope's **private warning becomes shared party knowledge only later in E096**; no confirmed demon identity. **Captain Waltz's replacement-airship arrival next noon is an NPC message, not an observed vessel**. **Key-to-Walnut is Alentris's intention, NOT possession changed**, Fist chest unopened; **Celestia/return home uncertain**. **Restricted library gate lever identified by Walnut, but not opened by cutoff**.
