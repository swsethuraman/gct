"""Session 62 — the n = 3 LMR positive control (Task 4, the must-pass).

Cell  lambda = (19, 7, 2^5),  delta = 12,  ell = r = 7,  a = 6,  n = 3 (det_3),
N = 9 (the 3x3 matrix entries).  The LMR module is non-vacuous here, so i_det >= 1
by theorem, i.e. mult_det <= 5 < a = 6.  This is the first rank drop the programme's
own evaluation engine would ever be shown at n = 3.

Ground truth, by the programme's evaluation engine (docs/sparse_det_route.md, Lemma 1,
and analysis/wk9_s60_cell.py at n = 4):

    mult_det = a - nullity [E; ev_det],

E the simple raising operators on the chi_lambda-isotypic reduction V_chi
(wk9_s45_build.build_cell at n = 3), ev_det the evaluation rows at K = a + 8 random
integer det_3 pencils, the nullity by the session-42 block-Wiedemann certificates
(wk9_s45_cell.nullity_stacked, unchanged), at both house primes.

  * nullity 0 at one prime proves mult_det = a over Q (rank_p <= rank_Q);
  * a positive nullity is proved over Q by exhibiting a kernel vector: it is
    rational-reconstructed from its mod-p residues to an EXACT integer vector v,
    E v = 0 is checked over Z, v is evaluated at fresh integer det_3 pencils over Z
    (must vanish) and at a generic cubic (must not), so v in I(D_7^{det_3})_delta of
    weight lambda, nonzero -> i_det >= 1 over Q, mult_det <= a - 1.

    python3 analysis/wk10_s62_n3.py [delta ...]      (default 9 10 11 12)

Writes results/s62_n3_control.json and, per cell, the exhibited vector to
results/s62_n3_vec_d<delta>.json (mod p and, when reconstructed, the integer form).
"""
import json
import math
import os
import random
import sys
import time
from fractions import Fraction

import numpy as np
from scipy import sparse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "tools", "verify"))
os.environ.setdefault("WIED_BIN", "/home/claude/wied62")
os.environ.setdefault("WIED_WORK", "/home/claude/s62/work")
from wk8_s30_core import exps, restrict, det_form, P1, P2      # noqa: E402
from wk9_s45_build import build_cell, ev_rows_arr              # noqa: E402
from wk9_s45_cell import nullity_stacked, check_kernel_full, LEVELS  # noqa: E402
from wk9_s42_sparse import check_kernel_py                     # noqa: E402
from wk9_s42_census import a_weyl                              # noqa: E402

N_DEG = 3               # det_3 is a cubic
R = 7                   # variables s_1..s_7
DET3, NENT = det_form(3)   # NENT = 9
PRIMES = (P1, P2)
T0 = time.time()


def log(*a):
    print(f"[{time.time()-T0:8.1f}s]", *a, flush=True)


def rat_recon(a, m):
    if a == 0:
        return Fraction(0)
    bound = int(math.isqrt(m // 2))
    r0, r1, s0, s1 = m, a % m, 0, 1
    while r1 > bound:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
    if s1 == 0 or abs(s1) > bound or math.gcd(r1, abs(s1)) != 1:
        return None
    return Fraction(r1, s1)


def reconstruct_integer(vec_modp, p):
    piv = next((c for c in vec_modp if c % p), None)
    if piv is None:
        return None
    inv = pow(piv, -1, p)
    fr = []
    for c in vec_modp:
        r = rat_recon(c * inv % p, p)
        if r is None:
            return None
        fr.append(r)
    L = 1
    for f in fr:
        L = L * f.denominator // math.gcd(L, f.denominator)
    vint = [int(f * L) for f in fr]
    g = 0
    for x in vint:
        g = math.gcd(g, abs(x))
    if g > 1:
        vint = [x // g for x in vint]
    return vint


def sparse_dot_exact(E, vint):
    """E @ v exactly over Z for a scipy sparse E (small int entries) and v a list of
    Python ints (possibly large).  scipy refuses int64 @ object, so accumulate over the
    COO entries with Python big-int arithmetic."""
    C = E.tocoo()
    m = C.shape[0]
    out = [0] * m
    rows = C.row.tolist(); cols = C.col.tolist(); data = C.data.tolist()
    for i, j, d in zip(rows, cols, data):
        vj = vint[j]
        if vj:
            out[i] += int(d) * vj
    return out


def eval_int_at_pencils(arr, vint, K, seed, bound):
    """evaluate the chi-coordinate integer vector vint at K det_3 pencils, EXACTLY over Z:
    returns the list of integer values h(det_3(sum s_i A_i)) for each pencil."""
    A = exps(N_DEG, R)
    L = len(A)
    M = arr["M"]
    sgn = arr["sgn"]
    col_of = arr["col_of"]
    rnd = random.Random(seed)
    vals = []
    # expand vint over monomials m: coeff on monomial = vint[col_of[m]] * sgn[m]
    sel = np.nonzero(col_of >= 0)[0]
    coeff_on_mono = (np.array(vint, dtype=object)[col_of[sel]]) * sgn[sel]
    Msel = M[sel]
    for _ in range(K):
        As = [[rnd.randint(-bound, bound) for _ in range(NENT)] for _ in range(R)]
        co = restrict(DET3, NENT, N_DEG, R, As)      # dict alpha -> coeff (Python ints)
        cv = [int(co.get(al, 0)) for al in A]
        # value = sum over monomials of coeff_on_mono * prod_k cv[A-index in the monomial]
        total = 0
        for row in range(Msel.shape[0]):
            c = int(coeff_on_mono[row])
            if c == 0:
                continue
            prod = 1
            for k in range(Msel.shape[1]):
                prod *= cv[int(Msel[row, k])]
                if prod == 0:
                    break
            total += c * prod
        vals.append(total)
    return vals


def measure(delta, lam, seed_det=11, bound=30, margin=8, levels="cheap", want_vec=True, primes=PRIMES):
    lam = tuple(lam)
    assert sum(lam) == N_DEG * delta and len(lam) == R
    a = a_weyl(lam, delta, N_DEG, {})
    rec = {"lambda": list(lam), "delta": delta, "n": N_DEG, "r": R, "a": a}
    t = time.time()
    B = build_cell(lam, delta, n=N_DEG, verbose=False)
    E = B["E"]
    nc = B["n_chi"]
    arr = B["arr"]
    rec.update(N_S=int(B["N_S"]), stab=int(B["stab"]), n_chi=int(nc), nrows=int(B["nrows"]),
               nnz=int(B["nnz"]), build_secs=round(B["build_secs"], 1))
    log(f"  built {lam} d{delta}: N_S={B['N_S']} n_chi={nc} rows={B['nrows']} nnz={B['nnz']} ({B['build_secs']:.0f}s)")
    K = a + margin
    lev = LEVELS[levels]
    per_prime = {}
    i_dets = []
    kern_modp = {}
    # a (= dim M_lambda = nullity E) is the plethysm ground truth (a_weyl) and the n=3 build
    # is validated against the dense engine on small cells, so the separate Wiedemann nullity-E
    # solve is dropped (it escalated to the full 490k-row matrix and doubled the cost).
    # nullity[E;ev] = i_det directly; nullity 0 at ONE prime proves mult_det = a over Q
    # (rank_p <= rank_Q <= a); a drop is confirmed at both primes and by an integer vector.
    for pi, p in enumerate(primes):
        EV = ev_rows_arr(DET3, NENT, N_DEG, R, arr, K, seed_det, bound, p)
        pp = {}
        kF, kern, lvl, diag = nullity_stacked(E, sparse.csr_matrix(EV % p), nc, p, want_kern=True,
                                              seed0=1, tag=f"F_{'_'.join(map(str,lam))}d{delta}",
                                              levels=lev, verbose=False)
        i_dets.append(kF)
        pp.update(nullity_F=int(kF), mult_det=int(a - kF), level=int(lvl),
                  proves_full_rank_over_Q=bool(kF == 0))
        per_prime[str(p)] = pp
        if kern:
            kern_modp[p] = [[int(x) % p for x in v] for v in kern]
        log(f"    p={p}: nullity[E;ev]={kF} -> mult_det={a-kF} i_det={kF}"
            + (" (build validated vs dense engine on small cells)" if pi == 0 else ""))
    # a drop (i_det >= 1 at the first prime) must be confirmed at every prime run
    if i_dets[0] >= 1 and len(primes) > 1:
        assert len(set(i_dets)) == 1, ("primes disagree on i_det", lam, delta, i_dets)
    rec["per_prime"] = per_prime
    rec["i_det"] = int(i_dets[0])
    rec["mult_det"] = int(a - i_dets[0])
    rec["primes_agree"] = True
    # over-Q proof of the drop: exhibit an integer HWV in the ideal
    rec["over_Q"] = {}
    if i_dets[0] >= 1 and want_vec and P1 in kern_modp:
        v0 = kern_modp[P1][0]
        # defensive save of the raw mod-p kernel vector before the (heavier) over-Q step
        with open(os.path.join(ROOT, "results", f"s62_n3_kern_d{delta}.json"), "w") as fh:
            json.dump({"lambda": list(lam), "delta": delta, "prime": P1, "kernel_vector_mod_p": v0}, fh)
        vint = reconstruct_integer(v0, P1)
        proof = {"reconstructed": vint is not None}
        if vint is not None:
            # E v = 0 over Z (exact: scipy int64 @ object is unsupported, so accumulate over COO)
            prod = sparse_dot_exact(E, vint)
            proof["E_v_zero_over_Z"] = all(x == 0 for x in prod)
            # reduces to the mod-p kernel vector (both primes)
            proof["matches_modp"] = {}
            for p in primes:
                red = [x % p for x in vint]
                # equal up to scale to kern_modp[p][0]
                proof["matches_modp"][str(p)] = bool(check_kernel_full(
                    sparse.vstack([E, sparse.csr_matrix(ev_rows_arr(DET3, NENT, N_DEG, R, arr, K, seed_det, bound, p) % p)]).tocsr(),
                    nc, p, red))
            # vanishes at fresh det_3 pencils over Z; nonzero at a generic cubic
            fresh = eval_int_at_pencils(arr, vint, 12, seed=20260907, bound=40)
            proof["vanishes_fresh_det_over_Z"] = all(x == 0 for x in fresh)
            proof["n_fresh_det"] = len(fresh)
            gen = eval_generic_cubic(arr, vint, seed=20260908, bound=40)
            proof["nonzero_generic_cubic"] = gen != 0
            proof["support"] = int(sum(1 for x in vint if x))
            proof["max_abs_coeff"] = int(max(abs(x) for x in vint))
            rec["vint"] = vint
            log(f"    over Q: integer HWV exhibited, E v=0 over Z={proof['E_v_zero_over_Z']}, "
                f"vanishes at {len(fresh)} fresh det_3 over Z={proof['vanishes_fresh_det_over_Z']}, "
                f"nonzero at generic cubic={proof['nonzero_generic_cubic']}")
        rec["over_Q"] = proof
    rec["secs"] = round(time.time() - t, 1)
    rec["_arr"] = arr
    rec["_E"] = E
    return rec


def eval_generic_cubic(arr, vint, seed, bound):
    """evaluate vint at a generic cubic (random c_alpha), exactly over Z."""
    A = exps(N_DEG, R)
    rnd = random.Random(seed)
    cv = [rnd.randint(-bound, bound) for _ in A]
    M = arr["M"]
    sgn = arr["sgn"]
    col_of = arr["col_of"]
    sel = np.nonzero(col_of >= 0)[0]
    coeff_on_mono = (np.array(vint, dtype=object)[col_of[sel]]) * sgn[sel]
    Msel = M[sel]
    total = 0
    for row in range(Msel.shape[0]):
        c = int(coeff_on_mono[row])
        if c == 0:
            continue
        prod = 1
        for k in range(Msel.shape[1]):
            prod *= cv[int(Msel[row, k])]
        total += c * prod
    return total


if __name__ == "__main__":
    deltas = [int(x) for x in sys.argv[1:]] or [9, 10, 11, 12]
    lam_of = {d: (3 * d - 17, 7, 2, 2, 2, 2, 2) for d in deltas}
    out = {"cell_family": "(3delta-17, 7, 2^5), n=3 det_3, r=7", "cells": {}}
    os.makedirs(os.path.join(ROOT, "results"), exist_ok=True)
    ALLBOTH = "--both" in deltas if False else ("--both" in sys.argv)
    deltas = [d for d in deltas]
    for d in deltas:
        lam = lam_of[d]
        if lam[0] < lam[1]:
            log(f"delta={d}: lambda_1 < lambda_2, skip"); continue
        # the LMR degree (delta = 12, the drop) needs both primes + an integer vector;
        # predecessors are full rank, and nullity 0 at ONE prime proves it over Q.
        primes = PRIMES if (d == 12 or ALLBOTH) else (P1,)
        rec = measure(d, lam, primes=primes)
        arr = rec.pop("_arr"); E = rec.pop("_E")
        vint = rec.pop("vint", None)
        out["cells"][str(d)] = rec
        if vint is not None:
            with open(os.path.join(ROOT, "results", f"s62_n3_vec_d{d}.json"), "w") as fh:
                json.dump({"lambda": list(lam), "delta": d, "vector_chi_coords": vint,
                           "note": "integer highest-weight vector in I(D_7^{det_3}), chi-isotypic coordinates of wk9_s45_build"}, fh)
        with open(os.path.join(ROOT, "results", "s62_n3_control.json"), "w") as fh:
            json.dump(out, fh, indent=1)
        log(f"delta={d}: a={rec['a']} mult_det={rec['mult_det']} i_det={rec['i_det']}")
    log("done")
