# Delvers S3E04–S3E01 — transcript-source identity batch

**Date:** 2026-10-27. **Scope:** complete source-byte provenance and local historical Git objects for four played Delvers episodes. No new interpretation, ASR measurement or listening.

## Finding

All eight local exports equal their recorded Git blobs after replacing CRLF pairs with LF only, in memory. Raw bytes differ. Source files are not rewritten.

## S3E04

[Original comparison](../reports/DELVERS_S3E04_ASR_COMPARISON_2026-10-25.md) · [Dossier](../delvers/episodes/S3E04.md). Recorded source commit: `10b82bdf4b36cd10b1c7b2189e5867bc0fe612ee`.

Originally fetched at a pinned commit.

| Export | Raw bytes | CRLF pairs | LF-only bytes | Recorded blob SHA-1 |
| --- | ---: | ---: | ---: | --- |
| P | 287,259 | 13,931 | 273,328 | `0bb6b6707cc30df2fae03989c0db86d906898948` |
| Q | 400,108 | 20,076 | 380,032 | `7a40187e62e04d6c6b1b7813a5f691779f1f6d66` |

Both complete byte comparisons and historical source-path checks passed.

## S3E03

[Original comparison](../reports/DELVERS_S3E03_ASR_COMPARISON_2026-10-25.md) · [Dossier](../delvers/episodes/S3E03.md). Recorded source commit: `351c80f93c4eba3a62296f92e8c146fd6719336e`.

Originally fetched at a pinned commit.

| Export | Raw bytes | CRLF pairs | LF-only bytes | Recorded blob SHA-1 |
| --- | ---: | ---: | ---: | --- |
| P | 240,337 | 11,608 | 228,729 | `34d39fae8c959f417f3731d4fafd8beeb0375ba6` |
| Q | 332,295 | 16,516 | 315,779 | `5d4ba1d8e1cb7bb2bd85443d378dcd7f644267e7` |

Both complete byte comparisons and historical source-path checks passed.

## S3E02

[Original comparison](../reports/DELVERS_S3E02_ASR_COMPARISON_2026-10-25.md) · [Dossier](../delvers/episodes/S3E02.md). Recorded source commit: `2e82c5bacffa26ce23e6ce7e28290134fe940108`.

Originally fetched from the default branch after pinned-ref failures; its precise historical tip remains unidentified.

| Export | Raw bytes | CRLF pairs | LF-only bytes | Recorded blob SHA-1 |
| --- | ---: | ---: | ---: | --- |
| P | 257,160 | 12,487 | 244,673 | `f554c9314ffe5dd2bfcdc5a13b93c7f8dbf920e5` |
| Q | 339,229 | 16,532 | 322,697 | `729433798f9b7a0f4788b5fedf5a3bd548d9bdd0` |

Both complete byte comparisons and historical source-path checks passed.

## S3E01

[Original comparison](../reports/DELVERS_S3E01_ASR_COMPARISON_2026-10-25.md) · [Dossier](../delvers/episodes/S3E01.md). Recorded source commit: `1701b3789a536e9197540e497f2ed92cea24a58a`.

Originally fetched at a pinned commit.

| Export | Raw bytes | CRLF pairs | LF-only bytes | Recorded blob SHA-1 |
| --- | ---: | ---: | ---: | --- |
| P | 234,056 | 11,361 | 222,695 | `1aac136e9cc845b89d4008a94963ac2772bfb2d4` |
| Q | 312,007 | 15,312 | 296,695 | `7acbb0d9e353e445fd6a1219ac3b2c7ab7ad7299` |

Both complete byte comparisons and historical source-path checks passed.

## Method and limits

Read complete local bytes once; compute raw SHA-256 and framed Git blob SHA-1; replace CRLF with LF in memory; directly compare with local `git cat-file blob` output and independently verify its framed hash. Use `git ls-tree` at each report’s recorded source commit to check exact source-path membership. No other normalization, approximate text matching, network retrieval or current remote-tip query is performed.

The [data/checkpoint](../project/DELVERS_S3E04_S3E01_SOURCE_IDENTITY_2026-10-27.json) preserves per-episode results, exact paths, hashes and source file states. These checks establish content correspondence with recorded objects and commits; they do not extend interpretive coverage or verify original audio. Prior measurements remain historical inter-ASR disagreement, not accuracy. No name, count, item custody, testimony or other fictional uncertainty is resolved.

## Preservation and validation

[Exact pre-edit originals](../research/legacy/2026-10-27/delvers-s3e04-s3e01-source-identity/README.md) preserve all eight dossier/comparison files and the two shared progress documents. Dated follow-ups supplement historical wording. Narrative and world files are protected by recorded hashes. Shared queue and manifest updates occur once for the batch.

Validation results are recorded in the checkpoint after execution. Checks cover guarded edits, archived originals, protected files, new link targets, source file states, targeted Markdownlint and scoped whitespace. No full-repository audit is claimed.

Next source-identity preflight: **S2E12**. Existing [source/listening questions](../delvers/REVIEW_QUEUE.md) remain active; the main-campaign intake queue remains closed.
