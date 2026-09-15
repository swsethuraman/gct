"""Bounded exact character pilot for the separated-cubic enlargement.

Numerical output is a source-module upper bound, not a padding rank.
Attribution: Murnaghan--Nakayama/partition helpers are the inspected retained
wk8_s30_pleth.py; exponential recurrence follows retained B14-04 recount.py.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
from math import factorial
import gzip
import hashlib
import importlib.util
import json
import os
import time

HERE = Path(__file__).resolve().parent
ROOT = Path(r'C:\Users\swami\Projects\gct-gpt')
SOURCE = ROOT/'work/batch15_workers/B15-06/analysis/wk8_s30_pleth.py'
spec = importlib.util.spec_from_file_location('retained_s30', SOURCE)
R = importlib.util.module_from_spec(spec)
spec.loader.exec_module(R)

def check_time():
    if time.monotonic()+2 > float(os.environ['CI73_DEADLINE']):
        raise RuntimeError('Stop before wrapper deadline; count is incomplete')

def logs(nmax):
    L = [defaultdict(Q) for _ in range(nmax+1)]
    for d in (2,3):
        for r in range(1,nmax//d+1):
            for rho in R.parts(d):
                L[d*r][tuple(r*v for v in rho)] += Q(d,R.zr(rho))
    return L

def main():
    start = time.monotonic()
    source_hash = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    nmax = 33
    L = logs(nmax)
    sizes = [len(R.parts(n)) for n in range(nmax+1)]
    ops = sum(len(L[m])*sizes[n-m] for n in range(1,nmax+1) for m in range(1,n+1))
    preflight = {'max_weight':nmax,'partition_counts':sizes,
                 'recurrence_pair_upper_bound':ops,
                 'storage_estimate_bytes_2048_per_partition':2048*sum(sizes),
                 'storage_is_estimate_not_bound':True,
                 'character_cache_clear_threshold':100000,
                 'numerical_processes':1,'hard_wall_seconds':60,'hard_memory_MiB':512}
    (HERE/'cubic_preflight.json').write_text(json.dumps(preflight,indent=2)+'\n')
    assert ops < 3000000 and 2048*sum(sizes) < 200*1024**2
    print('PREFLIGHT',json.dumps(preflight),flush=True)
    F = [{():Q(1)}]
    for n in range(1,nmax+1):
        check_time()
        row = defaultdict(Q)
        for m in range(1,n+1):
            for x,a in L[m].items():
                for y,b in F[n-m].items():
                    row[tuple(sorted(x+y,reverse=True))] += a*b
        F.append({x:a/n for x,a in row.items() if a})
    # Direct low-weight products check a separate expression for the series.
    for n in range(10):
        direct = defaultdict(Q)
        for a in range(n//2+1):
            if (n-2*a)%3: continue
            b = (n-2*a)//3
            for x,c in R.pleth_p(a,2).items():
                for y,d in R.pleth_p(b,3).items():
                    direct[tuple(sorted(x+y,reverse=True))] += c*d
        assert dict(direct) == F[n]
    # Complete character orthogonality through S5, independent of target values.
    for n in range(1,6):
        for lam in R.parts(n):
            for mu in R.parts(n):
                assert sum(Q(R.chi(lam,rho)*R.chi(mu,rho),R.zr(rho))
                           for rho in R.parts(n)) == int(lam==mu)
    rows=[]
    for b in range(2,20):
        check_time()
        beta=(b,)+(2,)*7
        terms=[]
        v=Q(0)
        for rho,c in sorted(F[sum(beta)].items(),reverse=True):
            char=R.chi(beta,rho)
            v += c*char
            terms.append([rho,c.numerator,c.denominator,char])
            if R.chi.cache_info().currsize>100000:
                R.chi.cache_clear()
        assert v.denominator == 1 and v >= 0
        row={'b':b,'tail':beta,'stable_cubic_upper':int(v),'terms':len(terms)}
        rows.append(row)
        data={'row':row,'generator_degrees':[2,3],
              'power_sum_numerator_denominator_character_rows':terms}
        (HERE/f'cubic_tail_{b}.json.gz').write_bytes(gzip.compress(
            (json.dumps(data,separators=(',',':'))+'\n').encode(),mtime=0))
        print('CUBIC',b,int(v),flush=True)
        R.chi.cache_clear()
    sums={str(t):sum(r['stable_cubic_upper'] for r in rows if r['b']<=t) for t in (15,17,19)}
    output={'status':'EXACT_CHARACTER_SUMS_SOURCE_UPPER_ONLY','rows':rows,
            'sum_b_2_through_t':sums,
            'candidate_cells':[{'d':d,'t':t,'lambda':[4*d-t-16,t]+[2]*8,
                                'source_upper':sums[str(t)]} for d,t in ((23,15),(25,17),(27,19),(35,19))],
            'source_path':str(SOURCE),'source_sha256':source_hash,
            'controls':'series direct product through weight9; complete character orthogonality through S5',
            'wall_seconds':time.monotonic()-start,
            'unproved_by_computation':'geometric ring maps and cubic highest-weight chart injection require the report proof'}
    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()==source_hash
    (HERE/'cubic_bound.json').write_text(json.dumps(output,indent=2)+'\n')
    print('SOURCE_UPPER_SUMS',json.dumps(sums),flush=True)

if __name__=='__main__': main()

