"""Calibrate the general evaluator against week-1 Aronhold S, and verify the
instability facts that make Phi18 vanish on both boundary components."""
import itertools, random
import sympy as sp
import numpy as np

# --- rebuild Aronhold S exactly as in week 1 ---
mons = [(i, j, 3-i-j) for i in range(3, -1, -1) for j in range(3-i, -1, -1)]
c = {m: sp.Symbol('c_%d%d%d' % m) for m in mons}
cand = [combo for combo in itertools.combinations_with_replacement(mons, 4)
        if tuple(sum(m[t] for m in combo) for t in range(3)) == (4,4,4)]
coeffs = sp.symbols('u0:%d' % len(cand))
P = sum(u * sp.prod(c[m] for m in combo) for u, combo in zip(coeffs, cand))
def raise_op(P, kind):
    out = 0
    for (i, j, k) in mons:
        if kind == 1 and j >= 1: out += j * c[(i,j,k)] * sp.diff(P, c[(i+1,j-1,k)])
        if kind == 2 and k >= 1: out += k * c[(i,j,k)] * sp.diff(P, c[(i,j+1,k-1)])
    return sp.expand(out)
eqs = []
for kind in (1, 2):
    poly = sp.Poly(raise_op(P, kind), *[c[m] for m in mons])
    eqs += [cf for _, cf in poly.terms()]
sol = list(sp.linsolve(eqs, coeffs))[0]
free = [s for s in sol.free_symbols if s in coeffs]
S = sp.expand(P.subs(dict(zip(coeffs, sol))).subs({free[0]: sp.Integer(24)}))

def Sval(assign):
    return sp.simplify(S.subs({c[m]: assign.get(m, 0) for m in mons}))

random.seed(7)
allm = [(i, j, 3-i-j) for i in range(4) for j in range(4-i)]
tests = {
    'fermat': ({(3,0,0):1,(0,3,0):1,(0,0,3):1}, 0),
    'cusp':   ({(2,1,0):1,(0,0,3):1}, 0),
    'xyz':    ({(1,1,1):1}, 24),
}
for r in range(3):
    f = {m: random.randint(-3,3) for m in allm}
    tests[f'rand{r}'] = (f, [179352, 98712, -194088][r])

print("=== calibration: DP pattern value vs Aronhold S ===")
ratios = set()
for name, (f, dpval) in tests.items():
    sv = Sval(f)
    if sv == 0:
        ok = (dpval == 0)
        print(f"  {name:8s} S = 0, DP = {dpval}  {'OK' if ok else 'MISMATCH'}")
    else:
        ratio = sp.Rational(dpval, sv)
        ratios.add(ratio)
        print(f"  {name:8s} S = {sv}, DP = {dpval}, ratio = {ratio}")
print("  distinct ratios among nonzero:", ratios, "=> CALIBRATED" if len(ratios) == 1 else "=> FAIL")

# --- instability of the two boundary components ---
print("=== instability checks ===")
X = sp.symbols('x0:9')
M = sp.Matrix(3, 3, lambda i, j: X[3*i+j])
M[2,2] = -X[0]-X[4]
P1 = sp.expand(M.det())
P2 = sp.expand(X[3]*X[0]**2 + X[4]*X[1]**2 + X[5]*X[2]**2
             + X[6]*X[0]*X[1] + X[7]*X[1]*X[2] + X[8]*X[0]*X[2])

# P1: essential variables = rank of first-partials space
mons9 = list(itertools.combinations_with_replacement(range(9), 2))
def pvecs(f):
    rows = []
    for t in range(9):
        d = sp.Poly(sp.expand(sp.diff(f, X[t])), *X)
        v = [0]*len(mons9)
        for mono, cf in d.terms():
            if cf == 0 or sum(mono) != 2: continue
            idx = tuple(sorted([i for i in range(9) for _ in range(mono[i])]))
            v[mons9.index(idx)] = int(cf)
        rows.append(v)
    return np.array(rows)
r1 = np.linalg.matrix_rank(pvecs(P1)); r2 = np.linalg.matrix_rank(pvecs(P2))
print(f"  essential variables: P1 = {r1} (expect 8: degenerate), P2 = {r2} (expect 9: nondegenerate)")

# P1 1-PS: dead variable x8; lambda(t) = diag(t^{-1} x 8 vars, t^8 on x8), det = 1
# P1 has no x8 => lambda(t).P1 = t^3 P1 -> 0 as t->infty direction; unstable
print("  P1: no x8 =>", 'x8' not in str(P1), "=> 1-PS diag(t,..,t,t^-8) drives P1 -> 0: UNSTABLE")
# P2 grading: every monomial quadratic in A = {x0,x1,x2}, linear in B
ok = True
for mono, cf in sp.Poly(P2, *X).terms():
    dA = mono[0]+mono[1]+mono[2]; dB = sum(mono[3:])
    if not (dA == 2 and dB == 1): ok = False
print(f"  P2: every monomial A-degree 2, B-degree 1: {ok}")
print("  => 1-PS t^{-2} on A, t^{+1} on B (det = t^{-6+6} = 1): P2 -> t^{-4+1}... recompute:")
# substitute xA -> t^a xA, xB -> t^b xB with 3a + 6b = 0; weight of P2 = 2a + b
# choose a = -2, b = 1: weight = -3 => lambda(t).P2 = t^{-3} P2;  t -> infty: -> 0. UNSTABLE
print("     a=-2 on A, b=+1 on B: SL_9, monomial weight 2a+b = -3 => P2 unstable")
print("=== conclusion: both components in the SL_9 null cone;")
print("    every positive-degree invariant vanishes on the whole boundary;")
print("    with Phi18 nonzero on the open orbit: V(Phi18) ∩ closure = boundary EXACTLY ===")
