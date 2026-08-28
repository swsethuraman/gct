"""Session 15 (math): the Psi-locus over the feasible {0,1} balanced cone.

Enumerates ALL pencils (A, B) with A, B in {0,1}^{3x3} (A = row-1 receiving
matrix, B = row-2; direction N = e1⊗A + e2⊗B), computes the monomial
expansion of det3∘(I+N) combinatorially (no sympy), tests weight-support
feasibility for demand (8,8,8,6^6), and evaluates Psi = 2u1 − 4u2 − D on
the feasible ones.

Output: the Psi value distribution over the feasible {0,1} cone, exemplars
per value, and the exotic points (Psi ∉ {0,1}) if any.
"""
import sys
from itertools import product

DET = [(1,(0,4,8)), (-1,(0,5,7)), (-1,(1,3,8)), (1,(1,5,6)), (1,(2,3,7)), (-1,(2,4,6))]
DEMAND = (8,8,8,6,6,6,6,6,6)

def mons_of_pencil(A, B):
    """A, B: 3x3 tuples (row-1 / row-2 receiving matrices, [target col][source col]).
    Returns dict sorted-var-tuple -> integer coefficient (zeros removed)."""
    md = {}
    for sgn, (v0, v1, v2) in DET:
        # v0 = 3*0+c0 row-0 var; v1 = 3+j1; v2 = 6+j2
        c0 = v0; j1 = v1 - 3; j2 = v2 - 6
        opts1 = [(1, v1)] + [(A[j1][a], a) for a in range(3) if A[j1][a]]
        opts2 = [(1, v2)] + [(B[j2][a], a) for a in range(3) if B[j2][a]]
        for c1, w1 in opts1:
            for c2, w2 in opts2:
                key = tuple(sorted((v0, w1, w2)))
                md[key] = md.get(key, 0) + sgn * c1 * c2
    return {k: c for k, c in md.items() if c}

def feasible(mons, ncopies=20):
    vecs = []
    for vs in mons:
        v = [0]*9
        for x in vs: v[x] += 1
        vecs.append(tuple(v))
    n = len(vecs)
    # cheap prescreens
    for k in range(9):
        if DEMAND[k] > 0 and not any(v[k] for v in vecs): return False
    if sum(1 for v in vecs if v[0]+v[1]+v[2] >= 2) == 0: return False
    # order types rich-first (more row-0 content first)
    vecs.sort(key=lambda v: -(v[0]+v[1]+v[2]))
    # suffix per-variable max supply
    maxs = [[0]*9 for _ in range(n+1)]
    for i in range(n-1, -1, -1):
        for k in range(9):
            maxs[i][k] = max(maxs[i+1][k], vecs[i][k])
    best = [False]
    def dfs(i, left, dem):
        if best[0]: return
        if left == 0:
            if all(d == 0 for d in dem): best[0] = True
            return
        if i == n: return
        M = maxs[i]
        for k in range(9):
            if dem[k] > left * M[k]: return
        v = vecs[i]; mx = left
        for k in range(9):
            if v[k]: mx = min(mx, dem[k]//v[k])
        for c in range(mx, -1, -1):
            dfs(i+1, left-c, tuple(dem[k]-c*v[k] for k in range(9)))
            if best[0]: return
    dfs(0, ncopies, DEMAND)
    return best[0]

def mm(X, Y):
    return tuple(tuple(sum(X[i][k]*Y[k][j] for k in range(3)) for j in range(3)) for i in range(3))
def tr(X): return X[0][0]+X[1][1]+X[2][2]

def psi(A, B):
    AA, BB, AB = mm(A,A), mm(B,B), mm(A,B)
    u1 = tr(AA)*tr(BB) - tr(AB)**2
    u2 = tr(mm(AA,BB)) - tr(mm(AB,AB))
    Dv = (tr(A)*tr(B) - tr(AB))**2 - (tr(A)**2 - tr(AA))*(tr(B)**2 - tr(BB))
    return 2*u1 - 4*u2 - Dv

def mat_of(bits):
    return tuple(tuple((bits >> (3*i+j)) & 1 for j in range(3)) for i in range(3))

if __name__ == '__main__':
    import time
    t0 = time.time()
    dist = {}          # psi value -> count
    exemplars = {}     # psi value -> first (A,B)
    exotic = []
    nfeas = 0
    for abits in range(512):
        A = mat_of(abits)
        for bbits in range(512):
            B = mat_of(bbits)
            mons = mons_of_pencil(A, B)
            if not feasible(list(mons)): continue
            nfeas += 1
            p = psi(A, B)
            dist[p] = dist.get(p, 0) + 1
            if p not in exemplars: exemplars[p] = (abits, bbits)
            if p not in (0, 1) and len(exotic) < 40:
                exotic.append((p, abits, bbits))
        if abits % 64 == 0:
            print(f"  ... A-block {abits}/512, feasible so far {nfeas} [{time.time()-t0:.0f}s]", flush=True)
    print(f"\nfeasible {{0,1}} pencils: {nfeas} / 262144   [{time.time()-t0:.0f}s]")
    print("Psi distribution:", dict(sorted(dist.items())))
    for p, (ab, bb) in sorted(exemplars.items()):
        print(f"  exemplar Psi={p}: A={mat_of(ab)} B={mat_of(bb)}")
