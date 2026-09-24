"""Administrative sealing of a stopped, incomplete delivery. No research computation."""
import datetime, hashlib, json, pathlib
OUT=pathlib.Path(__file__).resolve().parent
def digest(data): return hashlib.sha256(data).hexdigest()
def save(name,obj): (OUT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def bind(name):
    p=(OUT/name).resolve(); assert p.is_relative_to(OUT)
    b=p.read_bytes(); return dict(path=name,bytes=len(b),sha256=digest(b))
for r in json.loads((OUT/'INPUT_BINDINGS.json').read_text()):
    b=(OUT/r['snapshot']).read_bytes()
    assert len(b)==r['bytes'] and digest(b)==r['sha256'],r['snapshot']
r1=json.loads((OUT/'RUN_01_FAILURE.json').read_text())
r2=json.loads((OUT/'RUN_02_RECEIPT.json').read_text())
for r in r2['outputs']:
    assert bind(r['path'])==r,r['path']
assert digest((OUT/'b27_06_price_run02.py').read_bytes())==r2['script_sha256']
save('RESOURCE_RECEIPT.json',dict(
    label='READ: administrative run and ceiling receipt; COMPUTED result limited to pricing arithmetic',
    status='STOPPED_INCOMPLETE_TIME_CEILING_EXCEEDED',
    session_start_utc='2026-09-23T05:15:45Z',mismatch_detected_utc='2026-09-23T08:39:04Z',
    local_clock_confirmation_utc='2026-09-23T08:39:25.4947581Z',
    checkpoint_45_minutes='missed',ceiling_90_minutes='exceeded',
    sealing_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    allowance_attempts=2,allowance_limit=10,rank_replays=0,target_builds=0,target_measurements=0,
    run_01=dict(receipt=r1,receipt_binding=bind('RUN_01_FAILURE.json'),input_binding=bind('RUN_01_INPUTS.json'),
        output_bindings=[bind('RUN_01_INPUTS.json')],
        note='Failed parser version was overwritten; its source hash survives, exact old source unavailable. No mathematical result from this attempt.'),
    run_02=dict(receipt=r2,receipt_binding=bind('RUN_02_RECEIPT.json'),
        preserved_successful_script=bind('b27_06_price_run02.py')),
    resource_limits='Each pricing attempt used a 60-second wall watchdog and 512 MiB Windows process-memory Job Object. No separate measured peak was logged.',
    administrative_work='Read-only Git retrieval, archive/text searches, snapshots, JSON selection, raw hashing, drafting and sealing. These were not mathematical rank runs.',
    installations=0,git_writes=0,subagents=0,other_task_messages=0,
    research_stopped=True,automatic_continuation=False,
    final_preregistration_complete=False,mathematical_review_complete=False))
payloads=[]
for p in sorted(OUT.rglob('*')):
    if not p.is_file(): continue
    assert not p.is_symlink()
    rel=p.relative_to(OUT).as_posix()
    if rel=='MANIFEST.json': continue
    payloads.append(bind(rel))
save('MANIFEST.json',dict(schema='b27-06-manifest/1',slot='B27-06',status='STOPPED_INCOMPLETE',
    hash_convention='SHA-256 of raw payload file bytes; no newline normalization',
    excludes=['MANIFEST.json'],payloads=payloads))
m=json.loads((OUT/'MANIFEST.json').read_text())
assert [r['path'] for r in m['payloads']]==[p.relative_to(OUT).as_posix() for p in sorted(OUT.rglob('*')) if p.is_file() and p.relative_to(OUT).as_posix()!='MANIFEST.json']
for r in m['payloads']: assert bind(r['path'])==r
print(json.dumps(dict(status='sealed partial delivery',payload_count=len(payloads),
    manifest=bind('MANIFEST.json'),verification='All payload byte lengths and raw hashes match. No mathematical completion asserted.'),indent=2))
