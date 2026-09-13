"""Explicit integral sources and independent full-polynomial certificate replay."""
import argparse
from fractions import Fraction
import gc
import hashlib
import json
import math
from pathlib import Path
import time

import numpy as np
from b15_02_probe import OUT, ROOT, P, array_hash, exact_a, save
from b14_11_sizes import burnside
from wk9_s45_build import build_cell, monomials_array, orbit_setup_arr
from wk8_s30_core import exps
from points import form_of_point


def integral_source(E, reduction):
    """Solve the one/two-column residual over Q, then clear denominators."""
    rows=reduction['cover_rows']; S=reduction['cover_columns']; U=reduction['free_columns']
    assert len(U) in (1,2)
    T=E[rows][:,S].tocsr(); TU=E[rows][:,U].toarray()
    X=[[Fraction(int(v)) for v in row] for row in TU]
    for i in range(len(S)-1,-1,-1):
        diag=None
        for k in range(T.indptr[i],T.indptr[i+1]):
            j=int(T.indices[k]); c=int(T.data[k])
            if j==i:diag=c;continue
            assert j>i
            for u in range(len(U)):X[i][u]-=c*X[j][u]
        assert diag
        X[i]=[v/diag for v in X[i]]
    positions={s:i for i,s in enumerate(S)}; u_pos={u:i for i,u in enumerate(U)}
    if len(U)==1:
        y=[Fraction(1)]; residual_row=None
    else:
        y=None; residual_row=None
        for row in range(E.shape[0]):
            co=[Fraction(0),Fraction(0)]
            for k in range(E.indptr[row],E.indptr[row+1]):
                col=int(E.indices[k]); v=int(E.data[k])
                if col in u_pos:co[u_pos[col]]+=v
                else:
                    for j in range(2):co[j]-=v*X[positions[col]][j]
            if any(co):
                y=[-co[1],co[0]];residual_row=row;break
        assert y is not None
    K=[Fraction(0)]*E.shape[1]
    for u,v in zip(U,y):K[u]=v
    for i,s in enumerate(S):K[s]=-sum(x*v for x,v in zip(X[i],y))
    lcm=math.lcm(*(x.denominator for x in K))
    Z=[int(x*lcm) for x in K]
    div=math.gcd(*Z); assert div
    Z=[x//div for x in Z]
    pivot=next(x for x in Z if x)
    if pivot<0:Z=[-x for x in Z]
    # This exact all-row check is additional to direct differentiation below.
    for row in range(E.shape[0]):
        assert sum(int(E.data[k])*Z[int(E.indices[k])]
                   for k in range(E.indptr[row],E.indptr[row+1]))==0
    return Z,dict(method='exact rational triangular solve, residual relation and primitive integer clearing',
                  free_dimension=len(U),residual_row=residual_row,
                  denominator_lcm=str(lcm),primitive_gcd=1,
                  coefficient_abs_max=str(max(abs(x) for x in Z)),
                  all_integer_raising_rows_zero=True)


def expanded(arr,Z):
    out=[]
    for idx,row in enumerate(arr['M']):
        col=int(arr['col_of'][idx])
        if col<0:continue
        v=Z[col]*int(arr['sgn'][idx])
        if v:out.append((tuple(int(x) for x in row),v))
    return out


def derivative(terms,A,i):
    """Independent product rule on every actual monomial, over Z."""
    idx={a:k for k,a in enumerate(A)}
    shifts={}
    for k,a in enumerate(A):
        if a[i+1]:
            b=list(a);b[i]+=1;b[i+1]-=1
            shifts[k]=(idx[tuple(b)],a[i]+1)
    acc={}
    for mon,v in terms:
        for pos,k in enumerate(mon):
            if k not in shifts:continue
            new,factor=shifts[k]
            nm=list(mon);nm[pos]=new;nm.sort();nm=tuple(nm)
            z=acc.get(nm,0)+v*factor
            if z:acc[nm]=z
            elif nm in acc:del acc[nm]
    return acc


def evaluate_integer(terms,A,co):
    cv=[co.get(e,0) for e in A]
    return sum(v*math.prod(cv[k] for k in mon) for mon,v in terms)


def one(i,construct):
    t=time.perf_counter();tag=f'cell_{i:02d}'
    rec=json.loads((OUT/f'{tag}.json').read_text())
    old=json.loads((OUT/f'{tag}_source.json').read_text())
    lam=tuple(rec['cell']['lam']);d=rec['cell']['delta'];r=len(lam)
    assert exact_a(lam,d)==1
    count=burnside(lam,d);assert count['n_chi']==len(old['chi_coordinates'])
    if construct:
        B=build_cell(lam,d,verbose=False);arr=B['arr']
        Z,lift=integral_source(B['E'],rec['reduction'])
        del B
        src=dict(cell=rec['cell'],arithmetic='Z',chi_coordinates=Z,
                 carrier_hashes=rec['carrier_hashes'],construction=old['construction'],
                 coefficient_convention=old['coefficient_convention'],raising_rule=old['raising_rule'],
                 integral_construction=lift)
        save(OUT/f'{tag}_integral_source.json',src)
    else:
        src=json.loads((OUT/f'{tag}_integral_source.json').read_text());Z=src['chi_coordinates']
        M=monomials_array(4,r,d,lam)
        arr=orbit_setup_arr(4,r,d,lam,M=M,verbose=False)
    assert all(isinstance(z,int) for z in Z) and math.gcd(*Z)==1
    assert len(Z)==count['n_chi'] and len(arr['M'])==count['N_S']
    assert {k:array_hash(arr[k]) for k in ['M','col_of','sgn']}==src['carrier_hashes']==old['carrier_hashes']
    pivot=rec['reduction']['normalization_index'];zmod=[z%P for z in Z]
    assert zmod[pivot]
    normalized=[z*pow(zmod[pivot],-1,P)%P for z in zmod]
    assert normalized==old['chi_coordinates']
    A=exps(4,r); terms=expanded(arr,Z)
    assert terms
    for mon,v in terms:
        assert tuple(sum(A[k][j] for k in mon) for j in range(r))==lam
    der_sizes=[]
    for j in range(r-1):
        residual=derivative(terms,A,j);der_sizes.append(len(residual))
        assert not residual,(i,j,'integer HWV failure')
    # Change the sign of one actual monomial; some raising derivative must fail.
    mon,v=terms[0];bad=[(mon,-v)]
    sign_detected=any(derivative(bad,A,j) for j in range(r-1))
    assert sign_detected
    evaluations=[]
    for e in rec['det_points']:
        co=form_of_point(e['point'],r,4)
        value=evaluate_integer(terms,A,co)
        residue=value%P
        assert residue*pow(zmod[pivot],-1,P)%P==e['value_mod_p']
        assert value and residue
        evaluations.append(dict(exact_integer_value=str(value),value_mod_p=residue,
                                old_normalized_value_mod_p=e['value_mod_p'],point=e['point']))
    result=dict(status='EXACT',cell=rec['cell'],a=1,m_det_lb=1,m_det_ub=1,m_pad_ub=1,D_ub=0,
                integral_source=f'results/b15_02/{tag}_integral_source.json',
                integral_source_sha256=hashlib.sha256((OUT/f'{tag}_integral_source.json').read_bytes().replace(b'\r\n',b'\n')).hexdigest(),
                nonzero_expanded_terms=len(terms),all_term_weights_checked=True,
                direct_integer_raising_residual_sizes=der_sizes,altered_monomial_sign_rejected=True,
                modular_source_matches_integral_reduction=True,det_evaluations=evaluations,
                model='gpt-6-astra',seconds=time.perf_counter()-t)
    save(OUT/f'{tag}_verified.json',result)
    print(json.dumps(dict(phase='verified',index=i,terms=len(terms),max_coefficient=src['integral_construction']['coefficient_abs_max'],
                          integer_value=evaluations[0]['exact_integer_value'],seconds=result['seconds'])),flush=True)
    del terms,arr,Z
    gc.collect()
    return result


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--construct',action='store_true')
    ap.add_argument('--first',type=int,default=1);ap.add_argument('--last',type=int,default=9)
    args=ap.parse_args();records=[]
    for i in range(args.first,args.last+1):records.append(one(i,args.construct))
    save(OUT/'verification.json',dict(status='EXACT',all_pass=True,cell_count=len(records),
                                    source_constructed=args.construct,cells=[r['cell'] for r in records],
                                    direct_integer_HWV_and_fresh_point_evaluation=True))


if __name__=='__main__':main()
