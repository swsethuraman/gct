#!/usr/bin/env python3
"""Assemble the resource receipt and raw payload manifest after the review."""
import hashlib
import json
from pathlib import Path
import resource
import time

WT=Path(__file__).resolve().parents[1]
OUT=WT/'results/b28_01rb'
def fd(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1048576),b''): h.update(b)
    return dict(bytes=p.stat().st_size,sha256=h.hexdigest())
def save(p,o): p.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
start=time.monotonic()
receipts=['binding_receipt.json','preflight_receipt.json','replay_receipt.json','audit_attempt1_receipt.json','audit_receipt.json','supervisor_controls_receipt.json']
items=[]
total=0
for name in receipts:
    r=json.loads((OUT/name).read_text())
    total+=r['wall_seconds']
    items.append(dict(path='results/b28_01rb/'+name,**fd(OUT/name),wall_seconds=r['wall_seconds'],command=r['command']))
assert total<3600
save(OUT/'RESOURCE_RECEIPT.json',dict(schema='r28-01b-resource-receipt/1',runs=items,run_count_including_finalize=7,execution='sequential WSL runs only; no Windows mathematical runs',aggregate_measured_wall_seconds_before_finalize=total,review_compute_cap_seconds=3600,replay_enforcement='One MemoryMax=8000000000 / MemorySwapMax=0 scope, outer timeout 3500 s; controls and exactly one cal2 replay',other_runs='60 s / 512 MB or smaller, including the supplemental supervisor controls',installs=0,cellA_builds=0,cellB_builds=0,finalize=dict(command='timeout 60 bash -c "ulimit -v 500000; exec python3 analysis/b28_01rb_finalize.py"',script=fd(Path(__file__)),wall_seconds_before_manifest=time.monotonic()-start,maxrss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)))
paths=[WT/'docs/b28_01rb_review.md']+sorted((WT/'analysis').glob('b28_01rb_*'))+sorted(p for p in OUT.rglob('*') if p.is_file() and p.name!='MANIFEST.json')
assert all(p.is_file() for p in paths)
assert len(paths)==len(set(paths))
payloads=[dict(path=str(p.relative_to(WT)),**fd(p)) for p in sorted(paths)]
save(OUT/'MANIFEST.json',dict(schema='r28-01b-manifest/1',slot='R28-01b',branch='b28-01r',parent='8a86fec17b72b565baaef7f9e29709d1ced35168',hash_convention='raw SHA-256 and bytes; no conversion or filtering; excludes this manifest',payloads=payloads,count=len(payloads)))
print(json.dumps(dict(payloads=len(payloads),manifest=fd(OUT/'MANIFEST.json'),aggregate_wall_seconds=total)))
