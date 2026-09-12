#!/usr/bin/env python3
"""B14-02 -- exact rational LEFT kernel and rank witnesses for the degree-13
source matrix A (39 x 96).

Source vectors are ROWS and points are COLUMNS, so the ideal relations live in
the LEFT kernel: a combination sum_i c_i F_i is in the ideal iff c^T A = 0.
A . K = 0 is the RIGHT kernel, of dimension >= 57, and is NOT the object wanted;
it is computed here only so the report can state both and show they are
different.

Delivers K of size 39 x k with A^T . K = 0, rank(K) = k and rank(A) = 39 - k,
all over Q, plus a nonzero exact (39-k) x (39-k) minor as the rank witness.
"""
import argparse, json, math, os, random, sys, time
from flint import fmpz_mat

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from b14_02_source13 import OUT, PRIMES                              # noqa: E402

T0 = time.time()


def log(*a):
    print(f"[{time.time()-T0:8.1f}s]", *a, flush=True)


def load_A(role="primary"):
    d = json.load(open(os.path.join(OUT, f"A13_{role}.json"), encoding="utf-8"))
    A = [[int(x) for x in row] for row in d["A"]]
    return d, A


def mat(rows):
    nr, nc = len(rows), len(rows[0])
    return fmpz_mat(nr, nc, [int(x) for r in rows for x in r])


def left_kernel(A):
    """{c : c^T A = 0} = right nullspace of A^T.  Returned as columns of K
    (39 x k) with integer entries."""
    At = mat(A).transpose()                    # 96 x 39
    X, nul = At.nullspace()                    # X is 39 x 39, first `nul` cols span
    K = [[int(X[i, j]) for j in range(nul)] for i in range(len(A))]
    return K, nul


def nonzero_minor(A, r, tries=4000, seed=1402):
    """an explicit nonzero r x r minor of A, as the rank witness."""
    rng = random.Random(seed)
    nr, nc = len(A), len(A[0])
    # greedy first: row-reduce a copy to find independent row/col positions
    for t in range(tries):
        rs = sorted(rng.sample(range(nr), r)) if r < nr else list(range(nr))
        cs = sorted(rng.sample(range(nc), r))
        sub = [[A[i][j] for j in cs] for i in rs]
        d = int(mat(sub).det())
        if d:
            return dict(rows=rs, cols=cs, det=str(d), det_bits=abs(d).bit_length(), tries=t + 1)
    return None


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--role", default="primary")
    ap.add_argument("--holdout", action="store_true")
    a = ap.parse_args(argv)
    meta, A = load_A(a.role)
    nr, nc = len(A), len(A[0])
    log(f"A is {nr} x {nc}; max entry {max(abs(x) for r in A for x in r).bit_length()} bits")

    M = mat(A)
    rk = M.rank()
    K, k = left_kernel(A)
    log(f"rank_Q(A) = {rk};  dim left kernel k = {k};  rank + k = {rk + k} (must be {nr})")
    assert rk + k == nr, (rk, k, nr)

    # A^T . K = 0 verified in exact integer arithmetic
    if k:
        Kt = fmpz_mat(nr, k, [int(x) for row in K for x in row])
        prod = M.transpose() * Kt
        atk_zero = prod.is_zero()
        rkK = Kt.rank()
    else:
        atk_zero, rkK = True, 0
    log(f"A^T . K == 0 : {atk_zero};  rank(K) = {rkK} (must be k = {k})")

    # the right kernel, stated only to distinguish it from the object wanted
    Xr, right_nul = M.nullspace()
    log(f"RIGHT kernel dim = {right_nul} (>= {nc - nr}); this is NOT the object wanted")

    # rank witness: an explicit nonzero rk x rk minor
    w = nonzero_minor(A, rk)
    log(f"rank witness: nonzero {rk}x{rk} minor found in {w['tries']} draw(s), "
        f"det has {w['det_bits']} bits" if w else "rank witness NOT FOUND")

    # ---- C6 must-fail.  FIRST ATTEMPT WAS VACUOUS: setting row 5 := row 4 on the
    # full matrix left the rank at 36, because with a 3-dimensional left kernel
    # row 5 was already in the span of the other 38, so deleting its independent
    # contribution cost nothing.  Recorded, not quietly replaced.
    A2 = [list(r) for r in A]
    A2[5] = list(A2[4])
    rk2 = mat(A2).rank()
    _, k2 = left_kernel(A2)
    vacuous_attempt = dict(construction="full matrix, row 5 := row 4",
                           rank_after=rk2, k_after=k2,
                           control_can_fail=(rk2 == rk - 1 and k2 == k + 1),
                           why_vacuous="row 5 already lies in the span of the other 38")

    # the working version: operate on a submatrix of FULL row rank, where any
    # loss of independence must show.
    wrows = w["rows"]
    B = [A[i] for i in wrows]
    rkB = mat(B).rank()
    _, kB = left_kernel(B)
    B2 = [list(r) for r in B]; B2[1] = list(B2[0])            # duplicate a row
    rkB2 = mat(B2).rank(); _, kB2 = left_kernel(B2)
    B3 = [list(r) for r in B]; B3[2] = [0] * len(B3[2])       # zero a row
    rkB3 = mat(B3).rank(); _, kB3 = left_kernel(B3)
    dup_ok = (rkB2 == rkB - 1 and kB2 == kB + 1)
    zero_ok = (rkB3 == rkB - 1 and kB3 == kB + 1)
    can_fail = dup_ok and zero_ok
    log(f"C6 witness submatrix ({len(B)} rows): rank {rkB}, k {kB}")
    log(f"C6 MUST-FAIL duplicate row: rank {rkB}->{rkB2}, k {kB}->{kB2} -> "
        f"{'detected' if dup_ok else 'VACUOUS'}")
    log(f"C6 MUST-FAIL zero a row:    rank {rkB}->{rkB3}, k {kB}->{kB3} -> "
        f"{'detected' if zero_ok else 'VACUOUS'}")

    out = dict(
        values_are="exact integers; K's columns are a Z-basis of the rational LEFT "
                   "kernel {c : c^T A = 0} of the 39x96 degree-13 source matrix. "
                   "No transform applied.",
        orientation="source vectors are ROWS, points are COLUMNS; relation vectors "
                    "are the columns of K with A^T K = 0",
        n_rows=nr, n_cols=nc, rank_Q=rk, left_kernel_dim=k,
        left_kernel_K=[[str(x) for x in row] for row in K],
        A_transpose_K_is_zero=bool(atk_zero), rank_K=rkK,
        right_kernel_dim=right_nul,
        rank_witness=w,
        must_fail=dict(vacuous_first_attempt=vacuous_attempt,
                       submatrix_rows=len(B), submatrix_rank=rkB, submatrix_k=kB,
                       duplicate_row=dict(rank_after=rkB2, k_after=kB2, detected=dup_ok),
                       zeroed_row=dict(rank_after=rkB3, k_after=kB3, detected=zero_ok),
                       control_can_fail=can_fail),
        primes=PRIMES,
        label="SOURCE-MATRIX RESULT. Not i_red(13): that needs slot 1's target minor "
              "and slot 4's recount (PROVED.md: evaluation_cannot_certify_i_ge_1).")

    # ---- holdout: any left-kernel vector must also annihilate the 20 holdout points
    if a.holdout and k:
        hm, Ah = load_A("holdout")
        surv = []
        for j in range(k):
            c = [K[i][j] for i in range(nr)]
            vals = [sum(c[i] * Ah[i][t] for i in range(nr)) for t in range(len(Ah[0]))]
            surv.append(dict(vector=j, all_zero_on_holdout=all(v == 0 for v in vals),
                             nonzero_count=sum(1 for v in vals if v)))
        out["holdout_check"] = surv
        log(f"holdout: {sum(1 for s in surv if s['all_zero_on_holdout'])}/{k} "
            f"kernel vectors survive the 20 held-out points")

    json.dump(out, open(os.path.join(OUT, f"kernel_{a.role}.json"), "w"), indent=1)
    log("wrote " + os.path.join(OUT, f"kernel_{a.role}.json"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
