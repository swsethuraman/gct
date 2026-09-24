"""Administrative preflight for the user's explicit continuation. No rank work."""
import datetime, hashlib, json, pathlib, subprocess
OUT=pathlib.Path(__file__).resolve().parent
REPO=pathlib.Path('C:/Users/swami/Projects/gct-gpt/work/batch15')
def sha(b): return hashlib.sha256(b).hexdigest()
def save(p,x): (OUT/p).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
raw=(OUT/'MANIFEST.json').read_bytes()
assert sha(raw)=='64b132bd0b0f3a715382f3dc1556868bd6d6b845c03bd049ab163865d9757d2b'
old=json.loads(raw)
for r in old['payloads']:
    p=(OUT/r['path']).resolve(); assert p.is_relative_to(OUT)
    b=p.read_bytes(); assert len(b)==r['bytes'] and sha(b)==r['sha256'],r['path']
pre=json.loads((OUT/'PREFLIGHT.json').read_text())
for r in pre['controls']:
    b=pathlib.Path(r['path']).read_bytes()
    assert len(b)==r['bytes'] and sha(b)==r['sha256'],r['path']
for r in json.loads((OUT/'INPUT_BINDINGS.json').read_text()):
    b=subprocess.check_output(['git','-C',str(REPO),'show',r['commit']+':'+r['path']])
    assert len(b)==r['bytes'] and sha(b)==r['sha256'],r['path']
refs=subprocess.check_output(['git','-C',str(REPO),'for-each-ref','--format=%(refname) %(objectname)'])
same=refs==(OUT/'GIT_REFS.txt').read_bytes()
(OUT/'RESUME_GIT_REFS.txt').write_bytes(refs)
arc=OUT/'interrupted_delivery'; arc.mkdir(exist_ok=False)
archived=[]
for name in ['MANIFEST.json','REPORT.md','RESOURCE_RECEIPT.json','STOP_REPORT.md']:
    b=(OUT/name).read_bytes(); (arc/name).write_bytes(b)
    archived.append(dict(path='interrupted_delivery/'+name,sha256=sha(b),bytes=len(b)))
save('RESUME_PREFLIGHT.json',dict(label='READ: verified continuation preflight',
    start_utc='2026-09-23T10:51:42Z',checkpoint_due_utc='2026-09-23T11:36:42Z',ceiling_utc='2026-09-23T12:21:42Z',
    user_authorization='The internet connection probably dropped. COntinue?',
    interpretation='Continue this same task in its existing output directory; fresh 90-minute wall envelope; prior two allowance attempts still count toward ten.',
    prior_manifest_sha256=sha(raw),verified_prior_payloads=len(old['payloads']),
    controls_unchanged=True,committed_input_snapshots_match_git=True,git_refs_unchanged=same,
    archived=archived,connection_drop_cause='unverified; previous stop history preserved',
    measurements_authorized=False,git_writes_authorized=False,check_utc=datetime.datetime.now(datetime.timezone.utc).isoformat()))
print(json.dumps(dict(verified_payloads=len(old['payloads']),controls='unchanged',input_snapshots='match committed blobs',git_refs_unchanged=same,archive='interrupted_delivery'),indent=2))
