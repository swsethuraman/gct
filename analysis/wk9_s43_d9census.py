#!/usr/bin/env python3
"""
Session 43, Phase C -- the census of the first rung at delta = 9.

Built from session 41's census module (analysis/wk9_s41_census.py) but WITHOUT
its Kostant weight table: at delta = 9 that table is a dense int32 array of
shape (10, 37^5), 2.58 GB, which does not fit beside a running cell on this
container.  What is kept:

  a       Frobenius plethysm (wk8_s30_pleth.amb), and again by KERNEL DIMENSION
          inside every cell process that is actually measured (wk9_s41_cell.py
          asserts a(kernel) == a(plethysm)) -- the same two independent routes
          the ledger has always used per measured cell.  What is NOT available
          here is the third, census-wide Kostant cross-check of
          results/sixrow_census.md; that is recorded in the honest boundary.
  N_S     the generating-function DP of wk9_s36_census (one route only, for the
          same reason).
  m_det   the symmetric rectangular Kronecker bound (wk9_s38_screen, self-tested
          on the n = 3 anchors 3, 11, 43).
  n_chi   orbit enumeration where affordable, else the bound N_S/|Stab| (~).

Cells: ell(lam) = 6, lam |- 36, lam_1 >= 9 (obstruction-eligible); the lam_1 < 9
cells are onset-eligible only and are counted separately.

usage: python3 wk9_s43_d9census.py [--ns-cap 400000] [--nchi-cap 20000]
"""
import sys, os, pickle, time

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
from wk8_s30_pleth import amb
from ambient_screen import a as amb_a, m_det as m_det_ref, chi
from wk9_s38_screen import mdet_weights, m_det_fast
from wk9_s36_census import N_S as N_S_dp, stab_order, balance
from wk9_s36_stabred import n_chi_of, monomials

DELTA = 9
R = 6
MEM_PEAK_INPL = 1.4e-8
MEM_INPL_BASE = 0.4


def log(*a):
    print(*a, file=sys.stderr, flush=True)


if __name__ == '__main__':
    NS_CAP = int(sys.argv[sys.argv.index('--ns-cap') + 1]) if '--ns-cap' in sys.argv else 400000
    NCHI_CAP = int(sys.argv[sys.argv.index('--nchi-cap') + 1]) if '--nchi-cap' in sys.argv else 20000
    t0 = time.time()
    log(f"[d9census] route A plethysm ...")
    A = amb(DELTA, 4, R)
    lams = sorted(l for l in A if len(l) == R)
    log(f"[d9census] {len(lams)} ell=6 weights with a>=1, {sum(A[l] for l in lams)} units "
        f"({time.time()-t0:.0f}s); m_det weights ...")
    Ws = mdet_weights(DELTA, 4)
    chi.cache_clear()
    log(f"[d9census] |W-support| = {len(Ws)} ({time.time()-t0:.0f}s)")
    rows = []
    for k, lam in enumerate(lams):
        aA = A[lam]
        ns = N_S_dp(4, R, DELTA, lam)
        so = stab_order(lam)
        bound = (ns + so - 1) // so
        if ns <= NS_CAP and bound <= NCHI_CAP:
            ns2, nchi, so2 = n_chi_of(4, R, DELTA, lam)
            assert ns2 == ns and so2 == so, (lam, ns2, ns, so2, so)
            approx = ''
            monomials.cache_clear()
        else:
            nchi, approx = bound, '~'
        md = m_det_fast(lam, Ws) if approx == '' and nchi <= NCHI_CAP else -1
        if (k + 1) % 60 == 0:
            chi.cache_clear()
        rows.append(dict(lam=lam, delta=DELTA, a=aA, m_det=md, forced=(md >= 0 and aA > md),
                         N_S=ns, stab=so, n_chi=nchi, approx=approx, bal=balance(lam),
                         gb_inpl=MEM_PEAK_INPL * nchi * nchi + MEM_INPL_BASE,
                         eligible=lam[0] >= DELTA))
        if (k + 1) % 100 == 0:
            log(f"[d9census] {k+1}/{len(lams)} ({time.time()-t0:.0f}s)")
    chi.cache_clear()
    elig = [x for x in rows if x['eligible']]
    onset = [x for x in rows if not x['eligible']]
    reach = sorted([x for x in elig if x['approx'] == '' and x['n_chi'] <= NCHI_CAP],
                   key=lambda x: (x['n_chi'], x['lam']))
    # m_det route cross-check on the cells that will actually be measured
    for x in reach[:4]:
        assert x['m_det'] == m_det_ref(x['lam'], 4, DELTA), ("m_det route mismatch", x['lam'])
    os.makedirs('/root/s43', exist_ok=True)
    pickle.dump({DELTA: reach}, open('/root/s43/d9census.pkl', 'wb'))
    L = ["# `δ = 9` census — the first rung above session 41's range (`n = 4`, `ℓ(λ) = 6`, `a ≥ 1`)\n",
         "Session 43, `analysis/wk9_s43_d9census.py`.  `a` by Frobenius plethysm here, and again by **kernel "
         "dimension** inside every cell process that is measured (`wk9_s41_cell.py` asserts the two equal) — the "
         "two routes the ledger has always used per cell.  The census-wide Kostant cross-check of "
         "`results/sixrow_census.md` is **not** available at this degree on this container: its dense weight "
         "table is a 2.58 GB int32 array at `δ = 9`.  `N_S` by the generating-function DP; `m_det` the symmetric "
         "rectangular Kronecker bound (`wk9_s38_screen`, self-tested on the `n = 3` anchors 3, 11, 43), computed "
         "at the reachable cells and cross-checked against `ambient_screen.m_det` on the first four; `n_χ` by "
         "orbit enumeration where affordable, else the bound `N_S/|Stab|` (marked `~`).  Obstruction-eligible "
         "cells have `λ_1 ≥ δ` (`docs/sixrow_frontier.md` §1).\n",
         f"**{len(elig)} obstruction-eligible cells, {sum(x['a'] for x in elig)} ambient units; "
         f"{len(onset)} onset-only cells (`λ_1 < 9`); {len(reach)} eligible cells reachable at "
         f"`n_χ ≤ {NCHI_CAP}` ({sum(x['a'] for x in reach)} units).**\n",
         "## Reachable, ascending `n_χ`\n",
         "| lam | a | m_det | forced | balance | N_S | Stab | n_chi | GB peak (inpl) |",
         "|---|---|---|---|---|---|---|---|---|"]
    for x in reach:
        L.append(f"| `{x['lam']}` | {x['a']} | {x['m_det']} | {'**yes**' if x['forced'] else 'no'} | {x['bal']} | "
                 f"{x['N_S']} | {x['stab']} | {x['n_chi']} | {x['gb_inpl']:.2f} |")
    L.append("")
    forced = [x for x in reach if x['forced']]
    L.append(f"Arithmetic map on the reachable set: `a > m_det` at {len(forced)} of {len(reach)} cells"
             + (": " + ", ".join(f"`{x['lam']}`" for x in forced[:10]) if forced else "")
             + ".  Tightest margins `m_det − a`: "
             + ", ".join(f"`{x['lam']}` ({x['m_det']} − {x['a']} = {x['m_det']-x['a']})"
                         for x in sorted(reach, key=lambda y: y['m_det'] - y['a'])[:5]) + ".\n")
    L.append(f"Onset-only cells (`λ_1 < 9`; cannot be obstructions, can carry the determinant ideal): "
             f"{len(onset)}, smallest `n_χ` bound {min([x['n_chi'] for x in onset], default=0)} — "
             "out of reach, as at `δ = 7, 8`.\n")
    open(os.path.join(ROOT, 'results', 's43_d9census.md'), 'w').write("\n".join(L))
    log(f"[d9census] wrote results/s43_d9census.md ({len(reach)} reachable of {len(elig)} eligible) "
        f"in {time.time()-t0:.0f}s")
