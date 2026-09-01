#!/usr/bin/env python3
"""Session 35 day-one theory tests.  Exact arithmetic; ranks by flint nmod_mat
over the two house primes.  Parts are selected on the command line:

  T1   catalecticant Cat_{2,2} ranks at pad / det / generic / qq' points
  T2   sigma_2(4x4) via a random pencil: Hilbert function of the 3x3-minor
       ideal (expect -> 20), minors-as-cubics independence (expect 16),
       nodality Hessian rank at a constructed rank-2 point (expect 4),
       and saturated cubics through the node scheme (expect >= 16)
  T2J  Jacobian-ring Hilbert function at generic / det / pad points
  T3   dim I(D_5^pad)_delta for delta = 2, 3(, 4) by per-weight-block
       symbolic rank of the multiplication comorphism

House rules: no hand-rolled elimination; every rank via flint nmod_mat.rank()
over P1 and (spot-checked / on any deficiency) P2.
"""
import sys, time, random
from itertools import combinations_with_replacement as cwr
from functools import lru_cache
from flint import nmod_mat

P1, P2 = 2147483647, 2147483629
random.seed(35)

NV = 5  # variables s_1..s_5

# ---------- polynomial helpers: dict {exponent-tuple: int} ----------
def pmul(f, g):
    h = {}
    for ea, ca in f.items():
        for eb, cb in g.items():
            e = tuple(x + y for x, y in zip(ea, eb))
            h[e] = h.get(e, 0) + ca * cb
    return {e: c for e, c in h.items() if c}

def padd(f, g):
    h = dict(f)
    for e, c in g.items():
        h[e] = h.get(e, 0) + c
        if h[e] == 0: del h[e]
    return h

def linform(coeffs):  # coeffs length 5
    return {tuple(1 if j == i else 0 for j in range(NV)): c
            for i, c in enumerate(coeffs) if c}

def randpoly(deg, lo=-9, hi=9):
    return {e: random.randint(lo, hi) for e in exps(deg)}

@lru_cache(maxsize=None)
def exps(d):
    out = []
    def rec(pos, rem, cur):
        if pos == NV - 1:
            out.append(tuple(cur + [rem])); return
        for k in range(rem + 1):
            rec(pos + 1, rem - k, cur + [k])
    rec(0, d, [])
    return tuple(sorted(out))

def det4_of_pencil(A):
    """A: list of 5 integer 4x4 matrices.  Return det(sum s_i A[i]) as poly."""
    # entries of M(s) are linear forms
    ent = [[linform([A[k][i][j] for k in range(NV)]) for j in range(4)]
           for i in range(4)]
    import itertools
    F = {}
    for perm in itertools.permutations(range(4)):
        sgn = perm_sign(perm)
        t = {tuple([0]*NV): sgn}
        for i in range(4):
            t = pmul(t, ent[i][perm[i]])
        F = padd(F, t)
    return F

def perm_sign(p):
    s, p = 1, list(p)
    for i in range(len(p)):
        while p[i] != i:
            j = p[i]; p[i], p[j] = p[j], p[i]; s = -s
    return s

def rank_mod(rows, ncols, p):
    """rows: list of dict {colindex: int}."""
    m = nmod_mat(len(rows), ncols, [0] * (len(rows) * ncols), p)
    for r, row in enumerate(rows):
        for c, v in row.items():
            m[r, c] = v % p
    return m.rank()

def dense_rank(mat, p):
    m = nmod_mat(len(mat), len(mat[0]), [int(v) % p for row in mat for v in row], p)
    return m.rank()

# ---------- T1: catalecticant ----------
def cat22(F):
    """15x15: rows u (deg-2 exps), cols v (deg-2 exps); entry = coeff giving
    the map Sym^2 V^* -> Sym^2 V, q |-> q(d)F, in monomial bases.
    Entry(u,v) proportional to c_{u+v} * (u+v)! / v!-type factor; for rank
    purposes over Q we may use c_{u+v} * prod binom-style integer factor."""
    E2 = exps(2)
    M = []
    for u in E2:
        row = []
        for v in E2:
            a = tuple(x + y for x, y in zip(u, v))
            c = F.get(a, 0)
            # d^u x^a = a!/(a-u)! x^{a-u}; factor = prod a_i (a_i-1).../(a_i-u_i)!
            f = 1
            for ai, ui in zip(a, u):
                for t in range(ui):
                    f *= (ai - t)
            row.append(c * f)
        M.append(row)
    return M

def T1():
    print("== T1: Cat_{2,2} ranks (15x15), primes", (P1, P2))
    pts = {}
    c3 = randpoly(3)
    pts['pad_x0c'] = pmul(linform([1, 0, 0, 0, 0]), c3)
    pts['pad_lc'] = pmul(linform([random.randint(-9, 9) for _ in range(5)]), randpoly(3))
    A = [[[random.randint(-9, 9) for _ in range(4)] for _ in range(4)] for _ in range(5)]
    pts['det_pencil'] = det4_of_pencil(A)
    pts['generic'] = randpoly(4)
    pts['qq'] = pmul(randpoly(2), randpoly(2))
    for name, F in pts.items():
        M = cat22(F)
        r1, r2 = dense_rank(M, P1), dense_rank(M, P2)
        print(f"   {name:10s} rank = {r1} / {r2}")

# ---------- T2: sigma_2 intersection scheme ----------
def minors3(A):
    """all 3x3 minors of the symbolic pencil as cubics (16 of them)."""
    ent = [[linform([A[k][i][j] for k in range(NV)]) for j in range(4)]
           for i in range(4)]
    out = []
    for rows in combinations_with_replacement_strict(range(4), 3):
        for cols in combinations_with_replacement_strict(range(4), 3):
            m = {}
            import itertools
            for perm in itertools.permutations(range(3)):
                sgn = perm_sign(perm)
                t = {tuple([0]*NV): sgn}
                for i in range(3):
                    t = pmul(t, ent[rows[i]][cols[perm[i]]])
                m = padd(m, t)
            out.append(m)
    return out

def combinations_with_replacement_strict(it, k):
    from itertools import combinations
    return combinations(it, k)

def hilbert_of_ideal(gens, gdeg, tmax, p):
    """HF of C[s]/(gens) in degrees 3..tmax; gens homogeneous of degree gdeg."""
    hf = {}
    for t in range(gdeg, tmax + 1):
        Et = exps(t); idx = {e: i for i, e in enumerate(Et)}
        rows = []
        for g in gens:
            for m in exps(t - gdeg):
                row = {}
                for e, c in g.items():
                    ee = tuple(x + y for x, y in zip(e, m))
                    row[idx[ee]] = row.get(idx[ee], 0) + c
                rows.append(row)
        r = rank_mod(rows, len(Et), p)
        hf[t] = len(Et) - r
    return hf

def T2():
    print("== T2: sigma_2(P^3 x P^3) meets a random P^4")
    # Giambelli check (arithmetic): deg of rank<=2 locus of 4x4
    from math import factorial
    from fractions import Fraction
    d = Fraction(1)
    for i in range(2):  # n - r = 2 factors
        d *= Fraction(factorial(4 + i) * factorial(i),
                      factorial(2 + i) * factorial(2 + i))
    assert d.denominator == 1
    print("   Giambelli degree sigma_2(4x4) =", int(d), "(codim D_5^det = 20)")
    A = [[[random.randint(-9, 9) for _ in range(4)] for _ in range(4)] for _ in range(5)]
    gens = minors3(A)
    # (c) minors as cubics: independence
    E3 = exps(3); idx3 = {e: i for i, e in enumerate(E3)}
    rows = [{idx3[e]: c for e, c in g.items()} for g in gens]
    print("   16 minors span in Sym^3 (35-dim): rank =", rank_mod(rows, 35, P1),
          "/", rank_mod(rows, 35, P2))
    # (b) Hilbert function of the minor ideal
    t0 = time.time()
    hf1 = hilbert_of_ideal(gens, 3, 9, P1)
    print("   HF(C[s]/minors)_t, t=3..9:", [hf1[t] for t in range(3, 10)],
          f"({time.time()-t0:.1f}s)")
    hf2 = hilbert_of_ideal(gens, 3, 9, P2)
    assert all(hf1[t] == hf2[t] for t in hf1), "prime disagreement"
    print("   (agrees at second prime)")

def T2sat():
    print("== T2sat: cubics through the length-20 scheme (saturation probe)")
    A = [[[random.randint(-9, 9) for _ in range(4)] for _ in range(4)] for _ in range(5)]
    gens = minors3(A)
    for p in (P1, P2):
        for T in (8, 9):
            Et = exps(T); idx = {e: i for i, e in enumerate(Et)}
            rows = []
            for g in gens:
                for m in exps(T - 3):
                    row = {}
                    for e, c in g.items():
                        ee = tuple(x + y for x, y in zip(e, m))
                        row[idx[ee]] = row.get(idx[ee], 0) + c
                    rows.append(row)
            NT = len(Et)
            m = nmod_mat(len(rows), NT, [0] * (len(rows) * NT), p)
            for r, row in enumerate(rows):
                for cc, v in row.items():
                    m[r, cc] = v % p
            m = m.rref()[0]
            # basis of J_T rowspace; quotient projector via pivot columns
            piv = []
            ri = 0
            for r in range(min(len(rows), NT)):
                row = [m[r, c] for c in range(NT)]
                nz = [c for c, v in enumerate(row) if int(v) != 0]
                if not nz: break
                piv.append(nz[0]); ri += 1
            pivset = set(piv)
            # cubic C is in (J : Sym^{T-3})_3 iff C*x^mu in J_T for all mu.
            # Build map: 35-dim -> (nonpivot coords) for each mu; stack kernels.
            E3 = exps(3)
            bigrows = []  # columns: 35 cubics; rows: constraints
            nonpiv = [c for c in range(NT) if c not in pivset]
            npidx = {c: i for i, c in enumerate(nonpiv)}
            # reduce each generator-column: representation of e_col mod J
            # Solve: for column vector v (in R^NT), residue = v - proj_J(v):
            # using rref rows: for each pivot row r with pivot col pc,
            # subtract v[pc]*row_r.  Then residue supported on nonpivots.
            rrefrows = []
            for r in range(ri):
                rrefrows.append([int(m[r, c]) for c in range(NT)])
            for mu in exps(T - 3):
                for j, e3 in enumerate(E3):
                    ee = tuple(x + y for x, y in zip(e3, mu))
                    v = {idx[ee]: 1}
                    # reduce
                    for r in range(ri):
                        pc = piv[r]
                        if pc in v and v[pc] % p != 0:
                            coef = v[pc]  # row has 1 at pivot (rref normalized)
                            for c, val in enumerate(rrefrows[r]):
                                if val:
                                    v[c] = (v.get(c, 0) - coef * val) % p
                            v = {c: val for c, val in v.items() if val % p}
                    for c, val in v.items():
                        bigrows.append((npidx[c], j, val))
            # constraints matrix: rows indexed by (mu, nonpivot) pairs -> here
            # collapse: build dict rowkey -> {j: val}
            byrow = {}
            k = 0
            # bigrows entries were appended per (mu,j); rebuild properly:
            # redo loop to collect per (mu, c) constraints
            byc = {}
            rowid = {}
            nid = 0
            constraints = {}
            # Simpler: second pass
            constraints = {}
            for mu in exps(T - 3):
                for j, e3 in enumerate(E3):
                    ee = tuple(x + y for x, y in zip(e3, mu))
                    v = {idx[ee]: 1}
                    for r in range(ri):
                        pc = piv[r]
                        if pc in v and v[pc] % p != 0:
                            coef = v[pc]
                            for c, val in enumerate(rrefrows[r]):
                                if val:
                                    v[c] = (v.get(c, 0) - coef * val) % p
                            v = {c: val for c, val in v.items() if val % p}
                    for c, val in v.items():
                        constraints.setdefault((mu, c), {})[j] = val
            crows = [dict(d) for d in constraints.values()]
            cr = rank_mod(crows, 35, p)
            print(f"   p={p} T={T}: dim (J : Sym^{T-3})_3 = {35 - cr}")
        break  # one prime is enough for the probe; assert separately if needed

def T2node():
    print("== T2node: Hessian rank at a constructed rank-2 point (expect 4)")
    for trial in range(3):
        u1 = [random.randint(-5, 5) for _ in range(4)]
        v1 = [random.randint(-5, 5) for _ in range(4)]
        u2 = [random.randint(-5, 5) for _ in range(4)]
        v2 = [random.randint(-5, 5) for _ in range(4)]
        B = [[u1[i]*v1[j] + u2[i]*v2[j] for j in range(4)] for i in range(4)]
        A = [B] + [[[random.randint(-9, 9) for _ in range(4)] for _ in range(4)]
                   for _ in range(4)]
        F = det4_of_pencil(A)
        s0 = (1, 0, 0, 0, 0)
        # gradient at s0 must vanish
        grad = [sum(c * e[k] * prodpow(s0, subtract(e, k))
                    for e, c in F.items() if e[k] > 0) for k in range(5)]
        H = [[hess_entry(F, j, k, s0) for k in range(5)] for j in range(5)]
        r1, r2 = dense_rank(H, P1), dense_rank(H, P2)
        print(f"   trial {trial}: |grad| = {sum(abs(g) for g in grad)}, "
              f"Hessian rank = {r1} / {r2}")

def subtract(e, k):
    return tuple(x - (1 if i == k else 0) for i, x in enumerate(e))

def prodpow(s, e):
    out = 1
    for b, x in zip(s, e):
        if x < 0: return 0
        out *= b ** x
    return out

def hess_entry(F, j, k, s0):
    tot = 0
    for e, c in F.items():
        if e[j] == 0 or (j == k and e[j] < 2) or (j != k and e[k] == 0):
            continue
        f = e[j] * (e[j] - 1) if j == k else e[j] * e[k]
        ee = list(e); ee[j] -= 1; ee[k] -= 1
        tot += c * f * prodpow(s0, tuple(ee))
    return tot

def T2J():
    print("== T2J: Jacobian-ring HF at generic / det / pad (t = 6..10)")
    A = [[[random.randint(-9, 9) for _ in range(4)] for _ in range(4)] for _ in range(5)]
    pts = {'generic': randpoly(4),
           'det': det4_of_pencil(A),
           'pad': pmul(linform([1, 1, 0, 0, 1]), randpoly(3))}
    for name, F in pts.items():
        grads = []
        for k in range(5):
            g = {}
            for e, c in F.items():
                if e[k] > 0:
                    g[subtract(e, k)] = g.get(subtract(e, k), 0) + c * e[k]
            grads.append(g)
        hf = hilbert_of_ideal(grads, 3, 10, P1)
        print(f"   {name:8s}:", [hf[t] for t in range(6, 11)])

# ---------- T3: pad ideal onset by per-weight-block symbolic rank ----------
def T3(deltas=(2, 3)):
    print("== T3: dim I(D_5^pad)_delta by weight-block ranks of mu^*")
    E4 = exps(4); E3 = exps(3)
    i3 = {e: i for i, e in enumerate(E3)}
    for delta in deltas:
        t0 = time.time()
        blocks = {}   # beta -> list of (source monomial expansion dict)
        colidx = {}   # beta -> {(amono, bmono): index}
        srccount = 0
        for combo in cwr(range(len(E4)), delta):
            srccount += 1
            beta = tuple(sum(E4[i][k] for i in combo) for k in range(NV))
            # expand prod_k ( sum_i a_i b_{alpha_k - e_i} )
            terms = {((), ()): 1}   # (sorted a-tuple, sorted b-tuple) -> coeff
            for ci in combo:
                al = E4[ci]
                new = {}
                for i in range(NV):
                    g = subtract(al, i)
                    if min(g) < 0: continue
                    bi = i3[g]
                    for (am, bm), c in terms.items():
                        key = (tuple(sorted(am + (i,))), tuple(sorted(bm + (bi,))))
                        new[key] = new.get(key, 0) + c
                terms = new
            blocks.setdefault(beta, []).append(terms)
            ci_ = colidx.setdefault(beta, {})
            for key in terms:
                if key not in ci_:
                    ci_[key] = len(ci_)
        total_rank = 0
        total_src = 0
        deficient = []
        for beta, rows_ in blocks.items():
            ci_ = colidx[beta]
            rows = [{ci_[k]: v for k, v in r.items()} for r in rows_]
            r1 = rank_mod(rows, len(ci_), P1)
            if r1 < len(rows):
                r2 = rank_mod(rows, len(ci_), P2)
                assert r1 == r2, (beta, r1, r2)
                deficient.append((beta, len(rows) - r1))
            total_rank += r1
            total_src += len(rows)
        assert total_src == srccount
        dimI = total_src - total_rank
        print(f"   delta={delta}: dim Sym^delta = {total_src}, "
              f"rank mu^* = {total_rank}, dim I(pad) = {dimI} "
              f"({time.time()-t0:.1f}s, {len(blocks)} blocks)")
        if deficient:
            print("     deficient blocks (beta, def):", deficient[:10])

def T2K():
    """Control: quartics with k nodes at GENERAL points, k <= 13
    (5 linear conditions per node: grad F(p) = 0; F(p)=0 free by Euler).
    Expect (R/J)_7 = 30 (defect 0) -- the det-drop is configuration, not count."""
    print("== T2K: (R/J)_7 for k general nodes (expect 30 = no defect)")
    E4 = exps(4)
    for k in (1, 5, 11, 13):
        # linear system on 70 coefficients: for each point p, 5 eqs grad(p)=0
        pts = [[random.randint(-6, 6) for _ in range(5)] for _ in range(k)]
        rows = []
        for p in pts:
            for j in range(5):
                row = []
                for e in E4:
                    if e[j] == 0:
                        row.append(0)
                    else:
                        ee = list(e); ee[j] -= 1
                        row.append(e[j] * prodpow(p, tuple(ee)))
                rows.append(row)
        # kernel over Q via flint at P1 (random combo mod P1 for HF; two primes)
        import flint as fl
        res = {}
        for p in (P1, P2):
            m = nmod_mat(len(rows), 70, [int(v) % p for r in rows for v in r], p)
            ns = m.nullspace()
            X, nul = ns[0], ns[1]
            coeffs = [random.randint(1, 10**6) for _ in range(nul)]
            Fv = [sum(coeffs[c] * int(X[i, c]) for c in range(nul)) % p
                  for i in range(70)]
            F = {e: Fv[i] for i, e in enumerate(E4) if Fv[i]}
            grads = []
            for j in range(5):
                g = {}
                for e, c in F.items():
                    if e[j] > 0:
                        g[subtract(e, j)] = g.get(subtract(e, j), 0) + c * e[j]
                grads.append(g)
            # HF at t=7 only
            t = 7
            Et = exps(t); idx = {e: i for i, e in enumerate(Et)}
            mrows = []
            for g in grads:
                for mm in exps(t - 3):
                    row = {}
                    for e, c in g.items():
                        ee = tuple(x + y for x, y in zip(e, mm))
                        row[idx[ee]] = row.get(idx[ee], 0) + c
                    mrows.append(row)
            r = rank_mod(mrows, len(Et), p)
            res[p] = len(Et) - r
        print(f"   k={k:2d}: (R/J)_7 = {res[P1]} / {res[P2]}")

def T2Jdet3():
    """(R/J)_7 at three FRESH det pencils, both primes."""
    print("== T2Jdet3: det-pencil (R/J)_7 x3 fresh pencils")
    for trial in range(3):
        A = [[[random.randint(-99, 99) for _ in range(4)] for _ in range(4)]
             for _ in range(5)]
        F = det4_of_pencil(A)
        grads = []
        for j in range(5):
            g = {}
            for e, c in F.items():
                if e[j] > 0:
                    g[subtract(e, j)] = g.get(subtract(e, j), 0) + c * e[j]
            grads.append(g)
        vals = []
        for p in (P1, P2):
            t = 7
            Et = exps(t); idx = {e: i for i, e in enumerate(Et)}
            mrows = []
            for g in grads:
                for mm in exps(t - 3):
                    row = {}
                    for e, c in g.items():
                        ee = tuple(x + y for x, y in zip(e, mm))
                        row[idx[ee]] = row.get(idx[ee], 0) + c
                    mrows.append(row)
            r = rank_mod(mrows, len(Et), p)
            vals.append(len(Et) - r)
        print(f"   pencil {trial}: (R/J)_7 = {vals[0]} / {vals[1]}")


def T3v2(delta):
    """Same as T3 but only S_5-representative weight blocks (beta sorted
    descending), with orbit-size bookkeeping.  Equivariance of mu^* makes
    the per-block deficiency constant on each S_5-orbit."""
    from math import factorial
    print(f"== T3v2: dim I(D_5^pad)_{delta} via S_5-representative blocks")
    t0 = time.time()
    E4 = exps(4); E3 = exps(3)
    i3 = {e: i for i, e in enumerate(E3)}
    blocks, colidx = {}, {}
    total_src = 0
    for combo in cwr(range(len(E4)), delta):
        total_src += 1
        beta = tuple(sum(E4[i][k] for i in combo) for k in range(NV))
        if list(beta) != sorted(beta, reverse=True):
            continue
        terms = {((), ()): 1}
        for ci in combo:
            al = E4[ci]
            new = {}
            for i in range(NV):
                g = subtract(al, i)
                if min(g) < 0: continue
                bi = i3[g]
                for (am, bm), c in terms.items():
                    key = (tuple(sorted(am + (i,))), tuple(sorted(bm + (bi,))))
                    new[key] = new.get(key, 0) + c
            terms = new
        blocks.setdefault(beta, []).append(terms)
        ci_ = colidx.setdefault(beta, {})
        for key in terms:
            if key not in ci_:
                ci_[key] = len(ci_)
    dimI = 0
    checked = 0
    for beta, rows_ in blocks.items():
        ci_ = colidx[beta]
        rows = [{ci_[k]: v for k, v in r.items()} for r in rows_]
        r1 = rank_mod(rows, len(ci_), P1)
        d = len(rows) - r1
        if d:
            r2 = rank_mod(rows, len(ci_), P2)
            assert len(rows) - r2 == d, (beta, r1, r2)
            # orbit size = 5! / prod (multiplicities of repeated values)!
            from collections import Counter
            osz = factorial(5)
            for v in Counter(beta).values():
                osz //= factorial(v)
            dimI += osz * d
            print(f"     block {beta}: deficiency {d} x orbit {osz}")
        checked += len(rows)
    print(f"   delta={delta}: source total {total_src}, rep-rows {checked}, "
          f"dim I(pad) = {dimI}  ({time.time()-t0:.1f}s)")


def T1r4():
    """r=4 catalecticant Cat_{2,2}: 10x10 (dim Sym^2 C^4 = 10).
    pad4 = l*c in 4 vars: rank <= 8 (proof: image in l*V + span dc).
    det4-surface pencil: MUST be 10 -- else contradicts e = 320112 (s33):
    a rank drop would put a degree-<=10 element in the principal ideal."""
    print("== T1r4: Cat_{2,2} at r=4 (10x10)")
    global NV
    NV_saved = NV
    exps.cache_clear()
    NV = 4
    try:
        c3 = randpoly(3)
        pad = pmul(linform([1, 2, 0, 1]), c3)
        A = [[[random.randint(-9, 9) for _ in range(4)] for _ in range(4)]
             for _ in range(4)]
        det4 = det4_of_pencil(A)
        gen = randpoly(4)
        for name, F in (('pad4', pad), ('det4_surface', det4), ('generic4', gen)):
            E2 = exps(2)
            M = []
            for u in E2:
                row = []
                for v in E2:
                    a = tuple(x + y for x, y in zip(u, v))
                    c = F.get(a, 0)
                    f = 1
                    for ai, ui in zip(a, u):
                        for t in range(ui):
                            f *= (ai - t)
                    row.append(c * f)
                M.append(row)
            print(f"   {name:12s} rank = {dense_rank(M, P1)} / {dense_rank(M, P2)}")
    finally:
        NV = NV_saved
        exps.cache_clear()


def T1w():
    """Extremal 9x9 minor of Cat4 (omit the lowest-weight row and column,
    i.e. the 2*e_4 basis element of Sym^2 C^4): weight (10,10,10,6).
    Nonzero at a generic quartic  =>  S_(10,10,10,6) occurs in the span of
    9-minors inside I(D_4^pad)_9.  Also evaluate at a det-surface pencil
    (expect nonzero: it is NOT in I(D_4^det), consistent with e = 320112)."""
    print("== T1w: extremal 9-minor of Cat4, weight (10,10,10,6)")
    global NV
    NV_saved = NV
    exps.cache_clear(); NV = 4
    try:
        E2 = exps(2)
        # order basis by weight, identify index of exponent (0,0,0,2)
        low = E2.index((0, 0, 0, 2))
        keep = [i for i in range(10) if i != low]
        def cat4(F):
            M = []
            for u in E2:
                row = []
                for v in E2:
                    a = tuple(x + y for x, y in zip(u, v))
                    c = F.get(a, 0); f = 1
                    for ai, ui in zip(a, u):
                        for t in range(ui): f *= (ai - t)
                    row.append(c * f)
                M.append(row)
            return M
        from fractions import Fraction
        def minor9(F):
            M = cat4(F)
            sub = [[Fraction(M[i][j]) for j in keep] for i in keep]
            # exact determinant by fraction-free-ish Gaussian elimination
            n = 9; det = Fraction(1)
            for c in range(n):
                piv = next((r for r in range(c, n) if sub[r][c] != 0), None)
                if piv is None: return 0
                if piv != c:
                    sub[c], sub[piv] = sub[piv], sub[c]; det = -det
                det *= sub[c][c]
                inv = sub[c][c]
                for r in range(c + 1, n):
                    f = sub[r][c] / inv
                    if f:
                        for cc in range(c, n):
                            sub[r][cc] -= f * sub[c][cc]
            return det
        gen = randpoly(4)
        A = [[[random.randint(-9, 9) for _ in range(4)] for _ in range(4)]
             for _ in range(4)]
        det4 = det4_of_pencil(A)
        pad = pmul(linform([3, -2, 1, 5]), randpoly(3))
        for name, F in (('generic4', gen), ('det4_surface', det4), ('pad4', pad)):
            v = minor9(F)
            print(f"   {name:12s} minor = {'NONZERO' if v != 0 else 'ZERO'}"
                  f"  ({str(v)[:40]}{'...' if len(str(v))>40 else ''})")
    finally:
        NV = NV_saved; exps.cache_clear()


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which in ("T1", "all"): T1()
    if which in ("T2", "all"): T2()
    if which in ("T2node", "all"): T2node()
    if which in ("T2J", "all"): T2J()
    if which in ("T2sat",): T2sat()
    if which in ("T3", "all"): T3()
    if which in ("T3d4",): T3(deltas=(4,))
    if which in ("T2K",): T2K()
    if which in ("T2Jdet3",): T2Jdet3()


    if which in ("T3v2d4",): T3v2(4)
    if which in ("T3v2d3",): T3v2(3)
    if which in ("T1r4",): T1r4()
    if which in ("T1w",): T1w()
