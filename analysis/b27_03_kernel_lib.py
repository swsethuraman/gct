"""B27-03 run: exact rank certificates for Q_D on coefficient-weight spaces.

For a weight space H (coefficient degree k, torus weight w) with monomial basis h_m, build
E[j,m] = h_m(pi(det(sum_i x_i B_i^(j)))) at explicit integer pencils B^(j) (deterministic LCG,
entries in {-3..3}).  All coefficients are exact integers; the rank is taken mod p = 1e9+7.
rank_p(E) = dim H  ==>  rank_Q(E) = dim H  ==>  no nonzero h in H vanishes on these determinant
points  ==>  ker Q_D on H = 0 (COMPUTED certificate of injectivity; no nullspace is sampled).
A deficient rank is reported as such and is NOT used as a kernel claim.
Library form of analysis/b27_03_kernel.py (job list removed; EXTRA=None gives 2N points).
"""
import json, sys, time, itertools
import numpy as np

t0 = time.time()
EXTRA = 16
P = 1_000_000_007
E70 = sorted([a for a in itertools.product(range(5), repeat=5) if sum(a) == 4], reverse=True)
E65 = [a for a in E70 if max(a) >= 2]
IDX70 = {a: i for i, a in enumerate(E70)}

def basis(k, w, E):
    """all multisets of k exponents from E (in order) summing to w; returned as index tuples."""
    out, E = [], list(E)
    def rec(start, left, rem, cur):
        if left == 0:
            if not any(rem): out.append(tuple(cur))
            return
        for i in range(start, len(E)):
            a = E[i]
            if all(a[t] <= rem[t] for t in range(5)):
                cur.append(i)
                rec(i, left - 1, tuple(rem[t] - a[t] for t in range(5)), cur)
                cur.pop()
    rec(0, k, tuple(w), [])
    return out

# ---- explicit determinant points ----
state = 20260923
def lcg():
    global state
    state = (1103515245 * state + 12345) % 2**31
    return ((state >> 16) % 7) - 3

def points(n):
    B = np.array([[[[lcg() for v in range(5)] for c in range(4)] for r in range(4)] for _ in range(n)],
                 dtype=np.int64)                       # (n, row, col, var)
    tup2mono = np.zeros((625, 70), dtype=np.int64)
    for t, tup in enumerate(itertools.product(range(5), repeat=4)):
        a = [0] * 5
        for v in tup: a[v] += 1
        tup2mono[t, IDX70[tuple(a)]] = 1
    T = np.zeros((n, 5, 5, 5, 5), dtype=np.int64)
    for s in itertools.permutations(range(4)):
        sign = 1
        for i in range(4):
            for j in range(i + 1, 4):
                if s[i] > s[j]: sign = -sign
        T += sign * np.einsum('pi,pj,pk,pl->pijkl', B[:, 0, s[0]], B[:, 1, s[1]], B[:, 2, s[2]], B[:, 3, s[3]])
    return T.reshape(n, 625) @ tup2mono                # exact integer quartic coefficients (n,70)

def rank_mod_p(M):
    M = M.copy() % P
    r, (nr, nc) = 0, M.shape
    for c in range(nc):
        piv = np.nonzero(M[r:, c])[0]
        if len(piv) == 0: continue
        pr = r + piv[0]
        if pr != r: M[[r, pr]] = M[[pr, r]]
        inv = pow(int(M[r, c]), P - 2, P)
        M[r] = (M[r] * inv) % P
        rows = np.nonzero(M[:, c])[0]
        rows = rows[rows != r]
        if len(rows):
            M[rows] = (M[rows] - (M[rows, c][:, None] * M[r][None, :]) % P) % P
        r += 1
        if r == nr: break
    return r

def certify(name, k, w, ring, cap):
    E = E65 if ring == 65 else E70
    B = basis(k, w, E)
    N = len(B)
    rec = {"name": name, "k": k, "w": list(w), "ring": ring, "dim_H": N}
    if N == 0 or N > cap:
        rec["status"] = "skipped (dim 0)" if N == 0 else f"skipped (dim > cap {cap})"
        return rec
    npts = N + 16 if EXTRA is not None else 2 * N
    C = points(npts)
    cols = [IDX70[E[i]] for i in range(len(E))]
    Cm = (C[:, cols] % P)
    Emat = np.ones((npts, N), dtype=np.int64)
    for m, mono in enumerate(B):
        v = np.ones(npts, dtype=np.int64)
        for i in mono: v = (v * Cm[:, i]) % P
        Emat[:, m] = v
    r = rank_mod_p(Emat)
    rec.update({"n_points": npts, "rank_mod_p": r,
                "status": "ker Q_D on H = 0 (COMPUTED)" if r == N else "rank deficient at these points: no claim"})
    return rec

