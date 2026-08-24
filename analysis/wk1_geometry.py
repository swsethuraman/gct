"""Week 1, session 1 — geometry package at the boundary point w0 = x^3 y of
sigma_2(v_4) in binary quartics, all exact/symbolic.

Conventions: binary quartic in binomial-normalized coordinates
  f = a0 x^4 + 4 a1 x^3 y + 6 a2 x^2 y^2 + 4 a3 x y^3 + a4 y^4.
Classical invariants: I = a0 a4 - 4 a1 a3 + 3 a2^2 (degree 2, weight det^4),
J = det Hankel[[a0,a1,a2],[a1,a2,a3],[a2,a3,a4]] (degree 3, weight det^6,
the catalecticant), and disc proportional to I^3 - 27 J^2.
sigma_2-cone = {J = 0}.  Torus T1 = stabilizer of w0: t . f(x,y) = f(t x, t^-3 y).
"""
import sympy as sp

x, y, t, s, sig = sp.symbols('x y t s sigma')
a = sp.symbols('a0:5')

def coeffs_of(f):
    # binomial-normalized coefficients of a binary quartic
    P = sp.Poly(sp.expand(f), x, y)
    out = []
    for j in range(5):
        c = P.coeff_monomial(x**(4-j)*y**j)
        out.append(sp.nsimplify(c / sp.binomial(4, j)))
    return out

def I_inv(c):
    return sp.expand(c[0]*c[4] - 4*c[1]*c[3] + 3*c[2]**2)

def J_inv(c):
    M = sp.Matrix([[c[0], c[1], c[2]], [c[1], c[2], c[3]], [c[2], c[3], c[4]]])
    return sp.expand(M.det())

# ---------- 0. disc = 256 (I^3 - 27 J^2) for this normalization ----------
fgen = a[0]*x**4 + 4*a[1]*x**3*y + 6*a[2]*x**2*y**2 + 4*a[3]*x*y**3 + a[4]*y**4
c = [a[0], a[1], a[2], a[3], a[4]]
disc_poly = sp.discriminant(sp.Poly(fgen.subs(y, 1), x))
lhs = sp.expand(disc_poly)
rhs = sp.expand(256*(I_inv(c)**3 - 27*J_inv(c)**2))
print("disc == 256(I^3 - 27 J^2):", sp.simplify(lhs - rhs) == 0)

# ---------- 1. the transversal family f_s = x^3 y + s x y^3 lies in sigma_2 ----------
fs = x**3*y + s*x*y**3
cs = coeffs_of(fs)
print("J(f_s) == 0 for all s:", sp.simplify(J_inv(cs)) == 0)
print("I(f_s) =", I_inv(cs))
disc_fs = sp.expand(256*(I_inv(cs)**3 - 27*J_inv(cs)**2))
print("disc(f_s) =", disc_fs, "   => ord_s = 3, and disc|_sigma2 = 256 I^3 exactly (J = 0)")

# tangent path ((x+eps y)^4 - x^4)/(4 eps): contact order check
eps = sp.symbols('epsilon')
fe = sp.expand(((x + eps*y)**4 - x**4)/(4*eps))
ce = coeffs_of(fe)
disc_fe = sp.factor(256*(I_inv(ce)**3 - 27*J_inv(ce)**2))
print("disc(tangent path) =", disc_fe, "  (expect ord_eps = 6 = contact 2 x e0 3)")

# ---------- 2. tangent spaces and torus weights at w0 = x^3 y ----------
# gradient of J at w0 (b-coordinates)
w0c = coeffs_of(x**3*y)                      # (0, 1/4, 0, 0, 0)
grad = [sp.diff(J_inv(c), ai).subs(dict(zip(c, w0c))) for ai in c]
print("grad J at w0 (d/da0..d/da4):", grad)
print("=> T_{w0} sigma2 = {a4 = 0} = span{x^4, x^3y, x^2y^2, x y^3}; w0 is a SMOOTH point")

# tangent to the boundary (tangent-developable cone): d/dparams of l^3 l'
al, be, ga, de_ = sp.symbols('alpha beta gamma delta_')
l1 = x + al*y  # vary around l = x, l' = y
bnd = (x + al*y)**3 * (be*x + (1+ga)*y)
Tbnd = set()
for par in (al, be, ga):
    v = sp.expand(sp.diff(bnd, par).subs({al: 0, be: 0, ga: 0}))
    Tbnd.add(sp.simplify(v))
print("boundary tangent directions at w0:", Tbnd, " => T bd = span{x^4, x^3y, x^2y^2}")
print("=> normal line N = x y^3 - direction")

# torus weights: t . m_j means f(t x, t^-3 y)
for j, mon in enumerate([x**4, x**3*y, x**2*y**2, x*y**3, y**4]):
    w = sp.simplify(mon.subs({x: t*x, y: t**-3*y})/mon)
    print(f"  weight of m{j} = {sp.expand(w)}")
print("=> N has T1-weight t^-8 in this convention (|weight| = 8); conormal weight opposite")

# ---------- 3. exact Waring pair of f_s and pole calculus ----------
# claim: f_s = c1 (x + sqrt(s) y)^4 + c2 (x - sqrt(s) y)^4, c1 = -c2 = 1/(8 sqrt(s))
S = sig  # sigma = sqrt(s)
l1e, l2e = x + S*y, x - S*y
c1, c2 = 1/(8*S), -1/(8*S)
chk = sp.expand(c1*l1e**4 + c2*l2e**4 - (x**3*y + S**2*x*y**3))
print("Waring pair exact:", chk == 0)

wedge = -2*S  # l1 /\ l2

def hat_class(p, q, b):
    """symmetrized class  Sym[ lhat1^p lhat2^q ] (l1/\l2)^b, lhat_i = c_i^{1/4} l_i.
    Returns its exact expansion along f_s in sigma = sqrt(s)."""
    A = c1**sp.Rational(p, 4) * c2**sp.Rational(q, 4) * l1e**p * l2e**q
    B = c1**sp.Rational(q, 4) * c2**sp.Rational(p, 4) * l1e**q * l2e**p
    e = sp.expand(sp.powsimp((A + (-1)**b * B) * wedge**b, force=True))
    return sp.simplify(e)

def sigma_order(expr):
    """min exponent of sigma across coefficients in x,y (negative = pole)."""
    P = sp.Poly(sp.expand(expr), x, y)
    orders = []
    for coef in P.coeffs():
        cs_ = sp.simplify(coef)
        if cs_ == 0:
            continue
        orders.append(sp.degree(sp.together(cs_), sig) - sp.degree(sp.denom(sp.together(cs_)), sig)
                      if False else None)
    # robust: use series valuation via as_leading_term
    orders = []
    for coef in P.coeffs():
        cs_ = sp.simplify(coef)
        if cs_ == 0:
            continue
        lt = sp.together(cs_)
        num, den = sp.fraction(lt)
        onum = sp.Poly(sp.expand(num), sig).monoms()
        vnum = min(m[0] for m in onum) if onum else 0
        oden = sp.Poly(sp.expand(den), sig).monoms()
        vden = min(m[0] for m in oden) if oden else 0
        orders.append(vnum - vden)
    return min(orders) if orders else None

# I-units: I(f_s) = -s/4 = -sigma^2/4, so pole in I-units = -(sigma-order)/2
tests = [
    ("(8,0)  delta=2, class l1^4 l2^4 (b=0)",             (4, 4, 0)),
    ("(12,0) delta=3, class l1^12+l2^12 (b=0)",           (12, 0, 0)),
    ("(12,0) delta=3, class l1^8 l2^4 + sym (b=0)",       (8, 4, 0)),
    ("(11,1) delta=3, class l1^7 l2^3 (b=1)",             (7, 3, 1)),
    ("(16,0) delta=4, class l1^12 l2^4 + sym (b=0)",      (12, 4, 0)),
    ("(16,0) delta=4, class l1^8 l2^8 (b=0)",             (8, 8, 0)),
    ("(4,0)  delta=1, f itself: l1^4 + l2^4 (b=0)",       (4, 0, 0)),
]
print("\npole calculus along the transversal family (I-units = -ord_sigma / 2):")
for name, (p, q, b) in tests:
    e = hat_class(p, q, b)
    o = sigma_order(e)
    if o is None:
        print(f"  {name}: class vanishes identically")
    else:
        print(f"  {name}: ord_sigma = {o}, pole in I-units = {sp.Rational(-o, 2)}")
