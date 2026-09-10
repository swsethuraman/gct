#!/usr/bin/env python3
"""B13-04 -- exploratory control (not pre-registered): Lemma B(4) exercised on a
house cell with a reducible deficiency.

Cell (8,8,8), delta = 6, r = 3 (S4's calibration control: a = 2, reducible /
padded 1, explicit kernel (1,0); results/s64_calibration_unified.jsonl and
results/s64_calibration_r34.jsonl).  Here:

  * the two HWVs over Q (integer kernel of the raising operators, 561 monomials);
  * rank of the fixed-factor restriction rho over Q  ->  mult_R exactly;
  * the kernel vector of rho: an explicit HWV every monomial of which contains a
    letter not divisible by x_1 -- by Lemma B(4) a CERTIFIED element of I(R)_6;
  * independent confirmation: h(l . c) expanded symbolically in the 3 + 10
    coefficients of (l, c) is the zero polynomial;
  * cross-checks: evaluation ranks at reducible points and at true padded points
    l . per_3(A s) (A a 9 x 3 integer matrix), both primes.
"""
import sys, os, json, random, itertools, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from wk13_b04_model import (hwv_space, rho, weight_monomials, rank_Q, int_matrix, normalise,
                            combine, rank_eval_Q, rank_eval_p, poly_mul, linear_form, random_cubic,
                            random_linear, random_matrix, restrict_form, exps, P1, P2)
from flint import fmpz_mpoly_ctx

ROOT = os.path.abspath(os.path.join(HERE, '..'))


def per3_form():
    out = {}
    for perm in itertools.permutations(range(3)):
        b = [0] * 9
        for i in range(3):
            b[3 * i + perm[i]] += 1
        out[tuple(b)] = out.get(tuple(b), 0) + 1
    return out


def symbolic_mu_check(h, r):
    """h(l . c) as a polynomial in l_1..l_r and the c_alpha: is it zero?"""
    names = [f"l{i}" for i in range(r)] + [f"c{''.join(map(str, al))}" for al in exps(3, r)]
    ctx = fmpz_mpoly_ctx.get(tuple(names), 'lex')
    g = ctx.gens()
    L = g[:r]
    C = {al: g[r + k] for k, al in enumerate(exps(3, r))}
    zero = ctx.from_dict({})
    q = {}
    for be in exps(4, r):
        v = zero
        for i in range(r):
            if be[i] >= 1:
                al = tuple(be[k] - (1 if k == i else 0) for k in range(r))
                v = v + L[i] * C[al]
        q[be] = v
    tot = zero
    for mono, coef in h.items():
        v = ctx.from_dict({tuple([0] * len(names)): coef})
        for be in mono:
            v = v * q[be]
        tot = tot + v
    return tot.is_zero(), len(tot.monoms()) if not tot.is_zero() else 0


def main():
    t0 = time.time()
    r, delta, lam = 3, 6, (8, 8, 8)
    basis, H = hwv_space(4, r, delta, lam)
    a = len(H)
    lam_minus = (lam[0] - delta,) + lam[1:]
    cols = weight_monomials(3, r, delta, lam_minus)
    RH = [rho(h, r) for h in H]
    mR = rank_Q(RH, cols)
    print(f"cell {lam} delta={delta} r={r}: N_S={len(basis)} a={a} lam^-={lam_minus} "
          f"N_S(lam^-)={len(cols)} rank rho over Q = {mR}  =>  mult_R = {mR}, i_R = {a - mR}")
    # kernel of rho on H
    M = int_matrix(RH, cols)
    X, nul = M.transpose().nullspace()
    kers = [normalise([int(X[i, k]) for i in range(a)]) for k in range(nul)]
    out = dict(board_numbering='batch13', session='B13-04', cell=dict(lam=list(lam), delta=delta, r=r),
               N_S=len(basis), a=a, lam_minus=list(lam_minus), rank_rho_Q=mR, i_R_certified=a - mR,
               exploratory=True, values_are='none')
    rnd = random.Random(20260909)
    red_pts = [poly_mul(linear_form(random_linear(rnd, r, 7, True), r), random_cubic(rnd, r, 7)) for _ in range(30)]
    per3 = per3_form()
    pad_pts = [poly_mul(linear_form(random_linear(rnd, r, 7, True), r), restrict_form(per3, 9, r, random_matrix(rnd, 9, r, 7)))
               for _ in range(30)]
    out['mult_R_eval_Q'] = rank_eval_Q(H, red_pts)
    out['mult_R_eval_p'] = [rank_eval_p(H, red_pts, P1), rank_eval_p(H, red_pts, P2)]
    out['mult_P_eval_Q'] = rank_eval_Q(H, pad_pts)
    out['mult_P_eval_p'] = [rank_eval_p(H, pad_pts, P1), rank_eval_p(H, pad_pts, P2)]
    print(f"evaluation: reducible rank Q={out['mult_R_eval_Q']} p={out['mult_R_eval_p']}; "
          f"true padded (l.per3) rank Q={out['mult_P_eval_Q']} p={out['mult_P_eval_p']}")
    out['kernel'] = []
    for k in kers:
        h = normalise(combine(H, k))
        pure = [m for m in h if all(be[0] >= 1 for be in m)]
        ok_support = (len(pure) == 0)
        zero, nterms = symbolic_mu_check(h, r)
        print(f"kernel vector kappa={k}: {len(h)} monomials, x_1-pure monomials: {len(pure)} "
              f"(support test {'PASS' if ok_support else 'FAIL'}); h(l.c) symbolically zero: {zero}")
        out['kernel'].append(dict(kappa=k, terms=len(h), pure_monomials=len(pure), support_test=ok_support,
                                  symbolic_identity_zero=zero,
                                  h=[[list(map(list, m)), c] for m, c in sorted(h.items())]))
    # and the surviving vector: nonzero on reducible points
    out['seconds'] = round(time.time() - t0, 1)
    os.makedirs(os.path.join(ROOT, 'results', 'b13_04'), exist_ok=True)
    with open(os.path.join(ROOT, 'results', 'b13_04', 'control_888_d6.json'), 'w') as f:
        json.dump(out, f, indent=1)
    print(f"done in {out['seconds']}s")


if __name__ == '__main__':
    main()
