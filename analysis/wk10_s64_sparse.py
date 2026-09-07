#!/usr/bin/env python3
"""Session 64 -- the padded side on the SPARSE route, for the discriminating
cells above the dense cap.

    mult_pad = a - nullity_Q [E; ev_pad]

by the session-45 Wiedemann certificates (wk9_s45_cell.nullity_stacked,
unchanged), the same instrument session 60 uses for [E; ev_det] and [E; ev_red].
ev_pad is built by the same ev_rows_from_coeffs contraction; only the
coefficient producer (wk10_s64_pad.pad_coeffs = restrict(PAD34)) differs.

For each cell we measure mult_pad at both house primes and >=2 seeds, optionally
mult_red on the SAME build (a same-machinery cross-check of P_5 = R_5), and
compare to the session-60 banked (mult_det, mult_red).  Exhibited kernel vectors
of [E; ev_pad] (and [E; ev_red]) are saved in chi-coordinates -- vectors in
ker E, directly comparable across sides for session 65.

usage: python3 analysis/wk10_s64_sparse.py cells.json [--seeds 2] [--with-red 0|1]
                [--levels cheap|s42|full] [--out results/s64_calibration.jsonl]
"""
import os, sys, json, time, gzip
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
os.environ.setdefault('WIED_BIN', '/home/claude/wied64')
os.environ.setdefault('WIED_WORK', '/home/claude/s64/work')
import numpy as np
from scipy import sparse
from flint import nmod_mat
from wk8_s30_core import P1, P2
from wk9_s45_build import build_cell, log, _rss_gb
from wk9_s45_cell import nullity_stacked, LEVELS
from wk9_s42_census import a_weyl
from wk9_s60_cell import (det_pencils, det_coeffs, reducible_points, red_coeffs,
                          ev_rows_from_coeffs, expand_vector)
from wk10_s64_pad import pad_frames, pad_coeffs

N = 4
PRIMES = (P1, P2)
KERN = os.path.join(ROOT, 'results/s64_kern')


def _mult_side(B, coeff_lists, a, tag, levels, seed0, want_kern):
    """nullity of [E; ev] at both primes for a family given as coeff dicts;
    returns dict(mult, per_prime, kern_terms) with kern in chi-coords."""
    arr = B['arr']; E = B['E']; nc = B['n_chi']
    per = {}; kern_terms = None
    for p in PRIMES:
        EV = ev_rows_from_coeffs(arr, coeff_lists, p)
        k, kern, lvl, diag = nullity_stacked(E, sparse.csr_matrix(EV), nc, p,
                                             want_kern=want_kern, seed0=seed0,
                                             tag=tag, levels=levels, verbose=True)
        per[p] = dict(nullity=int(k), mult=int(a - k), level=int(lvl))
        if want_kern and kern and p == PRIMES[0]:
            kern_terms = [expand_vector(arr, np.array(v, dtype=np.int64), p) for v in kern]
    agree = len(set(per[p]['mult'] for p in PRIMES)) == 1
    return dict(mult=(per[PRIMES[0]]['mult'] if agree else None),
                per_prime={str(p): per[p] for p in PRIMES}, primes_agree=agree,
                kern_terms=kern_terms)


def measure_sparse(lam, delta, seeds=2, with_red=False, levels='s42', bound=40, npts=None,
                   seed_det=11, seed_red=29, seed_pad=37, a_given=None, hpad=None):
    lam = tuple(lam); r = len(lam)
    t0 = time.time()
    B = build_cell(lam, delta, n=N, verbose=True)
    a = a_weyl(lam, delta, N, {})
    if a_given is not None: assert a == a_given, ('a mismatch', lam, delta, a, a_given)
    K = npts if npts else a + 8
    nc = B['n_chi']
    lv = LEVELS[levels]
    tag = 'c' + '_'.join(map(str, lam)) + f'd{delta}'
    out = dict(lam=list(lam), delta=delta, ell=r, a=a, K=K, N_S=B['N_S'], n_chi=nc,
               nrows=B['nrows'], nnz=B['nnz'], primes=list(PRIMES), route='sparse',
               h_pad=hpad, P5eqR5=(r <= 5), seeds=dict(det=seed_det, red=seed_red, pad=seed_pad, extra=seeds - 1))
    if a == 0:
        out.update(status='a=0', secs=round(time.time() - t0, 1)); return out

    # pad side (primary), >=2 seeds
    pad_variants = []
    for si in range(seeds):
        s = seed_pad + 1000 * si
        pts = pad_frames(K, s, bound, r)
        res = _mult_side(B, [pad_coeffs(V) for V in pts], a, tag + f'_pad{si}', lv, 1 + si, want_kern=(si == 0))
        pad_variants.append(res)
    mult_pad = max((v['mult'] for v in pad_variants if v['mult'] is not None), default=None)
    pad_kern_terms = pad_variants[0]['kern_terms']
    out['sides'] = dict(pad=dict(mult=mult_pad, per_seed=[v['mult'] for v in pad_variants],
                                 primes_agree=all(v['primes_agree'] for v in pad_variants),
                                 seeds_agree=len(set(v['mult'] for v in pad_variants)) <= 1,
                                 per_prime=pad_variants[0]['per_prime']))
    out['mult_pad'] = mult_pad; out['i_pad'] = (a - mult_pad) if mult_pad is not None else None

    red_kern_terms = None
    if with_red:
        rpts = reducible_points(K, seed_red, bound)
        rres = _mult_side(B, [red_coeffs(pt) for pt in rpts], a, tag + '_red', lv, 5, want_kern=True)
        out['sides']['red'] = dict(mult=rres['mult'], primes_agree=rres['primes_agree'],
                                   per_prime=rres['per_prime'])
        out['mult_red_measured'] = rres['mult']; red_kern_terms = rres['kern_terms']

    # save exhibited kernel vectors (chi-coords, monomial term expansion) for session 65
    if pad_kern_terms is not None or red_kern_terms is not None:
        os.makedirs(KERN, exist_ok=True)
        art = dict(cell=dict(n=N, r=r, lam=list(lam), delta=delta, a=a, n_chi=nc, prime=int(PRIMES[0])),
                   route='sparse',
                   note="exhibited kernel vectors of [E; ev_side] in chi/monomial coords (ker E ∩ I(side)); "
                        "compare U_pad vs U_red as subspaces of the monomial space",
                   U_terms={k: v for k, v in (('pad', pad_kern_terms), ('red', red_kern_terms)) if v is not None})
        with gzip.open(os.path.join(KERN, f"kern_{'_'.join(map(str, lam))}_d{delta}.json.gz"), 'wt', encoding='utf-8') as f:
            json.dump(art, f, separators=(',', ':'))
    out['secs'] = round(time.time() - t0, 1); out['hwm_gb'] = round(_rss_gb(), 2)
    log(f"  RESULT[sparse] {lam} d{delta}: a={a} n_chi={nc} mult_pad={mult_pad} "
        f"({out['secs']}s, HWM {out['hwm_gb']} GB)")
    return out


if __name__ == '__main__':
    cells = json.load(open(sys.argv[1]))
    def arg(name, d): return type(d)(sys.argv[sys.argv.index(name) + 1]) if name in sys.argv else d
    seeds = arg('--seeds', 2); with_red = bool(arg('--with-red', 0)); levels = arg('--levels', 's42')
    OUT = arg('--out', os.path.join(ROOT, 'results/s64_calibration.jsonl'))
    done = set()
    if os.path.exists(OUT):
        for ln in open(OUT):
            try:
                r = json.loads(ln)
                if r.get('route') == 'sparse' and r.get('mult_pad') is not None:
                    done.add((r['delta'], tuple(r['lam'])))
            except Exception: pass
    for c in cells:
        key = (c['delta'], tuple(c['lam']))
        if key in done: log(f"  skip (already banked sparse): {key}"); continue
        res = measure_sparse(c['lam'], c['delta'], seeds=seeds, with_red=with_red, levels=levels,
                             a_given=c.get('a'), hpad=c.get('hpad'))
        # calibration verdict vs banked
        bd = c.get('mult_det'); br = c.get('mult_red')
        mp = res.get('mult_pad')
        res['banked'] = dict(mult_det=bd, mult_red=br)
        res['calibration'] = dict(route='sparse',
            containment_ok=bool(mp is not None and br is not None and mp <= br),
            pad_eq_red=bool(mp == br), pad_le_det=bool(mp is not None and bd is not None and mp <= bd),
            r5_exact_ok=bool(mp == br) if res['ell'] <= 5 else None,
            PASS=bool(mp is not None and mp == br))
        with open(OUT, 'a') as f: f.write(json.dumps(res) + "\n")
        v = res['calibration']
        log(f"  BANKED[sparse] {key}: mult_pad={mp} vs banked mult_red={br} mult_det={bd} "
            f"| pad=red {v['pad_eq_red']} PASS={v['PASS']}")
        if mp is not None and br is not None and mp > br:
            log(f"  *** STOP: containment violated mult_pad {mp} > mult_red {br} at {key}"); sys.exit(2)
    log("sparse calibration done")
