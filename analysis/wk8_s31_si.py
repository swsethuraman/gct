"""Session 31 -- the semi-invariant ring of the 5-arrow Kronecker quiver at
(3,3), by two independent routes, and the crossover that bounds delta_0.

DICTIONARY (derived in results/PREREG_s31.md before any computation).
Rep(K_5,(3,3)) = (M_3)^5 with GL_3 x GL_3 acting by A_k -> P A_k Q.  Since
det(P A Q) = det P det Q det A, the coefficients c_alpha of det(sum s_k A_k)
are semi-invariants of weight (det_P, det_Q).  Writing SI_{(d,d)} for the
weight-(det^d, det^d) part (automatically of degree 3d in the A's):

    SI_{(d,d)}  =  sum_{lam |- 3d, ell(lam) <= 5}  g(lam,(d^3),(d^3)) S_lam(C^5)

by Cauchy in the arrow slot and Kronecker in the two matrix slots.  The
transpose tau : A_k -> A_k^T commutes with GL_5 and fixes det(sum s_k A_k), so
C[D_5] ⊆ SI^tau and

    dim SI^tau_{(d,d)}  =  sum_{ell(lam) <= 5} m_det(lam) dim S_lam(C^5),

m_det being session 26's Peter-Weyl count.  Hence the quiver picture RE-DERIVES
mult <= m_det; it does not sharpen it.

ROUTE (i)  Kronecker: the sums above, using session 26's exact m_det machinery.
ROUTE (ii) Molien/Kostant: dim SI_{(d,d)} is the multiplicity of
(d^3) (x) (d^3) in Sym^{3d}(C^5 (x) C^3 (x) C^3), so by Kostant's alternating
sum over the Weyl group S_3 x S_3,

    dim SI_{(d,d)} = sum_{u,v in S_3} sgn(uv) N(d.1+rho-u.rho, d.1+rho-v.rho),

where N(r,c) counts degree-3d monomials in the 45 variables with row-marginals
r and column-marginals c.  Only the summed 3x3 exponent matrix E matters, and
each entry splits among the five arrows in C(E_ij+4,4) ways, so

    N(r,c) = sum_E prod_{ij} C(E_ij + 4, 4),   E >= 0, row sums r, col sums c.

The two routes share no code and no identity.
"""
import sys, os
from fractions import Fraction
from functools import lru_cache
from math import comb
from itertools import permutations

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk6_s26_core import partitions, z_of, chi_sn, m_det

RHO3 = (2, 1, 0)


# --------------------------------------------------------------- Weyl dims
def dim_S(lam, n=5):
    """dim S_lam(C^n) by the Weyl dimension formula."""
    lam = tuple(lam) + (0,) * (n - len(lam))
    if len(lam) > n:
        return 0
    num, den = 1, 1
    for i in range(n):
        for j in range(i + 1, n):
            num *= lam[i] - lam[j] + j - i
            den *= j - i
    assert num % den == 0
    return num // den


# ---------------------------------------------- ROUTE (i): Kronecker sums
def g_rect(lam, delta, n=3):
    """g(lam, (delta^n), (delta^n)) -- the rectangular Kronecker coefficient."""
    lam = tuple(x for x in lam if x)
    N = n * delta
    if sum(lam) != N:
        return 0
    rect = tuple([delta] * n)
    s = Fraction(0)
    for rho in partitions(N):
        c = chi_sn(lam, rho)
        if c:
            s += Fraction(c, z_of(rho)) * chi_sn(rect, rho) ** 2
    assert s.denominator == 1, (lam, s)
    return int(s)


def dim_SI_kron(delta, tau=False, nvars=5):
    """dim SI_{(delta,delta)} (tau=False) or dim SI^tau (tau=True)."""
    tot = 0
    for lam in partitions(3 * delta):
        if len(lam) > nvars:
            continue
        m = m_det(lam, 3, delta) if tau else g_rect(lam, delta)
        if m:
            tot += m * dim_S(lam, nvars)
    return tot


# --------------------------------------- ROUTE (ii): Molien / Kostant sum
@lru_cache(maxsize=None)
def _rowpoly(r, arrows=5):
    """{(e1,e2): prod_j C(e_j+arrows-1, arrows-1)} over e1+e2+e3 = r."""
    k = arrows - 1
    out = {}
    for e1 in range(r + 1):
        b1 = comb(e1 + k, k)
        for e2 in range(r - e1 + 1):
            out[(e1, e2)] = b1 * comb(e2 + k, k) * comb(r - e1 - e2 + k, k)
    return out


def _N(r, c, arrows=5):
    """# of 3x3 non-negative integer matrices with row sums r, col sums c,
    each entry weighted by C(E_ij + arrows-1, arrows-1)."""
    if min(r) < 0 or min(c) < 0 or sum(r) != sum(c):
        return 0
    p1, p2, p3 = (_rowpoly(r[i], arrows) for i in range(3))
    # convolve rows 1 and 2
    conv = {}
    for (a1, a2), va in p1.items():
        for (b1, b2), vb in p2.items():
            k = (a1 + b1, a2 + b2)
            conv[k] = conv.get(k, 0) + va * vb
    tot = 0
    for (a1, a2), v in conv.items():
        e1, e2 = c[0] - a1, c[1] - a2
        if e1 < 0 or e2 < 0:
            continue
        w = p3.get((e1, e2))
        if w:
            tot += v * w
    return tot


def dim_SI_molien(delta, arrows=5):
    tot = 0
    for u in permutations(range(3)):
        su = 1
        for i in range(3):
            for j in range(i + 1, 3):
                if u[i] > u[j]:
                    su = -su
        r = tuple(delta + RHO3[i] - RHO3[u[i]] for i in range(3))
        for v in permutations(range(3)):
            sv = 1
            for i in range(3):
                for j in range(i + 1, 3):
                    if v[i] > v[j]:
                        sv = -sv
            c = tuple(delta + RHO3[i] - RHO3[v[i]] for i in range(3))
            tot += su * sv * _N(r, c, arrows)
    return tot


def source_dim(delta, nSI1=35):
    """dim Sym^delta(SI_1) = dim Sym^delta(Sym^3 C^5)."""
    return comb(nSI1 - 1 + delta, delta)


if __name__ == '__main__':
    lo = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    hi = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    print("cross-check of the two routes, and the crossover test")
    print("%-4s %-14s %-16s %-16s %s"
          % ("d", "Sym^d(SI_1)", "dim SI (Molien)", "dim SI (Kron)", "SI^tau (Kron)"))
    for d in range(lo, hi + 1):
        src = source_dim(d)
        mo = dim_SI_molien(d)
        kr = dim_SI_kron(d) if d <= 8 else None
        kt = dim_SI_kron(d, tau=True) if d <= 8 else None
        print("%-4d %-14d %-16d %-16s %s%s"
              % (d, src, mo, kr if kr is not None else "-",
                 kt if kt is not None else "-",
                 "   *** src > SI ***" if src > mo else ""))
