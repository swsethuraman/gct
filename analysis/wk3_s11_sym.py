"""Sigma-symmetry harvest: find signed-permutation symmetries of point C that
preserve {x0,x1,x2} setwise, then compute their induced action on the 36
subproblems (sigma6, sigma7) of scheme 1 -> orbit/sign structure of subvalues.

A symmetry: pi in S9 (with sign eps_pi possible via C o pi = s * C, s = +-1),
plus an induced permutation of the eps9 labels {0..5} and possibly swapping
the two short columns, such that the scheme triple-set maps to itself.

If pi preserves the scheme's triples (as a labeled structure), then
V(sigma6', sigma7') = +- V(sigma6, sigma7) with computable sign
(from C-sign^20, per-eps variable-permutation parities, label reshuffles)."""
import itertools
import sympy as sp

X = sp.symbols('x0:9')
det3 = sp.expand(sp.Matrix(3, 3, lambda i, j: X[3*i+j]).det())
C = sp.expand(det3.subs({X[5]: X[5]+X[1], X[7]: X[7]+X[2]}, simultaneous=True))

def mons_of(f):
    out = {}
    for mono, cf in sp.Poly(f, *X).terms():
        vs = tuple(sorted(i for i in range(9) for _ in range(mono[i])))
        out[vs] = int(cf)
    return out

MC = mons_of(C)
support = set(MC)
print("point C:", len(MC), "monomials")

# search permutations pi of 0..8 with pi({0,1,2}) = {0,1,2} and C o pi = s*C
# backtracking on images constrained by monomial-support compatibility
syms = []
for pr in itertools.permutations((0,1,2)):          # image of row-0 vars
    for pw in itertools.permutations(range(3,9)):    # image of the rest
        pi = list(pr) + list(pw)
        newm = {}
        ok = True
        for vs, cf in MC.items():
            nvs = tuple(sorted(pi[v] for v in vs))
            if nvs not in support: ok = False; break
            newm[nvs] = cf
        if not ok: continue
        # C o pi^{-1} has coefficient at pi(m) equal cf(m): compare to s*MC
        ratios = set(sp.Rational(newm[m], MC[m]) for m in newm)
        if len(ratios) == 1 and abs(list(ratios)[0]) == 1:
            syms.append((tuple(pi), int(list(ratios)[0])))
print("signed symmetries preserving {x0,x1,x2}:", len(syms))
for pi, s in syms:
    print("  pi:", pi, " sign:", s, " rho on {0,1,2}:", pi[:3])
