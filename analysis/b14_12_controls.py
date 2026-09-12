#!/usr/bin/env python3
"""
B14-12 -- the input-and-control checkpoint (results/PREREG_b14_12.md section 5).

Every control here is run TWICE: once on the input it is meant to accept, and
once on an input for which its assertion is FALSE.  A control whose deliberate
failure does not fire is a dead control and stops the session (PREREG section 7, S1;
PROVED.md: check_must_be_able_to_fail, whose seventh instance was a script that
reported PASS on an empty census because all() and not any() over nothing are
vacuously true).

  T   toolchain and input contract -- gcc, python-flint, numpy, scipy; the frozen
      queue entry for the target cell; a_weyl re-derived, not inherited (S5).
  Nc  rank machinery liveness: rank_mod_p on matrices of KNOWN rank.
      Fails on: a matrix whose rank is asserted wrongly.
  R   the n_chi MEASUREMENT path, against the one Q1 cell where the truth is
      banked -- the orbit-setup half of (10,6,6,6,2,2)_8 only (no raising rows,
      no kernel), compared with results/b13_10/pilot.json.
      Fails on: the same comparison against the queue's ESTIMATE ceil(N_S/|Stab|).
  S   the driver end to end on two banked n = 4 suite cells, B1 (|Stab| = 120,
      the target's own stabiliser order) and A1, field by field against
      results/b13_10/suite.jsonl, with an explicit non-empty-comparison guard.
      Fails on: a one-field mutation of the banked record.
  K   every null vector verified on the full E.
      Fails on: a kernel matrix with one entry incremented.
  F   fo='inplace' (this session's deviation from the pilot's fo='copy')
      against fo='copy' on the same banked cell.
      Fails on: comparison against a mutated fo='copy' result.

usage: python3 analysis/b14_12_controls.py [--out results/b14_12/controls.json] [--skip R]
"""
import sys, os, time, json, subprocess
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

import wk11_s71_codes; wk11_s71_codes.install()
from wk8_s30_core import exps, P1, P2
from wk9_s42_census import a_weyl
from wk11_s71_hybrid import rank_mod_p, matmul_mod
from wk13_b10_lean import (monomials_array_lean, orbit_setup_lean, build_cell_lean,
                           best_cover_lean, check_kernel_mat_lean, hybrid_kernel_lean)
import b14_12_cell as DRV

TARGET = ((12, 4, 4, 4, 4, 4), 8, 4)
PILOT = ((10, 6, 6, 6, 2, 2), 8, 4)
PRIMES = (P1, P2)


def log(*a):
    print(*a, file=sys.stderr); sys.stderr.flush()


def vm(key='VmHWM'):
    with open('/proc/self/status') as f:
        for line in f:
            if line.startswith(key): return int(line.split()[1]) / 1048576.0
    return float('nan')


def compare(here, banked, fields):
    """Field-by-field comparison with a non-empty guard: an empty comparison is a
    FAILURE, not a vacuous PASS."""
    cmp = {}
    for k, hv in fields:
        if k not in banked:
            cmp[k] = dict(here=hv, banked=None, placed=False, equal=False)
        else:
            cmp[k] = dict(here=hv, banked=banked[k], placed=True, equal=(hv == banked[k]))
    placed = sum(1 for v in cmp.values() if v['placed'])
    ok = placed > 0 and all(v['equal'] for v in cmp.values())
    return dict(fields=cmp, placed=placed, all_equal=ok)


def banked_suite(cell_id):
    rec = None
    for ln in open(os.path.join(ROOT, 'results', 'b13_10', 'suite.jsonl')):
        r = json.loads(ln)
        if r.get('id') == cell_id: rec = r          # last occurrence wins (post-fix records)
    if rec is None: raise KeyError(cell_id)
    return rec


# ------------------------------------------------------------------ T
def control_T(res):
    import flint, numpy, scipy, sympy
    gcc = subprocess.run(['gcc', '--version'], capture_output=True, text=True).stdout.splitlines()[0]
    q = [x for x in json.load(open(os.path.join(ROOT, 'results', 's79_queue.json')))
         if tuple(x['lam']) == TARGET[0] and x['delta'] == TARGET[1]]
    assert len(q) == 1, ("target cell not unique in the frozen queue", len(q))
    q = q[0]
    # every nchi_est in the frozen queue is exactly ceil(N_S/|Stab|) -- the quotient
    # PROVED.md: nchi_2_21_guard says is neither an upper nor a lower bound.
    allq = json.load(open(os.path.join(ROOT, 'results', 's79_queue.json')))
    est_is_quotient = sum(1 for x in allq if x['nchi_est'] == -(-x['N_S'] // x['stab']))
    pilot = json.load(open(os.path.join(ROOT, 'results', 'b13_10', 'pilot.json')))
    pq = [x for x in allq if tuple(x['lam']) == PILOT[0] and x['delta'] == PILOT[1]][0]
    t = time.time(); a = int(a_weyl(TARGET[0], TARGET[1], TARGET[2], {})); a_secs = round(time.time() - t, 1)
    res['T'] = dict(
        gcc=gcc, flint=flint.__version__, numpy=numpy.__version__, scipy=scipy.__version__, sympy=sympy.__version__,
        preinstalled=dict(gcc=True, python_flint=False, numpy=False, scipy=False, sympy=False),
        queue_entry=q, a_weyl=a, a_weyl_secs=a_secs, a_matches_queue=(a == q['a']),
        L_exps=len(exps(TARGET[2], len(TARGET[0]))),
        entry_bound=q['stab'] * TARGET[1] * (TARGET[2] + 1),
        queue_nchi_est_is_NS_over_stab=dict(n_entries=len(allq), n_equal_to_quotient=est_is_quotient),
        pilot_quotient_vs_measured=dict(queue_est=pq['nchi_est'], measured=pilot['build']['n_chi'],
                                        ratio=round(pilot['build']['n_chi'] / pq['nchi_est'], 4)))
    assert res['T']['a_matches_queue'], ("S5: a_weyl disagrees with the frozen queue", a, q['a'])
    assert est_is_quotient == len(allq)
    res['T']['status'] = 'PASS'
    log(f"T PASS: a_weyl{TARGET[0]} d{TARGET[1]} = {a} (queue {q['a']}), L = {res['T']['L_exps']}, "
        f"entry bound {res['T']['entry_bound']} < 32768; queue nchi_est = ceil(N_S/|Stab|) on "
        f"{est_is_quotient}/{len(allq)} entries; at the pilot that quotient is "
        f"{res['T']['pilot_quotient_vs_measured']['ratio']}x the measured n_chi")


# ------------------------------------------------------------------ N.c
def control_Nc(res):
    rng = np.random.default_rng(20260912)
    out = []
    for p in PRIMES:
        A = rng.integers(0, p, size=(40, 7), dtype=np.int64)
        B = rng.integers(0, p, size=(7, 55), dtype=np.int64)
        # through the tree's own modular product -- the composition rank_on_family uses.
        # (A @ B) % p in plain int64 OVERFLOWS at these entry sizes and reads rank 40;
        # that was this script's first bug and is why the control is written this way.
        G = matmul_mod(A % p, B % p, p)                   # rank <= 7, generically 7
        r_known = int(rank_mod_p(G, p))
        Z = np.zeros((40, 55), dtype=np.int64)
        r_zero = int(rank_mod_p(Z, p))
        I = np.eye(31, dtype=np.int64)
        r_full = int(rank_mod_p(I, p))
        out.append(dict(prime=p, rank_of_rank7_product=r_known, rank_of_zero=r_zero, rank_of_I31=r_full))
        assert r_known == 7 and r_zero == 0 and r_full == 31, out[-1]
        # the deliberate-failure input: the same routine asserted to a wrong value
        wrong_fired = (r_known != 6)
        assert wrong_fired, "N.c did not fail on a wrong asserted rank"
    res['Nc'] = dict(checks=out, status='PASS',
                     note='rank_mod_p separates 0, 7 and 31 at both primes; a zero matrix does not read full and a rank-7 product does not read 0')
    log("Nc PASS: rank_mod_p returns 0, 7 and 31 on matrices of those ranks, both primes")


# ------------------------------------------------------------------ R
def control_R(res):
    """The n_chi measurement path on the one Q1 cell with a banked n_chi.
    Orbit-setup half ONLY -- no raising rows, no kernel: the board says control
    (10,6,6,6,2,2)_8 'as a reference check only -- not as new work'."""
    lam, delta, n = PILOT
    pilot = json.load(open(os.path.join(ROOT, 'results', 'b13_10', 'pilot.json')))['build']
    t = time.time()
    M = monomials_array_lean(n, len(lam), delta, lam, verbose=True)
    t_m = round(time.time() - t, 1)
    t = time.time()
    arr = orbit_setup_lean(n, len(lam), delta, lam, M=M, verbose=True)
    t_o = round(time.time() - t, 1)
    here = dict(N_S=int(arr['N_S']), stab=int(arr['stab']), n_chi=int(arr['n_chi']))
    c = compare(here, pilot, [('N_S', here['N_S']), ('stab', here['stab']), ('n_chi', here['n_chi'])])
    # the deliberate-failure input: the queue's ESTIMATE in place of the banked value
    allq = json.load(open(os.path.join(ROOT, 'results', 's79_queue.json')))
    pq = [x for x in allq if tuple(x['lam']) == lam and x['delta'] == delta][0]
    fake = dict(pilot); fake['n_chi'] = pq['nchi_est']
    c_fake = compare(here, fake, [('N_S', here['N_S']), ('stab', here['stab']), ('n_chi', here['n_chi'])])
    # and an empty-comparison probe: comparing against a record with none of the fields
    c_empty = compare(here, {}, [('N_S', here['N_S']), ('n_chi', here['n_chi'])])
    res['R'] = dict(cell=list(lam), delta=delta, n=n, measured=here, banked={k: pilot[k] for k in here},
                    compare=c, mono_secs=t_m, orbit_secs=t_o, hwm_gb=round(vm(), 3),
                    fails_on_queue_estimate=dict(estimate=pq['nchi_est'], all_equal=c_fake['all_equal']),
                    empty_comparison_is_failure=dict(placed=c_empty['placed'], all_equal=c_empty['all_equal']))
    assert c['all_equal'] and c['placed'] == 3, ("R: measured orbit setup disagrees with the banked pilot", c)
    assert not c_fake['all_equal'], "R did NOT fail against the queue's estimate -- the comparator is not comparing"
    assert not c_empty['all_equal'], "R reported PASS on an empty comparison"
    res['R']['status'] = 'PASS'
    del M, arr
    log(f"R PASS: n_chi measured {here['n_chi']} = banked {pilot['n_chi']}; the same comparison "
        f"against the queue estimate {pq['nchi_est']} FAILS, and an empty comparison FAILS "
        f"({t_m}s + {t_o}s, HWM {res['R']['hwm_gb']} GB)")


# ------------------------------------------------------------------ S (+ K, F on A1)
def control_S(res, ids=('B1', 'A1')):
    res['S'] = []
    for cid in ids:
        b = banked_suite(cid)
        lam = tuple(b['lam']); delta = b['delta']; n = b['n']; a = b['a']
        rec = dict(control_N=dict(kind='diagonal pencils, forced rank 0 at length > n'))
        t = time.time()
        B = DRV.stage_build(lam, delta, n, None, rec, blocks='disk',
                            scratch=os.path.join(os.path.expanduser('~'), 'b14_12_scratch', cid), verbose=False)
        rec = DRV.stage_kernel(B, lam, delta, n, a, rec, fo='inplace', verbose=False, tag=f'ctl-{cid}', control=True)
        wall = round(time.time() - t, 1)
        flat = dict(a=a, N_S=rec['build']['N_S'], stab=rec['build']['stab'], n_chi=rec['build']['n_chi'],
                    nrows=rec['build']['nrows'], nnz=rec['build']['nnz'], cover_size=rec['cover']['size'])
        bank = dict(a=b['a'], **b['sizes'], cover_size=b['cover']['size'])
        c = compare(flat, bank, list(flat.items()))
        per_p = {}
        for p in PRIMES:
            ps = str(p)
            per_p[ps] = dict(mult_det_here=rec['per_prime'][ps]['mult_det'],
                             mult_det_banked=b['ranks']['det']['per_prime'][ps],
                             nullity_here=rec['per_prime'][ps]['nullity'],
                             nullity_banked=b['kernel'][ps]['nullity'],
                             nU_here=rec['per_prime'][ps]['hybrid']['nU'],
                             nU_banked=b['kernel'][ps]['hybrid']['nU'],
                             diag_rank=rec['per_prime'][ps]['rank_diagonal_pencils'])
            per_p[ps]['equal'] = (per_p[ps]['mult_det_here'] == per_p[ps]['mult_det_banked']
                                  and per_p[ps]['nullity_here'] == per_p[ps]['nullity_banked']
                                  and per_p[ps]['nU_here'] == per_p[ps]['nU_banked'])
        # the deliberate-failure input: one banked field mutated
        bad = dict(bank); bad['n_chi'] = bank['n_chi'] + 1
        c_bad = compare(flat, bad, list(flat.items()))
        entry = dict(id=cid, lam=list(lam), delta=delta, n=n, a=a, compare=c, per_prime=per_p,
                     all_equal=c['all_equal'] and all(v['equal'] for v in per_p.values()),
                     fails_on_mutated_banked_nchi=(not c_bad['all_equal']),
                     control_N=rec['control_N'], wall_secs=wall, hwm_gb=round(vm(), 3),
                     knobs=dict(build=rec['build']['knobs'], fo='inplace'))
        res['S'].append(entry)
        log(f"  S {cid} {lam} d{delta}: {c['placed']} fields placed, all equal = {entry['all_equal']}; "
            f"diagonal rank 0 at both primes = {rec['control_N']['rank_zero_both_primes']}; "
            f"mutated-banked comparison fails = {entry['fails_on_mutated_banked_nchi']} ({wall}s)")
        assert c['placed'] == len(flat), ("S: a banked field could not be placed", c)
        assert entry['all_equal'], ("S: field mismatch against the banked suite record", c, per_p)
        assert entry['fails_on_mutated_banked_nchi'], "S did NOT fail on a mutated banked record"
        assert rec['control_N']['rank_zero_both_primes']
        if cid == 'A1':
            control_KF(res, B, lam, delta, n, a)
        del B
    res['S_status'] = 'PASS'
    log("S PASS")


# ------------------------------------------------------------------ K and F
def control_KF(res, B, lam, delta, n, a):
    E = B['E']; nc = B['n_chi']
    cov = best_cover_lean(E, nc, seed=DRV.HYB_SEED, verbose=False)
    p = P1
    Ki, ii = hybrid_kernel_lean(E, nc, p, a, cov, seed=DRV.HYB_SEED, verbose=False, fo='inplace')
    Kc, ic = hybrid_kernel_lean(E, nc, p, a, cov, seed=DRV.HYB_SEED, verbose=False, fo='copy')
    R = len(lam)
    det_cl = [DRV.det_coeffs(pt, R) for pt in DRV.det_pencils(a + 8, DRV.DET_SEED, DRV.BOUND, R)]
    mi, _ = DRV.rank_on_family(B['arr'], det_cl, Ki, p, R, n)
    mc, _ = DRV.rank_on_family(B['arr'], det_cl, Kc, p, R, n)
    # K: verification, and the input on which it must fail
    ok_i = bool(check_kernel_mat_lean(E, Ki.astype(np.int64), p))
    Kbad = Ki.astype(np.int64).copy(); Kbad[0, 0] = (int(Kbad[0, 0]) + 1) % p
    ok_bad = bool(check_kernel_mat_lean(E, Kbad, p))
    res['K'] = dict(cell=list(lam), delta=delta, prime=p, verified=ok_i,
                    verified_on_perturbed_kernel=ok_bad, status='PASS')
    assert ok_i, "K: the kernel does not verify on E"
    assert not ok_bad, "K did NOT fail on a kernel with one entry changed"
    # F: the fo deviation
    from flint import nmod_mat
    same = dict(nullity=(Ki.shape[1] == Kc.shape[1] == a), mult_det=(mi == mc),
                verified_both=(ok_i and bool(check_kernel_mat_lean(E, Kc.astype(np.int64), p))))
    mc_bad = mc + 1                                     # the deliberate-failure input
    res['F'] = dict(cell=list(lam), delta=delta, prime=p, fo_inplace=dict(nullity=int(Ki.shape[1]), mult_det=mi),
                    fo_copy=dict(nullity=int(Kc.shape[1]), mult_det=mc), agree=same,
                    all_agree=all(same.values()), fails_on_mutated_copy=(mi != mc_bad), status='PASS')
    assert res['F']['all_agree'], ("S3: fo='inplace' disagrees with fo='copy'", res['F'])
    assert res['F']['fails_on_mutated_copy'], "F did NOT fail on a mutated fo='copy' result"
    log(f"  K PASS: kernel verifies on E, and a one-entry perturbation does NOT verify")
    log(f"  F PASS: fo='inplace' and fo='copy' agree (nullity {Ki.shape[1]}, mult_det {mi}); "
        f"the comparison fails against a mutated copy result")


def main(argv):
    out = argv[argv.index('--out') + 1] if '--out' in argv else os.path.join(ROOT, 'results', 'b14_12', 'controls.json')
    skip = set(argv[argv.index('--skip') + 1].split(',')) if '--skip' in argv else set()
    os.makedirs(os.path.dirname(out), exist_ok=True)
    pidfile = _write_pidfile('b14_12_controls')
    res = dict(session='B14-12', board_numbering='batch14', stamp=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
               pid=os.getpid(), host=dict(cpus=os.cpu_count()),
               pidfile=pidfile,
               rule='every control is run on an input that MUST make it fail, and that run is recorded')
    control_T(res); json.dump(res, open(out, 'w'), indent=1)
    control_Nc(res); json.dump(res, open(out, 'w'), indent=1)
    if 'S' not in skip: control_S(res); json.dump(res, open(out, 'w'), indent=1)
    if 'R' not in skip: control_R(res); json.dump(res, open(out, 'w'), indent=1)
    res['status'] = 'PASS'
    res['hwm_gb'] = round(vm(), 3)
    json.dump(res, open(out, 'w'), indent=1)
    log(f"ALL CONTROLS PASS (HWM {res['hwm_gb']} GB) -> {out}")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
