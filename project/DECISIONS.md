# Decisions and rationale

Decisions marked **provisional** remain open to revision after listening tests.

| ID | Status | Decision | Why / evidence |
|---|---|---|---|
| D-001 | Agreed | Primary deliverable is human-readable transcripts for all episodes | Project goal; 1,000+ hours of primarily English audio |
| D-002 | Agreed | E000 and E001 are the first end-to-end milestone | Demonstrates short and long episode handling |
| D-003 | Provisional | Use Parakeet TDT 1.1B for initial readable transcript drafts | Faster than Qwen on user's hardware; appeared to preserve speech missing from Cohere |
| D-004 | Provisional | Use Qwen3-ASR 1.7B Q8 for difficult-passage comparison | Q8 notably faster than F16 in user testing; comparable draft coverage |
| D-005 | Confirmed | Do not use tested Cohere run as primary output | Listener verified it skips substantial speech |
| D-006 | Confirmed, per E001 | Merge numeric speaker 5 into Scott for reader-facing transcripts | Listener identified Scott doing a voice; source files stay unchanged |
| D-007 | Confirmed | E000 ends with spoken “Now”; remaining audio is music | Listener confirmation; raw and processed Parakeet timing differs |
| D-008 | Agreed | Keep original output files and explicit post-processing status | Model results changed across runs; reversibility and auditability matter |
| D-009 | Agreed | Separate speaker, role, and in-world identity | Same person can narrate, play a character, or perform an NPC voice |
| D-010 | Agreed | Keep source-cited world, character and location reference docs | Prevent later spellings and plot details from drifting |
| D-011 | Pilot implementation | Drafts use the available post-processed Parakeet text, reflowed but not corrected | Already readable punctuation and speaker names; retained raw for comparison |
| D-012 | Deferred | Choose final archival model by audio-grounded accuracy benchmark | Agreement among models is not a reference WER |
| D-013 | Provisional | Test Q4 + Canary CTC as a timing configuration | E001 invalid cues 56→0 and overlaps 19→1, while text stays identical |
| D-014 | Agreed | Keep alignment and speaker-quality decisions separate | E001 924/32,007 word positions have different speaker IDs between Q4 and Q4+Canary despite same text |
| D-015 | Deferred | Compare Qwen Q4 and Q8 against audio before choosing quantization | E001 differs by 1,070 token edits; Q8 has 237 more tokens, neither proves accuracy |

| D-016 | Agreed | Create reproducible *reader-edited* transcripts separately from generated machine drafts | Proper-name spelling improvements must not alter raw recognition data or get overwritten by the next build |
| D-017 | Agreed | Normalize documented names with per-turn edit logs and episode timestamps | Fan-wiki spellings are external orthography evidence, not word-by-word audio verification |
| D-018 | Agreed | Prefer cast label Jon in reader editions; retain John in original output | Wiki identifies Jon Jagger; speaker identities were already established by the pilot |
| D-019 | Agreed | Preserve the “Orifi or Orify?” name discussion pending audio check | Replacing both alternatives would erase actual pronunciation uncertainty |

| D-020 | Provisional | Retain no-explicit-VAD/no-chunk Parakeet as the E001 recognition baseline | Default VAD plausibly omits the greeting; 700 ms padding creates a boundary duplicate; chunked output loses other brief responses. No audio-grounded ranking yet. [Evidence](../reports/PARAKEET_SEGMENTATION_2026-10-21.md) |
| D-021 | Experimental result | Don't attribute the chunked missing greetings to LCS deduplication | 30 s chunks/3 s overlap with LCS auto vs off yielded identical JSON and SRT byte-for-byte. [Evidence](../reports/PARAKEET_SEGMENTATION_2026-10-21.md) |

## Decision changes

| ID | Status | Decision | Why / evidence |
|---|---|---|---|
| D-022 | Experimental implementation, 2026-10-21 | Compare primary Parakeet and independent Qwen Q8 with time-constrained anchors and bounded edit alignment | Preserves possible omissions and scales to multi-hour exported transcripts; [implementation and limits](../reports/MULTIPASS_PIPELINE.md) |
| D-023 | Implemented safeguard, 2026-10-21 | Keep original runs, source timing precision, alternatives and explicit reviewer decisions; no automatic transcript reconciliation | Agreement/majority and confidence do not establish audible speech; SRT cues do not supply word timing |
| D-024 | Evaluation pending, 2026-10-21 | Generate bounded targeted jobs and import third passes as additional evidence | A listening reference and independent deletion/insertion/substitution measures are required before claiming improved accuracy; [export pilot](../reports/MULTIPASS_PILOT_2026-10-21.md) |
| D-025 | Execution/import verified, 2026-10-21 | Retain the first real 29.640 s Parakeet clip as an additional unreviewed run | Original audio hash matched; 101 words imported with explicit clip offset; all prior runs, alignments and 971 candidate IDs preserved. Wording decisions remain pending listening. [Evidence](../reports/TARGETED_VERIFICATION_2026-10-21.md) |

When changing a decision, append a dated entry with reasons and affected episodes. Do not erase the original rationale; instead mark it superseded.

## Written-name evidence decisions (2026-10-21)

| ID | Status | Decision | Why / evidence |
|---|---|---|---|
| D-026 | **Accepted canonical spelling, 2026-10-21** | **Diontalus** is the curated project display spelling; keep `Dion Talus`, `Deontalus`, `Diantalus` and `Diontalis` as source/search aliases | Two Jon cast messages spell his own character **Diontalus**; the archive owner explicitly accepted creator authority for this spelling. [Discord report](../reports/DISCORD_SPELLING_2026-10-21.md). **This does not audio-verify any dialogue or certify the character's statements**. |
| D-027 | **Agreed provenance policy, 2026-10-21** | Keep **cast-written, creator-document, cast-posted handout, cast-shared recap, archived-link preview and fan inventory** distinct, and assign **Inverse** / **Delvers** references to those campaigns rather than **The Wastes** | [Discord report](../reports/DISCORD_SPELLING_2026-10-21.md) records source disagreements. **Tietkalla** is cast-supported, while **Catoblepraithe/Catobelpraithe**, **Angel Ashi/Angelashi** and other variants are still unresolved; orthography does not prove identity or chronology. |
| D-028 | **Owner-confirmed canonical item identity, 2026-10-21** | **Eye of Groxl** is the canonical display name for **one artifact**, also called `Eye of Grojil` in E053 processed ASR and `Eye of Groxel` in E054 processed ASR. Retain variants as source/search aliases; do **not** split them into separate items | **Archive owner explicitly confirmed** the variant names refer to **one item**, with **Groxl canonical**; this resolves the earlier cross-source uncertainty. Kyle's cast-written [Discord item title](../reports/DISCORD_SPELLING_2026-10-21.md) corroborates the spelling. The confirmation **does not independently identify a separately mentioned deity or legendary warrior**, and **does not count as audio verification**. Affects [E053](../episodes/E053.md), [E054](../episodes/E054.md) and [ledger](../world/CONSISTENCY_LEDGER.md). |

## Bonus episode curation decisions (2026-10-21)

| ID | Status | Decision | Why / evidence |
|---|---|---|---|
| D-029 | **Agreed, 2026-10-21** | Index **March 2019 The Year One Q&A!** as **BONUS-2019-03**, separate from Wastes E###. Original publisher **55** is a bonus, and original **56** becomes corrected **E055**. Treat bonus claims as **retrospective GM/player testimony, plans or speculation** according to provenance, not automatic played scenes | The archive's [episode crosswalk](EPISODE_NUMBERING.md) explicitly excludes the Q&A from main-story numbering. The [bonus dossier](../episodes/BONUS-2019-03.md) records valuable GM clarification (**Buttons/Stanley motives**, **Order 26**, **Nash's heart**) alongside **unplayed alternate routes, audience hypotheticals and future plans**. Keep old character knowledge/cutoffs intact; no audio verification was performed. |
