#!/usr/bin/env python3
"""
Session 24b -- Peter-Weyl counts for the permanent and the padded permanent.

Both stabilisers are MONOMIAL in the natural basis, so m(lam) is exact
coefficient extraction.  Two routes:
  R1  Jacobi-Trudi:  chi_{S_lam}(D f) = det(h_{lam_i-i+j}), sum the
      coefficients over the torus-invariant exponent vectors, average over F.
  R2  Schur-Weyl:    m(lam) = (1/N!) sum_rho |C_rho| chi^lam(rho) E(rho),
      E(rho) = average over H of prod_i tr(k^{rho_i}) -- power sums, no
      determinant, structurally independent of R1.
"""
import sys
from fractions import Fraction
sys.path.insert(0, '/root/gct/analysis')
from wk5_s24b_sf import (partitions, classsize, mn, m_monomial, chi_monomial,
                         padd, pmul, pscal)

# ---------------------------------------------------------------- per_3, GL_9
def perms_per3():
    """the 72 coordinate permutations of {(i,j)} : (P,Q) and (P,Q).transpose."""
    S3 = [(0,1,2),(0,2,1),(1,0,2),(1,2,0),(2,0,1),(2,1,0)]
    out = []
    for P in S3:
        for Q in S3:
            for t in (0, 1):
                pm = [0]*9
                for i in range(3):
                    for j in range(3):
                        ii, jj = (i, j) if t == 0 else (j, i)
                        pm[3*i+j] = 3*P[ii] + Q[jj]
                out.append(tuple(pm))
    assert len(set(out)) == 72, len(set(out))
    return sorted(set(out))

def ok_per3(delta):
    def f(e):
        for i in range(3):
            if sum(e[3*i+j] for j in range(3)) != delta: return False
        for j in range(3):
            if sum(e[3*i+j] for i in range(3)) != delta: return False
        return True
    return f

# --------------------------------------------- padded permanent, GL_{m^2+1}
def perms_perpad():
    """coordinate 0 is x_0 (fixed); coordinates 1..9 are y_ij."""
    out = []
    for pm in perms_per3():
        out.append((0,) + tuple(p + 1 for p in pm))
    return out

def ok_perpad(delta, n):
    p = n - 3
    def f(e):
        if e[0] != delta * p: return False
        for i in range(3):
            if sum(e[1+3*i+j] for j in range(3)) != delta: return False
        for j in range(3):
            if sum(e[1+3*i+j] for i in range(3)) != delta: return False
        return True
    return f

# ------------------------------------------------------------------ route 2
def power_sum_traces(perm, nv, r):
    """tr((diag(x) perm)^r) as a polynomial in nv variables."""
    seen, cycles = [False]*nv, []
    for i in range(nv):
        if seen[i]: continue
        c, j = [], i
        while not seen[j]:
            seen[j] = True; c.append(j); j = perm[j]
        cycles.append(c)
    out = {}
    for c in cycles:
        L = len(c)
        if r % L: continue
        Xc = [0]*nv
        for i in c: Xc[i] += 1
        e = tuple(x * (r // L) for x in Xc)
        out[e] = out.get(e, 0) + L
    return out

def m_monomial_R2(lam, perms, nv, weight_ok):
    from math import factorial
    N = sum(lam)
    tot = Fraction(0)
    for rho in partitions(N):
        E = 0
        for perm in perms:
            prod = {tuple([0]*nv): 1}
            for r in rho:
                prod = pmul(prod, power_sum_traces(perm, nv, r), nv)
                if not prod: break
            E += sum(c for e, c in prod.items() if weight_ok(e))
        E = Fraction(E, len(perms))
        tot += classsize(rho) * mn(lam, rho) * E
    tot /= factorial(N)
    assert tot.denominator == 1, (lam, tot)
    return int(tot)

def m_per3(lam, delta, route=1):
    f = ok_per3(delta)
    return (m_monomial(lam, perms_per3(), 9, f) if route == 1
            else m_monomial_R2(lam, perms_per3(), 9, f))

def m_perpad(lam, delta, n, route=1):
    if len(lam) > 10: return 0
    f = ok_perpad(delta, n)
    return (m_monomial(lam, perms_perpad(), 10, f) if route == 1
            else m_monomial_R2(lam, perms_perpad(), 10, f))

if __name__ == '__main__':
    from wk5_s24b_sf import m_det, plethysm_schur
    print("STEP 2, first weight.  Sym^2(Sym^3) contains no S_(2,2,2), so")
    print("mult_(2,2,2) = 0 for EVERY orbit closure in Sym^3 C^9 and")
    print("def = m there.\n")
    lam = (2, 2, 2)
    v1, v2 = m_per3(lam, 2, 1), m_per3(lam, 2, 2)
    print("  m_per3((2,2,2))  route 1 (Jacobi-Trudi) = %d" % v1)
    print("  m_per3((2,2,2))  route 2 (Schur-Weyl)   = %d" % v2)
    assert v1 == v2
    print("  m_det3((2,2,2))                         = %d" % m_det(lam, 3, 2))
    print()
    print("  => def_per3((2,2,2), 2) = %d ,  def_det3((2,2,2), 2) = %d"
          % (v1, m_det(lam, 3, 2)))
    print("  => P((2,2,2)) = m_per - m_det = %d" % (v1 - m_det(lam, 3, 2)))
