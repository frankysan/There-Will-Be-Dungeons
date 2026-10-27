# Delvers S3E12 — transcript-source identity follow-up

**Date:** 2026-10-27. **Scope:** recorded transcript fingerprints and local historical Git objects only. The existing [dossier](../delvers/episodes/S3E12.md) covers the completed campaign finale; this adds no new played event or source interpretation. Uses the bounded provenance workflow in the [episode-analysis skill](../.agents/skills/twbd-episode-analysis/SKILL.md).

## Finding

Both complete local SRT exports are exactly equal to the historically recorded Git blobs **after converting CRLF to LF only, in memory**. Their raw bytes are different. No source file was normalized, edited or replaced on disk.

| Export | Raw local bytes | CRLF pairs | LF-only / Git-object bytes | Recorded blob SHA-1 |
| --- | ---: | ---: | ---: | --- |
| Parakeet P | 230,059 | 11,275 | 218,784 | `9ca7f16780ee9adcb4bcc16c7977b303fe06c8b0` |
| Qwen Q | 314,983 | 15,908 | 299,075 | `2595bfc3f312d3a35f6b35ec74a2dbd30c933a29` |

The exact source paths, raw SHA-256/Git-blob fingerprints, phase-A file state and guarded documentation edits are in the [data/checkpoint](../project/DELVERS_S3E12_SOURCE_IDENTITY_2026-10-27.json). The difference in each byte count equals its CRLF count. Both files contain CRLF at every observed LF byte and no UTF-8 BOM; removing only CR bytes belonging to CRLF pairs produces the matching object bytes.

## Method and historical correspondence

The [2026-10-26 comparison](DELVERS_S3E12_ASR_COMPARISON_2026-10-26.md) recorded the two GitHub blob IDs but only checked nine local opening lines. This follow-up reads the raw local byte sequences, computes their SHA-256 and Git blob SHA-1, and compares the CRLF-to-LF result with the existing local Git objects returned by `git cat-file blob`. Each object's own Git SHA-1 framing is verified. This is a complete byte comparison, not a sample of dialogue or an approximate word match.

A local `git ls-tree` check at the originally recorded initial local commit, `6cf88c3d6a42c5698ff418cd22fc48ea80ec52f5`, assigns those same blob IDs to the two exact source paths. That establishes content correspondence with that recorded commit. It does not identify the precise historical default-branch tip used for the earlier remote fetch or query the current remote branch. No network retrieval is needed for the recorded immutable object comparison.

## What changes and what remains open

The finale's opening-line-only source-equivalence limit now has a supported, qualified resolution: complete local content corresponds exactly to the recorded blobs apart from CRLF/LF line endings. **Raw byte identity remains false.** Older provenance statements remain intact as dated history, with this follow-up linked from the dossier, original comparison, campaign queue and cleanup manifest.

The historical 1,946/20,356 inter-ASR disagreement figure is retained without recomputation. Exact byte correspondence neither proves transcription accuracy nor expands the earlier interpretive coverage: primary Parakeet was read fully, Qwen was computed fully and interpreted in selected windows. This pass performs no new dialogue reading or listening. It resolves no names, invitation wording, rescue count, blood application, item custody or Darmah revival detail.

Four exact pre-edit originals and rebased reading copies are preserved in the [archive](../research/legacy/2026-10-27/delvers-s3e12-source-identity/README.md). Narrative, WORLD, ledger and source-inventory files are protected unchanged. Source exports/audio, unrelated integration work and concurrent Wastes work are not written. No commit or push by this task.

## Validation and next verification

Targeted editorial/link checks, guarded-edit comparisons and changed-file Markdownlint results are recorded in the data/checkpoint after execution. Source fingerprints are phase-A evidence; final validation reuses them and checks file state rather than rerunning the entire source comparison. No whole-repository audit, rendered-site review or fresh ASR comparison is claimed.

A further source-identity audit can inspect the S3E11 recorded-blob/local-source limit. Existing source/listening questions remain in the [queue](../delvers/REVIEW_QUEUE.md); there is no new main-campaign episode after S3E12.
