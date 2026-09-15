"""Explicit bounded continuations of existing Slots04/11 after fresh read-only checks."""
import json,sqlite3,subprocess,ctypes
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parent.parent; B=ROOT/'Batch17'; L=B/'launch'
exe=Path(r'C:\Users\swami\AppData\Local\OpenAI\Codex\bin\bffc5354119c8421\codex.exe');assert exe.exists()
d=json.loads((B/'DISPATCHED.json').read_text()); pins=json.loads((L/'PREFLIGHT.json').read_text())['worktrees']
c=sqlite3.connect('file:C:/Users/swami/.codex/state_5.sqlite?mode=ro',uri=True);c.row_factory=sqlite3.Row
k=ctypes.WinDLL('kernel32',use_last_error=True);k.OpenProcess.restype=ctypes.c_void_p;k.CloseHandle.argtypes=[ctypes.c_void_p]
prompts={
'04':'''User has authorized continuing Batch17. Resume your SAME session and existing worktree. The integrator explicitly authorizes ONE corrected bounded invocation of your saved b17_04 verifier, max60seconds/512MiB, one process and BLAS thread, through inspected b15_bound.py with a new uniquely named log. Inspect all saved receipts and corrected code first; pin current inputs. This resolves the integrator-authorization blocker from the first failed rational-constructor run. Do not expand scope or rerun successful historical computations. Produce the basis-match/minor certificate if possible and update your report and manifest accurately; a rank floor9 is not exact rank9 without a global upper. A failure/cap must be reported, not retried unboundedly. Preserve Astra/xhigh and ordinary operation-specific approvals, sandbox, ownership and Git trust. No agents, worktrees, commits, push or publication. No heavy lease. Write only your existing owned b17_04 paths and log receipts.''',
'11':'''User has authorized continuing Batch17. Resume SAME session/worktree, preserve your accepted first-stage report and certificates. Add a separate b17_11_supplement02.md reviewing the newly finished sibling B15-02/docs/b17_02_report.md and its proof/certificate. Check the explicit skew/symmetric arc, coordinate convention, orbit multiplicity source, forbidden-weight interval [0,2d], ambient clipping threshold, and all-degree negative control for entry-diagonal arcs. No numerical improvement is claimed by producer. The integrator finds the written bound derivation sound provisionally, but requests independent scoped acceptance before numerical use. You may run ONE new bounded independent control if needed,60sec/512MiB, one process/BLAS thread using inspected original wrapper; no heavy lease or representation census. Update manifest with separately pinned inputs. Do not wait for unfinished04 or held09/10; finish this bounded supplement. Preserve Astra/xhigh, sandbox/config/ownership/trust, normal operation-specific approvals; no agents/worktrees/commits/push/publication.'''}
# All checks before any launch.
for slot in prompts:
 task=next(t for t in d['tasks'] if t['slot']==slot)
 handle=k.OpenProcess(0x1000,False,task['pid'])
 if handle:k.CloseHandle(handle);raise RuntimeError('Recorded process still exists: '+slot)
 row=c.execute('select * from threads where id=?',(task['threadId'],)).fetchone();assert row
 assert row['model']=='gpt-6-astra' and row['reasoning_effort']=='xhigh'
 lifecycle=None
 for line in Path(row['rollout_path']).read_text(encoding='utf-8').splitlines():
  event=json.loads(line); payload=event.get('payload',{})
  if event.get('type')=='event_msg' and payload.get('type') in ('task_started','task_complete','task_aborted'):lifecycle=payload['type']
 assert lifecycle in ('task_complete','task_aborted'),(slot,lifecycle)
 pin=next(w for w in pins if w['slot']==slot)
 for key,args in [('head',['rev-parse','HEAD']),('tree',['rev-parse','HEAD^{tree}']),('branch',['branch','--show-current'])]:
  result=subprocess.run(['git','-C',task['worktree'],*args],capture_output=True,text=True,check=True);assert result.stdout.strip()==pin[key]
 subprocess.run([task['python'],'-B','-c','import flint,sympy; assert sympy.Matrix([[1,2],[3,4]]).det()==-2'],check=True,timeout=30)
 print('PASS current session/Git/runtime '+slot,flush=True)
for slot,prompt in prompts.items():
 task=next(t for t in d['tasks'] if t['slot']==slot); attempt=len(task.get('continuations',[]))+1
 brief=L/f'B17-{slot}.continuation{attempt}.md';assert not brief.exists();brief.write_text(prompt+'\n')
 stdout=L/f'B17-{slot}.continuation{attempt}.jsonl';stderr=L/f'B17-{slot}.continuation{attempt}.stderr.txt'
 argv=[str(exe),'--search','exec','--approve-for-me','-C',task['worktree'],'-m','gpt-6-astra','-c','model_reasoning_effort="xhigh"','resume',task['threadId'],'-','--json','-o',str(L/f'B17-{slot}.continuation{attempt}.final.md')]
 with brief.open('rb') as fi,stdout.open('wb') as fo,stderr.open('wb') as fe:
  child=subprocess.Popen(argv,stdin=fi,stdout=fo,stderr=fe,cwd=task['worktree'],creationflags=subprocess.CREATE_NO_WINDOW|subprocess.CREATE_NEW_PROCESS_GROUP)
 task.setdefault('previous_runs',[]).append({key:task.get(key) for key in ('pid','stdout','stderr','state','error')})
 task.setdefault('continuations',[]).append(dict(attempt=attempt,utc=datetime.now(timezone.utc).isoformat(),pid=child.pid,argv=argv,brief=str(brief)))
 task.update(pid=child.pid,stdout=str(stdout),stderr=str(stderr),state='CONTINUATION_STARTED');task.pop('error',None)
 (B/'DISPATCHED.json').write_text(json.dumps(d,indent=2)+'\n');print(json.dumps(dict(slot=slot,pid=child.pid,threadId=task['threadId'])),flush=True)
