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
     det_pencil points: must PASS with mult = a = 1;
  7. a "matrix" certificate whose nonvanishing_minor determinant exceeds 4300
     decimal digits: must PASS.  Before the session-67 fix this was reported
     UNPARSEABLE -- the rank checks passed but rendering the exact determinant
     into the report line hit Python's int->str digit cap (session 56's defect);
  8. a "sparse_nullity" certificate at (r=2, lambda=(4,4), delta=2) with
     det_pencil points, field F_p: must PASS, re-deriving mult_det = a = 1 by an
     independent full-weight-space build and a Wiedemann full-column-rank check;
  9. a "matrix" certificate marked matrix_role "gram" over a finite field: must
     be UNPARSEABLE -- rank(Gram) = rank(Theta) is the characteristic-zero Gram
     identity, so a Gram rank over F_p certifies nothing (Part A4);
 10. a "sparse_nullity" certificate declaring field "Q": must be UNPARSEABLE --
     a full-column-rank mod p certifies mult = a over Q, but the kind is a
     finite-field object and a char-0 "nullity" is not it (Part A4);
 11. the certificate of 8 rewritten in session 73's dialect (prime instead of
     field, claim.nullity instead of nullity, reduction instead of recipe):
     must PASS identically.  Before the batch-12 fix it was ERROR -- the schema
     layer accepted both dialects and layer3 read cert["field"] unconditionally,
     so every s73-dialect certificate passed validation and then died in
     re-derivation.  Schema validation is not re-derivation;
 12. that same certificate misrepresenting its N_S in reduction: must FAIL, so
     the size guard is not lost by changing dialect.
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
    # 7: a matrix certificate whose nonvanishing_minor determinant exceeds 4300
    # decimal digits.  An upper-triangular integer matrix with a large diagonal
    # has determinant = product of the diagonal (a nonzero minor is the whole
    # matrix); 520 entries near 1e9 give ~4400 digits, comfortably over the cap.
    bign = 520
    rb = random.Random(56)
    big = [[0] * bign for _ in range(bign)]
    for i in range(bign):
        big[i][i] = rb.randint(10 ** 8, 10 ** 9 - 1)
        for j in range(i + 1, bign):
            big[i][j] = rb.randint(-5, 5)
    ndigits = len(str(abs(__import__("math").prod(big[i][i] for i in range(bign)))))
    bigcert = {
        "format": FORMAT, "kind": "matrix",
        "title": f"selftest: nonvanishing minor with a {ndigits}-digit determinant",
        "produced_by": "tools/verify/selftest.py",
        "matrix": big,
        "nonvanishing_minor": {"rows": list(range(bign)), "cols": list(range(bign))},
    }
    results.append((f"7 oversized minor ({ndigits} digits) PASS", "PASS", verify_file(write(d, bigcert))))
    # 8: sparse_nullity at (r=2, lambda=(4,4), delta=2), det_pencil, field F_p
    P1 = 2147483647
    sn = {
        "format": FORMAT, "kind": "sparse_nullity",
        "title": "selftest: mult_det((4,4),2) = 1 by the sparse route",
        "produced_by": "tools/verify/selftest.py",
        "cell": {"n": 4, "r": 2, "lambda": [4, 4], "delta": 2, "a": 1},
        "conventions": dict(CONVENTIONS), "field": f"F_{P1}", "variety": "det_pencil", "nullity": 0,
        "points": [fresh_point("det_pencil", 2, random.Random(67)) for _ in range(3)],
        "recipe": {"K": 3, "point_seed": 67, "bound": 1000}, "basis": None,
    }
    results.append(("8 sparse_nullity PASS", "PASS", verify_file(write(d, sn))))
    # 9: a gram matrix over a finite field must be rejected
    gram_fp = {
        "format": FORMAT, "kind": "matrix", "title": "selftest: gram over F_p (must reject)",
        "produced_by": "tools/verify/selftest.py",
        "matrix": [[2, 0], [0, 2]], "matrix_role": "gram", "field": f"F_{P1}",
        "claimed_ranks_mod_p": {str(P1): 2},
    }
    results.append(("9 gram over F_p UNPARSEABLE", "UNPARSEABLE", verify_file(write(d, gram_fp))))
    # 10: a sparse_nullity declaring field Q must be rejected
    sn_q = json.loads(json.dumps(sn)); sn_q["field"] = "Q"
    results.append(("10 sparse_nullity over Q UNPARSEABLE", "UNPARSEABLE", verify_file(write(d, sn_q))))
    # 11: THE SAME certificate in session 73's dialect -- prime instead of field,
    # claim.nullity instead of nullity, reduction instead of recipe -- must PASS
    # identically.  Before the batch-12 fix this was ERROR: the schema layer
    # accepted both dialects and layer3 read cert["field"] unconditionally, so
    # every s73-dialect certificate died in re-derivation with KeyError('field').
    sn73 = json.loads(json.dumps(sn))
    del sn73["field"], sn73["nullity"], sn73["recipe"], sn73["basis"]
    sn73["prime"] = P1
    sn73["claim"] = {"nullity": 0, "mult": 1}
    sn73["reduction"] = {"N_S": 3, "n_chi": 3, "stab": 1, "nrows_E": 2, "nnz_E": 4}
    sn73["title"] = "selftest: the same claim in the session-73 dialect"
    results.append(("11 sparse_nullity s73 dialect PASS", "PASS", verify_file(write(d, sn73))))
    # 12: and the size guard applies in that dialect too -- reduction.N_S is
    # checked against the verifier's own N_S exactly as recipe.N_S always was.
    sn73_bad = json.loads(json.dumps(sn73))
    sn73_bad["reduction"]["N_S"] = 99
    sn73_bad["title"] = "selftest: s73 dialect misrepresenting its size (must reject)"
    results.append(("12 s73 dialect wrong reduction.N_S FAIL", "FAIL", verify_file(write(d, sn73_bad))))
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
