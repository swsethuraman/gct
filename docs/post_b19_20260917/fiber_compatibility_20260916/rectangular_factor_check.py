"""Cheap falsification of a possible multiplier to cancel arc poles."""
import itertools as it
import json
import math
from collections import defaultdict
from pathlib import Path

HERE=Path(__file__).resolve().parent
P=524287

def add(*polys):
    out=defaultdict(int)
    for f in polys:
        for a,c in f.items():out[a]=(out[a]+c)%P
    return {a:c for a,c in out.items() if c}

def scale(f,c):return {a:v*c%P for a,v in f.items() if v*c%P}
def mul(f,g):
    out=defaultdict(int)
    for a,c in f.items():
        for b,d in g.items():
            ab=tuple(x+y for x,y in zip(a,b))
            out[ab]=(out[ab]+c*d)%P
    return {a:c for a,c in out.items() if c}
def linear(values):return {tuple(int(i==j) for i in range(5)):v%P for j,v in enumerate(values) if v%P}

def endpoint(Y):
    entry=lambda i,j:linear([m[i][j] for m in Y])
    a=entry(0,0)
    r=[entry(0,i+1) for i in range(3)]
    c=[entry(i+1,0) for i in range(3)]
    inv2=pow(2,-1,P)
    S=[[scale(add(entry(i+1,j+1),entry(j+1,i+1)),inv2) for j in range(3)] for i in range(3)]
    skew=lambda i,j:scale(add(entry(i,j),scale(entry(j,i),-1)),inv2)
    v=[scale(skew(2,3),-1),skew(1,3),scale(skew(1,2),-1)]
    cubic=add(*(mul(mul(v[i],S[i][j]),v[j]) for i in range(3) for j in range(3)))
    rv=add(*(mul(r[i],v[i]) for i in range(3)))
    cv=add(*(mul(c[i],v[i]) for i in range(3)))
    return add(mul(a,cubic),scale(mul(rv,cv),-1))

def H(f):
    rows=[[] for _ in range(5)]
    for a,c in f.items():
        inds=tuple(i for i,n in enumerate(a) for _ in range(n))
        v=c*math.prod(math.factorial(n) for n in a)%P
        for t in set(it.permutations(inds)):rows[t[0]].append((t[1:],v))
    dp={(0,0,0):1}
    for row in rows:
        nxt=defaultdict(int)
        for masks,val in dp.items():
            for vs,c in row:
                if any(m&(1<<v) for m,v in zip(masks,vs)):continue
                s=(-1)**sum((m>>(v+1)).bit_count() for m,v in zip(masks,vs))
                key=tuple(m|(1<<v) for m,v in zip(masks,vs))
                nxt[key]=(nxt[key]+s*val*c)%P
        dp={k:v for k,v in nxt.items() if v}
    return dp.get((31,31,31),0)

def main():
    data=json.loads(HERE.joinpath('pilot.json').read_text())
    vals=[H(endpoint(Y)) for Y in data['points']]
    result={'prime':P,'H5_at_arc_endpoints':vals,
            'interpretation':'Nonzero means H5 cannot serve as a multiplier vanishing on the boundary arc.'}
    HERE.joinpath('rectangular_factor_check.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))

if __name__=='__main__':main()
