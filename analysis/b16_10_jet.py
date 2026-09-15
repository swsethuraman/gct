"""Exact source-arc coefficients on independent z*per3; standard library.

B16-10, gpt-6-astra. Finite source formulas are attributed to the accepted
Hessian11_1631 report. All Hessians below are freshly differentiated from
the six permanent monomials. No saved Hessian/evaluation array is imported.
Run with -B through inspected analysis/b15_bound.py (60s, 512 MiB).
"""
import argparse
from copy import deepcopy
from fractions import Fraction as Q
from itertools import permutations, combinations
from math import comb
from pathlib import Path
import hashlib
import json
import os
import time

ORDER = 2
STATS = {'max_polynomial_support': 0, 'max_determinant_states': 0,
         'determinant_transitions': 0, 'polynomial_products': 0}
ROOT = Path(__file__).resolve().parents[1]


def need(ok, message):
    if not ok:
        raise ValueError(message)


def guard():
    if time.monotonic()+3 > float(os.environ.get('CI73_DEADLINE', 'inf')):
        raise RuntimeError('Incomplete: approaching bounded deadline')


def clean(p):
    p = {k: Q(v) for k,v in p.items() if v}
    need(len(p) <= 50000, 'support cap exceeded')
    STATS['max_polynomial_support'] = max(STATS['max_polynomial_support'],len(p))
    return p


def const(v):
    return {(0,0):Q(v)} if v else {}


def add(p,q):
    out = p.copy()
    for k,v in q.items(): out[k] = out.get(k,0)+v
    return clean(out)


def scale(p,v):
    return clean({k:x*v for k,x in p.items()})


def mul(p,q):
    STATS['polynomial_products'] += 1
    out = {}
    for (t,u),x in p.items():
        for (s,v),y in q.items():
            if u+v <= ORDER:
                k=(t+s,u+v)
                out[k]=out.get(k,0)+x*y
    return clean(out)


def power(p,n):
    need(n >= 0, 'negative power')
    out=const(1)
    while n:
        if n&1: out=mul(out,p)
        p=mul(p,p); n//=2
    return out


def inv(p):
    need(all(t==0 for t,u in p), 'inverse must be a u-series')
    a=p.get((0,0),0)
    need(a != 0, 'leading coefficient chart excludes c(0)=0')
    z=add(const(1),scale(p,-1/a))
    out=const(0)
    for k in range(ORDER+1): out=add(out,power(z,k))
    return scale(out,1/a)


def coeff(p,t):
    return {(0,u):v for (s,u),v in p.items() if s==t}


def det(A):
    """Subset determinant recurrence, no inverse or division by a pivot."""
    n=len(A); states={0:const(1)}
    for i in range(n):
        guard(); nxt={}
        for mask,v in states.items():
            for j in range(n):
                if mask & (1<<j) or not A[i][j]: continue
                sign=(-1)**((mask>>(j+1)).bit_count())
                key=mask|(1<<j)
                nxt[key]=add(nxt.get(key,{}),scale(mul(v,A[i][j]),sign))
                STATS['determinant_transitions']+=1
        states={k:v for k,v in nxt.items() if v}
        STATS['max_determinant_states']=max(STATS['max_determinant_states'],len(states))
    return states.get((1<<n)-1,{})


def remainder(p,q):
    degree=max(t for t,u in q)
    need(coeff(q,degree)==const(1), 'divisor must be monic')
    out=p.copy()
    for k in range(max((t for t,u in p),default=-1), degree-1,-1):
        v=coeff(out,k)
        if v:
            term={(t+k-degree,u):x for (t,u),x in mul(v,q).items()}
            out=add(out,scale(term,-1))
    return out


def shift(p,s):
    need(all(t==0 for t,u in s), 'shift must be a u-series')
    out={}
    for (t,u),v in p.items():
        for j in range(t+1):
            term=mul({(j,u):v*comb(t,j)},power(s,t-j))
            out=add(out,term)
    return out


def multiply_all(polys):
    out=const(1)
    for p in polys: out=mul(out,p)
    return out


MONS=[(0,)+tuple(1+3*i+p[i] for i in range(3))
      for p in permutations(range(3))]


def poly_mons(y,mons):
    out={}
    for mon in mons: out=add(out,multiply_all([y[i] for i in mon]))
    return out


def hessian(y,mons):
    n=len(y)
    return [[poly_mons(y,[tuple(k for k in mon if k not in (i,j))
                          for mon in mons if i in mon and j in mon])
             if i!=j else {} for j in range(n)] for i in range(n)]


def base_matrix():
    a=[1,1,0,0,0,1,0,0,0,1]
    b=[2,1,2,1,3,1,2,2,1,4]
    cols=[a,b]+[[int(i==j) for i in range(10)] for j in range(2,10)]
    return [list(row) for row in zip(*cols)]


def sources(L0,changes,direct_check=False):
    need(len(L0)==10 and all(len(row)==10 for row in L0),'10 by 10 source frame')
    L=[[const(v) for v in row] for row in L0]
    for row,col,value in changes:
        need(0<=row<10 and 0<=col<10 and type(value) is int,'arc direction')
        L[row][col]=add(L[row][col],{(0,1):Q(value)})
    detL=det(L)
    need(detL.get((0,0),0)!=0,'arc base must be invertible')
    y=[add(mul(row[0],{(1,0):Q(1)}),row[1]) for row in L]
    P=poly_mons(y,MONS)
    C=poly_mons(y,[m[1:] for m in MONS])
    HC=hessian(y,[m[1:] for m in MONS])
    HC=[row[1:] for row in HC[1:]]
    DH=scale(multiply_all([power(y[0],8),C,det(HC)]),-Q(3,2))
    if direct_check:
        need(det(hessian(y,MONS))==DH,'independent full 10-Hessian factorization')
    # Full Hessian congruence: det Hess(P composed L) = det(L)^2 det Hess(P).
    D=mul(power(detL,2),DH)
    c=coeff(P,4); cinv=inv(c)
    pn=mul(P,cinv); dn=mul(D,power(cinv,10))
    raw=remainder(dn,power(pn,2))
    s=scale(coeff(pn,3),-Q(1,4))
    dep=shift(pn,s); rem=shift(raw,s)
    need(coeff(dep,3)=={},'depression cubic coefficient')
    ss=[coeff(dep,i) for i in range(5)]
    S=[coeff(rem,i) for i in range(8)]
    need(add(add(S[3],scale(mul(ss[2],S[5]),-1)),
             add(scale(mul(ss[1],S[6]),-1),
                 scale(mul(add(ss[0],scale(power(ss[2],2),-1)),S[7]),-1)))=={},
         'exact shared padding remainder identity')
    f23=[mul(power(c,23),S[7])]
    f25=[mul(power(c,25),S[5]),mul(power(c,25),mul(ss[2],S[7]))]
    f27=[mul(power(c,27),v) for v in
         [S[3],mul(ss[2],S[5]),mul(ss[1],S[6]),mul(ss[0],S[7]),mul(power(ss[2],2),S[7])]]
    return dict(det_L=encode(detL),c=encode(c),P=encode(P),D=encode(D),
                depressed_P=encode(dep),S=encode(rem),
                coefficient_rows={str(d):[[pack(f.get((0,k),0)) for f in fs]
                                         for k in range(ORDER+1)]
                                  for d,fs in ((23,f23),(25,f25),(27,f27))},
                direct_full_hessian_check=direct_check)


def pack(q):
    q=Q(q)
    return str(q.numerator) if q.denominator==1 else f'{q.numerator}/{q.denominator}'


def encode(p):
    return [[t,u,pack(v)] for (t,u),v in sorted(p.items())]


def minor(A):
    n=len(A)
    need(all(len(row)==n for row in A),'square minor')
    out=Q(0)
    for p in permutations(range(n)):
        sign=(-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        v=Q(sign)
        for i in range(n): v*=Q(A[i][p[i]])
        out+=v
    return out


def independent_minor(rows):
    for n in range(min(len(rows),len(rows[0])),0,-1):
        for rr in combinations(range(len(rows)),n):
            for cc in combinations(range(len(rows[0])),n):
                m=minor([[rows[i][j] for j in cc] for i in rr])
                if m: return dict(rows=list(rr),columns=list(cc),determinant=pack(m),rank_floor=n)
    return dict(rows=[],columns=[],determinant='0',rank_floor=0)


def price():
    return {'order':ORDER,'arc_parameters':1,'jet_slots':ORDER+1,
            'determinant_states_ub_9':max(comb(9,k) for k in range(10)),
            'determinant_states_ub_10':max(comb(10,k) for k in range(11)),
            'determinant_transitions_ub_9':9*2**8,
            'determinant_transitions_ub_10':10*2**9,
            'Hessian_t_degree_bound':20,'polynomial_slots_t_u_ub':21*(ORDER+1),
            'candidate_functions':8,'hard_live_monomial_cap':50000,
            'dense_source_support_ub_not_allocated':{
                str(d):str(comb(4*d+100,100)) for d in (23,25,26,27)},
            'one_affine_line_complete_coefficient_rows':{str(d):4*d+1 for d in (23,25,26,27)},
            'scope':'tiny instrument; no dense ambient carrier or full rank production'}


def calculate(spec):
    need(spec['format']=='b16-10-padding-arc/1','format')
    need(spec['jet_order']==ORDER,'order')
    need(spec['source_order']==['z']+[f'X{i}{j}' for i in range(1,4) for j in range(1,4)],'source order')
    arcs=[]
    need(1<=len(spec['arcs'])<=4,'tiny arc count cap')
    for arc in spec['arcs']:
        arcs.append(sources(spec['base_matrix'],arc['changes'],arc['direct_hessian_check']))
    floors={}
    for d in (23,25,27):
        rows=[row for a in arcs for row in a['coefficient_rows'][str(d)]]
        floors[str(d)]=independent_minor(rows)
    need(arcs[0]['coefficient_rows']['23'][0][0]=='8918784','inherited point liveness independently regenerated')
    return {'arcs':arcs,'minors':floors,'pricing':price(),
            'claim':'Exact coefficient restriction floors for named inherited finite HW sources only; no positive gap.'}


def spec():
    return {'format':'b16-10-padding-arc/1','jet_order':ORDER,
            'source_order':['z']+[f'X{i}{j}' for i in range(1,4) for j in range(1,4)],
            'target_order':['t']+[f'x{i}' for i in range(1,10)],
            'base_matrix':base_matrix(),
            'arcs':[{'changes':[[2,0,1]],'direct_hessian_check':True}],
            'finite_sources':{'23':['c^23 S7'],'25':['c^25 S5','c^25 s2 S7'],
                              '27':['c^27 S3','c^27 s2 S5','c^27 s3 S6','c^27 s4 S7','c^27 s2^2 S7']}}


def main():
    p=argparse.ArgumentParser()
    p.add_argument('mode',choices=['price','produce','verify'])
    p.add_argument('--certificate',type=Path,default=ROOT/'results/b16_10/jet_certificate.json')
    p.add_argument('--receipt',type=Path)
    a=p.parse_args(); start=time.monotonic()
    if a.mode=='price': result=price()
    elif a.mode=='produce':
        need(not a.certificate.exists(),'preserve existing certificate')
        s=spec(); result=calculate(s)
        a.certificate.parent.mkdir(parents=True,exist_ok=True)
        a.certificate.write_text(json.dumps({'spec':s,'result':result},indent=2)+'\n')
    else:
        cert=json.loads(a.certificate.read_text())
        need(cert['spec']==spec(),'exact named source and arc specification')
        result=calculate(cert['spec'])
        need(result==cert['result'],'coefficient/minor certificate mismatch')
    receipt={'status':'PASS','mode':a.mode,'seconds':time.monotonic()-start,
             'statistics':STATS,'minors':result.get('minors'),
             'module_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    if a.receipt:
        need(not a.receipt.exists(),'preserve existing receipt')
        a.receipt.write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt if a.mode!='price' else result),flush=True)


if __name__=='__main__': main()
