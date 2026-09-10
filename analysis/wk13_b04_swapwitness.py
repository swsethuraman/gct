#!/usr/bin/env python3
"""B13-04, addendum 1 -- certify the swap-identity counterexample.

The descent sweep found one cell, r = 3, delta = 7, lam = (16,6,6), where the
swap-identity subspace T is strictly larger than rho(H_lam):

    a^(4) = 7,  mult_R = rank rho = 7,  dim B_full = 15,  dim T = 8.

Sampling can only UNDER-constrain a kernel, so a computed dim T equal to mult_R
certifies T = rho(H_lam) at that cell; a computed dim T larger than mult_R does
not by itself certify the excess.  This script closes that gap:

  * it recomputes T at the cell exactly over Q from a saturated point set;
  * it produces an explicit integer vector F in T with F not in rho(H_lam)
    (an exact rank statement over Q -- certified);
  * it verifies BOTH the swap identity and the general two-factor fibre
    condition for that F **symbolically**: the difference
    F(l.q) - F(u_l^{-1}(x_1.q)) is expanded as a polynomial in the r-1 free
    coordinates of l and the C(r+1,2) coefficients of q over Z, and shown to be
    the zero polynomial.  That is a proof, not a sample.

Writes results/b13_04/swap_witness_r3_d7.json.
"""
import sys, os, json, random, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from wk13_b04_model import (exps, weight_monomials, hwv_space, rho, rank_Q, normalise, combine,
                            poly_mul, linear_form, x1_times, substitute_x1, eval_poly, add_to,
                            P1, P2)
from wk13_b04_descent import swap_row, kernel_rows, rank_mod
from flint import fmpz_mpoly_ctx

ROOT = os.path.abspath(os.path.join(HERE, '..'))

LAM = (16, 6, 6)
DELTA = 7
R = 3
EXTRA = 300          # points beyond saturation, as a cheap independent check


def symbolic_swap_zero(F, r, delta):
    """expand F(l.q) - F(u_l^{-1}(x_1.q)) over Z in the variables
    l_2..l_r (l_1 = 1) and the coefficients of a general quadric q.
    Returns (is_zero, n_terms_of_each_side)."""
    quad = list(exps(2, r))
    names = [f"l{j}" for j in range(1, r)] + [f"q{''.join(map(str, a))}" for a in quad]
    ctx = fmpz_mpoly_ctx.get(tuple(names), 'lex')
    g = ctx.gens()
    L = {0: ctx.from_dict({tuple([0] * len(names)): 1})}      # l_1 = 1
    for j in range(1, r):
        L[j] = g[j - 1]
    Q = {a: g[(r - 1) + k] for k, a in enumerate(quad)}
    zero = ctx.from_dict({})

    def mpoly_mul(f1, f2):
        out = {}
        for a, ca in f1.items():
            for b, cb in f2.items():
                k = tuple(x + y for x, y in zip(a, b))
                out[k] = out.get(k, zero) + ca * cb
        return {k: v for k, v in out.items() if not v.is_zero()}

    # the cubic l . q, coefficients in ctx
    lin = {tuple(1 if k == j else 0 for k in range(r)): L[j] for j in range(r)}
    quadp = {a: Q[a] for a in quad}
    c_lq = mpoly_mul(lin, quadp)

    # the cubic u_l^{-1}(x_1 . q):  x_1 -> x_1 - sum_{j>=2} l_j x_j  applied to x_1*q
    x1q = mpoly_mul({tuple(1 if k == 0 else 0 for k in range(r)): L[0]}, quadp)
    shear = {tuple(1 if k == 0 else 0 for k in range(r)): ctx.from_dict({tuple([0] * len(names)): 1})}
    for j in range(1, r):
        shear[tuple(1 if k == j else 0 for k in range(r))] = -L[j]
    c_sub = {}
    for al, cf in x1q.items():
        term = {tuple([0] * r): cf}
        for _ in range(al[0]):
            term = mpoly_mul(term, shear)
        rest = (0,) + al[1:]
        term = mpoly_mul(term, {rest: ctx.from_dict({tuple([0] * len(names)): 1})})
        for k, v in term.items():
            c_sub[k] = c_sub.get(k, zero) + v
    c_sub = {k: v for k, v in c_sub.items() if not v.is_zero()}

    def evaluate(coeffs):
        tot = zero
        for mono, cf in F.items():
            v = ctx.from_dict({tuple([0] * len(names)): cf})
            ok = True
            for al in mono:
                cc = coeffs.get(al)
                if cc is None:
                    ok = False
                    break
                v = v * cc
            if ok:
                tot = tot + v
        return tot

    lhs = evaluate(c_lq)
    rhs = evaluate(c_sub)
    d = lhs - rhs
    return d.is_zero(), (len(lhs.monoms()), len(rhs.monoms()))


def symbolic_fibre_zero(F, r, delta):
    """expand  F(u_l^{-1}(l'.q)) - F(u_{l'}^{-1}(l.q))  over Z in l_2..l_r,
    l'_2..l'_r (both first coordinates 1) and the coefficients of a general
    quadric q.  Zero means the witness satisfies the GENERAL two-factor fibre
    condition identically, not merely at sampled points."""
    quad = list(exps(2, r))
    names = ([f"l{j}" for j in range(1, r)] + [f"m{j}" for j in range(1, r)] +
             [f"q{''.join(map(str, a))}" for a in quad])
    ctx = fmpz_mpoly_ctx.get(tuple(names), 'lex')
    g = ctx.gens()
    one = ctx.from_dict({tuple([0] * len(names)): 1})
    zero = ctx.from_dict({})
    L = {0: one}
    M = {0: one}
    for j in range(1, r):
        L[j] = g[j - 1]
        M[j] = g[(r - 1) + j - 1]
    Q = {a: g[2 * (r - 1) + k] for k, a in enumerate(quad)}

    def mul(f1, f2):
        out = {}
        for a, ca in f1.items():
            for b, cb in f2.items():
                k = tuple(x + y for x, y in zip(a, b))
                out[k] = out.get(k, zero) + ca * cb
        return {k: v for k, v in out.items() if not v.is_zero()}

    def lin_of(D):
        return {tuple(1 if k == j else 0 for k in range(r)): D[j] for j in range(r)}

    def shear_by(D):
        """substitution x_1 -> x_1 - sum_{j>=2} D_j x_j (first coordinate 1)."""
        sh = {tuple(1 if k == 0 else 0 for k in range(r)): one}
        for j in range(1, r):
            sh[tuple(1 if k == j else 0 for k in range(r))] = -D[j]
        return sh

    def apply_shear(cub, D):
        sh = shear_by(D)
        out = {}
        for al, cf in cub.items():
            term = {tuple([0] * r): cf}
            for _ in range(al[0]):
                term = mul(term, sh)
            rest = (0,) + al[1:]
            term = mul(term, {rest: one})
            for k, v in term.items():
                out[k] = out.get(k, zero) + v
        return {k: v for k, v in out.items() if not v.is_zero()}

    A = apply_shear(mul(lin_of(M), dict(Q)), L)      # u_l^{-1}(l' . q)
    B = apply_shear(mul(lin_of(L), dict(Q)), M)      # u_{l'}^{-1}(l . q)

    def evaluate(coeffs):
        tot = zero
        for mono, cf in F.items():
            v = ctx.from_dict({tuple([0] * len(names)): cf})
            ok = True
            for al in mono:
                cc = coeffs.get(al)
                if cc is None:
                    ok = False
                    break
                v = v * cc
            if ok:
                tot = tot + v
        return tot

    lhs, rhs = evaluate(A), evaluate(B)
    d = lhs - rhs
    return d.is_zero(), (len(lhs.monoms()), len(rhs.monoms()))


def main():
    t0 = time.time()
    rnd = random.Random(4242)
    basis4, H = hwv_space(4, R, DELTA, LAM)
    a4 = len(H)
    lam_minus = (LAM[0] - DELTA,) + LAM[1:]
    cols = weight_monomials(3, R, DELTA, lam_minus)
    RH = [rho(h, R) for h in H]
    mR = rank_Q(RH, cols)
    _, Bfull = hwv_space(3, R, DELTA, lam_minus, first=1)
    nB = len(Bfull)
    print(f"lam={LAM} delta={DELTA} r={R}: a4={a4} mult_R={mR} lam^-={lam_minus} "
          f"N_S(lam^-)={len(cols)} dim B_full={nB}")
    rows, dim, stable = [], nB, 0
    while stable < EXTRA:
        l = [1] + [rnd.randint(-9, 9) for _ in range(R - 1)]
        q = {al: rnd.randint(-9, 9) for al in exps(2, R)}
        rows.append(swap_row(Bfull, cols, l, q, R))
        K = kernel_rows(rows, nB)
        if len(K) == dim:
            stable += 1
        else:
            dim, stable = len(K), 0
    T = [normalise(combine(Bfull, k)) for k in kernel_rows(rows, nB)]
    print(f"dim T = {len(T)} after {len(rows)} points (fresh seed 4242, bound 9, "
          f"{EXTRA} stable), mod p: {[nB - rank_mod(rows, nB, p) for p in (P1, P2)]}")
    wit = None
    for v in T:
        if rank_Q(RH + [v], cols) > mR:
            wit = v
            break
    assert wit is not None, "no excess vector: the sweep's reading does not reproduce"
    indep = rank_Q(RH + [wit], cols) - mR
    print(f"witness: {len(wit)} monomials, rank(rho(H) + F) - mult_R = {indep} "
          f"(exact over Q: F is NOT a rho(h))")
    ok, sizes = symbolic_swap_zero(wit, R, DELTA)
    print(f"symbolic swap identity for the witness: difference is zero = {ok} "
          f"(sides had {sizes[0]} and {sizes[1]} monomials)")
    okf, sizesf = symbolic_fibre_zero(wit, R, DELTA)
    print(f"symbolic GENERAL two-factor fibre condition for the witness: difference is "
          f"zero = {okf} (sides had {sizesf[0]} and {sizesf[1]} monomials)")
    out = dict(board_numbering='batch13', session='B13-04', addendum=1, values_are='none',
               lam=list(LAM), delta=DELTA, r=R, a4=a4, mult_R=mR, dim_B_full=nB, dim_T=len(T),
               swap_points_used=len(rows), seed=4242, bound=9, stable_required=EXTRA,
               witness_terms=len(wit), witness_independent_of_rho_H=bool(indep == 1),
               witness_symbolic_swap_zero=bool(ok), swap_sides_monomials=list(sizes),
               witness_symbolic_fibre_zero=bool(okf), fibre_sides_monomials=list(sizesf),
               witness=[[list(map(list, m)), c] for m, c in sorted(wit.items())],
               seconds=round(time.time() - t0, 1))
    os.makedirs(os.path.join(ROOT, 'results', 'b13_04'), exist_ok=True)
    fn = os.path.join(ROOT, 'results', 'b13_04', 'swap_witness_r3_d7.json')
    with open(fn, 'w') as fh:
        json.dump(out, fh, indent=1)
    print(f"wrote {fn} ({out['seconds']}s)")


if __name__ == '__main__':
    main()
