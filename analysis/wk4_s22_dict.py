"""Session 22: the slot dictionary and the character chi, from scratch.

Conventions (all rebuilt here, none imported):
  V = M_3 = C^9, coordinate index 3i+j (i = row, j = column).
  A transvection "x_{3i+j} += x_k" (i in {1,2}) contributes 1 to (A or B)_{j,k}:
  row i of the matrix receives (A or B) applied to row 0.
  u_N acts on V with ROW 0 RECEIVING (session 17's orientation refinement):
        (u_N X)_{0j} = X_{0j} + sum_l A_{lj} X_{1l} + sum_l B_{lj} X_{2l},
  other rows unchanged.  W = {X : row 0 = 0} = span{x_3..x_8}, Q = Stab(W).
  Gamma_N = u_N^{-1}(W) = ker(first three rows of u_N),
  so Gamma_N^perp = rowspan(first three rows of u_N) = the net, and the j-th
  row of u_N IS the net element Y_j with rows (e_j^T, (A e_j)^T, (B e_j)^T):
  the canonical parameter v is exactly the u_N-transported basis of W^perp.
"""
import sympy as sp
from sympy import Rational as Q

Z = sp.zeros

def mat_from_transvections(tv):
    """tv: list of (target_index, source_index) with target in rows 1,2."""
    A = Z(3,3); B = Z(3,3)
    for t, s in tv:
        i, j = divmod(t, 3); ii, k = divmod(s, 3)
        assert ii == 0 and i in (1,2), (t,s)
        (A if i == 1 else B)[j, k] += 1
    return A, B

def uN(A, B):
    """9x9 matrix of u_N acting on V (row 0 receives)."""
    U = sp.eye(9)
    for j in range(3):
        for l in range(3):
            U[0*3+j, 1*3+l] += A[l, j]
            U[0*3+j, 2*3+l] += B[l, j]
    return U

def net_rows(A, B):
    """3x9 matrix whose rows span Gamma_N^perp, in the canonical v-basis."""
    return uN(A, B)[0:3, :]

def as_mat(row):
    return sp.Matrix(3, 3, list(row))

def graph_normalise(R):
    """R: 3x9 rows spanning a net.  Return (A', B', G) with G the 3x3 matrix of
    row-0 parts (G[j,l] = (Z_j)_{0l}); the graph basis is G^{-1} R."""
    Zs = [as_mat(R[j, :]) for j in range(3)]
    G = sp.Matrix(3, 3, lambda j, l: Zs[j][0, l])
    if G.det() == 0:
        return None, None, G
    Gi = G.inv()
    Ys = [sum((Gi[m, j] * Zs[j] for j in range(3)), Z(3,3)) for m in range(3)]
    for m in range(3):                      # sanity: row 0 of Y_m is e_m
        tgt = sp.Matrix([[1 if k == m else 0 for k in range(3)]])
        assert sp.simplify(sp.Matrix([list(Ys[m][0, :])]) - tgt) == sp.zeros(1,3)
    A = sp.Matrix(3, 3, lambda l, m: Ys[m][1, l])
    B = sp.Matrix(3, 3, lambda l, m: Ys[m][2, l])
    return A, B, G

# ---------- H, Q, chi ----------------------------------------------------
def h_elt(a, b, transpose=False):
    """9x9 matrix of X -> a X b  (optionally X -> a X^T b)."""
    T = Z(9,9)
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    src = (3*l+k) if transpose else (3*k+l)
                    T[3*i+j, src] += a[i, k]*b[l, j]
    return T

x = sp.symbols('x0:9')
def det3_form(T=None):
    X = sp.Matrix(3, 3, lambda i, j: x[3*i+j])
    if T is not None:
        y = T*sp.Matrix(9, 1, list(x))
        X = sp.Matrix(3, 3, list(y))
    return sp.expand(X.det())

def chi(q):
    """chi(q) = det(q|_{V/W})^8 * det(q|_W)^6 for q in Q = Stab(W),
    W = span{e_3..e_8}, V/W = the first three coordinates."""
    # q preserves W  <=>  q maps e_3..e_8 into W  <=>  top-right 3x6 block zero
    assert all(sp.simplify(q[i, j]) == 0 for i in range(3) for j in range(3, 9)), "q does not preserve W"
    d3 = q[0:3, 0:3].det()
    d6 = q[3:9, 3:9].det()
    return sp.nsimplify(d3**8 * d6**6)

# ---------- Psi ----------------------------------------------------------
def Psi(A, B):
    tr = lambda M: sp.trace(M)
    u1 = tr(A*A)*tr(B*B) - tr(A*B)**2
    u2 = tr(A*A*B*B) - tr(A*B*A*B)
    D  = (tr(A)*tr(B) - tr(A*B))**2 - ((tr(A)**2 - tr(A*A))*(tr(B)**2 - tr(B*B)))
    return sp.expand(2*u1 - 4*u2 - D)

# ---------- the transported point ---------------------------------------
def transport(A, B, t):
    """Gamma_{N'} = t Gamma_N.  Returns (A', B', G, q) with q = u_{N'} t u_N^{-1}."""
    U = uN(A, B)
    R = U[0:3, :]
    Rp = R * t.inv()                    # net of N' : rowspan(R t^{-1})
    Ap, Bp, G = graph_normalise(Rp)
    if Ap is None:
        return None, None, G, None
    q = uN(Ap, Bp) * t * U.inv()
    return Ap, Bp, G, q

BANK = {
 'C':   [(5,1),(7,2)],
 'R':   [(3,0),(7,1)],
 'T4':  [(3,0),(4,1),(7,1),(8,2)],
 'X4':  [(3,0),(7,2),(8,1)],
 'Xm3': [(3,2),(4,1),(7,1),(8,0)],
 'P':   [(3,0),(6,0)],
}
if __name__ == '__main__':
    print("=== validation of conventions against the banked pencils ===")
    exp = {'C':1,'R':1,'T4':1,'X4':4,'Xm3':-3,'P':0}
    for k, tv in BANK.items():
        A, B = mat_from_transvections(tv)
        Ac, Bc, G = graph_normalise(net_rows(A, B))
        ok = (Ac == A and Bc == B and G == sp.eye(3))
        print(f"  {k:4s} A={list(A)} B={list(B)}  Psi={Psi(A,B)}  (expected {exp[k]})  net-roundtrip {ok}")

# =========================================================================
#  TESTS
# =========================================================================
import random, itertools

def rand_sl3(rng, k=3):
    """Random SL_3(Z) matrix as a product of elementary transvections."""
    M = sp.eye(3)
    for _ in range(6):
        i, j = rng.sample(range(3), 2)
        M = M * (sp.eye(3) + rng.randint(-k, k)*sp.Matrix(3,3, lambda a,b: 1 if (a,b)==(i,j) else 0))
    return M

def rand_pencil(rng, k=3):
    return (sp.Matrix(3,3, lambda i,j: rng.randint(-k,k)),
            sp.Matrix(3,3, lambda i,j: rng.randint(-k,k)))

def run_case(A, B, a, b, transpose, label):
    t = h_elt(a, b, transpose)
    Ap, Bp, G, q = transport(A, B, t)
    if Ap is None:
        return None
    # q must preserve W
    assert all(q[i,j] == 0 for i in range(3) for j in range(3,9)), f"{label}: q leaves Q"
    ch = chi(q)
    dG = sp.simplify(G.det())
    pred = sp.simplify(dG**-2)
    psi0, psi1 = Psi(A,B), Psi(Ap,Bp)
    row = dict(label=label, chi=sp.simplify(ch), predicted=pred, detG=dG,
               psi=psi0, psip=sp.simplify(psi1),
               psi_ratio=(sp.simplify(psi1/psi0) if psi0 != 0 else None),
               detq3=sp.simplify(q[0:3,0:3].det()), detq6=sp.simplify(q[3:9,3:9].det()),
               dett=sp.simplify(t.det()))
    return row

if __name__ == '__main__':
    print()
    print("=== 0. t in H really fixes det_3 (symbolic, both cosets) ===")
    rng = random.Random(2202)
    f0 = det3_form()
    for tr in (False, True):
        a = rand_sl3(rng); b = rand_sl3(rng)
        t = h_elt(a, b, tr)
        ok = sp.expand(det3_form(t) - f0) == 0
        print(f"  transpose={tr}: det(a)det(b)={a.det()*b.det()}, t.det()={t.det()}, fixes det_3: {ok}")

    print()
    print("=== 1. HOMOGENEITY CALIBRATION: N -> s N, s = d^3 (symbolic in d) ===")
    d = sp.symbols('d', positive=True)
    a = sp.diag(d**2, 1/d, 1/d); b = sp.eye(3)
    A, B = mat_from_transvections(BANK['C'])
    t = h_elt(a, b)
    Ap, Bp, G, q = transport(A, B, t)
    Ap = sp.simplify(Ap); Bp = sp.simplify(Bp)
    print(f"  det(a)det(b) = {sp.simplify(a.det()*b.det())}")
    print(f"  (A',B') = (s A, s B) with s = {sp.simplify((Ap[2,1]/A[2,1]))} ; B'/B = {sp.simplify(Bp[1,2]/B[1,2])}")
    print(f"  det G = {sp.simplify(G.det())},  predicted chi = det(G)^-2 = {sp.simplify(G.det()**-2)}")
    print(f"  chi(q) computed from det(q|V/W)^8 det(q|W)^6 = {sp.simplify(chi(q))}")
    print(f"  Psi ratio = {sp.simplify(Psi(Ap,Bp)/Psi(A,B))}   [must equal s^4 = d^12]")
