#!/usr/bin/env python3
"""
B28-01 -- determinant-only driver for the blocked triangular-cover/Schur hybrid.

Adapted from analysis/wk12_s79_cell6.py (session 79) on the unchanged committed
engine (analysis/wk11_s71_hybrid.py + analysis/wk11_s71_schur.c, builder
analysis/wk9_s45_build.py, codes analysis/wk11_s71_codes.py), as B27-06's
PREREGISTRATION.md specifies:

  * determinant family only (pad / per4 / reducible families and their
    allocations removed);
  * session 79's fixes kept: X blocks sized by S71_MEM_X (= 250 MB here, the
    engine's 32-column minimum accounted for), evaluation in batches of at most
    eight points, candidate combinations from nullspace(VK) (never VK^T);
  * build-and-cover gate: after E and the cover, the remaining producer +
    verifier work is repriced with the phase model and the job stops (exit 3)
    before any Schur allocation if it does not fit the unused budget, or if the
    memory envelope exceeds 75% of the job cap;
  * one projection attempt per prime (a failed source gate is inconclusive,
    never retried with another seed);
  * the exact arithmetic bounds of the engine are asserted (matmul_mod's
    inner dimension < 2^21, |E| < 2^16 in check_kernel_mat, p < 2^31 in C);
  * integer pencils (bound 40, seed 11, a+8 of them, the same across primes)
    are serialized, so replay never depends on the PRNG;
  * primes 2147483647 and 2147483629, strictly sequential, one BLAS thread.

Output files are deterministic (no wall times); times and memory high-water
marks go only to the receipt file.

usage: python3 b28_01_driver.py --lam 12 8 6 4 2 --delta 8 --a 109 --nchi 813314
          --primes 2147483647 2147483629 --out DIR
          [--wall-budget SECONDS] [--mem-cap BYTES] [--rates FILE] [--gate-only]
exit codes: 0 done, 3 stopped at the build-and-cover gate, 4 source gate failed.
"""
import sys, os, json, time, hashlib, argparse, math
for _v in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[_v] = '1'
ENGINE = os.environ.get('B28_ENGINE', os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ENGINE)
os.environ.setdefault('S71_SCHUR_SO', os.path.join(ENGINE, 'schur.so'))
os.environ['S71_MEM_X'] = '250000000'
import numpy as np
from flint import nmod_mat
import wk11_s71_codes; wk11_s71_codes.install()
from wk8_s30_core import P1, P2
from wk9_s45_build import build_cell
from wk9_s42_census import a_weyl
from wk12_s79_cell6 import det_pencils, det_coeffs, ev_rows_from_coeffs, SEEDS, HYB_SEED
import wk11_s71_hybrid as H

N = 4
MEM_X = 250_000_000
BASELINE_RATES = dict(cB=2.1e-6, cS=5e-7, cH=8e-8, cV=2.7e-8, cR=1e-9, cD=5e-10, verifier_factor=1.0)


# ------------------------------------------------------------------ bookkeeping
def sha(b):
    return hashlib.sha256(b).hexdigest()


def phase_reset():
    """reset VmHWM so the next reading is the peak of this phase alone."""
    try:
        with open('/proc/self/clear_refs', 'w') as f: f.write('5')
    except OSError:
        pass


def hwm_bytes():
    with open('/proc/self/status') as f:
        for line in f:
            if line.startswith('VmHWM'): return int(line.split()[1]) * 1024
    return -1


class Receipt:
    def __init__(self): self.phases = []; self.t0 = time.perf_counter()
    def start(self, name): phase_reset(); self._n = name; self._t = time.perf_counter()
    def stop(self, **extra):
        d = dict(phase=self._n, secs=round(time.perf_counter() - self._t, 3), peak_rss_bytes=hwm_bytes()); d.update(extra)
        self.phases.append(d); H.log(f"  [phase] {d}")
        return d


def csr_hash(E):
    E = E.tocsr(); E.sort_indices()
    h = hashlib.sha256()
    for arr in (E.indptr.astype('<i8'), E.indices.astype('<i8'), E.data.astype('<i8')):
        h.update(np.ascontiguousarray(arr).tobytes())
    h.update(json.dumps(list(E.shape)).encode())
    return h.hexdigest()


def phase_model(n, k, a, z, U, rates):
    r = rates; K = a + 8
    return dict(B=r['cB'] * n * k, S=r['cS'] * z, H=r['cH'] * z * U, V=r['cV'] * K * n * k,
                R=r['cR'] * K * n * a, D=r['cD'] * U ** 3)


def mem_envelope(n, a, z, U):
    return 16 * n * a + 100 * z + 400 * n + 5 * max(250_000_000, 128 * n) + 80 * U * U + 500_000_000


# ------------------------------------------------------------------ the hybrid, one attempt
def hybrid_det(E, nc, p, a, cov, rc):
    """wk11_s71_hybrid.hybrid_kernel with retries = 1 (the preregistered single
    projection attempt), X blocks under S71_MEM_X, and the projected residual's
    hash and recipe exported.  Returns (K uint32 nc x a, info)."""
    rc.start('schur')
    E = E.tocsr(); E.sort_indices()
    rows = cov['rows']; S = cov['S']; U = cov['U']
    nS, nU = len(S), len(U)
    colS = np.full(nc, -1, dtype=np.int32); colS[S] = np.arange(nS, dtype=np.int32)
    colU = np.full(nc, -1, dtype=np.int32); colU[U] = np.arange(nU, dtype=np.int32)
    T, dinv, TU = H._split_rows(E, rows, colS, colU, p)
    TUc = TU.tocsc()
    ublock = nU if 4.0 * nS * nU <= MEM_X else max(32, int(MEM_X / (4.0 * nS)))
    nblocks = (nU + ublock - 1) // ublock if nU else 0
    mask = np.ones(E.shape[0], dtype=bool); mask[rows] = False
    Fo = E[np.nonzero(mask)[0]].tocsr(); Fo.sort_indices()
    indptr = Fo.indptr.astype(np.int64); indices = Fo.indices.astype(np.int32); data = (Fo.data % p).astype(np.uint32)
    extra, nproj, attempt = 64, 8, 0
    m = nU + extra
    pseed = np.uint64((HYB_SEED + 7919 * attempt + p % 1000) % (1 << 63))
    G = np.zeros((m, nU), dtype=np.uint32)
    t_solve = t_schur = 0.0
    for b0 in range(0, nU, ublock):
        b1 = min(nU, b0 + ublock); blk = b1 - b0
        ts = time.perf_counter()
        Bb = np.ascontiguousarray((TUc[:, b0:b1].toarray().astype(np.int64) % p).astype(np.uint32))
        H.trisolve(T, dinv, Bb, p)
        t_solve += time.perf_counter() - ts; ts = time.perf_counter()
        colUb = np.full(nc, -1, dtype=np.int32); colUb[U] = -2; colUb[U[b0:b1]] = np.arange(blk, dtype=np.int32)
        Gb = np.zeros((m, blk), dtype=np.uint32)
        r = H.lib().schur_project(Fo.shape[0], H._ptr(indptr), H._ptr(indices), H._ptr(data), H._ptr(colS), H._ptr(colUb),
                                  H._ptr(Bb), blk, m, H._ptr(Gb), p, pseed, nproj)
        assert r == 0, ("schur_project", r)
        G[:, b0:b1] = Gb
        del Bb, Gb, colUb
        t_schur += time.perf_counter() - ts
    G_sha = sha(np.ascontiguousarray(G).astype('<u4').tobytes())
    tn = time.perf_counter()
    yU = H.nullspace_mod_p(G.astype(np.int64), p)                 # nullspace(G): vectors y_U with G y_U = 0
    nul = yU.shape[0]
    del G
    rc.stop(trisolve_secs=round(t_solve, 3), schur_project_secs=round(t_schur, 3), nullspace_secs=round(time.perf_counter() - tn, 3),
            nS=int(nS), nU=int(nU), ublock=int(ublock), nblocks=int(nblocks))
    rc.start('lift_check')
    Kc = np.zeros((nc, nul), dtype=np.uint32)
    ok = True
    for v0 in range(0, nul, 64):
        v1 = min(nul, v0 + 64)
        yUt = np.ascontiguousarray(yU[v0:v1].T.astype(np.uint32))
        w = H.spmm_mod(TU, yUt, p)
        w = np.ascontiguousarray(((p - w.astype(np.int64)) % p).astype(np.uint32))
        yS = H.trisolve(T, dinv, w, p)
        Kc[S, v0:v1] = yS; Kc[U, v0:v1] = yUt
        if not H.check_kernel_mat(E, Kc[:, v0:v1].astype(np.int64), p): ok = False
    rk = H.rank_tall(Kc, p) if nul else 0
    rc.stop(nullity=int(nul))
    info = dict(nS=int(nS), nU=int(nU), nnzT=int(T.nnz), rows_other=int(Fo.shape[0]), ublock=int(ublock), nblocks=int(nblocks),
                projection=dict(base_seed=HYB_SEED, attempt=attempt, pseed=int(pseed), m=int(m), extra=extra, nproj=nproj,
                                generator='wk11_s71_schur.c splitmix64, z = pseed ^ (0xD1B54A32D192ED03*(r+1)), row t = x % m, sign = (x>>40)&1'),
                G_shape=[int(m), int(nU)], G_sha256=G_sha, projected_nullity=int(nul), verified_on_all_rows=bool(ok), rank_K=int(rk))
    info['source_gate'] = bool(ok and nul == a and rk == a)
    return Kc, info


# ------------------------------------------------------------------ evaluation
def minor_rows(VK, p):
    """row indices of a nonzero a x a minor of VK (pivot columns of rref(VK^T)), or None."""
    npts, a = VK.shape
    M = nmod_mat(a, npts, (VK.T % p).astype(np.int64).ravel().tolist(), p)
    Rm, rk = M.rref()
    piv = []
    for i in range(rk):
        for j in range(npts):
            if int(Rm[i, j]) != 0: piv.append(j); break
    return piv, rk


def evaluate(arr, K, pts, R, p, a, rc):
    rc.start('evaluation')
    Kp_ = np.asarray(K % p, dtype=np.int64)
    assert Kp_.shape[0] < (1 << 21)                                 # matmul_mod's exact-limb bound (asserted again inside)
    cl = [det_coeffs(pt, R) for pt in pts]
    parts = []
    for c0 in range(0, len(cl), 8):
        EV = ev_rows_from_coeffs(arr, cl[c0:c0 + 8], p, R)
        parts.append(H.matmul_mod(EV % p, Kp_, p)); del EV
    del Kp_
    VK = np.vstack(parts) % p
    mult = H.rank_mod_p(VK, p)
    piv, rk = minor_rows(VK, p)
    assert rk == mult
    out = dict(mult_det=int(mult), VK_shape=list(VK.shape), VK_sha256=sha(np.ascontiguousarray(VK.astype('<u4')).tobytes()))
    if mult == a:
        sub = VK[piv]
        d = nmod_mat(a, a, sub.astype(np.int64).ravel().tolist(), p).det()
        assert int(d) != 0
        out['minor_rows'] = [int(x) for x in piv]; out['minor_det_mod_p'] = int(d)
    rc.stop(npts=len(pts))
    return VK, out


# ------------------------------------------------------------------ the cell
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lam', type=int, nargs='+', required=True)
    ap.add_argument('--delta', type=int, required=True)
    ap.add_argument('--a', type=int, required=True)
    ap.add_argument('--nchi', type=int, required=True)
    ap.add_argument('--primes', type=int, nargs='+', default=[P1, P2])
    ap.add_argument('--out', required=True)
    ap.add_argument('--wall-budget', type=float, default=float('inf'), help='unused wall seconds for producer + verifier')
    ap.add_argument('--mem-cap', type=float, default=float('inf'), help='job memory cap in bytes')
    ap.add_argument('--rates', default='', help='JSON phase-rate coefficients (default: preregistered baseline)')
    ap.add_argument('--gate-only', action='store_true')
    ap.add_argument('--bound', type=int, default=40)
    args = ap.parse_args()
    lam = tuple(args.lam); delta = args.delta; R = len(lam)
    assert all(p in (P1, P2) for p in args.primes)
    os.makedirs(args.out, exist_ok=True)
    tag = '_'.join(map(str, lam)) + f'_d{delta}'
    rc = Receipt(); t_job = time.perf_counter()
    rates = dict(BASELINE_RATES)
    if args.rates:
        rates.update(json.load(open(args.rates)))

    rc.start('build')
    B = build_cell(lam, delta, n=N, verbose=True)
    a = a_weyl(lam, delta, N, {})
    assert a == args.a, ('a (Weyl alternation) disagrees with the frozen value', a, args.a)
    nc = B['n_chi']; E = B['E'].tocsr(); E.sort_indices()
    assert nc == args.nchi, ('n_chi disagrees with the frozen value', nc, args.nchi)
    assert int(np.abs(E.data).max()) < 65536
    csr_bytes = int(E.data.nbytes + E.indices.nbytes + E.indptr.nbytes)
    rc.stop()
    cell = dict(schema='b28-01-cell/1', lam=list(lam), delta=delta, R=R, a=a, N_S=int(B['N_S']), stab=int(B['stab']), n_chi=int(nc),
                rows_E=int(E.shape[0]), nnz_E=int(E.nnz), E_dtypes=dict(data=str(E.data.dtype), indices=str(E.indices.dtype), indptr=str(E.indptr.dtype)),
                E_csr_bytes=csr_bytes, E_sha256=csr_hash(E), E_hash_convention='sha256(indptr,indices,data as <i8, then json shape), sorted indices',
                conventions={"coefficient": "c_alpha(F) = coefficient of s^alpha in F", "raising": "E_ij c_alpha = (alpha_i + 1) c_{alpha + e_i - e_j}"})

    rc.start('cover')
    cov = H.best_cover(E, nc, seed=HYB_SEED)
    nU = int(len(cov['U']))
    rc.stop(cover_size=int(cov['size']), nU=nU)
    for nm, arrv in (('S', cov['S']), ('U', cov['U']), ('rows', cov['rows'])):
        np.save(os.path.join(args.out, f'{tag}_cover_{nm}.npy'), np.asarray(arrv, dtype='<i8'))
    cell['cover'] = dict(order=cov['order'], stats=cov['stats'], size=int(cov['size']), nU=nU, excess=int(nU - a),
                         S_sha256=sha(np.asarray(cov['S'], dtype='<i8').tobytes()), U_sha256=sha(np.asarray(cov['U'], dtype='<i8').tobytes()),
                         rows_sha256=sha(np.asarray(cov['rows'], dtype='<i8').tobytes()),
                         rule='five preregistered orders (natural, reversed, fill_asc, fill_desc, random seed 20260908); per leading column the sparsest row, ties by row index; largest cover, ties by order list')

    # ---- build-and-cover gate
    z = int(E.nnz); used = time.perf_counter() - t_job
    ph = phase_model(nc, delta, a, z, nU, rates)
    npr = len(args.primes); vf = rates.get('verifier_factor', 1.0)
    per_pass = ph['H'] + ph['V'] + ph['R'] + ph['D']
    remaining = npr * per_pass + vf * (ph['B'] + ph['S'] + per_pass)
    env = mem_envelope(nc, a, z, nU)
    gate = dict(z=z, U=nU, f_measured=(nU - a) / nc, phase_seconds={k: round(v, 3) for k, v in ph.items()},
                predicted_remaining_secs=round(remaining, 1), unused_budget_secs=(None if math.isinf(args.wall_budget) else round(args.wall_budget - used, 1)),
                mem_envelope_bytes=int(env), mem_cap_bytes=(None if math.isinf(args.mem_cap) else int(args.mem_cap)), rates=rates)
    gate['pass'] = bool(remaining <= args.wall_budget - used and env <= 0.75 * args.mem_cap)
    rec = dict(schema='b28-01-receipt/1', tag=tag, gate=gate, phases=rc.phases)
    cell['gate_inputs'] = dict(z=z, U=nU)
    with open(os.path.join(args.out, f'{tag}_cell.json'), 'w') as f: json.dump(cell, f, indent=1, sort_keys=True)
    if not gate['pass'] or args.gate_only:
        rec['stopped'] = 'gate' if not gate['pass'] else 'gate-only'
        with open(os.path.join(args.out, f'{tag}_receipt.json'), 'w') as f: json.dump(rec, f, indent=1)
        H.log(f"  GATE {'STOP' if not gate['pass'] else 'ok (gate-only)'}: {gate}")
        sys.exit(3 if not gate['pass'] else 0)

    Kp = a + 8
    pts = det_pencils(Kp, SEEDS['det'], args.bound, R)
    with open(os.path.join(args.out, f'{tag}_pencils.json'), 'w') as f:
        json.dump(dict(schema='b28-01-pencils/1', generator='wk12_s79_cell6.det_pencils (random.Random(11), randint(-40,40)), serialized',
                       seed=SEEDS['det'], bound=args.bound, count=Kp, R=R, pencils=pts), f, separators=(',', ':'))
    status = 0
    for p in args.primes:                                            # strictly sequential
        K, info = hybrid_det(E, nc, p, a, cov, rc)
        cert = dict(schema='b28-01-cert/1', tag=tag, prime=p, a=a, n_chi=int(nc), hybrid=info)
        if not info['source_gate']:
            cert['status'] = 'SOURCE GATE FAILED (inconclusive; no retry authorized)'
            status = 4
        else:
            kf = f'{tag}_p{p}_K.u32'
            K.astype('<u4').tofile(os.path.join(args.out, kf))
            cert['K'] = dict(file=kf, shape=[int(nc), int(a)], dtype='<u4 row-major', sha256=sha(K.astype('<u4').tobytes()))
            VK, ev = evaluate(B['arr'], K, pts, R, p, a, rc)
            VK.astype('<u4').tofile(os.path.join(args.out, f'{tag}_p{p}_VK.u32'))
            cert['evaluation'] = ev
            if ev['mult_det'] == a:
                cert['status'] = 'FULL RANK mod p: rank E = n_chi - a (cover + projected residual), a verified kernel vectors, nonzero a-minor of VK'
            else:
                rc.start('deficiency_candidates')
                cs = H.nullspace_mod_p(VK, p)                        # combinations c with (VK) c = 0 -- nullspace(VK), not VK^T
                vecs = H.matmul_mod(np.asarray(cs, dtype=np.int64) % p, np.asarray(K.T, dtype=np.int64) % p, p)
                okc = bool(np.any(vecs, axis=1).all() and H.check_kernel_mat(E, vecs.T, p))
                cf = f'{tag}_p{p}_candidates.u32'
                vecs.astype('<u4').tofile(os.path.join(args.out, cf))
                cert['candidates'] = dict(file=cf, shape=list(vecs.shape), sha256=sha(vecs.astype('<u4').tobytes()), E_equations_verified=okc)
                cert['status'] = f"MODULAR DEFICIENCY (finite-sample, mod p): mult_det >= {ev['mult_det']}; no characteristic-zero drop claimed"
                rc.stop()
            del K
        with open(os.path.join(args.out, f'{tag}_p{p}_cert.json'), 'w') as f: json.dump(cert, f, indent=1, sort_keys=True)
        H.log(f"  RESULT {tag} p={p}: {cert['status']}")
    rec['total_secs'] = round(time.perf_counter() - t_job, 3)
    with open(os.path.join(args.out, f'{tag}_receipt.json'), 'w') as f: json.dump(rec, f, indent=1)
    sys.exit(status)


if __name__ == '__main__':
    main()
