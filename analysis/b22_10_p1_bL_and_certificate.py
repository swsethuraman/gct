"""B22-10 pilot 1 — independent evaluator for the upper halves of b_L, and replay of B22-01's
certificate and decisive rows.  Imports no project code.

  A. b_L(11), b_L(12) by an exact character computation (INDEPENDENT EVALUATOR).
     The nu-degree-11 part of S_{(4^5)}(W' + W_0) is S_{(4,4,1)}(W') (x) S_{(4,4,3)}(W_0) and the
     degree-12 part is S_{(4,4)}(W') (x) S_{(4,4,4)}(W_0) (skew Schur / complement in the rectangle;
     checked here numerically at the level of dimensions).  L-invariants = multiplicity of the
     characters (alpha beta c^3 det^2)^k of GL_3 x (C*)^3, computed from Jacobi-Trudi and the Weyl
     numerator.  Weights of W under (alpha, beta, c, g):
       a: alpha beta | r_j: alpha c t_j | c_i: beta t_i | S_ij (i<=j): c t_i t_j | K_ij (i<j): c t_i t_j
  B. The 70 x 70 determinant and the 4 x 4 top minor, from the shipped matrices (REPLAY).
  C. The 140 decisive rows: my own Vandermonde extraction from the raw runner values, rank mod P,
     relation residuals, coordinates, span control against the ORIGINAL recorded sources (REPLAY).
  D. The G21 normalisation: det(g)^{-4}, not det(g)^{4} (REPLAY).
"""
import hashlib
import json
import sys
from itertools import permutations
from math import comb
from pathlib import Path

P = 524287
ALPHA, BETA = 265391, 275398
root = Path(sys.argv[1]).resolve()
out = {"pilot": "b22_10_p1_bL_and_certificate", "prime": P, "inputs": {}, "A": {}, "B": {}, "C": {}, "D": {}}


def load(rel, pin=None):
    p = root / rel
    b = p.read_bytes()
    h = hashlib.sha256(b).hexdigest()
    out["inputs"][rel] = {"sha256": h, "bytes": len(b), "pin": pin, "pin_matches": (None if pin is None else h == pin)}
    return json.loads(b)


# ====================================================================== A. characters
def padd(p, e, v):
    if v:
        p[e] = p.get(e, 0) + v
        if p[e] == 0:
            del p[e]


def pmul(p, q, ok):
    r = {}
    for e1, v1 in p.items():
        for e2, v2 in q.items():
            e = tuple(x + y for x, y in zip(e1, e2))
            if ok(e):
                padd(r, e, v1 * v2)
    return r


def h_list(weights, K, ok):
    """h_0..h_K of the weight monomials, truncated by ok()."""
    zero = (0,) * len(weights[0])
    H = [{zero: 1}] + [{} for _ in range(K)]
    for w in weights:
        for k in range(1, K + 1):            # H_new[k] = H[k] + w * H_new[k-1], k increasing
            add = pmul(H[k - 1], {w: 1}, ok)
            for e, v in add.items():
                padd(H[k], e, v)
    return H


def schur(lam, weights, ok):
    n = len(lam)
    K = lam[0] + n
    H = h_list(weights, K, ok)
    zero = (0,) * len(weights[0])

    def h(k):
        return H[k] if 0 <= k <= K else ({} if k != 0 else {zero: 1})

    total = {}
    for perm in permutations(range(n)):
        sign = 1
        for i in range(n):
            for j in range(i + 1, n):
                if perm[i] > perm[j]:
                    sign = -sign
        term = {zero: sign}
        for i in range(n):
            k = lam[i] - i + perm[i]
            if k < 0:
                term = {}
                break
            term = pmul(term, h(k), ok)
            if not term:
                break
        for e, v in term.items():
            padd(total, e, v)
    return total


def unit(i, n=3):
    return tuple(1 if j == i else 0 for j in range(n))


def W_prime_weights():
    # variables (alpha, t1, t2, t3); beta and c are eliminated: for a term of S_mu(W') with
    # |mu| = n, alpha-exponent 5 and t-degree 2n - 10 force #r = #c, beta-exponent 5 and the
    # c-exponent n - 5 (the counts are determined by (n, alpha, t-degree)), so the L-trivial
    # character (alpha beta c^3 det^2)^5 is exactly [alpha^5] x [GL_3 mult of det^10].
    ws = [(1, 0, 0, 0)]                                                  # a
    ws += [(1,) + unit(j) for j in range(3)]                             # r_j
    ws += [(0,) + unit(i) for i in range(3)]                             # c_i
    ws += [(0,) + tuple(x + y for x, y in zip(unit(i), unit(j)))         # S_ij, i <= j
           for i in range(3) for j in range(i, 3)]
    return ws


def W0_weights():
    return [(0,) + tuple(x + y for x, y in zip(unit(i), unit(j)))        # K_ij, i < j
            for i in range(3) for j in range(i + 1, 3)]


def gl3_mult(sym, mu):
    """Multiplicity of the GL_3 irrep of highest weight mu in the symmetric polynomial sym (dict t->coef)."""
    vand = {(2, 1, 0): 1, (2, 0, 1): -1, (1, 2, 0): -1, (0, 2, 1): 1, (1, 0, 2): 1, (0, 1, 2): -1}
    target = (mu[0] + 2, mu[1] + 1, mu[2])
    s = 0
    for e, v in sym.items():
        need = tuple(t - x for t, x in zip(target, e))
        s += v * vand.get(need, 0)
    return s


# unit tests of the extractor
V = {unit(i): 1 for i in range(3)}  # t only
V2 = pmul(V, V, lambda e: True)
V3 = pmul(V2, V, lambda e: True)
out["A"]["unit_tests"] = {
    "mult (2,0,0) in V(x)V = 1": gl3_mult(V2, (2, 0, 0)) == 1,
    "mult (1,1,0) in V(x)V = 1": gl3_mult(V2, (1, 1, 0)) == 1,
    "mult (2,1,0) in V^3 = 2": gl3_mult(V3, (2, 1, 0)) == 2,
    "mult (1,1,1) in V^3 = 1": gl3_mult(V3, (1, 1, 1)) == 1,
}


def bL(lam_prime, lam_zero, tdeg_prime):
    ok_prime = lambda e: e[0] <= 5 and sum(e[1:]) <= tdeg_prime
    A = schur(lam_prime, W_prime_weights(), ok_prime)
    B = schur(lam_zero, W0_weights(), lambda e: True)
    prod = pmul(A, B, lambda e: e[0] <= 5)
    sym = {e[1:]: v for e, v in prod.items() if e[0] == 5}
    # counts check: in A, every alpha^5 term has t-degree tdeg_prime (degree bookkeeping)
    degs = sorted(set(sum(e[1:]) for e in A if e[0] == 5))
    return {5: gl3_mult(sym, (10, 10, 10))}, len(A), len(B), degs


r11, nA11, nB11, dg11 = bL((4, 4, 1), (4, 4, 3), 8)
r12, nA12, nB12, dg12 = bL((4, 4), (4, 4, 4), 6)
out["A"]["alpha5_tdegrees_in_Wprime_part"] = {"nu11": dg11, "nu12": dg12}
out["A"]["multiplicity_of_(alpha beta c^3 det^2)^5_nu11"] = r11
out["A"]["multiplicity_of_(alpha beta c^3 det^2)^5_nu12"] = r12
out["A"]["b_L_11"] = sum(r11.values())
out["A"]["b_L_12"] = sum(r12.values())
out["A"]["terms"] = {"S441_Wprime_truncated": nA11, "S443_W0": nB11, "S44_Wprime_truncated": nA12, "S444_W0": nB12}


# dimension check of the branching step, one variable u marking W_0 (13 weights 1, 3 weights u)
def h_u(k):
    return [comb(12 + k - j, k - j) * comb(2 + j, j) if k >= j else 0 for j in range(0, 21)]


def polymul1(a, b):
    r = [0] * 41
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y and i + j < 41:
                    r[i + j] += x * y
    return r


def s_rect_u():
    lam = (4, 4, 4, 4, 4)
    tot = [0] * 41
    for perm in permutations(range(5)):
        sign = 1
        for i in range(5):
            for j in range(i + 1, 5):
                if perm[i] > perm[j]:
                    sign = -sign
        term = [sign] + [0] * 40
        for i in range(5):
            k = lam[i] - i + perm[i]
            term = polymul1(term, h_u(k) if k >= 0 else [0] * 21)
        tot = [x + y for x, y in zip(tot, term)]
    return tot


def dim_schur(lam, n):
    num = den = 1
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    for i, row in enumerate(lam):
        for j in range(row):
            num *= n + j - i
            den *= lam[i] + conj[j] - i - j - 1
    return num // den


su = s_rect_u()
out["A"]["branching_dimension_check"] = {
    "u11_coefficient_of_s_(4^5)(1^13,u^3)": su[11],
    "dim S441(C^13) * dim S443(C^3)": dim_schur((4, 4, 1), 13) * dim_schur((4, 4, 3), 3),
    "u12_coefficient": su[12],
    "dim S44(C^13) * dim S444(C^3)": dim_schur((4, 4), 13) * dim_schur((4, 4, 4), 3),
    "dim_S441_C13": dim_schur((4, 4, 1), 13),
}
bc = out["A"]["branching_dimension_check"]
out["A"]["branching_holds"] = (bc["u11_coefficient_of_s_(4^5)(1^13,u^3)"] == bc["dim S441(C^13) * dim S443(C^3)"]
                               and bc["u12_coefficient"] == bc["dim S44(C^13) * dim S444(C^3)"])


# ====================================================================== B. the certificate
def rank_det_mod(M):
    A = [[x % P for x in r] for r in M]
    nr, nc = len(A), len(A[0])
    det, rk, row = 1, 0, 0
    for col in range(nc):
        piv = next((i for i in range(row, nr) if A[i][col]), None)
        if piv is None:
            det = 0
            continue
        if piv != row:
            A[row], A[piv] = A[piv], A[row]
            det = -det
        det = det * A[row][col] % P
        inv = pow(A[row][col], P - 2, P)
        for i in range(row + 1, nr):
            if A[i][col]:
                f = A[i][col] * inv % P
                A[i] = [(x - f * y) % P for x, y in zip(A[i], A[row])]
        row += 1
        rk += 1
        if row == nr:
            break
    return rk, (det % P if nr == nc and rk == nr else 0)


def solve_mod(E, N):
    n = len(E)
    A = [[x % P for x in E[i]] + [x % P for x in N[i]] for i in range(n)]
    m = len(A[0])
    for col in range(n):
        piv = next(i for i in range(col, n) if A[i][col])
        A[col], A[piv] = A[piv], A[col]
        inv = pow(A[col][col], P - 2, P)
        A[col] = [x * inv % P for x in A[col]]
        for i in range(n):
            if i != col and A[i][col]:
                f = A[i][col]
                A[i] = [(x - f * y) % P for x, y in zip(A[i], A[col])]
    return [r[n:] for r in A]


cert = load("results/b22_01/p2_basis.json", "7162d852b4490d2f22702b9b974979e403dd0dfb8794cef92b6be894d9a66e79")
E = cert["certificate"]["E_rows_points_cols_patterns"]
sel = cert["selected"]
deg11 = [s for s in sel if s["pattern"]["deg"] == 11]
deg12 = [s for s in sel if s["pattern"]["deg"] == 12]
ints = all(isinstance(x, int) and 0 <= x < P for r in E for x in r)
E_from_vec80 = [[deg11[j]["vec80"][i] for j in range(70)] for i in range(70)]
rkE, detE = rank_det_mod(E)
T4 = [[deg12[j]["vec80"][i] for j in range(4)] for i in range(4)]
T70 = [[deg12[j]["vec80"][i] for j in range(4)] for i in range(70)]
rkT4, detT4 = rank_det_mod(T4)
blocks = {}
for s in deg11 + deg12:
    blocks[s["block"]] = blocks.get(s["block"], 0) + 1
kc = sorted(set(tuple(s["pattern"]["kcounts"]) for s in deg11))
out["B"] = {
    "E_shape": [len(E), len(E[0])],
    "E_entries_are_integers_in_[0,P)": ints,
    "E_equals_selected_vec80": E == E_from_vec80,
    "rank_E_mod_P": rkE, "det_E_mod_P": detE, "det_expected": 132757, "det_matches": detE == 132757,
    "top_4x4_minor_mod_P": detT4, "top_expected": 136525, "top_matches": detT4 == 136525,
    "top_70x4_rank": rank_det_mod(T70)[0],
    "patterns_per_block": blocks, "n_deg11": len(deg11), "n_deg12": len(deg12),
    "deg11_kcounts_present": kc,
}

# ====================================================================== C. the decisive rows
def vand_solve(nodes, vals, degs):
    rows = [[pow(t, d, P) for d in degs] for t in nodes]
    return solve_mod(rows, [[v] for v in vals])


ORDER = ["q3", "q7", "n02"]
rows11, rows12, extraction_agree = [], [], 0
for piece in range(1, 13):
    pc = load("results/b22_01/decide/piece_%02d.json" % piece)
    for key in sorted(pc["points"], key=int):
        pt = pc["points"][key]
        d11, d12 = [], []
        for name in ORDER:
            co = vand_solve([1, 2, 3, 4, 5], pt["raw"][name]["values_u1_to_5"], [8, 9, 10, 11, 12])
            d11.append(co[3][0])
            d12.append(co[4][0])
        extraction_agree += (d11 == pt["d11"] and d12 == pt["d12"])
        rows11.append(d11)
        rows12.append(d12)
res11 = [(r[2] - ALPHA * r[0] - BETA * r[1]) % P for r in rows11]
res12 = [(r[2] - ALPHA * r[0] - BETA * r[1]) % P for r in rows12]
X = solve_mod(E, rows11)                                        # coordinates in the certified basis
coord_res = [(x[2] - ALPHA * x[0] - BETA * x[1]) % P for x in X]
# tops: 4 coordinates from rows p_1..p_4
Y = solve_mod(T4, rows12[:4])
top_pred = [[sum(T70[i][j] * Y[j][v] for j in range(4)) % P for v in range(3)] for i in range(70)]
out["C"] = {
    "points": len(rows11),
    "my_extraction_agrees_with_shipped_d11_d12": extraction_agree,
    "rank_140x3_mod_P": rank_det_mod(rows11 + rows12)[0],
    "rank_d11_rows": rank_det_mod(rows11)[0], "rank_d12_rows": rank_det_mod(rows12)[0],
    "relation_residual_zero_d11": sum(1 for r in res11 if r == 0),
    "relation_residual_zero_d12": sum(1 for r in res12 if r == 0),
    "coordinate_relation_residual_zero": sum(1 for r in coord_res if r == 0),
    "top_consistency_rows": sum(1 for i in range(70) if top_pred[i] == rows12[i]),
}

# span control against the ORIGINAL recorded sources
p3 = load("p3_flag_rows.json", "73c3be3c0789d26001953f940792c9086ce19fc72d758566f5bea2c86ece66ee")
b21 = load("p1_type_test.json", "b6d047377cf4c3b082aea9d53a0a93d5ca4f4cf9677131813bc484ad69b0fa2e")
orig = []
for q in p3["new_points"]:
    orig.append(("b20_01_p3_pt%d" % q["point"], {"Z1": q["Z1"], "Z2": q["Z2"], "Z": q["Z"]}, q["row_d11"], q["row_d12"]))
for q in b21["points"]:
    df = q["direct_form"]
    orig.append(("b21_01_" + q["label"], q["Z"], [df["z11"][n] for n in ORDER], [df["z12"][n] for n in ORDER]))
span = []
for i, (label, Z, r11, r12) in enumerate(orig):
    cp = cert["points"][70 + i]
    same_point = (cp["Z1"] == Z["Z1"] and cp["Z2"] == Z["Z2"] and cp["Z"] == Z["Z"])
    v11 = [deg11[j]["vec80"][70 + i] for j in range(70)]
    v12 = [deg12[j]["vec80"][70 + i] for j in range(4)]
    p11 = [sum(v11[j] * X[j][v] for j in range(70)) % P for v in range(3)]
    p12 = [sum(v12[j] * Y[j][v] for j in range(4)) % P for v in range(3)]
    span.append({"label": label, "cert_label": cp["label"], "same_point_as_source": same_point,
                 "pred_d11": p11, "rec_d11": r11, "pred_d12": p12, "rec_d12": r12,
                 "hits": sum(a == b for a, b in zip(p11, r11)) + sum(a == b for a, b in zip(p12, r12))})
out["C"]["span_control"] = span
out["C"]["span_hits"] = sum(s["hits"] for s in span)
out["C"]["span_of"] = 6 * len(span)
out["C"]["span_points_match_original_sources"] = all(s["same_point_as_source"] for s in span)

# the 30 recorded rows, from the original sources
rec = [(r["label"], r["row"]) for r in p3["inherited_rows"]]
rec += [("b20_01_p3_pt%d_d%d" % (q["point"], d), q["row_d%d" % d]) for q in p3["new_points"] for d in (11, 12)]
rec += [("b21_01_%s_z%d" % (q["label"], d), [q["direct_form"]["z%d" % d][n] for n in ORDER]) for q in b21["points"] for d in (11, 12)]
out["C"]["recorded_rows"] = len(rec)
out["C"]["recorded_rows_residual_zero"] = sum(1 for _, r in rec if (r[2] - ALPHA * r[0] - BETA * r[1]) % P == 0)

# ====================================================================== D. normalisation
p00 = load("results/b22_01/decide/piece_00.json")
g = p00["G21_six_sealed"]
d4 = pow(g["det_g"], 4, P)
inv4 = pow(d4, P - 2, P)
SEALED = {"q3": (86170, 376209), "q7": (71919, 469277), "n02": (226580, 41046)}
rowsD = {}
for n, (s11, s12) in SEALED.items():
    pv = g["per_vector"][n]
    rowsD[n] = {"inverse_recipe": [pv["slice_sum_F"] * inv4 % P, pv["slice_top"] * inv4 % P],
                "wrong_recipe": [pv["slice_sum_F"] * d4 % P, pv["slice_top"] * d4 % P],
                "sealed": [s11, s12]}
out["D"] = {"det_g": g["det_g"], "det_g_inv4_recomputed": inv4, "det_g_inv4_shipped": g["det_g_inv4"],
            "shipped_is_inverse_fourth_power": inv4 == g["det_g_inv4"],
            "per_vector": rowsD,
            "inverse_recipe_reproduces_six": all(v["inverse_recipe"] == v["sealed"] for v in rowsD.values()),
            "wrong_recipe_reproduces_none": all(v["wrong_recipe"][k] != v["sealed"][k] for v in rowsD.values() for k in (0, 1))}

flat = []


def walk(o, pre=""):
    if isinstance(o, bool):
        flat.append((pre, o))
    elif isinstance(o, dict):
        for k, v in o.items():
            walk(v, pre + "." + str(k))
    elif isinstance(o, list):
        for i, v in enumerate(o):
            walk(v, pre + "[%d]" % i)


walk(out)
out["boolean_true"] = sum(1 for _, v in flat if v)
out["boolean_total"] = len(flat)
out["boolean_false"] = [k for k, v in flat if not v]
Path(sys.argv[2]).write_text(json.dumps(out, indent=1, default=str) + "\n")
print(json.dumps({k: out[k] for k in ("A",)}, indent=1, default=str)[:3000])
print(json.dumps(out["B"], indent=1)[:1500])
print(json.dumps({k: v for k, v in out["C"].items() if k != "span_control"}, indent=1))
print(json.dumps({k: v for k, v in out["D"].items() if k != "per_vector"}, indent=1))
print("BOOLEANS %d/%d true; false: %s" % (out["boolean_true"], out["boolean_total"], out["boolean_false"]))
