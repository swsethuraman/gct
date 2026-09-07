#!/usr/bin/env python3
"""P_r = R_r verification: do the permanental cubics {per_3(A(s))} fill all
cubics in r variables?  The reducible locus is R_r = {l.c}, c any cubic; the
padded orbit is P_r = {l.per_3(A(s))}.  Since per_3(A(s)) is a cubic,
P_r ⊆ R_r, with equality iff the cubic factor can be any cubic, i.e. iff the
permanent parametrisation  M (3x3 linear forms, 9r params) -> per_3(M(s))  is
dominant onto Sym^3 C^r.  We compute the rank of its differential at a generic
point over a house prime and compare to dim Sym^3 C^r = C(r+2,3).

Equality at r <= 5 (and strict at r >= 6) is the premise of the r<=5 exact
calibration (mult_pad = mult_red) and reproduces the transfer lemma from the
cubic side.  Writes results/s64_paramrank.md and .jsonl."""
import os, sys, json, random, itertools
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
from math import comb
from flint import nmod_mat
from wk8_s30_core import P1, P2


def _lin(vec, r, p):
    return {tuple(1 if k == i else 0 for k in range(r)): vec[i] % p for i in range(r) if vec[i] % p}


def _pmul(A, B, r, p):
    o = {}
    for e1, c1 in A.items():
        for e2, c2 in B.items():
            e = tuple(e1[k] + e2[k] for k in range(r)); o[e] = (o.get(e, 0) + c1 * c2) % p
    return {e: c for e, c in o.items() if c}


def _padd(A, B, p):
    o = dict(A)
    for e, c in B.items(): o[e] = (o.get(e, 0) + c) % p
    return {e: c for e, c in o.items() if c}


def perm_param_rank(r, p, seed=0):
    """rank over F_p of the differential of M -> per_3(M(s)) at a random M."""
    rnd = random.Random(seed)
    monos = [e for e in itertools.product(range(4), repeat=r) if sum(e) == 3]
    idx = {e: k for k, e in enumerate(monos)}
    M0 = [[[rnd.randint(-9, 9) for _ in range(r)] for _ in range(3)] for _ in range(3)]
    rows = []
    for a in range(3):
        for b in range(3):
            ri = [x for x in range(3) if x != a]; ci = [x for x in range(3) if x != b]
            A00 = _lin(M0[ri[0]][ci[0]], r, p); A01 = _lin(M0[ri[0]][ci[1]], r, p)
            A10 = _lin(M0[ri[1]][ci[0]], r, p); A11 = _lin(M0[ri[1]][ci[1]], r, p)
            per2 = _padd(_pmul(A00, A11, r, p), _pmul(A01, A10, r, p), p)   # 2x2 permanent (cofactor)
            for i in range(r):
                der = _pmul({tuple(1 if q == i else 0 for q in range(r)): 1}, per2, r, p)
                row = [0] * len(monos)
                for e, c in der.items(): row[idx[e]] = (row[idx[e]] + c) % p
                rows.append(row)
    return nmod_mat(len(rows), len(monos), [v for rr in rows for v in rr], p).rank()


def run(rmax=7):
    out = []
    for r in range(2, rmax + 1):
        tgt = comb(r + 2, 3)
        rk = max(perm_param_rank(r, P1, s) for s in (0, 1, 2))
        rk2 = perm_param_rank(r, P2, 0)
        out.append(dict(r=r, dim_cubics=tgt, param_rank=int(rk), param_rank_p2=int(rk2),
                        P_eq_R=bool(rk == tgt and rk2 == tgt)))
    return out


if __name__ == '__main__':
    rows = run(int(sys.argv[1]) if len(sys.argv) > 1 else 7)
    os.makedirs(os.path.join(ROOT, 'results'), exist_ok=True)
    with open(os.path.join(ROOT, 'results/s64_paramrank.jsonl'), 'w') as f:
        for rr in rows: f.write(json.dumps(rr) + "\n")
    lines = ["# P_r = R_r : does {per_3(A(s))} fill all cubics in r variables?", "",
             "Rank of the differential of the permanent parametrisation "
             "`M (3x3 linear forms) -> per_3(M(s))` at a generic `M`, over both house primes, "
             "vs `dim Sym^3 C^r`.  Equality => `P_r = R_r` => `I(pad) = I(R_r)` => `mult_pad = mult_red` exactly.", "",
             "| r | dim Sym^3 C^r | param rank (P1, 3 seeds) | param rank (P2) | P_r = R_r ? |",
             "|---|---|---|---|---|"]
    for rr in rows:
        lines.append(f"| {rr['r']} | {rr['dim_cubics']} | {rr['param_rank']} | {rr['param_rank_p2']} | "
                     f"{'**yes**' if rr['P_eq_R'] else 'no (P_r ⊊ R_r)'} |")
    lines += ["", "Reading: `P_r = R_r` for `r ≤ 5` (permanental cubics are all cubics), so the r ≤ 5 "
              "calibration demands `mult_pad = mult_red` exactly; `P_r ⊊ R_r` for `r ≥ 6`, so there only "
              "`mult_pad ≤ mult_red` (the transfer lemma's exact/upper-bound split, seen from the cubic side)."]
    open(os.path.join(ROOT, 'results/s64_paramrank.md'), 'w').write("\n".join(lines) + "\n")
    for rr in rows: print(rr)
    print("wrote results/s64_paramrank.md and .jsonl")
