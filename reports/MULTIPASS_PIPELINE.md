# Multi-pass ASR comparison — implementation and use

Status: experimental comparison/review infrastructure. No audio-grounded accuracy
improvement has been established. Python 3.10+; standard library only. Run commands
from the repository root. Existing sources, episode content, reader editions and
the five segmentation experiments are inputs, never output targets.

## Reproduce the local export pilot

```powershell
python -m unittest discover -s tests
python tools/pilot_asr.py --out local/multipass-pilot
```

Choose a new output directory for each run; existing directories are rejected.
The pilot compares only preserved exports and never invokes ASR. Individual runs:

```powershell
python tools/compare_asr.py experiments/multipass/E000-full.json --out local/e000-compare
python tools/compare_asr.py experiments/multipass/E001-full.json --out local/e001-compare
python tools/compare_asr.py experiments/multipass/E001-opening.json --out local/e001-opening
```

`E000-full` and `E001-full` compare full-episode raw Parakeet and Qwen Q8 SRTs.
`E001-opening` compares all five **600-second** detailed Parakeet exports plus
the full Qwen Q8 export, with explicit comparison scope `[0, 600000]` ms. Full
Qwen source evidence remains available, but later words are not omissions in a
ten-minute run. Scope-edge overruns remain visible as boundary anomalies.
`experiments/baseline.json` is excluded because its episode/window identity has
not been confirmed. Historical timings and configurations remain in the
[segmentation report](PARAKEET_SEGMENTATION_2026-10-21.md).

Each output directory contains:

| File | Purpose |
|---|---|
| `comparison.json` | Versioned runs, original segments, lexical words, token probabilities, pair agreements, disagreements and provenance |
| `comparison.md` | Time-coded candidate queue, compared texts, evidence, status and priority |
| `jobs.json` | Padded, consolidated, duration-bounded retranscription proposals; unlocated cases kept separately |
| `reconciliation.json` | Original primary segments/word references, all alternatives and explicit decision overlays; no text mutations |
| `decisions.json` | Separate editable reviewer ledger, initially empty |
| `summary.json` | Source hashes, run metadata, measured counts, alignment work and wall time |

The aggregate pilot also writes `pilot-summary.json`. Counts are pairwise review
records, **not unique speech errors**: six runs produce fifteen comparisons, and
a region may carry both an omission hypothesis and a hallucination suspicion.

## Manifest and evidence contracts

The checked-in [E001 opening manifest](../experiments/multipass/E001-opening.json)
is a complete example. Schema version 1 requires:

- `episode`, `primary`, and at least two uniquely identified `runs`.
- `audio`: portable `id`, `duration_ms`, `sha256` (or null if unverified), and
  `identity_evidence`. The historical audio hashes come from the existing source
  manifest; association between historical exports and audio is owner-reported,
  not independently proven by embedded metadata. Execution requires a matching
  actual audio hash. Optional per-run `audio_id`/`audio_sha256` must match.
- Each run: `id`, `path` relative to the manifest, `format` (`srt` or
  `crispasr-json`), `coverage_ms`, `model`, `version`, `quantization`, `settings`,
  `processing_seconds`. Unknown metadata is explicitly null; do not infer an
  aligner from a filename. `provenance_note` and `parent_disagreement_ids` are
  supported. Add additional runs without modifying the alignment engine.
- Optional `timestamp_offset_ms`: add an explicitly known clip origin to source
  times. Defaults to zero for episode-relative exports. Do not apply twice.
- Optional `comparison_coverage_ms` restricts the analysis, while keeping each
  source run's real coverage. Pairwise comparison uses intersection of coverage.

Detailed JSON imports millisecond `offsets.from/to`; it deliberately does not
guess units from `t0/t1`. Missing offsets remain unknown. SRT tokens retain the
**entire containing cue interval**, never interpolated word positions. Original
segment text, speaker labels and source hashes are retained alongside normalized
lexical tokens. `source_word_index` addresses a detailed JSON source word;
character offsets address that word's original text, or the full source cue/text
when no source-word index exists. Normalization applies NFKC, lowercasing and
apostrophe folding; punctuation is excluded from lexical comparison. Genuine
repetitions are retained. Number spelling and contractions can still disagree.

Token probabilities remain token-level evidence. They are not relabelled as word
confidence or calibrated correctness. Word confidence is populated only when the
source word itself supplies it. Embedded private model paths are reduced to a
basename; source files are not rewritten. Keep local paths, credentials and
private settings out of portable metadata. Input paths belong in local manifests
when private; all new checked-in manifests use relative paths.

## Alignment and classification

`asr_alignment.py` indexes normalized trigrams and selects unique matches within
compatible time intervals. An ordered increasing chain supplies local anchors.
At most 64 candidates are considered per phrase. Between anchors, bounded edit
alignment uses lexical and temporal costs, preserving every token on each side.
One-to-two/two-to-one concatenation matches (e.g. `dusthill` / `dust hill`) remain
`uncertain_segmentation`, not automatic spelling corrections. Speaker IDs never
affect lexical matching and are never assumed equivalent between runs.

Defaults: 2,000 ms drift tolerance, 192 tokens per edit-alignment side, 30,000 ms
fallback buckets. Override with `--drift-ms`, `--max-tokens`, `--window-ms`.
Oversized divergent regions are partitioned into time buckets and capped token
blocks, with **every fallback result flagged uncertain**, including equal text.
Unknown-time evidence is preserved with explicit uncertainty, and does not get a
fabricated job location. Original runs remain in original order even if fallback
comparison groups use temporal order. Work per DP block is at most 192² cells;
recorded `dp_cells`, `max_dp_cells`, `anchors`, `fallback_blocks` expose scaling.
Pairwise work grows with the number of run pairs; this is not archive scheduling.

| Classification | Interpretation |
|---|---|
| Agreement | Equivalent normalized words within compatible timing; stored in pair agreement ranges |
| Possible omission | One run has unmatched words; either missing speech or an insertion could explain it |
| Conflicting recognition | Different wording in compatible intervals |
| Possible hallucination | Unilateral text plus mean available probability below 0.5; an uncalibrated heuristic needing audio |
| Boundary anomaly | Invalid duration, coverage overrun, backward/overlapping intervals or near-identical duplicate words; overlap can be genuine |
| Uncertain segmentation | Concatenation-equivalent forms, unknown timing, scope-crossing equal words, fallback alignment, or inconsistent segment/word text |

Priorities are heuristic: omissions, hallucination suspicions and boundaries are
high; other disagreements medium. Each record has `status`, `audio_verified`,
source-run references, word/segment IDs, precision, available confidence and
diagnostics. Additional runs appear as `context_only` evidence and are also
compared pairwise. No majority vote chooses wording. IDs hash the episode/audio,
run IDs/configuration, source token identities, local text/timing, comparison
scope, classification and diagnostics. Identical reruns and adding a third pass
retain existing pair IDs. Changing source order/token indices, configuration,
scope or algorithm can invalidate IDs; stale ledger IDs cause an error rather
than silently migrating review decisions.

## Review and provisional reconciliation

Edit a copy of `decisions.json`, then supply it to a fresh comparison:

```powershell
python tools/compare_asr.py experiments/multipass/E001-opening.json --decisions local/e001-opening/decisions.json --out local/e001-reviewed-comparison
```

Example entry (replace the ID with a real generated candidate; do not claim a
listening review unless one actually occurred):

```json
{
  "schema_version": 1,
  "decisions": [{
    "disagreement_id": "d-REPLACE_WITH_ACTUAL_ID",
    "action": "defer",
    "reviewer": "reviewer name",
    "date": "2026-10-21",
    "evidence": "Competing ASR wording; awaiting original audio",
    "audio_verified": false
  }]
}
```

`accept` or `reject` additionally requires `candidate_run_id` naming an aligned
candidate. Empty wording is a candidate too; absence is never automatically
chosen. `audio_verified: true` requires `audio_evidence` documenting the recording
and checked interval. These decisions are overlays only: no accept/reject path
edits primary segments, inserts minority speech, deletes repetitions or publishes
anything. Conflicting decisions across overlapping candidates still require
manual reconciliation. Audio-verified accepted/rejected records are omitted from
future jobs, but their evidence remains. Non-audio decisions remain job candidates.

## Targeted jobs and the Windows adapter

Manifest `job_options` can set `before_ms`, `after_ms`, `merge_gap_ms`,
`max_job_ms`, and a `suggestion` object. Defaults are 2 s before/after, 1 s merge
gap, 120 s maximum. Intervals clamp to the audio duration. Long regions split;
split edges may have less context. Every job retains original disagreement IDs,
audio identity, suggested configuration and reasons. No jobs execute during
comparison. The executor selects **one job ID** and rejects clips over 120 s.

The installed CrispASR `--help` was inspected: `--backend`, `--model`,
`--language`, `--gpu-backend`, `--output-json-full`, `--output-srt`,
`--output-file`, `--offset-t` and `--duration` are supported. The implementation
extracts an explicit FFmpeg PCM clip instead of relying on undocumented offset
timestamp conventions. Recognition times are clip-relative, then imported using
the known clip origin. It rechecks the required advertised flags at execution.

Set runtime variables to your private local files; do not put them in Git:

```powershell
# Set $audioPath, $modelPath, $crispExe and $jobId to existing local values.
python tools/run_asr_job.py local/e001-opening/jobs.json --job-id $jobId --audio $audioPath --model $modelPath --exe $crispExe --out local/third-pass
# Inspect the printed argument arrays, then run the same command with --execute.
```

Default is a command plan. `--execute` verifies source audio SHA-256, checks that
the model exists, extracts mono 16 kHz PCM, runs CrispASR, and stores raw output,
private logs, stage times, hashes and a `run-spec.json` for additional evidence.
Optional `--ffmpeg`, `--backend`, `--gpu`, `--quantization` configure local tools;
no model downloads or invented settings. The actual model choice comes from
arguments, not a job suggestion. The executor currently has no VAD/chunk setting
interface; exported runs with those settings can still be imported normally.
There is no batch executor, recovery scheduler or publication adapter.

Copy the original comparison manifest into a local directory, adjust its input
paths relative to the new manifest location, append `run-spec.json` to `runs`
and adjust that spec's `path` to the retained export. Keep its coverage, explicit
offset and parent IDs. Recompare into another new directory. Do not replace the
primary or the other source runs. Raw execution artifacts may contain private
paths: keep them under ignored `local/`; portable normalized evidence strips
embedded model paths.

## Audio-grounded evaluation

`asr_reference_metrics.py` calculates independent substitution, deletion and
insertion counts/rates and WER against a manually verified reference. Example
input contract:

```json
{
  "schema_version": 1,
  "episode": "E001",
  "audio_id": "E001-original-mp3",
  "coverage_ms": [100000, 103000],
  "audio_verified": true,
  "reviewer": "actual listener",
  "evidence": "recording hash and listening notes",
  "reference_text": "replace with manually verified words",
  "hypotheses": {"run-id": "exact exported words for the same sample"}
}
```

```powershell
python tools/asr_reference_metrics.py local/verified-reference.json
```

The tool requires explicit audio-verification metadata; it cannot authenticate a
human attestation. Supply hypotheses covering the **same manually bounded sample**;
automatic cue clipping is deliberately avoided. Exact Levenshtein components use
linear memory and a four-million-cell work cap; split larger references into
verified samples. WER is undefined for an empty reference. Tie-breaking between
equal-cost edit paths is recorded. Do not use ASR agreement as reference truth.

## Limits and next experiment

This is ordered lexical alignment with overlap diagnostics, not multi-speaker
acoustic alignment. Reversed simultaneous utterances, large timestamp drift,
coarse cues, repeated phrases and fallback bucket boundaries may yield false
disagreements. Segment text that differs from detailed words is retained and
flagged, but only the detailed word stream participates in lexical alignment.
There is no independent VAD/speech detector, so speech omitted by **all** runs
can remain undetected. Confidence thresholds are uncalibrated. Majority agreement
and higher word counts prove neither completeness nor correctness.

Next: manually verify the opening greeting, 01:23–01:42 greetings/banter,
02:17–03:08 interjections, 04:13–04:37 reactions, a Dusthill narration sample,
and a random agreed passage as a control. Score Parakeet baseline and Qwen Q8 on
the same reference, then one targeted third pass. Report deletion/insertion/
substitution rates and reviewer workload separately from diarization, timing,
punctuation and wiki-supported orthography. Fan-wiki text is spelling evidence,
not audio truth; D&D Beyond sheets remain campaign-end snapshots.
