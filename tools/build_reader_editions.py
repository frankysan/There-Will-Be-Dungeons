#!/usr/bin/env python3
"""Build wiki-spelling-normalized reader drafts from immutable machine-readable drafts.

This is an editorial *layer*. Never rewrite SRT sources or the machine drafts.
A match is corrected only if it appears in a timed speaker turn. Ambiguous
recognition text (for example "Orifi or Orify?") is deliberately left intact.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EPISODES = ("E000", "E001")
WIKI = "https://twbd.fandom.com/wiki/There_Will_Be_Dungeons_Wiki"
EP6 = "https://twbd.fandom.com/wiki/Episode_6"
# Ordered substitutions. A source citation supports spelling, not audio accuracy.
RULES = (
    ("nash-surname", re.compile(r"\b(?:Magard|Maghard)\b"), "Maggard", WIKI),
    ("vorel-given", re.compile(r"\b(?:Borel|Varel|Vorell)\b"), "Vorel", WIKI),
    ("dusthill", re.compile(r"\bDust Hill\b"), "Dusthill", WIKI),
    ("jimster", re.compile(r"\b(?:Gimster|Gymster|gymster)\b"), None, EP6),
    ("shunti", re.compile(r"\bShun T\b"), "Shun'ti", EP6),
    ("jon-jagger", re.compile(r"\bJohn Jagger\b"), "Jon Jagger", WIKI),
)
TURN = re.compile(r"^\*\*([^*]+)\*\* \*\[([^\]]+)\]\*: (.*)$")
SECTION = "## 00:00:00–00:10:00"


def git_blob_sha(content: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(content)).encode() + b"\0" + content).hexdigest()


def render_reader(episode: str, source: str) -> tuple[str, dict]:
    if episode not in EPISODES:
        raise ValueError(f"Unknown episode {episode}")
    source = source.replace("\r\n", "\n").replace("\r", "\n")
    source = re.sub(r"(?m)^[ \t]+$", "", source)
    source = re.sub(r"\n{3,}", "\n\n", source)
    lines = source.split("\n")
    if len(lines) < 3 or not lines[2].startswith("> **Status: machine-generated readable draft"):
        raise ValueError("Unexpected source draft header")
    original_status = lines[2]
    changes: list[dict] = []

    def process_line(line: str, line_no: int) -> str:
        match = TURN.fullmatch(line)
        if not match:
            return line
        speaker, timestamp, speech = match.groups()
        if speaker == "John":
            changes.append({"rule": "cast-speaker-jon", "field": "speaker",
                            "from": "John", "to": "Jon", "time": timestamp,
                            "source_line": line_no, "source_url": WIKI})
            speaker = "Jon"
        for rule_id, pattern, fixed, source_url in RULES:
            def substitute(hit: re.Match[str]) -> str:
                old = hit.group(0)
                replacement = (
                    ("jimster" if old[0].islower() else "Jimster")
                    if rule_id == "jimster" else fixed
                )
                assert replacement is not None
                changes.append({"rule": rule_id, "field": "speech",
                                "from": old, "to": replacement,
                                "time": timestamp, "source_line": line_no,
                                "source_url": source_url})
                return replacement
            speech = pattern.sub(substitute, speech)
        return f"**{speaker}** *[{timestamp}]*: {speech}"

    output = "\n".join(process_line(line, n) for n, line in enumerate(lines, 1))
    new_status = (
        f"> **Status: Reader-edited spelling draft; not listener-verified.** "
        f"Derived from the [machine-generated readable draft]({episode}.readable-draft.md). "
        "Only source-supported name spellings and the cast speaker label **Jon** "
        "have been standardized. All other recognized dialogue, timecodes and "
        "speaker boundaries remain from the underlying Parakeet draft; raw SRT "
        f"files are unchanged. Every edit is recorded in [the spelling log]({episode}.reader-edits.json)."
    )
    output = output.replace(original_status, new_status, 1)
    if SECTION not in output:
        raise ValueError(f"Missing first section in {episode}")
    note = (
        f"**Name reference:** [TWBD fan wiki]({WIKI}) "
        "(and [Episode 6](https://twbd.fandom.com/wiki/Episode_6) for Jimster and Shun'ti). "
        "These spellings are externally supported, but are not independent verification "
        "of dialogue. "
        + ("The ASR's “Orifi or Orify?” exchange is intentionally left unchanged pending listening review."
           if episode == "E001" else
           "The wiki's full names are available in the world reference; no new dialogue has been inserted.")
    )
    output = output.replace(SECTION, note + "\n\n" + SECTION, 1)
    counts: dict[str, int] = {}
    for edit in changes:
        counts[edit["rule"]] = counts.get(edit["rule"], 0) + 1
    log = {
        "schema_version": 1,
        "episode": episode,
        "source_machine_draft": f"transcripts/{episode}.readable-draft.md",
        "source_git_blob_sha": git_blob_sha(source.encode("utf-8")),
        "output_reader_draft": f"transcripts/{episode}.reader-draft.md",
        "verification": "wiki-spelling-supported; audio still unverified",
        "wiki_main_url": WIKI,
        "editing_rules": ("Only recognized proper names and speaker label Jon are normalized; "
                          "ambiguous phonetic dialogue is preserved."),
        "counts": counts,
        "edits": changes,
    }
    return output, log


def build(episode: str) -> tuple[str, int]:
    machine = ROOT / "transcripts" / f"{episode}.readable-draft.md"
    reader = ROOT / "transcripts" / f"{episode}.reader-draft.md"
    ledger = ROOT / "transcripts" / f"{episode}.reader-edits.json"
    output, log = render_reader(episode, machine.read_text(encoding="utf-8"))
    reader.write_text(output, encoding="utf-8", newline="\n")
    ledger.write_text(json.dumps(log, ensure_ascii=False, indent=2) + "\n",
                      encoding="utf-8", newline="\n")
    return episode, len(log["edits"])


if __name__ == "__main__":
    for ep in EPISODES:
        label, count = build(ep)
        print(f"{label}: {count} source-linked editorial substitutions")
