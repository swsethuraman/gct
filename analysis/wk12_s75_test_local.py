#!/usr/bin/env python3
"""Unit test: the local block-swap recoupling S_{rho--,rho} must have
   +1 eigenspace of dim  sum_{j even} c^rho_{rho--,(8-j,j)}
   -1 eigenspace of dim  sum_{j odd}  c^rho_{rho--,(8-j,j)}
   and its matrix must be an involution (S^2 = I).  Checked over many
   (rho--, rho) pairs (rho/rho-- two horizontal 4-strips)."""
import sys, os, itertools
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from wk12_s75_recoup import (horiz_strips_below, cells_of_skew, build_local,
                             w0_matrix, is_h4_below)


def lr_two_row(rho, mu, a, b):
    """c^rho_{mu,(a,b)} : # LR tableaux of shape rho/mu, content (a,b), a>=b.
       Two-row content => count skew SSYT of shape rho/mu with a 1's and b 2's
       that are lattice (reading word: every prefix has #1 >= #2). For two rows
       the lattice/Yamanouchi condition on the reverse-reading word reduces to a
       simple check."""
    r = max(len(rho), len(mu))
    R = list(rho) + [0] * (r - len(rho))
    Mu = list(mu) + [0] * (r - len(mu))
    cells = []
    for i in range(r):
        for j in range(Mu[i], R[i]):
            cells.append((i, j))
    if len(cells) != a + b:
        return 0
    cellset = set(cells)
    cnt = 0
    # assign 1 or 2 to each cell: rows weakly increase (1's then 2's per row),
    # columns strictly increase (so a cell with a filled cell above must be >).
    # enumerate subsets choosing which cells are '2' (b of them)
    from itertools import combinations
    for twos in combinations(range(len(cells)), b):
        val = {}
        for idx, c in enumerate(cells):
            val[c] = 2 if idx in twos else 1
        ok = True
        # row weakly increasing
        for i in range(r):
            rowcells = sorted([c for c in cells if c[0] == i], key=lambda c: c[1])
            for k in range(len(rowcells) - 1):
                if val[rowcells[k]] > val[rowcells[k + 1]]:
                    ok = False; break
            if not ok:
                break
        if not ok:
            continue
        # column strictly increasing
        for c in cells:
            up = (c[0] - 1, c[1])
            if up in cellset and not (val[up] < val[c]):
                ok = False; break
        if not ok:
            continue
        # lattice word: read right-to-left, top-to-bottom; every prefix #1>=#2
        word = []
        for i in range(r):
            rowcells = sorted([c for c in cells if c[0] == i], key=lambda c: -c[1])
            for c in rowcells:
                word.append(val[c])
        c1 = c2 = 0; latt = True
        for x in word:
            if x == 1:
                c1 += 1
            else:
                c2 += 1
            if c2 > c1:
                latt = False; break
        if latt:
            cnt += 1
    return cnt


def two_strip_predecessors(rho):
    """all rho-- with rho/rho-- a union of two horizontal 4-strips (i.e. exists mu
       with rho--<mu<rho both h4). Return set."""
    out = set()
    for mu in horiz_strips_below(rho, 4):
        for rhomm in horiz_strips_below(mu, 4):
            out.add(rhomm)
    return sorted(out, reverse=True)


def eig_mult(S):
    """dims of +1 and -1 eigenspaces of exact-rational involution S (list of lists)."""
    n = len(S)
    # +1 eigenspace = ker(S - I); -1 = ker(S + I)
    def nullity(M):
        import copy
        A = [row[:] for row in M]
        rows = len(A); cols = len(A[0]); piv = 0
        for col in range(cols):
            sel = None
            for rr in range(piv, rows):
                if A[rr][col] != 0:
                    sel = rr; break
            if sel is None:
                continue
            A[piv], A[sel] = A[sel], A[piv]
            pv = A[piv][col]; A[piv] = [x / pv for x in A[piv]]
            for rr in range(rows):
                if rr != piv and A[rr][col] != 0:
                    f = A[rr][col]; A[rr] = [A[rr][k] - f * A[piv][k] for k in range(cols)]
            piv += 1
        return cols - piv
    I = [[Fr(1) if i == j else Fr(0) for j in range(n)] for i in range(n)]
    Sm = [[S[i][j] - I[i][j] for j in range(n)] for i in range(n)]
    Sp = [[S[i][j] + I[i][j] for j in range(n)] for i in range(n)]
    return nullity(Sm), nullity(Sp)


def check(rho):
    preds = two_strip_predecessors(rho)
    allok = True
    for rhomm in preds:
        mus, u = build_local(rho, rhomm)
        # LR multiplicities
        mult = {j: lr_two_row(rho, rhomm, 8 - j, j) for j in range(5)}
        even = sum(mult[j] for j in [0, 2, 4])
        odd = sum(mult[j] for j in [1, 3])
        if sum(mult.values()) != len(mus):
            print(f"  MISMATCH #mu {rho}/{rhomm}: paths {len(mus)} vs LR {sum(mult.values())}")
            allok = False; continue
        S = w0_matrix(mus, u)
        # involution check
        n = len(S)
        S2 = [[sum(S[i][k] * S[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
        isinv = all(S2[i][j] == (Fr(1) if i == j else Fr(0)) for i in range(n) for j in range(n))
        pdim, mdim = eig_mult(S)   # (+1, -1)
        tag = "ok" if (isinv and pdim == even and mdim == odd) else "FAIL"
        if tag != "ok":
            allok = False
        print(f"  {rho}/{rhomm}: #mu={len(mus)} LR(even,odd)=({even},{odd}) "
              f"eig(+,-)=({pdim},{mdim}) inv={isinv}  {tag}")
    return allok


if __name__ == "__main__":
    tests = [(8, 8), (6, 2), (10, 6), (8, 4, 4), (9, 5, 2), (12, 4)]
    ok = True
    for rho in tests:
        print("rho =", rho)
        ok = check(rho) and ok
    print("ALL LOCAL RECOUPLING TESTS", "PASSED" if ok else "FAILED")
