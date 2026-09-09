#!/usr/bin/env python3
"""
Session 79, part 2 (theorem route) -- I(D_6^{per_3})_delta on the cubic side by
the hybrid, one length-6 weight per call.

D_6^{per_3} = closure{ per_3(sum_{i<=6} s_i A_i) } in Sym^3 C^6 (dim 50 in 56).
Sessions 37/41/43/47 proved I(D_6^{per_3})_delta = 0 for delta <= 8 with the
Wiedemann/injectivity route (hours per weight at n_chi ~ 10^5).  By Prop. 8(1)
of docs/transfer_lemma.md that gives mult_pad = mult_red at EVERY six-row
quartic weight of degree delta.  This driver continues the scan at delta >= 9 on
session 45's build with n = 3 and session 71's hybrid kernel:

    a       = mult of S_mu in Sym^delta(Sym^3 C^6)   (plethysm a_of, asserted = Weyl alternation)
    K       = exact mod-p kernel of the raising operator on V_chi (hybrid, verified on E)
    mult    = rank_p(ev_per3 . K),  K_pts = a + 8 points per_3(sum s_i A_i), seed 41, bound 40
              (session 41's family), both house primes
    units   = a - mult;  units = 0 at one prime proves S_mu is not in I(D_6^{per_3})_delta over Q.

A drop (units >= 1) is re-checked inside the same call at 3a + 24 fresh points
(seed 907) before it is banked, the kernel vector is exhibited, and the caller
halts: it would be the first permanent-specific equation the programme has seen.

usage: python3 analysis/wk12_s79_per6.py delta mu1 .. mu6 [--out FILE] [--certs DIR]
"""
import sys, os, time, json, gzip, random
for _v in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ.setdefault(_v, '1')
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
os.environ.setdefault('S71_SCHUR_SO', '/home/claude/s79/schur.so')
import numpy as np
import wk11_s71_codes; wk11_s71_codes.install()
from wk8_s30_core import exps, restrict, per_form, P1, P2
from wk8_s30_pleth import a_of
from wk9_s45_build import build_cell, log, _rss_gb
from wk9_s42_census import a_weyl
from wk9_s60_cell import CONVENTIONS
from wk11_s71_hybrid import best_cover, hybrid_kernel, matmul_mod, rank_mod_p, nullspace_mod_p, check_kernel_mat
from wk12_s79_cell6 import ev_rows_from_coeffs, expand_vector

n3 = 3
R = 6
PRIMES = (P1, P2)
PER3, N_PER3 = per_form(3)
SEED, BOUND, SEED_RECHECK = 41, 40, 907
HYB_SEED = 20260908


def per3_pencils(K, seed, bound):
    rnd = random.Random(seed)
    return [[[[rnd.randint(-bound, bound) for _ in range(3)] for _ in range(3)] for _ in range(R)] for _ in range(K)]


def per3_coeffs(pencil):
    As = [[pencil[i][a][b] for a in range(3) for b in range(3)] for i in range(R)]
    return restrict(PER3, N_PER3, n3, R, As)


def measure_weight(mu, delta, verbose=True, certs=None):
    mu = tuple(mu); assert len(mu) == R and sum(mu) == 3 * delta
    t0 = time.time()
    a = a_of(mu, delta, n3, R)
    aw = a_weyl(mu, delta, n3, {})
    assert a == aw, ('a: plethysm and Weyl alternation disagree', mu, delta, a, aw)
    out = dict(mu=list(mu), delta=delta, n=n3, r=R, a=int(a), route='hybrid (n=3, per_3 pencils)', seeds=dict(per3=SEED, recheck=SEED_RECHECK),
               bound=BOUND, primes=list(PRIMES))
    if a == 0:
        out.update(status='a=0', secs=round(time.time() - t0, 1)); return out
    B = build_cell(mu, delta, n=n3, verbose=verbose)
    nc = B['n_chi']; E = B['E']
    out.update(N_S=B['N_S'], stab=B['stab'], n_chi=nc, nrows=B['nrows'], nnz=B['nnz'], build_secs=round(B['build_secs'], 1),
               NS_delta=int(B['N_S']) * int(delta))
    Kp = a + 8
    pts = per3_pencils(Kp, SEED, BOUND)
    cov = best_cover(E, nc, seed=HYB_SEED)
    out['cover_E'] = dict(size=cov['size'], order=cov['order'], excess=int(nc - cov['size'] - a))
    per_prime = {}
    for p in PRIMES:
        tp = time.time()
        K, info = hybrid_kernel(E, nc, p, a, cov, seed=HYB_SEED, tag=f"[per6 {'_'.join(map(str, mu))}d{delta}]", verbose=verbose)
        EV = ev_rows_from_coeffs(B['arr'], [per3_coeffs(pt) for pt in pts], p, R, n=n3)
        G = matmul_mod(EV % p, K % p, p)
        m = int(rank_mod_p(G, p))
        rec = dict(mult=m, units=int(a - m), hybrid=info, secs=round(time.time() - tp, 1))
        if m < a:
            pts2 = per3_pencils(3 * a + 24, SEED_RECHECK, BOUND)
            EV2 = ev_rows_from_coeffs(B['arr'], [per3_coeffs(pt) for pt in pts2], p, R, n=n3)
            G2 = matmul_mod(EV2 % p, K % p, p)
            m2 = int(rank_mod_p(np.vstack([G, G2]), p))
            rec['recheck'] = dict(points=3 * a + 24, seed=SEED_RECHECK, mult_with_all_points=m2)
            cs = nullspace_mod_p(np.vstack([G, G2]), p)
            vecs = matmul_mod(np.asarray(cs, dtype=np.int64) % p, np.asarray(K.T, dtype=np.int64) % p, p)
            assert check_kernel_mat(E, vecs.T, p)
            rec['ideal_chi'] = vecs.tolist()
            rec['ideal_terms'] = [expand_vector(B['arr'], v, p, R, n=n3) for v in vecs] if B['N_S'] * len(vecs) <= 3_000_000 else None
        if nc * a <= 400_000:
            rec['kernel_chi'] = K.T.tolist()
        per_prime[str(p)] = rec
        if verbose:
            log(f"  per6 {mu} d{delta} p={p}: a={a} n_chi={nc} mult={m} units={a - m}{'  *** DROP ***' if m < a else ''} [{rec['secs']}s]")
    out['per_prime'] = {p: {k: v for k, v in r.items() if k not in ('kernel_chi', 'ideal_chi', 'ideal_terms')} for p, r in per_prime.items()}
    ms = {p: r['mult'] for p, r in per_prime.items()}
    agree = len(set(ms.values())) == 1
    out['primes_agree'] = agree
    out['mult'] = ms[str(PRIMES[0])] if agree else None
    out['units'] = (a - out['mult']) if agree else None
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
                cert = {"format": "gct-cert/1", "kind": "full_rank",
                        "title": f"cubic side: mult_per3({mu}, {delta}) = a = {a} mod {p} in Sym^{delta}(Sym^3 C^6) -- S_mu not in I(D_6^per3) (session 79)",
                        "produced_by": "analysis/wk12_s79_per6.py (session 79)",
                        "cell": {"n": n3, "r": R, "lambda": [int(x) for x in mu], "delta": int(delta), "a": int(a)},
                        "conventions": dict(CONVENTIONS), "prime": int(p), "variety": "permanent_pencil",
                        "points": [{"type": "permanent_pencil", "pencil": pt} for pt in pts], "basis": basis_terms}
                fn = os.path.join(certs, f'per6_{tag}_fullrank_p{p}.json.gz')
                with gzip.open(fn, 'wt', encoding='utf-8') as f:
                    json.dump(cert, f, separators=(',', ':'))
                if os.path.getsize(fn) > 4_500_000: os.remove(fn)
                else: files.append([os.path.relpath(fn, ROOT), os.path.getsize(fn)])
            if 'ideal_chi' in r:
                fn = os.path.join(certs, f'per6_{tag}_ideal_p{p}.json.gz')
                with gzip.open(fn, 'wt', encoding='utf-8') as f:
                    json.dump(dict(mu=list(mu), delta=delta, prime=p, a=a, ideal_chi=r['ideal_chi'], ideal_terms=r['ideal_terms'],
                                   points=pts, recheck_points=per3_pencils(3 * a + 24, SEED_RECHECK, BOUND)), f, separators=(',', ':'))
                files.append([os.path.relpath(fn, ROOT), os.path.getsize(fn)])
        out['certs'] = files
    if verbose:
        log(f"  PER6 RESULT {mu} d{delta}: a={a} N_S={B['N_S']} n_chi={nc} mult={out['mult']} units={out['units']} {out['status']} ({out['secs']}s, HWM {out['hwm_gb']} GB)")
    return out


if __name__ == '__main__':
    args = sys.argv[1:]
    def arg(name, default):
        return type(default)(args[args.index(name) + 1]) if name in args else default
    pos = [int(x) for x in args if not x.startswith('--') and x.lstrip('-').isdigit() and args[max(0, args.index(x) - 1)] not in ('--out', '--certs')]
    delta, mu = pos[0], tuple(pos[1:7])
    res = measure_weight(mu, delta, certs=arg('--certs', '') or None)
    print("RESULT " + json.dumps(res), flush=True)
    outp = arg('--out', '')
    if outp:
        with open(outp, 'a') as f: f.write(json.dumps(res) + "\n")
