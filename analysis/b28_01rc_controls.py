#!/usr/bin/env python3
"""R28-01c reviewer-owned P5 fixtures. No imports of any matrix code."""
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time

SELF=Path(__file__).resolve()
if len(sys.argv)>1 and sys.argv[1]=='--term-resistant-child':
    # Same child body, duration and deadline as R28-01b's own failing fixture.
    signal.signal(signal.SIGTERM,signal.SIG_IGN)
    Path(sys.argv[2]).write_text(str(os.getpid()))
    time.sleep(40)
    raise SystemExit(0)
if len(sys.argv)>1 and sys.argv[1]=='--ordinary-child':
    time.sleep(40)
    raise SystemExit(0)
if len(sys.argv)>1 and sys.argv[1]=='--background-parent':
    child=subprocess.Popen([sys.executable,str(SELF),'--ordinary-child'])
    Path(sys.argv[2]).write_text(str(child.pid))
    raise SystemExit(0)

OUT=SELF.parents[1]/'results/b28_01rc'
FIX=OUT/'fixture_receipts'
SUP=Path.home()/'b28_01/frozen_d/b28_01d_supervise.py'
def fd(p):
    b=p.read_bytes();return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def save(p,obj):p.write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')
def group_exists(pgid):
    try:os.killpg(pgid,0);return True
    except ProcessLookupError:return False
def main():
    start=time.monotonic();FIX.mkdir(exist_ok=False)
    assert fd(SUP)['sha256']=='af3b5aa285713e20633189288589953b715d3027cb75432b959f0a485a2f7258'
    cg=Path('/sys/fs/cgroup')/Path('/proc/self/cgroup').read_text().strip().split('::',1)[1].lstrip('/')
    assert (cg/'memory.max').read_text().strip()=='512000000'
    assert (cg/'memory.swap.max').read_text().strip()=='0'
    record=dict(command='systemd-run --user --scope -p MemoryMax=512000000 -p MemorySwapMax=0 timeout --kill-after=2 60 python3 analysis/b28_01rc_controls.py',script=fd(SELF),input_supervisor=fd(SUP),binding_input=fd(OUT/'BINDINGS.json'),scope=dict(memory_max=512000000,memory_swap_max=0),timeout_seconds=60,runs=[])
    outcomes=[];pids=[]
    def run(name,steps,cap,limit,want,reason,extra=None):
        d=FIX/name;(d/'out').mkdir(parents=True)
        for st in steps:st['argv']=[a.replace('{DIR}',str(d)).replace('{OUT}',str(d/'out')) for a in st['argv']]
        argv=[sys.executable,str(SUP),'--cap-secs',str(cap),'--out',str(d/'out'),'--artifact-stop',str(limit),'--receipt',str(d/'job_receipt.json'),'--steps',json.dumps(steps)]
        t=time.monotonic()
        p=subprocess.run(argv,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=45)
        (d/'stdout_receipt.txt').write_bytes(p.stdout)
        job=json.loads((d/'job_receipt.json').read_text())
        groups_gone=all(not group_exists(st['pgid']) for st in job['steps'])
        result=dict(fixture=name,exit=p.returncode,expected_exit=want,resource_stop_reason=(job['resource_stop'] or {}).get('reason'),steps_recorded=len(job['steps']),groups_absent_by_independent_check=groups_gone,job_processes_remaining=job['job_processes_remaining_at_end'],subreaper=job['subreaper'])
        result['pass']=p.returncode==want and result['resource_stop_reason']==reason and groups_gone and result['job_processes_remaining']==0
        if extra:
            additions=extra(d,job)
            result['pass']=result['pass'] and additions.pop('pass',True)
            result.update(additions)
        outcomes.append(result)
        record['runs'].append(dict(fixture=name,argv=argv,rc=p.returncode,wall_seconds=time.monotonic()-t,stdout_sha256=hashlib.sha256(p.stdout).hexdigest(),job_receipt=fd(d/'job_receipt.json')))
        print(json.dumps(result),flush=True)
        assert result['pass'],name
    def child_check(d,job):
        pid=int((d/'child_pid_receipt.txt').read_text());pids.append(pid)
        absent=not (Path('/proc')/str(pid)).exists()
        listed=pid in job['steps'][0]['survivors_sigkilled']
        return dict(child_absent_by_independent_check=absent,child_listed_as_sigkilled=listed,**{'pass':outcomes_base_pass(job) and absent and listed})
    def outcomes_base_pass(job):
        return job['job_processes_remaining_at_end']==0 and all(not group_exists(s['pgid']) for s in job['steps'])
    try:
        run('term_resistant',[dict(label='child',argv=[sys.executable,str(SELF),'--term-resistant-child','{DIR}/child_pid_receipt.txt'])],2,1000000,124,'wall',child_check)
        writer=[sys.executable,'-c','from pathlib import Path; import sys; Path(sys.argv[1]).write_bytes(bytes(2048))','{OUT}/blob']
        def size_check(d,job):
            boundary='at the exit of step' in job['resource_stop']['detail']
            return dict(artifact_bytes=job['artifact_bytes_at_end'],artifact_limit_bytes=1024,boundary_detected=boundary,**{'pass':boundary and job['artifact_bytes_at_end']==2048})
        run('fast_writer',[dict(label='writer',argv=writer)],10,1024,125,'artifact',size_check)
        marker=[sys.executable,'-c','from pathlib import Path; import sys; Path(sys.argv[1]).write_text("ran")','{OUT}/marker']
        def marker_check(d,job):
            absent=not (d/'out/marker').exists()
            return dict(marker_absent=absent,**{'pass':job['exit']==125 and len(job['steps'])==1 and absent and outcomes_base_pass(job)})
        run('fast_writer_two_steps',[dict(label='writer',argv=writer),dict(label='marker',argv=marker)],10,1024,125,'artifact',marker_check)
        run('ordinary_wall',[dict(label='sleeper',argv=['/bin/sleep','60'])],3,1000000,124,'wall')
        run('normal_exit_background_child',[dict(label='parent',argv=[sys.executable,str(SELF),'--background-parent','{DIR}/child_pid_receipt.txt'])],10,1000000,0,None,child_check)
        assert all(x['pass'] and x['exit']==x['expected_exit'] for x in outcomes)
        assert all(not (Path('/proc')/str(pid)).exists() for pid in pids)
        save(OUT/'CONTROLS.json',dict(schema='r28-01c-controls/1',evidence='COMPUTED deterministic supervisor fixtures; independent process/group checks',input_supervisor_sha256=fd(SUP)['sha256'],fixtures=outcomes,all_pass=True,matrix_work=False,cellA_built=False))
        record['rc']=0
    except Exception as e:
        record['rc']=1;record['error']=repr(e);raise
    finally:
        # Only this harness's recorded test PIDs are eligible for fallback cleanup.
        remaining=[]
        for pidfile in FIX.glob('*/child_pid_receipt.txt'):
            pid=int(pidfile.read_text())
            if (Path('/proc')/str(pid)).exists():
                remaining.append(pid)
                try:os.kill(pid,signal.SIGKILL)
                except ProcessLookupError:pass
        record.update(wall_seconds=time.monotonic()-start,scope_peak_bytes=int((cg/'memory.peak').read_text()),memory_events=(cg/'memory.events').read_text(),fallback_cleanup_pids=remaining,outputs=[dict(path=str(p.relative_to(OUT)),**fd(p)) for p in sorted(FIX.rglob('*')) if p.is_file()])
        if (OUT/'CONTROLS.json').exists():record['certificate']=fd(OUT/'CONTROLS.json')
        save(OUT/'controls_receipt.json',record)
if __name__=='__main__':main()
