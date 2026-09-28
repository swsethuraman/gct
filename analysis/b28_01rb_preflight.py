#!/usr/bin/env python3
"""Run only the frozen launcher's read-only preflight; no measurement dispatch."""
import hashlib
import json
import os
from pathlib import Path
import resource
import subprocess
import time

OUT = Path(__file__).resolve().parents[1] / 'results/b28_01rb'
LAUNCHER = Path.home() / 'b28_01/frozen_c/b28_01c_cellA.sh'
def h(p):
    b = p.read_bytes()
    return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
start = time.monotonic()
assert h(LAUNCHER)['sha256'] == '3e823c4d6366a9f9bb4f5f7b7e7e6cd6e35b13008b38d079ba5283b0cd104453'
argv = ['/bin/bash',str(LAUNCHER),'--preflight-only']
p = subprocess.run(argv,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1'))
rec = dict(command=argv,input=h(LAUNCHER),script=h(Path(__file__)),wall_seconds=time.monotonic()-start,rc=p.returncode,stdout=p.stdout.decode(),stdout_sha256=hashlib.sha256(p.stdout).hexdigest(),maxrss_kib=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,timeout_seconds=60,address_limit_kib=500000)
(OUT/'preflight_receipt.json').write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n')
print(p.stdout.decode(),end='')
raise SystemExit(p.returncode)
