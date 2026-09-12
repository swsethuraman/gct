#!/usr/bin/env python3
"""B14-07 -- signed seven-prime CRT, the exact integer matrix A14, and its exact
rational LEFT kernel K14.

Reads results/b14_07/A14_mod_<p>.json for the seven primes of P14.json, forms

    A14[i][j] = native[i][j] * u_j^(14 - d_i)  mod p

at each prime, CRTs to the product modulus, lifts to the SIGNED representative in
(-M/2, M/2], and checks every entry against the re-derived height bound

    H_14 = 2^15 * (9!)^2 * 1176^14

before any of it is believed.  Then over Q:

    K14 = basis of { x in Q^93 : x^T A14 = 0 }        (the LEFT kernel)
    verify  A14^T . K14 = 0,  rank(K14) = k,  rank(A14) = 93 - k.

The kernel dimension is determined on the 192 PRIMARY columns only.  The 20
holdout columns are then used as a control that can fail: a genuine relation must
annihilate them too.

Orientation: source vectors are ROWS and points are COLUMNS.  A14 . K = 0 is the
RIGHT kernel, of dimension >= 99, and is NOT the object wanted.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
"""
import json
import math
import os
import sys
import time

from flint import fmpz_mat

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
OUT = os.path.join(ROOT, "results", "b14_07")
DEG = 14
T0 = time.time()

# the bound re-derived in PREREG section 4, recomputed here from its factors
H14 = (2 ** 15) * (math.factorial(9) ** 2) * ((24 * 7 * 7) ** DEG)


def log(*a):
    print(f"[{time.time()-T0:7.1f}s]", *a, flush=True)


def crt_pair(a1, m1, a2, m2):
    """CRT two coprime residues."""
    g, x, _ = ext_gcd(m1, m2)
    assert g == 1
    m = m1 * m2
    return (a1 + m1 * ((x * (a2 - a1)) % m2)) % m, m


def ext_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = ext_gcd(b, a % b)
    return g, y, x - (a // b) * y


def is_prime(n):
    """deterministic Miller-Rabin, bases 2..37, valid below 2^64."""
    if n < 2:
        return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % q == 0:
            return n == q
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def main():
    P = json.load(open(os.path.join(ROOT, "results", "b14_prep", "points", "P14.json")))
    primes = P["crt_primes"]

    # ---- C7: primality re-verified here, not inherited -------------------
    prim = {p: is_prime(p) for p in primes}
    assert all(prim.values()), f"not all CRT primes are prime: {prim}"
    M = 1
    for p in primes:
        M *= p
    log(f"C7 primality: all {len(primes)} primes verified in-house")
    log(f"H_14 = {H14}  ({H14.bit_length()} bits); 2H = {(2*H14).bit_length()} bits; "
        f"M = {M.bit_length()} bits; margin M/(2H) = {M/(2*H14):.4e}")
    assert M > 2 * H14, "modulus does not exceed 2H -- signed CRT invalid"

    # ---- load per-prime matrices -----------------------------------------
    data = {}
    for p in primes:
        path = os.path.join(OUT, f"A14_mod_{p}.json")
        if not os.path.exists(path):
            log(f"MISSING {path} -- prefix run")
            continue
        d = json.load(open(path))
        if len(d["native"]) != d["n_points"]:
            log(f"p={p} incomplete: {len(d['native'])}/{d['n_points']} points")
            continue
        data[p] = d
    have = [p for p in primes if p in data]
    log(f"complete primes: {len(have)}/{len(primes)} -> {have}")
    if not have:
        sys.exit("no complete prime file")

    ref = data[have[0]]
    rows = ref["rows"]
    pts = ref["points"]
    nR, nP = len(rows), len(pts)
    prim_idx = [q["j"] for q in pts if q["role"] == "primary"]
    hold_idx = [q["j"] for q in pts if q["role"] == "holdout"]
    log(f"{nR} rows x {nP} points ({len(prim_idx)} primary, {len(hold_idx)} holdout)")

    # rows/points identical across primes
    for p in have[1:]:
        assert [r["key"] for r in data[p]["rows"]] == [r["key"] for r in rows]
        assert [q["id"] for q in data[p]["points"]] == [q["id"] for q in pts]

    # ---- C4: u non-vanishing at every point and every prime ---------------
    uzero = []
    for p in have:
        for j in range(nP):
            if data[p]["native"][str(j)]["u"] % p == 0:
                uzero.append((pts[j]["id"], p))
    log(f"C4 u-nonvanishing: {len(uzero)} u-zeros" + (f" {uzero}" if uzero else " (none)"))

    # ---- transported row values mod each prime ----------------------------
    expo = [r["exponent"] for r in rows]
    assert set(expo) == {0, 1, 2}, f"unexpected transport exponents {set(expo)}"
    Amod = {}
    for p in have:
        nat = data[p]["native"]
        cols = []
        for j in range(nP):
            rec = nat[str(j)]
            u = rec["u"] % p
            upow = [1, u % p, u * u % p]
            cols.append([rec["native"][i] * upow[expo[i]] % p for i in range(nR)])
        Amod[p] = cols                      # cols[j][i]
    log("transported row values formed at every prime")

    # ---- signed CRT --------------------------------------------------------
    if len(have) < len(primes):
        log("PREFIX: fewer than seven primes -- signed reconstruction NOT attempted")
        exact = None
    else:
        half = M // 2
        exact = [[0] * nP for _ in range(nR)]
        maxabs = 0
        t = time.time()
        for i in range(nR):
            for j in range(nP):
                a, m = Amod[have[0]][j][i], have[0]
                for p in have[1:]:
                    a, m = crt_pair(a, m, Amod[p][j][i], p)
                x = a if a <= half else a - M
                exact[i][j] = x
                if abs(x) > maxabs:
                    maxabs = abs(x)
        log(f"signed CRT done in {time.time()-t:.1f}s; max |entry| = {maxabs} "
            f"({maxabs.bit_length()} bits)")
        # ---- STOPPING RULE 1: bound violation -----------------------------
        if maxabs > H14:
            sys.exit(f"STOP: bound violation, max |entry| {maxabs} > H_14 {H14}")
        log(f"bound check PASS: max |entry| / H_14 = {maxabs/H14:.6e}")

    # ---- exact rank and LEFT kernel on the primary columns ----------------
    res = dict(session="B14-07", degree=DEG, primes_used=have,
               n_rows=nR, n_primary=len(prim_idx), n_holdout=len(hold_idx),
               H14=str(H14), modulus_bits=M.bit_length(),
               u_zero_points=uzero,
               values_are=ref["values_are"],
               orientation=("rows are source fillings, columns are points; K14 is the "
                            "LEFT kernel: K14 columns x satisfy x^T A14 = 0"))

    # mod-p ranks first (a floor on the rational rank)
    from flint import nmod_mat
    rank_p = {}
    for p in have:
        Mp = nmod_mat(nR, len(prim_idx),
                      [Amod[p][j][i] for i in range(nR) for j in prim_idx], p)
        rank_p[p] = Mp.rank()
    log(f"mod-p ranks on primary columns: {rank_p}")
    res["rank_mod_p_primary"] = {str(k): v for k, v in rank_p.items()}

    if exact is None:
        res["status"] = "PREFIX -- no signed reconstruction"
        res["nullity_ceiling_from_mod_p"] = nR - max(rank_p.values())
        json.dump(res, open(os.path.join(OUT, "K14.json"), "w"), indent=1)
        log("prefix result written")
        return

    Apri = fmpz_mat(nR, len(prim_idx),
                    [exact[i][j] for i in range(nR) for j in prim_idx])
    t = time.time()
    rQ = Apri.rank()
    log(f"rank_Q(A14) on {len(prim_idx)} primary columns = {rQ}  ({time.time()-t:.1f}s)")

    # ---- STOPPING RULE 3: rank contradiction ------------------------------
    if rQ < max(rank_p.values()):
        sys.exit(f"STOP: rank_Q {rQ} < max mod-p rank {max(rank_p.values())} "
                 "-- contradicts rank_floor")

    At = Apri.transpose()                     # (#primary) x 93
    X, nul = At.nullspace()                   # columns of X span {x : A^T x = 0}
    k = nul
    log(f"LEFT kernel dimension k = {k}; 93 - rank = {nR - rQ}")
    assert k == nR - rQ, "nullity and rank disagree"

    K = fmpz_mat(nR, k, [X[i, j] for i in range(nR) for j in range(k)]) if k else None
    res.update(rank_Q_primary=rQ, k=k)

    if k:
        # primitive integer columns
        cols = []
        for j in range(k):
            v = [int(K[i, j]) for i in range(nR)]
            g = 0
            for x in v:
                g = math.gcd(g, abs(x))
            if g > 1:
                v = [x // g for x in v]
            if next((x for x in v if x != 0), 0) < 0:
                v = [-x for x in v]
            cols.append(v)
        Kp = fmpz_mat(nR, k, [cols[j][i] for i in range(nR) for j in range(k)])
        Z = At * Kp
        ann = Z.is_zero()
        rk = Kp.rank()
        log(f"verify A14^T . K14 = 0 : {ann};  rank(K14) = {rk} (want {k});  "
            f"rank(A14) = {rQ} = 93 - {k}")
        res.update(annihilates_primary=bool(ann), rank_K14=int(rk),
                   kernel_columns=cols,
                   max_abs_kernel_entry=max(abs(x) for c in cols for x in c))

        # ---- C8 holdout control -------------------------------------------
        if hold_idx:
            Ah = fmpz_mat(nR, len(hold_idx),
                          [exact[i][j] for i in range(nR) for j in hold_idx])
            Zh = Ah.transpose() * Kp
            res["annihilates_holdout"] = bool(Zh.is_zero())
            log(f"C8 holdout: K14 annihilates the {len(hold_idx)} held-out columns: "
                f"{res['annihilates_holdout']}")
            # the failing arm: a deliberately non-kernel vector must NOT annihilate
            import random
            rng = random.Random(1407)
            bad = fmpz_mat(nR, 1, [rng.randrange(-5, 6) for _ in range(nR)])
            res["c8_failure_arm_rejected"] = not (At * bad).is_zero()
            log(f"C8 failure arm (random vector must fail): "
                f"{res['c8_failure_arm_rejected']}")
    else:
        res["annihilates_primary"] = None
        log("k = 0: no left kernel; the 93 source rows are independent on P14")

    res["max_abs_entry"] = str(maxabs)
    res["max_abs_entry_over_H14"] = maxabs / H14
    json.dump(res, open(os.path.join(OUT, "K14.json"), "w"), indent=1)

    # the exact matrix, gzipped (5 MB rule)
    import gzip
    with gzip.open(os.path.join(OUT, "A14_exact.json.gz"), "wt") as fh:
        json.dump(dict(session="B14-07", degree=DEG,
                       values_are=ref["values_are"] + "; signed integers over Z",
                       rows=rows, points=pts,
                       matrix=[[str(x) for x in r] for r in exact]), fh)
    log("wrote results/b14_07/K14.json and A14_exact.json.gz")


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    main()
