# Multi-pass comparison implementation plan — 2026-10-21

Inspection: existing tools are small Python scripts; `build_transcripts.parse_srt`
already preserves cue text and source speaker labels. Tests use `unittest` (three
baseline reader-edition tests pass). Detailed CrispASR JSON uses millisecond
`offsets`, word arrays, and separate subword token probabilities. Its `t0/t1`
fields use a different unit; import offsets explicitly. SRT timing is cue-level.
The five `episode01-*` experiments cover 600 seconds, while E000/E001 source SRTs
are full-episode exports. The extra `baseline.json` has unconfirmed identity and
will not be assigned to an episode by guessing. Existing exports contain private
model paths; preserve originals and do not propagate those paths into new output.

1. Add a dependency-free recognition model and adapters, reusing the SRT parser.
   Record immutable source hashes, declared audio identity/coverage, and unknown
   metadata explicitly. Keep original text, token confidence, and timing precision.
2. Align using time-constrained local text anchors and bounded edit alignment.
   Preserve all tokens, flag ambiguous/fallback alignment and timing anomalies.
3. Emit JSON/Markdown review records and padded, merged retranscription jobs.
   Use content-based candidate IDs and a separate reviewer decision ledger.
4. Keep reconciliation as primary-source plus alternatives, never publication.
   Import clip results with explicit episode offsets and coverage as extra runs.
5. Exercise synthetic omissions, timing, repetitions, overlap, validation, and
   scaling; compare E000/E001 exports and the five historical experiments.
6. Document reproduction, measured comparison results, limitations, and the next
   audio-grounded reference experiment. Update the existing project documents.

Optional adapter: the installed CrispASR CLI was inspected with `--help` before
implementation. It supports `--offset-t`, `--duration`, `--output-json-full`,
`--output-file`, `--backend`, and `--model`. A bounded local clip pilot may use
these capabilities; no full-archive execution or transcript replacement.
