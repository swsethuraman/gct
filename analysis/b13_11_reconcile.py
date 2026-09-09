"""Produce the compact reconciled record, certificate availability and inventory."""
import ast
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys
import time
from b13_11_ledger import (ROOT,PRIMES,LMR,N3,cell_key,cell_id,partition,json_file,
                           json_rows,load_record,stable_record,quartic_closed_tails)

OUT=ROOT/'results/b13_11'


def save(name,obj):
    OUT.mkdir(exist_ok=True)
    (OUT/name).write_text(json.dumps(obj,indent=1,sort_keys=True)+'\n',encoding='utf-8')


def parts(name,rows,cap=4_500_000):
    data=bytearray(); paths=[]
    for row in rows:
        line=(json.dumps(row,separators=(',',':'),sort_keys=True)+'\n').encode()
        if len(line)>cap: raise ValueError('single record exceeds part cap')
        if len(data)+len(line)>cap and data:
            p=OUT/f'{name}.part{len(paths):02}.jsonl'; p.write_bytes(data); paths.append(p.name); data=bytearray()
        data.extend(line)
    if data:
        p=OUT/f'{name}.part{len(paths):02}.jsonl'; p.write_bytes(data); paths.append(p.name)
    return paths


def main():
    start=time.monotonic(); bank=load_record(); OUT.mkdir(exist_ok=True)
    rows=[bank.cells[k] for k in sorted(bank.cells)]
    record_parts=parts('ledger',rows)
    cert_manifest=json_file('results/s79_cert_manifest.json')
    certs=[]
    for r in cert_manifest['files']:
        p=ROOT/r['path']; present=p.is_file()
        match=None
        if present: match=hashlib.md5(p.read_bytes()).hexdigest()==r['md5']
        certs.append(dict(path=r['path'],expected_bytes=r['bytes'],expected_md5=r['md5'],
                          actual_bytes=p.stat().st_size if present else None,
                          actual_md5=hashlib.md5(p.read_bytes()).hexdigest() if present else None,
                          declared_shipped=r['shipped'],present=present,md5_matches=match,
                          verification_flag=('unshipped_entry_has_different_local_version' if present and not match and not r['shipped'] else
                              'missing_certificate' if not present else None)))
    cert_parts=parts('s79_certificate_availability',certs)
    summary=dict(board_numbering='batch13',session_id='B13-11',
                 cells=len(rows),by_n=dict(Counter(r['n'] for r in rows)),
                 observations=sum(len(r['observations']) for r in rows),
                 source_counts=dict(bank.source_counts),conflicts=bank.conflicts,
                 record_parts=record_parts,certificate_parts=cert_parts,
                 s79_certificates=dict(total=len(certs),present=sum(c['present'] for c in certs),
                      missing=sum(not c['present'] for c in certs),
                      digest_mismatches=[c['path'] for c in certs if c['md5_matches'] is False]),
                 elapsed_seconds=round(time.monotonic()-start,3))
    summary['quartic_full_rank_cells']=sum(r['n']==4 and r['sides'].get('det',{}).get('full_rank',False) for r in rows)
    summary['quartic_rank_cells']=sum(r['n']==4 and 'det' in r['sides'] for r in rows)
    summary['s79_deficient_red_records']=sum(r['mult_red']<r['a'] for _,r in json_rows('results/s79_cells.jsonl'))
    save('reconciliation.json',summary)
    save('input_hashes.json',dict(board_numbering='batch13',session_id='B13-11',files=[
        dict(path=p,sha256=hashlib.sha256((ROOT/p).read_bytes()).hexdigest()) for p in sorted(bank.inputs)]))
    print(json.dumps(summary),flush=True)
    if bank.conflicts or any(c['declared_shipped'] and (not c['present'] or not c['md5_matches']) for c in certs): return 1
    return 0


if __name__=='__main__': sys.exit(main())
