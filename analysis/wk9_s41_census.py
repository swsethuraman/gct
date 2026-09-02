#!/usr/bin/env python3
"""
Session 41 -- Phase 0: the six-row census (n = 4, ell(lam) = 6, delta = 7, 8).

For every lam |- 4*delta with ell(lam) = 6 and a(lam, delta) >= 1:
  a        route A: Frobenius/power-sum plethysm h_delta[h_4]
                    (wk8_s30_pleth.amb, cross-checked against the separately
                    written scripts/ambient_screen.a at every cell)
           route B: Kostant alternation  a = sum_{w in S_6} sgn(w) m(w(lam+rho) - rho)
                    with m(mu) the weight multiplicity of Sym^delta(Sym^4 C^6),
                    read from ONE dense generating-function table per delta
                    (numpy int32, exact; x_6 eliminated by the degree).
                    Shares no formula with route A.  Asserted equal.
  m_det    the symmetric rectangular Kronecker bound dim (S_lam^*)^{Stab(det_4)}
           (wk9_s38_screen.mdet_weights / m_det_fast, after the n = 3 self-test),
           cross-checked against scripts/ambient_screen.m_det on a sample.
  N_S      weight-space dimension: from the table (route B) and from the
           generating-function DP of wk9_s36_census (asserted equal).
  |Stab|   order of the Young subgroup Stab_W(lam).
  n_chi    dim of the chi_lam-isotypic part by orbit enumeration
           (wk9_s36_stabred.n_chi_of) where N_S <= NS_ENUM_CAP and the bound
           N_S/|Stab| <= NCHI_ENUM_CAP; otherwise the lower bound, marked '~'.
  memory   assembly RSS 1.7e-8 n_chi^2 (s36 measured), peak 2.4e-8 n_chi^2
           (inherited nullspace route, frontier 15500), peak 1.4e-8 n_chi^2 + 0.4
           (in-place rref route, pre-registered frontier 20000).
Cells with lam_1 < delta (not obstruction-eligible, onset-eligible) are listed
separately.  s36-banked cells are marked.

usage: python3 wk9_s41_census.py [--out results/sixrow_census.md] [--deltas 7,8]
"""
import sys, os, time, pickle, itertools
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..')
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
sys.setrecursionlimit(400000)
import numpy as np
from math import factorial
from collections import Counter
from wk8_s30_pleth import amb
from ambient_screen import a as amb_a, m_det as m_det_ref, chi
from wk9_s38_screen import mdet_weights, m_det_fast
from wk9_s36_census import N_S as N_S_dp, stab_order, balance
from wk9_s36_stabred import n_chi_of, exps, monomials

MEM_ASM = 1.7e-8          # GB per n_chi^2, assembly RSS (s36 measured)
MEM_PEAK_NULL = 2.4e-8    # GB per n_chi^2, peak inside flint nullspace (s36 measured)
MEM_PEAK_INPL = 1.4e-8    # GB per n_chi^2, peak of the in-place rref route (measured this session)
MEM_INPL_BASE = 0.4       # GB, sparse M + interpreter
FRONT_NULL = 15500        # inherited frontier (n_chi)
FRONT_INPL = 20000        # pre-registered frontier for the in-place route (n_chi)
NS_ENUM_CAP = 3000000
NCHI_ENUM_CAP = 40000
R = 6
RHO = (5, 4, 3, 2, 1, 0)

def log(*a):
    print(*a, file=sys.stderr, flush=True)

# ----------------------------------------------------------- route B table
def weight_table(delta, n=4, r=R):
    """T[d][mu_1..mu_{r-1}] = number of multisets of d exponent vectors
    (of Sym^n C^r) summing to (mu_1..mu_{r-1}, n d - sum).  Exact int32."""
    L = n * delta + 1
    shape = (delta + 1,) + (L,) * (r - 1)
    T = np.zeros(shape, dtype=np.int32)
    T[(0,) + (0,) * (r - 1)] = 1
    for al in exps(n, r):
        sh = al[:r - 1]
        src = tuple(slice(0, L - s) for s in sh)
        dst = tuple(slice(s, L) for s in sh)
        for d in range(1, delta + 1):
            # multiply by 1/(1 - t x^al): T_new[d] = T[d] + shift(T_new[d-1], al)
            T[d][dst] += T[d - 1][src]
    mx = int(T[delta].max())
    assert mx < 2 ** 31 - 1, mx
    return T

def mult_of(T, delta, mu, n=4, r=R):
    """weight multiplicity m(mu) from the table (0 if any part negative)."""
    if any(x < 0 for x in mu): return 0
    if sum(mu) != n * delta: return 0
    return int(T[(delta,) + tuple(mu[:r - 1])])

def perm_sign(p):
    s = 1
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]: s = -s
    return s

PERMS = [(p, perm_sign(p)) for p in itertools.permutations(range(R))]

def a_kostant(T, delta, lam):
    lam = tuple(lam) + (0,) * (R - len(lam))
    lr = [lam[i] + RHO[i] for i in range(R)]
    tot = 0
    for p, s in PERMS:
        mu = tuple(lr[p[i]] - RHO[i] for i in range(R))
        if min(mu) < 0: continue
        tot += s * mult_of(T, delta, mu)
    return tot

# ------------------------------------------------------------------ census
def banked_s36():
    """ell = 6 cells banked by s36: ledger Stratum B and the a = 1 extension."""
    out = {}
    for ln in open(os.path.join(ROOT, 'results', 's36_ledger.md')):
        if ln.startswith('| B |'):
            c = [x.strip() for x in ln.strip().strip('|').split('|')]
            lam = eval(c[1].strip('`'))
            out[lam] = ('s36 B', int(c[10]), int(c[11]))
    for ln in open(os.path.join(ROOT, 'results', 's36_aone.md')):
        if ln.startswith('| 6 |'):
            c = [x.strip() for x in ln.strip().strip('|').split('|')]
            lam = eval(c[2].strip('`'))
            out[lam] = ('s36 a=1', int(c[7]), int(c[8]))
    return out

def census(delta, n=4):
    t0 = time.time()
    log(f"[census] delta={delta}: route A plethysm ...")
    A = amb(delta, n, R)
    lams = sorted(l for l in A if len(l) == R)
    log(f"[census] delta={delta}: {len(lams)} ell=6 weights with a>=1, "
        f"{sum(A[l] for l in lams)} units ({time.time()-t0:.0f}s); route B table ...")
    T = weight_table(delta)
    log(f"[census] table built ({time.time()-t0:.0f}s); m_det weights ...")
    Ws = mdet_weights(delta, n)
    chi.cache_clear()
    log(f"[census] |W-support| = {len(Ws)} ({time.time()-t0:.0f}s)")
    banked = banked_s36()
    rows = []
    for k, lam in enumerate(lams):
        aA = A[lam]
        aA2 = amb_a(lam, delta, d=n, nv=R)
        aB = a_kostant(T, delta, lam)
        assert aA == aA2 == aB, ("a routes disagree", lam, aA, aA2, aB)
        ns_T = mult_of(T, delta, lam)
        ns_dp = N_S_dp(n, R, delta, lam)
        assert ns_T == ns_dp, ("N_S routes disagree", lam, ns_T, ns_dp)
        so = stab_order(lam)
        md = m_det_fast(lam, Ws)
        if (k + 1) % 60 == 0: chi.cache_clear()
        bound = (ns_T + so - 1) // so
        if ns_T <= NS_ENUM_CAP and bound <= NCHI_ENUM_CAP:
            ns2, nchi, so2 = n_chi_of(n, R, delta, lam)
            assert ns2 == ns_T and so2 == so, (lam, ns2, ns_T, so2, so)
            approx = ''
            monomials.cache_clear()
        else:
            nchi, approx = bound, '~'
        rows.append(dict(lam=lam, delta=delta, a=aA, m_det=md, forced=aA > md,
                         N_S=ns_T, stab=so, n_chi=nchi, approx=approx, bal=balance(lam),
                         gb_asm=MEM_ASM * nchi * nchi, gb_null=MEM_PEAK_NULL * nchi * nchi,
                         gb_inpl=MEM_PEAK_INPL * nchi * nchi + MEM_INPL_BASE,
                         reach_null=nchi <= FRONT_NULL, reach_inpl=nchi <= FRONT_INPL,
                         eligible=lam[0] >= delta, banked=banked.get(lam)))
        if (k + 1) % 50 == 0:
            log(f"[census] delta={delta}: {k+1}/{len(lams)} ({time.time()-t0:.0f}s)")
    # m_det cross-check on a sample (the screen's own discipline)
    for x in rows[:4] + rows[-4:]:
        assert x['m_det'] == m_det_ref(x['lam'], n, delta), ("m_det route mismatch", x['lam'])
    chi.cache_clear()
    log(f"[census] delta={delta} done ({time.time()-t0:.0f}s)")
    return rows

def render(all_rows):
    L = []
    L.append("# Six-row census — `n = 4`, `ℓ(λ) = 6`, `a ≥ 1`, degrees 7 and 8\n")
    L.append("Session 41 (`analysis/wk9_s41_census.py`).  `a` by two independent routes "
             "(Frobenius plethysm, and Kostant alternation over a dense weight-multiplicity table), asserted equal at every cell; "
             "`N_S` by the same table and by the generating-function DP, asserted equal; "
             "`m_det` = the symmetric rectangular Kronecker bound `dim (S_λ^*)^{Stab(det_4)}` "
             "(`wk9_s38_screen`, self-tested on the `n = 3` anchors `3, 11`); `n_χ` by orbit enumeration "
             f"(cells with `N_S > {NS_ENUM_CAP}` or bound `> {NCHI_ENUM_CAP}` carry the bound `N_S/|Stab|`, marked `~`).  "
             f"Memory: assembly `{MEM_ASM:.1e}·n_χ²` GB; peak `{MEM_PEAK_NULL:.1e}·n_χ²` (inherited nullspace route, frontier `n_χ ≤ {FRONT_NULL}`) "
             f"and `{MEM_PEAK_INPL:.1e}·n_χ² + {MEM_INPL_BASE}` (in-place rref route, pre-registered frontier `n_χ ≤ {FRONT_INPL}`, "
             "operative only after the validation of `results/PREREG_s41.md` §1).  "
             "`forced` = `a > m_det` (a det-side equation by arithmetic alone).  "
             "Obstruction-eligible cells have `λ_1 ≥ δ`; the `λ_1 < δ` cells are listed separately (onset-eligible only).\n")
    # feasibility line
    L.append("## Feasibility\n")
    L.append("| δ | cells (`λ_1 ≥ δ`) | units | forced (`a > m_det`) | reachable at 15500 | units | reachable at 20000 | units | banked by s36 | units | onset-only cells (`λ_1 < δ`) |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|")
    for delta in sorted(all_rows):
        rows = all_rows[delta]
        el = [x for x in rows if x['eligible']]
        oo = [x for x in rows if not x['eligible']]
        rn = [x for x in el if x['reach_null']]
        ri = [x for x in el if x['reach_inpl']]
        bk = [x for x in el if x['banked']]
        L.append(f"| {delta} | {len(el)} | {sum(x['a'] for x in el)} | {sum(1 for x in el if x['forced'])} | "
                 f"{len(rn)} | {sum(x['a'] for x in rn)} | {len(ri)} | {sum(x['a'] for x in ri)} | "
                 f"{len(bk)} | {sum(x['a'] for x in bk)} | {len(oo)} (min `n_χ` {min((x['n_chi'] for x in oo), default='-')}) |")
    L.append("")
    for delta in sorted(all_rows):
        rows = all_rows[delta]
        el = [x for x in rows if x['eligible']]
        L.append(f"\n## `δ = {delta}` — {len(el)} obstruction-eligible cells, {sum(x['a'] for x in el)} ambient units\n")
        # by a
        byA = Counter(); byAr = Counter()
        for x in el:
            byA[x['a']] += 1
            if x['reach_inpl']: byAr[x['a']] += 1
        L.append("Cells by `a` (total / reachable at 20000): " +
                 ", ".join(f"`a={k}`: {byA[k]}/{byAr[k]}" for k in sorted(byA)) + ".\n")
        byB = Counter(); byBr = Counter()
        for x in el:
            byB[x['bal']] += 1
            if x['reach_inpl']: byBr[x['bal']] += 1
        L.append("Cells by balance `λ_1 − λ_6` (total / reachable at 20000): " +
                 ", ".join(f"{k}: {byB[k]}/{byBr[k]}" for k in sorted(byB)) + ".\n")
        mn = min(x['m_det'] - x['a'] for x in el)
        tight = sorted(el, key=lambda x: (x['m_det'] - x['a'], -x['a']))[:5]
        L.append(f"Arithmetic map: `a > m_det` at {sum(1 for x in el if x['forced'])} cells; tightest margins `m_det − a`: " +
                 ", ".join(f"`{x['lam']}` ({x['m_det']} − {x['a']} = {x['m_det']-x['a']})" for x in tight) + ".\n")
        L.append("| lam | a | m_det | forced | balance | N_S | Stab | n_chi | GB asm | GB peak (null) | GB peak (inpl) | reach 15500 | reach 20000 | s36 |")
        L.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
        for x in sorted(el, key=lambda x: (x['n_chi'], x['lam'])):
            b = x['banked']
            L.append(f"| `{x['lam']}` | {x['a']} | {x['m_det']} | {'**yes**' if x['forced'] else 'no'} | {x['bal']} | {x['N_S']} | {x['stab']} | "
                     f"{x['approx']}{x['n_chi']} | {x['gb_asm']:.2f} | {x['gb_null']:.2f} | {x['gb_inpl']:.2f} | "
                     f"{'yes' if x['reach_null'] else 'no'} | {'yes' if x['reach_inpl'] else 'no'} | "
                     f"{(b[0] + ' (det ' + str(b[1]) + ', pad ' + str(b[2]) + ')') if b else ''} |")
        oo = [x for x in rows if not x['eligible']]
        if oo:
            L.append(f"\n### `δ = {delta}`, onset-only cells (`λ_1 < δ`; cannot be obstructions, can carry the det ideal)\n")
            L.append("| lam | a | m_det | N_S | Stab | n_chi | GB peak (inpl) | reach 20000 |")
            L.append("|---|---|---|---|---|---|---|---|")
            for x in sorted(oo, key=lambda x: (x['n_chi'], x['lam'])):
                L.append(f"| `{x['lam']}` | {x['a']} | {x['m_det']} | {x['N_S']} | {x['stab']} | {x['approx']}{x['n_chi']} | "
                         f"{x['gb_inpl']:.2f} | {'yes' if x['reach_inpl'] else 'no'} |")
    return "\n".join(L) + "\n"

if __name__ == '__main__':
    out = sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv else os.path.join(ROOT, 'results', 'sixrow_census.md')
    deltas = [int(x) for x in (sys.argv[sys.argv.index('--deltas') + 1] if '--deltas' in sys.argv else '7,8').split(',')]
    os.makedirs('/root/s41', exist_ok=True)
    allrows = {}
    for delta in deltas:
        allrows[delta] = census(delta)
        pickle.dump(allrows, open('/root/s41/census.pkl', 'wb'))
        open(out, 'w').write(render(allrows))
        log(f"wrote {out} (deltas {sorted(allrows)})")
