#!/usr/bin/env python3
"""
Session 71 -- the monomial code widened past the int64 wall (re-implementation
of session 67's C2 from its record; the session-67 bundle was not available).

wk9_s42_orbits._codes(M, L) is the multiset combinadic of each sorted row of the
(N x d) index array M:  code = sum_k C(M[:,k] + k, k + 1), injective on sorted
d-multisets from [0, L), and it asserts C(L + d - 1, d) < 2^63.  At n = 4,
r = 5 (L = 70) that holds for d <= 19 and fails at d = 20 -- the 27 closing
cells with delta_close = 20 could not be built by session 60.

Here `codes_wide` keeps the int64 combinadic BIT-IDENTICALLY whenever it fits
(so every cell session 60 built gets exactly the same codes, orbits, columns
and signs), and above the wall uses a two-part code: the exact combinadics of
the first 10 entries (c1 < C(79, 10) < 2^41) and of the remaining d - 10
entries (c2 < C(69 + d - 10, d - 10) < 2^53 for d <= 25), mixed into one
uint64 by two odd multipliers.  The mixed code is a deterministic function of
the row, so an image row that IS in the basis lands on its basis copy; the
callers assert injectivity of the code on the basis (`np.all(np.diff(sorted)
> 0)`) and on every target basis, and the raising images and stabiliser images
are provably members of those bases (weight preservation), so a hash collision
can only ever show as a failed injectivity assertion, never as a wrong lookup.
The constants below are fixed; a failed assertion would be reported, not
worked around.

`install()` patches the function into wk9_s42_orbits and wk9_s45_build.
"""
import numpy as np
from math import comb

MULT1 = np.uint64(0x9E3779B97F4A7C15)
MULT2 = np.uint64(0xC2B2AE3D27D4EB4F)
SPLIT = 10


def _combinadic(M, L, k0=0):
    """exact multiset combinadic of the sorted rows M[:, k0:] (positions re-based
    at 0), as int64; the caller guarantees it fits."""
    N, d = M.shape
    code = np.zeros(N, dtype=np.int64)
    for k in range(k0, d):
        kk = k - k0
        tab = np.array([comb(m + kk, kk + 1) for m in range(L)], dtype=np.int64)
        code += tab[M[:, k]]
    return code


def codes_wide(M, L):
    N, d = M.shape
    if comb(L + d - 1, d) < (1 << 63):
        # the session-42/45 int64 path, unchanged (bit-identical)
        code = np.zeros(N, dtype=np.int64)
        for k in range(d):
            tab = np.array([comb(m + k, k + 1) for m in range(L)], dtype=np.int64)
            code += tab[M[:, k]]
        return code
    assert d > SPLIT and comb(L + SPLIT - 1, SPLIT) < (1 << 62) and comb(L + d - SPLIT - 1, d - SPLIT) < (1 << 62), (L, d)
    c1 = _combinadic(M[:, :SPLIT], L).astype(np.uint64)
    c2 = _combinadic(M, L, k0=SPLIT).astype(np.uint64)
    with np.errstate(over='ignore'):
        h = c1 * MULT1 + c2 * MULT2
    return h.view(np.int64)


def install():
    import wk9_s42_orbits, wk9_s45_build
    wk9_s42_orbits._codes = codes_wide
    wk9_s45_build._codes = codes_wide


if __name__ == '__main__':
    # self-test: bit-identity below the wall, injectivity above it on a small basis
    import sys, os
    HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
    from wk9_s42_orbits import _codes as old
    from wk9_s45_build import monomials_array
    rng = np.random.default_rng(1)
    L = 70
    for d in (5, 12, 19):
        M = np.sort(rng.integers(0, L, size=(2000, d)), axis=1).astype(np.int32)
        assert np.array_equal(old(M, L), codes_wide(M, L)), d
    print("below the wall: bit-identical at d = 5, 12, 19")
    for d in (20, 21):
        M = np.unique(np.sort(rng.integers(0, L, size=(200000, d)), axis=1), axis=0).astype(np.int32)
        c = codes_wide(M, L)
        assert len(np.unique(c)) == len(c), ("collision", d)
        print(f"above the wall: d = {d}, {len(c)} distinct rows, codes injective")
    # a real delta = 20 basis: the smallest delta_close = 20 closing cell is (57,17,2,2,2); a cheap
    # weight of the same degree first
    M = monomials_array(4, 5, 20, (72, 2, 2, 2, 2))
    c = codes_wide(M, L)
    assert len(np.unique(c)) == len(c)
    print(f"(72,2,2,2,2) d20: N_S = {M.shape[0]}, codes injective")
