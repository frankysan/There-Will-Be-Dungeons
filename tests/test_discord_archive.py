"""Synthetic archives only: never reads the private Discord collection."""
import importlib.util
from contextlib import contextmanager
import json
from pathlib import Path
import sqlite3
import tempfile
import unittest
from unittest.mock import patch

SPEC=importlib.util.spec_from_file_location("discord_archive",Path(__file__).resolve().parents[1]/"tools/discord_archive.py")
assert SPEC is not None and SPEC.loader is not None
archive=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(archive)

MID=9007199254741011
REPLY=MID+1


@contextmanager
def database(path):
    c=sqlite3.connect(path)
    try:
        with c:
            yield c
    finally:
        c.close()


def fixture(path):
    c=sqlite3.connect(path)
    integers={"id","server","parent_id","position","nsfw","message_id","sender_id","channel_id",
              "timestamp","replied_to_id","edit_timestamp","attachment_id","size","width","height",
              "emoji_id","emoji_flags","count"}
    for table,columns in archive.REQUIRED.items():
        declarations=','.join('"'+col+'" '+('INTEGER' if col in integers else 'TEXT') for col in columns.split())
        c.execute(f'CREATE TABLE "{table}"({declarations})')
    c.execute("INSERT INTO metadata VALUES('version','11')")
    c.execute("INSERT INTO servers(id,name,type) VALUES(12,'Synthetic','SERVER')")
    c.execute("INSERT INTO channels(id,server,name) VALUES(34,12,'fixture')")
    c.execute("INSERT INTO users(id,name) VALUES(56,'synthetic-author')")
    c.executemany("INSERT INTO messages VALUES(?,?,?,?,?)",[(MID,56,34,"Copper dragon rules",1000),(REPLY,56,34,"Reply to dragon",2000)])
    c.execute("INSERT INTO message_replied_to VALUES(?,?)",(REPLY,MID))
    c.execute("INSERT INTO attachments(attachment_id,name,normalized_url,size,type) VALUES(78,'synthetic.png','local:fixture',99,'image/png')")
    c.execute("INSERT INTO message_attachments VALUES(?,78)",(MID,))
    c.execute("INSERT INTO message_reactions VALUES(?,NULL,'test',0,1)",(MID,))
    c.commit()
    c.close()


class DiscordArchiveTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base=Path(self.tmp.name)
        self.source=self.base/"input.dht"
        self.index=self.base/"private/research.sqlite"
        fixture(self.source)

    def mutate(self,sql,params=()):
        with database(self.source) as c:
            c.execute(sql,params)

    def test_idempotent_import_ids_links_and_source_immutability(self):
        before=archive.source_inventory(self.source,None)
        first=archive.ingest(self.source,self.index)
        second=archive.ingest(self.source,self.index)
        self.assertEqual((first["new"],second["new"],second["changed"],second["unchanged"]),(2,0,0,2))
        self.assertEqual(first["snapshot_id"],second["snapshot_id"])
        hit=archive.search(self.index,"copper dragon")[0]
        self.assertEqual(hit["message_id"],str(MID))
        self.assertEqual(hit["author"]["id"],"56")
        self.assertEqual(hit["url"],f"https://discord.com/channels/12/34/{MID}")
        self.assertEqual(archive.source_inventory(self.source,None),before)
        self.assertEqual(len(archive.history(self.index,MID)["versions"]),1)
        self.assertEqual(len(archive.history(self.index,MID)["observations"]),2)

    def test_older_edits_backfill_absence_and_reappearance(self):
        archive.ingest(self.source,self.index)
        self.mutate("UPDATE messages SET text='Silver wyrm corrected' WHERE message_id=?",(MID,))
        self.mutate("INSERT INTO message_edit_timestamps VALUES(?,5000)",(MID,))
        self.mutate("INSERT INTO messages VALUES(?,56,34,'Older backfill',500)",(MID-1,))
        self.mutate("DELETE FROM messages WHERE message_id=?",(REPLY,))
        result=archive.ingest(self.source,self.index)
        self.assertEqual((result["new"],result["changed"],result["not_observed"]),(1,1,1))
        self.assertEqual(archive.search(self.index,"Copper"),[])
        self.assertEqual(archive.search(self.index,"Silver")[0]["message_id"],str(MID))
        self.assertTrue(archive.context(self.index,REPLY)["message"])
        versions=archive.history(self.index,MID)["versions"]
        self.assertEqual(len(versions),2)
        self.assertIn("text",versions[1]["changed_fields"])
        self.mutate("UPDATE messages SET text='Copper dragon rules' WHERE message_id=?",(MID,))
        self.mutate("DELETE FROM message_edit_timestamps")
        archive.ingest(self.source,self.index)
        history=archive.history(self.index,MID)
        self.assertEqual(len(history["versions"]),2)
        self.assertEqual(history["observations"][0]["payload_hash"],history["observations"][-1]["payload_hash"])

    def test_missing_reply_and_context(self):
        self.mutate("UPDATE message_replied_to SET replied_to_id=123456")
        result=archive.ingest(self.source,self.index)
        self.assertEqual(result["missing_reply_targets"],1)
        ctx=archive.context(self.index,REPLY)
        self.assertEqual(ctx["replied_to"][0]["status"],"not_captured")
        self.assertEqual(len(ctx["chronological_context"]),2)

    def test_download_variants_are_hashed_and_versioned(self):
        dl=self.base/"input.dht_downloads"
        with database(dl) as c:
            c.executescript('CREATE TABLE download_metadata(normalized_url TEXT,download_url TEXT,status INTEGER,type TEXT,size INTEGER); CREATE TABLE download_blobs(normalized_url TEXT,blob BLOB);')
            c.execute("INSERT INTO download_metadata VALUES('local:fixture','local:fixture',200,'image/png',3)")
            c.execute("INSERT INTO download_blobs VALUES('local:fixture',?)",(b'abc',))
        archive.ingest(self.source,self.index,dl)
        p=archive.context(self.index,MID)["message"]
        a=p["attachments"][0]
        self.assertEqual(a["size"],99)
        self.assertEqual(a["download"]["actual_bytes"],3)
        self.assertEqual(a["download"]["blob_hash"],archive.hash_bytes(b'abc'))
        with database(dl) as c:
            c.execute("UPDATE download_blobs SET blob=?",(b'xyz',))
        result=archive.ingest(self.source,self.index,dl)
        self.assertEqual(result["changed"],1)
        self.assertEqual(len(archive.history(self.index,MID)["versions"]),2)

    def test_reaction_only_change_detected(self):
        archive.ingest(self.source,self.index)
        self.mutate("UPDATE message_reactions SET count=7")
        result=archive.ingest(self.source,self.index)
        self.assertEqual(result["changed"],1)
        self.assertIn("reactions",archive.history(self.index,MID)["versions"][1]["changed_fields"])

    def test_wal_snapshot_reads_committed_wal_without_source_changes(self):
        c=sqlite3.connect(self.source)
        self.addCleanup(c.close)
        c.execute("PRAGMA journal_mode=WAL")
        c.execute("UPDATE messages SET text='Committed WAL content' WHERE message_id=?",(MID,))
        c.commit()
        self.assertGreater(Path(str(self.source)+"-wal").stat().st_size,0)
        before=archive.source_inventory(self.source,None)
        archive.ingest(self.source,self.index)
        self.assertEqual(archive.search(self.index,"committed")[0]["message_id"],str(MID))
        self.assertEqual(before,archive.source_inventory(self.source,None))

    def test_unknown_schema_rejected_without_migrating(self):
        self.mutate("UPDATE metadata SET value='999' WHERE key='version'")
        before=archive.hash_file(self.source)
        with self.assertRaisesRegex(ValueError,"format 11"):
            archive.ingest(self.source,self.index)
        self.assertFalse(self.index.exists())
        self.assertEqual(archive.hash_file(self.source),before)

    def test_changed_copy_rejected(self):
        original=archive.shutil.copy2
        def change(src,dst):
            original(src,dst)
            Path(dst).write_bytes(b'not the source')
        with patch.object(archive.shutil,"copy2",side_effect=change):
            with self.assertRaisesRegex(ValueError,"changed during copying"):
                archive.ingest(self.source,self.index)
        self.assertFalse(self.index.exists())

    def test_fallback_search_literal_terms_and_filters(self):
        archive.ingest(self.source,self.index,fallback=True)
        self.assertEqual(len(archive.search(self.index,'dragon',channel='34',sender='56',since='1970-01-01',until='1970-01-02')),2)
        self.assertEqual(archive.search(self.index,'dragon',channel='99'),[])
        self.assertEqual(archive.search(self.index,'"dragon" OR nonexistent'),[])
        with self.assertRaises(ValueError):
            archive.search(self.index,'***')

    def test_refuse_source_as_destination_and_public_output(self):
        before=archive.hash_file(self.source)
        with self.assertRaises(ValueError):
            archive.ingest(self.source,self.source)
        with self.assertRaises(ValueError):
            archive.private_path(archive.ROOT/'reports/private.sqlite')
        with self.assertRaises(ValueError):
            archive.ingest(self.source,self.base/'input.dht',fallback=True)
        self.assertEqual(archive.hash_file(self.source),before)

    def test_queue_idempotent_and_does_not_overwrite_decisions(self):
        archive.ingest(self.source,self.index)
        seed=self.base/'queue.json'
        seed.write_text(json.dumps([{'id':'synthetic-claim','message_ids':[str(MID)],'status':'candidate',
                                    'source_class':'participant-recollection','review_note':'Check synthetic episode.'}]))
        archive.queue_import(self.index,seed)
        with database(self.index) as c:
            record=json.loads(c.execute('SELECT record FROM review_queue').fetchone()[0])
            self.assertEqual(record['sources'][0]['message_id'],str(MID))
            record['status']='disputed'
            c.execute('UPDATE review_queue SET record=?',(json.dumps(record),))
        archive.queue_import(self.index,seed)
        with database(self.index) as c:
            self.assertEqual(json.loads(c.execute('SELECT record FROM review_queue').fetchone()[0])['status'],'disputed')
        archive.review(self.index,'synthetic-claim','awaiting-audio','Synthetic listening check required.')
        record=archive.queue_records(self.index)[0]
        self.assertEqual(record['status'],'awaiting-audio')
        self.assertEqual(len(record['review_history']),1)
        self.mutate("UPDATE messages SET text='Changed underlying evidence' WHERE message_id=?",(MID,))
        archive.ingest(self.source,self.index)
        self.assertEqual(archive.queue_records(self.index)[0]['changed_since_review_baseline'],[str(MID)])

    def test_snapshot_tampering_rejected(self):
        result=archive.ingest(self.source,self.index)
        folder=self.index.parent/'snapshots'/result['snapshot_id']
        (folder/'archive').write_bytes(b'tampered')
        with self.assertRaisesRegex(ValueError,'snapshot bytes changed'):
            archive.ingest(self.source,self.index)

    def test_empty_channel_snapshot_keeps_messages_without_claiming_deletion(self):
        archive.ingest(self.source,self.index)
        self.mutate('DELETE FROM messages')
        result=archive.ingest(self.source,self.index)
        self.assertEqual(result['not_observed'],2)
        hits=archive.search(self.index,'dragon')
        self.assertEqual(len(hits),2)
        self.assertEqual(hits[0]['observation_status'],'not_observed_in_latest_channel_capture')

    def test_fts_literal_terms_and_filters(self):
        result=archive.ingest(self.source,self.index)
        self.assertIn(result['search_engine'],('fts5','substring'))
        self.assertEqual(len(archive.search(self.index,'Copper dragon',channel='34',sender='56')),1)
        self.assertEqual(archive.search(self.index,'dragon',until='1970-01-01'),[])
        self.assertEqual(archive.search(self.index,'"dragon" OR nonexistent'),[])

    def test_search_includes_attachment_names_and_embed_titles(self):
        self.mutate('INSERT INTO message_embeds VALUES(?,?)',(MID,json.dumps({'title':'Synthetic compass','fields':[{'name':'Test field','value':'Astral needle'}]})))
        archive.ingest(self.source,self.index)
        self.assertEqual(archive.search(self.index,'synthetic png')[0]['message_id'],str(MID))
        self.assertEqual(archive.search(self.index,'compass')[0]['message_id'],str(MID))
        self.assertEqual(archive.search(self.index,'Astral needle')[0]['message_id'],str(MID))

    def test_version_three_evidence_edges_preserve_existing_entity_lookup(self):
        """Synthetic Discord archive only; preserve the 18-ID v2 pilot prefix."""
        data=json.loads((archive.ROOT/"world/entities.json").read_text(encoding="utf-8"))
        self.assertEqual(data["version"],3)
        self.assertEqual(data["stage"],"evidence-edges-cohort")
        self.assertEqual(data["source_scope_policy"],"cited-episodes-only")
        records=data["entities"]
        ids=[record["id"] for record in records]
        original_ids=[
            "character.nash","character.hope","character.stanley","character.vorel",
            "npc.softhead","npc.hillmaster","npc.gimster","npc.shun_t",
            "place.dust_hill","place.blood_canyons","place.solar_mines",
            "place.verithica","place.caegro","tech.dragon_engines",
            "world.dark_pact","organization.hill_guard",
            "race.lizardfolk","race.tieflings",
        ]
        new_ids=[
            "race.dwarves","race.elves","race.harlequinari",
            "race.illithids","race.orcs","race.pixies",
        ]
        graph_ids=[
            "npc.p0d","character.blood_skunk","npc.delit_ornath",
            "tech.mask_of_eltanfawr",
        ]
        self.assertEqual(ids,original_ids+new_ids+graph_ids)
        self.assertEqual(len(ids),28)
        self.assertEqual(len(set(ids)),len(ids))
        by_id={record["id"]:record for record in records}

        cited=[source["episode"] for record in records for source in record["sources"]]
        self.assertEqual(set(data["source_scope"]),set(cited))
        self.assertEqual(len(data["source_scope"]),len(set(data["source_scope"])))
        known_types={
            "person_character","person_npc","place","artifact_or_technology",
            "organization","world_concept","race_culture",
        }
        for record in records:
            self.assertIn(record["type"],known_types)
            self.assertTrue(record["display_name"])
            self.assertEqual(len(record["aliases"]),len(set(record["aliases"])))
            self.assertNotIn(record["display_name"],record["aliases"])
            for source in record["sources"]:
                self.assertTrue((archive.ROOT/"episodes"/(source["episode"]+".md")).is_file())
                self.assertRegex(source["time"],r"^\d{2}:\d{2}:\d{2}$")
                self.assertTrue(source["evidence_type"])
            if "page_path" in record:
                page=Path(record["page_path"])
                self.assertFalse(page.is_absolute())
                self.assertNotIn("..",page.parts)
                self.assertTrue((archive.ROOT/page).is_file())
            seen_relations=set()
            for edge in record.get("relations",[]):
                self.assertIn(edge["entity_id"],by_id)
                key=(edge["relation"],edge["entity_id"])
                self.assertNotIn(key,seen_relations)
                seen_relations.add(key)

        for race_id,person_id in (
            ("race.lizardfolk","character.vorel"),("race.tieflings","character.hope")
        ):
            self.assertEqual(by_id[race_id]["relations"],[
                {"relation":"documented_individual","entity_id":person_id},
            ])
            self.assertEqual(by_id[person_id]["type"],"person_character")
        self.assertEqual(by_id["character.stanley"]["display_name"],"Stanley Billings")
        self.assertEqual(by_id["character.stanley"]["aliases"],[
            "Stanley","Valiir Or'Nath",
        ])
        self.assertEqual(by_id["npc.gimster"]["display_name"],"Jimster")
        self.assertEqual(by_id["place.dust_hill"]["display_name"],"Dusthill")

        for race_id in new_ids:
            race=by_id[race_id]
            self.assertEqual(race["type"],"race_culture")
            self.assertEqual(race["name_status"],"known_label")
            expected_members={
                "race.harlequinari":"character.blood_skunk",
                "race.pixies":"npc.p0d",
            }
            expected=(
                [{"relation":"documented_individual",
                  "entity_id":expected_members[race_id]}]
                if race_id in expected_members else []
            )
            self.assertEqual(race.get("relations",[]),expected)
            self.assertGreaterEqual(len(race["sources"]),1)
            self.assertGreaterEqual(len(race["questions"]),1)
            self.assertEqual(race["page_path"],"world/races/"+race_id.removeprefix("race.")+".md")

        self.mutate("UPDATE messages SET text=? WHERE message_id=?",(
            "Vorel lizardfolk Hope Tieflings Valiir Or'Nath Dwarves Elves "
            "Harlequinari Illithids Mind flayers Orcs Pixies P0D "
            "Blood Skunk Hendrickson Delit Or'Nath Mask of Eltanfawr",MID))
        archive.ingest(self.source,self.index,fallback=True)
        for entity_id in (
            "character.vorel","character.hope","character.stanley",
            "race.lizardfolk","race.tieflings",*new_ids,*graph_ids,
        ):
            result=archive.entity_search(self.index,entity_id)
            self.assertEqual(result["entity_id"],entity_id)
            self.assertIn(str(MID),[hit["message_id"] for hit in result["matches"]])
        self.assertIn("Valiir Or'Nath",
                      archive.entity_search(self.index,"character.stanley")["aliases_searched"])
        self.assertIn("Mind flayers",
                      archive.entity_search(self.index,"race.illithids")["aliases_searched"])
        with self.assertRaisesRegex(ValueError,"Unknown project entity ID"):
            archive.entity_search(self.index,"race.unknown")
        self.assertEqual(by_id["npc.p0d"]["page_path"],"world/characters/p0d.md")
        self.assertEqual(by_id["character.blood_skunk"]["page_path"],
                         "world/characters/blood-skunk-hendrickson.md")
        self.assertEqual(by_id["tech.mask_of_eltanfawr"]["page_path"],
                         "world/technology/mask-of-eltanfawr.md")
        self.assertEqual(by_id["npc.delit_ornath"]["display_name"],"Delit Or'Nath")

        edges=data["evidence_edges"]
        self.assertEqual(len(edges),4)
        edge_ids=[edge["id"] for edge in edges]
        self.assertEqual(len(edge_ids),len(set(edge_ids)))
        self.assertEqual([edge["kind"] for edge in edges],[
            "membership_evidence","membership_evidence",
            "kinship_evidence","custody_event",
        ])
        expected_links={
            "race.pixies":("npc.p0d","documented_individual"),
            "race.harlequinari":("character.blood_skunk","documented_individual"),
            "character.stanley":("npc.delit_ornath","child_of"),
        }
        for edge in edges:
            self.assertIn(edge["subject_id"],by_id)
            self.assertEqual(edge["episode"] in data["source_scope"],True)
            self.assertTrue((archive.ROOT/"episodes"/(edge["episode"]+".md")).is_file())
            self.assertRegex(edge["time"],r"^\d{2}:\d{2}:\d{2}$")
            self.assertTrue(edge["certainty"])
            self.assertTrue(edge["note"])
            if edge["kind"]=="custody_event":
                self.assertEqual(edge["relation"],"physical_transfer")
                self.assertEqual(edge["temporal_scope"],"at_event_only")
                self.assertEqual(edge["subject_id"],"tech.mask_of_eltanfawr")
                self.assertEqual(edge["from_entity_id"],"character.stanley")
                self.assertEqual(edge["to_entity_id"],"character.hope")
                self.assertNotIn("object_id",edge)
            else:
                self.assertNotIn("temporal_scope",edge)
                self.assertNotIn("from_entity_id",edge)
                self.assertNotIn("to_entity_id",edge)
                self.assertIn(edge["object_id"],by_id)
                self.assertEqual((edge["object_id"],edge["relation"]),
                                 expected_links[edge["subject_id"]])
            if edge["kind"]=="membership_evidence":
                subject=by_id[edge["subject_id"]]
                self.assertEqual(subject["type"],"race_culture")
                self.assertIn(
                    {"relation":"documented_individual","entity_id":edge["object_id"]},
                    subject["relations"],
                )
            if edge["kind"]=="kinship_evidence":
                self.assertEqual(edge["subject_id"],"character.stanley")
                self.assertEqual(edge["object_id"],"npc.delit_ornath")
                self.assertEqual(edge["certainty"],
                                 "owner_confirmed_written_name_and_played_family_discussion")
        self.assertEqual({(e["episode"],e["time"]) for e in edges},{
            ("E031","01:55:00"),("E113","02:22:00"),
            ("E115","01:19:00"),("S3E18","02:15:00"),
        })


if __name__=='__main__':
    unittest.main()
