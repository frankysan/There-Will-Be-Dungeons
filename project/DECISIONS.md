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

When changing a decision, append a dated entry with reasons and affected episodes. Do not erase the original rationale; instead mark it superseded.
