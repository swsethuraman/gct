#!/usr/bin/env python3
"""B13-10 -- bank the fo='inplace' equivalence check.

hybrid_kernel_lean(fo='inplace') passes every row of E to the Schur projection
instead of the copy F_o = E[rows not in the cover].  A cover row r satisfies
R_1[r,U] - R_1[r,S] X = 0 identically, so it contributes nothing to the Schur
complement; only the rows the pseudo-random draw indexes change.  Here both
settings are run on three banked cells at both primes: same nullity, every
vector verified on E, same rank, and the resulting mult_det compared."""
import sys, os, json, time
for _v in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ.setdefault(_v, '1')
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
os.environ.setdefault('S71_SCHUR_SO', '/home/claude/b13_10_scratch/schur.so')
import numpy as np
import wk11_s71_codes; wk11_s71_codes.install()
from wk8_s30_core import P1, P2
from wk9_s42_census import a_weyl
from wk11_s71_hybrid import matmul_mod, rank_mod_p, rank_tall
from wk12_s79_cell6 import ev_rows_from_coeffs, det_pencils, det_coeffs
from wk13_b10_lean import build_cell_lean, best_cover_lean, check_kernel_mat_lean, hybrid_kernel_lean

CELLS = [(4, (24, 13, 3, 2, 1, 1), 11), (3, (12, 5, 5, 3, 1, 1), 9), (4, (26, 7, 5, 5, 1), 11)]
out = []
for n, lam, d in CELLS:
    B = build_cell_lean(lam, d, n=n, verbose=False); E = B['E']; nc = B['n_chi']; a = int(a_weyl(lam, d, n, {}))
    cov = best_cover_lean(E, nc)
    rec = dict(n=n, lam=list(lam), delta=d, a=a, n_chi=nc, nnz=int(E.nnz), per_prime={})
    for p in (P1, P2):
        r = {}
        for fo in ('copy', 'inplace'):
            t = time.time()
            K, info = hybrid_kernel_lean(E, nc, p, a, cov, verbose=False, fo=fo)
            ver = bool(check_kernel_mat_lean(E, K.astype(np.int64), p))
            rk = int(rank_tall(K, p))
            R = len(lam)
            cl = [det_coeffs(pt, R) for pt in det_pencils(a + 8, 11, 40, R)] if n == 4 else None
            m = None
            if cl:
                Kp = np.asarray(K % p, dtype=np.int64)
                G = np.vstack([matmul_mod(ev_rows_from_coeffs(B['arr'], cl[c0:c0 + 8], p, R) % p, Kp, p) for c0 in range(0, len(cl), 8)])
                m = int(rank_mod_p(G, p))
            r[fo] = dict(nullity=int(K.shape[1]), verified_on_E=ver, rank=rk, mult_det=m, secs=round(time.time() - t, 1), attempts=len(info['attempts']))
            del K
        r['agree'] = (r['copy']['nullity'] == r['inplace']['nullity'] == a and r['copy']['rank'] == r['inplace']['rank'] == a
                      and r['copy']['verified_on_E'] and r['inplace']['verified_on_E'] and r['copy']['mult_det'] == r['inplace']['mult_det'])
        rec['per_prime'][str(p)] = r
    rec['agree'] = all(v['agree'] for v in rec['per_prime'].values())
    print("FO " + json.dumps(rec), flush=True)
    out.append(rec)
json.dump(dict(cells=out, all_agree=all(r['agree'] for r in out),
               note="fo='inplace' drops the F_o copy; a cover row contributes nothing to the Schur complement, so only the projection's row indexing changes"),
          open(os.path.join(ROOT, 'results', 'b13_10', 'fo_inplace_check.json'), 'w'))
print("ALL AGREE:", all(r['agree'] for r in out))
