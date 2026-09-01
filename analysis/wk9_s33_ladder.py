#!/usr/bin/env python3
"""
Session 33, Phase 1 -- the ambient ladder for the e4 hunt.

    a(delta) = <h_delta[h_4], s_{(delta^4)}>  =  dim of degree-delta
    SL_4-invariants of quartic surfaces  =  mult of S_{(delta^4)} in
    Sym^delta(Sym^4 C^4),

for delta = 1..24, by the weight-multiplicity route: a numpy DP computes
dim of every weight space of Sym^delta(Sym^4 C^4), and

    mult_lam = sum_{w in S_4} sgn(w) . dimWt(lam + rho - w(rho)),  rho=(3,2,1,0).

Also computed, for the ledger and the reduced-pipeline budget:
  N_S(delta)  = dimWt((delta^4))          -- the weight-space dimension
  N'(delta)   = dimWt((delta+1, delta-1, delta, delta))  -- E_12 target space
  n_chi(delta) = dim of the sign^delta-isotypic part of the S_4
                 variable-permutation action on the weight-(delta^4) basis
                 (Burnside over the five classes, per-class DP on sigma-orbits)

Self-checks (P5 of results/PREREG_s33.md), all assert:
  T1 brute-force multiset enumeration at delta <= 4 (N_S, dims, a, n_chi)
  T2 a(1..8) == (0,0,0,1,0,1,1,3)   [s29's published anchors]
  T3 a(10) >= 1                      [degree-10 catalecticant exists]
  T4 N_S(6) = 12652, N_S(7) = 57232  [s29's recorded dimensions]
  T5 pleth cross-check vs analysis/wk8_s30_pleth.py (delta <= 9, single-lam)
  T6 the r = 2 witness arithmetic: mult of s_(4,4) in Sym^2(Sym^4 C^2) = 1
Independent routes only meet in the asserts; no route feeds another.
"""
import itertools, sys, time
from functools import lru_cache
import numpy as np

sys.path.insert(0, 'analysis')
from wk8_s30_pleth import pleth_p, chi  # reused, not rewritten

T = 24
S = 4 * T  # max tracked value of each of the first three weight coordinates

def exps4():
    out = []
    for a in range(5):
        for b in range(5 - a):
            for c in range(5 - a - b):
                out.append((a, b, c, 4 - a - b - c))
    return out

MON = exps4()
assert len(MON) == 35

def run_dp(items):
    """dp[t, a, b, c] = # multisets of t items whose weight-sum has first
    three coordinates (a, b, c); items = [(step_t, (w1, w2, w3)), ...]."""
    dp = np.zeros((T + 1, S + 1, S + 1, S + 1), dtype=np.int64)
    dp[0, 0, 0, 0] = 1
    for k, (w1, w2, w3) in items:
        for t in range(k, T + 1):
            dp[t, w1:, w2:, w3:] += dp[t - k, :S + 1 - w1, :S + 1 - w2, :S + 1 - w3]
    return dp

def dimwt(dp, t, mu):
    if any(x < 0 for x in mu) or sum(mu) != 4 * t: return 0
    if any(x > S for x in mu[:3]): return 0
    return int(dp[t, mu[0], mu[1], mu[2]])

RHO = (3, 2, 1, 0)
PERMS = list(itertools.permutations(range(4)))
def sgn(p):
    s = 1
    for i in range(4):
        for j in range(i + 1, 4):
            if p[i] > p[j]: s = -s
    return s

def mult_rect(dp, delta):
    lam_rho = (delta + 3, delta + 2, delta + 1, delta)
    tot = 0
    for p in PERMS:
        mu = tuple(lam_rho[i] - RHO[p[i]] for i in range(4))
        tot += sgn(p) * dimwt(dp, delta, mu)
    return tot

# ---------------------------------------------------------------- sigma orbits
def orbits_of(perm):
    """orbits of the variable permutation on the 35 monomials; perm maps
    position i -> perm[i]: (sigma.alpha)[perm[i]] = alpha[i]."""
    idx = {m: i for i, m in enumerate(MON)}
    seen, orbs = set(), []
    for m in MON:
        if m in seen: continue
        orb, cur = [], m
        while cur not in seen:
            seen.add(cur); orb.append(cur)
            nxt = [0] * 4
            for i in range(4): nxt[perm[i]] = cur[i]
            cur = tuple(nxt)
        w = tuple(sum(x[j] for x in orb) for j in range(3))
        orbs.append((len(orb), w))
    return orbs

CLASS_REPS = {  # rep perm (as mapping tuple), class size, sign
    'id':  ((0, 1, 2, 3), 1, +1),
    't':   ((1, 0, 2, 3), 6, -1),
    'c3':  ((1, 2, 0, 3), 8, +1),
    'c4':  ((1, 2, 3, 0), 6, -1),
    'c22': ((1, 0, 3, 2), 3, +1),
}

def main():
    t0 = time.time()
    dps = {}
    dps['id'] = run_dp([(1, m[:3]) for m in MON])
    for k in ('t', 'c3', 'c4', 'c22'):
        dps[k] = run_dp(orbits_of(CLASS_REPS[k][0]))
    print(f"# DPs built in {time.time()-t0:.1f}s", file=sys.stderr)

    NS  = {d: dimwt(dps['id'], d, (d, d, d, d)) for d in range(1, T + 1)}
    NP  = {d: dimwt(dps['id'], d, (d + 1, d - 1, d, d)) for d in range(1, T + 1)}
    A   = {d: mult_rect(dps['id'], d) for d in range(1, T + 1)}
    FIX = {k: {d: dimwt(dps[k], d, (d, d, d, d)) for d in range(1, T + 1)}
           for k in CLASS_REPS}
    NCHI = {}
    for d in range(1, T + 1):
        tr = sum(sz * FIX[k][d] for k, (_, sz, _) in CLASS_REPS.items())
        sg = sum(sz * sg_ * FIX[k][d] for k, (_, sz, sg_) in CLASS_REPS.items())
        assert tr % 24 == 0 and sg % 24 == 0, d
        NCHI[d] = (tr // 24) if d % 2 == 0 else (sg // 24)

    # T1 -- brute force, delta <= 4
    for d in (2, 3, 4):
        wt = {}
        basis = []
        for c in itertools.combinations_with_replacement(range(35), d):
            m = tuple(sum(MON[i][j] for i in c) for j in range(4))
            wt[m] = wt.get(m, 0) + 1
            if m == (d, d, d, d): basis.append(c)
        assert wt.get((d, d, d, d), 0) == NS[d], ('T1 N_S', d)
        lam_rho = (d + 3, d + 2, d + 1, d)
        ab = sum(sgn(p) * wt.get(tuple(lam_rho[i] - RHO[p[i]] for i in range(4)), 0)
                 for p in PERMS)
        assert ab == A[d], ('T1 a', d, ab, A[d])
        # orbit count under S_4 with character sign^d, brute
        def act(perm, c):
            out = []
            for i in c:
                al = MON[i]; nx = [0] * 4
                for j in range(4): nx[perm[j]] = al[j]
                out.append(MON.index(tuple(nx)))
            return tuple(sorted(out))
        nb = 0
        seen = set()
        for c in basis:
            if c in seen: continue
            orb = {}
            for p in PERMS: orb.setdefault(act(p, c), []).append(sgn(p) ** d)
            for k in orb: seen.add(k)
            stab_ok = all(sum(v) != 0 for v in orb.values())  # char trivial on stab
            if stab_ok: nb += 1
        assert nb == NCHI[d], ('T1 n_chi', d, nb, NCHI[d])
    print("# T1 pass (brute delta<=4: N_S, a, n_chi)", file=sys.stderr)

    # T2, T3, T4
    assert [A[d] for d in range(1, 9)] == [0, 0, 0, 1, 0, 1, 1, 3], \
        ('T2 fail', [A[d] for d in range(1, 9)])
    assert A[10] >= 1, ('T3 fail', A[10])
    assert NS[6] == 12652 and NS[7] == 57232, ('T4 fail', NS[6], NS[7])
    print("# T2, T3, T4 pass (s29 anchors, catalecticant, N_S records)", file=sys.stderr)

    # T5 -- plethysm route (wk8_s30_pleth), single-lam evaluation
    for d in range(1, 10):
        P = pleth_p(d, 4)
        lam = tuple(x for x in (d, d, d, d) if x)
        v = sum(c * chi(lam, rho) for rho, c in P.items())
        assert v.denominator == 1 and int(v) == A[d], ('T5 fail', d, v, A[d])
    print("# T5 pass (pleth route agrees, delta <= 9)", file=sys.stderr)

    # T6 -- the r = 2 arithmetic behind the witness cell
    wt2 = {}
    for c in itertools.combinations_with_replacement(range(5), 2):
        m = (c[0] + c[1], 8 - c[0] - c[1])
        wt2[m] = wt2.get(m, 0) + 1
    m44 = wt2.get((4, 4), 0) - wt2.get((5, 3), 0)
    assert m44 == 1, ('T6 fail', m44)
    print("# T6 pass (r=2 witness arithmetic)", file=sys.stderr)

    # the ladder
    print("| delta | a | N_S | GB(unred, 5.6e-8 N_S^2) | n_chi | N' | GB(red matrix, 8 N' n_chi) |")
    print("|---|---|---|---|---|---|---|")
    for d in range(1, T + 1):
        gb_u = 5.6e-8 * NS[d] ** 2
        gb_r = 8 * NP[d] * NCHI[d] / 1e9
        print(f"| {d} | {A[d]} | {NS[d]} | {gb_u:.3g} | {NCHI[d]} | {NP[d]} | {gb_r:.3g} |")
    print(f"# total {time.time()-t0:.1f}s", file=sys.stderr)

if __name__ == '__main__':
    main()
