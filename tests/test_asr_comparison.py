"""Synthetic integrity/regression tests; no recognizer or audio dependencies."""
from dataclasses import replace
import hashlib
import json
from pathlib import Path
import sys
import subprocess
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from asr_alignment import align
from asr_evidence import Run, Word, load_run, load_manifest
from asr_reference_metrics import error_rates, evaluate
from compare_asr import compare, make_jobs, reconcile, run_comparison, validate_report
from run_asr_job import commands, execute

AUDIO = {'id': 'test-audio', 'sha256': 'a'*64, 'duration_ms': 100000,
         'identity_evidence': 'synthetic fixture'}
META = {'model': 'test', 'version': None, 'quantization': None, 'settings': {},
        'processing_seconds': None}


def run(name, text, times=None, speaker=None):
    words = text.split()
    if times is None:
        times = [(i*1000, i*1000+400) for i in range(len(words))]
    return Run(name, 'TEST', AUDIO, [0, 100000], dict(META), {'sha256': name},
               [Word(f'w{i}', w, w.lower().strip('.,!?'), f's{i}', 0, len(w), a, b,
                     'word' if a is not None and b is not None else 'unknown', speaker)
                for i, (w, (a, b)) in enumerate(zip(words, times))],
               [{'id': f's{i}', 'text': w, 'tokens': [], 'start_ms': a, 'end_ms': b}
                for i, (w, (a, b)) in enumerate(zip(words, times))])


def spec(name, path, fmt='crispasr-json'):
    return {'id': name, 'path': path, 'format': fmt, 'coverage_ms': [0, 100000], **META}


class AlignmentTests(unittest.TestCase):
    def assert_preserved(self, a, b, ops):
        self.assertCountEqual([w.id for _, aa, _, _ in ops for w in aa], [w.id for w in a.words])
        self.assertCountEqual([w.id for _, _, bb, _ in ops for w in bb], [w.id for w in b.words])

    def test_perfect_agreement_punctuation_and_case(self):
        a, b = run('a', 'Hi, yeah! no.'), run('b', 'hi yeah no')
        report = compare([a, b], 'a')
        self.assertEqual(report['counts'], {})
        self.assertEqual(report['pairs'][0]['agreement_word_pairs'], 3)

    def test_single_and_multiword_omissions(self):
        for text, times, missing in [('one three', [(0, 400), (2000, 2400)], 'two'),
                                     ('one', [(0, 400)], 'two three')]:
            a, b = run('a', 'one two three'), run('b', text, times)
            report = compare([a, b], 'a')
            rec = next(r for r in report['disagreements'] if r['classification'] == 'possible_omission')
            self.assertEqual(rec['sources'][0]['lexical_text'], missing)
            self.assertFalse(rec['audio_verified'])

    def test_substitution(self):
        report = compare([run('a', 'hi kyle'), run('b', 'hi scott')], 'a')
        self.assertEqual(report['counts']['conflicting_recognition'], 1)

    def test_genuine_repetitions_remain(self):
        a, b = run('a', 'if if yeah no hi'), run('b', 'if if yeah no hi')
        self.assertEqual(compare([a, b], 'a')['counts'], {})
        b = run('b', 'if yeah no hi', [(1000, 1400), (2000, 2400), (3000, 3400), (4000, 4400)])
        self.assertEqual(compare([a, b], 'a')['counts']['possible_omission'], 1)

    def test_duplicate_is_flagged_not_removed(self):
        a = run('a', 'if if', [(1000, 1240), (1010, 1250)])
        b = run('b', 'if', [(1000, 1240)])
        report = compare([a, b], 'a')
        self.assertTrue(any('possible boundary duplicate' in str(r['diagnostics']) for r in report['disagreements']))
        self.assertEqual(len(report['runs'][0]['words']), 2)

    def test_drift_and_distant_repeated_phrases(self):
        a = run('a', 'yes i do yes i do', [(i*1000, i*1000+200) for i in (1, 2, 3, 80, 81, 82)])
        b = run('b', 'yes i do', [(81000, 81200), (82000, 82200), (83000, 83200)])
        ops, _ = align(a.words, b.words)
        matched = [w.start_ms for kind, aa, _, _ in ops if kind == 'agreement' for w in aa]
        self.assertEqual(matched, [80000, 81000, 82000])
        self.assert_preserved(a, b, ops)

    def test_segmentation_equivalence_is_uncertain(self):
        a, b = run('a', 'dusthill'), run('b', 'dust hill', [(0, 300), (300, 400)])
        report = compare([a, b], 'a')
        self.assertEqual(report['counts'], {'uncertain_segmentation': 1})

    def test_overlap_and_conflicting_speakers(self):
        a = run('a', 'yeah hi no', [(0, 700), (300, 500), (800, 900)], speaker='speaker 0')
        b = run('b', 'yeah hi no', [(0, 700), (300, 500), (800, 900)], speaker='speaker 8')
        report = compare([a, b], 'a')
        self.assertEqual(report['pairs'][0]['agreement_word_pairs'], 3)
        self.assertTrue(report['counts']['boundary_anomaly'])
        self.assertNotIn('conflicting_recognition', report['counts'])
        reordered = run('c', 'hi yeah no', [(300, 500), (0, 700), (800, 900)])
        ops, _ = align(a.words, reordered.words)
        self.assert_preserved(a, reordered, ops)

    def test_unknown_timing_remains_unlocated(self):
        a, b = run('a', 'hi', [(None, None)]), run('b', 'no', [(None, None)])
        report = compare([a, b], 'a')
        jobs = make_jobs(report)
        self.assertFalse(jobs['jobs'])
        self.assertEqual(len(jobs['unlocated_disagreement_ids']), len(report['disagreements']))

    def test_invalid_timing_and_clip_coverage(self):
        a = run('a', 'hi no', [(-100, 200), (1000, 500)])
        b = run('b', 'hi no', [(0, 200), (500, 1000)])
        self.assertGreaterEqual(compare([a, b], 'a')['counts']['boundary_anomaly'], 2)
        full = run('full', 'hi no later', [(0, 200), (500, 1000), (60000, 61000)])
        clip = run('clip', 'hi no', [(0, 200), (500, 1000)])
        clip.coverage_ms = [0, 2000]
        report = compare([full, clip], 'full')
        self.assertEqual(report['counts'], {})
        self.assertEqual(report['pairs'][0]['word_counts'], [2, 2])

    def test_low_probability_is_suspicion_not_truth(self):
        a, b = run('a', 'noise hi'), run('b', 'hi', [(1000, 1400)])
        a.words[0].confidence = .1
        report = compare([a, b], 'a')
        self.assertEqual(report['counts']['possible_hallucination'], 1)
        self.assertTrue(all(not r['audio_verified'] for r in report['disagreements']))

    def test_scaling_60000_words_and_divergent_blocks(self):
        # Several-hour sequence. Check computational bounds, not flaky timing limits.
        a = run('a', ' '.join(f'word{i}' for i in range(60000)))
        b = run('b', ' '.join(f'word{i}' for i in range(60000)))
        ops, stats = align(a.words, b.words, max_tokens=64)
        self.assert_preserved(a, b, ops)
        self.assertLess(stats['dp_cells'], 100)
        a, b = run('a', ' '.join(['hi']*2400)), run('b', ' '.join(['no']*2400))
        ops, stats = align(a.words, b.words, max_tokens=64)
        self.assertLessEqual(stats['max_dp_cells'], 64*64)
        self.assertGreater(stats['fallback_blocks'], 0)
        self.assert_preserved(a, b, ops)
        self.assertTrue(all(notes for _, _, _, notes in ops))

    def test_coarse_cue_anchors_and_missing_long_timing(self):
        text = ' '.join(f'word{i}' for i in range(600))
        a = run('a', text, [(0, 90000)] * 600)
        a.words = [replace(w, timing='cue') for w in a.words]
        b = run('b', text, [(i*140, i*140+100) for i in range(600)])
        ops, stats = align(b.words, a.words, max_tokens=64)
        self.assert_preserved(b, a, ops)
        self.assertEqual(stats['fallback_blocks'], 0)
        self.assertTrue(all(kind == 'agreement' for kind, _, _, _ in ops))
        a.words = [replace(w, start_ms=None, end_ms=None, timing='unknown') for w in a.words]
        ops, stats = align(a.words, b.words, max_tokens=64)
        self.assert_preserved(a, b, ops)
        self.assertLessEqual(stats['max_dp_cells'], 64*64)

    def test_opening_scope_excludes_late_anomalies(self):
        a = run('a', 'hi later', [(0, 400), (80000, 70000)])
        b = run('b', 'hi later', [(0, 400), (70000, 80000)])
        full = compare([a, b], 'a')
        opening = compare([a, b], 'a', comparison_coverage_ms=[0, 10000])
        self.assertIn('boundary_anomaly', full['counts'])
        self.assertEqual(opening['counts'], {})
        self.assertEqual(opening['pairs'][0]['word_counts'], [1, 1])
        clip = run('clip', 'hi edge', [(0, 400), (10100, 10800)])
        clip.coverage_ms = [0, 10000]
        boundary = compare([clip, b], 'clip', comparison_coverage_ms=[0, 10000])
        self.assertTrue(any('outside declared run coverage' in str(r['diagnostics'])
                            for r in boundary['disagreements']))

    def test_third_clip_retains_original_pair_evidence(self):
        a, b = run('a', 'hi yeah no'), run('b', 'hi yes no')
        third = run('third', 'yeah', [(1000, 1400)])
        third.coverage_ms = [900, 1500]
        pair = compare([a, b], 'a')
        triple = compare([a, b, third], 'a')
        key = pair['disagreements'][0]['id']
        retained = next(r for r in triple['disagreements'] if r['id'] == key)
        self.assertEqual(retained['sources'][:2], pair['disagreements'][0]['sources'])
        self.assertEqual(retained['sources'][2]['role'], 'context_only')
        self.assertEqual(len(triple['runs']), 3)

    def test_resynchronizes_after_long_divergence(self):
        a = run('a', 'start phrase here ' + ' '.join(['missing']*400) + ' recover phrase now')
        b = run('b', 'start phrase here ' + ' '.join(['different']*400) + ' recover phrase now')
        ops, stats = align(a.words, b.words, max_tokens=64)
        self.assert_preserved(a, b, ops)
        self.assertTrue(all(kind == 'agreement' for kind, _, _, _ in ops[-3:]))
        self.assertGreater(stats['fallback_blocks'], 0)
        self.assertLessEqual(stats['max_dp_cells'], 4096)


class ImportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.addCleanup(self.temp.cleanup)

    def write(self, name, data):
        (self.root/name).write_text(json.dumps(data), encoding='utf-8')

    def test_srt_keeps_coarse_intervals_and_raw_text(self):
        (self.root/'a.srt').write_text('1\n00:00:00,000 --> 00:00:03,000\n(speaker 0) Yeah, hi!\n\n2\n00:00:03,000 --> 00:00:04,000\nNo.\n', encoding='utf-8')
        a = load_run(spec('a', 'a.srt', 'srt'), self.root, 'TEST', AUDIO)
        self.assertEqual(a.segments[0]['text'], 'Yeah, hi!')
        self.assertEqual([(w.start_ms, w.end_ms, w.timing) for w in a.words[:2]], [(0, 3000, 'cue')]*2)
        b = run('b', 'yeah hi no', [(100, 400), (1000, 1400), (3000, 3300)])
        self.assertEqual(compare([a, b], 'a')['counts'], {})

    def test_crisp_offsets_tokens_missing_times_and_private_paths(self):
        self.write('a.json', {'crispasr': {'model': 'C:\\private\\model.gguf'}, 'transcription': [
            {'text': 'Hi no', 'offsets': {'from': 100, 'to': 1000},
             'words': [{'text': 'Hi', 't0': 10, 't1': 20, 'offsets': {'from': 100, 'to': 200}}, {'text': 'no'}],
             'tokens': [{'text': ' Hi', 'p': .9, 'offsets': {'from': 100, 'to': 200}}]}]})
        s = spec('a', 'a.json')
        s['timestamp_offset_ms'] = 5000
        a = load_run(s, self.root, 'TEST', AUDIO)
        self.assertEqual(a.words[0].start_ms, 5100)
        self.assertIsNone(a.words[0].confidence)  # subword score never relabelled as word confidence
        self.assertEqual(a.segments[0]['tokens'][0]['p'], .9)
        self.assertEqual(a.words[1].timing, 'unknown')
        self.assertNotIn('private', json.dumps(a.export()))

    def test_word_segment_disagreement_keeps_both(self):
        self.write('a.json', {'transcription': [{'text': 'hi omitted', 'words': [{'text': 'hi'}]}]})
        a = load_run(spec('a', 'a.json'), self.root, 'TEST', AUDIO)
        report = compare([a, run('b', 'hi')], 'a')
        self.assertTrue(any('Detailed words disagree' in str(r['diagnostics']) for r in report['disagreements']))
        self.assertEqual(report['runs'][0]['segments'][0]['text'], 'hi omitted')

    def test_validation(self):
        self.write('bad.json', {'transcription': [{'text': 'hi', 'offsets': {'from': float('nan'), 'to': 2}}]})
        with self.assertRaises(ValueError):
            load_run(spec('bad', 'bad.json'), self.root, 'TEST', AUDIO)
        self.write('bad.json', {'transcription': [{'text': 'hi', 'tokens': [{'text': 'hi', 'p': 1.2}]}]})
        with self.assertRaises(ValueError):
            load_run(spec('bad', 'bad.json'), self.root, 'TEST', AUDIO)
        (self.root/'bad.srt').write_text('not srt', encoding='utf-8')
        with self.assertRaises(ValueError):
            load_run(spec('bad', 'bad.srt', 'srt'), self.root, 'TEST', AUDIO)
        wrong = spec('bad', 'bad.srt', 'srt')
        wrong['audio_id'] = 'different recording'
        with self.assertRaisesRegex(ValueError, 'different audio'):
            load_run(wrong, self.root, 'TEST', AUDIO)

    def test_command_outputs_and_no_overwrite(self):
        for name, text in [('a', 'Hi.'), ('b', 'No.')]:
            (self.root/f'{name}.srt').write_text(f'1\n00:00:01,000 --> 00:00:02,000\n{text}\n', encoding='utf-8')
        manifest = {'schema_version': 1, 'episode': 'TEST', 'audio': AUDIO, 'primary': 'a',
                    'runs': [spec('a', 'a.srt', 'srt'), spec('b', 'b.srt', 'srt')]}
        self.write('manifest.json', manifest)
        result = run_comparison(self.root/'manifest.json', self.root/'result')
        self.assertEqual(result['counts'], {'conflicting_recognition': 1})
        self.assertEqual(len(list((self.root/'result').iterdir())), 6)
        report = json.loads((self.root/'result/comparison.json').read_text(encoding='utf-8'))
        validate_report(report)
        with self.assertRaises(FileExistsError):
            run_comparison(self.root/'manifest.json', self.root/'result')
        report['disagreements'][0]['sources'][0]['word_ids'] = ['missing']
        with self.assertRaises(ValueError):
            validate_report(report)
        manifest['runs'][1]['id'] = 'a'
        self.write('manifest.json', manifest)
        with self.assertRaises(ValueError):
            load_manifest(self.root/'manifest.json')


class ReviewTests(unittest.TestCase):
    def test_stable_ids_and_no_majority_replacement(self):
        a, b, c = run('a', 'hi'), run('b', 'no'), run('c', 'no')
        pair = compare([a, b], 'a')
        triple = compare([a, b, c], 'a')
        self.assertIn(pair['disagreements'][0]['id'], {x['id'] for x in triple['disagreements']})
        provisional = reconcile(triple)
        self.assertEqual(provisional['primary'], 'a')
        self.assertEqual(provisional['automatic_text_changes'], [])
        self.assertFalse(provisional['publication_ready'])
        validate_report(triple)
        triple['disagreements'][0]['classification'] = 'verified_truth'
        with self.assertRaises(ValueError):
            validate_report(triple)

    def test_decisions_require_evidence_and_do_not_publish(self):
        report = compare([run('a', 'hi'), run('b', 'no')], 'a')
        decision = {'disagreement_id': report['disagreements'][0]['id'], 'action': 'accept',
                    'candidate_run_id': 'b', 'reviewer': 'Tester', 'date': '2026-10-21',
                    'evidence': 'synthetic fixture', 'audio_verified': False}
        ledger = {'schema_version': 1, 'decisions': [decision]}
        provisional = reconcile(report, ledger)
        self.assertEqual(provisional['decisions'][0], decision)
        self.assertFalse(provisional['publication_ready'])
        self.assertEqual(provisional['automatic_text_changes'], [])
        decision['audio_verified'] = True
        with self.assertRaises(ValueError):
            reconcile(report, ledger)
        decision['audio_evidence'] = 'test audio interval 0-400 ms'
        reconcile(report, ledger)
        self.assertFalse(make_jobs(report)['jobs'])
        decision['disagreement_id'] = 'stale'
        with self.assertRaises(ValueError):
            reconcile(report, ledger)

    def test_jobs_padding_merging_clamping_and_splitting(self):
        a, b = run('a', 'hi yeah no'), run('b', 'bye yes stop')
        report = compare([a, b], 'a')
        jobs = make_jobs(report, before_ms=2000, after_ms=2000)
        self.assertEqual(len(jobs['jobs']), 1)
        self.assertEqual(jobs['jobs'][0]['start_ms'], 0)
        self.assertEqual(jobs['jobs'][0]['end_ms'], 4400)
        report['disagreements'][0]['end_ms'] = 200000
        split = make_jobs(report, max_job_ms=30000)
        self.assertTrue(all(0 <= j['start_ms'] < j['end_ms'] <= AUDIO['duration_ms']
                            and j['end_ms']-j['start_ms'] <= 30000 for j in split['jobs']))
        with self.assertRaises(ValueError):
            make_jobs(report, before_ms=-1)

    def test_adapter_is_bounded_and_uses_argument_arrays(self):
        report = compare([run('a', 'hi'), run('b', 'no')], 'a')
        job = make_jobs(report)['jobs'][0]
        argv = commands(job, Path('audio with spaces.mp3'), Path('model.gguf'), Path('asr.exe'), Path('ffmpeg.exe'), Path('result'))
        self.assertIn('audio with spaces.mp3', argv[0])
        self.assertIn('--output-json-full', argv[1])
        job['end_ms'] = 200000
        with self.assertRaises(ValueError):
            commands(job, Path('audio'), Path('model'), Path('exe'), Path('ffmpeg'), Path('out'))

    def test_adapter_rejects_audio_mismatch_before_launch(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            audio, model = root/'audio', root/'model'
            audio.write_bytes(b'audio')
            model.write_bytes(b'model')
            job = make_jobs(compare([run('a', 'hi'), run('b', 'no')], 'a'))['jobs'][0]
            with patch('run_asr_job.subprocess.run') as launch:
                with self.assertRaises(ValueError):
                    execute(job, audio, model, Path('exe'), Path('ffmpeg'), root/'out')
                launch.assert_not_called()

    def test_adapter_imports_clip_offset_and_retains_receipt(self):
        for fail in (False, True):
            with self.subTest(fail=fail), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                audio, model, out = root/'audio', root/'model', root/'out'
                audio.write_bytes(b'audio')
                model.write_bytes(b'model')
                job = make_jobs(compare([run('a', 'hi'), run('b', 'no')], 'a'))['jobs'][0]
                job['audio'] = {**AUDIO, 'sha256': hashlib.sha256(b'audio').hexdigest()}
                job['start_ms'], job['end_ms'] = 1000, 3000

                def fake_launch(argv, **kwargs):
                    if '--help' in argv:
                        return subprocess.CompletedProcess(argv, 0, '--backend --model --language --gpu-backend --output-json-full --output-srt --output-file', '')
                    if '--version' in argv:
                        return subprocess.CompletedProcess(argv, 0, 'version : 0.8.43\ngit sha : eb633d90\ncompiler : private-detail', '')
                    if fail:
                        raise subprocess.CalledProcessError(1, argv)
                    if '--output-file' in argv:
                        (out/'recognition.json').write_text(json.dumps({'transcription': [
                            {'text': 'hi', 'offsets': {'from': 100, 'to': 400},
                             'words': [{'text': 'hi', 'offsets': {'from': 100, 'to': 400}}]}]}), encoding='utf-8')
                    else:
                        (out/'clip.wav').write_bytes(b'clip')
                    return subprocess.CompletedProcess(argv, 0)

                with patch('run_asr_job.subprocess.run', side_effect=fake_launch):
                    if fail:
                        with self.assertRaises(subprocess.CalledProcessError):
                            execute(job, audio, model, Path('exe'), Path('ffmpeg'), out)
                        receipt = json.loads((out/'execution.local.json').read_text())
                        self.assertEqual(receipt['status'], 'failed')
                        self.assertFalse((out/'run-spec.json').exists())
                    else:
                        receipt = execute(job, audio, model, Path('exe'), Path('ffmpeg'), out)
                        self.assertEqual(receipt['status'], 'complete')
                        exported = json.loads((out/'run-spec.json').read_text())
                        self.assertEqual(exported['version'], 'CrispASR 0.8.43 eb633d90')
                        imported = load_run(exported, out, 'TEST', job['audio'])
                        self.assertEqual(imported.words[0].start_ms, 1100)
                        self.assertEqual(exported['parent_disagreement_ids'], job['disagreement_ids'])

    def test_reference_metrics_and_ground_truth_gate(self):
        self.assertEqual(error_rates('one two three', 'one three')['deletions'], 1)
        self.assertEqual(error_rates('one two', 'one new')['substitutions'], 1)
        self.assertEqual(error_rates('one two', 'one hi two')['insertions'], 1)
        self.assertEqual(error_rates('if if hi', 'if hi')['deletion_rate'], 1/3)
        self.assertEqual(error_rates('Hi!', 'hi')['wer'], 0)
        self.assertIsNone(error_rates('', 'hi')['wer'])
        with self.assertRaises(ValueError):
            error_rates('one two', 'one two', max_cells=1)
        with self.assertRaises(ValueError):
            evaluate({'schema_version': 1, 'audio_verified': False})


if __name__ == '__main__':
    unittest.main()
