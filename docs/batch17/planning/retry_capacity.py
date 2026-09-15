"""One explicit same-session retry for capacity-interrupted B17 workers."""
import json,subprocess,shutil,ctypes
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parent.parent;B=ROOT/'Batch17';L=B/'launch'
p=B/'DISPATCHED.json';d=json.loads(p.read_text());exe=shutil.which('codex');assert exe
kernel=ctypes.WinDLL('kernel32',use_last_error=True)
kernel.OpenProcess.restype=ctypes.c_void_p
kernel.CloseHandle.argtypes=[ctypes.c_void_p]
for slot in ('02','06','12'):
    task=next(t for t in d['tasks'] if t['slot']==slot)
    assert task['state']=='ERROR' and 'capacity' in json.dumps(task.get('error',{})).lower(),slot
    handle=kernel.OpenProcess(0x1000,False,task['pid'])
    if handle:
        kernel.CloseHandle(handle);raise RuntimeError('Original process still exists; inspect before retry: '+slot)
    attempt=len(task.get('retries',[]))+1
    brief=L/f'B17-{slot}.retry{attempt}.md'
    brief.write_text('Resume the existing Batch17 assignment after the Astra capacity interruption. Retain gpt-6-astra/xhigh, original worktree and all original sandbox/approval/resource constraints. Inspect your saved files and receipts first; continue from the completed work instead of repeating successful calculations. No new heavy lease or expanded computation is authorized. Finalize your scoped report and input/resource manifest if the mathematics is already complete. Distinguish proved results, inherited premises and unresolved claims. Do not create another session or delegate.\n',encoding='utf-8')
    stdout=L/f'B17-{slot}.retry{attempt}.jsonl';stderr=L/f'B17-{slot}.retry{attempt}.stderr.txt'
    argv=[exe,'--search','exec','--approve-for-me','-C',task['worktree'],'-m','gpt-6-astra','-c','model_reasoning_effort="xhigh"','resume',task['threadId'],'-','--json','-o',str(L/f'B17-{slot}.final.md')]
    with brief.open('rb') as fi,stdout.open('wb') as fo,stderr.open('wb') as fe:
        child=subprocess.Popen(argv,stdin=fi,stdout=fo,stderr=fe,cwd=task['worktree'],creationflags=subprocess.CREATE_NO_WINDOW|subprocess.CREATE_NEW_PROCESS_GROUP)
    old={k:task.get(k) for k in ('pid','stdout','stderr','state','error')}
    task.setdefault('previous_runs',[]).append(old)
    task.setdefault('retries',[]).append(dict(attempt=attempt,utc=datetime.now(timezone.utc).isoformat(),pid=child.pid,argv=argv))
    task.update(pid=child.pid,stdout=str(stdout),stderr=str(stderr),state='RETRY_PROCESS_STARTED')
    task.pop('error',None)
    p.write_text(json.dumps(d,indent=2)+'\n')
    print(json.dumps(dict(slot=slot,pid=child.pid,threadId=task['threadId'])),flush=True)
