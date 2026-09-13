"""Package an already committed Batch 15 worker branch, then verify delivery."""
import argparse
import hashlib
import json
from pathlib import Path
from check_batch15 import check, git, txt

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--repo',default='.');p.add_argument('--branch',required=True)
    p.add_argument('--slot',required=True);p.add_argument('--output',required=True)
    p.add_argument('--model',required=True,help='Actual model that performed the work')
    p.add_argument('--phase',default='research and delivery')
    a=p.parse_args();repo=Path(a.repo).resolve();out=Path(a.output).resolve()
    if not out.is_relative_to(repo):raise ValueError('delivery output must be inside this worker checkout')
    out.mkdir(parents=True,exist_ok=True)
    base=txt(repo,'rev-parse','batch15-base^{commit}')
    pre=check(repo,a.branch,base,a.slot)
    if pre['status']!='PASS':print(json.dumps(pre,indent=2));return 1
    bundle=out/f'b15_{a.slot}.bundle'
    if bundle.exists():raise ValueError('Choose a fresh delivery directory; an existing bundle is preserved')
    git(repo,'bundle','create',str(bundle),base+'..'+a.branch,a.branch)
    raw=bundle.read_bytes()
    man=dict(head=pre['head'],head_tree=pre['head_tree'],base_commit=base,slot=a.slot,branch=a.branch,
             bundle_prerequisites=[base],bundle_bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),
             md5=hashlib.md5(raw).hexdigest(),models=[dict(model=a.model,phase=a.phase)])
    for algorithm in ('sha256','md5'):
        Path(str(bundle)+'.'+algorithm).write_text(man[algorithm]+'  '+bundle.name+'\n',encoding='ascii')
    if len(raw)>=5_000_000:
        man['parts']=[]
        for i,offset in enumerate(range(0,len(raw),4_500_000)):
            data=raw[offset:offset+4_500_000];part=Path(str(bundle)+f'.part{i:02d}')
            part.write_bytes(data);man['parts'].append(dict(name=part.name,bytes=len(data),sha256=hashlib.sha256(data).hexdigest()))
    mf=out/'delivery_manifest.json';mf.write_text(json.dumps(man,indent=2)+'\n',encoding='utf-8')
    post=check(repo,a.branch,base,a.slot,bundle=bundle,manifest=mf)
    (out/'delivery_check.json').write_text(json.dumps(post,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(post,indent=2));return 0 if post['status']=='PASS' else 1

if __name__=='__main__':raise SystemExit(main())
