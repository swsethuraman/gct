"""Balanced two-transvection point toolkit (salvaged from stale branch f0c6ecd).

Three tools, point-agnostic:

1. sweep(): weight-support feasibility over all 81 balanced two-transvection
   points (x_{3+j} += x_a, x_{6+k} += x_b) for demand (8,8,8,6^6), via the
   content DFS with SUFFIX-SUPPLY PRUNING: a branch dies as soon as some
   variable's remaining demand exceeds what the remaining monomial types can
   still supply. (Necessary condition only — rank/cancellation zeros pass it.)
2. symmetries(mons): signed variable-permutation symmetries of a point's
   monomial list fixing {x0,x1,x2} setwise — the rho-pairing generators.
3. pairing(rho): orbit pairs of the 36 (sigma6, sigma7) subproblems under
   sigma -> rho.sigma composition, itertools ordering (n = 6*i6 + i7).

Run: python3 wk3_s12_sweep.py            (sweep + per-point symmetry counts)
"""
import itertools
import sympy as sp

X = sp.symbols('x0:9')
det3 = sp.expand(sp.Matrix(3, 3, lambda i, j: X[3*i+j]).det())
DEMAND = (8,8,8,6,6,6,6,6,6)

def mons_of(f):
    out = []
    for mono, cf in sp.Poly(sp.expand(f), *X).terms():
        vs = tuple(i for i in range(9) for _ in range(mono[i]))
        out.append((int(cf), vs))
    return out

def feasible(mons, ncopies=20, demand=DEMAND):
    """Content feasibility with suffix-supply pruning."""
    vecs = []
    for _, vs in mons:
        v = [0]*9
        for x in vs: v[x] += 1
        vecs.append(tuple(v))
    n = len(vecs); best = [False]
    def dfs(i, left, dem):
        if best[0]: return
        if i == n or left == 0:
            if left == 0 and all(d == 0 for d in dem): best[0] = True
            return
        v = vecs[i]; mx = left
        for k in range(9):
            if v[k]: mx = min(mx, dem[k]//v[k])
        for c in range(mx, -1, -1):
            nd = tuple(dem[k]-c*v[k] for k in range(9))
            ok = all(x >= 0 for x in nd)
            if ok:
                # suffix-supply cut: every still-demanded variable must have
                # a supplier among the remaining monomial types
                for k in range(9):
                    if nd[k] > 0 and not any(vecs[j][k] for j in range(i+1, n)):
                        ok = False; break
            if ok: dfs(i+1, left-c, nd)
            if best[0]: return
    dfs(0, ncopies, demand)
    return best[0]

def sweep():
    out = []
    for j in range(3):
        for a in range(3):
            for k in range(3):
                for b in range(3):
                    sub = {X[3+j]: X[3+j]+X[a], X[6+k]: X[6+k]+X[b]}
                    m = mons_of(det3.subs(sub, simultaneous=True))
                    if feasible(m):
                        out.append(((3+j, a), (6+k, b), len(m)))
    return out

def symmetries(mons):
    """Signed variable-permutation symmetries fixing {x0,x1,x2} setwise.
    Returns [(pi_one_line, sign)] with pi != id."""
    MC = {tuple(sorted(vs)): c for c, vs in mons}
    support = set(MC)
    syms = []
    for pr in itertools.permutations((0,1,2)):
        for pw in itertools.permutations(range(3,9)):
            pi = list(pr)+list(pw)
            newm = {}
            ok = True
            for vs, cf in MC.items():
                nvs = tuple(sorted(pi[v] for v in vs))
                if nvs not in support: ok = False; break
                newm[nvs] = cf
            if not ok: continue
            ratios = set(sp.Rational(newm[m], MC[m]) for m in newm)
            if len(ratios) == 1 and abs(list(ratios)[0]) == 1 and tuple(pi) != tuple(range(9)):
                syms.append((tuple(pi), int(list(ratios)[0])))
    return syms

def pairing(rho):
    """Orbit pairs of the 36 subproblems under composition by rho (a dict
    on {0,1,2}); returns (pairs, reps)."""
    perms = list(itertools.permutations((0,1,2)))
    ap = lambda p: tuple(rho[v] for v in p)
    pairs = []
    for i6, p6 in enumerate(perms):
        for i7, p7 in enumerate(perms):
            n1 = 6*i6+i7
            n2 = 6*perms.index(ap(p6)) + perms.index(ap(p7))
            if n1 < n2: pairs.append((n1, n2))
    return pairs, sorted(p[0] for p in pairs)

if __name__ == '__main__':
    fl = sweep()
    print(f"feasible balanced two-transvection points: {len(fl)}/81")
    for p in fl: print("  ", p)
    for (r, a), (s, b), nm in fl:
        m = mons_of(det3.subs({X[r]: X[r]+X[a], X[s]: X[s]+X[b]}, simultaneous=True))
        print(f"point (x{r}+=x{a}, x{s}+=x{b}): {nm} mons, "
              f"{len(symmetries(m))} nontrivial signed symmetries")
