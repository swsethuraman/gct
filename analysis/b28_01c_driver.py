#!/usr/bin/env python3
"""
B28-01c -- determinant-only driver for the blocked triangular-cover/Schur hybrid,
with R28-01's repairs.  The arithmetic is B28-01a's frozen driver
(analysis/b28_01_driver.py, de202bb0...) unchanged; the changes are control flow,
certificate content and the gate:

  P1  a failed source gate (projected nullity != a) writes the failed-source
      certificate and receipt and exits 4 BEFORE the kernel lift allocates
      Kc(n, nul); a failed all-row check, independence check or deficiency
      candidate check likewise exits 4 before the next prime.  The randomized
      rank_tall is replaced by the deterministic flint rank of Kc[U,:] (the U
      coordinates are exactly the residual basis y_U).  After both primes the
      determinant ranks and outcome categories are compared; a disagreement is
      written as INCONCLUSIVE CONTROL FAILURE and exits 6.
  P2  (driver side) the deficiency branch saves the combinations c (nullspace(VK))
      and the vectors K c, and checks every one: nonzero, independent (rank of the
      U coordinates), E K c = 0 on every row, and zero at every saved point
      (the evaluation rows are regenerated in batches of eight).  Any failure
      exits 4.  Wording: MODULAR_DEFICIENCY with a lower bound, never more.
  P3/P4  the gate prices the verifier by max(direct verifier model, rho_up x
      producer model) and gates memory on max(producer envelope, verifier
      estimate); see b28_01c_model.py.
  P5  (driver side) refuses to start if the engine loader would recompile
      schur.so (missing, older than its C source, or not the bound hash).

Fixture switches, for the registered controls only (never used by the launcher;
each is recorded in the certificate under "fixture"):
  --fixture-proj-m M      projection with M rows instead of U + 64 (forces a source-gate failure)
  --fixture-npts P:N      evaluate only the first N (< a) of the a+8 pencils at prime P

Output files are deterministic (no wall times); times and memory high-water
marks go only to the receipt file.
exit codes: 0 done (all source gates passed, primes agree), 2 refused (recompile guard),
            3 stopped at the build-and-cover gate, 4 source gate or check failed,
            6 prime disagreement (inconclusive control failure).
"""
import sys, os, json, time, hashlib, argparse, math
for _v in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[_v] = '1'
HERE = os.path.dirname(os.path.abspath(__file__))
ENGINE = os.environ.get('B28_ENGINE', HERE)
sys.path.insert(0, ENGINE)
sys.path.insert(0, HERE)
os.environ.setdefault('S71_SCHUR_SO', os.path.join(ENGINE, 'schur.so'))
os.environ['S71_MEM_X'] = '250000000'


def recompile_guard():
    """the engine's lib() recompiles when schur.so is missing or older than its
    source; refuse instead (no recompile after the launch hash check)."""
    so = os.environ['S71_SCHUR_SO']; src = os.path.join(ENGINE, 'wk11_s71_schur.c')
    if not os.path.exists(so) or os.stat(so).st_mtime_ns < os.stat(src).st_mtime_ns:
        print(f'REFUSED: {so} missing or older than {src}; the engine would recompile', file=sys.stderr); sys.exit(2)
    want = os.environ.get('B28_SCHUR_SO_SHA256')
    if want and hashlib.sha256(open(so, 'rb').read()).hexdigest() != want:
        print(f'REFUSED: {so} is not the bound binary', file=sys.stderr); sys.exit(2)


recompile_guard()
import numpy as np
from flint import nmod_mat
import wk11_s71_codes; wk11_s71_codes.install()
from wk8_s30_core import P1, P2
from wk9_s45_build import build_cell
from wk9_s42_census import a_weyl
from wk12_s79_cell6 import det_pencils, det_coeffs, ev_rows_from_coeffs, SEEDS, HYB_SEED
import wk11_s71_hybrid as H
import b28_01c_model as MODEL

N = 4
MEM_X = 250_000_000


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


# ------------------------------------------------------------------ the hybrid, one attempt
def hybrid_det(E, nc, p, a, cov, rc, fixture_m=None):
    """wk11_s71_hybrid.hybrid_kernel with retries = 1 (the preregistered single
    projection attempt), X blocks under S71_MEM_X, and the projected residual's
    hash and recipe exported.  Returns (K uint32 nc x a or None, info); K is None
    whenever the source gate failed, and then no lift was attempted or finished."""
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
    m = nU + extra if fixture_m is None else int(fixture_m)
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
    proj = dict(base_seed=HYB_SEED, attempt=attempt, pseed=int(pseed), m=int(m), extra=extra, nproj=nproj,
                generator='wk11_s71_schur.c splitmix64, z = pseed ^ (0xD1B54A32D192ED03*(r+1)), row t = x % m, sign = (x>>40)&1')
    if fixture_m is not None: proj['fixture_m'] = int(fixture_m)
    info = dict(nS=int(nS), nU=int(nU), nnzT=int(T.nnz), rows_other=int(Fo.shape[0]), ublock=int(ublock), nblocks=int(nblocks),
                projection=proj, G_shape=[int(m), int(nU)], G_sha256=G_sha, projected_nullity=int(nul))
    if nul != a:                                                    # P1: stop before allocating Kc(n, nul)
        info.update(source_gate=False, failed_check='projected nullity != a (no lift attempted)')
        return None, info
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
        if not H.check_kernel_mat(E, Kc[:, v0:v1].astype(np.int64), p):
            ok = False; break                                       # P1: stop at the first failed check
    rk = H.rank_mod_p(Kc[U, :], p) if ok else None                 # deterministic flint rank of the U coordinates
    rc.stop(nullity=int(nul))
    info.update(verified_on_all_rows=bool(ok), rank_K=(None if rk is None else int(rk)),
                rank_K_method='flint nmod_mat rank of K[U,:] (deterministic; replaces rank_tall)')
    info['source_gate'] = bool(ok and rk == a)
    if not info['source_gate']:
        info['failed_check'] = 'E K = 0 on all rows' if not ok else 'rank K[U,:] != a'
        return None, info
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


def eval_rows(arr, pts, p, R):
    """the evaluation rows, in batches of at most eight points."""
    cl = [det_coeffs(pt, R) for pt in pts]
    for c0 in range(0, len(cl), 8):
        yield ev_rows_from_coeffs(arr, cl[c0:c0 + 8], p, R)


def evaluate(arr, K, pts, R, p, a, rc):
    rc.start('evaluation')
    Kp_ = np.asarray(K % p, dtype=np.int64)
    assert Kp_.shape[0] < (1 << 21)                                 # matmul_mod's exact-limb bound (asserted again inside)
    parts = []
    for EV in eval_rows(arr, pts, p, R):
        parts.append(H.matmul_mod(EV % p, Kp_, p)); del EV
    del Kp_
    VK = np.vstack(parts) % p
    mult = H.rank_mod_p(VK, p)
    piv, rk = minor_rows(VK, p)
    assert rk == mult
    out = dict(mult_det=int(mult), npts=len(pts), VK_shape=list(VK.shape), VK_sha256=sha(np.ascontiguousarray(VK.astype('<u4')).tobytes()))
    if mult == a:
        sub = VK[piv]
        d = nmod_mat(a, a, sub.astype(np.int64).ravel().tolist(), p).det()
        assert int(d) != 0
        out['minor_rows'] = [int(x) for x in piv]; out['minor_det_mod_p'] = int(d)
    rc.stop(npts=len(pts))
    return VK, out


def deficiency_candidates(E, K, VK, U, arr, pts, R, p, out, tag, rc):
    """P2: combinations c = nullspace(VK) (never VK^T), vectors K c, all checked."""
    rc.start('deficiency_candidates')
    cs = H.nullspace_mod_p(VK, p) % p                               # (a - r) x a
    vecs = H.matmul_mod(np.asarray(cs, dtype=np.int64), np.asarray(K.T, dtype=np.int64) % p, p)
    nz = bool(np.any(vecs, axis=1).all())
    indep = bool(H.rank_mod_p(vecs[:, U], p) == cs.shape[0])
    eq = bool(H.check_kernel_mat(E, vecs.T, p))
    zero = True
    VT = np.ascontiguousarray(vecs.T) % p
    for EV in eval_rows(arr, pts, p, R):
        if np.any(H.matmul_mod(EV % p, VT, p)): zero = False
        del EV
    cf = f'{tag}_p{p}_candidates.u32'; bf = f'{tag}_p{p}_combinations.u32'
    vecs.astype('<u4').tofile(os.path.join(out, cf)); cs.astype('<u4').tofile(os.path.join(out, bf))
    checks = dict(nonzero=nz, independent_on_U=indep, E_equations_all_rows=eq, zero_at_every_saved_point=zero)
    rc.stop(count=int(cs.shape[0]))
    return dict(file=cf, shape=list(vecs.shape), dtype='<u4 row-major', sha256=sha(vecs.astype('<u4').tobytes()),
                combinations=dict(file=bf, shape=list(cs.shape), sha256=sha(cs.astype('<u4').tobytes()), rule='candidates = combinations K^T'),
                checks=checks, status='unproved candidates (modular, finite sample)'), all(checks.values())


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
    ap.add_argument('--rates', required=True, help='JSON gate rates (schema b28-01c-gate-rates/1)')
    ap.add_argument('--gate-only', action='store_true')
    ap.add_argument('--bound', type=int, default=40)
    ap.add_argument('--fixture-proj-m', type=int, default=None)
    ap.add_argument('--fixture-npts', action='append', default=[])
    args = ap.parse_args()
    lam = tuple(args.lam); delta = args.delta; R = len(lam)
    assert all(p in (P1, P2) for p in args.primes)
    assert len(set(args.primes)) == len(args.primes)
    fx_npts = {}
    for s in args.fixture_npts:
        pp, nn = s.split(':'); fx_npts[int(pp)] = int(nn)
        assert int(nn) < args.a, 'a fixture point count must be below a'
    fixture = {}
    if args.fixture_proj_m is not None: fixture['proj_m'] = args.fixture_proj_m
    if fx_npts: fixture['npts'] = {str(k): v for k, v in fx_npts.items()}
    os.makedirs(args.out, exist_ok=True)
    tag = '_'.join(map(str, lam)) + f'_d{delta}'
    rc = Receipt(); t_job = time.perf_counter()
    rates = json.load(open(args.rates))
    assert rates.get('schema') == 'b28-01c-gate-rates/1', 'gate rates schema'

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

    # ---- build-and-cover gate (P3 verifier time, P4 verifier memory)
    z = int(E.nnz); used = time.perf_counter() - t_job
    lens = np.diff(E.indptr)
    z_R1 = int(lens[np.asarray(cov['rows'], dtype=np.int64)].sum()); z_Fo = z - z_R1
    nS = int(len(cov['S'])); ro = int(E.shape[0]) - int(len(cov['rows']))
    npr = len(args.primes)
    prod_secs, ver_secs, tdet = MODEL.remaining_secs(nc, delta, a, z, nU, npr, rates)
    remaining = prod_secs + ver_secs
    env = MODEL.mem_envelope(nc, a, z, nU)
    vmem, vdet = MODEL.verifier_mem(nc, int(B['N_S']), delta, a, z, int(E.shape[0]), nU, nS, ro, z_R1, z_Fo)
    need = max(env, vmem)
    gate = dict(z=z, U=nU, f_measured=(nU - a) / nc, rows_E=int(E.shape[0]), rows_other=ro, nS=nS, z_cover_rows=z_R1, z_other_rows=z_Fo,
                N_S=int(B['N_S']), phase_seconds={k: round(v, 3) for k, v in tdet['producer_phase_secs'].items()},
                verifier_phase_seconds={k: round(v, 3) for k, v in tdet['verifier_phase_secs'].items()},
                verifier_direct_secs=round(tdet['verifier_direct_secs'], 1), verifier_ratio_secs=round(tdet['verifier_ratio_secs'], 1),
                predicted_producer_remaining_secs=round(prod_secs, 1), predicted_verifier_secs=round(ver_secs, 1),
                predicted_remaining_secs=round(remaining, 1), unused_budget_secs=(None if math.isinf(args.wall_budget) else round(args.wall_budget - used, 1)),
                mem_envelope_bytes=int(env), verifier_mem_estimate_bytes=int(vmem), verifier_mem_terms=vdet, mem_needed_bytes=int(need),
                mem_cap_bytes=(None if math.isinf(args.mem_cap) else int(args.mem_cap)), rates=rates)
    gate['pass'] = bool(remaining <= args.wall_budget - used and need <= 0.75 * args.mem_cap)
    rec = dict(schema='b28-01c-receipt/1', tag=tag, gate=gate, phases=rc.phases)
    cell['gate_inputs'] = dict(z=z, U=nU)
    with open(os.path.join(args.out, f'{tag}_cell.json'), 'w') as f: json.dump(cell, f, indent=1, sort_keys=True)

    def write_receipt(**kw):
        rec.update(kw); rec['total_secs'] = round(time.perf_counter() - t_job, 3)
        with open(os.path.join(args.out, f'{tag}_receipt.json'), 'w') as f: json.dump(rec, f, indent=1)

    if not gate['pass'] or args.gate_only:
        write_receipt(stopped='gate' if not gate['pass'] else 'gate-only')
        H.log(f"  GATE {'STOP' if not gate['pass'] else 'ok (gate-only)'}: {gate}")
        sys.exit(3 if not gate['pass'] else 0)

    Kp = a + 8
    pts_all = det_pencils(Kp, SEEDS['det'], args.bound, R)
    with open(os.path.join(args.out, f'{tag}_pencils.json'), 'w') as f:
        json.dump(dict(schema='b28-01-pencils/1', generator='wk12_s79_cell6.det_pencils (random.Random(11), randint(-40,40)), serialized',
                       seed=SEEDS['det'], bound=args.bound, count=Kp, R=R, pencils=pts_all), f, separators=(',', ':'))
    outcome = {}
    for p in args.primes:                                            # strictly sequential
        K, info = hybrid_det(E, nc, p, a, cov, rc, fixture_m=args.fixture_proj_m)
        cert = dict(schema='b28-01c-cert/1', tag=tag, prime=p, a=a, n_chi=int(nc), hybrid=info)
        if fixture: cert['fixture'] = fixture
        stop = False
        if K is None:
            cert['status'] = 'SOURCE GATE FAILED (inconclusive; no retry authorized)'
            stop = True
        else:
            kf = f'{tag}_p{p}_K.u32'
            K.astype('<u4').tofile(os.path.join(args.out, kf))
            cert['K'] = dict(file=kf, shape=[int(nc), int(a)], dtype='<u4 row-major', sha256=sha(K.astype('<u4').tobytes()))
            pts = pts_all[:fx_npts[p]] if p in fx_npts else pts_all
            VK, ev = evaluate(B['arr'], K, pts, R, p, a, rc)
            VK.astype('<u4').tofile(os.path.join(args.out, f'{tag}_p{p}_VK.u32'))
            cert['evaluation'] = ev
            if ev['mult_det'] == a:
                cert['outcome'] = 'FULL_RANK'
                cert['status'] = 'FULL RANK mod p: rank E = n_chi - a (cover + projected residual), a verified kernel vectors, nonzero a-minor of VK'
            else:
                cand, okc = deficiency_candidates(E, K, VK, np.asarray(cov['U'], dtype=np.int64), B['arr'], pts, R, p, args.out, tag, rc)
                cert['candidates'] = cand
                cert['outcome'] = 'MODULAR_DEFICIENCY'
                cert['mult_det_lower_bound'] = int(ev['mult_det'])
                if okc:
                    cert['status'] = f"MODULAR_DEFICIENCY (finite sample, mod p): mult_det >= {ev['mult_det']}; {a - ev['mult_det']} unproved candidates; no characteristic-zero statement"
                else:
                    cert['status'] = 'CHECK FAILED: a deficiency candidate failed its checks (inconclusive)'
                    stop = True
            outcome[p] = (cert.get('outcome'), int(ev['mult_det']))
            del K
        with open(os.path.join(args.out, f'{tag}_p{p}_cert.json'), 'w') as f: json.dump(cert, f, indent=1, sort_keys=True)
        H.log(f"  RESULT {tag} p={p}: {cert['status']}")
        if stop:                                                     # P1: stop before the next prime
            write_receipt(stopped=f'source gate or check failed at p={p}')
            sys.exit(4)
    status = 0
    if len(args.primes) > 1:                                         # P1: compare the primes
        agree = len(set(outcome.values())) == 1
        cmp_ = dict(schema='b28-01c-primes/1', tag=tag, primes=args.primes,
                    per_prime={str(p): dict(outcome=o, mult_det=r) for p, (o, r) in outcome.items()}, agree=bool(agree),
                    verdict=('AGREE' if agree else 'INCONCLUSIVE CONTROL FAILURE: the primes disagree on rank or outcome (not averaged, not resolved by another prime)'))
        if fixture: cmp_['fixture'] = fixture
        with open(os.path.join(args.out, f'{tag}_primes.json'), 'w') as f: json.dump(cmp_, f, indent=1, sort_keys=True)
        H.log(f"  PRIMES {tag}: {cmp_['verdict']}")
        if not agree: status = 6
    write_receipt()
    sys.exit(status)


if __name__ == '__main__':
    main()
