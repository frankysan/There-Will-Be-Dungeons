# Delvers S3E10 — transcript-source identity follow-up

**Date:** 2026-10-27. **Scope:** recorded transcript fingerprints and local historical Git objects. This supplements the [existing dossier](../delvers/episodes/S3E10.md) without adding dialogue interpretation, played events or listening coverage. Uses the [episode-analysis skill](../.agents/skills/twbd-episode-analysis/SKILL.md) for bounded provenance work.

## Finding

Both complete local exports equal the historically recorded Git blobs **after converting CRLF to LF only, in memory**. Their raw bytes differ. No source file is normalized, edited or replaced on disk.

| Export | Raw local bytes | CRLF pairs | LF-only / Git-object bytes | Recorded blob SHA-1 |
| --- | ---: | ---: | ---: | --- |
| P | 211,521 | 10,284 | 201,237 | `0a42f9d16de8e3b1a2f8f0cfb5d79b05e7351eee` |
| Q | 282,783 | 13,920 | 268,863 | `40be0079e42b01b147c975b40c5edafd7d99d281` |

The [data/checkpoint](../project/DELVERS_S3E10_SOURCE_IDENTITY_2026-10-27.json) records exact source paths, raw SHA-256/Git-blob fingerprints, historical tree results and phase-A file state. Each byte-count difference equals its CRLF count; every observed LF belongs to CRLF, and neither local file has a UTF-8 BOM.

## Method and historical correspondence

The [2026-10-26 comparison](DELVERS_S3E10_ASR_COMPARISON_2026-10-26.md) recorded two default-branch blob IDs after HEAD-pinned fetches failed, but compared only ten local opening lines. This check reads complete raw bytes, computes SHA-256/Git blob SHA-1 and directly compares the CRLF-to-LF result with existing local objects returned by `git cat-file blob`. Each object's framed Git SHA-1 is independently verified. No approximate word matching or additional text normalization is used.

A local `git ls-tree` at the recorded initial local commit, `0df6f7ca95fc76d3ba976d28c9ef727450b2f701`, assigns the same blob IDs to the two exact source paths. The source-content correspondence with that commit is now verified. This does not identify the precise historical default-branch tip used for the old fetch or query the current remote branch; no network retrieval is performed.

## Consequences and limits

The opening-line-only source-equivalence limit has a supported resolution for complete content apart from line endings. **Raw byte identity remains false.** Earlier provenance statements remain dated history with this follow-up linked from the dossier, original comparison, queue and manifest.

The historical 1,529/19,536 (7.83%) ordered inter-ASR disagreement figure is not recomputed or treated as accuracy. Prior primary-full/secondary-selected interpretation limits are unchanged. This pass does no semantic dialogue reading and listens to no audio. It resolves no names, badge/urn custody gaps, testimony, medical/revival detail or other fictional claim. Later S3E11/S3E12 events are not backdated into the unchanged played cutoff.

## Preservation and validation

Four exact originals and rebased reading copies are preserved in the [archive](../research/legacy/2026-10-27/delvers-s3e10-source-identity/README.md). Protected narrative, WORLD, ledger, source-inventory and prior S3E11 verification files remain unchanged. The already-repaired S3E10 dossier link is preserved. Source exports/audio and unrelated work are not written. No commit or push by this task.

Targeted guarded-edit, local-link, archive/protected-hash, source-file-state, Markdownlint and whitespace checks are recorded in the checkpoint after execution. Source fingerprints are phase-A evidence reused during validation; no whole-repository or rendered-site audit is claimed.

A further bounded source-identity check can inspect S3E09's recorded fingerprints and local-source limit. Existing [source/listening questions](../delvers/REVIEW_QUEUE.md) remain active; no main-campaign episode follows S3E12.
