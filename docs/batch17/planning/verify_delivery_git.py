"""Read-only final Git delivery verification; no trust/config/worktree mutations."""
import json,subprocess
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parent.parent;B=ROOT/'Batch17'
pins=json.loads((B/'launch/PREFLIGHT.json').read_text())['worktrees'];rows=[]
for pin in pins:
 def git(*args):
  p=subprocess.run(['git','-C',pin['worktree'],*args],capture_output=True,text=True,check=True)
  return p.stdout.strip()
 actual={key:git(*args) for key,args in [('head',['rev-parse','HEAD']),('tree',['rev-parse','HEAD^{tree}']),('branch',['branch','--show-current'])]}
 same=all(actual[key]==pin[key] for key in actual)
 tracked=git('diff','--name-only','HEAD')
 rows.append(dict(slot=pin['slot'],worktree=pin['worktree'],**actual,matches_launch_pin=same,tracked_changes=tracked.splitlines()))
result=dict(checked_utc=datetime.now(timezone.utc).isoformat(),status='PASS' if all(r['matches_launch_pin'] and not r['tracked_changes'] for r in rows) else 'REVIEW_REQUIRED',scope='HEAD, tree, branch and tracked diff versus launch; untracked research artifacts delivered by manifests, not committed',git_mutations=False,worktrees=rows)
(B/'GIT_DELIVERY_VERIFICATION.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(status=result['status'],worktrees=len(rows),git_mutations=False)))
