#!/usr/bin/env python3
"""Render speaker-labelled, paragraph-form Markdown from chosen SRT inputs.

Deliberately does not rewrite words, fix names, or infer dialogue. Only reflows
whitespace and groups temporally adjacent cues of the same labelled speaker.
"""
from __future__ import annotations
import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = {
    "E000": {"title": "Introductions", "input": "E000.parakeet.processed.srt", "raw": "E000.parakeet.raw.srt"},
    "E001": {"title": "The Campaign Begins!", "input": "E001.parakeet.processed.srt", "raw": "E001.parakeet.raw.srt"},
}
# Episode-specific mappings, never assume numeric IDs persist across episodes.
LABEL_MAP = {
    "E000": {"speaker 0": "Scott", "speaker 1": "Beau", "speaker 2": "Kristen", "speaker 3": "John", "speaker 4": "Kyle"},
    "E001": {"speaker 0": "Scott", "speaker 1": "Beau", "speaker 2": "Kristen", "speaker 3": "Kyle", "speaker 4": "John", "speaker 5": "Scott"},
}

@dataclass
class Cue:
    idx: int
    start: int
    end: int
    speaker: str
    text: str


def msec(raw: str) -> int:
    m = re.fullmatch(r"(\d\d):(\d\d):(\d\d)[,.](\d\d\d)", raw.strip())
    if not m:
        raise ValueError(f"Unparseable timestamp: {raw!r}")
    h, mi, s, ms = (int(x) for x in m.groups())
    return ((h * 60 + mi) * 60 + s) * 1000 + ms


def parse_srt(path: Path) -> list[Cue]:
    content = path.read_text(encoding="utf-8-sig").replace("\r\n", "\n")
    entries = re.split(r"\n\s*\n", content.strip())
    cues: list[Cue] = []
    for block in entries:
        ls = block.strip().splitlines()
        if len(ls) < 3:
            raise ValueError(f"Invalid SRT block in {path}: {block[:80]!r}")
        idx = int(ls[0].strip())
        start_str, end_str = re.split(r"\s*-->\s*", ls[1])
        text = " ".join(x.strip() for x in ls[2:]).strip()
        mo = re.match(r"^\(([^)]+)\)\s*", text)
        speaker = mo.group(1) if mo else "Unknown"
        if mo:
            text = text[mo.end():]
        text = re.sub(r"\s+", " ", text).strip()
        cues.append(Cue(idx, msec(start_str), msec(end_str), speaker, text))
    return cues


def clock(ms: int, include_hours: bool = True) -> str:
    sec = int(ms // 1000)
    h, rem = divmod(sec, 3600)
    mi, s = divmod(rem, 60)
    return f"{h:02}:{mi:02}:{s:02}" if include_hours else f"{mi:02}:{s:02}"


def display_name(episode: str, label: str) -> str:
    if label in LABEL_MAP[episode]:
        return LABEL_MAP[episode][label]
    if episode == "E001" and label in ("speaker 5", "Unidentified"):
        return "Scott"
    return label


def group_turns(episode: str, cues: list[Cue], target_words=90, hard_words=240, gap_ms=4000) -> list[dict]:
    """Prefer paragraph boundaries at sentence ends; never edit the words themselves."""
    turns: list[dict] = []
    for c in cues:
        sp = display_name(episode, c.speaker)
        if not c.text:
            continue
        can_join = bool(turns and turns[-1]["speaker"] == sp and
                        c.start - turns[-1]["end_ms"] <= gap_ms)
        if can_join:
            prev = turns[-1]
            nwords = len(prev["text"].split())
            if nwords >= hard_words or (nwords >= target_words and
               re.search(r"[.!?][\"'’)]?$", prev["text"])):
                can_join = False
        if can_join:
            prev = turns[-1]
            prev["text"] += " " + c.text
            prev["end_ms"] = max(prev["end_ms"], c.end)
            prev["last_cue"] = c.idx
        else:
            turns.append({"speaker": sp, "start_ms": c.start, "end_ms": c.end, "first_cue": c.idx,
                          "last_cue": c.idx, "text": c.text})
    return turns


def render(episode: str):
    meta = FILES[episode]
    src = ROOT / "sources" / meta["input"]
    cues = parse_srt(src)
    turns = group_turns(episode, cues)
    sections = []
    cur_section = None
    for t in turns:
        n = t["start_ms"] // (10 * 60 * 1000)
        if n != cur_section:
            cur_section = n
            a, b = n * 10 * 60 * 1000, (n + 1) * 10 * 60 * 1000
            sections.append(f"\n## {clock(a)}–{clock(b)}\n")
        # Preserve speech text exactly apart from rewrapping existing SRT line breaks.
        if episode == "E000" and t["last_cue"] == cues[-1].idx and t["first_cue"] == cues[-1].idx:
            stamp = "timestamp unreliable; source SRT says 00:13:20"
        else:
            stamp = clock(t["start_ms"])
        sections.append(f"**{t['speaker']}** *[{stamp}]*: {t['text']}\n")
    header = (
        f"# {episode} — {meta['title']}\n\n"
        f"> **Status: machine-generated readable draft — not a verified transcript.** "
        f"Uses the supplied *post-processed Parakeet SRT* as its text source, reflowing subtitles into "
        f"speaker-labelled paragraphs. It does **not** independently fix transcription errors, punctuation, "
        f"speaker boundaries or timing. The original raw Parakeet output and other model versions remain in `sources/`.\n\n"
        f"**Speaker normalization:** For E001 only, `speaker 5` is labelled **Scott**, "
        f"based on the listener-confirmed character voice. This does not alter source SRT files. "
        f"Timestamps refer to approximate audio positions.\n\n"
    ) if episode == "E001" else (
        f"# {episode} — {meta['title']}\n\n"
        f"> **Status: machine-generated readable draft — not a verified transcript.** "
        f"Based on the supplied *post-processed Parakeet SRT*; cues have been reflowed into paragraphs "
        f"without lexical correction. The unprocessed SRT is preserved under `sources/`.\n\n"
        f"**Listener-verified ending:** “Now” is the final spoken word; the remainder is music. "
        f"Do not extend spoken-word timings into the outro.\n\n"
    )
    out = ROOT / "transcripts" / f"{episode}.readable-draft.md"
    out.write_text(header + "\n".join(sections).rstrip() + "\n", encoding="utf-8", newline="\n")
    jpath = ROOT / "transcripts" / f"{episode}.turns.json"
    jpath.write_text(json.dumps({"episode": episode, "source_srt":meta["input"], "status":"unverified-machine-draft",
                                "note":"Adjacent cues grouped, speaker labels normalized; no lexical corrections.","turns": turns},
                                ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    return {"episode":episode,"cues":len(cues),"turns":len(turns),"words":sum(len(t["text"].split()) for t in turns),
            "last_cue_end":clock(max(c.end for c in cues)),"outfile":str(out.relative_to(ROOT))}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("episodes", nargs="*", default=None, choices=list(FILES))
    args = parser.parse_args()
    for episode in (args.episodes or list(FILES)):
        print(render(episode))
