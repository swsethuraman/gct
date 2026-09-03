#!/usr/bin/env python3
"""
Session 42 -- P1 / P1b validation: reproduce s36's banked mult_red (= mult_pad)
at every banked cell reachable in the time budget, by the sparse certificate
route (both primes) and, where n_red <= DENSE_CAP_VAL, by the dense flint
route as well (both must agree); the full-E nullity is asserted equal to a
(plethysm) by the sparse route on every cell.

usage: python3 wk9_s42_validate.py [nchi_cap] [dense_cap]
"""
import sys, os, time, json, re
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from wk9_s42_redengine import build, rank_compressed, nullity_exact, EXACT_CAP
from wk9_s42_sparse import nullity_sparse, log
from wk9_s42_hpad import h_pad, banked
from wk8_s30_pleth import a_of
from wk9_s36_stabred import P1, P2, monomials

NCHI_CAP = int(sys.argv[1]) if len(sys.argv) > 1 else 16000
DENSE_CAP_VAL = int(sys.argv[2]) if len(sys.argv) > 2 else 9000
OUT = os.path.join(HERE, '..', 'results', 's42_validation.jsonl')
done = set()
if os.path.exists(OUT):
    for line in open(OUT):
        d = json.loads(line); done.add((tuple(d['lam']), d['delta']))

cells = banked()
# extra: the two invariants (a = 1, mult_red = 0) -- not in the red table
cells = [((4,4,4,4,4), 5, 1, 1, 0, 0), ((4,4,4,4,4,4), 6, 1, 1, 0, 0)] + cells
from wk9_s42_census import N_S_tail, stab_order
cells.sort(key=lambda c: N_S_tail(c[0], c[1]) / stab_order(c[0]))     # ascending n_chi (lower bound)
FULL_A_CAP, FULL_NCHI_CAP = 4, 10000
rows = []
for lam, delta, a_b, mdet, mpad, mred_b in cells:
    if (lam, delta) in done: continue
    t0 = time.time()
    B = build(lam, delta, verbose=False)
    if B['n_chi'] > NCHI_CAP:
        log(f"skip {lam} d{delta}: n_chi {B['n_chi']} > cap"); monomials.cache_clear(); continue
    a = a_of(lam, delta, 4, len(lam))
    assert a == a_b, (lam, delta, a, a_b)
    log(f"== {lam} d{delta}: a={a} N_S={B['N_S']} n_chi={B['n_chi']} n_red={B['n_red']} rows_red={len(B['rows_red'])} nnz_red={sum(len(d) for d in B['rows_red'])}")
    rec = dict(lam=list(lam), delta=delta, a=a, N_S=B['N_S'], stab=B['stab'], n_chi=B['n_chi'], n_red=B['n_red'],
               nrows_red=len(B['rows_red']), banked_mult_red=mred_b, mult_det_s36=mdet, mult_pad_s36=mpad, primes={})
    for p in (P1, P2):
        t1 = time.time()
        ks, _ = nullity_sparse(B['rows_red'], B['n_red'], p, tag=f"v{'_'.join(map(str,lam))}d{delta}", verbose=False)
        ts = time.time() - t1
        t1 = time.time()
        if a <= FULL_A_CAP and B['n_chi'] <= FULL_NCHI_CAP:
            kf, _ = nullity_sparse(B['rows'], B['n_chi'], p, tag=f"vf{'_'.join(map(str,lam))}d{delta}", verbose=False)
            assert kf == a, ("full-E nullity != a", lam, delta, p, kf, a)
        else:
            kf = None
        tf = time.time() - t1
        pr = dict(sparse_nullity_red=ks, sparse_secs=round(ts, 1), full_nullity=kf, full_secs=round(tf, 1))
        if B['n_red'] <= DENSE_CAP_VAL:
            t1 = time.time()
            if B['n_red'] <= EXACT_CAP:
                kd, _ = nullity_exact(B['rows_red'], B['n_red'], p); route = 'exact'
            else:
                kd = B['n_red'] - rank_compressed(B['rows_red'], B['n_red'], p); route = 'compressed'
            pr.update(dense_nullity_red=kd, dense_route=route, dense_secs=round(time.time() - t1, 1))
            assert kd == ks, ("dense vs sparse nullity mismatch", lam, delta, p, kd, ks)
        rec['primes'][str(p)] = pr
        log(f"   p={p}: sparse nullity {ks} ({ts:.0f}s), full {kf} (a={a}) ({tf:.0f}s)" + (f", dense {pr['dense_nullity_red']} [{pr['dense_route']}] ({pr['dense_secs']}s)" if 'dense_nullity_red' in pr else ''))
    ks = {pr['sparse_nullity_red'] for pr in rec['primes'].values()}
    assert len(ks) == 1, ("primes disagree", lam, delta, rec)
    k = ks.pop()
    rec['mult_red'] = a - k
    rec['h_pad'] = h_pad(lam, delta)
    rec['agree'] = (rec['mult_red'] == mred_b)
    rec['secs'] = round(time.time() - t0, 1)
    assert rec['agree'], ("P1 FAILURE: banked mult_red differs", lam, delta, rec['mult_red'], mred_b)
    with open(OUT, 'a') as f: f.write(json.dumps(rec) + "\n")
    log(f"   -> mult_red {rec['mult_red']} (banked {mred_b}) AGREE; h_pad {rec['h_pad']}; {rec['secs']}s")
    monomials.cache_clear()
log("validation pass complete")
