#!/usr/bin/env python3
"""
Session 36 -- the REDUCED census: n_chi (not N_S) governs memory now.

For every cell (n = 4, delta in {6, 7}, ell(lam) >= 5, a >= 2):
  a        by plethysm (wk8_s30_pleth.amb)
  N_S      weight-space dimension, by a generating-function DP (no enumeration)
  |Stab|   order of the Young subgroup Stab_W(lam)
  n_chi    dim of the chi_lam-isotypic part, by orbit enumeration when
           N_S <= NS_ENUM_CAP, else the lower bound N_S/|Stab| (marked '~')
  GB       predicted peak, MEM_PER * n_chi^2 (s33's measured constant for the
           compressed route: 2.89 GB at n_chi = 10738 -> 2.5e-8)
Strata: A = delta 6, ell 5 (the balanced corner s30 could not reach; NOT
permanent-sensitive, docs/s35_review.md section 1); B = ell 6 (permanent-
sensitive), at delta 6 and 7.  s34's domain (delta 7, ell 5, N_S <= 11269)
is listed but marked theirs.

usage: python3 wk9_s36_census.py [out.md]
"""
import sys, os, time, pickle
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk8_s30_pleth import amb
from wk9_s36_stabred import n_chi_of, stab_group, exps
from math import factorial

MEM_PER = 2.5e-8
BUDGET_GB = 6.5
NS_ENUM_CAP = 400000
S34_NS_CAP = 11269

def N_S(n, r, delta, lam):
    """coefficient of t^delta x^lam in prod_alpha (1 - t x^alpha)^-1."""
    lam = tuple(lam) + (0,) * (r - len(lam))
    st = {(0,) + (0,) * r: 1}
    for al in exps(n, r):
        new = dict(st)
        # multiply by 1/(1 - t x^al): add k copies for k >= 1
        frontier = st
        while frontier:
            nxt = {}
            for key, c in frontier.items():
                d = key[0] + 1
                if d > delta: continue
                w = tuple(key[1 + i] + al[i] for i in range(r))
                if any(w[i] > lam[i] for i in range(r)): continue
                k = (d,) + w
                nxt[k] = nxt.get(k, 0) + c
            for k, c in nxt.items(): new[k] = new.get(k, 0) + c
            frontier = nxt
        st = new
    return st.get((delta,) + lam, 0)

def stab_order(lam):
    from collections import Counter
    o = 1
    for v, k in Counter(lam).items(): o *= factorial(k)
    return o

def balance(lam): return lam[0] - lam[-1]

def census(delta, n=4):
    A = amb(delta, n, 6)
    rows = []
    for lam, a in sorted(A.items()):
        if len(lam) < 5 or a < 2: continue
        r = len(lam)
        ns = N_S(n, r, delta, lam)
        so = stab_order(lam)
        if ns <= NS_ENUM_CAP:
            ns2, nchi, so2 = n_chi_of(n, r, delta, lam)
            assert ns2 == ns and so2 == so, (lam, ns, ns2, so, so2)
            approx = ''
        else:
            nchi = (ns + so - 1) // so; approx = '~'
        gb = MEM_PER * nchi * nchi
        rows.append(dict(lam=lam, ell=r, a=a, N_S=ns, stab=so, n_chi=nchi,
                         approx=approx, gb=gb, bal=balance(lam),
                         fits=gb <= BUDGET_GB,
                         s34=(delta == 7 and r == 5 and ns <= S34_NS_CAP)))
    return rows

def render(rows6, rows7):
    L = []
    L.append("# Reduced census — `n = 4`, `ell >= 5`, `a >= 2`, memory by `n_chi`\n")
    L.append("Session 36.  `N_S` by generating-function DP; `n_chi` by orbit enumeration "
             f"(cells with `N_S > {NS_ENUM_CAP}` carry the lower bound `N_S/|Stab|`, marked `~`); "
             f"predicted peak `{MEM_PER:.1e} · n_chi^2` GB (s33's measured compressed-route "
             f"constant) against a `{BUDGET_GB}` GB budget.  Strata: **A** = `delta = 6, ell = 5` "
             "(not permanent-sensitive); **B** = `ell = 6` (permanent-sensitive).  "
             f"`delta = 7, ell = 5, N_S <= {S34_NS_CAP}` is session 34's domain and is not swept here.\n")
    for delta, rows in ((6, rows6), (7, rows7)):
        for ell in (5, 6):
            sub = [x for x in rows if x['ell'] == ell]
            if not sub: continue
            strat = 'A' if ell == 5 else 'B'
            fits = [x for x in sub if x['fits'] and not x['s34']]
            L.append(f"\n## `delta = {delta}`, `ell = {ell}` — stratum {strat}"
                     + (" (delta 7, ell 5: outside the brief's strata; s34 domain marked)" if (delta, ell) == (7, 5) else "") + "\n")
            L.append(f"{len(sub)} cells; {sum(1 for x in sub if x['fits'])} fit the budget"
                     + (f", of which {len(fits)} outside s34's domain" if delta == 7 and ell == 5 else "")
                     + f"; ambient units {sum(x['a'] for x in sub)}, fitting {sum(x['a'] for x in sub if x['fits'])}.\n")
            L.append("| lam | a | balance | N_S | Stab | n_chi | GB | fits |")
            L.append("|---|---|---|---|---|---|---|---|")
            for x in sorted(sub, key=lambda x: x['n_chi']):
                L.append(f"| `{x['lam']}` | {x['a']} | {x['bal']} | {x['N_S']} | {x['stab']} | "
                         f"{x['approx']}{x['n_chi']} | {x['gb']:.2f} | "
                         f"{'yes' if x['fits'] else 'no'}{' (s34)' if x['s34'] else ''} |")
    return "\n".join(L) + "\n"

if __name__ == '__main__':
    t = time.time()
    r6 = census(6); print("delta 6:", len(r6), f"{time.time()-t:.0f}s", flush=True)
    r7 = census(7); print("delta 7:", len(r7), f"{time.time()-t:.0f}s", flush=True)
    pickle.dump((r6, r7), open('/root/s36/census.pkl', 'wb'))
    out = sys.argv[1] if len(sys.argv) > 1 else 'results/s36_census.md'
    open(out, 'w').write(render(r6, r7))
    print("wrote", out)
