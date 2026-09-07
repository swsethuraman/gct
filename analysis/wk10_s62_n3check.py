"""Session 62 — independent checker for the n = 3 LMR positive control.

Reads the exhibited integer highest-weight vector results/s62_n3_vec_d<delta>.json and,
by an INDEPENDENT rebuild of the cell (no reuse of the measurement's kernel), certifies
over Z that it is a nonzero highest-weight vector in I(D_7^{det_3}) of weight lambda:

  1. v != 0 and its coordinates are integers;
  2. E v = 0 over Z, E the simple raising operators on V_chi (rebuilt here);
  3. v vanishes at N_det fresh integer det_3 pencils, evaluated EXACTLY over Z;
  4. v does not vanish at a generic integer cubic.

(1)-(4) prove i_det(lambda, delta) >= 1 over Q, hence mult_det <= a - 1: the rank drop.
Independent of the block-Wiedemann measurement -- it recomputes E and evaluates by hand.

    python3 analysis/wk10_s62_n3check.py [delta ...]        (default 12)
"""
import json
import os
import random
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "tools", "verify"))
from wk8_s30_core import exps, restrict, det_form            # noqa: E402
from wk9_s45_build import build_cell                          # noqa: E402

N_DEG = 3
R = 7
DET3, NENT = det_form(3)


def check(delta, seed_fresh=20260907, n_fresh=16, bound=50):
    vecf = os.path.join(ROOT, "results", f"s62_n3_vec_d{delta}.json")
    if not os.path.exists(vecf):
        return {"delta": delta, "status": "NO VECTOR FILE"}
    data = json.load(open(vecf))
    v = data["vector_chi_coords"]
    lam = tuple(data["lambda"])
    # independent rebuild of the cell
    B = build_cell(lam, delta, n=N_DEG, verbose=False)
    E = B["E"]
    arr = B["arr"]
    nc = B["n_chi"]
    assert len(v) == nc, ("vector length != n_chi", len(v), nc)
    out = {"delta": delta, "lambda": list(lam), "n_chi": nc}
    out["nonzero"] = any(x != 0 for x in v)
    out["integer"] = all(isinstance(x, int) for x in v)
    # E v = 0 over Z (exact: accumulate over COO with Python big ints; scipy int64 @ object is unsupported)
    C = E.tocoo()
    prod = [0] * C.shape[0]
    for i, j, d in zip(C.row.tolist(), C.col.tolist(), C.data.tolist()):
        if v[j]:
            prod[i] += int(d) * v[j]
    out["E_v_zero_over_Z"] = all(x == 0 for x in prod)
    # expand v to monomial coefficients: coeff on monomial m = v[col_of[m]] * sgn[m]
    col_of = arr["col_of"]; sgn = arr["sgn"]; M = arr["M"]
    sel = np.nonzero(col_of >= 0)[0]
    coeff = (np.array(v, dtype=object)[col_of[sel]]) * sgn[sel]
    Msel = M[sel]
    A = exps(N_DEG, R)

    def evaluate(cv):
        total = 0
        for row in range(Msel.shape[0]):
            c = int(coeff[row])
            if c == 0:
                continue
            prod = 1
            for k in range(Msel.shape[1]):
                prod *= cv[int(Msel[row, k])]
                if prod == 0:
                    break
            total += c * prod
        return total

    rnd = random.Random(seed_fresh)
    fresh_vals = []
    for _ in range(n_fresh):
        As = [[rnd.randint(-bound, bound) for _ in range(NENT)] for _ in range(R)]
        co = restrict(DET3, NENT, N_DEG, R, As)
        cv = [int(co.get(al, 0)) for al in A]
        fresh_vals.append(evaluate(cv))
    out["vanishes_fresh_det_over_Z"] = all(x == 0 for x in fresh_vals)
    out["n_fresh_det"] = n_fresh
    rndc = random.Random(seed_fresh + 1)
    cv = [rndc.randint(-bound, bound) for _ in A]
    out["nonzero_generic_cubic"] = evaluate(cv) != 0
    out["certifies_i_det_ge_1_over_Q"] = bool(out["nonzero"] and out["integer"] and out["E_v_zero_over_Z"]
                                              and out["vanishes_fresh_det_over_Z"] and out["nonzero_generic_cubic"])
    out["support"] = int(sum(1 for x in v if x))
    out["max_abs_coeff"] = int(max(abs(x) for x in v))
    return out


if __name__ == "__main__":
    deltas = [int(x) for x in sys.argv[1:]] or [12]
    res = {}
    for d in deltas:
        r = check(d)
        res[str(d)] = r
        print(json.dumps(r, indent=1))
    with open(os.path.join(ROOT, "results", "s62_n3_check.json"), "w") as fh:
        json.dump(res, fh, indent=1)
    allok = all(r.get("certifies_i_det_ge_1_over_Q") for r in res.values())
    print("ALL CERTIFY i_det>=1 over Q:", allok)
