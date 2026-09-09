#!/usr/bin/env python3
"""
Session 79, part 1 -- the stable pullback at a_inf > 1, both house primes.

The batch-10 stable instrument (analysis/wk10_int_stable_hwv.py, then
wk10_int_stable_subst.py; integrator code) tests one weight-|rho| tail rho at a
time in the stable picture of Proposition S (docs/s57_report.md):

    C[Z] = Sym(Sym^2 U + Sym^3 U + Sym^4 U),  U = C^5,  120 generators y_(d,alpha)
    HWV_rho(C[Z]) = common kernel of the four raisings E_{i,i+1}
    M_6 = closure{ (e_2, e_3, e_4)(A(s')) : A a traceless 5-pencil of 4x4 matrices }
    i_det^inf(rho) = dim { F in HWV_rho : F vanishes on M_6 } = a_inf - rank(ev . K)

That instrument only saved a kernel of dimension one.  This module keeps its
conventions verbatim (generators, raising rule, the char-poly point map, the
covariance check) and adds what a_inf = 4 needs:

  * the kernel K of the stacked raising operator at BOTH house primes, taken as
    the exact nullspace (python-flint) of a random projection R.E with nc + 24
    rows -- ker(R.E) contains ker(E); every vector is re-verified on the sparse
    E and the dimension is compared with a_inf (characteristic-zero Weyl
    alternation, wk9_s57_stable.a_inf).  nullity_p(E) >= a_inf always, so
    dim ker(R.E) = a_inf with every vector verified pins ker_p(E) exactly and
    identifies it with the reduction of the integral HWV lattice;
  * evaluation of the whole kernel at K_pts = a_inf + 8 integer points of M_6
    (the same integer pencils reduced mod each prime), G = ev.K, mult = rank_p G;
    full rank at one prime proves i_det^inf = 0 over Q (rank_p <= rank_Q);
  * the covariance check per kernel vector and prime -- F(A') = F(A) under
    A_{i+1} -> A_{i+1} + eps A_i, four raisings, eps in {1, 7, 999} -- together
    with a NEGATIVE control (a random weight-space vector, and for the first
    block a vector killed by three raisings but not the fourth) that must FAIL;
  * a JSON record per block under results/s79_stable/ with the kernel basis,
    the points, G and every check, for the independent checker
    wk12_s79_stable_check.py.

usage: python3 analysis/wk12_s79_stable.py 6,3,3,1 [4,4,3,2 ...] [--npts 12] [--out DIR]
                                            [--partial-control] [--seed 20260908]
"""
import itertools, json, os, random, sys, time
import numpy as np
from scipy import sparse
from flint import nmod_mat

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
from wk9_s57_stable import a_inf as a_inf_weyl

P1, P2 = 2147483647, 2147483629
PRIMES = (P1, P2)
NV = 5      # ell - 1 = 5 tail variables s_2..s_6 (called s_1..s_5 here)
N = 4       # 4x4 matrices
CONVENTIONS = {"generators": "y_(d,alpha) = coefficient of s^alpha in the degree-d form, d in {2,3,4}, 5 variables",
               "raising": "E_{i,i+1} y_(d,alpha) = (alpha_i + 1) y_(d, alpha + e_i - e_{i+1})  (0 if alpha_{i+1} = 0), extended as a derivation",
               "point": "y_(2,.), y_(3,.), y_(4,.) = coefficients of e_2, e_3, e_4 of det(t I - A(s')), A(s') = sum_k s_k A_k traceless",
               "source": "analysis/wk10_int_stable_hwv.py + wk10_int_stable_subst.py (batch-10 integrator instrument), unchanged conventions"}


def log(*a):
    print(*a, file=sys.stderr); sys.stderr.flush()


# ------------------------------------------------------------ generators
def monos(d):
    return [a for a in itertools.product(range(d + 1), repeat=NV) if sum(a) == d]


GENS = [(d, a) for d in (2, 3, 4) for a in monos(d)]
GIDX = {g: i for i, g in enumerate(GENS)}
assert len(GENS) == 120


def weight_monomials(w):
    """multisets of generators with exponent sum w (sorted tuples of generator indices),
    in the DFS order of the batch-10 instrument."""
    out = []; n = len(GENS)

    def rec(start, rem, cur):
        if all(x == 0 for x in rem):
            out.append(tuple(cur)); return
        if sum(rem) < 2: return
        for gi in range(start, n):
            d, a = GENS[gi]
            if d > sum(rem): continue
            if all(a[k] <= rem[k] for k in range(NV)):
                rec(gi, tuple(rem[k] - a[k] for k in range(NV)), cur + [gi])
    rec(0, tuple(w), [])
    return out


def raising_blocks(w, src):
    """the four raising operators E_{i,i+1} on the weight-w space, as COO triples
    (rows, cols, vals) against directly enumerated target bases; vals are small
    positive integers (the coefficient alpha_i + 1, accumulated)."""
    blocks = []
    for i in range(NV - 1):
        tw = list(w); tw[i] += 1; tw[i + 1] -= 1
        if tw[i + 1] < 0:
            blocks.append(dict(i=i, target=0, rows=np.zeros(0, np.int64), cols=np.zeros(0, np.int64), vals=np.zeros(0, np.int64)))
            continue
        tgt = weight_monomials(tuple(tw)); tix = {m: k for k, m in enumerate(tgt)}
        ent = {}
        for ci, m in enumerate(src):
            for pos in range(len(m)):
                d, a = GENS[m[pos]]
                if a[i + 1] == 0: continue
                na = list(a); na[i] += 1; na[i + 1] -= 1
                nm = tuple(sorted(m[:pos] + m[pos + 1:] + (GIDX[(d, tuple(na))],)))
                k = (tix[nm], ci); ent[k] = ent.get(k, 0) + a[i] + 1
        rows = np.array([k[0] for k in ent], dtype=np.int64); cols = np.array([k[1] for k in ent], dtype=np.int64)
        vals = np.array(list(ent.values()), dtype=np.int64)
        blocks.append(dict(i=i, target=len(tgt), rows=rows, cols=cols, vals=vals))
    return blocks


def stacked(blocks, nc, which=None):
    rows = []; cols = []; vals = []; off = 0
    for b in blocks:
        if which is None or b['i'] in which:
            rows.append(b['rows'] + off); cols.append(b['cols']); vals.append(b['vals'])
        off += b['target']
    if not rows:
        return sparse.csr_matrix((off, nc), dtype=np.int64)
    E = sparse.coo_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(off, nc), dtype=np.int64)
    return E.tocsr()


# ------------------------------------------------------------------ kernel
def _to_nmod(Mnp, p):
    """dense numpy int64 (entries in [0,p)) -> nmod_mat, by setitem (no giant Python list)."""
    m, n = Mnp.shape
    A = nmod_mat(m, n, p)
    for i in range(m):
        row = Mnp[i]
        nz = np.nonzero(row)[0]
        for j in nz:
            A[i, int(j)] = int(row[j])
    return A


def kernel_mod_p(E, nc, p, a_expect, seed, extra=24, retries=3):
    """exact nullspace of R.E for a random dense R with nc + extra rows; every
    vector verified on E; returns (K numpy nc x k with k = dim ker(R.E), verified flag)."""
    nr = E.shape[0]
    Et = E.T.tocsr()
    rng = np.random.default_rng(seed + p % 1000)
    for attempt in range(retries):
        m = nc + extra
        Gt = np.zeros((nc, m), dtype=np.int64)
        blk = 4096
        for r0 in range(0, nr, blk):
            r1 = min(nr, r0 + blk)
            Rb = rng.integers(0, 1 << 20, size=(r1 - r0, m), dtype=np.int64)     # entries < 2^20; E entries <= 6: no overflow
            Gt += Et[:, r0:r1] @ Rb
            Gt %= p
        G = np.ascontiguousarray(Gt.T % p); del Gt
        t = time.time()
        A = _to_nmod(G, p); del G
        X, nul = A.nullspace(); del A
        K = np.zeros((nc, nul), dtype=np.int64)
        for j in range(nul):
            for i in range(nc):
                K[i, j] = int(X[i, j])
        del X
        # verify on the full sparse E, exactly mod p
        EK = (E @ K) % p                     # E entries <= 6, K < 2^31: no overflow
        ok = not EK.any()
        log(f"    kernel p={p} attempt {attempt}: nullity(R.E) = {nul} (a_inf {a_expect}), verified on E: {ok}  [{time.time()-t:.1f}s nullspace]")
        if ok and (a_expect is None or nul == a_expect):
            return K, True
        if ok and nul > a_expect:
            # every projected-kernel vector is a genuine kernel vector: nullity_p(E) > a_inf
            return K, False
        extra += nc // 2 + 64
    raise RuntimeError("projection retries exhausted", p, a_expect)


def partial_control(w, p, seed=20260908, bound=10 ** 6):
    """negative control with teeth: a vector killed by three of the four raisings
    but not the fourth must PASS the covariance check at those three and FAIL it
    at the fourth.  Returns the per-raising outcome."""
    w = tuple(w) + (0,) * (NV - len(w))
    src = weight_monomials(w); nc = len(src)
    maxlen = max(len(m) for m in src)
    src_arr = np.full((nc, maxlen), len(GENS), dtype=np.int64)
    for ci, m in enumerate(src): src_arr[ci, :len(m)] = m
    blocks = raising_blocks(w, src)
    live = [b['i'] for b in blocks if b['target'] > 0]
    drop = live[-1]
    E3 = stacked(blocks, nc, which=[i for i in live if i != drop])
    K3, _ = kernel_mod_p(E3, nc, p, None, seed + 1)
    Ed = stacked(blocks, nc, which=[drop])
    img = (Ed @ K3) % p
    cols = [j for j in range(K3.shape[1]) if img[:, j].any()]
    assert cols, "every three-raising kernel vector is also killed by the fourth -- no partial control available"
    v = K3[:, cols[0]:cols[0] + 1]
    Acov = traceless_pencil(random.Random(4242), bound)
    base = eval_matrix(src_arr, v, point_values(Acov, p), p)
    out = {}
    for i in live:
        res = []
        for eps in (1, 7, 999):
            val = eval_matrix(src_arr, v, point_values(shifted(Acov, i, eps), p), p)
            res.append(bool(val == base))
        out[f"E_{i+1}{i+2}"] = dict(invariant=res, expected_invariant=bool(i != drop))
    ok = all(all(d['invariant']) == d['expected_invariant'] for d in out.values())
    return dict(rho=list(w), prime=p, dropped_raising=f"E_{drop+1}{drop+2}", three_raising_nullity=int(K3.shape[1]),
                per_raising=out, control_behaves=bool(ok))


def rank_mod_p(M, p):
    if M.size == 0: return 0
    return _to_nmod(np.ascontiguousarray(M % p), p).rank()


# ------------------------------------------------------------- the points
def pmul(a, b, p):
    o = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            e = tuple(x + y for x, y in zip(e1, e2)); o[e] = (o.get(e, 0) + c1 * c2) % p
    return {e: c for e, c in o.items() if c}


def padd(a, b, p):
    o = dict(a)
    for e, c in b.items(): o[e] = (o.get(e, 0) + c) % p
    return {e: c for e, c in o.items() if c}


def psc(a, s, p):
    return {e: (c * s) % p for e, c in a.items() if (c * s) % p}


def matmul(X, Y, p):
    return [[_sum([pmul(X[i][k], Y[k][j], p) for k in range(N)], p) for j in range(N)] for i in range(N)]


def _sum(polys, p):
    o = {}
    for q in polys: o = padd(o, q, p)
    return o


def trace(X, p):
    return _sum([X[i][i] for i in range(N)], p)


def traceless_pencil(rnd, bound):
    """5 random integer 4x4 matrices, each traceless (last diagonal entry fixes it)."""
    As = []
    for _ in range(NV):
        M = [[rnd.randint(-bound, bound) for _ in range(N)] for _ in range(N)]
        s = sum(M[i][i] for i in range(N - 1)); M[N - 1][N - 1] = -s
        As.append(M)
    return As


def point_values(As, p):
    """the 120 generator values at the pencil As (integers): coefficients of
    e_2, e_3, e_4 of det(tI - A(s')) with A(s') = sum_k s_k A_k, computed as in the
    batch-10 instrument through power sums (A traceless):
        g2 = -p2/2,  g3 = -p3/3,  g4 = p2^2/8 - p4/4."""
    A = [[{} for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            d = {}
            for k in range(NV):
                v = As[k][i][j] % p
                if v:
                    e = tuple(1 if q == k else 0 for q in range(NV)); d[e] = v
            A[i][j] = d
    A2 = matmul(A, A, p); A3 = matmul(A2, A, p); A4 = matmul(A2, A2, p)
    p2, p3, p4 = trace(A2, p), trace(A3, p), trace(A4, p)
    i2 = pow(2, p - 2, p); i3 = pow(3, p - 2, p); i4 = pow(4, p - 2, p); i8 = pow(8, p - 2, p)
    g = {2: psc(p2, (-i2) % p, p), 3: psc(p3, (-i3) % p, p), 4: padd(psc(pmul(p2, p2, p), i8, p), psc(p4, (-i4) % p, p), p)}
    return np.array([g[d].get(a, 0) for (d, a) in GENS], dtype=np.int64)


def eval_matrix(src_arr, K, yv, p):
    """values of every kernel vector at one point: prod over factors, then K^T . prod (mod p)."""
    prod = np.ones(src_arr.shape[0], dtype=np.int64)
    yext = np.concatenate([yv % p, np.array([1], dtype=np.int64)])
    for k in range(src_arr.shape[1]):
        prod = (prod * yext[src_arr[:, k]]) % p
    out = []
    for j in range(K.shape[1]):
        t = (K[:, j] * prod) % p          # < 2^31 each; sum of nc < 2^45 terms fits int64
        out.append(int(t.sum() % p))
    return out


def shifted(As, i, eps):
    Bs = [[list(r) for r in M] for M in As]
    for r in range(N):
        for c in range(N):
            Bs[i + 1][r][c] = Bs[i + 1][r][c] + eps * As[i][r][c]
    return Bs


# ------------------------------------------------------------------- block
def run_block(w, npts=None, seed=20260908, bound=10 ** 6, out_dir=None, do_partial=False, verbose=True):
    w = tuple(w) + (0,) * (NV - len(w))
    t0 = time.time()
    a_exp = a_inf_weyl(w, {})
    src = weight_monomials(w); nc = len(src)
    maxlen = max(len(m) for m in src)
    src_arr = np.full((nc, maxlen), len(GENS), dtype=np.int64)        # index len(GENS) = the value 1
    for ci, m in enumerate(src): src_arr[ci, :len(m)] = m
    blocks = raising_blocks(w, src)
    E = stacked(blocks, nc)
    if verbose:
        log(f"rho = {w}: a_inf = {a_exp}, raw weight space {nc}, targets {[b['target'] for b in blocks]}, nnz {E.nnz}  [{time.time()-t0:.1f}s build]")
    Kp = npts or (a_exp + 8)
    rnd = random.Random(seed)
    pts = [traceless_pencil(rnd, bound) for _ in range(Kp)]
    rec = dict(rho=list(w), weight=int(sum(w)), a_inf=int(a_exp), raw_weight_space=int(nc), targets=[int(b['target']) for b in blocks],
               nnz=int(E.nnz), K_pts=int(Kp), point_seed=seed, point_bound=bound, primes=list(PRIMES), conventions=CONVENTIONS,
               points=pts, per_prime={}, monomials=[list(m) for m in src])
    verdicts = {}
    for p in PRIMES:
        tp = time.time()
        K, ok = kernel_mod_p(E, nc, p, a_exp, seed)
        k = K.shape[1]
        rk = rank_mod_p(K, p)
        pr = dict(nullity=int(k), nullity_eq_a_inf=bool(ok), kernel_rank=int(rk), kernel_verified_on_E=True)
        if not ok:
            pr['status'] = 'F1: nullity_p(E) != a_inf'
            rec['per_prime'][str(p)] = pr; verdicts[p] = None
            log(f"  p={p}: F1 -- nullity {k} != a_inf {a_exp}"); continue
        # evaluation matrix G (K_pts x a) at the integer points reduced mod p
        yvs = [point_values(As, p) for As in pts]
        G = np.array([eval_matrix(src_arr, K, yv, p) for yv in yvs], dtype=np.int64)
        mult = rank_mod_p(G, p)
        pr['G'] = G.tolist(); pr['mult_det_inf'] = int(mult); pr['i_det_inf'] = int(a_exp - mult)
        # covariance check per kernel vector at a fixed pencil, plus negative controls
        Acov = traceless_pencil(random.Random(4242), bound)
        base = eval_matrix(src_arr, K, point_values(Acov, p), p)
        cov = dict(pencil_seed=4242, eps=[1, 7, 999], base=base, results={}, all_pass=True)
        for i in range(NV - 1):
            for eps in (1, 7, 999):
                val = eval_matrix(src_arr, K, point_values(shifted(Acov, i, eps), p), p)
                same = [bool(x == y) for x, y in zip(val, base)]
                cov['results'][f"E_{i+1}{i+2},eps={eps}"] = same
                if not all(same): cov['all_pass'] = False
        pr['covariance'] = cov
        # negative control 1: a random weight-space vector (not a HWV) must fail somewhere
        rr = np.random.default_rng(seed + 17 + p % 1000)
        vrand = rr.integers(1, p, size=(nc, 1), dtype=np.int64)
        b0 = eval_matrix(src_arr, vrand, point_values(Acov, p), p)
        fails = 0
        for i in range(NV - 1):
            v1 = eval_matrix(src_arr, vrand, point_values(shifted(Acov, i, 1), p), p)
            if v1 != b0: fails += 1
        pr['negative_control_random'] = dict(raisings_failed=int(fails), of=NV - 1, has_teeth=bool(fails > 0))
        # negative control 2 (optional): a vector killed by three raisings only must fail exactly the fourth
        if do_partial:
            pc = partial_control(w, p, seed=seed, bound=bound)
            pr['negative_control_partial'] = pc
            log(f"    partial control p={p}: dropped {pc['dropped_raising']}, three-raising nullity {pc['three_raising_nullity']}, behaves: {pc['control_behaves']}")
        pr['secs'] = round(time.time() - tp, 1)
        pr['kernel'] = K.T.tolist()
        rec['per_prime'][str(p)] = pr
        verdicts[p] = mult
        if verbose:
            log(f"  p={p}: nullity {k} = a_inf, rank K {rk}, G rank {mult} -> i_det^inf = {a_exp - mult}; covariance {'PASS' if cov['all_pass'] else 'FAIL'}; "
                f"random-vector control fails {fails}/{NV-1} raisings  [{pr['secs']}s]")
    vals = [v for v in verdicts.values() if v is not None]
    if len(vals) == len(PRIMES) and len(set(vals)) == 1:
        rec['mult_det_inf'] = int(vals[0]); rec['i_det_inf'] = int(a_exp - vals[0]); rec['primes_agree'] = True
        rec['status'] = ('PROVED: i_det^inf = 0 (full rank at both primes; one suffices)' if vals[0] == a_exp
                         else f'CANDIDATE: rank {vals[0]} < a_inf at both primes -- verification protocol')
    else:
        rec['mult_det_inf'] = None; rec['i_det_inf'] = None; rec['primes_agree'] = False; rec['status'] = 'UNRESOLVED (F1 or primes disagree)'
    rec['covariance_all_pass'] = all(rec['per_prime'][str(p)].get('covariance', {}).get('all_pass', False) for p in PRIMES)
    rec['secs'] = round(time.time() - t0, 1)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
        tag = '_'.join(str(x) for x in w if x)
        with open(os.path.join(out_dir, f"stable_{tag}.json"), 'w') as f:
            json.dump(rec, f)
        summ = {k: v for k, v in rec.items() if k not in ('points', 'monomials', 'per_prime')}
        summ['per_prime'] = {p: {k: v for k, v in d.items() if k not in ('kernel', 'G')} for p, d in rec['per_prime'].items()}
        with open(os.path.join(out_dir, f"stable_{tag}_summary.json"), 'w') as f:
            json.dump(summ, f, indent=1)
    log(f"  RESULT rho={w}: a_inf={a_exp} nc={nc} mult_det^inf={rec['mult_det_inf']} i_det^inf={rec['i_det_inf']} {rec['status']}  "
        f"covariance {'PASS' if rec['covariance_all_pass'] else 'FAIL'}  ({rec['secs']}s)")
    return rec


def main(argv):
    npts = int(argv[argv.index('--npts') + 1]) if '--npts' in argv else None
    out = argv[argv.index('--out') + 1] if '--out' in argv else os.path.join(ROOT, 'results', 's79_stable')
    seed = int(argv[argv.index('--seed') + 1]) if '--seed' in argv else 20260908
    tails = [tuple(int(x) for x in t.split(',')) for t in argv if ',' in t and not t.startswith('--')]
    pc = '--partial-control' in argv
    for t in tails:
        run_block(t, npts=npts, seed=seed, out_dir=out, do_partial=pc)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
