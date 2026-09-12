#!/usr/bin/env python3
"""
B14-09 -- decide one open six-row degree-10 cell, with the per-cell controls the
pre-registration requires.

One cell per process, so the process bound (`timeout`, `ulimit -v`) is the cell
bound and a cell that does not fit is recorded as NOT REACHED with the bound it
did not fit inside, rather than taking the sweep down with it.

The decision is the house engine, unmodified: `wk13_b08_per6_lean` (which is
`wk12_s79_per6.measure_weight` with B13-08's two memory-only changes and
`matmul_mod_wide` installed).  Nothing here changes what is computed.

What is added is two controls, both of which can fail:

  C5  the pre-registered `n_chi`.  `results/b14_09/sizing.json` was committed
      BEFORE any build, carrying an exact character-sum `n_chi` for all 58.  The
      builder measures `n_chi` by an entirely different route -- enumerate all
      N_S monomials, canonicalise under Stab_W(mu), keep the twisted orbits that
      survive.  They must agree exactly.  This is the sharpest possible test of
      the sizing instrument: a registered prediction against a measurement, at
      the cells it was built for.

  C6  `PROVED.md: negative_control_forced`, required on every evaluation-rank
      sweep.  A diagonal per_3 pencil is a product of three linear forms, whose
      coordinate ring carries no constituent of more than three rows, so a
      length-6 weight MUST read evaluation rank 0.  Run on the same kernel K at
      both primes, together with the positive side (the per_3 family must read
      rank a on that same K) and the det_3 family (must read <= a).  The
      diagonal pencil is independently verified to BE the product of its three
      diagonal linear forms before it is used, so the control's own input is
      checked.

usage:
  python3 analysis/b14_09_sweep.py --rank 349 [--out results/b14_09/per6_d10.jsonl]
  python3 analysis/b14_09_sweep.py --list
"""
import sys, os, time, json, random
for _v in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ.setdefault(_v, '1')
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
os.environ.setdefault('S71_SCHUR_SO', '/home/claude/b14_09/schur.so')
os.environ.setdefault('S71_MEM_X', '250000000')
import numpy as np

SIZING = os.path.join(ROOT, 'results/b14_09/sizing.json')
NEG_SEED = 20260909


def log(*a):
    print(*a, file=sys.stderr); sys.stderr.flush()


def sizing():
    return {c['rank']: c for c in json.load(open(SIZING))['cells']}


def negative_control(B, Ks, mu, a, want_terms=True):
    """C6.  Diagonal per_3 pencils -> rank 0; per_3 pencils -> rank a; det_3 -> <= a."""
    from wk12_s79_per6 import per3_pencils, per3_coeffs, R, n3, PRIMES, SEED, BOUND
    from wk8_s30_core import det_form, restrict
    from wk12_s79_cell6 import ev_rows_from_coeffs
    from wk13_b08_per6_lean import matmul_mod_wide
    from wk11_s71_hybrid import rank_mod_p
    DET3, N_DET3 = det_form(3)
    Kp = a + 8
    rnd = random.Random(NEG_SEED)
    dpts = [[[[ (rnd.randint(-BOUND, BOUND) if x == y else 0) for x in range(3)] for y in range(3)]
             for _ in range(R)] for _ in range(Kp)]
    dco = [per3_coeffs(pt) for pt in dpts]
    # the control's own input is checked: a diagonal pencil's per_3 IS the product
    # of its three diagonal linear forms, multiplied out here independently.
    for pt, co in zip(dpts, dco):
        prod = {tuple([0] * R): 1}
        for aa in range(3):
            nxt = {}
            for al, c in prod.items():
                for i in range(R):
                    v = pt[i][aa][aa]
                    if v == 0: continue
                    k = list(al); k[i] += 1
                    nxt[tuple(k)] = nxt.get(tuple(k), 0) + c * v
            prod = nxt
        assert {k: v for k, v in prod.items() if v} == {k: v for k, v in co.items() if v}, \
            "diagonal pencil is not the product of its three linear forms"
    def det3_coeffs(pencil):
        As = [[pencil[i][x][y] for x in range(3) for y in range(3)] for i in range(R)]
        return restrict(DET3, N_DET3, 3, R, As)
    ppts = per3_pencils(Kp, SEED, BOUND)
    pco = [per3_coeffs(pt) for pt in ppts]
    tco = [det3_coeffs(pt) for pt in ppts]
    out = dict(diag_seed=NEG_SEED, points=Kp, per_prime={})
    for p in PRIMES:
        Kp_ = np.asarray(Ks[p] % p, dtype=np.int64)
        def rk(co):
            parts = []
            for c0 in range(0, len(co), 8):
                EV = ev_rows_from_coeffs(B['arr'], co[c0:c0 + 8], p, R, n=3)
                parts.append(matmul_mod_wide(EV % p, Kp_, p)); del EV
            G = np.vstack(parts)
            return int(rank_mod_p(G, p)), bool(not np.any(G))
        rd, dz = rk(dco)
        rp, _ = rk(pco)
        rt, _ = rk(tco)
        out['per_prime'][str(p)] = dict(rank_diagonal_pencils=rd, rank_per3_pencils=rp,
                                        rank_det3_pencils=rt, diag_all_rows_zero=dz,
                                        values_are='ranks mod p of ev.K, no transform')
        log(f"  C6 {mu} p={p}: diagonal rank {rd} (must be 0, rows all zero={dz}); "
            f"per_3 rank {rp} (must be {a}); det_3 rank {rt} (must be <= {a})")
        out['per_prime'][str(p)]['pass'] = bool(rd == 0 and rp == a and rt <= a)
    out['C6'] = 'PASS' if all(v['pass'] for v in out['per_prime'].values()) else 'FAIL'
    return out


def run(rank, outp):
    S = sizing()
    if rank not in S:
        sys.exit(f"rank {rank} is not one of the 58 open cells")
    cell = S[rank]
    mu = tuple(cell['mu']); a = cell['a']
    pred_nchi = cell['n_chi']
    log(f"== rank {rank} mu={mu} a={a}  PRE-REGISTERED n_chi = {pred_nchi} "
        f"(N_S={cell['N_S']}, |Stab|={cell['stab']}, wide={cell['needs_matmul_mod_wide']}) ==")
    from wk13_b08_per6_lean import measure_weight_lean
    t0 = time.time()
    res, Ks, B = measure_weight_lean(mu, 10, verbose=True, a_given=a, want_K=True)
    res['rank'] = rank
    res['C5_pre_registered_n_chi'] = dict(predicted=pred_nchi, measured=int(res['n_chi']),
                                          agree=bool(int(res['n_chi']) == pred_nchi),
                                          predicted_at='results/b14_09/sizing.json, committed before any build',
                                          instrument='exact character sum, analysis/b14_09_sizing.py')
    res['C5'] = 'PASS' if res['C5_pre_registered_n_chi']['agree'] else 'FAIL'
    res['wide_used'] = bool(int(res['n_chi']) >= (1 << 21))
    res['C6_negative_control'] = negative_control(B, Ks, mu, a)
    res['C6'] = res['C6_negative_control']['C6']
    res['total_secs'] = round(time.time() - t0, 1)
    res['host'] = dict(cpus=2, ram_mb=8023, swap=0)
    with open(outp, 'a') as f:
        f.write(json.dumps(res) + "\n")
    log(f"== rank {rank} {mu}: mult={res['mult']} units={res['units']} C5={res['C5']} C6={res['C6']} "
        f"[{res['total_secs']}s, HWM {res['hwm_gb']} GB] ==")
    if res['C5'] != 'PASS':
        sys.exit("C5 FAILED: the pre-registered n_chi does not match the build. "
                 "The sizing table is withdrawn, per the decision table.")
    if res['C6'] != 'PASS':
        sys.exit("C6 FAILED: negative_control_forced did not hold. Sweep halts.")
    if res['halt']:
        sys.exit("HALT: units >= 1 or primes disagree -- the verification protocol takes over.")
    return 0


def main():
    args = sys.argv[1:]
    if '--list' in args:
        S = sizing()
        for c in sorted(S.values(), key=lambda d: d['pred_total_secs']):
            print(f"{c['rank']:>4} {str(tuple(c['mu'])):<22} a={c['a']:<3} n_chi={c['n_chi']:>9} "
                  f"pred {c['pred_total_secs']:>8.0f}s {c['pred_peak_gb']:>6.2f} GB "
                  f"{'WIDE' if c['needs_matmul_mod_wide'] else ''}")
        return 0
    rank = int(args[args.index('--rank') + 1])
    outp = args[args.index('--out') + 1] if '--out' in args else 'results/b14_09/per6_d10.jsonl'
    return run(rank, os.path.join(ROOT, outp))


if __name__ == '__main__':
    sys.exit(main())
