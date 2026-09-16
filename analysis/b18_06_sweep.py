"""B18-06 sweep: the nineteen untested degree-five five-row cells.

Ladder per cell (docs/b18_06_sweep.md):
  1. exact integer highest-weight vector h_lambda, exact evaluation at integer
     determinant points; a nonzero value closes the cell;
  2. only if it survives: symmetric rectangular Kronecker s;
  3. only if it survives both: exact evaluation at an actual padding point.

Conventions (preamble): forms in Sym^4(V*), coefficient ring Sym(Sym^4 V),
ordinary coefficients c_alpha = [x^alpha] f, weights alpha, and
  E_ij c_alpha = (alpha_i + 1) c_(alpha + e_i - e_j)   when alpha_j > 0,
extended as a derivation. Raising operators move weight from j to i (i < j).

h_lambda is produced by a Casimir projector over F_p, lifted to Z by CRT plus
rational reconstruction, and then VERIFIED EXACTLY over Z: the four simple
raising operators must annihilate it. That verification, not the projector, is
the certificate. a = dim H_lambda is recomputed here by the Weyl alternant on
weight multiplicities, independently of any census in the tree.
"""
import itertools
import json
import sys
import time
from functools import lru_cache
from math import gcd
from pathlib import Path

import numpy as np

NV = 5
D = 5
PRIMES = [2147483647, 2147483629, 2147483587, 2147483579, 2147483563,
          2147483549, 2147483543, 2147483497]
MAX_PRIMES = 8
SEEDS = [7, 11, 13]

CELLS = {
    "S01": (11, 4, 2, 2, 1), "S02": (10, 5, 3, 1, 1), "S03": (10, 5, 2, 2, 1),
    "S04": (8, 7, 3, 1, 1), "S05": (9, 5, 4, 1, 1), "S06": (9, 6, 2, 2, 1),
    "S07": (8, 5, 5, 1, 1), "S08": (10, 4, 2, 2, 2), "S09": (9, 5, 3, 2, 1),
    "S10": (9, 4, 4, 2, 1), "S11": (8, 6, 3, 2, 1), "S12": (8, 5, 4, 2, 1),
    "S13": (8, 6, 2, 2, 2), "S14": (7, 6, 4, 2, 1), "S15": (7, 5, 4, 3, 1),
    "S16": (8, 4, 4, 2, 2), "S17": (7, 4, 4, 4, 1), "S18": (6, 6, 4, 2, 2),
    "S19": (6, 4, 4, 4, 2),
    # known-outcome replays (controls)
    "R01": (9, 7, 2, 1, 1), "R02": (12, 2, 2, 2, 2),
}


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
        tot = 0
        r = rem
        k = 0
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
    """a = dim of the highest-weight space, by the Weyl alternant."""
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


def op_arrays(src_basis, tgt_index, i, j, convention="standard"):
    """E_ij restricted to one weight space; coefficient (alpha_i + 1) * multiplicity.

    convention='factorial' deliberately uses alpha_i instead: a wrong operator,
    used only by the failure control.
    """
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
            coeff = mult * (a[i] + 1 if convention == "standard" else a[i])
            if coeff == 0:
                continue
            s.append(bi)
            t.append(tgt_index[tuple(sorted(new))])
            c.append(coeff)
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
        tot = 0
        for idx in range(st[k], st[k + 1]):
            tot += int(c[idx]) * W[int(s[idx])]
        out[int(u)] = tot
    return out


def shift(lam, i, j):
    """weight of E_ij applied to weight lam: move one unit from j to i."""
    mu = list(lam)
    mu[i] += 1
    mu[j] -= 1
    return tuple(mu)


def build_ops(lam, d=D, convention="standard"):
    base = weight_basis(lam, d)
    idx = {m: k for k, m in enumerate(base)}
    ops = {}
    dims = {}
    cache = {}
    for i in range(NV):
        for j in range(NV):
            if i == j:
                continue
            mu = shift(lam, j, i)          # weight of E_ji(v)
            if min(mu) < 0:
                continue
            if mu not in cache:
                b = weight_basis(mu, d)
                cache[mu] = (b, {m: k for k, m in enumerate(b)})
            b, bidx = cache[mu]
            ops[("down", i, j)] = op_arrays(base, bidx, j, i, convention)
            ops[("up", i, j)] = op_arrays(b, idx, i, j, convention)
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
    res = []
    for k in range(min(n, maxpart), 0, -1):
        for r in parts_le(n - k, maxlen - 1, k):
            res.append((k,) + r)
    return res


def dominates(mu, lam):
    a = list(mu) + [0] * 8
    b = list(lam) + [0] * 8
    s = 0
    for i in range(8):
        s += a[i] - b[i]
        if s < 0:
            return False
    return True


def casimir_targets(lam, d=D):
    return sorted({cas(mu) for mu in parts_le(4 * d, NV)
                   if dominates(mu, lam) and tuple(mu) != tuple(lam) and cas(mu) != cas(lam)})


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


def raising_residues(lam, W, ops, dims):
    """exact E_(i,i+1) W for the four simple raising operators."""
    res = []
    for i in range(NV - 1):
        op = ops[("down", i + 1, i)]           # E_(i,i+1) : lam -> lam + e_i - e_(i+1)
        dim = dims[("mid", i + 1, i)]
        res.append(apply_exact(op, W, dim))
    return res


def exact_hwv(lam, d=D, convention="standard", record=None):
    base, idx, ops, dims = build_ops(lam, d, convention)
    K = len(base)
    targets = casimir_targets(lam, d)
    attempts = []
    for seed in SEEDS:
        acc, M, j0 = None, 1, None
        for n, p in enumerate(PRIMES[:MAX_PRIMES], 1):
            v = project(lam, K, ops, dims, targets, p, seed)
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
                acc = [int(x) for x in u]
                M = p
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
            W = [nn * (L // dd) for nn, dd in zip(nums, dens)]
            g = 0
            for x in W:
                g = gcd(g, abs(x))
            if g > 1:
                W = [x // g for x in W]
            res = raising_residues(lam, W, ops, dims)
            if any(any(r) for r in res) or not any(W):
                attempts.append({"seed": seed, "prime_index": n, "event": "exact_verification_failed"})
                continue
            if record is not None:
                record["lift_attempts"] = attempts
                record["primes_used"] = n
                record["seed_used"] = seed
                record["hwv_max_abs"] = max(abs(x) for x in W)
                record["hwv_nonzeros"] = sum(1 for x in W if x)
                record["raising_target_dims"] = [dims[("mid", i + 1, i)] for i in range(NV - 1)]
            return W, base, ops, dims, K
    if record is not None:
        record["lift_attempts"] = attempts
    return None, base, ops, dims, K


# ---------------------------------------------------------------- points

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
    import fractions
    mat = [[fractions.Fraction(x) for x in r] for r in rows]
    rank = 0
    ncols = len(mat[0])
    for col in range(ncols):
        piv = None
        for r in range(rank, len(mat)):
            if mat[r][col]:
                piv = r
                break
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
    """det(sum_k x_k A_k); valid iff its 16x5 coefficient block has rank 5."""
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
    return {"kind": "det", "A": A, "block_rank": NV}, f


def pad_point(rng):
    """F* shape: l(x) * per_3(sum_k x_k N_k), all ten linear forms nonzero."""
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
    total = 0
    for coeff, mono in zip(W, base):
        if not coeff:
            continue
        prod = coeff
        for mi in mono:
            prod *= cv[mi]
            if prod == 0:
                break
        total += prod
    return total


def hess5_e1_det(f):
    """det of the 5x5 Hessian of f at e1, exactly (control for (12,2^4))."""
    import fractions
    H = [[0] * NV for _ in range(NV)]
    for i in range(NV):
        for j in range(NV):
            e = [0] * NV
            e[0] = 2
            e[i] += 1
            e[j] += 1
            e = tuple(e)
            val = f.get(e, 0)
            H[i][j] = val * (e[i] * (e[i] - 1) if i == j else e[i] * e[j])
    mat = [[fractions.Fraction(x) for x in row] for row in H]
    det = fractions.Fraction(1)
    for col in range(NV):
        piv = None
        for r in range(col, NV):
            if mat[r][col]:
                piv = r
                break
        if piv is None:
            return 0
        if piv != col:
            mat[col], mat[piv] = mat[piv], mat[col]
            det = -det
        det *= mat[col][col]
        for r in range(col + 1, NV):
            if mat[r][col]:
                fct = mat[r][col] / mat[col][col]
                mat[r] = [a - fct * b for a, b in zip(mat[r], mat[col])]
    assert det.denominator == 1
    return int(det)


# ------------------------------------------------- symmetric Kronecker (step 2)

@lru_cache(None)
def partitions(n, maxpart=None):
    if maxpart is None:
        maxpart = n
    if n == 0:
        return ((),)
    return tuple((k,) + rest for k in range(min(n, maxpart), 0, -1)
                 for rest in partitions(n - k, k))


def zpart(p):
    from collections import Counter
    from math import factorial
    ans = 1
    for k, c in Counter(p).items():
        ans *= k ** c * factorial(c)
    return ans


@lru_cache(None)
def character(lam, rho):
    if not rho:
        return int(not lam)
    if sum(lam) != sum(rho):
        return 0
    k, tail = rho[0], rho[1:]
    ell = len(lam)
    beta = tuple(lam[i] + ell - i - 1 for i in range(ell))
    ans = 0
    for b in beta:
        c = b - k
        if c < 0 or c in beta:
            continue
        sign = (-1) ** sum(1 for t in beta if c < t < b)
        new = sorted([t for t in beta if t != b] + [c], reverse=True)
        mu = tuple(t - ell + i + 1 for i, t in enumerate(new))
        mu = tuple(t for t in mu if t)
        ans += sign * character(mu, tail)
    return ans


def square_type(rho):
    out = []
    for k in rho:
        if k % 2:
            out.append(k)
        else:
            out.extend([k // 2, k // 2])
    return tuple(sorted(out, reverse=True))


def symmetric_kronecker(lam, d=D):
    """s = [S^lambda : Sym^2(S^(d^4))], transposition included."""
    from fractions import Fraction
    R = (d,) * 4
    g = Fraction(0)
    tr = Fraction(0)
    for rho in partitions(4 * d):
        z = zpart(rho)
        chi = character(lam, rho)
        if chi == 0:
            continue
        g += Fraction(chi * character(R, rho) ** 2, z)
        tr += Fraction(chi * character(R, square_type(rho)), z)
    s = (g + tr) / 2
    assert s.denominator == 1 and g.denominator == 1
    return int(s), int(g), int(tr)


# ---------------------------------------------------------------- controls

def run_controls(out):
    rec = {"control_suite": True, "checks": []}
    rng = np.random.default_rng(99)

    # (a) known cell R02 = (12,2^4): exact HWV must be proportional to det Hess_5(e1)
    lam = CELLS["R02"]
    r = {}
    W, base, ops, dims, K = exact_hwv(lam, record=r)
    ratios, ok = [], W is not None
    if ok:
        for _ in range(3):
            meta, f = det_point(rng)
            hv = hess5_e1_det(f)
            val = evaluate_exact(W, base, f)
            ratios.append([val, hv])
        from fractions import Fraction
        rs = {Fraction(v, h) for v, h in ratios if h}
        ok = len(rs) == 1 and all(h != 0 for _, h in ratios)
    rec["checks"].append({"name": "hwv_is_hessian_covariant_(12,2^4)", "expect": "pass",
                          "passed": bool(ok), "value_pairs": ratios})

    # (b) wrong convention (alpha_i instead of alpha_i+1) must be rejected
    rw = {}
    Ww, basew, opsw, dimsw, Kw = exact_hwv(lam, convention="factorial", record=rw)
    if Ww is None:
        detected = True
        detail = "no vector reconstructed under the wrong convention"
    else:
        res = raising_residues(lam, Ww, ops, dims)     # verify against CORRECT operators
        detected = any(any(x) for x in res)
        detail = "nonzero residues against the correct operators" if detected else "NOT DETECTED"
    rec["checks"].append({"name": "wrong_raising_convention_rejected", "expect": "rejected",
                          "passed": bool(detected), "detail": detail})

    # (c) corrupted vector must be rejected
    if W is not None:
        Wbad = list(W)
        k = next(i for i, x in enumerate(Wbad) if x)
        Wbad[k] += 1
        res = raising_residues(lam, Wbad, ops, dims)
        detected = any(any(x) for x in res)
    else:
        detected = False
    rec["checks"].append({"name": "corrupted_vector_rejected", "expect": "rejected",
                          "passed": bool(detected)})

    # (d) invalid determinant point (rank-deficient block) must be rejected
    bad_rows = [[1, 0, 0, 0, 0] for _ in range(16)]
    rec["checks"].append({"name": "rank_deficient_point_rejected", "expect": "rejected",
                          "passed": rank_over_Q(bad_rows) != NV, "block_rank": rank_over_Q(bad_rows)})

    # (e) symmetric Kronecker routine against the known value s = 8 for (12,2^4)
    s, g, tr = symmetric_kronecker(CELLS["R02"])
    rec["checks"].append({"name": "symmetric_kronecker_(12,2^4)_equals_8", "expect": 8,
                          "passed": s == 8, "s": s, "g": g, "transpose_trace": tr})

    # (f) Weyl alternant against a shape whose multiplicity is not 1
    a_known = weyl_multiplicity((14, 4, 2, 2, 2), 6)
    rec["checks"].append({"name": "weyl_alternant_(14,4,2,2,2)_d6_equals_2", "expect": 2,
                          "passed": a_known == 2, "a": a_known})

    rec["all_passed"] = all(c["passed"] for c in rec["checks"])
    out.write_text(json.dumps(rec, indent=1) + "\n")
    print(json.dumps({"controls_all_passed": rec["all_passed"],
                      "checks": [(c["name"], c["passed"]) for c in rec["checks"]]}))


# ---------------------------------------------------------------- one cell

def run_cell(cid, out):
    lam = CELLS[cid]
    t0 = time.perf_counter()
    rec = {"cell": cid, "lambda": lam, "d": D}
    rec["a_weyl_alternant"] = weyl_multiplicity(lam)
    W, base, ops, dims, K = exact_hwv(lam, record=rec)
    rec["weight_space_dim"] = K
    rec["seconds_hwv"] = time.perf_counter() - t0
    if W is None:
        rec["status"] = "NOT_REACHED_no_exact_hwv"
        out.write_text(json.dumps(rec, indent=1) + "\n")
        print(json.dumps({k: v for k, v in rec.items() if k != "lift_attempts"}))
        return
    rec["exact_raising_residues_all_zero"] = True
    rng = np.random.default_rng(4100 + int(cid[1:]) if cid[0] in "SR" else 1)
    det_vals, pad_vals = [], []
    for _ in range(3):
        meta, f = det_point(rng)
        det_vals.append({"point": meta, "value": evaluate_exact(W, base, f)})
    for _ in range(3):
        meta, f = pad_point(rng)
        pad_vals.append({"point": meta, "value": evaluate_exact(W, base, f)})
    rec["det_values"] = det_vals
    rec["pad_values"] = pad_vals
    rec["m_det_floor"] = 1 if any(v["value"] for v in det_vals) else 0
    rec["m_pad_floor"] = 1 if any(v["value"] for v in pad_vals) else 0
    if rec["m_det_floor"] == 1:
        rec["status"] = "CLOSED_m_det_equals_a"
        rec["D"] = 0 if rec["m_pad_floor"] == 1 else "<=0"
    else:
        rec["status"] = "NOT_CLOSED_sampled_zero_only"
        s, g, tr = symmetric_kronecker(lam)
        rec["symmetric_kronecker_s"] = s
        rec["ordinary_kronecker_g"] = g
        rec["transpose_trace"] = tr
        rec["m_det_certified_zero"] = (s == 0)
    rec["seconds_total"] = time.perf_counter() - t0
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(rec, indent=1) + "\n")
    print(json.dumps({k: v for k, v in rec.items()
                      if k not in ("det_values", "pad_values", "lift_attempts")}))


def main():
    what = sys.argv[1]
    out = Path(sys.argv[2])
    out.parent.mkdir(parents=True, exist_ok=True)
    if what == "controls":
        run_controls(out)
    else:
        run_cell(what, out)


if __name__ == "__main__":
    main()
