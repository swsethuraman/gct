"""Hash-verify and copy explicitly delivered 03/07 artifacts to owned immutable intake."""
from pathlib import Path
import hashlib
import json
import sys

WORK=Path(__file__).resolve().parents[1]
PROJECT=WORK.parents[2]
OUT=WORK/'results/b16_12'

def hashed_records(obj):
    if isinstance(obj,dict):
        if 'path' in obj and 'sha256' in obj:
            yield obj
        for v in obj.values():
            yield from hashed_records(v)
    elif isinstance(obj,list):
        for v in obj:
            yield from hashed_records(v)

def main():
    slot=sys.argv[1]
    assert slot in ('03','07')
    worker=PROJECT/f'work/batch15_workers/B15-{slot}'
    delivery=worker/f'delivery/b16_{slot}'
    target=OUT/'intake'/slot
    assert not target.exists(), 'Preserve previous intake; choose explicit version instead'
    raw=(delivery/'MANIFEST.json').read_bytes()
    manifest=json.loads(raw)
    copies=[]
    for row in manifest['files']:
        p=Path(row['path'])
        source=p if p.is_absolute() else delivery/p
        source=source.resolve()
        rel=source.relative_to(worker) if p.is_absolute() else p
        if p.is_absolute() and str(rel).replace('\\','/').startswith(f'delivery/b16_{slot}/'):
            rel=source.relative_to(delivery)
        assert not rel.is_absolute() and '..' not in rel.parts
        data=source.read_bytes()
        digest=hashlib.sha256(data).hexdigest()
        assert digest == row['sha256'] and len(data)==row['bytes'], str(source)
        copies.append((source,rel,data,digest))
    # All source delivery bytes checked before any snapshot is written.
    inputs_path=delivery/f'results/b16_{slot}/input_hashes.json' if slot=='03' else worker/f'results/b16_{slot}/input_hashes.json'
    input_records=[]
    for row in hashed_records(json.loads(inputs_path.read_bytes())):
        source=Path(row['path'])
        data=source.read_bytes()
        digest=hashlib.sha256(data).hexdigest()
        assert digest==row['sha256'], str(source)
        if 'bytes' in row:
            assert len(data)==row['bytes']
        input_records.append({'path':str(source),'sha256':digest,'bytes':len(data)})
    target.mkdir(parents=True)
    (target/'MANIFEST.json').write_bytes(raw)
    records=[]
    for source,rel,data,digest in copies:
        dest=target/rel
        dest.parent.mkdir(parents=True,exist_ok=True)
        dest.write_bytes(data)
        assert hashlib.sha256(dest.read_bytes()).hexdigest()==digest
        assert hashlib.sha256(source.read_bytes()).hexdigest()==digest
        records.append({'source':str(source),'snapshot':str(dest),'relative':str(rel),
                        'sha256':digest,'bytes':len(data)})
    receipt={'slot':slot,'status':'PASS_IMMUTABLE_INTAKE_AND_INPUT_HASHES',
             'manifest_source':str(delivery/'MANIFEST.json'),
             'manifest_sha256':hashlib.sha256(raw).hexdigest(),
             'files':records,'original_inputs':input_records,
             'receiver_will_not_write_intake_or_worker':True}
    (OUT/f'intake_{slot}.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({'slot':slot,'files':len(records),'input_hashes':len(input_records),'status':receipt['status']}))

if __name__=='__main__':
    main()
