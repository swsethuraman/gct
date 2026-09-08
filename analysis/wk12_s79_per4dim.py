#!/usr/bin/env python3
"""
Session 79 -- the per_4 column is PROPER at length 6 (and vacuous at 5): session 71's
Jacobian (wk11_s71_per4.jacobian, unchanged arithmetic) at general R.

    Phi_f : (M_4)^R -> Sym^4 C^R,  (A_1..A_R) -> f(sum s_i A_i),  f in {det_4, per_4}.

rank_p(dPhi) at one integer point is a lower bound on the generic rank = dim of
the image cone; the trivial upper bound is 16R.  At R = 6: 16R = 96 < 126 =
dim Sym^4 C^6, so Per_6 is proper whatever the rank; the measured rank is the
dimension (expected 90 = 16R - 6, the 4-torus fibre); det_4 must give
16R - 30 = 66 (the control on the control).
"""
import sys, os, random, json, itertools
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from flint import nmod_mat
from wk8_s30_core import P1, P2, exps
import wk11_s71_per4 as s71


def jacobian_R(A, signed, R):
    s71.R = R
    return s71.jacobian(A, signed)


if __name__ == '__main__':
    R = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 20260908
    rnd = random.Random(seed)
    L = len(exps(4, R))
    out = {}
    for name, signed in (('det_4', True), ('per_4', False)):
        ranks = []
        for trial in range(2):
            A = [[[rnd.randint(-40, 40) for _ in range(4)] for _ in range(4)] for _ in range(R)]
            J = jacobian_R(A, signed, R)
            ranks.append((s71.rank_mod(J, P1), s71.rank_mod(J, P2)))
        out[name] = ranks
        print(f"R={R} {name}: Jacobian ranks (P1, P2) at 2 random integer points: {ranks}  [dim Sym^4 C^R = {L}; 16R = {16*R}; 16R-30 = {16*R-30}; 16R-6 = {16*R-6}]")
    proper = 16 * R < L
    print(f"per_4 column at R={R}: {'PROPER (16R < dim Sym^4 C^R, so the image is a proper subvariety; measured dim = max rank)' if proper else 'not proper by the dimension count'}")
    json.dump(dict(R=R, seed=seed, dim_ambient=L, ranks=out, proper_by_dimension_count=proper,
                   measured_dim_per4=max(max(r) for r in out['per_4']), measured_dim_det4=max(max(r) for r in out['det_4'])),
              open(os.path.join(HERE, '..', 'results', f's79_per4_dimension_R{R}.json'), 'w'), indent=1)
