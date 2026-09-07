#!/usr/bin/env python3
"""
P0-A (integrator, batch 11) -- mult_{per_3} at the n = 3 member of the LMR family.

Cell  lambda = (19,7,2^5), delta = 12, n = 3, r = 7, a = 6.  Session 63 measured
i_det = 1 (mult_det = 5) there with the sparse-Wiedemann instrument

    i_X = nullity_p [E ; ev_X],   mult_X = a - i_X.

This script runs the SAME instrument with ev_per (per_3) alongside ev_det, so the
two numbers are produced by one engine on one build and are directly comparable.

Note this is the UNPADDED (3,3) comparison, not the programme's padded model:

    ambient Sym^3(C^7)              dim 84
    det_3 cubics in 7 variables     9r - 16 = 47
    per_3 cubics in 7 variables     9r -  4 = 59

so the determinant variety is the smaller one and D = i_det - i_per is
favourably directed here, unlike the padded n = 3 cell, where per_2 = det_2 up to
GL forces P subset D and D <= 0 (docs/stocktake_batch10.md 6).

    mult_per = 6  =>  i_per = 0  =>  D = +1.

Only the positive branch is rigorous: rank_p <= rank_Q <= a, so a measured
i_per = 0 at either prime forces mult_per = 6 over Q.

usage: python3 analysis/wk11_int_p0a.py [--seed 20260907] [--bound 40]
"""
import sys, os, time, json, random, pickle
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.normpath(os.path.join(HERE, '..'))
os.environ.setdefault('WIED_BIN', '/root/wied11')
os.environ.setdefault('WIED_WORK', '/root/s63work')
import numpy as np
from scipy import sparse
from wk8_s30_core import exps, restrict, det_form, per_form
from wk9_s45_build import build_cell
from wk9_s45_cell import nullity_stacked, LEVELS
from wk10_s63_n3control import ev_rows_from_coeffs

P1, P2 = 2147483647, 2147483629
N3 = 3; R = 7; LAM = (19, 7, 2, 2, 2, 2, 2); DELTA = 12; A_AMB = 6
DET3, N_DET3 = det_form(3)
PER3, N_PER3 = per_form(3)


def log(*a):
    print(*a, file=sys.stderr); sys.stderr.flush()


def pencils(K, seed, bound):
    rnd = random.Random(seed)
    return [[[[rnd.randint(-bound, bound) for _ in range(3)] for _ in range(3)]
             for _ in range(R)] for _ in range(K)]


def coeffs(form, Nv, pencil):
    As = [[pencil[i][a][b] for a in range(3) for b in range(3)] for i in range(R)]
    return restrict(form, Nv, N3, R, As)


def main():
    args = sys.argv[1:]
    def arg(name, d): return type(d)(args[args.index(name) + 1]) if name in args else d
    seed = arg('--seed', 20260907); bound = arg('--bound', 40)
    t0 = time.time()
    os.makedirs('/root/s63work', exist_ok=True)
    cache = '/root/s63work/n3_build.pkl'
    if os.path.exists(cache):
        B = pickle.load(open(cache, 'rb')); log(f'  loaded cached build (n_chi={B["n_chi"]})')
    else:
        B = build_cell(LAM, DELTA, n=N3, verbose=True)
        tmp = cache + '.tmp'
        pickle.dump(B, open(tmp, 'wb')); os.replace(tmp, cache)
    n_chi = B['n_chi']
    log(f'  cell: N_S={B["N_S"]} |Stab|={B["stab"]} n_chi={n_chi}')

    K = A_AMB + 8
    pen = pencils(K, seed, bound)
    res = dict(check='P0A', cell=dict(n=3, r=R, lam=list(LAM), delta=DELTA), a=A_AMB,
               n_chi=int(n_chi), seed=seed, bound=bound, K=K,
               instrument='i_X = nullity_p [E; ev_X] (sparse Wiedemann), mult_X = a - i_X',
               per_prime={})
    got = {}
    for p in (P1, P2):
        row = {}
        for tag, form, Nv in (('det', DET3, N_DET3), ('per', PER3, N_PER3)):
            tk = time.time()
            cds = [coeffs(form, Nv, q) for q in pen]
            EV = sparse.csr_matrix(ev_rows_from_coeffs(B['arr'], cds, p) % p)
            k, kern, lvl, diag = nullity_stacked(B['E'], EV, n_chi, p, want_kern=False,
                                                 seed0=1, tag=f'p0a_{tag}_{p}',
                                                 levels=LEVELS['cheap'], verbose=True)
            row[tag] = dict(i=int(k), mult=int(A_AMB - k), level=int(lvl),
                            secs=round(time.time() - tk, 1))
            got[(p, tag)] = int(k)
            log(f'  p={p} {tag}: i_{tag}={k}  mult_{tag}={A_AMB-k}  ({time.time()-tk:.0f}s)')
        row['D'] = row['det']['i'] - row['per']['i']
        res['per_prime'][str(p)] = row

    agree = all(got[(P1, t)] == got[(P2, t)] for t in ('det', 'per'))
    res['primes_agree'] = bool(agree)
    if agree:
        idet, iper = got[(P1, 'det')], got[(P1, 'per')]
        res['i_det'] = idet; res['i_per'] = iper
        res['mult_det'] = A_AMB - idet; res['mult_per'] = A_AMB - iper
        res['D'] = idet - iper
        res['det_control_ok'] = bool(idet == 1)
        if iper == 0 and idet >= 1:
            res['verdict'] = (f'D = +{idet}: i_det={idet} > 0 = i_per, so I(D) not contained in I(P), '
                              'so per_3 is not in the closure of GL_9 . det_3 -- an exhibited '
                              'occurrence obstruction, rigorous (rank_p <= rank_Q).')
        elif iper >= 1 and idet > iper:
            res['verdict'] = f'D = {idet-iper} > 0 but i_per={iper} >= 1: compare the kernel lines.'
        elif idet == iper:
            res['verdict'] = f'D = 0 (i_det = i_per = {idet}): the multiplicity does not separate here.'
        else:
            res['verdict'] = f'D = {idet-iper} < 0: multiplicity points the wrong way.'
    else:
        res['verdict'] = '*** PRIMES DISAGREE ***'
    res['secs'] = round(time.time() - t0, 1)
    log('  ' + res['verdict'])
    os.makedirs(os.path.join(ROOT, 'results'), exist_ok=True)
    json.dump(res, open(os.path.join(ROOT, 'results', 'wk11_int_p0a.json'), 'w'), indent=1)
    print('RESULT ' + json.dumps({k: v for k, v in res.items() if k != 'per_prime'}))
    return 0


if __name__ == '__main__':
    sys.exit(main())
