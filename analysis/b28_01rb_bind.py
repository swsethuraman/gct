#!/usr/bin/env python3
"""Raw committed/host bindings for the bounded R28-01b review."""
import difflib
import hashlib
import json
from pathlib import Path
import resource
import subprocess
import time

ROOT = Path('/mnt/c/Users/swami/Projects/gct-gpt')
WT = ROOT / 'work/batch28/b28-01r'
OUT = WT / 'results/b28_01rb'
HOST = Path.home() / 'b28_01'
TIP = '5a3174cd3a1ec96b05b92a8bcb73fbee58c0544b'
OLD = 'a1c3c3a69b789c91909ed5476354ad762f3e71c2'
GIT = ['git', '--git-dir=' + str(ROOT / 'work/batch15/.git')]

def git(*args):
    return subprocess.check_output(GIT + list(args))

def blob(ref, path):
    return git('show', ref + ':' + path)

def digest(data):
    return dict(bytes=len(data), sha256=hashlib.sha256(data).hexdigest())

def fd(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda: f.read(1048576), b''):
            h.update(b)
    return dict(bytes=path.stat().st_size, sha256=h.hexdigest())

def save(path, obj):
    path.write_text(json.dumps(obj, sort_keys=True, indent=2) + '\n')

def main():
    start = time.monotonic()
    OUT.mkdir(exist_ok=False)
    parent = git('show', '-s', '--format=%P', TIP).decode().strip()
    assert parent == OLD
    changed = git('diff-tree', '--no-commit-id', '--name-status', '-r', TIP).decode().splitlines()
    paths = []
    for line in changed:
        status, p = line.split('\t')
        assert status == 'A'
        assert p.startswith(('analysis/b28_01c_', 'results/b28_01c/')) or p == 'docs/b28_01c_report.md'
        paths.append(p)
    mp = 'results/b28_01c/MANIFEST.json'
    raw_manifest = blob(TIP, mp)
    manifest = json.loads(raw_manifest)
    payloads = []
    for e in manifest['files']:
        got = digest(blob(TIP, e['path']))
        assert got == {k:e[k] for k in ('bytes', 'sha256')}, e['path']
        payloads.append(dict(path=e['path'], **got))
    assert len(payloads) == manifest['count'] == 211
    assert set(paths) == {e['path'] for e in payloads} | {mp}
    frozen = []
    for line in blob(TIP, 'results/b28_01c/frozen_c_hashes.txt').decode().splitlines():
        expected, name = line.split()
        got = fd(HOST / 'frozen_c' / name)
        assert got['sha256'] == expected, name
        source = 'results/b28_01c/' + name if name.endswith('.json') else 'analysis/' + name
        if not name.endswith('.so'):
            assert digest(blob(TIP, source)) == got, source
        frozen.append(dict(host_path='frozen_c/' + name, **got))
    regression = []
    for listpath, folder in [('results/b28_01/frozen_v2_hashes.txt', 'frozen'), ('results/b28_01/engine_hashes.txt', 'engine')]:
        for line in blob(OLD, listpath).decode().splitlines():
            expected, name = line.split()
            got = fd(HOST / folder / name)
            assert got['sha256'] == expected, name
            regression.append(dict(host_path=folder + '/' + name, **got))
    retained = []
    for e in json.loads(blob(TIP, 'results/b28_01c/HOST_RETAINED.json'))['files']:
        got = fd(HOST / e['host_path'])
        assert got == {k:e[k] for k in ('bytes', 'sha256')}, e['host_path']
        retained.append(dict(host_path=e['host_path'], **got))
    assert not (HOST / 'out/cellA').exists()
    assert not (HOST / 'job_cellA').exists()
    assert not list(HOST.rglob('12_8_6_4_2_d8_*'))
    launch = ROOT / 'Claude_Handover_B15_B18/post_b19_housekeeping_20260917/batch28_launch'
    briefs = {n:fd(launch / n) for n in ('B28_COMMON.md','R28-01b.md','R28-01.md','BATCH28_BOARD.md','B28-01c.md')}
    diffs = []
    for kind, ext in [('driver','py'),('verify','py'),('vfy','c'),('cellA','sh'),('reprice','py')]:
        a = 'analysis/b28_01_' + kind + '.' + ext
        b = 'analysis/b28_01c_' + kind + '.' + ext
        old, new = blob(OLD,a), blob(TIP,b)
        diff = ''.join(difflib.unified_diff(old.decode().splitlines(True),new.decode().splitlines(True),fromfile=OLD+':'+a,tofile=TIP+':'+b))
        dp = OUT / (kind + '.diff')
        dp.write_text(diff)
        diffs.append(dict(old=dict(commit=OLD,path=a,**digest(old)),new=dict(commit=TIP,path=b,**digest(new)),diff=dict(path=dp.name,**fd(dp))))
    inputs = []
    for ref,p in [('8a86fec17b72b565baaef7f9e29709d1ced35168','docs/b28_01r_review.md'),('96a8074d','results/b27_06/PREREGISTRATION.md')]:
        inputs.append(dict(commit=ref,path=p,**digest(blob(ref,p))))
    result = dict(schema='r28-01b-bindings/1',evidence='COMPUTED raw SHA-256; committed inputs READ separately',hash_convention='raw bytes, without newline conversion or Git filters',tip=TIP,parent=parent,changed_paths=paths,manifest=digest(raw_manifest),payloads=payloads,frozen=frozen,unchanged_host_regression=regression,retained=retained,briefs=briefs,diffs=diffs,inputs=inputs,initial_preflight=dict(branch='b28-01r',head='8a86fec17b72b565baaef7f9e29709d1ced35168',clean=True,output_paths_absent=True,producer_pushed=True),all_match=True,cellA_output_absent=True)
    save(OUT / 'BINDINGS.json', result)
    outputs = [dict(path=p.name,**fd(p)) for p in sorted(OUT.iterdir())]
    save(OUT / 'binding_receipt.json',dict(command='timeout 60 bash -c "ulimit -v 500000; exec python3 analysis/b28_01rb_bind.py"',script=fd(Path(__file__)),input_manifest=digest(raw_manifest),input_commit=TIP,outputs=outputs,wall_seconds=time.monotonic()-start,maxrss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,address_limit_kib=500000,timeout_seconds=60))
    print(json.dumps(dict(payloads=len(payloads),frozen=len(frozen),retained=len(retained),manifest=digest(raw_manifest),all_match=True)))

if __name__ == '__main__':
    main()
