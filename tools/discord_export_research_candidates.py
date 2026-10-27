"""Extract selected newly archived Discord attachments to a private local folder.

Uses only the verified snapshot and audit JSON. Does not contact Discord,
open Office documents, alter original databases, or write into tracked content.

Default selection focuses on the Wastes map, visual references and episode notes.
Use --list to inspect the selected candidate metadata before extracting.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "local/discord/new-channels-audit.json"
DEST = ROOT / "local/discord/recovered-research"

# Selected message IDs are discovery leads, not assertions of verified authorship.
SELECTED = {
    "669709591344316416": "Beau-attributed Known Wastes map",
    "738777012444856381": "Jon-attributed Stanley S1 reference",
    "738777095118782495": "Jon-attributed Stanley S2 reference",
    "672186714638254090": "Nash visual evolution lead",
    "761462415833038878": "Vorel screenshot",
    "761462418051301387": "Hope screenshot",
    "761462421486436363": "Nash screenshot",
    "761767030457630720": "Group character screenshots",
    "765592086245670922": "Diontalus screenshots",
    "713764067969335371": "Unreviewed episode 105 document",
    "716274279448182917": "Unreviewed episode 106 document",
    "716274314911023115": "Unreviewed episode 107 document",
}

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def filename(value: str) -> str:
    safe = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", value).strip(" .")
    if not safe:
        safe = "attachment"
    if len(safe) > 140:
        safe = safe[:115] + Path(safe).suffix[:15]
    if safe.split(".")[0].upper() in {"CON", "PRN", "AUX", "NUL"}:
        safe = "_" + safe
    return safe

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--list", action="store_true", help="Show selected metadata without copying files")
    parser.add_argument("--message-id", action="append", default=[],
                        help="Select additional archived message IDs (repeatable)")
    parser.add_argument("--output", type=Path, default=DEST)
    parser.add_argument("--max-mib", type=int, default=50)
    args = parser.parse_args()
    if args.max_mib <= 0:
        parser.error("--max-mib must be positive")
    out = args.output.resolve()
    if not out.is_relative_to((ROOT / "local").resolve()):
        parser.error("Export directory must remain private under local/")
    audit = json.loads(AUDIT.read_text(encoding="utf-8"))
    snapshot_id = audit["current_summary"]["snapshot_id"]
    folder = ROOT / "local/discord/snapshots" / snapshot_id
    snap_manifest = json.loads((folder / "manifest.json").read_text(encoding="utf-8"))
    assert snap_manifest["snapshot_id"] == snapshot_id
    dl = folder / "downloads"
    assert dl.is_file(), "Captured snapshot lacks download database"
    selected = SELECTED | {m: "Manually selected" for m in args.message_id}
    entries = []
    for item in audit["candidates"]:
        if item["kind"] != "attachment":
            continue
        message_id = item["message_url"].split("/")[-1]
        if message_id in selected:
            entries.append((message_id, selected[message_id], item))
    if args.list:
        for mid, label, item in entries:
            print(f"{mid}  {label}: {item.get('name')}  "
                  f"blob={'yes' if item.get('archive_blob_present') else 'no'}")
        print(f"Selected occurrences: {len(entries)}")
        return
    out.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(dl.resolve().as_uri() + "?mode=ro", uri=True)
    connection.execute("PRAGMA query_only=ON")
    manifest = {"snapshot_id": snapshot_id, "created_utc": datetime.now(timezone.utc).isoformat(),
                "scope": "Private selected Discord attachments, no external fetching",
                "items": []}
    written = {}
    try:
        for mid, label, item in entries:
            url = item["url"]
            record = {"message_id": mid, "message_url": item["message_url"],
                      "channel": item["channel"], "label": label,
                      "source_name": item.get("name"), "url": url,
                      "attributed_cast": item.get("cast_attributed")}
            row = connection.execute(
                "SELECT blob FROM download_blobs WHERE normalized_url=?", (url,)
            ).fetchone()
            if not row or row[0] is None:
                record["status"] = "no-archived-blob"
            else:
                data = row[0]
                digest = sha256(data)
                expected = item.get("blob_sha256")
                if expected and digest != expected:
                    raise ValueError(f"Hash mismatch for message {mid}")
                if len(data) > args.max_mib * 1024 * 1024:
                    record["status"] = "oversize-not-copied"
                else:
                    if digest in written:
                        path = written[digest]
                        record["status"] = "duplicate-byte-reuse"
                    else:
                        name = filename(f"{mid}--{item.get('name') or 'attachment'}")
                        path = out / name
                        if path.exists():
                            if sha256(path.read_bytes()) != digest:
                                raise ValueError(f"Existing file conflict: {path}")
                        else:
                            path.write_bytes(data)
                        if sha256(path.read_bytes()) != digest:
                            raise ValueError(f"Saved bytes did not verify: {path}")
                        written[digest] = path
                        record["status"] = "saved-verified"
                    record.update(path=str(path.relative_to(out)), sha256=digest, size=len(data))
            manifest["items"].append(record)
    finally:
        connection.close()
    target = out / "manifest.private.json"
    target.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(out), "selected_occurrences": len(entries),
                      "unique_files": len(written), "snapshot": snapshot_id}, ensure_ascii=False))

if __name__ == "__main__":
    main()
