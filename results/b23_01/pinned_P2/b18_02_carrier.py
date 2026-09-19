"""B18-02 carrier control: full-stabilizer invariants of det4 in the row model.

For a partition lambda of N = 4d with at most five rows this script
  1. computes s = [S^lambda : Sym^2 S^(d^4)] and g = [S^lambda : S^R (x) S^R]
     by Murnaghan-Nakayama characters (formula (3.1) of the report);
  2. builds the spanning polynomials P_{pi,rho} + P_{rho,pi} of Proposition 2.2
     as tensor-network contractions evaluated at random points modulo a prime;
  3. certifies a basis of M_lambda by a modular rank equal to s;
  4. certifies a rank floor b for the forbidden projection C via the
     skew-degree cut of Lemma 4.1 (u-interpolation, 3d+1 nodes);
  5. checks Lemma 4.1 numerically by a full Laurent interpolation in t
     (8d+1 nodes) on one cell;
  6. records timings and intermediate sizes for the price model.

Exact arithmetic modulo P = 2^19 - 1 with int64 numpy; every pairwise
contraction sums at most 4^12 products below P^2, so no overflow.
Only standard library, numpy and sympy.isprime are used.
"""
import itertools
import json
import os
import random
import sys
import time
from functools import lru_cache
from math import factorial

import numpy as np
from sympy import isprime

P = 524269  # B23-01 second prime 2**19 - 19
assert isprime(P)
MAX_SUM_LEGS = 12  # 4**12 * P**2 < 2**63


# ---------------------------------------------------------------- characters
def partitions(n, maxpart=None):
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def z_eta(eta):
    z = 1
    for part in set(eta):
        m = eta.count(part)
        z *= part ** m * factorial(m)
    return z


def square_type(eta):
    out = []
    for L in eta:
        if L % 2 == 1:
            out.append(L)
        else:
            out += [L // 2, L // 2]
    return tuple(sorted(out, reverse=True))


@lru_cache(maxsize=None)
def chi(lam, eta):
    """Murnaghan-Nakayama via beta-sets. lam, eta tuples (eta any order)."""
    if not eta:
        return 1 if sum(lam) == 0 else 0
    k = eta[0]
    rest = eta[1:]
    n = len(lam)
    beta = [lam[i] + (n - 1 - i) for i in range(n)]
    bset = set(beta)
    total = 0
    for idx, b in enumerate(beta):
        nb = b - k
        if nb < 0 or nb in bset:
            continue
        height = sum(1 for x in beta if nb < x < b)
        newbeta = sorted([x for x in beta if x != b] + [nb], reverse=True)
        newlam = tuple(newbeta[i] - (n - 1 - i) for i in range(n))
        newlam = tuple(x for x in newlam if x > 0)
        total += (-1) ** height * chi(newlam, rest)
    return total


def s_and_g(lam, d):
    N = 4 * d
    R = (d,) * 4
    s2 = 0  # 2*s as rational
    g2 = 0
    from fractions import Fraction
    s2 = Fraction(0)
    g = Fraction(0)
    for eta in partitions(N):
        cl = chi(lam, eta)
        cr = chi(R, eta)
        cr2 = chi(R, square_type(eta))
        z = z_eta(eta)
        g += Fraction(cl * cr * cr, z)
        s2 += Fraction(cl * (cr * cr + cr2), z)
    s = s2 / 2
    assert s.denominator == 1 and g.denominator == 1
    return int(s), int(g)


# ------------------------------------------------------------ tensor network
def levi_civita4():
    e = np.zeros((4, 4, 4, 4), dtype=np.int64)
    for perm in itertools.permutations(range(4)):
        sgn = 1
        pl = list(perm)
        for i in range(4):
            for j in range(i + 1, 4):
                if pl[i] > pl[j]:
                    sgn = -sgn
        e[perm] = sgn
    return e % P


EPS4 = levi_civita4()


def perm_sign(perm):
    sgn = 1
    pl = list(perm)
    for i in range(len(pl)):
        for j in range(i + 1, len(pl)):
            if pl[i] > pl[j]:
                sgn = -sgn
    return sgn


def column_tensor(Yrows, h):
    """D[c_1,...,c_h] = det[ Y_i[c_k] ]_{i,k}, each c a 16-index, mod P.
    Laplace expansion along the first slot with memoisation over row subsets;
    cost about h * 16^h element operations. Returned with shape (16,)*h."""
    mats = [Yrows[i].reshape(16) % P for i in range(h)]
    memo = {}

    def D(rows):
        if rows in memo:
            return memo[rows]
        if len(rows) == 1:
            memo[rows] = mats[rows[0]].copy()
            return memo[rows]
        acc = np.zeros((16,) * len(rows), dtype=np.int64)
        for idx, i in enumerate(rows):
            sub = D(rows[:idx] + rows[idx + 1:])
            term = np.multiply.outer(mats[i], sub) % P
            if idx % 2 == 0:
                acc += term
            else:
                acc -= term
            acc %= P
        memo[rows] = acc
        return acc

    return D(tuple(range(h)))


MAX_INTERMEDIATE = 4 ** 12  # 16.7M entries = 128 MiB of int64; guard for 512 MiB cap


class ContractionTooLarge(Exception):
    pass


class Net:
    """List of (array, index-labels) contracted greedily modulo P."""

    def __init__(self):
        self.tensors = []
        self.max_intermediate = 0
        self.flops = 0

    def add(self, arr, labels):
        self.tensors.append((arr, list(labels)))

    @staticmethod
    def _pair_cost(l1, l2):
        shared = set(l1) & set(l2)
        out = [x for x in l1 if x not in shared] + [x for x in l2 if x not in shared]
        return 4 ** len(out), shared, out

    def contract_pair(self, t1, t2):
        a1, l1 = t1
        a2, l2 = t2
        shared = [x for x in l1 if x in set(l2)]
        keep = [x for x in l1 if x not in shared] + [x for x in l2 if x not in shared]
        # sum over at most MAX_SUM_LEGS shared legs per einsum; keep the rest
        # as batch legs and sum them afterwards in chunks.
        summed = shared[:MAX_SUM_LEGS]
        batch = shared[MAX_SUM_LEGS:]
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lab = {}
        for x in l1 + l2:
            if x not in lab:
                lab[x] = alphabet[len(lab)]
        s1 = "".join(lab[x] for x in l1)
        s2 = "".join(lab[x] for x in l2)
        outlabels = keep + batch
        so = "".join(lab[x] for x in outlabels)
        res = np.einsum(s1 + "," + s2 + "->" + so, a1, a2) % P
        self.flops += 4 ** (len(set(l1) | set(l2)))
        while batch:
            chunk = batch[:MAX_SUM_LEGS]
            batch = batch[MAX_SUM_LEGS:]
            axes = tuple(outlabels.index(x) for x in chunk)
            res = res.sum(axis=axes) % P
            outlabels = [x for x in outlabels if x not in chunk]
        self.max_intermediate = max(self.max_intermediate, res.size)
        return (res, outlabels)

    @staticmethod
    def plan(label_lists):
        """Greedy contraction plan on index labels only (no arrays).
        Returns (steps, max_intermediate_entries, flop_units) where a step is
        (i, j, out_labels) and flop_units = sum over steps of 4^(#legs of union)."""
        ts = [list(l) for l in label_lists]
        steps = []
        maxint = 1
        flops = 0
        while len(ts) > 1:
            best = None
            for i in range(len(ts)):
                for j in range(i + 1, len(ts)):
                    cost, shared, out = Net._pair_cost(ts[i], ts[j])
                    if not shared:
                        continue
                    if best is None or cost < best[0]:
                        best = (cost, i, j, out)
            if best is None:
                order = sorted(range(len(ts)), key=lambda k: len(ts[k]))
                i, j = sorted(order[:2])
                out = ts[i] + ts[j]
            else:
                _, i, j, out = best
            flops += 4 ** len(set(ts[i]) | set(ts[j]))
            maxint = max(maxint, 4 ** len(out))
            steps.append((i, j, out))
            ts = [t for k, t in enumerate(ts) if k not in (i, j)] + [out]
        return steps, maxint, flops

    def run(self):
        steps, maxint, flops = self.plan([t[1] for t in self.tensors])
        if maxint > MAX_INTERMEDIATE:
            raise ContractionTooLarge(maxint)
        ts = self.tensors
        for i, j, _ in steps:
            new = self.contract_pair(ts[i], ts[j])
            ts = [t for k, t in enumerate(ts) if k not in (i, j)] + [new]
        arr, labels = ts[0]
        assert labels == []
        return int(arr) % P


def evaluate_pair(pi, rho, coltensors, slot_col, slot_pos):
    """P_{pi,rho}(Y) from precomputed column tensors (one per column)."""
    net = Net()
    for j, D in enumerate(coltensors):
        h = D.ndim
        # reshape each 16-leg into (a,b) legs of dim 4
        arr = D.reshape((4, 4) * h)
        labels = []
        for k in range(h):
            slot = (j, k)
            labels += [("a", slot), ("b", slot)]
        net.add(arr, labels)
    for block in pi:
        net.add(EPS4, [("a", slot) for slot in block])
    for block in rho:
        net.add(EPS4, [("b", slot) for slot in block])
    val = net.run()
    return val, net.max_intermediate, net.flops


def random_block_partition(slots, rng):
    s = list(slots)
    rng.shuffle(s)
    return [tuple(s[4 * i:4 * i + 4]) for i in range(len(s) // 4)]


# --------------------------------------------------------- adapted coordinates
def adapted_scale_u(Y, u):
    """Scale only the skew part of the 3x3 block of each Y_i by u (mod P)."""
    Z = Y.copy() % P
    E = Z[:, 1:, 1:]
    inv2 = pow(2, P - 2, P)
    S = ((E + np.swapaxes(E, 1, 2)) * inv2) % P
    K = ((E - np.swapaxes(E, 1, 2)) * inv2) % P
    Z[:, 1:, 1:] = (S + (u % P) * K) % P
    return Z


def adapted_gamma_t(Y, t):
    """Y gamma(t): row-1 entries * t^-1, column-1 entries (rows 2-4) * t,
    block -> t*Sym + Skew."""
    Z = Y.copy() % P
    tinv = pow(t % P, P - 2, P)
    Z[:, 0, :] = (Z[:, 0, :] * tinv) % P
    Z[:, 1:, 0] = (Z[:, 1:, 0] * (t % P)) % P
    E = Y[:, 1:, 1:] % P
    inv2 = pow(2, P - 2, P)
    S = ((E + np.swapaxes(E, 1, 2)) * inv2) % P
    K = ((E - np.swapaxes(E, 1, 2)) * inv2) % P
    Z[:, 1:, 1:] = ((t % P) * S + K) % P
    return Z


# ------------------------------------------------------------- modular algebra
def rank_mod(M):
    M = [[int(x) % P for x in row] for row in M]
    rows, cols = len(M), (len(M[0]) if M else 0)
    r = 0
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if M[i][c]:
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = pow(M[r][c], P - 2, P)
        M[r] = [(x * inv) % P for x in M[r]]
        for i in range(rows):
            if i != r and M[i][c]:
                f = M[i][c]
                M[i] = [(x - f * y) % P for x, y in zip(M[i], M[r])]
        r += 1
        if r == rows:
            break
    return r


def solve_vandermonde(nodes, values, degrees):
    """Coefficients c_e (e in degrees) with sum_e c_e node^e = value, mod P."""
    n = len(nodes)
    assert n == len(degrees)
    A = [[pow(x, e, P) for e in degrees] + [v % P] for x, v in zip(nodes, values)]
    # Gauss-Jordan
    for c in range(n):
        piv = next(i for i in range(c, n) if A[i][c])
        A[c], A[piv] = A[piv], A[c]
        inv = pow(A[c][c], P - 2, P)
        A[c] = [(x * inv) % P for x in A[c]]
        for i in range(n):
            if i != c and A[i][c]:
                f = A[i][c]
                A[i] = [(x - f * y) % P for x, y in zip(A[i], A[c])]
    return [A[i][n] for i in range(n)]


# ------------------------------------------------------ ambient multiplicity a
def ambient_a(lam, d):
    """a = [S_lambda : Sym^d(Sym^4)] for length(lambda) <= 5 and d <= 3, by the
    alternating weight-space formula in m = length(lambda) variables.
    Returns None (unknown) outside that range."""
    if d > 3:
        return None
    m = len(lam)
    monos = [mu for mu in itertools.product(range(5), repeat=m) if sum(mu) == 4]
    from collections import Counter
    wt = Counter()
    for combo in itertools.combinations_with_replacement(range(len(monos)), d):
        tot = tuple(sum(monos[i][k] for i in combo) for k in range(m))
        wt[tot] += 1
    rho = tuple(range(m - 1, -1, -1))
    total = 0
    for w in itertools.permutations(range(m)):
        sgn = perm_sign(w)
        wrho = tuple(rho[w[k]] for k in range(m))
        mu = tuple(lam[k] + rho[k] - wrho[k] for k in range(m))
        if min(mu) < 0:
            continue
        total += sgn * wt.get(mu, 0)
    return total


# ------------------------------------------------------------------ pricing
def local_pairs(slots, shift):
    """Blocks of four consecutive slots in column-major order; rho is the same
    with the cyclic order shifted by `shift` slots (keeps the network local)."""
    n = len(slots)
    pi = [tuple(slots[4 * i:4 * i + 4]) for i in range(n // 4)]
    rot = slots[shift:] + slots[:shift]
    rho = [tuple(rot[4 * i:4 * i + 4]) for i in range(n // 4)]
    return pi, rho


def plan_only(lam, d, rng, trials=8):
    heights = conjugate(lam)
    slots = [(j, k) for j, h in enumerate(heights) for k in range(h)]
    label_lists_base = []
    for j, h in enumerate(heights):
        labels = []
        for k in range(h):
            labels += [("a", (j, k)), ("b", (j, k))]
        label_lists_base.append(labels)

    def cost(pi, rho):
        ll = list(label_lists_base)
        ll += [[("a", sl) for sl in b] for b in pi]
        ll += [[("b", sl) for sl in b] for b in rho]
        _, maxint, flops = Net.plan(ll)
        return maxint, flops

    rand = [cost(random_block_partition(slots, rng), random_block_partition(slots, rng))
            for _ in range(trials)]
    loc = [cost(*local_pairs(slots, sh)) for sh in (1, 2, 3)]
    from math import comb
    dense = 1
    for part in lam:
        dense *= comb(part + 15, 15)
    colfact = 1
    for h in heights:
        colfact *= factorial(h)
    return {
        "lambda": list(lam), "d": d, "heights": list(heights),
        "column_tensor_entries": [16 ** h for h in heights],
        "random_pairs_max_intermediate": [c[0] for c in rand],
        "random_pairs_flop_units": [c[1] for c in rand],
        "local_pairs_max_intermediate": [c[0] for c in loc],
        "local_pairs_flop_units": [c[1] for c in loc],
        "dense_monomial_count_multidegree_lambda": dense,
        "raw_expansion_terms_per_contraction": (24 ** (2 * d)) * colfact,
        "u_nodes_per_point": 3 * d + 1,
    }


# --------------------------------------------------------------------- driver
def conjugate(lam):
    return tuple(sum(1 for x in lam if x > j) for j in range(lam[0]))


def run_cell(lam, d, rng, n_points, max_pairs, budget_s, do_t_check=False):
    N = 4 * d
    assert sum(lam) == N
    m = len(lam)
    heights = conjugate(lam)
    slots = [(j, k) for j, h in enumerate(heights) for k in range(h)]
    slot_col = {sl: sl[0] for sl in slots}
    slot_pos = {sl: sl[1] for sl in slots}
    s, g = s_and_g(tuple(lam), d)
    a = ambient_a(tuple(lam), d)
    out = {"lambda": list(lam), "d": d, "s": s, "g": g, "a": a, "heights": list(heights)}
    t0 = time.perf_counter()
    if s == 0:
        # still build a few pairs to check they vanish identically at points
        pts = [rng.integers(0, P, size=(m, 4, 4)).astype(np.int64) for _ in range(2)]
        cols = [[column_tensor(Y, h) for h in heights] for Y in pts]
        vals = []
        for _ in range(3):
            pi = random_block_partition(slots, rng)
            rho = random_block_partition(slots, rng)
            for ct in cols:
                v1, _, _ = evaluate_pair(pi, rho, ct, slot_col, slot_pos)
                v2, _, _ = evaluate_pair(rho, pi, ct, slot_col, slot_pos)
                vals.append((v1 + v2) % P)
        out["zero_check_values"] = vals
        out["all_symmetrised_values_zero"] = all(v == 0 for v in vals)
        out["wall_s"] = time.perf_counter() - t0
        return out
    unodes = list(range(1, 3 * d + 2))  # 3d+1 nodes, all nonzero mod P
    udeg = list(range(0, 3 * d + 1))
    forb = list(range(2 * d + 1, 3 * d + 1))
    pts = [rng.integers(0, P, size=(m, 4, 4)).astype(np.int64) for _ in range(n_points)]
    tc0 = time.perf_counter()
    coltensors = {}
    for ip, Y in enumerate(pts):
        for u in unodes:
            coltensors[(ip, u)] = [column_tensor(adapted_scale_u(Y, u), h) for h in heights]
    out["column_tensor_wall_s"] = time.perf_counter() - tc0
    plain_rows = []   # rows: (point) ; columns: pairs      (u = 1 values)
    forb_rows = []    # rows: (point, forbidden degree)
    pair_list = []
    evals = 0
    ev_wall = 0.0
    maxint = 0
    flops = 0
    plain_rank = 0
    for npair in range(max_pairs):
        pi = random_block_partition(slots, rng)
        rho = random_block_partition(slots, rng)
        pair_list.append((pi, rho))
        col_plain = []
        col_forb = []
        for ip in range(n_points):
            vals_u = []
            for u in unodes:
                te = time.perf_counter()
                v1, mi1, f1 = evaluate_pair(pi, rho, coltensors[(ip, u)], slot_col, slot_pos)
                v2, mi2, f2 = evaluate_pair(rho, pi, coltensors[(ip, u)], slot_col, slot_pos)
                ev_wall += time.perf_counter() - te
                evals += 2
                maxint = max(maxint, mi1, mi2)
                flops += f1 + f2
                vals_u.append((v1 + v2) % P)
            coeffs = solve_vandermonde(unodes, vals_u, udeg)
            col_plain.append(vals_u[0])  # u = 1
            col_forb += [coeffs[e] for e in forb]
        plain_rows.append(col_plain)
        forb_rows.append(col_forb)
        # matrices are stored pair-major; rank is transpose-invariant
        plain_rank = rank_mod(plain_rows)
        if plain_rank == s and npair + 1 >= s:
            break
        if time.perf_counter() - t0 > budget_s:
            break
    forb_rank = rank_mod(forb_rows) if forb_rows else 0
    out["certificate"] = {
        "prime": P,
        "points_standard_entries": [Y.tolist() for Y in pts],
        "pairs_slots_as_[column,position]": [
            [[list(sl) for sl in b] for b in pi] for pi, rho in pair_list],
        "pairs_rho": [[[list(sl) for sl in b] for b in rho] for pi, rho in pair_list],
        "u_nodes": unodes,
        "plain_matrix_pair_by_point_u1": plain_rows,
        "forbidden_matrix_pair_by_point_and_degree": forb_rows,
        "forbidden_degrees": forb,
    }
    out.update({
        "pairs_used": len(pair_list),
        "points": n_points,
        "u_nodes": len(unodes),
        "basis_rank_mod_P": plain_rank,
        "basis_certified": plain_rank == s,
        "forbidden_rank_floor_b": forb_rank,
        "evaluations": evals,
        "evaluation_wall_s": ev_wall,
        "wall_per_evaluation_s": ev_wall / max(evals, 1),
        "max_intermediate_entries": int(maxint),
        "flop_units_total": int(flops),
        "wall_s": time.perf_counter() - t0,
    })
    if do_t_check and pair_list:
        # Laurent check of Lemma 4.1 on a pair that is nonzero at the first point
        idx = next((i for i, row in enumerate(plain_rows) if row[0]), 0)
        out["laurent_check_pair_index"] = idx
        pi, rho = pair_list[idx]
        Y = pts[0]
        tnodes = list(range(2, 8 * d + 4))  # 8d+1 distinct nonzero nodes
        tnodes = tnodes[:8 * d + 1]
        vals = []
        for t in tnodes:
            ct = [column_tensor(adapted_gamma_t(Y, t), h) for h in heights]
            v1, _, _ = evaluate_pair(pi, rho, ct, slot_col, slot_pos)
            v2, _, _ = evaluate_pair(rho, pi, ct, slot_col, slot_pos)
            vals.append(((v1 + v2) * pow(t, 4 * d, P)) % P)  # multiply by t^{4d}
        degs = list(range(0, 8 * d + 1))
        co = solve_vandermonde(tnodes, vals, degs)
        laurent = {e - 4 * d: c for e, c in enumerate(co) if c}
        # compare with u-expansion at u-node set for the same point
        vals_u = []
        for u in unodes:
            ct = coltensors[(0, u)]
            v1, _, _ = evaluate_pair(pi, rho, ct, slot_col, slot_pos)
            v2, _, _ = evaluate_pair(rho, pi, ct, slot_col, slot_pos)
            vals_u.append((v1 + v2) % P)
        cu = solve_vandermonde(unodes, vals_u, udeg)
        weights_ok = all(-d <= k <= 2 * d for k in laurent)
        match = all(laurent.get(2 * d - j, 0) == cu[j] for j in range(3 * d + 1))
        out["laurent_support"] = sorted(laurent)
        out["laurent_within_[-d,2d]"] = weights_ok
        out["laurent_equals_skew_degree_expansion"] = match
    return out


def main():
    mode = sys.argv[1]
    rng = np.random.default_rng(20260915)
    random.seed(20260915)
    start = time.perf_counter()
    if mode == "price":
        outpath = sys.argv[2]
        cells = [tuple(int(x) for x in c.split(",")) for c in sys.argv[3].split(";")]
        res = []
        for lam in cells:
            d = sum(lam) // 4
            r = plan_only(lam, d, rng)
            res.append(r)
            print(json.dumps(r), flush=True)
        summary = {"mode": "price", "cells": res, "total_wall_s": time.perf_counter() - start}
    elif mode == "control":
        d = int(sys.argv[2])
        max_rows = int(sys.argv[3])
        budget = float(sys.argv[4])
        outpath = sys.argv[5]
        only = sys.argv[6] if len(sys.argv) > 6 else None
        cells = [lam for lam in partitions(4 * d) if len(lam) <= max_rows]
        if only:
            cells = [tuple(int(x) for x in c.split(",")) for c in only.split(";")]
        # characters first (cheap), evaluation afterwards, s>0 cells first
        table = []
        for lam in cells:
            s, g = s_and_g(tuple(lam), d)
            table.append((lam, s, g, ambient_a(tuple(lam), d)))
        print(json.dumps({"character_table": [[list(l), s, g, a] for l, s, g, a in table]}),
              flush=True)
        results = []
        first = True
        order = sorted(table, key=lambda r: (r[1] == 0, r[0][0] * -1))
        for lam, s, g, a in order:
            n_points = max(s + 2, 3)
            remaining = budget - (time.perf_counter() - start)
            if remaining < 5:
                results.append({"lambda": list(lam), "d": d, "s": s, "g": g, "a": a,
                                "status": "NOT REACHED (budget)"})
                continue
            try:
                res = run_cell(lam, d, rng, n_points=n_points, max_pairs=40 * s + 40,
                               budget_s=min(remaining - 3, 25.0),
                               do_t_check=(first and s > 0))
                res["status"] = "MEASURED"
            except ContractionTooLarge as exc:
                res = {"lambda": list(lam), "d": d, "s": s, "g": g, "a": a,
                       "status": f"NOT REACHED (intermediate {exc} entries exceeds guard)"}
            if first and s > 0 and res["status"] == "MEASURED":
                first = False
            results.append(res)
            print(json.dumps(res), flush=True)
        summary = {"mode": "control", "d": d, "prime": P, "cells": results,
                   "total_wall_s": time.perf_counter() - start,
                   "d1_control": {str(lam): s_and_g(lam, 1) for lam in partitions(4)}}
    else:
        raise SystemExit("mode must be control or price")
    os.makedirs(os.path.dirname(outpath), exist_ok=True)
    with open(outpath, "w") as fh:
        json.dump(summary, fh, indent=1)
    print("WROTE", outpath, "total_wall_s", summary["total_wall_s"])


if __name__ == "__main__":
    main()
