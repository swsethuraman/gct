"""Direct epsilon products, without the signed aggregate used by the producer."""
import itertools as it
import json
import math
import time
from collections import defaultdict
from pathlib import Path
import sixrow_witness as producer

START=time.monotonic()

def eps(v):
    if sorted(v)!=list(range(4)):
        return 0
    return (-1)**sum(v[i]>v[j] for i in range(4) for j in range(i+1,4))

def subset_key(a,b,side):
    out=[]
    for indices,blocks in ((a,producer.PI),(b,producer.RHO)):
        for block in blocks:
            pair=block[:2] if side==0 else tuple(x-6 for x in block[2:])
            p=[indices[i] for i in pair]
            if p[0]==p[1]:
                return None
            out.append((1<<p[0])|(1<<p[1]))
    return tuple(out)

def direct_P(matrices):
    terms=producer.column_assignments(matrices)
    right=defaultdict(list)
    for a,b,v in terms:
        key=subset_key(a,b,1)
        if key is not None:
            right[key].append((a,b,v))
    total=pairs=0
    for a,b,v in terms:
        key=subset_key(a,b,0)
        if key is None:
            continue
        for c,d,w in right.get(tuple(15^x for x in key),()):
            aa,bb=a+c,b+d
            ss=math.prod(eps(tuple(aa[i] for i in block)) for block in producer.PI)
            ss*=math.prod(eps(tuple(bb[i] for i in block)) for block in producer.RHO)
            total+=v*w*ss
            pairs+=1
    return total,pairs

def direct_H(f):
    rows=[[] for _ in range(6)]
    for alpha,c in f.items():
        inds=[i for i,a in enumerate(alpha) for _ in range(a)]
        for t in set(it.permutations(inds)):
            rows[t[0]].append((t[1:],c*math.prod(math.factorial(a) for a in alpha)))
    leaves=0
    def visit(i,cols,val):
        nonlocal leaves
        if i==6:
            leaves+=1
            ss=math.prod((-1)**sum(c[j]>c[k] for j in range(6) for k in range(j+1,6)) for c in cols)
            return ss*val
        total=0
        for triple,c in rows[i]:
            if all(v not in col for col,v in zip(cols,triple)):
                total+=visit(i+1,[col+[v] for col,v in zip(cols,triple)],val*c)
        return total
    return visit(0,[[],[],[]],1),leaves

def main():
    data=json.loads(Path(__file__).with_name('sixrow_witness.json').read_text())
    out={'checks':[]}
    for point in data['points']:
        matrices=point['matrices']
        p,n=direct_P(matrices)
        pt,nt=direct_P(producer.transpose(matrices))
        h,leaves=direct_H(producer.quartic(matrices))
        assert p+pt==point['Q']
        assert h==point['H']
        out['checks'].append(dict(point=point['label'],Q=p+pt,H=h,epsilon_pairs=n+nt,H_terms=leaves))
    p0,p1=data['points']
    minor=p0['H']*p1['Q_squared']-p1['H']*p0['Q_squared']
    assert minor==data['descent_minor'] and minor!=0
    out['minor']=minor
    out['elapsed_seconds']=time.monotonic()-START
    out['all_passed']=True
    Path(__file__).with_name('verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':
    main()
