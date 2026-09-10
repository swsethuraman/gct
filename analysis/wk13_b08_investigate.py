#!/usr/bin/env python3
"""
B13-08 -- the pre-registered investigation of a DROP (results/PREREG_b13_08.md
section 7): fresh points and an exact source check on the recorded kernel
vector(s), mod each prime.  Nothing here lifts a vector to Q or claims
membership; the output is a measurement.

For each prime p with an ideal file results/certs/b13_08_per6/per6_<tag>_ideal_p<p>.json.gz:
  (a) fresh family: 4a + 32 per_3 pencils, seed 20260909, bound 200, evaluated on the
      recorded chi-vector(s) through the engine's own evaluation rows (rebuild of the cell,
      no kernel computation) -- the rank of ev . V must be 0 for sampled vanishing to persist;
  (b) exact source check: the vector expanded over the monomial basis (ideal_terms) is
      evaluated at the same fresh pencils by direct term evaluation (wk8_s30_core.restrict
      for the point's coefficients, a product per term), with no chi-machinery;
  (c) the nullities and the behaviour under (a) and (b) are compared across the two primes.

usage: python3 analysis/wk13_b08_investigate.py mu1 .. mu6 [--delta 10] [--certs results/certs/b13_08_per6]
"""
import sys, os, json, gzip, random, time
for _v in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ.setdefault(_v, '1')
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
os.environ.setdefault('S71_SCHUR_SO', '/home/claude/b13_08/schur.so')
import numpy as np
import wk11_s71_codes; wk11_s71_codes.install()
from wk8_s30_core import per_form, restrict, P1, P2
from wk9_s45_build import build_cell
from wk11_s71_hybrid import matmul_mod, rank_mod_p, check_kernel_mat
from wk12_s79_cell6 import ev_rows_from_coeffs

R, n3 = 6, 3
PER3, N3 = per_form(3)
FRESH_SEED, FRESH_BOUND = 20260909, 200


def pencils(K, seed, bound):
    rnd = random.Random(seed)
    return [[[[rnd.randint(-bound, bound) for _ in range(3)] for _ in range(3)] for _ in range(R)] for _ in range(K)]


def coeffs(pt):
    As = [[pt[i][a][b] for a in range(3) for b in range(3)] for i in range(R)]
    return restrict(PER3, N3, n3, R, As)


def term_value(terms, co, p):
    """sum over terms of coeff * prod_j c_{alpha_j}(point), mod p, straight from the expanded polynomial."""
    tot = 0
    for alphas, c in terms:
        v = c % p
        for al in alphas:
            v = (v * (co.get(tuple(al), 0) % p)) % p
            if v == 0: break
        tot = (tot + v) % p
    return tot


def main(argv):
    pos = [int(x) for x in argv if not x.startswith('--') and x.lstrip('-').isdigit()]
    mu = tuple(pos[:6]); delta = int(argv[argv.index('--delta') + 1]) if '--delta' in argv else 10
    certs = argv[argv.index('--certs') + 1] if '--certs' in argv else os.path.join(ROOT, 'results', 'certs', 'b13_08_per6')
    tag = '_'.join(map(str, mu)) + f'_d{delta}'
    out = dict(mu=list(mu), delta=delta, fresh=dict(seed=FRESH_SEED, bound=FRESH_BOUND), per_prime={})
    B = build_cell(mu, delta, n=n3, verbose=False)
    for p in (P1, P2):
        fn = os.path.join(certs, f'per6_{tag}_ideal_p{p}.json.gz')
        if not os.path.exists(fn):
            out['per_prime'][str(p)] = dict(status='no ideal file'); continue
        I = json.load(gzip.open(fn, 'rt'))
        V = np.array(I['ideal_chi'], dtype=np.int64) % p        # nul x n_chi
        a = I['a']; nul = V.shape[0]
        assert check_kernel_mat(B['E'], V.T, p), "recorded vector is not in the kernel of E"
        pts = pencils(4 * a + 32, FRESH_SEED, FRESH_BOUND)
        cos = [coeffs(pt) for pt in pts]
        EV = ev_rows_from_coeffs(B['arr'], cos, p, R, n=n3)
        G = matmul_mod(EV % p, V.T % p, p)
        rank_fresh = int(rank_mod_p(G, p))
        rec = dict(a=a, nullity_recorded=nul, fresh_points=len(pts), rank_on_fresh_points=rank_fresh,
                   sampled_vanishing_persists=bool(rank_fresh == 0), E_times_v_zero=True)
        if I.get('ideal_terms'):
            direct = []
            for vi, T in enumerate(I['ideal_terms']):
                vals = [term_value(T['terms'], co, p) for co in cos]
                direct.append(dict(vector=vi, nterms=len(T['terms']), nonzero_at=sum(1 for v in vals if v), of=len(vals)))
            rec['exact_source_check'] = direct
            rec['exact_source_all_zero'] = all(d['nonzero_at'] == 0 for d in direct)
        else:
            rec['exact_source_check'] = 'ideal_terms not stored (N_S * nul > 3e6): expand from ideal_chi with wk12_s79_cell6.expand_vector before this check'
        out['per_prime'][str(p)] = rec
        print(f"  p={p}: nullity {nul}, rank of the {nul} recorded vector(s) on {len(pts)} fresh points = {rank_fresh} "
              f"(0 = sampled vanishing persists); exact source check: {rec.get('exact_source_all_zero')}", flush=True)
    both = [out['per_prime'].get(str(p), {}) for p in (P1, P2)]
    out['primes_agree_nullity'] = (both[0].get('nullity_recorded') == both[1].get('nullity_recorded'))
    out['status'] = 'MEASURED: a candidate deficiency, mod p only; not a membership statement over Q'
    fn = os.path.join(ROOT, 'results', 'b13_08', f'investigate_{tag}.json')
    json.dump(out, open(fn, 'w'), indent=1)
    print(json.dumps({k: v for k, v in out.items() if k != 'per_prime'}))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
