"""Session 56 — the Foulkes engine: shared exact routines.

Everything here lives in the symmetric-group category.  No highest-weight
vectors, no determinantal pencils, no floating point.

Objects
-------
* set partitions of [N], N = 4*delta, into delta blocks of size 4, each block a
  bit mask; the canonical form is the tuple of block masks sorted by lowest
  element.  These are the basis vectors of the Foulkes permutation module
  H_{4,delta} = Ind_{S_4 wr S_delta}^{S_N} 1.
* eps_pi = (x) over blocks of the 4x4x4x4 alternating tensor; the Gram kernel
      K(pi, pi') = sum_{x in [4]^N} eps_pi(x) eps_pi'(x)
  computed by the transparent sum (x runs over the 24^delta support of eps_pi).
* the relative position rel(pi, pi') = the delta x delta block-intersection
  matrix up to row and column permutation (a double coset W\S_N/W).
* Murnaghan–Nakayama characters of S_N (own implementation; cross-checked
  against scripts/ambient_screen.chi in the setup script).
* Kostka numbers K_{nu,mu} by horizontal-strip removal.
* exact ranks: flint nmod_mat at both house primes, fmpz_mat over Q.
"""
import itertools
from fractions import Fraction
from functools import lru_cache
from math import factorial

import flint

P1, P2 = 2147483647, 2147483629          # the house primes

# ----------------------------------------------------------------- partitions

def partitions(n, maxpart=None, maxlen=None):
    """Integer partitions of n, weakly decreasing tuples."""
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield ()
        return
    if maxlen == 0:
        return
    for p in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - p, p, None if maxlen is None else maxlen - 1):
            yield (p,) + rest


def dominates(nu, mu):
    """nu >= mu in dominance order (same size)."""
    s1 = s2 = 0
    for i in range(max(len(nu), len(mu))):
        s1 += nu[i] if i < len(nu) else 0
        s2 += mu[i] if i < len(mu) else 0
        if s1 < s2:
            return False
    return True


def hook_length_f(lam):
    """f^lambda = number of standard Young tableaux of shape lambda."""
    n = sum(lam)
    if n == 0:
        return 1
    conj = [sum(1 for x in lam if x > j) for j in range(lam[0])]
    prod = 1
    for i, li in enumerate(lam):
        for j in range(li):
            prod *= (li - j - 1) + (conj[j] - i - 1) + 1
    return factorial(n) // prod


# ---------------------------------------------------- Murnaghan–Nakayama rule

@lru_cache(maxsize=None)
def mn_char(lam, rho):
    """chi^lambda at cycle type rho (both tuples of positive ints, weakly
    decreasing), by rim-hook removal of the largest cycle."""
    lam = tuple(x for x in lam if x)
    if not rho:
        return 1 if not lam else 0
    r, rest = rho[0], rho[1:]
    L = len(lam)
    beta = [lam[j] + (L - 1 - j) for j in range(L)]      # beta numbers
    bset = set(beta)
    total = 0
    for i in range(L):
        b = beta[i] - r
        if b < 0 or b in bset:
            continue
        # height = number of beta numbers strictly between b and beta[i]
        ht = sum(1 for x in beta if b < x < beta[i])
        newbeta = sorted([x for j, x in enumerate(beta) if j != i] + [b], reverse=True)
        newlam = tuple(newbeta[j] - (L - 1 - j) for j in range(L))
        total += (-1) ** ht * mn_char(tuple(x for x in newlam if x), rest)
    return total


def cycle_type(perm):
    """perm: tuple, perm[i] = image of i.  Returns the partition of cycle lengths."""
    n = len(perm)
    seen = [False] * n
    ct = []
    for i in range(n):
        if not seen[i]:
            l, j = 0, i
            while not seen[j]:
                seen[j] = True
                j = perm[j]
                l += 1
            ct.append(l)
    return tuple(sorted(ct, reverse=True))


def class_size(rho):
    n = sum(rho)
    z = 1
    cnt = {}
    for p in rho:
        cnt[p] = cnt.get(p, 0) + 1
    for p, m in cnt.items():
        z *= p ** m * factorial(m)
    return factorial(n) // z


def sym2_char_value(chi_rect, rect, rho):
    """(Sym^2 chi)(g) = (chi(g)^2 + chi(g^2))/2 at cycle type rho; the cycle type
    of g^2 replaces each even cycle 2k by k, k and keeps odd cycles."""
    sq = []
    for r in rho:
        if r % 2:
            sq.append(r)
        else:
            sq += [r // 2, r // 2]
    sq = tuple(sorted(sq, reverse=True))
    return Fraction(chi_rect ** 2 + mn_char(rect, sq), 2)


def sk_coefficient(lam, delta):
    """sk(lambda, delta^4) = <chi^lambda, Sym^2 chi^{(delta^4)}> over S_{4 delta}."""
    N = 4 * delta
    rect = (delta,) * 4
    tot = Fraction(0)
    for rho in partitions(N):
        c = mn_char(tuple(lam), rho)
        if c:
            cr = mn_char(rect, rho)
            tot += Fraction(c * class_size(rho)) * sym2_char_value(cr, rect, rho)
    tot /= factorial(N)
    assert tot.denominator == 1, (lam, tot)
    return int(tot)


def g_coefficient(lam, delta):
    """the ordinary rectangular Kronecker coefficient g(lambda, delta^4, delta^4)."""
    N = 4 * delta
    rect = (delta,) * 4
    tot = 0
    for rho in partitions(N):
        c = mn_char(tuple(lam), rho)
        if c:
            tot += c * class_size(rho) * mn_char(rect, rho) ** 2
    assert tot % factorial(N) == 0
    return tot // factorial(N)


# ------------------------------------------------------------ Kostka numbers

@lru_cache(maxsize=None)
def kostka(nu, mu):
    """K_{nu,mu} = number of SSYT of shape nu and content mu, by removing the
    horizontal strip of the largest entry."""
    nu = tuple(x for x in nu if x)
    mu = tuple(x for x in mu if x)
    if sum(nu) != sum(mu):
        return 0
    if not mu:
        return 1 if not nu else 0
    if not dominates(nu, tuple(sorted(mu, reverse=True))):
        return 0
    k = mu[-1]
    rest = mu[:-1]
    total = 0
    # remove a horizontal strip of size k from nu: nu' with nu'_i <= nu_i,
    # nu'_i >= nu_{i+1}, sum nu - sum nu' = k
    L = len(nu)

    def rec(i, remaining, acc):
        nonlocal total
        if i == L:
            if remaining == 0:
                total += kostka(tuple(acc), rest)
            return
        lo = nu[i + 1] if i + 1 < L else 0
        for take in range(0, min(remaining, nu[i] - lo) + 1):
            acc.append(nu[i] - take)
            rec(i + 1, remaining - take, acc)
            acc.pop()

    rec(0, k, [])
    return total


# ------------------------------------------------- set partitions (H_{4,delta})

def set_partitions(N):
    """All partitions of range(N) into N/4 blocks of size 4, each as a tuple of
    block masks ordered by lowest element (canonical)."""
    assert N % 4 == 0
    out = []

    def rec(remaining, blocks):
        if not remaining:
            out.append(tuple(blocks))
            return
        first = remaining & -remaining
        rest = remaining ^ first
        others = [1 << i for i in range(N) if rest >> i & 1]
        for c in itertools.combinations(others, 3):
            m = first | c[0] | c[1] | c[2]
            blocks.append(m)
            rec(remaining ^ m, blocks)
            blocks.pop()

    rec((1 << N) - 1, [])
    return out


def canonical_partition(blocks):
    return tuple(sorted(blocks, key=lambda m: m & -m))


def apply_perm(perm, blocks):
    """perm: tuple with perm[i] = image of i, acting on block masks."""
    N = len(perm)
    new = []
    for m in blocks:
        mm = 0
        for i in range(N):
            if m >> i & 1:
                mm |= 1 << perm[i]
        new.append(mm)
    return canonical_partition(new)


def standard_partition(delta):
    return tuple(0xF << (4 * j) for j in range(delta))


def popcount(x):
    return bin(x).count("1")


def intersection_matrix(pi, pi2):
    return tuple(tuple(popcount(a & b) for b in pi2) for a in pi)


def rel(pi, pi2):
    """canonical form of the block-intersection matrix under independent row and
    column permutations (delta <= 5: brute force over column permutations, rows
    sorted)."""
    M = intersection_matrix(pi, pi2)
    delta = len(pi)
    best = None
    for cp in itertools.permutations(range(delta)):
        rows = sorted(tuple(row[c] for c in cp) for row in M)
        key = tuple(rows)
        if best is None or key < best:
            best = key
    return best


# --------------------------------------------------------------- the kernel K

def eps_sign(vals):
    """sign of the 4 values (a permutation of 0..3) or 0 if repeated."""
    if len(set(vals)) < 4:
        return 0
    s = 1
    v = list(vals)
    for i in range(4):
        for j in range(i + 1, 4):
            if v[i] > v[j]:
                s = -s
    return s


def block_positions(mask, N):
    return [i for i in range(N) if mask >> i & 1]


def kernel_K(pi, pi2, N):
    """K(pi, pi2) = sum_x eps_pi(x) eps_pi2(x) over x in [4]^N, by running x over
    the support of eps_pi (a permutation of 0..3 on every block of pi)."""
    blocks = [block_positions(m, N) for m in pi]
    blocks2 = [block_positions(m, N) for m in pi2]
    perms = list(itertools.permutations(range(4)))
    signs = {p: eps_sign(p) for p in perms}
    total = 0
    x = [0] * N
    for choice in itertools.product(perms, repeat=len(blocks)):
        s = 1
        for b, p in zip(blocks, choice):
            s *= signs[p]
            for pos, v in zip(b, p):
                x[pos] = v
        for b in blocks2:
            e = eps_sign(tuple(x[pos] for pos in b))
            if e == 0:
                s = 0
                break
            s *= e
        total += s
    return total


# -------------------------------------------------------------- exact ranks

def rank_mod_p(rows, p):
    """rows: list of lists of Python ints."""
    if not rows or not rows[0]:
        return 0
    m, n = len(rows), len(rows[0])
    M = flint.nmod_mat(m, n, [int(v) % p for row in rows for v in row], p)
    return M.rank()


def rank_both_primes(rows):
    return rank_mod_p(rows, P1), rank_mod_p(rows, P2)


def rank_Q(rows):
    if not rows or not rows[0]:
        return 0
    m, n = len(rows), len(rows[0])
    M = flint.fmpz_mat(m, n, [int(v) for row in rows for v in row])
    return M.rank()


def inverse_kostka_matrix(weights):
    """weights: list of partitions (same size) sorted so that dominance is
    compatible (any linear extension: larger first).  Returns (K, Kinv) as
    lists of lists of Fractions, K[i][j] = K_{weights[i], weights[j]}."""
    n = len(weights)
    K = [[Fraction(kostka(weights[i], weights[j])) for j in range(n)] for i in range(n)]
    # unitriangular in a dominance-compatible order: invert by back substitution
    Kinv = [[Fraction(0)] * n for _ in range(n)]
    for i in range(n):
        Kinv[i][i] = Fraction(1)
    # solve K * Kinv = I column by column (K upper unitriangular when rows/cols
    # are ordered with the most dominant first: K[i][j] != 0 only if w_i >= w_j)
    for j in range(n):
        col = [Fraction(0)] * n
        col[j] = Fraction(1)
        # forward: K is upper triangular (i <= j nonzero), solve from bottom
        x = [Fraction(0)] * n
        for i in range(n - 1, -1, -1):
            s = col[i] - sum(K[i][k] * x[k] for k in range(i + 1, n))
            x[i] = s / K[i][i]
        for i in range(n):
            Kinv[i][j] = x[i]
    return K, Kinv


# ------------------------------------------------ signed kernel via one row

def coset_rep(pi, delta):
    """g with g(pi0) = pi, block j of pi0 -> block j of pi, increasing on each
    block (so sigma(g, pi0) = +1 and eps_pi = g . eps_0)."""
    N = 4 * delta
    g = [0] * N
    for j, m in enumerate(pi):
        dst = block_positions(m, N)
        for t in range(4):
            g[4 * j + t] = dst[t]
    return tuple(g)


def block_sign(h, pi, N):
    """sigma(h, pi) = prod over blocks B of pi of the sign of the permutation
    sorting (h(b_1), ..., h(b_4)), b_1 < ... < b_4 the elements of B."""
    s = 1
    for m in pi:
        img = [h[p] for p in block_positions(m, N)]
        for i in range(4):
            for j in range(i + 1, 4):
                if img[i] > img[j]:
                    s = -s
    return s


def support_of_eps0(delta):
    """all x in [4]^N with eps_0(x) != 0, as an int8 array (24^delta x N), and
    the signs eps_0(x)."""
    import numpy as np
    perms = list(itertools.permutations(range(4)))
    sg = np.array([eps_sign(p) for p in perms], dtype=np.int8)
    P = np.array(perms, dtype=np.int8)
    X = P
    S = sg.copy()
    for _ in range(delta - 1):
        X = np.concatenate([np.repeat(X, 24, axis=0), np.tile(P, (X.shape[0], 1))], axis=1)
        S = np.repeat(S, 24) * np.tile(sg, S.shape[0])
    return X, S


def krow_direct(H, delta):
    """K(pi0, pi) for every pi in H by the transparent tensor sum, vectorised
    over the 24^delta support of eps_0."""
    import numpy as np
    N = 4 * delta
    X, S = support_of_eps0(delta)
    # sign table for 4-tuples with values 0..3 (code base 4)
    table = np.zeros(256, dtype=np.int8)
    for p in itertools.permutations(range(4)):
        table[p[0] * 64 + p[1] * 16 + p[2] * 4 + p[3]] = eps_sign(p)
    out = []
    for pi in H:
        s = S.astype(np.int32).copy()
        for m in pi:
            pos = block_positions(m, N)
            c = X[:, pos[0]].astype(np.int32) * 64 + X[:, pos[1]] * 16 + X[:, pos[2]] * 4 + X[:, pos[3]]
            s *= table[c]
        out.append(int(s.sum()))
    return out


def margin4_matrices(delta):
    """all delta x delta nonnegative integer matrices with every row and column
    sum 4 (the labelled block-intersection matrices)."""
    out = []
    rows = [c for c in itertools.product(range(5), repeat=delta) if sum(c) == 4]

    def rec(i, colsum, acc):
        if i == delta:
            if all(c == 4 for c in colsum):
                out.append(tuple(acc))
            return
        remaining = delta - i
        for r in rows:
            nc = tuple(colsum[j] + r[j] for j in range(delta))
            if any(x > 4 for x in nc):
                continue
            # feasibility: remaining rows must supply 4 - nc[j] to each column
            if sum(4 - x for x in nc) != 4 * (remaining - 1):
                continue
            acc.append(r)
            rec(i + 1, nc, acc)
            acc.pop()

    rec(0, (0,) * delta, [])
    return out


def canonical_matrix(M):
    """canonical form of a matrix under independent row and column permutations
    (brute force over column permutations, rows sorted)."""
    delta = len(M)
    best = None
    for cp in itertools.permutations(range(delta)):
        key = tuple(sorted(tuple(row[c] for c in cp) for row in M))
        if best is None or key < best:
            best = key
    return best
