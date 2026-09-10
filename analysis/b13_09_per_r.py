#!/usr/bin/env python3
"""
B13-09 -- I(D_r^{per_3})_delta on the cubic side by the hybrid, one weight of ANY
length per call.  This is session 79's evaluator (analysis/wk12_s79_per6.py,
fixed at R = 6) made length-general, R = len(mu), on the unchanged engine:

    build      wk9_s45_build.build_cell         (monomials, chi-isotypic reduction, raising rows; length-general)
    kernel     wk11_s71_hybrid.hybrid_kernel    (initial-term cover + exact Schur residual, every vector verified E.K = 0)
    rows       wk12_s79_cell6.ev_rows_from_coeffs (chi-coordinate evaluation rows; length-general)

D_r^{per_3} = closure{ per_3(sum_{i<=r} s_i A_i) } in Sym^3 C^r.

    a       = mult of S_mu in Sym^delta(Sym^3 C^r)   (Weyl alternation, asserted = the queue's plethysm value)
    K       = exact mod-p kernel of the raising operator on V_chi (hybrid, verified on E)
    mult    = rank_p(ev_per3 . K),  K_pts = a + 8 points per_3(sum_{i<=r} s_i A_i), A_i integer 3x3 in [-40, 40],
              seed 41 (session 41's family, now with r matrices per point), both house primes
    units   = a - mult;  units = 0 at one prime proves S_mu is not in I(D_r^{per_3})_delta over Q (rank_p <= rank_Q).

A drop (units >= 1) is re-checked inside the same call at 3a + 24 fresh points
(seed 907) before it is banked, the kernel vector is exhibited (chi-coordinates
and, where small, canonical terms) and the caller halts: the verification
protocol of docs/batch13_worker_preamble.md takes over.  A sampled drop is a
MEASUREMENT (a ceiling on the rank, hence a floor on units, mod p only); it is
never promoted here.

Exponent letters: every coefficient dictionary is keyed by the exponent TUPLE
alpha and read back through exps(3, r) of wk8_s30_core by tuple lookup
(`co.get(al)`), never by a literal position, so the two opposite `exps`
orderings in the tree cannot be confused here.

usage: python3 analysis/b13_09_per_r.py delta mu1 .. muR [--a A] [--out FILE] [--certs DIR] [--quiet] [--control-diag]
  --control-diag  the NEGATIVE CONTROL: the same code path on per_3 of diagonal pencils (split cubics),
                  which must read mult = 0 at every weight of length >= 4; never writes a certificate.
prints one JSON line (RESULT ...) and appends it to --out.
"""
import sys, os, time, json, gzip, random
for _v in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ.setdefault(_v, '1')
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
os.environ.setdefault('S71_SCHUR_SO', '/home/claude/b13_09/schur.so')
import numpy as np
import wk11_s71_codes; wk11_s71_codes.install()
from wk8_s30_core import exps, restrict, per_form, P1, P2
from wk9_s45_build import build_cell, log, _rss_gb
from wk9_s42_census import a_weyl
from wk9_s60_cell import CONVENTIONS
from wk11_s71_hybrid import best_cover, hybrid_kernel, matmul_mod, rank_mod_p, nullspace_mod_p, check_kernel_mat
from wk12_s79_cell6 import ev_rows_from_coeffs, expand_vector

n3 = 3
PRIMES = (P1, P2)
PER3, N_PER3 = per_form(3)
SEED, BOUND, SEED_RECHECK = 41, 40, 907
HYB_SEED = 20260908
SESSION = 'B13-09'


def per3_pencils(K, seed, bound, R, diagonal=False):
    """K points, each an R-tuple of integer 3x3 matrices.  `diagonal=True` is the
    NEGATIVE CONTROL family only: per_3 of a diagonal pencil is a product of three
    linear forms, so the points lie on the Chow variety of split cubics, whose
    coordinate ring in degree delta is a quotient of Sym^3(Sym^delta V) and has no
    constituent with more than three rows -- every weight of length >= 4 MUST read
    mult = 0 there.  A control that reads anything else is an instrument defect."""
    rnd = random.Random(seed)
    if diagonal:
        return [[[[rnd.randint(-bound, bound) if a == b else 0 for b in range(3)] for a in range(3)] for _ in range(R)] for _ in range(K)]
    return [[[[rnd.randint(-bound, bound) for _ in range(3)] for _ in range(3)] for _ in range(R)] for _ in range(K)]


def per3_coeffs(pencil, R):
    As = [[pencil[i][a][b] for a in range(3) for b in range(3)] for i in range(R)]
    return restrict(PER3, N_PER3, n3, R, As)


def measure_weight(mu, delta, verbose=True, certs=None, a_given=None, control_diag=False):
    mu = tuple(mu); R = len(mu)
    if control_diag: certs = None                        # a control never writes a certificate
    assert sum(mu) == 3 * delta and all(mu[i] >= mu[i + 1] for i in range(R - 1)) and mu[-1] > 0, (mu, delta)
    t0 = time.time()
    aw = a_weyl(mu, delta, n3, {})
    if a_given is None:
        a = aw
    else:
        a = int(a_given)                                 # the queue's value (results/b13_09_census.json: Weyl alternation AND the symmetric-function plethysm, asserted equal there)
        assert a == aw, ('a: queue value and Weyl alternation disagree', mu, delta, a, aw)
    out = dict(board_numbering='batch13', session=SESSION, mu=list(mu), delta=delta, n=n3, r=R, a=int(a),
               route='hybrid (n=3, per_3 pencils of length r)', seeds=dict(per3=SEED, recheck=SEED_RECHECK, hybrid=HYB_SEED),
               bound=BOUND, primes=list(PRIMES),
               family=('NEGATIVE CONTROL: per_3 of DIAGONAL pencils (split cubics; mult must be 0 at length >= 4)' if control_diag
                       else 'per_3(sum_{i<=r} s_i A_i), A_i integer 3x3 in [-bound, bound]'))
    if a == 0:
        out.update(status='a=0', secs=round(time.time() - t0, 1)); return out
    B = build_cell(mu, delta, n=n3, verbose=verbose)
    nc = B['n_chi']; E = B['E']
    out.update(N_S=B['N_S'], stab=B['stab'], n_chi=nc, nrows=B['nrows'], nnz=B['nnz'], build_secs=round(B['build_secs'], 1),
               build_hwm_gb=round(B['hwm_gb'], 2), NS_delta=int(B['N_S']) * int(delta))
    Kp = a + 8
    pts = per3_pencils(Kp, SEED, BOUND, R, diagonal=control_diag)
    cov = best_cover(E, nc, seed=HYB_SEED)
    out['cover_E'] = dict(size=cov['size'], order=cov['order'], excess=int(nc - cov['size'] - a))
    per_prime = {}
    for p in PRIMES:
        tp = time.time()
        K, info = hybrid_kernel(E, nc, p, a, cov, seed=HYB_SEED, tag=f"[per{R} {'_'.join(map(str, mu))}d{delta}]", verbose=verbose)
        EV = ev_rows_from_coeffs(B['arr'], [per3_coeffs(pt, R) for pt in pts], p, R, n=n3)
        G = matmul_mod(EV % p, K % p, p)
        m = int(rank_mod_p(G, p))
        rec = dict(mult=m, units=int(a - m), hybrid=info, secs=round(time.time() - tp, 1))
        if m < a:
            pts2 = per3_pencils(3 * a + 24, SEED_RECHECK, BOUND, R, diagonal=control_diag)
            EV2 = ev_rows_from_coeffs(B['arr'], [per3_coeffs(pt, R) for pt in pts2], p, R, n=n3)
            G2 = matmul_mod(EV2 % p, K % p, p)
            m2 = int(rank_mod_p(np.vstack([G, G2]), p))
            rec['recheck'] = dict(points=3 * a + 24, seed=SEED_RECHECK, mult_with_all_points=m2)
            cs = nullspace_mod_p(np.vstack([G, G2]), p)
            vecs = matmul_mod(np.asarray(cs, dtype=np.int64) % p, np.asarray(K.T, dtype=np.int64) % p, p)
            assert check_kernel_mat(E, vecs.T, p)
            rec['ideal_chi'] = vecs.tolist()
            rec['ideal_chi_values_are'] = f'native chi-coordinate vectors mod {p} (no transform), columns = the chi-orbits of build_cell'
            rec['ideal_terms'] = [expand_vector(B['arr'], v, p, R, n=n3) for v in vecs] if B['N_S'] * len(vecs) <= 3_000_000 else None
        if nc * a <= 400_000:
            rec['kernel_chi'] = K.T.tolist()
            rec['kernel_chi_values_are'] = f'native chi-coordinate kernel vectors mod {p} (no transform), columns = the chi-orbits of build_cell'
        per_prime[str(p)] = rec
        if verbose:
            log(f"  per{R} {mu} d{delta} p={p}: a={a} n_chi={nc} mult={m} units={a - m}{'  *** DROP ***' if m < a else ''} [{rec['secs']}s]")
    out['per_prime'] = {p: {k: v for k, v in r.items() if k not in ('kernel_chi', 'ideal_chi', 'ideal_terms')} for p, r in per_prime.items()}
    ms = {p: r['mult'] for p, r in per_prime.items()}
    agree = len(set(ms.values())) == 1
    out['primes_agree'] = agree
    out['mult'] = ms[str(PRIMES[0])] if agree else None
    out['units'] = (a - out['mult']) if agree else None
    if control_diag:
        out['status'] = ('CONTROL PASS: mult = 0 at both primes on the split-cubic family' if agree and out['mult'] == 0
                         else 'CONTROL FAIL: the split-cubic family must read mult = 0 at every weight of length >= 4')
        out['halt'] = bool(not (agree and out['mult'] == 0))
    else:
        out['status'] = ('PRIMES DISAGREE' if not agree else
                         'proved: mult = a at both primes (S_mu not in the ideal over Q)' if out['mult'] == a else
                         f'DROP measured: units = {out["units"]} at both primes, re-checked at 3a+24 fresh points -- verification protocol')
        out['halt'] = bool(not agree or out['mult'] != a)
    out['secs'] = round(time.time() - t0, 1); out['hwm_gb'] = round(_rss_gb(), 2)
    if certs:
        os.makedirs(certs, exist_ok=True)
        tag = '_'.join(map(str, mu)) + f'_d{delta}'
        files = []
        for p_str, r in per_prime.items():
            p = int(p_str)
            if 'kernel_chi' in r and r['mult'] == a and B['N_S'] * a <= 3_000_000:
                basis_terms = [expand_vector(B['arr'], np.array(v, dtype=np.int64), p, R, n=n3) for v in r['kernel_chi']]
                # NO board_numbering here: gct-cert/1 is a CLOSED schema and tools/verify
                # rejects an unknown top-level key (correctly).  The board number lives in
                # the manifest and the report, which is what the preamble asks for.
                cert = {"format": "gct-cert/1", "kind": "full_rank",
                        "title": f"cubic side: mult_per3({mu}, {delta}) = a = {a} mod {p} in Sym^{delta}(Sym^3 C^{R}) -- S_mu not in I(D_{R}^per3) ({SESSION})",
                        "produced_by": f"analysis/b13_09_per_r.py ({SESSION})",
                        "cell": {"n": n3, "r": R, "lambda": [int(x) for x in mu], "delta": int(delta), "a": int(a)},
                        "conventions": dict(CONVENTIONS), "prime": int(p), "variety": "permanent_pencil",
                        "points": [{"type": "permanent_pencil", "pencil": pt} for pt in pts], "basis": basis_terms}
                fn = os.path.join(certs, f'per{R}_{tag}_fullrank_p{p}.json.gz')
                with gzip.open(fn, 'wt', encoding='utf-8') as f:
                    json.dump(cert, f, separators=(',', ':'))
                if os.path.getsize(fn) > 4_500_000: os.remove(fn)
                else: files.append([os.path.relpath(fn, ROOT), os.path.getsize(fn)])
            if 'ideal_chi' in r:
                fn = os.path.join(certs, f'per{R}_{tag}_ideal_p{p}.json.gz')
                with gzip.open(fn, 'wt', encoding='utf-8') as f:
                    json.dump(dict(board_numbering='batch13', session=SESSION, mu=list(mu), delta=delta, r=R, prime=p, a=a,
                                   ideal_chi=r['ideal_chi'], values_are=r['ideal_chi_values_are'], ideal_terms=r['ideal_terms'],
                                   points=pts, recheck_points=per3_pencils(3 * a + 24, SEED_RECHECK, BOUND, R)), f, separators=(',', ':'))
                files.append([os.path.relpath(fn, ROOT), os.path.getsize(fn)])
        out['certs'] = files
    if verbose:
        log(f"  PER{R} RESULT {mu} d{delta}: a={a} N_S={B['N_S']} n_chi={nc} mult={out['mult']} units={out['units']} {out['status']} ({out['secs']}s, HWM {out['hwm_gb']} GB)")
    return out


if __name__ == '__main__':
    args = sys.argv[1:]
    def arg(name, default):
        return type(default)(args[args.index(name) + 1]) if name in args else default
    pos = []; i = 0
    while i < len(args):
        if args[i].startswith('--') and i + 1 < len(args) and not args[i + 1].startswith('--'): i += 2
        elif args[i].startswith('--'): i += 1
        else: pos.append(int(args[i])); i += 1
    delta, mu = pos[0], tuple(pos[1:])
    res = measure_weight(mu, delta, verbose='--quiet' not in args, certs=arg('--certs', '') or None,
                         a_given=(arg('--a', -1) if '--a' in args else None), control_diag='--control-diag' in args)
    print("RESULT " + json.dumps(res), flush=True)
    outp = arg('--out', '')
    if outp:
        with open(outp, 'a') as f: f.write(json.dumps(res) + "\n")
