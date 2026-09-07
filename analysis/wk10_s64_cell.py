#!/usr/bin/env python3
"""
Session 64 -- one length-(r) cell, THREE sides from ONE common source, dense.

    mult_det = a - nullity_Q [E; ev_det]      det_4 pencils
    mult_red = a - nullity_Q [E; ev_red]      l . (generic cubic)
    mult_pad = a - nullity_Q [E; ev_pad]      l(s) . per_3(A(s))   (the TRUE padded permanent)

with E the SAME stacked simple raising operators on the chi_lam-isotypic
reduction V_chi (analysis/wk9_s45_build.build_cell, unchanged) and ev_* the SAME
chi-coordinate contraction (wk9_s60_cell.ev_rows_from_coeffs).  Only the
coefficient-dict producer differs between sides:

    det_coeffs   (wk9_s60_cell)     l.c producer   red_coeffs (wk9_s60_cell)
    pad_coeffs   (wk10_s64_pad)     -- restrict(PAD34) = l(s).per_3(A(s))

Because all three sides read the ONE dense highest-weight kernel `kern`
(a x n_chi, exact flint nullspace of E, s41 semantics, every vector verified on
the full sparse E), the three ideal slices

    U_D = ker T_det ,  U_R = ker T_red ,  U_P = ker T_pad   (subspaces of C^a)

live in the SAME coordinates on M_lam = span(kern) and can be compared, not just
their dimensions -- which is what session 65 needs.  T_side = ev_side . kern^T
is the a-column "point matrix"; mult_side = rank T_side, i_side = a - mult_side =
dim U_side, and U_side = nullspace(T_side) pulled back to span(kern).

Containment the run must respect (docs/reducible_ideal.md Theorem 1; this brief):
    per_3 is one cubic, so  P_r-orbit  subset  R_r  =>  I(R_r) subset I(pad)
    => i_red <= i_pad => mult_pad <= mult_red.
A measured  mult_pad > mult_red  is a defect, not a discovery: the run halts.
At r <= 5 the permanental cubics fill all cubics (P_r = R_r, verified
independently in results/s64_calibration.md), so there  mult_pad == mult_red
exactly; a mismatch there is a FAIL and blocks any downstream use.

usage: python3 analysis/wk10_s64_cell.py delta lam1 .. lam_r
          [--route auto|dense|sparse] [--dense-cap 4600]
          [--seeds 2] [--seed-det 11 --seed-red 29 --seed-pad 37]
          [--bound 40] [--npts K] [--kern-dir DIR] [--certs DIR] [--out FILE]
prints one JSON line (RESULT ...) and appends it to --out.
"""
import sys, os, time, json, gzip, pickle
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
os.environ.setdefault('WIED_BIN', '/home/claude/wied64')
os.environ.setdefault('WIED_WORK', '/home/claude/s64/work')
import numpy as np
from scipy import sparse
from flint import nmod_mat
from wk8_s30_core import exps, P1, P2
from wk9_s45_build import build_cell, log, _rss_gb
from wk9_s42_census import a_weyl
# reuse the validated s60 primitives verbatim
from wk9_s60_cell import (det_pencils, det_coeffs, reducible_points, red_coeffs,
                          ev_rows_from_coeffs, kernel_dense, rank_mod_p,
                          nullspace_mod_p, expand_vector, point_record, red_mask)
from wk10_s64_pad import pad_frames, pad_coeffs, point_record_pad

N = 4
PRIMES = (P1, P2)


def _T(EV, kern, p):
    """point matrix T = EV . kern^T mod p  (K x a), 16-bit split (a < 2^16)."""
    EV = np.asarray(EV, dtype=np.int64) % p
    K = kern.T % p
    assert kern.shape[0] < 65536
    lo = K & 0xFFFF; hi = K >> 16
    return ((EV @ lo) % p + ((EV @ hi) % p) * 65536) % p


def _side(EV, kern, a, p):
    """(mult, U) for one side: mult = rank(T), U = basis of ker(T) in the
    a-coordinates on span(kern) (each U-vector c means sum_j c_j kern_j is in the
    side's ideal)."""
    if EV.shape[0] == 0:
        return 0, [np.eye(a, dtype=np.int64)[j] for j in range(a)]
    T = _T(EV, kern, p)                       # K x a
    mult = rank_mod_p(T, p)
    U = nullspace_mod_p(T, p)                 # basis of {c : T c = 0}, dim a-mult
    return int(mult), U


def _prime_job(args):
    p, S = args
    B = S['B']; arr = B['arr']; E = B['E']; nc = B['n_chi']; a = S['a']
    lam = B['lam']; delta = B['delta']; r = len(lam)
    t0 = time.time()
    out = dict(prime=p, sides={}, timings={})

    # one shared dense kernel of E (the a HWVs of weight lam), s41 semantics
    tk = time.time()
    kern, kroute = kernel_dense(E, nc, p, a, exact_cap=S['exact_cap'])
    out['kernel_route'] = kroute; out['timings']['kernel'] = round(time.time() - tk, 1)

    families = {
        'det': [det_coeffs(pt) for pt in S['det_pts']],
        'red': [red_coeffs(pt) for pt in S['red_pts']],
        'pad': [pad_coeffs(V) for V in S['pad_pts']],
    }
    # extra independent seeds for pad and red (rank agreement / margin)
    for si, (dp, rp, pp) in enumerate(S['extra_pts']):
        families[f'det@{si+1}'] = [det_coeffs(pt) for pt in dp]
        families[f'red@{si+1}'] = [red_coeffs(pt) for pt in rp]
        families[f'pad@{si+1}'] = [pad_coeffs(V) for V in pp]

    U = {}
    for name, coeffs in families.items():
        tv = time.time()
        EV = ev_rows_from_coeffs(arr, coeffs, p)
        mult, Uside = _side(EV, kern, a, p)
        out['sides'][name] = dict(mult=int(mult), i=int(a - mult), npts=len(coeffs),
                                  margin=int(len(coeffs) - mult), secs=round(time.time() - tv, 1))
        U[name] = Uside

    # kernel coordinates in M_lam (span kern): keep for session 65.  Saved at the
    # first prime only (bases mod P1); the second prime is the agreement check.
    if p == PRIMES[0] and S['want_kern']:
        out['_kern'] = kern
        out['_U'] = {k: [v.tolist() for v in U[k]] for k in ('det', 'red', 'pad')}
        # monomial-term expansions of the ideal-slice vectors (machine-readable,
        # verifier-checkable): term = [[alpha_1..alpha_delta], coeff]
        out['_U_terms'] = {}
        for k in ('det', 'red', 'pad'):
            vs = []
            for c in U[k]:
                v = np.zeros(nc, dtype=np.int64)
                for j, cj in enumerate(c):
                    if cj: v = (v + cj * kern[j]) % p
                vs.append(expand_vector(arr, v, p))
            out['_U_terms'][k] = vs
    out['secs'] = round(time.time() - t0, 1); out['hwm_gb'] = round(_rss_gb(), 2)
    return out


def measure_cell(lam, delta, seeds=2, seed_det=11, seed_red=29, seed_pad=37,
                 bound=40, npts=None, dense_cap=4600, exact_cap=2500,
                 want_kern=True, parallel=True, verbose=True, a_given=None, hpad=None):
    lam = tuple(lam); r = len(lam)
    assert sum(lam) == N * delta and all(lam[i] >= lam[i + 1] for i in range(r - 1)) and lam[-1] > 0
    t0 = time.time()
    B = build_cell(lam, delta, n=N, verbose=verbose)
    a = a_weyl(lam, delta, N, {})
    if a_given is not None:
        assert a == a_given, ('a disagrees with the Weyl alternation', lam, delta, a_given, a)
    nc = B['n_chi']
    K = npts if npts else a + 8
    out = dict(lam=list(lam), delta=delta, ell=r, a=a, K=K, N_S=B['N_S'], stab=B['stab'],
               n_chi=nc, nrows=B['nrows'], nnz=B['nnz'], build_secs=round(B['build_secs'], 1),
               build_hwm_gb=round(B['hwm_gb'], 2), seeds=dict(det=seed_det, red=seed_red, pad=seed_pad, extra=seeds - 1),
               bound=bound, primes=list(PRIMES), h_pad=hpad, P5eqR5=(r <= 5))
    if a == 0:
        out.update(status='a=0', secs=round(time.time() - t0, 1)); return out, {}
    if nc > dense_cap:
        out.update(status='skipped: n_chi > dense_cap (use --route sparse or raise --dense-cap)',
                   secs=round(time.time() - t0, 1))
        return out, {}

    det_pts = det_pencils(K, seed_det, bound)
    red_pts = reducible_points(K, seed_red, bound)
    pad_pts = pad_frames(K, seed_pad, bound, r)
    extra = []
    for si in range(seeds - 1):
        extra.append((det_pencils(K, seed_det + 1000 * (si + 1), bound),
                      reducible_points(K, seed_red + 1000 * (si + 1), bound),
                      pad_frames(K, seed_pad + 1000 * (si + 1), bound, r)))
    S = dict(B=B, a=a, det_pts=det_pts, red_pts=red_pts, pad_pts=pad_pts,
             extra_pts=extra, exact_cap=exact_cap, want_kern=want_kern)

    jobs = [(p, S) for p in PRIMES]
    if parallel:
        import multiprocessing as mp
        with mp.get_context('fork').Pool(2) as pool:
            res = pool.map(_prime_job, jobs)
    else:
        res = [_prime_job(j) for j in jobs]

    # combine over primes: every side must agree across the two primes and across seeds
    sidenames = ['det', 'red', 'pad'] + [f'{s}@{i+1}' for i in range(seeds - 1) for s in ('det', 'red', 'pad')]
    combined = {}
    for name in sidenames:
        vals = {rr['prime']: rr['sides'][name]['mult'] for rr in res}
        agree = len(set(vals.values())) == 1
        combined[name] = dict(mult=(vals[PRIMES[0]] if agree else None),
                              per_prime={str(pp): int(v) for pp, v in vals.items()},
                              primes_agree=agree,
                              margin=min(rr['sides'][name]['margin'] for rr in res))
    # consolidate the primary three plus seed agreement
    def consolidate(base):
        variants = [base] + [f'{base}@{i+1}' for i in range(seeds - 1)]
        muls = [combined[v]['mult'] for v in variants]
        best = max(m for m in muls if m is not None) if any(m is not None for m in muls) else None
        return dict(mult=best, per_seed={v: combined[v]['mult'] for v in variants},
                    per_prime=combined[base]['per_prime'], primes_agree=all(combined[v]['primes_agree'] for v in variants),
                    seeds_agree=(len(set(m for m in muls if m is not None)) <= 1),
                    margin=min(combined[v]['margin'] for v in variants))
    md = consolidate('det'); mr = consolidate('red'); mp_ = consolidate('pad')
    out['mult_det'] = md['mult']; out['mult_red'] = mr['mult']; out['mult_pad'] = mp_['mult']
    out['i_det'] = a - md['mult']; out['i_red'] = a - mr['mult']; out['i_pad'] = a - mp_['mult']
    out['sides'] = dict(det=md, red=mr, pad=mp_)
    out['D'] = (out['mult_pad'] - out['mult_det']) if None not in (out['mult_pad'], out['mult_det']) else None

    # ---- calibration verdicts ----------------------------------------------
    checks = {}
    checks['primes_agree'] = md['primes_agree'] and mr['primes_agree'] and mp_['primes_agree']
    checks['seeds_agree'] = md['seeds_agree'] and mr['seeds_agree'] and mp_['seeds_agree']
    # containment  mult_pad <= mult_red <= mult_det  (i_det <= i_red <= i_pad)
    checks['containment_pad_le_red'] = (out['mult_pad'] <= out['mult_red'])
    checks['containment_red_le_det'] = (out['mult_red'] <= out['mult_det'])
    # r<=5 : P_r = R_r  => mult_pad == mult_red exactly
    if r <= 5:
        checks['P5eqR5_pad_eq_red'] = (out['mult_pad'] == out['mult_red'])
    out['checks'] = checks
    out['ok'] = all(checks.values())
    # the containment violation is a STOP condition (a defect, not a finding)
    if out['mult_pad'] is not None and out['mult_red'] is not None and out['mult_pad'] > out['mult_red']:
        out['STOP'] = 'containment violated: mult_pad > mult_red -- defect in the implementation'
    out['secs'] = round(time.time() - t0, 1)
    out['hwm_gb'] = round(max(_rss_gb(), max(rr['hwm_gb'] for rr in res)), 2)

    kern_payload = {}
    for rr in res:
        if '_kern' in rr:
            kern_payload = dict(kern=rr['_kern'], U=rr['_U'], U_terms=rr['_U_terms'], prime=rr['prime'])
    if verbose:
        log(f"  RESULT {lam} d{delta}: a={a} n_chi={nc} mult_det={out['mult_det']} "
            f"mult_red={out['mult_red']} mult_pad={out['mult_pad']} D={out['D']} "
            f"ok={out['ok']}{'  *** '+out['STOP'] if 'STOP' in out else ''}  ({out['secs']}s, HWM {out['hwm_gb']} GB)")
    return out, kern_payload


if __name__ == '__main__':
    args = sys.argv[1:]
    def arg(name, default):
        return type(default)(args[args.index(name) + 1]) if name in args else default
    pos = []; i = 0
    while i < len(args):
        if args[i].startswith('--'): i += 2
        else: pos.append(int(args[i])); i += 1
    delta, lam = pos[0], tuple(pos[1:])
    res, kern = measure_cell(lam, delta, seeds=arg('--seeds', 2), seed_det=arg('--seed-det', 11),
                             seed_red=arg('--seed-red', 29), seed_pad=arg('--seed-pad', 37),
                             bound=arg('--bound', 40), npts=(arg('--npts', 0) or None),
                             dense_cap=arg('--dense-cap', 4600), exact_cap=arg('--exact-cap', 2500),
                             want_kern=('--no-kern' not in args),
                             a_given=(arg('--a', -1) if '--a' in args else None),
                             hpad=(arg('--hpad', -1) if '--hpad' in args else None))
    print("RESULT " + json.dumps(res), flush=True)
    outp = arg('--out', '')
    if outp:
        with open(outp, 'a') as f: f.write(json.dumps(res) + "\n")
    kd = arg('--kern-dir', '')
    if kd and kern:
        os.makedirs(kd, exist_ok=True)
        tag = '_'.join(map(str, lam)) + f'_d{delta}'
        # compact machine-readable kernel artefact: kern basis + U bases + term expansions
        art = dict(cell=dict(n=N, r=len(lam), lam=list(lam), delta=delta, a=res['a'],
                             n_chi=res['n_chi'], prime=int(kern['prime'])),
                   conventions={"kernel": "kern[j] = j-th HWV of weight lambda in chi-coords (E kern[j] = 0)",
                                "U": "U[side] : basis of ker T_side in the a-coords; sum_j U[k][j] kern[j] in I(side)",
                                "raising": "E_ij c_alpha = (alpha_i+1) c_{alpha+e_i-e_j}"},
                   kern=kern['kern'].tolist(), U=kern['U'], U_terms=kern['U_terms'])
        with gzip.open(os.path.join(kd, f'kern_{tag}.json.gz'), 'wt', encoding='utf-8') as f:
            json.dump(art, f, separators=(',', ':'))
        print(f"  kernel artefact -> {os.path.join(kd, f'kern_{tag}.json.gz')}", file=sys.stderr)
