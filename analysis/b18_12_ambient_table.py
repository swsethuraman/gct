"""Ambient multiplicities a(d,lambda) = mult of S_lambda(C^5) in Sym^d(Sym^4 C^5)
for all lambda |- 4d with exactly five rows, d = 5, 6.  Pure-integer character
arithmetic (cycle index of S_d + Weyl/Klimyk inversion).  Control: the sum over all
lambda of a * dim S_lambda must equal binom(69+d, d)."""
import itertools, math, sys, time
from collections import defaultdict
t0 = time.time()
NV = 5

def monomials(deg):
    out = []
    def rec(prefix, left, k):
        if k == NV - 1:
            out.append(tuple(prefix + [left])); return
        for i in range(left, -1, -1):
            rec(prefix + [i], left - i, k + 1)
    rec([], deg, 0); return out

chi = {m: 1 for m in monomials(4)}            # character of Sym^4 C^5

def padd(p, q, s=1):
    r = dict(p)
    for k, v in q.items():
        r[k] = r.get(k, 0) + s * v
        if r[k] == 0: del r[k]
    return r

def pmul(p, q):
    r = defaultdict(int)
    for k1, v1 in p.items():
        for k2, v2 in q.items():
            r[tuple(a + b for a, b in zip(k1, k2))] += v1 * v2
    return {k: v for k, v in r.items() if v}

def pk(p, k):                                  # p_k plethysm: x -> x^k
    return {tuple(k * e for e in m): v for m, v in p.items()}

def partitions(n, maxpart=None):
    if maxpart is None: maxpart = n
    if n == 0: yield (); return
    for p in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - p, p):
            yield (p,) + rest

def sym_power_char(chi, d):
    total = {}
    for mu in partitions(d):
        # number of permutations of cycle type mu
        cnt = defaultdict(int)
        for m in mu: cnt[m] += 1
        z = 1
        for m, c in cnt.items(): z *= (m ** c) * math.factorial(c)
        term = {tuple([0] * NV): 1}
        for m in mu: term = pmul(term, pk(chi, m))
        total = padd(total, {k: v * (math.factorial(d) // z) for k, v in term.items()})
    return {k: v // math.factorial(d) for k, v in total.items()}

def weyl_dim(lam):
    n = NV; num = 1; den = 1
    for i in range(n):
        for j in range(i + 1, n):
            num *= (lam[i] - lam[j] + j - i); den *= (j - i)
    return num // den

def multiplicities(char, size, rows_exact=None):
    rho = tuple(range(NV - 1, -1, -1))
    res = {}
    for lam in partitions(size):
        if len(lam) > NV: continue
        lam5 = tuple(list(lam) + [0] * (NV - len(lam)))
        if rows_exact is not None and len(lam) != rows_exact: continue
        m = 0
        for w in itertools.permutations(range(NV)):
            sgn = 1
            for i in range(NV):
                for j in range(i + 1, NV):
                    if w[i] > w[j]: sgn = -sgn
            wrho = tuple(rho[w[i]] for i in range(NV))
            wt = tuple(lam5[i] + rho[i] - wrho[i] for i in range(NV))
            m += sgn * char.get(wt, 0)
        if m: res[lam] = m
    return res

for d in (5, 6):
    ch = sym_power_char(chi, d)
    allm = multiplicities(ch, 4 * d)
    control = sum(m * weyl_dim(tuple(list(l) + [0] * (NV - len(l)))) for l, m in allm.items())
    print(f"d={d}: control sum a*dim = {control}, binom(69+d,d) = {math.comb(69 + d, d)}, "
          f"match={control == math.comb(69 + d, d)}")
    five = {l: m for l, m in allm.items() if len(l) == 5}
    print(f"d={d}: five-row cells with a>0: {len(five)}; total a over them = {sum(five.values())}")
    for l in sorted(five, key=lambda t: (-five[t], t)):
        print("   ", l, "a =", five[l])
print("elapsed s:", round(time.time() - t0, 2))
