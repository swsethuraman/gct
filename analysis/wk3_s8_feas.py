"""Weight-support feasibility: does f^{x20} have a nonzero (8,8,8,6^6)-weight component?
Necessary for any HWV value at f. DFS over monomial multiplicities."""
import itertools, sys
import sympy as sp

X = sp.symbols('x0:9')
det3 = sp.expand(sp.Matrix(3, 3, lambda i, j: X[3*i+j]).det())

SUBS = {
    'A': {X[5]: X[5] + X[1]},
    'C': {X[5]: X[5] + X[1], X[7]: X[7] + X[2]},
    'D': {X[3]: X[3] + X[0], X[8]: X[8] + X[1]},
    'E': {X[5]: X[5] + X[1], X[4]: X[4] + X[2]},
    'F': {X[7]: X[7] + X[2], X[3]: X[3] + X[1]},   # x3=(1,0)<-x1=(0,1): col0->col1; x7: col1->col2 ... unbalanced? test
    'G': {X[5]: X[5] + X[1], X[7]: X[7] + X[2], X[3]: X[3] + X[0]},
}
DEMAND = (8,8,8,6,6,6,6,6,6)

def cubic_mons(f):
    out = []
    for mono, cf in sp.Poly(sp.expand(f), *X).terms():
        if cf == 0: continue
        out.append((int(cf), tuple(mono)))
    return out

def feasible(mons, ncopies=20):
    vecs = [m for _, m in mons]
    n = len(vecs)
    best = [False]
    def dfs(i, left, dem):
        if best[0]: return
        if i == n:
            if left == 0 and all(d == 0 for d in dem): best[0] = True
            return
        # prune: remaining copies can't overshoot/undershoot
        if left == 0:
            if all(d == 0 for d in dem): best[0] = True
            return
        v = vecs[i]
        # max copies of this monomial limited by demand
        mx = left
        for k in range(9):
            if v[k]:
                mx = min(mx, dem[k]//v[k])
        for c in range(mx, -1, -1):
            nd = tuple(dem[k] - c*v[k] for k in range(9))
            if all(x >= 0 for x in nd):
                # quick check: rest of monomials can still supply each var
                ok = True
                for k in range(9):
                    if nd[k] > 0 and not any(vecs[j][k] for j in range(i+1, n)):
                        ok = False; break
                if ok: dfs(i+1, left-c, nd)
            if best[0]: return
    dfs(0, ncopies, DEMAND)
    return best[0]

for name, sub in SUBS.items():
    mons = cubic_mons(det3.subs(sub, simultaneous=True))
    f = feasible(mons)
    print(f"point {name}: {len(mons)} monomials, weight-(8,8,8,6^6) support: {'FEASIBLE' if f else 'INFEASIBLE'}")
