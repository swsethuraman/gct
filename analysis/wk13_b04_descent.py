#!/usr/bin/env python3
"""B13-04, addendum 1 (Q6, Q9) -- is the swap identity SUFFICIENT for descent?

For a quartic weight lam with lam_1 >= delta, Lemma B(3) says the additional
padded equations at (lam, delta) are the elements of

    W^lam = rho(H_lam) = { h(x_1 . -) : h a quartic HWV of weight lam }

that lie in the cubic ideal.  Lemma F says every F in W^lam satisfies the swap
identity

    F(l . q)  =  F( u_l^{-1}(x_1 . q) )        for every l with l_1 = 1
                                               and every quadric q,
    u_l^{-1}: x_1 |-> x_1 - sum_{j>=2} l_j x_j,   x_j |-> x_j  (j >= 2),

which is necessary, exact, and costs two evaluations per test point.  This
script asks whether it is sufficient.  Define

    B_full  =  { F of weight lam^- : E_{i,i+1} F = 0 for i >= 2 }
               (every GL_{r-1}-highest vector of that weight -- the Pieri
                channels of the predecessors of (lam,delta) AND the channels of
                the non-predecessor shapes nu with nu_1 > lam_1)
    T^lam   =  { F in B_full : F satisfies the swap identity }.

Then rho(H_lam) subset T^lam subset B_full, and the question is whether the
first containment is an equality.  The swap conditions are linear in F, so
T^lam is an exact kernel over Q; conditions are added until the dimension has
been stable for a stated number of further random points, and the answer is
cross-checked at both house primes.

Also (Q9) an independent check of every a-value: dim of the exact highest-weight
kernel against the Kostant alternation of analysis/wk13_b04_pred13.kostant.

Note the swap conditions and B_full involve only (r, delta, lam) -- not the
cubic f.  So the descent question is a statement about the reducible locus
alone, and `sweep` mode runs it with no model attached.

usage: python3 wk13_b04_descent.py <tag> <delta>       tag in A B C D E
       python3 wk13_b04_descent.py sweep <r> <delta>   descent only, no model
"""
import sys, os, json, random, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'tools', 'verify'))
from wk13_b04_model import (exps, weight_monomials, hwv_space, rho, rank_Q, int_matrix, normalise,
                            combine, poly_mul, poly_pow, linear_form, x1_times, substitute_x1,
                            eval_poly, partitions_with_parts, predecessors, restrict_form,
                            random_matrix, SymbolicCubic, add_to, P1, P2)
from wk13_b04_pred13 import kostant
from flint import fmpz_mat, nmod_mat

ROOT = os.path.abspath(os.path.join(HERE, '..'))

MODELS = {
    'A': ({(3,): 1}, 1, 2),
    'B': ({(3, 0): 1, (0, 3): 1}, 2, 3),
    'C': ({(1, 1, 1): 1}, 3, 3),
    'D': ({(3, 0, 0, 0): 1}, 4, 4),
    'E': ({(3, 0, 0, 0): 1, (0, 3, 0, 0): 1}, 4, 4),
}
STABLE = 25          # extra points with no dimension change before saturation


def log(*a):
    print(*a, flush=True)


def swap_row(vecs, cols, l, q, r):
    """the linear functional F |-> F(l.q) - F(u_l^{-1}(x_1.q)) evaluated on each
    basis vector; returns the row of coefficients."""
    lhs_pt = poly_mul(linear_form(l, r), q)
    rhs_pt = substitute_x1(x1_times(q, r), l, r)
    return [eval_poly(v, lhs_pt) - eval_poly(v, rhs_pt) for v in vecs]


def kernel_rows(rows, nc):
    if not rows:
        return [[1 if i == k else 0 for i in range(nc)] for k in range(nc)]
    M = fmpz_mat(len(rows), nc, [0] * (len(rows) * nc))
    for i, rw in enumerate(rows):
        for j, v in enumerate(rw):
            M[i, j] = v
    X, nul = M.nullspace()
    return [normalise([int(X[i, k]) for i in range(nc)]) for k in range(nul)]


def rank_mod(rows, nc, p):
    if not rows:
        return 0
    ent = []
    for rw in rows:
        for v in rw:
            ent.append(v % p)
    return nmod_mat(len(rows), nc, ent, p).rank()


def descent_cell(lam, delta, r, rnd, want_witness=True):
    """dim rho(H_lam), dim B_full, dim T (the swap-identity subspace of B_full),
    exactly over Q, with both primes as a cross-check."""
    basis4, H = hwv_space(4, r, delta, lam)
    a4 = len(H)
    lam_minus = (lam[0] - delta,) + tuple(lam[1:])
    cols = weight_monomials(3, r, delta, lam_minus)
    RH = [rho(h, r) for h in H]
    mR = rank_Q(RH, cols)
    _, Bfull = hwv_space(3, r, delta, lam_minus, first=1)
    nB = len(Bfull)
    rows, dim, stable, npts = [], nB, 0, 0
    while stable < STABLE:
        l = [1] + [rnd.randint(-6, 6) for _ in range(r - 1)]
        q = {al: rnd.randint(-6, 6) for al in exps(2, r)}
        rows.append(swap_row(Bfull, cols, l, q, r))
        npts += 1
        K = kernel_rows(rows, nB)
        if len(K) == dim:
            stable += 1
        else:
            dim, stable = len(K), 0
    T = [normalise(combine(Bfull, k)) for k in kernel_rows(rows, nB)]
    rk_p = [nB - rank_mod(rows, nB, P1), nB - rank_mod(rows, nB, P2)]
    contained = (rank_Q(T + RH, cols) == rank_Q(T, cols)) if T else (mR == 0)
    assert contained, ("Lemma F violated by rho(H_lam): instrument defect", lam)
    return dict(lam=list(lam), a4=a4, lam_minus=list(lam_minus), N_S_lam_minus=len(cols),
                mult_R=mR, dim_B_full=nB, dim_T=len(T), dim_T_mod_p=rk_p,
                swap_points_used=npts, excess_T_over_W=len(T) - mR,
                swap_is_exact=(len(T) == mR), rho_H_in_T=contained), T, RH, cols


def sweep():
    """Q6 over a range of (r, delta, lam) with no cubic model attached."""
    r, delta = int(sys.argv[2]), int(sys.argv[3])
    t0 = time.time()
    rnd = random.Random(20260909)
    out = dict(board_numbering='batch13', session='B13-04', addendum=1, mode='sweep',
               r=r, delta=delta, primes=[P1, P2], seed=20260909, values_are='none',
               stable_points_required=STABLE, cells=[])
    for lam in partitions_with_parts(4 * delta, r):
        basis4, H = hwv_space(4, r, delta, lam)
        if not H:
            continue
        a4k = kostant(4, r, delta, lam)
        assert len(H) == a4k, ("Q9: a^(4) disagrees with the Kostant alternation", lam, len(H), a4k)
        if lam[0] < delta:
            out['cells'].append(dict(lam=list(lam), a4=len(H), mult_R=0, note='lam_1 < delta'))
            continue
        cell, T, RH, cols = descent_cell(lam, delta, r, rnd)
        cell['a4_kostant'] = a4k
        if not cell['swap_is_exact']:
            wit = next((v for v in T if rank_Q(RH + [v], cols) > cell['mult_R']), None)
            cell['excess_witness_terms'] = len(wit) if wit else None
            cell['excess_witness'] = ([[list(map(list, m)), c] for m, c in sorted(wit.items())]
                                      if wit is not None and len(wit) <= 80 else None)
        out['cells'].append(cell)
        log(f"[sweep r={r} d={delta}] lam={lam} a4={cell['a4']} mult_R={cell['mult_R']} "
            f"B_full={cell['dim_B_full']} T={cell['dim_T']} {cell['dim_T_mod_p']} "
            f"pts={cell['swap_points_used']} -> excess {cell['excess_T_over_W']} "
            f"{'EXACT' if cell['swap_is_exact'] else 'STRICTLY WEAKER'}")
    cells = [c for c in out['cells'] if 'dim_T' in c]
    out['summary'] = dict(cells=len(cells), swap_exact=sum(1 for c in cells if c['swap_is_exact']),
                          swap_weaker=sum(1 for c in cells if not c['swap_is_exact']),
                          total_excess=sum(c['excess_T_over_W'] for c in cells),
                          total_mult_R=sum(c['mult_R'] for c in cells),
                          total_B_full=sum(c['dim_B_full'] for c in cells))
    out['seconds'] = round(time.time() - t0, 1)
    log(f"summary r={r} delta={delta}: {out['summary']}  ({out['seconds']}s)")
    os.makedirs(os.path.join(ROOT, 'results', 'b13_04'), exist_ok=True)
    fn = os.path.join(ROOT, 'results', 'b13_04', f'descent_sweep_r{r}_d{delta}.json')
    with open(fn, 'w') as fh:
        json.dump(out, fh, indent=1)
    log(f"wrote {fn}")


def main():
    if sys.argv[1] == 'sweep':
        return sweep()
    tag = sys.argv[1]
    delta = int(sys.argv[2])
    f, N, r = MODELS[tag]
    t0 = time.time()
    rnd = random.Random(20260909)
    sym = SymbolicCubic(f, N, r)
    out = dict(board_numbering='batch13', session='B13-04', addendum=1, model=tag, delta=delta,
               N=N, r=r, f={str(k): v for k, v in f.items()}, primes=[P1, P2], seed=20260909,
               values_are='none', stable_points_required=STABLE, cells=[])

    # ---- cubic side: i^(3) per shape, certified, plus the Kostant a-check
    cubic_pts = [restrict_form(f, N, r, random_matrix(rnd, N, r, 7)) for _ in range(60)]
    cubic = {}
    for nu in partitions_with_parts(3 * delta, r):
        basis, G = hwv_space(3, r, delta, nu)
        if not G:
            continue
        a3 = len(G)
        a3k = kostant(3, r, delta, nu)
        assert a3 == a3k, ("Q9: a^(3) disagrees with the Kostant alternation", nu, a3, a3k)
        # exact cubic ideal in this weight: kernel of evaluation, every vector certified
        M = fmpz_mat(len(cubic_pts), a3, [0] * (len(cubic_pts) * a3))
        for i, F in enumerate(cubic_pts):
            for j, g in enumerate(G):
                M[i, j] = eval_poly(g, F)
        X, nul = M.nullspace()
        ker = [normalise([int(X[i, k]) for i in range(a3)]) for k in range(nul)]
        cert = all(sym.vanishes(combine(G, k)) for k in ker)
        cubic[tuple(nu)] = dict(a3=a3, i3=(len(ker) if cert else None), certified=cert)
    out['cubic'] = {str(k): v for k, v in cubic.items()}
    log(f"[cubic] {sum(v['a3'] for v in cubic.values())} channel dimensions over "
        f"{len(cubic)} shapes; ideal shapes: "
        f"{[(k, v['i3']) for k, v in cubic.items() if v['i3']]}")

    # ---- quartic side
    for lam in partitions_with_parts(4 * delta, r):
        basis4, H = hwv_space(4, r, delta, lam)
        if not H:
            continue
        a4 = len(H)
        a4k = kostant(4, r, delta, lam)
        assert a4 == a4k, ("Q9: a^(4) disagrees with the Kostant alternation", lam, a4, a4k)
        if lam[0] < delta:
            out['cells'].append(dict(lam=list(lam), a4=a4, a4_kostant=a4k, mult_R=0,
                                     note='lam_1 < delta: rho = 0'))
            continue
        lam_minus = (lam[0] - delta,) + tuple(lam[1:])
        cols = weight_monomials(3, r, delta, lam_minus)
        RH = [rho(h, r) for h in H]
        mR = rank_Q(RH, cols)
        _, Bfull = hwv_space(3, r, delta, lam_minus, first=1)
        nB = len(Bfull)
        preds = [tuple(p) for p in predecessors(lam, delta)]
        sum_a3 = sum(cubic.get(p, dict(a3=0))['a3'] for p in preds)
        sum_i3 = sum((cubic.get(p, dict(i3=0))['i3'] or 0) for p in preds)
        by_len = {}
        for p in preds:
            L = len([x for x in p if x])
            e = by_len.setdefault(L, dict(count=0, a3=0, i3=0))
            e['count'] += 1
            e['a3'] += cubic.get(p, dict(a3=0))['a3']
            e['i3'] += (cubic.get(p, dict(i3=0))['i3'] or 0)
        # saturate the swap conditions on B_full
        rows, dim, stable, npts = [], nB, 0, 0
        while stable < STABLE:
            l = [1] + [rnd.randint(-6, 6) for _ in range(r - 1)]
            q = {al: rnd.randint(-6, 6) for al in exps(2, r)}
            rows.append(swap_row(Bfull, cols, l, q, r))
            npts += 1
            K = kernel_rows(rows, nB)
            if len(K) == dim:
                stable += 1
            else:
                dim, stable = len(K), 0
        T = [normalise(combine(Bfull, k)) for k in kernel_rows(rows, nB)]
        dimT = len(T)
        rk_p = [nB - rank_mod(rows, nB, P1), nB - rank_mod(rows, nB, P2)]
        # instrument check: rho(H_lam) must satisfy the swap identity
        contained = (rank_Q(T + RH, cols) == rank_Q(T, cols)) if T else (mR == 0)
        assert contained, ("Lemma F violated by rho(H_lam): instrument defect", lam)
        excess = dimT - mR
        cell = dict(lam=list(lam), a4=a4, a4_kostant=a4k, lam_minus=list(lam_minus),
                    N_S_lam_minus=len(cols), mult_R=mR, dim_B_full=nB, dim_B_pred=sum_a3,
                    sum_a3=sum_a3, sum_i3=sum_i3, dim_T=dimT, dim_T_mod_p=rk_p,
                    swap_points_used=npts, excess_T_over_W=excess,
                    swap_is_exact=(excess == 0), predecessors_by_length=by_len,
                    rho_H_in_T=contained)
        if excess > 0:
            # a vector satisfying the swap identity that is NOT a rho(h): the negative
            wit = None
            for v in T:
                if rank_Q(RH + [v], cols) > mR:
                    wit = v
                    break
            cell['excess_witness'] = ([[list(map(list, m)), c] for m, c in sorted(wit.items())]
                                      if wit is not None and len(wit) <= 60 else None)
            cell['excess_witness_terms'] = len(wit) if wit is not None else None
        out['cells'].append(cell)
        log(f"[cell] lam={lam} a4={a4} mult_R={mR} dim B_full={nB} (predecessor channels {sum_a3}) "
            f"dim T={dimT} {rk_p} after {npts} points -> excess {excess} "
            f"{'SWAP EXACT' if excess == 0 else 'SWAP STRICTLY WEAKER'} | by length {by_len}")
    cells = [c for c in out['cells'] if 'dim_T' in c]
    out['summary'] = dict(cells=len(cells), swap_exact=sum(1 for c in cells if c['swap_is_exact']),
                          swap_weaker=sum(1 for c in cells if not c['swap_is_exact']),
                          total_excess=sum(c['excess_T_over_W'] for c in cells))
    out['seconds'] = round(time.time() - t0, 1)
    log(f"summary: {out['summary']}  ({out['seconds']}s)")
    os.makedirs(os.path.join(ROOT, 'results', 'b13_04'), exist_ok=True)
    fn = os.path.join(ROOT, 'results', 'b13_04', f'descent_{tag}_d{delta}.json')
    with open(fn, 'w') as fh:
        json.dump(out, fh, indent=1)
    log(f"wrote {fn}")


if __name__ == '__main__':
    main()
