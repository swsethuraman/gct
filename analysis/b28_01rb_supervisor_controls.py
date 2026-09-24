#!/usr/bin/env python3
"""Bounded deterministic P5 boundary controls; only tiny synthetic outputs."""
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time

if len(sys.argv) > 1 and sys.argv[1] == '--term-resistant-child':
    signal.signal(signal.SIGTERM, signal.SIG_IGN)
    Path(sys.argv[2]).write_text(str(os.getpid()))
    time.sleep(40)
    raise SystemExit(0)

OUT = Path(__file__).resolve().parents[1] / 'results/b28_01rb'
TMP = Path('/tmp/b28_01rb_supervisor_controls')
SUP = Path.home() / 'b28_01/frozen_c/b28_01c_supervise.py'
def fd(p):
    b=p.read_bytes()
    return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def save(p,x):
    p.write_text(json.dumps(x,indent=2,sort_keys=True)+'\n')
assert fd(SUP)['sha256'] == '772979a1e2c72c9f854c12d4ca3e0a708047ddfbdff10ca93fbd4603312a9b4e'
TMP.mkdir(exist_ok=False)
start=time.monotonic()
records=[]
def launch(name,argv,cap,stop):
    d=TMP/name
    (d/'out').mkdir(parents=True)
    cmd=[sys.executable,str(SUP),'--cap-secs',str(cap),'--out',str(d/'out'),'--artifact-stop',str(stop),'--receipt',str(d/'job_receipt.json'),'--steps',json.dumps([dict(label='step',argv=argv)])]
    t=time.monotonic()
    p=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=45)
    rec=json.loads((d/'job_receipt.json').read_text())
    records.append(dict(name=name,argv=cmd,rc=p.returncode,stdout=p.stdout.decode(),wall_seconds=time.monotonic()-t,supervisor_receipt=rec,outputs=[dict(path=str(q.relative_to(TMP)),**fd(q)) for q in sorted(d.rglob('*')) if q.is_file()]))
    return p.returncode,rec

# A process which exits before the first poll can exceed the artifact cap.
d=TMP/'fast_artifact'/'out'
artifact_code='from pathlib import Path; import sys; Path(sys.argv[1]).write_bytes(bytes(2048))'
rc,rec=launch('fast_artifact',[sys.executable,'-c',artifact_code,str(d/'blob')],10,1024)
artifact=dict(exit=rc,resource_stop=rec['resource_stop'],artifact_bytes=rec['artifact_bytes_at_end'],limit_bytes=1024,stop_enforced=(rc==125))

# GNU time is the process-group leader. Its exit does not prove its child exited.
pidpath=TMP/'child_pid_receipt.txt'
child_rc=None
alive=False
cleanup=False
try:
    rc,rec=launch('term_resistant',[sys.executable,str(Path(__file__).resolve()),'--term-resistant-child',str(pidpath)],2,1000000)
    child_pid=int(pidpath.read_text())
    proc=Path('/proc')/str(child_pid)/'stat'
    state=proc.read_text().split(') ',1)[1].split()[0] if proc.exists() else None
    alive=state not in (None,'Z')
    child_rc=rc
    records[-1]['child_pid']=child_pid
    records[-1]['child_state_after_supervisor']=state
finally:
    if pidpath.exists():
        child_pid=int(pidpath.read_text())
        try:
            os.kill(child_pid,signal.SIGKILL)
            cleanup=True
        except ProcessLookupError:
            cleanup=True
result=dict(schema='r28-01b-supervisor-controls/1',evidence='COMPUTED synthetic exact boundary controls, no mathematical cell',fast_artifact=artifact,term_resistant_child=dict(supervisor_exit=child_rc,child_running_after_supervisor_exit=alive,whole_group_termination_enforced=not alive,reviewer_cleanup_performed=cleanup))
save(OUT/'SUPERVISOR_CONTROLS.json',result)
cg=Path('/sys/fs/cgroup')/Path('/proc/self/cgroup').read_text().strip().split('::',1)[1].lstrip('/')
save(OUT/'supervisor_controls_receipt.json',dict(command='systemd-run --user --scope -p MemoryMax=512000000 -p MemorySwapMax=0 timeout --kill-after=2 60 python3 analysis/b28_01rb_supervisor_controls.py',input=fd(SUP),script=fd(Path(__file__)),wall_seconds=time.monotonic()-start,memory_max=(cg/'memory.max').read_text().strip(),memory_swap_max=(cg/'memory.swap.max').read_text().strip(),scope_peak=(cg/'memory.peak').read_text().strip(),runs=records,output=fd(OUT/'SUPERVISOR_CONTROLS.json')))
print(json.dumps(result))
