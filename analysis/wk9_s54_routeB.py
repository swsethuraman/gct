#!/usr/bin/env python3
"""
Session 54 -- Route B viability: base-locus degenerations of det_4 at r=5.

Base locus B_5 = {M : det M(s) ≡ 0} = 5-variable pencils whose image is a
bounded-rank-<=3 space of M_4. Over such M_0, an arc M(t,s)=M_0+tM_1+...+t^k M_k
has det M(t,s) = t^q f(s) + O(t^{q+1}); the leading quartic f is a point of the
exceptional image, i.e. of the boundary of D_5^{det_4}. We:
  (1) estimate the tangent dimension of the family of leading quartics f over
      each bounded-rank-3 stratum (rank of the collected 70-vectors mod p),
  (2) screen each f for reducibility (a linear factor) -- does l.c appear?

Strata implemented (bounded-rank-3 spaces E ⊆ M_4; s32 Thm 4 / Atkinson):
  ker   : common kernel vector      (column 1 == 0)              dim 12
  coker : common image hyperplane   (row 1 == 0)                 dim 12
  c21   : (2,1) compression         (rows 2..4 of cols 1,2 == 0) dim 10
  prim  : primitive k=4  M_0(y)t = phi(y ^ t)                    dim 4
"""
import sys, random, itertools, argparse, json
sys.path.insert(0, 'analysis')
from flint import nmod_mat, fmpz_mpoly_ctx, Ordering

P = 2147483647
R = 5   # variables s_1..s_5
n = 4   # 4x4

# --- s-polynomials as dict{exp-tuple(len R): coeff mod p} ---
def smul(a, b):
    out = {}
    for ea, ca in a.items():
        for eb, cb in b.items():
            e = tuple(ea[i] + eb[i] for i in range(R))
            out[e] = (out.get(e, 0) + ca * cb) % P
    return out

def sadd(acc, b, sign=1):
    for e, c in b.items():
        acc[e] = (acc.get(e, 0) + sign * c) % P

def lin(vec):
    """linear form from coeff vector (len R) -> {e_i: c}."""
    d = {}
    for i in range(R):
        if vec[i] % P:
            e = [0]*R; e[i] = 1; d[tuple(e)] = vec[i] % P
    return d

# --- matrix entry as poly in t: list indexed by t-power, each a linear s-form dict ---
def rand_pencil(rng, mask=None, bound=20):
    """M(s)=sum s_k B_k; B_k 4x4 int, optional mask(a,b)->bool zeroing entries."""
    B = [[[0]*n for _ in range(n)] for _ in range(R)]
    for k in range(R):
        for a in range(n):
            for b in range(n):
                if mask and not mask(a, b): continue
                B[k][a][b] = rng.randint(-bound, bound)
    # entry(a,b) -> linear form: {e_k: B[k][a][b]}
    return B

def entry_lin(B, a, b):
    return lin([B[k][a][b] for k in range(R)])

# masks / builders for the strata
def mask_ker(a, b):    return b != 0           # column 0 == 0  (common kernel e_0)
def mask_coker(a, b):  return a != 0           # row 0 == 0     (common cokernel)
def mask_c21(a, b):    return not (b in (0,1) and a in (1,2,3))   # (2,1) compression

def build_primitive(rng, bound=12):
    """M_0(y) t = phi(y ^ t): entry M_0(y)_{a,b} = sum_c phi[a][b][c] y_c,
    antisymmetric in (b,c). Realizes the k=4 primitive bounded-rank-3 space."""
    # phi: choose phi[a][b][c] antisymmetric in b,c
    phi = [[[0]*n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(b+1, n):
                v = rng.randint(-bound, bound)
                phi[a][b][c] = v; phi[a][c][b] = -v
    # M_0(y)_{a,b} = sum_c phi[a][b][c] y_c  -> B_c[a][b] = phi[a][b][c]
    B = [[[phi[a][b][c] for b in range(n)] for a in range(n)] for c in range(R if R<=n else n)]
    # pad to R pencils (extra s-vars act as 0 -> but we need a genuine 5-var pencil;
    # use the 4 primitive directions + 1 random singular extra to stay in bounded rank)
    while len(B) < R:
        B.append([[0]*n for _ in range(n)])
    return B

def det_ts(M0, jets):
    """det of M(t,s)=M0 + t*jets[0] + t^2*jets[1] + ...; returns {tpow: {s-exp4: coeff}}."""
    # entry(a,b) as dict tpow -> linear s-form
    def entry(a, b):
        e = {0: entry_lin(M0, a, b)}
        for i, J in enumerate(jets):
            lf = entry_lin(J, a, b)
            if lf: e[i+1] = lf
        return e
    E = [[entry(a, b) for b in range(n)] for a in range(n)]
    out = {}
    for perm in itertools.permutations(range(n)):
        sgn = 1
        pl = list(perm)
        for i in range(n):
            for j in range(i+1, n):
                if pl[i] > pl[j]: sgn = -sgn
        # product of E[a][perm[a]]
        prod = {0: {tuple([0]*R): 1}}   # tpow -> s-poly
        for a in range(n):
            fac = E[a][perm[a]]
            nxt = {}
            for tp1, sp1 in prod.items():
                for tp2, sp2 in fac.items():
                    tp = tp1 + tp2
                    nxt.setdefault(tp, {})
                    sadd(nxt[tp], smul(sp1, sp2))
            prod = nxt
        for tp, sp in prod.items():
            out.setdefault(tp, {})
            sadd(out[tp], sp, sgn)
    # clean zeros
    return {tp: {e: c for e, c in sp.items() if c % P} for tp, sp in out.items()
            if any(c % P for c in sp.values())}

# quartic monomial index (deg 4 in R vars)
QEXP = []
def _q(k, left, cur):
    if k == R-1: QEXP.append(tuple(cur+[left])); return
    for v in range(left+1): _q(k+1, left-v, cur+[v])
_q(0, 4, [])
QIDX = {e: i for i, e in enumerate(QEXP)}

def leading_quartic(dets):
    """lowest t-power q>=1 whose coefficient is a genuine quartic (deg 4 in s)."""
    for tp in sorted(dets):
        if tp == 0:
            assert not dets.get(0), "det M_0 not identically zero!"
            continue
        sp = dets[tp]
        # is it degree 4? (all exps sum to 4 by construction of det). vector:
        vec = [0]*len(QEXP)
        for e, c in sp.items():
            vec[QIDX[e]] = c % P
        if any(vec): return tp, vec
    return None, None

# reducibility via exact factorization over Z (recompute det over Z for one sample)
def factor_check_Z(M0, jets, tp):
    ctx = fmpz_mpoly_ctx.get(tuple(f's{i}' for i in range(R)), Ordering.lex)
    S = ctx.gens()
    # rebuild the t^tp coefficient exactly over Z using python ints (no mod)
    def entry(a, b):
        e = {0: [M0[k][a][b] for k in range(R)]}
        for i, J in enumerate(jets):
            e[i+1] = [J[k][a][b] for k in range(R)]
        return e
    E = [[entry(a, b) for b in range(n)] for a in range(n)]
    # compute only the t^tp coefficient as an fmpz_mpoly
    from itertools import permutations
    total = ctx.constant(0)
    for perm in permutations(range(n)):
        sgn = 1; pl = list(perm)
        for i in range(n):
            for j in range(i+1, n):
                if pl[i] > pl[j]: sgn = -sgn
        # product over a of entry(a,perm[a]); track t-power, keep <=tp
        prod = {0: ctx.constant(1)}
        for a in range(n):
            fac = E[a][perm[a]]
            nxt = {}
            for tp1, poly1 in prod.items():
                for ti, coeffs in fac.items():
                    tp2 = tp1 + ti
                    if tp2 > tp: continue
                    lforms = ctx.constant(0)
                    for k in range(R):
                        if coeffs[k]: lforms += coeffs[k]*S[k]
                    if lforms == 0: continue
                    nxt[tp2] = nxt.get(tp2, ctx.constant(0)) + poly1*lforms
            prod = nxt
        if tp in prod:
            total += sgn*prod[tp]
    if total == 0: return None
    fac = total.factor()   # (const, [(poly, mult), ...])
    def tdeg(poly):
        return max((sum(mono) for mono in poly.monoms()), default=0)
    degs = []
    lins = []
    for poly, m in fac[1]:
        td = tdeg(poly)
        degs.extend([td] * m)
        if td == 1:
            lins.append((str(poly), m))
    degs.sort()
    return dict(nfactors=sum(m for _, m in fac[1]),
                factor_degrees=degs,
                linear_factors=lins,
                reducible=(len(degs) > 1))

STRATA = {
    'ker':   lambda rng: rand_pencil(rng, mask_ker),
    'coker': lambda rng: rand_pencil(rng, mask_coker),
    'c21':   lambda rng: rand_pencil(rng, mask_c21),
    'prim':  lambda rng: build_primitive(rng),
}

def run_stratum(name, ntrials=60, kmax=3, seed=1, do_factor=True, nfac=8):
    rng = random.Random(seed)
    vecs = []          # leading quartic vectors (mod P)
    orders = {}
    fac_samples = []
    for _ in range(ntrials):
        M0 = STRATA[name](rng)
        jets = [rand_pencil(rng) for _ in range(kmax)]
        dets = det_ts(M0, jets)
        tp, vec = leading_quartic(dets)
        if tp is None: continue
        orders[tp] = orders.get(tp, 0) + 1
        vecs.append(vec)
    # tangent dimension = rank of collected vectors
    if vecs:
        M = nmod_mat(len(vecs), len(QEXP),
                     [int(v[j]) for v in vecs for j in range(len(QEXP))], P)
        tandim = M.rank()
    else:
        tandim = 0
    # factor a few leading quartics exactly
    rng2 = random.Random(seed+1000)
    nred = 0; ntested = 0
    for _ in ([] if not do_factor else range(min(nfac, ntrials))):
        M0 = STRATA[name](rng2); jets = [rand_pencil(rng2) for _ in range(kmax)]
        dets = det_ts(M0, jets); tp, vec = leading_quartic(dets)
        if tp is None: continue
        info = factor_check_Z(M0, jets, tp)
        ntested += 1
        if info and (info['linear_factors'] or info['reducible']): nred += 1
        fac_samples.append((tp, info))
    return dict(stratum=name, ntrials=ntrials, kmax=kmax,
                leading_orders=orders, tangent_dim=tandim,
                n_ambient=len(QEXP),
                reducible_of_tested=(nred, ntested),
                sample_factors=fac_samples[:4])

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--strata', default='ker,coker,c21,prim')
    ap.add_argument('--ntrials', type=int, default=60)
    ap.add_argument('--kmax', type=int, default=3)
    ap.add_argument('--out', default='results/s54_routeB.json')
    ap.add_argument('--nofactor', action='store_true')
    ap.add_argument('--nfac', type=int, default=8)
    a = ap.parse_args()
    res = []
    for name in a.strata.split(','):
        r = run_stratum(name, a.ntrials, a.kmax, do_factor=not a.nofactor, nfac=a.nfac)
        res.append(r)
        print(f"[{name}] leading t-orders={r['leading_orders']} "
              f"tangent_dim={r['tangent_dim']}/{r['n_ambient']} "
              f"reducible_of_tested={r['reducible_of_tested']}", flush=True)
    json.dump(res, open(a.out, 'w'), indent=1, default=str)
    print("wrote", a.out)
