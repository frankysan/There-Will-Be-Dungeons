# Delvers S2E12–S2E08 — transcript-source identity batch

**Date:** 2026-10-27. **Scope:** complete source-byte provenance and local historical Git objects for five played Delvers episodes. No new interpretation, ASR measurement or listening.

## Finding

All ten local exports equal their recorded Git blobs after replacing CRLF pairs with LF only, in memory. Raw bytes differ. Source files are not rewritten.

## S2E12

[Original comparison](../reports/DELVERS_S2E12_ASR_COMPARISON_2026-10-25.md) · [Dossier](../delvers/episodes/S2E12.md). Recorded source commit: `2dcbb98eaf12484e91225dacdf60d0a81f092a60`.

Originally fetched at a pinned commit.

| Export | Raw bytes | CRLF pairs | LF-only bytes | Recorded blob SHA-1 |
| --- | ---: | ---: | ---: | --- |
| P | 270,986 | 13,165 | 257,821 | `a9b7f9d5cbba70c4f4ccfa2d95704de2e399739a` |
| Q | 352,014 | 16,980 | 335,034 | `e2b59b51a2b184dc476e6e68e29de6ec85246af0` |

Both complete byte comparisons and historical source-path checks passed.

## S2E11

[Original comparison](../reports/DELVERS_S2E11_ASR_COMPARISON_2026-10-25.md) · [Dossier](../delvers/episodes/S2E11.md). Recorded source commit: `ce23faa581b0584917ac5256be1c634e5d28ba7b`.

Originally fetched at a pinned commit.

| Export | Raw bytes | CRLF pairs | LF-only bytes | Recorded blob SHA-1 |
| --- | ---: | ---: | ---: | --- |
| P | 224,490 | 10,939 | 213,551 | `bcf95e175155955297dfeca97298b6a0c48a150f` |
| Q | 307,665 | 15,376 | 292,289 | `856968710298341a9a6510ae87ddfd8222c32d3c` |

Both complete byte comparisons and historical source-path checks passed.

## S2E10

[Original comparison](../reports/DELVERS_S2E10_ASR_COMPARISON_2026-10-25.md) · [Dossier](../delvers/episodes/S2E10.md). Recorded source commit: `f79b869d9a41a13e96ceeb5907a0c09bdd5fc92f`.

Originally fetched at a pinned commit.

| Export | Raw bytes | CRLF pairs | LF-only bytes | Recorded blob SHA-1 |
| --- | ---: | ---: | ---: | --- |
| P | 199,063 | 9,740 | 189,323 | `691e5e2ddd35ad7639a646a7067d343125a76e89` |
| Q | 265,287 | 13,136 | 252,151 | `f35c0149912e2998b5e0d2059ae0a9cfc44d4aa4` |

Both complete byte comparisons and historical source-path checks passed.

## S2E09

[Original comparison](../reports/DELVERS_S2E09_ASR_COMPARISON_2026-10-25.md) · [Dossier](../delvers/episodes/S2E09.md). Recorded source commit: `bd23743219702ca258bd181a2e1999f4b3c9af48`.

Originally fetched at a pinned commit.

| Export | Raw bytes | CRLF pairs | LF-only bytes | Recorded blob SHA-1 |
| --- | ---: | ---: | ---: | --- |
| P | 249,994 | 12,125 | 237,869 | `cc5ffe74604a724e9553658c1c29b3063391820f` |
| Q | 335,681 | 16,576 | 319,105 | `79c4082052244debf45bac6e7ed27cafdb6afc3a` |

Both complete byte comparisons and historical source-path checks passed.

## S2E08

[Original comparison](../reports/DELVERS_S2E08_ASR_COMPARISON_2026-10-25.md) · [Dossier](../delvers/episodes/S2E08.md). Recorded source commit: `14c70f8be6772f0f7c7bd3e53fb8301da01e80d5`.

Originally fetched from the default branch after pinned-ref failures; its precise historical tip remains unidentified.

| Export | Raw bytes | CRLF pairs | LF-only bytes | Recorded blob SHA-1 |
| --- | ---: | ---: | ---: | --- |
| P | 264,489 | 12,855 | 251,634 | `4beb0c05072d34e8ac6f634dc9285aee71b9ec01` |
| Q | 360,393 | 17,992 | 342,401 | `a951ecbd9fba469584f628cf76881f272800c2e9` |

Both complete byte comparisons and historical source-path checks passed.

## Method and limits

Read complete local bytes once; compute raw SHA-256 and framed Git blob SHA-1; replace CRLF with LF in memory; directly compare with local `git cat-file blob` output and independently verify its framed hash. Use `git ls-tree` at each report’s recorded source commit to check exact source-path membership. No other normalization, approximate text matching, network retrieval or current remote-tip query is performed.

The [data/checkpoint](../project/DELVERS_S2E12_S2E08_SOURCE_IDENTITY_2026-10-27.json) preserves per-episode results, exact paths, hashes and source file states. These checks establish content correspondence with recorded objects and commits; they do not extend interpretive coverage or verify original audio. Prior measurements remain historical inter-ASR disagreement, not accuracy. No name, count, item custody, testimony or other fictional uncertainty is resolved.

## Preservation and validation

[Exact pre-edit originals](../research/legacy/2026-10-27/delvers-s2e12-s2e08-source-identity/README.md) preserve all ten dossier/comparison files and the two shared progress documents. Dated follow-ups supplement historical wording. Narrative and world files are protected by recorded hashes. Shared queue and manifest updates occur once for the batch.

Validation results are recorded in the checkpoint after execution. Checks cover guarded edits, archived originals, protected files, new link targets, source file states, targeted Markdownlint and scoped whitespace. No full-repository audit is claimed.

Next source-identity preflight: **S2E07**. Existing [source/listening questions](../delvers/REVIEW_QUEUE.md) remain active; the main-campaign intake queue remains closed.
