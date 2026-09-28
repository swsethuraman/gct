#!/usr/bin/env python3
"""Replay the hash-bound repair controls and cal2, never Cell A or cal1."""
import contextlib
import hashlib
import json
import os
from pathlib import Path
import runpy
import sys
import time

OUT = Path(__file__).resolve().parents[1] / 'results/b28_01rb'
SCRATCH = Path('/tmp/b28_01rb_replay_5a3174cd')
F = Path.home() / 'b28_01/frozen_c'
def fd(p):
    h = hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1048576),b''):
            h.update(b)
    return dict(bytes=p.stat().st_size,sha256=h.hexdigest())
def save(p,obj):
    p.write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')
assert not SCRATCH.exists()
bindings = json.loads((OUT/'BINDINGS.json').read_text())
for e in bindings['frozen']:
    assert fd(Path.home()/'b28_01'/e['host_path']) == {k:e[k] for k in ('bytes','sha256')}
cg = Path('/sys/fs/cgroup') / Path('/proc/self/cgroup').read_text().strip().split('::',1)[1].lstrip('/')
assert (cg/'memory.max').read_text().strip() == '8000000000'
assert (cg/'memory.swap.max').read_text().strip() == '0'
start = time.monotonic()
sys.argv = [str(F/'b28_01c_controls.py'),str(F),str(SCRATCH)]
module = runpy.run_path(sys.argv[0],run_name='r28_01b_bound_controls')
original_run = module['run']
skipped = []
def run(label,*args,**kwargs):
    if label == 'cal1_gate_only':
        skipped.append(label)
        return
    return original_run(label,*args,**kwargs)
module['main'].__globals__['run'] = run
rc = 1
try:
    with (OUT/'replay_stdout_receipt.txt').open('w') as log, contextlib.redirect_stdout(log):
        try:
            module['main']()
        except SystemExit as e:
            rc = int(e.code or 0)
finally:
    output_hashes = [dict(path=str(p.relative_to(SCRATCH)),**fd(p)) for p in sorted(SCRATCH.rglob('*')) if p.is_file()]
    rec = dict(schema='r28-01b-replay-receipt/1',command='systemd-run --user --scope -p MemoryMax=8000000000 -p MemorySwapMax=0 timeout --kill-after=10 3500 python3 analysis/b28_01rb_replay.py',script=fd(Path(__file__)),input_binding=fd(OUT/'BINDINGS.json'),frozen=bindings['frozen'],wall_seconds=time.monotonic()-start,rc=rc,memory_max=8000000000,memory_swap_max=0,scope_peak=(cg/'memory.peak').read_text().strip(),memory_events=(cg/'memory.events').read_text(),timeout_seconds=3500,skipped=skipped,reason_skipped='Only cal2 is replayed; cal1 is already accepted and its committed gate inputs suffice.',scratch=str(SCRATCH),outputs=output_hashes)
    save(OUT/'replay_receipt.json',rec)
    if (SCRATCH/'controls_receipt.json').exists():
        (OUT/'controls_receipt.json').write_bytes((SCRATCH/'controls_receipt.json').read_bytes())
print(json.dumps(dict(rc=rc,seconds=rec['wall_seconds'],scope_peak=rec['scope_peak'],skipped=skipped)))
raise SystemExit(rc)
