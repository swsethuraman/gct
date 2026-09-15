"""Release Slot 11 only after read-only worktree/session checks; preserve launch history."""
import hashlib,json,sqlite3,subprocess,os,runpy,sys
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parent.parent
B=ROOT/'Batch17'; L=B/'launch'
manifest=json.loads((L/'INPUT_MANIFEST.json').read_text())
dispatch=json.loads((B/'DISPATCHED.json').read_text())
assert not any(t['slot']=='11' for t in dispatch['tasks'])
task=next(t for t in manifest['tasks'] if t['slot']=='11')
assert task['status']=='HELD'
worktree=Path(task['worktree'])
assert not list((worktree/'docs').glob('b17_11*'))
c=sqlite3.connect('file:C:/Users/swami/.codex/state_5.sqlite?mode=ro',uri=True)
existing=c.execute("select id,title from threads where (title like '%B17-11%' or name like '%B17-11%')").fetchall()
assert not existing,existing
pin=next(w for w in json.loads((L/'PREFLIGHT.json').read_text())['worktrees'] if w['slot']=='11')
for key,args in [('head',['rev-parse','HEAD']),('tree',['rev-parse','HEAD^{tree}']),('branch',['branch','--show-current'])]:
 p=subprocess.run(['git','-C',str(worktree),*args],capture_output=True,text=True,check=True)
 assert p.stdout.strip()==pin[key]
assert not subprocess.run(['git','-C',str(worktree),'diff','--name-only','HEAD'],capture_output=True,text=True,check=True).stdout.strip()
subprocess.run([task['python'],'-B','-c','import sympy; assert sympy.Matrix([[1,2],[3,4]]).det()==-2'],check=True,timeout=30)
brief=Path(task['brief']); original=brief.read_bytes()
assert hashlib.sha256(original).hexdigest()==task['sha256']
backup=L/'B17-11.initial-held.md'; assert not backup.exists(); backup.write_bytes(original)
sources=[]
for slot in ['01','03','05','06','07']:
 path=ROOT/f'work/batch15_workers/B15-{slot}/docs/b17_{slot}_report.md'
 sources.append(dict(slot=slot,path=str(path),sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
append='''

Integrator release: the substantive-output gate is met. Start independent review now.
Review saved reports for slots 01,03,05,06,07 in the sibling B15-NN/docs directories.
Prioritize 01's claim about closure (not merely exact matrix representations), 03's all-degree four-row exclusion and representation-theoretic transfer, then 05's exact image versus full LMR ideal distinction. Audit 06 and 07 to the extent feasible in this bounded session. Inspect linked proof artifacts, not only report summaries. Distinguish ACCEPTED, REJECTED, and UNVERIFIED claim by claim; document any missing controls. Reports 02/04/12 are unfinished: do not treat their partial claims as accepted. Slots 09/10 have no candidates yet, so do not wait for them. Deliver a first-stage review that enables a responsible Slot08 selection or explicitly identifies the remaining blocker. Existing compute cap remains unchanged; no heavy lease.
'''
brief.write_text(original.decode('utf-8')+append,encoding='utf-8')
task.update(status='READY',sha256=hashlib.sha256(brief.read_bytes()).hexdigest())
(L/'INPUT_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
(L/'B17-11.RELEASE.json').write_text(json.dumps(dict(released_utc=datetime.now(timezone.utc).isoformat(),slot='11',reason='Five substantive reports available; user requests eligible remaining sessions',sources=sources,git_read_only=True,heavy_lease=False),indent=2)+'\n')
os.environ['PATH']=r'C:\Users\swami\AppData\Local\OpenAI\Codex\bin\bffc5354119c8421'+os.pathsep+os.environ['PATH']
sys.argv=['dispatch_cli.py','11']
runpy.run_path(str(ROOT/'Batch17_Planning/dispatch_cli.py'),run_name='__main__')
