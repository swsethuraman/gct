"""B23-03 pilot 1 -- D45 cap P5: the three families T1, T2, T3; dimensions; the cap-minor test;
the certificate D35 not inside Sigma_Pi.  Imports no project code.

Coordinates x = (x0..x4), l = t = x4 on the T2/T3/type-IV side, y = (x0..x3).
Every rank below is either exact over Q (python-flint fmpz_mat) or modulo P = 2^31 - 1
(nmod_mat); a modular rank is a floor for the rank over Q, and the rank at one point is a floor
for the generic rank (lower semicontinuity).  Nothing here is a ceiling unless the report proves one.

  E0  G25: sha256 of the pre-registration snapshot, printed first.
  E1  T3 normal form A0(y) v = y' (x) v'' - v' (x) y'' plus t*B; and T3 with four random skew Phi_r.
      Identity checks (A0 y = 0; adj A0 has columns proportional to y), C = F / t,
      Macaulay coranks of C at k = 2..7 (mod P), exact rank M_4(C).
  E2  Jacobian floors: T3 normal form (gl_5 x Mat_4, 41 params), T3 random Phi (65 params),
      T2 template (55 params), T1 (l, M) -> l det_3 M (50 params) and its orbit rank.
  E3  T1 not in T2: an S_3-symmetric D35 cubic with six rank-one points; LGP; coranks at k = 6, 7.
  E4  the extra quadratic syzygy on C = x0 q1 + x1 q2, and the hand proof's witness.
  E5  the skew-bordered (type IV) cubic vanishes on the claimed plane.
  E6  exact rank M_4 at random members of T1, T2, T3 and at a random cubic (the cap test).
"""
import hashlib
import json
import random
import sys
import time
import traceback
from itertools import combinations_with_replacement, permutations
from pathlib import Path

import flint

T0 = time.perf_counter()
OUT = Path(sys.argv[1])
PREREG = Path("results/b23_03/preregistration_snapshot.md")
P = 2147483647
SEED = 2309181
NV = 5
out = {"pilot": "b23_03_p1_classification", "prereg_path": str(PREREG),
       "prereg_sha256": hashlib.sha256(PREREG.read_bytes()).hexdigest(),
       "modulus_for_floors": P, "seed": SEED, "sections": {}}
print("PREREG_SHA256", out["prereg_sha256"], flush=True)


def dump():
    out["elapsed_s"] = round(time.perf_counter() - T0, 3)
    OUT.write_text(json.dumps(out, indent=1) + "\n")


dump()
rng = random.Random(SEED)

# ------------------------------------------------------------------ polynomial utilities
ZERO_E = (0,) * NV


def mono(d):
    if d < 0:
        return []
    res = []
    for c in combinations_with_replacement(range(NV), d):
        e = [0] * NV
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


def add_all(ps):
    r = {}
    for p in ps:
        r = add(r, p)
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


def neg(p):
    return scal(-1, p)


def var(i):
    return {tuple(1 if j == i else 0 for j in range(NV)): 1}


def lin(v):
    return {tuple(1 if j == i else 0 for j in range(NV)): v[i] for i in range(NV) if v[i]}


def const(c):
    return {ZERO_E: c} if c else {}


def rlin(lo=-3, hi=3):
    v = [rng.randint(lo, hi) for _ in range(NV)]
    while not any(v):
        v = [rng.randint(lo, hi) for _ in range(NV)]
    return lin(v)


def rform(d, lo=-3, hi=3):
    return {e: c for e in mono(d) for c in [rng.randint(lo, hi)] if c}


def sgn(perm):
    s = 1
    for i in range(len(perm)):
        for j in range(i + 1, len(perm)):
            if perm[i] > perm[j]:
                s = -s
    return s


def det(Mx):
    n = len(Mx)
    tot = {}
    for perm in permutations(range(n)):
        t = const(sgn(perm))
        for i in range(n):
            t = mul(t, Mx[i][perm[i]])
            if not t:
                break
        if t:
            tot = add(tot, t)
    return tot


def minor(Mx, i, j):
    return [[Mx[a][b] for b in range(len(Mx)) if b != j] for a in range(len(Mx)) if a != i]


def cof(Mx, i, j):
    d = det(minor(Mx, i, j))
    return d if (i + j) % 2 == 0 else neg(d)


def partial(p, i):
    r = {}
    for e, v in p.items():
        if e[i]:
            f = list(e)
            f[i] -= 1
            r[tuple(f)] = r.get(tuple(f), 0) + v * e[i]
    return r


def coeffs(p, basis):
    return [p.get(e, 0) for e in basis]


def degree_set(p):
    return sorted({sum(e) for e in p})


def rank_exact(rows):
    rows = [list(r) for r in rows]
    if not rows or not rows[0]:
        return 0
    return flint.fmpz_mat(rows).rank()


def macaulay(C, k, exact=False):
    """M_k(C) for a cubic C: rows S_k, columns (partial_i) x S_{k-2}. Returns (rank, rows, cols)."""
    parts = [partial(C, i) for i in range(NV)]
    rows = mono(k)
    idx = {m: i for i, m in enumerate(rows)}
    cols = [(i, m) for i in range(NV) for m in mono(k - 2)]
    M = flint.fmpz_mat(len(rows), len(cols)) if exact else flint.nmod_mat(len(rows), len(cols), P)
    for c, (i, m) in enumerate(cols):
        for e, v in parts[i].items():
            r = idx[tuple(a + b for a, b in zip(e, m))]
            M[r, c] = v if exact else v % P
    return M.rank(), len(rows), len(cols)


def divide_by_var(F, i):
    if any(e[i] == 0 for e in F):
        return None
    return {tuple(a - (1 if j == i else 0) for j, a in enumerate(e)): v for e, v in F.items()}


def profile(C, ks=(2, 3, 4, 5, 6, 7)):
    res = {}
    for k in ks:
        r, nr, nc = macaulay(C, k)
        res[str(k)] = {"rank_mod_P": r, "rows": nr, "cols": nc, "corank_mod_P": nr - r}
    return res


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


M3, M4 = mono(3), mono(4)
TV = 4  # index of t = l

# ------------------------------------------------------------------ T3 construction
PAIRS = [(0, 2), (0, 3), (1, 2), (1, 3)]  # y' = (y0, y1), y'' = (y2, y3)


def A0_std():
    A = [[{} for _ in range(4)] for _ in range(4)]
    for r, (a, b) in enumerate(PAIRS):  # (y ^ v)_{ab} = y_a v_b - y_b v_a
        A[r][b] = var(a)
        A[r][a] = neg(var(b))
    return A


def A0_phi(Phi):
    """row r = the functional v -> y^T Phi_r v, Phi_r skew 4 x 4 (y = x0..x3)."""
    return [[{tuple(1 if q == i else 0 for q in range(NV)): Phi[r][i][j]
              for i in range(4) if Phi[r][i][j]} for j in range(4)] for r in range(4)]


def plus_tB(A, B):
    return [[add(A[i][j], scal(B[i][j], var(TV))) for j in range(4)] for i in range(4)]


def rand_mat(n, lo=-3, hi=3):
    return [[rng.randint(lo, hi) for _ in range(n)] for _ in range(n)]


def rand_skew():
    S = [[0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(i + 1, 4):
            v = rng.randint(-3, 3)
            S[i][j], S[j][i] = v, -v
    return S


store = {}


@section("E1_T3_members")
def e1():
    res = {}
    A0 = A0_std()
    ker = [add_all([mul(A0[r][j], var(j)) for j in range(4)]) for r in range(4)]
    res["A0_std_times_y_is_zero"] = all(not k for k in ker)
    adj = [[cof(A0, j, i) for j in range(4)] for i in range(4)]  # adj[i][j] = cof(j, i)
    prop = all(mul(adj[i][j], var(i2)) == mul(adj[i2][j], var(i))
               for j in range(4) for i in range(4) for i2 in range(4))
    res["adj_A0_std_nonzero"] = any(adj[i][j] for i in range(4) for j in range(4))
    res["adj_A0_std_columns_proportional_to_y"] = prop
    res["det_A0_std_is_zero"] = not det(A0)
    members = []
    for trial in range(2):
        B = rand_mat(4)
        F = det(plus_tB(A0, B))
        C = divide_by_var(F, TV)
        entry = {"kind": "T3 normal form", "B": B, "F_nonzero": bool(F), "t_divides_F": C is not None}
        if C:
            entry["C_degrees"] = degree_set(C)
            entry["profile"] = profile(C)
            entry["rank_M4_exact"] = macaulay(C, 4, exact=True)[0]
            entry["smooth_certified"] = entry["profile"]["6"]["rank_mod_P"] == 210
            store.setdefault("T3_C", []).append(C)
            store.setdefault("T3_B", []).append(B)
        members.append(entry)
    for trial in range(2):
        Phi = [rand_skew() for _ in range(4)]
        B = rand_mat(4)
        A0p = A0_phi(Phi)
        kerp = all(not add_all([mul(A0p[r][j], var(j)) for j in range(4)]) for r in range(4))
        F = det(plus_tB(A0p, B))
        C = divide_by_var(F, TV)
        entry = {"kind": "T3 random skew Phi", "Phi": Phi, "B": B, "A0_times_y_is_zero": kerp,
                 "F_nonzero": bool(F), "t_divides_F": C is not None}
        if C:
            entry["profile"] = profile(C)
            entry["rank_M4_exact"] = macaulay(C, 4, exact=True)[0]
            entry["smooth_certified"] = entry["profile"]["6"]["rank_mod_P"] == 210
            store.setdefault("T3phi", []).append((Phi, B))
        members.append(entry)
    res["members"] = members
    return res


# ------------------------------------------------------------------ E2 Jacobian floors
def orbit_cols(F):
    """tangent of the GL_5 orbit at F: x_j d_i F."""
    return [coeffs(mul(var(j), partial(F, i)), M4) for i in range(NV) for j in range(NV)]


@section("E2_jacobian_floors")
def e2():
    res = {}
    # T3 normal form: (g, B) -> det(A0(gx') + (gx)_t B), tangent at g = I
    A0 = A0_std()
    B = store["T3_B"][0] if store.get("T3_B") else rand_mat(4)
    A = plus_tB(A0, B)
    F = det(A)
    cols = orbit_cols(F)
    cofs = [[cof(A, a, b) for b in range(4)] for a in range(4)]
    cols += [coeffs(mul(var(TV), cofs[a][b]), M4) for a in range(4) for b in range(4)]
    res["T3_normal_form"] = {"params": len(cols), "rank_exact": rank_exact(list(zip(*cols))),
                             "proved_ceiling_aff": 29}
    # T3 with random skew Phi: add the 24 Phi-directions
    Phi = [rand_skew() for _ in range(4)]
    B2 = rand_mat(4)
    A = plus_tB(A0_phi(Phi), B2)
    F = det(A)
    cols = orbit_cols(F)
    cofs = [[cof(A, a, b) for b in range(4)] for a in range(4)]
    cols += [coeffs(mul(var(TV), cofs[a][b]), M4) for a in range(4) for b in range(4)]
    for r in range(4):
        for i in range(4):
            for j in range(i + 1, 4):  # d/dPhi_r[i][j] with Phi_r[j][i] = -Phi_r[i][j]
                cols.append(coeffs(add(mul(var(i), cofs[r][j]), mul(var(j), cofs[r][i]), -1), M4))
    res["T3_random_phi"] = {"params": len(cols), "rank_exact": rank_exact(list(zip(*cols)))}
    # T2 template (B22-10's (2,1)-compression), re-implemented
    l = rlin()
    a = [rlin() for _ in range(4)]
    D = [[rlin(), rlin()] for _ in range(3)]
    A = [[a[0], a[1], a[2], a[3]], [l, {}, D[0][0], D[0][1]], [{}, l, D[1][0], D[1][1]],
         [{}, {}, D[2][0], D[2][1]]]
    F = det(A)
    Q1 = add_all([neg(mul(a[0], D[0][0])), neg(mul(a[1], D[1][0])), mul(l, a[2])])
    Q2 = add_all([neg(mul(a[0], D[0][1])), neg(mul(a[1], D[1][1])), mul(l, a[3])])
    Cf = add(mul(D[2][1], Q1), mul(D[2][0], Q2), -1)
    cols = []
    for (i, j) in [(0, 0), (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 2), (2, 3), (3, 2), (3, 3)]:
        cf = cof(A, i, j)
        cols += [coeffs(mul(var(k), cf), M4) for k in range(NV)]
    cl = add(cof(A, 1, 0), cof(A, 2, 1))
    cols += [coeffs(mul(var(k), cl), M4) for k in range(NV)]
    res["T2_template"] = {"params": len(cols), "rank_exact": rank_exact(list(zip(*cols))),
                          "detA_equals_l_times_C": F == mul(l, Cf), "proved_ceiling_aff": 35}
    # T2 via Sigma_Pi directly: (l, m1, m2, q1, q2) -> l (m1 q1 + m2 q2)
    m1, m2, q1, q2 = rlin(), rlin(), rform(2), rform(2)
    C = add(mul(m1, q1), mul(m2, q2))
    cols = [coeffs(mul(var(k), C), M4) for k in range(NV)]
    cols += [coeffs(mul(l, mul(var(k), q1)), M4) for k in range(NV)]
    cols += [coeffs(mul(l, mul(var(k), q2)), M4) for k in range(NV)]
    cols += [coeffs(mul(l, mul(m1, {e: 1})), M4) for e in mono(2)]
    cols += [coeffs(mul(l, mul(m2, {e: 1})), M4) for e in mono(2)]
    res["T2_via_Sigma_Pi"] = {"params": len(cols), "rank_exact": rank_exact(list(zip(*cols)))}
    # T1: (l, M) -> l det_3 M, and the orbit rank of {(s, g, h): s det g det h = 1}
    Mm = [[rlin() for _ in range(3)] for _ in range(3)]
    dM = det(Mm)
    cols = [coeffs(mul(var(k), dM), M4) for k in range(NV)]
    for i in range(3):
        for j in range(3):
            cf = mul(l, cof(Mm, i, j))
            cols += [coeffs(mul(var(k), cf), M4) for k in range(NV)]
    res["T1"] = {"params": len(cols), "rank_exact": rank_exact(list(zip(*cols)))}

    def lv(p):
        return [p.get(tuple(1 if j == k else 0 for j in range(NV)), 0) for k in range(NV)]
    Mv = [[lv(Mm[i][j]) for j in range(3)] for i in range(3)]
    gens = []
    for which in ("X", "Y"):
        for u in range(3):
            for v in range(3):
                dMv = [[[0] * NV for _ in range(3)] for _ in range(3)]
                for i in range(3):
                    for j in range(3):
                        if which == "X" and i == u:      # (E_uv M)_{ij} = delta_iu M_vj
                            dMv[i][j] = list(Mv[v][j])
                        if which == "Y" and j == v:      # (M E_uv)_{ij} = M_iu delta_vj
                            dMv[i][j] = list(Mv[i][u])
                s = -1 if u == v else 0
                gens.append([s * x for x in lv(l)] + [x for i in range(3) for j in range(3) for x in dMv[i][j]])
    res["T1"]["orbit_rank_exact"] = rank_exact(gens)
    res["T1"]["dimension_upper_bound_aff"] = 50 - res["T1"]["orbit_rank_exact"]
    return res


# ------------------------------------------------------------------ E3 T1 not in T2
@section("E3_T1_not_in_T2")
def e3():
    E = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
    cands = [((1, 2, 5), (0, 1, 4)), ((1, 3, 7), (0, 1, 3)), ((2, 3, 11), (0, 1, 9)),
             ((1, 4, 6), (0, 3, 5))]
    attempts = []
    for a, b in cands:
        rec = {"a": a, "b": b,
               "aEb": sum(a[i] * E[i][j] * b[j] for i in range(3) for j in range(3))}
        perms = list(permutations(range(3)))
        Rs = []
        for s in perms:
            av = [a[s[i]] for i in range(3)]
            bv = [b[s[i]] for i in range(3)]
            Rs.append([av[i] * bv[j] for i in range(3) for j in range(3)])
        rec["span_rank"] = rank_exact(Rs)
        rec["sgn_relation_holds"] = all(sum(sgn(perms[q]) * Rs[q][c] for q in range(6)) == 0 for c in range(9))
        if rec["span_rank"] != 5 or rank_exact(Rs[:5]) != 5 or not rec["sgn_relation_holds"]:
            attempts.append(rec)
            continue
        Nb = Rs[:5]
        Mx = [[lin([Nb[i][3 * r + c] for i in range(5)]) for c in range(3)] for r in range(3)]
        C = det(Mx)
        coords6 = [-sgn(perms[i]) * sgn(perms[5]) for i in range(5)]
        rec["sixth_point_coords_verified"] = all(
            sum(coords6[i] * Nb[i][c] for i in range(5)) == Rs[5][c] for c in range(9))
        pts = [[1 if j == i else 0 for j in range(5)] for i in range(5)] + [coords6]
        rec["points"] = pts

        def ev(p, x):
            return sum(v * x[e.index(1)] for e, v in p.items()) if p else 0

        def rank1(x):
            Mn = [[ev(Mx[r][c], x) for c in range(3)] for r in range(3)]
            return all(Mn[r1][c1] * Mn[r2][c2] - Mn[r1][c2] * Mn[r2][c1] == 0
                       for r1 in range(3) for r2 in range(3) for c1 in range(3) for c2 in range(3))
        rec["all_six_rank_one"] = all(rank1(x) for x in pts)
        rec["LGP_all_5_subsets_det_nonzero"] = all(
            flint.fmpz_mat([pts[q] for q in range(6) if q != drop]).det() != 0 for drop in range(6))

        def evalp(p, x):
            tot = 0
            for e, v in p.items():
                term = v
                for i2, k2 in enumerate(e):
                    term *= x[i2] ** k2
                tot += term
            return tot
        rec["grad_zero_at_points"] = all(evalp(partial(C, i), x) == 0 for x in pts for i in range(5))
        rec["hessian_ranks"] = [rank_exact([[evalp(partial(partial(C, i), j), x) for j in range(5)]
                                            for i in range(5)]) for x in pts]
        rec["partials_rank_exact"] = rank_exact([coeffs(partial(C, i), mono(2)) for i in range(5)])
        prof = profile(C, ks=(4, 5, 6, 7))
        rec["profile"] = prof
        rec["corank_k6"], rec["corank_k7"] = prof["6"]["corank_mod_P"], prof["7"]["corank_mod_P"]
        rec["certificate_passes"] = (rec["sixth_point_coords_verified"] and rec["all_six_rank_one"]
                                     and rec["LGP_all_5_subsets_det_nonzero"]
                                     and rec["corank_k6"] == 6 and rec["corank_k7"] == 6)
        attempts.append(rec)
        if rec["certificate_passes"]:
            break
    return {"attempts": attempts, "passed": any(r.get("certificate_passes") for r in attempts)}


# ------------------------------------------------------------------ E4 the quadratic syzygy on Sigma_Pi
@section("E4_Sigma_Pi_syzygy")
def e4():
    res = {}

    def check(q1, q2):
        C = add(mul(var(0), q1), mul(var(1), q2))
        d1 = [partial(q1, j) for j in range(NV)]
        d2 = [partial(q2, j) for j in range(NV)]

        def Mjk(j, k):
            return add(mul(d1[j], d2[k]), mul(d1[k], d2[j]), -1)
        g = [Mjk(3, 4), neg(Mjk(2, 4)), Mjk(2, 3)]
        s = add_all([mul(g[0], partial(C, 2)), mul(g[1], partial(C, 3)), mul(g[2], partial(C, 4))])
        return C, g, s
    q1, q2 = rform(2), rform(2)
    C, g, s = check(q1, q2)
    res["random"] = {"syzygy_identity_holds": not s, "g_nonzero": any(g),
                     "rank_M4_exact": macaulay(C, 4, exact=True)[0]}
    # the witness of the hand proof: q1 = x2^2 + x3^2, q2 = x4^2 + x2 x3
    q1 = add(mul(var(2), var(2)), mul(var(3), var(3)))
    q2 = add(mul(var(4), var(4)), mul(var(2), var(3)))
    C, g, s = check(q1, q2)
    res["witness"] = {"syzygy_identity_holds": not s,
                      "partials_rank_exact": rank_exact([coeffs(partial(C, i), mono(2)) for i in range(5)]),
                      "g0_has_monomial_free_of_x0_x1": any(e[0] == 0 and e[1] == 0 for e in g[0]),
                      "g0": {str(e): v for e, v in g[0].items()},
                      "rank_M4_exact": macaulay(C, 4, exact=True)[0]}
    return res


# ------------------------------------------------------------------ E5 skew-bordered type lies in Sigma_Pi
@section("E5_type_IV_plane")
def e5():
    res = []
    for trial in range(2):
        u1, u2, u3, w, t = (var(i) for i in range(5))
        S = [[{}, neg(u3), u2], [u3, {}, neg(u1)], [neg(u2), u1, {}]]
        B11 = rand_mat(3)
        B11[0][0] = 0  # z = e1 is then a root of z^T B11 z = 0 with z3 = 0
        c = [rlin() for _ in range(3)]
        a = rlin()
        A = [[add(S[i][j], scal(B11[i][j], t)) for j in range(3)] + [c[i]] for i in range(3)]
        A.append([{}, {}, t, a])
        F = det(A)
        C = divide_by_var(F, TV)
        rec = {"B11": B11, "F_nonzero": bool(F), "t_divides_F": C is not None}
        if C:
            # plane: x1 = B11[2][0] t, x2 = -B11[1][0] t  (u2 = t beta_3, u3 = -t beta_2)
            sub = {}
            for e, v in C.items():
                coef = v * (B11[2][0] ** e[1]) * ((-B11[1][0]) ** e[2])
                ne = (e[0], 0, 0, e[3], e[4] + e[1] + e[2])
                sub[ne] = sub.get(ne, 0) + coef
            rec["C_on_plane_identically_zero"] = not any(sub.values())
            rec["A_restricted_to_H_singular"] = not {e: v for e, v in det(
                [[{k: x for k, x in A[i][j].items() if k[TV] == 0} for j in range(4)] for i in range(4)]).items()}
            rec["rank_M4_exact"] = macaulay(C, 4, exact=True)[0]
        res.append(rec)
    return res


# ------------------------------------------------------------------ E6 the cap test
@section("E6_cap_test")
def e6():
    res = {}
    Mm = [[rlin() for _ in range(3)] for _ in range(3)]
    res["T1_random_D35_cubic"] = macaulay(det(Mm), 4, exact=True)[0]
    m1, m2, q1, q2 = rlin(), rlin(), rform(2), rform(2)
    res["T2_random_plane_cubic"] = macaulay(add(mul(m1, q1), mul(m2, q2)), 4, exact=True)[0]
    res["T3_normal_form_cubics"] = [macaulay(C, 4, exact=True)[0] for C in store.get("T3_C", [])]
    res["random_cubic"] = macaulay(rform(3), 4, exact=True)[0]
    res["M4_shape"] = [70, 75]
    return res


dump()
print(json.dumps(out, indent=1)[:6000], flush=True)
