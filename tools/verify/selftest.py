#!/usr/bin/env python3
"""Self-test of the verifier on hand-made certificates with known answers.

  1. the degree-2 invariant of binary quartics, 12 f0 f4 - 3 f1 f3 + f2^2, as an
     "hwv" certificate at the cell (r=2, lambda=(4,4), delta=2): must PASS,
     including full row rank at fresh det / pad / reducible / generic points
     (every binary quartic is a product of linear forms, so nothing vanishes);
  2. the same with one coefficient altered: must FAIL the raising-operator check;
  3. the same with an unknown key: must be UNPARSEABLE;
  4. a "matrix" certificate: the degree-7 Macaulay matrix of the five partials
     of det_4 of a random pencil in five variables (350 x 330), claimed rank 299
     over Q and modulo both house primes, with a nonvanishing 299 x 299 minor:
     must PASS (this is paper 2's cap(4) = 300 mechanism);
  5. the same matrix with claimed rank 300: must FAIL;
  6. a "full_rank" certificate at the cell (r=2, lambda=(4,4), delta=2) with
     det_pencil points: must PASS with mult = a = 1.
"""
import os, sys, json, random, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from verify import verify_file, CONVENTIONS, FORMAT      # noqa: E402
from forms import det_pencil_form                        # noqa: E402
from layer1 import macaulay_matrix, rank_mod             # noqa: E402
from points import fresh_point                           # noqa: E402


def write(d, obj):
    fd, path = tempfile.mkstemp(suffix=".json", dir=d)
    with os.fdopen(fd, "w") as f:
        json.dump(obj, f)
    return path


def main():
    d = tempfile.mkdtemp(prefix="verify_selftest_")
    results = []
    inv = {
        "format": FORMAT, "kind": "hwv", "title": "selftest: degree-2 invariant of binary quartics",
        "produced_by": "tools/verify/selftest.py",
        "cell": {"n": 4, "r": 2, "lambda": [4, 4], "delta": 2, "a": 1},
        "conventions": dict(CONVENTIONS), "modulus": None,
        "vectors": [{"terms": [[[[0, 4], [4, 0]], 12], [[[1, 3], [3, 1]], -3], [[[2, 2], [2, 2]], 1]]}],
        "claims": {"independent": True,
                   "fresh_points": {"seed": 1, "count": 4,
                                    "nonvanishing_on": ["det_pencil", "padded_permanent", "reducible", "generic"]}},
    }
    results.append(("1 invariant PASS", "PASS", verify_file(write(d, inv))))
    bad = json.loads(json.dumps(inv))
    bad["vectors"][0]["terms"][1][1] = -2
    results.append(("2 altered coefficient FAIL", "FAIL", verify_file(write(d, bad))))
    unk = json.loads(json.dumps(inv))
    unk["extra"] = 1
    results.append(("3 unknown key UNPARSEABLE", "UNPARSEABLE", verify_file(write(d, unk))))
    # 4/5: Macaulay matrix at (n, r, d) = (4, 5, 7)
    rnd = random.Random(49)
    pencil = [[[rnd.randint(-1000, 1000) for _ in range(4)] for _ in range(4)] for _ in range(5)]
    F = det_pencil_form(pencil, 5)
    M = macaulay_matrix(F, 4, 5, 7)
    # a nonvanishing 299 x 299 minor: pick pivot rows/cols by a mod-p echelon form
    from flint import nmod_mat
    p = 2147483647
    A = nmod_mat(len(M), len(M[0]), [v % p for r in M for v in r], p)
    R, rk = A.rref()
    pivcols = []
    for i in range(rk):
        pivcols.append(next(j for j in range(len(M[0])) if int(R[i, j]) != 0))
    # rows: take the pivot rows of the transpose's rref
    At = nmod_mat(len(M[0]), len(M), [M[i][j] % p for j in range(len(M[0])) for i in range(len(M))], p)
    Rt, rkt = At.rref()
    pivrows = [next(j for j in range(len(M)) if int(Rt[i, j]) != 0) for i in range(rkt)]
    mat = {
        "format": FORMAT, "kind": "matrix", "title": "selftest: Macaulay M_7 of a det_4 pencil in 5 variables",
        "produced_by": "tools/verify/selftest.py",
        "matrix_source": {"type": "macaulay_det_pencil", "n": 4, "r": 5, "d": 7, "pencil": pencil},
        "claimed_rank_Q": 299, "claimed_ranks_mod_p": {"2147483647": 299, "2147483629": 299},
        "nonvanishing_minor": {"rows": pivrows, "cols": pivcols},
    }
    results.append(("4 Macaulay rank 299 PASS", "PASS", verify_file(write(d, mat))))
    mat2 = json.loads(json.dumps(mat))
    mat2["claimed_rank_Q"] = 300
    del mat2["nonvanishing_minor"]
    results.append(("5 Macaulay rank 300 FAIL", "FAIL", verify_file(write(d, mat2))))
    fr = {
        "format": FORMAT, "kind": "full_rank", "title": "selftest: mult_det((4,4),2) = 1",
        "produced_by": "tools/verify/selftest.py",
        "cell": {"n": 4, "r": 2, "lambda": [4, 4], "delta": 2, "a": 1},
        "conventions": dict(CONVENTIONS), "prime": 2147483647, "variety": "det_pencil",
        "points": [fresh_point("det_pencil", 2, random.Random(5)) for _ in range(3)], "basis": None,
    }
    results.append(("6 full_rank PASS", "PASS", verify_file(write(d, fr))))
    allok = True
    for name, expect, (status, log) in results:
        good = status == expect
        allok &= good
        print(f"{'ok ' if good else 'BAD'} {name}: got {status}")
        if not good:
            for n_, ok, det in log:
                print(f"      [{'ok' if ok else 'FAIL'}] {n_} {det}")
    print("selftest", "PASSED" if allok else "FAILED")
    return 0 if allok else 1


if __name__ == "__main__":
    sys.exit(main())
