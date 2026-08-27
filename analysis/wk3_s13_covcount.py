"""Session 13: the n=3 covariant-space dimension count for the rigidity theorem.

Computes m = dim Hom_L(Sym4(W)* ⊗ (det_a det_b)^20-block, (Res_{P_H} S_λ')^{U_P})
i.e. the multiplicity pairing between the L-irreducible constituents of
Sym^4(W)* twisted by the base content det^20, and the α1=24 block of
S_λ'(C3⊗C3) branched to GL3a×GL3b, U_P-invariants taken on the a-side.

Pipeline:
  stage V:  validate the branching machinery (Kostant alternation over S3 +
            iterated Littlewood-Richardson via lrcalc) against brute-force
            character pairing on small S_λ(C3⊗C3).
  stage W:  decompose Sym4 W, W = C2_z ⊗ α^{-1} ⊗ gl3_y, into L-irreps
            (α-power, GL2-Schur (m1,m2), rational GL3-Schur γ·det^{-k}).
  stage M:  demanded (α, β) list from stage W duals + det^20 shift;
            multiplicities m(α, β) in S_λ'(C3⊗C3) by alternation with
            K_{μ,·} accumulated in one pass per μ over 3-row triples.
  stage R:  assemble m with per-constituent breakdown.

Weight conventions (pinned by the diagonal-torus computation, session 13):
  direction coordinate c_{r,j,a} (x_{r-row,j-col} += c·x_{0,a}) has L-weight
  (ε_r − ε_0)_a + (ε_j − ε_a)_b;  the degree-4 slice of the evaluation is a
  matrix element in Sym4(W)* ⊗ det_a^20 det_b^20 ⊗ S_λ'-constituents, forcing
  a-side α = (24, α2, α3), α2+α3 = 36, and b-side β ⊢ 60 within ±4 of
  (20,20,20).
"""
import itertools, sys, time
from functools import lru_cache
import sympy as sp
import lrcalc

LAM_PRIME = (8,8,8,6,6,6,6,6,6)

# ---------------- iterated LR machinery ----------------

@lru_cache(maxsize=None)
def lr_mult(sh1, sh2, rows):
    """s_sh1 * s_sh2 restricted to <= rows rows: dict partition -> coeff."""
    return tuple(sorted((tuple(k), v) for k, v in
                        lrcalc.mult(list(sh1), list(sh2), rows=rows).items()))

@lru_cache(maxsize=None)
def c_lam3(lam, e1, e2, e3):
    """c^lam_{e1,e2,e3} = sum_tau c^tau_{e1 e2} c^lam_{tau e3}."""
    tot = 0
    for tau, c in lr_mult(e1, e2, len(lam)):
        if sum(tau) + sum(e3) != sum(lam): continue
        c2 = lrcalc.lrcoef(list(lam), list(tau), list(e3))
        if c2: tot += c * c2
    return tot

def partitions_le3(n, cap=None):
    """partitions of n with at most 3 parts (cap = max part)."""
    if cap is None: cap = n
    out = []
    for a in range(min(n, cap), (n+2)//3 - 1, -1):
        for b in range(min(a, n-a), -1, -1):
            c = n - a - b
            if 0 <= c <= b: out.append((a, b, c) if c else ((a, b) if b else (a,)))
    return out

def K_mu_all(lam, mu):
    """dict beta -> multiplicity of S_beta(C3_b) in the a-torus-weight-mu
    subspace of S_lam(C3⊗C3). mu = (m1,m2,m3) nonneg ints, sum = |lam|."""
    out = {}
    if any(m < 0 for m in mu): return out
    P1 = partitions_le3(mu[0]); P2 = partitions_le3(mu[1]); P3 = partitions_le3(mu[2])
    for e1 in P1:
        for e2 in P2:
            prod12 = lr_mult(e1, e2, 3)
            if not prod12: continue
            for e3 in P3:
                c123 = c_lam3(lam, e1, e2, e3)
                if not c123: continue
                for t12, c12 in prod12:
                    for beta, cb in lr_mult(t12, e3, 3):
                        out[beta] = out.get(beta, 0) + c123 * c12 * cb
    return out

RHO3 = (2, 1, 0)
S3 = list(itertools.permutations(range(3)))
def sgn(p):
    s = 1
    for i in range(len(p)):
        for j in range(i+1, len(p)):
            if p[i] > p[j]: s = -s
    return s

def mult_alpha_beta_all(lam, alpha):
    """dict beta -> mult of S_alpha(C3_a)⊗S_beta(C3_b) in S_lam(C3⊗C3),
    by Kostant alternation on the a-side."""
    acc = {}
    for w in S3:
        wr = tuple(RHO3[w[i]] for i in range(3))
        mu = tuple(alpha[i] + RHO3[i] - wr[i] for i in range(3))
        if any(m < 0 for m in mu): continue
        s = sgn(w)
        for beta, k in K_mu_all(lam, mu).items():
            acc[beta] = acc.get(beta, 0) + s * k
    return {b: v for b, v in acc.items() if v}

# ---------------- stage V: validation ----------------

def brute_branching(lam, n=3):
    """Brute force: expand s_lam(x_i y_j) (n*n alphabet) via Jacobi-Trudi in
    complete homogeneous sums, then extract S_alpha⊗S_beta multiplicities by
    double Weyl alternation. Exact but only for small |lam|."""
    xs = sp.symbols(f'x0:{n}'); ys = sp.symbols(f'y0:{n}')
    prods = [xs[i]*ys[j] for i in range(n) for j in range(n)]
    N = sum(lam)
    # h_k of the product alphabet via power sums
    p = {k: sum(t**k for t in prods) for k in range(1, N+1)}
    h = {0: sp.Integer(1)}
    for k in range(1, N+1):
        h[k] = sp.expand(sum(p[i]*h[k-i] for i in range(1, k+1))/k)
    lamt = [len([1 for l in lam if l > i]) for i in range(max(lam))] if lam else []
    # Jacobi-Trudi on the CONJUGATE with elementary sums is heavier; use h-JT on lam directly
    m = len(lam)
    M = sp.Matrix(m, m, lambda i, j: h.get(lam[i]-i+j, sp.Integer(0)) if 0 <= lam[i]-i+j <= N else sp.Integer(0))
    slam = sp.expand(M.det())
    poly = sp.Poly(slam, *xs, *ys)
    # weight dict
    wd = {}
    for mono, cf in poly.terms():
        wd[(mono[:n], mono[n:])] = int(cf)
    def getw(a, b): return wd.get((tuple(a), tuple(b)), 0)
    rho = tuple(range(n-1, -1, -1))
    perms = list(itertools.permutations(range(n)))
    out = {}
    for alpha in partitions_le3(N):
        if len(alpha) > n: continue
        al = tuple(list(alpha) + [0]*(n-len(alpha)))
        for beta in partitions_le3(N):
            if len(beta) > n: continue
            be = tuple(list(beta) + [0]*(n-len(beta)))
            tot = 0
            for w1 in perms:
                mu = tuple(al[i] + rho[i] - rho[w1[i]] for i in range(n))
                if any(v < 0 for v in mu): continue
                for w2 in perms:
                    nu = tuple(be[i] + rho[i] - rho[w2[i]] for i in range(n))
                    if any(v < 0 for v in nu): continue
                    tot += sgn(w1)*sgn(w2)*getw(mu, nu)
            if tot: out[(alpha, beta)] = tot
    return out

def stage_V():
    print("== stage V: validation on S_lam(C3xC3), |lam| = 4 and 5 ==")
    ok = True
    for lam in [(2,1,1), (3,1), (2,2), (4,), (1,1,1,1), (3,2), (2,2,1)]:
        bf = brute_branching(lam)
        for alpha in set(a for a, b in bf) | {p for p in partitions_le3(sum(lam)) if len(p) <= 3}:
            got = mult_alpha_beta_all(lam, tuple(list(alpha)+[0]*(3-len(alpha))))
            for beta, v in got.items():
                bv = bf.get((alpha, tuple(b for b in beta if b)), 0) if False else bf.get((alpha, beta), bf.get((alpha, tuple(x for x in beta if x)), 0))
                if bv != v:
                    print(f"  MISMATCH lam={lam} alpha={alpha} beta={beta}: alt={v} brute={bv}")
                    ok = False
            for (a2, b2), v2 in bf.items():
                if a2 == alpha:
                    g = got.get(tuple(list(b2)+[0]*0), got.get(b2, 0))
                    if g != v2:
                        print(f"  MISMATCH lam={lam} alpha={alpha} beta={b2}: alt={g} brute={v2}")
                        ok = False
        print(f"  lam={lam}: {'OK' if ok else 'FAILED'}")
        if not ok: sys.exit(1)
    print("stage V PASSED")

if __name__ == '__main__':
    t0 = time.time()
    stage_V()
    print(f"[{time.time()-t0:.1f}s]")

# ---------------- stage W: Sym4(W) decomposition ----------------
# Sym4(X⊗Y) = ⊕_{rho ⊢ 4} S_rho(X) ⊗ S_rho(Y); X = C2_z·α^{-1} (2-dim),
# Y = gl3_y (9-dim). S_rho(Y) decomposed as ⊕ m_gt S_gt(y)·det_y^{-4}, gt ⊢ 12.

def schur_via_JT_of_h(hdict, lam):
    m = len(lam)
    M = sp.Matrix(m, m, lambda i, j: hdict.get(lam[i]-i+j, sp.Integer(0)))
    return sp.expand(M.det())

def decomp_poly_char_gl3(char_poly, ys):
    """decompose a polynomial GL3 character (sympy expr in ys) into Schurs
    by triple alternation on weights."""
    poly = sp.Poly(sp.expand(char_poly), *ys)
    wd = {}
    for mono, cf in poly.terms(): wd[mono] = int(cf)
    deg = sum(next(iter(wd)))  # homogeneous
    rho = (2,1,0)
    out = {}
    for gam in partitions_le3(deg):
        if len(gam) > 3: continue
        g3 = tuple(list(gam)+[0]*(3-len(gam)))
        tot = 0
        for w in S3:
            mu = tuple(g3[i] + rho[i] - rho[w[i]] for i in range(3))
            if any(v < 0 for v in mu): continue
            tot += sgn(w)*wd.get(mu, 0)
        if tot: out[g3] = tot
    return out

def stage_W():
    print("== stage W: Sym4 W decomposition ==")
    ys = sp.symbols('y0:3')
    gl3 = sp.expand(sum(ys[i]/ys[j] for i in range(3) for j in range(3)))
    # power sums of gl3 char
    pk = {k: sp.expand(sum((ys[i]/ys[j])**k for i in range(3) for j in range(3))) for k in range(1,5)}
    # S_rho[gl3] for rho ⊢ 4 via char formula: s_rho = det(h) JT with h_k[gl3]
    hk = {0: sp.Integer(1)}
    for k in range(1,5):
        hk[k] = sp.expand(sum(pk[i]*hk[k-i] for i in range(1,k+1))/k)
    det4 = (ys[0]*ys[1]*ys[2])**4
    RHOS = [(4,), (3,1), (2,2)]           # ell(rho) <= 2 only (X is 2-dim)
    demanded = []   # (rho, alpha, gtilde, beta, mult_in_Sym4W)
    total_dim = 0
    dim_gl2 = {(4,): 5, (3,1): 3, (2,2): 1}   # dim S_rho(C2) = rho1-rho2+1
    for rho in RHOS:
        ch = schur_via_JT_of_h(hk, list(rho))
        polych = sp.expand(ch*det4)
        dec = decomp_poly_char_gl3(polych, ys)
        r1, r2 = rho[0], (rho[1] if len(rho) > 1 else 0)
        alpha = (24, 20-r2, 20-r1)
        for gt, mg in sorted(dec.items()):
            beta = (24-gt[2], 24-gt[1], 24-gt[0])
            demanded.append((rho, alpha, gt, beta, mg))
            dimg = None
            # dim S_gt(C3) via Weyl dim formula
            a,b,c = gt
            dimg = (a-b+1)*(b-c+1)*(a-c+2)//2
            total_dim += dim_gl2[rho]*mg*dimg
    print(f"  dimension check: sum over constituents = {total_dim} vs C(21,4) = 5985: "
          f"{'OK' if total_dim == 5985 else 'FAIL'}")
    assert total_dim == 5985
    for rho, alpha, gt, beta, mg in demanded:
        print(f"  rho={rho} -> alpha={alpha}; gtilde={gt} x{mg} -> beta={beta}")
    return demanded

# ---------------- stage M + R ----------------

def stage_MR(demanded):
    print("== stage M: multiplicities m(alpha, beta) in S_lam'(C3xC3) ==")
    alphas = sorted(set(a for _, a, _, _, _ in demanded))
    mult = {}
    for al in alphas:
        t0 = time.time()
        mult[al] = mult_alpha_beta_all(LAM_PRIME, al)
        print(f"  alpha={al}: {len(mult[al])} betas with nonzero mult [{time.time()-t0:.0f}s]", flush=True)
    print("== stage R: assembly ==")
    m_total = 0
    for rho, alpha, gt, beta, mg in demanded:
        mb = mult[alpha].get(beta, 0)
        contrib = mg*mb
        if contrib:
            print(f"  rho={rho} alpha={alpha} beta={beta}: Sym4W-mult {mg} x branching {mb} = {contrib}")
        m_total += contrib
    print(f"\nRESULT: m = dim Hom_L(per-M-slot) = {m_total}")
    return m_total

if __name__ == '__main__' and '--full' in sys.argv:
    t0 = time.time()
    demanded = stage_W()
    m = stage_MR(demanded)
    print(f"[total {time.time()-t0:.0f}s]")
