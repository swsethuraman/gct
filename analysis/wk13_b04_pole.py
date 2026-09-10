#!/usr/bin/env python3
"""B13-04, addendum 1 -- the boundary (pole) condition at l_1 = 0.

Lemma B(1) reconstructs h from F = rho(h) by  h(l.c) = l_1^delta F(u_l^{-1}c).
Write l(s) = (s, a_2, ..., a_r) with the a_j fixed integers, and let c be a
fixed integer cubic.  Every coefficient of u_{l(s)}^{-1}c is N(s)/s^m with
deg N <= 3 and m <= 3, so

    P(s)  :=  s^{3 delta} F( u_{l(s)}^{-1} c )        is a polynomial in s,
                                                      deg P <= 6 delta,
    h(l(s).c)  "="  s^delta F( u_{l(s)}^{-1} c )  =  P(s) / s^{2 delta}.

So F comes from a polynomial h only if  s^{2 delta} | P(s), i.e.

    (POLE)   ord_{s=0} P  >=  2 delta.

A specialisation can only RAISE the order of vanishing, so ord < 2 delta at a
single integer (a, c) is a PROOF that F does not descend -- no sampling caveat.

This script evaluates P exactly (Fraction arithmetic, Lagrange interpolation at
6 delta + 1 integer points, denominators cleared) for

  * every F in rho(H_lam)  -- which must satisfy (POLE), an instrument check;
  * the excess witness of results/b13_04/swap_witness_r3_d7.json, which
    satisfies the swap identity symbolically and the general two-factor fibre
    condition, and is not a rho(h).

usage: python3 wk13_b04_pole.py [r delta lam_1 lam_2 ...]      (default 3 7 16 6 6)
"""
import sys, os, json, random, time
from fractions import Fraction
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from wk13_b04_model import (exps, weight_monomials, hwv_space, rho, rank_Q, normalise, combine,
                            random_cubic, eval_poly, poly_mul, linear_form)

ROOT = os.path.abspath(os.path.join(HERE, '..'))


def log(*a):
    print(*a, flush=True)


def shear_cubic(c, a, s, r):
    """u_{l(s)}^{-1} c  with l(s) = (s, a_2..a_r): substitute
    x_1 -> x_1 - sum_{j>=2} (a_j/s) x_j.  Exact Fractions."""
    t = [Fraction(0)] + [Fraction(-a[j], s) for j in range(1, r)]
    lin = {tuple(1 if k == 0 else 0 for k in range(r)): Fraction(1)}
    for j in range(1, r):
        if t[j]:
            lin[tuple(1 if k == j else 0 for k in range(r))] = t[j]
    out = {}
    for al, cf in c.items():
        term = {tuple([0] * r): Fraction(cf)}
        for _ in range(al[0]):
            nt = {}
            for k1, v1 in term.items():
                for k2, v2 in lin.items():
                    kk = tuple(x + y for x, y in zip(k1, k2))
                    nt[kk] = nt.get(kk, Fraction(0)) + v1 * v2
            term = nt
        rest = (0,) + al[1:]
        term = {tuple(x + y for x, y in zip(k, rest)): v for k, v in term.items()}
        for k, v in term.items():
            out[k] = out.get(k, Fraction(0)) + v
    return {k: v for k, v in out.items() if v}


def P_values(F, c, a, r, delta, npts):
    """P(s) = s^{3 delta} F(u_{l(s)}^{-1} c) at s = 1..npts, exactly."""
    vals = []
    for s in range(1, npts + 1):
        cs = shear_cubic(c, a, s, r)
        v = Fraction(0)
        for mono, cf in F.items():
            term = Fraction(cf)
            for al in mono:
                term *= cs.get(al, Fraction(0))
                if term == 0:
                    break
            v += term
        vals.append(v * Fraction(s) ** (3 * delta))
    return vals


def interpolate(vals):
    """coefficients of the polynomial through (i, vals[i-1]), i = 1..n, exactly."""
    n = len(vals)
    xs = [Fraction(i) for i in range(1, n + 1)]
    coeffs = [Fraction(0)] * n
    for i in range(n):
        # Lagrange basis polynomial for node i
        num = [Fraction(1)]
        den = Fraction(1)
        for j in range(n):
            if j == i:
                continue
            num = [Fraction(0)] + num[:]  # multiply by x
            for k in range(len(num) - 1):
                num[k] -= xs[j] * (num[k + 1] if k + 1 < len(num) else 0)
            den *= (xs[i] - xs[j])
        f = vals[i] / den
        for k in range(len(num)):
            if k < n:
                coeffs[k] += f * num[k]
    return coeffs


def poly_from_points(vals):
    """Newton's divided differences -> coefficients in the monomial basis (exact)."""
    n = len(vals)
    xs = [Fraction(i) for i in range(1, n + 1)]
    dd = [Fraction(v) for v in vals]
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            dd[i] = (dd[i] - dd[i - 1]) / (xs[i] - xs[i - j])
    coeffs = [Fraction(0)] * n
    cur = [Fraction(1)] + [Fraction(0)] * (n - 1)      # product (x - x_0)...(x - x_{k-1})
    for k in range(n):
        for t in range(n):
            coeffs[t] += dd[k] * cur[t]
        if k < n - 1:
            new = [Fraction(0)] * n
            for t in range(n - 1, -1, -1):
                if cur[t]:
                    if t + 1 < n:
                        new[t + 1] += cur[t]
                    new[t] -= xs[k] * cur[t]
            cur = new
    return coeffs


def order_at_zero(coeffs):
    for k, v in enumerate(coeffs):
        if v != 0:
            return k
    return None      # identically zero


def main():
    if len(sys.argv) > 1:
        r, delta = int(sys.argv[1]), int(sys.argv[2])
        lam = tuple(int(x) for x in sys.argv[3:])
    else:
        r, delta, lam = 3, 7, (16, 6, 6)
    t0 = time.time()
    rnd = random.Random(777)
    npts = 6 * delta + 2
    basis4, H = hwv_space(4, r, delta, lam)
    lam_minus = (lam[0] - delta,) + tuple(lam[1:])
    cols = weight_monomials(3, r, delta, lam_minus)
    RH = [rho(h, r) for h in H]
    mR = rank_Q(RH, cols)
    a = [0] + [rnd.randint(-5, 5) or 3 for _ in range(r - 1)]
    c = random_cubic(rnd, r, 5)
    log(f"lam={lam} delta={delta} r={r}: a4={len(H)} mult_R={mR}; "
        f"specialisation a={a[1:]}, one random integer cubic, {npts} interpolation nodes; "
        f"the pole test needs ord_0 P >= 2 delta = {2*delta}")
    out = dict(board_numbering='batch13', session='B13-04', addendum=1, mode='pole',
               r=r, delta=delta, lam=list(lam), a=a[1:], seed=777, npts=npts,
               threshold=2 * delta, values_are='none', rho_H=[], seconds=None)
    for i, F in enumerate(RH):
        if not F:
            continue
        ordk = order_at_zero(poly_from_points(P_values(F, c, a, r, delta, npts)))
        out['rho_H'].append(dict(index=i, order=ordk, passes=(ordk is None or ordk >= 2 * delta)))
        log(f"  rho(h_{i}): ord_0 P = {ordk}  {'OK' if (ordk is None or ordk >= 2*delta) else 'FAIL (instrument defect)'}")
    assert all(x['passes'] for x in out['rho_H']), "a rho(h) failed the pole test: instrument defect"
    wf = os.path.join(ROOT, 'results', 'b13_04', 'swap_witness_r3_d7.json')
    if os.path.exists(wf) and (r, delta, tuple(lam)) == (3, 7, (16, 6, 6)):
        w = json.load(open(wf))
        F = {tuple(tuple(x) for x in m): cf for m, cf in w['witness']}
        ordk = order_at_zero(poly_from_points(P_values(F, c, a, r, delta, npts)))
        out['witness'] = dict(order=ordk, threshold=2 * delta,
                              passes=(ordk is None or ordk >= 2 * delta),
                              terms=len(F))
        log(f"  swap/fibre witness: ord_0 P = {ordk} against the threshold {2*delta} -> "
            f"{'passes (unexpected)' if (ordk is None or ordk >= 2*delta) else 'POLE: does not descend'}")
    out['seconds'] = round(time.time() - t0, 1)
    fn = os.path.join(ROOT, 'results', 'b13_04', f'pole_r{r}_d{delta}_{"-".join(map(str, lam))}.json')
    with open(fn, 'w') as fh:
        json.dump(out, fh, indent=1)
    log(f"wrote {fn} ({out['seconds']}s)")


if __name__ == '__main__':
    main()
