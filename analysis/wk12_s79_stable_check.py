#!/usr/bin/env python3
"""
Session 79 -- independent checker for the stable-block records of wk12_s79_stable.py.

Reads results/s79_stable/stable_<rho>.json and re-derives every claim with none
of the engine's code:

  1. the weight space is re-enumerated (its own recursion) and compared with the
     recorded monomial list, as a set;
  2. a_inf is recomputed by the Weyl alternation over S_5 with its own multiset
     counter (no wk9_s57_stable);
  3. the four raising operators are rebuilt from the derivation rule
     E y_(d,a) = (a_i + 1) y_(d, a + e_i - e_{i+1}) with its own dictionary
     arithmetic, and E v = 0 mod p is checked for every recorded kernel vector
     at each prime; the vectors are checked independent (rank a_inf mod p by a
     hand-written elimination);
  4. the generator values at every recorded pencil are recomputed from the
     Leibniz expansion of det(t I - A(s)) over the 24 permutations (not the
     power-sum route of the engine), and the evaluation matrix G is rebuilt and
     compared entry by entry with the record; its rank mod p is recomputed by
     the hand-written elimination;
  5. the covariance check is re-run on the recomputed values;
  6. the verdict is recomputed from (2)-(4) and compared with the record.

usage: python3 analysis/wk12_s79_stable_check.py results/s79_stable/stable_5_3_2_2_1.json [...]
"""
import itertools, json, random, sys

NV, N = 5, 4


def monos(d):
    return [a for a in itertools.product(range(d + 1), repeat=NV) if sum(a) == d]


GENS = [(d, a) for d in (2, 3, 4) for a in monos(d)]
GIDX = {g: i for i, g in enumerate(GENS)}


def count_weight(w):
    """number of multisets of generators with exponent sum w (its own DP)."""
    from functools import lru_cache
    n = len(GENS)

    @lru_cache(maxsize=None)
    def rec(start, rem):
        if all(x == 0 for x in rem): return 1
        if sum(rem) < 2: return 0
        tot = 0
        for gi in range(start, n):
            d, a = GENS[gi]
            if d > sum(rem): continue
            if all(a[k] <= rem[k] for k in range(NV)):
                tot += rec(gi, tuple(rem[k] - a[k] for k in range(NV)))
        return tot
    return rec(0, tuple(w))


def enumerate_weight(w):
    out = []; n = len(GENS)

    def rec(start, rem, cur):
        if all(x == 0 for x in rem):
            out.append(tuple(cur)); return
        if sum(rem) < 2: return
        for gi in range(start, n):
            d, a = GENS[gi]
            if d > sum(rem): continue
            if all(a[k] <= rem[k] for k in range(NV)):
                rec(gi, tuple(rem[k] - a[k] for k in range(NV)), cur + [gi])
    rec(0, tuple(w), [])
    return out


def a_inf_weyl(rho):
    """sum over w in S_5 of sgn(w) K(w(rho + delta) - delta), delta = (4,3,2,1,0)."""
    delta = tuple(range(NV - 1, -1, -1))
    tot = 0
    for perm in itertools.permutations(range(NV)):
        sgn = 1
        for i in range(NV):
            for j in range(i + 1, NV):
                if perm[i] > perm[j]: sgn = -sgn
        v = tuple(rho[perm[i]] + delta[perm[i]] - delta[i] for i in range(NV))
        if min(v) < 0: continue
        tot += sgn * count_weight(v)
    return tot


def raising_apply(vec_dict, i):
    """apply E_{i,i+1} to a polynomial given as {monomial tuple: coeff}."""
    out = {}
    for m, c in vec_dict.items():
        for pos in range(len(m)):
            d, a = GENS[m[pos]]
            if a[i + 1] == 0: continue
            na = list(a); na[i] += 1; na[i + 1] -= 1
            nm = tuple(sorted(m[:pos] + m[pos + 1:] + (GIDX[(d, tuple(na))],)))
            out[nm] = out.get(nm, 0) + c * (a[i] + 1)
    return out


def rank_mod(rows, p):
    """rank of a list of integer rows mod p by elimination (hand-written)."""
    M = [[x % p for x in r] for r in rows]
    rank = 0; ncol = len(M[0]) if M else 0
    for col in range(ncol):
        piv = next((r for r in range(rank, len(M)) if M[r][col]), None)
        if piv is None: continue
        M[rank], M[piv] = M[piv], M[rank]
        inv = pow(M[rank][col], p - 2, p)
        M[rank] = [(x * inv) % p for x in M[rank]]
        for r in range(len(M)):
            if r != rank and M[r][col]:
                f = M[r][col]
                M[r] = [(x - f * y) % p for x, y in zip(M[r], M[rank])]
        rank += 1
    return rank


# ---- the point map, by Leibniz expansion of det(tI - A(s)) in Z[t, s_1..s_5]
def poly_mul(f, g):
    out = {}
    for e1, c1 in f.items():
        for e2, c2 in g.items():
            e = tuple(x + y for x, y in zip(e1, e2)); out[e] = out.get(e, 0) + c1 * c2
    return {e: c for e, c in out.items() if c}


def point_values_leibniz(As):
    """generator values (integers) from det(t I - A(s)), A(s) = sum_k s_k A_k; exponent
    tuples are (t, s_1..s_5); the degree-d generator y_(d,a) is the coefficient of t^{4-d} s^a."""
    ent = {}
    for i in range(N):
        for j in range(N):
            f = {}
            if i == j: f[(1,) + (0,) * NV] = 1
            for k in range(NV):
                v = -As[k][i][j]
                if v: f[(0,) + tuple(1 if q == k else 0 for q in range(NV))] = v
            ent[(i, j)] = f
    det = {}
    for perm in itertools.permutations(range(N)):
        sgn = 1
        for i in range(N):
            for j in range(i + 1, N):
                if perm[i] > perm[j]: sgn = -sgn
        term = {(0,) * (NV + 1): sgn}
        for i in range(N): term = poly_mul(term, ent[(i, perm[i])])
        for e, c in term.items(): det[e] = det.get(e, 0) + c
    assert all(c == 0 for e, c in det.items() if e[0] == 3), "trace not zero"
    return [det.get((4 - d,) + tuple(a), 0) for (d, a) in GENS]


def evaluate(monomials, vec, yv, p):
    tot = 0
    for m, c in zip(monomials, vec):
        if not c: continue
        t = c
        for gi in m:
            t = t * yv[gi] % p
            if not t: break
        tot += t
    return tot % p


def check(path):
    rec = json.load(open(path))
    rho = tuple(rec['rho']); a_rec = rec['a_inf']
    ok = True
    print(f"== {path}: rho = {rho}, recorded a_inf = {a_rec}, status: {rec['status']}")
    # 1. weight space
    mine = enumerate_weight(rho); rec_mon = [tuple(m) for m in rec['monomials']]
    same = set(mine) == set(rec_mon) and len(mine) == len(rec_mon)
    print(f"  [1] weight space: {len(mine)} monomials, matches record as a set: {same}"); ok &= same
    # 2. a_inf
    a_mine = a_inf_weyl(rho)
    print(f"  [2] a_inf by own Weyl alternation: {a_mine} (record {a_rec}): {a_mine == a_rec}"); ok &= (a_mine == a_rec)
    pts = rec['points']
    for p_str, pr in rec['per_prime'].items():
        p = int(p_str)
        if 'kernel' not in pr:
            print(f"  [p={p}] no kernel recorded ({pr.get('status')})"); ok = False; continue
        K = pr['kernel']
        # 3. raising operators and independence
        killed = True
        for v in K:
            vd = {m: c for m, c in zip(rec_mon, v) if c}
            for i in range(NV - 1):
                img = raising_apply(vd, i)
                if any(c % p for c in img.values()): killed = False
        rk = rank_mod(K, p)
        print(f"  [3] p={p}: {len(K)} kernel vectors killed by all four raisings mod p: {killed}; rank mod p = {rk} (a_inf {a_mine}): {rk == a_mine}")
        ok &= killed and rk == a_mine and len(K) == a_mine
        # 4. evaluation matrix by the Leibniz point map
        G = []
        for As in pts:
            yv = [x % p for x in point_values_leibniz(As)]
            G.append([evaluate(rec_mon, v, yv, p) for v in K])
        same = (G == pr['G'])
        rG = rank_mod(G, p)
        print(f"  [4] p={p}: G ({len(G)} x {len(K)}) recomputed from det(tI - A(s)) by Leibniz: matches record entry by entry: {same}; rank {rG} (record mult {pr['mult_det_inf']}): {rG == pr['mult_det_inf']}")
        ok &= same and rG == pr['mult_det_inf']
        # 5. covariance on recomputed values
        Acov = pr['covariance']; seedA = Acov['pencil_seed']
        rnd = random.Random(seedA); bound = rec['point_bound']
        A0 = []
        for _ in range(NV):
            M = [[rnd.randint(-bound, bound) for _ in range(N)] for _ in range(N)]
            s = sum(M[i][i] for i in range(N - 1)); M[N - 1][N - 1] = -s; A0.append(M)
        base = [evaluate(rec_mon, v, [x % p for x in point_values_leibniz(A0)], p) for v in K]
        cov_ok = True
        for i in range(NV - 1):
            for eps in Acov['eps']:
                B = [[list(r) for r in M] for M in A0]
                for r in range(N):
                    for c in range(N): B[i + 1][r][c] += eps * A0[i][r][c]
                val = [evaluate(rec_mon, v, [x % p for x in point_values_leibniz(B)], p) for v in K]
                if val != base: cov_ok = False
        print(f"  [5] p={p}: covariance (A_{{i+1}} -> A_{{i+1}} + eps A_i, 4 raisings, eps {Acov['eps']}) on recomputed values: {'PASS' if cov_ok else 'FAIL'} (record {'PASS' if Acov['all_pass'] else 'FAIL'})")
        ok &= cov_ok and Acov['all_pass']
    verdict = 'i_det^inf = 0 (PROVED: full rank)' if all(int(pr.get('mult_det_inf', -1)) == a_mine for pr in rec['per_prime'].values()) else 'not full rank'
    print(f"  [6] verdict recomputed: {verdict}; record i_det_inf = {rec['i_det_inf']}")
    print(f"  ==> {'ALL CHECKS PASS' if ok else 'CHECK FAILED'}")
    return ok


if __name__ == '__main__':
    res = [check(pth) for pth in sys.argv[1:]]
    sys.exit(0 if all(res) else 1)
