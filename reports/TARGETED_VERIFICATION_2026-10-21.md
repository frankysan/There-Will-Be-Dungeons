# First real targeted retranscription — 2026-10-21

**Result:** the Windows job executor successfully extracted, transcribed and
imported one selected E001 region. The third pass is additional unreviewed
evidence. No wording has been accepted, rejected or published; no improvement in
recognition accuracy has been established.

## Input and configuration

The newly available original E000/E001 MP3s were checked against the existing
archive manifest. Both SHA-256 values and byte sizes match. E001's SHA-256 is
`88b5e4f196dfa982e479d70e5b9e73694edba8994c8c46ed703efc1e00313795`.
The executor independently verified the source audio hash before execution.

Selected job: `j-00a3a4db22730d4516ae`, E001
**01:14.760–01:44.400**, 29.640 seconds. This consolidated job links 129
pairwise candidate IDs from the original opening comparison, including the
disputed short greetings around 01:40. Those IDs are not 129 independent audio
errors. Job context settings were 2,000 ms before/after and a 1,000 ms merge gap.

- Recognizer: **Parakeet TDT 1.1B**, `parakeet-tdt-1.1b.gguf`; quantization
  remains unspecified. Model-file SHA-256:
  `1a9259a18138179240be0f3d3d788c5dc9fd59979610b9c1e60a5ddc287ef302`.
- CLI: **CrispASR 0.8.43 / eb633d90**, backend `parakeet`, language `en`,
  GPU backend `vulkan`; no explicit VAD or chunking options. This uses the same
  recognizer family as the primary, with a different input window. It is not a
  new independent-model opinion; the historical Qwen Q8 run remains that opinion.
- Input extraction: FFmpeg mono 16 kHz PCM WAV. FFprobe confirmed one channel,
  16,000 Hz, and exactly 29.640 seconds. Full FFmpeg version is in the
  [machine-readable evidence](TARGETED_VERIFICATION_2026-10-21.json).
- Clip timestamps start at zero. Import adds **74,760 ms**, exactly once, to
  recover episode positions. All 101 output words fall within the job coverage;
  the first starts at 75,560 ms and the final word ends at 104,200 ms.

## Performance and findings

| Measured stage | Elapsed |
|---|---:|
| Audio extraction | 0.816 s |
| CrispASR process, including model startup | 2.850 s |
| Execution stages plus output validation/receipt writing | 3.672 s |

These are single-run wall-clock observations, not replicated performance
benchmarks. The recognizer's internal timing log is a different measurement from
the process wall time. Hash checking and help/version probes precede the timed
execution stages.

The output includes **`hi kyle hi hi`** around 01:40–01:42, compared with the
chunked runs' **`i guess`**. The initial `hi` is timed 100,440–100,600 ms;
`kyle` 100,680–101,080 ms; the following `hi` words are timed
101,480–101,720 ms and 101,960–102,280 ms. This is more ASR evidence for the
greeting candidate, not a listening-verified correction. The third pass also
recognizes an extra `there` around 99,640–99,720 ms relative to some prior runs;
that candidate likewise remains unresolved.

All **six previous runs**, all **15 previous pairwise alignments**, and all
**971 previous candidate IDs** were verified unchanged. The new run creates six
additional pairwise comparisons and **56 additional review records**, for
**1,027** records overall: 577 possible omissions, 338 conflicting recognitions,
32 possible hallucinations, 14 boundary anomalies and 66 uncertain segmentations.
Adding evidence can increase the record count; this is not an error-rate change.
No bounded alignment fallback was needed for the new pairs.

## Preservation and reproduction

Private logs, the original raw JSON/SRT, the extracted WAV and execution receipt
remain under ignored `local/third-pass-E001-greetings-2026-10-21/`. The original
raw JSON hash is
`df86bd1ae651a5143654c349b34b93ba9597b84efc7b52b64632d54a20beb281`;
the extracted WAV hash is
`a3f1b4a789a0c8ac45682f8a6457739d74c1675d71e14b09229f8a12c3ca3785`.

The [portable detailed export](../experiments/multipass/E001-greetings-third-pass.crispasr.json)
replaces only the embedded private model path with its filename. Its
`transcription` array, including original wording, word timestamps and token
probabilities, was checked equal to the immutable local raw export. Both hashes
are recorded in the evidence JSON. This is an explicitly derived artifact, not
a claim of raw-file byte identity.

Recompare the preserved outputs without running a recognizer:

```powershell
python tools/compare_asr.py experiments/multipass/E001-opening-with-third.json --out local/e001-third-recomparison
```

This produces JSON/Markdown reports, jobs, reconciliation and the separate
decision ledger. Choose a fresh output directory. The original primary and six
historical runs are retained by the new manifest. The executed comparison is
available locally in `local/E001-opening-with-third-2026-10-21/`.

To reproduce the bounded recognizer execution itself, set `$crispExe` and
`$modelPath` to the existing local executable/model paths; keep those settings
outside Git. Regenerate the original jobs in a new directory if needed:

```powershell
python tools/compare_asr.py experiments/multipass/E001-opening.json --out local/e001-targeted-source
python tools/run_asr_job.py local/e001-targeted-source/jobs.json --job-id j-00a3a4db22730d4516ae --audio "local/The Wastes S1E001. The Campaign Begins!.mp3" --model $modelPath --exe $crispExe --out local/e001-targeted-repeat --execute
```

Model nondeterminism or changed tool versions can change output. Preserve each
new receipt and its hashes instead of overwriting this run. The end of the clip
cuts a subsequent utterance; its wording remains source evidence, not a complete
utterance or a target for automatic repair.

## Validation and next step

The actual subprocesses completed with zero exit status; the CLI log confirms
the requested Parakeet model/backend and a 29.6-second clip. Source SHA-256,
FFprobe properties, coverage/offset, output validation, stable IDs, unchanged
historical runs/alignments and portable-export equivalence were checked.
The existing 31-test regression suite also passes.

Next, listen to 01:39–01:43 and create an explicitly reviewed reference/decision
entry. Then expand to the planned 20–30-minute sample, including agreed controls,
and calculate deletion/insertion/substitution rates independently. No listening
decision or reference WER was manufactured from recognizer agreement.
