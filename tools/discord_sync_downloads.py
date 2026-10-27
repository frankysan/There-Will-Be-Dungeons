"""Incrementally export a DHT snapshot to private raw and curated downloads.

- Reads the already-verified, immutable snapshot created by discord_archive.py.
- Preserves existing paths and old byte variants; never alters the original DHT DBs.
- Restores ALL new cached downloads to local/discord-downloads/{attachments,other-media}.
- Copies a conservative, explicitly selected campaign subset to local/downloads.
- Records source URLs, Discord message provenance, exact content hashes and dates.
- --dry-run computes the plan without changing either directory.

Run from repository root:
    python tools/discord_sync_downloads.py --dry-run
    python tools/discord_sync_downloads.py
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from datetime import datetime, timezone
import hashlib
import json
import mimetypes
import os
from pathlib import Path
import re
import sqlite3
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "local/discord-downloads"
CURATED = ROOT / "local/downloads"
AUDIT = ROOT / "local/discord/new-channels-audit.json"

# Manual research leads. Folder assignment does not establish canonical design,
# authorship, episode correspondence or permission to redistribute.
CURATED_MESSAGES = {
    "669709591344316416": ("wastes", "Beau-attributed Known Wastes v3 map"),
    "638103354488127548": ("wastes", "Vorel Rage artwork lead"),
    "638103874078769248": ("wastes", "Stanley and Nash artwork leads"),
    "672186714638254090": ("wastes", "Nash visual evolution"),
    "738777012444856381": ("wastes", "Stanley season 1 visual reference"),
    "738777095118782495": ("wastes", "Stanley season 2 visual reference"),
    "761462415833038878": ("wastes", "Vorel screenshot"),
    "761462418051301387": ("wastes", "Hope screenshot"),
    "761462421486436363": ("wastes", "Nash screenshot"),
    "761767030457630720": ("wastes", "Cast/character screenshots"),
    "765592086245670922": ("wastes", "Diontalus visual references"),
    "713764067969335371": ("wastes", "Episode 105 historical notes - unverified"),
    "716274279448182917": ("wastes", "Episode 106 historical notes - unverified"),
    "716274314911023115": ("wastes", "Episode 107 historical notes - unverified"),
    # GM-posted Delvers reference maps and player aids (provisional grouping).
    "813596628526825504": ("delvers", "Guild guide reference"),
    "803736050500894721": ("delvers", "S1E3 maps"),
    "816005531802009620": ("delvers", "Carries map"),
    "816005979236991027": ("delvers", "Carries notes"),
    "818622251560730644": ("delvers", "Well encounter map"),
    "821063868385722368": ("delvers", "S1E9 map"),
    "823602387259752468": ("delvers", "S1E10 map"),
    "823602428272181248": ("delvers", "S1E10 map"),
    "823602459180138537": ("delvers", "S1E10 map"),
    "836289898587619378": ("delvers", "Atymer region map"),
    "836290829597278268": ("delvers", "S2E1 map"),
    "838811364994449420": ("delvers", "S2E2 map"),
    "841426333582098453": ("delvers", "S2E3 map"),
    "843919769164840992": ("delvers", "Withers Estate map"),
    "843920127442944082": ("delvers", "Withers basement map"),
    "848976809521315861": ("delvers", "S2E5 map"),
    "848977308462088212": ("delvers", "Battle map"),
    "851511595825102950": ("delvers", "Withers map"),
    "854032716773589032": ("delvers", "Tide map"),
    "854032841909993473": ("delvers", "Tide map"),
    "856574170842398742": ("delvers", "Waterfall map"),
    "856574415080521728": ("delvers", "River of Fire map"),
    "856574469496766504": ("delvers", "Mini map"),
    "864184770983493644": ("delvers", "Withers map"),
    "864185089952841759": ("delvers", "Map part 1"),
    "864185131811078174": ("delvers", "Map part 2"),
    "869283278228684820": ("delvers", "Starting map"),
    "876922083483975741": ("delvers", "Atymer expanded map"),
    "883103944950292541": ("delvers", "S3E4 map"),
    "884517517928824842": ("delvers", "S3E5 map"),
    "887023756395044905": ("delvers", "S3E6 map"),
    "889586287919628288": ("delvers", "Ancient Elvish reference"),
    "892108130631155763": ("delvers", "Temple map"),
    "904783484202143755": ("delvers", "Map part 1"),
    "904783525692207135": ("delvers", "Map part 2"),
}
CAST = {
    "beauschwartz": "Beau",
    "jonjagger": "Jon",
    "frogpants": "Scott",
    "kyle_tarrasque": "Kyle",
    "kristenashton": "Kristen",
}
README_MARKER = "\n## Expanded Discord channel archive — incremental additions\n"


def sha_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def atomic_json(path: Path, value: dict) -> None:
    temporary = path.with_name(path.name + ".sync-tmp")
    temporary.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    os.replace(temporary, path)


def atomic_text(path: Path, value: str) -> None:
    temporary = path.with_name(path.name + ".sync-tmp")
    temporary.write_text(value, encoding="utf-8")
    os.replace(temporary, path)


def read_only(path: Path) -> sqlite3.Connection:
    c = sqlite3.connect(path.resolve().as_uri() + "?mode=ro", uri=True)
    c.row_factory = sqlite3.Row
    c.execute("PRAGMA query_only=ON")
    return c


def safe_name(name: str) -> str:
    name = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", name).strip(" .") or "attachment"
    if name.split(".")[0].upper() in {"CON", "PRN", "AUX", "NUL"} | {
        f"{prefix}{i}" for prefix in ("COM", "LPT") for i in range(1, 10)
    }:
        name = "_" + name
    if len(name) > 125:
        name = name[:110] + Path(name).suffix[:12]
    return name


def detect(blob: bytes) -> tuple[str | None, str | None]:
    if blob.startswith(b"\x89PNG\r\n\x1a\n"):
        return "image/png", ".png"
    if blob.startswith(b"\xff\xd8\xff"):
        return "image/jpeg", ".jpg"
    if blob.startswith((b"GIF87a", b"GIF89a")):
        return "image/gif", ".gif"
    if blob[:4] == b"RIFF" and blob[8:12] == b"WEBP":
        return "image/webp", ".webp"
    if blob[:4] == b"RIFF" and blob[8:12] == b"WAVE":
        return "audio/wav", ".wav"
    if blob.startswith(b"%PDF-"):
        return "application/pdf", ".pdf"
    if blob.startswith(b"ID3"):
        return "audio/mpeg", ".mp3"
    if blob[4:8] == b"ftyp":
        return "video/mp4", ".mp4"
    if blob.startswith(b"PK\x03\x04"):
        return "application/zip", ".zip"
    return None, None


def choose_path(base: Path, preferred: Path, digest: str, claimed: set[str],
                tag: str) -> Path:
    """Stable collision handling; existing different bytes are never overwritten."""
    candidates = [preferred]
    stem, suffix = preferred.stem, preferred.suffix
    candidates.extend(
        [preferred.with_name(stem + "--" + tag + suffix),
         preferred.with_name(stem + "--" + digest[:12] + suffix),
         preferred.with_name(stem + "--" + digest + suffix)]
    )
    for rel in candidates:
        path = (base / rel).resolve()
        if not path.is_relative_to(base.resolve()):
            raise ValueError("Attempted output path traversal")
        key = rel.as_posix().casefold()
        if key in claimed:
            continue
        if not path.exists() or sha_file(path) == digest:
            claimed.add(key)
            return rel
    raise ValueError(f"Unresolvable output filename collision: {preferred}")


def checked_save(base: Path, rel: Path, data: bytes, digest: str, dry_run: bool) -> bool:
    target = base / rel
    if target.exists():
        if sha_file(target) != digest:
            raise ValueError(f"Existing file mismatch: {target}")
        return False
    if not dry_run:
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("xb") as out:
            out.write(data)
        if sha_file(target) != digest:
            raise ValueError(f"Written file mismatch: {target}")
    return True


def sources(db: sqlite3.Connection):
    refs: dict[str, list[dict]] = defaultdict(list)
    src = db.execute(
        """SELECT a.attachment_id,a.name,a.type,a.normalized_url,a.size,
                  a.width,a.height,m.message_id,m.channel_id,m.timestamp,
                  c.server,c.name AS channel_name,u.name AS sender_name
           FROM attachments a
           LEFT JOIN message_attachments ma ON ma.attachment_id=a.attachment_id
           LEFT JOIN messages m ON m.message_id=ma.message_id
           LEFT JOIN channels c ON c.id=m.channel_id
           LEFT JOIN users u ON u.id=m.sender_id
           ORDER BY a.attachment_id,m.timestamp"""
    )
    for r in src:
        item = {
            "attachment_id": str(r["attachment_id"]),
            "name": r["name"], "type": r["type"],
            "normalized_url": r["normalized_url"], "size": r["size"],
            "width": r["width"], "height": r["height"], "messages": [],
        }
        if r["message_id"] is not None:
            item["messages"].append({
                "message_id": str(r["message_id"]),
                "channel_id": str(r["channel_id"]), "channel_name": r["channel_name"],
                "server_id": str(r["server"]), "timestamp_ms": r["timestamp"],
                "author_name": r["sender_name"],
                "url": ("https://discord.com/channels/"
                        f"{r['server']}/{r['channel_id']}/{r['message_id']}"),
            })
        # One file can be linked by more than one message; merge associations.
        parts = refs[r["normalized_url"]]
        prior = next((p for p in parts if p["attachment_id"] == item["attachment_id"]), None)
        if prior:
            prior["messages"].extend(item["messages"])
        else:
            parts.append(item)
    return refs


def curated_plan(assocs: list[dict]) -> list[tuple[str, str, dict]]:
    targets = []
    for association in assocs:
        for m in association["messages"]:
            match = CURATED_MESSAGES.get(m["message_id"])
            if match:
                targets.append((*match, {"message": m, "name": association["name"]}))
    return targets


def run(dry_run: bool, curated: bool, verify_snapshot: bool) -> None:
    audit = json.loads(AUDIT.read_text(encoding="utf-8"))
    snapshot_id = audit["current_summary"]["snapshot_id"]
    folder = ROOT / "local/discord/snapshots" / snapshot_id
    snap = json.loads((folder / "manifest.json").read_text(encoding="utf-8"))
    if snap["snapshot_id"] != snapshot_id:
        raise ValueError("Snapshot ID mismatch")
    current_source = {k: {x: v[x] for x in ("sha256", "size", "mtime_ns")}
                      for k, v in snap["sources"].items()}
    if verify_snapshot:
        for label in ("archive", "downloads"):
            if sha_file(folder / label) != snap["fingerprint"][label]["sha256"]:
                raise ValueError(f"Snapshot hash mismatch: {label}")
    raw_manifest_path = RAW / "manifest.json"
    curated_manifest_path = CURATED / "manifest.private.json"
    old = json.loads(raw_manifest_path.read_text(encoding="utf-8"))
    old_curated = json.loads(curated_manifest_path.read_text(encoding="utf-8"))
    previous = {e["normalized_url"]: e for e in old["files"]}
    prior_curated = {(e.get("url"), str(e.get("message_id"))) for e in old_curated["assets"]
                     if e.get("path")}
    curated_by_hash = {e["sha256"]: e["path"] for e in old_curated["assets"]
                       if e.get("sha256") and e.get("path") and
                       (CURATED / e["path"]).is_file()}
    old_paths = {e["path"].casefold() for e in old["files"] if e.get("path")}
    new_raw: list[dict] = []
    current_urls: set[str] = set()
    new_curation: list[dict] = []
    curation_keys = set(prior_curated)
    raw_written = curated_written = 0
    new_urls = altered_blobs = missed = 0
    byte_variants: list[dict] = []

    with read_only(folder / "archive") as db, read_only(folder / "downloads") as dl:
        associations = sources(db)
        for r in dl.execute(
            """SELECT m.normalized_url,m.status,m.type,m.size,b.blob
               FROM download_metadata m
               LEFT JOIN download_blobs b USING(normalized_url)
               ORDER BY m.normalized_url"""
        ):
            url = r["normalized_url"]
            current_urls.add(url)
            existing = previous.get(url)
            assocs = associations.get(url, [])
            data = r["blob"]
            digest = hashlib.sha256(data).hexdigest() if data is not None else None
            found_type, extension = detect(data or b"")
            if data is None:
                missed += 1
                if existing and existing.get("path"):
                    # Retain a prior recoverable byte version even if no longer available.
                    rec = dict(existing)
                    rec["latest_status"] = r["status"]
                    rec["blob_missing_in_latest_snapshot"] = True
                    rec["attachments"] = assocs
                else:
                    rec = {
                        "normalized_url": url, "status": r["status"], "path": None,
                        "reason": "No blob in latest snapshot", "attachments": assocs,
                        "declared_type": r["type"], "declared_bytes": r["size"],
                    }
            else:
                if existing and existing.get("sha256") == digest and existing.get("path"):
                    rel = Path(existing["path"])
                    raw_path = RAW / rel
                    if raw_path.exists() and sha_file(raw_path) != digest:
                        raise ValueError(f"Prior raw file changed: {raw_path}")
                    if checked_save(RAW, rel, data, digest, dry_run):
                        raw_written += 1
                    old_paths.add(rel.as_posix().casefold())
                else:
                    if existing and existing.get("path"):
                        altered_blobs += 1
                        byte_variants.append(dict(existing))
                    elif existing is None:
                        new_urls += 1
                    if assocs:
                        name = safe_name(assocs[0]["name"])
                        tag = assocs[0]["attachment_id"]
                        subfolder = "attachments"
                    else:
                        name = safe_name(unquote(urlsplit(url).path.rsplit("/", 1)[-1]))
                        if not Path(name).suffix:
                            name += extension or mimetypes.guess_extension(r["type"] or "") or ".bin"
                        tag = hashlib.sha256(url.encode()).hexdigest()[:12]
                        subfolder = "other-media"
                    preferred = Path(subfolder) / name
                    # A reused normalized URL with different bytes gets a new filename,
                    # preserving the originally exported file and its provenance.
                    if existing and existing.get("path"):
                        preferred = preferred.with_name(
                            preferred.stem + "--" + digest[:12] + preferred.suffix)
                    rel = choose_path(RAW, preferred, digest, old_paths, tag)
                    raw_written += int(checked_save(RAW, rel, data, digest, dry_run))
                rec = {
                    "normalized_url": url, "status": r["status"],
                    "path": rel.as_posix(), "sha256": digest,
                    "actual_bytes": len(data), "declared_type": r["type"],
                    "declared_bytes": r["size"], "detected_type": found_type,
                    "attachments": assocs,
                    "attachment_size_mismatch": any(a["size"] != len(data) for a in assocs),
                }
                if existing and existing.get("sha256") not in (None, digest):
                    rec["previous_versions"] = existing.get("previous_versions", []) + [{
                        "path": existing.get("path"), "sha256": existing.get("sha256"),
                        "snapshot_id": old.get("latest_snapshot_id"),
                    }]
                if curated:
                    for category, label, selected in curated_plan(assocs):
                        m = selected["message"]
                        key = (url, m["message_id"])
                        if key in curation_keys:
                            continue
                        filename = safe_name(m["message_id"] + "--" + selected["name"])
                        preferred = Path(category) / filename
                        prior_copy = curated_by_hash.get(digest)
                        if prior_copy:
                            preferred = Path(prior_copy)
                            if sha_file(CURATED / preferred) != digest:
                                raise ValueError(f"Existing curated hash mismatch: {preferred}")
                        else:
                            candidate = CURATED / preferred
                            if candidate.exists() and sha_file(candidate) != digest:
                                preferred = preferred.with_name(
                                    preferred.stem + "--" + digest[:12] + preferred.suffix)
                            if checked_save(CURATED, preferred, data, digest, dry_run):
                                curated_written += 1
                            curated_by_hash[digest] = preferred.as_posix()
                        new_curation.append({
                            "cast": CAST.get(m["author_name"]),
                            "message_id": m["message_id"], "message_url": m["url"],
                            "timestamp_ms": m["timestamp_ms"], "channel": m["channel_name"],
                            "kind": "attachment", "url": url, "original_name": selected["name"],
                            "campaign": category, "title": label, "path": preferred.as_posix(),
                            "sha256": digest, "bytes": len(data), "status": "saved",
                            "acquisition": "expanded DHT snapshot cached blob",
                            "archive_snapshot_id": snapshot_id,
                            "duplicate_of_existing_path": prior_copy,
                            "provenance_note": ("Curated research lead; attribution is account-based. "
                                                "Campaign and artwork status require contextual review."),
                        })
                        curation_keys.add(key)
            new_raw.append(rec)
        # Source entries absent from the new snapshot must not be lost.
        new_raw.extend({**v, "not_observed_in_current_snapshot": True}
                       for k, v in previous.items() if k not in current_urls)

    new_record_count = len(current_urls - previous.keys())
    if dry_run:
        print(json.dumps({
            "dry_run": True, "source_snapshot": snapshot_id,
            "prior_download_records": len(previous), "current_download_records": len(current_urls),
            "new_download_records": new_record_count,
            "new_urls_with_blobs": new_urls, "altered_cached_blobs": altered_blobs,
            "no_current_blob": missed, "raw_files_to_write": raw_written,
            "curated_files_to_write": curated_written, "curated_new_entries": len(new_curation),
        }, indent=2))
        return

    if not RAW.is_dir() or (curated and not CURATED.is_dir()):
        raise ValueError("Required download directory is missing")
    first_sync = not old.get("sync_history")
    initial_summary = dict(old.get("summary", {}))
    old_sources = dict(old.get("sources", {}))
    old["files"] = sorted(new_raw, key=lambda a: a["normalized_url"])
    old["sources"] = {
        "There Will Be Dungeons.dht": current_source["archive"],
        "There Will Be Dungeons.dht_downloads": current_source["downloads"],
    }
    counts = old["files"]
    old["summary"] = {
        "exported_files": sum(bool(x.get("path")) for x in counts),
        "attachment_files": sum(bool(x.get("path")) and bool(x.get("attachments")) for x in counts),
        "other_media_files": sum(bool(x.get("path")) and not x.get("attachments") for x in counts),
        "unavailable_downloads": sum(not x.get("path") for x in counts),
        "exported_bytes": sum(x.get("actual_bytes", 0) for x in counts if x.get("path")),
        "attachment_size_mismatches": sum(bool(x.get("attachment_size_mismatch")) for x in counts),
        "original_databases_unchanged": True, "all_exported_file_hashes_verified": True,
    }
    observed = datetime.now(timezone.utc).isoformat()
    old["latest_snapshot_id"] = snapshot_id
    old["last_synced_at_utc"] = observed
    old.setdefault("sync_history", []).append({
        "at_utc": observed, "snapshot_id": snapshot_id,
        "previous_sources": old_sources if first_sync else None,
        "new_download_records": new_record_count, "new_urls_with_blobs": new_urls,
        "altered_blobs": altered_blobs,
        "raw_new_files": raw_written, "curated_new_files": curated_written,
        "baseline_summary": initial_summary if first_sync else None,
    })
    if byte_variants:
        old.setdefault("superseded_blob_versions", []).extend(byte_variants)
    atomic_json(raw_manifest_path, old)

    if curated:
        old_curated["assets"].extend(new_curation)
        old_curated.setdefault("expanded_archive_sync", []).append({
            "at_utc": observed, "snapshot_id": snapshot_id,
            "new_files": curated_written, "new_manifest_entries": len(new_curation),
        })
        atomic_json(curated_manifest_path, old_curated)

    old_readme = (RAW / "README.md").read_text(encoding="utf-8")
    old_readme = old_readme.split(README_MARKER)[0].rstrip() + README_MARKER
    old_readme += (
        f"\nLatest imported snapshot: {snapshot_id}.\n"
        f"Recorded downloads: {len(counts)}; entries with local data: "
        f"{old['summary']['exported_files']}; new files written by this pass: {raw_written}.\n"
        "Older byte variants are retained; consult manifest.json for original message "
        "permalinks, exact hashes and the source snapshot. File presence does not "
        "establish authorship, canon or reuse rights.\n"
    )
    atomic_text(RAW / "README.md", old_readme)
    if curated:
        curated_readme = (CURATED / "README.md").read_text(encoding="utf-8")
        curated_readme = curated_readme.split(README_MARKER)[0].rstrip() + README_MARKER
        curated_readme += (
            "\nThese selected research leads came from additional archived channels. "
            "Campaign attribution is provisional, and episode/visual details need review.\n\n"
            "| Research file | Source message |\n|---|---|\n"
        )
        added = [a for a in old_curated["assets"] if a.get("archive_snapshot_id") == snapshot_id
                 and a.get("path")]
        for a in sorted(added, key=lambda d: d["path"]):
            curated_readme += (
                f"| [{a['path']}](<{a['path']}>) | "
                f"[Discord]({a['message_url']}) |\n"
            )
        atomic_text(CURATED / "README.md", curated_readme)

    print(json.dumps({
        "dry_run": False, "source_snapshot": snapshot_id,
        "current_download_records": len(current_urls),
        "new_download_records": new_record_count,
        "new_urls_with_blobs": new_urls, "altered_cached_blobs": altered_blobs,
        "new_raw_files": raw_written, "new_curated_files": curated_written,
        "new_curated_manifest_entries": len(new_curation),
        "raw_files_total": old["summary"]["exported_files"],
    }, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--no-curated", action="store_true",
                        help="Update only the complete raw discord-downloads archive")
    parser.add_argument("--skip-snapshot-hash", action="store_true",
                        help="For repeated local tests only; snapshot ingestion already verified hashes")
    args = parser.parse_args()
    run(dry_run=args.dry_run, curated=not args.no_curated,
        verify_snapshot=not args.skip_snapshot_hash)
