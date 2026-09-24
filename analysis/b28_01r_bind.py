#!/usr/bin/env python3
"""Read-only producer/host binding audit; writes only this review's results."""
import hashlib
import json
import pathlib
import resource
import subprocess
import time

ROOT = pathlib.Path('/mnt/c/Users/swami/Projects/gct-gpt')
WT = ROOT / 'work/batch28/b28-01r'
OUT = WT / 'results/b28_01r'
HOST = pathlib.Path.home() / 'b28_01'
TIP = 'a1c3c3a69b789c91909ed5476354ad762f3e71c2'
BASE = '96a8074d'
GIT = ['git', '--git-dir=' + str(ROOT / 'work/batch15/.git')]

def git(*args):
    return subprocess.check_output(GIT + list(args))

def blob(ref, path):
    return git('show', ref + ':' + path)

def digest(data):
    return dict(bytes=len(data), sha256=hashlib.sha256(data).hexdigest())

def file_digest(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for part in iter(lambda: f.read(1024 * 1024), b''):
            h.update(part)
    return dict(bytes=path.stat().st_size, sha256=h.hexdigest())

def save(path, obj):
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + '\n')

def main():
    start = time.monotonic()
    OUT.mkdir(parents=True, exist_ok=True)
    manifest_bytes = blob(TIP, 'results/b28_01/MANIFEST.json')
    assert digest(manifest_bytes)['sha256'] == '420eb69ab49165338cfe9afab87f02ecb4ffc9d270b2fcc50ce2acb8172b934e'
    manifest = json.loads(manifest_bytes)
    assert len(manifest['payloads']) == 186
    parent = git('show', '-s', '--format=%P', TIP).decode().strip()
    assert parent == 'c0122f57e745097ddb84d3f6ee6a26e1de8d8314'
    changed = git('diff-tree', '--no-commit-id', '--name-status', '-r', TIP).decode().splitlines()
    paths = []
    for line in changed:
        status, path = line.split('\t')
        assert status == 'A'
        assert path.startswith(('analysis/b28_01_', 'results/b28_01/')) or path == 'docs/b28_01a_report.md'
        paths.append(path)
    payloads = []
    for entry in manifest['payloads']:
        got = digest(blob(TIP, entry['path']))
        assert got == {k: entry[k] for k in ('bytes', 'sha256')}, entry['path']
        payloads.append(dict(path=entry['path'], **got))
    assert set(paths) == {x['path'] for x in payloads} | {'results/b28_01/MANIFEST.json'}
    engine = []
    for line in blob(TIP, 'results/b28_01/engine_hashes.txt').decode().splitlines():
        expected, name = line.split()
        got = file_digest(HOST / 'engine' / name)
        assert got['sha256'] == expected, name
        entry = dict(name=name, host=str(HOST / 'engine' / name), **got)
        if name != 'schur.so':
            for ref in (BASE, '7c36a52ddf338eb390a9bcd491cb9c50cf9e2a19'):
                assert digest(blob(ref, 'analysis/' + name)) == got, (ref, name)
            entry['committed_at'] = [BASE, '7c36a52ddf338eb390a9bcd491cb9c50cf9e2a19']
        engine.append(entry)
    assert sum(x['name'] != 'schur.so' for x in engine) == 19
    frozen = []
    for line in blob(TIP, 'results/b28_01/frozen_v2_hashes.txt').decode().splitlines():
        expected, name = line.split()
        got = file_digest(HOST / 'frozen' / name)
        assert got['sha256'] == expected, name
        if not name.endswith('.so'):
            assert digest(blob(TIP, 'analysis/' + name)) == got
        frozen.append(dict(name=name, **got))
    for name, committed in [('b28_01_cellA.sh', 'analysis/b28_01_cellA.sh'),
                            ('b28_01_reprice.py', 'analysis/b28_01_reprice.py'),
                            ('gate_rates.json', 'results/b28_01/gate_rates.json')]:
        got = file_digest(HOST / 'frozen' / name)
        assert digest(blob(TIP, committed)) == got, name
        frozen.append(dict(name=name, **got))
    retained = []
    for entry in json.loads(blob(TIP, 'results/b28_01/HOST_RETAINED.json'))['files']:
        got = file_digest(HOST / entry['host_path'])
        assert got == {k: entry[k] for k in ('bytes', 'sha256')}, entry['host_path']
        retained.append(dict(host_path=str(HOST / entry['host_path']), **got))
    assert not (HOST / 'out/cellA').exists()
    launch = ROOT / 'Claude_Handover_B15_B18/post_b19_housekeeping_20260917/batch28_launch'
    briefs = {n: file_digest(launch / n) for n in ('B28_COMMON.md', 'R28-01.md', 'BATCH28_BOARD.md')}
    extra = ['results/b27_06/PREREGISTRATION.md', 'results/b27_06/INPUT_BINDINGS.json',
             'results/b27_06/REPORT.md', 'results/s71_sweep.jsonl', 'results/s71_calibration.jsonl',
             'results/s79_cells.jsonl', 'docs/stabiliser_reduction.md', 'docs/sparse_det_route.md',
             'results/s60_census.json', 'results/occurrence_screen.csv']
    inputs = [dict(commit=BASE, path=p, **digest(blob(BASE, p))) for p in extra]
    result = dict(schema='r28-01-bindings/1', evidence='READ committed blobs; COMPUTED raw SHA-256 comparisons',
                  hash_convention='raw file/blob bytes (no newline or encoding conversion)',
                  producer_tip=TIP, producer_parent=parent, changed_paths=paths,
                  manifest=digest(manifest_bytes), payloads=payloads, engine=engine,
                  frozen=frozen, host_retained=retained, briefs=briefs, inputs=inputs,
                  review_preflight=dict(branch='b28-01r', setup='ee354b57a9f60baacef7f451db28e5cce86d29bd',
                                        clean=True, output_paths_absent=True, fresh_Astra_session=True),
                  cellA_output_absent=True, all_match=True)
    save(OUT / 'BINDINGS.json', result)
    save(OUT / 'binding_receipt.json', dict(command='timeout 60 bash -c "ulimit -v 500000; exec python3 analysis/b28_01r_bind.py"',
          script=file_digest(pathlib.Path(__file__)), input_commit=TIP, input_manifest=digest(manifest_bytes),
          output=file_digest(OUT / 'BINDINGS.json'), wall_seconds=time.monotonic()-start,
          maxrss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, address_limit_kib=500000, timeout_seconds=60))
    print(json.dumps(dict(payloads=len(payloads), engine_sources=19, retained=len(retained), all_match=True)))

if __name__ == '__main__':
    main()
