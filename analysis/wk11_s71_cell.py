#!/usr/bin/env python3
"""
Session 71 -- one closing cell, three evaluation families, by the hybrid route.

    a          = dim HWV_lam (Weyl alternation, asserted = census a_inf)
    K          = the exact mod-p kernel of E on V_chi (n_chi x a), by the hybrid
                 route (wk11_s71_hybrid: initial-term cover + Schur residual),
                 every vector verified on the full E, both primes
    mult_det   = rank_p(ev_det  . K)    K_pts = a + 8 det_4 pencils, seed 11   (session 60's points)
    mult_per4  = rank_p(ev_per4 . K)    K_pts       unpadded per_4 pencils, seed 47
    mult_red   = rank_p(K[non-red rows])            point-free, Theorem (star)
    mult_red'  = rank_p(ev_red  . K)    K_pts       reducible points l.c, seed 29 (session 60's)

A full rank (= a) at ONE prime proves the corresponding mult = a over Q
(docs/sparse_det_route.md Lemma 2: rank_p <= rank_Q, and mult <= a); a drop is
a measurement until the verification protocol of results/PREREG_s71.md sec. 7.
i_det = a - mult_det, i_red = a - mult_red, i_per4 = a - mult_per4,
D = i_det - i_red = mult_red - mult_det; the falsifier is D > 0.

The sieve: the cover of E_red reaching n_red certifies nullity_p(E_red) = 0,
i.e. mult_red = a, i_red = 0, at O(nnz) with no rank; recorded per cell.

usage: python3 analysis/wk11_s71_cell.py delta lam1 .. lam5 [--a A] [--hpad H] [--out FILE]
          [--certs DIR] [--sequential] [--bound 40] [--npts K]
prints one JSON line (RESULT ...) and appends it to --out.
"""
import sys, os, time, json, gzip
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
os.environ.setdefault('WIED_BIN', '/home/claude/s71/wied71')
os.environ.setdefault('WIED_WORK', '/home/claude/s71/work')
import numpy as np
from scipy import sparse
import wk11_s71_codes; wk11_s71_codes.install()
from wk8_s30_core import exps, restrict, det_form, per_form, P1, P2
from wk9_s45_build import build_cell, log, _rss_gb
from wk9_s42_census import a_weyl
from wk9_s60_cell import (det_pencils, det_coeffs, reducible_points, red_coeffs, ev_rows_from_coeffs,
                          red_mask, point_record, CONVENTIONS)
from wk11_s71_hybrid import best_cover, hybrid_kernel, matmul_mod, rank_mod_p, rank_tall, nullspace_mod_p

N = 4
R = 5
PRIMES = (P1, P2)
PER4, N_PER = per_form(4)
SEEDS = dict(det=11, red=29, per4=47)
HYB_SEED = 20260908


def per4_coeffs(pencil):
    As = [[pencil[i][a][b] for a in range(4) for b in range(4)] for i in range(R)]
    return restrict(PER4, N_PER, N, R, As)


_SHARED = {}


def _prime_job(args):
    p, opts = args
    B = _SHARED['B']; arr = B['arr']; E = B['E']; nc = B['n_chi']; a = opts['a']
    red = _SHARED['red']; nonred = np.nonzero(~red)[0]
    cov = _SHARED['cov']
    t0 = time.time()
    out = dict(prime=p, sides={})
    K, info = hybrid_kernel(E, nc, p, a, cov, seed=HYB_SEED, tag=f"[{opts['tag']}]", verbose=opts['verbose'])
    out['hybrid'] = info
    t = time.time()
    fam = {}
    fam['det'] = ev_rows_from_coeffs(arr, [det_coeffs(pt) for pt in opts['det_pts']], p)
    fam['per4'] = ev_rows_from_coeffs(arr, [per4_coeffs(pt) for pt in opts['per4_pts']], p)
    fam['red_pts'] = ev_rows_from_coeffs(arr, [red_coeffs(pt) for pt in opts['red_pts']], p)
    out['ev_secs'] = round(time.time() - t, 1)
    t = time.time()
    G = {}
    for name, EV in fam.items():
        G[name] = matmul_mod(EV % p, K % p, p)              # K_pts x a
        m = rank_mod_p(G[name], p)
        out['sides'][name] = dict(mult=int(m), nullity=int(a - m), instrument=f'hybrid kernel + {name} evaluation rows')
    # (star): kernel vectors supported on the red columns
    if len(nonred):
        mstar = rank_tall(K[nonred], p)
    else:
        mstar = 0
    out['sides']['red_star'] = dict(mult=int(mstar), nullity=int(a - mstar), instrument='hybrid kernel + (star)')
    out['rank_secs'] = round(time.time() - t, 1)
    if opts['hpad'] is not None:
        assert mstar <= opts['hpad'], ('mult_red exceeds the normalisation bound h_pad', mstar, opts['hpad'])
    # ideal vectors on the determinant side (the falsifier object), kept when they exist
    if out['sides']['det']['mult'] < a:
        cs = nullspace_mod_p(G['det'].T, p)                 # combos c with ev_det K c = 0
        out['det_ideal_chi'] = ((cs @ K.T) % p).tolist()     # vectors in chi-coordinates
    if opts['keep_kernel'] and nc * a <= 400_000:
        out['kernel_chi'] = K.T.tolist()
    out['secs'] = round(time.time() - t0, 1)
    out['hwm_gb'] = round(_rss_gb(), 2)
    return out


def measure_cell(lam, delta, a_given=None, hpad=None, bound=40, npts=None, parallel=True, verbose=True,
                 certs=None, keep_kernel=True):
    lam = tuple(lam)
    assert len(lam) == R and sum(lam) == N * delta
    t0 = time.time()
    B = build_cell(lam, delta, n=N, verbose=verbose)
    a = a_weyl(lam, delta, N, {})
    if a_given is not None:
        assert a == a_given, ('a: census value disagrees with the Weyl alternation', lam, delta, a_given, a)
    nc = B['n_chi']; E = B['E']
    Kp = npts if npts else a + 8
    out = dict(lam=list(lam), delta=delta, ell=R, a=a, K=Kp, N_S=B['N_S'], stab=B['stab'], n_chi=nc,
               nrows=B['nrows'], nnz=B['nnz'], nfixed=B['nfixed'], build_secs=round(B['build_secs'], 1),
               build_hwm_gb=round(B['hwm_gb'], 2), route='hybrid', h_pad=hpad,
               seeds=dict(det=SEEDS['det'], red=SEEDS['red'], per4=SEEDS['per4'], hybrid=HYB_SEED), bound=bound, primes=list(PRIMES))
    if a == 0:
        out.update(status='a=0', secs=round(time.time() - t0, 1)); return out
    # ---- the sieve
    t = time.time()
    red = red_mask(B['arr']); nred = int(red.sum()); out['n_red'] = nred
    cov = best_cover(E, nc, seed=HYB_SEED)
    out['cover_E'] = dict(size=cov['size'], order=cov['order'], stats=cov['stats'], n_chi=nc, a=a,
                          excess=int(nc - cov['size'] - a), certified_rank_lb=cov['size'])
    if nred:
        Ered = E[:, np.nonzero(red)[0]].tocsr(); Ered.eliminate_zeros()
        Ered = Ered[np.nonzero(np.diff(Ered.indptr) > 0)[0]]
        cr = best_cover(Ered, nred, seed=HYB_SEED)
        out['cover_Ered'] = dict(size=cr['size'], order=cr['order'], stats=cr['stats'], n_red=nred,
                                 certified=bool(cr['size'] == nred))
        del Ered
    else:
        out['cover_Ered'] = dict(size=0, n_red=0, certified=True, note='no red columns: mult_red = 0 by (star)')
    out['sieve_secs'] = round(time.time() - t, 1)
    if verbose:
        log(f"  sieve {lam} d{delta}: cover(E) {cov['size']}/{nc} by {cov['order']} (a={a}, |U|={nc - cov['size']}, "
            f"excess {nc - cov['size'] - a}; {cov['stats']}); cover(E_red) {out['cover_Ered']['size']}/{nred}"
            f"{' CERTIFIED i_red = 0' if out['cover_Ered']['certified'] else ''} ({out['sieve_secs']}s)")
    # ---- points (fixed seeds)
    det_pts = det_pencils(Kp, SEEDS['det'], bound)
    per4_pts = det_pencils(Kp, SEEDS['per4'], bound)
    red_pts = reducible_points(Kp, SEEDS['red'], bound)
    opts = dict(a=a, det_pts=det_pts, per4_pts=per4_pts, red_pts=red_pts, hpad=hpad, verbose=verbose,
                tag='_'.join(map(str, lam)) + f'd{delta}', keep_kernel=keep_kernel)
    _SHARED['B'] = B; _SHARED['red'] = red; _SHARED['cov'] = cov
    jobs = [(p, opts) for p in PRIMES]
    nU = nc - cov['size']
    mem_x = 4.0 * cov['size'] * nU
    out['pred_mem_x_bytes'] = int(mem_x)
    if parallel and 2 * mem_x < 2.5e9:
        import multiprocessing as mp
        with mp.get_context('fork').Pool(2) as pool:
            res = pool.map(_prime_job, jobs)
        out['primes_concurrent'] = True
    else:
        res = [_prime_job(j) for j in jobs]
        out['primes_concurrent'] = False
    _SHARED.clear()
    out['per_prime'] = {str(r['prime']): {k: v for k, v in r.items() if k not in ('prime', 'kernel_chi', 'det_ideal_chi')} for r in res}
    sides = {}
    for sd in ('det', 'per4', 'red_star', 'red_pts'):
        vals = {r['prime']: r['sides'][sd]['mult'] for r in res}
        agree = len(set(vals.values())) == 1
        sides[sd] = dict(mult=(vals[PRIMES[0]] if agree else None), per_prime={str(p): v for p, v in vals.items()},
                         primes_agree=agree, instrument=res[0]['sides'][sd]['instrument'])
        if not agree: sides[sd]['status'] = 'PRIMES DISAGREE'
        elif vals[PRIMES[0]] == a: sides[sd]['status'] = 'proved (full rank at both primes: mult = a over Q)'
        elif sd == 'red_star' and hpad is not None and vals[PRIMES[0]] == hpad:
            sides[sd]['status'] = 'proved (rank = h_pad at both primes: (star) <= h_pad meets the exhibited kernel)'
        else: sides[sd]['status'] = 'measured (exact mod both primes, kernel exhibited): mult = %d' % vals[PRIMES[0]]
    out['sides'] = sides
    out['mult_det'] = sides['det']['mult']; out['mult_per4'] = sides['per4']['mult']
    out['mult_red_star'] = sides['red_star']['mult']; out['mult_red_pts'] = sides['red_pts']['mult']
    out['mult_red'] = out['mult_red_star']
    out['star_eq_pts'] = (out['mult_red_pts'] == out['mult_red_star'])
    if out['cover_Ered']['certified']:
        assert out['mult_red_star'] == a, ('sieve certified i_red = 0 but (star) rank disagrees', out['mult_red_star'], a)
    ok = all(s['primes_agree'] for s in sides.values()) and out['star_eq_pts']
    if ok:
        out['i_det'] = a - out['mult_det']; out['i_red'] = a - out['mult_red']; out['i_per4'] = a - out['mult_per4']
        out['D'] = out['i_det'] - out['i_red']
    else:
        out['i_det'] = out['i_red'] = out['i_per4'] = out['D'] = None
    out['refute'] = bool(out['D'] is not None and out['D'] > 0)
    out['halt'] = bool(not ok or out['refute'] or (out['i_det'] is not None and out['i_det'] > 0) or (out['i_per4'] is not None and out['i_per4'] > 0))
    out['ok'] = ok
    out['secs'] = round(time.time() - t0, 1)
    out['hwm_gb'] = round(max(_rss_gb(), max(r['hwm_gb'] for r in res)), 2)
    if verbose:
        log(f"  RESULT {lam} d{delta}: a={a} n_chi={nc} |U|={nU} mult_det={out['mult_det']} mult_per4={out['mult_per4']} "
            f"mult_red(star)={out['mult_red_star']} mult_red(pts)={out['mult_red_pts']} i_det={out['i_det']} i_red={out['i_red']} "
            f"i_per4={out['i_per4']} D={out['D']}{'  *** HALT ***' if out['halt'] else ''}  ({out['secs']}s, HWM {out['hwm_gb']} GB)")
    if certs:
        os.makedirs(certs, exist_ok=True)
        tagl = '_'.join(map(str, lam)) + f'_d{delta}'
        files = []
        for r in res:
            p = r['prime']
            cert = {"format": "gct-cert/1", "kind": "hybrid_kernel",
                    "title": f"mod-{p} kernel of the raising operator at {tuple(lam)}, degree {delta}, by the hybrid route; "
                             f"mult_det={r['sides']['det']['mult']}, mult_per4={r['sides']['per4']['mult']}, "
                             f"mult_red(star)={r['sides']['red_star']['mult']}, mult_red(pts)={r['sides']['red_pts']['mult']}, a={a} (session 71)",
                    "produced_by": "analysis/wk11_s71_cell.py (session 71)",
                    "cell": {"n": N, "r": R, "lambda": [int(x) for x in lam], "delta": int(delta), "a": int(a)},
                    "conventions": dict(CONVENTIONS), "field": f"F_{p}", "prime": int(p),
                    "sizes": {"N_S": int(B['N_S']), "stab": int(B['stab']), "n_chi": int(nc), "n_red": int(nred),
                              "rows_E": int(B['nrows']), "nnz_E": int(B['nnz'])},
                    "recipe": {"cover_order": cov['order'], "cover_size": int(cov['size']), "orders_tried": cov['stats'],
                               "projection_seed": HYB_SEED, "attempts": r['hybrid']['attempts'],
                               "points": {"det": {"seed": SEEDS['det'], "bound": bound, "count": Kp},
                                          "per4": {"seed": SEEDS['per4'], "bound": bound, "count": Kp},
                                          "reducible": {"seed": SEEDS['red'], "bound": bound, "count": Kp}},
                               "note": "the cover rows, S, U and the projection are reproducible from the order name and seeds; "
                                       "a checker rebuilds E on V_chi, recomputes the cover, verifies E K = 0 and rank K = a for the "
                                       "recorded kernel (when recorded), and re-derives the four ranks"},
                    "claims": {"nullity_p_E": int(a), "mult_det": r['sides']['det']['mult'], "mult_per4": r['sides']['per4']['mult'],
                               "mult_red_star": r['sides']['red_star']['mult'], "mult_red_pts": r['sides']['red_pts']['mult'],
                               "field_note": "a full rank mod p proves mult = a over Q (rank_p <= rank_Q); a kernel mod p bounds i from below only"},
                    "points": {"det": [point_record('det_pencil', pt) for pt in det_pts],
                               "per4": [{"type": "per4_pencil", "pencil": pt} for pt in per4_pts],
                               "reducible": [point_record('reducible', pt) for pt in red_pts]}}
            if 'kernel_chi' in r: cert['kernel_chi'] = r['kernel_chi']
            if 'det_ideal_chi' in r: cert['det_ideal_chi'] = r['det_ideal_chi']
            fn = os.path.join(certs, f'{tagl}_hybrid_p{p}.json.gz')
            with gzip.open(fn, 'wt', encoding='utf-8') as f:
                json.dump(cert, f, separators=(',', ':'))
            files.append([os.path.relpath(fn, ROOT), os.path.getsize(fn)])
        out['certs'] = files
    # keep the ideal vectors out of the record line but on disk, when they exist
    if any('det_ideal_chi' in r for r in res):
        import pickle
        kd = os.environ.get('S71_KERN_DIR', '/home/claude/s71/kern'); os.makedirs(kd, exist_ok=True)
        pickle.dump(dict(res=out, ideal={r['prime']: r.get('det_ideal_chi') for r in res}, kernel={r['prime']: r.get('kernel_chi') for r in res}),
                    open(os.path.join(kd, f"ideal_{'_'.join(map(str, lam))}_d{delta}.pkl"), 'wb'))
    return out


if __name__ == '__main__':
    args = sys.argv[1:]
    def arg(name, default):
        return type(default)(args[args.index(name) + 1]) if name in args else default
    pos = []
    i = 0
    while i < len(args):
        if args[i].startswith('--') and i + 1 < len(args) and not args[i + 1].startswith('--') and args[i] not in ('--sequential',):
            i += 2
        elif args[i].startswith('--'):
            i += 1
        else:
            pos.append(int(args[i])); i += 1
    delta, lam = pos[0], tuple(pos[1:])
    res = measure_cell(lam, delta, a_given=(arg('--a', -1) if '--a' in args else None),
                       hpad=(arg('--hpad', -1) if '--hpad' in args else None), bound=arg('--bound', 40),
                       npts=arg('--npts', 0) or None, parallel=('--sequential' not in args), certs=arg('--certs', '') or None)
    print("RESULT " + json.dumps(res), flush=True)
    outp = arg('--out', '')
    if outp:
        with open(outp, 'a') as f: f.write(json.dumps(res) + "\n")
