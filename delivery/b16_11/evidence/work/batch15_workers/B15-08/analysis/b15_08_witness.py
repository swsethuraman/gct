"""Replay the two-point analytic witness; small modes need no heavy carrier.

The native launch must obtain its integrator's resource ruling before executing
the h=8 mode. This script does not grant or update any host lease.
"""
import argparse
from itertools import combinations_with_replacement
import json
from math import factorial
from pathlib import Path
import time

from b15_08_bracket import brute,det,point_json,rank,value

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'results/b15_08'
PRIMES=(2147483647,2147483629)


def make(h):
    P={d:{idx:0 for idx in combinations_with_replacement(range(h),d)} for d in (2,3,4)}
    Q={d:dict(T) for d,T in P.items()}
    for i in range(h):P[2][(i,i)]=Q[2][(i,i)]=1
    P[3][(1,1,1)]=1;Q[3][(0,0,0)]=1;Q[4][(0,1,1,1)]=1
    B=((2,3),)*(h-1)+((2,4),(3,7))
    H=((2,3),)*(h-2)+((3,7),(4,7))
    return (B,H),(P,Q)


def run(hs,name):
    start=time.perf_counter();records=[]
    for h in hs:
        bs,pts=make(h);expected=[[factorial(h-1),0],[0,factorial(h-2)]]
        t0=time.perf_counter()
        matrix=[[value(b,pt,h) for pt in pts] for b in bs]
        eval_seconds=time.perf_counter()-t0
        assert matrix==expected
        if h<=3:
            assert [[brute(b,pt,h) for pt in pts] for b in bs]==matrix
        witness=det(matrix);assert witness==factorial(h-1)*factorial(h-2)
        ranks=[]
        for p in PRIMES:
            m=[[value(b,pt,h,p) for pt in pts] for b in bs]
            assert m==[[x%p for x in row] for row in matrix]
            ranks.append(rank(m,p));assert ranks[-1]==2
        record=dict(status='EXACT',h=h,tail=[4,3]+[2]*(h-2),sources=bs,
                    points=[point_json(pt) for pt in pts],integer_matrix=matrix,
                    integer_determinant=witness,prime_ranks=ranks,primes=PRIMES,
                    integer_evaluation_seconds=eval_seconds)
        if h==8:
            import sys
            sys.path.insert(0,str(ROOT/'analysis/b14_04'))
            from recount import exp_series,scalar
            from wk8_s30_pleth import chi
            F=exp_series(19)[19];tail=tuple(record['tail']);a=scalar(F,tail)
            assert a==2
            record.update(a_inf_lb=a,a_inf_ub=a,generic_rank_lb=2,
                          character_certificate=[[rho,c.numerator,c.denominator,chi(tail,rho)]
                                                 for rho,c in sorted(F.items())])
        records.append(record)
        print('analytic witness',h,matrix,'integer det',witness,flush=True)
    result=dict(status='EXACT',records=records,seconds=time.perf_counter()-start,
                fresh_integer_and_modular_evaluation=True,model='gpt-6-astra')
    OUT.mkdir(exist_ok=True)
    (OUT/name).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['small','full','replay'])
    args=ap.parse_args()
    if args.mode=='small':run([2,3],'analytic_small.json')
    else:run([8],'analytic_fullheight.json' if args.mode=='full' else 'analytic_replay.json')
