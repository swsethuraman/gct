"""B23-10 pilot 1.  Imports no project code; exact integer arithmetic only.

  A. B23-03 Prop. 2.5 witness C = x1 (x3^2 + x4^2) + x2 (x5^2 + x3 x4):
     the syzygy g = u x v (u, v the (d3,d4,d5)-gradients of q1, q2) kills (d3 C, d4 C, d5 C);
     g_1 has a monomial free of x1, x2 (so g is not Koszul); the five partials are independent;
     rank M_4(C) exact over Q; control: rank M_4 at a smooth cubic (Fermat) is 65.
  B. B23-03 Thm 3.2 tail: Hilbert function of S/J_{F0} built independently (brute-force per block,
     then convolution), padding ceiling h_N(k); margin D(k) = h_N(k) - H(k) for k <= 80;
     Newton coefficients at k_1; order-6 differences vanish on [k_1, 80]; the table's padding
     ceilings at k = 6..8.
  C. B23-01: the reconstruction (737/646, -1421/969) against both primes; the 20 minors of the
     shipped six rows mod P2; height-2000 searches under both readings.
"""
import json
import sys
from itertools import combinations, combinations_with_replacement
from math import comb
from pathlib import Path

out = {"pilot": "b23_10_p1_witness_tail_height"}
NV = 5


# ------------------------------------------------------------------ polynomial helpers (5 vars)
def mono(d, n=NV):
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


def var(i):
    return {tuple(1 if j == i else 0 for j in range(NV)): 1}


def partial(p, i):
    r = {}
    for e, v in p.items():
        if e[i]:
            f = list(e)
            f[i] -= 1
            r[tuple(f)] = r.get(tuple(f), 0) + v * e[i]
    return r


def rank_exact(rows):
    A = [list(r) for r in rows]
    m, n = len(A), len(A[0])
    rk, prev = 0, 1
    for col in range(n):
        piv = next((i for i in range(rk, m) if A[i][col]), None)
        if piv is None:
            continue
        A[rk], A[piv] = A[piv], A[rk]
        for i in range(rk + 1, m):
            A[i] = [(A[rk][col] * A[i][j] - A[i][col] * A[rk][j]) // prev for j in range(n)]
        prev = A[rk][col]
        rk += 1
        if rk == m:
            break
    return rk


M2, M4 = mono(2), mono(4)


def macaulay4(C):
    parts = [partial(C, i) for i in range(NV)]
    cols = [[mul(parts[i], {m: 1}).get(e, 0) for e in M4] for i in range(NV) for m in M2]
    return [list(r) for r in zip(*cols)]


x = [var(i) for i in range(NV)]
q1 = add(mul(x[2], x[2]), mul(x[3], x[3]))
q2 = add(mul(x[4], x[4]), mul(x[2], x[3]))
C = add(mul(x[0], q1), mul(x[1], q2))
u = [partial(q1, j) for j in (2, 3, 4)]
v = [partial(q2, j) for j in (2, 3, 4)]
g = [add(mul(u[1], v[2]), mul(u[2], v[1]), -1),
     add(mul(u[2], v[0]), mul(u[0], v[2]), -1),
     add(mul(u[0], v[1]), mul(u[1], v[0]), -1)]            # u x v
dC = [partial(C, j) for j in (2, 3, 4)]
syz = {}
for gj, dj in zip(g, dC):
    syz = add(syz, mul(gj, dj))
parts = [partial(C, i) for i in range(NV)]
part_rank = rank_exact([[p.get(e, 0) for e in M2] for p in parts])
fermat = {}
for i in range(NV):
    fermat = add(fermat, mul(mul(x[i], x[i]), x[i]))
out["A"] = {
    "g_components": [{str(k): v for k, v in gi.items()} for gi in g],
    "syzygy_identity_zero": syz == {},
    "g1_has_monomial_free_of_x1_x2": any(e[0] == 0 and e[1] == 0 for e in g[0]),
    "partials_rank": part_rank,
    "rank_M4_witness": rank_exact(macaulay4(C)),
    "rank_M4_fermat_control": rank_exact(macaulay4(fermat)),
}


# ------------------------------------------------------------------ B. Theorem 3.2 tail
def hf_block(gens, nv, kmax):
    """Hilbert function of C[y_1..y_nv]/(monomials gens), brute force."""
    res = []
    for k in range(kmax + 1):
        cnt = 0
        for e in mono(k, nv):
            if not any(all(e[i] >= gv[i] for i in range(nv)) for gv in gens):
                cnt += 1
        res.append(cnt)
    return res


def conv(a, b, kmax):
    return [sum(a[i] * b[k - i] for i in range(k + 1)) for k in range(kmax + 1)]


KMAX = 60
blockA = [(0, 1, 1, 1), (1, 0, 1, 1), (1, 1, 0, 1), (1, 1, 1, 0)]      # partials of x1x2x3x4
second = {8: ([(0, 1, 1, 1), (1, 0, 1, 1), (1, 1, 0, 1), (1, 1, 1, 0)], 4),   # x5x6x7x8
          7: ([(1, 1, 1), (2, 0, 1), (2, 1, 0)], 3),                       # x5^2 x6 x7
          6: ([(1, 2), (2, 1)], 2)}                                         # x5^2 x6^2
hA = hf_block(blockA, 4, KMAX)
claimed_newton = {6: (9, [11, 50, 21, 3, 0]), 7: (9, [119, 216, 117, 30, 3, 0]),
                  8: (8, [69, 420, 371, 163, 36, 3, 0])}
table_ceilings = {6: [287, 532, 918], 7: [518, 1050, 1968], 8: [876, 1926]}
B = {"A_block_formula_6a_minus_2": all(hA[a] == (1 if a == 0 else 6 * a - 2) for a in range(KMAX + 1))}
for N, (gens2, nv2) in second.items():
    hB = hf_block(gens2, nv2, KMAX)
    H = conv(hA, hB, KMAX)
    hN = [comb(k + N - 2, N - 2) - (comb(k + N - 5, N - 2) if k >= 3 else 0) for k in range(KMAX + 1)]
    dimS = [comb(k + N - 1, N - 1) for k in range(KMAX + 1)]
    D = [hN[k] - H[k] for k in range(KMAX + 1)]
    k1, claimed = claimed_newton[N]
    # Newton coefficients at k1 from forward differences
    newton = []
    seq = D[k1:k1 + 12]
    diffs = list(seq)
    for i in range(len(claimed)):
        newton.append(diffs[0])
        diffs = [diffs[j + 1] - diffs[j] for j in range(len(diffs) - 1)]
    # order-6 differences on [k1, KMAX]
    d = D[k1:]
    for _ in range(6):
        d = [d[j + 1] - d[j] for j in range(len(d) - 1)]
    ceil = [dimS[k] - hN[k] for k in (6, 7, 8)][:len(table_ceilings[N])]
    B["N%d" % N] = {
        "k1": k1, "newton_mine": newton, "newton_claimed": claimed,
        "newton_matches": newton == claimed,
        "min_margin_k1_to_60": min(D[k1:]), "all_positive_k1_to_60": min(D[k1:]) > 0,
        "order6_differences_vanish_k1_to_60": all(t == 0 for t in d),
        "padding_ceilings_k6_8_mine": ceil, "padding_ceilings_claimed": table_ceilings[N],
        "ceilings_match": ceil == table_ceilings[N],
        "F0_floor_minus_padding_ceiling_k3_to_12": [D[k] for k in range(3, 13)],
    }
out["B"] = B

# ------------------------------------------------------------------ C. B23-01 arithmetic and height
P, P2 = 524287, 524269
ALPHA, BETA = 265391, 275398
A2, B2 = 109562, 163393
inv = lambda a, m: pow(a % m, m - 2, m)
rows = [[27584, 18096, 154260], [452721, 62665, 501156], [106259, 105559, 231269],
        [299003, 30949, 169404], [354414, 320659, 412386], [444066, 497271, 511044]]


def det3(m, p):
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])) % p


minors = [det3([rows[i] for i in c], P2) for c in combinations(range(6), 3)]
C_ = {
    "alpha_737_646_mod_P": 737 * inv(646, P) % P, "alpha_mod_P_expected": ALPHA,
    "alpha_737_646_mod_P2": 737 * inv(646, P2) % P2, "alpha_mod_P2_expected": A2,
    "beta_m1421_969_mod_P": -1421 * inv(969, P) % P, "beta_mod_P_expected": BETA,
    "beta_m1421_969_mod_P2": -1421 * inv(969, P2) % P2, "beta_mod_P2_expected": B2,
    "minors_mod_P2_all_zero": all(m == 0 for m in minors), "n_minors": len(minors),
    "relation_residual_P2_rows": [(r[2] - A2 * r[0] - B2 * r[1]) % P2 for r in rows],
}
C_["reconstruction_consistent"] = (C_["alpha_737_646_mod_P"] == ALPHA and C_["alpha_737_646_mod_P2"] == A2
                                  and C_["beta_m1421_969_mod_P"] == BETA and C_["beta_m1421_969_mod_P2"] == B2)


def bal(t, m):
    t %= m
    return t - m if t > m // 2 else t


H = 2000
per_alpha = [(bal(ALPHA * b, P), b) for b in range(1, H + 1) if abs(bal(ALPHA * b, P)) <= H]
per_beta = [(bal(BETA * b, P), b) for b in range(1, H + 1) if abs(bal(BETA * b, P)) <= H]
joint = [(bal(ALPHA * d, P), bal(BETA * d, P), d) for d in range(1, H + 1)
         if abs(bal(ALPHA * d, P)) <= H and abs(bal(BETA * d, P)) <= H]
joint_to_3000 = [(bal(ALPHA * d, P), bal(BETA * d, P), d) for d in range(1, 3001)
                 if abs(bal(ALPHA * d, P)) <= 3000 and abs(bal(BETA * d, P)) <= 3000]
C_["height_search_bound"] = H
C_["per_coefficient_lifts_alpha"] = per_alpha
C_["per_coefficient_lifts_beta"] = per_beta
C_["joint_common_denominator_lifts_height_le_2000"] = joint
C_["joint_lifts_height_le_3000"] = joint_to_3000
out["C"] = C_

Path(sys.argv[1]).write_text(json.dumps(out, indent=1) + "\n")
print(json.dumps({"A": {k: v for k, v in out["A"].items() if k != "g_components"}}, indent=1))
print(json.dumps({k: {kk: vv for kk, vv in v.items() if kk != "F0_floor_minus_padding_ceiling_k3_to_12"} if isinstance(v, dict) else v
                  for k, v in out["B"].items()}, indent=1))
print(json.dumps({k: v for k, v in out["C"].items()}, indent=1))
