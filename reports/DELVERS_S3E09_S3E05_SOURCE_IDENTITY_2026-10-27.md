# Delvers S3E09–S3E05 — transcript-source identity batch

**Date:** 2026-10-27. **Scope:** complete source-byte provenance and local historical Git objects for five played Delvers episodes. No new interpretation, ASR measurement or listening.

## Finding

All ten local exports equal their recorded Git blobs after replacing CRLF pairs with LF only, in memory. Raw bytes differ. Source files are not rewritten.

## S3E09

[Original comparison](../reports/DELVERS_S3E09_ASR_COMPARISON_2026-10-26.md) · [Dossier](../delvers/episodes/S3E09.md). Recorded initial commit: `9f963c06ffa882c863d0b45f4ed9221c8f0ca438`.

Originally fetched from the default branch after pinned-ref failures; its precise historical tip remains unidentified.

| Export | Raw bytes | CRLF pairs | LF-only bytes | Recorded blob SHA-1 |
| --- | ---: | ---: | ---: | --- |
| P | 260,594 | 12,681 | 247,913 | `5b283b1d2193e0d70591a32c9d6ef47b276b1ae8` |
| Q | 361,152 | 18,232 | 342,920 | `33917e223b6c6cd7c969c0768476478cddeec175` |

Both complete byte comparisons and historical source-path checks passed.

## S3E08

[Original comparison](../reports/DELVERS_S3E08_ASR_COMPARISON_2026-10-26.md) · [Dossier](../delvers/episodes/S3E08.md). Recorded initial commit: `9aa01b155e7465d0a74ef10653d02e23dc84a631`.

Originally fetched from the default branch after pinned-ref failures; its precise historical tip remains unidentified.

| Export | Raw bytes | CRLF pairs | LF-only bytes | Recorded blob SHA-1 |
| --- | ---: | ---: | ---: | --- |
| P | 225,798 | 11,007 | 214,791 | `0078bcd05b9c9b2836bbba0a34d1ee5a7becca62` |
| Q | 313,067 | 15,824 | 297,243 | `32151bd68f78c03c3636fab2cd53c6a3a3a7e183` |

Both complete byte comparisons and historical source-path checks passed.

## S3E07

[Original comparison](../reports/DELVERS_S3E07_ASR_COMPARISON_2026-10-25.md) · [Dossier](../delvers/episodes/S3E07.md). Recorded initial commit: `be83933f8338dfc347466c3e691f754721d6c1d5`.

Originally fetched at a pinned commit.

| Export | Raw bytes | CRLF pairs | LF-only bytes | Recorded blob SHA-1 |
| --- | ---: | ---: | ---: | --- |
| P | 252,170 | 12,240 | 239,930 | `994f7871713ff2197fa9bf48830052fc9ab40d61` |
| Q | 348,384 | 17,464 | 330,920 | `519f4927e57e667b0c32bc7258498576bd31d7f0` |

Both complete byte comparisons and historical source-path checks passed.

## S3E06

[Original comparison](../reports/DELVERS_S3E06_ASR_COMPARISON_2026-10-25.md) · [Dossier](../delvers/episodes/S3E06.md). Recorded initial commit: `8c63b10189f375019f815bd838416caacc0f6822`.

Originally fetched at a pinned commit.

| Export | Raw bytes | CRLF pairs | LF-only bytes | Recorded blob SHA-1 |
| --- | ---: | ---: | ---: | --- |
| P | 223,490 | 10,889 | 212,601 | `87a82c9211d9762c1e73f887e8d0ade4c916d7d3` |
| Q | 296,521 | 14,588 | 281,933 | `d99b8123042e78865fb13d5403e6d6cf9c7326b2` |

Both complete byte comparisons and historical source-path checks passed.

## S3E05

[Original comparison](../reports/DELVERS_S3E05_ASR_COMPARISON_2026-10-25.md) · [Dossier](../delvers/episodes/S3E05.md). Recorded initial commit: `2ad71c746c7d118ac408cf24e492df520351377a`.

Originally fetched at a pinned commit.

| Export | Raw bytes | CRLF pairs | LF-only bytes | Recorded blob SHA-1 |
| --- | ---: | ---: | ---: | --- |
| P | 230,524 | 11,176 | 219,348 | `e58be47876ed187ba1426da9682b3dab942991ad` |
| Q | 311,504 | 15,508 | 295,996 | `b428c2d8937fd8751a8226255ff1ac32bc0e05ae` |

Both complete byte comparisons and historical source-path checks passed.

## Method and limits

Read complete local bytes once; compute raw SHA-256 and framed Git blob SHA-1; replace CRLF with LF in memory; directly compare with local `git cat-file blob` output and independently verify its framed hash. Use `git ls-tree` at each report’s recorded initial commit to check exact source-path membership. No other normalization, approximate text matching, network retrieval or current remote-tip query is performed.

The [data/checkpoint](../project/DELVERS_S3E09_S3E05_SOURCE_IDENTITY_2026-10-27.json) preserves per-episode results, exact paths, hashes and source file states. These checks establish content correspondence with recorded objects and commits; they do not extend interpretive coverage or verify original audio. Prior measurements remain historical inter-ASR disagreement, not accuracy. No name, count, item custody, testimony or other fictional uncertainty is resolved.

## Preservation and validation

[Exact pre-edit originals](../research/legacy/2026-10-27/delvers-s3e09-s3e05-source-identity/README.md) preserve all ten dossier/comparison files and the two shared progress documents. Dated follow-ups supplement historical wording. Narrative and world files are protected by recorded hashes. Shared queue and manifest updates occur once for the batch.

Validation results are recorded in the checkpoint after execution. Checks cover guarded edits, archived originals, protected files, new link targets, source file states, targeted Markdownlint and scoped whitespace. No full-repository audit is claimed.

Next source-identity preflight: **S3E04**. Existing [source/listening questions](../delvers/REVIEW_QUEUE.md) remain active; the main-campaign intake queue remains closed.
