#!/usr/bin/env python3
"""
Session 30 -- dimensions of the two short-weight varieties at r = 5.

A weight of length r sees a form f only through the short-weight reduction
    D_r^f = closure{ f(s_1 A_1 + ... + s_r A_r) }  <=  Sym^n C^r,
so at n = 4, r = 5 both sides of this sweep live in Sym^4 C^5, dim 70.

dim D_5^f is the generic rank of the Jacobian of the parametrisation
    Phi : (A_1, ..., A_5) |--> coefficients of f(sum s_i A_i).
The derivative is taken EXACTLY, not by finite differences: arithmetic runs in
the dual numbers F_P[t]/(t^2), so the coefficient of t in Phi(A + t E_k) is the
partial derivative with no truncation error.  Generic rank is attained off a
proper closed subset, so a random point gives it with probability 1; the rank
is confirmed at three independent random points and over two primes.

This is a line of evidence SEPARATE from the sweep: it bounds how much room
there is for an ideal at all, without measuring any multiplicity.
"""
import sys, random
from itertools import permutations, combinations_with_replacement
from flint import nmod_mat

PRIMES = (2147483647, 2147483629)

# ---- dual numbers a + b t over F_P, t^2 = 0 -------------------------------
def dmul(x, y, P): return ((x[0] * y[0]) % P, (x[0] * y[1] + x[1] * y[0]) % P)
def dadd(x, y, P): return ((x[0] + y[0]) % P, (x[1] + y[1]) % P)

# ---- polynomials in s_1..s_r with dual coefficients -----------------------
def pmul(a, b, P):
    out = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            k = tuple(sorted(ka + kb))
            out[k] = dadd(out.get(k, (0, 0)), dmul(va, vb, P), P)
    return out

def padd(out, t, P):
    for k, v in t.items():
        out[k] = dadd(out.get(k, (0, 0)), v, P)

def parity(perm):
    vis = [False] * len(perm); par = 0
    for i in range(len(perm)):
        if not vis[i]:
            j, c = i, 0
            while not vis[j]: vis[j] = True; j = perm[j]; c += 1
            par += c - 1
    return par % 2

def lin(coords, idx, r, P):
    """The linear form sum_i s_i * coords[i][idx], as a poly with dual coeffs."""
    return {(i,): coords[i][idx] for i in range(r)}

def det4(coords, r, P):
    """det of the 4x4 matrix whose (p,q) entry is sum_i s_i A_i[p][q]."""
    out = {}
    for perm in permutations(range(4)):
        term = {(): (1, 0)}
        for p in range(4):
            term = pmul(term, lin(coords, p * 4 + perm[p], r, P), P)
        if parity(perm):
            term = {k: ((-v[0]) % P, (-v[1]) % P) for k, v in term.items()}
        padd(out, term, P)
    return out

def padper3(coords, r, P):
    """x_0 . per_3(M): coordinate 0 is x_0, coordinates 1..9 are M row-major."""
    out = {}
    for perm in permutations(range(3)):
        term = lin(coords, 0, r, P)
        for p in range(3):
            term = pmul(term, lin(coords, 1 + p * 3 + perm[p], r, P), P)
        padd(out, term, P)
    return out

def jac_rank(form, nvar, r, P, seed):
    """Rank of dPhi at a random point.  nvar = coords per A_i."""
    rnd = random.Random(seed)
    A = [[(rnd.randrange(1, P), 0) for _ in range(nvar)] for _ in range(r)]
    keys = sorted(combinations_with_replacement(range(r), 4))
    kidx = {k: c for c, k in enumerate(keys)}
    M = nmod_mat(r * nvar, len(keys), P)
    row = 0
    for i in range(r):
        for j in range(nvar):
            save = A[i][j]
            A[i][j] = (save[0], 1)            # seed the dual unit here
            poly = form(A, r, P)
            A[i][j] = save
            for k, v in poly.items():
                if v[1] % P: M[row, kidx[k]] = v[1] % P   # d/dA_ij
            row += 1
    return M.rank(), len(keys)

if __name__ == '__main__':
    r = 5
    print("Sym^4 C^5 has dimension %d\n" % len(list(combinations_with_replacement(range(r), 4))))
    for name, form, nvar in (("D_5^det4      ", det4, 16),
                             ("D_5^pad(per_3)", padper3, 10)):
        seen = []
        for P in PRIMES:
            for seed in (1, 2, 3):
                rk, amb = jac_rank(form, nvar, r, P, seed)
                seen.append(rk)
        rk = max(seen)
        assert len(set(seen)) == 1, (name, seen)
        print("%s : params %3d  dim %2d  codim in Sym^4 C^5 = %2d   "
              "(rank agreed at %d random points x %d primes)"
              % (name, r * nvar, rk, amb - rk, 3, len(PRIMES)))
