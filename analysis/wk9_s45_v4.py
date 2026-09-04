#!/usr/bin/env python3
"""Session 45 -- V4: the sparse route (Berlekamp-Massey included) against
python-flint on synthetic sparse matrices with planted nullities 0-6.

Two batteries at both house primes:
  (A) wk9_s42_sparse.selftest as written (s42's own levels), n in [50, 800];
  (B) the same generator through wk9_s45_cell.nullity_stacked with the s45
      'cheap' level set ((3,2),(12,2),(None,1)) and a pinned dense block
      standing in for the evaluation rows, so the level set actually used in the
      sweep is validated, not just s42's.
Every verdict is compared with the exact flint rank of the dense matrix.

usage: python3 wk9_s45_v4.py [nA] [nB]
"""
import sys, os, json, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
os.environ.setdefault('WIED_BIN', '/home/claude/wied45')
os.environ.setdefault('WIED_WORK', '/home/claude/s45/work')
import numpy as np
from scipy import sparse
from flint import nmod_mat
from wk9_s42_sparse import selftest, rows_to_csr, log
from wk9_s45_cell import nullity_stacked, LEVELS, check_kernel_full
P1, P2 = 2147483647, 2147483629

def gen(rnd, n, k, m, ndense):
    """m x n sparse of rank exactly n - k (columns n-k..n-1 are combinations of
    the others), plus ndense dense rows in the same column space."""
    G = [{} for _ in range(m)]
    for i in range(m):
        for _ in range(rnd.randint(1, 4)):
            G[i][rnd.randrange(n - k)] = rnd.choice([1, -1, 2, -3, 5, 7])
    X = [{} for _ in range(n - k)]
    for c in range(k):
        for _ in range(rnd.randint(1, 3)):
            X[rnd.randrange(n - k)][c] = rnd.choice([1, -1, 2, 3])
    rows = []
    for i in range(m):
        d = dict(G[i])
        for j, g in G[i].items():
            for c, xv in X[j].items(): d[n - k + c] = d.get(n - k + c, 0) + g * xv
        d = {c: v for c, v in d.items() if v}
        if d: rows.append(d)
    dense = []
    for _ in range(ndense):
        base = {rnd.randrange(n - k): rnd.randint(1, 1000) for _ in range(n - k)}
        row = [0] * n
        for j, g in base.items():
            row[j] += g
            for c, xv in X[j].items(): row[n - k + c] += g * xv
        dense.append(row)
    return rows, dense

def batteryB(ntests=100, seed=13):
    rnd = random.Random(seed); ok = 0
    for t in range(ntests):
        p = P1 if t % 2 == 0 else P2
        n = rnd.randint(60, 700); k = rnd.randint(0, 6); m = n + rnd.randint(0, 3 * n)
        nd = rnd.randint(1, 12)
        rows, dense = gen(rnd, n, k, m, nd)
        E = rows_to_csr(rows, n)
        EV = sparse.csr_matrix(np.array(dense, dtype=np.int64)) if dense else sparse.csr_matrix((0, n), dtype=np.int64)
        Full = sparse.vstack([E, EV]).tocoo()
        M = nmod_mat(Full.shape[0], n, p)
        for a, b, v in zip(Full.row, Full.col, Full.data): M[int(a), int(b)] = int(v) % p
        true_nul = n - M.rank()
        got, kern, lvl, _ = nullity_stacked(E, EV, n, p, want_kern=True,
                                            seed0=rnd.randint(1, 10**6), tag=f'v4b{t}',
                                            levels=LEVELS['cheap'], verbose=False)
        assert got == true_nul, ("V4B mismatch", t, n, k, nd, true_nul, got)
        assert len(kern) == got
        for y in kern:
            assert check_kernel_full(Full.tocsr(), n, p, y), ("V4B kernel vector fails", t)
        ok += 1
        if t % 20 == 0: log(f"  V4B {t}: n={n} planted k={k} dense {nd} true nullity {true_nul} -> {got} (level {lvl}) OK")
    log(f"V4B: {ok}/{ntests} passed (s45 'cheap' levels, pinned dense rows)")
    return ok

if __name__ == '__main__':
    nA = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    nB = int(sys.argv[2]) if len(sys.argv) > 2 else 100
    t0 = time.time()
    a = selftest(nA)
    b = batteryB(nB)
    res = dict(battery_A=dict(passed=a, total=nA, levels='s42 default ((12,2),(None,1))'),
               battery_B=dict(passed=b, total=nB, levels="s45 'cheap' ((3,2),(12,2),(None,1)) + pinned dense rows"),
               secs=round(time.time() - t0, 1))
    print(json.dumps(res))
    open(os.path.join(HERE, '..', 'results', 's45_v4.json'), 'w').write(json.dumps(res, indent=1))
