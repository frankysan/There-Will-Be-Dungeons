# The Wastes — transcription and campaign-reference pilot

**Status:** The E000/E001 reader-edition pilot remains incomplete and not manually proofread. Processed Parakeet SRTs for subsequent episodes are now included as source material; E002–E012 have preliminary, unverified **reference dossiers**, not new publishable reader editions.

This package establishes a repeatable, **local-first** path from podcast audio to readable, speaker-labelled text, with a separate campaign reference that cites episode time positions. It covers the *There Will Be Dungeons* campaign described in the supplied files as *The Wastes*.

## Start here

1. [E000 — Introductions: reader-edited draft](transcripts/E000.reader-draft.md) ([machine draft](transcripts/E000.readable-draft.md), [edit log](transcripts/E000.reader-edits.json))
2. [E001 — The Campaign Begins!: reader-edited draft](transcripts/E001.reader-draft.md) ([machine draft](transcripts/E001.readable-draft.md), [edit log](transcripts/E001.reader-edits.json))
3. [External sources and chronology policy](project/EXTERNAL_REFERENCES.md), [Project charter](project/PROJECT_CHARTER.md), [workflow](project/WORKFLOW.md), [editorial rules](project/EDITORIAL_GUIDE.md) and [decision log](project/DECISIONS.md), [model test record](project/MODEL_TESTS.md) and [roadmap](project/BACKLOG.md)
4. [World reference index](world/README.md), [characters](world/CHARACTERS.md), [places](world/PLACES.md), [world history](world/WORLD.md), [chronology](world/CHRONOLOGY.md), and [consistency issues](world/CONSISTENCY_LEDGER.md), and [machine-readable entity index](world/entities.json)
5. [Episode dossiers](episodes/E000.md) and [E001](episodes/E001.md)
6. [Review queue](project/REVIEW_QUEUE.md), [automated file audit](reports/SRT_AUDIT.md), and [Qwen Q4/Q8/Canary variant evaluation](reports/QWEN_VARIANTS_2026-10-21.md)
7. **Expanded campaign context:** [E002 — Spiders](episodes/E002.md), [E003 — Soft Head Returns](episodes/E003.md), [E004 — The Oil Demon](episodes/E004.md), [E005 — Goblincide](episodes/E005.md), [E006 — Start your engines!](episodes/E006.md), [E007 — Bok Bok Keeping It Fresh](episodes/E007.md), and [E008 — Stupid Gnomes!](episodes/E008.md), [E009 — Surfacing](episodes/E009.md), [E010 — Shackles](episodes/E010.md), [E011 — Kick me as hard as you can](episodes/E011.md), and [E012 — Work Hours](episodes/E012.md). These are reference dossiers, **not publishable reader transcripts**, drawn from processed Parakeet SRTs; audio accuracy, names, and speaker assignments still need verification. E008 features guest players/characters, not substitute actors for the absent regular performers. See the [expanded chronology](world/CHRONOLOGY.md), [characters](world/CHARACTERS.md), [places](world/PLACES.md), and [consistency ledger](world/CONSISTENCY_LEDGER.md). See the [expanded chronology](world/CHRONOLOGY.md), [characters](world/CHARACTERS.md), [places](world/PLACES.md), and [consistency ledger](world/CONSISTENCY_LEDGER.md).

## New segmentation benchmark (2026-10-21)

[Five controlled CrispASR/Parakeet runs on E001's first ten minutes](reports/PARAKEET_SEGMENTATION_2026-10-21.md) cover no VAD, default Silero VAD, 700 ms padding, overlapping 30 s chunks and a chunked deduplication-off test. The two chunked JSON and SRT pairs are **byte-identical**, and transcription disagreements are **not yet audio-verified**. The existing episode drafts were not replaced.

## Important distinctions

- **Multi-pass review tooling:** [usage and limitations](reports/MULTIPASS_PIPELINE.md),
  [measured export pilot](reports/MULTIPASS_PILOT_2026-10-21.md). Compare preserved
  Parakeet/Qwen outputs, inspect time-coded disagreements, generate targeted jobs,
  and retain reviewer decisions without rewriting these reader editions.

  ```powershell
  python -m unittest discover -s tests
  python tools/pilot_asr.py --out local/multipass-pilot
  ```

  Use a new output directory. This command compares E000/E001 exports only; it
  does not launch recognition or process the archive. Model agreement is not
  audio verification.

- The **reader-edited drafts** normalize source-supported spelling (e.g. Dusthill, Nash Maggard, Vorel, Jimster and Shun'ti) and the cast speaker name **Jon**, with every edit logged. They are still **not audio-proofread**; ambiguous speech such as “Orifi or Orify?” remains as recognized. The machine-derived drafts and all original SRTs stay unchanged.

- **Readable draft** means subtitle lines have been grouped into paragraphs with named speakers and approximate timestamps. It does **not** mean every word or speaker boundary was checked against audio.
- The text source for these drafts is the supplied **post-processed Parakeet TDT 1.1B SRT**. The original unprocessed Parakeet output and other tested outputs are in [`sources/`](sources/), unchanged in content.
- Episode 1's numeric `speaker 5` is the same person as `speaker 0` (Scott, performing a voice), **verified by the archive owner**. This is a per-episode correction; don't generalize ID assignments to other episodes.
- Cohere's substantial omissions were **verified by listening** and its outputs are preserved for comparison only.
- The final spoken word of E000 is **“Now”**; the remaining audio is music. The processed Parakeet ending has unreliable timing, so the last cue is **not verified** even though the word is.
- The world's details are provisional reference entries. **A character's belief is not automatically objective world fact**, and uncertain spellings are deliberately flagged.

## Rebuild

Python 3.10+ is sufficient; the scripts use only the standard library.

```bash
python tools/build_transcripts.py
python tools/build_reader_editions.py
python -m unittest discover -s tests -p 'test_reader_editions.py'
python tools/audit_sources.py
# Optional: pip install rapidfuzz
python tools/evaluate_qwen_variants.py
```

The first command recreates the immutable machine-derived drafts; the second command recreates the *separate* wiki-spelling reader drafts and correction logs. Files produced by the first command: `transcripts/E000.readable-draft.md`, `transcripts/E001.readable-draft.md`, and `*.turns.json` containing original cue indexes for traceability. The second command creates `reports/SRT_AUDIT.md` and `reports/source_manifest.json`.

The original MP3 files are **not** bundled in the archive, to avoid duplicating the large uploads. The manifest records their SHA-256 digests and file sizes when they were available to build the pilot. Keep them in a separately backed-up, read-only audio collection.

## Production definition of done (per episode)

An episode is *drafted* after automatic transcription and readable rendering, but is *reviewed* only after checking flagged omissions, proper nouns, speaker IDs, beginning/end speech boundaries, broken cue boundaries, and audio-linked uncertain sections. This package is at the **drafted** milestone.

## Additional ASR tests (2026-10-21)

Six further **raw Qwen variants** are preserved under `sources/`. See [comparison](reports/QWEN_VARIANTS_2026-10-21.md) for exact-text results, timing-validity findings and discrepancies worth checking against audio. Neither the existing readable drafts nor the world reference were silently rewritten from these competing model outputs. This repository is the canonical project home; external fan-wiki and end-of-campaign character-sheet references are governed by the [external sources policy](project/EXTERNAL_REFERENCES.md).


## Newly archived visual references (2026-10-21)

The archive owner added **85 WebP images** downloaded from the fan wiki to [`sources/images/`](sources/images/). They are now indexed in the [image provenance and editorial register](project/IMAGE_ASSETS.md). Most are fan art or undated image assets; the two-page **Fate 4 vehicle design** explicitly credits **Kristen Ashton** and can inform E006–E010 vehicle references. The **Beyond the Deadfingers** regional map contains names including Dusthill and Slavetown, but may include **later campaign annotations**. Neither this map nor the **Teet** map is confirmed to be the exact player-facing map discussed in early episodes.

**Important:** Fandom's wiki-text license does **not** automatically license images. Original file-description pages, authors, individual media permissions and upload dates still require verification before public distribution. Visual corroboration never counts as **audio verification** of ASR output. The supplied image binaries and original SRTs have not been changed.

