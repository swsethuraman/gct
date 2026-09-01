"""Session 32 -- the consistency checks the brief asks for (task D), and the
structural verifications of docs/singular_spaces.md.

  C1.  dim D_5^{det_3} = 29, computed here from scratch (dual-number Jacobian
       of  (A_1..A_5 in M_3) -> det_3(sum s_i A_i)  in Sym^3 C^5), matching the
       common-kernel branch rank.  Also r = 2..6 for the table.
  C2.  The common-kernel branch cubic IS a 3x3 determinant of linear forms --
       verified as an identity of polynomials, not just as an equality of
       dimensions.  This is the "built-in consistency check" of the brief,
       upgraded from a coincidence of numbers to an identity.
  C3.  The pre-registered example E_1 = {diag(N(x), w)}: its cubic reduces mod
       s_1 to (linear) x (quadratic of rank <= 3), as predicted in
       results/PREREG_s32.md §3, verified by exact factorisation.
  C4.  Bounded rank <= 2 cannot contribute: adj(M_0) == 0 forces s_1 | c.
  C5.  Task E: the stacking criterion.  dim D_r^{det_3} for r = 3..6.
"""
import itertools, random, sys, os
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk8_s32_branches import (pmul, padd, det4_dual, div_s1, lin, rank_Q,
                              rank_mod, PRIME, PRIME2, MON3, IDX, NC,
                              mask_branch, skew_pad_branch, kernel_branch)

ONE5 = {tuple([0] * 5): 1}


def pmul_r(a, b):
    """pmul for an arbitrary number of variables (wk8_s32_branches.pmul is
    unrolled for 5)."""
    if not a or not b:
        return {}
    o = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            e = tuple(x + y for x, y in zip(e1, e2))
            o[e] = o.get(e, 0) + c1 * c2
    return {e: c for e, c in o.items() if c}


# ------------------------------------------------------- C1 : dim D_r^{det_3}
def det3_dual(M0, M1, R):
    val, der = {}, {}
    one = {tuple([0] * R): 1}
    for perm in itertools.permutations(range(3)):
        sgn = 1
        for i in range(3):
            for j in range(i + 1, 3):
                if perm[i] > perm[j]:
                    sgn = -sgn
        t = one
        for p in range(3):
            t = pmul_r(t, M0[p][perm[p]])
        val = padd(val, t, sgn)
        for j in range(3):
            if not M1[j][perm[j]]:
                continue
            t = M1[j][perm[j]]
            for i in range(3):
                if i != j:
                    t = pmul_r(t, M0[i][perm[i]])
            if t:
                der = padd(der, t, sgn)
    return val, der


def dim_Ddet3(r, seed=5):
    """dim of {det_3(sum_{i=1}^r s_i A_i)} inside Sym^3 C^r."""
    rnd = random.Random(seed)
    mon = [e for e in itertools.product(range(4), repeat=r) if sum(e) == 3]
    idx = {e: k for k, e in enumerate(mon)}
    A = [[[rnd.randint(-9, 9) for _ in range(3)] for _ in range(3)]
         for _ in range(r)]
    M0 = [[None] * 3 for _ in range(3)]
    for p in range(3):
        for q in range(3):
            d = {}
            for i in range(r):
                v = A[i][p][q]
                if v:
                    e = [0] * r
                    e[i] = 1
                    d[tuple(e)] = v
            M0[p][q] = d
    rows = []
    for i in range(r):
        for p in range(3):
            for q in range(3):
                M1 = [[{} for _ in range(3)] for _ in range(3)]
                e = [0] * r
                e[i] = 1
                M1[p][q] = {tuple(e): 1}
                _, der = det3_dual(M0, M1, r)
                row = [0] * len(mon)
                for ee, c in der.items():
                    row[idx[ee]] += c
                rows.append(row)
    n = len(mon)
    # local rank routines (column count differs from NC)
    def rk_mod(rs, p):
        Am = [[x % p for x in q] for q in rs]
        rk = 0
        for col in range(n):
            sel = next((i for i in range(rk, len(Am)) if Am[i][col]), None)
            if sel is None:
                continue
            Am[rk], Am[sel] = Am[sel], Am[rk]
            inv = pow(Am[rk][col], p - 2, p)
            Am[rk] = [(x * inv) % p for x in Am[rk]]
            for i in range(len(Am)):
                if i != rk and Am[i][col]:
                    f = Am[i][col]
                    Am[i] = [(Am[i][c] - f * Am[rk][c]) % p for c in range(n)]
            rk += 1
        return rk
    a, b = rk_mod(rows, PRIME), rk_mod(rows, PRIME2)
    assert a == b, (r, a, b)
    return a


# --------------------------------- C2 : the common-kernel cubic is a 3x3 det
def check_common_kernel_identity(seed=7):
    """Build a common-kernel branch point, compute G = det(M)/s_1 directly,
    and independently write G as det_3 of an explicit 3x3 matrix of linear
    forms; assert the two polynomials are equal coefficient by coefficient."""
    rnd = random.Random(seed)
    A1 = [[rnd.randint(-9, 9) for _ in range(4)] for _ in range(4)]
    mats = [A1]
    for _ in range(4):
        mats.append([[rnd.randint(-9, 9) if q < 3 else 0 for q in range(4)]
                     for p in range(4)])
    M = lin(mats)
    val, _ = det4_dual(M, [[{} for _ in range(4)] for _ in range(4)])
    G = div_s1(val, "common kernel det")

    # column 3 of M is s_1 * v with v = column 3 of A_1
    v = [A1[p][3] for p in range(4)]
    for p in range(4):
        assert M[p][3] == ({(1, 0, 0, 0, 0): v[p]} if v[p] else {})
    # P invertible with P v = e_3 (exact rationals)
    assert any(v)
    j0 = next(p for p in range(4) if v[p])
    P = [[Fraction(1) if a == b else Fraction(0) for b in range(4)]
         for a in range(4)]
    # swap row j0 <-> 3, then scale, then clear
    P[j0], P[3] = P[3], P[j0]
    w = [v[j0] if p == 3 else (v[3] if p == j0 else v[p]) for p in range(4)]
    P[3] = [x / w[3] for x in P[3]]
    w3 = 1
    for p in range(3):
        if w[p]:
            P[p] = [P[p][b] - Fraction(w[p]) * P[3][b] for b in range(4)]
    chk = [sum(P[p][b] * v[b] for b in range(4)) for p in range(4)]
    assert chk == [0, 0, 0, 1], chk

    # top-left 3x3 of P.M restricted to columns 0,1,2
    def rowcomb(p):
        out = []
        for q in range(3):
            d = {}
            for b in range(4):
                c = P[p][b]
                if c:
                    for e, co in M[b][q].items():
                        d[e] = d.get(e, 0) + c * co
            out.append({e: co for e, co in d.items() if co})
        return out
    N = [rowcomb(p) for p in range(3)]
    # det_3 N, cleared of denominators
    val3, _ = det3_dual(N, [[{} for _ in range(3)] for _ in range(3)], 5)
    # det(P) * G  ==  det_3(N)  (expansion along the last column, P v = e_3)
    detP = _det4_frac(P)
    lhs = {e: detP * c for e, c in G.items()}
    rhs = {e: Fraction(c) for e, c in val3.items()}
    assert lhs == rhs, ("common-kernel identity FAILED",
                        sorted(set(lhs) ^ set(rhs))[:5])
    return True


def _det4_frac(P):
    acc = Fraction(0)
    for perm in itertools.permutations(range(4)):
        sgn = 1
        for i in range(4):
            for j in range(i + 1, 4):
                if perm[i] > perm[j]:
                    sgn = -sgn
        t = Fraction(sgn)
        for p in range(4):
            t *= P[p][perm[p]]
        acc += t
    return acc


# ---------------------------------------- C3 : E_1's leading part factorises
def check_E1_leading(seed=11):
    import sympy
    s = sympy.symbols('s1 s2 s3 s4 s5')
    mats, _ = skew_pad_branch(seed)
    M = lin(mats)
    val, _ = det4_dual(M, [[{} for _ in range(4)] for _ in range(4)])
    G = div_s1(val, "E_1 det")
    expr = 0
    for e, c in G.items():
        term = c
        for i in range(5):
            term *= s[i] ** e[i]
        expr += term
    lead = sympy.expand(expr.subs(s[0], 0))
    fl = sympy.factor_list(lead)
    degs = sorted(sympy.total_degree(f) for f, m in fl[1] for _ in range(m))
    return fl, degs


# ---------------------------------------------------- C4 : bounded rank <= 2
def check_rank2_forces_divisible(seed=3):
    """A 4-dim space of 4x4 matrices of generic rank <= 2: take M_0(y) with
    only two nonzero rows.  Then G = det(M)/s_1 must vanish on s_1 = 0."""
    rnd = random.Random(seed)
    mats = [[[rnd.randint(-9, 9) for _ in range(4)] for _ in range(4)]]
    for _ in range(4):
        mats.append([[rnd.randint(-9, 9) if p < 2 else 0 for q in range(4)]
                     for p in range(4)])
    M = lin(mats)
    val, _ = det4_dual(M, [[{} for _ in range(4)] for _ in range(4)])
    G = div_s1(val, "rank<=2 det")
    return all(e[0] >= 1 for e in G)


if __name__ == '__main__':
    print("C1  dim D_r^{det_3}, own dual-number Jacobian")
    tab = {r: dim_Ddet3(r) for r in (3, 4, 5, 6)}
    print("    r        :", "  ".join("%4d" % r for r in (3, 4, 5, 6)))
    print("    dim       :", "  ".join("%4d" % tab[r] for r in (3, 4, 5, 6)))
    print("    Sym^3 C^r :", "  ".join("%4d" % (len([e for e in
          itertools.product(range(4), repeat=r) if sum(e) == 3]))
          for r in (3, 4, 5, 6)))
    assert tab[4] == 20, tab
    assert tab[5] == 29, tab
    print("    [ok] dim D_4^{det_3} = 20 = all 4-ary cubics (session 27's fact)")
    print("    [ok] dim D_5^{det_3} = 29 = the common-kernel branch rank")
    print()
    print("C2  common-kernel branch cubic IS a 3x3 determinant (identity, not")
    print("    just equal dimensions)")
    for sd in (7, 8, 9):
        assert check_common_kernel_identity(sd)
    print("    [ok] verified at three independent points")
    print()
    print("C3  E_1 = {diag(N(x), w)}: leading part mod s_1 factorises")
    fl, degs = check_E1_leading()
    print("    factor degrees:", degs, " ->", "linear x quadratic"
          if degs == [1, 2] else "NOT as predicted")
    assert degs == [1, 2], degs
    print("    [ok] matches results/PREREG_s32.md §3 (P2's reasoning)")
    print()
    print("C4  bounded rank <= 2 forces s_1 | c, so cannot give a generic c")
    assert check_rank2_forces_divisible()
    print("    [ok] G vanishes identically on s_1 = 0")
    print()
    print("C5  task E, the stacking criterion: {ell.c} <= D_r^{det_n} by")
    print("    stacking iff every r-ary (n-1)-form is (n-1)x(n-1) determinantal")
    for r in (3, 4, 5, 6):
        n = len([e for e in itertools.product(range(4), repeat=r) if sum(e) == 3])
        print("    r = %d : dim D_r^{det_3} = %2d of %2d  -> stacking %s"
              % (r, tab[r], n, "works" if tab[r] == n else "FAILS (short %d)"
                 % (n - tab[r])))
