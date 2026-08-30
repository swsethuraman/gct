"""Step 3: RE-DERIVED vanishing rule for degree-6 3x3x3 patterns.

PROVED LEMMA (transposition rule).  Let tau = (a b) transpose two copies.
Since every copy carries the SAME tensor T, tau maps the pattern (P1,P2,P3) to
(tau P1, tau P2, tau P3) with the same value up to the sign of restoring
canonical block orders.  A 3-element block cannot be exchanged with its
complement by a transposition, so tau fixes a partition iff a,b lie in the SAME
block; and then it transposes two arguments of that slot's epsilon, sign -1.
Hence if a,b share a block in ALL THREE slots, the pattern is fixed by tau with
sign (-1)^3 = -1, so I = 0.

This is a statement about identical tensor COPIES and epsilon antisymmetry
only.  It is NOT the census vanishing law (two legs of one copy of a symmetric
cubic into the same epsilon), which relies on symmetry of a second derivative
and does NOT apply here: T's three slots live in different factors.
"""
import numpy as np, sys
sys.path.insert(0,'analysis')
from wk4_s19_fast import all_values, PARTS
from itertools import combinations

def samepairs(P):
    s = set()
    for blk in P:
        for p in combinations(blk, 2): s.add(p)
    return s

P1 = PARTS[0]
rng = np.random.default_rng(77)
tab = [all_values(rng.integers(-30,31,size=(3,3,3)).astype(np.int64)) for _ in range(20)]

pred_zero, act_zero = set(), set()
for i in range(10):
    for j in range(10):
        S = samepairs(P1) & samepairs(PARTS[i]) & samepairs(PARTS[j])
        if S: pred_zero.add((i,j))
        if all(t[(i,j)] == 0 for t in tab): act_zero.add((i,j))
print("predicted zero by the transposition lemma:", len(pred_zero))
print("actually zero                            :", len(act_zero))
print("rule is EXACT (predicted == actual):", pred_zero == act_zero)
print("  lemma-zeros not actually zero:", sorted(pred_zero - act_zero))
print("  extra zeros not explained    :", sorted(act_zero - pred_zero))
