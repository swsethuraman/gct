#!/usr/bin/env python3
"""
Session 46 -- exact n_chi (and exact N_S) for any six-row cell, without
enumerating a single monomial.

results/sixrow_census.md carries n_chi by orbit enumeration only for the small
cells; every cell with N_S > 3,000,000 or bound > 40,000 carries the BOUND
N_S/|Stab| instead, marked `~`.  That bound is neither an upper nor a lower
bound on n_chi in general (orbits shorter than |Stab| push the orbit count up,
dropped orbits push n_chi down), and at the balanced cells this session needs it
is wrong in both directions: at (8,8,5,5,1,1)_7 the bound is 75,474 and the
measured n_chi is 62,613; at (8,8,6,2,2,2)_7 the bound is 98,744 and the
measured n_chi is 114,875.  The reach table cannot be built on it.

The exact value is a character count.  The lam-weight space has the monomials as
a basis and Stab_W(lam) permutes them, so

    n_chi = dim V_chi = <perm character, chi> = (1/|Stab|) sum_g chi(g) Fix(g),

and Fix(g) -- the number of weight-lam monomials fixed by g -- is a small DP: a
multiset of exponent vectors is g-invariant iff it is a union of <g>-orbits of
exponent vectors taken with a constant multiplicity, so

    Fix(g) = #{ (c_O)_{O in orbits of <g> on exps} :
                sum_O c_O |O| = delta,  sum_O c_O sigma_O = lam },
                                        sigma_O = sum_{alpha in O} alpha.

Taking g = identity gives N_S itself, so both numbers come out of one routine
and each is available as a cross-check against the census.  Cost: |Stab| DPs
over (partial degree, partial weight), independent of N_S.
"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from wk8_s30_core import exps
from wk9_s36_stabred import stab_group, perm_tables
from wk8_s30_pleth import a_of
from functools import lru_cache

def _orbit_data(tab, A):
    """<g>-orbits on the exponent set: [(size, weight-sum tuple)]."""
    L = len(A); seen = [False] * L; out = []
    for k in range(L):
        if seen[k]: continue
        cyc = []; x = k
        while not seen[x]:
            seen[x] = True; cyc.append(x); x = tab[x]
        w = [0] * len(A[0])
        for c in cyc:
            for i, v in enumerate(A[c]): w[i] += v
        out.append((len(cyc), tuple(w)))
    return out

def fix_count(orbs, delta, lam):
    """#{(c_O) : sum c_O |O| = delta, sum c_O sigma_O = lam}."""
    r = len(lam)
    cur = {(0,) + (0,) * r: 1}
    for size, w in orbs:
        nxt = {}
        for st, c in cur.items():
            k = st[0]; wt = st[1:]
            m = 0
            while True:
                nk = k + m * size
                if nk > delta: break
                nw = tuple(wt[i] + m * w[i] for i in range(r))
                if any(nw[i] > lam[i] for i in range(r)): break
                key = (nk,) + nw
                nxt[key] = nxt.get(key, 0) + c
                m += 1
        cur = nxt
    return cur.get((delta,) + tuple(lam), 0)

@lru_cache(maxsize=None)
def census_cell(lam, delta, n=4):
    """(N_S, n_chi, |Stab|, a) -- all exact, no monomial enumerated."""
    lam = tuple(lam); r = len(lam)
    A = exps(n, r)
    group = stab_group(lam)
    tabs = perm_tables(n, r, group)
    tot = 0; N_S = None
    for (tab, ch), (p, _) in zip(tabs, group):
        f = fix_count(_orbit_data(tab, A), delta, lam)
        if all(p[i] == i for i in range(r)): N_S = f
        tot += ch * f
    assert tot % len(group) == 0, ("character count not an integer", lam, delta, tot, len(group))
    return N_S, tot // len(group), len(group), a_of(lam, delta, n, r)

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        v = [int(x) for x in arg.split(',')]
        d, lam = v[0], tuple(v[1:])
        N_S, nchi, st, a = census_cell(lam, d)
        print(json.dumps(dict(lam=list(lam), delta=d, N_S=N_S, n_chi=nchi, stab=st, a=a,
                              bal=lam[0] - lam[-1], elig=lam[0] >= d)))

# ------------------------------------------------------------------ nrows
def rows_cell(lam, delta, n=4):
    """The exact row count of E: for each simple raising operator E_{i,i+1} the
    rows kept are the non-dropped H-orbits of the target basis (weight
    lam + e_i - e_{i+1}), H = Stab(lam) cap Stab(lam') the elements fixing i and
    i+1, so the count is the SAME character formula with (H, chi|_H):

        rows_i = (1/|H|) sum_{h in H} chi(h) Fix_{lam'}(h).

    Exact and enumeration-free, like n_chi.  It is an UPPER bound on the E built
    by wk9_s46_gen only in that rows which come out identically zero are dropped
    there; measured against the ten cells that have been built, the two agree to
    better than 0.01 %."""
    lam = tuple(lam); r = len(lam)
    A = exps(n, r)
    tot = 0
    for i in range(r - 1):
        j = i + 1
        if lam[j] == 0: continue
        # E_{i,i+1} vanishes IDENTICALLY on V_chi when i, i+1 lie in a common
        # block of value 1: spins are bounded by j <= m, so the sign-isotypic
        # part of a value-1 block is entirely spin 0 (docs/stabiliser_reduction.md
        # section 1, the second proof of the lemma).  Those rows never appear.
        if lam[i] == 1 and lam[j] == 1: continue
        tgt = tuple(lam[k] + (1 if k == i else (-1 if k == j else 0)) for k in range(r))
        H = stab_group(lam, fix=(i, j))
        tabs = perm_tables(n, r, H)
        s = 0
        for (tab, ch) in tabs:
            s += ch * fix_count(_orbit_data(tab, A), delta, tgt)
        assert s % len(H) == 0, ("row character count not an integer", lam, i)
        tot += s // len(H)
    return tot
