#!/usr/bin/env python3
"""
B13-08 -- the lean contingency driver: wk12_s79_per6.measure_weight with exactly
two MEMORY-ONLY changes, used only for a weight the unchanged engine could not
finish within this host's memory (results/PREREG_b13_08.md section 6).

    1. the kernel check E . K == 0 (mod p) is evaluated in row blocks of E
       (check_kernel_mat_rowblocked below): the same predicate, never more than
       ROWS_PER_BLOCK rows of E @ K live at once.  Patched into wk11_s71_hybrid's
       namespace so hybrid_kernel's own verification uses it.
    2. the evaluation rows are formed eight points at a time (the pattern of
       wk12_s79_cell6._prime_job) and G = ev . K is stacked from the eight-point
       blocks: the same points in the same order, so G is the same matrix.

Everything else -- the build, the cover, the hybrid kernel and its seeds, the
point families and their seeds, the ranks, the re-check on a drop, the
certificate format -- is the engine's code, imported, not copied.  Records
carry engine = "lean (b13_08)" so the report can say which weights ran here.

usage: python3 analysis/wk13_b08_per6_lean.py delta mu1 .. mu6 [--a A] [--out FILE] [--certs DIR]
"""
import sys, os, time, json, gzip
for _v in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ.setdefault(_v, '1')
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
os.environ.setdefault('S71_SCHUR_SO', '/home/claude/b13_08/schur.so')
import numpy as np
import wk11_s71_hybrid
import wk12_s79_per6 as ENGINE
from wk12_s79_per6 import (per3_pencils, per3_coeffs, n3, R, PRIMES, SEED, BOUND, SEED_RECHECK, HYB_SEED)
from wk9_s45_build import build_cell, log, _rss_gb
from wk9_s42_census import a_weyl
from wk9_s60_cell import CONVENTIONS
from wk11_s71_hybrid import best_cover, hybrid_kernel, matmul_mod, rank_mod_p, nullspace_mod_p
from wk12_s79_cell6 import ev_rows_from_coeffs, expand_vector

ROWS_PER_BLOCK = 1_000_000
ENGINE_TAG = "lean (b13_08)"


def check_kernel_mat_rowblocked(E, K, p, chunk=16, rows_per_block=ROWS_PER_BLOCK):
    """E K == 0 mod p, the predicate of wk11_s71_hybrid.check_kernel_mat, evaluated on
    row blocks of E so that at most rows_per_block x chunk entries of E @ K exist at once."""
    assert int(np.abs(E.data).max(initial=0)) < 65536
    K = np.asarray(K, dtype=np.int64) % p
    E = E.tocsr()
    for c0 in range(0, K.shape[1], chunk):
        Kc = K[:, c0:c0 + chunk]
        lo = Kc & 0xFFFF; hi = Kc >> 16
        for r0 in range(0, E.shape[0], rows_per_block):
            Eb = E[r0:r0 + rows_per_block]
            r = ((Eb @ lo) % p + ((Eb @ hi) % p) * 65536) % p
            if np.any(r): return False
            del Eb, r
    return True


def install():
    """route every kernel check of this process through the row-blocked predicate."""
    wk11_s71_hybrid.check_kernel_mat = check_kernel_mat_rowblocked
    ENGINE.check_kernel_mat = check_kernel_mat_rowblocked


def ev_times_K(arr, coeff_dicts, p, Kp_, block=8):
    """G = ev . K formed eight points at a time (same points, same order -> the same G)."""
    parts = []
    for c0 in range(0, len(coeff_dicts), block):
        EV = ev_rows_from_coeffs(arr, coeff_dicts[c0:c0 + block], p, R, n=n3)
        parts.append(matmul_mod(EV % p, Kp_, p)); del EV
    return np.vstack(parts)


def measure_weight_lean(mu, delta, verbose=True, certs=None, a_given=None, want_K=False):
    install()
    mu = tuple(mu); assert len(mu) == R and sum(mu) == 3 * delta
    t0 = time.time()
    aw = a_weyl(mu, delta, n3, {})
    if a_given is None:
        from wk8_s30_pleth import a_of
        a = a_of(mu, delta, n3, R)
        assert a == aw, ('a: plethysm and Weyl alternation disagree', mu, delta, a, aw)
    else:
        a = int(a_given)
        assert a == aw, ('a: queue value and Weyl alternation disagree', mu, delta, a, aw)
    out = dict(mu=list(mu), delta=delta, n=n3, r=R, a=int(a), route='hybrid (n=3, per_3 pencils)', engine=ENGINE_TAG,
               seeds=dict(per3=SEED, recheck=SEED_RECHECK), bound=BOUND, primes=list(PRIMES))
    if a == 0:
        out.update(status='a=0', secs=round(time.time() - t0, 1)); return out
    B = build_cell(mu, delta, n=n3, verbose=verbose)
    nc = B['n_chi']; E = B['E']
    out.update(N_S=B['N_S'], stab=B['stab'], n_chi=nc, nrows=B['nrows'], nnz=B['nnz'], build_secs=round(B['build_secs'], 1),
               NS_delta=int(B['N_S']) * int(delta), build_hwm_gb=round(_rss_gb(), 2))
    Kp = a + 8
    pts = per3_pencils(Kp, SEED, BOUND)
    cov = best_cover(E, nc, seed=HYB_SEED)
    out['cover_E'] = dict(size=cov['size'], order=cov['order'], excess=int(nc - cov['size'] - a))
    per_prime = {}; Ks = {}
    coeffs = [per3_coeffs(pt) for pt in pts]
    for p in PRIMES:
        tp = time.time()
        K, info = hybrid_kernel(E, nc, p, a, cov, seed=HYB_SEED, tag=f"[per6-lean {'_'.join(map(str, mu))}d{delta}]", verbose=verbose)
        Kp_ = np.asarray(K % p, dtype=np.int64)
        G = ev_times_K(B['arr'], coeffs, p, Kp_)
        m = int(rank_mod_p(G, p))
        rec = dict(mult=m, units=int(a - m), hybrid=info, secs=round(time.time() - tp, 1))
        if m < a:
            pts2 = per3_pencils(3 * a + 24, SEED_RECHECK, BOUND)
            G2 = ev_times_K(B['arr'], [per3_coeffs(pt) for pt in pts2], p, Kp_)
            m2 = int(rank_mod_p(np.vstack([G, G2]), p))
            rec['recheck'] = dict(points=3 * a + 24, seed=SEED_RECHECK, mult_with_all_points=m2)
            cs = nullspace_mod_p(np.vstack([G, G2]), p)
            vecs = matmul_mod(np.asarray(cs, dtype=np.int64) % p, np.asarray(K.T, dtype=np.int64) % p, p)
            assert check_kernel_mat_rowblocked(E, vecs.T, p)
            rec['ideal_chi'] = vecs.tolist()
            rec['ideal_terms'] = [expand_vector(B['arr'], v, p, R, n=n3) for v in vecs] if B['N_S'] * len(vecs) <= 3_000_000 else None
        if nc * a <= 400_000:
            rec['kernel_chi'] = K.T.tolist()
        if want_K: Ks[p] = K.copy()
        del Kp_, G
        per_prime[str(p)] = rec
        if verbose:
            log(f"  per6-lean {mu} d{delta} p={p}: a={a} n_chi={nc} mult={m} units={a - m}{'  *** DROP ***' if m < a else ''} [{rec['secs']}s]")
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
                        "title": f"cubic side: mult_per3({mu}, {delta}) = a = {a} mod {p} in Sym^{delta}(Sym^3 C^6) -- S_mu not in I(D_6^per3) (B13-08, lean driver)",
                        "produced_by": "analysis/wk13_b08_per6_lean.py (B13-08; the engine of analysis/wk12_s79_per6.py with two memory-only changes)",
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
                                   values_are='chi-coordinates of the kernel basis, residues mod prime; ideal_terms expanded over the monomial basis, no transform',
                                   points=pts, recheck_points=per3_pencils(3 * a + 24, SEED_RECHECK, BOUND)), f, separators=(',', ':'))
                files.append([os.path.relpath(fn, ROOT), os.path.getsize(fn)])
        out['certs'] = files
    if verbose:
        log(f"  PER6-LEAN RESULT {mu} d{delta}: a={a} N_S={B['N_S']} n_chi={nc} mult={out['mult']} units={out['units']} {out['status']} ({out['secs']}s, HWM {out['hwm_gb']} GB)")
    if want_K:
        return out, Ks, B
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
    delta, mu = pos[0], tuple(pos[1:7])
    res = measure_weight_lean(mu, delta, certs=arg('--certs', '') or None, a_given=(arg('--a', -1) if '--a' in args else None))
    print("RESULT " + json.dumps(res), flush=True)
    outp = arg('--out', '')
    if outp:
        with open(outp, 'a') as f: f.write(json.dumps(res) + "\n")
