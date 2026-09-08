#!/usr/bin/env python3
"""
Session 68 -- verification artefacts (closes the audit gaps):
  (V1) independent a cross-check: flint nullity of E  vs  plethysm a_of, all cells.
  (V2) GENUINE end-to-end chained climb on L1: carry the ASSEMBLED predecessor
       M_{delta-1} = [J(M_{delta-2}) | B_{delta-1}] forward (never the recomputed
       ground-truth kernel), and only compare to ground truth at the end.
  (V3) u-free quotient injectivity: rank pi(B_delta) = birth, and pi(J M_{prev}) = 0.
Writes results/s68_vcheck.json.
"""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
os.environ.setdefault('WIED_BIN', '/home/claude/wied68'); os.environ.setdefault('WIED_WORK', '/home/claude/s68/work')
import numpy as np
from flint import nmod_mat
from wk11_s68_ladder import (build_one, transport_matrix, vstack2, hstack, rank_of,
                             kernel_cols, idx0_free_columns)
from wk8_s30_pleth import a_of
from wk9_s36_stabred import P1, P2

def restrict_rows(M, idx, p):
    return nmod_mat(len(idx), M.ncols(), [int(M[int(i), j]) for i in idx for j in range(M.ncols())], p)

def chained_climb(tail, deltas, p, seed_rng):
    """Carry the assembled predecessor forward; compare to ground truth only at the end."""
    rows = []
    Mprev = None; aprev = 0; prev = None
    for d in deltas:
        lam = (4 * d - sum(tail),) + tail
        cur = build_one(lam, d, p, verbose=False)
        Kgt = cur['K']                                    # ground truth kernel (for comparison only)
        if Mprev is None:
            Massembled = Kgt                              # seed: from scratch
            birth = cur['a']; role = 'seed'; transported_in_ker = True; complete = True
        else:
            J = transport_matrix(prev, cur, p)
            JM = J * Mprev                                # transport the ASSEMBLED predecessor
            # deflate
            R = nmod_mat(aprev, cur['n_chi'], [int(x) for x in seed_rng.integers(0, p, size=aprev * cur['n_chi'])], p)
            Bdef, birth = kernel_cols(vstack2(cur['Efl'], R, p))
            Massembled = hstack([JM, Bdef], p)
            # checks against ground truth
            Z = cur['Efl'] * Massembled
            transported_in_ker = all(Z[i, j] == 0 for i in range(Z.nrows()) for j in range(Z.ncols()))
            withK = hstack([Massembled, Kgt], p)
            complete = (rank_of(Massembled) == cur['a']) and (rank_of(withK) == cur['a'])
            role = 'rung'
        rows.append(dict(delta=d, lam=list(lam), a=cur['a'], role=role, birth=birth,
                         birth_expected=cur['a'] - aprev,
                         assembled_rank=rank_of(Massembled),
                         E_annihilates_assembled=bool(transported_in_ker),
                         assembled_equals_kernel=bool(complete)))
        Mprev = Massembled; aprev = cur['a']; prev = cur
    return rows

def main():
    out = dict(V1_a_crosscheck=[], V2_chained_climb={}, V3_ufree_quotient=[])
    # V1: a_of vs flint nullity
    for name, tail, deltas in [('L1', (6, 4, 2), range(5, 9)), ('L2', (4, 4, 2), range(4, 9))]:
        for d in deltas:
            lam = (4 * d - sum(tail),) + tail
            cur = build_one(lam, d, P1, verbose=False)
            a_pleth = a_of(lam, d, 4, len(lam))
            out['V1_a_crosscheck'].append(dict(ladder=name, delta=d, lam=list(lam),
                                               a_flint_nullity=cur['a'], a_plethysm=int(a_pleth),
                                               match=bool(cur['a'] == a_pleth)))
    # V2: genuine chained climb on L1, both primes
    for p in (P1, P2):
        rng = np.random.default_rng(31 + p % 1000)
        out['V2_chained_climb'][str(p)] = chained_climb((6, 4, 2), range(5, 9), p, rng)
    # V3: u-free quotient injectivity on L1 (P1)
    from wk11_s68_ladder import certify_rung
    rng = np.random.default_rng(7); prev = None
    for d in range(5, 9):
        lam = (4 * d - 12, 6, 4, 2); cur = build_one(lam, d, P1, verbose=False)
        if prev is None:
            prev = cur; continue
        res, mats = certify_rung(prev, cur, P1, rng)
        free, nfree = idx0_free_columns(cur); idx = np.nonzero(free)[0]
        rk_b = rank_of(restrict_rows(mats['Bdef'], idx, P1))
        rk_j = rank_of(restrict_rows(mats['JK'], idx, P1))
        out['V3_ufree_quotient'].append(dict(delta=d, birth=res['birth'],
                                             rank_pi_births=rk_b, injective=(rk_b == res['birth']),
                                             rank_pi_transported=rk_j, transport_vanishes=(rk_j == 0)))
        prev = cur
    json.dump(out, open('/home/claude/gct/results/s68_vcheck.json', 'w'), indent=1)
    # summary
    print("V1 a-crosscheck: %d/%d match" % (sum(r['match'] for r in out['V1_a_crosscheck']), len(out['V1_a_crosscheck'])))
    for p, rows in out['V2_chained_climb'].items():
        ok = all(r['E_annihilates_assembled'] and r['assembled_equals_kernel'] for r in rows)
        print("V2 chained climb p=%s: %s  births=%s" % (p, 'ALL PASS' if ok else 'FAIL',
              [r['birth'] for r in rows]))
    print("V3 u-free quotient:", [(r['delta'], r['injective'], r['transport_vanishes']) for r in out['V3_ufree_quotient']])
    print("wrote results/s68_vcheck.json")

if __name__ == '__main__':
    main()
