#!/usr/bin/env python3
"""B13-04, addendum 1 -- the general two-factor (fibre) condition.

Lemma B(1) reconstructs a quartic highest-weight vector from F = rho(h) by

    h(l . c) = l_1^delta . F(u_l^{-1} c),        l_1 != 0.

For that to be a well-defined function on the reducible locus, the value must
not depend on WHICH linear factor is called l.  A quartic with two linear
factors is l . l' . q, and the condition is

    (FIB)   l_1^delta F( u_l^{-1}(l'.q) )  =  l'_1^delta F( u_{l'}^{-1}(l.q) )
            for all l, l' with l_1, l'_1 != 0 and all quadrics q.

Taking l = x_1 gives exactly the swap identity of Lemma F, so

    rho(H_lam)  subset  T_fib  subset  T_swap  subset  B_full,

and the descent sweep found one cell -- r = 3, delta = 7, lam = (16,6,6) --
where T_swap is strictly bigger than rho(H_lam).  This script computes T_fib
there (and at any cell named on the command line), exactly over Q, with
l_1 = l'_1 = 1 so every evaluation is integral.  It answers: is the general
fibre condition strictly stronger than its x_1 slice, and is it exactly
descent?

Sampling can only UNDER-constrain a kernel, so a computed dim equal to mult_R
certifies equality with rho(H_lam); a computed dim above mult_R is a ceiling
and is reported as such.

usage: python3 wk13_b04_fibre.py <r> <delta> [lam_1 lam_2 ...]
       (no lam: every lam of the (r, delta) census with lam_1 >= delta)
"""
import sys, os, json, random, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from wk13_b04_model import (exps, weight_monomials, hwv_space, rho, rank_Q, normalise, combine,
                            poly_mul, linear_form, x1_times, substitute_x1, eval_poly,
                            partitions_with_parts, P1, P2)
from wk13_b04_descent import swap_row, kernel_rows, rank_mod

ROOT = os.path.abspath(os.path.join(HERE, '..'))
STABLE = 40


def log(*a):
    print(*a, flush=True)


def fibre_row(vecs, l, lp, q, r):
    """F |-> F(u_l^{-1}(l'.q)) - F(u_{l'}^{-1}(l.q)), for l_1 = l'_1 = 1."""
    lhs_pt = substitute_x1(poly_mul(linear_form(lp, r), q), l, r)
    rhs_pt = substitute_x1(poly_mul(linear_form(l, r), q), lp, r)
    return [eval_poly(v, lhs_pt) - eval_poly(v, rhs_pt) for v in vecs]


def saturate(rowfn, nB, rnd, stable_needed=STABLE):
    rows, dim, stable = [], nB, 0
    while stable < stable_needed:
        rows.append(rowfn(rnd))
        K = kernel_rows(rows, nB)
        if len(K) == dim:
            stable += 1
        else:
            dim, stable = len(K), 0
    return rows, kernel_rows(rows, nB)


def main():
    r, delta = int(sys.argv[1]), int(sys.argv[2])
    if len(sys.argv) > 3:
        lams = [tuple(int(x) for x in sys.argv[3:])]
    else:
        lams = [l for l in partitions_with_parts(4 * delta, r) if l[0] >= delta]
    t0 = time.time()
    rnd = random.Random(20260909)
    out = dict(board_numbering='batch13', session='B13-04', addendum=1, mode='fibre',
               r=r, delta=delta, primes=[P1, P2], seed=20260909, values_are='none',
               stable_points_required=STABLE, cells=[])
    for lam in lams:
        basis4, H = hwv_space(4, r, delta, lam)
        if not H:
            continue
        lam_minus = (lam[0] - delta,) + tuple(lam[1:])
        cols = weight_monomials(3, r, delta, lam_minus)
        RH = [rho(h, r) for h in H]
        mR = rank_Q(RH, cols)
        _, Bfull = hwv_space(3, r, delta, lam_minus, first=1)
        nB = len(Bfull)

        def swapfn(rd):
            l = [1] + [rd.randint(-7, 7) for _ in range(r - 1)]
            q = {al: rd.randint(-7, 7) for al in exps(2, r)}
            return swap_row(Bfull, cols, l, q, r)

        def fibfn(rd):
            l = [1] + [rd.randint(-7, 7) for _ in range(r - 1)]
            lp = [1] + [rd.randint(-7, 7) for _ in range(r - 1)]
            q = {al: rd.randint(-7, 7) for al in exps(2, r)}
            return fibre_row(Bfull, l, lp, q, r)

        rows_s, Ks = saturate(swapfn, nB, rnd)
        rows_f, Kf = saturate(fibfn, nB, rnd)
        # both families together
        rows_b = rows_s + rows_f
        Kb = kernel_rows(rows_b, nB)
        Tb = [normalise(combine(Bfull, k)) for k in Kb]
        contained = (rank_Q(Tb + RH, cols) == rank_Q(Tb, cols)) if Tb else (mR == 0)
        assert contained, ("rho(H_lam) fails the fibre condition: instrument defect", lam)
        cell = dict(lam=list(lam), a4=len(H), lam_minus=list(lam_minus), N_S_lam_minus=len(cols),
                    mult_R=mR, dim_B_full=nB, dim_T_swap=len(Ks), dim_T_fib=len(Kf),
                    dim_T_both=len(Kb),
                    dim_T_both_mod_p=[nB - rank_mod(rows_b, nB, p) for p in (P1, P2)],
                    swap_points=len(rows_s), fibre_points=len(rows_f),
                    fibre_exact=(len(Kb) == mR), swap_exact=(len(Ks) == mR),
                    fibre_strictly_stronger=(len(Kb) < len(Ks)), rho_H_in_T=contained)
        if len(Kb) > mR:
            wit = next((v for v in Tb if rank_Q(RH + [v], cols) > mR), None)
            cell['excess_witness_terms'] = len(wit) if wit is not None else None
            cell['excess_witness'] = ([[list(map(list, m)), c] for m, c in sorted(wit.items())]
                                      if wit is not None and len(wit) <= 120 else None)
        out['cells'].append(cell)
        log(f"[fibre] lam={lam} a4={cell['a4']} mult_R={mR} B_full={nB} "
            f"T_swap={len(Ks)} T_fib={len(Kf)} T_both={len(Kb)} {cell['dim_T_both_mod_p']} "
            f"-> {'FIBRE EXACT' if cell['fibre_exact'] else 'FIBRE STILL WEAKER (ceiling)'}"
            f"{'; fibre beats swap' if cell['fibre_strictly_stronger'] else ''}")
    cells = out['cells']
    out['summary'] = dict(cells=len(cells),
                          fibre_exact=sum(1 for c in cells if c['fibre_exact']),
                          swap_exact=sum(1 for c in cells if c['swap_exact']),
                          fibre_beats_swap=sum(1 for c in cells if c['fibre_strictly_stronger']))
    out['seconds'] = round(time.time() - t0, 1)
    log(f"summary: {out['summary']} ({out['seconds']}s)")
    os.makedirs(os.path.join(ROOT, 'results', 'b13_04'), exist_ok=True)
    tag = f"r{r}_d{delta}" + ("" if len(sys.argv) <= 3 else "_" + "-".join(sys.argv[3:]))
    fn = os.path.join(ROOT, 'results', 'b13_04', f'fibre_{tag}.json')
    with open(fn, 'w') as fh:
        json.dump(out, fh, indent=1)
    log(f"wrote {fn}")


if __name__ == '__main__':
    main()
