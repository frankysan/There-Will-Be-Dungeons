# Delvers S3E11 — transcript-source identity follow-up

**Date:** 2026-10-27. **Scope:** recorded transcript fingerprints and local historical Git objects. This follows the existing [penultimate-episode dossier](../delvers/episodes/S3E11.md) without adding played events, dialogue interpretation or listening coverage. Uses the [episode-analysis skill](../.agents/skills/twbd-episode-analysis/SKILL.md) for bounded provenance work.

## Finding

Both complete local exports equal the historically recorded Git blobs **after converting CRLF to LF only, in memory**. Their raw bytes differ. No source file is normalized, edited or replaced on disk.

| Export | Raw local bytes | CRLF pairs | LF-only / Git-object bytes | Recorded blob SHA-1 |
| --- | ---: | ---: | ---: | --- |
| P | 230,783 | 11,228 | 219,555 | `cd63b7834a96f7ca353aa10c11150aee53becf1c` |
| Q | 303,324 | 14,784 | 288,540 | `315f59825b3775f428457d060c3f5fd5f30ef8f7` |

The exact source paths, raw SHA-256 and Git-blob fingerprints, historical tree results and phase-A file state are in the [data/checkpoint](../project/DELVERS_S3E11_SOURCE_IDENTITY_2026-10-27.json). Each byte-count difference equals its CRLF count. Every observed LF belongs to CRLF, and neither local file has a UTF-8 BOM.

## Method and historical correspondence

The [2026-10-26 comparison](DELVERS_S3E11_ASR_COMPARISON_2026-10-26.md) recorded GitHub default-branch blob IDs but compared only ten local opening lines. This check reads complete raw byte sequences, computes SHA-256/Git blob SHA-1, and compares the CRLF-to-LF result directly with the existing local objects returned by `git cat-file blob`. Each object's own framed Git SHA-1 is also verified. No word-level normalization or approximate text match is used.

A local `git ls-tree` at the recorded initial local commit, `4938750dffdf49e572a88853554e9b0ca07d68a9`, assigns those same blob IDs to the two exact source paths. This establishes content correspondence with that commit. It does not identify the historical default-branch tip used for the old fetch or query the current remote branch. No remote retrieval is performed.

## Consequences and limits

The opening-line-only source-equivalence limit now has a supported resolution for complete content apart from line endings. **Raw byte identity remains false.** The older provenance statements are retained as dated history, with this follow-up linked from the dossier, original comparison, queue and manifest.

The historical 1,486/21,260 (6.99%) ordered inter-ASR disagreement figure is not recomputed or treated as accuracy. Earlier primary-full/secondary-selected interpretation limits remain unchanged. This pass reads no dialogue semantically and listens to no audio; exact names, source/recording alignment, maps and sheets remain outside its scope.

The S3E11 played cutoff remains the gate opening/entry, discovery of captives and the bat diversion with rescue preparation. It does not become S3E12's completed evacuations, bat death or final victory. No narrative, custody, roster, medical/revival or other fictional claim changes.

## Preservation and validation

Four exact originals and rebased reading copies are in the [archive](../research/legacy/2026-10-27/delvers-s3e11-source-identity/README.md). Protected narrative, WORLD, ledger, source inventory and prior S3E12 verification files remain unchanged. Source exports/audio and unrelated integration or Wastes work are not written. No commit or push by this task.

Targeted guarded-edit, local-link, archive/protected-hash, source-file-state, Markdownlint and whitespace results are recorded in the data/checkpoint after execution. Phase-A source fingerprints are reused during validation; this is not a whole-repository or rendered-site audit.

A subsequent bounded source-identity check can inspect S3E10's recorded fingerprints and local-source limit. Existing [source/listening questions](../delvers/REVIEW_QUEUE.md) remain active, with no new main-campaign episode after S3E12.
