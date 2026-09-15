"""Read-only final source-head check; no new research commit is asserted."""
from pathlib import Path
import json,subprocess
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[2];B=ROOT/'Batch16'
mf=json.loads((B/'launch/INPUT_MANIFEST.json').read_text());rows=[]
for w in mf['worktrees']:
    def git(*args):
        p=subprocess.run(['git','-C',w['worktree'],*args],text=True,capture_output=True)
        if p.returncode: raise RuntimeError(p.stderr)
        return p.stdout.strip()
    head=git('rev-parse','HEAD');tree=git('rev-parse','HEAD^{tree}');branch=git('branch','--show-current')
    assert (head,tree,branch)==(w['head'],w['tree'],w['branch'])
    tracked=git('diff','--name-only','HEAD')
    assert not tracked, (w['slot'],tracked)
    rows.append(dict(slot=w['slot'],head=head,tree=tree,branch=branch,tracked_changes=0))
(B/'reviews/FINAL_GIT.json').write_text(json.dumps(dict(status='PASS12_FROZEN_HEADS_UNCHANGED_NO_TRACKED_DIFF',checked_utc=datetime.now(timezone.utc).isoformat(),rows=rows,limits='New B16 filesystem outputs remain uncommitted. No Git content/configuration/index/trust/ownership mutation.'),indent=2)+'\n')
print('PASS12 unchanged heads, trees, branches; no tracked diff')
