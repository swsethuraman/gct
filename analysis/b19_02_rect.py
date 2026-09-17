"""B19-02: close the one remaining degree-five cell, lambda = (4,4,4,4,4).

Corollary 8.1 of docs/b19_02_report.md needs i_det = 0 in this cell. Since
a = 1 there, one exact nonzero value of the unique highest-weight vector at an
actual determinant point gives m_det = 1 = a, hence i_det = 0.

Method (same as the batch-18 degree-five sweep, reimplemented here):
  * build the weight space and every shifted weight space lambda + e_i - e_j;
  * Casimir projector over F_p to get a candidate highest-weight vector;
  * lift to Z by CRT + rational reconstruction;
  * VERIFY EXACTLY over Z that the four simple raising operators annihilate it,
    recording source/target weights, both dimensions and the operator nonzero
    counts, so that an empty operator cannot pass vacuously;
  * evaluate exactly at integer determinant points det(sum_k x_k B_k), used only
    when the 16x5 coefficient block has rank 5 over Q.

Conventions: ordinary coefficients, E_ij c_alpha = (alpha_i+1) c_(alpha+e_i-e_j).
"""
import itertools
import json
import sys
import time
from fractions import Fraction
from functools import lru_cache
from math import gcd
from pathlib import Path

import numpy as np

NV = 5
D = 5
LAM = (4, 4, 4, 4, 4)
PRIMES = [2147483647, 2147483629, 2147483587, 2147483579, 2147483563, 2147483549]
SEEDS = [7, 11, 13]


def exps(n, k):
    if n == 1:
        return [(k,)]
    return [(v,) + r for v in range(k, -1, -1) for r in exps(n - 1, k - v)]


MONS = exps(NV, 4)
MIDX = {m: i for i, m in enumerate(MONS)}


def weight_basis(w, d=D):
    out = []

    def rec(start, rem, left, cur):
        if left == 0:
            if not any(rem):
                out.append(tuple(cur))
            return
        for i in range(start, len(MONS)):
            m = MONS[i]
            r = tuple(a - b for a, b in zip(rem, m))
            if min(r) < 0:
                continue
            rec(i, r, left - 1, cur + [i])

    rec(0, tuple(w), d, [])
    return out


@lru_cache(None)
def weight_dim(w, d=D):
    @lru_cache(None)
    def f(i, rem, left):
        if left == 0:
            return 1 if not any(rem) else 0
        if i == len(MONS):
            return 0
        m = MONS[i]
        tot, r, k = 0, rem, 0
        while True:
            tot += f(i + 1, r, left - k)
            r = tuple(a - b for a, b in zip(r, m))
            k += 1
            if k > left or min(r) < 0:
                break
        return tot
    v = f(0, tuple(w), d)
    f.cache_clear()
    return v


def weyl_multiplicity(lam, d=D):
    rho = [NV - 1 - i for i in range(NV)]
    tot = 0
    for perm in itertools.permutations(range(NV)):
        sgn = 1
        for x in range(NV):
            for y in range(x + 1, NV):
                if perm[x] > perm[y]:
                    sgn = -sgn
        mu = tuple(lam[i] + rho[i] - rho[perm[i]] for i in range(NV))
        if min(mu) < 0 or sum(mu) != 4 * d:
            continue
        tot += sgn * weight_dim(mu, d)
    return tot


def op_arrays(src_basis, tgt_index, i, j):
    """E_ij on one weight space: c_alpha -> (alpha_i + 1) c_(alpha + e_i - e_j)."""
    s, t, c = [], [], []
    for bi, mono in enumerate(src_basis):
        seen = {}
        for mi in mono:
            seen[mi] = seen.get(mi, 0) + 1
        for mi, mult in seen.items():
            a = MONS[mi]
            if a[j] == 0:
                continue
            b = list(a)
            b[i] += 1
            b[j] -= 1
            new = list(mono)
            new.remove(mi)
            new.append(MIDX[tuple(b)])
            s.append(bi)
            t.append(tgt_index[tuple(sorted(new))])
            c.append(mult * (a[i] + 1))
    s = np.array(s, dtype=np.int64)
    t = np.array(t, dtype=np.int64)
    c = np.array(c, dtype=np.int64)
    o = np.argsort(t, kind="stable")
    s, t, c = s[o], t[o], c[o]
    if len(t):
        uniq, starts = np.unique(t, return_index=True)
    else:
        uniq = np.array([], dtype=np.int64)
        starts = np.array([], dtype=np.int64)
    return (s, c, uniq, starts)


def apply_mod(op, v, dim, p):
    s, c, uniq, starts = op
    out = np.zeros(dim, dtype=np.int64)
    if len(s) == 0:
        return out
    prod = (c * v[s]) % p
    out[uniq] = np.add.reduceat(prod, starts) % p
    return out


def apply_exact(op, W, dim):
    s, c, uniq, starts = op
    out = [0] * dim
    if len(s) == 0:
        return out
    st = list(starts) + [len(s)]
    for k, u in enumerate(uniq):
        out[int(u)] = sum(int(c[x]) * W[int(s[x])] for x in range(st[k], st[k + 1]))
    return out


def build(lam, d=D):
    base = weight_basis(lam, d)
    idx = {m: k for k, m in enumerate(base)}
    ops, dims, cache = {}, {}, {}
    for i in range(NV):
        for j in range(NV):
            if i == j:
                continue
            mu = list(lam)
            mu[j] += 1
            mu[i] -= 1
            if min(mu) < 0:
                continue
            mu = tuple(mu)
            if mu not in cache:
                b = weight_basis(mu, d)
                cache[mu] = (b, {m: k for k, m in enumerate(b)})
            b, bidx = cache[mu]
            ops[("down", i, j)] = op_arrays(base, bidx, j, i)
            ops[("up", i, j)] = op_arrays(b, idx, i, j)
            dims[("mid", i, j)] = len(b)
    return base, idx, ops, dims


def cas(mu):
    mu = list(mu) + [0] * (NV - len(mu))
    return sum(m * m for m in mu) + sum((NV + 1 - 2 * (k + 1)) * mu[k] for k in range(NV))


def parts_le(n, maxlen, maxpart=None):
    if maxpart is None:
        maxpart = n
    if n == 0:
        return [()]
    if maxlen == 0:
        return []
    return [(k,) + r for k in range(min(n, maxpart), 0, -1)
            for r in parts_le(n - k, maxlen - 1, k)]


def dominates(mu, lam):
    a = list(mu) + [0] * 8
    b = list(lam) + [0] * 8
    s = 0
    for i in range(8):
        s += a[i] - b[i]
        if s < 0:
            return False
    return True


def project(lam, K, ops, dims, targets, p, seed):
    rng = np.random.default_rng(seed)
    v = rng.integers(0, 4, size=K, dtype=np.int64)
    lam2 = sum(x * x for x in lam)
    for t in targets:
        out = (lam2 * v) % p
        for i in range(NV):
            for j in range(NV):
                if i == j or ("down", i, j) not in ops:
                    continue
                mid = apply_mod(ops[("down", i, j)], v, dims[("mid", i, j)], p)
                out = (out + apply_mod(ops[("up", i, j)], mid, K, p)) % p
        v = (out - t * v) % p
    return v


def ratrec(u, M, bound):
    a, b = M, u % M
    x0, x1 = 0, 1
    while b > bound:
        q = a // b
        a, b = b, a - q * b
        x0, x1 = x1, x0 - q * x1
    if x1 == 0 or abs(x1) > bound or b > bound:
        return None
    return (b if x1 > 0 else -b, abs(x1))


def polymul(f, g):
    h = {}
    for ea, ca in f.items():
        for eb, cb in g.items():
            k = tuple(x + y for x, y in zip(ea, eb))
            h[k] = h.get(k, 0) + ca * cb
    return {e: c for e, c in h.items() if c}


def linear(vec):
    return {tuple(1 if t == k else 0 for t in range(NV)): c for k, c in enumerate(vec) if c}


def rank_over_Q(rows):
    mat = [[Fraction(x) for x in r] for r in rows]
    rank = 0
    for col in range(len(mat[0])):
        piv = next((r for r in range(rank, len(mat)) if mat[r][col]), None)
        if piv is None:
            continue
        mat[rank], mat[piv] = mat[piv], mat[rank]
        pv = mat[rank][col]
        for r in range(len(mat)):
            if r != rank and mat[r][col]:
                f = mat[r][col] / pv
                mat[r] = [a - f * b for a, b in zip(mat[r], mat[rank])]
        rank += 1
    return rank


def det_point(rng):
    while True:
        A = [[[int(rng.integers(-5, 6)) for _ in range(NV)] for _ in range(4)] for _ in range(4)]
        rows = [A[r][c] for r in range(4) for c in range(4)]
        if rank_over_Q(rows) == NV:
            break
    f = {}
    for perm in itertools.permutations(range(4)):
        sgn = (-1) ** sum(1 for x in range(4) for y in range(x + 1, 4) if perm[x] > perm[y])
        term = {(0,) * NV: sgn}
        for r in range(4):
            term = polymul(term, linear(A[r][perm[r]]))
        for e, c in term.items():
            f[e] = f.get(e, 0) + c
    return {"kind": "det", "A": A, "block_rank_over_Q": NV}, f


def pad_point(rng):
    while True:
        l = [int(rng.integers(-5, 6)) for _ in range(NV)]
        N = [[[int(rng.integers(-5, 6)) for _ in range(NV)] for _ in range(3)] for _ in range(3)]
        if any(l) and all(any(N[r][c]) for r in range(3) for c in range(3)):
            break
    per = {}
    for perm in itertools.permutations(range(3)):
        term = {(0,) * NV: 1}
        for r in range(3):
            term = polymul(term, linear(N[r][perm[r]]))
        for e, c in term.items():
            per[e] = per.get(e, 0) + c
    return {"kind": "pad", "l": l, "N": N}, polymul(linear(l), per)


def evaluate_exact(W, base, f):
    cv = [f.get(m, 0) for m in MONS]
    tot = 0
    for coeff, mono in zip(W, base):
        if not coeff:
            continue
        prod = coeff
        for mi in mono:
            prod *= cv[mi]
            if prod == 0:
                break
        tot += prod
    return tot


def main():
    out = Path(sys.argv[1])
    t0 = time.perf_counter()
    rec = {"cell": "(4,4,4,4,4)", "d": D, "lambda": list(LAM)}
    rec["a_weyl_alternant"] = weyl_multiplicity(LAM)
    base, idx, ops, dims = build(LAM)
    K = len(base)
    rec["weight_space_dim"] = K
    targets = sorted({cas(mu) for mu in parts_le(4 * D, NV)
                      if dominates(mu, LAM) and tuple(mu) != LAM and cas(mu) != cas(LAM)})
    rec["casimir_factors"] = len(targets)
    # operator census: an empty operator must not pass vacuously
    rec["raising_operators"] = [
        {"operator": f"E_{i+1}{i+2}",
         "source_weight": list(LAM), "source_dim": K,
         "target_weight": [LAM[k] + (1 if k == i else (-1 if k == i + 1 else 0)) for k in range(NV)],
         "target_dim": dims[("mid", i + 1, i)],
         "nonzero_entries": int(len(ops[("down", i + 1, i)][0]))}
        for i in range(NV - 1)]
    W = None
    attempts = []
    for seed in SEEDS:
        acc, M, j0 = None, 1, None
        for n, p in enumerate(PRIMES, 1):
            v = project(LAM, K, ops, dims, targets, p, seed)
            if not v.any():
                attempts.append({"seed": seed, "prime_index": n, "event": "zero_projection"})
                break
            if j0 is None:
                j0 = int(np.nonzero(v)[0][0])
            if int(v[j0]) == 0:
                attempts.append({"seed": seed, "prime_index": n, "event": "pivot_vanished"})
                break
            u = (v * pow(int(v[j0]), p - 2, p)) % p
            if acc is None:
                acc, M = [int(x) for x in u], p
            else:
                nm = M * p
                mi = pow(M % p, p - 2, p)
                acc = [(a + M * (((int(b) - a) % p) * mi % p)) % nm for a, b in zip(acc, u)]
                M = nm
            bound = int((M // 2) ** 0.5)
            nums, dens, ok = [], [], True
            for a in acc:
                if a == 0:
                    nums.append(0)
                    dens.append(1)
                    continue
                r = ratrec(a, M, bound)
                if r is None:
                    ok = False
                    break
                nums.append(r[0])
                dens.append(r[1])
            if not ok:
                attempts.append({"seed": seed, "prime_index": n, "event": "reconstruction_incomplete"})
                continue
            L = 1
            for dd in dens:
                L = L * dd // gcd(L, dd)
            cand = [nn * (L // dd) for nn, dd in zip(nums, dens)]
            g = 0
            for x in cand:
                g = gcd(g, abs(x))
            if g > 1:
                cand = [x // g for x in cand]
            res = [apply_exact(ops[("down", i + 1, i)], cand, dims[("mid", i + 1, i)])
                   for i in range(NV - 1)]
            if any(any(r) for r in res) or not any(cand):
                attempts.append({"seed": seed, "prime_index": n, "event": "exact_verification_failed"})
                continue
            W = cand
            rec.update(primes_used=n, seed_used=seed,
                       hwv_max_abs=max(abs(x) for x in W),
                       hwv_nonzeros=sum(1 for x in W if x),
                       exact_raising_residues_all_zero=True)
            break
        if W is not None:
            break
    rec["lift_attempts"] = attempts
    if W is None:
        rec["status"] = "NOT_REACHED_no_exact_hwv"
    else:
        rng = np.random.default_rng(1902)
        dets, pads = [], []
        for _ in range(3):
            meta, f = det_point(rng)
            dets.append({"point": meta, "value": evaluate_exact(W, base, f)})
        for _ in range(3):
            meta, f = pad_point(rng)
            pads.append({"point": meta, "value": evaluate_exact(W, base, f)})
        rec["det_values"] = dets
        rec["pad_values"] = pads
        rec["m_det_floor"] = 1 if any(x["value"] for x in dets) else 0
        rec["m_pad_floor"] = 1 if any(x["value"] for x in pads) else 0
        rec["status"] = ("CLOSED_i_det_zero" if rec["m_det_floor"] == 1
                         else "NOT_CLOSED_sampled_zero_only")
    rec["seconds"] = time.perf_counter() - t0
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(rec, indent=1) + "\n")
    print(json.dumps({k: v for k, v in rec.items()
                      if k not in ("det_values", "pad_values")}))


if __name__ == "__main__":
    main()
