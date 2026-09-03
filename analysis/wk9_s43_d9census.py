#!/usr/bin/env python3
"""
Session 43, Phase C -- the census of the first rung at delta = 9.

Cells: ell(lam) = 6, lam |- 36, lam_1 >= 9 (the obstruction-eligibility gate of
docs/sixrow_frontier.md section 1), a(lam, 9) >= 1.  a by the Frobenius
plethysm route (wk8_s30_pleth.a_of) and, on the cells that are actually going to
be measured, again by the kernel dimension inside the cell process -- the same
two-route discipline as the six-row census.  m_det by the symmetric rectangular
Kronecker bound of wk9_s38_screen (self-tested on the n = 3 anchors 3, 11, 43).
n_chi by orbit enumeration.  Output: results/s43_d9census.md, ascending n_chi,
and a pickle for the sweep.

usage: python3 wk9_s43_d9census.py [--cap 20000] [--nmax 60]
  --cap    only cells at or below this n_chi are enumerated for n_chi/m_det
           (above it the row carries the N_S/|Stab| bound, marked ~)
"""
import sys, os, pickle, time

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
from wk8_s30_pleth import a_of
from wk9_s36_stabred import orbit_setup, stab_group, monomials, log
from wk9_s41_per6 import partitions

DELTA = 9
N = 4
R = 6


def m_det_of(lam):
    from wk9_s38_screen import m_det_ref
    return m_det_ref(tuple(lam), 4, DELTA)


if __name__ == '__main__':
    cap = int(sys.argv[sys.argv.index('--cap') + 1]) if '--cap' in sys.argv else 20000
    t0 = time.time()
    lams = [l for l in partitions(N * DELTA, R) if l[0] >= DELTA]
    log(f"delta=9: {len(lams)} partitions of {N*DELTA} into exactly 6 parts with lam_1 >= {DELTA}")
    rows = []
    for i, lam in enumerate(lams):
        a = a_of(lam, DELTA, N, R)
        if a < 1:
            continue
        rows.append(dict(lam=tuple(lam), delta=DELTA, a=a, bal=lam[0] - lam[-1]))
        if i % 200 == 0:
            log(f"  ... {i}/{len(lams)} scanned, {len(rows)} with a>=1 ({time.time()-t0:.0f}s)")
    log(f"a>=1 at {len(rows)} cells, sum a = {sum(x['a'] for x in rows)} ({time.time()-t0:.0f}s)")
    # n_chi: cheapest first.  |Stab| is free; N_S needs the orbit enumeration, so
    # bound n_chi below by N_S/|Stab| only where the enumeration is affordable.
    for x in rows:
        x['stab'] = len(stab_group(x['lam']))
    rows.sort(key=lambda x: (-x['stab'], x['a']))
    got = 0
    for x in rows:
        try:
            basis, vecs, group = orbit_setup(N, R, DELTA, x['lam'], verbose=False)
            x['N_S'] = len(basis); x['n_chi'] = len(vecs); x['approx'] = ''
            monomials.cache_clear()
            got += 1
        except MemoryError:
            x['N_S'] = -1; x['n_chi'] = 10 ** 9; x['approx'] = '~'
        if x['n_chi'] <= cap:
            x['m_det'] = m_det_of(x['lam'])
        else:
            x['m_det'] = -1
        if got % 50 == 0:
            log(f"  ... {got} cells enumerated ({time.time()-t0:.0f}s)")
    rows.sort(key=lambda x: (x['n_chi'], x['lam']))
    reach = [x for x in rows if x['n_chi'] <= cap]
    os.makedirs('/root/s43', exist_ok=True)
    pickle.dump({DELTA: reach}, open('/root/s43/d9census.pkl', 'wb'))
    L = ["# `δ = 9` census — the first rung above session 41's range (`n = 4`, `ℓ(λ) = 6`, `λ_1 ≥ 9`, `a ≥ 1`)\n",
         f"Session 43, `analysis/wk9_s43_d9census.py`.  `a` by Frobenius plethysm (and again by kernel dimension "
         f"inside every cell measured); `m_det` the symmetric rectangular Kronecker bound (`wk9_s38_screen`, "
         f"self-tested on the `n = 3` anchors 3, 11, 43) computed at the cells inside the frontier; `n_χ` by orbit "
         f"enumeration.  Eligibility as `docs/sixrow_frontier.md` §1.  Reachable at `n_χ ≤ {cap}`.\n",
         f"**{len(rows)} eligible cells, {sum(x['a'] for x in rows)} ambient units; "
         f"{len(reach)} reachable at `n_χ ≤ {cap}` ({sum(x['a'] for x in reach)} units).**\n",
         "| lam | a | m_det | balance | N_S | Stab | n_chi | pred GB |",
         "|---|---|---|---|---|---|---|---|"]
    for x in reach:
        pred = 0.5 if x['n_chi'] <= 800 else 1.4e-8 * x['n_chi'] ** 2 + 0.4
        L.append(f"| `{x['lam']}` | {x['a']} | {x['m_det']} | {x['bal']} | {x['N_S']} | {x['stab']} | "
                 f"{x['n_chi']} | {pred:.2f} |")
    L.append("")
    forced = [x for x in reach if x['m_det'] >= 0 and x['a'] > x['m_det']]
    L.append(f"Arithmetic map on the reachable set: `a > m_det` at {len(forced)} cells"
             + (": " + ", ".join(f"`{x['lam']}`" for x in forced) if forced else "") + ".\n")
    open(os.path.join(ROOT, 'results', 's43_d9census.md'), 'w').write("\n".join(L))
    log(f"wrote results/s43_d9census.md ({len(reach)} reachable of {len(rows)}) in {time.time()-t0:.0f}s")
