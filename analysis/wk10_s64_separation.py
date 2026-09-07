#!/usr/bin/env python3
"""Session 64 -- the r >= 6 separation test (integrator note 2 §4), done right.

At r <= 5, P_r = R_r, so mult_pad = mult_red by theorem and NO multiplicity
calibration can tell a correct padded engine from one that silently implemented
the reducible side.  At r = 6 the varieties separate (P_6 ⊊ R_6), but session 47
proved mult_pad = mult_red at every reachable r = 6 cell too -- so the
multiplicities coincide in reach as well; the permanent-specific ideal appears
only at the LMR degree.

The separation available in reach is at the level of the sample VARIETY, and it
is NOT linear: the permanental cubics linearly span all of Sym^3 C^6 (they are a
50-dimensional variety, not a 50-dimensional subspace).  The right invariant is
the DIMENSION of the variety ev_pad samples, i.e. the Jacobian rank of ev_pad's
own parametrisation:

    ev_pad : (l, A) -> l(s)·per_3(A(s))          dim P_r
    ev_red : (l, c) -> l·c                        dim R_r

  dim R_r = r + C(r+2,3) - 1
  dim P_r = r + (permanental-cubic image dim) - 1 = r + min(9r-4, C(r+2,3)) - 1

so dim P_r = dim R_r for r <= 5 (why no r<=5 test separates) and
dim P_6 = 55 < 61 = dim R_6 (deficit 6, the permanental fibre = the 4-torus of
per(D1 M D2)).  Computing the Jacobian rank of the ACTUAL pad_coeffs
parametrisation and getting dim P_6 = 55 (not 61) proves ev_pad samples the
padded variety, not the reducible one -- an engine that had silently implemented
ev_red would return 61.

Also measures mult_pad vs mult_red on small r=6 cells (independent engine):
expect equality (session-47 exactness), i.e. the coincidence at r<=6 is a
theorem about the varieties, not the two engines being the same code.
"""
import os, sys, random, itertools, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
from math import comb
from flint import nmod_mat
from wk8_s30_core import exps, restrict, per_padded, P1, P2
from wk10_s64_pad import pad_coeffs

PRIMES = (P1, P2)
PAD34, N_PAD = per_padded(3, 4)


def quartic_monos(r):
    return exps(4, r)


def _vec(cd, monos, idx, p):
    v = [0] * len(monos)
    for e, c in cd.items():
        if c % p: v[idx[e]] = c % p
    return v


def _num_jac_rank(param_dim, coeff_of, base, r, p, eps_seed=0):
    """Jacobian rank at `base` of a polynomial map params->quartic, by exact finite
    differences over the integers reduced mod p (the map is multilinear/low-degree,
    so a symmetric difference with unit step is exact up to the map's degree; we use
    the exact partial via param perturbation and subtraction of the base, valid
    because each coordinate enters coeff_of polynomially and we take the linear part
    by a fresh random direction refinement).  Simpler and exact here: build the
    Jacobian columns as coeff_of(base + t e_k) expanded — but coeff_of is not linear,
    so we instead sample the tangent space by many secants, which for an irreducible
    parametrisation gives the variety dimension."""
    raise NotImplementedError


def variety_dim(sample, param_draw, ncols, nsamp, p, base_pt, tangent=True):
    pass


def dim_padded(r, p, seed=0, nsamp=None):
    """dim of the padded variety P_r = closure{ l(s)·per_3(A(s)) } in Sym^4 C^r,
    as the rank of the secant/tangent sample: the span of {F(x) - F(x0)} for many
    random parameter points x near a fixed x0 is the tangent space of the cone;
    for an irreducible parametrisation its rank = dim of the affine cone over P_r.
    We use the exact tangent space: partial derivatives of the parametrisation."""
    monos = quartic_monos(r); nc = len(monos); idx = {e: k for k, e in enumerate(monos)}
    rnd = random.Random(seed * 131 + p % 101)
    # base parameters: l in Z^r, A (3x3) each a length-r linear form == a frame V (r x 10):
    # v_i[0] = l coefficient on s_i ; v_i[1+3a+b] = A_{ab} coefficient on s_i
    V0 = [[rnd.randint(-30, 30) for _ in range(10)] for _ in range(r)]
    base = _vec(pad_coeffs(V0), monos, idx, p)
    rows = []
    # tangent = partial wrt each of the 10r frame entries, by exact directional derivative:
    # pad_coeffs is multilinear of degree 4 in the frame entries along s; use the identity
    # d/dt F(V0 + t E_{i,c}) |_{t=0}, computed exactly by a two-point difference at t=1 with the
    # nonlinear-in-t terms removed via a 4-point stencil (degree <= 4 in t).
    for i in range(r):
        for c in range(10):
            # 4-point exact derivative for a degree-<=4 polynomial in t (coeffs mod p):
            # f'(0) = (-2 f(2) + 16 f(1) - 16 f(-1) + 2 f(-2)) / 24   (5-pt, exact to degree 4)
            def fval(t):
                Vt = [list(row) for row in V0]; Vt[i][c] = (Vt[i][c] + t)
                return _vec(pad_coeffs(Vt), monos, idx, p)
            f1 = fval(1); fm1 = fval(-1); f2 = fval(2); fm2 = fval(-2)
            inv24 = pow(24, p - 2, p)
            col = [((-2 * f2[k] + 16 * f1[k] - 16 * fm1[k] + 2 * fm2[k]) * inv24) % p for k in range(nc)]
            rows.append(col)
    return nmod_mat(len(rows), nc, [x % p for row in rows for x in row], p).rank()


def dim_reducible(r, p, seed=0):
    """dim of R_r = closure{ l·c } in Sym^4 C^r, by the exact tangent space of
    (l, c) -> l·c at a random point."""
    monos = quartic_monos(r); nc = len(monos); idx = {e: k for k, e in enumerate(monos)}
    cmon = exps(3, r); clen = len(cmon)
    rnd = random.Random(seed * 977 + p % 103)
    l0 = [rnd.randint(-30, 30) for _ in range(r)]
    c0 = {e: rnd.randint(-30, 30) for e in cmon}
    def mul(l, c):
        out = {}
        for e3, cc in c.items():
            for i in range(r):
                if l[i] == 0: continue
                a4 = list(e3); a4[i] += 1; k = tuple(a4)
                out[k] = (out.get(k, 0) + l[i] * cc) % p
        return out
    rows = []
    # d/d l_i : c0 shifted by x_i
    for i in range(r):
        d = {}
        for e3, cc in c0.items():
            a4 = list(e3); a4[i] += 1; d[tuple(a4)] = cc % p
        rows.append(_vec(d, monos, idx, p))
    # d/d c_e : l0 * x^e
    for e3 in cmon:
        d = {}
        for i in range(r):
            if l0[i] == 0: continue
            a4 = list(e3); a4[i] += 1; k = tuple(a4)
            d[k] = (d.get(k, 0) + l0[i]) % p
        rows.append(_vec(d, monos, idx, p))
    return nmod_mat(len(rows), nc, [x % p for row in rows for x in row], p).rank()


def main():
    do_mult = '--with-mult' in sys.argv
    res = dict(note="r>=6 separation of ev_pad from ev_red at the sample-variety level (integrator note 2 §4)")
    res['dims'] = []
    print("r | dim Sym^4 | dim P_r (ev_pad) | dim R_r (ev_red) | expected P/R | separates?")
    for r in (5, 6, 7):
        nc = comb(r + 3, 4)
        dp = max(dim_padded(r, P1, s) for s in (0, 1)); dp2 = dim_padded(r, P2, 0)
        dr = dim_reducible(r, P1, 0); dr2 = dim_reducible(r, P2, 0)
        exp_p = r + min(9 * r - 4, comb(r + 2, 3)) - 1
        exp_r = r + comb(r + 2, 3) - 1
        sep = dp < dr
        res['dims'].append(dict(r=r, dim_quartic=nc, dim_P=dp, dim_P_p2=dp2, dim_R=dr, dim_R_p2=dr2,
                                expected_P=exp_p, expected_R=exp_r, separates=bool(sep)))
        print(f"{r} | {nc:8d} | {dp:3d} (exp {exp_p}) {'✓' if dp==exp_p else '✗'} | {dr:3d} (exp {exp_r}) {'✓' if dr==exp_r else '✗'} | "
              f"{exp_p}/{exp_r} | {'YES (deficit %d)'%(dr-dp) if sep else 'no (equal)'}")
    res['r6_multiplicity'] = []
    if do_mult:
        from wk10_s64_indep import measure_indep
        for c in [dict(delta=6, lam=[18, 2, 2, 2, 2, 2]), dict(delta=6, lam=[16, 4, 2, 2, 2, 2])]:
            m = measure_indep(c['lam'], c['delta'], seeds=2)
            if m.get('status') == 'a=0':
                res['r6_multiplicity'].append(dict(cell=c, status='a=0')); continue
            res['r6_multiplicity'].append(dict(cell=c, a=m['a'], mult_det=m['mult_det'],
                                               mult_red=m['mult_red'], mult_pad=m['mult_pad'],
                                               pad_eq_red=(m['mult_pad'] == m['mult_red'])))
        print("\nr=6 multiplicity (independent engine): expect mult_pad = mult_red (s47 exactness)")
        for m in res['r6_multiplicity']:
            if m.get('status') == 'a=0': print(f"  {tuple(m['cell']['lam'])}: a=0"); continue
            print(f"  {tuple(m['cell']['lam'])} d{m['cell']['delta']}: a={m['a']} mult_det={m['mult_det']} "
                  f"mult_red={m['mult_red']} mult_pad={m['mult_pad']} pad=red:{m['pad_eq_red']}")
    json.dump(res, open(os.path.join(ROOT, 'results/s64_separation.json'), 'w'), indent=1)
    ok = all(d['separates'] and d['dim_P'] == d['expected_P'] and d['dim_R'] == d['expected_R']
             for d in res['dims'] if d['r'] >= 6) and \
         all(d['dim_P'] == d['dim_R'] for d in res['dims'] if d['r'] == 5)
    print("\nSEPARATION VERDICT:", "ev_pad's sample variety P_r is strictly smaller than R_r at r>=6 "
          "(dim P_6=55 < 61=dim R_6) and equal at r=5 — the engine provably samples the padded variety, "
          "not the reducible one" if ok else "INCONCLUSIVE — inspect")
    return ok


if __name__ == '__main__':
    sys.exit(0 if main() else 1)
