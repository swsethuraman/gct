"""B24-02 pilot 1.  Imports no project code (python-flint for the modular ranks only).

Can B23-03's method (elementary padding ceiling + certified determinant floor at explicit
integer points + Newton certificate for the tail) discharge Kleiman from row 1 at N = 5?

  A. Padding ceilings at k = 3..9, exact integer arithmetic.
  B. Determinant floors at k = 3..9: rank M_k mod P at a fresh random integer point of D45.
  C. The tail point F_0 = x1x2x3x4 - x5^4: verified to be a 4x4 determinant of linear forms,
     its monomial Jacobian Hilbert function H(k) by brute-force enumeration.
  D. Newton certificate for D(k) = h_5(k) - H(k) on k >= k_1 = 10.

All dimensions are AFFINE dimensions of graded pieces of C[x_1..x_5] (G24).
Usage: b24_02_p1_n5_kleiman.py <out.json> <prereg sha256>
"""
import hashlib
import json
import sys
import time
import random
from itertools import combinations_with_replacement
from pathlib import Path

T0 = time.time()
OUT = Path(sys.argv[1])
PREREG = Path("results/b24_02/p1_prereg.md")
got = hashlib.sha256(PREREG.read_bytes()).hexdigest()
out = {"preregistration": {"path": str(PREREG).replace("\\", "/"), "sha256": got,
                           "expected": sys.argv[2], "match": got == sys.argv[2],
                           "recorded_at_elapsed_s": round(time.time() - T0, 4)},
       "pilot": "b24_02_p1_n5_kleiman"}


def dump():
    out["elapsed_s"] = round(time.time() - T0, 3)
    OUT.write_text(json.dumps(out, indent=1) + "\n")


dump()
if got != sys.argv[2]:
    out["status"] = "prereg hash mismatch; nothing run"
    dump()
    sys.exit(1)

import flint  # noqa: E402

N = 5
P = 2147483647
SEED = 20260919
rng = random.Random(SEED)
out.update({"N": N, "modulus": P, "seed": SEED, "dimension_convention": "affine (G24)"})


def binom(n, k):
    if k < 0 or n < 0 or k > n:
        return 0
    r = 1
    for i in range(k):
        r = r * (n - i) // (i + 1)
    return r


def monos(d, n):
    res = []
    for c in combinations_with_replacement(range(n), d):
        e = [0] * n
        for i in c:
            e[i] += 1
        res.append(tuple(e))
    return res


def mul(p, q):
    r = {}
    for a, x in p.items():
        for b, y in q.items():
            e = tuple(i + j for i, j in zip(a, b))
            r[e] = r.get(e, 0) + x * y
    return {e: v for e, v in r.items() if v}


def add(p, q, s=1):
    r = dict(p)
    for e, v in q.items():
        r[e] = r.get(e, 0) + s * v
    return {e: v for e, v in r.items() if v}


def partial(p, i):
    r = {}
    for e, v in p.items():
        if e[i]:
            f = list(e)
            f[i] -= 1
            r[tuple(f)] = r.get(tuple(f), 0) + v * e[i]
    return r


def det(M):
    if len(M) == 1:
        return M[0][0]
    res = {}
    for j in range(len(M)):
        minor = [row[:j] + row[j + 1:] for row in M[1:]]
        res = add(res, mul(M[0][j], det(minor)), 1 if j % 2 == 0 else -1)
    return res


def macaulay_rank_mod(F, k, n=N):
    parts = [partial(F, i) for i in range(n)]
    rows = {e: i for i, e in enumerate(monos(k, n))}
    cols = monos(k - 3, n)
    M = flint.nmod_mat(len(rows), n * len(cols), P)
    c = 0
    for pd in parts:
        for m in cols:
            for e, v in pd.items():
                M[rows[tuple(a + b for a, b in zip(e, m))], c] = v % P
            c += 1
    return M.rank(), len(rows), n * len(cols)


def h5(k):
    return binom(k + 3, 3) - binom(k, 3)


def dimS(k):
    return binom(k + 4, 4)


# ---------------------------------------------------------------- A. padding ceilings
KS = list(range(3, 10))
universal = {3: N * dimS(0), 4: N * dimS(1), 5: N * dimS(2), 6: N * 35 - binom(N, 2)}
A = {}
for k in KS:
    ci = dimS(k) - h5(k)
    u = universal.get(k)
    A[k] = {"dim_S_k": dimS(k), "h5_k": h5(k), "lP_ceiling": ci,
            "universal_ceiling": u, "padding_ceiling": ci if u is None else min(ci, u)}
out["A_padding_ceilings"] = A
out["A_h5_closed_form_check"] = all(h5(k) == (3 * k * k + 3 * k + 2) // 2 for k in range(0, 40))
dump()


# ---------------------------------------------------------------- B. determinant floors
def linform(n=N):
    while True:
        f = {}
        for i in range(n):
            c = rng.randint(-5, 5)
            if c:
                f[tuple(1 if t == i else 0 for t in range(n))] = c
        if f:
            return f


MAT = [[linform() for _ in range(4)] for _ in range(4)]
F = det(MAT)
out["B_point"] = {"what": "det of a random 4x4 matrix of integer linear forms in 5 variables",
                  "entries_range": [-5, 5], "n_monomials_of_F": len(F),
                  "deg_check": sorted({sum(e) for e in F}) == [4]}
B = {}
for k in KS:
    r, nr, nc = macaulay_rank_mod(F, k)
    B[k] = {"det_floor": r, "rows": nr, "cols": nc,
            "padding_ceiling": A[k]["padding_ceiling"],
            "margin": r - A[k]["padding_ceiling"]}
    out["B_determinant_floors"] = B
    dump()

# ---------------------------------------------------------------- C. the tail point F_0
x = [{tuple(1 if t == i else 0 for t in range(N)): 1} for i in range(N)]
Z = {}
CYC = [[x[0], Z, Z, x[4]],
       [x[4], x[1], Z, Z],
       [Z, x[4], x[2], Z],
       [Z, Z, x[4], x[3]]]
F0_from_det = det(CYC)
F0 = add({(1, 1, 1, 1, 0): 1}, {(0, 0, 0, 0, 4): 1}, -1)
out["C_F0"] = {"form": "x1x2x3x4 - x5^4",
               "is_det_of_cyclic_matrix": F0_from_det == F0,
               "det_expansion": {"".join(map(str, e)): v for e, v in sorted(F0_from_det.items())}}
dump()

# A(a): degree-a monomials in x1..x4 not divisible by x2x3x4, x1x3x4, x1x2x4 or x1x2x3
gens4 = [(0, 1, 1, 1), (1, 0, 1, 1), (1, 1, 0, 1), (1, 1, 1, 0)]
Aval, Aformula = {}, {}
for a in range(0, 13):
    cnt = 0
    for e in monos(a, 4):
        if not any(all(e[i] >= g[i] for i in range(4)) for g in gens4):
            cnt += 1
    Aval[a] = cnt
    Aformula[a] = 1 if a == 0 else 6 * a - 2
out["C_A_ladder"] = {"brute_force": Aval, "formula_6a_minus_2": Aformula,
                     "match": Aval == Aformula}

# H(k): brute-force Hilbert function of S/J(F_0); J is monomial, so this is exact
gens5 = [(0, 1, 1, 1, 0), (1, 0, 1, 1, 0), (1, 1, 0, 1, 0), (1, 1, 1, 0, 0), (0, 0, 0, 0, 3)]
Hval, Hformula = {}, {}
for k in range(0, 13):
    cnt = 0
    for e in monos(k, N):
        if not any(all(e[i] >= g[i] for i in range(N)) for g in gens5):
            cnt += 1
    Hval[k] = cnt
    Hformula[k] = 18 * k - 24 if k >= 3 else None
out["C_H_hilbert"] = {"brute_force": Hval, "formula_18k_minus_24_from_k3": Hformula,
                      "match_from_k3": all(Hval[k] == 18 * k - 24 for k in range(3, 13))}
# cross-check: rank M_k(F_0) mod P should equal dim S_k - H(k)
xc = {}
for k in range(3, 8):
    r, _, _ = macaulay_rank_mod(F0, k)
    xc[k] = {"rank_M_k_F0": r, "dim_S_k_minus_H_k": dimS(k) - Hval[k],
             "match": r == dimS(k) - Hval[k]}
out["C_F0_rank_crosscheck"] = xc
dump()

# ---------------------------------------------------------------- D. Newton certificate
K1 = 10


def Dk(k):
    return h5(k) - (18 * k - 24)


out["D_closed_form_check"] = all(2 * Dk(k) == 3 * k * k - 33 * k + 50 for k in range(3, 40))
vals = [Dk(K1 + i) for i in range(8)]
e = []
for i in range(8):
    s = 0
    for j in range(i + 1):
        s += (-1) ** (i - j) * binom(i, j) * vals[j]
    e.append(s)
out["D_newton"] = {"k_1": K1, "D_at_k1_plus": vals, "newton_coefficients_e": e,
                   "all_e_nonnegative": all(v >= 0 for v in e), "e_0": e[0],
                   "certificate_holds": all(v >= 0 for v in e) and e[0] > 0}
out["D_signs_below_k1"] = {k: Dk(k) for k in range(3, 11)}
dump()

# ---------------------------------------------------------------- decision
cond_a = all(B[k]["margin"] >= 0 for k in (3, 4, 5))
cond_b = all(B[k]["margin"] > 0 for k in (6, 7, 8, 9))
cond_c = out["D_newton"]["certificate_holds"]
out["decision"] = {
    "rule": "PASS iff (a) margins >= 0 at k=3,4,5; (b) margins > 0 at k=6,7,8,9; "
            "(c) Newton certificate holds at k_1 = 10",
    "cond_a_ties_k345": cond_a, "cond_b_strict_k6789": cond_b, "cond_c_newton_tail": cond_c,
    "verdict": "PASS" if (cond_a and cond_b and cond_c) else "FAIL",
    "coverage": "k <= 2: M_k has no columns. k = 3,4,5: tie at the universal ceiling. "
                "k = 6..9: certified modular floor at a random integer point of D45. "
                "k >= 10: F_0 with an exact monomial Hilbert function and the Newton certificate."}
dump()
