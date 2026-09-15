"""Finite quartic counts by exact hook corrections to accepted stable counts.

Uses B16-02 branching identity, skew Jacobi-Trudi, and power-sum pairing.
No assumption of stability in the six requested cells.
"""
from collections import defaultdict
from fractions import Fraction as Q
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
from time import perf_counter
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('toy',ROOT/'symmetry_dream/astra/toy_character_screen.py')
t=importlib.util.module_from_spec(spec);spec.loader.exec_module(t)

def mul(A,B):
    out=defaultdict(Q)
    for x,a in A.items():
        for y,b in B.items():out[tuple(sorted(x+y,reverse=True))]+=a*b
    return {x:a for x,a in out.items() if a}

@lru_cache(None)
def G(b,m):
    out=defaultdict(Q)
    for b4 in range(b+1):
        b3=m-2*b-2*b4;b2=b-b3-b4
        if min(b2,b3)<0:continue
        P=mul(mul(t.pleth_ps(b2,2),t.pleth_ps(b3,3)),t.pleth_ps(b4,4))
        for x,a in P.items():out[x]+=a
    return dict(out)

def skew_ps(lam,mu):
    """s_(lam/mu)=det(h_(lam_i-mu_j-i+j)), exact determinant DP."""
    n=len(lam);mu=mu+(0,)*(n-len(mu))
    if len(mu)>n or any(a<b for a,b in zip(lam,mu)):return {}
    states={0:{():1}}
    for i in range(n):
        nxt={}
        for mask,terms in states.items():
            for j in range(n):
                if mask>>j&1:continue
                k=lam[i]-mu[j]-i+j
                if k<0:continue
                sign=(-1)**sum(mask>>v&1 for v in range(j+1,n))
                dest=nxt.setdefault(mask|1<<j,defaultdict(int))
                for hs,c in terms.items():dest[tuple(sorted(hs+((k,) if k else ()),reverse=True))]+=sign*c
        states={mask:{hs:c for hs,c in terms.items() if c} for mask,terms in nxt.items()}
    out=defaultdict(Q)
    for hs,c in states.get((1<<n)-1,{}).items():
        P={():Q(c)}
        for h in hs:P=mul(P,t.pleth_ps(h,1))
        for rho,a in P.items():out[rho]+=a
    return {rho:a for rho,a in out.items() if a}

def correction(d,tail):
    n=sum(tail);records=[];total=0
    assert d>=n//2
    for b in range(n//2+1):
        for m in range(2*b,min(4*b,n)+1):
            L=n-m;D=d-b
            if not L>D>=0:continue
            hook=(D+1,)+(1,)*(L-D-1)
            if len(hook)>len(tail) or any(x>y for x,y in zip(hook,tail)):continue
            P=G(b,m);S=skew_ps(tail,hook)
            v=sum((a*S.get(rho,0)*t.zpart(rho) for rho,a in P.items()),Q())
            assert v.denominator==1 and v>=0
            signed=(-1)**(L-D)*int(v);total+=signed
            records.append(dict(b=b,m=m,hook=hook,lr_pairing=int(v),signed=signed))
    return total,records

def stable(tail):
    return sum((sum((a*t.char(tail,rho) for rho,a in G(b,sum(tail)).items()),Q())
                for b in range(sum(tail)//2+1)),Q())

def main():
    start=perf_counter();t.controls();controls=0
    for d in range(1,5):
        for lam in t.parts(4*d):
            tail=lam[1:]
            if not tail or len(tail)>3 or sum(tail)>8 or d<sum(tail)//2:continue
            delta,_=correction(d,tail)
            assert stable(tail)+delta==t.pleth_mult(d,4,lam),(d,lam)
            controls+=1
    rows=[]
    for d,tailfirst,q,U,ainf in [(23,17,2,218,294),(24,17,3,218,294),
                               (23,19,4,288,429),(24,19,7,288,429),
                               (25,19,9,288,429),(26,19,10,288,429)]:
        tail=(tailfirst,)+(2,)*8
        delta,records=correction(d,tail);a=ainf+delta
        row=dict(d=d,t=tailfirst,weight=(4*d-sum(tail),)+tail,stable_a=ainf,
                 correction=delta,a=a,exact_i_det=q,padding_ceiling=U,
                 determinant_multiplicity=a-q,D_upper=q+U-a,
                 excluded=q+U<=a,correction_terms=records)
        rows.append(row)
        print(json.dumps({k:v for k,v in row.items() if k!='correction_terms'}),flush=True)
        (ROOT/'finite_screen.json').write_text(json.dumps(dict(status='PARTIAL',controls=controls,rows=rows),indent=2)+'\n')
    result=dict(status='COMPLETE',controls=controls,rows=rows,seconds=perf_counter()-start,
                inherited='B16 stable counts294/429; complete finite ideals; split-cubic ceilings218/288',
                method='Exact B16 finite hook corrections, skew Jacobi-Trudi and rational power-sum pairing')
    (ROOT/'finite_screen.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status='COMPLETE',controls=controls,seconds=result['seconds'])),flush=True)
if __name__=='__main__':main()
