"""B18-01 exact certificate for dim D45 = 50.

phi : (Mat_4)^5 -> Sym^4(C^5*),  phi(B) = det(x0 B0 + ... + x4 B4), ordinary monomial coefficients.

At an integer point B this script computes, exactly over Z (hence over Q):
  J(B)  80 x 70   J[(k,i,j)][alpha] = d c_alpha / d (B_k)_{ij} = [x^alpha] x_k * cof_{ij}(M(x))
  T(B)  31 x 80   rows = tangent vectors (X B_k + B_k Y)_k of the group {(P,Q): det P det Q = 1},
                  for a basis of {(X,Y) in gl4 x gl4 : tr X + tr Y = 0}
and checks  rank_Q J(B) = 50,  rank_Q T(B) = 30,  T(B) J(B) = 0.

Logic (see docs/b18_01_report.md, section 4):
  lower:  dim D45 = generic rank of dphi >= rank dphi_B = rank_Q J(B) = 50.
  upper:  T(B') J(B') = 0 for every B' (Jacobi: d/dt det((1+tX)M(1+tY)) = (trX+trY) det M = 0);
          rank T >= 30 on a dense open set (it is 30 at B); so rank J <= 80-30 = 50 there;
          generic rank of J is attained on a dense open set; the two meet; so dim D45 <= 50.
Controls: Laplace/adjugate identity, Euler identity sum_r B_r J_r = 4*coeff(det), all 70 monomials
present, reproduction of the v1 modular rank, a second independent point, and two negative controls
that must fail (sign-flipped cofactor; a tangent direction with nonzero trace).

Run bounded:  timeout 60 python analysis/b18_01_rank_certificate.py
"""
import hashlib, itertools, json, os, random, sys, time
import flint

t0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "results", "b18_01")
os.makedirs(OUT, exist_ok=True)
NV = 5


def monomials(deg, n=NV):
    """exponent tuples of total degree deg in n variables, descending lexicographic order"""
    out = []
    def rec(prefix, left, k):
        if k == n - 1:
            out.append(tuple(prefix + [left]))
            return
        for e in range(left, -1, -1):
            rec(prefix + [e], left - e, k + 1)
    rec([], deg, 0)
    return out


MON4 = monomials(4)
IDX4 = {m: i for i, m in enumerate(MON4)}
assert len(MON4) == 70


def padd(p, q, s=1):
    r = dict(p)
    for m, c in q.items():
        r[m] = r.get(m, 0) + s * c
        if r[m] == 0:
            del r[m]
    return r


def pmul(p, q):
    r = {}
    for m1, c1 in p.items():
        for m2, c2 in q.items():
            m = tuple(a + b for a, b in zip(m1, m2))
            r[m] = r.get(m, 0) + c1 * c2
    return {m: c for m, c in r.items() if c}


def var(k):
    e = [0] * NV
    e[k] = 1
    return {tuple(e): 1}


def det_poly(A):
    """determinant of a square matrix of polynomials by Laplace expansion along row 0"""
    n = len(A)
    if n == 1:
        return A[0][0]
    tot = {}
    for j in range(n):
        minor = [row[:j] + row[j + 1:] for row in A[1:]]
        tot = padd(tot, pmul(A[0][j], det_poly(minor)), (-1) ** j)
    return tot


def pencil(Bs):
    """M(x)_{ij} = sum_k (B_k)_{ij} x_k as a linear polynomial"""
    return [[{tuple(1 if t == k else 0 for t in range(NV)): Bs[k][i][j] for k in range(NV) if Bs[k][i][j]}
             for j in range(4)] for i in range(4)]


def certificate(Bs, flip_sign=False):
    M = pencil(Bs)
    cof = [[None] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            minor = [[M[r][c] for c in range(4) if c != j] for r in range(4) if r != i]
            sgn = (-1) ** (i + j)
            if flip_sign and (i, j) == (0, 0):
                sgn = -sgn
            cof[i][j] = {m: sgn * c for m, c in det_poly(minor).items()}
    detM = det_poly(M)
    # controls on the cofactors: M * adj(M) = det(M) * I  (adj = cof^T)
    adj_ok = True
    for i in range(4):
        for k in range(4):
            s = {}
            for j in range(4):
                s = padd(s, pmul(M[i][j], cof[k][j]))
            want = detM if i == k else {}
            if s != want:
                adj_ok = False
    rows = []
    for k in range(NV):
        for i in range(4):
            for j in range(4):
                p = pmul(var(k), cof[i][j])
                row = [0] * 70
                for m, c in p.items():
                    row[IDX4[m]] = c
                rows.append(row)
    detvec = [0] * 70
    for m, c in detM.items():
        detvec[IDX4[m]] = c
    euler = [sum(Bs[k][i][j] * rows[(k * 4 + i) * 4 + j][a] for k in range(NV) for i in range(4) for j in range(4))
             for a in range(70)]
    return rows, detvec, adj_ok, euler == [4 * v for v in detvec]


def E(a, b):
    return [[1 if (r, c) == (a, b) else 0 for c in range(4)] for r in range(4)]


def mat_mul(X, Y):
    return [[sum(X[r][t] * Y[t][c] for t in range(4)) for c in range(4)] for r in range(4)]


def mat_add(X, Y, s=1):
    return [[X[r][c] + s * Y[r][c] for c in range(4)] for r in range(4)]


Z4 = [[0] * 4 for _ in range(4)]


def trace_zero_basis():
    basis = []
    for a in range(4):
        for b in range(4):
            if a != b:
                basis.append((E(a, b), Z4))
    for a in range(4):
        for b in range(4):
            if a != b:
                basis.append((Z4, E(a, b)))
    for a in range(3):
        basis.append((mat_add(E(a, a), E(3, 3), -1), Z4))
        basis.append((Z4, mat_add(E(a, a), E(3, 3), -1)))
    basis.append((E(0, 0), [[-x for x in row] for row in E(0, 0)]))
    assert len(basis) == 31
    return basis


def tangent_rows(Bs, basis):
    out = []
    for X, Y in basis:
        v = []
        for k in range(NV):
            W = mat_add(mat_mul(X, Bs[k]), mat_mul(Bs[k], Y))
            v.extend(W[i][j] for i in range(4) for j in range(4))
        out.append(v)
    return out


def rank_Z(rows):
    return flint.fmpz_mat(rows).rank()


def rank_p(rows, p):
    return flint.nmod_mat(rows, p).rank()


def sha_rows(rows):
    return hashlib.sha256(json.dumps(rows, separators=(",", ":")).encode()).hexdigest()


def run_point(name, Bs):
    J, detvec, adj_ok, euler_ok = certificate(Bs)
    T = tangent_rows(Bs, trace_zero_basis())
    TJ = flint.fmpz_mat(T) * flint.fmpz_mat(J)
    TJ_zero = all(TJ[r, c] == 0 for r in range(TJ.nrows()) for c in range(TJ.ncols()))
    # negative control 1: sign-flipped cofactor must break the adjugate identity
    _, _, adj_bad, euler_bad = certificate(Bs, flip_sign=True)
    # negative control 2: a tangent direction with tr X + tr Y != 0 must NOT be annihilated
    T_bad = tangent_rows(Bs, [(E(0, 0), Z4)])
    TJ_bad = flint.fmpz_mat(T_bad) * flint.fmpz_mat(J)
    bad_nonzero = any(TJ_bad[0, c] != 0 for c in range(70))
    bad_is_det = [int(TJ_bad[0, c]) for c in range(70)] == detvec   # (tr X + tr Y) * coeff(det), trX+trY = 1
    rec = {
        "point": name, "B": Bs,
        "rank_Q_J": rank_Z(J), "rank_Q_T": rank_Z(T), "T_times_J_is_zero": TJ_zero,
        "rank_mod_2147483647_J": rank_p(J, 2147483647), "rank_mod_65521_J": rank_p(J, 65521),
        "controls": {"adjugate_identity": adj_ok, "euler_identity": euler_ok,
                     "det_has_all_70_monomials": all(v != 0 for v in detvec),
                     "NEGATIVE_sign_flip_breaks_adjugate_identity": (not adj_bad) and (not euler_bad),
                     "NEGATIVE_trace_one_direction_not_annihilated": bad_nonzero,
                     "trace_one_direction_gives_det_coefficients": bad_is_det},
        "J_sha256": sha_rows(J), "T_sha256": sha_rows(T), "det_coefficients": detvec,
    }
    return rec, J, T


V1_POINT = [
    [[1, 0, 2, -1], [3, 1, 0, 4], [-2, 5, 1, 0], [0, -3, 2, 1]],
    [[2, -1, 1, 0], [0, 3, -2, 1], [1, 0, 4, -3], [5, 2, 0, 1]],
    [[-1, 4, 0, 2], [1, -2, 3, 0], [0, 1, -1, 5], [2, 0, 1, -4]],
    [[3, 1, -2, 0], [-1, 0, 1, 2], [4, -3, 0, 1], [0, 2, 5, -1]],
    [[0, 2, 1, 3], [2, -1, 0, 1], [-3, 1, 2, 0], [1, 4, -2, 0]],
]
rng = random.Random(1801)
SECOND = [[[rng.randint(-9, 9) for _ in range(4)] for _ in range(4)] for _ in range(5)]

results = []
matrices = {}
for name, Bs in (("v1_point", V1_POINT), ("seed_1801", SECOND)):
    rec, J, T = run_point(name, Bs)
    results.append(rec)
    matrices[name] = {"J_rows_k_i_j__cols_monomials": J, "T_rows_basis__cols_k_i_j": T}

verdict = all(r["rank_Q_J"] == 50 and r["rank_Q_T"] == 30 and r["T_times_J_is_zero"]
              and all(r["controls"].values()) for r in results)
out = {
    "schema": "b18_01-rank-certificate/1",
    "statement": "dim D45 = 50 (affine cone in C^70), dim P(D45) = 49",
    "conventions": "ordinary coefficients c_alpha=[x^alpha]F; J row order (k,i,j) lexicographic; "
                   "monomial columns = exponent tuples of degree 4 in x0..x4, descending lexicographic",
    "monomial_order": MON4,
    "trace_zero_basis": "12 X=E_ab (a!=b); 12 Y=E_ab (a!=b); X=E_aa-E_33 (a=0,1,2) and Y likewise, interleaved; (X,Y)=(E_00,-E_00)",
    "points": results,
    "verdict_all_checks_pass": verdict,
    "script_sha256": hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(),
    "python": sys.version.split()[0], "python_flint": flint.__version__,
    "wall_seconds": round(time.time() - t0, 3),
}
with open(os.path.join(OUT, "rank_certificate.json"), "w", newline="\n") as f:
    json.dump(out, f, indent=1)
with open(os.path.join(OUT, "rank_certificate_matrices.json"), "w", newline="\n") as f:
    json.dump(matrices, f, separators=(",", ":"))
for r in results:
    print(r["point"], "rank_Q J =", r["rank_Q_J"], " rank_Q T =", r["rank_Q_T"], " T*J=0:", r["T_times_J_is_zero"],
          " rank mod p:", r["rank_mod_2147483647_J"], r["rank_mod_65521_J"], " controls:", r["controls"])
print("VERDICT", verdict, "seconds", out["wall_seconds"])
