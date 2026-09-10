#!/usr/bin/env python3
"""
B13-09 -- an INDEPENDENT re-check of the banked `mult = a` readings, by a route
that never forms the kernel.

The sweep's reading is `mult = rank_p(ev . K)` where `K` is the hybrid's exact
mod-p kernel of the raising operator `E` on `V_chi`.  That path depends on the
initial-term cover, the Schur complement, the triangular lift and the projection
retries of wk11_s71_hybrid.  This verifier decides the same question without any
of them, by the criterion sessions 43 and 47 used ("inject"):

    mult(mu, delta) = a   <=>   the stacked matrix  [ E ; ev ]  has FULL COLUMN RANK n_chi.

  (=>) if [E; ev] had a nonzero kernel vector v, then E v = 0 so v is a
       highest-weight vector, and ev.v = 0 so v is in the ideal, giving
       mult <= a - 1.
  (<=) if mult = a then every nonzero v with E v = 0 has ev.v != 0, and any
       kernel vector of [E; ev] is such a v; so there is none.

and a full column rank is read as a PROOF, not a probability: for any matrix P,
rank(P.M) <= rank(M) <= n_chi, so a projected rank of n_chi forces
rank(M) = n_chi.  P here is a sparse random +-1 matrix with n_chi + 32 rows, so
the flint rank is taken on an (n_chi + 32) x n_chi dense matrix -- which is why
this verifier is applied to the weights whose n_chi fits the cap (default 4200),
and reports the rest as not covered rather than pretending to cover them.

It also re-derives, on the same projection, `rank_p(E) = n_chi - a`, which pins
`a` a FOURTH way -- from the raising operator itself, independently of both the
Weyl alternation and the symmetric-function plethysm.

Everything here is rebuilt from the weight: its own `build_cell`, its own point
family (regenerated from the recorded seed and bound), its own projection seed,
its own flint ranks.  The only shared code is the engine's build, which is the
thing the calibration against s47/s79 tests.

A weight that FAILS is reported and the run returns nonzero; a check that could
not place a weight is reported as such and never silently skipped.

usage: python3 analysis/b13_09_verify.py [--in results/b13_09/per_r7_d7.jsonl ...]
          [--out results/b13_09/verify.json] [--nchi-cap 4200] [--seed 20260910]
"""
import sys, os, json, time, random
for _v in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ.setdefault(_v, '1')
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
os.environ.setdefault('S71_SCHUR_SO', '/home/claude/b13_09/schur.so')
import numpy as np
from scipy import sparse
from flint import nmod_mat
import wk11_s71_codes; wk11_s71_codes.install()
from wk8_s30_core import P1, P2
from wk9_s45_build import build_cell
from wk9_s42_census import a_weyl
from b13_09_per_r import per3_pencils, per3_coeffs, SEED, BOUND
from wk12_s79_cell6 import ev_rows_from_coeffs

PRIMES = (P1, P2)


def flint_rank(M, p):
    M = np.asarray(M, dtype=np.int64) % p
    if M.size == 0: return 0
    return nmod_mat(M.shape[0], M.shape[1], M.ravel().tolist(), p).rank()


def project(M, rows, p, rng, per=8):
    """sparse random +-1 projection of a CSR matrix M to `rows` rows, mod p.
    rank(P.M) <= rank(M), so a full column rank read on the projection is a proof."""
    n = M.shape[0]
    cols = np.repeat(np.arange(n), per)
    rws = rng.integers(0, rows, size=n * per)
    sg = rng.choice(np.array([-1, 1], dtype=np.int64), size=n * per)
    P = sparse.csr_matrix((sg, (rws, cols)), shape=(rows, n), dtype=np.int64)
    return np.asarray((P @ M).todense(), dtype=np.int64) % p


def verify_weight(mu, delta, a_banked, mult_banked, nchi_cap, seed, verbose=True):
    mu = tuple(mu); R = len(mu)
    t0 = time.time()
    out = dict(mu=list(mu), delta=delta, r=R, a_banked=a_banked, mult_banked=mult_banked)
    aw = a_weyl(mu, delta, 3, {})
    out['a_weyl'] = int(aw)
    if aw != a_banked:
        out.update(verdict='FAIL', why='the Weyl alternation disagrees with the banked a'); return out
    B = build_cell(mu, delta, n=3, verbose=False)
    nc = B['n_chi']; E = B['E'].tocsr()
    out.update(n_chi=nc, N_S=B['N_S'])
    if nc > nchi_cap:
        out.update(verdict='NOT COVERED', why=f'n_chi {nc} above this verifier\'s dense cap {nchi_cap}',
                   secs=round(time.time() - t0, 1))
        return out
    pts = per3_pencils(a_banked + 8, SEED, BOUND, R)
    rng = np.random.default_rng(seed + nc)
    per_prime = {}
    ok = True
    for p in PRIMES:
        EV = ev_rows_from_coeffs(B['arr'], [per3_coeffs(pt, R) for pt in pts], p, R, n=3)
        St = sparse.vstack([E, sparse.csr_matrix(EV % p)]).tocsr()
        rk_stack = flint_rank(project(St, nc + 32, p, rng), p)
        rk_E = flint_rank(project(E, nc + 32, p, rng), p)
        rec = dict(rank_stacked=int(rk_stack), n_chi=int(nc), full_column_rank=bool(rk_stack == nc),
                   rank_E=int(rk_E), a_from_operator=int(nc - rk_E))
        # the operator's own nullity pins a, independently of both plethysm routes
        rec['a_agrees'] = bool(nc - rk_E == a_banked)
        rec['implies_mult_eq_a'] = bool(rk_stack == nc)
        per_prime[str(p)] = rec
        if not (rec['a_agrees'] and rec['full_column_rank'] == (mult_banked == a_banked)): ok = False
    out['per_prime'] = per_prime
    agree_full = all(v['full_column_rank'] for v in per_prime.values())
    out['verdict'] = ('PASS' if ok and (agree_full == (mult_banked == a_banked)) else 'FAIL')
    out['statement'] = ('[E; ev] has full column rank n_chi at both primes, so mult = a: '
                        'S_mu is NOT in I(D_r^{per_3})_delta -- proved over Q, kernel-free route'
                        if agree_full else
                        '[E; ev] is column-rank deficient at a prime: consistent with the banked drop')
    out['secs'] = round(time.time() - t0, 1)
    if verbose:
        print(f"  verify {mu} d{delta}: n_chi={nc} a={a_banked} (operator says "
              f"{ {p: v['a_from_operator'] for p, v in per_prime.items()} }) "
              f"stacked rank {[v['rank_stacked'] for v in per_prime.values()]} -> {out['verdict']} [{out['secs']}s]",
              file=sys.stderr, flush=True)
    return out


def main(argv):
    ins = []
    if '--in' in argv:
        i = argv.index('--in') + 1
        while i < len(argv) and not argv[i].startswith('--'): ins.append(argv[i]); i += 1
    if not ins:
        ins = sorted(os.path.join(ROOT, 'results', 'b13_09', f)
                     for f in os.listdir(os.path.join(ROOT, 'results', 'b13_09'))
                     if f.startswith('per_r') and f.endswith('.jsonl'))
    out_path = argv[argv.index('--out') + 1] if '--out' in argv else os.path.join(ROOT, 'results', 'b13_09', 'verify.json')
    nchi_cap = int(argv[argv.index('--nchi-cap') + 1]) if '--nchi-cap' in argv else 4200
    seed = int(argv[argv.index('--seed') + 1]) if '--seed' in argv else 20260910
    recs = []
    for path in ins:
        for ln in open(path):
            try: recs.append(json.loads(ln))
            except Exception: pass
    seen = set(); todo = []
    for rec in recs:
        k = (tuple(rec['mu']), rec['delta'])
        if k in seen or rec.get('mult') is None: continue
        seen.add(k); todo.append(rec)
    todo.sort(key=lambda rec: rec.get('n_chi') or 0)
    res = dict(board_numbering='batch13', session='B13-09', route='kernel-free: full column rank of [E; ev] (the s43/s47 inject criterion)',
               primes=list(PRIMES), nchi_cap=nchi_cap, projection_seed=seed, sources=[os.path.relpath(p, ROOT) for p in ins],
               weights=[])
    fails = 0
    for rec in todo:
        v = verify_weight(rec['mu'], rec['delta'], rec['a'], rec['mult'], nchi_cap, seed)
        res['weights'].append(v)
        if v['verdict'] == 'FAIL': fails += 1
    res['summary'] = dict(considered=len(todo),
                          passed=sum(1 for v in res['weights'] if v['verdict'] == 'PASS'),
                          failed=fails,
                          not_covered=sum(1 for v in res['weights'] if v['verdict'] == 'NOT COVERED'))
    json.dump(res, open(out_path, 'w'), indent=1)
    print(f"verify: {res['summary']} -> {out_path}", file=sys.stderr)
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
