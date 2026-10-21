#!/usr/bin/env python3
"""Execute one bounded job via a local clip and the inspected CrispASR CLI.

All paths are runtime arguments. Logs/raw exports stay in the chosen local output.
No shell interpolation, auto-download, archive batching, or transcript mutation.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import subprocess
import time

from asr_evidence import interval, load_run
from audit_sources import sha256 as file_hash
from compare_asr import write_json


def commands(job, audio, model, exe, ffmpeg, out, backend='parakeet', gpu='vulkan'):
    start, end = interval([job['start_ms'], job['end_ms']], 'job interval')
    if end-start > 120000 or end > job['audio']['duration_ms']:
        raise ValueError('Execution is restricted to one valid clip of at most 120 seconds')
    clip = out/'clip.wav'
    return [[str(ffmpeg), '-nostdin', '-v', 'error', '-n', '-i', str(audio),
             '-ss', f'{start/1000:.3f}', '-t', f'{(end-start)/1000:.3f}',
             '-ac', '1', '-ar', '16000', '-c:a', 'pcm_s16le', str(clip)],
            [str(exe), '--backend', backend, '--model', str(model), '--language', 'en',
             '--gpu-backend', gpu, '--output-json-full', '--output-srt',
             '--output-file', str(out/'recognition'), str(clip)]]


def execute(job, audio, model, exe, ffmpeg, out, backend='parakeet', gpu='vulkan',
            quantization=None, timeout=180):
    argv = commands(job, audio, model, exe, ffmpeg, out, backend, gpu)
    if not audio.is_file() or not model.is_file():
        raise ValueError('Audio and model must be existing local files')
    expected = job['audio'].get('sha256')
    if not expected or file_hash(audio) != expected:
        raise ValueError('Job audio SHA-256 must match the actual source before execution')
    help_run = subprocess.run([str(exe), '--help'], capture_output=True, text=True,
                              encoding='utf-8', errors='replace', timeout=30, check=True)
    help_text = help_run.stdout + help_run.stderr
    for flag in ('--backend', '--model', '--language', '--gpu-backend', '--output-json-full', '--output-srt', '--output-file'):
        if flag not in help_text:
            raise ValueError(f'Installed CLI does not advertise {flag}')
    version = subprocess.run([str(exe), '--version'], capture_output=True, text=True,
                             encoding='utf-8', errors='replace', timeout=30, check=True)
    out.mkdir(parents=True, exist_ok=False)
    receipt = {'schema_version': 1, 'job': job, 'commands': argv,
               'version': version.stdout + version.stderr, 'status': 'running'}
    write_json(out/'execution.local.json', receipt)
    started = time.perf_counter()
    try:
        for index, command in enumerate(argv):
            stage = time.perf_counter()
            with (out/f'stage-{index}.local.log').open('w', encoding='utf-8') as log:
                subprocess.run(command, stdout=log, stderr=subprocess.STDOUT, check=True, timeout=timeout)
            receipt[f'stage_{index}_seconds'] = round(time.perf_counter()-stage, 3)
        version_match = re.search(r'(?m)^\s*version\s*:\s*(\S+)', receipt['version'])
        revision_match = re.search(r'(?m)^\s*git sha\s*:\s*(\S+)', receipt['version'])
        public_version = ('CrispASR ' + version_match[1] +
                          (' ' + revision_match[1] if revision_match else '')) if version_match else None
        spec = {'id': job['id'] + '-third', 'path': 'recognition.json', 'format': 'crispasr-json',
                'coverage_ms': [job['start_ms'], job['end_ms']], 'timestamp_offset_ms': job['start_ms'],
                'model': model.name, 'version': public_version, 'quantization': quantization,
                'settings': {'backend': backend, 'gpu_backend': gpu, 'language': 'en',
                             'explicit_vad': False, 'explicit_chunking': False,
                             'input': 'FFmpeg mono 16 kHz PCM clip; timestamps relative to clip'},
                'processing_seconds': receipt['stage_1_seconds'],
                'parent_disagreement_ids': job['disagreement_ids']}
        imported = load_run(spec, out, job['episode'], job['audio'])
        if not imported.segments:
            raise ValueError('Recognizer produced no segments; retain output for diagnosis')
        receipt.update({'status': 'complete', 'clip_sha256': file_hash(out/'clip.wav'),
                        'output_sha256': file_hash(out/'recognition.json')})
        write_json(out/'run-spec.json', spec)
    except (OSError, ValueError, subprocess.SubprocessError) as exc:
        receipt.update({'status': 'failed', 'error': str(exc)})
        raise
    finally:
        receipt['total_seconds'] = round(time.perf_counter()-started, 3)
        write_json(out/'execution.local.json', receipt)
    return receipt


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('jobs', type=Path)
    parser.add_argument('--job-id', required=True)
    for name in ('audio', 'model', 'exe', 'out'):
        parser.add_argument('--'+name, required=True, type=Path)
    parser.add_argument('--ffmpeg', type=Path, default=Path('ffmpeg'))
    parser.add_argument('--backend', default='parakeet')
    parser.add_argument('--gpu', default='vulkan')
    parser.add_argument('--quantization')
    parser.add_argument('--execute', action='store_true', help='Default prints an argument-array plan only')
    args = parser.parse_args()
    try:
        jobs = json.loads(args.jobs.read_text(encoding='utf-8'))
        if jobs.get('schema_version') != 1:
            raise ValueError('Unsupported jobs schema')
        matches = [j for j in jobs['jobs'] if j['id'] == args.job_id]
        if len(matches) != 1:
            raise ValueError('Select exactly one existing job ID')
        job = matches[0]
        if args.execute:
            result = execute(job, args.audio, args.model, args.exe, args.ffmpeg, args.out,
                             args.backend, args.gpu, args.quantization)
            print(json.dumps({'status': result['status'], 'total_seconds': result['total_seconds']}))
        else:
            print(json.dumps(commands(job, args.audio, args.model, args.exe, args.ffmpeg,
                                      args.out, args.backend, args.gpu), indent=2))
    except (ValueError, KeyError, OSError, subprocess.SubprocessError) as exc:
        parser.exit(2, f'Job failed: {exc}\n')


if __name__ == '__main__':
    main()
