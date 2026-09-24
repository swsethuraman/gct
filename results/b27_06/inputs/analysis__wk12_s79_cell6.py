#!/usr/bin/env python3
"""
Session 79, part 2 -- one cell of any length by the hybrid route, four families.

Session 71's driver (wk11_s71_cell.py) is fixed at R = 5.  This is the same
driver made length-general (R = len(lam)) on the unchanged engine:

    build      wk9_s45_build.build_cell        (monomials, chi-isotypic reduction, raising rows)
    kernel     wk11_s71_hybrid.hybrid_kernel   (initial-term cover + exact Schur residual,
                                                every vector verified on the full E, both primes)
    rows       wk9_s60_cell.ev_rows_from_coeffs (session 60's chi-coordinate evaluation rows)

and with the padded family of session 64 added (wk10_s64_pad: the TRUE padded
permanent x_0.per_3 restricted to a generic R-plane):

    mult_det   = rank_p(ev_det  . K)   K_pts = a + 8 det_4 pencils of length R, seed 11
    mult_pad   = rank_p(ev_pad  . K)   K_pts padded-permanent frames,           seed 37
    mult_per4  = rank_p(ev_per4 . K)   K_pts unpadded per_4 pencils,            seed 47
    mult_red   = rank_p(K[non-red rows])  point-free, Theorem (star), length-general mask
    mult_red'  = rank_p(ev_red  . K)   K_pts reducible points l.c,              seed 29

A full rank (= a) at ONE prime proves mult = a over Q (rank_p <= rank_Q); a drop
is a measurement until the verification protocol (results/PREREG_s79.md sec. 2.5).
i_X = a - mult_X;  D = mult_pad - mult_det (docs/brief_wording.md sec. 7);
D_R = mult_red - mult_det is the reducible screen (transfer lemma Thm 3).

The per_4 family is PROPER at R = 6 (16R - 6 = 90 < C(9,4) = 126) and vacuous at
R = 5 (session 71); the driver records the dimension check per length.

usage: python3 analysis/wk12_s79_cell6.py delta lam1 .. lamR [--a A] [--out FILE] [--certs DIR]
                                          [--sequential] [--bound 40] [--npts K] [--seedshift S]
prints one JSON line (RESULT ...) and appends it to --out.
"""
import sys, os, time, json, gzip
for _v in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ.setdefault(_v, '1')
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
os.environ.setdefault('S71_SCHUR_SO', '/home/claude/s79/schur.so')
import random
import numpy as np
from scipy import sparse
import wk11_s71_codes; wk11_s71_codes.install()
from wk8_s30_core import exps, restrict, det_form, per_form, P1, P2
from wk9_s45_build import build_cell, log, _rss_gb, _grouping
from wk9_s42_census import a_weyl
from wk9_s60_cell import CONVENTIONS
from wk10_s64_pad import pad_frames, pad_coeffs, point_record_pad
from wk11_s71_hybrid import best_cover, hybrid_kernel, matmul_mod, rank_mod_p, rank_tall, nullspace_mod_p, check_kernel_mat

N = 4
PRIMES = (P1, P2)
DET4, N_DET = det_form(4)
PER4, N_PER = per_form(4)
SEEDS = dict(det=11, red=29, pad=37, per4=47)
HYB_SEED = 20260908


# ------------------------------------------------------------------ points (length-general)
def det_pencils(K, seed, bound, R):
    rnd = random.Random(seed)
    return [[[[rnd.randint(-bound, bound) for _ in range(4)] for _ in range(4)] for _ in range(R)] for _ in range(K)]


def det_coeffs(pencil, R):
    As = [[pencil[i][a][b] for a in range(4) for b in range(4)] for i in range(R)]
    return restrict(DET4, N_DET, N, R, As)


def per4_coeffs(pencil, R):
    As = [[pencil[i][a][b] for a in range(4) for b in range(4)] for i in range(R)]
    return restrict(PER4, N_PER, N, R, As)


def reducible_points(K, seed, bound, R):
    rnd = random.Random(seed)
    out = []
    for _ in range(K):
        lin = [rnd.randint(-bound, bound) for _ in range(R)]
        cub = {al: rnd.randint(-bound, bound) for al in exps(3, R)}
        out.append((lin, cub))
    return out


def red_coeffs(pt, R):
    lin, cub = pt
    out = {}
    for a3, cc in cub.items():
        if cc == 0: continue
        for i in range(R):
            if lin[i] == 0: continue
            a4 = list(a3); a4[i] += 1; k = tuple(a4)
            out[k] = out.get(k, 0) + lin[i] * cc
    return {k: v for k, v in out.items() if v}


def point_record(kind, pt):
    if kind == 'det_pencil':
        return {"type": "det_pencil", "pencil": pt}
    if kind == 'per4_pencil':
        return {"type": "permanent_pencil", "pencil": pt}        # the verifier's name for the unpadded per_n pencil at the cell's n
    lin, cub = pt
    return {"type": "reducible", "l": list(lin), "cubic": [[list(al), int(c)] for al, c in sorted(cub.items()) if c]}


# ------------------------------------------------------------- evaluation rows (length-general)
def ev_rows_from_coeffs(arr, coeff_dicts, prime, R, chunk=2_000_000, n=N):
    A = exps(n, R); L = len(A)
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
                term *= cv[M[mm, k]]
                term %= prime
            term *= sgn[mm]
            term %= prime
            s0 = np.searchsorted(starts, b0, side='right') - 1
            s1 = np.searchsorted(starts, b0 + len(mm), side='left')
            loc = np.maximum(starts[s0:s1] - b0, 0)
            np.add.at(row, np.arange(s0, s1), np.add.reduceat(term, loc) % prime)
            del term, mm, loc
        out.append((row % prime).astype(np.int64))
    return np.array(out, dtype=np.int64).reshape(len(coeff_dicts), n_chi)


def expand_vector(arr, vec, p, R, n=N):
    """chi-coordinate vector (length n_chi, mod p) -> canonical term list
    [[alpha_1..alpha_delta], coeff] over the monomial basis (session 60's expand_vector, length-general)."""
    A = exps(n, R)
    M = arr['M']; col_of = arr['col_of']; sgn = arr['sgn']
    vec = np.asarray(vec, dtype=np.int64) % p
    sel = np.nonzero(col_of >= 0)[0]
    vals = (vec[col_of[sel]] * sgn[sel]) % p
    nz = vals != 0
    terms = []
    for m, c in zip(sel[nz].tolist(), vals[nz].tolist()):
        terms.append([[list(A[k]) for k in M[m].tolist()], int(c)])
    return {"terms": terms}


def red_mask(arr, R, chunk=500_000):
    """True on the chi-columns whose monomials have, for EVERY i in [R], a factor
    c_alpha with alpha_i = 0 (Theorem (star)); constant on orbits (asserted)."""
    A = np.array(exps(N, R), dtype=np.int8)
    M = arr['M']; col_of = arr['col_of']; n_chi = arr['n_chi']
    Nn = M.shape[0]
    cnt_red = np.zeros(n_chi, dtype=np.int64); cnt_all = np.zeros(n_chi, dtype=np.int64)
    for b0 in range(0, Nn, chunk):
        b1 = min(b0 + chunk, Nn)
        Z = (A[M[b0:b1]] == 0)
        red = Z.any(axis=1).all(axis=1)
        c = col_of[b0:b1]; ok = c >= 0
        cnt_all += np.bincount(c[ok], minlength=n_chi)
        cnt_red += np.bincount(c[ok & red], minlength=n_chi)
        del Z, red
    assert np.all((cnt_red == 0) | (cnt_red == cnt_all)), "red condition not constant on an orbit"
    return cnt_red > 0


_SHARED = {}


def _prime_job(args):
    p, opts = args
    B = _SHARED['B']; arr = B['arr']; E = B['E']; nc = B['n_chi']; a = opts['a']; R = opts['R']
    red = _SHARED['red']; nonred = np.nonzero(~red)[0]
    cov = _SHARED['cov']
    t0 = time.time()
    out = dict(prime=p, sides={})
    K, info = hybrid_kernel(E, nc, p, a, cov, seed=HYB_SEED, tag=f"[{opts['tag']}]", verbose=opts['verbose'])
    out['hybrid'] = info
    t = time.time()
    # one family at a time (the evaluation rows of a large-a cell are the memory peak: (a+8) x n_chi int64 per family)
    coeffs = {'det': lambda: [det_coeffs(pt, R) for pt in opts['det_pts']],
              'pad': lambda: [pad_coeffs(V) for V in opts['pad_pts']],
              'per4': lambda: [per4_coeffs(pt, R) for pt in opts['per4_pts']],
              'red_pts': lambda: [red_coeffs(pt, R) for pt in opts['red_pts']]}
    G = {}; ev_secs = 0.0; rank_secs = 0.0
    Kp_ = np.asarray(K % p, dtype=np.int64)
    for name in ('det', 'pad', 'per4', 'red_pts'):
        t1 = time.time()
        cl = coeffs[name](); parts = []
        for c0 in range(0, len(cl), 8):                       # eight points at a time: the rows never exceed 8 x n_chi
            EV = ev_rows_from_coeffs(arr, cl[c0:c0 + 8], p, R)
            parts.append(matmul_mod(EV % p, Kp_, p)); del EV
        ev_secs += time.time() - t1; t1 = time.time()
        G[name] = np.vstack(parts); del parts
        m = rank_mod_p(G[name], p)
        rank_secs += time.time() - t1
        out['sides'][name] = dict(mult=int(m), nullity=int(a - m), instrument=f'hybrid kernel + {name} evaluation rows')
    del Kp_
    out['ev_secs'] = round(ev_secs, 1)
    t = time.time() - rank_secs
    mstar = rank_tall(K[nonred], p) if len(nonred) else 0
    out['sides']['red_star'] = dict(mult=int(mstar), nullity=int(a - mstar), instrument='hybrid kernel + (star)')
    out['rank_secs'] = round(time.time() - t, 1)
    # ideal vectors (chi-coordinates, exact mod p) for every side with a drop
    for name in ('det', 'pad', 'per4'):
        if out['sides'][name]['mult'] < a:
            cs = nullspace_mod_p(G[name], p)                    # (a - mult) x a combinations c with ev_X K c = 0
            assert cs.shape == (a - out['sides'][name]['mult'], a)
            vecs = matmul_mod(np.asarray(cs, dtype=np.int64) % p, np.asarray(K.T, dtype=np.int64) % p, p)   # (a - mult) x n_chi
            assert np.any(vecs, axis=1).all() and check_kernel_mat(E, vecs.T, p)
            out[f'{name}_ideal_chi'] = vecs.tolist()
    if opts['keep_kernel'] and nc * a <= 400_000:
        out['kernel_chi'] = K.T.tolist()
    out['secs'] = round(time.time() - t0, 1)
    out['hwm_gb'] = round(_rss_gb(), 2)
    return out


def measure_cell(lam, delta, a_given=None, bound=40, npts=None, parallel=True, verbose=True, certs=None,
                 keep_kernel=True, seedshift=0, fullrank_certs=True):
    lam = tuple(lam); R = len(lam)
    assert sum(lam) == N * delta and all(lam[i] >= lam[i + 1] for i in range(R - 1)) and lam[-1] >= 1
    t0 = time.time()
    B = build_cell(lam, delta, n=N, verbose=verbose)
    a = a_weyl(lam, delta, N, {})
    if a_given is not None:
        assert a == a_given, ('a: given value disagrees with the Weyl alternation', lam, delta, a_given, a)
    nc = B['n_chi']; E = B['E']
    Kp = npts if npts else a + 8
    seeds = {k: v + seedshift for k, v in SEEDS.items()}
    out = dict(lam=list(lam), delta=delta, ell=R, a=a, K=Kp, N_S=B['N_S'], stab=B['stab'], n_chi=nc,
               nrows=B['nrows'], nnz=B['nnz'], nfixed=B['nfixed'], build_secs=round(B['build_secs'], 1),
               build_hwm_gb=round(B['hwm_gb'], 2), route='hybrid (length-general driver wk12_s79_cell6)',
               cost_model='s71 hybrid: build 2.1e-6 s per N_S*delta; evaluation rows 2.7e-8 s per point per N_S*delta',
               NS_delta=int(B['N_S']) * int(delta), seeds=seeds, bound=bound, primes=list(PRIMES))
    if a == 0:
        out.update(status='a=0', secs=round(time.time() - t0, 1)); return out
    t = time.time()
    red = red_mask(B['arr'], R); nred = int(red.sum()); out['n_red'] = nred
    cov = best_cover(E, nc, seed=HYB_SEED)
    out['cover_E'] = dict(size=cov['size'], order=cov['order'], stats=cov['stats'], n_chi=nc, a=a,
                          excess=int(nc - cov['size'] - a), certified_rank_lb=cov['size'])
    if nred:
        Ered = E[:, np.nonzero(red)[0]].tocsr(); Ered.eliminate_zeros()
        Ered = Ered[np.nonzero(np.diff(Ered.indptr) > 0)[0]]
        cr = best_cover(Ered, nred, seed=HYB_SEED)
        out['cover_Ered'] = dict(size=cr['size'], order=cr['order'], stats=cr['stats'], n_red=nred, certified=bool(cr['size'] == nred))
        del Ered
    else:
        out['cover_Ered'] = dict(size=0, n_red=0, certified=True, note='no red columns: mult_red = 0 by (star)')
    out['sieve_secs'] = round(time.time() - t, 1)
    if verbose:
        log(f"  sieve {lam} d{delta}: cover(E) {cov['size']}/{nc} by {cov['order']} (a={a}, |U|={nc - cov['size']}, excess {nc - cov['size'] - a}); "
            f"cover(E_red) {out['cover_Ered']['size']}/{nred}{' CERTIFIED i_red = 0' if out['cover_Ered']['certified'] else ''} ({out['sieve_secs']}s)")
    det_pts = det_pencils(Kp, seeds['det'], bound, R)
    per4_pts = det_pencils(Kp, seeds['per4'], bound, R)
    red_pts = reducible_points(Kp, seeds['red'], bound, R)
    pad_pts = pad_frames(Kp, seeds['pad'], bound, R)
    opts = dict(a=a, R=R, det_pts=det_pts, per4_pts=per4_pts, red_pts=red_pts, pad_pts=pad_pts, verbose=verbose,
                tag='_'.join(map(str, lam)) + f'd{delta}', keep_kernel=keep_kernel)
    _SHARED['B'] = B; _SHARED['red'] = red; _SHARED['cov'] = cov
    jobs = [(p, opts) for p in PRIMES]
    nU = nc - cov['size']
    mem_x = min(4.0 * cov['size'] * nU, 1.0e9) + 4.0 * nc * a
    out['pred_mem_x_bytes'] = int(mem_x)
    if parallel and 2 * mem_x < 6.0e8 and nc < 150_000:
        import multiprocessing as mp
        with mp.get_context('fork').Pool(2) as pool:
            res = pool.map(_prime_job, jobs)
        out['primes_concurrent'] = True
    else:
        res = [_prime_job(j) for j in jobs]
        out['primes_concurrent'] = False
    _SHARED.clear()
    out['per_prime'] = {str(r['prime']): {k: v for k, v in r.items() if k not in ('prime', 'kernel_chi') and not k.endswith('_ideal_chi')} for r in res}
    sides = {}
    for sd in ('det', 'pad', 'per4', 'red_star', 'red_pts'):
        vals = {r['prime']: r['sides'][sd]['mult'] for r in res}
        agree = len(set(vals.values())) == 1
        sides[sd] = dict(mult=(vals[PRIMES[0]] if agree else None), per_prime={str(p): v for p, v in vals.items()},
                         primes_agree=agree, instrument=res[0]['sides'][sd]['instrument'])
        if not agree: sides[sd]['status'] = 'PRIMES DISAGREE'
        elif vals[PRIMES[0]] == a: sides[sd]['status'] = 'proved (full rank at both primes: mult = a over Q)'
        else: sides[sd]['status'] = 'measured (exact mod both primes, kernel exhibited): mult = %d' % vals[PRIMES[0]]
    out['sides'] = sides
    out['mult_det'] = sides['det']['mult']; out['mult_pad'] = sides['pad']['mult']; out['mult_per4'] = sides['per4']['mult']
    out['mult_red_star'] = sides['red_star']['mult']; out['mult_red_pts'] = sides['red_pts']['mult']
    out['mult_red'] = out['mult_red_star']
    out['star_eq_pts'] = (out['mult_red_pts'] == out['mult_red_star'])
    if out['cover_Ered']['certified']:
        assert out['mult_red_star'] == a, ('sieve certified i_red = 0 but (star) rank disagrees', out['mult_red_star'], a)
    ok = all(s['primes_agree'] for s in sides.values()) and out['star_eq_pts']
    if ok:
        out['i_det'] = a - out['mult_det']; out['i_red'] = a - out['mult_red']; out['i_pad'] = a - out['mult_pad']; out['i_per4'] = a - out['mult_per4']
        out['D'] = out['mult_pad'] - out['mult_det']              # the programme's D (pad minus det); D > 0 refutes containment
        out['D_R'] = out['mult_red'] - out['mult_det']            # the reducible screen
        out['pad_lt_red'] = bool(out['mult_pad'] < out['mult_red'])
        # directional invariant of the engine: i_det <= i_red <= i_pad (P_R <= R_R; the det side is the ambient reference)
        out['monotone_ok'] = bool(out['mult_pad'] <= out['mult_red'])
    else:
        out['i_det'] = out['i_red'] = out['i_pad'] = out['i_per4'] = out['D'] = out['D_R'] = None; out['pad_lt_red'] = None; out['monotone_ok'] = None
    out['refute'] = bool(out['D'] is not None and out['D'] > 0)
    out['halt'] = bool(not ok or out['refute'] or (out['i_det'] or 0) > 0 or bool(out['pad_lt_red']) or (out['i_per4'] or 0) > 0)
    out['ok'] = ok
    out['secs'] = round(time.time() - t0, 1)
    out['hwm_gb'] = round(max(_rss_gb(), max(r['hwm_gb'] for r in res)), 2)
    if verbose:
        log(f"  RESULT {lam} d{delta}: a={a} n_chi={nc} |U|={nU} det={out['mult_det']} pad={out['mult_pad']} per4={out['mult_per4']} "
            f"red(star)={out['mult_red_star']} red(pts)={out['mult_red_pts']} i_det={out['i_det']} i_pad={out['i_pad']} i_red={out['i_red']} "
            f"i_per4={out['i_per4']} D={out['D']} D_R={out['D_R']} pad<red={out['pad_lt_red']}{'  *** HALT ***' if out['halt'] else ''}  "
            f"({out['secs']}s, HWM {out['hwm_gb']} GB)")
    if certs:
        os.makedirs(certs, exist_ok=True)
        tagl = '_'.join(map(str, lam)) + f'_d{delta}'
        files = []
        for r in res:
            p = r['prime']
            cert = {"format": "gct-cert/1", "kind": "hybrid_kernel",
                    "title": f"mod-{p} kernel of the raising operator at {tuple(lam)}, degree {delta}, by the hybrid route (length {R}); "
                             f"mult_det={r['sides']['det']['mult']}, mult_pad={r['sides']['pad']['mult']}, mult_per4={r['sides']['per4']['mult']}, "
                             f"mult_red(star)={r['sides']['red_star']['mult']}, mult_red(pts)={r['sides']['red_pts']['mult']}, a={a} (session 79)",
                    "produced_by": "analysis/wk12_s79_cell6.py (session 79)",
                    "cell": {"n": N, "r": R, "lambda": [int(x) for x in lam], "delta": int(delta), "a": int(a)},
                    "conventions": dict(CONVENTIONS), "field": f"F_{p}", "prime": int(p),
                    "sizes": {"N_S": int(B['N_S']), "stab": int(B['stab']), "n_chi": int(nc), "n_red": int(nred),
                              "rows_E": int(B['nrows']), "nnz_E": int(B['nnz'])},
                    "recipe": {"cover_order": cov['order'], "cover_size": int(cov['size']), "orders_tried": cov['stats'],
                               "projection_seed": HYB_SEED, "attempts": r['hybrid']['attempts'],
                               "points": {"det": {"seed": seeds['det'], "bound": bound, "count": Kp},
                                          "pad": {"seed": seeds['pad'], "bound": bound, "count": Kp},
                                          "per4": {"seed": seeds['per4'], "bound": bound, "count": Kp},
                                          "reducible": {"seed": seeds['red'], "bound": bound, "count": Kp}}},
                    "claims": {"nullity_p_E": int(a), "mult_det": r['sides']['det']['mult'], "mult_pad": r['sides']['pad']['mult'],
                               "mult_per4": r['sides']['per4']['mult'], "mult_red_star": r['sides']['red_star']['mult'],
                               "mult_red_pts": r['sides']['red_pts']['mult'],
                               "field_note": "a full rank mod p proves mult = a over Q (rank_p <= rank_Q); a kernel mod p bounds i from below only"},
                    "points": {"det": [point_record('det_pencil', pt) for pt in det_pts],
                               "pad": [point_record_pad(V) for V in pad_pts],
                               "per4": [point_record('per4_pencil', pt) for pt in per4_pts],
                               "reducible": [point_record('reducible', pt) for pt in red_pts]}}
            if 'kernel_chi' in r: cert['kernel_chi'] = r['kernel_chi']
            for name in ('det', 'pad', 'per4'):
                if f'{name}_ideal_chi' in r: cert[f'{name}_ideal_chi'] = r[f'{name}_ideal_chi']
            fn = os.path.join(certs, f'{tagl}_hybrid_p{p}.json.gz')
            with gzip.open(fn, 'wt', encoding='utf-8') as f:
                json.dump(cert, f, separators=(',', ':'))
            files.append([os.path.relpath(fn, ROOT), os.path.getsize(fn)])
            # format-verifiable full_rank certificates (kind full_rank, tools/verify) for the full-rank families,
            # with the kernel basis expanded to canonical terms when it is small enough to ship
            if 'kernel_chi' in r and B['N_S'] * a <= 3_000_000 and fullrank_certs:
                basis_terms = [expand_vector(B['arr'], np.array(v, dtype=np.int64), p, R) for v in r['kernel_chi']]
                for name, variety, recs in (('det', 'det_pencil', [point_record('det_pencil', pt) for pt in det_pts]),
                                            ('pad', 'padded_permanent', [point_record_pad(V) for V in pad_pts]),
                                            ('per4', 'permanent_pencil', [point_record('per4_pencil', pt) for pt in per4_pts])):
                    if r['sides'][name]['mult'] == a:
                        cert2 = {"format": "gct-cert/1", "kind": "full_rank",
                                 "title": f"mult_{name}({tuple(lam)}, {delta}) = a = {a} mod {p} (session 79, hybrid kernel basis recorded)",
                                 "produced_by": "analysis/wk12_s79_cell6.py (session 79)",
                                 "cell": {"n": N, "r": R, "lambda": [int(x) for x in lam], "delta": int(delta), "a": int(a)},
                                 "conventions": dict(CONVENTIONS), "prime": int(p), "variety": variety, "points": recs, "basis": basis_terms}
                        fn2 = os.path.join(certs, f'{tagl}_fullrank_{name}_p{p}.json.gz')
                        with gzip.open(fn2, 'wt', encoding='utf-8') as f:
                            json.dump(cert2, f, separators=(',', ':'))
                        if os.path.getsize(fn2) > 4_500_000:
                            os.remove(fn2)
                        else:
                            files.append([os.path.relpath(fn2, ROOT), os.path.getsize(fn2)])
        out['certs'] = files
    if any(k.endswith('_ideal_chi') for r in res for k in r):
        import pickle
        kd = os.environ.get('S79_KERN_DIR', '/home/claude/s79/kern'); os.makedirs(kd, exist_ok=True)
        pickle.dump(dict(res=out, ideal={r['prime']: {k: v for k, v in r.items() if k.endswith('_ideal_chi')} for r in res},
                         kernel={r['prime']: r.get('kernel_chi') for r in res}),
                    open(os.path.join(kd, f"ideal_{'_'.join(map(str, lam))}_d{delta}.pkl"), 'wb'))
    return out


if __name__ == '__main__':
    args = sys.argv[1:]
    def arg(name, default):
        return type(default)(args[args.index(name) + 1]) if name in args else default
    pos = []; i = 0
    while i < len(args):
        if args[i].startswith('--') and i + 1 < len(args) and not args[i + 1].startswith('--') and args[i] not in ('--sequential',):
            i += 2
        elif args[i].startswith('--'):
            i += 1
        else:
            pos.append(int(args[i])); i += 1
    delta, lam = pos[0], tuple(pos[1:])
    res = measure_cell(lam, delta, a_given=(arg('--a', -1) if '--a' in args else None), bound=arg('--bound', 40),
                       npts=arg('--npts', 0) or None, parallel=('--sequential' not in args), certs=arg('--certs', '') or None,
                       seedshift=arg('--seedshift', 0), fullrank_certs=('--no-fullrank' not in args))
    print("RESULT " + json.dumps(res), flush=True)
    outp = arg('--out', '')
    if outp:
        with open(outp, 'a') as f: f.write(json.dumps(res) + "\n")
