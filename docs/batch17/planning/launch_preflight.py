"""Read-only Git/runtime/session preflight. Writes only Batch17 launch receipts."""
import json,sqlite3,subprocess,sys
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'Batch17/launch';OUT.mkdir(parents=True,exist_ok=True)
old=json.loads((ROOT/'Batch16/launch/INPUT_MANIFEST.json').read_text())
rows=[]
for w in old['worktrees']:
    def git(*args):
        p=subprocess.run(['git','-C',w['worktree'],*args],capture_output=True,text=True)
        if p.returncode:raise RuntimeError(p.stderr)
        return p.stdout.strip()
    actual=dict(head=git('rev-parse','HEAD'),tree=git('rev-parse','HEAD^{tree}'),branch=git('branch','--show-current'))
    assert all(actual[k]==w[k] for k in actual),(w['slot'],actual)
    assert not git('diff','--name-only','HEAD'),w['slot']
    py=Path(w['worktree'])/'.venv/Scripts/python.exe'
    if not py.exists():py=Path(w['worktree'])/'.venv/python.exe'
    env=__import__('os').environ.copy()
    for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):env[k]='1'
    probe=subprocess.run([str(py),'-B','-c','import json,numpy,sympy,flint; assert sympy.Matrix([[1,2],[3,4]]).det()==-2; print(json.dumps(dict(numpy=numpy.__version__,sympy=sympy.__version__,flint=flint.__version__,exact_control=-2)))'],capture_output=True,text=True,timeout=30,env=env)
    assert probe.returncode==0,probe.stderr
    rows.append(dict(**w,python=str(py),runtime=json.loads(probe.stdout),tracked_changes=0))
    print('PASS worktree/runtime '+w['slot'],flush=True)
c=sqlite3.connect('file:C:/Users/swami/.codex/state_5.sqlite?mode=ro',uri=True);c.row_factory=sqlite3.Row
prior=json.loads((ROOT/'Batch16/DISPATCHED.json').read_text())['tasks'];sessions=[]
for oldtask in prior:
    tid=oldtask['result']['threadId'];r=c.execute('select id,rollout_path,model,reasoning_effort,updated_at from threads where id=?',(tid,)).fetchone()
    if r is None:raise RuntimeError('Missing previous session '+tid)
    entry=dict(r);last=None
    for line in Path(r['rollout_path']).open(encoding='utf-8'):
        e=json.loads(line);p=e.get('payload',{})
        if e.get('type')=='event_msg' and p.get('type') in ('task_started','task_complete','task_aborted'):
            last=p.get('type')
    entry.pop('rollout_path');entry['last_lifecycle_event']=last;sessions.append(entry)
    assert last in ('task_complete','task_aborted'),entry
duplicates=[dict(r) for r in c.execute("select id,title,model,reasoning_effort from threads where title like 'B17-%' or name like 'B17-%'")]
result=dict(status='PASS',checked_utc=datetime.now(timezone.utc).isoformat(),worktrees=rows,prior_sessions=sessions,b17_existing=duplicates,git_mutations=False)
(OUT/'PREFLIGHT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(status='PASS',worktrees=len(rows),prior_sessions=len(sessions),b17_existing=duplicates)))
