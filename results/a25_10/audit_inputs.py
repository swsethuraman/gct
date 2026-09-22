"""Administrative committed-blob/manifest audit only; performs no mathematics."""
import hashlib, json, pathlib, subprocess, datetime
ROOT=pathlib.Path('C:/Users/swami/Projects/gct-gpt/work/batch15')
OUT=ROOT/'results/a25_10'
PINS={'a25_01':'aca16c7531483163d392200baced8757fb8746ca','a25_02':'5007de860ba195100adc4f5a6cdebd3d344cadaa','a25_03':'90dd22151511867f5dbb3488c5f3085034c6d7b3','a25_04':'81967ddeb68340f31762bc41d424379cdd57527c','a25_05':'eb53b97cf0904e2d54fdb7d101d83b024822811b','b25_04':'92a7d054369a20854fd51685ee09ecb756344e8d'}
def git(*args): return subprocess.check_output(['git',*args],cwd=ROOT)
def digest(b): return hashlib.sha256(b).hexdigest()
rows=[]
def bind(commit,path,expected=None,repo=None):
    b=git('show',f'{commit}:{path}')
    row={'commit':commit,'path':path,'blob':git('rev-parse',f'{commit}:{path}').decode().strip(),'bytes':len(b),'sha256':digest(b)}
    if expected: row['expected_sha256']=expected; row['hash_match']=digest(b)==expected
    p=pathlib.Path(repo or ROOT)/path
    if p.is_file():
        w=p.read_bytes(); row['working_sha256']=digest(w); row['working_bytes_equal']=w==b; row['line_ending_only_difference']=w!=b and w.replace(b'\r\n',b'\n')==b.replace(b'\r\n',b'\n')
    rows.append(row)
    return b
packets=[]
for slot,commit in PINS.items():
    git('cat-file','-e',commit+'^{commit}')
    repo=ROOT if slot.startswith('a') else ROOT.parent/'batch15_workers/B15-02'
    mpath=f'results/{slot}/MANIFEST.json'; mb=bind(commit,mpath,repo=repo); m=json.loads(mb)
    files=m.get('files',m.get('artifacts',[]))
    if isinstance(files,dict): files=[dict(v,path=k) for k,v in files.items()]
    for f in files:
        path=f.get('path',f.get('relative_path'))
        if not path: raise ValueError((slot,f))
        b=bind(commit,path,f.get('sha256'),repo)
        if 'bytes' in f: rows[-1]['size_match']=len(b)==f['bytes']
    start=m.get('research_head',m.get('starting_head',m.get('baseline_head',m.get('head'))))
    ancestors=None
    if start: ancestors=subprocess.run(['git','merge-base','--is-ancestor',start,commit],cwd=ROOT).returncode==0
    packets.append({'slot':slot,'commit':commit,'manifest_sha256':digest(mb),'manifest_entries':len(files),'starting_head':start,'starting_head_is_ancestor':ancestors,'manifest_keys':list(m)})
    # Verify producer-declared transitive byte bindings, without treating them as read/accepted.
    for s in m.get('source_bindings',m.get('sources',[])):
        if isinstance(s,dict) and s.get('commit') and s.get('path'):
            bind(s['commit'],s['path'],s.get('sha256'),s.get('original_repository'))
# Supplemental report actually read for the same-regime numerical onset premise.
supplement='feed104ea865ed5f76809f6d77455060af01433c'
sm=json.loads(bind(supplement,'results/b23_06/MANIFEST.json'))
for path,expected in sm['outputs'].items():
    bind(supplement,path,expected)
# Audit every already-bound transitive manifest's payload, including original controls/receipts.
transitive=[]
for row in list(rows):
    if row['path'].endswith('/MANIFEST.json') and row['commit'] not in PINS.values():
        key=(row['commit'],row['path'])
        if key in transitive: continue
        transitive.append(key)
        m=json.loads(git('show',f'{key[0]}:{key[1]}'))
        fs=m.get('files',m.get('artifacts',[]))
        if isinstance(fs,dict): fs=[dict(v,path=k) for k,v in fs.items() if isinstance(v,dict)]
        for f in fs:
            if isinstance(f,dict) and f.get('path') and f.get('sha256'):
                p=f['path'].replace('\\','/')
                if p.startswith('C:'): continue
                # Some archival manifests use packet-relative paths.
                exists=subprocess.run(['git','cat-file','-e',f'{key[0]}:{p}'],cwd=ROOT,stderr=subprocess.DEVNULL).returncode==0
                if not exists: p=str(pathlib.PurePosixPath(key[1]).parent/p)
                bind(key[0],p,f['sha256'])
                if 'bytes' in f: rows[-1]['size_match']=rows[-1]['bytes']==f['bytes']
ledger_commit='1f3814ff5d3ede6969dfd0fcf3fb3ba45b22666d'
bind(ledger_commit,'docs/b25_12_ledger.md',repo=ROOT.parent/'batch15_workers/B15-12')
admin=[]
admin_paths=[ROOT.parents[1]/'RUNBOOK.md',ROOT.parents[1]/'Claude_Handover_B15_B18/post_b19_housekeeping_20260917/batch25_launch/v1_20260921T003934Z/astra/A25-10.md',ROOT.parents[1]/'Claude_Handover_B15_B18/post_b19_housekeeping_20260917/launch_prompts/B25_REVIEW_LAUNCH_20260922.md',ROOT.parents[1]/'Claude_Handover_B15_B18/post_b19_housekeeping_20260917/B24_COMMIT_REPORT.md',ROOT.parents[1]/'Claude_Handover_B15_B18/post_b19_housekeeping_20260917/B24_10_COMMIT_REPORT.md',ROOT.parents[1]/'Claude_Handover_B15_B18/post_b19_housekeeping_20260917/batch25_launch/v1_20260921T003934Z/COMPUTE_PROTOCOL.md']
for p in admin_paths:
    b=p.read_bytes(); admin.append({'path':str(p),'bytes':len(b),'sha256':digest(b),'state':'UNCOMMITTED administrative input; no scientific authority'})
external=[]
for p in (OUT/'literature').glob('*.pdf'):
    b=p.read_bytes(); external.append({'path':str(p),'bytes':len(b),'sha256':digest(b),'state':'Downloaded primary input; not a Git packet'})
result={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat().replace('+00:00','Z'),'method':'Administrative raw committed-blob verification; no mathematical computation','packets':packets,'bindings':rows,'failures':[r for r in rows if r.get('hash_match') is False or r.get('size_match') is False]}
result['administrative_inputs']=admin
result['primary_source_files']=external
(OUT/'INPUT_BINDINGS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'packets':packets,'binding_count':len(rows),'failures':result['failures']},indent=2))
