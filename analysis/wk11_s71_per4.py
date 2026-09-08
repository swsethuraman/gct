#!/usr/bin/env python3
"""
Session 71 -- is the unpadded per_4 pencil map dominant on Sym^4 C^5?

    Phi_f : (M_4)^5 -> Sym^4 C^5,   (A_1..A_5) -> f(s_1 A_1 + ... + s_5 A_5),   f in {det_4, per_4}.

The rank of dPhi at one point is a lower bound for the generic rank, and
rank_p <= rank_Q, so rank_p(dPhi) = 70 at ONE integer point and ONE prime
proves Phi_per4 dominant (I(Per_5) = 0: mult_per4 = a at every cell, a
theorem).  The same computation at f = det_4 must give dim D_5 = 50 (the
brief's 16r - 30) -- the control on the control.

d/d(A_i)_{ab} f(M(s)) = s_i . (d f / d M_{ab})(M(s)), the cofactor (det) or the
permanental minor (per) of M(s) at (a, b), a cubic form in s; times s_i, a
quartic -- exact integer arithmetic on dicts {exponent: coefficient}.
"""
import sys, os, itertools, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from flint import nmod_mat
from wk8_s30_core import P1, P2, exps

R = 5


def lin(coeffs):                      # linear form sum_i c_i s_i as a dict
    return {tuple(1 if j == i else 0 for j in range(R)): c for i, c in enumerate(coeffs) if c}


def mul(f, g):
    out = {}
    for ea, ca in f.items():
        for eb, cb in g.items():
            e = tuple(x + y for x, y in zip(ea, eb)); out[e] = out.get(e, 0) + ca * cb
    return {e: c for e, c in out.items() if c}


def add(f, g, sg=1):
    out = dict(f)
    for e, c in g.items(): out[e] = out.get(e, 0) + sg * c
    return {e: c for e, c in out.items() if c}


def minor3(Mlin, rows, cols, signed):
    """det (signed) or permanent (unsigned) of the 3x3 submatrix of the linear-form matrix."""
    out = {}
    for perm in itertools.permutations(range(3)):
        sg = 1
        if signed:
            for i in range(3):
                for j in range(i + 1, 3):
                    if perm[i] > perm[j]: sg = -sg
        term = {tuple([0] * R): 1}
        for i in range(3):
            term = mul(term, Mlin[rows[i]][cols[perm[i]]])
        out = add(out, term, sg)
    return out


def jacobian(A, signed):
    """70 x 80 integer matrix: rows = quartic monomials (exps(4, 5) order), columns = parameters (i, a, b)."""
    Mlin = [[lin([A[i][a][b] for i in range(R)]) for b in range(4)] for a in range(4)]
    mons = exps(4, R); idx = {m: k for k, m in enumerate(mons)}
    J = [[0] * (R * 16) for _ in range(len(mons))]
    for i in range(R):
        si = {tuple(1 if j == i else 0 for j in range(R)): 1}
        for a in range(4):
            for b in range(4):
                rows = [x for x in range(4) if x != a]; cols = [y for y in range(4) if y != b]
                cof = minor3(Mlin, rows, cols, signed)
                if signed and (a + b) % 2: cof = {e: -c for e, c in cof.items()}
                q = mul(si, cof)
                col = i * 16 + a * 4 + b
                for e, c in q.items(): J[idx[e]][col] = c
    return J


def rank_mod(J, p):
    m, n = len(J), len(J[0])
    return nmod_mat(m, n, [v % p for row in J for v in row], p).rank()


if __name__ == '__main__':
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 20260908
    rnd = random.Random(seed)
    out = {}
    for name, signed in (('det_4', True), ('per_4', False)):
        ranks = []
        for trial in range(3):
            A = [[[rnd.randint(-40, 40) for _ in range(4)] for _ in range(4)] for _ in range(R)]
            J = jacobian(A, signed)
            ranks.append((rank_mod(J, P1), rank_mod(J, P2)))
        out[name] = ranks
        print(f"{name}: Jacobian ranks (P1, P2) at 3 random integer points: {ranks}  [70 = dim Sym^4 C^5; 16r-30 = {16*R-30}]")
    dom = max(max(r) for r in out['per_4']) == 70
    print("per_4 pencils DOMINANT in Sym^4 C^5 (rank_p = 70 => rank_Q = 70 => I(Per_5) = 0, i_per4 = 0 is a theorem)" if dom
          else "per_4 pencils NOT dominant: Per_5 is a proper subvariety, i_per4 is a genuine third column")
    import json
    json.dump(dict(seed=seed, ranks=out, per4_dominant=dom, dim_D5_control=max(max(r) for r in out['det_4'])),
              open(os.path.join(HERE, '..', 'results', 's71_per4_dominance.json'), 'w'), indent=1)
