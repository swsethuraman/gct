#!/usr/bin/env python3
"""Launch exactly one unchanged frozen verifier in one capped systemd scope."""
import json, os, pathlib, platform, subprocess, sys, time
from b28_01rd_audit import ROOT, OUT, HOST, TAG, fileinfo, save

PY = pathlib.Path.home()/'b28venv/bin/python'
F = HOST/'frozen_d'
REC = OUT/'receipts'
RESULT = OUT/(TAG+'_p2147483647_verify.json')
env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', B28_VFY_SO=str(F/'b28_01c_vfy.so'))
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'): env[key]='1'

def inside():
    cg = pathlib.Path('/sys/fs/cgroup'+pathlib.Path('/proc/self/cgroup').read_text().strip().split('::')[1])
    assert (cg/'memory.max').read_text().strip() == '24000000000'
    assert (cg/'memory.swap.max').read_text().strip() == '0'
    argv = [str(PY),str(F/'b28_01c_verify.py'),'--lam','12','8','6','4','2','--delta','8','--a','109',
        '--prime','2147483647','--dir',str(OUT/'inputs'),'--kernel',str(HOST/'out/cellA'/(TAG+'_p2147483647_K.u32')),'--out',str(RESULT)]
    command = [str(PY),str(F/'b28_01d_supervise.py'),'--cap-secs','3540','--out',str(OUT),
        '--artifact-stop','50000000000','--receipt',str(REC/'job_receipt.json'),
        '--steps',json.dumps([dict(label='cellA_verify',argv=argv)])]
    save(REC/'scope_receipt.json',dict(cgroup=str(cg),memory_max=(cg/'memory.max').read_text().strip(),
        memory_swap_max=(cg/'memory.swap.max').read_text().strip(),runtime_max_sec=3600,
        supervisor_cap_sec=3540,command=command,platform=platform.platform(),
        versions=subprocess.check_output([str(PY),'-c','import sys,numpy,scipy,flint;print(sys.version.split()[0],numpy.__version__,scipy.__version__,flint.__version__)'],env=env,text=True).strip()))
    return subprocess.call(command,env=env)

def launch():
    assert not REC.exists() and not RESULT.exists(), 'one-run guard: prior run output exists'
    bindings = json.loads((OUT/'BINDINGS.json').read_text())
    for row in bindings['frozen_d']:
        assert fileinfo(F/row['path']) == {k:row[k] for k in ('bytes','sha256')}
    for row in bindings['host_retained']:
        assert fileinfo(HOST/row['host_path']) == {k:row[k] for k in ('bytes','sha256')}
    for p in (OUT/'inputs').iterdir():
        row = next(r for r in bindings['payloads'] if r['path'].endswith('/'+p.name))
        assert fileinfo(p) == {k:row[k] for k in ('bytes','sha256')}
    versions = subprocess.check_output([str(PY),'-c','import sys,numpy,scipy,flint;print(sys.version.split()[0],numpy.__version__,scipy.__version__,flint.__version__)'],env=env,text=True).strip()
    assert versions == '3.12.3 2.5.3 1.18.1 0.9.0', versions
    REC.mkdir()
    cmd = ['systemd-run','--user','--scope','--quiet','--unit=b28-01rd-review',
        '-p','MemoryMax=24000000000','-p','MemorySwapMax=0','-p','RuntimeMaxSec=3600',
        str(PY),str(pathlib.Path(__file__).resolve()),'--inside']
    start=time.time(); mono=time.monotonic()
    rc=subprocess.call(cmd,env=env)
    save(REC/'launch_receipt.json',dict(command=cmd,exit=rc,start_unix=start,end_unix=time.time(),
        elapsed_monotonic_secs=time.monotonic()-mono,script=fileinfo(pathlib.Path(__file__)),
        input_bindings=fileinfo(OUT/'BINDINGS.json'),output=fileinfo(RESULT) if RESULT.exists() else None))
    return rc

if __name__ == '__main__':
    sys.exit(inside() if sys.argv[1:] == ['--inside'] else launch())
