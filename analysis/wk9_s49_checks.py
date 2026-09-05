#!/usr/bin/env python3
"""Session 49 exact checks (results/PREREG_s49.md, M2 and the r <= 4 containment).

A. Dominance of N |-> det_3(N(s)) onto Sym^3 C^r for r <= 4 by one full-rank
   Jacobian point (Lemma 1 of docs/washout_lemma.md): rank dPhi at a random
   integer point modulo both house primes, r = 2..5 (r = 5 must fall short:
   29 < 35, the length-5 failure of the block construction).

B. Theorem C, density at r = 3 for every m: at the structured point
   A(s) = s_1 I + s_2 diag(w, w^2, ..., w^m) + s_3 P (P the cyclic shift,
   w a primitive m-th root of unity taken modulo a prime p = 1 mod m), the
   Jacobian of (A_1, A_2, A_3) |-> per_m(A(s)) has full rank C(m+2, 2).  The
   sub-permanents are computed by a generic Laplace routine that knows nothing
   of the closed form in docs/washout_threshold.md.

C. The window lemma behind B: for x_r = s_1 + w^r s_2 and 1 <= j <= m-1, the m
   cyclic-window products prod_{r=a}^{a+j-1} x_r span Sym^j C^2; checked as a
   rank over F_p for m up to 40.

usage: wk9_s49_checks.py A|B|C [mmax]
"""
import sys, random, itertools, math
from flint import nmod_mat, fmpz

SEED = 20260905
P1, P2 = 2147483647, 2147483629


def monos(r, d):
    if r == 1:
        return [(d,)]
    out = []
    for a in range(d, -1, -1):
        for rest in monos(r - 1, d - a):
            out.append((a,) + rest)
    return out


def padd(a, b, sc=1):
    o = dict(a)
    for k, v in b.items():
        o[k] = o.get(k, 0) + sc * v
    return {k: v for k, v in o.items() if v}


def pmul(a, b):
    o = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            k = tuple(x + y for x, y in zip(ka, kb))
            o[k] = o.get(k, 0) + va * vb
    return {k: v for k, v in o.items() if v}


def laplace(ent, rows, cols, sign):
    if len(rows) == 1:
        return ent[rows[0]][cols[0]]
    tot = {}
    i = rows[0]
    for k, j in enumerate(cols):
        e = ent[i][j]
        if not e:
            continue
        sub = laplace(ent, rows[1:], cols[:k] + cols[k + 1:], sign)
        tot = padd(tot, pmul(e, sub), (-1) ** k if sign else 1)
    return tot


def jacobian_rank(ent, r, m, p, sign):
    """rows: s_k * (sub-determinant or sub-permanent at (i,j)); rank mod p over
    the monomials of degree m in r variables."""
    cols = monos(r, m)
    cidx = {c: t for t, c in enumerate(cols)}
    n = len(ent)
    rows = []
    unit = [tuple(1 if t == k else 0 for t in range(r)) for k in range(r)]
    for i in range(n):
        for j in range(n):
            ri = [x for x in range(n) if x != i]
            cj = [x for x in range(n) if x != j]
            q = laplace(ent, ri, cj, sign) if n > 1 else {tuple([0] * r): 1}
            for k in range(r):
                row = [0] * len(cols)
                for mono, v in q.items():
                    row[cidx[tuple(x + y for x, y in zip(mono, unit[k]))]] = v % p
                rows.append(row)
    M = nmod_mat(len(rows), len(cols), [v for rw in rows for v in rw], p)
    return M.rank(), len(cols)


def A_det3():
    print("A. dominance of det_3 pencils onto Sym^3 C^r (seed 20260905, box 1e3)")
    for r in (2, 3, 4, 5):
        rnd = random.Random(SEED + 300 + r)
        unit = [tuple(1 if t == k else 0 for t in range(r)) for k in range(r)]
        N = [[[rnd.randint(-1000, 1000) for _ in range(3)] for _ in range(3)] for _ in range(r)]
        ent = [[{unit[k]: N[k][i][j] for k in range(r) if N[k][i][j]} for j in range(3)] for i in range(3)]
        ranks = [jacobian_rank(ent, r, 3, p, True) for p in (P1, P2)]
        print(f"  r={r}: rank dPhi = {ranks[0][0]},{ranks[1][0]} of dim Sym^3 = {ranks[0][1]}  "
              f"-> {'DOMINANT' if ranks[0][0] == ranks[0][1] and ranks[1][0] == ranks[1][1] else 'not dominant'}",
              flush=True)


def prime_1_mod(m, start=10 ** 9):
    q = start - (start % m) + 1
    while not fmpz(q).is_probable_prime():
        q += m
    return q


def primitive_root_of_unity(m, p):
    # find g with g^m = 1 and g^k != 1 for 0 < k < m
    for g in range(2, 10 ** 6):
        w = pow(g, (p - 1) // m, p)
        if w != 1 and all(pow(w, k, p) != 1 for k in range(1, m) if m % k == 0):
            return w
    raise RuntimeError("no primitive root found")


def B_theoremC(mmax):
    print("B. Theorem C density at r = 3: Jacobian rank at the structured point (I, diag(w^r), P)")
    for m in range(2, mmax + 1):
        p = prime_1_mod(m)
        w = primitive_root_of_unity(m, p)
        r = 3
        unit = [tuple(1 if t == k else 0 for t in range(r)) for k in range(r)]
        ent = [[{} for _ in range(m)] for _ in range(m)]
        for i in range(m):
            ent[i][i] = {unit[0]: 1, unit[1]: pow(w, i + 1, p)}
            ent[i][(i + 1) % m] = padd(ent[i][(i + 1) % m], {unit[2]: 1})
        rk, dim = jacobian_rank(ent, r, m, p, False)
        print(f"  m={m:2d}: p={p} w={w}: rank dPhi_(m,3) = {rk} of C(m+2,2) = {dim}  "
              f"-> {'FULL' if rk == dim else 'NOT full'}", flush=True)


def C_windows(mmax):
    print("C. window lemma: cyclic-window products of length j span Sym^j C^2, x_r = s_1 + w^r s_2")
    for m in range(2, mmax + 1):
        p = prime_1_mod(m, 10 ** 6)
        w = primitive_root_of_unity(m, p)
        x = [{(1, 0): 1, (0, 1): pow(w, rr + 1, p)} for rr in range(m)]
        bad = []
        for j in range(1, m):
            rows = []
            for a in range(m):
                prod = {(0, 0): 1}
                for t in range(j):
                    prod = pmul(prod, x[(a + t) % m])
                rows.append([prod.get((j - b, b), 0) % p for b in range(j + 1)])
            rk = nmod_mat(m, j + 1, [v for rw in rows for v in rw], p).rank()
            if rk != j + 1:
                bad.append((j, rk))
        print(f"  m={m:2d}: {'all j = 1..m-1 span' if not bad else 'FAILS at ' + str(bad)}", flush=True)


if __name__ == "__main__":
    mode = sys.argv[1]
    mmax = int(sys.argv[2]) if len(sys.argv) > 2 else 9
    {"A": lambda: A_det3(), "B": lambda: B_theoremC(mmax), "C": lambda: C_windows(mmax)}[mode]()
