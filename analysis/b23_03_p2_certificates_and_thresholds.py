"""B23-03 pilot 2 -- (Question A) the certificate D35 not inside Sigma_Pi, and a check of T3 in T2;
(Question B) rank thresholds of d_1 at N = 6, 7, 8: determinant floors against padding ceilings.
Imports no project code.

  F1  a D35 cubic C = det(sum_{i<5} x_i R_i), R_1..R_6 rank one with R_1 + ... + R_6 = 0, built
      from two rank-one decompositions of one integer matrix X; its six rank-one points are
      e_0..e_4 and -(1,..,1).  dim (S/J_C)_k at k = 4..7 (mod P); LGP; Hessian ranks.
  F2  T3 normal form with row 0 of B = (c1, 0, c2, 0): C vanishes on {x2 = c1 t, x0 = -c2 t}.
  QB  for N = 6, 7, 8 and k = 3..8: the proved padding ceiling min(dim S_k - h_N(k), G_N(k));
      the monomial-Jacobian determinant point F0 (exact Hilbert function, all k, with a Newton
      forward-difference certificate for large k); modular floors of rank M_k at a random
      integer point of D_N; and, time permitting, modular ranks at a random padding point
      (z per_3) o T (MEASURED context only).
A modular rank is a floor for the rank over Q; the rank at one point is a floor for the generic rank.
"""
import hashlib
import json
import random
import sys
import time
import traceback
from itertools import combinations_with_replacement, permutations
from math import comb
from pathlib import Path

import flint

T0 = time.perf_counter()
OUT = Path(sys.argv[1])
P = 2147483647
SEED = 2309182
DOCS = {"preregistration_snapshot": Path("results/b23_03/preregistration_snapshot.md"),
        "addendum_before_p2": Path("results/b23_03/addendum_before_p2.md")}
out = {"pilot": "b23_03_p2_certificates_and_thresholds", "modulus_for_floors": P, "seed": SEED,
       "hashes": {k: hashlib.sha256(v.read_bytes()).hexdigest() for k, v in DOCS.items()},
       "sections": {}}
for k, v in out["hashes"].items():
    print(k.upper() + "_SHA256", v, flush=True)
rng = random.Random(SEED)


def el():
    return time.perf_counter() - T0


def dump():
    out["elapsed_s"] = round(el(), 3)
    OUT.write_text(json.dumps(out, indent=1) + "\n")


dump()


# ------------------------------------------------------------------ polynomial utilities (n variables)
def mono(d, n):
    if d < 0:
        return []
    res = []
    for c in combinations_with_replacement(range(n), d):
        e = [0] * n
        for i in c:
            e[i] += 1
        res.append(tuple(e))
    return res


def add(p, q, s=1):
    r = dict(p)
    for e, v in q.items():
        w = r.get(e, 0) + s * v
        if w:
            r[e] = w
        else:
            r.pop(e, None)
    return r


def mul(p, q):
    r = {}
    for e1, v1 in p.items():
        for e2, v2 in q.items():
            e = tuple(a + b for a, b in zip(e1, e2))
            r[e] = r.get(e, 0) + v1 * v2
    return {e: v for e, v in r.items() if v}


def scal(c, p):
    return {e: c * v for e, v in p.items()} if c else {}


def var(i, n):
    return {tuple(1 if j == i else 0 for j in range(n)): 1}


def lin(v):
    n = len(v)
    return {tuple(1 if j == i else 0 for j in range(n)): v[i] for i in range(n) if v[i]}


def rlin(n, lo=-3, hi=3):
    v = [rng.randint(lo, hi) for _ in range(n)]
    while not any(v):
        v = [rng.randint(lo, hi) for _ in range(n)]
    return lin(v)


def sgn(perm):
    s = 1
    for i in range(len(perm)):
        for j in range(i + 1, len(perm)):
            if perm[i] > perm[j]:
                s = -s
    return s


def det(Mx, n, signed=True):
    tot = {}
    for perm in permutations(range(len(Mx))):
        t = {(0,) * n: sgn(perm) if signed else 1}
        for i in range(len(Mx)):
            t = mul(t, Mx[i][perm[i]])
            if not t:
                break
        if t:
            tot = add(tot, t)
    return tot


def partial(p, i):
    r = {}
    for e, v in p.items():
        if e[i]:
            f = list(e)
            f[i] -= 1
            r[tuple(f)] = r.get(tuple(f), 0) + v * e[i]
    return r


def rank_exact(rows):
    rows = [list(r) for r in rows]
    return flint.fmpz_mat(rows).rank() if rows and rows[0] else 0


def macaulay_rank(F, k, n, dF):
    """rank mod P of M_k(F): rows S_k, columns (d_i F) x S_{k - dF + 1}; dF = deg F."""
    parts = [partial(F, i) for i in range(n)]
    rows = mono(k, n)
    idx = {m: i for i, m in enumerate(rows)}
    cols = [(i, m) for i in range(n) for m in mono(k - dF + 1, n)]
    if not cols:
        return 0, len(rows), 0
    M = flint.nmod_mat(len(rows), len(cols), P)
    for c, (i, m) in enumerate(cols):
        for e, v in parts[i].items():
            M[idx[tuple(a + b for a, b in zip(e, m))], c] = v % P
    return M.rank(), len(rows), len(cols)


def section(name):
    def deco(fn):
        t = time.perf_counter()
        try:
            out["sections"][name] = fn()
        except Exception:
            out["sections"][name] = {"ERROR": traceback.format_exc()}
            print("ERROR in", name, flush=True)
        out["sections"][name + "_seconds"] = round(time.perf_counter() - t, 3)
        dump()
        print(name, "done", out["sections"][name + "_seconds"], "s", flush=True)
        return fn
    return deco


# ------------------------------------------------------------------ F1: D35 not inside Sigma_Pi
def mat3_det(A):
    return (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1]) - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
            + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))


def mat3_adj(A):
    c = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            m = [[A[a][b] for b in range(3) if b != j] for a in range(3) if a != i]
            c[i][j] = (-1) ** (i + j) * (m[0][0] * m[1][1] - m[0][1] * m[1][0])
    return [[c[j][i] for j in range(3)] for i in range(3)]


def matmul(A, B):
    return [[sum(A[i][t] * B[t][j] for t in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def unimodular():
    U = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
    for _ in range(8):
        i, j = rng.sample(range(3), 2)
        c = rng.choice([-2, -1, 1, 2])
        U[i] = [a + c * b for a, b in zip(U[i], U[j])]
    return U


@section("F1_D35_not_in_Sigma_Pi")
def f1():
    attempts = []
    n = 5
    for trial in range(4):
        X = [[rng.randint(-3, 3) for _ in range(3)] for _ in range(3)]
        while mat3_det(X) == 0:
            X = [[rng.randint(-3, 3) for _ in range(3)] for _ in range(3)]
        U, W = unimodular(), unimodular()
        dU, dW = mat3_det(U), mat3_det(W)
        Uinv = [[dU * a for a in row] for row in mat3_adj(U)]   # det = +-1, inverse = det * adj
        Winv = [[dW * a for a in row] for row in mat3_adj(W)]
        Vt, Zt = matmul(Uinv, X), matmul(Winv, X)
        R = [[U[a][i] * Vt[i][b] for a in range(3) for b in range(3)] for i in range(3)]
        R += [[-W[a][j] * Zt[j][b] for a in range(3) for b in range(3)] for j in range(3)]
        rec = {"X": X, "U": U, "W": W, "dets_U_W": [dU, dW],
               "sum_of_six_is_zero": all(sum(R[q][c] for q in range(6)) == 0 for c in range(9)),
               "span_rank_first5": rank_exact(R[:5]), "span_rank_all6": rank_exact(R)}
        Mx = [[lin([R[i][3 * r + c] for i in range(5)]) for c in range(3)] for r in range(3)]
        C = det(Mx, n)
        pts = [[1 if j == i else 0 for j in range(5)] for i in range(5)] + [[-1] * 5]

        def ev(p, x):
            tot = 0
            for e, v in p.items():
                term = v
                for i2, k2 in enumerate(e):
                    term *= x[i2] ** k2
                tot += term
            return tot

        def minors2_zero(x):
            Mn = [[ev(Mx[r][c], x) for c in range(3)] for r in range(3)]
            return all(Mn[r1][c1] * Mn[r2][c2] - Mn[r1][c2] * Mn[r2][c1] == 0
                       for r1 in range(3) for r2 in range(3) for c1 in range(3) for c2 in range(3))
        rec["all_six_rank_one"] = all(minors2_zero(x) for x in pts)
        rec["LGP_all_5_subsets_det_nonzero"] = all(
            flint.fmpz_mat([pts[q] for q in range(6) if q != drop]).det() != 0 for drop in range(6))
        rec["gradient_zero_at_six"] = all(ev(partial(C, i), x) == 0 for x in pts for i in range(5))
        rec["hessian_ranks"] = [rank_exact([[ev(partial(partial(C, i), j), x) for j in range(5)]
                                            for i in range(5)]) for x in pts]
        rec["partials_rank_exact"] = rank_exact([[partial(C, i).get(m, 0) for m in mono(2, 5)] for i in range(5)])
        rec["corank_mod_P"] = {}
        for k in (4, 5, 6, 7):
            r, nr, nc = macaulay_rank(C, k, 5, 3)
            rec["corank_mod_P"][str(k)] = nr - r
        rec["certificate_passes"] = (rec["sum_of_six_is_zero"] and rec["span_rank_first5"] == 5
                                     and rec["all_six_rank_one"] and rec["LGP_all_5_subsets_det_nonzero"]
                                     and rec["corank_mod_P"]["6"] == 6 and rec["corank_mod_P"]["7"] == 6)
        rec["C_nonzero_terms"] = len(C)
        attempts.append(rec)
        if rec["certificate_passes"]:
            rec["C"] = {str(e): v for e, v in sorted(C.items())}
            break
    return {"attempts": attempts, "passed": any(a["certificate_passes"] for a in attempts)}


# ------------------------------------------------------------------ F2: T3 in T2, a check
@section("F2_T3_plane_check")
def f2():
    n = 5
    res = []
    for trial in range(2):
        B = [[rng.randint(-3, 3) for _ in range(4)] for _ in range(4)]
        B[0][1] = B[0][3] = 0
        A = [[{} for _ in range(4)] for _ in range(4)]
        for r, (a, b) in enumerate([(0, 2), (0, 3), (1, 2), (1, 3)]):
            A[r][b] = var(a, n)
            A[r][a] = scal(-1, var(b, n))
        A = [[add(A[i][j], scal(B[i][j], var(4, n))) for j in range(4)] for i in range(4)]
        F = det(A, n)
        tdiv = all(e[4] >= 1 for e in F)
        C = {tuple(a - (1 if j == 4 else 0) for j, a in enumerate(e)): v for e, v in F.items()} if tdiv else {}
        sub = {}
        for e, v in C.items():   # x2 = B00 t, x0 = -B02 t
            coef = v * ((-B[0][2]) ** e[0]) * (B[0][0] ** e[2])
            ne = (0, e[1], 0, e[3], e[4] + e[0] + e[2])
            sub[ne] = sub.get(ne, 0) + coef
        r4, _, _ = macaulay_rank(C, 6, 5, 3) if C else (None, 0, 0)
        res.append({"B": B, "t_divides_F": tdiv, "C_nonzero": bool(C),
                    "C_vanishes_on_plane": bool(C) and not any(sub.values()),
                    "corank_k6_mod_P": 210 - r4 if C else None})
    return res


# ------------------------------------------------------------------ Question B
def C_(n, r):
    return comb(n, r) if (n >= 0 and 0 <= r <= n) else 0


def dimS(N, k):
    return C_(k + N - 1, N - 1) if k >= 0 else 0


def h_pad(N, k):
    return C_(k + N - 2, N - 2) - C_(k + N - 5, N - 2)


def G_ceiling(N, k):
    if k < 3:
        return 0
    if k == 3:
        return N
    if k == 4:
        return N * N
    if k == 5:
        return N * dimS(N, 2)
    if k == 6:
        return N * dimS(N, 3) - C_(N, 2)
    return dimS(N, k)


def A_blk(a):
    return 1 if a == 0 else 6 * a - 2


def B_blk(N, b):
    if N == 8:
        return A_blk(b)
    if N == 7:
        return [1, 3][b] if b < 2 else b + 4
    if N == 6:
        return [1, 2, 3][b] if b < 3 else 2


def H_F0(N, k):
    return sum(A_blk(a) * B_blk(N, k - a) for a in range(k + 1))


def F0_matrix(N):
    x = [lambda i: None]
    v = lambda i: var(i, N)
    if N == 8:
        off = [v(4), v(5), v(6), v(7)]
    elif N == 7:
        off = [v(4), v(5), v(6), v(4)]
    else:
        off = [v(4), v(5), v(4), v(5)]
    # [[x0,0,0,o0],[o1,x1,0,0],[0,o2,x2,0],[0,0,o3,x3]]: det = x0x1x2x3 - o0 o1 o2 o3
    Z = {}
    return [[v(0), Z, Z, off[0]], [off[1], v(1), Z, Z], [Z, off[2], v(2), Z], [Z, Z, off[3], v(3)]]


def brute_H(N, k, gens):
    cnt = 0
    for m in mono(k, N):
        if not any(all(a >= b for a, b in zip(m, g)) for g in gens):
            cnt += 1
    return cnt


@section("QB_tables_and_F0")
def qb_tables():
    res = {}
    for N in (6, 7, 8):
        F0 = det(F0_matrix(N), N)
        gens = [next(iter(partial(F0, i))) for i in range(N)]
        mono_parts = all(len(partial(F0, i)) == 1 for i in range(N))
        ks = list(range(0, 21))
        rowsN = []
        for k in ks:
            rowsN.append({"k": k, "dimS": dimS(N, k), "h_pad": h_pad(N, k),
                          "pad_UB": dimS(N, k) - h_pad(N, k), "G": G_ceiling(N, k),
                          "pad_ceiling": min(dimS(N, k) - h_pad(N, k), G_ceiling(N, k)),
                          "H_F0": H_F0(N, k), "r_F0": dimS(N, k) - H_F0(N, k),
                          "D": h_pad(N, k) - H_F0(N, k)})
        brute_ok = all(brute_H(N, k, gens) == H_F0(N, k) for k in range(0, 8))
        f0_rank_ok = all(macaulay_rank(F0, k, N, 4)[0] == dimS(N, k) - H_F0(N, k) for k in range(3, 7))
        # Newton forward-difference certificate for D(k) = h_pad - H_F0 >= 0, k >= k1
        cert = None
        for k1 in range(3, 30):
            vals = [h_pad(N, k) - H_F0(N, k) for k in range(k1, k1 + 10)]
            diffs, cur = [], vals[:]
            for i in range(10):
                diffs.append(cur[0])
                cur = [cur[j + 1] - cur[j] for j in range(len(cur) - 1)]
            if all(d >= 0 for d in diffs[:8]) and all(d == 0 for d in diffs[6:10]):
                cert = {"k1": k1, "forward_differences": diffs}
                break
        res[str(N)] = {"F0": {str(e): c for e, c in F0.items()}, "F0_partials_are_monomials": mono_parts,
                       "F0_generators": [list(g) for g in gens],
                       "H_F0_formula_matches_brute_force_k0_7": brute_ok,
                       "F0_rank_mod_P_matches_formula_k3_6": f0_rank_ok,
                       "newton_certificate": cert, "table": rowsN}
    return res


def rand_det(N):
    Ls = [[[rng.randint(-3, 3) for _ in range(4)] for _ in range(4)] for _ in range(N)]
    A = [[lin([Ls[i][r][c] for i in range(N)]) for c in range(4)] for r in range(4)]
    return det(A, N), Ls


def rand_pad(N):
    z = rlin(N)
    Y = [[rlin(N) for _ in range(3)] for _ in range(3)]
    return mul(z, det(Y, N, signed=False))


QB = {"det": {}, "pad": {}}
out["sections"]["QB_ranks"] = QB


def run_ranks(kind, jobs, budget):
    for N, k in jobs:
        key = f"N{N}_k{k}"
        if el() > budget:
            QB[kind][key] = {"skipped_time": round(el(), 2)}
            dump()
            continue
        t = time.perf_counter()
        F = QB_pts[kind][N]
        r, nr, nc = macaulay_rank(F, k, N, 4)
        QB[kind][key] = {"rank_mod_P": r, "rows": nr, "cols": nc, "seconds": round(time.perf_counter() - t, 3)}
        dump()
        print(kind, key, QB[kind][key], flush=True)


try:
    QB_pts = {"det": {}, "pad": {}}
    for N in (6, 7, 8):
        Fd, Ls = rand_det(N)
        QB_pts["det"][N] = Fd
        QB.setdefault("det_points", {})[str(N)] = Ls
        QB_pts["pad"][N] = rand_pad(N)
    small = [(6, k) for k in range(3, 9)] + [(7, k) for k in range(3, 8)] + [(8, k) for k in range(3, 7)]
    big = [(7, 8), (8, 7)]
    run_ranks("det", small, 45)
    run_ranks("det", big, 35)
    run_ranks("pad", small, 42)
    run_ranks("pad", big, 30)
except Exception:
    QB["ERROR"] = traceback.format_exc()
dump()
print("TOTAL", round(el(), 2), flush=True)
