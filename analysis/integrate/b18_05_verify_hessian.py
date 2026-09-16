"""Integrator check of B18-05's structure lemma, derived here from scratch.

F = z * C(y),  z one variable, C a cubic on the complementary 9-space y.
In block form (1 + 9), Hess F = [[0, grad C^T], [grad C, z * Hess C]].

Claimed: rank 2 at the root of the linear factor; corank 1 at the roots of the cubic,
with kernel vector 3z*zeta - x.
"""
import random
from fractions import Fraction
from itertools import combinations_with_replacement as cwr

random.seed(1805)
NY = 9

def rand_cubic():
    return {m: random.randint(-9, 9) for m in cwr(range(NY), 3)}

def C_val(Cc, y):
    t = 0
    for m, c in Cc.items():
        p = c
        for i in m: p *= y[i]
        t += p
    return t

def grad_C(Cc, y):
    g = [0]*NY
    for m, c in Cc.items():
        for pos in range(3):
            i = m[pos]; p = c
            for q in range(3):
                if q != pos: p *= y[m[q]]
            g[i] += p
    return g

def hess_C(Cc, y):
    H = [[0]*NY for _ in range(NY)]
    for m, c in Cc.items():
        for a in range(3):
            for b in range(3):
                if a == b: continue
                i, j = m[a], m[b]
                k = [q for q in range(3) if q not in (a, b)][0]
                H[i][j] += c * y[m[k]]
    return H

def hess_F(Cc, z, y):
    g = grad_C(Cc, y); H = hess_C(Cc, y)
    M = [[0]*(NY+1) for _ in range(NY+1)]
    for i in range(NY): M[0][i+1] = g[i]; M[i+1][0] = g[i]
    for i in range(NY):
        for j in range(NY): M[i+1][j+1] = z * H[i][j]
    return M

def rank(M):
    A = [[Fraction(v) for v in row] for row in M]
    R, Cn = len(A), len(A[0]); r = 0
    for c in range(Cn):
        piv = next((i for i in range(r, R) if A[i][c] != 0), None)
        if piv is None: continue
        A[r], A[piv] = A[piv], A[r]
        for i in range(r+1, R):
            if A[i][c] != 0:
                f = A[i][c]/A[r][c]
                for j in range(c, Cn): A[i][j] -= f*A[r][j]
        r += 1
    return r

def matvec(M, v): return [sum(M[i][j]*v[j] for j in range(len(v))) for i in range(len(M))]

print("case 1: z = 0 (root of the linear factor)  -- claim rank 2")
for trial in range(6):
    Cc = rand_cubic(); y = [random.randint(-50, 50) for _ in range(NY)]
    print(f"   trial {trial}: rank Hess F = {rank(hess_F(Cc, 0, y))}")

print("\ncase 2: C(y) = 0, z != 0 (root of the cubic)  -- claim corank 1, kernel 3z*zeta - x")
found = 0; trial = 0
while found < 6 and trial < 4000:
    trial += 1
    Cc = rand_cubic(); y = [random.randint(-30, 30) for _ in range(NY)]
    # force C(y) = 0 by solving for the coefficient of one pure monomial
    key = (0,0,0)
    if y[0] == 0: continue
    rest = C_val({k:v for k,v in Cc.items() if k != key}, y)
    if rest % (y[0]**3) != 0: continue
    Cc[key] = -rest // (y[0]**3)
    if C_val(Cc, y) != 0: continue
    z = random.choice([i for i in range(-9,10) if i != 0])
    M = hess_F(Cc, z, y)
    r = rank(M)
    ker = [3*z - z] + [-yy for yy in y]          # 3z*zeta - x, with x = (z, y)
    img = matvec(M, ker)
    print(f"   trial {found}: rank = {r}  corank = {10-r}   Hess*(3z*zeta - x) = "
          f"{'ZERO' if all(v == 0 for v in img) else 'NONZERO ' + str(img[:3])}")
    found += 1
