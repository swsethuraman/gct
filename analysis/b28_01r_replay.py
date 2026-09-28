#!/usr/bin/env python3
"""Controls and exactly one calibration cell, from hash-checked frozen bytes.

Invoke inside one systemd scope (MemoryMax=8000000000, MemorySwapMax=0)
and a 3600-second timeout. Never writes under ~/b28_01. No target dispatch.
"""
import hashlib
import json
import os
import pathlib
import shutil
import subprocess
import tempfile
import time

WT = pathlib.Path('/mnt/c/Users/swami/Projects/gct-gpt/work/batch28/b28-01r')
OUT = WT / 'results/b28_01r'
HOST = pathlib.Path.home() / 'b28_01'
PY = pathlib.Path.home() / 'b28venv/bin/python'
TIP = 'a1c3c3a69b789c91909ed5476354ad762f3e71c2'
GIT = ['git', '--git-dir=/mnt/c/Users/swami/Projects/gct-gpt/work/batch15/.git']

def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for x in iter(lambda: f.read(1048576), b''): h.update(x)
    return dict(bytes=path.stat().st_size, sha256=h.hexdigest())

def save(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + '\n')

def main():
    start = time.monotonic()
    bind = json.loads((OUT / 'BINDINGS.json').read_text())
    assert bind['all_match'] and not (HOST / 'out/cellA').exists()
    for group, sub in [('engine', 'engine'), ('frozen', 'frozen')]:
        for ent in bind[group]:
            assert sha(HOST / sub / ent['name']) == {k: ent[k] for k in ('bytes', 'sha256')}
    assert (HOST / 'engine/schur.so').stat().st_mtime >= (HOST / 'engine/wk11_s71_schur.c').stat().st_mtime
    scratch = pathlib.Path(tempfile.mkdtemp(prefix='b28_01r_replay_'))
    receipts = OUT / 'replay_receipts'
    receipts.mkdir(exist_ok=True)
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', B28_ENGINE=str(HOST/'engine'),
               S71_SCHUR_SO=str(HOST/'engine/schur.so'), B28_VFY_SO=str(HOST/'frozen/b28_01_vfy.so'),
               OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', MKL_NUM_THREADS='1', NUMEXPR_NUM_THREADS='1')
    runs = []
    def run(label, script, args, expected=0):
        command = [str(PY), str(HOST/'frozen'/script)] + [str(x) for x in args]
        left = 3590 - (time.monotonic() - start)
        assert left > 0
        t = time.monotonic()
        stdout = receipts / (label + '_stdout_receipt.txt')
        stderr = receipts / (label + '_stderr_receipt.txt')
        timer = receipts / (label + '_time_receipt.txt')
        with stdout.open('wb') as so, stderr.open('wb') as se:
            proc = subprocess.run(['/usr/bin/time', '-v', '-o', str(timer)] + command,
                                  cwd=scratch, env=env, stdout=so, stderr=se, timeout=left)
        entry = dict(label=label, command=command, expected_rc=expected, rc=proc.returncode,
                     wall_seconds=time.monotonic()-t, code_input=sha(HOST/'frozen'/script),
                     stdout=sha(stdout), stderr=sha(stderr), timer=sha(timer))
        runs.append(entry)
        save(receipts/'runs_receipt.json', dict(runs=runs, scratch=str(scratch),
             aggregate_wall_seconds=time.monotonic()-start, scope_memory_bytes=8000000000,
             scope_swap_bytes=0, scope_wall_limit_seconds=3600, input_bindings=sha(OUT/'BINDINGS.json')))
        print(label, 'rc', proc.returncode, flush=True)
        assert proc.returncode == expected, label
    ctl = scratch/'control'; cal = scratch/'cal2'
    ct = '22_6_5_2_1_d9'; ca = '13_9_9_3_1_1_d9'; p1=2147483647; p2=2147483629
    run('ctl_driver', 'b28_01_driver.py', ['--lam',22,6,5,2,1,'--delta',9,'--a',24,'--nchi',21093,
        '--primes',p1,p2,'--out',ctl,'--wall-budget',3590,'--mem-cap',8000000000,'--rates',HOST/'frozen/gate_rates.json'])
    for p in (p1,p2):
        run('ctl_verify_'+str(p),'b28_01_verify.py',['--lam',22,6,5,2,1,'--delta',9,'--a',24,
            '--prime',p,'--dir',ctl,'--out',ctl/f'{ct}_p{p}_verify.json'])
    corrupt = ctl/'corrupt'; corrupt.mkdir()
    run('corrupt_kernel_input','b28_01_corrupt.py',['kernel',ctl/f'{ct}_p{p1}_K.u32',corrupt/'K_corrupt.u32',p1])
    run('corrupt_point_input','b28_01_corrupt.py',['pencil',ctl/f'{ct}_pencils.json',corrupt/'pencils_corrupt.json'])
    for kind, flag, path in [('kernel','--kernel',corrupt/'K_corrupt.u32'),('point','--pencils',corrupt/'pencils_corrupt.json')]:
        run('ctl_corrupt_'+kind,'b28_01_verify.py',['--lam',22,6,5,2,1,'--delta',9,'--a',24,
            '--prime',p1,'--dir',ctl,flag,path,'--out',corrupt/f'{ct}_p{p1}_verify_corrupt_{kind}.json'],expected=5)
    run('cal2_driver','b28_01_driver.py',['--lam',13,9,9,3,1,1,'--delta',9,'--a',70,'--nchi',732815,
        '--primes',p1,'--out',cal,'--wall-budget',int(3590-(time.monotonic()-start)),'--mem-cap',8000000000,
        '--rates',HOST/'frozen/gate_rates.json'])
    run('cal2_verify','b28_01_verify.py',['--lam',13,9,9,3,1,1,'--delta',9,'--a',70,
        '--prime',p1,'--dir',cal,'--out',cal/f'{ca}_p{p1}_verify.json'])
    manifest=json.loads(subprocess.check_output(GIT+['show',TIP+':results/b28_01/MANIFEST.json']))
    expected={x['path']: {k:x[k] for k in ('bytes','sha256')} for x in manifest['payloads']}
    retained=json.loads(subprocess.check_output(GIT+['show',TIP+':results/b28_01/HOST_RETAINED.json']))
    for x in retained['files']:
        if x['host_path'].startswith('out/'):
            expected['results/b28_01/'+x['host_path'][4:]]={k:x[k] for k in ('bytes','sha256')}
    comparisons=[]; retained_new=[]
    for path in sorted(scratch.rglob('*')):
        if not path.is_file(): continue
        rel=path.relative_to(scratch).as_posix(); got=sha(path)
        if rel.endswith('_receipt.json'):
            dest=receipts/rel; dest.parent.mkdir(parents=True,exist_ok=True); shutil.copyfile(path,dest)
            continue
        key='results/b28_01/'+rel
        comparisons.append(dict(path=rel,actual=got,expected=expected[key],byte_identical=got==expected[key]))
        if got['bytes']<=5000000:
            dest=OUT/'replay'/rel; dest.parent.mkdir(parents=True,exist_ok=True); shutil.copyfile(path,dest)
        else: retained_new.append(dict(path=rel,host_path=str(path),**got))
    assert all(x['byte_identical'] for x in comparisons)
    # Paths of retained files are receipt metadata, not mathematical output.
    save(receipts/'host_retained_receipt.json',dict(files=retained_new))
    save(OUT/'REPLAY_COMPARISON.json',dict(schema='r28-01-replay/1',evidence='COMPUTED',
        selected_calibration='(13,9,9,3,1,1), k=9, p=2147483647',comparisons=comparisons,
        all_mathematical_outputs_byte_identical=True,calibration_cells_run=1,cellA_built=False))
    for group, sub in [('engine','engine'),('frozen','frozen')]:
        for ent in bind[group]: assert sha(HOST/sub/ent['name']) == {k:ent[k] for k in ('bytes','sha256')}
    assert not (HOST/'out/cellA').exists()
    save(receipts/'completion_receipt.json',dict(wall_seconds=time.monotonic()-start,runs=len(runs),
        output=sha(OUT/'REPLAY_COMPARISON.json'),script=sha(pathlib.Path(__file__)),frozen_host_bytes_unchanged=True))
    print('Replay complete:',len(comparisons),'mathematical files byte-identical.',flush=True)

if __name__=='__main__': main()
