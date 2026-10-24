#!/usr/bin/env python3
"""Prepare one complete SRT episode for bounded, resumable, ASR-only research.

Produces compact source/metric summaries, timed primary-text windows, and
optional heuristic two-export disagreement candidates. Does not edit inputs,
run recognition, listen to audio, or make canon decisions.

Example:
  python tools/prepare_episode.py --id E121 \
    --primary "sources/The Wastes S1E121. The Heart of The Matter.parakeet.processed.srt" \
    --secondary "sources/The Wastes S1E121. The Heart of The Matter.qwen-q8.canary-ctc.nemotron.srt" \
    --out local/episode-analysis/E121
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path
import re
import tempfile

from asr_alignment import align
from asr_evidence import TOKEN, Word, normalized
from asr_metrics import distance, tokens
from audit_sources import sha256
from build_transcripts import parse_srt

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = 1


def stamp(ms: int | float) -> str:
    seconds, millis = divmod(int(ms), 1000)
    hours, rem = divmod(seconds, 3600)
    minutes, seconds = divmod(rem, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}.{millis:03}"


def readable_path(path: Path) -> str:
    """Never write absolute workstation locations to generated evidence."""
    try:
        return path.resolve().relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        return path.name


def source(path: Path):
    """Parse every cue and keep the export's structural/provenance metadata."""
    cues = parse_srt(path)
    if not cues:
        raise ValueError(f"Empty SRT: {path.name}")
    if any(b.start < a.start for a, b in zip(cues, cues[1:])):
        raise ValueError(f"Nonchronological SRT cues: {path.name}")
    lexical = tokens(" ".join(c.text for c in cues))
    if not lexical:
        raise ValueError(f"No recognized words: {path.name}")
    invalid = sum(c.end <= c.start for c in cues)
    overlaps = sum(b.start < a.end for a, b in zip(cues, cues[1:]))
    summary = {
        "path": readable_path(path),
        "filename": path.name,
        "label_provenance": "filename only; ASR settings and acoustic source unverified",
        "bytes": path.stat().st_size,
        "sha256": sha256(path),
        "cue_count": len(cues),
        "first_cue_start_ms": cues[0].start,
        "last_cue_end_ms": max(c.end for c in cues),
        "normalized_token_count": len(lexical),
        "invalid_duration_cues": invalid,
        "overlapping_cue_pairs": overlaps,
    }
    return summary, cues, lexical


def alignment_words(cues):
    """Attach the existing alignment's cue-level timing (not word timestamps)."""
    words = []
    for cue in cues:
        for match in TOKEN.finditer(cue.text):
            words.append(Word(
                f"w{len(words)}", match.group(), normalized(match.group())[0],
                str(cue.idx), match.start(), match.end(), cue.start, cue.end,
                "cue", cue.speaker,
            ))
    return words


def disagreement_candidates(primary_cues, secondary_cues):
    """Heuristic time-aware comparison, independent of exact global distance."""
    a = alignment_words(primary_cues)
    b = alignment_words(secondary_cues)
    operations, stats = align(a, b)
    if [w.id for _, left, _, _ in operations for w in left] != [w.id for w in a]:
        raise RuntimeError("Alignment dropped or reordered primary words")
    if [w.id for _, _, right, _ in operations for w in right] != [w.id for w in b]:
        raise RuntimeError("Alignment dropped or reordered secondary words")
    groups = []
    for kind, left, right, notes in operations:
        key = (kind, bool(left), bool(right), tuple(notes))
        if groups and groups[-1][0] == key:
            groups[-1][1].extend(left)
            groups[-1][2].extend(right)
        else:
            groups.append((key, list(left), list(right)))
    candidates = []
    for (kind, _, _, notes), left, right in groups:
        if kind == "agreement" and not notes:
            continue
        words = left + right
        starts = [w.start_ms for w in words if w.start_ms is not None]
        ends = [w.end_ms for w in words if w.end_ms is not None]
        if not starts or not ends:
            raise RuntimeError("Untimed candidate from timestamped SRT source")
        primary_text = " ".join(w.text for w in left)
        secondary_text = " ".join(w.text for w in right)
        risky_negation = bool(re.search(
            r"\b(?:not|no|never|cant|cannot|wont|wouldnt|didnt|dont|isnt|wasnt)\b",
            (primary_text + " " + secondary_text).lower().replace("'", "").replace("’", "")
        ))
        score = (
            (3 if kind in ("possible_omission", "conflicting_recognition") else 1)
            + min(3, max(len(left), len(right)) // 5)
            + (2 if risky_negation else 0)
            + (1 if notes else 0)
        )
        candidates.append({
            "id": f"d{len(candidates) + 1:05}",
            "classification": kind,
            "review_score_heuristic": score,
            "start_ms": min(starts),
            "end_ms": max(ends),
            "primary": primary_text,
            "secondary": secondary_text,
            "primary_cue_ids": list(dict.fromkeys(w.segment_id for w in left)),
            "secondary_cue_ids": list(dict.fromkeys(w.segment_id for w in right)),
            "diagnostics": list(notes),
            "timing_precision": "SRT cue intervals, not word-aligned",
            "audio_verified": False,
        })
    return candidates, stats


def primary_windows(cues, window_ms: int):
    buckets = defaultdict(list)
    for cue in cues:
        buckets[cue.start // window_ms].append(cue)
    result = []
    for index, selected in sorted(buckets.items()):
        start, end = index * window_ms, (index + 1) * window_ms
        filename = f"windows/{stamp(start).replace(':', '-')}_{stamp(end).replace(':', '-')}.md"
        lines = [
            f"# Primary ASR — {stamp(start)}–{stamp(end)}",
            "",
            "> Machine-recognized text only; cue timestamps, not audio-verified wording.",
            "> Cues are assigned to the window containing their start; some may extend beyond it.",
            "",
        ]
        for cue in selected:
            lines.append(
                f"- [{stamp(cue.start)}–{stamp(cue.end)}] "
                f"(cue {cue.idx}, {cue.speaker}): {cue.text}"
            )
        result.append((
            filename,
            "\n".join(lines) + "\n",
            {
                "file": filename,
                "window_start_ms": start,
                "window_end_ms": end,
                "cue_count": len(selected),
                "first_cue_id": selected[0].idx,
                "last_cue_id": selected[-1].idx,
                "last_cue_end_ms": max(c.end for c in selected),
            },
        ))
    if sum(item[2]["cue_count"] for item in result) != len(cues):
        raise RuntimeError("Incomplete primary SRT window coverage")
    return result


def short_text(value: str, limit: int = 115) -> str:
    value = value.replace("|", "\\|").replace("\n", " ")
    return value if len(value) <= limit else value[:limit - 1] + "…"


def markdown_summary(record, candidates, review_limit):
    src = record["sources"]
    lines = [
        f"# Episode preparation — {record['episode']}",
        "",
        "> Provisional ASR text evidence. No audio listening, source verification or "
        "canon determination performed.",
        "",
        "## Source inventory",
        "",
        "| Export | Filename | Cues | Normalized words | First cue | Final cue | SHA-256 |",
        "| --- | --- | ---: | ---: | --- | --- | --- |",
    ]
    for index, item in enumerate(src):
        role = "Primary" if index == 0 else "Secondary"
        lines.append(
            f"| {role} | {short_text(item['filename'], 90)} | {item['cue_count']} | "
            f"{item['normalized_token_count']} | {stamp(item['first_cue_start_ms'])} | "
            f"{stamp(item['last_cue_end_ms'])} | {item['sha256']} |"
        )
    lines += ["", "Labels inferred from filenames only. Exact acoustic-input identity is unverified.", ""]
    metric = record["metric"]
    if metric:
        lines += [
            "## Whole-export inter-ASR metric",
            "",
            f"**{metric['ordered_word_edits']} exact ordered edits / "
            f"{metric['primary_normalized_tokens']} primary normalized tokens "
            f"= {metric['disagreement_percent']:.2f}% inter-ASR text disagreement.**",
            "",
            "This is **not WER**, measured recognition accuracy, or confirmed missing/invented speech.",
            "Candidate alignment uses a different normalization and is **not** this distance.",
            "",
        ]
    lines += [
        "## Primary transcript windows",
        "",
        "Read every window before making full-recording narrative claims; "
        "window extraction is complete, but editorial review is not.",
        "",
    ]
    for window in record["windows"]:
        lines.append(
            f"- [{stamp(window['window_start_ms'])}–{stamp(window['window_end_ms'])}]"
            f"({window['file']}) — {window['cue_count']} cues"
        )
    if record["alignment_statistics"] is not None:
        lines += ["", "## Prioritized ASR disagreements (heuristics only)", ""]
        lines.append(
            f"{len(candidates)} groups in candidates.json; displaying up to {review_limit}. "
            "Review both readings against audio before deciding which is correct."
        )
        lines += ["", "| Time / ID | Kind | Primary | Secondary |", "| --- | --- | --- | --- |"]
        ranked = sorted(candidates, key=lambda c: (-c["review_score_heuristic"], c["start_ms"]))
        for candidate in ranked[:review_limit]:
            lines.append(
                f"| {stamp(candidate['start_ms'])} {candidate['id']} | "
                f"{candidate['classification']} | {short_text(candidate['primary'])} | "
                f"{short_text(candidate['secondary'])} |"
            )
    lines += ["", "## Limits", "",
              "- Source exports are fully **parsed**, not automatically fully **reviewed**.",
              "- Similar SRT clocks/hashes do not verify identical original audio.",
              "- No inferred speaker/word timing is treated as audio-confirmed.",
              "- Generated files may be reused only when their source hashes and options match.", ""]
    return "\n".join(lines)


def prepare(episode: str, primary: Path, out: Path, secondary: Path | None = None,
            window_minutes: int = 10, review_limit: int = 30, do_alignment: bool = True):
    if not 1 <= window_minutes <= 60:
        raise ValueError("Window size must be 1–60 minutes")
    if not 1 <= review_limit <= 200:
        raise ValueError("Review limit must be 1–200")
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*", episode):
        raise ValueError("Episode ID must be a portable label")
    primary, out = Path(primary).resolve(), Path(out).resolve()
    secondary = Path(secondary).resolve() if secondary is not None else None
    if not primary.is_file() or (secondary is not None and not secondary.is_file()):
        raise FileNotFoundError("Input SRT file unavailable")
    if out in (primary, secondary) or out in primary.parents or (
        secondary is not None and out in secondary.parents
    ):
        raise ValueError("Output directory must not contain input sources")
    if secondary == primary:
        raise ValueError("The same SRT cannot be both exports")

    info_a, cues_a, tokens_a = source(primary)
    records = [info_a]
    metric = None
    candidates = []
    alignment_stats = None
    if secondary:
        info_b, cues_b, tokens_b = source(secondary)
        if info_a["sha256"] == info_b["sha256"]:
            raise ValueError("Identical exports do not supply an independent text comparison")
        records.append(info_b)
        edits = distance(tokens_a, tokens_b)
        metric = {
            "method": "exact unit-cost whole-sequence ordered word Levenshtein",
            "normalization": "lowercase; delete straight/curly apostrophes; split on non-Unicode alphanumeric",
            "ordered_word_edits": edits,
            "primary_normalized_tokens": len(tokens_a),
            "secondary_normalized_tokens": len(tokens_b),
            "disagreement_percent": 100.0 * edits / len(tokens_a),
            "is_wer": False,
        }
        if do_alignment:
            candidates, alignment_stats = disagreement_candidates(cues_a, cues_b)

    windows = primary_windows(cues_a, window_minutes * 60000)
    record = {
        "schema": SCHEMA,
        "episode": episode,
        "evidence_level": "ASR-only; not listened to",
        "audio_verified": False,
        "shared_audio_identity_verified": False,
        "options": {
            "window_minutes": window_minutes,
            "review_limit": review_limit,
            "do_alignment": do_alignment,
        },
        "sources": records,
        "metric": metric,
        "alignment_statistics": alignment_stats,
        "candidate_count": len(candidates) if alignment_stats is not None else None,
        "candidate_classifications": (
            dict(sorted(Counter(c["classification"] for c in candidates).items()))
            if alignment_stats is not None else None
        ),
        "windows": [item[2] for item in windows],
        "artifacts": ["summary.json", "summary.md"]
                     + ([ "candidates.json" ] if alignment_stats is not None else [])
                     + [item[0] for item in windows],
    }

    # Reuse only a complete matching preparation. Never replace an existing
    # different run's generated outputs or consume existing user files.
    manifest = out / "summary.json"
    if out.exists() and any(out.iterdir()):
        if manifest.is_file():
            previous = json.loads(manifest.read_text(encoding="utf-8"))
            if previous == record and all((out / item).is_file() for item in record["artifacts"]):
                return record, True
        raise FileExistsError(f"Output exists with different/incomplete evidence: {out.name}")

    out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=f".{out.name}-", dir=out.parent) as temp:
        staging = Path(temp)
        for rel, body, _ in windows:
            target = staging / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(body, encoding="utf-8", newline="\n")
        if alignment_stats is not None:
            (staging / "candidates.json").write_text(
                json.dumps(candidates, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8", newline="\n",
            )
        (staging / "summary.md").write_text(
            markdown_summary(record, candidates, review_limit), encoding="utf-8", newline="\n",
        )
        (staging / "summary.json").write_text(
            json.dumps(record, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8", newline="\n",
        )
        if sha256(primary) != info_a["sha256"] or (
            secondary is not None and sha256(secondary) != records[1]["sha256"]
        ):
            raise RuntimeError("Input source changed during preparation; discard this run")
        if out.exists():
            out.rmdir()  # only an empty directory is allowed
        staging.rename(out)
    return record, False


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--id", required=True, help="Corrected, campaign-qualified episode ID")
    parser.add_argument("--primary", required=True, type=Path, help="Primary complete SRT export")
    parser.add_argument("--secondary", type=Path, help="Optional independent second SRT")
    parser.add_argument("--out", required=True, type=Path, help="Fresh output directory (prefer local/)")
    parser.add_argument("--window-minutes", type=int, default=10)
    parser.add_argument("--max-review", type=int, default=30)
    parser.add_argument("--no-alignment", action="store_true", help="Exact distance still computed")
    args = parser.parse_args()
    record, cached = prepare(
        args.id, args.primary, args.out, args.secondary, args.window_minutes,
        args.max_review, not args.no_alignment,
    )
    label = "Reused" if cached else "Prepared"
    count = record['candidate_count']
    candidate_label = str(count) if count is not None else 'not computed'
    print(f"{label} {record['episode']}: {len(record['windows'])} primary windows; "
          f"{record['sources'][0]['cue_count']} primary cues; "
          f"{candidate_label} comparison candidates")
    if record["metric"]:
        print(f"Exact inter-ASR distance: {record['metric']['ordered_word_edits']} / "
              f"{record['metric']['primary_normalized_tokens']} = "
              f"{record['metric']['disagreement_percent']:.2f}% (not WER)")
    print(f"Outputs: {args.out / 'summary.md'} and {args.out / 'summary.json'}")


if __name__ == "__main__":
    main()
