# Delvers S1E02–S1E01 — transcript-source identity batch

**Date:** 2026-10-27. **Scope:** complete source-byte provenance and local historical Git objects for S1E02 and S1E01, plus two supplemental advertised S1E04 copies. No new interpretation, ASR measurement or listening.

## Finding

All four S1E02/S1E01 inputs equal their historical Git blobs after replacing CRLF pairs with LF only, in memory. Raw bytes differ. Source files are not rewritten.

## S1E02

[Original comparison](../reports/DELVERS_S1E02_ASR_COMPARISON_2026-10-24.md) · [Dossier](../delvers/episodes/S1E02.md). Recorded source commit: `e908edb7b1b05207e6de2c281af72fb0f0415f8e`.

Originally fetched at a pinned commit.

| Export | Raw bytes | CRLF pairs | LF-only bytes | Historical blob SHA-1 |
| --- | ---: | ---: | ---: | --- |
| P | 245,097 | 11,962 | 233,135 | `d44dff08c13fe79b7d2c492dff4a47b43ece9825` |
| Q | 336,430 | 16,916 | 319,514 | `31516a81dbb8caf1f9b5bb35911df95173adc151` |

Both complete byte comparisons and historical source-path checks passed.

## S1E01

[Original comparison](../reports/DELVERS_S1E01_ASR_COMPARISON_2026-10-24.md) · [Dossier](../delvers/episodes/S1E01.md). Recorded source commit: `9c74201783dbc53f21f724fcd3ef2ced8de144ba`.

Originally read locally. Both recorded raw SHA-256 hashes match exactly; historical Git blob IDs were obtained from the originally recorded commit tree.

| Export | Raw bytes | CRLF pairs | LF-only bytes | Historical blob SHA-1 |
| --- | ---: | ---: | ---: | --- |
| P | 228,254 | 11,125 | 217,129 | `b7f36f432ba4d2098e4a30f2a62a88d20aa47856` |
| Q | 313,158 | 15,700 | 297,458 | `a08f857c78a2aabf48dbfb2cf7b60e88df450fe0` |

Both complete byte comparisons and historical source-path checks passed.

## Supplemental S1E04 advertised copies

The [identity audit](DELVERS_S1E03_SOURCE_IDENTITY_2026-10-24.md) records separate blob IDs for the correctly named S1E04 copies with ads. Both complete local copies match those recorded blobs after CRLF-to-LF conversion only. They remain separate from the older ad-free S1E03-named S1E04 comparison inputs. No metric or interpretation is transferred between copies. The identity audit records no source commit for these two blobs, so historical commit-path membership is not checked for them.

| Exact source | Raw bytes | CRLF pairs | Recorded blob SHA-1 |
| --- | ---: | ---: | --- |
| `sources/Delvers S1E04. Where did this dungeon come from.parakeet.processed.srt` | 233,671 | 11,372 | `182a2291c2820d6b75be3e633b0c6c94bb87d198` |
| `sources/Delvers S1E04. Where did this dungeon come from.qwen-q8.canary-ctc.nemotron.srt` | 312,862 | 15,564 | `858eaa0f05f713971803dd4fc1dfdbf3d7eaf102` |

## Method and limits

Read complete local bytes once; compute raw SHA-256 and framed Git blob SHA-1; replace CRLF with LF in memory; directly compare with local `git cat-file blob` output and independently verify its framed hash. Use `git ls-tree` at each report’s recorded source commit to check exact source-path membership. No other normalization, approximate text matching, network retrieval or current remote-tip query is performed.

The [data/checkpoint](../project/DELVERS_S1E02_S1E01_SOURCE_IDENTITY_2026-10-27.json) preserves per-episode results, exact paths, hashes and source file states. These checks establish content correspondence with recorded objects and commits; they do not extend interpretive coverage or verify original audio. Prior measurements remain historical inter-ASR disagreement, not accuracy. No name, count, item custody, testimony or other fictional uncertainty is resolved.

## Campaign coverage reconciliation

The eleven persisted source-identity checkpoints now cover **37 campaign archive IDs and all 77 inventoried SRT exports**, with no missing or extra source paths. This includes genuine corrected S1E03 P/Q4/Q8, both distinct S1E04 copy pairs, and the narrated S2E00 cutaway. Seventy-five exports have historical commit-path correspondence verified; the two advertised S1E04 copies have recorded-blob correspondence only. S1E01 additionally matches both originally recorded raw SHA-256 hashes exactly.

Previously recorded byte comparisons are reused, not rerun. All 77 source paths retain their recorded size and modification time. This closes transcript-fingerprint coverage, not semantic, listening or audio-copy verification. Earlier branch-tip uncertainties, ASR/interpretive limits and baseline lint findings remain recorded in their individual checkpoints.

## Preservation and validation

[Exact pre-edit originals](../research/legacy/2026-10-27/delvers-s1e02-s1e01-source-identity/README.md) preserve all four dossier/comparison files and the two shared progress documents. Dated follow-ups supplement historical wording. Narrative and world files are protected by recorded hashes. Shared queue and manifest updates occur once for the batch.

Validation results are recorded in the checkpoint after execution. Checks cover guarded edits, archived originals, protected files, new link targets, source file states, targeted Markdownlint and scoped whitespace. No full-repository audit is claimed.

Next verification: **targeted listening/alignment preparation**. Existing [source/listening questions](../delvers/REVIEW_QUEUE.md) remain active; the main-campaign intake queue remains closed.
