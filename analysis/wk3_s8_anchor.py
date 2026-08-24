"""Small anchor for mixed-width columns: the S_(4,2,0) HWV of Sym^2(Sym^3 C^3).
Shape transpose (2,2,1,1): two eps_2 (top-2 vars) + two width-1 slots (x0 only).
Build the HWV classically (weight (4,2,0), killed by raising ops), compare with
the DP scheme at several cubics: ratio must be one constant.
Scheme: copy0 -> (e0,e1,e2), copy1 -> (e0,e1,e3): distinct triples, covers 2,2,1,1."""
import itertools, os, subprocess, random
import sympy as sp

mons = [(i, j, 3-i-j) for i in range(3, -1, -1) for j in range(3-i, -1, -1)]
c = {m: sp.Symbol('c_%d%d%d' % m) for m in mons}
cand = [combo for combo in itertools.combinations_with_replacement(mons, 2)
        if tuple(sum(m[t] for m in combo) for t in range(3)) == (4,2,0)]
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
assert len(free) == 1, len(free)
H = sp.expand(P.subs(dict(zip(coeffs, sol))).subs({free[0]: sp.Integer(12)}))
print("S_(4,2) HWV built:", len(sp.Poly(H, *[c[m] for m in mons]).terms()), "terms")

def Hval(assign):
    return sp.simplify(H.subs({c[m]: assign.get(m, 0) for m in mons}))

random.seed(23)
allm = [(i, j, 3-i-j) for i in range(4) for j in range(4-i)]
tests = {'fermat': {(3,0,0):1,(0,3,0):1,(0,0,3):1},
         'cusp':   {(2,1,0):1,(0,0,3):1},
         'xyz':    {(1,1,1):1}}
for r in range(3):
    tests[f'rand{r}'] = {m: random.randint(-3,3) for m in allm}

os.makedirs('evalin', exist_ok=True)
os.makedirs('anchor', exist_ok=True)
ratios = set()
for name, f in tests.items():
    ms = []
    for (i,j,k), cf in f.items():
        if cf == 0: continue
        vs = tuple([0]*i + [1]*j + [2]*k)
        ms.append((cf, vs))
    fn = f'evalin/a42_{name}.txt'
    with open(fn, 'w') as fo:
        fo.write("3 4 2 3\n2 2 1 1\n0 1 2\n0 1 3\n")
        fo.write(f"{len(ms)}\n")
        for cf, vs in ms:
            fo.write(f"{cf} " + " ".join(map(str, vs)) + "\n")
        fo.write("-1 1\n")
    out = subprocess.run(['../dp2', 'evalfile2', f'../{fn}'], cwd='anchor',
                         capture_output=True, text=True).stdout
    dpval = int(out.split("VALUE")[1].split("(")[0])
    hv = Hval(f)
    if hv == 0:
        print(f"  {name:8s} H = 0, DP = {dpval}", "OK" if dpval == 0 else "MISMATCH")
    else:
        ratios.add(sp.Rational(dpval, hv))
        print(f"  {name:8s} H = {hv}, DP = {dpval}, ratio {sp.Rational(dpval, hv)}")
print("distinct ratios:", ratios, "=> MIXED-WIDTH MACHINERY", "CALIBRATED" if len(ratios) == 1 else "FAIL")
