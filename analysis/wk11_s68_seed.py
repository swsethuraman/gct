#!/usr/bin/env python3
"""
Session 68 -- Part A: size the LMR seed M_12 at lam=(17,17,2^7), delta=12, and
project the build/solve cost against the 7 GB / 2-core container.  Also fits
nnz/n_chi vs |Stab| on reachable cells to test whether a streaming
orbit-representative build (s63's named opening) would open the seed.

No LMR object is built (stopping rule 3: do not form the full carrier).  The
sizing uses the exact N_S DP (wk9_s57_lib.N_S_mod), the exact |Stab| order, and
the s45 measured cost laws, cross-checked by a direct fit here.
"""
import os, sys, time, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import numpy as np
from wk9_s57_lib import N_S_mod, stab_order
from wk9_s45_build import build_cell

def fit_nnz_vs_stab():
    """nnz(E)/n_chi vs |Stab| on a spread of small reachable cells.  s45's law is
    nnz ~ 3.5 N_S = 3.5 |Stab| n_chi, i.e. nnz/n_chi ~ c*|Stab| with c~3-3.5.
    Confirming c*|Stab| (not c*constant) means the REDUCED matrix stays large when
    |Stab| is large -- so a streaming orbit-rep build (which removes the monomial
    ARRAY, size N_S) does NOT remove the MATRIX (size nnz ~ 3.5 N_S)."""
    cells = [((10, 4, 2, 2, 2), 5), ((12, 2, 2, 2, 2), 5), ((8, 6, 4, 2), 5),
             ((6, 6, 2, 2, 2, 2), 5), ((10, 4, 4, 2), 5), ((8, 4, 4, 4), 5),
             ((12, 6, 4, 2), 6), ((16, 6, 4, 2), 7)]
    rows = []
    for lam, d in cells:
        B = build_cell(lam, d, verbose=False)
        rows.append(dict(lam=lam, delta=d, stab=B['stab'], N_S=B['N_S'],
                         n_chi=B['n_chi'], nnz=int(B['E'].nnz),
                         nnz_over_NS=round(B['E'].nnz / B['N_S'], 3),
                         nnz_over_nchi=round(B['E'].nnz / B['n_chi'], 2),
                         nnz_over_nchi_stab=round(B['E'].nnz / B['n_chi'] / B['stab'], 3)))
    return rows

def seed_sizing():
    lam12 = (17, 17, 2, 2, 2, 2, 2, 2, 2); d = 12
    t0 = time.time()
    N_S = N_S_mod(lam12, d)               # exact by CRT of two modular DPs
    stab = stab_order(lam12)              # 2! * 7! = 10080
    n_chi = N_S / stab                    # n_chi~ (upper bound; dropped orbits only lower it)
    # s45 measured laws
    bytes_per_mono = 159                  # peak resident, s45 sec 3a
    peak_build = bytes_per_mono * N_S
    mono_array = N_S * d * 4              # (N_S x delta) int32, the dominant object
    nnz = 3.5 * N_S                       # s45 law nnz ~ 3.5 N_S
    csr_bytes = nnz * 12                  # ~ (int64 val + int32 col) per entry, +indptr
    solve_secs = 10.6e-9 * n_chi * nnz    # s45 sec 3b: cell ~ 10.6e-9 * n_chi * nnz_c
    GB = 1024**3
    return dict(lam=lam12, delta=d, N_S=int(N_S), stab=stab, n_chi_tilde=n_chi,
                mono_array_TB=round(mono_array / 1e12, 3),
                peak_build_TB=round(peak_build / 1e12, 3),
                nnz=nnz, csr_TB=round(csr_bytes / 1e12, 3),
                solve_secs=solve_secs, solve_years=round(solve_secs / 3.15e7, 1),
                container_GB=7, sizing_secs=round(time.time() - t0, 1))

if __name__ == '__main__':
    print("== nnz vs |Stab| fit (reachable cells) ==", flush=True)
    fit = fit_nnz_vs_stab()
    for r in fit:
        print("  lam=%s d=%d |Stab|=%d N_S=%d n_chi=%d nnz=%d  nnz/N_S=%.2f nnz/n_chi=%.1f nnz/(n_chi|Stab|)=%.3f"
              % (r['lam'], r['delta'], r['stab'], r['N_S'], r['n_chi'], r['nnz'],
                 r['nnz_over_NS'], r['nnz_over_nchi'], r['nnz_over_nchi_stab']), flush=True)
    print("\n== LMR seed sizing (lam=(17,17,2^7), delta=12) ==", flush=True)
    s = seed_sizing()
    for k, v in s.items():
        print("  %-16s %s" % (k, v), flush=True)
    json.dump(dict(seed=s, fit=fit), open('/home/claude/gct/results/s68_seed_sizing.json', 'w'), indent=1)
    print("\nsaved results/s68_seed_sizing.json", flush=True)
