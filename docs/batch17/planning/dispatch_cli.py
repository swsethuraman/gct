"""Launch only explicitly requested ready slots, preserving sandbox and automatic operation review."""
import json,subprocess,sys,hashlib,shutil
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parent.parent;B=ROOT/'Batch17';L=B/'launch'
manifest=json.loads((L/'INPUT_MANIFEST.json').read_text());out=B/'DISPATCHED.json'
dispatch=json.loads(out.read_text());exe=shutil.which('codex')
assert exe and json.loads((L/'PREFLIGHT.json').read_text())['status']=='PASS'
for pin in manifest['inputs']:
    assert hashlib.sha256(Path(pin['path']).read_bytes()).hexdigest()==pin['sha256'],pin['path']
for slot in sys.argv[1:]:
    assert not any(t['slot']==slot for t in dispatch['tasks']),'Already dispatched '+slot
    task=next(t for t in manifest['tasks'] if t['slot']==slot)
    assert task['status']=='READY',slot
    brief=Path(task['brief']);assert hashlib.sha256(brief.read_bytes()).hexdigest()==task['sha256']
    stdout=L/f'B17-{slot}.jsonl';stderr=L/f'B17-{slot}.stderr.txt';last=L/f'B17-{slot}.final.md'
    argv=[exe,'--search','exec','--approve-for-me','-m','gpt-6-astra','-c','model_reasoning_effort="xhigh"','-C',task['worktree'],'--json','--color','never','-o',str(last),'-']
    with brief.open('rb') as fi,stdout.open('wb') as fo,stderr.open('wb') as fe:
        p=subprocess.Popen(argv,stdin=fi,stdout=fo,stderr=fe,cwd=task['worktree'],creationflags=subprocess.CREATE_NO_WINDOW|subprocess.CREATE_NEW_PROCESS_GROUP)
    receipt=dict(**task,pid=p.pid,launched_utc=datetime.now(timezone.utc).isoformat(),argv=argv,stdout=str(stdout),stderr=str(stderr),state='PROCESS_STARTED_THREAD_PENDING',transport='codex exec; workspace-write with operation-specific automatic review')
    dispatch['tasks'].append(receipt);dispatch['status']='LAUNCHING'
    out.write_text(json.dumps(dispatch,indent=2)+'\n')
    print(json.dumps(dict(slot=slot,pid=p.pid)),flush=True)
