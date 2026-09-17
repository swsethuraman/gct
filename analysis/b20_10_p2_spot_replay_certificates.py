"""B20-10 pilot 2: spot REPLAY of saved arithmetic in three committed certificates.

This is a replay of recorded integers, not an independent evaluator: no source vector is
evaluated. It checks that each certificate's stated linear algebra follows from the
integers it records, modulo P = 524287.

  (a) routeA_signfilter_20260917/certificates/transverse_triple_rank3.json:
      rebuild the 3x3 matrix [row functional applied to (q3, q7, n02)] from the recorded
      pencil values and the three displayed formulas; compare with the stored matrix;
      recompute det mod P (expected 225843, nonzero => rank 3 over Q).
  (b) routeA_signfilter_20260917/certificates/independence_q3_q7_e_n02.json:
      recompute the five 4x4 minors of the 4x5 value matrix (expected 426380, 191230,
      255288, 485311, 35010) and the rank mod P.
  (c) final_arc_diagnostic/results/f1_new_point_minor.json: stack the 10 inherited and
      4 new forbidden rows (14 x 3), recompute rank mod P (expected 2), verify that every
      one of the C(14,3) = 364 3x3 minors vanishes mod P, and verify the residuals of
      n02 - 265391 q3 - 275398 q7 on all 14 rows.
"""
import hashlib
import itertools
import json
import sys
import time

t0 = time.time()
P = 524287
paths = sys.argv[1:4]
outpath = sys.argv[4]
out = {"inputs": {}}
docs = []
for p in paths:
    raw = open(p, "rb").read()
    out["inputs"][p] = hashlib.sha256(raw).hexdigest()
    docs.append(json.loads(raw))
tri, ind, f1 = docs


def det_mod(M):
    n = len(M)
    A = [[x % P for x in row] for row in M]
    d = 1
    for k in range(n):
        piv = None
        for r in range(k, n):
            if A[r][k]:
                piv = r
                break
        if piv is None:
            return 0
        if piv != k:
            A[k], A[piv] = A[piv], A[k]
            d = -d
        d = d * A[k][k] % P
        inv = pow(A[k][k], P - 2, P)
        for r in range(k + 1, n):
            f = A[r][k] * inv % P
            if f:
                for c in range(k, n):
                    A[r][c] = (A[r][c] - f * A[k][c]) % P
    return d % P


def rank_mod(M):
    A = [[x % P for x in row] for row in M]
    n, m = len(A), len(A[0])
    r = 0
    for c in range(m):
        piv = None
        for i in range(r, n):
            if A[i][c]:
                piv = i
                break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        inv = pow(A[r][c], P - 2, P)
        A[r] = [x * inv % P for x in A[r]]
        for i in range(n):
            if i != r and A[i][c]:
                f = A[i][c]
                A[i] = [(x - f * y) % P for x, y in zip(A[i], A[r])]
        r += 1
    return r


# (a) transverse triple
coef = {
    "C2": {"K5": -177, "K5+S1": 112, "K5+2S1": -7},
    "C4_S1S2": {"K5": -27, "K5+S1": -60, "K5+2S1": 15, "K5+S2": 368, "K5+2S2": -92},
    "C4_S1S4": {"K5": -2211, "K5+S1": -252, "K5+2S1": 63, "K5+S4": 2576, "K5+2S4": -644},
}
mat = []
for row in tri["row_order"]:
    r = []
    for col in tri["columns"]:
        v = sum(c * tri["pencil_values"][col][k] for k, c in coef[row].items()) % P
        r.append(v)
    mat.append(r)
det = det_mod(mat)
out["a_transverse_triple"] = {"rebuilt_matrix": mat, "stored_matrix": tri["matrix"],
                              "matrix_matches": mat == tri["matrix"],
                              "det_mod_P": det, "stored_det": tri["det_mod_P"],
                              "det_matches": det == tri["det_mod_P"], "rank_mod_P": rank_mod(mat)}

# (b) independence of q3, q7, e, n02
rows = ind["matrix_rows_by_point"]
minors = {}
for cols in itertools.combinations(range(5), 4):
    sub = [[rows[i][j] for j in cols] for i in range(4)]
    minors[str(list(cols))] = det_mod(sub)
stored = {k.replace(" ", ""): v for k, v in ind["nonzero_4x4_minors_by_point_columns"].items()}
mine = {k.replace(" ", ""): v for k, v in minors.items()}
out["b_independence"] = {"minors": mine, "stored": stored, "all_match": mine == stored,
                         "rank_mod_P": rank_mod(rows), "stored_rank": ind["rank_mod_P"]}

# (c) 14 x 3 forbidden matrix
M14 = [r["row"] for r in f1["inherited_rows"]] + [r["row"] for r in f1["new_rows"]]
nz = 0
for cols in itertools.combinations(range(len(M14)), 3):
    if det_mod([M14[i] for i in cols]):
        nz += 1
resid = [(r[2] - 265391 * r[0] - 275398 * r[1]) % P for r in M14]
out["c_forbidden_matrix"] = {"rows": len(M14), "rank_mod_P": rank_mod(M14), "stored_rank": f1["combined_rank_mod_P"],
                             "three_by_three_minors_checked": sum(1 for _ in itertools.combinations(range(len(M14)), 3)),
                             "nonzero_3x3_minors": nz, "relation_residuals_all_zero": all(x == 0 for x in resid),
                             "degree12_rows_rank": rank_mod([r for r, lab in zip(M14, [x["label"] for x in f1["inherited_rows"]] + [x["label"] for x in f1["new_rows"]]) if lab.endswith("d12")]),
                             "degree11_rows_rank": rank_mod([r for r, lab in zip(M14, [x["label"] for x in f1["inherited_rows"]] + [x["label"] for x in f1["new_rows"]]) if lab.endswith("d11")])}
out["seconds"] = time.time() - t0
json.dump(out, open(outpath, "w"), indent=1)
print(json.dumps(out, indent=1))
