#!/usr/bin/env python3
"""
Session 42 -- driver for the sparse Wiedemann certificates (wk9_s42_wied.c).

nullity_sparse(rows, nc, p) returns (k, kern) with

    k = nullity_p(E)   certified in both directions:
        >= k : k verified vectors y (E y = 0 checked in C AND re-checked here by
               scipy sparse products), independent (flint rank of the k x nc matrix);
        <= k : the matrix [E; R] (R = k random dense rows) is nonsingular-certified
               by a Wiedemann minimal polynomial of degree nc with f(0) != 0.

The randomness (D, u, b, R, seeds) affects only whether a run is conclusive,
never the correctness of a conclusive verdict.  Inconclusive runs are retried
with fresh seeds up to MAX_INCONCLUSIVE times, then an error is raised (the
cell is then reported as not reached by this route).

usage (self-test): python3 wk9_s42_sparse.py --selftest [ntests]
"""
import sys, os, time, subprocess, random
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from flint import nmod_mat

WIED = os.environ.get('WIED_BIN', '/home/claude/wied')
WORK = os.environ.get('WIED_WORK', '/root/s42/work')
MAX_INCONCLUSIVE = 8

def log(*a):
    print(*a, file=sys.stderr); sys.stderr.flush()

def build_bin():
    src = os.path.join(HERE, 'wk9_s42_wied.c')
    if not os.path.exists(WIED) or os.path.getmtime(WIED) < os.path.getmtime(src):
        subprocess.check_call(['gcc', '-O3', '-march=native', '-o', WIED, src])

def rows_to_csr(rows, nc):
    """list of {col: val} -> scipy csr (int64, raw small values)."""
    from scipy import sparse
    nrows = len(rows)
    lens = np.fromiter((len(d) for d in rows), dtype=np.int64, count=nrows)
    rowptr = np.zeros(nrows + 1, dtype=np.int64); rowptr[1:] = np.cumsum(lens)
    nnz = int(rowptr[-1])
    col = np.fromiter((c for d in rows for c in d), dtype=np.int64, count=nnz)
    val = np.fromiter((v for d in rows for v in d.values()), dtype=np.int64, count=nnz)
    return sparse.csr_matrix((val, col, rowptr), shape=(nrows, nc))

def compress(E, sample, group, rng, margin=64):
    """random row sampling + grouping.  Rows of the result are +-1 sums of
    `group` sampled rows of E; `sample * nc` rows are sampled (all if larger
    than nrows).  Sampling and grouping can only LOSE rank, so
    'result injective => E injective' is exact; the kernel direction is
    re-verified against E by the caller."""
    from scipy import sparse
    nrows, nc = E.shape
    ns = min(nrows, int(sample * nc) + margin)
    if ns >= nrows and group <= 1:
        return E
    idx = rng.choice(nrows, size=ns, replace=False) if ns < nrows else np.arange(nrows)
    ng = max(nc + margin, (ns + group - 1) // group)
    grp = rng.integers(0, ng, size=ns)
    sgn = rng.choice(np.array([-1, 1], dtype=np.int64), size=ns)
    Pm = sparse.csr_matrix((sgn, (grp, idx)), shape=(ng, nrows), dtype=np.int64)
    PE = (Pm @ E).tocsr()
    PE.eliminate_zeros()
    return PE

def write_csr_mat(E, p, path):
    """scipy csr (int64, any sign) -> wied file, reduced mod p."""
    E = E.tocsr(); E.sort_indices()
    nrows, nc = E.shape
    rowptr = E.indptr.astype(np.int64); col = E.indices.astype(np.int32); val = (E.data % p).astype(np.uint32)
    nnz = int(rowptr[-1])
    with open(path, 'wb') as f:
        np.array([nc, nrows, nnz], dtype=np.int64).tofile(f)
        rowptr.tofile(f); col.tofile(f); val.tofile(f)
    return nrows, nnz

def write_csr(rows, nc, p, path):
    E = rows_to_csr(rows, nc)
    nrows, nnz = write_csr_mat(E, p, path)
    return nrows, nnz, E

def run_wied(path, p, seed, k_extra):
    out = subprocess.run([WIED, path, str(p), str(seed), str(k_extra)], capture_output=True, text=True)
    if out.returncode != 0:
        raise RuntimeError(("wied failed", out.returncode, out.stderr[-500:]))
    status, payload, diag = None, None, []
    for line in out.stdout.splitlines():
        if line.startswith('NONSINGULAR'): status = 'NONSINGULAR'; payload = line
        elif line.startswith('KERNEL'): status = 'KERNEL'; payload = [int(x) for x in line.split()[1:]]
        elif line.startswith('INCONCLUSIVE'): status = 'INCONCLUSIVE'; payload = line
        else: diag.append(line)
    if status is None: raise RuntimeError(("wied: no verdict", out.stdout[-300:], out.stderr[-300:]))
    return status, payload, diag

def check_kernel_py(E, nc, p, y):
    """E y == 0 mod p for scipy csr E (int64 raw values) and y a list of ints < p."""
    yv = np.array(y, dtype=np.int64)
    lo = yv & 0xFFFF; hi = yv >> 16          # |E| < 2^16 assumed (raw operator entries are tiny); products < 2^32, sums safe
    assert int(np.abs(E.data).max()) < 65536
    r = ((E @ lo) % p + ((E @ hi) % p) * 65536) % p
    return not np.any(r)

LEVELS = ((12, 2), (None, 1))     # (sample factor, group size); last = the full matrix.  Sampling can only lose rank; escalation on a spurious kernel vector.

def nullity_sparse(rows, nc, p, want_kern=False, seed0=1, tag='cell', verbose=True, levels=LEVELS):
    build_bin()
    os.makedirs(WORK, exist_ok=True)
    path = os.path.join(WORK, f'{tag}_{p}_{os.getpid()}.csr')
    E = rows if not isinstance(rows, list) else rows_to_csr(rows, nc)
    E = E.tocsr()
    assert E.shape[1] == nc
    rng = np.random.default_rng(seed0 * 7919 + p % 1000 + nc)
    kern = []
    seed = seed0
    bad = 0
    t0 = time.time()
    try:
        for li, (sample, group) in enumerate(levels):
            F = E if sample is None else compress(E, sample, group, rng)
            nrows, nnz = write_csr_mat(F, p, path)
            if verbose: log(f"    level {li}: {nrows} rows, nnz {nnz} (E: {E.shape[0]} rows, nnz {E.nnz})")
            escalate = False
            while not escalate:
                st, payload, diag = run_wied(path, p, seed, len(kern))
                if verbose:
                    log(f"    wied[{tag} p={p} seed={seed} k={len(kern)}]: {st} {' | '.join(diag)} ({time.time()-t0:.0f}s)")
                seed += 1
                if st == 'NONSINGULAR':
                    return len(kern), (kern if want_kern else None)
                if st == 'KERNEL':
                    y = payload
                    assert len(y) == nc
                    if not check_kernel_py(E, nc, p, y):
                        if verbose: log("    (kernel vector of the compressed matrix is not in ker E: escalate)")
                        escalate = True; continue
                    cand = kern + [y]
                    rk = nmod_mat(len(cand), nc, [v for vec in cand for v in vec], p).rank()
                    if rk == len(cand):
                        kern.append(y)
                    else:
                        bad += 1
                        if verbose: log("    (dependent kernel vector; retry)")
                else:
                    bad += 1
                if bad > MAX_INCONCLUSIVE:
                    raise RuntimeError(("sparse route inconclusive", tag, p, len(kern), bad))
        raise RuntimeError(("sparse route: escalation exhausted", tag, p, len(kern)))
    finally:
        try: os.remove(path)
        except OSError: pass

# ------------------------------------------------------------------ self-test
def selftest(ntests=200, seed=7):
    rnd = random.Random(seed)
    P1, P2 = 2147483647, 2147483629
    ok = 0
    for t in range(ntests):
        p = P1 if t % 2 == 0 else P2
        n = rnd.randint(50, 800); k = rnd.randint(0, 6); m = n + rnd.randint(0, 3 * n)
        # G: m x (n-k) sparse, then E = [G | G X] with X sparse (n-k) x k
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
                for c, xv in X[j].items():
                    d[n - k + c] = d.get(n - k + c, 0) + g * xv
            rows.append({c: v for c, v in d.items() if v})
        rows = [d for d in rows if d]
        # true nullity by flint on the dense matrix
        M = nmod_mat(len(rows), n, p)
        for i, d in enumerate(rows):
            for c, v in d.items(): M[i, c] = v % p
        true_nul = n - M.rank()
        got, kern = nullity_sparse(rows, n, p, want_kern=True, seed0=rnd.randint(1, 10**6), tag=f'self{t}', verbose=False)
        assert got == true_nul, ("selftest mismatch", t, n, k, true_nul, got)
        assert len(kern) == got
        ok += 1
        if t % 20 == 0: log(f"  selftest {t}: n={n} planted k={k} true nullity {true_nul} -> {got} OK")
    log(f"selftest: {ok}/{ntests} passed")
    return ok

if __name__ == '__main__':
    if sys.argv[1:2] == ['--selftest']:
        selftest(int(sys.argv[2]) if len(sys.argv) > 2 else 200)
