"""Administrative provenance receipts and script archival. No mathematical computation."""
import datetime, hashlib, json, pathlib, subprocess
OUT=pathlib.Path(__file__).resolve().parent
BASE=OUT.parent
REPO=pathlib.Path('C:/Users/swami/Projects/gct-gpt/work/batch15')
def sha(b): return hashlib.sha256(b).hexdigest()
def save(name,obj): (OUT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def binding(path):
    b=path.read_bytes()
    return dict(path=str(path),sha256=sha(b),bytes=len(b))
expected={
 'B27_COMMON.md':'891e3ca872bc795b6f943ac89f55112573803f006e0208940dd6cad1f750d6ee',
 'B27-06.md':'3f75ef35f7de580e28210627cc7ef70a63f54129b6240d83f92f8f5e11a0911a',
 'BATCH27_BOARD.md':'b0bc2501aba62d49b91862d821232ac1b9904480057a8dcdb4cbc03fbd86efec'}
controls=[]
for name,want in expected.items():
    b=(BASE/name).read_bytes(); assert sha(b)==want,(name,sha(b))
    target='inputs/control__'+name; (OUT/target).write_bytes(b)
    controls.append(dict(**binding(BASE/name),snapshot=target,verified_unchanged=True))
prev=BASE/'b27_05_out'; b=(prev/'MANIFEST.json').read_bytes()
assert sha(b)=='325c1c817bce32e0f11fbd587bee16ea14ae3111c2ee56129fa7028571558a5c'
(OUT/'inputs/control__B27_05_MANIFEST.json').write_bytes(b)
checked=[]
for r in json.loads(b)['payloads']:
    p=(prev/r['path']).resolve(); assert p.is_relative_to(prev.resolve())
    d=p.read_bytes(); assert len(d)==r['bytes'] and sha(d)==r['sha256'],r['path']
    checked.append(r)
save('B27_05_VERIFICATION.json',dict(label='READ: raw-file integrity check, not adoption of mathematical claims',manifest=binding(prev/'MANIFEST.json'),checked=checked,failures=[]))
save('PREFLIGHT.json',dict(label='READ: administrative session observations and current byte recheck',
    slot='B27-06',start_utc='2026-09-23T05:15:45Z',output_folder=str(OUT),
    initial_observations=dict(output_folder_existed=False,project_root_is_git=False,
        ancestor_AGENTS_found=False,fresh_session_not_B27_05=True,permission_mode='default',
        output_created_only_after_checks=True,branch_setup_gate='overridden by slot-specific preflight and no-Git-write delivery'),
    controls=controls,source_repo=str(REPO),source_commit='7c36a52ddf338eb390a9bcd491cb9c50cf9e2a19',
    git_access='read-only: show, rev-parse, for-each-ref, rev-list, cat-file, log',
    no_installs=True,runtime='bundled Python; Python int/Fraction available; sympy and flint unavailable; numpy and pypdf present',
    mismatches=[],recheck_utc=datetime.datetime.now(datetime.timezone.utc).isoformat()))
current=(OUT/'b27_06_price.py').read_bytes()
want='78812517b5bb285da908c5755184bbf7d647dfcde053a665d924182cdb79b39f'
for base in (current,current.replace(b'\r\n',b'\n')):
    for run in (base,base.replace(b'RUN_02',b'RUN_01')):
        for ending in (b'\r\n',b'\n'):
            candidate=run.replace(b'    if len(v)<14 or not v[7].isdigit(): continue'+ending,b'')
            if sha(candidate)==want:
                (OUT/'b27_06_price_run01_failed.py').write_bytes(candidate)
                print('Recovered exact failed-run source bytes')
if sha(current)=='d09fc7c61233f91a29e954b38ff4ffb98b0fa156a7b11cbc6fd071c7d0fe35ac':
    (OUT/'b27_06_price_run02.py').write_bytes(current)
matches=json.loads((OUT/'RECORD_SEARCH_MATCHES.json').read_text())
bindings=[]
for r in matches:
    d=subprocess.check_output(['git','-C',str(REPO),'cat-file','blob',r['oid']])
    bindings.append(dict(git_blob=r['oid'],path=r['path'],member=r['member'],bytes=len(d),raw_blob_sha256=sha(d),searched_content_sha256=r['searched_content_sha256']))
save('SEARCH_BLOB_BINDINGS.json',bindings)
print('Preflight controls and all',len(checked),'B27-05 payloads verified; bound',len(bindings),'search matches.')
