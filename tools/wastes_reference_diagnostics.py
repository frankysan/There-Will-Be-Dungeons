"""Bounded read-only Wastes Markdown diagnostics. Findings are not canon or browser proof."""
from __future__ import annotations
import argparse
from collections import Counter
import html
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

LINK = re.compile(r"\[[^\]\n]+\]\((<[^>\n]+>|[^)\n]+)\)")
NOTE = re.compile(r"\[\^([^\]\n]+)\]")
DEF = re.compile(r"^\[\^([^\]\n]+)\]:", re.M)
HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$", re.M)
RAW_ID = re.compile(r'\b(?:id|name)=["\x27]([^"\x27]+)["\x27]')
SUBJECTS = {"characters", "places", "technology", "creatures", "races"}
# Do not indirectly scan files whose separate workspace rendering/lint checks were restricted.
RESTRICTED = {"world/CONSISTENCY_LEDGER.md", "world/characters/bok-bok.md"}
NAMES = {
    "the Principle": re.compile(r"\bthe Principle\b", re.I),
    "Kervalon": re.compile(r"\bKervalon\b", re.I),
    "Tietkalla": re.compile(r"\bTietkalla\b", re.I),
    "Mask of Elton IV": re.compile(r"\bMask of Elton IV\b", re.I),
}
CLAIMS = {
    "unused Ruby": re.compile(r"\b(?:Ruby|Triangulosphere)\b.{0,45}\b(?:never activated|still unactivated)\b", re.I),
    "unbanished Worldbreaker": re.compile(r"\bWorldbreaker\b.{0,45}\b(?:still on Earth|remains on Earth)\b", re.I),
    "rebuilt Tietkalla": re.compile(r"\bT['’]?ietkalla\b.{0,45}\b(?:fully|completely)\s+rebuilt\b", re.I),
}

def slug(text: str) -> str:
    """Conservative GitHub-style approximation, not actual native browser proof."""
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]+>", "", html.unescape(text)).lower().strip()
    return re.sub(r"[^\w\- ]", "", text.replace(chr(96), "")).replace(" ", "-")

def heading_ids(text: str) -> set[str]:
    seen: Counter[str] = Counter()
    ids: set[str] = set(RAW_ID.findall(text))
    for m in HEADING.finditer(text):
        key = slug(m.group(1))
        n = seen[key]
        seen[key] += 1
        ids.add(key if n == 0 else f"{key}-{n}")
    return ids

def scan(root: Path, domains: tuple[str, ...] = ("world",), max_files: int = 200,
         max_bytes: int = 450000, max_links: int = 12000, max_findings: int = 600) -> dict:
    """Read-only and bounded. Report issues as review candidates, not verified errors."""
    root = root.resolve()
    files: list[Path] = []
    for domain in domains:
        base = (root / domain).resolve()
        if base.is_relative_to(root) and base.is_dir():
            files.extend(p for p in base.rglob("*.md")
                         if not p.is_symlink() and p.resolve().is_relative_to(root))
    files = sorted(set(files))
    restricted_found = sorted(p.relative_to(root).as_posix() for p in files
                              if p.relative_to(root).as_posix() in RESTRICTED)
    files = [p for p in files if p.relative_to(root).as_posix() not in RESTRICTED]
    report = dict(files_discovered=len(files) + len(restricted_found), files_scanned=0, links_checked=0,
                  links_skipped=0, scope=list(domains), findings=[], limits=[],
                  disclaimer="Heuristic static checks; no audio, canon or native-browser verification.")
    if restricted_found:
        report["limits"].append("Capability-restricted source pages excluded: "
                                + ", ".join(restricted_found))
    cache: dict[Path, set[str]] = {}

    def flag(kind: str, level: str, path: Path, line: int, detail: str) -> None:
        if len(report["findings"]) >= max_findings:
            if "findings cap" not in report["limits"]:
                report["limits"].append("findings cap")
            return
        report["findings"].append(dict(kind=kind, level=level,
                                       file=path.relative_to(root).as_posix(),
                                       line=line, detail=detail))

    if len(files) > max_files:
        report["limits"].append(f"{len(files) - max_files} files over cap")
    for path in files[:max_files]:
        if path.stat().st_size > max_bytes:
            report["limits"].append(f"size cap: {path.relative_to(root)}")
            continue
        source = path.read_text(encoding="utf-8-sig")
        report["files_scanned"] += 1
        defs = {m.group(1) for m in DEF.finditer(source)}
        refs = {m.group(1) for m in NOTE.finditer(DEF.sub("", source))}
        for label in sorted(refs - defs):
            flag("missing_footnote_definition", "structural", path, 1, label)
        for m in DEF.finditer(source):
            if m.group(1) not in refs:
                flag("unused_footnote_definition", "review", path,
                     source.count("\n", 0, m.start()) + 1, m.group(1))
        if path.parent.name in SUBJECTS and path.parent.parent.name == "world":
            if not re.search(r"^#{2,3}\s+(?:Current status|Lasting legacy)\b", source, re.I | re.M):
                flag("missing_final_status", "review", path, 1, "No Current status / Lasting legacy heading")
        body = re.split(r"^## (?:Sources and project notes|Research notes)\s*$",
                        source, maxsplit=1, flags=re.I | re.M)[0]
        for line_no, line in enumerate(body.splitlines(), 1):
            if line.startswith("[^") or line.startswith("    ") or line.startswith(chr(96) * 3):
                continue
            plain = re.sub(r"\]\([^)]*\)", "]()", line)
            # Original word-form arc editions are deliberately frozen historical text.
            historical_arc = (path.parent.name == "narrative" and
                              re.fullmatch(r"ARC_[A-Z]+\.md", path.name) is not None)
            if not historical_arc:
                for key, pattern in NAMES.items():
                    if pattern.search(plain):
                        flag("canonical_name_candidate", "review", path, line_no, key)
            for key, pattern in CLAIMS.items():
                if pattern.search(plain):
                    flag("finale_claim_candidate", "review", path, line_no, key)
        for m in LINK.finditer(source):
            if report["links_checked"] >= max_links:
                report["links_skipped"] += 1
                continue
            raw = m.group(1).strip()
            dest = raw[1:].split(">", 1)[0] if raw.startswith("<") else raw.split(' "', 1)[0].split(" '", 1)[0]
            parsed = urlsplit(dest)
            if parsed.scheme or parsed.netloc or dest.startswith("//"):
                continue
            report["links_checked"] += 1
            line = source.count("\n", 0, m.start()) + 1
            target = ((path.parent / unquote(parsed.path)) if parsed.path else path).resolve()
            if not target.is_relative_to(root):
                flag("outside_repository_link", "structural", path, line, dest)
            elif not target.exists():
                flag("missing_link_target", "structural", path, line, dest)
            elif parsed.fragment and target.suffix.lower() == ".md":
                if target.relative_to(root).as_posix() in RESTRICTED:
                    flag("restricted_fragment_target", "review", path, line, dest)
                    continue
                if target.stat().st_size > max_bytes:
                    flag("large_fragment_target", "review", path, line, dest)
                    continue
                if target not in cache:
                    cache[target] = heading_ids(target.read_text(encoding="utf-8-sig"))
                if unquote(parsed.fragment) not in cache[target]:
                    flag("fragment_candidate", "review", path, line, dest)
    report["counts"] = dict(sorted(Counter(x["kind"] for x in report["findings"]).items()))
    report["complete_within_limits"] = not report["limits"] and report["links_skipped"] == 0
    return report

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--domain", choices=("world", "wastes", "narrative"), action="append")
    parser.add_argument("--max-files", type=int, default=200)
    parser.add_argument("--max-bytes", type=int, default=450000)
    parser.add_argument("--max-links", type=int, default=12000)
    parser.add_argument("--max-findings", type=int, default=600)
    parser.add_argument("--sample-per-kind", type=int, default=3)
    args = parser.parse_args()
    if min(args.max_files, args.max_bytes, args.max_links, args.max_findings) < 1 or args.sample_per_kind < 0:
        parser.error("All bounds must be positive")
    report = scan(Path(__file__).resolve().parents[1], tuple(args.domain or ("world",)),
                  args.max_files, args.max_bytes, args.max_links, args.max_findings)
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(f"{report['files_scanned']}/{report['files_discovered']} files; "
              f"{report['links_checked']} links; {len(report['findings'])} findings")
        for kind, value in report["counts"].items():
            print(f"  {kind}: {value}")
        shown: Counter[str] = Counter()
        for item in report["findings"]:
            if shown[item["kind"]] >= args.sample_per_kind:
                continue
            shown[item["kind"]] += 1
            print(f"  REVIEW {item['kind']} {item['file']}:{item['line']} - {item['detail']}")
        for item in report["limits"]:
            print(f"LIMIT: {item}")
        print("No files changed. Findings require human/source review.")

if __name__ == "__main__":
    main()
