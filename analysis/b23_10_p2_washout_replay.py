"""B23-10 pilot 2 — independent replay of washout_lemma.md Theorem 2's premise (lineage gap G-15 item).

Phi_r : M_3^r -> Sym^3 C^r, (A_i) |-> per_3(sum_i s_i A_i).  By the record's Lemma 1 (one point of full
Jacobian rank proves dominance; a full rank mod p at an integer point is a full rank over Q), the
theorem needs rank dPhi_5 = 35 at one point.  Replayed here at a fresh random integer point, with code
written here (no project imports), mod two primes, for r = 2..6 (expected 4, 10, 20, 35, 50; the r = 6
value is only a floor).  Also: the census table of Paper 1 Prop. 4.1 at m = 9, D = 3 (arithmetic).
"""
import json
import random
import sys
from itertools import combinations_with_replacement, permutations
from math import comb
from pathlib import Path

PRIMES = [2147483647, 1000000007]
rng = random.Random(20260919)
out = {"pilot": "b23_10_p2_washout_replay", "seed": 20260919, "primes": PRIMES}


def monos(d, n):
    res = []
    for c in combinations_with_replacement(range(n), d):
        e = [0] * n
        for i in c:
            e[i] += 1
        res.append(tuple(e))
    return res


def mul(p, q):
    r = {}
    for a, x in p.items():
        for b, y in q.items():
            e = tuple(i + j for i, j in zip(a, b))
            r[e] = r.get(e, 0) + x * y
    return r


def add(p, q):
    r = dict(p)
    for e, v in q.items():
        r[e] = r.get(e, 0) + v
    return r


def rank_mod(rows, pm):
    A = [[x % pm for x in r] for r in rows]
    rk = 0
    for col in range(len(A[0])):
        piv = next((i for i in range(rk, len(A)) if A[i][col]), None)
        if piv is None:
            continue
        A[rk], A[piv] = A[piv], A[rk]
        inv = pow(A[rk][col], pm - 2, pm)
        for i in range(rk + 1, len(A)):
            if A[i][col]:
                f = A[i][col] * inv % pm
                A[i] = [(x - f * y) % pm for x, y in zip(A[i], A[rk])]
        rk += 1
    return rk


def perm_cofactor(M, j, k):
    """d per_3 / d M_{jk}: the permanent of the 2x2 minor deleting row j, column k (a quadric in s)."""
    rows = [a for a in range(3) if a != j]
    cols = [b for b in range(3) if b != k]
    t1 = mul(M[rows[0]][cols[0]], M[rows[1]][cols[1]])
    t2 = mul(M[rows[0]][cols[1]], M[rows[1]][cols[0]])
    return add(t1, t2)


res = {}
for r in range(2, 7):
    A = [[[rng.randint(-10**6, 10**6) for _ in range(3)] for _ in range(3)] for _ in range(r)]
    # M(s)_{jk} = sum_i s_i A_i[j][k], linear forms in r variables
    M = [[{tuple(1 if t == i else 0 for t in range(r)): A[i][j][k] for i in range(r) if A[i][j][k]}
          for k in range(3)] for j in range(3)]
    basis = monos(3, r)
    cols = []
    for i in range(r):
        si = {tuple(1 if t == i else 0 for t in range(r)): 1}
        for j in range(3):
            for k in range(3):
                d = mul(si, perm_cofactor(M, j, k))
                cols.append([d.get(e, 0) for e in basis])
    J = [list(x) for x in zip(*cols)]
    res[r] = {"rank_mod": [rank_mod(J, p) for p in PRIMES], "dim_Sym3": comb(r + 2, 3), "params": 9 * r}
out["jacobian_ranks"] = res
out["theorem2_premise_rank35_at_r5"] = all(x == 35 for x in res[5]["rank_mod"])
out["dominant_r_le_5"] = all(all(x == res[r]["dim_Sym3"] for x in res[r]["rank_mod"]) for r in range(2, 6))
out["r6_floor_50"] = res[6]["rank_mod"]

# Paper 1 Prop. 4.1 census at (m, D) = (9, 3): first delta (multiple of 3) with delta <= C(delta/3, 3)
census = [(d, d // 3, comb(d // 3, 3), d <= comb(d // 3, 3)) for d in range(3, 22, 3)]
out["census_table_m9_D3"] = census
out["census_first_admitted_delta"] = next(d for d, k, c, ok in census if ok)
Path(sys.argv[1]).write_text(json.dumps(out, indent=1) + "\n")
print(json.dumps(out, indent=1))
