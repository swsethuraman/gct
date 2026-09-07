#!/usr/bin/env python3
"""
Session 63 -- the n = 3 LMR positive control, the programme's first rank drop.

Cell  lambda = (19,7,2^5), delta = 12, n = 3 (cubics, det_3), r = 7.
a = 6 (LMR's own value at n=3), and the LMR module is non-vacuous, so i_det >= 1
there and the determinant multiplicity MUST come back

    mult_det = rank G <= 5,   NOT 6.

Every cell the programme has ever measured has mult_det = a (full rank); this is
the one cell below LMR where a drop is guaranteed by theorem, so it is the
mandatory calibration that shows the HWV/evaluation instrument can SEE the LMR
phenomenon at all (docs/lmr_cell.md 3b, docs/s58_review.md 4, both integrator
notes).  It is n = 3, so it does not test the r = 9 wall -- it tests the method.

    mult_det = a - nullity_Q[E; ev_det],   E the raising operators on the
    chi_lambda reduction (wk9_s45_build.build_cell, n=3), ev_det evaluation rows
    at K = a + 8 random det_3 pencils; mult_det = rank(EVd @ kern^T), kern the
    a-dim HWV kernel.  rank_p <= rank_Q, and BOTH house primes are run: an
    agreeing rank r0 gives mult_det <= r0 over Q; a full-rank G at either prime
    would REFUTE the LMR non-vacuity and is a STOP-EVERYTHING event.

usage: python3 analysis/wk10_s63_n3control.py [--seed 20260907] [--bound 40] [--certs DIR]
"""
import sys, os, time, json, random, gzip
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.normpath(os.path.join(HERE, '..'))
os.environ.setdefault('WIED_BIN', '/root/wied60')
os.environ.setdefault('WIED_WORK', '/root/s63work')
import numpy as np
from scipy import sparse
from flint import nmod_mat
from wk8_s30_core import exps, restrict, det_form
from wk9_s45_build import build_cell, _grouping
from wk9_s45_cell import nullity_stacked, LEVELS, check_kernel_full

P1, P2 = 2147483647, 2147483629
N3 = 3
R = 7
LAM = (19, 7, 2, 2, 2, 2, 2)
DELTA = 12
DET3, N_DET3 = det_form(3)     # 3x3 determinant as a form in 9 entry-variables


def log(*a):
    print(*a, file=sys.stderr); sys.stderr.flush()


def det3_pencils(K, seed, bound):
    rnd = random.Random(seed)
    out = []
    for _ in range(K):
        out.append([[[rnd.randint(-bound, bound) for _ in range(3)] for _ in range(3)] for _ in range(R)])
    return out


def det3_coeffs(pencil):
    """coefficient dict {alpha (|alpha|=3, in N^7): coeff} of det_3(sum_i s_i A_i)."""
    As = [[pencil[i][a][b] for a in range(3) for b in range(3)] for i in range(R)]
    return restrict(DET3, N_DET3, N3, R, As)


def ev_rows_from_coeffs(arr, coeff_dicts, prime, n=N3, r=R, chunk=2_000_000):
    """chi-coordinate evaluation rows from coefficient dicts (the wk9_s60_cell
    kernel, n-agnostic)."""
    A = exps(n, r); L = len(A)
    M = arr['M']; sgn = arr['sgn']; n_chi = arr['n_chi']
    mem, starts = _grouping(arr)
    out = []
    for co in coeff_dicts:
        cv = np.zeros(L, dtype=np.int64)
        for a, al in enumerate(A):
            cv[a] = co.get(al, 0) % prime
        row = np.zeros(n_chi, dtype=np.int64)
        for b0 in range(0, len(mem), chunk):
            mm = mem[b0:b0 + chunk]
            term = cv[M[mm, 0]].copy()
            for k in range(1, M.shape[1]):
                term *= cv[M[mm, k]]; term %= prime
            term *= sgn[mm]; term %= prime
            s0 = np.searchsorted(starts, b0, side='right') - 1
            s1 = np.searchsorted(starts, b0 + len(mm), side='left')
            loc = np.maximum(starts[s0:s1] - b0, 0)
            np.add.at(row, np.arange(s0, s1), np.add.reduceat(term, loc) % prime)
            del term, mm, loc
        out.append((row % prime).astype(np.int64))
    return np.array(out, dtype=np.int64).reshape(len(coeff_dicts), n_chi)


def kernel_vecs(E, n_chi, a, p, seed=20260907):
    """the a-dim kernel of E mod p as an (a x n_chi) int64 array (flint nullspace,
    dense direct or one-shot chunked random compression)."""
    Em = sparse.csr_matrix(E); nrows = Em.shape[0]
    CAP = 120_000_000
    if nrows * n_chi <= CAP:
        D = np.zeros((nrows, n_chi), dtype=np.int64)
        coo = Em.tocoo(); D[coo.row, coo.col] = coo.data % p
        Mf = nmod_mat(nrows, n_chi, D.ravel().tolist(), p); del D
    else:
        rs = n_chi + 64; rng = np.random.default_rng(seed)
        C = np.zeros((rs, n_chi), dtype=np.int64); blk = max(1, 40_000_000 // n_chi)
        for b0 in range(0, nrows, blk):
            b1 = min(b0 + blk, nrows)
            Rblk = rng.integers(1, p, (rs, b1 - b0), dtype=np.int64)
            C = (C + (Rblk @ Em[b0:b1])) % p
        Mf = nmod_mat(rs, n_chi, np.ascontiguousarray(C).ravel().tolist(), p); del C
    X, nul = Mf.nullspace()
    K = np.array([[int(X[i, j]) for i in range(n_chi)] for j in range(nul)], dtype=np.int64).reshape(nul, n_chi)
    return K, nul


def rank_mod_p(Mat, p):
    Mat = np.asarray(Mat, dtype=np.int64) % p
    if Mat.size == 0: return 0
    return nmod_mat(Mat.shape[0], Mat.shape[1], Mat.ravel().tolist(), p).rank()


def main():
    args = sys.argv[1:]
    def arg(name, d):
        return type(d)(args[args.index(name) + 1]) if name in args else d
    seed = arg('--seed', 20260907); bound = arg('--bound', 40); certs = arg('--certs', '')
    t0 = time.time()
    log(f"[n=3 control] lam={LAM} delta={DELTA} n=3 r={R}")
    import pickle
    os.makedirs('/root/s63work', exist_ok=True)
    cache = '/root/s63work/n3_build.pkl'
    if os.path.exists(cache):
        B = pickle.load(open(cache, 'rb')); log(f"  loaded cached build (n_chi={B['n_chi']})")
    else:
        B = build_cell(LAM, DELTA, n=N3, verbose=True)
        pickle.dump(B, open(cache, 'wb'))
    n_chi = B['n_chi']
    log(f"  built: N_S={B['N_S']} |Stab|={B['stab']} n_chi={n_chi} nrows={B['nrows']} nnz={B['nnz']} ({B['build_secs']:.0f}s)")
    K = 6 + 8
    pencils = det3_pencils(K, seed, bound)
    coeff_dicts = [det3_coeffs(p) for p in pencils]
    res = dict(cell=dict(n=3, r=R, lam=list(LAM), delta=DELTA), a=6, n_chi=int(n_chi),
               seed=seed, bound=bound, K=K, per_prime={}, build_secs=round(B['build_secs'], 1),
               instrument='mult_det = a - nullity[E; ev_det], sparse Wiedemann (wk9_s45_cell.nullity_stacked)')
    idet = {}
    kern_p = {}
    for p in (P1, P2):
        tk = time.time()
        EVd = ev_rows_from_coeffs(B['arr'], coeff_dicts, p)      # K x n_chi (dense rows)
        EVs = sparse.csr_matrix(EVd % p)
        k, kern, lvl, diag = nullity_stacked(B['E'], EVs, n_chi, p, want_kern=True,
                                             seed0=1, tag=f'n3ctrl_{p}', levels=LEVELS['cheap'], verbose=True)
        idet[p] = int(k); kern_p[p] = kern
        res['per_prime'][str(p)] = dict(i_det=int(k), mult_det=int(6 - k), level=int(lvl),
                                        secs=round(time.time() - tk, 1))
        log(f"  p={p}: nullity[E;ev_det]=i_det={k}  mult_det={6-k}  ({time.time()-tk:.0f}s)")
    agree = idet[P1] == idet[P2]
    res['primes_agree'] = agree
    res['i_det'] = idet[P1] if agree else None
    res['mult_det'] = (6 - idet[P1]) if agree else None
    res['rank_drop'] = bool(agree and idet[P1] >= 1)
    res['verdict'] = ('POSITIVE CONTROL PASSED: rank drop, i_det=%d >= 1, mult_det=%d <= 5' % (idet[P1], 6 - idet[P1])) if res['rank_drop'] \
        else ('*** i_det=0 (mult_det=6, FULL RANK) -- REFUTES LMR non-vacuity, STOP ***' if agree else '*** PRIMES DISAGREE ***')
    res['secs'] = round(time.time() - t0, 1)
    log("  " + res['verdict'])
    # preserve U_D = ker T_det = the i_det ideal HWV(s) in source (chi) coordinates
    if agree and idet[P1] >= 1 and kern_p[P1]:
        kv = np.array(kern_p[P1], dtype=np.int64)
        os.makedirs(os.path.join(ROOT, 'results', 'artefacts'), exist_ok=True)
        np.savez_compressed(os.path.join(ROOT, 'results', 'artefacts', 's63_n3_ideal_vectors.npz'),
                            kernel=kv, prime=P1, a=6, i_det=idet[P1], mult_det=6 - idet[P1],
                            lam=np.array(LAM), delta=DELTA, n_chi=n_chi)
        res['ideal_dim_i_det'] = int(idet[P1])
        log(f"  U_D = {idet[P1]} ideal HWV(s) preserved (results/artefacts/s63_n3_ideal_vectors.npz)")
    os.makedirs(os.path.join(ROOT, 'results'), exist_ok=True)
    json.dump(res, open(os.path.join(ROOT, 'results', 's63_n3control.json'), 'w'), indent=1)
    print("RESULT " + json.dumps({k: v for k, v in res.items() if k != 'per_prime'}))
    return 0 if res['rank_drop'] else 1


if __name__ == '__main__':
    sys.exit(main())
