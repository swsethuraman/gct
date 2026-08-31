"""Session 22, F5: independently re-verify the uniqueness input.
(a) dim of bidegree-(2,2) simultaneous-conjugation invariants of a pencil = 9,
    by an SL_3 character computation (independent of the trace-word basis);
(b) inside that space, the two slab equivariances DERIVED IN THIS SESSION
    (delta A = -A^2, delta B = -BA, character 2 tr A;  and the B-mirror)
    cut out exactly one dimension, spanned by Psi.
"""
import sympy as sp, random
from itertools import product
from wk4_s22_dict import Psi

# ---------- (a) character computation --------------------------------------
def mul(p, q):
    r = {}
    for k1, v1 in p.items():
        for k2, v2 in q.items():
            k = (k1[0]+k2[0], k1[1]+k2[1]); r[k] = r.get(k, 0) + v1*v2
    return {k: v for k, v in r.items() if v}

def add(p, q):
    r = dict(p)
    for k, v in q.items():
        r[k] = r.get(k, 0) + v
    return {k: v for k, v in r.items() if v}

def scal(p, c): return {k: v*c for k, v in p.items() if v*c}

# torus of SL_3: weights of gl_3 = {e_i - e_j}; use coordinates (a,b) with
# t_1 = x, t_2 = y, t_3 = 1/(xy); exponent vector = power of (x,y).
W3 = [(1,0), (0,1), (-1,-1)]
def sub(u, v): return (u[0]-v[0], u[1]-v[1])
chi_gl3 = {}
for u in W3:
    for v in W3:
        k = sub(u, v); chi_gl3[k] = chi_gl3.get(k, 0) + 1

def frob(p, n):                      # chi(t^n)
    return {(k[0]*n, k[1]*n): v for k, v in p.items()}

chi_sym2 = scal(add(mul(chi_gl3, chi_gl3), frob(chi_gl3, 2)), sp.Rational(1,2))
chi_U = mul(chi_sym2, chi_sym2)                     # Sym^2(gl3) tensor Sym^2(gl3)
roots = [sub(u, v) for u in W3 for v in W3 if u != v]
weyl = {(0,0): 1}
for a in roots:
    weyl = add(weyl, {}) ; weyl = mul(weyl, {(0,0): 1, a: -1})
inv = mul(chi_U, weyl).get((0,0), 0) / 6
print(f"(a) dim (Sym^2 gl_3 (x) Sym^2 gl_3)^{{SL_3}} = {inv}   [expected 9]")
print(f"    sanity: dim Sym^2(gl_3) = {sum(chi_sym2.values())} (expect 45); "
      f"dim U = {sum(chi_U.values())} (expect 2025)")

# ---------- (b) the equivariant subspace ------------------------------------
a_ = sp.symbols('a0:9'); b_ = sp.symbols('b0:9')
A = sp.Matrix(3,3, lambda i,j: a_[3*i+j]); B = sp.Matrix(3,3, lambda i,j: b_[3*i+j])
tr = sp.trace

WORDS = [tr(A*A)*tr(B*B), tr(A*B)**2, tr(A*A*B*B), tr(A*B*A*B),
         tr(A)*tr(A*B*B), tr(B)*tr(B*A*A), tr(A)*tr(A)*tr(B*B),
         tr(B)*tr(B)*tr(A*A), tr(A)*tr(B)*tr(A*B), tr(A)**2*tr(B)**2]
WORDS = [sp.expand(w) for w in WORDS]

def deriv(f, dA, dB):
    out = 0
    for i in range(3):
        for j in range(3):
            out += sp.diff(f, a_[3*i+j])*dA[i,j] + sp.diff(f, b_[3*i+j])*dB[i,j]
    return sp.expand(out)

CondA = [sp.expand(deriv(w, -A*A, -B*A) + 2*tr(A)*w) for w in WORDS]   # slab_0 += t slab_1
CondB = [sp.expand(deriv(w, -A*B, -B*B) + 2*tr(B)*w) for w in WORDS]   # slab_0 += t slab_2

rng = random.Random(4242)
VARS = list(a_) + list(b_)
fW  = [sp.lambdify(VARS, w, modules='math') for w in WORDS]
fA  = [sp.lambdify(VARS, c, modules='math') for c in CondA]
fB  = [sp.lambdify(VARS, c, modules='math') for c in CondB]
fPsi = sp.lambdify(VARS, sp.expand(Psi(A, B)), modules='math')

PTS = [[rng.randint(-6, 6) for _ in range(18)] for _ in range(40)]
E  = sp.Matrix([[sp.Integer(f(*p)) for f in fW] for p in PTS])
MA = sp.Matrix([[sp.Integer(f(*p)) for f in fA] for p in PTS])
MB = sp.Matrix([[sp.Integer(f(*p)) for f in fB] for p in PTS])
M  = MA.col_join(MB)
rE, rM = E.rank(), M.rank()
ns = M.nullspace()
print(f"(b) rank of the 10 trace words as functions = {rE}  [expected 9: one relation]")
print(f"    rank of the stacked equivariance conditions = {rM}; coefficient nullspace dim = {len(ns)}")
print(f"    => dimension in FUNCTION space = {len(ns)} - (10 - {rE}) = {len(ns)-(10-rE)}  [expected 1]")
tgt = sp.Matrix([sp.Integer(fPsi(*p)) for p in PTS])
sol = sp.Matrix(list(sp.linsolve((E, tgt)))[0])
print(f"    Psi in the word basis (one solution): {list(sol)}")
for k, v in enumerate(ns):
    diff = sp.expand(sum(v[i]*WORDS[i] for i in range(10)))
    print(f"    nullspace vector {k}: {list(v)}")
    for c in (sp.Rational(1,1),):
        pass
    # test whether v is proportional to Psi AS A FUNCTION
    vals = [sp.Integer(0)]*0
    num = [sum(v[i]*fW[i](*p) for i in range(10)) for p in PTS]
    den = [fPsi(*p) for p in PTS]
    rats = set(sp.Rational(n, d) for n, d in zip(num, den) if d != 0)
    print(f"        value/Psi over the sample: {rats if len(rats)<4 else 'not constant'}")
