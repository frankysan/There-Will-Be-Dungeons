"""Offline DHT v11 research index. All archive-derived outputs must stay private.

Run with --help. Uses only the Python standard library; never opens source SQLite
files or visits URLs. Source files must be quiescent during the snapshot copy.
"""
from __future__ import annotations

import argparse
from contextlib import closing
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import shutil
import sqlite3
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INDEX = ROOT / "local/discord/research.sqlite"
FORMAT = "discord-research-v1"
REQUIRED = {
    "metadata": "key value", "servers": "id name type icon_hash",
    "channels": "id server name parent_id position topic nsfw",
    "users": "id name display_name avatar_url discriminator",
    "messages": "message_id sender_id channel_id text timestamp",
    "message_replied_to": "message_id replied_to_id",
    "message_edit_timestamps": "message_id edit_timestamp",
    "message_attachments": "message_id attachment_id",
    "attachments": "attachment_id name type normalized_url download_url size width height",
    "message_embeds": "message_id json",
    "message_reactions": "message_id emoji_id emoji_name emoji_flags count",
}


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def hash_bytes(data):
    return hashlib.sha256(data).hexdigest()


def hash_file(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def now():
    return datetime.now(timezone.utc).isoformat()


def private_path(path):
    """Reject archive-derived output in the tracked part of this checkout."""
    path = Path(path).resolve()
    if path.is_relative_to(ROOT) and not path.is_relative_to(ROOT / "local"):
        raise ValueError("Archive-derived output must be under local/ or outside this checkout")
    return path


def readonly(path):
    c = sqlite3.connect(Path(path).resolve().as_uri() + "?mode=ro", uri=True)
    c.row_factory = sqlite3.Row
    c.execute("PRAGMA query_only=ON")
    return c


def source_inventory(source, downloads):
    result = {}
    for label, base in (("archive", source), ("downloads", downloads)):
        if base is None:
            continue
        for suffix in ("", "-wal", "-shm", "-journal"):
            p = Path(str(base) + suffix)
            if p.exists():
                stat = p.stat()
                result[label + suffix] = {"path": str(p.resolve()), "size": stat.st_size,
                                          "mtime_ns": stat.st_mtime_ns, "sha256": hash_file(p)}
    return result


def snapshot(source, downloads, destination):
    source = Path(source).resolve()
    downloads = Path(downloads).resolve() if downloads is not None else None
    if not source.is_file() or (downloads is not None and not downloads.is_file()):
        raise ValueError("Source database does not exist")
    before = source_inventory(source, downloads)
    fingerprint = {k: {f: v[f] for f in ("size", "sha256")} for k, v in before.items()}
    sid = hash_bytes(canonical(fingerprint).encode())
    destination = private_path(destination)
    destination.mkdir(parents=True, exist_ok=True)
    target = destination / sid
    if target.exists():
        manifest = json.loads((target / "manifest.json").read_text(encoding="utf-8"))
        if manifest["fingerprint"] != fingerprint:
            raise ValueError("Snapshot manifest mismatch")
        # SQLite may create/update an SHM on the disposable copy; verify main/WAL bytes.
        for k, v in fingerprint.items():
            if not k.endswith("-shm") and hash_file(target / k) != v["sha256"]:
                raise ValueError("Existing snapshot bytes changed")
    else:
        with tempfile.TemporaryDirectory(prefix="copy-", dir=destination) as tmp:
            tmp = Path(tmp)
            for k, v in before.items():
                shutil.copy2(v["path"], tmp / k)
                if hash_file(tmp / k) != v["sha256"]:
                    raise ValueError("Source changed during copying; stop the capture writer")
            if source_inventory(source, downloads) != before:
                raise ValueError("Source changed during copying; stop the capture writer")
            (tmp / "manifest.json").write_text(canonical({"sources": before,
                "fingerprint": fingerprint, "snapshot_id": sid, "observed_at": now()}), encoding="utf-8")
            tmp.rename(target)
    if source_inventory(source, downloads) != before:
        raise ValueError("Source changed while inspecting snapshot")
    return sid, target, before


def validate_schema(c, required, version=False):
    for table, columns in required.items():
        found = {r["name"] for r in c.execute(f'PRAGMA table_info("{table}")')}
        if not set(columns.split()) <= found:
            raise ValueError(f"Unsupported source schema: {table}")
    if version and dict(c.execute("SELECT key,value FROM metadata")).get("version") != "11":
        raise ValueError("Only inspected DHT format 11 is supported; no migration attempted")
    if c.execute("PRAGMA quick_check").fetchone()[0] != "ok":
        raise ValueError("Source snapshot failed SQLite quick_check")


def schema_details(c):
    return [dict(r) for r in c.execute("SELECT type,name,sql FROM sqlite_master ORDER BY type,name")]


def schema_index(c, fallback=False):
    c.executescript("""
        CREATE TABLE IF NOT EXISTS settings(key TEXT PRIMARY KEY,value TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS snapshots(id TEXT PRIMARY KEY, observed_at TEXT, manifest TEXT, schema_json TEXT);
        CREATE TABLE IF NOT EXISTS runs(id INTEGER PRIMARY KEY, snapshot_id TEXT, observed_at TEXT, summary TEXT);
        CREATE TABLE IF NOT EXISTS messages(key TEXT PRIMARY KEY, server_id TEXT, channel_id TEXT,
            message_id TEXT, sender_id TEXT, timestamp INTEGER, text TEXT, payload_hash TEXT,
            last_run INTEGER, payload TEXT NOT NULL);
        CREATE INDEX IF NOT EXISTS message_chronology ON messages(channel_id,timestamp,message_id);
        CREATE TABLE IF NOT EXISTS search_documents(key TEXT PRIMARY KEY,body TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS versions(key TEXT, payload_hash TEXT, first_run INTEGER,
            payload TEXT NOT NULL, PRIMARY KEY(key,payload_hash));
        CREATE TABLE IF NOT EXISTS observations(run_id INTEGER,key TEXT,payload_hash TEXT,
            PRIMARY KEY(run_id,key));
        CREATE TABLE IF NOT EXISTS assets(snapshot_id TEXT,normalized_url TEXT,blob_hash TEXT,
            actual_bytes INTEGER,status INTEGER,declared_type TEXT,declared_size INTEGER,signature_hex TEXT,
            PRIMARY KEY(snapshot_id,normalized_url));
        CREATE INDEX IF NOT EXISTS asset_hash ON assets(blob_hash);
        CREATE TABLE IF NOT EXISTS review_queue(id TEXT PRIMARY KEY,record TEXT NOT NULL);
    """)
    fmt = c.execute("SELECT value FROM settings WHERE key='format'").fetchone()
    if fmt and fmt[0] != FORMAT:
        raise ValueError("Unsupported research-index format")
    c.execute("INSERT OR IGNORE INTO settings VALUES('format',?)", (FORMAT,))
    engine = c.execute("SELECT value FROM settings WHERE key='search_engine'").fetchone()
    if not engine:
        engine = "substring"
        if not fallback:
            try:
                c.execute("CREATE VIRTUAL TABLE message_fts USING fts5(key UNINDEXED,text)")
                engine = "fts5"
            except sqlite3.OperationalError as exc:
                if "no such module" not in str(exc):
                    raise
        c.execute("INSERT INTO settings VALUES('search_engine',?)", (engine,))
    c.commit()


def open_index(path, write=False):
    path = private_path(path)
    if write:
        if path.exists():
            with closing(readonly(path)) as existing:
                try:
                    row = existing.execute("SELECT value FROM settings WHERE key='format'").fetchone()
                except sqlite3.DatabaseError as exc:
                    raise ValueError("Destination is not a research index") from exc
                if not row or row[0] != FORMAT:
                    raise ValueError("Destination is not a supported research index")
        path.parent.mkdir(parents=True, exist_ok=True)
        c = sqlite3.connect(path)
        c.row_factory = sqlite3.Row
        return c
    c = readonly(path)
    if c.execute("SELECT value FROM settings WHERE key='format'").fetchone()[0] != FORMAT:
        c.close()
        raise ValueError("Unsupported research index")
    return c


def grouped(c, table):
    result = {}
    for r in c.execute(f'SELECT * FROM "{table}"'):
        item = dict(r)
        result.setdefault(str(item.pop("message_id")), []).append(item)
    return result


def permalink(server, channel, message):
    return f"https://discord.com/channels/{server}/{channel}/{message}"


def search_body(payload):
    parts=[payload["text"]]
    parts.extend(a["name"] for a in payload["attachments"])
    for item in payload["embeds"]:
        try:
            embed=json.loads(item["json"])
        except (ValueError,TypeError):
            continue  # Preserve malformed source JSON in payload; do not guess its meaning.
        if not isinstance(embed,dict):
            continue
        parts.extend(str(embed.get(k) or "") for k in ("title","description"))
        for field in embed.get("fields",[]) or []:
            if isinstance(field,dict):
                parts.extend(str(field.get(k) or "") for k in ("name","value"))
    return "\n".join(parts)


def ingest(source, index=DEFAULT_INDEX, downloads=None, fallback=False):
    index = private_path(index)
    if index == Path(source).resolve() or (downloads and index == Path(downloads).resolve()):
        raise ValueError("Index must be separate from sources")
    sid, folder, original = snapshot(source, downloads, index.parent / "snapshots")
    with closing(readonly(folder / "archive")) as src:
        validate_schema(src, REQUIRED, version=True)
        schema = {"archive": schema_details(src)}
        servers = {str(r["id"]): dict(r) for r in src.execute("SELECT * FROM servers")}
        channels = {str(r["id"]): dict(r) for r in src.execute("SELECT * FROM channels")}
        users = {str(r["id"]): dict(r) for r in src.execute("SELECT * FROM users")}
        # IDs are strings in all JSON, including nested source metadata.
        def strings(obj):
            return {k: str(v) if v is not None and (k == "id" or k == "server" or k.endswith("_id")) else v
                    for k, v in obj.items()}
        relations = {t: grouped(src, t) for t in ("message_replied_to", "message_edit_timestamps",
                     "message_embeds", "message_reactions", "message_attachments")}
        attachments = {str(r["attachment_id"]): strings(dict(r)) for r in src.execute("SELECT * FROM attachments")}
        assets = {}
        if downloads:
            with closing(readonly(folder / "downloads")) as dl:
                validate_schema(dl, {"download_metadata": "normalized_url download_url status type size",
                                     "download_blobs": "normalized_url blob"})
                schema["downloads"] = schema_details(dl)
                for r in dl.execute("SELECT m.*,b.blob FROM download_metadata m LEFT JOIN download_blobs b USING(normalized_url)"):
                    b = r["blob"]
                    assets[r["normalized_url"]] = {"blob_hash": hash_bytes(b) if b is not None else None,
                        "actual_bytes": len(b) if b is not None else None, "status": r["status"],
                        "declared_type": r["type"], "declared_size": r["size"],
                        "signature_hex": b[:16].hex() if b is not None else None}
        payloads = []
        for r in src.execute("SELECT * FROM messages ORDER BY timestamp,message_id"):
            m = strings(dict(r))
            mid = m["message_id"]
            channel = strings(channels[m["channel_id"]])
            server = strings(servers[channel["server"]])
            author = strings(users[m["sender_id"]])
            attachment_rows = []
            for a in relations["message_attachments"].get(mid, []):
                a = attachments[str(a["attachment_id"])]
                attachment_rows.append({**a, "download": assets.get(a["normalized_url"])})
            p = {**m, "server_id": server["id"], "server": server, "channel": channel, "author": author,
                 "url": permalink(server["id"],channel["id"],mid),
                 "reply_to": [strings(x) for x in relations["message_replied_to"].get(mid,[])],
                 "edits": relations["message_edit_timestamps"].get(mid,[]),
                 "embeds": relations["message_embeds"].get(mid,[]),
                 "reactions": [strings(x) for x in relations["message_reactions"].get(mid,[])],
                 "attachments": sorted(attachment_rows,key=lambda a:a["attachment_id"])}
            for field in ("embeds", "reactions", "reply_to", "edits"):
                p[field] = sorted(p[field], key=canonical)
            payloads.append(p)
    if source_inventory(Path(source),Path(downloads) if downloads else None) != original:
        raise ValueError("Sources changed during inspection; index not updated")
    with closing(open_index(index, write=True)) as c:
        schema_index(c, fallback)
        with c:
            observed_at = now()
            c.execute("INSERT OR IGNORE INTO snapshots VALUES(?,?,?,?)",
                (sid,observed_at,canonical(original),canonical(schema)))
            run = c.execute("INSERT INTO runs(snapshot_id,observed_at) VALUES(?,?)",(sid,observed_at)).lastrowid
            summary = {"run_id":run,"snapshot_id":sid,"messages":len(payloads),"new":0,"changed":0,
                       "unchanged":0,"missing_reply_targets":0,"assets":len(assets),"not_observed":0,
                       "channel_scopes":[{"server_id":str(ch["server"]),"channel_id":str(ch["id"])} for ch in channels.values()]}
            fts = c.execute("SELECT value FROM settings WHERE key='search_engine'").fetchone()[0] == "fts5"
            ids = {p["message_id"] for p in payloads}
            for p in payloads:
                key = f'discord/{p["server_id"]}/{p["channel_id"]}/{p["message_id"]}'
                encoded = canonical(p)
                digest = hash_bytes(encoded.encode())
                old = c.execute("SELECT payload_hash FROM messages WHERE key=?",(key,)).fetchone()
                summary["new" if old is None else "unchanged" if old[0] == digest else "changed"] += 1
                summary["missing_reply_targets"] += sum(x["replied_to_id"] not in ids for x in p["reply_to"])
                c.execute("INSERT OR IGNORE INTO versions VALUES(?,?,?,?)",(key,digest,run,encoded))
                c.execute("INSERT INTO observations VALUES(?,?,?)",(run,key,digest))
                c.execute("INSERT OR REPLACE INTO messages VALUES(?,?,?,?,?,?,?,?,?,?)",
                    (key,p["server_id"],p["channel_id"],p["message_id"],p["sender_id"],p["timestamp"],p["text"],digest,run,encoded))
                body=search_body(p)
                old_body=c.execute("SELECT body FROM search_documents WHERE key=?",(key,)).fetchone()
                if old_body is None or old_body[0]!=body:
                    c.execute("INSERT OR REPLACE INTO search_documents VALUES(?,?)",(key,body))
                    if fts:
                        c.execute("DELETE FROM message_fts WHERE key=?",(key,))
                        c.execute("INSERT INTO message_fts VALUES(?,?)",(key,body))
            for url,a in assets.items():
                c.execute("INSERT OR IGNORE INTO assets VALUES(?,?,?,?,?,?,?,?)",(sid,url,a["blob_hash"],
                    a["actual_bytes"],a["status"],a["declared_type"],a["declared_size"],a["signature_hex"]))
            # Absence is scoped to channels observed in this snapshot, not a deletion.
            scopes = {(str(ch["server"]),str(ch["id"])) for ch in channels.values()}
            for server,channel in scopes:
                summary["not_observed"] += c.execute("SELECT count(*) FROM messages WHERE server_id=? AND channel_id=? AND last_run<>?",(server,channel,run)).fetchone()[0]
            summary["search_engine"] = "fts5" if fts else "substring"
            summary["schema_hash"] = hash_bytes(canonical(schema).encode())
            c.execute("UPDATE runs SET summary=? WHERE id=?",(canonical(summary),run))
        return summary


def observation_state(c, payload):
    row=c.execute("SELECT last_run FROM messages WHERE message_id=?",(payload["message_id"],)).fetchone()
    last_scope=row[0]
    for run in c.execute("SELECT id,summary FROM runs ORDER BY id DESC"):
        summary=json.loads(run["summary"])
        if {"server_id":payload["server_id"],"channel_id":payload["channel_id"]} in summary.get("channel_scopes",[]):
            last_scope=run["id"]
            break
    return {**payload,"last_observed_run":row[0],"latest_channel_capture_run":last_scope,
            "observation_status":"observed" if row[0]==last_scope else "not_observed_in_latest_channel_capture"}


def search(index, query, limit=20, channel=None, sender=None, since=None, until=None):
    if not 1 <= limit <= 100:
        raise ValueError("Limit must be between 1 and 100")
    terms = re.findall(r"\w+", query, re.UNICODE)
    if not terms:
        raise ValueError("Search needs at least one word")
    with closing(open_index(index)) as c:
        fts = c.execute("SELECT value FROM settings WHERE key='search_engine'").fetchone()[0] == "fts5"
        params = []
        if fts:
            join = " JOIN message_fts f ON f.key=m.key"
            where = ["message_fts MATCH ?"]
            params.append(" AND ".join('"'+t+'"' for t in terms))
        else:
            join = " JOIN search_documents sd ON sd.key=m.key"
            where = ["instr(lower(sd.body),lower(?))>0" for _ in terms]
            params.extend(terms)
        for field,value in (("channel_id",channel),("sender_id",sender)):
            if value:
                where.append(f"m.{field}=?")
                params.append(value)
        for op,value in ((">=",since),("<",until)):
            if value:
                dt = datetime.fromisoformat(value.replace("Z","+00:00"))
                if dt.tzinfo is None:
                    dt = dt.replace(tzinfo=timezone.utc)
                where.append(f"m.timestamp{op}?")
                params.append(int(dt.timestamp()*1000))
        sql = "SELECT m.payload FROM messages m"+join+" WHERE "+" AND ".join(where)+" ORDER BY m.timestamp,m.message_id LIMIT ?"
        return [observation_state(c,json.loads(r[0])) for r in c.execute(sql,(*params,limit))]


def context(index, message_id, radius=2):
    if not 0 <= radius <= 10:
        raise ValueError("Context radius must be 0..10")
    with closing(open_index(index)) as c:
        r = c.execute("SELECT * FROM messages WHERE message_id=?",(str(message_id),)).fetchone()
        if r is None:
            raise ValueError("Message not indexed")
        p=json.loads(r["payload"])
        rows=list(c.execute("SELECT payload FROM messages WHERE server_id=? AND channel_id=? ORDER BY timestamp,message_id",(r["server_id"],r["channel_id"])))
        at=next(i for i,x in enumerate(rows) if json.loads(x[0])["message_id"]==str(message_id))
        replies=[]
        for edge in p["reply_to"]:
            target=c.execute("SELECT payload FROM messages WHERE server_id=? AND channel_id=? AND message_id=?",(r["server_id"],r["channel_id"],edge["replied_to_id"])).fetchone()
            replies.append({"target_id":edge["replied_to_id"],"status":"captured" if target else "not_captured",
                            "message":json.loads(target[0]) if target else None})
        return {"message":observation_state(c,p),"replied_to":replies,"chronological_context":[observation_state(c,json.loads(x[0])) for x in rows[max(0,at-radius):at+radius+1]],
                "note":"Chronological neighbors are not necessarily a conversation or an endorsement."}


def history(index, message_id):
    with closing(open_index(index)) as c:
        row=c.execute("SELECT key FROM messages WHERE message_id=?",(str(message_id),)).fetchone()
        if row is None:
            raise ValueError("Message not indexed")
        versions=[]
        previous={}
        for r in c.execute("SELECT * FROM versions WHERE key=? ORDER BY first_run",(row[0],)):
            payload=json.loads(r["payload"])
            changed=[k for k in sorted(set(previous)|set(payload)) if previous.get(k)!=payload.get(k)]
            versions.append({"payload_hash":r["payload_hash"],"first_run":r["first_run"],
                             "changed_fields":changed,"payload":payload})
            previous=payload
        observations=[dict(r) for r in c.execute("SELECT o.run_id,o.payload_hash,r.snapshot_id,r.observed_at FROM observations o JOIN runs r ON r.id=o.run_id WHERE o.key=? ORDER BY o.run_id",(row[0],))]
        return {"versions":versions,"observations":observations,
                "note":"Observed versions only, not the original Discord edit history. Absence from a run is not proof of deletion."}


def entity_search(index, entity_id, limit=20):
    entities=json.loads((ROOT/"world/entities.json").read_text(encoding="utf-8"))["entities"]
    entity=next((e for e in entities if e["id"]==entity_id),None)
    if entity is None:
        raise ValueError("Unknown project entity ID")
    terms=list(dict.fromkeys([entity["display_name"],*entity.get("aliases",[])]))
    hits={}
    for term in terms:
        for p in search(index,term,limit):
            hits[p["message_id"]]=p
    return {"entity_id":entity_id,"aliases_searched":terms,
            "matches":sorted(hits.values(),key=lambda p:(p["timestamp"],int(p["message_id"])))[:limit],
            "note":"Search candidates only. No episode assignment, factual endorsement or documentation edit."}


def queue_import(index, path):
    records=json.loads(Path(path).read_text(encoding="utf-8"))
    with closing(open_index(index,write=True)) as c:
        with c:
            for r in records:
                if r.get("status") != "candidate" or not r.get("source_class") or not r.get("review_note"):
                    raise ValueError("Queue seeds require candidate status, source class and review note")
                sources=[]
                for mid in r["message_ids"]:
                    row=c.execute("SELECT key,payload_hash,payload,last_run FROM messages WHERE message_id=?",(str(mid),)).fetchone()
                    if row is None:
                        raise ValueError("Queue seed cites an unindexed message")
                    p=json.loads(row["payload"])
                    sources.append({"message_id":str(mid),"key":row["key"],"payload_hash":row["payload_hash"],
                                    "run_id":row["last_run"],"url":p["url"]})
                r={**r,"sources":sources}
                c.execute("INSERT OR IGNORE INTO review_queue VALUES(?,?)",(r["id"],canonical(r)))
    return {"seed_candidates":len(records),"policy":"Existing review decisions preserved"}


def queue_records(index):
    with closing(open_index(index)) as c:
        result=[]
        for row in c.execute("SELECT record FROM review_queue ORDER BY id"):
            record=json.loads(row[0])
            changes=[]
            for source in record["sources"]:
                current=c.execute("SELECT payload_hash FROM messages WHERE key=?",(source["key"],)).fetchone()
                if current is None or current[0]!=source["payload_hash"]:
                    changes.append(source["message_id"])
            result.append({**record,"changed_since_review_baseline":changes})
        return result


def review(index, claim_id, status, note, episode=None):
    allowed={"candidate","awaiting-audio","corroborated","disputed","rejected"}
    if status not in allowed or not note.strip():
        raise ValueError("A supported review status and explanatory note are required")
    if episode and (not re.fullmatch(r"E\d{3}(?:\.5)?",episode) or not (ROOT/"episodes"/(episode+".md")).is_file()):
        raise ValueError("Episode must identify an existing corrected episode dossier")
    with closing(open_index(index,write=True)) as c:
        with c:
            row=c.execute("SELECT record FROM review_queue WHERE id=?",(claim_id,)).fetchone()
            if row is None:
                raise ValueError("Unknown review candidate")
            record=json.loads(row[0])
            record.setdefault("review_history",[]).append({"at":now(),"previous_status":record["status"],
                "status":status,"note":note,"episode":episode})
            record["status"]=status
            record["review_note"]=note
            if episode:
                record["corrected_episode"]=episode
            c.execute("UPDATE review_queue SET record=? WHERE id=?",(canonical(record),claim_id))
    return {"id":claim_id,"status":status,"note":"Private review recorded; no project documentation changed."}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index",type=Path,default=DEFAULT_INDEX)
    sub=parser.add_subparsers(dest="command",required=True)
    p=sub.add_parser("ingest",help="Copy quiescent sources, verify schema, reconcile a private index")
    p.add_argument("source",type=Path)
    p.add_argument("--downloads",type=Path)
    p.add_argument("--fallback-search",action="store_true")
    p=sub.add_parser("search",help="Literal word search; all words required")
    p.add_argument("query")
    p.add_argument("--limit",type=int,default=20)
    for flag in ("channel","sender","since","until"):
        p.add_argument("--"+flag)
    p=sub.add_parser("context")
    p.add_argument("message_id")
    p.add_argument("--radius",type=int,default=2)
    p=sub.add_parser("history")
    p.add_argument("message_id")
    p=sub.add_parser("entity")
    p.add_argument("entity_id")
    p.add_argument("--limit",type=int,default=20)
    sub.add_parser("status")
    p=sub.add_parser("seed-queue")
    p.add_argument("file",type=Path)
    sub.add_parser("queue")
    p=sub.add_parser("review",help="Record a private editorial decision; never rewrites documentation")
    p.add_argument("claim_id")
    p.add_argument("--status",required=True,choices=["candidate","awaiting-audio","corroborated","disputed","rejected"])
    p.add_argument("--note",required=True)
    p.add_argument("--episode",help="Existing corrected Wastes dossier ID, after manual crosswalk review")
    args=parser.parse_args()
    if args.command=="ingest":
        result=ingest(args.source,args.index,args.downloads,args.fallback_search)
    elif args.command=="search":
        result=search(args.index,args.query,args.limit,args.channel,args.sender,args.since,args.until)
    elif args.command=="context":
        result=context(args.index,args.message_id,args.radius)
    elif args.command=="history":
        result=history(args.index,args.message_id)
    elif args.command=="entity":
        result=entity_search(args.index,args.entity_id,args.limit)
    elif args.command=="seed-queue":
        result=queue_import(args.index,args.file)
    elif args.command=="review":
        result=review(args.index,args.claim_id,args.status,args.note,args.episode)
    elif args.command=="queue":
        result=queue_records(args.index)
    else:
        with closing(open_index(args.index)) as c:
            if args.command=="status":
                result={"messages":c.execute("SELECT count(*) FROM messages").fetchone()[0],
                        "versions":c.execute("SELECT count(*) FROM versions").fetchone()[0],
                        "review_candidates":c.execute("SELECT count(*) FROM review_queue").fetchone()[0],
                        "latest_run":json.loads(c.execute("SELECT summary FROM runs ORDER BY id DESC LIMIT 1").fetchone()[0])}
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=="__main__":
    try:
        main()
    except (ValueError,sqlite3.Error,OSError) as exc:
        print(f"Discord archive: {exc}",file=sys.stderr)
        sys.exit(1)
