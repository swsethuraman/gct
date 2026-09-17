"""B18-12 small exact check (one process, no BLAS, sympy integers).

(1) Z != empty: the 4-dim singular space X_Lambda = {Lambda(x,.)} with
    Lambda: Wedge^2 C^4 -> C^4 generic integer.  Each Lambda(x,.) kills x, so the
    pencil determinant is identically zero; a nonzero degree-8 semi-invariant
    det(sum_k M_k (x) B_k), M_k in Mat_2, certifies semistability (King).
(2) Independent semistable tuple over a cone: (E11,E22,E33,E44,E12).
(3) Block-triangular fibres: for f in A the value is independent of the
    off-diagonal block (symbolic control); a tau-symmetric degree-8 invariant of R
    is NOT constant there (so the constraint Delta_p has content in R^tau_8).
"""
import random, sympy as sp
random.seed(20260916)
R = lambda: random.randint(-5, 5)
x = sp.symbols('x1:6')

def kron(M, B):
    return sp.Matrix(sp.BlockMatrix([[M[i, j] * B for j in range(M.cols)] for i in range(M.rows)]))

def semi_inv(Bs, Ms):
    return sum((kron(Ms[k], Bs[k]) for k in range(5)), sp.zeros(8, 8)).det()

def tau_semi_inv(Bs, Ms):
    return semi_inv(Bs, Ms) + semi_inv([B.T for B in Bs], Ms)

def pencil_det(Bs):
    return sp.expand(sum((x[k] * Bs[k] for k in range(5)), sp.zeros(4, 4)).det())

out = {}
# ---------- (1) X_Lambda ----------
w = {(i, j): sp.Matrix([R() for _ in range(4)]) for i in range(4) for j in range(i + 1, 4)}
def Lam(xv, yv):
    v = sp.zeros(4, 1)
    for (i, j), wij in w.items():
        v += (xv[i] * yv[j] - xv[j] * yv[i]) * wij
    return v
def Bof(xv):
    cols = [Lam(xv, sp.Matrix([1 if t == c else 0 for t in range(4)])) for c in range(4)]
    return sp.Matrix.hstack(*cols)
E = [sp.Matrix([1 if t == k else 0 for t in range(4)]) for k in range(4)]
Bs1 = [Bof(E[k]) for k in range(4)] + [Bof(E[0] + E[1] + E[2] + E[3])]
out['X_Lambda_pencil_det_is_zero'] = (pencil_det(Bs1) == 0)
out['X_Lambda_each_singular'] = all(B.det() == 0 for B in Bs1)
Ms = [sp.Matrix(2, 2, [R() for _ in range(4)]) for _ in range(5)]
out['X_Lambda_semi_invariant_deg8'] = semi_inv(Bs1, Ms)
out['X_Lambda_tau_semi_invariant_deg8'] = tau_semi_inv(Bs1, Ms)
# ---------- (2) cone fibre, independent tuple ----------
def Eij(i, j):
    M = sp.zeros(4, 4); M[i, j] = 1; return M
Bs2 = [Eij(0, 0), Eij(1, 1), Eij(2, 2), Eij(3, 3), Eij(0, 1)]
out['cone_tuple_pencil_det'] = pencil_det(Bs2)
out['cone_tuple_semi_invariant_deg8'] = semi_inv(Bs2, Ms)
# ---------- (3) block-triangular fibres (1,3) and (2,2) ----------
res = {}
for p in (1, 2):
    q = 4 - p
    B0 = []
    for k in range(5):
        M = sp.zeros(4, 4)
        M[:p, :p] = sp.Matrix(p, p, [R() for _ in range(p * p)])
        M[p:, p:] = sp.Matrix(q, q, [R() for _ in range(q * q)])
        B0.append(M)
    N = []
    for k in range(5):
        M = sp.zeros(4, 4)
        M[:p, p:] = sp.Matrix(p, q, [R() for _ in range(p * q)])
        N.append(M)
    B1 = [B0[k] + N[k] for k in range(5)]
    Ms2 = [sp.Matrix(2, 2, [R() for _ in range(4)]) for _ in range(5)]
    res[p] = {
        'A_control_pencil_dets_equal': (pencil_det(B0) - pencil_det(B1) == 0),
        'R_tau_deg8_value_diag': tau_semi_inv(B0, Ms2),
        'R_tau_deg8_value_offdiag': tau_semi_inv(B1, Ms2),
    }
    res[p]['Delta_nonzero_on_R_tau_8'] = (res[p]['R_tau_deg8_value_diag'] != res[p]['R_tau_deg8_value_offdiag'])
out['block_triangular'] = res
for k, v in out.items():
    print(k, '=', v)
