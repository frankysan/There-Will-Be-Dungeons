# Delvers S2E07–S2E03 — transcript-source identity batch

**Date:** 2026-10-27. **Scope:** complete source-byte provenance and local historical Git objects for five played Delvers episodes. No new interpretation, ASR measurement or listening.

## Finding

All ten local exports equal their recorded Git blobs after replacing CRLF pairs with LF only, in memory. Raw bytes differ. Source files are not rewritten.

## S2E07

[Original comparison](../reports/DELVERS_S2E07_ASR_COMPARISON_2026-10-25.md) · [Dossier](../delvers/episodes/S2E07.md). Recorded source commit: `bba3e150ed807966cd540e0c0c29218037f77c80`.

Originally fetched at a pinned commit.

| Export | Raw bytes | CRLF pairs | LF-only bytes | Recorded blob SHA-1 |
| --- | ---: | ---: | ---: | --- |
| P | 244,626 | 11,862 | 232,764 | `21e24394085960a57a51eb383397545353c50845` |
| Q | 323,330 | 15,844 | 307,486 | `2834696fe3564ce583a6f1aaa30b3c6548dd23ac` |

Both complete byte comparisons and historical source-path checks passed.

## S2E06

[Original comparison](../reports/DELVERS_S2E06_ASR_COMPARISON_2026-10-25.md) · [Dossier](../delvers/episodes/S2E06.md). Recorded source commit: `63fe810a272a9168c75d41fe7471b5637f118306`.

Originally fetched at a pinned commit.

| Export | Raw bytes | CRLF pairs | LF-only bytes | Recorded blob SHA-1 |
| --- | ---: | ---: | ---: | --- |
| P | 230,604 | 11,192 | 219,412 | `dd2babf6ab951562498cb50ceeb496720200cdd9` |
| Q | 305,909 | 14,984 | 290,925 | `c9ac3fcc0477c11952446eadba15327cc336ba07` |

Both complete byte comparisons and historical source-path checks passed.

## S2E05

[Original comparison](../reports/DELVERS_S2E05_ASR_COMPARISON_2026-10-25.md) · [Dossier](../delvers/episodes/S2E05.md). Recorded source commit: `bef7e3fc64ef1630ae06aed5121e502b33dff85b`.

Originally fetched at a pinned commit.

| Export | Raw bytes | CRLF pairs | LF-only bytes | Recorded blob SHA-1 |
| --- | ---: | ---: | ---: | --- |
| P | 211,361 | 10,290 | 201,071 | `ab54c19e0dca772e7c1702e597140f14867ff019` |
| Q | 278,534 | 13,556 | 264,978 | `9a8c2ad47964f80a816ada5656fc2f92f09bc18e` |

Both complete byte comparisons and historical source-path checks passed.

## S2E04

[Original comparison](../reports/DELVERS_S2E04_ASR_COMPARISON_2026-10-25.md) · [Dossier](../delvers/episodes/S2E04.md). Recorded source commit: `c287223fb98dd8433ba9e267bd4a50a4cddf7d51`.

Originally fetched at a pinned commit.

| Export | Raw bytes | CRLF pairs | LF-only bytes | Recorded blob SHA-1 |
| --- | ---: | ---: | ---: | --- |
| P | 266,819 | 13,019 | 253,800 | `89fbb54593e74e65c1088a62ca8d914b7dd3c656` |
| Q | 368,487 | 18,624 | 349,863 | `7dd05ae980bb13a1a2e8b9f378b4a1f752ff3f85` |

Both complete byte comparisons and historical source-path checks passed.

## S2E03

[Original comparison](../reports/DELVERS_S2E03_ASR_COMPARISON_2026-10-25.md) · [Dossier](../delvers/episodes/S2E03.md). Recorded source commit: `a8a5164fd670a1e7b230a3f07d54e52386769f41`.

Originally fetched at a pinned commit.

| Export | Raw bytes | CRLF pairs | LF-only bytes | Recorded blob SHA-1 |
| --- | ---: | ---: | ---: | --- |
| P | 208,295 | 10,162 | 198,133 | `47aae89567d85021aa91d56b496508b71135671d` |
| Q | 271,848 | 13,228 | 258,620 | `35d8cc033912779885d84550b5094cc8e2360857` |

Both complete byte comparisons and historical source-path checks passed.

## Method and limits

Read complete local bytes once; compute raw SHA-256 and framed Git blob SHA-1; replace CRLF with LF in memory; directly compare with local `git cat-file blob` output and independently verify its framed hash. Use `git ls-tree` at each report’s recorded source commit to check exact source-path membership. No other normalization, approximate text matching, network retrieval or current remote-tip query is performed.

The [data/checkpoint](../project/DELVERS_S2E07_S2E03_SOURCE_IDENTITY_2026-10-27.json) preserves per-episode results, exact paths, hashes and source file states. These checks establish content correspondence with recorded objects and commits; they do not extend interpretive coverage or verify original audio. Prior measurements remain historical inter-ASR disagreement, not accuracy. No name, count, item custody, testimony or other fictional uncertainty is resolved.

## Preservation and validation

[Exact pre-edit originals](../research/legacy/2026-10-27/delvers-s2e07-s2e03-source-identity/README.md) preserve all ten dossier/comparison files and the two shared progress documents. Dated follow-ups supplement historical wording. Narrative and world files are protected by recorded hashes. Shared queue and manifest updates occur once for the batch.

Validation results are recorded in the checkpoint after execution. Checks cover guarded edits, archived originals, protected files, new link targets, source file states, targeted Markdownlint and scoped whitespace. No full-repository audit is claimed.

**Markdownlint baseline:** The targeted 13-file run reports four pre-existing violations, independently reproduced from the archived originals: missing final newlines in the S2E03 dossier, S2E04 dossier and S2E03 comparison, plus a skipped heading level in the S2E04 comparison. There are no new lint violations. These historical formatting issues are preserved. Archive README lint passed separately.

Next source-identity preflight: **S2E02**. Existing [source/listening questions](../delvers/REVIEW_QUEUE.md) remain active; the main-campaign intake queue remains closed.
