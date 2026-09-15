"""Release bounded Slot08 theory selection; numerical use of Slot02 remains review-gated."""
import hashlib,json,sqlite3,subprocess,os,runpy,sys
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parent.parent; B=ROOT/'Batch17'; L=B/'launch'
manifest=json.loads((L/'INPUT_MANIFEST.json').read_text());dispatch=json.loads((B/'DISPATCHED.json').read_text())
assert not any(t['slot']=='08' for t in dispatch['tasks'])
task=next(t for t in manifest['tasks'] if t['slot']=='08');assert task['status']=='HELD'
worktree=Path(task['worktree']);assert not list((worktree/'docs').glob('b17_08*'))
c=sqlite3.connect('file:C:/Users/swami/.codex/state_5.sqlite?mode=ro',uri=True);c.row_factory=sqlite3.Row
assert not c.execute("select id from threads where title like '%B17-08%' or name like '%B17-08%'").fetchall()
old=json.loads((ROOT/'Batch16/DISPATCHED.json').read_text())['tasks']
oldtask=next(t for t in old if t['slot']=='08');tid=oldtask['result']['threadId']
row=c.execute('select rollout_path from threads where id=?',(tid,)).fetchone();assert row
last=None
for line in Path(row['rollout_path']).read_text(encoding='utf-8').splitlines():
 e=json.loads(line);p=e.get('payload',{})
 if e.get('type')=='event_msg' and p.get('type') in ('task_started','task_complete','task_aborted'):last=p['type']
assert last in ('task_complete','task_aborted'),last
pin=next(w for w in json.loads((L/'PREFLIGHT.json').read_text())['worktrees'] if w['slot']=='08')
for key,args in [('head',['rev-parse','HEAD']),('tree',['rev-parse','HEAD^{tree}']),('branch',['branch','--show-current'])]:
 p=subprocess.run(['git','-C',str(worktree),*args],capture_output=True,text=True,check=True);assert p.stdout.strip()==pin[key]
subprocess.run([task['python'],'-B','-c','import flint,sympy; assert sympy.Matrix([[1,2],[3,4]]).det()==-2'],check=True,timeout=30)
brief=Path(task['brief']);original=brief.read_bytes();assert hashlib.sha256(original).hexdigest()==task['sha256']
backup=L/'B17-08.initial-held.md';assert not backup.exists();backup.write_bytes(original)
append='''

Integrator release for a bounded THEORY SELECTION contribution. This supersedes the blanket starting hold above, not the numerical-evaluation gate. Read B15-11/docs/b17_11_report.md: scoped01/03/05/06/07 claims are independently accepted. Read their original reports. Slot02 now has B15-02/docs/b17_02_report.md and a manifest; its independent review is running in Slot11. Its proposed bound min(a,s-rank C) and skew/symmetric arc can be analyzed provisionally, but do not call its claims reviewed or use them to authorize computation before a supplement is available. Do not idle-poll the reviewer; label dependencies in your finished report.

Try to nominate at most ONE specific finite representation family/cell with a concrete determinant upper-bound route, padding ceiling and actual-padding lower-bound construction. Prioritize exactly five rows, where01/03 locate first separation, and assess whether02's forbidden-weight projection can buy enough multiplicity loss after ambient clipping. Slot06 supplies an exact all-entry coefficient method, not a rank promise. If no supported candidate is available, explain the smallest missing lemma and close this selection proposal honestly. No unrestricted character census. This continuation is theory-only: no scientific computation, heavy lease or rank hunt. Pin inputs and price any proposed finite calculation for09 without executing it. 09/10 remain held until a reviewed numerical gate is met. A complete negative/no-candidate selection is acceptable. Keep original ownership, runtime/model, sandbox and approval constraints.
'''
brief.write_text(original.decode('utf-8')+append,encoding='utf-8');task.update(status='READY',sha256=hashlib.sha256(brief.read_bytes()).hexdigest())
(L/'INPUT_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
(L/'B17-08.RELEASE.json').write_text(json.dumps(dict(slot='08',released_utc=datetime.now(timezone.utc).isoformat(),scope='Theory-only selection;02 provisional pending independent review;09/10 remain gated',heavy_lease=False,git_read_only=True),indent=2)+'\n')
os.environ['PATH']=r'C:\Users\swami\AppData\Local\OpenAI\Codex\bin\bffc5354119c8421'+os.pathsep+os.environ['PATH'];sys.argv=['dispatch_cli.py','08']
runpy.run_path(str(ROOT/'Batch17_Planning/dispatch_cli.py'),run_name='__main__')
