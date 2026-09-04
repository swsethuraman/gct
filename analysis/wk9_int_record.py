import re, json
def cells(txt):
    out=[]
    for line in txt.splitlines():
        if not line.startswith('|'): continue
        f=[c.strip() for c in line.strip().strip('|').split('|')]
        m=re.search(r'\(([\d,\s]+)\)', line)
        if not m: continue
        lam=tuple(int(x) for x in m.group(1).split(','))
        out.append((f,lam))
    return out
def num(s):
    m=re.search(r'-?\d+', s.replace('**',''))
    return int(m.group()) if m else None
rec={}   # (lam,delta) -> dict
def add(lam,delta,a,det,pad,red,src):
    k=(lam,delta)
    if k in rec:
        p=rec[k]
        if (p['a'],p['det'],p['pad'])!=(a,det,pad):
            print("  CONFLICT",k,p,'vs',(a,det,pad,src))
        p['src'].append(src); return
    rec[k]=dict(a=a,det=det,pad=pad,red=red,src=[src])

# s36 ledger: stratum|lam|delta|ell|a|N_S|Stab|n_chi|rows|route|mult_det|mult_pad|D
for f,lam in cells(open('s36_ledger.md').read()):
    if len(f)<13 or f[0] not in ('A','B','A7'): continue
    delta=num(f[2]); ell=num(f[3])
    if ell!=6: continue
    add(lam,delta,num(f[4]),num(f[10]),num(f[11]),None,'s36')
# s36_aone: ell|delta|lam|a|N_S|n_chi|mult_det|mult_pad|mult_red|D
for f,lam in cells(open('s36_aone.md').read()):
    if len(f)<10: continue
    ell=num(f[0])
    if ell!=6: continue
    add(lam,num(f[1]),num(f[3]),num(f[6]),num(f[7]),num(f[8]),'s36a1')
# s41 / s43: delta|lam|a|m_det|N_S|Stab|n_chi|rows|route|mult_det|mult_pad|mult_red|D
for fn,src in (('s41_ledger.md','s41'),('s43_ledger.md','s43')):
    for f,lam in cells(open(fn).read()):
        if len(f)<13 or f[0] in ('delta','---'): continue
        d=num(f[0])
        if d is None or len(lam)!=6: continue
        add(lam,d,num(f[2]),num(f[9]),num(f[10]),num(f[11]),src)
# s45: delta|lam|elig|bal|a|full-E|N_S|Stab|n_chi|rows|nnz|nnz/n|nullity|mult_det|...
for f,lam in cells(open('s45_ledger.md').read()):
    if len(f)<14 or f[2] not in ('yes','onset-only'): continue
    add(lam,num(f[0]),num(f[4]),num(f[13]),None,None,'s45')
json.dump({f"{k[0]}|{k[1]}":v for k,v in rec.items()}, open('rec.json','w'))
print("distinct six-row cells with mult_det:",len(rec))
from collections import Counter
print("by source:",Counter(s for v in rec.values() for s in v['src']))
print("by degree:",Counter(k[1] for k in rec))
print("total ambient units (sum a):",sum(v['a'] for v in rec.values()))
print("cells with mult_det < a:",[(k,v) for k,v in rec.items() if v['det']!=v['a']])
import json, sys
from collections import Counter, defaultdict
sys.path.insert(0,'/root/work')
from verify42 import kostant_mult, h_pad
rec={}
for k,v in json.load(open('rec.json')).items():
    ls,d=k.split('|'); lam=eval(ls); rec[(lam,int(d))]=v
print("=== totals ===")
print("distinct six-row cells with mult_det measured:",len(rec),"  ambient units:",sum(v['a'] for v in rec.values()))
print()
print("=== by degree ===")
for d in (6,7,8,9):
    sub={k:v for k,v in rec.items() if k[1]==d}
    el=[k for k in sub if k[0][0]>=d]; on=[k for k in sub if k[0][0]<d]
    print(f"  delta={d}: {len(sub):3d} cells, {sum(v['a'] for v in sub.values()):4d} units   (eligible {len(el)}, onset-only {len(on)})")
print()
print("=== by balance (lam_1 - lam_6) ===")
bal=Counter(k[0][0]-k[0][5] for k in rec)
for b in sorted(bal): print(f"  balance {b:2d}: {bal[b]:3d} cells")
print()
print("=== pad-side bites (mult_pad < a) ===")
bites=sorted([(k[1],k[0],v) for k,v in rec.items() if v['pad'] is not None and v['pad']<v['a']])
print(f"  {len(bites)} bites\n")
print("  d  lam                     a  det  pad  red   D   h_pad  bound fires?")
for d,lam,v in bites:
    h,_=h_pad(lam,d)
    a=kostant_mult(lam,d,6,4)
    assert a==v['a'],(lam,a,v)
    print(f"  {d}  {str(lam):22s} {v['a']:3d} {v['det']:4d} {v['pad']:4d} {str(v['red']):>4s} {v['pad']-v['det']:+3d}  {h:5d}   {'YES (exact)' if h<v['a'] and h==v['pad'] else ('YES but not exact' if h<v['a'] else 'no')}")
print()
print("=== consistency ===")
print("  cells with mult_det < a:", [k for k,v in rec.items() if v['det']!=v['a']] or "none")
print("  cells with mult_pad > mult_det:", [k for k,v in rec.items() if v['pad'] is not None and v['pad']>v['det']] or "none  (no obstruction anywhere)")
print("  cells with mult_pad != mult_red where both known:",
      [k for k,v in rec.items() if v['pad'] is not None and v['red'] is not None and v['pad']!=v['red']] or "none  (no permanent-specific equation)")
