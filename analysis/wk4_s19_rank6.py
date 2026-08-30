"""Step 4 (continued): the degree-6 span is 1-dimensional; which patterns die."""
import numpy as np, sympy as sp, sys
sys.path.insert(0,'analysis')
from wk4_s19_fast import all_values, PARTS
from collections import Counter

rng = np.random.default_rng(2026)
NPT = 60
TESTS = [rng.integers(-40, 41, size=(3,3,3)).astype(np.int64) for _ in range(NPT)]
tab = [all_values(T) for T in TESTS]
keys = [(i,j) for i in range(10) for j in range(10)]
rows = [[t[k] for k in keys] for t in tab]
print("max |value|:", max(abs(v) for r in rows for v in r))
M = sp.Matrix(rows)
print("RANK over %d random points, %d patterns  =  %d" % (NPT, len(keys), M.rank()))

nz = [k for k in keys if any(t[k] for t in tab)]
print("nonvanishing patterns: %d / 100" % len(nz))
base = [t[nz[0]] for t in tab]
rat = {}
for k in keys:
    rs = {sp.Rational(t[k], b) for t, b in zip(tab, base) if b}
    assert len(rs) == 1, (k, rs)
    rat[k] = rs.pop()
print("ratios to pattern", nz[0], ":", Counter(rat.values()))

# --- the S6 relabelling reduction, checked empirically on non-canonical P1 ---
sys.path.insert(0,'analysis')
from wk4_s19_eps import contract, partitions_2n
P = partitions_2n(3)
T = TESTS[0]
import itertools, random
random.seed(1)
print("\nS6-reduction spot check (non-canonical P1 vs +-canonical):")
for trial in range(3):
    a, b, c = random.randrange(10), random.randrange(10), random.randrange(10)
    v = contract(T, (P[a], P[b], P[c]), 3)
    # relabel so that P[a] -> P[0] = ((0,1,2),(3,4,5))
    perm = {}
    for pos, cp in enumerate(P[a][0] + P[a][1]): perm[cp] = pos
    def img(Q): 
        B0 = tuple(sorted(perm[x] for x in Q[0])); B1 = tuple(sorted(perm[x] for x in Q[1]))
        return (B0, B1) if B0[0] == 0 else (B1, B0)
    b2, c2 = img(P[b]), img(P[c])
    i2 = PARTS.index(b2); j2 = PARTS.index(c2)
    w = tab[0][(i2, j2)]
    print("  P1=%d P2=%d P3=%d -> %d ; canonical (%d,%d) -> %d ; equal up to sign: %s"
          % (a, b, c, v, i2, j2, w, abs(v) == abs(w)))
