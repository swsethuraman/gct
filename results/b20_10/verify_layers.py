import json, subprocess, hashlib, re, sys, os
HK=r'C:\Users\swami\Projects\gct-gpt\Claude_Handover_B15_B18\post_b19_housekeeping_20260917'
REPO=r'C:\Users\swami\Projects\gct-gpt\work\batch15_workers\B15-10'
def git(*a):
    p=subprocess.run(['git','-C',REPO]+list(a),capture_output=True)
    return p.returncode,p.stdout
def blob(commit,path):
    rc,out=git('show',f'{commit}:{path}')
    return None if rc else out
r=json.load(open(os.path.join(HK,'COMMIT_RECEIPTS.json')))
out={'layer0':[],'layer1':{},'layer2':[],'layer3':[],'refs':[]}
# Layer 0
tot=0; ok=0; bad=[]
for c in r['commits']:
    cm=c['commit']
    rc,p=git('rev-parse',f'{cm}^{{commit}}'); exists=(rc==0)
    rc,par=git('log','-1','--format=%P %T %s',cm)
    par=par.decode().strip().split(' ',2)
    rc,br=git('rev-parse',c['branch'])
    rec={'branch':c['branch'],'commit':cm,'exists':exists,'parent_ok':par[0]==c['parent'],'tree_ok':par[1]==c['tree'],
         'branch_tip_is_commit':br.decode().strip()==cm,'subject_ok':par[2]==c['subject'] if len(par)>2 else None}
    n=0;g=0
    for path,h in c.get('committed_sha256',{}).items():
        b=blob(cm,path); n+=1; tot+=1
        if b is not None and hashlib.sha256(b).hexdigest()==h: g+=1; ok+=1
        else: bad.append((c['branch'],path,h, None if b is None else hashlib.sha256(b).hexdigest()))
    rec['paths']=f'{g}/{n}'; rec['count_matches_receipt']=(n==c['staged_path_count'])
    out['layer0'].append(rec)
out['layer0_total']=f'{ok}/{tot}'; out['layer0_bad']=bad
# Layer 1: manifests at 82633a60
ARCH='82633a60893236fab4fbc317df416e1b8a349005'
rc,ls=git('ls-tree','-r','--name-only',ARCH,'docs/post_b19_20260917')
files=ls.decode().split('\n')
blobhash={}
for f in files:
    if not f: continue
    b=blob(ARCH,f); blobhash[hashlib.sha256(b).hexdigest()]=f
out['archive_file_count']=len(blobhash)
mans=[f for f in files if f.endswith('MANIFEST.json')]
hexre=re.compile(r'\b[0-9a-f]{64}\b')
tot1=0; res1=0; unres={}
for m in mans:
    txt=blob(ARCH,m).decode('utf-8','replace')
    hs=hexre.findall(txt)
    # dedupe? brief says 565 in-tree hash values; count all occurrences and unique separately
    u=set(hs); rr=[h for h in u if h in blobhash]
    tot1+=len(u); res1+=len(rr)
    miss=[h for h in u if h not in blobhash]
    out['layer1'][m.replace('docs/post_b19_20260917/','')]={'unique_hashes':len(u),'occurrences':len(hs),'resolved':len(rr),'unresolved':miss, 'manifest_blob_sha256':hashlib.sha256(blob(ARCH,m)).hexdigest()}
out['layer1_totals']={'unique':tot1,'resolved':res1}
# Layer 2 pins: find in all archive text where worker file hashes appear
workers={'B15-01':'6b16151328d38dc0ce39bcfab51e83459a035d79','B15-02':'75ddb900a0b47b911c53f941885bac73b358eacb','B15-05':'e3aa25b42399595e0959101e098d20d6bf069f13','B15-12':'f008ac39d5a58c9afe61504108e537ac5c898e7a','B15-06':'0a236381df697b07fa35e073fab34435d33e5f4a','B15-11':'b9dcbbc18a13dc6affe0825fdbed0c5b93f52da9','B15-10':'5764e7ffc03439b7f34b912ff9ff984554c0884e'}
pins=[('B15-01','docs/b19_01_report.md'),('B15-02','docs/b19_02_report.md'),('B15-02','docs/b19_02_review.md'),('B15-02','analysis/b19_02_rect.py'),('B15-02','results/b19_02/rect_4_4_4_4_4.json'),('B15-05','docs/b18_05_report.md'),('B15-12','analysis/b18_12_ambient_table.py'),('B15-12','analysis/b18_12_fibre_check.py'),('B15-12','docs/b18_12_coefficient_algebra.md'),('B15-12','results/b18_12/ambient_table.out'),('B15-12','results/b18_12/fibre_check.out')]
alltext=''
for f in files:
    if f.endswith(('.json','.md','.txt','.py','.out')):
        b=blob(ARCH,f)
        if b: alltext+=b.decode('utf-8','replace')
for w,p in pins:
    b=blob(workers[w],p); h=hashlib.sha256(b).hexdigest() if b else None
    out['layer2'].append({'worker':w,'path':p,'committed_sha256':h,'pinned_in_archive':(h in alltext) if h else False})
# Layer 3 listed
l3=[('B15-01','docs/b19_01_report.md','aa136106'),('B15-01','docs/b19_01_review.md','33b154e6'),('B15-02','docs/b19_02_report.md','52a9e474'),('B15-02','docs/b19_02_review.md','e28bcc93'),('B15-05','docs/b19_05_intake.md','dc074191'),('B15-06','docs/b18_06_sweep_review.md','8a321a18'),('B15-11','docs/b19_11_report.md','30942342'),('B15-11','docs/b19_11_review.md','c9604f9e'),('B15-11','docs/delivery_contract.md','ee256f38'),('B15-11','results/b19_11/MANIFEST.json','63f002d4'),('B15-12','docs/b19_12_ledger.md','129a7c2c'),('B15-12','docs/b18_12_ledger.md','575b1cae'),('B15-10','docs/b18_10_integrator_review.md',None)]
for w,p,pre in l3:
    b=blob(workers[w],p); h=hashlib.sha256(b).hexdigest() if b else None
    out['layer3'].append({'worker':w,'path':p,'sha256':h,'prefix_expected':pre,'ok':(h.startswith(pre) if (h and pre) else None)})
# refs
for k,v in r['final_verification']['refs_unchanged_by_this_session'].items():
    rc,cur=git('rev-parse',k); cur=cur.decode().strip()
    out['refs'].append({'ref':k,'receipt':v,'now':cur,'same':cur==v})
for k,v in r['final_verification']['checkouts'].items():
    rc,cur=git('rev-parse',v['branch']); out['refs'].append({'ref':v['branch'],'receipt':v['head'],'now':cur.decode().strip(),'same':cur.decode().strip()==v['head']})
json.dump(out,open(sys.argv[1],'w'),indent=1)
print('layer0',out['layer0_total'],'bad',len(bad))
for x in out['layer0']: print(x)
print('layer1',out['layer1_totals'],'archive files',out['archive_file_count'])
for k,v in out['layer1'].items(): print(k,v['unique_hashes'],v['occurrences'],v['resolved'],v['unresolved'][:3])
for x in out['layer2']: print(x)
for x in out['layer3']: print(x)
for x in out['refs']: print(x)
