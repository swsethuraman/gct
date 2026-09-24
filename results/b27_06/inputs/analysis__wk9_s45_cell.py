#!/usr/bin/env python3
"""
Session 45 -- one determinant-side (or pad-side) cell by sparse certificate.

    mult_det(lam, delta) = a - dim ker [ E ; ev_1 ; ... ; ev_K ],   K = a + 8,

with E the stacked simple raising operators on the chi_lam-isotypic reduction
V_chi and ev_j the evaluation at the j-th point contracted to chi-coordinates.
Since rank_p <= rank_Q,

    a - nullity_p([E; ev])  <=  mult_det  <=  a,

so nullity_p([E; ev]) = 0 at ONE prime PROVES mult_det = a over Q.  A positive
nullity is a measurement until its kernel vectors are exhibited and verified.

The nullity is decided by the session-42 Wiedemann certificates
(analysis/wk9_s42_wied.c through analysis/wk9_s42_sparse.py, whose compress /
write_csr_mat / run_wied / check_kernel_py are used unchanged).  Two changes,
both conservative:

  * the K evaluation rows are PINNED: only the rows of E are sampled and
    grouped, and the ev rows are stacked on afterwards.  Sampling can only lose
    rank, so a nonsingularity certificate for [compress(E); ev] still proves
    [E; ev] injective; pinning avoids sampling away an evaluation row and
    manufacturing a spurious kernel;
  * the two house primes are run concurrently in forked children (2 cores), the
    build being shared copy-on-write.

Kernel candidates are verified against the FULL [E; ev] (in C by the sparse
product, and again here by scipy) before being reported, exactly as in s42.

usage: python3 wk9_s45_cell.py delta lam1 lam2 ... [--side det|pad|both]
       [--levels cheap|s42|full] [--full-check] [--kern] [--npts K] [--out FILE]
"""
import sys, os, time, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
os.environ.setdefault('WIED_BIN', '/home/claude/wied45')
os.environ.setdefault('WIED_WORK', '/home/claude/s45/work')
import numpy as np
from scipy import sparse
from flint import nmod_mat
from wk9_s42_sparse import (build_bin, compress, write_csr_mat, run_wied,
                            check_kernel_py, MAX_INCONCLUSIVE)
from wk9_s45_build import build_cell, ev_rows_arr, log, _rss_gb
from wk9_s36_stabred import DET4, N_DET, PAD34, N_PAD, P1, P2
from wk8_s30_pleth import a_of

FORMS = dict(det=(DET4, N_DET), pad=(PAD34, N_PAD))
SEEDS = dict(det=11, pad=29)
# (sample factor on the rows of E, group size).  Sampling and +-1 grouping can
# only lose rank, so a nonsingularity certificate at any level proves the full
# matrix injective; a kernel vector that fails on the full matrix escalates to
# the next level.  The last level is the uncompressed matrix.
LEVELS = dict(cheap=((3, 2), (12, 2), (None, 1)),
              s42=((12, 2), (None, 1)),
              full=((None, 1),))

def check_kernel_full(F, nc, p, y):
    """F y == 0 mod p for a scipy CSR F whose entries may be as large as p-1
    (the pinned evaluation rows are reduced mod p, unlike the tiny raw operator
    entries wk9_s42_sparse.check_kernel_py assumes).  Both sides are split into
    16-bit limbs so every partial product is < 2^32 and every row sum stays well
    inside int64."""
    F = sparse.csr_matrix(F)
    d = (F.data % p).astype(np.int64)
    Flo = sparse.csr_matrix((d & 0xFFFF, F.indices, F.indptr), shape=F.shape)
    Fhi = sparse.csr_matrix((d >> 16, F.indices, F.indptr), shape=F.shape)
    yv = np.array(y, dtype=np.int64) % p
    ylo = yv & 0xFFFF; yhi = yv >> 16
    t0 = (Flo @ ylo) % p
    t1 = ((Flo @ yhi) % p + (Fhi @ ylo) % p) % p
    t2 = (Fhi @ yhi) % p
    r = (t0 + t1 * 65536 + t2 * ((65536 * 65536) % p)) % p
    return not np.any(r)

def nullity_stacked(E, EV, nc, p, want_kern=False, seed0=1, tag='cell',
                    levels=LEVELS['cheap'], verbose=True, maxbad=MAX_INCONCLUSIVE):
    """nullity_p of F = [E; EV] with the EV rows pinned through every level.
    Returns (k, kern, level_used, diag)."""
    build_bin()
    WORK = os.environ['WIED_WORK']; os.makedirs(WORK, exist_ok=True)
    path = os.path.join(WORK, f'{tag}_{p}_{os.getpid()}.csr')
    E = sparse.csr_matrix(E); EV = sparse.csr_matrix(EV)
    assert E.shape[1] == nc and EV.shape[1] == nc
    Full = sparse.vstack([E, EV]).tocsr()
    rng = np.random.default_rng(seed0 * 7919 + p % 1000 + nc)
    kern = []; seed = seed0; bad = 0; t0 = time.time(); diag = []
    try:
        for li, (sample, group) in enumerate(levels):
            Ec = E if sample is None else compress(E, sample, group, rng)
            F = sparse.vstack([Ec, EV]).tocsr()
            nrows, nnz = write_csr_mat(F, p, path)
            if verbose:
                log(f"    level {li} ({sample},{group}): {nrows} rows, nnz {nnz} "
                    f"(full: {Full.shape[0]} rows, nnz {Full.nnz})")
            escalate = False
            while not escalate:
                st, payload, dg = run_wied(path, p, seed, len(kern))
                if verbose:
                    log(f"    wied[{tag} p={p} lvl={li} seed={seed} k={len(kern)}]: {st} "
                        f"{' | '.join(dg)} ({time.time()-t0:.0f}s)")
                diag.append(dict(level=li, seed=seed, status=st, note=' | '.join(dg),
                                 rows=int(nrows), nnz=int(nnz)))
                seed += 1
                if st == 'NONSINGULAR':
                    return len(kern), (kern if want_kern else None), li, diag
                if st == 'KERNEL':
                    y = payload
                    assert len(y) == nc
                    chk = check_kernel_py if int(np.abs(Full.data).max(initial=0)) < 65536 else check_kernel_full
                    if not chk(Full, nc, p, y):
                        if verbose: log("    (kernel vector of the compressed matrix is not in ker[E; ev]: escalate)")
                        escalate = True; continue
                    cand = kern + [y]
                    rk = nmod_mat(len(cand), nc, [v for vec in cand for v in vec], p).rank()
                    if rk == len(cand): kern.append(y)
                    else:
                        bad += 1
                        if verbose: log("    (dependent kernel vector; retry)")
                else:
                    bad += 1
                if bad > maxbad:
                    raise RuntimeError(("sparse route inconclusive", tag, p, len(kern), bad))
        raise RuntimeError(("sparse route: escalation exhausted", tag, p, len(kern)))
    finally:
        try: os.remove(path)
        except OSError: pass

# --------------------------------------------------------------- the cell
_SHARED = {}

def _prime_job(args):
    side, p, K, bound, levels, want_kern, seed0, tag, full_check, a = args
    B = _SHARED['B']; arr = B['arr']; E = B['E']; nc = B['n_chi']
    r = B['r']; n = 4
    out = dict(side=side, prime=p)
    t0 = time.time()
    if full_check:
        kE, _, lvE, _ = nullity_stacked(E, sparse.csr_matrix((0, nc), dtype=np.int64), nc, p,
                                        seed0=seed0 + 500, tag=tag + '_fullE', levels=levels,
                                        verbose=True)
        assert kE == a, ("nullity_p(E) != a (plethysm)", B['lam'], B['delta'], p, kE, a)
        out['full_E_nullity'] = kE
        log(f"  p={p}: full-E nullity {kE} = a (plethysm) [level {lvE}]")
    f, N = FORMS[side]
    t_ev = time.time()
    EV = ev_rows_arr(f, N, n, r, arr, K, SEEDS[side], bound, p)
    out['ev_secs'] = round(time.time() - t_ev, 1)
    k, kern, lvl, diag = nullity_stacked(E, sparse.csr_matrix(EV), nc, p,
                                         want_kern=want_kern, seed0=seed0,
                                         tag=tag + '_' + side, levels=levels)
    out.update(nullity=k, level=lvl, diag=diag, secs=round(time.time() - t0, 1))
    if want_kern and kern: out['kern'] = kern
    return out

def measure_cell(lam, delta, sides=('det',), primes=(P1, P2), npts=None, bound=40,
                 levels=LEVELS['cheap'], full_check=False, want_kern=False,
                 parallel=True, verbose=True, seed0=1):
    lam = tuple(lam); r = len(lam); n = 4
    t0 = time.time()
    B = build_cell(lam, delta, n=n, verbose=verbose)
    a = a_of(lam, delta, n, r)
    K = npts if npts else a + 8
    tag = 'c' + '_'.join(map(str, lam)) + f'd{delta}'
    out = dict(lam=list(lam), delta=delta, ell=r, a=a, K=K, N_S=B['N_S'], stab=B['stab'],
               n_chi=B['n_chi'], nrows=B['nrows'], nnz=B['nnz'], nfixed=B['nfixed'],
               build_secs=round(B['build_secs'], 1), mono_secs=round(B['mono_secs'], 1),
               orbit_secs=round(B['orbit_secs'], 1), rows_secs=round(B['rows_secs'], 1),
               build_hwm_gb=round(B['hwm_gb'], 2), sides={})
    if a == 0:
        out.update(status='a=0', secs=round(time.time() - t0, 1)); return out
    _SHARED['B'] = B
    jobs = [(sd, p, K, bound, levels, want_kern, seed0, tag, full_check and p == primes[0], a)
            for sd in sides for p in primes]
    if parallel and len(jobs) > 1:
        import multiprocessing as mp
        with mp.get_context('fork').Pool(min(2, len(jobs))) as pool:
            res = pool.map(_prime_job, jobs)
    else:
        res = [_prime_job(j) for j in jobs]
    for sd in sides:
        rs = [x for x in res if x['side'] == sd]
        ks = {x['prime']: x['nullity'] for x in rs}
        assert len(set(ks.values())) == 1, ("primes disagree on nullity", lam, delta, sd, ks)
        k = rs[0]['nullity']
        out['sides'][sd] = dict(
            nullity=k, mult=a - k,
            status=('proved (nullity 0 at %d)' % rs[0]['prime']) if k == 0
                   else 'measured (nullity %d, two primes); mult >= %d proved' % (k, a - k),
            per_prime={str(x['prime']): {kk: vv for kk, vv in x.items()
                                          if kk not in ('kern', 'side', 'prime')} for x in rs})
        if want_kern:
            for x in rs:
                if 'kern' in x: out['sides'][sd].setdefault('kern', {})[str(x['prime'])] = x['kern']
        out['mult_' + sd] = a - k
        if verbose:
            log(f"  {lam} d{delta} [{sd}]: nullity = {k} -> mult_{sd} = {a-k}"
                + (" = a PROVED" if k == 0 else "") + f"  ({time.time()-t0:.0f}s)")
    if 'full_E_nullity' in res[0]: out['full_E_nullity'] = res[0]['full_E_nullity']
    out['secs'] = round(time.time() - t0, 1)
    out['hwm_gb'] = round(_rss_gb(), 2)
    _SHARED.clear()
    return out

if __name__ == '__main__':
    args = sys.argv[1:]
    sides = ('det',); lv = 'cheap'; full = False; kern = False; outp = None; npts = None
    pos = []; i = 0
    while i < len(args):
        if args[i] == '--side':
            sides = ('det', 'pad') if args[i + 1] == 'both' else (args[i + 1],); i += 2
        elif args[i] == '--levels': lv = args[i + 1]; i += 2
        elif args[i] == '--npts': npts = int(args[i + 1]); i += 2
        elif args[i] == '--out': outp = args[i + 1]; i += 2
        elif args[i] == '--full-check': full = True; i += 1
        elif args[i] == '--kern': kern = True; i += 1
        else: pos.append(int(args[i])); i += 1
    delta, lam = pos[0], tuple(pos[1:])
    res = measure_cell(lam, delta, sides=sides, levels=LEVELS[lv], full_check=full,
                       want_kern=kern, npts=npts)
    kv = {}
    for sd in res.get('sides', {}):
        if 'kern' in res['sides'][sd]: kv[sd] = res['sides'][sd].pop('kern')
    print(json.dumps(res))
    if outp:
        with open(outp, 'a') as f: f.write(json.dumps(res) + "\n")
    if kv:
        import pickle
        os.makedirs('/home/claude/s45', exist_ok=True)
        pickle.dump(dict(res=res, kern=kv),
                    open(f"/home/claude/s45/kern_{'_'.join(map(str, lam))}_d{delta}.pkl", 'wb'))
