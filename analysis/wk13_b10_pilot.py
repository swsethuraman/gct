#!/usr/bin/env python3
"""
B13-10 -- the difficult-cell pilot: the cell session 79 abandoned.

(10,6,6,6,2,2) at delta = 8: N_S = 18 337 360, N_S*delta = 1.47e8, n_chi = 1 606 104,
a = 10.  s79 built it to E_34 and was ended by the box inside E_45 with the rows
over 4 GB (results/logs/s79_sweep6.log).  Here: the lean build, then -- if the
build completes -- the initial-term cover, the hybrid kernel at both house primes
with every vector verified on E, and mult_det on session 79's own det_4 family
(seed 11, bound 40, K = a + 8 points), both primes.

A full rank at one prime proves mult_det = a over Q (rank_p <= rank_Q); a drop is
a measurement and nothing here enters a decision-table branch on one.

usage: python3 analysis/wk13_b10_pilot.py [--stage build|kernel|all] [--scratch DIR] [--out FILE]
"""
import sys, os, time, json
for _v in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ.setdefault(_v, '1')
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
os.environ.setdefault('S71_SCHUR_SO', '/home/claude/b13_10_scratch/schur.so')
os.environ.setdefault('S71_MEM_X', '250000000')
import numpy as np
from scipy import sparse
import wk11_s71_codes; wk11_s71_codes.install()
from wk8_s30_core import exps, restrict, det_form, P1, P2
from wk9_s45_build import log, _rss_gb
from wk9_s42_census import a_weyl
from wk11_s71_hybrid import matmul_mod, rank_mod_p, rank_tall
from wk12_s79_cell6 import ev_rows_from_coeffs, det_pencils, det_coeffs
from wk13_b10_lean import build_cell_lean, best_cover_lean, check_kernel_mat_lean, hybrid_kernel_lean

LAM = (10, 6, 6, 6, 2, 2); DELTA = 8; N = 4
PRIMES = (P1, P2); HYB_SEED = 20260908; BOUND = 40; DET_SEED = 11


def vm(key):
    with open('/proc/self/status') as f:
        for line in f:
            if line.startswith(key): return int(line.split()[1]) / 1048576.0
    return float('nan')


def main():
    args = sys.argv[1:]
    def arg(name, default=None): return args[args.index(name) + 1] if name in args else default
    stage = arg('--stage', 'all')
    scratch = arg('--scratch', '/home/claude/b13_10_scratch')
    outp = arg('--out', os.path.join(ROOT, 'results', 'b13_10', 'pilot.json'))
    os.makedirs(scratch, exist_ok=True); os.makedirs(os.path.dirname(outp), exist_ok=True)
    npz = os.path.join(scratch, 'pilot_E.npz')
    a = int(a_weyl(LAM, DELTA, N, {}))
    rec = dict(lam=list(LAM), delta=DELTA, n=N, a=a, builder='wk13_b10_lean.build_cell_lean', knobs=dict(chunk=400000, triples='store', blocks='memory'),
               primes=list(PRIMES), seeds=dict(det=DET_SEED, hybrid=HYB_SEED), bound=BOUND, pid=os.getpid(),
               s79=dict(log='results/logs/s79_sweep6.log', outcome='ended by the box inside E_45, rows over 4 GB', N_S=18337360, n_chi=1606104, NS_delta=146698880,
                        build_hwm_gb_at_E34=4.20, orbit_secs=633),
               stamp=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))
    phases = []
    if stage in ('build', 'all'):
        base = vm('VmHWM')
        t0 = time.time()
        B = build_cell_lean(LAM, DELTA, n=N, verbose=True, phase_hook=lambda ph: phases.append(ph))
        rec['build'] = dict(secs=round(time.time() - t0, 1), mono_secs=round(B['mono_secs'], 1), orbit_secs=round(B['orbit_secs'], 1),
                            rows_secs=round(B['rows_secs'], 1), N_S=int(B['N_S']), stab=int(B['stab']), n_chi=int(B['n_chi']),
                            nrows=int(B['nrows']), nnz=int(B['nnz']), nfixed=int(B['nfixed']),
                            hwm_gb=round(vm('VmHWM'), 3), hwm_above_baseline_gb=round(vm('VmHWM') - base, 3),
                            hwm_mono_gb=round(B['hwm_mono_gb'], 3), hwm_orbit_gb=round(B['hwm_orbit_gb'], 3),
                            phases=B['phases'], dtypes=B['dtypes'], baseline_gb=round(base, 3))
        E = B['E']; arr = B['arr']
        np.savez(npz, indptr=E.indptr, indices=E.indices, data=E.data, M=arr['M'], col_of=arr['col_of'], sgn=arr['sgn'], n_chi=np.int64(arr['n_chi']))
        rec['build']['npz_bytes'] = os.path.getsize(npz)
        with open(outp, 'w') as f: json.dump(rec, f)
        log(f"  PILOT BUILD DONE: {rec['build']}")
        if stage == 'build':
            print("PILOT " + json.dumps(rec['build'])); return
    else:
        if os.path.exists(outp): rec = json.load(open(outp))
        z = np.load(npz); E = sparse.csr_matrix((z['data'], z['indices'], z['indptr']), shape=(len(z['indptr']) - 1, int(z['n_chi'])))
        arr = dict(M=z['M'], col_of=z['col_of'], sgn=z['sgn'], n_chi=int(z['n_chi']), N_S=int(z['M'].shape[0]))
        B = dict(E=E, arr=arr, n_chi=arr['n_chi'])
    E = B['E']; arr = B['arr']; nc = B['n_chi']; R = len(LAM)
    t = time.time()
    cov = best_cover_lean(E, nc, seed=HYB_SEED, verbose=True)
    rec['cover'] = dict(size=int(cov['size']), order=cov['order'], stats={k: int(v) for k, v in cov['stats'].items()},
                        n_chi=int(nc), a=a, nU=int(nc - cov['size']), excess=int(nc - cov['size'] - a),
                        certified_rank_lb=int(cov['size']), secs=round(time.time() - t, 1), hwm_gb=round(vm('VmHWM'), 3))
    with open(outp, 'w') as f: json.dump(rec, f)
    log(f"  PILOT COVER: {rec['cover']}")
    pts = det_pencils(a + 8, DET_SEED, BOUND, R)
    cl = [det_coeffs(pt, R) for pt in pts]
    per_prime = {}
    for p in PRIMES:
        tp = time.time()
        K, info = hybrid_kernel_lean(E, nc, p, a, cov, seed=HYB_SEED, tag='[pilot]', verbose=True)
        ver = bool(check_kernel_mat_lean(E, K.astype(np.int64), p))
        rk = int(rank_tall(K, p))
        tk = time.time()
        Kp_ = np.asarray(K % p, dtype=np.int64)
        parts = []
        for c0 in range(0, len(cl), 8):
            EV = ev_rows_from_coeffs(arr, cl[c0:c0 + 8], p, R)
            parts.append(matmul_mod(EV % p, Kp_, p)); del EV
        G = np.vstack(parts); del parts, Kp_
        m = int(rank_mod_p(G, p))
        per_prime[str(p)] = dict(nullity=int(K.shape[1]), verified_on_E=ver, kernel_rank=rk, mult_det=m, i_det=int(a - m),
                                 hybrid=info, kernel_secs=round(tk - tp, 1), ev_rank_secs=round(time.time() - tk, 1),
                                 hwm_gb=round(vm('VmHWM'), 3))
        rec['per_prime'] = per_prime
        with open(outp, 'w') as f: json.dump(rec, f)
        log(f"  PILOT p={p}: nullity {K.shape[1]} verified {ver} rank {rk} mult_det {m} i_det {a - m} [{round(time.time()-tp,1)}s, HWM {vm('VmHWM'):.2f} GB]")
        del K, G
    ms = {p: r['mult_det'] for p, r in per_prime.items()}
    rec['primes_agree'] = len(set(ms.values())) == 1
    rec['mult_det'] = list(ms.values())[0] if rec['primes_agree'] else None
    rec['i_det'] = (a - rec['mult_det']) if rec['primes_agree'] else None
    rec['status'] = ('proved: mult_det = a at both primes (i_det = 0 over Q)' if rec['mult_det'] == a else
                     f'MEASURED drop: mult_det = {rec["mult_det"]} -- the verification protocol takes over' if rec['primes_agree'] else 'PRIMES DISAGREE')
    rec['kernel_ok'] = all(r['nullity'] == a and r['verified_on_E'] and r['kernel_rank'] == a for r in per_prime.values())
    rec['hwm_gb'] = round(vm('VmHWM'), 3)
    with open(outp, 'w') as f: json.dump(rec, f)
    print("PILOT " + json.dumps({k: rec[k] for k in ('lam', 'delta', 'a', 'mult_det', 'i_det', 'status', 'kernel_ok', 'hwm_gb')}))


if __name__ == '__main__':
    main()
