#!/usr/bin/env python3
"""Compare raw Qwen variants: recognition, SRT timing, and speaker attribution.

Dependencies: pip install rapidfuzz
Run: python tools/evaluate_qwen_variants.py
This is NOT an accuracy/word error rate benchmark without a verified reference.
"""
from __future__ import annotations
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from rapidfuzz.distance import Levenshtein
from build_transcripts import ROOT,parse_srt

WORD=re.compile(r"[a-z0-9]+(?:['’][a-z0-9]+)*")

def words_and_speakers(cues):
    items=[]
    for cue in cues:
        for word in WORD.findall(cue.text.lower()):
            items.append((word,cue.speaker))
    return items

def audit(episode,model):
    path=ROOT/'sources'/f'{episode}.qwen-{model}.raw.srt'
    cues=parse_srt(path)
    pairs=words_and_speakers(cues)
    return {
        'filename':path.name,
        'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
        'cue_count':len(cues),
        'word_count':len(pairs),
        'words_sha256':hashlib.sha256(' '.join(w for w,_ in pairs).encode()).hexdigest(),
        'nonpositive_cues':sum(c.end<=c.start for c in cues),
        'adjacent_cue_overlaps':sum(a.end>b.start for a,b in zip(cues,cues[1:])),
        'first_cue_ms':cues[0].start,
        'last_cue_end_ms':cues[-1].end,
        'speaker_counts_by_cue':dict(Counter(c.speaker for c in cues)),
    }, cues, pairs

def main():
    comparison={}
    for episode in ('E000','E001'):
        variants={name:audit(episode,name) for name in ('q4','q4+canary-ctc','q8')}
        normal,canary,q8=(variants[name][2] for name in variants)
        assert [w for w,_ in normal]==[w for w,_ in canary],f'{episode}: aligner changed word sequence'
        atext=' '.join(c.text for c in variants['q4'][1])
        btext=' '.join(c.text for c in variants['q4+canary-ctc'][1])
        assert atext==btext,f'{episode}: aligner changed raw textual content'
        speaker_mismatch=sum(a[1]!=b[1] for a,b in zip(normal,canary))
        a,b=[w for w,_ in normal],[w for w,_ in q8]
        word_edit=Levenshtein.distance(a,b)
        edit_types=Counter(e.tag for e in Levenshtein.editops(a,b))
        comparison[episode]={
            'variants':{name:stat for name,(stat,_,_) in variants.items()},
            'q4_versus_canary':{
                'word_sequence_identical':True,
                'full_concatenated_text_identical':True,
                'speaker_id_mismatched_word_positions':speaker_mismatch,
                'speaker_id_mismatch_fraction':speaker_mismatch/len(normal),
                'note':'Speaker IDs assigned per subtitle cue; resegmentation changes word-level attribution.'},
            'q4_versus_q8':{'levenshtein_word_edits':word_edit,
                            'normalized_by_longer_word_count':word_edit/max(len(a),len(b)),
                            'edit_types':dict(edit_types),
                            'note':'Disagreement, not WER; neither output is an independently verified reference.'}
        }
    target=ROOT/'reports'/'QWEN_VARIANTS.json'
    target.write_text(json.dumps(comparison,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
    print('PASS exact text preservation between Q4 and Q4+Canary in both episodes')
    for ep,v in comparison.items():
        print(ep,'Q4-Q8 word edits',v['q4_versus_q8']['levenshtein_word_edits'],
              'speaker-id word mismatches Q4-Canary',v['q4_versus_canary']['speaker_id_mismatched_word_positions'])
    return comparison

if __name__=='__main__':main()
