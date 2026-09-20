"""B23-10 pilot 3.  Imports no project code (python-flint for the ranks only).

  A. B23-03 Thm 3.2, determinant side: rank M_k mod p at a fresh random integer point of D_N,
     N = 6, 7 (k = 6, 7, 8) and N = 8 (k = 6, 7).  The quartic is computed exactly over Z, then
     reduced.  A modular rank at an integer point is a floor on the generic rank of D_N.
  B. B23-03 Prop. 2.5 floor: exact rank over Q of M_4 at a fresh random integer cubic through the plane
     x1 = x2 = 0 (expect 64), and at a fresh random integer cubic (expect 65).
Usage: b23_10_p3_det_floor_replay.py <out.json> <prereg sha256>
"""
import hashlib
import json
import random
import sys
import time
from itertools import combinations_with_replacement
from pathlib import Path

T0 = time.time()
OUT = Path(sys.argv[1])
PREREG = Path("results/b23_10/p3_prereg.md")
got = hashlib.sha256(PREREG.read_bytes()).hexdigest()
out = {"pilot": "b23_10_p3_det_floor_replay",
       "preregistration": {"path": str(PREREG).replace("\\", "/"), "sha256": got, "expected": sys.argv[2],
                           "match": got == sys.argv[2], "recorded_at_elapsed_s": round(time.time() - T0, 4)}}


def dump():
    out["elapsed_s"] = round(time.time() - T0, 3)
    OUT.write_text(json.dumps(out, indent=1) + "\n")


dump()
if got != sys.argv[2]:
    out["status"] = "prereg hash mismatch; nothing run"
    dump()
    sys.exit(1)

import flint  # noqa: E402

P = 2147483647
SEED = 20260922
rng = random.Random(SEED)
out.update({"modulus": P, "seed": SEED, "A": {}, "B": {}})


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
    return {e: v for e, v in r.items() if v}


def add(p, q, s=1):
    r = dict(p)
    for e, v in q.items():
        r[e] = r.get(e, 0) + s * v
    return {e: v for e, v in r.items() if v}


def partial(p, i):
    r = {}
    for e, v in p.items():
        if e[i]:
            f = list(e)
            f[i] -= 1
            r[tuple(f)] = r.get(tuple(f), 0) + v * e[i]
    return r


def det(M):
    if len(M) == 1:
        return M[0][0]
    res = {}
    for j in range(len(M)):
        minor = [row[:j] + row[j + 1:] for row in M[1:]]
        res = add(res, mul(M[0][j], det(minor)), 1 if j % 2 == 0 else -1)
    return res


def linform(n):
    while True:
        f = {}
        for i in range(n):
            c = rng.randint(-5, 5)
            if c:
                f[tuple(1 if t == i else 0 for t in range(n))] = c
        if f:
            return f


def macaulay_mod(F, n, k):
    parts = [partial(F, i) for i in range(n)]
    rows = {e: i for i, e in enumerate(monos(k, n))}
    cols = monos(k - 3, n)
    M = flint.nmod_mat(len(rows), n * len(cols), P)
    c = 0
    for pd in parts:
        for m in cols:
            for e, v in pd.items():
                M[rows[tuple(a + b for a, b in zip(e, m))], c] = v % P
            c += 1
    return M.rank(), len(rows), n * len(cols)


def macaulay4_exact(C, n=5):
    parts = [partial(C, i) for i in range(n)]
    rows = {e: i for i, e in enumerate(monos(4, n))}
    cols = monos(2, n)
    A = [[0] * (n * len(cols)) for _ in range(len(rows))]
    c = 0
    for pd in parts:
        for m in cols:
            for e, v in pd.items():
                A[rows[tuple(a + b for a, b in zip(e, m))]][c] = v
            c += 1
    return flint.fmpz_mat(A).rank()


# ---------------------------------------------------------------- B first (small, exact)
x = [{tuple(1 if t == i else 0 for t in range(5)): 1} for i in range(5)]


def rand_form(d, n=5):
    f = {}
    for e in monos(d, n):
        c = rng.randint(-5, 5)
        if c:
            f[e] = c
    return f


C_plane = add(mul(x[0], rand_form(2)), mul(x[1], rand_form(2)))
C_gen = rand_form(3)
out["B"] = {"rank_M4_random_plane_cubic_exact": macaulay4_exact(C_plane),
            "rank_M4_random_cubic_exact": macaulay4_exact(C_gen),
            "predicted": [64, 65]}
dump()

# ---------------------------------------------------------------- A
claimed = {6: {6: 321, 7: 660, 8: 1146}, 7: {6: 567, 7: 1279, 8: 2435}, 8: {6: 932, 7: 2248}}
ceiling = {6: {6: 287, 7: 532, 8: 918}, 7: {6: 518, 7: 1050, 8: 1968}, 8: {6: 876, 7: 1926}}
for N in (6, 7, 8):
    A = [[linform(N) for _ in range(4)] for _ in range(4)]
    F = det(A)
    out["A"]["N%d" % N] = {"quartic_terms": len(F)}
    for k in sorted(claimed[N]):
        if time.time() - T0 > 45:
            out["A"]["N%d" % N]["k%d" % k] = "skipped (45 s stop rule)"
            dump()
            continue
        t = time.time()
        r, nr, nc = macaulay_mod(F, N, k)
        out["A"]["N%d" % N]["k%d" % k] = {
            "rank_mod_p": r, "shape": [nr, nc], "claimed_floor": claimed[N][k],
            "equals_claimed": r == claimed[N][k], "padding_ceiling": ceiling[N][k],
            "margin_mine": r - ceiling[N][k], "seconds": round(time.time() - t, 2)}
        dump()

out["status"] = "done"
dump()
print(json.dumps(out, indent=1))
