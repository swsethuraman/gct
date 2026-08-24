"""Week 1 — Sylvester-model pole calculus, tau-formulation (sigma = tau^4).
lhat_i = C_i l_i with C1 = 8^{-1/4} tau^{-1}, C2 = (-1)^{1/4} 8^{-1/4} tau^{-1};
l1 = x + tau^4 y, l2 = x - tau^4 y; normalized wedge w = C1 C2 (l1 /\ l2).
Class e_{p,q,b} = (lhat1^p lhat2^q + (-1)^b lhat1^q lhat2^p) * w^b.
I(f_s) = -s/4 with s = tau^8  =>  pole in I-units = -ord_tau(e)/8.
Also: independent model count of orbit multiplicities vs the 32-group average.
"""
import sympy as sp
import itertools, math, cmath

x, y, tau = sp.symbols('x y tau')
R8 = sp.Rational(-1, 4)
C1 = sp.Pow(8, R8) / tau
C2 = sp.Pow(-1, sp.Rational(1, 4)) * sp.Pow(8, R8) / tau
l1 = x + tau**4 * y
l2 = x - tau**4 * y
wedge_un = -2 * tau**4          # l1 /\ l2
w_norm = sp.expand(C1 * C2 * wedge_un)

def tau_order(expr):
    e = sp.expand(sp.radsimp(sp.powsimp(expr, force=True)))
    e = sp.expand(e * tau**200)           # shift to make all tau-exponents >= 0
    P = sp.Poly(e, x, y, tau)
    degs = [m[2] for m in P.monoms()]
    return (min(degs) - 200) if degs else None

def cls(p, q, b):
    A = (C1*l1)**p * (C2*l2)**q
    B = (C1*l1)**q * (C2*l2)**p
    return sp.expand(sp.powsimp((A + (-1)**b * B) * w_norm**b, force=True))

def pole_I(p, q, b):
    o = tau_order(cls(p, q, b))
    if o is None:
        return None
    po = sp.Rational(-o, 8)
    assert po == int(po), (p, q, b, o)
    return int(po)

print("pole calculus (I-units), class = Sym[lhat1^p lhat2^q] w^b :")
tests = [
    ("(4,0)  d=1  f itself", (4, 0, 0)),
    ("(8,0)  d=2 first deficit", (8, 0, 0)), ("(8,0)  d=2 other class", (4, 4, 0)),
    ("(12,0) d=3", (12, 0, 0)), ("(12,0) d=3", (8, 4, 0)), ("(12,0) d=3", (4, 8, 0)),
    ("(11,1) d=3  b=1", (11, 3, 1)),
    ("(16,0) d=4", (16, 0, 0)), ("(16,0) d=4", (12, 4, 0)), ("(16,0) d=4", (8, 8, 0)),
    ("(14,2) d=4  b=2", (10, 2, 2)), ("(14,2) d=4  b=2", (6, 6, 2)),
]
for name, (p, q, b) in tests:
    e = cls(p, q, b)
    if sp.simplify(e) == 0:
        print(f"  {name} (p,q,b)=({p},{q},{b}): vanishes"); continue
    print(f"  {name} (p,q,b)=({p},{q},{b}): pole_I = {pole_I(p,q,b)}")

print("\nconductor-2 family (32,0) at delta=8, all classes:")
for p in (32, 28, 24, 20, 16):
    q = 32 - p
    print(f"  (p,q)=({p},{q}): pole_I = {pole_I(p, q, 0)}")

# ---------- model count of orbit multiplicities vs group average ----------
I_ = 1j
H = []
for pp in range(4):
    for qq in range(4):
        H.append((I_**pp, I_**qq))
for pp in range(4):
    for qq in range(4):
        z = cmath.exp(1j*math.pi*(pp+qq)/4.0)
        H.append((z, -z))

def schur2(aa, bb, xx, yy):
    m = aa - bb
    if abs(xx - yy) > 1e-9:
        val = (xx**(m+1) - yy**(m+1)) / (xx - yy)
    else:
        val = (m+1) * xx**m
    return (xx*yy)**bb * val

def orbit_avg(aa, bb):
    ssum = sum(schur2(aa, bb, xx, yy) for (xx, yy) in H) / 32
    r = round(ssum.real)
    assert abs(ssum - r) < 1e-6
    return r

def orbit_model(aa, bb):
    n = aa - bb
    cnt = 0
    for p in range(n, -1, -1):
        q = n - p
        if p < q: break
        if (p + bb) % 4 == 0 and (q + bb) % 4 == 0:
            if p == q and bb % 2 == 1:
                continue
            cnt += 1
    return cnt

bad = 0
for tot in range(0, 41, 4):
    for bb in range(-12, tot//2 + 1):
        aa = tot - bb
        if aa < bb: continue
        if orbit_avg(aa, bb) != orbit_model(aa, bb):
            bad += 1
            print("MISMATCH", (aa, bb), orbit_avg(aa, bb), orbit_model(aa, bb))
print(f"\nmodel vs group-average orbit dims: {'ALL MATCH' if bad == 0 else f'{bad} mismatches'} on grid |lambda|<=40 incl. polar sector")
