#!/usr/bin/env python3
"""
Session 57 -- a numerical check of Theorem P (report section 1): at a random
determinantal quartic f = det(sum_i s_i A_i) in ell variables, the bordered
discriminant

    h(f) = c . det(G_2) - (3/8) g_1^T adj(G_2) g_1,

with c = [s_1^4] f, g_1 = [s_1^3] f (a linear form in s_2..s_ell), G_2 the symmetric
matrix of the quadric [s_1^2] f, is nonzero.  Exact rational arithmetic (sympy),
ell = 6..10, several seeds.  Also checks the identity h(f) = c^{ell} .
disc(e_2(B) - (3/8) tr(B)^2) with B = A_1^{-1} A(s') (so that h(f) / c^{ell} is
the discriminant of -1/2 tr(B_0^2), B_0 the traceless part), which is the form the
proof uses.

usage: python3 wk9_s57_thmP_check.py
"""
import sys, random
import sympy as sp

def bordered_disc(f, s):
    ell = len(s); s1 = s[0]; tail = s[1:]
    P = sp.Poly(f, *s)
    c = P.coeff_monomial(s1**4)
    g1 = [P.coeff_monomial(s1**3 * t) for t in tail]
    G = sp.zeros(ell - 1, ell - 1)
    for i, ti in enumerate(tail):
        G[i, i] = P.coeff_monomial(s1**2 * ti**2)
        for j in range(i + 1, ell - 1):
            G[i, j] = G[j, i] = sp.Rational(1, 2) * P.coeff_monomial(s1**2 * ti * tail[j])
    g = sp.Matrix(g1)
    return c * G.det() - sp.Rational(3, 8) * (g.T * G.adjugate() * g)[0, 0], c, g, G

if __name__ == '__main__':
    rnd = random.Random(57)
    ok = True
    for ell in range(6, 11):
        for seed in range(3 if ell < 10 else 1):
            s = sp.symbols('s1:%d' % (ell + 1))
            A = [sp.Matrix(4, 4, lambda i, j: rnd.randint(-3, 3)) for _ in range(ell)]
            while A[0].det() == 0:
                A[0] = sp.Matrix(4, 4, lambda i, j: rnd.randint(-3, 3))
            M = sum((s[k] * A[k] for k in range(ell)), sp.zeros(4, 4))
            f = sp.expand(M.det())
            h, c, g, G = bordered_disc(f, s)
            # the proof's form: B = A_1^{-1} A(s'), q = e_2(B) - 3/8 tr(B)^2 = -1/2 tr(B_0^2)
            Bp = sum((s[k] * (A[0].inv() * A[k]) for k in range(1, ell)), sp.zeros(4, 4))
            tr = Bp.trace(); tr2 = (Bp * Bp).trace()
            q = sp.expand((tr**2 - tr2) / 2 - sp.Rational(3, 8) * tr**2)
            Q = sp.zeros(ell - 1, ell - 1)
            Pq = sp.Poly(q, *s[1:])
            for i in range(ell - 1):
                Q[i, i] = Pq.coeff_monomial(s[1 + i]**2)
                for j in range(i + 1, ell - 1):
                    Q[i, j] = Q[j, i] = sp.Rational(1, 2) * Pq.coeff_monomial(s[1 + i] * s[1 + j])
            rhs = c**ell * Q.det()
            good = (h != 0) and sp.simplify(h - rhs) == 0
            ok &= good
            print(f"ell={ell} seed={seed}: c={c}, h(f)={h}, c^ell disc(q)={rhs}, nonzero and equal: {good}")
    print("ALL CHECKS PASSED" if ok else "*** CHECK FAILED ***")
    sys.exit(0 if ok else 1)
