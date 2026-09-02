#!/usr/bin/env python3
"""
Session 40 -- the reduced census at n = 3 (paper 1's object): every cell
(delta in 8..12, lam |- 3 delta, ell(lam) = 5 exactly, a >= 1) of
C[Sym^3 C^5]_delta, with

  a        plethysm multiplicity (wk8_s30_pleth.amb, n = 3)
  N_S      weight-space dimension (generating-function DP, wk9_s36_census.N_S)
  |Stab|   order of the Young subgroup Stab_W(lam)
  n_chi    dim of the chi_lam-isotypic part (orbit enumeration when
           N_S <= NS_ENUM_CAP and the bound N_S/|Stab| <= NCHI_ENUM_CAP; else
           the lower bound N_S/|Stab|, marked '~')
  GB       predicted peak 2.5e-8 n_chi^2 (s36's calibrated constant; the
           container frontier is n_chi ~ 15500 = 6 GB)

Only length exactly 5 is listed: I(D_5^{det_3}) is concentrated at length-5
weights (paper 1, Remark after Theorem 3.x; docs/d5_ideal.md section 3), and
the `a >= 1` gate is the correct one (docs/s37_review.md section 2b).

usage: python3 wk9_s40_n3census.py [out.md] [pickle]
"""
import sys, os, time, pickle
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk8_s30_pleth import amb
from wk9_s36_census import N_S, stab_order
from wk9_s36_stabred import n_chi_of, monomials

MEM_PER = 2.5e-8
BUDGET_GB = 6.5
FRONTIER = 15500
NS_ENUM_CAP = 250000
NCHI_ENUM_CAP = 16000
DELTAS = (8, 9, 10, 11, 12)
N = 3

def census(delta, cache):
    A = amb(delta, N, 5)
    rows = []
    for lam, a in sorted(A.items()):
        if len(lam) != 5 or a < 1: continue
        key = (delta, lam)
        if key in cache: rows.append(cache[key]); continue
        ns = N_S(N, 5, delta, lam)
        so = stab_order(lam)
        lb = (ns + so - 1) // so
        if ns <= NS_ENUM_CAP and lb <= NCHI_ENUM_CAP:
            ns2, nchi, so2 = n_chi_of(N, 5, delta, lam)
            assert ns2 == ns and so2 == so, (lam, ns, ns2, so, so2)
            approx = ''
            monomials.cache_clear()
        else:
            nchi = lb; approx = '~'
        gb = MEM_PER * nchi * nchi
        row = dict(delta=delta, lam=lam, a=a, N_S=ns, stab=so, n_chi=nchi, approx=approx,
                   gb=gb, bal=lam[0] - lam[-1], fits=(nchi <= FRONTIER),
                   invariant=(len(set(lam)) == 1))
        cache[key] = row; rows.append(row)
    return rows

def render(allrows):
    L = [f"# Reduced census — `n = 3`, `ell = 5`, `a >= 1`, `delta = 8..12` (paper 1's `D_5`)\n",
         f"Session 40.  `a` by plethysm (`wk8_s30_pleth.amb(delta, 3, 5)`); `N_S` by the s36 generating-function DP; "
         f"`n_chi` by orbit enumeration where `N_S <= {NS_ENUM_CAP}` and `N_S/|Stab| <= {NCHI_ENUM_CAP}`, otherwise the lower bound `N_S/|Stab|` marked `~`; "
         f"predicted peak `{MEM_PER:.1e} · n_chi^2` GB (s36's calibrated constant); **fits** means `n_chi <= {FRONTIER}` (s36's measured frontier on a 7 GB container, 6.5 usable).  "
         "Only weights of length exactly 5 are listed (the ideal is concentrated there).  `inv` marks the rectangular weights `((3 delta/5)^5)` — candidate `SL_5`-invariants of cubic threefolds.\n"]
    for delta in DELTAS:
        sub = [x for x in allrows if x['delta'] == delta]
        fits = [x for x in sub if x['fits']]
        L.append(f"\n## `delta = {delta}` — {len(sub)} cells, {sum(x['a'] for x in sub)} ambient units; "
                 f"{len(fits)} cells ({sum(x['a'] for x in fits)} units) fit the frontier\n")
        L.append("| lam | a | balance | N_S | Stab | n_chi | GB | fits | inv |")
        L.append("|---|---|---|---|---|---|---|---|---|")
        for x in sorted(sub, key=lambda x: (x['n_chi'], x['lam'])):
            L.append(f"| `{x['lam']}` | {x['a']} | {x['bal']} | {x['N_S']} | {x['stab']} | {x['approx']}{x['n_chi']} | "
                     f"{x['gb']:.2f} | {'yes' if x['fits'] else 'no'} | {'I' if x['invariant'] else ''} |")
    return "\n".join(L) + "\n"

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else 'results/n3_census.md'
    pk = sys.argv[2] if len(sys.argv) > 2 else 'results/logs/s40_n3census.pkl'
    cache = pickle.load(open(pk, 'rb')) if os.path.exists(pk) else {}
    allrows = []
    t = time.time()
    for delta in DELTAS:
        rows = census(delta, cache)
        pickle.dump(cache, open(pk, 'wb'))
        allrows += rows
        fits = [x for x in rows if x['fits']]
        print(f"delta {delta}: {len(rows)} cells, {len(fits)} fit, units {sum(x['a'] for x in rows)} / fitting {sum(x['a'] for x in fits)}  [{time.time()-t:.0f}s]", flush=True)
        open(out, 'w').write(render(allrows))
    print("wrote", out)
