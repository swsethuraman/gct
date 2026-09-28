#!/usr/bin/env python3
"""R28-01c raw bindings and exactly one preflight-only launcher invocation."""
import difflib
import hashlib
import json
import os
from pathlib import Path
import resource
import subprocess
import time

ROOT=Path('/mnt/c/Users/swami/Projects/gct-gpt')
WT=ROOT/'work/batch28/b28-01r'
OUT=WT/'results/b28_01rc'
HOST=Path.home()/'b28_01'
TIP='0f7af8b11e55da20cd135c73d04554a0360dd97f'
PARENT='5a3174cd3a1ec96b05b92a8bcb73fbee58c0544b'
REVIEW='93db0679fc06d4c51733b47a640c307128a5631a'
GIT=['git','--git-dir='+str(ROOT/'work/batch15/.git')]
def git(*args): return subprocess.check_output(GIT+list(args))
def blob(ref,path): return git('show',ref+':'+path)
def digest(b): return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def fd(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1048576),b''): h.update(b)
    return dict(bytes=p.stat().st_size,sha256=h.hexdigest())
def save(p,obj): p.write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')
def main():
    start=time.monotonic(); OUT.mkdir(exist_ok=False)
    rec=dict(command='timeout 60 bash -c "ulimit -v 500000; exec python3 analysis/b28_01rc_bind.py"',script=fd(Path(__file__)),timeout_seconds=60,address_limit_kib=500000,input_commit=TIP)
    try:
        parent=git('show','-s','--format=%P',TIP).decode().strip(); assert parent==PARENT
        changes=git('diff-tree','--no-commit-id','--name-status','-r',TIP).decode().splitlines()
        paths=[]
        for row in changes:
            status,p=row.split('\t'); assert status=='A'
            assert p.startswith(('analysis/b28_01d_','results/b28_01d/')) or p=='docs/b28_01d_report.md'
            paths.append(p)
        mp='results/b28_01d/MANIFEST.json'; mb=blob(TIP,mp)
        assert digest(mb)['sha256']=='2129631d0b9189c4bd21a6ebafb8b148ff49dfb94829d9ad6adda9eaf66d3d90'
        rec['input_manifest']=digest(mb); m=json.loads(mb); checked=[]
        assert len(m['files'])==m['count']==63
        for e in m['files']:
            got=digest(blob(TIP,e['path']))
            assert got=={k:e[k] for k in ('bytes','sha256')},e['path']
            checked.append(dict(path=e['path'],**got))
        assert set(paths)=={e['path'] for e in checked}|{mp}
        oldhash={n:h for h,n in (s.split() for s in blob(PARENT,'results/b28_01c/frozen_c_hashes.txt').decode().splitlines())}
        frozen=[]
        for line in blob(TIP,'results/b28_01d/frozen_d_hashes.txt').decode().splitlines():
            h,n=line.split(); got=fd(HOST/'frozen_d'/n); assert got['sha256']==h,n
            unchanged=n in oldhash
            if unchanged:
                assert h==oldhash[n] and got==fd(HOST/'frozen_c'/n),n
            if not n.endswith('.so'):
                source='results/b28_01c/'+n if n=='gate_rates_c.json' else 'analysis/'+n
                assert got==digest(blob(TIP,source)),source
                if unchanged: assert blob(TIP,source)==blob(PARENT,source)
            frozen.append(dict(name=n,unchanged_from_c=unchanged,**got))
        assert len(frozen)==9 and sum(e['unchanged_from_c'] for e in frozen)==6
        oldfrozen=[]
        for n,h in oldhash.items():
            got=fd(HOST/'frozen_c'/n); assert got['sha256']==h,n
            oldfrozen.append(dict(name=n,**got))
        review_manifest=digest(blob(REVIEW,'results/b28_01rb/MANIFEST.json'))
        assert review_manifest['sha256']=='5068e6cdabfb0d578bb5c1c5f3d02ba36f15542e5c3bcfba63cae5bd1266d4b4'
        diffs=[]
        for kind,ext in [('supervise','py'),('cellA','sh')]:
            a='analysis/b28_01c_'+kind+'.'+ext;b='analysis/b28_01d_'+kind+'.'+ext
            old,new=blob(PARENT,a),blob(TIP,b)
            d=''.join(difflib.unified_diff(old.decode().splitlines(True),new.decode().splitlines(True),fromfile=PARENT+':'+a,tofile=TIP+':'+b))
            target=OUT/(kind+'.diff');target.write_text(d)
            diffs.append(dict(old=dict(commit=PARENT,path=a,**digest(old)),new=dict(commit=TIP,path=b,**digest(new)),diff=dict(path=target.name,**fd(target))))
        launch=ROOT/'Claude_Handover_B15_B18/post_b19_housekeeping_20260917/batch28_launch'
        expected={'B28_COMMON.md':'06799a9e404fc45a0944f7fcae88d8dd5511f7721f704ebe69872dd3061c87b9','R28-01c.md':'947405cefedc81b425263c356d318c506a1d5b2b3e4ee72e4ac1f1c85b2ddbdc','BATCH28_BOARD.md':'34b0852845c0e4caca809e4f2bdfb10e1b36ffa492f61380dfd3678de7809e81'}
        briefs={n:fd(launch/n) for n in expected}
        assert all(briefs[n]['sha256']==h for n,h in expected.items())
        result=dict(schema='r28-01c-bindings/1',evidence='COMPUTED raw SHA-256 and byte comparisons; committed inputs READ separately',hash_convention='raw file/blob bytes without newline conversion or Git filters',tip=TIP,parent=parent,changed_paths=paths,manifest=digest(mb),payloads=checked,frozen_d=frozen,frozen_c=oldfrozen,review_input=dict(commit=REVIEW,path='docs/b28_01rb_review.md',**digest(blob(REVIEW,'docs/b28_01rb_review.md'))),review_manifest=review_manifest,briefs=briefs,diffs=diffs,preflight=dict(branch='b28-01r',head=REVIEW,clean=True,output_paths_absent=True,producer_pushed=True,user_authorization='Yes authorized, current turn'),all_match=True)
        save(OUT/'BINDINGS.json',result)
        argv=['/bin/bash',str(HOST/'frozen_d/b28_01d_cellA.sh'),'--preflight-only']
        pt=time.monotonic()
        p=subprocess.run(argv,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1'))
        rec['launcher_preflight']=dict(argv=argv,input=fd(Path(argv[1])),rc=p.returncode,wall_seconds=time.monotonic()-pt,stdout=p.stdout.decode(),stdout_sha256=hashlib.sha256(p.stdout).hexdigest())
        assert p.returncode==0,p.stdout.decode()
        rec['rc']=0
        print(json.dumps(dict(payloads=63,frozen_d=9,unchanged=6,all_bindings_match=True,launcher_preflight='PASS')))
    except Exception as e:
        rec['rc']=1;rec['error']=repr(e);raise
    finally:
        rec.update(wall_seconds=time.monotonic()-start,maxrss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,child_maxrss_kib=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,outputs=[dict(path=p.name,**fd(p)) for p in sorted(OUT.iterdir()) if p.is_file()])
        save(OUT/'binding_receipt.json',rec)
if __name__=='__main__': main()
