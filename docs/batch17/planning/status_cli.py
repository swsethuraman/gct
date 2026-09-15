"""Read worker JSONL and registry; update only integrator delivery receipts."""
import json,sqlite3
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parent.parent;B=ROOT/'Batch17';p=B/'DISPATCHED.json'
d=json.loads(p.read_text());c=sqlite3.connect('file:C:/Users/swami/.codex/state_5.sqlite?mode=ro',uri=True);c.row_factory=sqlite3.Row
for task in d['tasks']:
    last='PROCESS_STARTED_THREAD_PENDING';message=None
    for line in Path(task['stdout']).read_text(encoding='utf-8',errors='replace').splitlines():
        try:e=json.loads(line)
        except json.JSONDecodeError:continue
        if e['type']=='thread.started':task['threadId']=e['thread_id']
        if e['type']=='turn.started':last='RUNNING'
        if e['type']=='turn.completed':last='TURN_COMPLETE_REVIEW_PENDING'
        if e['type'] in ('turn.failed','error'):last='ERROR';task['error']=e
        if e['type']=='item.completed' and e.get('item',{}).get('type')=='agent_message':message=e['item'].get('text','')
    if last=='PROCESS_STARTED_THREAD_PENDING':
        stderr=Path(task['stderr']).read_text(encoding='utf-8',errors='replace')
        if 'already has an active writer' in stderr:
            last='RESUME_BLOCKED_ACTIVE_WRITER'
    task['state']=last
    if 'threadId' in task:
        row=c.execute('select model,reasoning_effort,approval_mode,sandbox_policy,cwd from threads where id=?',(task['threadId'],)).fetchone()
        if row:
            meta=dict(row);s=json.loads(meta.pop('sandbox_policy'));meta['sandbox_type']=s['type'];meta['filesystem']=s.get('file_system',{}).get('type');meta['network']=s.get('network')
            assert meta['model']=='gpt-6-astra' and meta['reasoning_effort']=='xhigh'
            assert meta['approval_mode']=='on-request' and meta['filesystem']=='restricted'
            task['verified_runtime']=meta
    if message:task['latest_message']=message[-2500:]
d['status']='FIRST_STAGE_DISPATCHED';d['checked_utc']=datetime.now(timezone.utc).isoformat()
p.write_text(json.dumps(d,indent=2)+'\n')
state=dict(status='ACTIVE_FIRST_STAGE',checked_utc=d['checked_utc'],launched=[t['slot'] for t in d['tasks']],
           held={'08':'reviewed 01/02/03/05 results','09':'one reviewed family from08','10':'reviewed B<U and actual padding plan','11':'substantive proof/certificate ready for independent review'},
           heavy_leases=[],model='gpt-6-astra',reasoning='xhigh',transport='CLI persistent sessions; app task tools unavailable',
           automatic_release=False,next='Review completed first-stage receipts, then release dependencies; no blind repeated dispatch')
state['held']={k:v for k,v in state['held'].items() if k not in state['launched']}
if (B/'NOT_TRIGGERED.json').exists():
    state['not_triggered']=json.loads((B/'NOT_TRIGGERED.json').read_text())['slots']
    state['held']={k:v for k,v in state['held'].items() if k not in state['not_triggered']}
(B/'COORDINATION.json').write_text(json.dumps(state,indent=2)+'\n')
print(json.dumps([dict(slot=t['slot'],threadId=t.get('threadId'),state=t['state'],verified='verified_runtime' in t,commentary=t.get('latest_message','')[:180]) for t in d['tasks']],indent=2))
