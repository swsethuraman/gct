"""B18-06 pilot P1: determinant/padding evaluation of highest-weight vectors
in declared five-row cells (docs/b18_06_report.md section 6).

Ordinary coefficients c_alpha = [x^alpha] f, positive weights,
E_(i,i+1) c_alpha = (alpha_i + 1) c_(alpha + e_i - e_(i+1)) when alpha_(i+1) > 0,
extended as a derivation. Arithmetic modulo p = 2^31 - 1.
"""
import itertools
import json
import random
import sys
import time
from collections import Counter
from pathlib import Path

import flint

P = 2147483647
CELLS = {
    "C0": (5, (12, 2, 2, 2, 2), 1),
    "C1": (5, (9, 7, 2, 1, 1), 1),
    "C2": (6, (15, 3, 2, 2, 2), 1),
    "C3": (5, (7, 7, 4, 1, 1), 1),
    "C4": (6, (11, 9, 2, 1, 1), 1),
    "C5": (6, (14, 4, 2, 2, 2), 2),
}
NV = 5


def exponents(n, k):
    if n == 1:
        return [(k,)]
    return [(v,) + rest for v in range(k, -1, -1) for rest in exponents(n - 1, k - v)]


MONS = exponents(NV, 4)
MINDEX = {m: i for i, m in enumerate(MONS)}


def weight_basis(lam, d):
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

    rec(0, tuple(lam), d, [])
    return out


def raising_columns(basis):
    """For each source monomial, list of (row_key, coeff) over all four E_(i,i+1)."""
    cols = []
    for mono in basis:
        entries = Counter()
        mult = Counter(mono)
        for op in range(NV - 1):
            i, j = op, op + 1
            for idx, k in mult.items():
                a = MONS[idx]
                if a[j] == 0:
                    continue
                b = list(a)
                b[i] += 1
                b[j] -= 1
                new = list(mono)
                new.remove(idx)
                new.append(MINDEX[tuple(b)])
                key = (op, tuple(sorted(new)))
                entries[key] += k * (a[i] + 1)
        cols.append(entries)
    return cols


def kernel(basis, a, rng, factor):
    cols = raising_columns(basis)
    n = len(basis)
    rows = n + 10 if factor == 1 else factor * n
    bucket, sign = {}, {}
    M = flint.nmod_mat(rows, n, P)
    nnz = 0
    for j, entries in enumerate(cols):
        for key, v in entries.items():
            if key not in bucket:
                bucket[key] = rng.randrange(rows)
                sign[key] = rng.randrange(1, P)
            r = bucket[key]
            M[r, j] = (int(M[r, j]) + sign[key] * v) % P
            nnz += 1
    X, nullity = M.nullspace()
    vecs = [[int(X[i, c]) for i in range(n)] for c in range(nullity)]
    return vecs, nullity, rows, nnz, len(bucket)


def polymul(f, g):
    h = Counter()
    for ea, ca in f.items():
        for eb, cb in g.items():
            h[tuple(x + y for x, y in zip(ea, eb))] += ca * cb
    return {e: c for e, c in h.items() if c}


def linear(vec):
    return {tuple(1 if t == k else 0 for t in range(NV)): c for k, c in enumerate(vec) if c}


def det_point(rng):
    while True:
        A = [[[rng.randint(-5, 5) for _ in range(NV)] for _ in range(4)] for _ in range(4)]
        block = flint.fmpz_mat([[A[r][c][k] for k in range(NV)] for r in range(4) for c in range(4)])
        if block.rank() == NV:
            break
    f = Counter()
    for perm in itertools.permutations(range(4)):
        sgn = (-1) ** sum(1 for x in range(4) for y in range(x + 1, 4) if perm[x] > perm[y])
        term = {(0,) * NV: sgn}
        for r in range(4):
            term = polymul(term, linear(A[r][perm[r]]))
        for e, c in term.items():
            f[e] += c
    return {"kind": "det", "data": A}, dict(f)


def pad_point(rng):
    while True:
        l = [rng.randint(-5, 5) for _ in range(NV)]
        N = [[[rng.randint(-5, 5) for _ in range(NV)] for _ in range(3)] for _ in range(3)]
        if any(l) and all(any(N[r][c]) for r in range(3) for c in range(3)):
            break
    per = Counter()
    for perm in itertools.permutations(range(3)):
        term = {(0,) * NV: 1}
        for r in range(3):
            term = polymul(term, linear(N[r][perm[r]]))
        for e, c in term.items():
            per[e] += c
    f = polymul(linear(l), dict(per))
    return {"kind": "pad", "l": l, "data": N}, f


def evaluate(vec, basis, f):
    cvals = [f.get(m, 0) % P for m in MONS]
    total = 0
    for coeff, mono in zip(vec, basis):
        if coeff:
            prod = coeff
            for idx in mono:
                prod = prod * cvals[idx] % P
            total += prod
    return total % P


def hess5_e1(f):
    """det of Hessian at e1 (exact integers), for the control cell."""
    def coeff(e):
        return f.get(e, 0)
    H = [[0] * NV for _ in range(NV)]
    for i in range(NV):
        for j in range(NV):
            e = [0] * NV
            e[0] = 2
            e[i] += 1
            e[j] += 1
            e = tuple(e)
            # d^2/dx_i dx_j of x^e at e1
            val = coeff(e)
            if i == j:
                val *= e[i] * (e[i] - 1)
            else:
                val *= e[i] * e[j]
            H[i][j] = val
    return int(flint.fmpz_mat(H).det())


def minor2(rows):
    return (rows[0][0] * rows[1][1] - rows[0][1] * rows[1][0]) % P


def main():
    cid = sys.argv[1]
    out = Path(sys.argv[2])
    d, lam, a = CELLS[cid]
    t0 = time.perf_counter()
    rng = random.Random(1806 + list(CELLS).index(cid))
    basis = weight_basis(lam, d)
    rec = {"cell": cid, "d": d, "lambda": lam, "a_census": a, "prime": P,
           "weight_space_dim": len(basis)}
    vecs, nullity, rows, nnz, targets = kernel(basis, a, rng, 1)
    if nullity != a:
        rec["retry_factor2_previous_nullity"] = nullity
        vecs, nullity, rows, nnz, targets = kernel(basis, a, rng, 2)
    rec.update(sketch_rows=rows, raising_nonzeros=nnz, raising_target_monomials=targets,
               kernel_dim_mod_p=nullity, seconds_kernel=time.perf_counter() - t0)
    if nullity != a:
        rec["status"] = "FAILED_INCONSISTENT_KERNEL"
        out.write_text(json.dumps(rec, indent=1) + "\n")
        print(json.dumps(rec))
        return
    for kind, maker in (("det", det_point), ("pad", pad_point)):
        pts = []
        for _ in range(3 if a == 1 else 4):
            meta, f = maker(rng)
            vals = [evaluate(v, basis, f) for v in vecs]
            entry = {"point": meta, "values_mod_p": vals}
            if cid == "C0":
                entry["hess5_e1_exact"] = hess5_e1(f)
                entry["c_4e1"] = f.get((4, 0, 0, 0, 0), 0)
            pts.append(entry)
        if a == 1:
            nonzero = any(p_["values_mod_p"][0] for p_ in pts)
            rank_floor = 1 if nonzero else 0
        else:
            mins = [minor2([pts[i]["values_mod_p"], pts[j]["values_mod_p"]])
                    for i in range(len(pts)) for j in range(i + 1, len(pts))]
            rec[kind + "_2x2_minors_mod_p"] = mins
            rank_floor = 2 if any(mins) else (1 if any(any(p_["values_mod_p"]) for p_ in pts) else 0)
        rec[kind + "_points"] = pts
        rec[kind + "_rank_floor"] = rank_floor
    if cid == "C0":
        ratios = []
        for p_ in rec["det_points"] + rec["pad_points"]:
            h = p_["hess5_e1_exact"] % P
            v = p_["values_mod_p"][0]
            ratios.append(v * pow(h, P - 2, P) % P if h else None)
        rec["control_ratio_F_over_H_mod_p"] = ratios
    rec["status"] = ("CLOSED_m_det_equals_a" if rec["det_rank_floor"] == a
                     else "SAMPLED_DET_DEFICIENCY_ONLY")
    rec["seconds_total"] = time.perf_counter() - t0
    rec["kernel_vector_nonzero_count"] = [sum(1 for x in v if x) for v in vecs]
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(rec, indent=1) + "\n")
    print(json.dumps({k: v for k, v in rec.items() if not k.endswith("_points")}))


if __name__ == "__main__":
    main()
