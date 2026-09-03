#!/usr/bin/env python3
"""Session 45 -- V2 (every pad-side bite the programme has) and V3 (banked
det-side D = 0 rows of results/s41_ledger.md) through the sparse route.

V2 is the part of the battery that decides whether the route is worth anything:
a route that answered "full column rank" unconditionally would pass every
determinant-side test in the repository, because mult_det = a at every cell ever
measured.  At each bite the sparse route must return the DROP, and the exhibited
kernel vectors are lifted to Q and verified exactly (E v = 0 over Z) and against
Theorem (★).

usage: python3 wk9_s45_v23.py [v2|v3|all]
"""
import sys, os, json, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
os.environ.setdefault('WIED_BIN', '/home/claude/wied45')
os.environ.setdefault('WIED_WORK', '/home/claude/s45/work')
from wk9_s45_lift import certify
from wk9_s45_cell import measure_cell, LEVELS
from wk9_s45_build import log
from wk9_s36_stabred import P1, P2

# (lam, delta, a, mult_pad) -- results/s36_ledger.md and results/s41_ledger.md
BITES = [((8, 4, 4, 4, 4), 6, 2, 1),
         ((9, 9, 8, 1, 1), 7, 2, 1),
         ((8, 8, 8, 2, 2), 7, 3, 2),
         ((12, 4, 4, 4, 4), 7, 4, 3),
         ((10, 8, 7, 1, 1, 1), 7, 3, 2),
         ((13, 10, 6, 1, 1, 1), 8, 9, 8)]

# (lam, delta, a, mult_det, n_chi) -- D = 0 rows of results/s41_ledger.md,
# spanning n_chi from the smallest to the session-41 frontier
BANKED = [((22, 2, 2, 2, 2, 2), 8, 1, 1, 197),
          ((19, 5, 5, 1, 1, 1), 8, 1, 1, 645),
          ((12, 10, 3, 1, 1, 1), 7, 1, 1, 1282),
          ((16, 10, 3, 1, 1, 1), 8, 2, 2, 1850),
          ((20, 4, 2, 2, 2, 2), 8, 3, 3, 2725),
          ((12, 12, 5, 1, 1, 1), 8, 3, 3, 3923),
          ((15, 7, 7, 1, 1, 1), 8, 5, 5, 3985),
          ((12, 10, 2, 2, 1, 1), 7, 1, 1, 5282),
          ((14, 9, 6, 1, 1, 1), 8, 10, 10, 9159),
          ((13, 10, 6, 1, 1, 1), 8, 9, 9, 10682),
          ((11, 9, 2, 2, 2, 2), 7, 1, 1, 11538),
          ((12, 12, 2, 2, 2, 2), 8, 5, 5, 12942),
          ((12, 8, 3, 3, 1, 1), 7, 5, 5, 18716),
          ((12, 9, 3, 2, 1, 1), 7, 5, 5, 19985)]

OUT = os.path.join(HERE, '..', 'results')

def run_v2():
    rows = []
    for lam, delta, a_w, pad_w in BITES:
        t0 = time.time()
        res, vecs = certify(lam, delta, side='pad', verbose=True)
        assert res['a'] == a_w, ("a mismatch vs the ledger", lam, delta, res['a'], a_w)
        assert res['mult'] == pad_w, ("mult_pad mismatch vs the ledger", lam, delta, res['mult'], pad_w)
        assert res['nullity'] == a_w - pad_w
        assert res['star'], ("(★) fails on an exhibited vector", lam, delta)
        res['ledger'] = dict(a=a_w, mult_pad=pad_w); res['secs'] = round(time.time() - t0, 1)
        res['verdict'] = 'PASS'
        rows.append(res)
        log(f"V2 PASS {lam} d{delta}: a={a_w}, mult_pad={pad_w} reproduced; "
            f"{res['exact_vectors']} exact vector(s), (★) holds, max|coeff| {res['max_abs']}")
        with open(os.path.join(OUT, 's45_v2.jsonl'), 'a') as f: f.write(json.dumps(res) + "\n")
    return rows

def run_v3():
    rows = []
    for lam, delta, a_w, det_w, nchi_w in BANKED:
        t0 = time.time()
        res = measure_cell(lam, delta, sides=('det',), levels=LEVELS['cheap'],
                           full_check=(nchi_w <= 13000), verbose=True)
        assert res['a'] == a_w, ("a mismatch vs the ledger", lam, delta, res['a'], a_w)
        assert res['n_chi'] == nchi_w, ("n_chi mismatch vs the ledger", lam, delta, res['n_chi'], nchi_w)
        assert res['mult_det'] == det_w, ("mult_det mismatch vs the ledger", lam, delta, res['mult_det'], det_w)
        res['ledger'] = dict(a=a_w, mult_det=det_w, n_chi=nchi_w)
        res['verdict'] = 'PASS'
        rows.append(res)
        log(f"V3 PASS {lam} d{delta}: n_chi={nchi_w}, a={a_w}, mult_det={det_w} "
            f"(nullity {res['sides']['det']['nullity']}) in {res['secs']}s")
        with open(os.path.join(OUT, 's45_v3.jsonl'), 'a') as f: f.write(json.dumps(res) + "\n")
    return rows

if __name__ == '__main__':
    what = sys.argv[1] if len(sys.argv) > 1 else 'all'
    if what in ('v2', 'all'): run_v2()
    if what in ('v3', 'all'): run_v3()
    log("V2/V3 complete")
