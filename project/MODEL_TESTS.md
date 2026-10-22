# Initial model tests (supplied by archive owner)

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
