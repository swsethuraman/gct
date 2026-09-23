"""Administrative byte binding and manifest; no mathematical computation."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'results/b27_02'
PROJECT = ROOT.parents[2]
GIT = ['git', '-c', 'safe.directory=' + ROOT.as_posix(), '-C', str(ROOT)]

def git(*args):
    return subprocess.check_output(GIT + list(args))

def bind(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

def write(name, data):
    (OUT / name).write_bytes((json.dumps(data, indent=2) + '\n').encode())

def inputs():
    launch = PROJECT / 'Claude_Handover_B15_B18/post_b19_housekeeping_20260917'
    names = ['batch27_launch/B27_COMMON.md', 'batch27_launch/B27-02.md',
             'batch27_launch/BATCH27_BOARD.md', 'B27_PART25_SETUP_RECEIPTS.json']
    admin = [{'path': str(launch / p), 'byte_domain': 'raw working-copy administrative bytes',
              **bind((launch / p).read_bytes())} for p in names]
    sources = [
        ('f7967d17', 'results/a26_03/PROOF.md', 'READ, full text: normalization, Q^2 determinant'),
        ('f7967d17', 'docs/a26_03_report.md', 'READ, full text: achievement scope'),
        ('cdf6839c', 'docs/b26_02_review.md', 'READ, full text: D4, actual p4, prior blindness'),
        ('a7b7c19f', 'docs/b26_10c_review.md', 'READ, Part 2: corrected mixed-sign reopening rule'),
        ('92a7d054', 'docs/b25_04_report.md', 'READ excerpts only; not a mathematical premise'),
        ('6dea55ec', 'analysis/b15_bound.py', 'READ, administrative memory-limit implementation')]
    mathematical = []
    for ref, path, scope in sources:
        commit = git('rev-parse', ref).decode().strip()
        data = git('show', commit + ':' + path)
        mathematical.append({'commit': commit, 'path': path,
                             'git_blob_oid': git('rev-parse', commit + ':' + path).decode().strip(),
                             'byte_domain': 'exact committed blob payload, excluding Git header; no newline conversion',
                             'scope': scope, **bind(data)})
    assert git('branch', '--show-current').decode().strip() == 'b27-02'
    assert git('rev-parse', 'HEAD').decode().strip() == '6dea55ec926c1618cc60ad71209795528705bf61'
    write('INPUT_BINDINGS.json', {'administrative': admin, 'committed_inputs': mathematical})
    write('PREFLIGHT.json', {
        'label': 'READ: administrative observations',
        'first_clock_utc': '2026-09-23T03:48:28Z',
        'budget_accounting_origin_utc': '2026-09-23T03:43:28Z',
        'clock_note': 'Accounting origin adds a conservative five minutes for brief reading and preflight before the first explicit clock; it is not a measured session-start timestamp.',
        'fresh_session': 'This task has no B27-01 work and no subagents or other task messages.',
        'branch': 'b27-02', 'worktree': str(ROOT),
        'head': git('rev-parse', 'HEAD').decode().strip(),
        'expected_head_source': 'PART 25 receipt row b27-02',
        'initial_status': '## b27-02...origin/b27-02; no tracked changes or untracked entries',
        'initial_output_paths_absent': ['docs/b27_02_report.md', 'results/b27_02/', 'analysis/b27_02_*'],
        'brief_hashes_match_board': True,
        'applicable_AGENTS_files': [],
        'environment_notes': [
            'Initial read-only git calls needed a command-local safe.directory setting for the sandbox account.',
            'Global ignore file was unreadable. No global or repository configuration was changed.',
            'python was absent on PATH; the bundled Python is installed but has no sympy.',
            'Exact verification uses installed Python standard-library integers and Fraction. No installs.'],
        'mismatches': []})
    print('Input bindings and preflight recorded.')

def seal():
    paths = [ROOT / 'docs/b27_02_report.md']
    paths += sorted(p for p in OUT.rglob('*') if p.is_file() and p.name != 'MANIFEST.json')
    paths += sorted((ROOT / 'analysis').glob('b27_02_*.py'))
    payload = []
    for p in paths:
        rel = p.relative_to(ROOT).as_posix()
        raw = p.read_bytes()
        filtered = git('hash-object', rel).strip()
        unfiltered = git('hash-object', '--no-filters', rel).strip()
        if filtered != unfiltered:
            raise RuntimeError('Filter changes payload: ' + rel)
        payload.append({'path': rel, **bind(raw), 'git_blob_oid': unfiltered.decode()})
    write('MANIFEST.json', {'slot': 'B27-02', 'hash_domain': 'raw payload bytes; manifest excludes itself',
                            'payloads': payload})
    manifest = OUT / 'MANIFEST.json'
    assert git('hash-object', str(manifest)).strip() == git('hash-object', '--no-filters', str(manifest)).strip()
    print(json.dumps({'manifest': bind(manifest.read_bytes()), 'payload_count': len(payload)}))

def audit():
    manifest = json.loads((OUT / 'MANIFEST.json').read_text())
    names = {entry['path'] for entry in manifest['payloads']}
    actual = {p.relative_to(ROOT).as_posix() for p in OUT.rglob('*') if p.is_file() and p.name != 'MANIFEST.json'}
    actual |= {p.relative_to(ROOT).as_posix() for p in (ROOT / 'analysis').glob('b27_02_*.py')}
    actual.add('docs/b27_02_report.md')
    assert names == actual and len(names) == len(manifest['payloads'])
    for entry in manifest['payloads']:
        assert bind((ROOT / entry['path']).read_bytes()) == {k: entry[k] for k in ('bytes', 'sha256')}
        assert git('hash-object', entry['path']).decode().strip() == entry['git_blob_oid']
        assert git('hash-object', '--no-filters', entry['path']).decode().strip() == entry['git_blob_oid']
    for tag in ('run01', 'run02'):
        receipt = json.loads((OUT / (tag + '_resources.json')).read_text())
        for entry in receipt['inputs'] + [receipt['output']]:
            assert bind((ROOT / entry['path']).read_bytes()) == {k: entry[k] for k in ('bytes', 'sha256')}
        assert receipt['exit_code'] == 0 and receipt['wall_seconds'] < 60
        assert receipt['job_object_enforced'] and receipt['peak_job_bytes'] < receipt['memory_cap_bytes']
    staged = git('diff', '--cached', '--name-only').decode().splitlines()
    expected = names | {'results/b27_02/MANIFEST.json'}
    if staged:
        assert set(staged) == expected, (staged, expected)
    print(json.dumps({'payloads_checked': len(names), 'run_receipts_checked': 2,
                      'staged_paths_checked': len(staged), 'manifest': bind((OUT / 'MANIFEST.json').read_bytes())}))

if __name__ == '__main__':
    {'inputs': inputs, 'seal': seal, 'audit': audit}[sys.argv[1]]()
