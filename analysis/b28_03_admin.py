"""Administrative raw-blob binding and final sealing; no mathematical computation."""
import hashlib
import datetime
import importlib.util
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'results/b28_03'
GIT = ['git', '-c', 'safe.directory=' + ROOT.as_posix(), '-C', str(ROOT)]
LAUNCH = ROOT.parents[2] / 'Claude_Handover_B15_B18/post_b19_housekeeping_20260917/batch28_launch'

def git(*args):
    return subprocess.check_output(GIT + list(args))

def digest(data):
    return {'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)}

def write(path, obj):
    path.write_bytes((json.dumps(obj, indent=2, ensure_ascii=False) + '\n').encode())

def extract():
    review = git('show', '53206b43:docs/b27_k4_review.md')
    start = review.index(b'### 2.2 Independent re-derivation (HAND)')
    end = review.index(b'\n\n## 3. The `P_r` identification', start) + 1
    (OUT / 'R27_K4_SECTION_2_2_EXACT.md').write_bytes(review[start:end])

def bind():
    assert git('branch', '--show-current').decode().strip() == 'b28-03'
    assert git('rev-parse', 'HEAD').decode().strip() == 'b0863403798832668d114f177e672738f1e8be57'
    commit = git('rev-parse', '53206b43').decode().strip()
    manifest_path = 'results/b27_k4/MANIFEST.json'
    raw = git('show', commit + ':' + manifest_path)
    assert digest(raw)['sha256'] == 'd63c535f68c35f5e0a959be8fcd88c78db9a3501d69c48c8d51269cb2ac4555e'
    rows = []
    def record(ref, path, scope):
        full = git('rev-parse', ref).decode().strip()
        data = git('show', full + ':' + path)
        rows.append({'commit': full, 'path': path, 'blob': git('rev-parse', full + ':' + path).decode().strip(), **digest(data), 'CR_bytes': data.count(b'\r'), 'LF_bytes': data.count(b'\n'), 'read_scope': scope})
        return data
    record(commit, manifest_path, 'READ: complete manifest')
    for p in json.loads(raw)['payloads']:
        data = record(commit, p['path'], 'READ: complete payload')
        assert digest(data) == {'sha256': p['sha256'], 'bytes': p['bytes']}, p['path']
        assert git('show', '96a8074d:' + p['path']) == data, p['path']
    assert git('show', '96a8074d:' + manifest_path) == raw
    record('21816b3c', 'docs/b26_10a_review.md', 'READ: sections 2.1-3.4; remaining sections not used')
    record('f8326974', 'paper/det4-onset.tex', 'READ: lines 65-145, 249-323, 650-720, 837-910, 1040-1103; complete eq:lengthred occurrence inventory')
    record('96a8074d', 'docs/batch_closes/BATCH27_CLOSE.md', 'READ: complete close; especially result 5 and L2')
    OUT.mkdir(parents=True, exist_ok=False)
    local = []
    for name in ['B28_COMMON.md', 'B28-03.md', 'BATCH28_BOARD.md']:
        data = (LAUNCH / name).read_bytes()
        local.append({'path': str(LAUNCH / name), **digest(data), 'scope': 'administrative launch bytes, not mathematical premises'})
    receipt = LAUNCH.parent / 'B28_PART27_SETUP_RECEIPTS.json'
    local.append({'path': str(receipt), **digest(receipt.read_bytes()), 'scope': 'administrative setup receipt'})
    write(OUT / 'INPUT_BINDINGS.json', {'hash_semantics': 'SHA-256 of raw committed Git blob bytes; local administrative bindings explicitly distinguished. No EOL conversion.', 'packet_manifest_matches_brief': True, 'all_five_payloads_match': True, 'packet_unchanged_at_merge_96a8074d': True, 'committed_inputs': rows, 'local_administrative_inputs': local})
    source = git('show', commit + ':analysis/b27_k4_hwv_check.py')
    (ROOT / 'analysis/b28_03_replay_source.py').write_bytes(source)
    extract()
    write(OUT / 'PREFLIGHT.json', {'label': 'READ administrative observations', 'branch': 'b28-03', 'head': 'b0863403798832668d114f177e672738f1e8be57', 'expected_head_source': str(receipt), 'tracked_and_untracked_status_before_work': 'clean', 'output_paths_initially_absent': ['docs/b28_03_review.md', 'results/b28_03/', 'analysis/b28_03_*'], 'fresh_session': True, 'prior_exposure_to_R27_K4_production': False, 'applicable_AGENTS_md_found': [], 'git_access_note': 'Sandbox user differs from repository owner; read commands use a command-local safe.directory for this one authorized worktree. No global configuration changed.', 'subagents': 0})
    print(json.dumps({'bindings': 'PASS', 'packet_payloads': 5, 'manifest_sha256': digest(raw)['sha256'], 'python': sys.version, 'executable': sys.executable, 'sympy_available': importlib.util.find_spec('sympy') is not None}, indent=2))

def seal():
    receipt_path = OUT / 'resource_receipt.json'
    receipt = json.loads(receipt_path.read_bytes())
    receipt.setdefault('substantive_review_complete_utc', datetime.datetime.now(datetime.timezone.utc).isoformat())
    receipt['outcome'] = 'ACCEPT; rungs 3a and 3b complete, rung 3c accepted; transfer lemma only'
    write(receipt_path, receipt)
    paths = [ROOT / 'docs/b28_03_review.md'] + sorted((ROOT / 'analysis').glob('b28_03_*')) + sorted(p for p in OUT.iterdir() if p.name != 'MANIFEST.json')
    assert all(p.is_file() for p in paths)
    manifest = {'slot': 'B28-03', 'branch': 'b28-03', 'parent': 'b0863403798832668d114f177e672738f1e8be57', 'excludes': 'results/b28_03/MANIFEST.json (itself)', 'hash_semantics': 'SHA-256 and byte count of complete raw file bytes', 'payloads': [{'path': p.relative_to(ROOT).as_posix(), **digest(p.read_bytes())} for p in paths]}
    write(OUT / 'MANIFEST.json', manifest)
    print(json.dumps({'manifest': digest((OUT / 'MANIFEST.json').read_bytes()), 'payload_count': len(paths)}, indent=2))

def verify():
    manifest = json.loads((OUT / 'MANIFEST.json').read_bytes())
    for p in manifest['payloads']:
        data = (ROOT / p['path']).read_bytes()
        assert digest(data) == {'sha256': p['sha256'], 'bytes': p['bytes']}, p['path']
    paths = [p['path'] for p in manifest['payloads']] + ['results/b28_03/MANIFEST.json']
    for p in paths:
        assert git('hash-object', p) == git('hash-object', '--no-filters', p), p
    for row in json.loads((OUT / 'INPUT_BINDINGS.json').read_bytes())['committed_inputs']:
        assert digest(git('show', row['commit'] + ':' + row['path'])) == {'sha256': row['sha256'], 'bytes': row['bytes']}
    source = git('show', '53206b43:docs/b27_k4_review.md')
    excerpt = (OUT / 'R27_K4_SECTION_2_2_EXACT.md').read_bytes()
    assert excerpt in source
    report = (ROOT / 'docs/b28_03_review.md').read_text(encoding='utf-8')
    source_lines = [line.strip() for line in source.decode().splitlines()]
    for line in report.splitlines():
        if line.startswith('> ') and line[2:].strip():
            assert line[2:].strip() in source_lines, line
    assert all(ord(c)>=32 or c in '\r\n\t' for c in report)
    print(json.dumps({'manifest_and_filter_parity': 'PASS', 'files': len(paths), 'manifest': digest((OUT / 'MANIFEST.json').read_bytes())}, indent=2))

if __name__ == '__main__':
    {'bind': bind, 'extract': extract, 'seal': seal, 'verify': verify}[sys.argv[1]]()
