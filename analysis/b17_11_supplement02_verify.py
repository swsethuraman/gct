"""Sole new supplement02 control: fixed polynomial identities, no representation search.

Independent subset determinant recurrence in exponent-vector polynomials.
No producer code is imported. Use the unchanged b15_bound.py with -B,
60 seconds / 512 MiB, one process and one BLAS thread.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import permutations
from math import comb
from pathlib import Path
import hashlib
import json
import time

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'results/b17_11/supplement02'
NAMES = ['a','r1','r2','r3','c1','c2','c3','v1','v2','v3',
         's11','s22','s33','s12','s13','s23','t','u']
WT = [-1]*4+[1]*3+[0]*3+[1]*6
Z = (0,)*18
ONE = {Z:1}
STATS = {'pair_products':0,'peak_support':0}
START = time.perf_counter()


def need(ok, message):
    if not ok: raise AssertionError(message)


def clean(a):
    a = {e:c for e,c in a.items() if c}
    STATS['peak_support'] = max(STATS['peak_support'],len(a))
    need(len(a)<=10000,'UNCOMPUTED support cap')
    return a


def add(*args):
    z=defaultdict(int)
    for a in args:
        for e,c in a.items(): z[e]+=c
    return clean(z)


def scale(a,c): return clean({e:x*c for e,x in a.items()})


def mul(a,b):
    STATS['pair_products']+=len(a)*len(b)
    need(STATS['pair_products']<=1000000,'UNCOMPUTED operation cap')
    z=defaultdict(int)
    for e,c in a.items():
        for f,v in b.items(): z[tuple(x+y for x,y in zip(e,f))]+=c*v
    return clean(z)


def shift(a,j,n):
    z={}
    for e,c in a.items():
        f=list(e); f[j]+=n
        need(f[j]>=0,'division by t requires a proved polynomial factor')
        z[tuple(f)]=c
    return z


def coeff(a,j,n):
    return {tuple(0 if i==j else x for i,x in enumerate(e)):c
            for e,c in a.items() if e[j]==n}


def determinant(M):
    # Ordered row expansion grouped by used columns, unlike producer permutations.
    layer={0:ONE}
    for row in M:
        nxt={}
        for mask,p in layer.items():
            for j,x in enumerate(row):
                if mask & (1<<j): continue
                key=mask | (1<<j)
                term=scale(mul(p,x),(-1)**((mask>>(j+1)).bit_count()))
                nxt[key]=add(nxt.get(key,{}),term)
        layer=nxt
    return layer[(1<<len(M))-1]


def dot(a,b): return add(*(mul(x,y) for x,y in zip(a,b)))
def mv(M,v): return [dot(r,v) for r in M]
def mm(A,B): return [[dot(r,c) for c in zip(*B)] for r in A]
def skew(v):
    return [[{},scale(v[2],-1),v[1]],[v[2],{},scale(v[0],-1)],
            [scale(v[1],-1),v[0],{}]]


def adj3(E):
    # Cayley-Hamilton adjugate, independent of producer's cofactor routine.
    tr=add(*(E[i][i] for i in range(3)))
    e2=add(*(add(mul(E[i][i],E[j][j]),scale(mul(E[i][j],E[j][i]),-1))
             for i in range(3) for j in range(i+1,3)))
    E2=mm(E,E)
    return [[add(E2[i][j],scale(mul(tr,E[i][j]),-1),e2 if i==j else {})
             for j in range(3)] for i in range(3)]


def translate_J(a):
    # x -> J+u*x via binomial coefficients; only three diagonal S coordinates shift.
    ans={}
    for e,c in a.items():
        base=list(e); base[17]+=sum(e[:16])
        terms={tuple(base):c}
        for j in (10,11,12):
            expanded=defaultdict(int)
            for f,v in terms.items():
                for k in range(f[j]+1):
                    g=list(f); g[j]=k; g[17]-=f[j]-k
                    expanded[tuple(g)]+=v*comb(f[j],k)
            terms=clean(expanded)
        ans=add(ans,terms)
    return ans


def from_records(rows):
    out=defaultdict(int)
    for row in rows:
        e=[0]*18; e[16]=row['t']; e[17]=row['u']
        for name in row['variables']: e[NAMES.index(name)]+=1
        out[tuple(e)]+=row['coefficient']
    return clean(out)


def numeric_det(a):
    a=[list(map(Fraction,row)) for row in a]; value=Fraction(1)
    for k in range(len(a)):
        i=next((i for i in range(k,len(a)) if a[i][k]),None)
        if i is None: return 0
        if i!=k: a[i],a[k]=a[k],a[i]; value=-value
        p=a[k][k]; value*=p
        for j in range(k+1,len(a)):
            q=a[j][k]/p
            a[j]=[x-q*y for x,y in zip(a[j],a[k])]
    return value


def main():
    need(not (OUT/'verification.json').exists(),'preserve sole-run receipt')
    pins=json.loads((OUT/'input_hashes.json').read_text(encoding='utf-8-sig'))
    for item in pins['files']:
        need(hashlib.sha256(Path(item['path']).read_bytes()).hexdigest()==item['sha256'],'input drift')
    saved=json.loads((ROOT.parent/'B15-02/results/b17_02/verification.json').read_text())
    x=[{tuple(int(j==i) for j in range(18)):1} for i in range(18)]
    a,r,c,v=x[0],x[1:4],x[4:7],x[7:10]
    S=[[x[10],x[13],x[14]],[x[13],x[11],x[15]],[x[14],x[15],x[12]]]
    A=skew(v)
    E=[[add(A[i][j],shift(S[i][j],16,1)) for j in range(3)] for i in range(3)]
    # Multiply first row by t before expansion; every resulting term has a t factor.
    N=[[a]+r]+[[shift(c[i],16,1)]+E[i] for i in range(3)]
    numerator=determinant(N)
    need(min(e[16] for e in numerator)==1,'t factor')
    arc=shift(numerator,16,-1)
    Q0=add(mul(a,dot(v,mv(S,v))),scale(mul(dot(r,v),dot(v,c)),-1))
    Q1=dot(r,mv(skew(mv(S,v)),c))
    Q2=add(mul(a,determinant(S)),scale(dot(r,mv(adj3(S),c)),-1))
    qs=[Q0,Q1,Q2]
    need(arc==add(*(shift(q,16,k) for k,q in enumerate(qs))),'three-term arc')
    need(qs==[from_records(row) for row in saved['arc_coefficient_records']],'all saved arc coefficients')
    need(all(sum(e[:16])==4 and e[16]==sum(w*k for w,k in zip(WT,e)) for e in arc),'gamma weights')
    need([len(q) for q in qs]==[15,18,23],'arc supports')
    need(determinant(E)==add(shift(dot(v,mv(S,v)),16,1),shift(determinant(S),16,3)),'skew determinant')
    adjE,adjS,mid=adj3(E),adj3(S),skew(mv(S,v))
    for i in range(3):
        for j in range(3):
            need(adjE[i][j]==add(mul(v[i],v[j]),scale(shift(mid[i][j],16,1),-1),shift(adjS[i][j],16,2)),'adjugate entry')
    J=translate_J(arc)
    need([coeff(J,17,k) for k in range(1,5)]==[from_records(row) for row in saved['taylor_coefficient_records']],'all Taylor coefficients')
    boundary=coeff(J,16,0)
    need(not coeff(boundary,17,1) and not coeff(boundary,17,2),'triple-point lower orders')
    need(coeff(boundary,17,3)==mul(a,dot(v,v))!= {},'reducible cubic leading form')
    need(coeff(boundary,17,4)==Q0,'quartic Taylor term')
    raw=[[a]+r]+[[c[i]]+[add(A[i][j],S[i][j]) for j in range(3)] for i in range(3)]
    linear=[[entry.get(tuple(int(k==j) for k in range(18)),0) for j in range(16)]
            for row in raw for entry in row]
    change=numeric_det(linear)
    need(abs(change)==8 and sum(WT)==5,'invertible adapted coordinates and gamma determinant')
    wrong=add(Q0,scale(shift(Q1,16,1),-1),shift(Q2,16,2))
    missing=add(arc,scale(mul(mul(mul(a,v[0]),v[1]),S[0][1]),-2))
    need(wrong!=arc and missing!=arc,'sign and factorial controls')
    need(Q0 and Q2,'both interval endpoints required by degree1 determinant')
    clipping_checks=0
    for ambient in range(7):
        for s in range(7):
            for b in range(s+1):
                B0=min(ambient,s); B=min(ambient,s-b)
                need((B<B0)==(b>=s-B0+1),'clipping threshold equivalence')
                clipping_checks+=1
    need(min(3,5-1)==3 and min(3,5-3)==2,'nonzero b can fail after clipping')
    perms=list(permutations(range(4)))
    base=[[0,1,0,2],[1,0,2,0],[2,0,0,1],[0,2,1,0]]
    w=[[base[i][j]+[-3,1,1,1][i] for j in range(4)] for i in range(4)]
    pw=[sum(w[i][sig[i]] for i in range(4)) for sig in perms]
    need(min(pw)>=0,'fixed original-entry arc is polynomial')
    chosen=[perms[0],(1,2,3,0),(3,2,1,0)]
    margins=[[sum(sig[i]==j for sig in chosen) for j in range(4)] for i in range(4)]
    work=[row[:] for row in margins]; decomposed=[]
    for _ in range(3):
        sig=next(sig for sig in perms if all(work[i][sig[i]]>0 for i in range(4)))
        decomposed.append(sig)
        for i in range(4): work[i][sig[i]]-=1
    need(not any(sum(row) for row in work),'matching decomposition')
    total=sum(w[i][j]*margins[i][j] for i in range(4) for j in range(4))
    need(total==sum(sum(w[i][sig[i]] for i in range(4)) for sig in decomposed),'weight additivity')
    need(0<=total<=3*max(pw) and 12*w[0][0]<0,'torus margins are necessary control')
    result={'status':'PASS','input_hashes_checked':len(pins['files']),
            'arc_supports':[len(q) for q in qs],'taylor_support':len(J),
            'coordinate_change_determinant':str(change),'gamma_determinant_exponent':sum(WT),
            'all_saved_arc_and_taylor_coefficients_match':True,'all_nine_adjugate_entries_match':True,
            'clipping_arithmetic_checks':clipping_checks,
            'entry_diagonal_control':{'d':3,'permutation_weight_range':[min(pw),max(pw)],'matrix':margins,'weight':total,'matching_decomposition':decomposed},
            'adversarial_controls':['Q1 sign','missing symmetric cross-term factor2','both degree1 interval endpoints','nonzero rank need not improve clipped bound','non-torus-invariant word can have negative weight'],
            'statistics':STATS,'seconds':time.perf_counter()-START,
            'scope':'Fixed identities and tiny arithmetic only; all-degree and representation statements are proved in supplement',
            'producer_imports':False,'new_representation_rank':'UNCOMPUTED','numeric_improvement':False}
    (OUT/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))


if __name__=='__main__': main()
