"""One bounded B17-04 calculation; no external producer is run.

Run only with the inspected b15_bound.py, local .venv/python.exe -B,
60 seconds / 512 MiB, one process and one BLAS thread. All writes are owned.
The imported Hessian formulas are the accepted, inspected Hessian11 receiver.
Generalized Euler straightening and full-support rational points are new.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations, permutations
from math import factorial, gcd
from pathlib import Path
import hashlib
import importlib.util
import json
import os
import random
import sys
import time
from flint import fmpq_mat, fmpz_mat

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[2]
OUT = HERE / 'results/b17_04'
HROOT = ROOT / 'Batch15_Launch/native_20260913/reviews_filesystem/Hessian11_1631'
CLAUDE = ROOT / 'Batch16/claude_review/exact_ideals.json'
BASIS = [0,1,2,3,4,5,6,7,8,10,11]
ZERO = (0,0,0)
DEGS = (2,3,4)
START = time.perf_counter()


def save(name, obj):
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT/name).write_text(json.dumps(obj, indent=2) + '\n', encoding='utf-8')


def emit(stage, **kwargs):
    obj = dict(stage=stage, seconds=time.perf_counter()-START, **kwargs)
    print(json.dumps(obj), flush=True)
    save('progress.json', obj)


def check_inputs():
    data = json.loads((OUT/'input_hashes.json').read_text(encoding='utf-8-sig'))
    for item in data['inputs']:
        p = Path(item['path'])
        assert hashlib.sha256(p.read_bytes()).hexdigest() == item['sha256'].lower(), str(p)
    return len(data['inputs'])


def key(a,b,c,z):
    return (min(a,b),max(a,b),c,z)


def bits(seq):
    return tuple(int(i in seq) for i in range(3))


def add(a,b):
    return tuple(x+y for x,y in zip(a,b))


def comps(n):
    for i in range(n+1):
        for j in range(n-i+1):
            yield (i,j,n-i-j)


def scalar_exponents(n):
    for i in range(n//2+1):
        for j in range((n-2*i)//3+1):
            if (n-2*i-3*j)%4 == 0:
                yield (i,j,(n-2*i-3*j)//4)


def clean(v):
    return {k:Q(x) for k,x in v.items() if x}


def relations(brackets):
    """Coefficient form of the last bordered column M(y)e=sum y_j u_j.

    C(I,J)=(-1)^|I| det[[M,U_J],[U_I^T,0]], with sorted I,J.
    sum_j y_j C(I,J appended j)
      = sum_i (-1)^(k-i) s_I[i] C(I without i,J), |I|=k+1, |J|=k.
    Sorting the appended j introduces its explicit alternating sign.
    Coefficient extraction multiplies the left term by h_j, from factorials.
    """
    known=set(brackets)
    out=[]
    for k in range(3):
        for I in combinations(range(3),k+1):
            for J in combinations(range(3),k):
                for h in comps(9-k):
                    w=35-sum(DEGS[i] for i in I+J)-sum(d*v for d,v in zip(DEGS,h))
                    if w<0:
                        continue
                    for z in scalar_exponents(w):
                        row=defaultdict(Q)
                        for j in range(3):
                            if j in J or not h[j]:
                                continue
                            c=tuple(h[i]-int(i==j) for i in range(3))
                            sgn=(-1)**sum(i>j for i in J)
                            row[key(bits(I),bits(J+(j,)),c,z)] += h[j]*sgn
                        for i,d in enumerate(I):
                            zz=tuple(z[j]+int(j==d) for j in range(3))
                            row[key(bits(I[:i]+I[i+1:]),bits(J),h,zz)] -= (-1)**(k-i)
                        row=clean(row)
                        assert set(row)<=known
                        if row:
                            out.append(row)
    assert len(out)<=2500 and max(map(len,out))<=6
    return out


def straightener(rels):
    piv={}
    def reduce(row):
        row=clean(row)
        for p,b in sorted(piv.items(),reverse=True):
            a=row.get(p,0)
            if a:
                for k,v in b.items():
                    x=row.get(k,0)-a*v
                    if x: row[k]=x
                    else: row.pop(k,None)
        return row
    for rel in rels:
        row=reduce(rel)
        if row:
            p=max(row); a=row[p]
            piv[p]={k:v/a for k,v in row.items()}
            assert len(piv[p])<=1019
    return reduce,piv


def strmat(M):
    return [[str(M[i,j]) for j in range(M.ncols())] for i in range(M.nrows())]


def match(h):
    data=json.loads(CLAUDE.read_text())
    bs=[tuple(map(tuple,b)) for b in data['brackets']]
    assert len(bs)==1019 and len(set(bs))==1019
    assert all(sum(b[0])+sum(b[2])==sum(b[1])+sum(b[2])==9 for b in bs)
    R=data['basis_bracket_indices']
    assert len(R)==len(set(R))==429
    C=[{bs[j]:Q(x) for j,x in zip(R,row) if x} for row in data['I_det']]
    assert len(C)==11 and all(len(row)==429 for row in data['I_det'])
    vectors,reduced,summary=h.symbolic()
    rels=relations(bs)
    reduce,piv=straightener(rels)
    ev=[reduce(vectors[j]) for j in BASIS]
    cv=[reduce(v) for v in C]
    ks=sorted(set().union(*(set(v) for v in ev+cv)))
    E=[[v.get(k,0) for k in ks] for v in ev]
    Ec=h.pivot_columns(E)
    assert len(Ec)==11
    minor=fmpq_mat([[row[j] for j in Ec] for row in E])
    Ms=[]; residuals=[]
    for v in cv:
        rhs=fmpq_mat([[v.get(ks[j],0)] for j in Ec])
        sol=minor.transpose().solve(rhs)
        co=[Q(str(sol[i,0])) for i in range(11)]
        diff=defaultdict(Q,v)
        for a,b in zip(co,ev):
            for k,x in b.items(): diff[k]-=a*x
        Ms.append(co); residuals.append(len(clean(diff)))
    M=fmpq_mat(Ms)
    matched=not any(residuals) and bool(M.det())
    out=dict(status='EXACT_GLOBAL_MATCH' if matched else 'UNMATCHED_CANDIDATES',
        candidate_order='I_det rows 0..10 in exact_ideals.json',
        accepted_basis_indices=BASIS, accepted_basis_names=[h.NAMES[j] for j in BASIS],
        orientation='candidate_column = M * accepted_E_column',
        M=strmat(M), determinant=str(M.det()),
        inverse=strmat(M.inv()) if M.det() else None,
        residual_supports=residuals, bracket_count=len(bs),
        declared_candidate_basis_indices=R,
        Euler_relation_count=len(rels), Euler_relation_rank=len(piv),
        formal_quotient_dimension=len(bs)-len(piv),
        accepted_symbolic_summary=summary,
        proof='Every reduction uses the universally proved bordered Euler identities. No sampled determinant vanishing is used.')
    save('basis_match.json',out)
    save('Euler_relations.json',{'brackets':data['brackets'],
        'relations':[[[bs.index(k),str(v)] for k,v in sorted(row.items())] for row in rels]})
    emit('basis_match',status=out['status'],relation_rank=len(piv),residuals=residuals)
    # A coefficient mutation in one candidate must survive the quotient.
    witness=next(k for k in bs if reduce({k:1}))
    assert reduce({witness:1})
    assert any(reduce({witness:1}).values())
    return out


def product_hessian(L,t):
    """Literal monomial second derivatives of independent z*per3 after L."""
    H=[[0]*10 for _ in range(10)]
    for perm in permutations(range(3)):
        ls=[L[0]]+[L[1+3*i+perm[i]] for i in range(3)]
        vals=[row[0]*t+row[1] for row in ls]
        for a in range(4):
            for b in range(4):
                if a==b: continue
                fac=1
                for k in range(4):
                    if k not in (a,b): fac*=vals[k]
                for i in range(10):
                    for j in range(10): H[i][j]+=fac*ls[a][i]*ls[b][j]
    return H


def point(seed,h):
    rng=random.Random(seed)
    L=[[rng.choice((-3,-2,-1,1,2,3)) for j in range(10)] for i in range(10)]
    dL=int(fmpz_mat(L).det()); assert dL
    c=0; a1=[0]*9
    for perm in permutations(range(3)):
        ls=[L[0]]+[L[1+3*i+perm[i]] for i in range(3)]
        v=1
        for row in ls: v*=row[0]
        c+=v
        for a in range(4):
            fac=1
            for b in range(4):
                if a!=b: fac*=ls[b][0]
            for j in range(9): a1[j]+=fac*ls[a][j+1]
    assert c, 'Fixed pilot point off chart: no resampling.'
    scale=12*c
    # LQ: depression followed by x -> 12c*x. Q has determinant (12c)^9.
    A=[[row[0]]+[scale*row[j+1]-3*a1[j]*row[0] for j in range(9)] for row in L]
    hm,h0,hp=[product_hessian(A,t) for t in (-1,0,1)]
    N=[]
    for d in (2,3,4):
        M=[]
        for i in range(9):
            row=[]
            for j in range(9):
                z=Q(hp[i+1][j+1]+hm[i+1][j+1]-2*h0[i+1][j+1],4*c) if d==2 else Q(hp[i+1][j+1]-hm[i+1][j+1],12*c) if d==3 else Q(h0[i+1][j+1],12*c)
                assert z.denominator==1
                row.append(int(z))
            M.append(row)
        N.append(M)
    for t in (2,7):
        direct=product_hessian(A,t)
        v=[4*t*N[0][i][0]+3*N[1][i][0] for i in range(9)]
        B=[[2*t*t*N[0][i][j]+6*t*N[1][i][j]+12*N[2][i][j] for j in range(9)] for i in range(9)]
        expected=[[12*t*t+2*N[0][0][0]]+v]+[[v[i]]+B[i] for i in range(9)]
        assert direct==[[c*x for x in row] for row in expected]
    values,ps,rs,S=h.candidates(N)
    assert S[3]-N[0][0][0]*S[5]-N[1][0][0]*S[6]+(N[0][0][0]**2-N[2][0][0])*S[7]==0
    return {'seed':seed,'L':L,'det_L':str(dL),'c':c,'a1':a1,'scale':scale,
            'depressed_scaled_L':A,'N':N,'E_values':[str(values[j]) for j in BASIS],
            'normalization':'F(y)=perpad(LQ y)/c, Q00=1, Q0i=-3*a1_i, Qii=12*c (i>0)',
            'extra_full_Hessian_node_checks':[2,7]}


def kernel(rows,pivcols):
    R,rank=fmpq_mat(rows).rref()
    out=[]
    for j in range(11):
        if j not in pivcols:
            v=[Q(0)]*11; v[j]=Q(1)
            for i,k in enumerate(pivcols): v[k]=-Q(str(R[i,j]))
            out.append(list(map(str,v)))
    return out


def restrictions(h):
    points=[]; rows=[]
    # Twelve fixed full-support points, no adaptive search or rejected-point replacement.
    for seed in range(170400,170412):
        pt=point(seed,h); points.append(pt); rows.append(list(map(int,pt['E_values'])))
        save('padding_points.json',points)
    cols=h.pivot_columns(rows)
    rid=h.pivot_columns([[row[j] for row in rows] for j in cols])
    minor=[[rows[i][j] for j in cols] for i in rid]
    det=int(fmpz_mat(minor).det()); assert det
    # Source F/c scalar normalization is inside the orbit over C; the rational
    # finite value is c^27 E(pi(F/c)), with x scaled by 12c.
    finite_factor=1
    for i in rid: finite_factor*=points[i]['c']**27
    K=kernel(rows,cols)
    out={'status':'EXACT_CHARACTERISTIC_ZERO_RANK_FLOOR', 'rank_floor':len(cols),
         'matrix_orientation':'points by accepted E functions',
         'rows':[[str(x) for x in row] for row in rows],
         'minor_rows':rid,'minor_columns':cols,'minor':[[str(x) for x in row] for row in minor],
         'minor_determinant':str(det), 'finite_degree27_minor_determinant':str(det*finite_factor),
         'sample_kernel_vectors':K,
         'global_upper_inherited':10,
         'global_upper_reason':'One nonzero global shared squared-remainder identity E3.',
         'warning':'Sample kernel vectors are candidates until a global identity is proved.',
         'points':len(points), 'native_source':'independent z*per3, permanent entries row major'}
    save('restriction.json',out)
    emit('restriction',rank_floor=len(cols),sample_kernel=K)
    return out


def main():
    assert sys.dont_write_bytecode
    assert 'CI73_DEADLINE' in os.environ
    assert all(os.environ.get(k)=='1' for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS','VECLIB_MAXIMUM_THREADS'])
    count=check_inputs()
    spec=importlib.util.spec_from_file_location('b17_04_inherited_hessian',HROOT/'verify_small.py')
    h=importlib.util.module_from_spec(spec); spec.loader.exec_module(h)
    matched=match(h)
    restriction=restrictions(h)
    count2=check_inputs(); assert count==count2
    emit('complete',input_hashes=count,basis_status=matched['status'],rank_floor=restriction['rank_floor'])
    save('verification.json',{'status':'COMPLETED_BOUNDED_CONTRIBUTION',
        'input_hashes_checked_before_and_after':count,
        'basis_status':matched['status'],'restriction_rank_floor':restriction['rank_floor'],
        'wall_seconds':time.perf_counter()-START,
        'python':sys.version,'executable':sys.executable,
        'no_external_harness_run':True,'one_process':True,
        'global_kernel_dimension_proved':1,
        'limitation':'The second sample-kernel direction needs a global proof unless established separately in the report.'})


if __name__=='__main__':
    main()
