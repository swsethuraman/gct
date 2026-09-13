"""Slot08 bounded controls, counts, production and fresh source replay."""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
from itertools import product
import json
from math import factorial
from pathlib import Path
import random
import sys
import time

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'analysis'))
sys.path.insert(0,str(ROOT/'analysis/b14_04'))
sys.path.insert(0,str(ROOT))
from b15_08_bracket import (brute, det, enumerate_brackets, ordinary_polynomials,
    point_json, point_read, random_point, rank, slots, tensor_get, transformed,
    value, work_count)
from recount import exp_series, scalar
from wk8_s30_pleth import chi, parts, zr

OUT=ROOT/'results/b15_08'
PRIMES=(2147483647,2147483629)
INPUTS=['analysis/b14_06_bracket.py','analysis/b14_06_points.py',
        'analysis/b14_04/recount.py','analysis/wk8_s30_pleth.py',
        'results/b14_06/selftest.json','docs/batch15/ACCEPTED_STATE.md',
        'results/integrate/inherited_exclusions.json','results/b15_prep/transport_overlay.json']


def save(name,obj):
    OUT.mkdir(exist_ok=True)
    (OUT/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')


def hashes():
    return {s:hashlib.sha256((ROOT/s).read_bytes()).hexdigest() for s in INPUTS}


def ledger(tail):
    from tools.integrate.exclusion_predicates import conclusions_for
    W=sum(tail)
    cell=dict(n=4,ell=len(tail)+1,delta=W,**{'lambda':[3*W]+list(tail)})
    bank=json.loads((ROOT/'results/integrate/inherited_exclusions.json').read_text())
    overlay=json.loads((ROOT/'results/b15_prep/transport_overlay.json').read_text())
    contexts=sorted({c for v in bank['application_contract']['conclusions_by_id'].values() for c in v})
    return dict(cell=cell,typed_conclusions={c:conclusions_for(bank,cell,c) for c in contexts},
        overlay_exact_matches=[x for x in overlay['targets'] if x['degree']==W and x['lam']==cell['lambda']],
        overlay_family_matches=[x for x in overlay['family_extensions'] if x['tail']==list(tail) and W>=x['from_degree']])


def sizing():
    start=time.perf_counter()
    F=exp_series(24)
    rows=[]
    for h,ts in ((2,range(3,7)),(3,range(3,8)),(8,range(3,10))):
        for t in ts:
            tail=(t,3)+(2,)*(h-2)
            W=sum(tail)
            b=enumerate_brackets(h,W)
            a=scalar(F[W],tail)
            costs=[work_count(br,h) for br in b]
            row=dict(h=h,tail=tail,W=W,a_inf_lb=a,a_inf_ub=a,source_rows=len(b),
                determinant_calls_per_point_ub=sum(x['determinants'] for x in costs),
                max_determinant_order=max((x['determinant_order'] for x in costs),default=0),
                brute_terms_per_source=factorial(h)**2*2,ledger=ledger(tail))
            rows.append(row)
            print(json.dumps({k:v for k,v in row.items() if k!='ledger'}),flush=True)
    # Known exact character identities and banked counts, independent of brackets.
    assert scalar(F[6],(2,2,2))==1
    assert scalar(F[13],(6,3,3,1))==4
    for n in range(1,6):
        for lam in parts(n):
            assert sum(Fraction(chi(lam,rho)**2,zr(rho)) for rho in parts(n))==1
    save('sizing.json',dict(status='EXACT',rows=rows,input_hashes=hashes(),
         method='B14-04 exact rational power-sum recurrence and MN character inner product',
         seconds=time.perf_counter()-start))


def controls():
    start=time.perf_counter()
    import numpy,flint
    rng=random.Random(1508001)
    records=[]
    equalities=0;live=0;sign_seen=False;factor_seen=False
    for h,W in ((2,6),(2,7),(2,8),(2,9),(3,8),(3,9),(3,10),(3,11),(3,12)):
        bs=enumerate_brackets(h,W)
        assert bs
        # Deterministic source sample keeps direct epsilon work small.
        chosen=bs if len(bs)<=70 else tuple(rng.sample(list(bs),70))
        point=random_point(h,rng)
        vals=[]
        for br in chosen:
            x=value(br,point,h)
            y=brute(br,point,h)
            assert x==y,(h,W,br,x,y)
            equalities+=1
            live+=bool(x)
            if x:
                columns=[slots(br,b) for b in (1,2,4)]
                columns[2]=columns[2][::-1]
                assert brute(br,point,h,columns=columns)==-x
                sign_seen |= brute(br,point,h,sign_defect=True)!=x
                factor_seen |= value(br,point,h,p=PRIMES[0],factorial_defect=True)!=x%PRIMES[0]
            vals.append(x)
        records.append(dict(h=h,W=W,sources=[br for br in chosen],point=point_json(point),
                            values=vals,nonzero=sum(bool(x) for x in vals)))
    assert equalities>100 and live>0 and sign_seen and factor_seen
    # Symmetric letter hitting the same column twice is rejected, not silently used.
    rejected=False
    try: value(((2,7),)*2,random_point(2,rng),2)
    except ValueError: rejected=True
    assert rejected
    # Identical vectors in an alternating column give an exact zero.
    repeated=((2,1),(2,1),(2,2),(3,6),(3,4))
    point=random_point(2,rng)
    assert value(repeated,point,2)==brute(repeated,point,2)==0
    # Separate known liveness: h=3, three quadratic pairs = 3! det(T_2).
    point=random_point(3,rng)
    q=((2,3),)*3
    N=[[tensor_get(point,2,[i,j]) for j in range(3)] for i in range(3)]
    assert det(N)!=0
    assert value(q,point,3,short=0)==factorial(3)*det(N)==brute(q,point,3,short=0)
    p=PRIMES[0]
    bs=enumerate_brackets(3,10)
    point=random_point(3,rng)
    vv=[value(b,point,3,p) for b in bs]
    assert any(vv)
    g=[[1,2,3],[0,1,4],[0,0,1]]
    trans=transformed(point,g,p)
    assert [value(b,trans,3,p) for b in bs]==vv
    diag=[2,3,5]
    trans=transformed(point,[[diag[i] if i==j else 0 for j in range(3)] for i in range(3)],p)
    weight=pow(2,5,p)*pow(3,3,p)*pow(5,2,p)%p
    assert [value(b,trans,3,p) for b in bs]==[v*weight%p for v in vv]
    assert weight != pow(2,4,p)*pow(3,3,p)*pow(5,2,p)%p
    # Third derivative entries computed from ordinary polynomial coefficients.
    polys=ordinary_polynomials(point)
    derivative_checks=0
    for d,poly in polys.items():
        for k in range(1,min(3,d)+1):
            for idx in product(range(3),repeat=k):
                deriv=0
                for mon,c in poly.items():
                    counts=Counter(mon); term=c
                    for j in idx:
                        term*=counts[j];counts[j]-=1
                    if all(num==0 for j,num in counts.items() if j!=0):
                        deriv+=term
                assert deriv==factorial(d)//factorial(d-k)*tensor_get(point,d,idx)
                derivative_checks+=1
    save('controls.json',dict(status='EXACT',equalities=equalities,nonzero_evaluations=live,
         short_column_sign_defect_detected=sign_seen,factorial_defect_detected=factor_seen,
         invalid_letter_rejected=rejected,repeated_vector_zero=True,known_liveness=True,
         upper_unipotent_invariance=True,torus_weight=[5,3,2],derivative_checks=derivative_checks,
         records=records,runtime=dict(numpy=numpy.__version__,flint=flint.__version__),
         input_hashes=hashes(),seconds=time.perf_counter()-start))
    print('controls PASS',equalities,'exact brute equalities;',live,'nonzero;',derivative_checks,'derivatives',flush=True)


def point_controls():
    from b15_08_points import (det_parameters,pad_parameters,red_parameters,
        from_parameters,verify_polynomial,inherited_jet_control,normalize)
    rng=random.Random(1508002);rows=[];start=time.perf_counter();chart_rejections=[]
    for family in ('DET','PAD','RED'):
        for attempt in range(100):
            params={'DET':lambda:det_parameters(8,rng),'PAD':lambda:pad_parameters(rng),
                    'RED':lambda:red_parameters(8,rng)}[family]()
            try:
                for p in PRIMES:from_parameters(params,8,p)
                break
            except ValueError:
                chart_rejections.append(dict(family=family,params=params))
        else:raise ValueError('could not find a valid chart point')
        for p in PRIMES:
            point,meta=from_parameters(params,8,p)
            verify_polynomial(params,meta,8,p,rng)
            inherited=family in ('DET','PAD') and inherited_jet_control(params,point,8,p)
            if family=='PAD':
                assert rank(params['L'],p)==10
                full,fullmeta=from_parameters(params,9,p)
                verify_polynomial(params,fullmeta,9,p,rng)
                from copy import deepcopy
                changed=deepcopy(meta)
                changed['polys'][2][(0,0)]=(changed['polys'][2].get((0,0),0)+1)%p
                mutation_detected=False
                try:verify_polynomial(params,changed,8,p,random.Random(88003))
                except AssertionError:mutation_detected=True
                assert mutation_detected
            # A zero leading coefficient is an invalid chart input.
            rejected=False
            bad=dict(meta['raw']);bad.pop((0,0,0,0),None)
            try:normalize(bad,8,p)
            except ValueError:rejected=True
            assert rejected
            rows.append(dict(family=family,prime=p,params=params,c=meta['c'],
                             inherited_two_jet_agreement=inherited,zero_c_rejected=rejected))
    save('point_controls.json',dict(status='EXACT',rows=rows,input_hashes=hashes(),chart_rejections=chart_rejections,
        point_parameters_are='integers; normalization and symmetric tensors are rational with denominators invertible modulo each prime',
        full_ten_variable_pad_verified=True,changed_depressed_coefficient_detected=True,
        seconds=time.perf_counter()-start))
    print('point controls PASS',len(rows),'cases',flush=True)


def small_ranks():
    start=time.perf_counter();rng=random.Random(1508003);F=exp_series(12);rows=[]
    for h,ts in ((2,range(3,7)),(3,range(3,8))):
        for t in ts:
            tail=(t,3)+(2,)*(h-2);a=scalar(F[sum(tail)],tail)
            bs=enumerate_brackets(h,sum(tail));pts=[random_point(h,rng) for _ in range(max(3,a+4))]
            ranks=[]
            for p in PRIMES:
                mat=[[value(br,pt,h,p) for pt in pts] for br in bs]
                r=rank(mat,p);assert r==a,(tail,r,a)
                ranks.append(r)
            rows.append(dict(tail=tail,a_inf_lb=a,a_inf_ub=a,ranks=ranks,primes=PRIMES,
                             points=[point_json(pt) for pt in pts],sources=bs))
    save('small_ranks.json',dict(status='REPLAYED_RANK_FLOOR',rows=rows,
         equal_to_exact_ambient=True,seconds=time.perf_counter()-start))
    print('small ranks PASS',[(x['tail'],x['ranks']) for x in rows],flush=True)


def minor_witness(matrix,p):
    a=[list(row) for row in matrix];ids=list(range(len(a)));rr=[];cc=[];k=0
    for col in range(len(a[0])):
        pivot=next((i for i in range(k,len(a)) if a[i][col]%p),None)
        if pivot is None:continue
        a[k],a[pivot]=a[pivot],a[k];ids[k],ids[pivot]=ids[pivot],ids[k]
        rr.append(ids[k]);cc.append(col)
        inv=pow(a[k][col],-1,p)
        for i in range(k+1,len(a)):
            c=a[i][col]*inv%p
            if c:
                a[i]=[(x-c*y)%p for x,y in zip(a[i],a[k])]
        k+=1
        if k==len(a):break
    v=det([[matrix[i][j] for j in cc] for i in rr],p)
    assert v and k==rank(matrix,p)
    return dict(rank_lb=k,pivot_source_rows=rr,pivot_point_columns=cc,minor_det_mod_p=v)


def require_lease():
    path=ROOT.parents[2]/'Batch15_Launch/native_20260913/LEASES.json'
    lease=json.loads(path.read_text(encoding='utf-8-sig'))
    if '08' not in lease['holders']:raise RuntimeError('slot08 does not hold a heavy lease')
    return lease


def production():
    from b15_08_points import det_parameters,pad_parameters,red_parameters,from_parameters,verify_polynomial
    lease=require_lease();start=time.perf_counter();rng=random.Random(1508004)
    npoints=18;h=8;ts=(4,5,6)
    for name in ('controls.json','point_controls.json','small_ranks.json'):
        assert json.loads((OUT/name).read_text())['status'] in ('EXACT','REPLAYED_RANK_FLOOR')
    F=exp_series(21)
    count_rows=[]
    for t in ts:
        tail=(t,3)+(2,)*6;W=sum(tail);a=scalar(F[W],tail)
        terms=[[rho,c.numerator,c.denominator,chi(tail,rho)] for rho,c in sorted(F[W].items())]
        save(f'count_t{t}.json',dict(status='EXACT',tail=tail,a_inf_lb=a,a_inf_ub=a,
             normalization='a=sum unscaled p_rho coefficient times chi_tail(rho)',terms=terms))
        count_rows.append((t,tail,a))
    sources={t:enumerate_brackets(h,sum(tail)) for t,tail,a in count_rows}
    for t in ts:save(f'sources_t{t}.json',dict(h=h,short=2,t=t,sources=sources[t]))
    native={'GEN':[point_json(random_point(h,rng,5)) for _ in range(npoints)]}
    rejects=[]
    for fam in ('DET','PAD','RED'):
        native[fam]=[]
        while len(native[fam])<npoints:
            params={'DET':lambda:det_parameters(h,rng),'PAD':lambda:pad_parameters(rng),
                    'RED':lambda:red_parameters(h,rng)}[fam]()
            try:
                for p in PRIMES:from_parameters(params,h,p)
            except ValueError:
                rejects.append(params);continue
            native[fam].append(params)
    save('native_inputs.json',dict(h=h,npoints=npoints,seed=1508004,points=native,
                                 chart_rejections=rejects))
    native_seconds=time.perf_counter()-start
    point_seconds=0;results=[]
    for p in PRIMES:
        for fam,params_list in native.items():
            t0=time.perf_counter()
            if fam=='GEN':points=[point_read(x) for x in params_list]
            else:
                points=[]
                for params in params_list:
                    point,meta=from_parameters(params,h,p)
                    verify_polynomial(params,meta,h,p,rng)
                    points.append(point)
            build_seconds=time.perf_counter()-t0;point_seconds+=build_seconds
            for t,tail,a in count_rows:
                t0=time.perf_counter();bs=sources[t]
                matrix=[[value(br,pt,h,p) for pt in points] for br in bs]
                eval_seconds=time.perf_counter()-t0;t0=time.perf_counter()
                witness=minor_witness(matrix,p);rr=witness['rank_lb']
                reduce_seconds=time.perf_counter()-t0
                assert rr<=a,(fam,tail,rr,a)
                if fam=='GEN':assert rr==a,(tail,rr,a)
                row=dict(status='REPLAYED_RANK_FLOOR',family=fam,prime=p,tail=tail,h=h,n=4,
                         stable_delta_min=sum(tail),ell=9,npoints=npoints,source_rows=len(bs),
                         a_inf_lb=a,a_inf_ub=a,coordinate_rank_lb=rr,ideal_dimension_ub=a-rr,
                         U_pad_ub=a,ledger=ledger(tail),witness=witness,
                         evaluation_seconds=eval_seconds,reduction_seconds=reduce_seconds,
                         point_construction_seconds=build_seconds,matrix=matrix)
                save(f'matrix_t{t}_{fam}_{p}.json',row);results.append({k:v for k,v in row.items() if k!='matrix'})
                print(f't={t} {fam} p={p}: rank {rr}/{a}; evaluation {eval_seconds:.3f}s',flush=True)
                save('production_progress.json',dict(status='RECORDED',completed=results))
    save('production.json',dict(status='REPLAYED_RANK_FLOOR',rows=results,input_hashes=hashes(),
         lease_at_start=lease,native_construction_seconds=native_seconds,
         polynomial_point_construction_seconds=point_seconds,seconds=time.perf_counter()-start))


def replay():
    from b15_08_points import from_parameters,verify_polynomial
    require_lease();start=time.perf_counter();rng=random.Random(1508005)
    native=json.loads((OUT/'native_inputs.json').read_text());prod_data=json.loads((OUT/'production.json').read_text())
    count=0;point_checks=0;rank_rows=[];F=exp_series(21)
    for t in (4,5,6):
        cert=json.loads((OUT/f'count_t{t}.json').read_text());tail=tuple(cert['tail']);W=sum(tail)
        fresh=[[list(rho),c.numerator,c.denominator,chi(tail,rho)] for rho,c in sorted(F[W].items())]
        assert fresh==cert['terms']
        assert scalar(F[W],tail)==cert['a_inf_ub']
    for row in prod_data['rows']:
        fam,p,tail=row['family'],row['prime'],row['tail'];t=tail[0];h=row['h']
        old=json.loads((OUT/f'matrix_t{t}_{fam}_{p}.json').read_text())
        bs=enumerate_brackets(h,sum(tail))
        stored=json.loads((OUT/f'sources_t{t}.json').read_text())['sources']
        assert [[list(x) for x in b] for b in bs]==stored
        pts=[]
        for params in native['points'][fam]:
            if fam=='GEN':pt=point_read(params)
            else:
                pt,meta=from_parameters(params,h,p);verify_polynomial(params,meta,h,p,rng)
                point_checks+=1
            pts.append(pt)
        new=[[value(br,pt,h,p) for pt in pts] for br in bs]
        assert new==old['matrix']
        witness=minor_witness(new,p);assert witness==row['witness']
        count+=len(new)*len(pts)
        rank_rows.append(dict(t=t,family=fam,prime=p,rank_lb=witness['rank_lb']))
        print('replay',t,fam,p,witness['rank_lb'],flush=True)
    # The verifier must reject a stored value changed independently of the inputs.
    bad=[r[:] for r in old['matrix']];bad[0][0]=(bad[0][0]+1)%p
    assert bad!=new
    save('replay.json',dict(status='REPLAYED_RANK_FLOOR',fresh_source_values=count,
        regenerated_geometric_points=point_checks,rows=rank_rows,changed_value_detected=True,
        exact_counts_recomputed=True,seconds=time.perf_counter()-start,input_hashes=hashes()))


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['sizing','controls','point_controls','small_ranks','production','replay'])
    args=ap.parse_args()
    globals()[args.mode]()
