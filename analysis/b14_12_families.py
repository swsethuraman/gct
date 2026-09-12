#!/usr/bin/env python3
"""
B14-12 stretch (results/PREREG_b14_12.md section 8, item 1) -- the three families the
determinant column did not need, on the operator already built, so that
(12,4,4,4,4,4)_8 has a COMPLETE session-79-schema row rather than a determinant
column alone.

B13-10 section 6.1 defect 3 records the same gap for its own pilot: the cell's result
"is in results/b13_10/pilot.json and is not merged into results/s79_cells.jsonl,
whose schema carries four families and not one."

Every convention, seed and instrument is session 79's own (wk12_s79_cell6):

    mult_det   det_4 pencils of length R                      seed 11
    mult_pad   TRUE padded permanent x_0.per_3 on an R-frame   seed 37
    mult_per4  unpadded per_4 pencils                          seed 47
    mult_red'  reducible points l.c                            seed 29   (mult_red_pts)
    mult_red   point-free, Theorem (star): rank of K on the non-red rows   (mult_red_star)

with K = a + 8 points and bound 40, both house primes.  Derived exactly as that
driver derives them: i_X = a - mult_X, D = mult_pad - mult_det,
D_R = mult_red - mult_det, monotone_ok = (mult_pad <= mult_red),
star_eq_pts = (mult_red_pts == mult_red_star).

A full rank at one prime proves mult = a over Q.  A drop is a ceiling on i and is
never read downward (PROVED.md: rank_floor, evaluation_cannot_certify_i_ge_1).

usage: python3 analysis/b14_12_families.py [--tag b14_12] [--lam ..] [--delta ..] [--n ..]
"""
import sys, os, time, json
for _v in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ.setdefault(_v, '1')
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
import numpy as np
import b14_12_cell as DRV
from wk8_s30_core import P1, P2
from wk9_s45_build import log
from wk11_s71_hybrid import rank_tall
from wk12_s79_cell6 import (det_pencils, det_coeffs, per4_coeffs, reducible_points, red_coeffs,
                            red_mask, SEEDS)
from wk10_s64_pad import pad_frames, pad_coeffs
from wk13_b10_lean import best_cover_lean, check_kernel_mat_lean, hybrid_kernel_lean

PRIMES = (P1, P2)
BOUND = 40


def main(argv):
    def arg(name, d=None): return argv[argv.index(name) + 1] if name in argv else d
    tag = arg('--tag', 'b14_12')
    lam = tuple(int(x) for x in arg('--lam', '12,4,4,4,4,4').split(','))
    delta = int(arg('--delta', '8')); n = int(arg('--n', '4')); R = len(lam)
    out = arg('--out', os.path.join(ROOT, 'results', 'b14_12', f'{tag}_families.json'))
    DRV._write_pidfile(f'{tag}_families')
    core = json.load(open(os.path.join(ROOT, 'results', 'b14_12', f'{tag}.json')))
    a = int(core['a'])
    B = DRV.load_build(os.path.join(DRV.OUTDIR, f'{tag}_E.npz'), lam)
    E = B['E']; arr = B['arr']; nc = B['n_chi']
    Kp = a + 8
    rec = dict(session='B14-12', board_numbering='batch14', kind='stretch: the three families the determinant column did not need',
               lam=list(lam), delta=delta, n=n, ell=R, a=a, K=Kp, bound=BOUND, seeds=dict(SEEDS),
               N_S=core['build']['N_S'], stab=core['build']['stab'], n_chi=nc,
               nrows=core['build']['nrows'], nnz=core['build']['nnz'], nfixed=core['build']['nfixed'],
               NS_delta=int(core['build']['N_S']) * delta, primes=list(PRIMES),
               pid=os.getpid(), stamp=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))

    t = time.time()
    red = red_mask(arr, R); nred = int(red.sum()); nonred = np.nonzero(~red)[0]
    rec['n_red'] = nred
    cov = best_cover_lean(E, nc, seed=DRV.HYB_SEED, verbose=False)
    rec['cover_E'] = dict(size=int(cov['size']), order=cov['order'], n_chi=nc, a=a,
                          excess=int(nc - cov['size'] - a), certified_rank_lb=int(cov['size']))
    if nred:
        Ered = E[:, np.nonzero(red)[0]].tocsr(); Ered.eliminate_zeros()
        Ered = Ered[np.nonzero(np.diff(Ered.indptr) > 0)[0]]
        cr = best_cover_lean(Ered, nred, seed=DRV.HYB_SEED, verbose=False)
        rec['cover_Ered'] = dict(size=int(cr['size']), order=cr['order'], n_red=nred,
                                 certified=bool(cr['size'] == nred))
        del Ered
    else:
        rec['cover_Ered'] = dict(size=0, n_red=0, certified=True, note='no red columns: mult_red = 0 by (star)')
    rec['sieve_secs'] = round(time.time() - t, 1)
    log(f"  [{tag}] sieve: n_red {nred}/{nc}; cover(E) {cov['size']}/{nc} |U| {nc-cov['size']}; "
        f"cover(E_red) {rec['cover_Ered']['size']}/{nred} certified={rec['cover_Ered']['certified']} ({rec['sieve_secs']}s)")

    fams = dict(det=[det_coeffs(pt, R) for pt in det_pencils(Kp, SEEDS['det'], BOUND, R)],
                pad=[pad_coeffs(V) for V in pad_frames(Kp, SEEDS['pad'], BOUND, R)],
                per4=[per4_coeffs(pt, R) for pt in det_pencils(Kp, SEEDS['per4'], BOUND, R)],
                red_pts=[red_coeffs(pt, R) for pt in reducible_points(Kp, SEEDS['red'], BOUND, R)])
    # the forced negative, carried again on this kernel (PROVED.md: negative_control_forced)
    diag_pts = DRV.diag_pencils(Kp, DRV.NEG_SEED, BOUND, R, n)
    fams['diag_control'] = [DRV.detn_coeffs(pt, R, n) for pt in diag_pts]
    assert all(DRV.diag_identity_ok(pt, R, n) for pt in diag_pts)
    assert not any(DRV.diag_identity_ok(pt, R, n) for pt in det_pencils(Kp, SEEDS['det'], BOUND, R)), \
        "N.a did not fail on generic det_4 pencils"

    per_prime = {}
    for p in PRIMES:
        t0 = time.time()
        K, info = hybrid_kernel_lean(E, nc, p, a, cov, seed=DRV.HYB_SEED, verbose=False, fo='inplace')
        assert bool(check_kernel_mat_lean(E, K.astype(np.int64), p)) and int(rank_tall(K, p)) == a
        ent = dict(nullity=int(K.shape[1]), hybrid=info, sides={})
        for name in ('det', 'pad', 'per4', 'red_pts', 'diag_control'):
            m, allzero = DRV.rank_on_family(arr, fams[name], K, p, R, n)
            ent['sides'][name] = dict(mult=int(m), nullity=int(a - m), all_rows_zero=allzero)
            log(f"  [{tag}] p={p} {name}: mult {m} (a = {a})")
        mstar = int(rank_tall(K[nonred], p)) if len(nonred) else 0
        ent['sides']['red_star'] = dict(mult=mstar, nullity=int(a - mstar), instrument='hybrid kernel + (star)')
        assert ent['sides']['diag_control']['mult'] == 0 and ent['sides']['diag_control']['all_rows_zero'], \
            "Control N failed on this kernel"
        assert ent['sides']['det']['mult'] > 0, "N.b did not fail on the generic det_4 family"
        ent['secs'] = round(time.time() - t0, 1); ent['hwm_gb'] = round(DRV.vm(), 3)
        per_prime[str(p)] = ent
        rec['per_prime'] = per_prime
        json.dump(rec, open(out, 'w'))
        del K

    sides = {}
    for sd in ('det', 'pad', 'per4', 'red_star', 'red_pts'):
        vals = {p: per_prime[str(p)]['sides'][sd]['mult'] for p in PRIMES}
        agree = len(set(vals.values())) == 1
        v = vals[PRIMES[0]]
        sides[sd] = dict(mult=(v if agree else None), per_prime={str(p): vv for p, vv in vals.items()},
                         primes_agree=agree,
                         status=('PRIMES DISAGREE' if not agree else
                                 'proved (full rank at both primes: mult = a over Q)' if v == a else
                                 f'measured (exact mod both primes): mult = {v} -- a CEILING on i, never read downward'))
    rec['sides'] = sides
    for k in ('det', 'pad', 'per4'):
        rec[f'mult_{k}'] = sides[k]['mult']
    rec['mult_red_star'] = sides['red_star']['mult']; rec['mult_red_pts'] = sides['red_pts']['mult']
    rec['mult_red'] = rec['mult_red_star']
    rec['star_eq_pts'] = (rec['mult_red_pts'] == rec['mult_red_star'])
    if rec['cover_Ered']['certified']:
        assert rec['mult_red_star'] == a, ('sieve certified i_red = 0 but (star) rank disagrees', rec['mult_red_star'], a)
    ok = all(s['primes_agree'] for s in sides.values()) and rec['star_eq_pts']
    if ok:
        for k in ('det', 'red', 'pad', 'per4'):
            rec[f'i_{k}'] = a - rec[f'mult_{k}']
        rec['D'] = rec['mult_pad'] - rec['mult_det']
        rec['D_R'] = rec['mult_red'] - rec['mult_det']
        rec['pad_lt_red'] = bool(rec['mult_pad'] < rec['mult_red'])
        rec['monotone_ok'] = bool(rec['mult_pad'] <= rec['mult_red'])
    else:
        for k in ('i_det', 'i_red', 'i_pad', 'i_per4', 'D', 'D_R'):
            rec[k] = None
        rec['pad_lt_red'] = rec['monotone_ok'] = None
    rec['refute'] = bool(rec['D'] is not None and rec['D'] > 0)
    rec['halt'] = bool(not ok or rec['refute'] or (rec['i_det'] or 0) > 0 or bool(rec['pad_lt_red']) or (rec['i_per4'] or 0) > 0)
    rec['ok'] = ok
    if 'mult_det' in core:
        rec['det_agrees_with_core'] = (rec['mult_det'] == core['mult_det'])
        assert rec['det_agrees_with_core'], ('the determinant column disagrees with the banked core run',
                                             rec['mult_det'], core['mult_det'])
    else:
        rec['det_agrees_with_core'] = None
        rec['det_cross_check'] = ('the core record carries no mult_det (build-only stage): the cross-check was '
                                  'NOT performed, and is recorded as not performed rather than as a pass')
    rec['hwm_gb'] = round(DRV.vm(), 3)
    json.dump(rec, open(out, 'w'))
    log(f"  RESULT {lam} d{delta}: a={a} n_chi={nc} det={rec['mult_det']} pad={rec['mult_pad']} per4={rec['mult_per4']} "
        f"red(star)={rec['mult_red_star']} red(pts)={rec['mult_red_pts']} i_det={rec['i_det']} i_pad={rec['i_pad']} "
        f"i_red={rec['i_red']} i_per4={rec['i_per4']} D={rec['D']} D_R={rec['D_R']} pad<red={rec['pad_lt_red']}"
        f"{'  *** HALT ***' if rec['halt'] else ''} (HWM {rec['hwm_gb']} GB)")
    print("B14_12_FAMILIES " + json.dumps({k: rec.get(k) for k in
          ('lam', 'delta', 'a', 'mult_det', 'mult_pad', 'mult_red', 'mult_per4',
           'i_det', 'i_pad', 'i_red', 'i_per4', 'D', 'D_R', 'monotone_ok', 'star_eq_pts', 'halt', 'ok')}))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
