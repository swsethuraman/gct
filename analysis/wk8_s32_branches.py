"""Session 32 -- 4-dimensional singular subspaces of M_4(C), and the reachable
cubics.

QUESTION (integrator, docs/l5_containment.md).  Is  s_1 . c  a 4x4 determinant
of linear forms in s_1..s_5, for generic quinary cubic c?  det(sum s_i A_i) is
divisible by s_1 iff S_0 := span(A_2..A_5) is a 4-dimensional space of SINGULAR
4x4 matrices.  For each branch of such spaces, the reachable family of cubics
G = det(M)/s_1 has dimension = rank of the Jacobian  params -> coeffs of G,
and containment needs 35 (= dim Sym^3 C^5).

THIS FILE IS AN INDEPENDENT REIMPLEMENTATION (brief task D) plus the new
branches (task C).  Two things are deliberately NOT shared with
analysis/l5contain.py:

  * the derivative mechanism.  l5contain.py uses the adjugate identity
    d(det)/dA_pq = cofactor(p,q).  Here the determinant is computed by Leibniz
    expansion over the ring of DUAL NUMBERS (entries a + eps.b, eps^2 = 0), so
    the eps-part IS the directional derivative and no cofactor identity is
    invoked anywhere.
  * the arithmetic.  Ranks are taken exactly over Q (Fraction-free Bareiss
    elimination on integer rows), and independently modulo a prime unrelated to
    2^61-1.

CLASSIFICATION (proved in docs/singular_spaces.md).  Let S_0 be 4-dimensional,
singular, of generic rank exactly 3 (generic rank <= 2 forces s_1 | c and
cannot give a generic c).  Then adj(M_0(y)) is a rank-one matrix of cubics, so
adj(M_0) = f . u v^T with u, v primitive vectors of forms and
deg f + deg u + deg v = 3.  Transposing S_0 leaves det(s_1 A_1 + M_0)
unchanged, so WLOG deg u <= deg v, hence deg u <= 1.

  deg u = 0 :  common kernel  --  the k = 1 compression space.
  deg u = 1 :  u(y) = L y and  M_0(y) L y = 0  identically, so
               beta(y,t) := M_0(y) L t  is bilinear and alternating, hence
               beta(y,t) = phi(y ^ t)  for a unique phi : Lambda^2 C^4 -> C^4.
               Well-definedness forces phi(C^4 ^ ker L) = 0.

So with k = rank L and a basis in which im L = <f_1..f_k>, ker L = <f_{k+1}..f_4>:

    column j of M_0(y)  =  phi(y ^ f_j)          for j <= k   (phi_{ij} = 0
                                                  unless i,j <= k)
    column j of M_0(y)  =  arbitrary linear in y for j >  k

That is ONE parametrised family indexed by k = 1,2,3,4, linear in its
parameters, and it exhausts the classification up to transpose.  k = 1 is the
common-kernel compression and k = 2 is the 2->1 compression (columns 1,2 of
every M_0(y) are multiples of the single fixed vector phi_{12}); k = 3 and
k = 4 are NOT compression spaces and are the exceptional branches this session
was sent to find.  k = 3 contains diag(N(x), w) with N(x) the 3x3 skew matrix
-- the "skew 3x3 padded by a scalar" example of results/PREREG_s32.md.

Usage:  python3 wk8_s32_branches.py
"""
import itertools, random, sys
from fractions import Fraction

R = 5                                    # variables s_1..s_5
MON3 = [e for e in itertools.product(range(4), repeat=R) if sum(e) == 3]
MON3.sort()
IDX = {e: k for k, e in enumerate(MON3)}
NC = len(MON3)                           # 35
ONE = {tuple([0] * R): 1}

PRIME = 1000003                          # unrelated to 2^61 - 1
PRIME2 = 2147483647
PRIME3 = 1000000007
ENTRY_HI = 9                             # half-width of the random parameter box


# ------------------------------------------------------------ polynomials
def pmul(a, b):
    if not a or not b:
        return {}
    o = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            e = (e1[0] + e2[0], e1[1] + e2[1], e1[2] + e2[2],
                 e1[3] + e2[3], e1[4] + e2[4])
            o[e] = o.get(e, 0) + c1 * c2
    return {e: c for e, c in o.items() if c}


def padd(a, b, sgn=1):
    o = dict(a)
    for e, c in b.items():
        o[e] = o.get(e, 0) + sgn * c
    return {e: c for e, c in o.items() if c}


def det4_dual(M0, M1):
    """(det M0,  d/d(eps) det(M0 + eps M1)) by Leibniz over dual numbers.

    No adjugate, no cofactor identity: the eps-part of a product of four dual
    entries is expanded term by term."""
    val, der = {}, {}
    for perm in itertools.permutations(range(4)):
        sgn = 1
        for i in range(4):
            for j in range(i + 1, 4):
                if perm[i] > perm[j]:
                    sgn = -sgn
        t = ONE
        ok = True
        for p in range(4):
            t = pmul(t, M0[p][perm[p]])
            if not t:
                ok = False
                break
        if ok:
            val = padd(val, t, sgn)
        for j in range(4):
            if not M1[j][perm[j]]:
                continue
            t = M1[j][perm[j]]
            for i in range(4):
                if i != j:
                    t = pmul(t, M0[i][perm[i]])
                    if not t:
                        break
            if t:
                der = padd(der, t, sgn)
    return val, der


def div_s1(poly, what):
    out = {}
    for e, c in poly.items():
        assert e[0] >= 1, "%s not divisible by s_1: monomial %s" % (what, e)
        out[(e[0] - 1,) + e[1:]] = c
    return out


def lin(mats):
    """5 integer 4x4 matrices A_1..A_5  ->  4x4 array of linear polys."""
    M = [[None] * 4 for _ in range(4)]
    for p in range(4):
        for q in range(4):
            d = {}
            for i in range(5):
                v = mats[i][p][q]
                if v:
                    e = [0] * R
                    e[i] = 1
                    d[tuple(e)] = d.get(tuple(e), 0) + v
            M[p][q] = d
    return M


# ------------------------------------------------------------------ ranks
def rank_Q(rows):
    """Exact rank over Q by Gaussian elimination in Fraction arithmetic.
    (A fraction-free Bareiss variant was written first and gave a wrong answer
    on the very first branch -- column skipping breaks the exact-division
    invariant.  Kept out; this one is checked against two primes on every
    branch.)"""
    A = [[Fraction(x) for x in r] for r in rows]
    rk = 0
    for col in range(NC):
        sel = next((i for i in range(rk, len(A)) if A[i][col]), None)
        if sel is None:
            continue
        A[rk], A[sel] = A[sel], A[rk]
        pv = A[rk][col]
        A[rk] = [x / pv for x in A[rk]]
        for i in range(len(A)):
            if i != rk and A[i][col]:
                f = A[i][col]
                A[i] = [A[i][c] - f * A[rk][c] for c in range(NC)]
        rk += 1
    return rk


def rank_mod(rows, p):
    A = [[x % p for x in r] for r in rows]
    rk = 0
    for col in range(NC):
        sel = next((i for i in range(rk, len(A)) if A[i][col]), None)
        if sel is None:
            continue
        A[rk], A[sel] = A[sel], A[rk]
        inv = pow(A[rk][col], p - 2, p)
        A[rk] = [(x * inv) % p for x in A[rk]]
        for i in range(len(A)):
            if i != rk and A[i][col]:
                f = A[i][col]
                A[i] = [(A[i][c] - f * A[rk][c]) % p for c in range(NC)]
        rk += 1
    return rk


def measure(mats, tangents, name, check_Q=True):
    """mats = [A_1..A_5]; tangents = list of 5-tuples of 4x4 int matrices."""
    M0 = lin(mats)
    rows = []
    val = None
    for T in tangents:
        M1 = lin(T)
        v, d = det4_dual(M0, M1)
        if val is None:
            val = v
            div_s1(val, "%s: det M" % name)          # branch really singular
        dG = div_s1(d, "%s: a derivative" % name)    # deformation stays in branch
        row = [0] * NC
        for e, c in dG.items():
            row[IDX[e]] += c
        rows.append(row)
    rq = rank_Q(rows) if check_Q else None
    rp = rank_mod(rows, PRIME)
    rp2 = rank_mod(rows, PRIME2)
    return rq, rp, rp2, len(rows)


# --------------------------------------------------------------- branches
def mask_branch(zero_rows, zero_cols, seed):
    """Integrator's parametrisation: A_1 free, A_2..A_5 free off the mask."""
    rnd = random.Random(seed)
    free = [[not (p in zero_rows and q in zero_cols) for q in range(4)]
            for p in range(4)]
    mats = [[[rnd.randint(-ENTRY_HI, ENTRY_HI) for _ in range(4)] for _ in range(4)]]
    for _ in range(4):
        mats.append([[rnd.randint(-ENTRY_HI, ENTRY_HI) if free[p][q] else 0 for q in range(4)]
                     for p in range(4)])
    tang = []
    for i in range(5):
        for p in range(4):
            for q in range(4):
                if i >= 1 and not free[p][q]:
                    continue
                T = [[[0] * 4 for _ in range(4)] for _ in range(5)]
                T[i][p][q] = 1
                tang.append(T)
    return mats, tang


def kernel_branch(k, seed, transpose=False, with_g=True):
    """The classification family.  im L = <f_1..f_k>, L normalised to
    [I_k | 0] on the y-coordinates.

    column j of A_{m+1}  =  phi[m][j]  (= -phi[j][m], zero unless m,j <= k)  j<=k
    column j of A_{m+1}  =  free vector                                       j>k
    A_1 free.

    IMPORTANT (a bug found and fixed here, recorded in docs/session_32.md):
    normalising L to [I_k | 0] uses up the GL_4 acting on the coordinates
    y = (s_2..s_5).  That GL_4 moves the CUBIC, so the normalised slice sees a
    smaller image than the stratum does.  For k = 4 the L is absorbed by a
    constant right multiplication of M_0 (which only rescales the determinant),
    so no y-change is needed; for k < 4 it is not, and the residual
    Grassmannian freedom -- k(4-k) parameters -- has to be restored.  We
    restore it by composing with a general substitution y -> g y, i.e.
    A_{m+1} = sum_n g_{nm} A^norm_{n+1}, and carrying g as a parameter.  The
    parametrisation is then bilinear, so the tangent directions include the
    d/dg ones."""
    rnd = random.Random(seed)
    R4 = lambda: [rnd.randint(-ENTRY_HI, ENTRY_HI) for _ in range(4)]
    Z4 = lambda: [[0] * 4 for _ in range(4)]

    pairs = [(i, j) for i in range(k) for j in range(i + 1, k)]
    phi = {pr: R4() for pr in pairs}
    colfree = {(j, m): R4() for j in range(k, 4) for m in range(4)}
    A1 = [[rnd.randint(-ENTRY_HI, ENTRY_HI) for _ in range(4)] for _ in range(4)]
    g = [[rnd.randint(-ENTRY_HI, ENTRY_HI) for _ in range(4)] for _ in range(4)]
    if not with_g:
        g = [[1 if a == b else 0 for b in range(4)] for a in range(4)]

    def norm_mats(phi_d, colfree_d):
        """A^norm_2 .. A^norm_5 from the normalised parameters."""
        def pv(m, j):
            if m == j:
                return [0] * 4
            if (m, j) in phi_d:
                return phi_d[(m, j)]
            if (j, m) in phi_d:
                return [-x for x in phi_d[(j, m)]]
            return [0] * 4
        out = []
        for m in range(4):
            A = Z4()
            for j in range(4):
                v = pv(m, j) if j < k else colfree_d[(j, m)]
                for p in range(4):
                    A[p][j] = v[p]
            out.append(A)
        return out

    def subst(nm, g_d):
        """A_{m+1} = sum_n g_{nm} A^norm_{n+1}."""
        out = []
        for m in range(4):
            A = Z4()
            for n in range(4):
                c = g_d[n][m]
                if c:
                    for p in range(4):
                        for q in range(4):
                            A[p][q] += c * nm[n][p][q]
            out.append(A)
        return out

    NM = norm_mats(phi, colfree)
    mats = [A1] + subst(NM, g)

    tang = []
    zphi = {pr: [0] * 4 for pr in pairs}
    zcol = {key: [0] * 4 for key in colfree}
    # d/d(phi) and d/d(colfree), at fixed g
    for pr in pairs:
        for p in range(4):
            d = {q: list(zphi[q]) for q in pairs}
            d[pr][p] = 1
            tang.append([Z4()] + subst(norm_mats(d, zcol), g))
    for key in colfree:
        for p in range(4):
            d = {q: list(zcol[q]) for q in zcol}
            d[key][p] = 1
            tang.append([Z4()] + subst(norm_mats(zphi, d), g))
    # d/d(g), at fixed normalised parameters
    if with_g:
        for n in range(4):
            for m in range(4):
                gd = [[0] * 4 for _ in range(4)]
                gd[n][m] = 1
                tang.append([Z4()] + subst(NM, gd))
    # d/d(A_1)
    for p in range(4):
        for q in range(4):
            T = [Z4() for _ in range(5)]
            T[0][p][q] = 1
            tang.append(T)

    if transpose:
        tr = lambda A: [[A[q][p] for q in range(4)] for p in range(4)]
        mats = [tr(A) for A in mats]
        tang = [[tr(A) for A in T] for T in tang]
    return mats, tang


def skew_pad_branch(seed):
    """The explicit pre-registered counterexample E_1 = {diag(N(x), w)},
    N(x) the 3x3 skew matrix with N(x)y = x cross y, with a general basis of
    S_0 and A_1 free.  A sub-branch of k = 3; measured on its own so the
    pre-registered example gets its own number."""
    rnd = random.Random(seed)
    # basis of E_1: N(e_1), N(e_2), N(e_3), diag(0,0,0,1)
    def emb(Nm):
        A = [[0] * 4 for _ in range(4)]
        for p in range(3):
            for q in range(3):
                A[p][q] = Nm[p][q]
        return A
    NX = [emb([[0, 0, 0], [0, 0, -1], [0, 1, 0]]),
          emb([[0, 0, 1], [0, 0, 0], [-1, 0, 0]]),
          emb([[0, -1, 0], [1, 0, 0], [0, 0, 0]])]
    W = [[0] * 4 for _ in range(4)]
    W[3][3] = 1
    BASIS = NX + [W]
    g = [[rnd.randint(-ENTRY_HI, ENTRY_HI) for _ in range(4)] for _ in range(4)]

    def assemble(g_d, A1_d):
        out = [A1_d]
        for m in range(4):
            A = [[0] * 4 for _ in range(4)]
            for b in range(4):
                c = g_d[b][m]
                if c:
                    for p in range(4):
                        for q in range(4):
                            A[p][q] += c * BASIS[b][p][q]
            out.append(A)
        return out

    A1 = [[rnd.randint(-ENTRY_HI, ENTRY_HI) for _ in range(4)] for _ in range(4)]
    mats = assemble(g, A1)
    Z4 = lambda: [[0] * 4 for _ in range(4)]
    tang = []
    for b in range(4):
        for m in range(4):
            gd = [[0] * 4 for _ in range(4)]
            gd[b][m] = 1
            T = assemble(gd, Z4())
            T[0] = Z4()
            tang.append(T)
    for p in range(4):
        for q in range(4):
            T = [Z4() for _ in range(5)]
            T[0][p][q] = 1
            tang.append(T)
    return mats, tang


# ------------------------------------------------------------------ driver
def report(label, maker, seeds=(11, 12, 13), check_Q=True):
    best = (0, 0, 0, 0)
    for s in seeds:
        mats, tang = maker(s)
        rq, rp, rp2, n = measure(mats, tang, label, check_Q)
        if (rp or 0) > best[1]:
            best = (rq, rp, rp2, n)
    rq, rp, rp2, n = best
    agree = (rp == rp2) and (rq is None or rq == rp)
    print("  %-46s  rank %2d  of 35   [params %3d, Q=%s p1=%d p2=%d %s]%s"
          % (label, rp, n, rq, rp, rp2, "agree" if agree else "DISAGREE",
             "   <-- DENSE: CONTAINMENT PROVED" if rp == 35 else ""))
    assert agree, "arithmetic routes disagree on " + label
    return rp


def certify(label, maker, seeds=(101, 202, 303)):
    """Upper-bound certification.  The Jacobian rank at a point is <= the
    generic rank, so a measured 31 only shows generic rank >= 31; the claim
    needs generic rank <= 31.  If the generic rank were >= 32 then some 32x32
    minor of the Jacobian would be a nonzero polynomial in the parameters, of
    degree <= 32 * 3 = 96 (each Jacobian entry is a cubic in the parameters).
    Drawing the parameters uniformly from a box of half-width H, Schwartz-Zippel
    bounds the chance of hitting a zero of it by 96 / (2H+1).  With
    H = 10^9 that is < 5e-8 per point, and the points are independent."""
    out = []
    for s in seeds:
        mats, tang = maker(s)
        M0 = lin(mats)
        rows = []
        first = True
        for T in tang:
            v, d = det4_dual(M0, lin(T))
            if first:
                div_s1(v, label)
                first = False
            dG = div_s1(d, label)
            row = [0] * NC
            for e, c in dG.items():
                row[IDX[e]] += c
            rows.append(row)
        out.append((rank_mod(rows, PRIME2), rank_mod(rows, PRIME3)))
    return out


if __name__ == '__main__':
    print("target 35 = dim Sym^3 C^5.  rank = dim{ cubics c : s_1.c is a 4x4")
    print("linear determinant realised through this branch }.\n")
    print("A. Re-verification of the integrator's four compression branches")
    print("   (own code, dual-number derivative, exact Q + two primes)")
    got = {}
    got['k1'] = report("compression k=1  common kernel (col 4 = 0)",
                       lambda s: mask_branch({0, 1, 2, 3}, {3}, s))
    got['k2'] = report("compression k=2  2->1 (rows 2-4 x cols 3-4)",
                       lambda s: mask_branch({1, 2, 3}, {2, 3}, s))
    got['k3'] = report("compression k=3  3->2 (rows 3-4 x cols 2-4)",
                       lambda s: mask_branch({2, 3}, {1, 2, 3}, s))
    got['k4'] = report("compression k=4  common cokernel (row 4 = 0)",
                       lambda s: mask_branch({3}, {0, 1, 2, 3}, s))
    print()
    print("B. The classification family  col_j M_0(y) = phi(y ^ f_j), j <= k")
    for k in (1, 2, 3, 4):
        got['L%d' % k] = report("rank L = %d  %s" % (k, {1: "(= common kernel)",
                                2: "(= 2->1 compression)", 3: "EXCEPTIONAL",
                                4: "EXCEPTIONAL"}[k]),
                                lambda s, k=k: kernel_branch(k, s))
    print()
    print("B'. The same strata with the y-normalisation NOT undone (diagnostic:")
    print("    the gap is the Grassmannian freedom k(4-k) = 0,4,3,0)")
    for k in (1, 2, 3, 4):
        report("rank L = %d, L-slice only" % k,
               lambda s, k=k: kernel_branch(k, s, with_g=False))
    print()
    print("C. Transposes of the exceptional strata (same cubics expected)")
    for k in (3, 4):
        got['L%dT' % k] = report("rank L = %d, transposed" % k,
                                 lambda s, k=k: kernel_branch(k, s, transpose=True))
    print()
    print("D. The pre-registered explicit counterexample E_1 = {diag(N(x), w)}")
    got['E1'] = report("skew-3 padded by a scalar (inside rank L = 3)",
                       skew_pad_branch)
    print()
    mx = max(got.values())
    print("MAXIMUM OVER ALL BRANCHES: %d of 35" % mx)
    print()
    print("E. Upper-bound certification: parameters drawn uniformly from a box")
    print("   of half-width 10^9, ranks modulo two large primes.  A generic")
    print("   rank >= 32 would need a nonzero 32x32 minor of degree <= 96;")
    print("   Schwartz-Zippel bounds a false low reading by 96/(2.10^9+1) per")
    print("   point, and there are three independent points per branch.")
    import wk8_s32_branches as _self
    _self.ENTRY_HI = 10 ** 9
    globals()['ENTRY_HI'] = 10 ** 9
    cert = {}
    cert['compression k=1'] = certify("cert k1", lambda s: mask_branch({0,1,2,3},{3},s))
    cert['compression k=2'] = certify("cert k2", lambda s: mask_branch({1,2,3},{2,3},s))
    cert['compression k=3'] = certify("cert k3", lambda s: mask_branch({2,3},{1,2,3},s))
    cert['compression k=4'] = certify("cert k4", lambda s: mask_branch({3},{0,1,2,3},s))
    for k in (1, 2, 3, 4):
        cert['rank L = %d' % k] = certify("cert L%d" % k,
                                          lambda s, k=k: kernel_branch(k, s))
    worst = 0
    for name, rs in sorted(cert.items()):
        flat = [x for pair in rs for x in pair]
        worst = max(worst, max(flat))
        print("   %-18s ranks at 3 wide points, 2 primes: %s"
              % (name, " ".join(str(x) for x in flat)))
    print()
    print("CERTIFIED MAXIMUM: %d of 35 -- containment %s"
          % (worst, "HOLDS (REVERSAL)" if worst == 35 else "FAILS"))
    print("containment %s" % ("HOLDS -- REVERSAL" if mx == 35 else
                              "FAILS: shortfall %d dimensions" % (35 - mx)))
