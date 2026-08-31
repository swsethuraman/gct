#!/usr/bin/env python3
"""
Session 27 -- independent Jacobian ranks for D_r^f.

The map  Phi : (A_1..A_r) in (C^N)^r -> Sym^n C^r,  (A_i) |-> f(sum s_i A_i).
By the chain rule the column of dPhi for the coordinate (A_k)_t is

    s_k . (d f / d x_t)(sum s_i A_i),

so the Jacobian is assembled from the N partial derivatives of f, each
restricted to the r-plane, times s_k.  Rank at one integer point is a PROOF of
dominance where it attains the target (rank is lower semicontinuous).
"""
import sys, random
sys.path.insert(0, '/root/gct/analysis')
from wk7_s27_rank import exps, restrict, det_form, per_form, per_padded, rank_mod
from math import comb

def partials(f, N):
    """d f / d x_t for each t, as dicts (degree n-1)."""
    out = []
    for t in range(N):
        d = {}
        for beta, c in f.items():
            if beta[t] == 0: continue
            nb = list(beta); nb[t] -= 1
            d[tuple(nb)] = d.get(tuple(nb), 0) + c * beta[t]
        out.append(d)
    return out

def jac_rank(f, N, n, r, seed=7, bound=30, primes=(2147483647, 2147483629)):
    rnd = random.Random(seed)
    As = [[rnd.randint(-bound, bound) for _ in range(N)] for _ in range(r)]
    dfs = partials(f, N)
    Eb = exps(n, r)
    idx = {a: i for i, a in enumerate(Eb)}
    cols = []
    for k in range(r):
        for t in range(N):
            g = restrict(dfs[t], N, n - 1, r, As)      # degree n-1 in s
            v = [0] * len(Eb)
            for al, c in g.items():
                na = list(al); na[k] += 1
                v[idx[tuple(na)]] += c
            cols.append(v)
    rks = [rank_mod(cols, len(Eb), p) for p in primes]
    assert rks[0] == rks[1], (n, r, rks)
    return rks[0], len(Eb)

if __name__ == '__main__':
    print("f            n  r   rank   target   dense?   predicted bound")
    def row(name, f, N, n, r, bound_expr):
        rk, tgt = jac_rank(f, N, n, r)
        print("%-12s %d  %d  %5d  %6d   %-6s   %s"
              % (name, n, r, rk, tgt, "YES" if rk == tgt else "no", bound_expr))
        return rk
    d3, N3 = det_form(3); p3, _ = per_form(3)
    d4, N4 = det_form(4); pp, Np = per_padded(3)
    print("--- session 26's n=3 rows, reproduced independently ---")
    for r in (2, 3, 4, 5, 6):
        row("det_3", d3, N3, 3, r, "min(C(r+2,3), 9r-16)")
    for r in (4, 5, 6):
        row("per_3", p3, N3, 3, r, "min(C(r+2,3), 9r-4)")
    print("--- n=4: the determinant and the padded permanent ---")
    for r in (3, 4, 5):
        row("det_4", d4, N4, 4, r, "min(C(r+3,4), 16r-30)")
    for r in (3, 4, 5, 6):
        rk = row("per_3^pad", pp, Np, 4, r, "reducible locus r+C(r+2,3)-1")
        print("             closed form r + C(r+2,3) - 1 = %d   %s"
              % (r + comb(r + 2, 3) - 1,
                 "MATCH" if rk == r + comb(r + 2, 3) - 1 else "*** MISMATCH ***"))
