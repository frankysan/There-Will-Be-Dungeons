"""Private, read-only delta audit of a refreshed Discord research index.

Run only after tools/discord_archive.py ingest has finished. This script
does not open the original DHT files, download links, or publish source text.
Reports are stored only in ignored local/discord/.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit
import argparse
import hashlib
import json
import re
import sqlite3

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "local/discord/research.sqlite"
OUTPUT = ROOT / "local/discord/new-channels-audit"
ARCHIVE_ID = "623342794047619103"
CAST_NAMES = {"beauschwartz": "Beau", "jonjagger": "Jon",
              "frogpants": "Scott", "kyle_tarrasque": "Kyle",
              "kristenashton": "Kristen"}
KEYWORDS = re.compile(
    r"\b(wastes|wasteland|dusthill|slavetown|trashburg|teet|deadfingers|"
    r"fate[ -]?4|nash|stanley|hope|vorel|diontalus|tedna|ma storm|"
    r"dragonmetal|dragon heart|jimster|principle city|tylander|"
    r"catoblepraithe|solar mines|squirts|bok bok|delvers|inverse)\b",
    re.I,
)
RESOURCES = re.compile(
    r"\b(map|maps|art|artwork|portrait|image|drawing|illustration|"
    r"character sheet|handout|lore|notes|pdf|document|google|"
    r"background|guide|world map|floorplan|file|download|reference)\b",
    re.I,
)
URL = re.compile(r"https?://[^\s<>\[\]\(\)\{\}\"']+", re.I)


def read_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return None


def previous_downloads():
    saved_urls, filenames, hashes = set(), set(), set()
    for path in (ROOT / "local/downloads/manifest.private.json",
                 ROOT / "local/discord-downloads/manifest.json"):
        obj = read_json(path)
        if not obj:
            continue
        for entry in obj.get("assets", []) + obj.get("links", []) + obj.get("files", []):
            if entry.get("path") and entry.get("status", "saved") not in ("unavailable", "excluded"):
                if entry.get("url"):
                    saved_urls.add(entry["url"].split("?")[0])
                if entry.get("normalized_url"):
                    saved_urls.add(entry["normalized_url"].split("?")[0])
                filenames.add(Path(entry["path"]).name.split("--")[-1].casefold())
                if entry.get("sha256"):
                    hashes.add(entry["sha256"].lower())
    for folder in (ROOT / "local/downloads", ROOT / "local/images-wiki/maps",
                   ROOT / "sources/images"):
        if folder.is_dir():
            for file in folder.rglob("*"):
                if file.is_file():
                    filenames.add(file.name.casefold())
                    if folder == ROOT / "sources/images" or folder == ROOT / "local/images-wiki/maps":
                        h = hashlib.sha256()
                        with file.open("rb") as stream:
                            for block in iter(lambda: stream.read(1024 * 1024), b""):
                                h.update(block)
                        hashes.add(h.hexdigest())
    return saved_urls, filenames, hashes


def stamp(milliseconds):
    return datetime.fromtimestamp(milliseconds / 1000, tz=timezone.utc).isoformat()


def resource_type(link):
    host = urlsplit(link).netloc.lower()
    path = urlsplit(link).path.lower()
    if "docs.google.com" in host or "drive.google.com" in host:
        return "google-document"
    if "dndbeyond.com" in host or "ddb.ac" in host:
        return "character-sheet"
    if path.endswith((".pdf", ".docx", ".txt", ".zip", ".json")):
        return "document-download"
    if path.endswith((".png", ".webp", ".jpg", ".jpeg", ".gif", ".svg", ".mp4", ".wav", ".mp3")):
        return "media"
    if "discord" in host:
        return "discord-link"
    return "web-page"


def urls_for(payload):
    out = set(URL.findall(payload.get("text") or ""))
    for wrapper in payload.get("embeds", []):
        try:
            embed = json.loads(wrapper["json"])
        except (KeyError, TypeError, ValueError):
            continue
        if not isinstance(embed, dict):
            continue
        for prop in ("url", "thumbnail", "image", "video"):
            val = embed.get(prop)
            if isinstance(val, str) and val.startswith("http"):
                out.add(val)
            elif isinstance(val, dict) and isinstance(val.get("url"), str):
                out.add(val["url"])
    return sorted(url.rstrip(".,;:") for url in out)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index", type=Path, default=INDEX)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    output = args.output.resolve()
    if output.is_relative_to(ROOT.resolve()) and not output.is_relative_to((ROOT / "local").resolve()):
        parser.error("Private Discord-derived output must remain under local/")
    if not args.index.is_file():
        parser.error("Missing research index; ingest the archives first")
    c = sqlite3.connect(args.index.resolve().as_uri() + "?mode=ro", uri=True)
    c.row_factory = sqlite3.Row
    c.execute("PRAGMA query_only=ON")
    runs = [(int(r["id"]), json.loads(r["summary"])) for r in c.execute(
        "SELECT id,summary FROM runs WHERE summary IS NOT NULL ORDER BY id")]
    baseline = next(((rid, s) for rid, s in runs if s.get("messages") == 3708
                     and {e["channel_id"] for e in s.get("channel_scopes", [])} == {ARCHIVE_ID}), None)
    if not baseline or not runs:
        parser.error("Could not locate the verified 3,708-message baseline")
    current_id, current = runs[-1]
    if current_id == baseline[0] or len(current.get("channel_scopes", [])) <= 1:
        parser.error("The expanded archive has not yet been ingested. Run the documented ingest command first")
    old_hashes = {r["key"]: r["payload_hash"] for r in c.execute(
        "SELECT key,payload_hash FROM observations WHERE run_id=?", (baseline[0],))}
    new_hashes = {r["key"]: r["payload_hash"] for r in c.execute(
        "SELECT key,payload_hash FROM observations WHERE run_id=?", (current_id,))}
    old_keys, new_keys = set(old_hashes), set(new_hashes)
    new_only = new_keys - old_keys
    changed = {k for k in old_keys & new_keys if old_hashes[k] != new_hashes[k]}
    to_review = new_only | changed
    channel_stats = defaultdict(lambda: {"new_messages": 0, "changed_messages": 0,
                                        "first_utc": None, "last_utc": None,
                                        "attachment_count": 0, "external_links": 0})
    old_urls, old_names, old_hashes = previous_downloads()
    snapshot = current["snapshot_id"]
    assets = {r["normalized_url"]: dict(r) for r in c.execute(
        "SELECT normalized_url,blob_hash,actual_bytes,status FROM assets WHERE snapshot_id=?", (snapshot,))}
    candidates = []
    for row in c.execute("SELECT key,payload FROM messages ORDER BY timestamp,message_id"):
        if row["key"] not in to_review:
            continue
        p = json.loads(row["payload"])
        chan = p.get("channel", {}).get("name", p["channel_id"])
        author = p.get("author", {}).get("name", "")
        cast = CAST_NAMES.get(author)
        text = p.get("text") or ""
        timestamp = stamp(p["timestamp"])
        stats = channel_stats[chan]
        stats["new_messages" if row["key"] in new_only else "changed_messages"] += 1
        stats["first_utc"] = min(stats["first_utc"] or timestamp, timestamp)
        stats["last_utc"] = max(stats["last_utc"] or timestamp, timestamp)
        links = urls_for(p)
        att = p.get("attachments", [])
        stats["attachment_count"] += len(att)
        stats["external_links"] += len(links)
        context = bool(KEYWORDS.search(text))
        resource = bool(RESOURCES.search(text))
        for a in att:
            link = a.get("normalized_url") or a.get("download_url") or ""
            filename = a.get("name") or ""
            entry = assets.get(link) or {}
            saved_by_url = link.split("?")[0] in old_urls
            saved_by_hash = bool(entry.get("blob_hash") and entry["blob_hash"] in old_hashes)
            name_match = filename.casefold() in old_names
            candidates.append({
                "message_url": p["url"], "channel": chan, "date_utc": timestamp,
                "cast_attributed": cast, "kind": "attachment", "name": filename,
                "url": link, "downloaded_before": saved_by_hash or (saved_by_url and not entry.get("blob_hash")),
                "duplicate_evidence": "sha256" if saved_by_hash else "url-no-blob" if saved_by_url and not entry.get("blob_hash") else None,
                "filename_match_only": name_match,
                "blob_sha256": entry.get("blob_hash"), "blob_bytes": entry.get("actual_bytes"),
                "archive_blob_present": entry.get("blob_hash") is not None,
                "wastes_keyword": context, "resource_keyword": resource,
                "status": ("confirmed-byte-duplicate" if saved_by_hash else
                           "same-url-unmatched-hash" if saved_by_url and entry.get("blob_hash") else
                           "previously-saved-url-no-blob" if saved_by_url else "unreviewed-in-new-capture"),
            })
        for link in links:
            saved = link.split("?")[0] in old_urls
            candidates.append({
                "message_url": p["url"], "channel": chan, "date_utc": timestamp,
                "cast_attributed": cast, "kind": resource_type(link), "url": link,
                "downloaded_before": saved, "wastes_keyword": context,
                "resource_keyword": resource, "status": "previously-saved" if saved else "unverified-external",
            })
    priority = {"twbd-art": 5, "twbd-spoiler": 3, "dm-questions": 3,
                "bonus-show-questions": 2, "table-talk": 1,
                "make-monsters-community-event": 1}
    for item in candidates:
        item["priority_score"] = (priority.get(item["channel"], 0)
                                  + (4 if item["wastes_keyword"] else 0)
                                  + (3 if item["cast_attributed"] else 0)
                                  + (2 if item["resource_keyword"] else 0)
                                  + (3 if item["kind"] in ("attachment", "google-document", "document-download") else 0)
                                  - (15 if item["downloaded_before"] else 0))
    candidates.sort(key=lambda x: (-x["priority_score"], x["date_utc"], x["url"]))
    report = {"baseline_run": baseline[0], "current_run": current_id, "current_summary": current,
              "new_messages_vs_baseline": len(new_only), "changed_messages": len(changed),
              "previously_observed_messages_missing_from_current_capture": len(old_keys - new_keys),
              "channels": dict(sorted(channel_stats.items())),
              "candidate_count": len(candidates), "candidates": candidates,
              "policy": "PRIVATE research leads; cast-attributed is not authenticated authorship. No links fetched. Same filename is not proof of matching bytes."}
    output.parent.mkdir(parents=True, exist_ok=True)
    output.with_suffix(".json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = ["# Discord new-channel delta audit (private)", "",
             f"Baseline run: {baseline[0]}; current run: {current_id}.",
             f"New messages: **{len(new_only)}**; changed messages: **{len(changed)}**. Older messages absent from current capture: **{len(old_keys-new_keys)}** (not confirmed deletions).",
             f"Resource/URL occurrences: **{len(candidates)}**.", "",
             "## New-channel summary", "",
             "| Channel | New messages | Changed messages | Attachments | URL occurrences | First UTC | Last UTC |",
             "|---|---:|---:|---:|---:|---|"]
    for ch, s in sorted(channel_stats.items()):
        lines.append(f"| {ch} | {s['new_messages']} | {s['changed_messages']} | {s['attachment_count']} | {s['external_links']} | {s['first_utc']} | {s['last_utc']} |")
    lines += ["", "## Top unresolved resources (triage leads, not verified missing files)", ""]
    for item in [i for i in candidates if not i["downloaded_before"]][:100]:
        name = (item.get("name") or item["url"]).replace("|", "%7C")
        lines.append(f"- **{item['channel']} / {item['kind']}** (score {item['priority_score']}): {name} "
                     f"— [source]({item['message_url']}); attribution: {item['cast_attributed'] or 'not established'}; "
                     f"archived blob: {item.get('archive_blob_present', 'external link')}; "
                     f"filename match only: {item.get('filename_match_only', False)}")
    lines += ["", "Source text, cast IDs and private asset metadata remain in the JSON and local index.",
              "Neither a linked URL nor an archive blob establishes re-use rights or creator authorship.", ""]
    output.with_suffix(".md").write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({"report": str(output.with_suffix('.md')),
                      "new_messages": len(new_only), "channels": len(channel_stats),
                      "candidates": len(candidates)}, ensure_ascii=False))
    c.close()


if __name__ == "__main__":
    main()
