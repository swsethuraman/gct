"""Week 2, session 2 — conductor-transport mechanism in World B.
(1) Exact order of T along the transversal family f_s = x^2 y + s y^3 + z^3
    (velocity y^3 = the normal direction): expect ord_s = 1, proving nu(T) = 1.
(2) Waring pole calculus on the (lambda_1, 0, 0)-family:
    binary part x^2 y + s y^3 = c1 l1^3 + c2 l2^3 with c1 = -c2 = 1/(6 sigma),
    l_{1,2} = x +- sigma y, sigma^2 = 3 s; l3 = z.  Set sigma = rho^3 so that
    cube-root normalizations are integral in rho.  T-units: pole = -ord_rho/6.
"""
from fractions import Fraction
from itertools import combinations_with_replacement as cwr, permutations
import sympy as sp

mons = [(i, j, 3-i-j) for i in range(3, -1, -1) for j in range(3-i, -1, -1)]
midx = {m: i for i, m in enumerate(mons)}

def apply_V(mono, kind):
    out = {}
    for pos in range(len(mono)):
        I, J, K = mons[mono[pos]]
        if kind == 1:
            if I >= 1 and J+1 <= 3: src = (I-1, J+1, K); w = J+1
            else: continue
        else:
            if J >= 1 and K+1 <= 3: src = (I, J-1, K+1); w = K+1
            else: continue
        if sum(src) != 3: continue
        new = list(mono); new[pos] = midx[src]; new.sort()
        t = tuple(new)
        out[t] = out.get(t, 0) + w
    return out

def build_invariant(degree, weight):
    cand = []
    for combo in cwr(range(10), degree):
        w = [0, 0, 0]
        for idx in combo:
            for t in range(3): w[t] += mons[idx][t]
        if tuple(w) == weight: cand.append(combo)
    eq_index = {}; triples = []
    for kind in (1, 2):
        for ci, combo in enumerate(cand):
            for tgt, w in apply_V(combo, kind).items():
                key = (kind, tgt)
                if key not in eq_index: eq_index[key] = len(eq_index)
                triples.append((eq_index[key], ci, w))
    nr, nc = len(eq_index), len(cand)
    M = [[Fraction(0)]*nc for _ in range(nr)]
    for r, c, w in triples: M[r][c] += w
    rank = 0; pivots = []
    for col in range(nc):
        piv = None
        for r in range(rank, nr):
            if M[r][col] != 0: piv = r; break
        if piv is None: continue
        M[rank], M[piv] = M[piv], M[rank]
        pr = M[rank]; pc = pr[col]
        M[rank] = [a/pc for a in pr]; pr = M[rank]
        for r in range(nr):
            if r != rank and M[r][col] != 0:
                f = M[r][col]
                M[r] = [a - f*b for a, b in zip(M[r], pr)]
        pivots.append(col); rank += 1
    free = [c for c in range(nc) if c not in pivots]
    assert len(free) == 1, len(free)
    sol = [Fraction(0)]*nc; sol[free[0]] = Fraction(1)
    for r, col in enumerate(pivots): sol[col] = -M[r][free[0]]
    from math import gcd
    den = 1
    for v in sol: den = den*v.denominator//gcd(den, v.denominator)
    ints = [int(v*den) for v in sol]
    g = 0
    for v in ints: g = gcd(g, abs(v))
    return cand, [v//g for v in ints]

candS, Sco = build_invariant(4, (4, 4, 4))
candT, Tco = build_invariant(6, (6, 6, 6))

s = sp.Symbol('s')
fam = {(2, 1, 0): 1, (0, 3, 0): s, (0, 0, 3): 1}

def ev(cand, co, assign):
    tot = 0
    for combo, cf in zip(cand, co):
        if cf == 0: continue
        p = sp.Integer(cf)
        for idx in combo:
            v = assign.get(mons[idx], 0)
            if v == 0: p = 0; break
            p = p*v
        tot += p
    return sp.expand(tot)

Sval = ev(candS, Sco, fam)
Tval = ev(candT, Tco, fam)
print("S(f_s) =", Sval, "  (family lies in sigma_3 for all s:", Sval == 0, ")")
Tp = sp.Poly(Tval, s)
print("T(f_s) =", Tval, " => ord_s T =", min(m[0] for m in Tp.monoms()))
print("  => nu_boundary(T) = 1 exactly (transversal family, velocity = normal direction y^3)\n")

# ---------------- Waring pole calculus on (lam1, 0, 0) ----------------
x, y, z, rho = sp.symbols('x y z rho')
sig = rho**3
l1, l2 = x + sig*y, x - sig*y
c1third = sp.Pow(6, sp.Rational(-1, 3)) / rho          # c1^{1/3}
c2third = sp.Pow(-1, sp.Rational(1, 3)) * c1third      # c2^{1/3}
LH = [c1third*l1, c2third*l2, z]                        # lhat_1, lhat_2, lhat_3

def rho_order(expr):
    e = sp.expand(sp.radsimp(sp.powsimp(expr, force=True)))
    e = sp.expand(e * rho**600)
    P = sp.Poly(e, x, y, z, rho)
    degs = [m[3] for m in P.monoms()]
    return (min(degs) - 600) if degs else None

def cls_row(p1, p2, p3):
    """S3-symmetrized  sum over assignments of exponents to the three lines."""
    tot = 0
    seen = set()
    for perm in set(permutations((p1, p2, p3))):
        term = LH[0]**perm[0] * LH[1]**perm[1] * LH[2]**perm[2]
        tot += term
    return sp.expand(sp.powsimp(tot, force=True))

print("pole calculus on the (3delta,0,0)-row (T-units = -ord_rho/6):")
print("formula prediction: conductor(3delta,0,0) = floor(delta/2)")
for delta in (1, 2, 3, 4):
    best = None
    parts = []
    for p1 in range(3*delta, -1, -3):
        for p2 in range(min(p1, 3*delta - p1), -1, -3):
            p3 = 3*delta - p1 - p2
            if p3 > p2 or p3 % 3: continue
            e = cls_row(p1, p2, p3)
            if sp.simplify(e) == 0:
                parts.append(((p1, p2, p3), "vanishes")); continue
            o = rho_order(e)
            pole = sp.Rational(-o, 6)
            assert pole == int(pole), ((p1, p2, p3), o)
            parts.append(((p1, p2, p3), int(pole)))
            if best is None or int(pole) > best: best = int(pole)
    pred = delta // 2
    print(f"  delta={delta}, lam=({3*delta},0,0): class poles {parts} -> max {best}, predicted {pred}",
          "MATCH" if best == pred else "MISMATCH")
