# Delvers S2E02–S2E00 — transcript-source identity batch

**Date:** 2026-10-27. **Scope:** complete source-byte provenance and local historical Git objects for two played Delvers sessions and the S2E00 narrated guild-academy cutaway. No new interpretation, ASR measurement or listening.

## Finding

All six local exports equal their recorded Git blobs after replacing CRLF pairs with LF only, in memory. Raw bytes differ. Source files are not rewritten.

## S2E02

**Recording type:** played session. Archive ID retained; no story chronology is inferred from its season prefix.

[Original comparison](../reports/DELVERS_S2E02_ASR_COMPARISON_2026-10-25.md) · [Dossier](../delvers/episodes/S2E02.md). Recorded source commit: `e82cc0d9ec5ae818c044ae0fcffdcd7593589238`.

Originally fetched at a pinned commit.

| Export | Raw bytes | CRLF pairs | LF-only bytes | Recorded blob SHA-1 |
| --- | ---: | ---: | ---: | --- |
| P | 264,255 | 12,798 | 251,457 | `ed501751e06a63c6567359f318ddc8633f174341` |
| Q | 353,578 | 17,312 | 336,266 | `8e2a08d1f4a192b2513f678f9327deb898663cd7` |

Both complete byte comparisons and historical source-path checks passed.

## S2E01

**Recording type:** played session. Archive ID retained; no story chronology is inferred from its season prefix.

[Original comparison](../reports/DELVERS_S2E01_ASR_COMPARISON_2026-10-25.md) · [Dossier](../delvers/episodes/S2E01.md). Recorded source commit: `181342d2540927c2411e37e1115df480eff3c51f`.

Originally fetched at a pinned commit.

| Export | Raw bytes | CRLF pairs | LF-only bytes | Recorded blob SHA-1 |
| --- | ---: | ---: | ---: | --- |
| P | 248,466 | 12,133 | 236,333 | `37a4785e5be816a49c3ac60fd55e26ae29546fc8` |
| Q | 328,433 | 16,104 | 312,329 | `47e86b06ebeceb6e799ec46b6d65fda1343aae13` |

Both complete byte comparisons and historical source-path checks passed.

## S2E00

**Recording type:** narrated guild-academy cutaway during Season One. Archive ID retained; no story chronology is inferred from its season prefix.

[Original comparison](../reports/DELVERS_S2E00_ASR_COMPARISON_2026-10-25.md) · [Dossier](../delvers/episodes/S2E00.md). Recorded source commit: `5a024d072e3a5a65d7e0bc15675b1bed9ce9459d`.

Originally fetched at a pinned commit.

| Export | Raw bytes | CRLF pairs | LF-only bytes | Recorded blob SHA-1 |
| --- | ---: | ---: | ---: | --- |
| P | 17,152 | 854 | 16,298 | `105b185598848ff09e8df3183d9a1804544e9493` |
| Q | 19,588 | 880 | 18,708 | `4fccc6a466ffaabbf8a73263aaef0acd1e94dda2` |

Both complete byte comparisons and historical source-path checks passed.

## Method and limits

Read complete local bytes once; compute raw SHA-256 and framed Git blob SHA-1; replace CRLF with LF in memory; directly compare with local `git cat-file blob` output and independently verify its framed hash. Use `git ls-tree` at each report’s recorded source commit to check exact source-path membership. No other normalization, approximate text matching, network retrieval or current remote-tip query is performed.

The [data/checkpoint](../project/DELVERS_S2E02_S2E00_SOURCE_IDENTITY_2026-10-27.json) preserves per-episode results, exact paths, hashes and source file states. These checks establish content correspondence with recorded objects and commits; they do not extend interpretive coverage or verify original audio. Prior measurements remain historical inter-ASR disagreement, not accuracy. No name, count, item custody, testimony or other fictional uncertainty is resolved.

## Preservation and validation

[Exact pre-edit originals](../research/legacy/2026-10-27/delvers-s2e02-s2e00-source-identity/README.md) preserve all six dossier/comparison files and the two shared progress documents. Dated follow-ups supplement historical wording. Narrative and world files are protected by recorded hashes. Shared queue and manifest updates occur once for the batch.

Validation results are recorded in the checkpoint after execution. Checks cover guarded edits, archived originals, protected files, new link targets, source file states, targeted Markdownlint and scoped whitespace. No full-repository audit is claimed.

Next source-identity preflight: **S1E12**. Existing [source/listening questions](../delvers/REVIEW_QUEUE.md) remain active; the main-campaign intake queue remains closed.
