#!/usr/bin/env python3
"""
B13-05 -- validation cells on the real instrument (NOT a census; B13-09 owns the queue).

One cell at a time on the isotypic-reduced build (wk9_s45_build.build_cell, n = 3), exact kernel of the
raising rows at BOTH house primes by dense flint nullspace, evaluation at a + 8 per_3 pencils
(seed 41, box 40 -- session 41's family, the one s79 used), mult = rank_p(EV . K), units = a - mult.

Purpose: validate the census (N_S, |Stab|, a) against the builder that would actually run the queue,
give B13-09 a calibrated timing point, and check Theorem D (the ladder) empirically by measuring a
degree-8 cell and its degree-9 successor mu + 3e_1 independently.

    units = 0 at one prime PROVES mult = a over Q (rank_p <= rank_Q).
    A drop is a CANDIDATE only -- a sampled deficiency is a ceiling on i, never a floor.  The run
    re-checks at 3a + 24 fresh points (seed 907) and halts; it does not promote the drop.

usage: python3 analysis/wk13_b13_05_validate.py --cells "15,2,2,2,2,2,2@9;..." [--nchi-cap 20000]
board_numbering: batch13
"""
import sys, os, time, json, random, argparse
for _v in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ.setdefault(_v, '1')
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import numpy as np
import wk11_s71_codes; wk11_s71_codes.install()
from wk8_s30_core import restrict, per_form, P1, P2
from wk8_s30_pleth import a_of
from wk9_s42_census import a_weyl
from wk9_s45_build import build_cell, log, _rss_gb
from wk11_s71_hybrid import matmul_mod, rank_mod_p, nullspace_mod_p, check_kernel_mat
from wk12_s79_cell6 import ev_rows_from_coeffs

PER3, N_PER3 = per_form(3)
SEED, BOUND, SEED_RECHECK = 41, 40, 907


def per3_pencils(K, seed, bound, R):
    rnd = random.Random(seed)
    return [[[[rnd.randint(-bound, bound) for _ in range(3)] for _ in range(3)] for _ in range(R)] for _ in range(K)]


def per3_coeffs(pencil, R):
    As = [[pencil[i][a][b] for a in range(3) for b in range(3)] for i in range(R)]
    return restrict(PER3, N_PER3, 3, R, As)


def run_inject(B, rec, mu, delta, R, a, t0):
    """s43's injectivity certificate (session 42's sparse Wiedemann tool), wired to the s45 lean build.

        ker[E; Ev] = {weight-mu HWVs vanishing at the K points}, of dimension a - mult,
        so  [E; Ev] injective  <=>  mult = a,  for every a.

    NONSINGULAR is a Berlekamp-Massey minimal polynomial of degree exactly n_chi with f(0) != 0 --
    it proves nonsingularity with no randomness in the implication, and rank_p <= rank_Q carries it
    to Q.  A KERNEL vector proves only mult < a: it is verified against E, banked as a CANDIDATE,
    and the run halts.  Memory is O(nnz), not O(n_chi^2)."""
    from scipy import sparse
    import wk9_s42_sparse as SP
    SP.WORK = os.environ.get('WIED_WORK', '/home/claude/wied_work')
    SP.WIED = os.environ.get('WIED_BIN', '/home/claude/wied_bin')
    os.makedirs(SP.WORK, exist_ok=True)
    SP.build_bin()
    nc = B['n_chi']
    pts = per3_pencils(a + 8, SEED, BOUND, R)
    rec['route'] = 'inject (sparse Wiedemann on [E; Ev], s42/s43 tool, s45 lean build)'
    per_prime = {}
    for p in (P1, P2):
        tp = time.time()
        EV = ev_rows_from_coeffs(B['arr'], [per3_coeffs(pt, R) for pt in pts], p, R, n=3)
        Mp = B['E'].copy(); Mp.data = Mp.data % p
        S = sparse.vstack([Mp, sparse.csr_matrix(np.asarray(EV, dtype=np.int64) % p)], format='csr')
        S.eliminate_zeros()
        path = os.path.join(SP.WORK, f'b13_05_{delta}_{"_".join(map(str, mu))}_{p}_{os.getpid()}.csr')
        nrows, nnz = SP.write_csr_mat(S, p, path)
        st, payload, diag = SP.run_wied(path, p, 1, 0)
        tries = 0
        while st == 'INCONCLUSIVE' and tries < 6:
            tries += 1
            st, payload, diag = SP.run_wied(path, p, 1 + tries, 0)
        try: os.remove(path)
        except OSError: pass
        r2 = dict(status_wied=st, nrows=int(nrows), nnz=int(nnz), secs=round(time.time() - tp, 1),
                  diag=diag[-2:] if diag else [])
        if st == 'NONSINGULAR':
            r2.update(mult=a, units=0)
        elif st == 'KERNEL':
            y = np.asarray(payload, dtype=np.int64)
            assert len(y) == nc, ('kernel vector length', len(y), nc)
            resid = (B['E'].dot(y % p)) % p
            r2['kernel_verified_against_E'] = bool(not resid.any())
            assert r2['kernel_verified_against_E'], 'reported kernel vector fails E y = 0'
            r2.update(mult=None, units=None, ideal_chi=y.tolist())
        else:
            raise RuntimeError(('injectivity route inconclusive', mu, delta, p, diag[-3:]))
        per_prime[str(p)] = r2
        log(f"  {mu} d{delta} p={p}: a={a} n_chi={nc} {st}{'' if st=='NONSINGULAR' else '  *** CANDIDATE ONLY ***'} [{r2['secs']}s]")
    rec['per_prime'] = per_prime
    ms = {p: r['mult'] for p, r in per_prime.items()}
    agree = len(set(str(v) for v in ms.values())) == 1
    rec['primes_agree'] = agree
    rec['mult'] = per_prime[str(P1)]['mult']
    rec['units'] = per_prime[str(P1)]['units']
    rec['status'] = ('PRIMES DISAGREE -- instrument defect' if not agree else
                     'CERTIFIED i = 0: [E; Ev] NONSINGULAR at both primes (proves mult = a over Q)' if rec['mult'] == a else
                     'CANDIDATE: kernel vector found -- sampled ceiling on i, NOT a membership statement; verification protocol')
    rec['secs'] = round(time.time() - t0, 1)
    rec['hwm_gb'] = round(_rss_gb(), 2)
    return rec


def run_cell(mu, delta, nchi_cap):
    mu = tuple(mu); R = len(mu)
    t0 = time.time()
    aw = a_weyl(mu, delta, 3, {})
    ap = a_of(mu, delta, 3, R)
    assert aw == ap, ('a routes disagree', mu, delta, aw, ap)
    a = int(aw)
    rec = dict(mu=list(mu), delta=delta, r=R, ell=R, a=a, primes=[P1, P2],
               points=dict(family='per_3 pencils', seed=SEED, bound=BOUND, count=a + 8),
               values_are='raw evaluation rows over the isotypic-reduced chi basis, no transform')
    B = build_cell(mu, delta, n=3, verbose=True)
    nc = B['n_chi']
    rec.update(N_S=int(B['N_S']), stab=int(B['stab']), n_chi=int(nc), nrows=int(B['nrows']),
               nnz=int(B['nnz']), build_secs=round(B['build_secs'], 1), build_hwm_gb=round(B['hwm_gb'], 2))
    if nc > nchi_cap:
        return run_inject(B, rec, mu, delta, R, a, t0)
    E = B['E']
    Ed = np.asarray(E.todense(), dtype=np.int64) if hasattr(E, 'todense') else np.asarray(E, dtype=np.int64)
    pts = per3_pencils(a + 8, SEED, BOUND, R)
    per_prime = {}
    for p in (P1, P2):
        tp = time.time()
        K = nullspace_mod_p(Ed, p)                      # (nullity, n_chi)
        nul = K.shape[0]
        assert nul == a, ('kernel dimension != a', mu, delta, nul, a, p)
        assert check_kernel_mat(E, K.T % p, p), ('kernel does not satisfy E K = 0', mu, delta, p)
        EV = ev_rows_from_coeffs(B['arr'], [per3_coeffs(pt, R) for pt in pts], p, R, n=3)
        G = matmul_mod(EV % p, K.T % p, p)
        m = int(rank_mod_p(G, p))
        r2 = dict(kernel_dim=int(nul), mult=m, units=int(a - m), secs=round(time.time() - tp, 1))
        if m < a:
            pts2 = per3_pencils(3 * a + 24, SEED_RECHECK, BOUND, R)
            EV2 = ev_rows_from_coeffs(B['arr'], [per3_coeffs(pt, R) for pt in pts2], p, R, n=3)
            m2 = int(rank_mod_p(np.vstack([G, matmul_mod(EV2 % p, K.T % p, p)]), p))
            r2['recheck'] = dict(points=3 * a + 24, seed=SEED_RECHECK, mult_with_all_points=m2)
        per_prime[str(p)] = r2
        log(f"  {mu} d{delta} p={p}: a={a} n_chi={nc} mult={m} units={a-m}{'  *** DROP -- CANDIDATE ONLY ***' if m < a else ''} [{r2['secs']}s]")
    rec['per_prime'] = per_prime
    ms = {p: r['mult'] for p, r in per_prime.items()}
    agree = len(set(ms.values())) == 1
    rec['primes_agree'] = agree
    rec['mult'] = ms[str(P1)] if agree else None
    rec['units'] = (a - rec['mult']) if agree else None
    rec['status'] = ('PRIMES DISAGREE -- instrument defect' if not agree else
                     'CERTIFIED i = 0: mult = a at both primes (full rank mod p proves full rank over Q)' if rec['mult'] == a else
                     f"CANDIDATE drop, units = {rec['units']} -- sampled ceiling on i, NOT a membership statement; verification protocol")
    rec['secs'] = round(time.time() - t0, 1)
    rec['hwm_gb'] = round(_rss_gb(), 2)
    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--cells', required=True, help='semicolon-separated  mu1,mu2,...@delta')
    ap.add_argument('--nchi-cap', type=int, default=20000)
    ap.add_argument('--out', default='results/b13_05_validate.json')
    args = ap.parse_args()
    out = dict(board_numbering='batch13', session='B13-05', purpose='validation cells only -- B13-09 owns the numerical queue',
               instrument='wk9_s45_build.build_cell (n=3) + dense flint nullspace + per_3 pencil evaluation, both house primes',
               cells=[])
    if os.path.exists(args.out):
        out = json.load(open(args.out))
    done = {(tuple(c['mu']), c['delta']) for c in out['cells']}
    for spec in args.cells.split(';'):
        spec = spec.strip()
        if not spec: continue
        mus, ds = spec.split('@')
        mu = tuple(int(x) for x in mus.split(',')); delta = int(ds)
        if (mu, delta) in done:
            log(f'{mu} d{delta}: already banked, skipping'); continue
        rec = run_cell(mu, delta, args.nchi_cap)
        out['cells'].append(rec)
        json.dump(out, open(args.out, 'w'), indent=0)      # bank per cell
        log(f"BANKED {mu} d{delta}: {rec['status']}")
    log('wrote', args.out)


if __name__ == '__main__':
    main()
