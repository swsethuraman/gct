"""Sanity: the b-polynomials in s78_reduced_polys.json reproduce
det(s5 I + sum s_k B_k) coefficient-by-coefficient at random integer B, both primes."""
import json, random
import sympy as sp

data = json.load(open('results/s78_reduced_polys.json'))
BN = data['bnames']
s1, s2, s3, s4, s5 = sp.symbols('s1 s2 s3 s4 s5')
S = [s1, s2, s3, s4, s5]
bsyms = {n: sp.Symbol(n) for n in BN}

rng = random.Random(11)
def bid(k, i, j): return k * 16 + i * 4 + j

ok = True
for trial in range(3):
    val = {n: rng.randint(-4, 4) for n in BN}
    # direct det
    M = s5 * sp.eye(4)
    for k in range(4):
        Bk = sp.Matrix(4, 4, lambda i, j: val[BN[bid(k, i, j)]])
        M += S[k] * Bk
    d = sp.Poly(sp.expand(M.det()), *S)
    direct = {m: c for m, c in zip(d.monoms(), d.coeffs())}
    # from json
    def evalpoly(expr):
        e = sp.sympify(expr, locals=bsyms)
        return int(e.subs(val))
    recon = {}
    for key, expr in list(data['good'].items()) + list(data['p4'].items()):
        sv = tuple(int(t) for t in key.split(','))
        recon[sv] = evalpoly(expr)
    recon[(0, 0, 0, 0, 4)] = 1
    # compare on all monomials
    allkeys = set(direct) | set(recon)
    for kk in allkeys:
        a = direct.get(kk, 0); b = recon.get(kk, 0)
        if a != b:
            ok = False; print("MISMATCH", kk, a, b)
print("reduced polynomials reproduce det(s5 I + sum s_k B_k):", ok)
assert ok
print("OK")
