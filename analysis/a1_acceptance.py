#!/usr/bin/env python3
"""A1 -- the two production-path components wk13_b10_suite.py does not reach.

The suite covers the builders, the kernel and the evaluation ranks.  It does not
exercise matmul_mod_wide, because no cell in it has n_chi at or above the
16-bit-limb ceiling; B13-08 reports 17 of its 95 degree-10 weights do.  Nor does
it probe dtype discipline at the consumer boundary.  Both are checked here
against python-flint as an independent exact reference -- not against numpy,
which is the thing under test.

usage: python3 analysis/a1_acceptance.py [--out results/b14_a1/components.json]
"""
import json, os, sys, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
for _v in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ.setdefault(_v, '1')
import numpy as np
from flint import fmpz_mat
from wk11_s71_hybrid import matmul_mod
from wk13_b08_per6_lean import matmul_mod_wide, INNER_BLOCK

PRIMES = (2147483647, 2147483629)
CEIL = 1 << 21
results = []


def exact(A, B, p):
    """Independent reference: exact integer matmul in flint, then reduce."""
    M = fmpz_mat([[int(x) for x in row] for row in A]) * \
        fmpz_mat([[int(x) for x in row] for row in B])
    return np.array([[int(M[i, j]) % p for j in range(M.ncols())]
                     for i in range(M.nrows())], dtype=object)


def check(tag, A, B, p, expect_mod_fails):
    ref = exact(A, B, p)
    row = dict(tag=tag, K=int(A.shape[1]), p=p)

    w = matmul_mod_wide(A, B, p)
    row["wide_exact"] = bool(np.array_equal(np.asarray(w, dtype=object) % p, ref))

    try:
        n = matmul_mod(A, B, p)
        row["narrow"] = "exact" if np.array_equal(np.asarray(n, dtype=object) % p, ref) \
                        else "WRONG -- silently"
        row["narrow_raised"] = False
    except AssertionError:
        row["narrow"] = "raised AssertionError"
        row["narrow_raised"] = True

    # below the ceiling the wide path must DELEGATE, i.e. be bit-identical
    if A.shape[1] < CEIL and not expect_mod_fails:
        row["wide_identical_to_narrow"] = bool(np.array_equal(
            np.asarray(w, dtype=np.int64), np.asarray(matmul_mod(A, B, p), dtype=np.int64)))

    row["ok"] = row["wide_exact"] and (
        row["narrow_raised"] if expect_mod_fails else row["narrow"] == "exact")
    # the delegation flag must GATE, not merely be printed: below the ceiling a wide
    # path that is not bit-identical to the narrow one is a failure, and until batch 14
    # a False here passed silently.  Astra caught it.
    if "wide_identical_to_narrow" in row:
        row["ok"] = row["ok"] and row["wide_identical_to_narrow"]
    results.append(row)
    print(f"  {'OK  ' if row['ok'] else 'FAIL'} {tag:34s} K={row['K']:>9,} p={p}  "
          f"wide_exact={row['wide_exact']} narrow={row['narrow']}"
          + (f" delegates={row.get('wide_identical_to_narrow')}"
             if 'wide_identical_to_narrow' in row else ""))


def main():
    rng = np.random.default_rng(20260911)
    print("== matmul_mod_wide vs flint, at the seams ==")
    # the seams are where a blocking bug lives: the inner-block boundary and the
    # 2^21 ceiling itself, each side of each.
    for K, above in ((1_000, False),
                     (INNER_BLOCK - 1, False), (INNER_BLOCK, False), (INNER_BLOCK + 1, False),
                     (CEIL - 1, False), (CEIL, True), (CEIL + 1, True),
                     (3_000_000, True)):
        p = PRIMES[0]
        A = rng.integers(0, p, size=(2, K), dtype=np.int64)
        B = rng.integers(0, p, size=(K, 2), dtype=np.int64)
        check(f"K={'>=' if above else '< '}2^21", A, B, p, above)

    print("\n== both house primes, above the ceiling ==")
    K = CEIL + 7
    for p in PRIMES:
        A = rng.integers(0, p, size=(2, K), dtype=np.int64)
        B = rng.integers(0, p, size=(K, 2), dtype=np.int64)
        check("both primes", A, B, p, True)

    print("\n== dtype discipline at the consumer boundary ==")
    p = PRIMES[0]; K = 4_000
    A0 = rng.integers(0, p, size=(3, K), dtype=np.int64)
    B0 = rng.integers(0, p, size=(K, 3), dtype=np.int64)
    ref = exact(A0, B0, p)
    variants = {
        "int64 contiguous (baseline)": (A0, B0),
        "int32 inputs":               (A0.astype(np.int32), B0.astype(np.int32)),
        "uint32 inputs":              (A0.astype(np.uint32), B0.astype(np.uint32)),
        "object inputs":              (A0.astype(object), B0.astype(object)),
        "non-contiguous (transposed view)": (np.asfortranarray(A0), np.asfortranarray(B0)),
        "unreduced: entries shifted by +p": (A0 + p, B0 + p),
        "negative representatives":   (A0 - p, B0 - p),
    }
    for name, (A, B) in variants.items():
        row = dict(tag=f"dtype: {name}", K=K, p=p)
        try:
            w = matmul_mod_wide(A, B, p)
            row["ok"] = bool(np.array_equal(np.asarray(w, dtype=object) % p, ref))
            row["note"] = "matches the int64 baseline exactly" if row["ok"] else "DIVERGES"
        except Exception as e:
            row["ok"] = False; row["note"] = f"{type(e).__name__}: {e}"
        results.append(row)
        print(f"  {'OK  ' if row['ok'] else 'FAIL'} {name:36s} {row['note']}")

    out = dict(generated=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
               reference="python-flint fmpz_mat, exact integer matmul",
               inner_block=INNER_BLOCK, ceiling=CEIL,
               all_ok=all(r["ok"] for r in results), checks=results)
    path = "results/b14_a1/components.json"
    for i, a in enumerate(sys.argv):
        if a == "--out": path = sys.argv[i + 1]
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w").write(json.dumps(out, indent=1) + "\n")
    print(f"\n  {sum(r['ok'] for r in results)}/{len(results)} checks pass -> {path}")
    return 0 if out["all_ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
