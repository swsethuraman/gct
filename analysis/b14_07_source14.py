#!/usr/bin/env python3
"""B14-07 -- the exact degree-14 source matrix at P14.

Rows: the 93 source fillings born by degree 14 (rungs 12, 13, 14 of
results/s74/source.json).  Columns: the points of results/b14_prep/points/P14.json
(192 primary, 20 holdout; the holdout columns are computed but never used to
determine the kernel dimension).

Row system at degree 14, s74's declared convention with the transport exponent
changed from 24 - d_i to 14 - d_i:

    A14[i][j] = F_{T_i}(f_j) * msym_u(f_j)^(14 - d_i),
    msym_u(f) = 4! * [s_1^4] f,   d_i = native degree of row i.

Rows are LITERAL transported fillings (not u-normalised).  Stored matrices carry
a values_are field saying so.

Orientation: source vectors are ROWS and points are COLUMNS, so ideal relations
live in the LEFT kernel: sum_i c_i F_i is a candidate relation iff c^T A = 0.

    --prime P        evaluate one prime (resumable, per-point checkpoint)
    --all            evaluate every prime in P14.json order

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
"""
import argparse
import json
import os
import sys
import time
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)

from wk8_s30_core import exps                                            # noqa: E402
from wk11_s69_circuit import Filling, sym_table, cached_order            # noqa: E402
from wk12_s74_dp import dp_eval_compact                                  # noqa: E402

N, H, DEG = 4, 9, 14
OUT = os.path.join(ROOT, "results", "b14_07")
T0 = time.time()

_E = exps(N, H)
IU = _E.index(tuple([N] + [0] * (H - 1)))        # never a literal -- board rule
_EIDX = {a: k for k, a in enumerate(_E)}
_A, _idx, FACT, TAB = sym_table(N, H)

VALUES_ARE = ("literal transported fillings at degree 14: "
              "A[i][j] = F_native_i(f_j) * u(f_j)^(14 - d_i) mod p, "
              "u = 4! [s_1^4] f; NOT u-normalised (the u-normalised vector "
              "would be this divided by 24^(14 - d_i)); reduced to [0, p)")


def log(*a):
    print(f"[{time.time()-T0:8.1f}s]", *a, flush=True)


# --------------------------------------------------------------------- inputs
def load_rows():
    src = json.load(open(os.path.join(ROOT, "results", "s74", "source.json")))
    ent = [e for e in src["entries"] if e["rung"] <= DEG]
    assert len(ent) == 93, f"expected 93 rows born by degree {DEG}, got {len(ent)}"
    rows = []
    for e in ent:
        F = Filling.from_json(e["native"])
        assert F.delta == e["rung"] == e["native"]["delta"]
        rows.append(dict(index=e["index"], rung=e["rung"], d=F.delta,
                         exponent=DEG - F.delta, key=e["key"], F=F))
    return rows


def quartic_cv(pt, cub_exps):
    """coefficient vector of f = l * c over exps(4,9), as python ints."""
    cv = [0] * len(_E)
    lin = pt["linear"]
    for b, cb in zip(cub_exps, pt["cubic_coefficients"]):
        if cb == 0:
            continue
        for i in range(H):
            li = lin[i]
            if li == 0:
                continue
            al = list(b)
            al[i] += 1
            cv[_EIDX[tuple(al)]] += li * cb
    return cv


def load_points():
    P = json.load(open(os.path.join(ROOT, "results", "b14_prep", "points", "P14.json")))
    cub = [tuple(b) for b in P["cubic_exponents"]]
    pts = []
    for j, pt in enumerate(P["points"]):
        cv = quartic_cv(pt, cub)
        msym_int = [FACT[a] * cv[a] for a in range(len(_E))]
        # controls on the point construction itself, both able to fail
        assert msym_int[IU] == pt["u_symbol"], (
            f"point {pt['id']}: u symbol {msym_int[IU]} != declared {pt['u_symbol']}")
        assert max(abs(x) for x in msym_int) == pt["max_abs_quartic_symbol"], (
            f"point {pt['id']}: max |symbol| {max(abs(x) for x in msym_int)} "
            f"!= declared {pt['max_abs_quartic_symbol']}")
        pts.append(dict(j=j, id=pt["id"], role=pt["role"], cv=cv))
    return P, pts


# ----------------------------------------------------------------- evaluation
_W = {}


def _init(rows, prime):
    _W["rows"] = rows
    _W["p"] = prime
    # warm the module-level order cache in this worker; cached_order returns (order, W)
    _W["order"] = [cached_order(r["F"])[0] for r in rows]


def _one_point(cv):
    """native values of all 93 rows at one point, plus u."""
    p = _W["p"]
    ms = [(c % p) * FACT[a] % p for a, c in enumerate(cv)]
    u = ms[IU]
    nat = [dp_eval_compact(r["F"], ms, p, TAB, order=o) % p
           for r, o in zip(_W["rows"], _W["order"])]
    return u, nat


def run_prime(prime, rows, pts, procs=2):
    path = os.path.join(OUT, f"A14_mod_{prime}.json")
    done = {}
    if os.path.exists(path):
        old = json.load(open(path))
        done = {int(k): v for k, v in old.get("native", {}).items()}
        log(f"resume p={prime}: {len(done)} points already done")
    todo = [q for q in pts if q["j"] not in done]
    if todo:
        with Pool(procs, initializer=_init, initargs=(rows, prime)) as pool:
            t = time.time()
            for q, (u, nat) in zip(todo, pool.imap(_one_point, [q["cv"] for q in todo],
                                                   chunksize=1)):
                done[q["j"]] = dict(u=u, native=nat)
                n = len(done)
                if n % 10 == 0 or n == len(pts):
                    rate = (time.time() - t) / max(1, n - (len(pts) - len(todo)))
                    log(f"p={prime} {n}/{len(pts)} points ({rate:.2f}s/point)")
                    _write(path, prime, rows, pts, done)
    _write(path, prime, rows, pts, done)
    return done


def _write(path, prime, rows, pts, done):
    rec = dict(
        session="B14-07", degree=DEG, prime=prime,
        values_are=VALUES_ARE,
        row_system=("A[i][j] = F_native_i(f_j) * u(f_j)^(14 - d_i) mod p; "
                    "rows are source fillings, columns are points; "
                    "ideal relations live in the LEFT kernel"),
        rows=[dict(index=r["index"], rung=r["rung"], d=r["d"],
                   exponent=r["exponent"], key=r["key"]) for r in rows],
        points=[dict(j=q["j"], id=q["id"], role=q["role"]) for q in pts],
        n_rows=len(rows), n_points=len(pts),
        native={str(k): v for k, v in sorted(done.items())},
    )
    tmp = path + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(rec, fh, separators=(",", ":"))
    os.replace(tmp, path)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prime", type=int)
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--procs", type=int, default=2)
    a = ap.parse_args()

    os.makedirs(OUT, exist_ok=True)
    P, pts = load_points()
    rows = load_rows()
    log(f"rows={len(rows)} points={len(pts)} "
        f"(primary={sum(1 for q in pts if q['role']=='primary')}, "
        f"holdout={sum(1 for q in pts if q['role']=='holdout')})")
    log(f"u index resolved by exps().index -> {IU}; exps[0]={_E[0]}")

    primes = P["crt_primes"] if a.all else [a.prime]
    for p in primes:
        assert p is not None
        t = time.time()
        done = run_prime(p, rows, pts, a.procs)
        zero_u = [pts[j]["id"] for j in done if done[j]["u"] == 0]
        log(f"p={p} complete in {time.time()-t:.1f}s; u-zero points: {zero_u or 'none'}")


if __name__ == "__main__":
    main()
