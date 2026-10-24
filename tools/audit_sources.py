#!/usr/bin/env python3
"""Audit supplied SRT sources and record optional original-audio identities."""
from __future__ import annotations
import hashlib
import json
import subprocess
from pathlib import Path
from build_transcripts import ROOT, parse_srt, clock


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as fh:
        while True:
            block = fh.read(2 << 20)
            if not block:
                break
            h.update(block)
    return h.hexdigest()


def audit_srt(path: Path) -> dict:
    cues = parse_srt(path)
    invalid = [c.idx for c in cues if c.end <= c.start]
    overlaps = []
    for prev, c in zip(cues, cues[1:]):
        if c.start < prev.end:
            overlaps.append(c.idx)
    speakers = sorted({c.speaker for c in cues})
    return {
        'file':path.name,
        'bytes':path.stat().st_size,
        'sha256':sha256(path),
        'cues':len(cues),
        'words':sum(len(c.text.split()) for c in cues),
        'first_cue':clock(cues[0].start),
        'last_cue_end':clock(max(c.end for c in cues)),
        'nonpositive_duration_cues':len(invalid),
        'nonpositive_cue_ids':invalid,
        'overlap_pairs':len(overlaps),
        'overlap_second_cue_ids':overlaps,
        'speakers':speakers,
    }


def audio_record(path: Path) -> dict:
    data={'filename':path.name, 'bytes':path.stat().st_size, 'sha256':sha256(path)}
    try:
        output=subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','default=noprint_wrappers=1:nokey=1',str(path)],text=True).strip()
        data['duration_seconds']=float(output)
    except (OSError, subprocess.CalledProcessError, ValueError):
        data['duration_seconds']=None
    return data


def build():
    files=[audit_srt(p) for p in sorted((ROOT/'sources').glob('*.srt'))]
    audios=[]
    for ep in ['E000','E001']:
        for p in sorted(ROOT.parent.glob(f'The Wastes S1{ep}. *.mp3')):
            audios.append(audio_record(p))
    info={
        'project':'The Wastes — first two episodes transcription pilot',
        'archive_stage':'readable-draft, not proofread',
        'source_srt_files':files,
        'source_audio_files_outside_package':audios,
        'audio_included':False,
        'known_user_verified_facts':[
            'Cohere skipped substantial speech in E001.',
            'E001 Nemotron speaker 5 is Scott performing a voice.',
            'E000 final spoken word is Now; subsequent audio is music.'
        ]
    }
    (ROOT/'reports'/'source_manifest.json').write_text(json.dumps(info,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
    rows='\n'.join(f"| {r['file']} | {r['cues']:,} | {r['words']:,} | {r['nonpositive_duration_cues']} | {r['overlap_pairs']} | {r['first_cue']} | {r['last_cue_end']} |" for r in files)
    note='''# SRT source audit

**Scope:** Structural properties of the supplied SRT files. This is **not** a word-accuracy or speaker-correctness measurement. Overlaps may legitimately result from simultaneous speakers; invalid durations should be reviewed. The original MP3 files are excluded from the ZIP but are hashed in `source_manifest.json`.

| Source SRT | Cues | Words | Invalid (end ≤ start) | Overlap pairs | First cue | Last cue end |
|---|---:|---:|---:|---:|---|---|
'''+rows+'''

## Known interpretation

- All `.processed.srt` sources were provided after Subtitle Edit post-processing and automatic speaker name find/replace in some files; they are **not raw recognition outputs**.
- Parakeet `.raw.srt` sources were supplied from a later run with post-processing disabled. Therefore differences between raw and processed files may include inference/run differences.
- Valid subtitle timing does **not** imply words are aligned correctly: the E000 processed final word is visibly placed much later than in the raw file.
- An ASR engine that skips speech may have perfectly valid cue structure. Cohere's verified E001 omissions are a **coverage** issue, not merely an SRT structural error.

## Next testing milestone

Verify against audio a hand-transcribed 20–30-minute sample that includes proper nouns, rapid dialogue, quieter speech and the two known Cohere omissions. Measure WER, omissions and speaker attribution separately for Parakeet and Qwen Q8.
'''
    (ROOT/'reports'/'SRT_AUDIT.md').write_text(note,encoding='utf-8',newline='\n')
    return files,audios

if __name__=='__main__':
    src,audio=build()
    print(f'Analyzed {len(src)} SRT files and {len(audio)} audio files')
    for a in audio:
        print(a['filename'],a.get('duration_seconds'),a['sha256'][:14])
