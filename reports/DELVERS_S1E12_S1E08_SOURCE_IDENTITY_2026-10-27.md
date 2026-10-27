# Delvers S1E12–S1E08 — transcript-source identity batch

**Date:** 2026-10-27. **Scope:** complete source-byte provenance and local historical Git objects for five played Delvers episodes. No new interpretation, ASR measurement or listening.

## Finding

All ten local exports equal their recorded Git blobs after replacing CRLF pairs with LF only, in memory. Raw bytes differ. Source files are not rewritten.

## S1E12

[Original comparison](../reports/DELVERS_S1E12_ASR_COMPARISON_2026-10-25.md) · [Dossier](../delvers/episodes/S1E12.md). Recorded source commit: `89df0a269f956b7572ca905c7202d03bba466b46`.

Originally fetched from the main branch after pinned-ref failure; its precise historical tip remains unidentified.

| Export | Raw bytes | CRLF pairs | LF-only bytes | Recorded blob SHA-1 |
| --- | ---: | ---: | ---: | --- |
| P | 271,515 | 13,256 | 258,259 | `f56f8043dcc87edf0d1378ecbd8ea9a51f82d892` |
| Q | 362,673 | 17,940 | 344,733 | `f93f47b1269c66bc6e120fb67188a58ef0aa2f19` |

Both complete byte comparisons and historical source-path checks passed.

## S1E11

[Original comparison](../reports/DELVERS_S1E11_ASR_COMPARISON_2026-10-25.md) · [Dossier](../delvers/episodes/S1E11.md). Recorded source commit: `d2763e5d2f3998286aecc27c42e42db9b835bb8c`.

Originally fetched at a pinned commit.

| Export | Raw bytes | CRLF pairs | LF-only bytes | Recorded blob SHA-1 |
| --- | ---: | ---: | ---: | --- |
| P | 243,024 | 11,858 | 231,166 | `5bdbbd397aeca078a0bc51251f80b3ca8100ede5` |
| Q | 325,614 | 16,092 | 309,522 | `98fe8e3dd3ee5224298e2091ea5be3231b3a72af` |

Both complete byte comparisons and historical source-path checks passed.

## S1E10

[Original comparison](../reports/DELVERS_S1E10_ASR_COMPARISON_2026-10-25.md) · [Dossier](../delvers/episodes/S1E10.md). Recorded source commit: `aabee4ffbdba2ff981522294c9dc0e62bfb0553d`.

Originally fetched at a pinned commit.

| Export | Raw bytes | CRLF pairs | LF-only bytes | Recorded blob SHA-1 |
| --- | ---: | ---: | ---: | --- |
| P | 271,003 | 13,203 | 257,800 | `941924c983b27ba8f81ed77a7d550befd6dcf6f0` |
| Q | 367,042 | 18,076 | 348,966 | `8ae4c5ab3a6e2868c477d86de97521248ae96b33` |

Both complete byte comparisons and historical source-path checks passed.

## S1E09

[Original comparison](../reports/DELVERS_S1E09_ASR_COMPARISON_2026-10-25.md) · [Dossier](../delvers/episodes/S1E09.md). Recorded source commit: `33372182a7cd6518355ffd4dff93c036ca82574a`.

Originally fetched at a pinned commit.

| Export | Raw bytes | CRLF pairs | LF-only bytes | Recorded blob SHA-1 |
| --- | ---: | ---: | ---: | --- |
| P | 242,705 | 11,787 | 230,918 | `5912bf61d92f7908e2a8b351847473ca2cfc9525` |
| Q | 324,928 | 16,036 | 308,892 | `9e142de2b0ae4eed5270a355212e702394a3eb13` |

Both complete byte comparisons and historical source-path checks passed.

## S1E08

[Original comparison](../reports/DELVERS_S1E08_ASR_COMPARISON_2026-10-25.md) · [Dossier](../delvers/episodes/S1E08.md). Recorded source commit: `6f36aecd601641ecea798e75be0024a1b64021e5`.

Originally fetched at a pinned commit.

| Export | Raw bytes | CRLF pairs | LF-only bytes | Recorded blob SHA-1 |
| --- | ---: | ---: | ---: | --- |
| P | 206,656 | 10,078 | 196,578 | `c33726511bd66309d593ecd9cc61d7b5dde4e24b` |
| Q | 282,241 | 14,104 | 268,137 | `339b0a578cf1141b84639aec2580c5b41c73d21f` |

Both complete byte comparisons and historical source-path checks passed.

## Method and limits

Read complete local bytes once; compute raw SHA-256 and framed Git blob SHA-1; replace CRLF with LF in memory; directly compare with local `git cat-file blob` output and independently verify its framed hash. Use `git ls-tree` at each report’s recorded source commit to check exact source-path membership. No other normalization, approximate text matching, network retrieval or current remote-tip query is performed.

The [data/checkpoint](../project/DELVERS_S1E12_S1E08_SOURCE_IDENTITY_2026-10-27.json) preserves per-episode results, exact paths, hashes and source file states. These checks establish content correspondence with recorded objects and commits; they do not extend interpretive coverage or verify original audio. Prior measurements remain historical inter-ASR disagreement, not accuracy. No name, count, item custody, testimony or other fictional uncertainty is resolved.

## Preservation and validation

[Exact pre-edit originals](../research/legacy/2026-10-27/delvers-s1e12-s1e08-source-identity/README.md) preserve all ten dossier/comparison files and the two shared progress documents. Dated follow-ups supplement historical wording. Narrative and world files are protected by recorded hashes. Shared queue and manifest updates occur once for the batch.

Validation results are recorded in the checkpoint after execution. Checks cover guarded edits, archived originals, protected files, new link targets, source file states, targeted Markdownlint and scoped whitespace. No full-repository audit is claimed.

**Markdownlint baseline:** The targeted 13-file run reports three pre-existing missing-final-newline violations (MD047), independently reproduced from the archived originals: the S1E10 dossier and the S1E10/S1E12 comparison reports. There are no new lint violations. Historical formatting is preserved; the archive README passed lint separately.

Next source-identity preflight: **S1E07**. Existing [source/listening questions](../delvers/REVIEW_QUEUE.md) remain active; the main-campaign intake queue remains closed.
