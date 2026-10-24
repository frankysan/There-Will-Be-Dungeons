#!/usr/bin/env python3
"""Regression checks for deterministic, non-destructive transcript rendering."""
from __future__ import annotations
import json
import re
from build_transcripts import FILES, ROOT, parse_srt


def main():
    for ep, meta in FILES.items():
        cues=parse_srt(ROOT/'sources'/meta['input'])
        turns=json.loads((ROOT/'transcripts'/f'{ep}.turns.json').read_text())['turns']
        expected=' '.join(c.text for c in cues if c.text)
        produced=' '.join(t['text'] for t in turns)
        assert expected==produced, f'Word text changed or lost for {ep}'
        assert turns[0]['first_cue']==cues[0].idx
        assert turns[-1]['last_cue']==cues[-1].idx
        for t in turns:
            assert t['first_cue'] <= t['last_cue']
            assert t['start_ms'] < t['end_ms']
            assert t['speaker'] in {'Scott','Beau','Kristen','John','Kyle'},(ep,t['speaker'])
        if ep=='E001':
            assert all(t['speaker']!='speaker 5' for t in turns)
            assert any(c.speaker=='speaker 5' for c in cues)
        assert '# '+ep in (ROOT/'transcripts'/f'{ep}.readable-draft.md').read_text()
        print(f'PASS {ep}: {len(cues)} source cues; {len(turns)} turns; exact word coverage')

    # Ensure project Markdown links to actual local files (ignore external URLs).
    markdown=list(ROOT.rglob('*.md'))
    bad=[]
    for md in markdown:
        for url in re.findall(r'\[[^]]+\]\(([^)]+)\)',md.read_text(encoding='utf-8')):
            if url.startswith(('http:','https:','#','mailto:')):
                continue
            target=(md.parent/url.split('#',1)[0]).resolve()
            if not target.exists():
                bad.append((md.relative_to(ROOT).as_posix(),url))
    assert not bad, f'Broken relative links: {bad}'
    print(f'PASS links: {len(markdown)} Markdown documents')

if __name__=='__main__':
    main()
