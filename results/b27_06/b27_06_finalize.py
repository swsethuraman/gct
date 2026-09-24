"""Administrative final checks and sealing. Never runs a target or pricing experiment."""
import datetime, hashlib, json, pathlib, re, subprocess
OUT=pathlib.Path(__file__).resolve().parent
REPO=pathlib.Path('C:/Users/swami/Projects/gct-gpt/work/batch15')
def sha(data): return hashlib.sha256(data).hexdigest()
def read(name): return json.loads((OUT/name).read_bytes())
def save(name,obj): (OUT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def bind(name):
    p=(OUT/name).resolve(); assert p.is_relative_to(OUT)
    b=p.read_bytes(); return dict(path=name,bytes=len(b),sha256=sha(b))
def verify(row): assert bind(row['path'])==row,row['path']
pre=read('PREFLIGHT.json'); resume=read('RESUME_PREFLIGHT.json')
for r in pre['controls']:
    b=pathlib.Path(r['path']).read_bytes()
    assert len(b)==r['bytes'] and sha(b)==r['sha256'],r['path']
inputs=read('INPUT_BINDINGS.json')
for r in inputs:
    b=(OUT/r['snapshot']).read_bytes()
    assert len(b)==r['bytes'] and sha(b)==r['sha256'],r['snapshot']
current_refs=subprocess.check_output(['git','-C',str(REPO),'for-each-ref','--format=%(refname) %(objectname)'])
assert current_refs==(OUT/'GIT_REFS.txt').read_bytes(),'Record universe changed: stop and update record search.'
for r in resume['archived']: verify(r)
assert sha((OUT/'interrupted_delivery/MANIFEST.json').read_bytes())==resume['prior_manifest_sha256']
old_manifest=read('interrupted_delivery/MANIFEST.json')
for r in old_manifest['payloads']:
    archived=OUT/'interrupted_delivery'/r['path']
    b=(archived if archived.is_file() else OUT/r['path']).read_bytes()
    assert len(b)==r['bytes'] and sha(b)==r['sha256'],('old payload changed without archive',r['path'])
r1=read('RUN_01_FAILURE.json'); r2=read('RUN_02_RECEIPT.json'); r3=read('RUN_03_RECEIPT.json')
for r in r2['outputs']: verify(r)
assert sha((OUT/'b27_06_price_run02.py').read_bytes())==r2['script_sha256']
for r in read('RUN_02_INPUTS.json'): verify(r)
verify(r3['script']); verify(r3['inputs'])
for r in r3['outputs']: verify(r)
for r in read('RUN_03_INPUTS.json'): verify(r)
assert r2['wall_seconds']<60 and r3['wall_seconds']<60
assert r3['peak_working_set_bytes']<500000000
docs=['README.md','REPORT.md','PREREGISTRATION.md','SEARCH_AUDIT.md','VERIFICATION.md']
links=[]; citations=[]
known={(r['commit'],r['path']) for r in inputs}
C='7c36a52ddf338eb390a9bcd491cb9c50cf9e2a19'
for name in docs:
    text=(OUT/name).read_text(encoding='utf-8')
    for dest in re.findall(r'\]\(([^)]+)\)',text):
        if '://' in dest or dest.startswith('#'): continue
        rel=dest.split('#')[0]
        p=(OUT/rel).resolve(); assert p.is_relative_to(OUT) and p.exists(),(name,dest)
        links.append(dict(document=name,target=rel))
    for path in re.findall(r'C:((?:docs|analysis|results)/[A-Za-z0-9_./-]+)',text):
        assert (C,path) in known,(name,path)
        citations.append(dict(document=name,commit=C,path=path))
    assert 'No five-row determinant equation is known to be nonzero on padding.' in text or name in ['SEARCH_AUDIT.md','VERIFICATION.md']
now=datetime.datetime.now(datetime.timezone.utc)
started=datetime.datetime.fromisoformat(resume['start_utc'].replace('Z','+00:00'))
elapsed=(now-started).total_seconds()
assert elapsed<45*60,'Checkpoint is due: do not silently finalize with an obsolete timing statement.'
save('FINAL_VALIDATION.json',dict(label='READ: final integrity and document checks, not a target rank certificate',
    utc=now.isoformat(),controls_unchanged=True,input_snapshots_verified=len(inputs),
    git_refs_unchanged=True,prior_payloads_still_recoverable=len(old_manifest['payloads']),
    receipt_hashes_verified=True,current_document_links=links,explicit_C_citations=citations,
    exact_pricing_check_receipt=bind('RUN_03_RECEIPT.json'),
    mathematical_review='Source/certificate/cost audit documented in VERIFICATION.md; no target measurement.',
    resumed_segment_seconds=elapsed,checkpoint_45_minutes='not due; completion before checkpoint',
    known_provenance_limitation='Original failed parser source overwritten; hash retained; no result was used from it.'))
save('RESOURCE_RECEIPT.json',dict(label='READ: all allowance attempts and administrative completion receipt',
    status='COMPLETE_PRICED_PREREGISTRATION',registered_outcome=2,
    initial_segment=dict(start_utc=pre['start_utc'],stop_detection_utc='2026-09-23T08:39:04Z',
        checkpoint_45_minutes='missed',ceiling_90_minutes='exceeded',
        archived_receipt=bind('interrupted_delivery/RESOURCE_RECEIPT.json'),
        archived_manifest=bind('interrupted_delivery/MANIFEST.json')),
    resumed_segment=dict(start_utc=resume['start_utc'],finished_utc=now.isoformat(),wall_seconds=elapsed,
        authorization=resume['user_authorization'],checkpoint_45_minutes='not due; completed',ceiling_90_minutes='within ceiling'),
    allowance_attempts_total=3,allowance_limit=10,allowance_was_not_reset=True,
    runs=[dict(number=1,receipt=bind('RUN_01_FAILURE.json'),command=r1['command'],script_sha256=r1['script_sha256'],
            input_index=bind('RUN_01_INPUTS.json'),outputs=[bind('RUN_01_INPUTS.json')],wall_seconds=r1['wall_seconds'],status='parser failure; no mathematical result',
            limitation='Exact failed source version was overwritten; only its hash survives.'),
          dict(number=2,receipt=bind('RUN_02_RECEIPT.json'),details=r2,preserved_script=bind('b27_06_price_run02.py'),status='successful exact pricing arithmetic'),
          dict(number=3,receipt=bind('RUN_03_RECEIPT.json'),details=r3,status='successful exact formula audit and disclosed corrections')],
    rank_replays=0,target_builds=0,target_measurements=0,
    original_memory_receipt_limit='Runs 1 and 2 used a 512 MiB process-memory cap; no measured peak was logged. Run 3 used 500,000,000 bytes and logged its peak.',
    administrative_work='Read-only Git retrieval, archive/text searches, snapshots, exact-byte hashing, record selection, document authoring and sealing; no rank experiment.',
    installations=0,git_writes=0,subagents=0,other_task_messages=0,publication=False,automatic_continuation=False,
    final_preregistration_complete=True,mathematical_review_complete=True,validation=bind('FINAL_VALIDATION.json')))
payloads=[]
for p in sorted(OUT.rglob('*')):
    if not p.is_file(): continue
    assert not p.is_symlink()
    rel=p.relative_to(OUT).as_posix()
    if rel=='MANIFEST.json': continue
    payloads.append(bind(rel))
save('MANIFEST.json',dict(schema='b27-06-manifest/2',slot='B27-06',status='COMPLETE_PRICED_PREREGISTRATION',
    registered_outcome=2,hash_convention='SHA-256 of raw payload file bytes; no newline normalization',
    excludes=['MANIFEST.json'],payloads=payloads))
manifest=read('MANIFEST.json')
actual={p.relative_to(OUT).as_posix() for p in OUT.rglob('*') if p.is_file() and p.relative_to(OUT).as_posix()!='MANIFEST.json'}
assert {r['path'] for r in manifest['payloads']}==actual
for r in manifest['payloads']: verify(r)
print(json.dumps(dict(status=manifest['status'],registered_outcome=2,payload_count=len(payloads),
    manifest=bind('MANIFEST.json'),resumed_segment_seconds=elapsed,verification='PASS: all raw payload hashes and sizes; complete coverage; committed inputs; receipts; current document links'),indent=2))
