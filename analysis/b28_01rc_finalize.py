#!/usr/bin/env python3
"""Bind the completed R28-01c review and its complete resource receipts."""
import hashlib
import json
from pathlib import Path
import resource
import time

WT=Path(__file__).resolve().parents[1]
OUT=WT/'results/b28_01rc'
def fd(p):
    b=p.read_bytes();return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def save(p,x):p.write_text(json.dumps(x,indent=2,sort_keys=True)+'\n')
start=time.monotonic()
receipts=['binding_receipt.json','controls_attempt1_receipt.json','controls_receipt.json']
runs=[]
for n in receipts:
    r=json.loads((OUT/n).read_text())
    runs.append(dict(path='results/b28_01rc/'+n,**fd(OUT/n),command=r['command'],wall_seconds=r['wall_seconds']))
total=sum(r['wall_seconds'] for r in runs)
assert total<900
controls=json.loads((OUT/'CONTROLS.json').read_text());assert controls['all_pass']
save(OUT/'RESOURCE_RECEIPT.json',dict(schema='r28-01c-resource-receipt/1',runs=runs,invocations_including_finalize=4,fixture_runs_executed=1,failed_parser_invocations=1,aggregate_measured_seconds_before_finalize=total,slot_compute_limit_seconds=900,fixture_scope=dict(memory_max=512000000,memory_swap_max=0,timeout_seconds=60),binding_and_finalize_limits=dict(address_limit_kib=500000,timeout_seconds=60),matrix_work=False,cellA_built=False,installs=0,launcher_preflight_invocations=1,finalize=dict(command='timeout 60 bash -c "ulimit -v 500000; exec python3 analysis/b28_01rc_finalize.py"',script=fd(Path(__file__)),wall_seconds_before_manifest=time.monotonic()-start,maxrss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)))
paths=[WT/'docs/b28_01rc_review.md']+sorted((WT/'analysis').glob('b28_01rc_*'))+sorted(p for p in OUT.rglob('*') if p.is_file() and p.name!='MANIFEST.json')
assert len(paths)==len(set(paths)) and all(p.is_file() for p in paths)
payloads=[dict(path=str(p.relative_to(WT)),**fd(p)) for p in sorted(paths)]
save(OUT/'MANIFEST.json',dict(schema='r28-01c-manifest/1',slot='R28-01c',branch='b28-01r',parent='93db0679fc06d4c51733b47a640c307128a5631a',hash_convention='raw SHA-256 and bytes; excludes this manifest; no newline conversion or Git filtering',count=len(payloads),payloads=payloads))
print(json.dumps(dict(payloads=len(payloads),manifest=fd(OUT/'MANIFEST.json'),measured_seconds_before_finalize=total)))
