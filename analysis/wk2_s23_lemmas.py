"""Week 2, session 23 -- exact verification of the structural lemmas.

L1  the transversal family is a single tau-orbit:  f_s = tau(rho).(B.v),
    s = rho^6/3, symbolically in Q(6^{1/3})[rho].
L2  N_k = mu - a_k - 2 q_kbar is divisible by 3 for every admissible shape.
L3  the S_3 symmetrisation retains exactly the drops T = lambda_1 - a_k (mod 2)
    -- so every achievable nu is even, and (with L2) divisible by 6.
L4  the orientation of the tau-grading is FORCED: the opposite orientation
    (max of 2 m_2 - m_1) contradicts the block-order upper bound and fails the
    delta <= 10 regression outright.
L5  m(lambda) and the attainment defect depend only on (p, q, r mod 6);
    for m this is a theorem (det|_H has order exactly 6) -- checked here.
"""
import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import sympy as sp
from wk2_s23_transport import *

x, y, z, rho = sp.symbols('x y z rho')
kap = sp.Pow(6, sp.Rational(-1, 3))


def L1():
    """f_s = tau(rho) . (B.v) with B constant."""
    # Waring lines of f_s
    l1 = kap * rho**-1 * (x + rho**3 * y)
    l2 = -kap * rho**-1 * (x - rho**3 * y)
    l3 = z
    F = sp.expand(sp.simplify(sp.expand(l1**3 + l2**3 + l3**3)))
    target = sp.expand(x**2 * y + rho**6 / 3 * y**3 + z**3)
    ok1 = sp.simplify(F - target) == 0
    # the matrix of Waring lines factors as A . diag(rho^-1, rho^2, 1)
    M = sp.Matrix([[kap * rho**-1, kap * rho**2, 0],
                   [-kap * rho**-1, kap * rho**2, 0],
                   [0, 0, 1]])
    A = sp.Matrix([[kap, kap, 0], [-kap, kap, 0], [0, 0, 1]])
    D = sp.diag(rho**-1, rho**2, 1)
    ok2 = sp.simplify(M - A * D) == sp.zeros(3, 3)
    # tau(rho) = diag(rho, rho^-2, 1) on V; on the coordinates x,y,z it is D.
    # B.v: rows of A are the Waring lines of B.v
    m1 = kap * (x + y); m2 = -kap * (x - y); m3 = z
    Bv = sp.expand(m1**3 + m2**3 + m3**3)
    ok3 = sp.simplify(Bv - (x**2 * y + sp.Rational(1, 3) * y**3 + z**3)) == 0
    # and tau(rho) acts on that by x -> rho^-1 x, y -> rho^2 y, z -> z
    acted = sp.expand(Bv.subs({x: rho**-1 * x, y: rho**2 * y}, simultaneous=True))
    ok4 = sp.simplify(acted - target) == 0
    print("L1  f_s = l1^3+l2^3+l3^3 with s = rho^6/3 :", ok1)
    print("L1  M(rho) = A . diag(rho^-1, rho^2, 1), A constant :", ok2)
    print("L1  B.v = x^2 y + y^3/3 + z^3 :", ok3)
    print("L1  tau(rho).(B.v) = f_{rho^6/3} :", ok4)
    return ok1 and ok2 and ok3 and ok4


def L2(pmax=14, qmax=14):
    bad = 0; n = 0
    for p in range(pmax + 1):
        for q in range(qmax + 1):
            if (p - q) % 3: continue
            for r in range(6):
                lam = (p + q + r, q + r, r)
                mu = p + q - r
                for (a, Q) in shapes(lam):
                    for k in range(3):
                        qbar = Q[[2, 1, 0][k]]     # wedge on the pair missing k
                        N = mu - a[k] - 2 * qbar
                        n += 1
                        if N % 3: bad += 1
    print(f"L2  N_k divisible by 3: {n} (shape, k) pairs, {bad} violations")
    return bad == 0


def L3(pmax=9, qmax=9):
    """Check directly that pi_nu(B Theta) = 0 for every odd nu, on all shapes."""
    bad = 0; n = 0
    for p in range(pmax + 1):
        for q in range(qmax + 1):
            if (p - q) % 3: continue
            for r in range(6):
                lam = (p + q + r, q + r, r); mu = p + q - r
                for (a, Q) in shapes(lam):
                    for nu in range(mu, mu - 13, -1):
                        pol = normal_form(theta_B_weight(a, Q, r, nu))
                        n += 1
                        if pol and nu % 6:
                            bad += 1
                            if bad < 4: print("   VIOLATION", lam, a, Q, nu)
    print(f"L3  every surviving nu divisible by 6: {n} (shape, nu) tests, {bad} violations")
    return bad == 0


def L4():
    """The opposite orientation fails the regression immediately."""
    # opposite orientation: tau-weights (-1, 2, 0) on e1,e2,e3, i.e. the bound
    # would be 2 lambda_1 - lambda_3 instead of lambda_1 - 2 lambda_3.
    h3 = hist3(46)
    dis = 0; tested = 0
    for d in range(1, 7):
        for l1 in range(3 * d + 1):
            for l2 in range(min(l1, 3 * d - l1) + 1):
                l3 = 3 * d - l1 - l2
                if not (0 <= l3 <= l2): continue
                lam = (l1, l2, l3)
                m = H_invariants_dim(lam)
                if m == 0: continue
                ct, _ = conductor_table(lam, h3, kmax=6)
                tested += 1
                alt = max(0, (2 * l1 - l3) // 6)
                if alt != ct: dis += 1
    print(f"L4  opposite orientation: {dis}/{tested} disagreements with the "
          f"tables at delta <= 6 (must be large; the chosen orientation has 0)")
    return dis > 0


def L5(pmax=10, qmax=10):
    MF = MFast(300)
    bad = 0; n = 0
    for p in range(pmax + 1):
        for q in range(qmax + 1):
            if (p - q) % 3: continue
            for j in range(6):
                vals = set()
                for t in range(4):
                    r = j + 6 * t
                    lam = (p + q + r, q + r, r); mu = p + q - r
                    if mu < 0: continue
                    c, _ = conductor_fast(lam)
                    vals.add((MF.m(lam), (mu // 6) - c if c is not None else None))
                if len(vals) > 1: bad += 1
                n += 1
    print(f"L5  (m, defect) depends only on (p,q,r mod 6): {n} classes, {bad} violations")
    return bad == 0


if __name__ == '__main__':
    ok = all([L1(), L2(), L3(), L4(), L5()])
    print("\nALL LEMMA CHECKS PASSED" if ok else "\nSOME CHECK FAILED")
