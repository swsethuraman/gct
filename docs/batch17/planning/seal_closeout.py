"""Metadata-only final acceptance binding. No scientific calculation or Git mutation."""
import json,hashlib
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parent.parent;B=ROOT/'Batch17'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def record(p):return dict(path=str(p),sha256=sha(p))
d=json.loads((B/'DISPATCHED.json').read_text());t=next(t for t in d['tasks'] if t['slot']=='11')
events=[json.loads(line) for line in Path(t['stdout']).read_text(encoding='utf-8').splitlines() if line.strip()]
life=[e['type'] for e in events if e['type'] in ('turn.started','turn.completed','turn.failed','error')]
assert life[-1]=='turn.completed',life[-1]
m11p=ROOT/'work/batch15_workers/B15-11/delivery/b17_11/MANIFEST.json';m11=json.loads(m11p.read_text())
assert '04/08 complete' in m11['scope']
m12p=ROOT/'work/batch15_workers/B15-12/delivery/b17_12/MANIFEST.json';m12=json.loads(m12p.read_text())
verified=[]
for manifest,items in [(m11,m11['artifacts']),(m12,m12['output_files'])]:
 for item in items:
  path=Path(item['path']);path=path if path.is_absolute() else Path(manifest['workspace'])/path
  assert sha(path)==item['sha256'],str(path)
  verified.append(record(path))
reviews=[ROOT/'work/batch15_workers/B15-11/docs'/name for name in ['b17_11_report.md','b17_11_supplement02.md','b17_11_supplement04_08.md']]
assert json.loads((B/'GIT_DELIVERY_VERIFICATION.json').read_text())['status']=='PASS'
entries=[]
for slot in ['01','02','03','04','05','06','07','08']:
 wp=ROOT/f'work/batch15_workers/B15-{slot}'
 entries.append(dict(slot=slot,status='ACCEPTED_SCOPED',report=record(wp/f'docs/b17_{slot}_report.md'),manifest=record(wp/f'delivery/b17_{slot}/MANIFEST.json')))
intake=dict(status='COMPLETE_SCOPED_ACCEPTANCE',sealed_utc=datetime.now(timezone.utc).isoformat(),entries=entries,reviews=[record(p) for p in reviews],reviewer_manifest=record(m11p),ledger_manifest=record(m12p),verified_delivery_files=verified,not_triggered=['09','10'],supplementary_cayley='PRODUCER_VERIFIED_ONLY; no independent acceptance',scope='No positive gap or asymptotic improvement. Original12 pending04/08 snapshot superseded by final reviewer supplement.')
(B/'INTAKE.json').write_text(json.dumps(intake,indent=2)+'\n')
coord=dict(status='COMPLETE',decision='STOP_CURRENT_EVALUATION_BRANCH_NO_FINITE_FAMILY',launched=[x['slot'] for x in d['tasks']],not_triggered=['09','10'],heavy_leases=[],automatic_release=False)
(B/'COORDINATION.json').write_text(json.dumps(coord,indent=2)+'\n')
close=dict(status='COMPLETE',closed_utc=datetime.now(timezone.utc).isoformat(),decision=coord['decision'],scoped_results_accepted=['01','02','03','04','05','06','07','08'],review='11 complete',ledger='12 complete; final intake supersedes pending-review snapshot',not_triggered=['09','10'],positive_multiplicity_gap=False,improved_asymptotic_growth=False,heavy_leases=[],git_mutations=False,artifacts=[record(B/name) for name in ['INTAKE.json','STOCKTAKE.md','COORDINATION.json','NOT_TRIGGERED.json','GIT_DELIVERY_VERIFICATION.json']],reviewer_manifest=record(m11p),ledger_manifest=record(m12p))
(B/'CLOSEOUT.json').write_text(json.dumps(close,indent=2)+'\n')
print(json.dumps(dict(status='COMPLETE',accepted_slots=8,verified_delivery_files=len(verified),not_triggered=['09','10'])))
