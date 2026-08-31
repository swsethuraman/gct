"""Session 23(a), step 4: what the m = 3 generator does on the banked points and
on the {0,1} balanced cone, with weight-feasibility at lambda' = (9,9,9,6^6).

Compression is characterised correctly here: the net has a common left kernel
iff u_0 I + u_1 A + u_2 B = 0 for some u != 0, i.e. iff {I, A, B} is linearly
DEPENDENT.  (Setting a row of A and B to zero is not compression.)
"""
import random, sys
from itertools import product
from wk4_s23_words import mm, mtr
from wk4_s23_gens import extract, fval, Psi

DET = [(1,(0,4,8)), (-1,(0,5,7)), (-1,(1,3,8)), (1,(1,5,6)), (1,(2,3,7)), (-1,(2,4,6))]

def mons_of_pencil(A, B):
    md = {}
    for sgn, (v0, v1, v2) in DET:
        j1 = v1 - 3; j2 = v2 - 6
        opts1 = [(1, v1)] + [(A[j1][a], a) for a in range(3) if A[j1][a]]
        opts2 = [(1, v2)] + [(B[j2][a], a) for a in range(3) if B[j2][a]]
        for c1, w1 in opts1:
            for c2, w2 in opts2:
                key = tuple(sorted((v0, w1, w2)))
                md[key] = md.get(key, 0) + sgn*c1*c2
    return {k: c for k, c in md.items() if c}

def feasible(mons, demand, ncopies):
    vecs = []
    for vs in mons:
        v = [0]*9
        for xx in vs: v[xx] += 1
        vecs.append(tuple(v))
    n = len(vecs)
    for k in range(9):
        if demand[k] > 0 and not any(v[k] for v in vecs): return False
    vecs.sort(key=lambda v: -(v[0]+v[1]+v[2]))
    maxs = [[0]*9 for _ in range(n+1)]
    for i in range(n-1, -1, -1):
        for k in range(9): maxs[i][k] = max(maxs[i+1][k], vecs[i][k])
    best = [False]
    def dfs(i, left, dem):
        if best[0]: return
        if left == 0:
            if all(d == 0 for d in dem): best[0] = True
            return
        if i == n: return
        M = maxs[i]
        for k in range(9):
            if dem[k] > left*M[k]: return
        v = vecs[i]; mx = left
        for k in range(9):
            if v[k]: mx = min(mx, dem[k]//v[k])
        for c in range(mx, -1, -1):
            dfs(i+1, left-c, tuple(dem[k]-c*v[k] for k in range(9)))
            if best[0]: return
    dfs(0, ncopies, demand)
    return best[0]

def mat_of(bits):
    return tuple(tuple((bits >> (3*i+j)) & 1 for j in range(3)) for i in range(3))

if __name__ == '__main__':
    r3, gens3, mons3 = extract(3)
    g3v = gens3[0]
    g3 = lambda A, B: fval(g3v, mons3, A, B)
    rng = random.Random(99)
    def rmat(k=4): return tuple(tuple(rng.randint(-k,k) for _ in range(3)) for _ in range(3))

    print("=== compression, correctly characterised: {I, A, B} linearly dependent ===")
    out = []
    for _ in range(6):
        A = rmat(); a, b = rng.randint(-3,3), rng.randint(-3,3)
        B = tuple(tuple(a*(1 if i==j else 0) + b*A[i][j] for j in range(3)) for i in range(3))
        out.append((Psi(A,B), g3(A,B)))
    print(f"  (Psi, g3) at six compression nets: {out}")

    print()
    print("=== the {0,1} balanced cone at lambda' = (9,9,9,6^6), delta = 21, t = (3,3) ===")
    DEMAND = (9,9,9,6,6,6,6,6,6); NC = 21
    nfeas = 0; nz = []; dist = {}
    for ab in range(512):
        A = mat_of(ab)
        for bb in range(512):
            B = mat_of(bb)
            mons = mons_of_pencil(A, B)
            if not feasible(list(mons), DEMAND, NC): continue
            nfeas += 1
            g = g3(A, B)
            dist[g] = dist.get(g, 0) + 1
            if g and len(nz) < 12: nz.append((g, Psi(A,B), ab, bb))
        if ab % 128 == 0: print(f"   ... A-block {ab}/512, feasible {nfeas}", flush=True)
    print(f"  feasible {{0,1}} pencils at delta = 21: {nfeas}")
    print(f"  g3 distribution: {dict(sorted(dist.items()))}")
    print("  first pencils with g3 != 0:")
    for g, p, ab, bb in nz:
        print(f"    g3 = {g:>4}  Psi = {p:>4}   A = {mat_of(ab)}  B = {mat_of(bb)}")
