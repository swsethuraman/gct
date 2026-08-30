"""Session 19: complete epsilon-contraction machinery for n x n x n tensors.

A degree-2n invariant of an n x n x n tensor is a COMPLETE epsilon contraction
of T^{(x)2n}: 2n copies, 6n indices, each of the 3 slots carrying 2n indices
which must be absorbed by 2 epsilon_n's.  A *pattern* is therefore a triple
(P1,P2,P3) of ordered set partitions of the 2n copies into two blocks of size n
-- one per slot.

Sign convention: within a block, copies in increasing order; blocks ordered by
their least element.  Any other choice differs by an overall sign.

Everything is exact integer arithmetic (int64; magnitudes bounded below).
"""
import numpy as np
from itertools import combinations, product

def eps(n):
    E = np.zeros((n,)*n, dtype=np.int64)
    from itertools import permutations
    for p in permutations(range(n)):
        s = 1
        q = list(p)
        for i in range(n):
            for j in range(i+1, n):
                if q[i] > q[j]: s = -s
        E[p] = s
    return E

def partitions_2n(n):
    """Unordered pairs of blocks of size n covering range(2n); canonical order."""
    cps = list(range(2*n))
    out = []
    for blk in combinations(cps, n):
        if blk[0] != 0: continue            # block containing 0 is listed first
        rest = tuple(c for c in cps if c not in blk)
        out.append((blk, rest))
    return out

LET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def contract(T, pattern, n):
    """T: (n,n,n) int array.  pattern: (P1,P2,P3), each a pair of blocks."""
    # index label for (copy c, slot s)
    lab = {}
    k = 0
    for c in range(2*n):
        for s in range(3):
            lab[(c, s)] = LET[k]; k += 1
    ops, subs = [], []
    for c in range(2*n):
        ops.append(T); subs.append("".join(lab[(c, s)] for s in range(3)))
    E = eps(n)
    for s in range(3):
        for blk in pattern[s]:
            ops.append(E); subs.append("".join(lab[(c, s)] for c in blk))
    return int(np.einsum(",".join(subs) + "->", *ops, optimize=True))

def all_patterns(n):
    P = partitions_2n(n)
    return [(a, b, c) for a in P for b in P for c in P]
