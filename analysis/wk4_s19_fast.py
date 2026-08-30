"""Fast exact evaluator for the degree-6 complete epsilon contractions of a
3x3x3 tensor, plus the PROVED reduction that fixes the slot-1 partition.

REDUCTION (proved, not assumed).  All six copies carry the SAME tensor T, so
for any pi in S6 the pattern (P1,P2,P3) and its relabelling (pi P1, pi P2,
pi P3) have equal contractions up to the sign incurred by restoring the
canonical within-block ordering.  S6 acts transitively on the 10 partitions of
{0..5} into two 3-blocks, hence every pattern equals +- one with
P1 = ((0,1,2),(3,4,5)).  Only 10 x 10 = 100 patterns need evaluating.
(NOTE: this is a symmetry of the *copies*, independent of any census law about
symmetric cubic forms -- those do not apply here, see the doc.)

Contraction, done in two cheap stages:
  H[j0,k0,j1,k1,j2,k2] = sum_i eps_{i0 i1 i2} T[i0,j0,k0] T[i1,j1,k1] T[i2,j2,k2]
  I = sum  H(copies 0,1,2) H(copies 3,4,5) * (2 slot-2 eps) * (2 slot-3 eps)
"""
import numpy as np
from itertools import combinations

EPS3 = np.zeros((3,3,3), dtype=np.int64)
for p, s in [((0,1,2),1),((1,2,0),1),((2,0,1),1),((0,2,1),-1),((2,1,0),-1),((1,0,2),-1)]:
    EPS3[p] = s

def partitions6():
    out = []
    for blk in combinations(range(6), 3):
        if blk[0] != 0: continue
        out.append((blk, tuple(c for c in range(6) if c not in blk)))
    return out
PARTS = partitions6()

LET = "abcdefghijklmnopqrstuvwxyz"

def make_H(T):
    return np.einsum('abc,axy,bzw,cuv->xyzwuv', EPS3, T, T, T, optimize=True)

# axis of copy c inside (H1,H2): H1 carries copies 0,1,2 ; H2 carries 3,4,5
def axes(c, slot):          # slot 1 -> j (offset 0), slot 2 -> k (offset 1)
    which = 0 if c < 3 else 1
    return which, 2*(c % 3) + slot

_PATHCACHE = {}
def contract6(H, P2, P3):
    lab = {}
    k = 0
    subs1, subs2 = [None]*6, [None]*6
    for c in range(6):
        for slot in (0, 1):
            w, ax = axes(c, slot)
            lab[(c, slot)] = LET[k]
            (subs1 if w == 0 else subs2)[ax] = LET[k]
            k += 1
    ops = [H, H]
    subs = ["".join(subs1), "".join(subs2)]
    for slot, P in ((0, P2), (1, P3)):
        for blk in P:
            ops.append(EPS3); subs.append("".join(lab[(c, slot)] for c in blk))
    key = ",".join(subs)
    if key not in _PATHCACHE:
        _PATHCACHE[key] = np.einsum_path(key + "->", *ops, optimize='optimal')[0]
    return int(np.einsum(key + "->", *ops, optimize=_PATHCACHE[key]))

def all_values(T):
    H = make_H(T)
    return {(i, j): contract6(H, PARTS[i], PARTS[j])
            for i in range(10) for j in range(10)}
