import os, pathlib
ROOT = pathlib.Path(os.environ.get('GCT_ROOT', pathlib.Path(__file__).resolve().parents[2]))
WORK = pathlib.Path(os.environ.get('GCT_WORK', ROOT / 'results' / 'integrate' / 'b14_11_replay'))
WORK.mkdir(parents=True, exist_ok=True)
import json, sys, time
sys.path.insert(0, str(ROOT / 'analysis'))
from wk9_s57_lib import a_weyl_mod
rows=[json.loads(l) for l in open(str(WORK / 'census_all.jsonl'))]
rows.sort(key=lambda r:(r['delta'],len(r['lam'])))
cache={}; out=[]; bad=[]; t=time.time()
for i,r in enumerate(rows):
    a,nt,nd=a_weyl_mod(tuple(r['lam']), r['delta'], n=4, cache=cache)
    rec={'delta':r['delta'],'lam':r['lam'],'a_house':a,'a_theirs':r['a']}
    out.append(rec)
    if a!=r['a']: bad.append(rec)
    if i%250==0: print(i, len(rows), 'mismatch',len(bad), '%.1fs'%(time.time()-t), flush=True)
json.dump({'n':len(out),'mismatches':bad,'rows':out}, open(str(WORK / 'a_recount.json'),'w'))
print('DONE rows',len(out),'mismatches',len(bad),'elapsed %.1f'%(time.time()-t))
print('positive',sum(1 for r in out if r['a_house']>0),'a1',sum(1 for r in out if r['a_house']==1))
