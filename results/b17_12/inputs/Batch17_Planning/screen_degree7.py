"""Bounded degree-seven slice; reuses reviewed Astra exact character routines."""
import importlib.util
import json
from pathlib import Path
from time import perf_counter

ROOT = Path(__file__).resolve().parent
src = ROOT/'symmetry_dream/astra/toy_character_screen.py'
spec = importlib.util.spec_from_file_location('toy', src)
t = importlib.util.module_from_spec(spec)
spec.loader.exec_module(t)
t.controls()
start = perf_counter()
rows=[]
considered=0
for w in range(11):
    for nu in t.parts(w):
        if not 2 <= len(nu) <= 6 or 28-w < nu[0]:
            continue
        lam=(28-w,)+nu
        considered+=1
        a=t.pleth_mult(7,4,lam)
        if a<2:
            continue
        # Only interlacing core shapes can contribute; no whole cubic census.
        core=[mu for mu in t.parts(21) if len(mu)<=7 and t.horizontal(lam,mu)]
        raw=sum(t.pleth_mult(7,3,mu) for mu in core)
        g,tr,s,minus=t.kron(lam,(7,)*4)
        U=min(a,raw)
        B=min(a,s)
        rows.append(dict(weight=lam,a=a,U=U,source_raw=raw,g=g,t=tr,s=s,B=B,
                         headroom=U-B,required_minor=B+1))
        t.char.cache_clear()
survivors=sorted((r for r in rows if 1<=r['B']<r['U']),key=lambda r:(r['B']+1,-r['headroom'],r['weight']))
result=dict(status='COMPLETE',scope='d=7, tail size <=10, tail length 2..6, ambient>=2',
            considered=considered,eligible=len(rows),rows=rows,survivors=survivors,
            seconds=perf_counter()-start,controls='Inherited exact S6 orthogonality and S4 transpose controls passed',
            limitation='No closure-rank claim. Failure excludes this symmetry-only certificate, not actual gaps.')
(ROOT/'degree7_screen.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='rows'}),flush=True)
