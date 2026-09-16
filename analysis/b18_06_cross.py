"""Cross-method control: P1's compressed elimination versus the sweep's Casimir
projector, on the same cell. Two independent code paths must give proportional
highest-weight vectors modulo p, and the elimination must see nullity a = 1.
"""
import importlib.util
import json
import random
import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent


def load(name):
    spec = importlib.util.spec_from_file_location(name, HERE / (name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    cid = sys.argv[1]
    out = Path(sys.argv[2])
    sweep = load("b18_06_sweep")
    pilot = load("b18_06_pilot")
    lam = sweep.CELLS[cid]
    p = pilot.P
    t0 = time.perf_counter()
    rec = {"cell": cid, "lambda": lam, "prime": p}

    W, base, ops, dims, K = sweep.exact_hwv(lam, record=rec)
    rec["weight_space_dim"] = K
    assert W is not None

    pbasis = pilot.weight_basis(lam, sweep.D)
    rec["pilot_basis_matches"] = (pbasis == base)
    rng = random.Random(2026)
    vecs, nullity, rows, nnz, targets = pilot.kernel(pbasis, 1, rng, 1)
    rec["elimination_first_nullity"] = nullity
    if nullity != 1:
        vecs, nullity, rows, nnz, targets = pilot.kernel(pbasis, 1, rng, 2)
        rec["elimination_retry_nullity"] = nullity
    rec["elimination_sketch_rows"] = rows

    ok = False
    if nullity == 1:
        u = np.array([x % p for x in vecs[0]], dtype=np.int64)
        w = np.array([x % p for x in W], dtype=np.int64)
        j = int(np.nonzero(w)[0][0])
        ratio = int(u[j]) * pow(int(w[j]), p - 2, p) % p
        ok = bool(np.all((w * ratio - u) % p == 0))
        rec["ratio_mod_p"] = ratio
    rec["projector_and_elimination_proportional"] = ok
    rec["seconds"] = time.perf_counter() - t0
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(rec, indent=1) + "\n")
    print(json.dumps({k: v for k, v in rec.items() if k != "lift_attempts"}))


if __name__ == "__main__":
    main()
