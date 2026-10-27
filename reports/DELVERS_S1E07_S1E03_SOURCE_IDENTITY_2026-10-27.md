# Delvers S1E07–S1E03 — transcript-source identity batch

**Date:** 2026-10-27. **Scope:** complete source-byte provenance and local historical Git objects for five played Delvers episodes. No new interpretation, ASR measurement or listening.

## Finding

All eleven recorded comparison exports equal their recorded Git blobs after replacing CRLF pairs with LF only, in memory. Raw bytes differ. Source files are not rewritten.

## S1E07

[Original comparison](../reports/DELVERS_S1E07_ASR_COMPARISON_2026-10-25.md) · [Dossier](../delvers/episodes/S1E07.md). Recorded source commit: `972e14ab8ac17e0e06558dea9e68111cba2e5b50`.

Originally fetched at a pinned commit.

| Export | Raw bytes | CRLF pairs | LF-only bytes | Recorded blob SHA-1 |
| --- | ---: | ---: | ---: | --- |
| P | 231,020 | 11,267 | 219,753 | `415015cee85f480cafccaa97fd8aacd80ddfa83e` |
| Q8 | 307,719 | 15,164 | 292,555 | `464814af25dfca0b7bbb3d6fdb5f40576886d5c2` |

All listed byte comparisons and historical source-path checks passed.

## S1E06

[Original comparison](../reports/DELVERS_S1E06_ASR_COMPARISON_2026-10-25.md) · [Dossier](../delvers/episodes/S1E06.md). Recorded source commit: `24b2c62932b64fc280c7f67eb31a0177306e094e`.

Originally fetched at a pinned commit.

| Export | Raw bytes | CRLF pairs | LF-only bytes | Recorded blob SHA-1 |
| --- | ---: | ---: | ---: | --- |
| P | 263,208 | 12,846 | 250,362 | `484ee2a69200d9d398d5ec22ba262336cca91c60` |
| Q8 | 348,414 | 17,064 | 331,350 | `aebb3ad8a139653da4011296f3dffc3c764c46e9` |

All listed byte comparisons and historical source-path checks passed.

## S1E05

[Original comparison](../reports/DELVERS_S1E05_ASR_COMPARISON_2026-10-24.md) · [Dossier](../delvers/episodes/S1E05.md). Recorded source commit: `a2fc719e9ea1997b7b5b679c0a9fec3a4c2f4864`.

Originally fetched at a pinned commit.

| Export | Raw bytes | CRLF pairs | LF-only bytes | Recorded blob SHA-1 |
| --- | ---: | ---: | ---: | --- |
| P | 233,426 | 11,418 | 222,008 | `6e3ecaebc689ab19e465b48082745fe56d720050` |
| Q8 | 311,807 | 15,476 | 296,331 | `3ea4d625cde319a7aeec76abc404cd3b69b74281` |

All listed byte comparisons and historical source-path checks passed.

## S1E04

[Original comparison](../reports/DELVERS_S1E04_ASR_COMPARISON_2026-10-24.md) · [Dossier](../delvers/episodes/S1E04.md). Recorded source commit: `d475a95ea7d4a69b79bfbd2fb93b643e2464ab20`.

Originally fetched at a pinned commit.

| Export | Raw bytes | CRLF pairs | LF-only bytes | Recorded blob SHA-1 |
| --- | ---: | ---: | ---: | --- |
| P | 231,816 | 11,296 | 220,520 | `0a56deaad51f03734dabb441e31d47a843c8f8a9` |
| Q8 | 310,084 | 15,408 | 294,676 | `ca6611fd7992660be490876926f4292f9a80298e` |

All listed byte comparisons and historical source-path checks passed.

## S1E03

[Original comparison](../reports/DELVERS_S1E03_ASR_COMPARISON_2026-10-24.md) · [Dossier](../delvers/episodes/S1E03.md). Recorded source commit: `4c94049d48e45d4ac589f038d593619c9d2bf068`.

Originally fetched at a pinned commit.

| Export | Raw bytes | CRLF pairs | LF-only bytes | Recorded blob SHA-1 |
| --- | ---: | ---: | ---: | --- |
| P | 236,721 | 11,481 | 225,240 | `f7a2823f5b2ad8e048a324c2a05d9789cbcf5506` |
| Q4 | 310,435 | 15,108 | 295,327 | `bd0e0373989511d9045eec74ecc06f3325a896da` |
| Q8 | 321,575 | 15,980 | 305,595 | `da85b4f44a0d397c64670dc3fac2397e343bf34c` |

All listed byte comparisons and historical source-path checks passed.

## Identity boundaries

The three genuine S1E03 sources all contain `(corrected)` in their filenames and include separate P, Q4 and Q8 exports. S1E04’s historical comparison instead uses two uncorrected S1E03-named files that contain S1E04. The correctly named S1E04 copies prepend ads and are not included in this comparison. No files are renamed, merged or substituted. Existing metrics and recording clocks keep their original input sets.

## Method and limits

Read complete local bytes once; compute raw SHA-256 and framed Git blob SHA-1; replace CRLF with LF in memory; directly compare with local `git cat-file blob` output and independently verify its framed hash. Use `git ls-tree` at each report’s recorded source commit to check exact source-path membership. No other normalization, approximate text matching, network retrieval or current remote-tip query is performed.

The [data/checkpoint](../project/DELVERS_S1E07_S1E03_SOURCE_IDENTITY_2026-10-27.json) preserves per-episode results, exact paths, hashes and source file states. These checks establish content correspondence with recorded objects and commits; they do not extend interpretive coverage or verify original audio. Prior measurements remain historical inter-ASR disagreement, not accuracy. No name, count, item custody, testimony or other fictional uncertainty is resolved.

## Preservation and validation

[Exact pre-edit originals](../research/legacy/2026-10-27/delvers-s1e07-s1e03-source-identity/README.md) preserve all ten dossier/comparison files and the two shared progress documents. Dated follow-ups supplement historical wording. Narrative and world files are protected by recorded hashes. Shared queue and manifest updates occur once for the batch.

Validation results are recorded in the checkpoint after execution. Checks cover guarded edits, archived originals, protected files, new link targets, source file states, targeted Markdownlint and scoped whitespace. No full-repository audit is claimed.

**Markdownlint baseline:** The targeted 13-file run reports three pre-existing violations, independently reproduced from archived originals: consecutive blank lines (MD012) in the S1E03 dossier/comparison and a table-column mismatch (MD056) in the S1E04 dossier. There are no new lint violations. The older formatting remains preserved; archive README lint passed separately.

Next source-identity preflight: **S1E02**. Existing [source/listening questions](../delvers/REVIEW_QUEUE.md) remain active; the main-campaign intake queue remains closed.
