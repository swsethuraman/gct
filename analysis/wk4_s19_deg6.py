"""Step 4: enumerate the degree-6 complete epsilon contractions of a 3x3x3
tensor and determine the dimension of their span."""
import numpy as np, sympy as sp, sys, time
sys.path.insert(0, 'analysis')
from wk4_s19_eps import contract, all_patterns, partitions_2n

P = partitions_2n(3)
print("partitions of 6 copies into two ordered blocks of 3:", len(P), P)
pats = all_patterns(3)
print("patterns (10^3):", len(pats))

rng = np.random.default_rng(19)
NPT = 40
TESTS = [rng.integers(-9, 10, size=(3,3,3)).astype(np.int64) for _ in range(NPT)]

t0 = time.time()
rows = [[contract(T, p, 3) for p in pats] for T in TESTS]
print("evaluated %d patterns x %d points in %.1fs" % (len(pats), NPT, time.time()-t0))
print("max |value| =", max(abs(v) for r in rows for v in r), " (int64 headroom fine)")

M = sp.Matrix(rows)                      # NPT x 1000
print("RANK of the pattern-evaluation matrix =", M.rank())

# proportionality audit
nzcols = [j for j in range(len(pats)) if any(rows[i][j] for i in range(NPT))]
print("nonvanishing patterns: %d / %d" % (len(nzcols), len(pats)))
j0 = nzcols[0]
base = [rows[i][j0] for i in range(NPT)]
ratios = {}
for j in range(len(pats)):
    rs = {sp.Rational(rows[i][j], base[i]) for i in range(NPT) if base[i] != 0}
    assert len(rs) == 1, (j, rs)
    ratios[j] = rs.pop()
from collections import Counter
print("distinct ratios to pattern", pats[j0], ":", sorted(set(ratios.values())))
print("ratio multiset:", Counter(ratios.values()))
np.save('/home/claude/j0.npy', np.array([j0]))
