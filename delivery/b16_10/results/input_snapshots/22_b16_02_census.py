"""B16-02 finite ambient census via a proved finite-stability criterion.

Run with -B through inspected analysis/b15_bound.py, at one process/thread.
Rational power-sum recurrence follows B14-04 / B15-06; the finite hook
identity and its application here are fresh. No geometric source is built.
"""
import argparse
from collections import defaultdict
from fractions import Fraction as Q
from functools import lru_cache
import gzip
import hashlib
import json
from math import factorial
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'results/b16_02'
PROJECT = ROOT.parents[2]
sys.path.insert(0, str(ROOT / 'analysis'))
from wk8_s30_pleth import parts, zr, chi, pleth_p

CELLS = [(23, 15, 1, 158), (25, 17, 2, 218),
         (26, 17, 2, 218), (27, 19, 5, 288)]


def save(name, value):
    OUT.mkdir(parents=True, exist_ok=True)
    raw = (json.dumps(value, sort_keys=True, separators=(',', ':')) + '\n').encode()
    if name.endswith('.gz'):
        raw = gzip.compress(raw, mtime=0)
    (OUT / name).write_bytes(raw)


def read(name):
    raw = (OUT / name).read_bytes()
    if name.endswith('.gz'):
        raw = gzip.decompress(raw)
    return json.loads(raw)


def mul(A, B):
    out = defaultdict(Q)
    for rho, a in A.items():
        for sigma, b in B.items():
            out[tuple(sorted(rho + sigma, reverse=True))] += a * b
    return {rho: a for rho, a in out.items() if a}


def logs(nmax):
    L = [defaultdict(Q) for _ in range(nmax + 1)]
    for j in (2, 3, 4):
        for k in range(1, nmax // j + 1):
            for rho in parts(j):
                L[j * k][tuple(k * x for x in rho)] += Q(j, zr(rho))
    return L


def series(nmax, progress=False):
    L = logs(nmax)
    F = [{(): Q(1)}]
    for n in range(1, nmax + 1):
        row = defaultdict(Q)
        for m in range(1, n + 1):
            for rho, a in L[m].items():
                for sigma, b in F[n-m].items():
                    row[tuple(sorted(rho + sigma, reverse=True))] += a * b
        F.append({rho: a/n for rho, a in row.items() if a})
        if progress and n % 5 == 0:
            print(json.dumps({'weight_completed': n, 'terms': len(F[-1])}), flush=True)
    return F


def scalar(P, lam, character=chi):
    result = sum((a * character(lam, rho) for rho, a in P.items()), Q())
    assert result.denominator == 1
    return int(result)


def finite_branching(d, tail):
    """Small-control direct GL1 branching with the missing first-row roots.

    Sum e_k (-1)^k Sym^{n1}V Sym^{n2}Sym2V ...,
    n1+2n2+3n3+4n4 = |tail|-k, n1+n2+n3+n4 <= d.
    """
    n = sum(tail)
    P = defaultdict(Q)
    for k in range(min(len(tail), n) + 1):
        E = {rho: Q((-1)**(k-len(rho)), zr(rho)) for rho in parts(k)}
        for n4 in range((n-k)//4 + 1):
            for n3 in range((n-k-4*n4)//3 + 1):
                for n2 in range((n-k-4*n4-3*n3)//2 + 1):
                    n1 = n-k-4*n4-3*n3-2*n2
                    if n1+n2+n3+n4 > d:
                        continue
                    term = E
                    for deg, number in ((1,n1),(2,n2),(3,n3),(4,n4)):
                        term = mul(term, pleth_p(number, deg))
                    for rho, a in term.items():
                        P[rho] += (-1)**k * a
    return scalar(P, tail)


def controls():
    F = series(10)
    direct = []
    for d in range(1, 5):
        P = pleth_p(d, 4)
        for lam in parts(4*d):
            if len(lam)>4 or sum(lam[1:])>8:
                continue
            tail = lam[1:]
            actual = scalar(P, lam)
            branch = finite_branching(d, tail)
            assert actual == branch, (d,lam,actual,branch)
            stable = scalar(F[sum(tail)], tail)
            bound = not tail or 2*d-sum(tail)+2 > tail[0]
            if bound:
                assert actual == stable, (d,lam,actual,stable)
            direct.append({'d':d, 'lambda':lam, 'a':actual, 'a_inf':stable,
                           'finite_branching':branch, 'criterion':bound})
    # Verify the hook truncation identity in the symmetric-function ring.
    hooks = []
    for L in range(1, 9):
        for D in range(L):
            P = defaultdict(Q)
            s = L-D
            for k in range(s, L+1):
                E = {rho: Q((-1)**(k-len(rho)),zr(rho)) for rho in parts(k)}
                for rho, a in mul(E, pleth_p(L-k,1)).items():
                    P[rho] += (-1)**k*a
            shape = (D+1,)+(1,)*(s-1)
            for rho in parts(L):
                assert P[rho] == Q((-1)**s*chi(shape,rho), zr(rho))
            hooks.append([L,D,shape])
    # A lower degree outside the bound genuinely fails: Sym^2(Sym4).
    assert scalar(pleth_p(2,4),(4,2,2)) == 0
    assert scalar(F[4],(2,2)) == 1
    result = {'status':'PASS','direct_plethysm_and_branching_rows':direct,
              'hook_identity_rows':hooks,
              'outside_bound_control':{'d':2,'lambda':[4,2,2],'finite':0,'stable':1},
              'method':'exact Fraction power sums; independent direct h_d[h_4] small expansion'}
    save('controls.json', result)
    print(json.dumps({'controls':'PASS','finite_rows':len(direct),'hook_rows':len(hooks)}))


def sizing():
    # Counts only: no production symmetric-function or weight carrier allocation.
    p = [len(parts(n)) for n in range(36)]
    L = logs(35)
    operations = sum(len(L[m])*p[n-m] for n in range(1,36) for m in range(1,n+1))
    corrections = []
    for d,t,q,h in CELLS:
        n=t+16
        rows=[]
        for b in range(n//2+1):
            for m in range(2*b,min(4*b,n)+1):
                if n-m>d-b and b<=d:
                    rows.append({'b':b,'m':m,'L':n-m,'D':d-b,
                                 'hook':[d-b+1]+[1]*(n-m-d+b-1),
                                 'excluded_by_first_row':d-b+1>t})
        assert all(row['excluded_by_first_row'] for row in rows)
        corrections.append({'d':d,'tail':[t]+[2]*8,'n':n,
                            'first_row_lower_bound':2*d-n+2,
                            'all_correction_carriers':rows})
    record={'status':'EXACT_SIZE_PREFLIGHT','partition_counts':p,
            'all_series_partition_storage_upper_bound':sum(p),
            'max_single_series_support':max(p),
            'recurrence_multiply_add_upper_bound':operations,
            'storage_estimate_at_2048_bytes_per_partition':2048*sum(p),
            'storage_estimate_is_not_rigorous_memory_bound':True,
            'max_character_cache_entries':180000,
            'pilot_cap_seconds':60,'pilot_cap_memory_mib':512,
            'finite_hook_exclusions':corrections,
            'no_full_degree_108_power_sum_or_dense_weight_expansion':True}
    save('sizing.json',record)
    print(json.dumps({k:v for k,v in record.items() if k!='finite_hook_exclusions'}))


def census():
    assert read('controls.json')['status']=='PASS'
    assert read('sizing.json')['status']=='EXACT_SIZE_PREFLIGHT'
    start=time.perf_counter()
    F=series(35, progress=True)
    complete=[]
    for t in (15,17,19):
        tail=(t,)+(2,)*8
        rows=[]
        subtotals=defaultdict(Q)
        for rho,a in sorted(F[t+16].items(),reverse=True):
            char=chi(tail,rho)
            rows.append([rho,a.numerator,a.denominator,char])
            subtotals[rho[0]]+=a*char
            if chi.cache_info().currsize>180000:
                chi.cache_clear()
        value=sum(subtotals.values(),Q())
        assert value.denominator==1 and value>=0
        cert={'status':'EXACT','tail':tail,'weighted_degree':t+16,
              'generator_degrees':[2,3,4],'a_inf':int(value),
              'coefficient_convention':'[p_rho] F_n, not multiplied by z_rho',
              'rows_rho_numerator_denominator_character':rows,
              'signed_subtotals':[[k,a.numerator,a.denominator] for k,a in sorted(subtotals.items())]}
        save(f'count_t{t}.json.gz',cert)
        complete.append({'t':t,'a_inf':int(value),'terms':len(rows)})
        print(json.dumps(complete[-1]),flush=True)
        chi.cache_clear()
    records=[]
    for d,t,q,h in CELLS:
        n=t+16
        a=next(row['a_inf'] for row in complete if row['t']==t)
        assert 2*d-n+2>t
        records.append({'degree':d,'lambda':[4*d-n,t]+[2]*8,'tail_size':n,
                        'a':a,'finite_equals_stable':True,
                        'given_global_det_floor':q,'source_ceiling':h,
                        'inherited_full_det_ideal_upper':11,
                        'padded_ideal_lower':a-h,'D_upper':11+h-a,
                        'r_needed_with_given_q':a-q+1,
                        'r_needed_even_at_q11':a-10,
                        'q_needed_if_r_reached_source_ceiling':a-h+1,
                        'exclusion':'full determinant ideal upper <= padded ideal lower'})
    result={'status':'EXACT_FINITE_AMBIENT_AND_CONDITIONAL_EXCLUSIONS','rows':records,
            'counts':complete,'seconds':time.perf_counter()-start,
            'fresh':['finite hook criterion','finite ambient equality','exact rational counts','exclusion arithmetic'],
            'inherited':['B15-06 stable det floor418 in ambient429','S57 ideal filtration',
                         'same-row s2 multiplication injection','Dream padding source ceilings',
                         'Hessian11 global equation floors'],
            'geometric_ranks_recomputed':False}
    save('census.json',result)
    print(json.dumps(result),flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('mode',choices=['controls','sizing','census'])
    args=parser.parse_args()
    globals()[args.mode]()
