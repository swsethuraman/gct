#!/usr/bin/env python3
"""Read-only input audit and receipt assembly; never invokes numerical machinery."""
import hashlib, json, pathlib, subprocess, sys, time

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / 'results/b28_01rd'
TIP = '467e8402478bca64923c0a1a852bd0efee331356'
PARENT = '0f7af8b11e55da20cd135c73d04554a0360dd97f'
HEAD = 'ff62d929e53edf5abcf772c4b44cd0ff4c302b49'
HOST = pathlib.Path.home() / 'b28_01'
TAG = '12_8_6_4_2_d8'

def git(*args):
    # Windows-created worktree .git contains a Windows absolute path; translate
    # explicitly for Linux Git without altering repository configuration.
    gd = (ROOT/'.git').read_text().strip().removeprefix('gitdir: ')
    gd = '/mnt/' + gd[0].lower() + gd[2:]
    return subprocess.check_output(['git', '-c', f'safe.directory={ROOT}', '--git-dir='+gd, '--work-tree='+str(ROOT), *args])

def digest(b): return hashlib.sha256(b).hexdigest()
def fileinfo(p):
    h = hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda: f.read(1048576), b''): h.update(b)
    return dict(bytes=p.stat().st_size, sha256=h.hexdigest())
def save(p, obj): p.write_text(json.dumps(obj, indent=2, sort_keys=True)+'\n')

def bind():
    assert not OUT.exists(), 'output directory already exists'
    assert not (ROOT/'docs/b28_01rd_review.md').exists()
    assert git('rev-parse','HEAD').decode().strip() == HEAD
    assert git('branch','--show-current').decode().strip() == 'b28-01r'
    assert git('rev-parse','b28-01').decode().strip() == TIP
    assert git('rev-parse',TIP+'^').decode().strip() == PARENT
    changed = git('diff-tree','--no-commit-id','--name-only','-r',TIP).decode().splitlines()
    assert all(p == 'docs/b28_01b_report.md' or p.startswith('results/b28_01b/') for p in changed)
    mp = 'results/b28_01b/MANIFEST.json'
    mb = git('show',TIP+':'+mp)
    assert digest(mb) == '9beba33cce900aed46940d25eacf535820c379385c2a3225d9f944541a45f314'
    manifest = json.loads(mb)
    assert len(manifest['files']) == manifest['count'] == 25
    assert set(changed) == {mp} | {r['path'] for r in manifest['files']}
    payloads = []
    for row in manifest['files']:
        b = git('show',TIP+':'+row['path'])
        assert len(b) == row['bytes'] and digest(b) == row['sha256'], row['path']
        payloads.append(row)
    host = json.loads(git('show',TIP+':results/b28_01b/HOST_RETAINED.json'))
    for row in host['files']:
        assert fileinfo(HOST/row['host_path']) == {k:row[k] for k in ('bytes','sha256')}, row
    fb = git('show',PARENT+':results/b28_01d/frozen_d_hashes.txt')
    frozen = []
    for line in fb.decode().splitlines():
        expected, name = line.split()
        info = fileinfo(HOST/'frozen_d'/name)
        assert info['sha256'] == expected, name
        frozen.append(dict(path=name, **info))
    assert len(frozen) == 9
    launch = ROOT.parents[2]/'Claude_Handover_B15_B18/post_b19_housekeeping_20260917/batch28_launch'
    briefs = {name:fileinfo(launch/name) for name in ('B28_COMMON.md','R28-01d.md','R28-01.md','BATCH28_BOARD.md')}
    assert briefs['B28_COMMON.md']['sha256'] == '06799a9e404fc45a0944f7fcae88d8dd5511f7721f704ebe69872dd3061c87b9'
    assert briefs['R28-01d.md']['sha256'] == '388da3404e8f1550858ef8976ed81fc15fa647053db4caae4d02ac98e6f17510'
    assert briefs['BATCH28_BOARD.md']['sha256'] == '8948710ad4ed3bc7ce7c3a5cf4588518eb967bfa766beca8e34e28531bbfd9a4'
    OUT.mkdir()
    (OUT/'inputs').mkdir()
    for suffix in ('_cell.json','_p2147483647_cert.json','_pencils.json','_p2147483647_verify.json'):
        name = TAG+suffix
        (OUT/'inputs'/name).write_bytes(git('show',TIP+':results/b28_01b/out_cellA/'+name))
    sources = {}
    for rev,path in [(PARENT,'analysis/b28_01c_verify.py'),(PARENT,'analysis/b28_01d_supervise.py'),('96a8074d','results/b27_06/PREREGISTRATION.md')]:
        b = git('show',rev+':'+path)
        sources[rev+':'+path] = dict(bytes=len(b),sha256=digest(b))
    save(OUT/'BINDINGS.json',dict(label='COMPUTED',review_head=HEAD,producer_tip=TIP,producer_parent=PARENT,
        changed_paths=changed,manifest=dict(path=mp,bytes=len(mb),sha256=digest(mb)),payloads=payloads,
        host_retained=host['files'],frozen_d=frozen,briefs=briefs,read_sources=sources,
        hash_meaning='SHA-256 of raw committed blob bytes, raw local launch-file bytes, or raw host-file bytes as identified; no Git filters'))
    print('PASS: 25 committed payloads, 4 host-retained files, 9 frozen files; branch, parent, paths, briefs')

if __name__ == '__main__':
    t = time.perf_counter()
    assert sys.argv[1:] == ['bind']
    bind()
    save(OUT/'binding_receipt.json',dict(command='python3 analysis/b28_01rd_audit.py bind',wall_secs=time.perf_counter()-t,
        script=fileinfo(pathlib.Path(__file__)),output=fileinfo(OUT/'BINDINGS.json'),operation='hashing and metadata only; no numerical verifier'))
