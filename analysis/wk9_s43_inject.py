#!/usr/bin/env python3
"""
Session 43 -- the `a = 1` injectivity route (pre-registered in
results/PREREG_s43.md section 2, P3).

Why it exists.  Phase B's last delta = 7 weight, mu = (6,5,4,3,2,1), has trivial
stabiliser and n_chi = N_S = 39,921.  The dense in-place rref would need about
19 GB; the container has 8.  But when a(mu, delta) = 1 the question is only
whether the single highest-weight vector vanishes at the evaluation points, and
that is a rank question about a SPARSE matrix:

    mult = 1   <=>   [M ; Ev] is injective,

with M the reduced raising-operator rows and Ev the K evaluation rows in the
same chi-coordinates.  Indeed ker[M; Ev] = HWV_mu(C[W]_delta) intersected with
the functions vanishing at the K points, which for a = 1 is zero exactly when
the highest-weight vector survives.  Full column rank over F_p forces full
column rank over Q (rank_p <= rank_Q), so a certificate here proves mult = a in
the same one-sided direction as every other "empty" verdict in the programme.

The certificate is session 42's sparse Wiedemann tool (analysis/wk9_s42_wied.c):
for the matrix F it forms M = D2 F^T D1 F D2 and reports NONSINGULAR only when a
Berlekamp-Massey minimal polynomial of the Wiedemann sequence has degree exactly
n_chi with f(0) != 0, which proves M nonsingular and hence F injective with no
randomness in the implication.  A reported KERNEL vector is verified here, mod p,
against E itself.  Memory is O(nnz), not O(n_chi^2).

usage:
  python3 wk9_s43_inject.py --validate            # the gate: three banked a=1 weights
  python3 wk9_s43_inject.py --one <delta> <mu>    # one weight, both primes
"""
import sys, os, json, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import numpy as np
from scipy import sparse
from wk9_s36_stabred import orbit_setup, reduced_rows, point_rows, monomials, P1, P2, log
from wk8_s30_core import per_form
from wk8_s30_pleth import a_of
import wk9_s42_sparse as SP

PER3, N_PER = per_form(3)
os.environ.setdefault('WIED_WORK', '/root/s43/wied')
SP.WORK = os.environ['WIED_WORK']
SP.WIED = os.environ.get('WIED_BIN', '/root/s43/wied_bin')


def vm_hwm():
    for ln in open('/proc/self/status'):
        if ln.startswith('VmHWM'):
            return int(ln.split()[1]) / 1048576.0
    return 0.0


def check_kernel_modp(E, p, y):
    """E y == 0 mod p, done in mod-p arithmetic (E already reduced mod p)."""
    yv = np.array(y, dtype=np.int64) % p
    lo = yv & 0xFFFF
    hi = yv >> 16
    r = ((E @ lo) % p + ((E @ hi) % p) % p * 65536) % p
    return not np.any(r)


def inject_one(delta, mu, a_exp, K=None, seed=41, bound=40, primes=(P1, P2), verbose=True):
    """mult of I(D_6^{per_3}) at (mu, delta) by the injectivity certificate; a must be 1."""
    assert a_exp == 1, "the injectivity route is pre-registered for a = 1 only"
    n, r = 3, 6
    t0 = time.time()
    SP.build_bin()
    os.makedirs(SP.WORK, exist_ok=True)
    basis, vecs, group = orbit_setup(n, r, delta, mu, verbose=False)
    nchi = len(vecs)
    rows, nfx = reduced_rows(n, r, delta, mu, vecs, verbose=False)
    K = K if K else a_exp + 8
    if verbose:
        log(f"  {mu} d={delta}: n_chi={nchi} N_S={len(basis)} stab={len(group)} rows={len(rows)}")
    Msp = SP.rows_to_csr(rows, nchi)
    del rows
    out = {}
    for p in primes:
        ev = point_rows(PER3, N_PER, n, r, basis, vecs, K, seed, bound, p)
        Ed = sparse.csr_matrix(np.array(ev, dtype=np.int64) % p)
        Mp = Msp.copy()
        Mp.data = Mp.data % p
        E = sparse.vstack([Mp, Ed], format='csr')
        E.eliminate_zeros()
        path = os.path.join(SP.WORK, f'inj_{delta}_{"_".join(map(str,mu))}_{p}.csr')
        nrows, nnz = SP.write_csr_mat(E, p, path)
        if verbose:
            log(f"   p={p}: [M;Ev] {nrows}x{nchi}, nnz {nnz}; wiedemann ...")
        st, payload, diag = SP.run_wied(path, p, 1, 0)
        tries = 0
        while st == 'INCONCLUSIVE' and tries < 6:
            tries += 1
            st, payload, diag = SP.run_wied(path, p, 1 + tries, 0)
        os.remove(path)
        if verbose:
            log(f"   p={p}: {st} {' | '.join(diag[-2:])} ({time.time()-t0:.0f}s)")
        if st == 'NONSINGULAR':
            out[p] = 1
        elif st == 'KERNEL':
            y = payload
            assert len(y) == nchi
            assert check_kernel_modp(E, p, y), "reported kernel vector fails E y = 0"
            out[p] = 0
        else:
            raise RuntimeError(("injectivity route inconclusive", mu, delta, p, diag[-3:]))
        del E, Ed, ev, Mp
    assert out[primes[0]] == out[primes[1]], ("primes disagree", mu, out)
    monomials.cache_clear()
    return dict(lam=list(mu), delta=delta, a=a_exp, N_S=len(basis), stab=len(group), n_chi=nchi,
                nrows=len(basis) and nrows, mult=out[primes[0]], npts=K, route='inject',
                secs=time.time() - t0, hwm=vm_hwm())


VALIDATION = [(7, (8, 4, 4, 2, 2, 1)), (7, (7, 6, 4, 2, 1, 1)), (7, (6, 5, 5, 3, 1, 1))]


def validate():
    """the pre-registered gate: three already-measured a = 1 weights of the same
    family, whose dense verdict is mult = 1 in results/s41_per6.md."""
    ok = True
    for delta, mu in VALIDATION:
        a = a_of(mu, delta, 3, 6)
        assert a == 1, (mu, a)
        res = inject_one(delta, mu, a)
        good = res['mult'] == 1
        ok = ok and good
        log(f"VALIDATE {mu} d={delta}: injectivity route mult={res['mult']}, dense route (s41_per6) mult=1 "
            f"-> {'agree' if good else 'DISAGREE'} ({res['secs']:.0f}s, HWM {res['hwm']:.2f} GB)")
        print("VALRESULT " + json.dumps(res), flush=True)
    log("injectivity validation: " + ("PASSED" if ok else "FAILED"))
    return ok


if __name__ == '__main__':
    if '--validate' in sys.argv:
        sys.exit(0 if validate() else 1)
    i = sys.argv.index('--one')
    delta = int(sys.argv[i + 1]); mu = tuple(int(x) for x in sys.argv[i + 2].split(','))
    a = a_of(mu, delta, 3, 6)
    res = inject_one(delta, mu, a)
    print("RESULT " + json.dumps(res), flush=True)
