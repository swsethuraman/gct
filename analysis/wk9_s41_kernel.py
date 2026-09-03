#!/usr/bin/env python3
"""
Session 41 -- the in-place kernel route, and the cell driver that uses it.

Everything up to the kernel is wk9_s36_stabred.py unchanged (isotypic basis,
every simple raising operator restricted to V_chi, H-orbit row dedup with the
chi-obstructed rows asserted to cancel, the certified random compression
Agg = P.M of docs/e4_hunt.md section 4).  What changes is only how the kernel
of the square-ish Agg is taken:

    inherited ('compressed'):  flint nullspace()  -> ~3 copies of Agg resident
                                (matrix, its rref, the n x n nullspace buffer);
                                s36's frontier n_chi ~ 15500 on this container.
    this session ('inplace'):  flint rref(inplace=True) -> ~1.7 copies resident
                                (measured: +0.76 / +0.62 copies at n = 4000 /
                                8000 against +2.04 / +1.96 for nullspace);
                                kernel read off the rref: pivot columns are
                                found by scanning at most a+1 entries per row,
                                one kernel vector per free column f
                                (v[f] = 1, v[pivot(i)] = -rref[i, f]).

Certificate (unchanged): rank(Agg) <= rank_p(M) <= rank_Q(M) = n_chi - a(pleth);
the assert n_chi - rank(Agg) = a forces equality throughout, so ker(Agg) =
ker_p(M).  ADDED: every kernel vector is multiplied against the uncompressed
sparse rows of all simple raising operators and asserted to vanish mod p -- an
exact certificate that the exhibited vectors are highest-weight vectors mod p,
independent of the compression.

Validation (results/PREREG_s41.md P1): identical kernel span to the exact and
compressed routes on the s36 validation cells and on three banked ell = 6 cells.
"""
import sys, os, time, random, pickle
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import numpy as np
from scipy import sparse
from flint import nmod_mat
from wk9_s36_stabred import (orbit_setup, reduced_rows, kernel_exact, kernel_compressed,
                             point_rows, mult_from, expand, monomials, exps,
                             DET4, N_DET, PAD34, N_PAD, P1, P2, log)

def vm_hwm():
    for ln in open('/proc/self/status'):
        if ln.startswith('VmHWM'): return int(ln.split()[1]) / 1048576.0
    return 0.0

def sparse_M(rows, nchi):
    ri = np.fromiter((r for r, d in enumerate(rows) for _ in d), dtype=np.int64)
    ci = np.fromiter((c for d in rows for c in d), dtype=np.int64)
    vv = np.fromiter((v for d in rows for v in d.values()), dtype=np.int64)
    return sparse.csr_matrix((vv, (ri, ci)), shape=(len(rows), nchi), dtype=np.int64)

def verify_kernel(Msp, kern, prime):
    """assert M v = 0 mod p for every kernel vector, using the UNCOMPRESSED rows."""
    maxabs = int(np.abs(Msp.data).max()) if Msp.nnz else 0
    rowfill = int(np.diff(Msp.indptr).max()) if Msp.nnz else 0
    assert maxabs * (prime - 1) * rowfill < (1 << 62), ("int64 bound", maxabs, rowfill)
    for kv in kern:
        v = np.array([x % prime for x in kv], dtype=np.int64)
        res = (Msp @ v) % prime
        assert not res.any(), "kernel vector fails M v = 0 on the uncompressed rows"

def kernel_inplace(rows, nchi, prime, margin=64, pseed=101, chunk=64, Msp=None):
    """Agg = P.M assembled as in kernel_compressed (chunks of `chunk` Agg rows),
    then ONE flint rref in place; kernel from the pivot structure."""
    t0 = time.time()
    nrows = len(rows)
    rs = nchi + margin
    MT = Msp.T.tocsr() if Msp is not None else sparse_M(rows, nchi).T.tocsr()
    vv = MT.data
    maxabs = int(np.abs(vv).max())
    colfill = int(np.diff(MT.indptr).max())
    assert maxabs * (prime - 1) * colfill < (1 << 62), ("int64 bound", maxabs, colfill)
    rng = np.random.default_rng(pseed * 1000003 + prime % 1000003 + nchi)
    M = nmod_mat(rs, nchi, prime)
    for k0 in range(0, rs, chunk):
        cs = min(chunk, rs - k0)
        Pc = rng.integers(0, prime, (nrows, cs), dtype=np.int64)
        C = (MT @ Pc) % prime
        del Pc
        CT = np.ascontiguousarray(C.T); del C
        for k in range(cs):
            rl = CT[k].tolist()
            for j, v in enumerate(rl):
                if v: M[k0 + k, j] = v
        del CT
    del MT
    log(f"    Agg {rs}x{nchi} assembled into flint ({time.time()-t0:.0f}s; nrows {nrows}, "
        f"max|M| {maxabs}, max column fill {colfill}); rref in place ...")
    R, rk = M.rref(inplace=True)
    nul = nchi - rk
    log(f"    rref: rank {rk}, dim ker {nul} ({time.time()-t0:.0f}s); reading pivots ...")
    # pivot columns: row i's pivot lies in [i, i + nul] (only nul free columns exist)
    piv = []
    free = []
    j = 0
    for i in range(rk):
        while int(M[i, j]) == 0:
            free.append(j); j += 1
            assert j < nchi, "pivot scan overran"
        assert int(M[i, j]) == 1, ("rref pivot not 1", i, j)
        piv.append(j); j += 1
    free += list(range(j, nchi))
    assert len(free) == nul and len(piv) == rk
    kern = []
    for f in free:
        v = [0] * nchi
        v[f] = 1
        for i, c in enumerate(piv):
            x = int(M[i, f])
            if x: v[c] = (-x) % prime
        kern.append(v)
    del M, R
    log(f"    kernel: {nul} vectors ({time.time()-t0:.0f}s)")
    return nul, rk, kern

def measure_cell(n, r, delta, lam, a_expect, sides=('det', 'pad'), primes=(P1, P2),
                 npts=None, seeds=None, bound=40, route='inplace', pseed=101,
                 exact_cap=2500, verify=True, verbose=True):
    """One cell, s36 semantics (wk9_s36_stabred.measure_reduced) with the kernel
    route selectable: 'exact' | 'compressed' | 'inplace' | 'auto'
    ('auto' = exact below exact_cap, else inplace)."""
    t0 = time.time()
    lam = tuple(lam) + (0,) * (r - len(lam))
    basis, vecs, group = orbit_setup(n, r, delta, lam, verbose)
    nchi = len(vecs)
    rows, nfx = reduced_rows(n, r, delta, lam, vecs, verbose)
    out = dict(lam=lam, delta=delta, N_S=len(basis), stab=len(group), n_chi=nchi,
               nrows=len(rows), per_prime={}, hwm_before=vm_hwm())
    if route == 'auto':
        route = 'exact' if nchi <= exact_cap else 'inplace'
    out['route'] = route
    Msp = sparse_M(rows, nchi) if (verify or route == 'inplace') else None
    if seeds is None: seeds = dict(det=11, pad=29)
    forms = dict(det=(DET4, N_DET), pad=(PAD34, N_PAD))
    K = npts if npts else a_expect + 8
    for prime in primes:
        if route == 'exact':
            a, rk, kern = kernel_exact(rows, nchi, prime)
        elif route == 'compressed':
            a, rk, kern = kernel_compressed(rows, nchi, prime, pseed=pseed)
            if a != a_expect:
                log(f"    compressed certificate missed ({a} != {a_expect}); retry pseed")
                a, rk, kern = kernel_compressed(rows, nchi, prime, pseed=pseed + 1)
        else:
            a, rk, kern = kernel_inplace(rows, nchi, prime, pseed=pseed, Msp=Msp)
            if a != a_expect:
                log(f"    in-place certificate missed ({a} != {a_expect}); retry pseed")
                a, rk, kern = kernel_inplace(rows, nchi, prime, pseed=pseed + 1, Msp=Msp)
        assert a == a_expect, ("a mismatch vs plethysm", lam, prime, a, a_expect)
        assert rk == nchi - a, ("rank(R) != n_chi - a", lam, prime, rk, nchi, a)
        if verify and a > 0:
            verify_kernel(Msp, kern, prime)
        res = dict(a=a, rank=rk, kern=kern, mult={})
        if a > 0:
            for sd in sides:
                f, N = forms[sd]
                ev = point_rows(f, N, n, r, basis, vecs, K, seeds[sd], bound, prime)
                res['mult'][sd] = mult_from(kern, ev, a, prime)
        else:
            for sd in sides: res['mult'][sd] = 0
        out['per_prime'][prime] = res
        if verbose:
            log(f"  p={prime}: a={a} rank(R)={rk} mult={res['mult']} npts={K} route={route} "
                f"({time.time()-t0:.0f}s, VmHWM {vm_hwm():.2f} GB)")
    for sd in sides:
        ms = {p: out['per_prime'][p]['mult'][sd] for p in primes}
        assert len(set(ms.values())) == 1, ("primes disagree", lam, sd, ms)
        out['mult_' + sd] = ms[primes[0]]
    out['a'] = a_expect
    out['npts'] = K
    out['secs'] = time.time() - t0
    out['hwm'] = vm_hwm()
    return out

def span_identical(k1, k2, a, prime):
    both = k1 + k2
    if not both: return a == 0
    rk = nmod_mat(len(both), len(both[0]), [v % prime for rw in both for v in rw], prime).rank()
    return rk == a

def mult_red_of(out):
    """point-free reducibility multiplicity by (*) — wk9_s36_red.mult_red, inline
    so the banked pickle format of this session is accepted."""
    from wk9_s36_red import is_red
    lam = out['lam']; r = len(lam); delta = out['delta']; a = out['a']
    A = exps(4, r)
    basis, vecs, group = orbit_setup(4, r, delta, lam, verbose=False)
    assert len(vecs) == out['n_chi']
    nonred = [j for j, vec in enumerate(vecs) if not is_red(next(iter(vec)), A, r)]
    res = {}
    for p in (P1, P2):
        kern = out['per_prime'][p]['kern']
        if a == 0: res[p] = 0; continue
        rows = [[kv[j] % p for j in nonred] for kv in kern]
        res[p] = nmod_mat(a, len(nonred), [v for rw in rows for v in rw], p).rank() if nonred else 0
    assert res[P1] == res[P2], (lam, res)
    monomials.cache_clear()
    return res[P1], len(nonred), len(vecs) - len(nonred)
