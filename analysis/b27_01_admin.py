"""Administrative byte binding only; no mathematical computations."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'results/b27_01'
GIT = ['git', '-c', 'safe.directory=' + ROOT.as_posix(), '-C', str(ROOT)]
SETUP = '6dea55ec926c1618cc60ad71209795528705bf61'
LAUNCH = ROOT.parents[2] / 'Claude_Handover_B15_B18/post_b19_housekeeping_20260917/batch27_launch'

SOURCES = [
    ('b17_report', '01c49022', 'docs/b17_01_report.md', 'Full report'),
    ('b17_certificate', '01c49022', 'results/b17_01/certificate.json', 'Fixed matrices, coefficients, smoothness minor row indices, and frame minor'),
    ('b17_verifier', '01c49022', 'analysis/b17_01_verify.py', 'Full script, read only; historical random generator is NOT executed'),
    ('a26_symmetric', '7464a2bd', 'results/a26_01/PROOF.md', 'Full proof'),
    ('a26_c1', SETUP, 'docs/a26_02_review.md', 'Full report; accepted smooth-cubic scope'),
    ('b26_expander', 'cdf6839c', 'docs/b26_02_review.md', 'Sections 1-4, including literal-family classification and its limits'),
    ('b26_classification', '21816b3c', 'docs/b26_10a_review.md', 'Section 4; no use of general transfer under separate R27-K4 review'),
    ('b26_paired', 'a7b7c19f', 'docs/b26_10c_review.md', 'Sections 1 and 2.4; paired-column correction and Application 3 status'),
    ('b18_degree', 'ea045cef', 'docs/b18_01_report.md', 'Sections 2-3.6; fixed-point separation theorem and dependency'),
    ('b19_lower', '75ddb900', 'docs/b19_02_report.md', 'Sections 0, 2-3, 7-8.1; degree <=5 exclusion'),
    ('cap', SETUP, 'docs/onset_conjecture.md', 'Sections 0-2.2; cap statement and historical onset bracket'),
    ('applications', SETUP, 'results/a25_02/APPLICATIONS.md', 'Full text, especially Application 3'),
    ('b24_scope', 'ab2f8a40', 'docs/b24_10_review.md', 'Cap dependency ruling and cubic-factor restriction, sections 6-7 and 11'),
    ('a25_decision', SETUP, 'docs/a25_10_report.md', 'Opening verdict and Application 3 audit'),
    ('b23_intersection', '3bcad666', 'docs/b23_03_report.md', 'Sections 0-2.6: direct-point classification, the two closed families, and plane-cubic cap'),
    ('b23_review', '239dd6e8', 'docs/b23_10_review.md', 'Sections 3.0-3.4 and rulings B23-10.3, .6, .12'),
    ('paper3_scope', '0a8029bb', 'papers/det4-blindness/det4-blindness.tex', 'C06-C12 and C34-C37 only; stale smooth-boundary and C45 prose is superseded by B27_COMMON'),
    ('paper2_scope', '721d54a2', 'paper/det4-onset.tex', 'Introduction cubic-onset bracket and cap section; measured totals are not silently upgraded'),
]

def git(*args):
    return subprocess.check_output(GIT + list(args))

def binding(data):
    return {'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)}

def write_json(path, obj):
    path.write_bytes((json.dumps(obj, indent=2, ensure_ascii=False) + '\n').encode('utf-8'))

def inputs():
    assert git('rev-parse', 'HEAD').decode().strip() == SETUP
    assert git('branch', '--show-current').decode().strip() == 'b27-01'
    OUT.mkdir(parents=True, exist_ok=True)
    dest = OUT / 'inputs'
    dest.mkdir(exist_ok=True)
    rows = []
    for key, pin, path, extent in SOURCES:
        commit = git('rev-parse', pin + '^{commit}').decode().strip()
        data = git('show', commit + ':' + path)
        snapshot = dest / (key + ('.json' if path.endswith('.json') else '.txt'))
        snapshot.write_bytes(data)
        rows.append(dict(key=key, commit=commit, path=path,
                         blob_oid=git('rev-parse', commit + ':' + path).decode().strip(),
                         **binding(data), cr_bytes=data.count(b'\r'),
                         hash_names='Exact committed blob payload, excluding Git object header',
                         snapshot=snapshot.relative_to(ROOT).as_posix(), read_extent=extent,
                         method='READ; hashing is not mathematical verification'))
    write_json(OUT / 'INPUT_BINDINGS.json', rows)
    brief_rows = []
    for name in ['B27_COMMON.md', 'B27-01.md', 'BATCH27_BOARD.md']:
        data = (LAUNCH / name).read_bytes()
        (dest / name).write_bytes(data)
        brief_rows.append(dict(path=str(LAUNCH / name), **binding(data),
                               hash_names='Raw administrative launch-file bytes, not a mathematical premise'))
    write_json(OUT / 'PREFLIGHT.json', dict(
        started_utc='2026-09-23T03:47:00Z', first_clock_utc='2026-09-23T03:47:57Z',
        worktree=str(ROOT), branch='b27-01', expected_head=SETUP, actual_head=SETUP,
        source_of_expected_head='PART 25 setup report and receipts, b27-01 row',
        brief_bindings=brief_rows, board_hashes_match=True,
        original_status='## b27-01...origin/b27-01; no tracked or untracked changes',
        report_absent_before_writing=True, results_directory_absent_before_writing=True,
        analysis_glob_empty_before_writing=True, applicable_agents_files=[],
        git_access='Per-command safe.directory for this authorized worktree only; no global config change. Sandbox ownership differs from owner; read-only retry succeeded.',
        permission_profile='Codex default collaboration, workspace-write sandbox, auto-review escalation',
        resource_limits=dict(max_math_runs=10, seconds_each=60, memory_bytes_each=512*1024*1024),
        installs=0, subagents=0, other_task_messages=0))
    print(json.dumps({'committed_sources_bound': len(rows), 'preflight': 'PASS'}))

def manifest():
    files = [ROOT / 'docs/b27_01_report.md']
    files += sorted((ROOT / 'analysis').glob('b27_01_*'))
    files += sorted(p for p in OUT.rglob('*') if p.is_file() and p.name != 'MANIFEST.json')
    rows = []
    for path in files:
        assert path.is_file()
        rel = path.relative_to(ROOT).as_posix()
        filtered = git('hash-object', rel).decode().strip()
        raw = git('hash-object', '--no-filters', rel).decode().strip()
        assert filtered == raw, rel
        rows.append(dict(path=rel, **binding(path.read_bytes()), git_blob_oid=raw,
                         filtered_equals_no_filters=True))
    write_json(OUT / 'MANIFEST.json', dict(slot='B27-01', setup_commit=SETUP,
        byte_convention='Raw payload bytes; SHA-256 excludes Git headers; manifest excludes itself',
        payloads=rows))
    rel = 'results/b27_01/MANIFEST.json'
    assert git('hash-object', rel) == git('hash-object', '--no-filters', rel)
    print(json.dumps({'payloads':len(rows), 'manifest':binding((OUT / 'MANIFEST.json').read_bytes())}))

def audit():
    records = json.loads((OUT/'INPUT_BINDINGS.json').read_bytes())
    for item in records:
        data = git('show',item['commit']+':'+item['path'])
        assert binding(data) == {k:item[k] for k in ('sha256','bytes')}
        assert (ROOT/item['snapshot']).read_bytes() == data
    for n in (1,2,3):
        receipt = json.loads((OUT/f'RUN_{n:02d}_RECEIPT.json').read_bytes())
        assert receipt['wall_seconds'] < 60 and receipt['peak_job_memory_bytes'] < 512_000_000
        for item in receipt.get('inputs',[]):
            assert binding((ROOT/item['path']).read_bytes())['sha256'] == item['sha256']
        outputs = receipt.get('outputs', [receipt['output']] if 'output' in receipt else [])
        for item in outputs:
            assert binding((ROOT/item['path']).read_bytes()) == {k:item[k] for k in ('sha256','bytes')}
    first = json.loads((OUT/'RUN_01_RECEIPT.json').read_bytes())
    assert binding((ROOT/'analysis/b27_01_verify.py').read_bytes())['sha256'] == first['script_sha256']
    assert binding((ROOT/'results/b27_01/inputs/b17_certificate.json').read_bytes())['sha256'] == first['input_sha256']
    print(json.dumps({'source_blob_bindings_verified':len(records),'run_receipt_bindings_verified':3,'status':'PASS'}))

def verify_commit():
    data=(OUT/'MANIFEST.json').read_bytes()
    manifest=json.loads(data)
    for item in manifest['payloads']:
        assert binding((ROOT/item['path']).read_bytes()) == {k:item[k] for k in ('sha256','bytes')}
        committed=git('show','HEAD:'+item['path'])
        assert binding(committed) == {k:item[k] for k in ('sha256','bytes')}
    assert git('show','HEAD:results/b27_01/MANIFEST.json') == data
    assert git('rev-parse','HEAD^').decode().strip() == SETUP
    assert git('branch','--show-current').decode().strip() == 'b27-01'
    print(json.dumps({'commit':git('rev-parse','HEAD').decode().strip(),
                      'committed_payloads_verified':len(manifest['payloads']),
                      'manifest_sha256':binding(data)['sha256'],'status':'PASS'}))

if __name__ == '__main__':
    {'inputs': inputs, 'manifest': manifest, 'audit':audit, 'verify-commit':verify_commit}[sys.argv[1]]()
