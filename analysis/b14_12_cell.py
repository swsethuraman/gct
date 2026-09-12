#!/usr/bin/env python3
"""
B14-12 -- one cell of any length and any n on the integrated (lean) engine,
determinant-first, with the forced negative control carried in the same process.

This is wk13_b10_pilot.py (B13-10) re-parametrised over (lam, delta, n) with
three changes, every one of them pre-registered in results/PREREG_b14_12.md:

  * blocks='disk'    B13-10 section 3 measured this to cut the lean build peak by a
                     further 17-36% at 1.02-1.14x the time, and names it "the
                     setting a box-constrained production run should use".
  * fo='inplace'     B13-10 section 5: "A batch-14 production run should measure
                     fo='inplace' first; on the pilot it should save about 0.7 GB
                     of the 4.53."  Equivalence banked at
                     results/b13_10/fo_inplace_check.json and re-checked here by
                     Control F in analysis/b14_12_controls.py.
  * Control N        the diagonal-pencil forced negative (PROVED.md:
                     negative_control_forced) at the cell's own n, run on the same
                     kernel K in the same process, together with the generic
                     det_n family as the input on which its rank-zero assertion
                     MUST fail.

No mathematics is new here: every routine called is the tree's own.  Letters are
resolved through wk8_s30_core.exps(n, r) by index -- never by a literal -- because
two opposite exps orderings exist in this tree, and n is passed explicitly to
ev_rows_from_coeffs rather than left to its module default.

A full rank at ONE prime proves mult_det = a over Q (rank_p <= rank_Q).  A drop is
a ceiling on i_det and NEVER establishes i_det >= 1 (PROVED.md: rank_floor,
evaluation_cannot_certify_i_ge_1); no branch here reads one downward.

usage: python3 analysis/b14_12_cell.py --lam 12,4,4,4,4,4 --delta 8 --n 4
                                       [--stage build|kernel|all] [--scratch DIR]
                                       [--out FILE] [--blocks disk|memory]
                                       [--fo inplace|copy] [--tag NAME] [--quiet]
"""
import sys, os, time, json, random
for _v in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ.setdefault(_v, '1')
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
os.environ.setdefault('S71_SCHUR_SO', os.path.join(os.path.expanduser('~'), 'b14_12_scratch', 'schur.so'))
os.environ.setdefault('S71_MEM_X', '250000000')
os.makedirs(os.path.dirname(os.environ['S71_SCHUR_SO']), exist_ok=True)
import numpy as np

def _write_pidfile(name):
    """The run's own process id, not the wrapper's.  A run that must be ended
    early is ended by THIS id (docs/brief_wording.md section 1)."""
    d = os.path.join(ROOT, 'results', 'logs'); os.makedirs(d, exist_ok=True)
    fp = os.path.join(d, name + '.pid')
    with open(fp, 'w') as f: f.write(str(os.getpid()) + "\n")
    return fp

from scipy import sparse
import wk11_s71_codes; wk11_s71_codes.install()
from wk8_s30_core import exps, restrict, det_form, P1, P2
from wk9_s45_build import log
from wk9_s42_census import a_weyl
from wk11_s71_hybrid import matmul_mod, rank_mod_p, rank_tall
from wk12_s79_cell6 import ev_rows_from_coeffs, det_pencils, det_coeffs
from wk13_b10_lean import build_cell_lean, best_cover_lean, check_kernel_mat_lean, hybrid_kernel_lean

PRIMES = (P1, P2)
HYB_SEED = 20260908          # session 71's hybrid seed, as the pilot
DET_SEED = 11                # session 79's det_n family seed
NEG_SEED = 20260909          # B13-08 Control C's diagonal seed
BOUND = 40


def vm(key='VmHWM'):
    try:
        with open('/proc/self/status') as f:
            for line in f:
                if line.startswith(key): return int(line.split()[1]) / 1048576.0
    except Exception: pass
    return float('nan')


# ---------------------------------------------------------------- the forced negative, at any n
def diag_pencils(K, seed, bound, R, n):
    """A_i = diag(d_i0..d_i,n-1), so det_n(sum_i s_i A_i) = prod_c (sum_i s_i d_ic):
    a product of n linear forms in the R variables s.  The coordinate ring of a
    product of n linear forms carries no constituent of more than n rows, so at a
    weight of length > n the evaluation rank is FORCED to 0 by representation
    theory, with no banked history needed (PROVED.md: negative_control_forced)."""
    rnd = random.Random(seed)
    out = []
    for _ in range(K):
        pen = []
        for _i in range(R):
            d = [rnd.randint(-bound, bound) for _ in range(n)]
            pen.append([[d[a] if a == b else 0 for b in range(n)] for a in range(n)])
        out.append(pen)
    return out


def detn_coeffs(pencil, R, n):
    DETN, NN = det_form(n)
    As = [[pencil[i][a][b] for a in range(n) for b in range(n)] for i in range(R)]
    return restrict(DETN, NN, n, R, As)


def linear_product_coeffs(pencil, R, n):
    """The explicit n-fold product prod_c (sum_i s_i pencil[i][c][c]), built by
    repeated multiplication -- an independent route to the same polynomial."""
    prod = {tuple([0] * R): 1}
    for c in range(n):
        nxt = {}
        for al, cf in prod.items():
            for i in range(R):
                v = pencil[i][c][c]
                if v == 0: continue
                k = list(al); k[i] += 1; k = tuple(k)
                nxt[k] = nxt.get(k, 0) + cf * v
        prod = nxt
    return {k: v for k, v in prod.items() if v}


def diag_identity_ok(pencil, R, n):
    """True iff the restricted det_n of a pencil equals the explicit product of its
    n diagonal linear forms.  MUST be True on a diagonal pencil and MUST be False
    on a generic one -- that second call is the input that makes this check fail."""
    return {k: v for k, v in detn_coeffs(pencil, R, n).items() if v} == linear_product_coeffs(pencil, R, n)


def rank_on_family(arr, coeff_dicts, K, p, R, n, batch=8):
    """rank_p of (evaluation rows on the family) . K, in batches."""
    Kp = np.asarray(K % p, dtype=np.int64)
    parts = []
    for c0 in range(0, len(coeff_dicts), batch):
        EV = ev_rows_from_coeffs(arr, coeff_dicts[c0:c0 + batch], p, R, n=n)
        parts.append(matmul_mod(EV % p, Kp, p)); del EV
    G = np.vstack(parts); del parts, Kp
    r = int(rank_mod_p(G, p))
    allzero = bool(not np.any(G))
    del G
    return r, allzero


# ---------------------------------------------------------------- stages
def stage_build(lam, delta, n, npz, rec, blocks='disk', triples='store', chunk=400000,
                scratch=None, verbose=True):
    base = vm('VmHWM')
    phases = []
    t0 = time.time()
    B = build_cell_lean(lam, delta, n=n, verbose=verbose, chunk=chunk, triples=triples,
                        blocks=blocks, scratch=scratch, phase_hook=lambda ph: phases.append(ph))
    E = B['E']; arr = B['arr']
    rec['build'] = dict(
        secs=round(time.time() - t0, 1), mono_secs=round(B['mono_secs'], 1),
        orbit_secs=round(B['orbit_secs'], 1), rows_secs=round(B['rows_secs'], 1),
        N_S=int(B['N_S']), stab=int(B['stab']), n_chi=int(B['n_chi']),
        nrows=int(E.shape[0]), nnz=int(E.nnz), nfixed=int(B['nfixed']),
        hwm_gb=round(vm('VmHWM'), 3), hwm_above_baseline_gb=round(vm('VmHWM') - base, 3),
        hwm_mono_gb=round(B['hwm_mono_gb'], 3), hwm_orbit_gb=round(B['hwm_orbit_gb'], 3),
        baseline_gb=round(base, 3), phases=phases, dtypes=B['dtypes'],
        knobs=dict(chunk=chunk, triples=triples, blocks=blocks),
        entry_max=int(np.abs(E.data).max()) if E.nnz else 0)
    if npz:
        np.savez(npz, indptr=E.indptr, indices=E.indices, data=E.data, M=arr['M'],
                 col_of=arr['col_of'], sgn=arr['sgn'], n_chi=np.int64(arr['n_chi']))
        rec['build']['npz_bytes'] = os.path.getsize(npz)
    return B


def load_build(npz, lam):
    z = np.load(npz)
    E = sparse.csr_matrix((z['data'], z['indices'], z['indptr']),
                          shape=(len(z['indptr']) - 1, int(z['n_chi'])))
    arr = dict(M=z['M'], col_of=z['col_of'], sgn=z['sgn'], n_chi=int(z['n_chi']),
               N_S=int(z['M'].shape[0]))
    return dict(E=E, arr=arr, n_chi=arr['n_chi'])


def stage_kernel(B, lam, delta, n, a, rec, fo='inplace', verbose=True, tag='',
                 out=None, control=True):
    E = B['E']; arr = B['arr']; nc = B['n_chi']; R = len(lam)
    t = time.time()
    cov = best_cover_lean(E, nc, seed=HYB_SEED, verbose=verbose)
    rec['cover'] = dict(size=int(cov['size']), order=cov['order'],
                        stats={k: int(v) for k, v in cov['stats'].items()},
                        n_chi=int(nc), a=int(a), nU=int(nc - cov['size']),
                        excess=int(nc - cov['size'] - a), certified_rank_lb=int(cov['size']),
                        secs=round(time.time() - t, 1), hwm_gb=round(vm('VmHWM'), 3))
    if out: json.dump(rec, open(out, 'w'))
    log(f"  [{tag}] COVER: {rec['cover']}")

    npts = a + 8
    det_pts = det_pencils(npts, DET_SEED, BOUND, R)
    det_cl = [det_coeffs(pt, R) for pt in det_pts]
    diag_pts = diag_pencils(npts, NEG_SEED, BOUND, R, n) if control else []
    diag_cl = [detn_coeffs(pt, R, n) for pt in diag_pts]

    # Control N.a, run before any rank: the diagonal pencil IS the product of its
    # n linear forms (must hold), and a generic det_n pencil is NOT (must fail).
    if control:
        na_pos = [diag_identity_ok(pt, R, n) for pt in diag_pts]
        na_neg = [diag_identity_ok(pt, R, n) for pt in det_pts]
        rec['control_N']['identity_on_diagonal_all_true'] = bool(all(na_pos)) and len(na_pos) == npts
        rec['control_N']['identity_on_generic_any_true'] = bool(any(na_neg))
        rec['control_N']['npoints'] = npts
        assert rec['control_N']['identity_on_diagonal_all_true'], "diagonal pencil is not the product of its linear forms"
        assert not rec['control_N']['identity_on_generic_any_true'], \
            "N.a did NOT fail on generic det_n pencils -- the identity check is vacuous"
        log(f"  [{tag}] N.a: identity holds on all {npts} diagonal pencils and on 0 of {npts} generic pencils (must be 0)")

    per_prime = {}
    for p in PRIMES:
        tp = time.time()
        K, info = hybrid_kernel_lean(E, nc, p, a, cov, seed=HYB_SEED, tag=f'[{tag}]',
                                     verbose=verbose, fo=fo)
        ver = bool(check_kernel_mat_lean(E, K.astype(np.int64), p))
        rk = int(rank_tall(K, p))
        tk = time.time()
        ent = dict(nullity=int(K.shape[1]), verified_on_E=ver, kernel_rank=rk,
                   hybrid=info, kernel_secs=round(tk - tp, 1))
        assert ver and rk == int(K.shape[1]) == a, ("S2: kernel not verified / wrong dimension", ver, rk, K.shape, a)
        m, _z = rank_on_family(arr, det_cl, K, p, R, n)
        ent['mult_det'] = m; ent['i_det'] = int(a - m)
        if control:
            rd, allzero = rank_on_family(arr, diag_cl, K, p, R, n)
            ent['rank_diagonal_pencils'] = rd
            ent['diag_all_rows_zero'] = allzero
            # N.b: the rank-zero assertion, and the input on which it must fail.
            assert rd == 0, ("Control N failed: diagonal pencils read non-zero rank -- "
                             "halt the sweep; the verification protocol takes over", rd)
            nb_would_fail = (m != 0)
            ent['Nb_zero_assertion_fails_on_generic_det'] = bool(nb_would_fail)
            assert nb_would_fail, ("N.b did NOT fail on the generic det_n family: the evaluation-and-rank "
                                   "path returns 0 on everything, so no rank here means anything")
            log(f"  [{tag}] N.b p={p}: diagonal rank {rd} (must be 0, all-zero={allzero}); "
                f"generic det rank {m} (must be > 0 for the control to have teeth)")
        ent['ev_rank_secs'] = round(time.time() - tk, 1)
        ent['hwm_gb'] = round(vm('VmHWM'), 3)
        per_prime[str(p)] = ent
        rec['per_prime'] = per_prime
        if out: json.dump(rec, open(out, 'w'))
        log(f"  [{tag}] p={p}: nullity {K.shape[1]} verified {ver} rank {rk} "
            f"mult_det {ent['mult_det']} i_det {ent['i_det']} "
            f"[{round(time.time()-tp,1)}s, HWM {vm('VmHWM'):.2f} GB]")
        del K
    ms = {p: r['mult_det'] for p, r in per_prime.items()}
    rec['primes_agree'] = len(set(ms.values())) == 1
    rec['mult_det'] = list(ms.values())[0] if rec['primes_agree'] else None
    rec['i_det'] = (a - rec['mult_det']) if rec['primes_agree'] else None
    rec['status'] = ('proved: mult_det = a at both primes (i_det = 0 over Q)' if rec['mult_det'] == a else
                     f'MEASURED drop: mult_det = {rec["mult_det"]} -- a ceiling on i_det; '
                     'the verification protocol (PREREG_s79 sec 2.5) takes over' if rec['primes_agree'] else
                     'PRIMES DISAGREE -- instrument fault, no mathematical claim')
    rec['kernel_ok'] = all(r['nullity'] == a and r['verified_on_E'] and r['kernel_rank'] == a
                           for r in per_prime.values())
    if control:
        rec['control_N']['rank_zero_both_primes'] = all(
            per_prime[str(p)]['rank_diagonal_pencils'] == 0 for p in PRIMES)
        rec['control_N']['status'] = 'PASS' if rec['control_N']['rank_zero_both_primes'] else 'FAIL'
    rec['hwm_gb'] = round(vm('VmHWM'), 3)
    if out: json.dump(rec, open(out, 'w'))
    return rec


def main(argv):
    def arg(name, default=None): return argv[argv.index(name) + 1] if name in argv else default
    lam = tuple(int(x) for x in arg('--lam').split(','))
    delta = int(arg('--delta')); n = int(arg('--n', '4'))
    stage = arg('--stage', 'all')
    tag = arg('--tag', 'b14_12')
    scratch = arg('--scratch', os.path.join(os.path.expanduser('~'), 'b14_12_scratch'))
    out = arg('--out', os.path.join(ROOT, 'results', 'b14_12', f'{tag}.json'))
    blocks = arg('--blocks', 'disk'); fo = arg('--fo', 'inplace')
    verbose = '--quiet' not in argv
    control = '--no-control' not in argv
    os.makedirs(scratch, exist_ok=True); os.makedirs(os.path.dirname(out), exist_ok=True)
    npz = os.path.join(scratch, f'{tag}_E.npz')
    pidfile = _write_pidfile(f'{tag}_{stage}')

    t_a = time.time()
    a = int(a_weyl(lam, delta, n, {}))
    rec = dict(session='B14-12', board_numbering='batch14', lam=list(lam), delta=delta, n=n, r=len(lam),
               a=a, a_secs=round(time.time() - t_a, 1),
               builder='wk13_b10_lean.build_cell_lean', kernel='wk13_b10_lean.hybrid_kernel_lean',
               knobs=dict(blocks=blocks, fo=fo, triples='store', chunk=400000,
                          S71_MEM_X=os.environ.get('S71_MEM_X')),
               primes=list(PRIMES), seeds=dict(det=DET_SEED, hybrid=HYB_SEED, diag=NEG_SEED),
               bound=BOUND, pid=os.getpid(), pidfile=pidfile, control_N=dict(kind='diagonal pencils, forced rank 0 at length > n'),
               host=dict(cpus=os.cpu_count(), mem_total_gb=round(int(open('/proc/meminfo').readline().split()[1]) / 1048576.0, 2)),
               stamp=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))
    log(f"  [{tag}] {lam} d{delta} n={n}: a_weyl = {a} ({rec['a_secs']}s)")
    if stage in ('build', 'all'):
        B = stage_build(lam, delta, n, npz if stage == 'build' else None, rec,
                        blocks=blocks, scratch=scratch, verbose=verbose)
        json.dump(rec, open(out, 'w'))
        log(f"  [{tag}] BUILD DONE: " + json.dumps({k: rec['build'][k] for k in
            ('secs', 'N_S', 'stab', 'n_chi', 'nrows', 'nnz', 'hwm_gb', 'entry_max')}))
        if stage == 'build':
            print("B14_12_BUILD " + json.dumps(rec['build'])); return 0
    else:
        if os.path.exists(out): rec = json.load(open(out)); rec['pid'] = os.getpid()
        B = load_build(npz, lam)
    rec = stage_kernel(B, lam, delta, n, a, rec, fo=fo, verbose=verbose, tag=tag, out=out, control=control)
    print("B14_12 " + json.dumps({k: rec.get(k) for k in
          ('lam', 'delta', 'n', 'a', 'mult_det', 'i_det', 'status', 'kernel_ok', 'hwm_gb')}))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
