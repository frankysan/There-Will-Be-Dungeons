# Multi-pass export pilot — 2026-10-21

**Result:** working local comparison/review pipeline, tested on preserved E000 and
E001 exports. No audio-grounded improvement claim, new listening verification,
recognition run or canonical transcript changes. See [implementation and exact
usage](MULTIPASS_PIPELINE.md), [original plan](MULTIPASS_IMPLEMENTATION_PLAN.md)
and [machine-readable measurements, source/tool hashes and example IDs](MULTIPASS_PILOT_2026-10-21.json).

## Reproduction and inputs

```powershell
python -m unittest discover -s tests
python tools/pilot_asr.py --out local/multipass-pilot-verified
```

The output directory must be new. The recorded run used the above commands with
Python 3.15 on Windows. Portable inputs/settings are the three manifests under
`experiments/multipass/`. Python 3.10+ is supported; Windows/Linux Python 3.11 CI
configuration was added but hosted CI was not run in this session.

- **Full E000:** raw Parakeet SRT (1,606 normalized words), raw Qwen Q8 SRT
  (1,623); declared audio duration 813.120 s.
- **Full E001:** raw Parakeet SRT (31,205 words), raw Qwen Q8 SRT (32,244);
  declared audio duration 11,013.888 s. These are full-episode exports, not the
  600-second segmentation tests. Exact build, aligner, settings and recognition
  runtime for these historical SRT runs remain unknown where not documented.
- **Opening E001:** five detailed Parakeet JSON exports, each covering 600 s,
  with 1,701 / 1,699 / 1,699 / 1,692 / 1,692 words; the same full Qwen export is
  compared only within the opening scope. Pairwise intersections and source
  timing precision are explicit. The retained full Qwen word count in metadata
  must not be mistaken for an opening-window word count.

Audio hashes/durations come from the pre-existing source manifest. Historical
export association is owner-supplied evidence. Source files are hashed as read;
the original audio was not available in the expected `local/` or parent-directory
locations for a fresh identity/listening check. The unlabelled extra
`experiments/baseline.*` pair is excluded pending identity confirmation.

## Measured results

| Comparison | Run pairs | Review records | Possible omission | Conflicting recognition | Possible hallucination | Boundary anomaly | Uncertain segmentation | Merged jobs | Elapsed |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| E000 full | 1 | 61 | 25 | 27 | 0 | 2 | 7 | 22 | 0.059 s |
| E001 full | 1 | 2,336 | 1,286 | 874 | 0 | 96 | 80 | 439 | 1.618 s |
| E001 opening, five Parakeet runs + Qwen Q8 | 15 | 971 | 540 | 325 | 31 | 14 | 61 | 25 | 1.117 s |

Single local wall-clock observations include parsing, alignment and report
writing; they are **not ASR runtimes or replicated benchmarks**. Pairwise records
can describe the same underlying passage repeatedly. The hallucination category
requires both unilateral wording and low available probability; SRT imports have
no confidence, so absence of such flags in full-episode comparisons is not proof
of no hallucinations. The fourteen opening boundary records include individual
overrun words, not fourteen independent audio events. All records are unreviewed
and all audio-verification fields are false. No unlocated job candidates occurred
in these real exports; synthetic tests cover missing timing.

Full E000/E001 comparisons matched 1,560 / 29,688 word pairs respectively under
normalization. Neither is a reference accuracy score. No bounded fallback was
needed in these export pilots. Largest edit-alignment blocks were 80 / 323 / 154
cells, below the configured 192² cap. Different source boundaries do not imply
word-level precision in the resulting report.

## Representative candidates

| Approximate time | Preserved alternatives/evidence | Required check |
|---|---|---|
| E000 00:18 | Qwen includes `a` without a corresponding Parakeet word | Listen before insertion or deletion |
| E001 opening 00:00.320–00:12.400 | Baseline `no m h hello everybody` versus default VAD with no corresponding words; shorter `no m h` comparisons also trigger low-confidence suspicion | Separate initial music/noise from the audible greeting |
| E001 full 00:22.320–00:22.560 | Qwen `Oops`, absent from Parakeet | Determine whether the brief response is audible |
| E001 opening 01:40–01:42 | Baseline `hi` / `kyle hi` / `hi` versus chunked `i` / no matching words / `guess` | Check short greetings and overlapping speakers |
| E001 03:08.510–03:08.760 | Padded VAD `if if` with near-identical word intervals | Possible stitching duplicate; words remain preserved |
| E001 10:00 boundary | Chunked words extend beyond the 600-second request, ending at 600.800 s | Inspect exported boundary timing; do not infer extra input was read |

The JSON evidence snapshot contains selected records with stable IDs, source
references and diagnostic evidence. It is a representative subset, not the full
queue. Reproduction writes the complete `comparison.json` and Markdown reports
under the chosen local directory.

The five historical experiment artifacts remain unchanged. The two chunked
JSON exports are still byte-identical, SHA-256
`ac9dc3c9dc6d338bc7804cdba1a979da6b645a526c1159fdc097c9818a8187f6`;
their SRTs are also identical, SHA-256
`e9d7ed524e39f241f33588f5025b921a23b22adbdf8cdf7aa108f6dee84b2ddc`.
Turning deduplication off remains a no-op in this historical test.

## Validation and practical limits

- **31 unit tests passed**, including the three existing reader-edition tests.
  New cases cover omissions, substitutions, repetitions versus duplicates, drift,
  cue segmentation, overlap and conflicting speaker labels, short replies,
  missing/invalid timing, partial third-pass evidence, input/output validation,
  stable IDs, decisions, job bounds, adapter audio-hash rejection and mocked
  success/failure receipts, and independent reference edit rates.
- A **60,000-word** synthetic agreement test checks scaling. Long divergent and
  untimed sequences verify bounded DP, preservation of every token, explicit
  fallback uncertainty and resynchronization. These are integrity/complexity
  checks, not evidence that alignment is always correct.
- All **37 source SRTs / 127,224 cues** parsed in a read-only audit using the
  existing audit function. It recorded **158 nonpositive cues and 118 adjacent
  overlaps** across all variants. Those are preserved source properties;
  overlapping dialogue can be legitimate.
- Standard `python tools/validate_pilot.py` is **blocked by an existing filename
  migration**: it requests absent `sources/E000.parakeet.processed.srt` and the
  equivalent E001 short name. A read-only invocation with in-memory mapping to
  current full-title filenames passed exact source-to-draft coverage for E000
  (193 cues / 21 turns) and E001 (4,819 cues / 1,444 turns). Its remaining link
  failures are two pre-existing short-name raw-SRT links in `episodes/E000.md`
  and `episodes/E001.md`. No canonical episode content was changed to mask them.
- Installed CrispASR **0.8.43 / eb633d90** was checked with `--help` and
  `--version`. The adapter uses advertised options, one bounded job, matching
  audio SHA-256 and local model files, and retains private execution logs plus
  portable run metadata. **No real third-pass transcription was executed**:
  the original pilot audio was unavailable in the expected locations. Adapter
  tests use mocked processes and do not establish recognition quality.

Known limitations: ordered lexical alignment cannot resolve crossing simultaneous
utterances; drift, broad cues, repeated phrases or fallback boundaries can cause
false disagreements. No speech detector finds speech omitted by every model.
Confidence is uncalibrated. Reviewer overlays do not yet compose a publishable
transcript. These limits are explicit in the technical documentation.

## Next experiment

Create 20–30 minutes of manually audio-verified E000/E001 reference material,
including the greeting/interjection cases, a narrative sample and randomly
selected agreed passages. Evaluate Parakeet baseline and Qwen Q8 against the
same reference, then execute one selected padded third-pass job and import it
as additional evidence. Measure deletion, insertion and substitution rates plus
review workload; evaluate diarization, timing, punctuation and lore spelling
separately. Keep the baseline model choice provisional until those measurements
show an audio-grounded benefit.
