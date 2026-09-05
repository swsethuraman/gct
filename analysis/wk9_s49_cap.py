#!/usr/bin/env python3
"""Session 49, M1: the two six-row cap degrees recomputed from scratch.

For (n, r) = (4, 6) and d in a range: dim S_d, h_d = [t^d]((1-t^{n-1})/(1-t))^r,
rho_d = dim S_d - h_d, the Gulliksen--Negard Hilbert function H_{S/J(M)}(d) of
the ideal of 3x3 minors of a generic-grade pencil and its ceiling
dim S_d - H(d); then the rank of the degree-d Macaulay matrix of the r partials
of det_4(sum s_i A_i) at fresh integer pencils modulo both house primes.

Smallest usable minor = (generic determinantal rank) + 1, NOT rho_d: a k x k
minor vanishes identically on D_r^{det_n} iff k > generic determinantal rank,
and is not identically zero iff k <= rho_d.

usage: wk9_s49_cap.py ladder [dmin] [dmax] [pencils]
       wk9_s49_cap.py certify <d> <k> <pencil_index>     (multimodular, size k)

Shares no code with analysis/wk9_s44_*.py; polynomial arithmetic is a dict of
exponent tuples, ranks are python-flint nmod_mat only.
"""
import sys, os, math, random, time, itertools
from flint import nmod_mat, fmpz

SEED = 20260905                      # results/PREREG_s49.md
P1, P2 = 2147483647, 2147483629
N, R = 4, 6                          # det_n, r variables


# ---------------------------------------------------------------- monomials
def monomials(r, d):
    """All exponent tuples of length r summing to d, lexicographic."""
    if r == 1:
        return [(d,)]
    out = []
    for a in range(d, -1, -1):
        for rest in monomials(r - 1, d - a):
            out.append((a,) + rest)
    return out


def hseries(n, r, d):
    """h_d = [t^d] ((1 - t^{n-1})/(1 - t))^r = [t^d] (1 + t + ... + t^{n-2})^r."""
    poly = {0: 1}
    for _ in range(r):
        new = {}
        for e, c in poly.items():
            for k in range(n - 1):
                new[e + k] = new.get(e + k, 0) + c
        poly = new
    return poly.get(d, 0)


def gn_hilbert(n, r, d):
    """H_{S/J}(d), J = ideal of (n-1)-minors of a generic n x n pencil in r
    variables with grade 4: numerator 1 - n^2 t^{n-1} + (2n^2-2) t^n - n^2 t^{n+1}
    + t^{2n} over (1-t)^r."""
    num = {0: 1, n - 1: -n * n, n: 2 * n * n - 2, n + 1: -n * n, 2 * n: 1}
    tot = 0
    for e, c in num.items():
        k = d - e
        if k >= 0:
            tot += c * math.comb(k + r - 1, r - 1)
    return tot


# ---------------------------------------------------------------- polynomials
def padd(a, b, scale=1):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, 0) + scale * v
    return {k: v for k, v in out.items() if v != 0}


def pmul(a, b):
    out = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            k = tuple(x + y for x, y in zip(ka, kb))
            out[k] = out.get(k, 0) + va * vb
    return {k: v for k, v in out.items() if v != 0}


def det_poly(mats, r):
    """det(sum_i s_i A_i) as a dict monomial -> int, Laplace expansion."""
    n = len(mats[0])
    # entry (i,j) as a linear polynomial in s
    unit = [tuple(1 if t == k else 0 for t in range(r)) for k in range(r)]
    ent = [[{unit[k]: mats[k][i][j] for k in range(r) if mats[k][i][j] != 0}
            for j in range(n)] for i in range(n)]

    def rec(rows, cols):
        if len(rows) == 1:
            return ent[rows[0]][cols[0]]
        i = rows[0]
        tot = {}
        for idx, j in enumerate(cols):
            e = ent[i][j]
            if not e:
                continue
            sub = rec(rows[1:], cols[:idx] + cols[idx + 1:])
            tot = padd(tot, pmul(e, sub), scale=(-1) ** idx)
        return tot

    return rec(list(range(n)), list(range(n)))


def partial(f, i):
    out = {}
    for k, v in f.items():
        if k[i] > 0:
            kk = list(k); kk[i] -= 1
            out[tuple(kk)] = out.get(tuple(kk), 0) + v * k[i]
    return out


def random_pencil(rnd, box, n, r):
    return [[[rnd.randint(-box, box) for _ in range(n)] for _ in range(n)]
            for _ in range(r)]


def random_form(rnd, box, n, r):
    return {m: rnd.randint(-box, box) for m in monomials(r, n)}


# ---------------------------------------------------------------- Macaulay
def macaulay_rows(F, n, r, d):
    """Rows of M_d(F): for each partial i and monomial m of degree d-n+1,
    the coefficient vector (over columns = monomials of degree d) of m*d_iF.
    Returned as a list of dicts column-index -> int."""
    cols = monomials(r, d)
    cidx = {m: t for t, m in enumerate(cols)}
    parts = [partial(F, i) for i in range(r)]
    rows = []
    for i in range(r):
        for m in monomials(r, d - n + 1):
            row = {}
            for k, v in parts[i].items():
                col = tuple(x + y for x, y in zip(k, m))
                row[cidx[col]] = v
            rows.append(row)
    return rows, len(cols)


def rank_mod(rows, ncols, p):
    M = nmod_mat(len(rows), ncols, p)
    for a, row in enumerate(rows):
        for b, v in row.items():
            M[a, b] = v % p
    return M.rank()


def row_norm_bound(F, r):
    """max_i ||d_i F||_2 (exact rational -> ceiling as integer, via squares)."""
    best = 0
    for i in range(r):
        s = sum(v * v for v in partial(F, i).values())
        best = max(best, s)
    return best  # squared norm, exact integer


# ---------------------------------------------------------------- primes
def is_probable_prime(n):
    return fmpz(n).is_probable_prime()


def primes_62bit(count_bits_needed):
    """Descending 62-bit primes until sum log2 p > count_bits_needed."""
    out, acc = [], 0.0
    q = 2 ** 62 - 1
    while acc <= count_bits_needed:
        if is_probable_prime(q):
            out.append(q)
            acc += math.log2(q)
        q -= 2
    return out


# ---------------------------------------------------------------- modes
def ladder(dmin, dmax, npencils):
    print(f"[s49 cap] n={N} r={R} d={dmin}..{dmax}; seed {SEED}; box 1e6; primes {P1},{P2}",
          flush=True)
    print(" d | dim S_d | h_d | rho_d | H_GN(d) | ceiling | smooth ranks | determinantal ranks | minor size")
    for d in range(dmin, dmax + 1):
        dimS = math.comb(d + R - 1, R - 1)
        h = hseries(N, R, d)
        rho = dimS - h
        H = gn_hilbert(N, R, d)
        ceil = dimS - H
        smooth, dets = [], []
        for t in range(npencils):
            rnd = random.Random(SEED + 1000 * d + 10 * t + 1)   # offset stated
            G = random_form(rnd, 10 ** 6, N, R)
            rows, nc = macaulay_rows(G, N, R, d)
            smooth.append(tuple(rank_mod(rows, nc, p) for p in (P1, P2)))
            rnd = random.Random(SEED + 1000 * d + 10 * t + 2)
            A = random_pencil(rnd, 10 ** 6, N, R)
            F = det_poly(A, R)
            rows, nc = macaulay_rows(F, N, R, d)
            dets.append(tuple(rank_mod(rows, nc, p) for p in (P1, P2)))
        drank = max(max(x) for x in dets)
        print(f" {d} | {dimS} | {h} | {rho} | {H} | {ceil} | {smooth} | {dets} | {drank + 1}",
              flush=True)


def certify(d, k, t):
    """Multimodular certificate: all k x k minors of M_d(F) vanish over Z at the
    pencil t, provided rank_p < k for a set of primes with product > 2*Hadamard."""
    rnd = random.Random(SEED + 7000 + 5150081 * t)             # offset stated
    A = random_pencil(rnd, 10 ** 12, N, R)
    F = det_poly(A, R)
    rows, nc = macaulay_rows(F, N, R, d)
    sq = row_norm_bound(F, R)
    # Hadamard: |minor| <= (max row norm)^k = sq^(k/2); need prod p > 2*that
    bits = 1 + 0.5 * k * math.log2(sq)
    primes = primes_62bit(bits)
    print(f"[s49 certify] n={N} r={R} d={d} size {k}, pencil {t} (seed {SEED}+7000+{5150081*t}), "
          f"box 1e12, shape {len(rows)}x{nc}", flush=True)
    print(f"  pencil A_1 first row: {A[0][0]}", flush=True)
    print(f"  max ||d_iF||_2^2 = {sq} (~2^{math.log2(sq):.1f}); log2 Hadamard(size {k}) <= {bits:.0f}; "
          f"need {len(primes)} 62-bit primes", flush=True)
    ranks, t0 = set(), time.time()
    for i, p in enumerate(primes, 1):
        ranks.add(rank_mod(rows, nc, p))
        if i % 250 == 0 or i == len(primes):
            print(f"    {i}/{len(primes)} primes, ranks {sorted(ranks)}, {time.time()-t0:.0f}s", flush=True)
    if max(ranks) < k:
        print(f"  -> every {k}x{k} minor of M_{d} is divisible by a product exceeding twice its Hadamard "
              f"bound, hence zero: rank_Q M_{d} <= {k-1} at this pencil.  With rank_p = {max(ranks)} "
              f"as the lower bound, rank_Q = {max(ranks)} exactly.  CERTIFIED", flush=True)
    else:
        print(f"  -> NOT certified: some prime gave rank {max(ranks)} >= {k}", flush=True)
    # also the two house primes, for the record
    print(f"  house primes: {[rank_mod(rows, nc, p) for p in (P1, P2)]}", flush=True)


if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "ladder":
        dmin = int(sys.argv[2]) if len(sys.argv) > 2 else 4
        dmax = int(sys.argv[3]) if len(sys.argv) > 3 else 9
        npen = int(sys.argv[4]) if len(sys.argv) > 4 else 3
        ladder(dmin, dmax, npen)
    elif mode == "certify":
        certify(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    else:
        raise SystemExit(__doc__)
