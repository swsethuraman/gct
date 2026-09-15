"""Batch16 preflight. Reuse twelve worktrees; never mutate Git configuration."""
from pathlib import Path
import json, os, sqlite3, subprocess, sys
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'Batch16/launch'
OUT.mkdir(exist_ok=True)
tasks=json.loads((ROOT/'Batch15_Launch/native_20260913/DISPATCHED.json').read_text())['tasks']
def save(name,data): (OUT/name).write_text(json.dumps(data,indent=2)+'\n')
if '--git' in sys.argv:
    rows=[]
    for t in tasks:
        def git(*args):
            p=subprocess.run(['git','-C',t['worktree'],*args],capture_output=True,text=True)
            if p.returncode: raise RuntimeError(p.stderr)
            return p.stdout.strip()
        branch=git('branch','--show-current')
        assert branch==t['branch']
        rows.append(dict(slot=t['slot'],worktree=t['worktree'],branch=branch,head=git('rev-parse','HEAD'),tree=git('rev-parse','HEAD^{tree}'),status=git('status','--porcelain=v1'),common_dir=git('rev-parse','--git-common-dir')))
    save('git_preflight.json',dict(status='PASS',checked_utc=datetime.now(timezone.utc).isoformat(),rows=rows,scope='Read-only Git identity/status; no configuration/index/ownership changes'))
    print('PASS12 read-only Git checks')
else:
    db=sqlite3.connect('file:C:/Users/swami/.codex/state_5.sqlite?mode=ro',uri=True)
    db.row_factory=sqlite3.Row
    records=[dict(r) for r in db.execute('select id,title,cwd,archived from threads')]
    matches=[r for r in records if 'b16-' in r['title'].lower()]
    save('registry_before.json',matches)
    assert not matches, 'Existing B16 tasks require reconciliation'
    env=os.environ.copy();env.update(PYTHONUTF8='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1')
    rows=[]
    for t in tasks:
        w=Path(t['worktree']); slot=t['slot']
        cmd=[str(w/'.venv/python.exe'),'-B',str(w/'analysis/b15_bound.py'),'--slot',slot,'--name','b16_'+slot+'_runtime','--seconds','30','--memory-mb','512',str(w/'.venv/b15_runtime_control.py')]
        p=subprocess.run(cmd,cwd=w,env=env,capture_output=True,text=True,timeout=45)
        row=dict(slot=slot,returncode=p.returncode,stdout=p.stdout,stderr=p.stderr)
        save('runtime_'+slot+'.json',row);rows.append(row)
        assert p.returncode==0,row
        print('PASS runtime',slot,flush=True)
    save('runtime_preflight.json',dict(status='PASS',rows=rows,registry_matches=matches,checked_utc=datetime.now(timezone.utc).isoformat()))
