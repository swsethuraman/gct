#!/usr/bin/env python3
"""Session 61, M3 (continued): transversal type of per_3 along its singular locus.

Exact rational Hessian ranks (python-flint fmpq_mat) of per_3 at random points of
each of the 15 components of Sing(per_3) (as found by analysis/wk9_s61_sing.sing:
six coordinate planes {two rows = 0} / {two columns = 0} and nine quadric surfaces
{row i = 0, column j = 0, complementary 2x2 permanent = 0}), and at random points of
the 18 lines along which three components meet.  Expected: rank 6 on every component
(transversal A_1 in the six normal directions), rank 4 on the lines.

Also the check behind the M5 Teissier prediction: at every singular point the
Hessian of per_3 restricted to a generic P^6 through the point has rank 6, i.e. the
point is an ordinary node of the section.
"""
import itertools, random, sys
from flint import fmpq_mat, fmpq

PERMS3 = list(itertools.permutations(range(3)))

def per3(X):
    return sum(X[0][p[0]] * X[1][p[1]] * X[2][p[2]] for p in PERMS3)

def hessian_per3(X):
    """9x9 Hessian at the 3x3 matrix X (entries fmpq).  d^2 per / dx_ij dx_kl =
    sum over permutations with p(i)=j, p(k)=l of the product of the remaining entry."""
    H = fmpq_mat(9, 9)
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    if i == k or j == l:
                        continue
                    m = 3 - i - k
                    n = 3 - j - l
                    H[3*i+j, 3*k+l] = X[m][n]
    return H

def rank(H):
    return H.rank()

def rnd(rng):
    while True:
        v = rng.randint(-40, 40)
        if v != 0:
            return fmpq(v)

def zero_matrix():
    return [[fmpq(0)] * 3 for _ in range(3)]

def main():
    rng = random.Random(61)
    ok = True
    print("component                                      point-type   Hessian ranks (5 random points)")
    # planes: two rows zero
    for (r1, r2) in itertools.combinations(range(3), 2):
        r3 = 3 - r1 - r2
        ranks = []
        for _ in range(5):
            X = zero_matrix()
            for j in range(3):
                X[r3][j] = rnd(rng)
            ranks.append(rank(hessian_per3(X)))
        print(f"rows {r1},{r2} = 0 (plane)                      generic      {ranks}")
        ok &= all(r == 6 for r in ranks)
    for (c1, c2) in itertools.combinations(range(3), 2):
        c3 = 3 - c1 - c2
        ranks = []
        for _ in range(5):
            X = zero_matrix()
            for i in range(3):
                X[i][c3] = rnd(rng)
            ranks.append(rank(hessian_per3(X)))
        print(f"cols {c1},{c2} = 0 (plane)                      generic      {ranks}")
        ok &= all(r == 6 for r in ranks)
    # quadrics: row i = 0, col j = 0, complementary permanent = 0
    for i in range(3):
        for j in range(3):
            rows = [r for r in range(3) if r != i]
            cols = [c for c in range(3) if c != j]
            ranks = []
            for _ in range(5):
                X = zero_matrix()
                a, b, c = rnd(rng), rnd(rng), rnd(rng)
                # X[r0][c0]*X[r1][c1] + X[r0][c1]*X[r1][c0] = 0 -> X[r1][c1] = -X[r0][c1]*X[r1][c0]/X[r0][c0]
                X[rows[0]][cols[0]] = a
                X[rows[0]][cols[1]] = b
                X[rows[1]][cols[0]] = c
                X[rows[1]][cols[1]] = -b * c / a
                assert per3(X) == 0
                ranks.append(rank(hessian_per3(X)))
            print(f"row {i} = 0, col {j} = 0, 2x2 permanent = 0 (quadric)   generic      {ranks}")
            ok &= all(r == 6 for r in ranks)
    # the 18 lines: two rows zero and one column zero (and transposes)
    for (r1, r2) in itertools.combinations(range(3), 2):
        r3 = 3 - r1 - r2
        for j in range(3):
            ranks = []
            for _ in range(5):
                X = zero_matrix()
                for c in range(3):
                    if c != j:
                        X[r3][c] = rnd(rng)
                ranks.append(rank(hessian_per3(X)))
            print(f"rows {r1},{r2} = 0, col {j} = 0 (line)             special      {ranks}")
            ok &= all(r == 4 for r in ranks)
    for (c1, c2) in itertools.combinations(range(3), 2):
        c3 = 3 - c1 - c2
        for i in range(3):
            ranks = []
            for _ in range(5):
                X = zero_matrix()
                for r in range(3):
                    if r != i:
                        X[r][c3] = rnd(rng)
                ranks.append(rank(hessian_per3(X)))
            print(f"cols {c1},{c2} = 0, row {i} = 0 (line)             special      {ranks}")
            ok &= all(r == 4 for r in ranks)
    # coordinate points e_ij (where six components meet)
    ranks = []
    for i in range(3):
        for j in range(3):
            X = zero_matrix(); X[i][j] = fmpq(1)
            ranks.append(rank(hessian_per3(X)))
    print(f"the nine coordinate points e_ij                 special      {ranks}")
    print()
    print("M3 transversal check (rank 6 on all 15 components, rank 4 on the 18 lines):", "PASS" if ok else "FAIL")
    # restriction to a random 7-dimensional linear subspace through the point (a P^6):
    # the Hessian of the restricted cubic at the point is B^T H B for a 9x7 basis B whose
    # first column is the point itself; the node condition is rank 6 (the point direction
    # is in the kernel of the restricted Hessian since the point is singular).
    print()
    print("Node check for the P^6-section (M5): rank of B^T H B, B = [point | 6 random directions]")
    node_ok = True
    def section_rank(X):
        H = hessian_per3(X)
        B = fmpq_mat(9, 7)
        flat = [X[i][j] for i in range(3) for j in range(3)]
        for a in range(9):
            B[a, 0] = flat[a]
            for b in range(1, 7):
                B[a, b] = fmpq(rng.randint(-40, 40))
        return (B.transpose() * H * B).rank()
    for (r1, r2) in itertools.combinations(range(3), 2):
        r3 = 3 - r1 - r2
        X = zero_matrix()
        for j in range(3):
            X[r3][j] = rnd(rng)
        r = section_rank(X); node_ok &= (r == 6)
        print(f"  rows {r1},{r2} = 0 plane: restricted Hessian rank {r}")
    for i in range(3):
        for j in range(3):
            rows = [r for r in range(3) if r != i]; cols = [c for c in range(3) if c != j]
            X = zero_matrix()
            a, b, c = rnd(rng), rnd(rng), rnd(rng)
            X[rows[0]][cols[0]] = a; X[rows[0]][cols[1]] = b; X[rows[1]][cols[0]] = c; X[rows[1]][cols[1]] = -b*c/a
            r = section_rank(X); node_ok &= (r == 6)
            print(f"  row {i}, col {j} quadric: restricted Hessian rank {r}")
    print("Node check:", "PASS (every generic-section singular point is an A_1 node of the 5-fold)" if node_ok else "FAIL")
    return 0 if (ok and node_ok) else 1

if __name__ == "__main__":
    sys.exit(main())
