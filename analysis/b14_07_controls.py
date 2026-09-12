#!/usr/bin/env python3
"""B14-07 -- the controls, each run twice: once on the true input and once on a
deliberately corrupted input that MUST make it fail.

A control that does not fail on its failure arm is reported as VOID, not as a
pass (PROVED.md: check_must_be_able_to_fail -- and the batch-14 reachability
script is the seventh instance, which is why every arm here is exercised).

    C1  DP evaluator vs banked rows_native        fail arm: two letters swapped
    C2  row-system identity at degree 14          fail arm: transport exponent 13 - d
    C3  independent algorithm (Identity 3)        fail arm: one symbol + 1
    C5  signed CRT round trip                     fail arm: an integer above H_14
    C6  exact INTEGER evaluator, no modulus       fail arm: entry altered by 1
    C9  negative_control_forced (span < l(lambda)) fail arm: a generic point

C4, C7 and C8 live in b14_07_kernel.py where their data is.

    --controls C1,C2,...     which to run (default all)
    --entries N              how many entries for C6 (default 3)

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
"""
import argparse
import copy
import json
import math
import os
import random
import sys
import time

from flint import fmpz_mat

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)

from wk8_s30_core import exps                                                # noqa: E402
from wk11_s69_circuit import (Filling, sym_table, fast_eval_c, cached_order,  # noqa: E402
                              unit_structure, letter_tensors)
from wk12_s74_dp import dp_eval_compact                                      # noqa: E402

N, H, DEG = 4, 9, 14
OUT = os.path.join(ROOT, "results", "b14_07")
T0 = time.time()
_E = exps(N, H)
IU = _E.index(tuple([N] + [0] * (H - 1)))
_EIDX = {a: k for k, a in enumerate(_E)}
_A, _idx, FACT, TAB = sym_table(N, H)
H14 = (2 ** 15) * (math.factorial(9) ** 2) * ((24 * 7 * 7) ** DEG)
P1 = 2147483647


def log(*a):
    print(f"[{time.time()-T0:7.1f}s]", *a, flush=True)


def syms(cv, p):
    return [(int(cv[a]) % p) * FACT[a] % p for a in range(len(_E))]


def syms_exact(cv):
    return [FACT[a] * int(cv[a]) for a in range(len(_E))]


def quartic_cv(lin, cub_exps, cub):
    cv = [0] * len(_E)
    for b, cb in zip(cub_exps, cub):
        if cb == 0:
            continue
        for i in range(H):
            if lin[i] == 0:
                continue
            al = list(b)
            al[i] += 1
            cv[_EIDX[tuple(al)]] += lin[i] * cb
    return cv


# --------------------------------------------------- exact integer Identity 3
def exact_eval_identity3(F, msym_int):
    """F_T over Z with no modulus at all: Identity 3 (inclusion-exclusion over
    subsets of the h row-units, integer determinants).  This is a different
    ALGORITHM from the compact-state DP used in production, not a different
    implementation of the same one."""
    h = F.h
    units, neither, pi_sign, _ = unit_structure(F)
    LT = letter_tensors(F, msym_int, None, TAB)   # pure indexing, no arithmetic

    def bits_of(l, s):
        b = 0
        for q, (e, side) in enumerate(LT[l][2]):
            se = (s >> e) & 1
            b |= (se if side == 0 else 1 - se) << q
        return b

    total = 0
    for s in range(1 << F.n2):
        ssign = -1 if bin(s).count("1") % 2 else 1
        Nf = 1
        for l in neither:
            Nf *= LT[l][3][(None, None, bits_of(l, s))]
            if Nf == 0:
                break
        if Nf == 0:
            continue
        Ms = []
        for u in units:
            if u[0] == "shared":
                l = u[1]; b = bits_of(l, s); T = LT[l][3]
                Ms.append([[T[(i, j, b)] for j in range(h)] for i in range(h)])
            else:
                l, m = u[1], u[2]
                bl, bm = bits_of(l, s), bits_of(m, s)
                v = [LT[l][3][(i, None, bl)] for i in range(h)]
                w = [LT[m][3][(None, j, bm)] for j in range(h)]
                Ms.append([[v[i] * w[j] for j in range(h)] for i in range(h)])
        acc = 0
        for S in range(1 << h):
            if S == 0:
                continue
            sm = [[0] * h for _ in range(h)]
            for k in range(h):
                if (S >> k) & 1:
                    Mk = Ms[k]
                    for i in range(h):
                        ri, mi = sm[i], Mk[i]
                        for j in range(h):
                            ri[j] += mi[j]
            dS = int(fmpz_mat(h, h, [sm[i][j] for i in range(h) for j in range(h)]).det())
            if dS:
                acc += -dS if (h - bin(S).count("1")) % 2 else dS
        total += ssign * Nf * acc
    return pi_sign * total


# ------------------------------------------------------------------- controls
def load_common():
    src = json.load(open(os.path.join(ROOT, "results", "s74", "source.json")))
    ent = [e for e in src["entries"] if e["rung"] <= DEG]
    P = json.load(open(os.path.join(ROOT, "results", "b14_prep", "points", "P14.json")))
    cub = [tuple(b) for b in P["cubic_exponents"]]
    return ent, P, cub


def c1(ent, res):
    """DP evaluator against banked rows_native, and a corrupted filling."""
    col = json.load(open(os.path.join(ROOT, "results", "s74",
                                      f"columns_red_{P1}.json")))
    rn, cvs = col["rows_native"], col["points_cv"]
    js = [0, 1, 2, 3]
    ok = bad = 0
    ms = {j: syms(cvs[j], P1) for j in js}
    for e in ent:
        key = json.dumps(e["key"])
        F = Filling.from_json(e["native"])
        for j in js:
            v = dp_eval_compact(F, ms[j], P1, TAB) % P1
            if v == rn[key][j] % P1:
                ok += 1
            else:
                bad += 1
    # failure arm: swap two letters of one filling's first tall column
    e = ent[0]
    nat = copy.deepcopy(e["native"])
    nat["C1"][0], nat["C1"][1] = nat["C1"][1], nat["C1"][0]
    Fb = Filling.from_json(nat)
    vb = dp_eval_compact(Fb, ms[0], P1, TAB) % P1
    arm_failed = (vb != rn[json.dumps(e["key"])][0] % P1)
    # the agreement must not be between two zeros
    nz = sum(1 for e in ent for j in js if rn[json.dumps(e["key"])][j] % P1 != 0)
    res["C1"] = dict(rows=len(ent), points=len(js), agree=ok, disagree=bad,
                     true_arm_pass=(bad == 0),
                     nonzero_banked_values=nz, total_compared=len(ent) * len(js),
                     failure_arm_detected=bool(arm_failed),
                     void=not (arm_failed and nz > 0))
    log(f"C1 banked rows_native: {ok}/{ok+bad} agree ({nz} of them nonzero); "
        f"failure arm detected={arm_failed}")


def c2(ent, P, cub, res):
    """row-system identity: literal filling climbed to 14 == native * u^(14-d)."""
    pt = P["points"][0]
    cv = quartic_cv(pt["linear"], cub, pt["cubic_coefficients"])
    ms = syms(cv, P1)
    u = ms[IU]
    ok = bad = 0
    sample = [ent[0], ent[1], ent[2], ent[40], ent[92]]
    for e in sample:
        F = Filling.from_json(e["native"])
        d = F.delta
        # climb the native filling to degree 14 the way s74 climbs to 24
        one = list(F.one)
        nxt = d
        for _ in range(DEG - d):
            one += [nxt] * N
            nxt += 1
        Fup = Filling(F.h, F.n, DEG, F.C1, F.C2, F.two, one)
        direct = dp_eval_compact(Fup, ms, P1, TAB) % P1
        viatr = dp_eval_compact(F, ms, P1, TAB) * pow(u, DEG - d, P1) % P1
        ok += (direct == viatr)
        bad += (direct != viatr)
    # failure arm: the wrong transport exponent
    e = sample[0]
    F = Filling.from_json(e["native"])
    d = F.delta
    one = list(F.one); nxt = d
    for _ in range(DEG - d):
        one += [nxt] * N
        nxt += 1
    Fup = Filling(F.h, F.n, DEG, F.C1, F.C2, F.two, one)
    direct = dp_eval_compact(Fup, ms, P1, TAB) % P1
    wrong = dp_eval_compact(F, ms, P1, TAB) * pow(u, DEG - 1 - d, P1) % P1
    arm_failed = (direct != wrong)
    res["C2"] = dict(sample=len(sample), agree=ok, disagree=bad,
                     true_arm_pass=(bad == 0),
                     failure_arm_detected=bool(arm_failed), void=not arm_failed)
    log(f"C2 row-system identity: {ok}/{ok+bad} agree; failure arm detected={arm_failed}")


def referenced_symbols(F):
    """the set of msym indices this filling actually reads.  Passing the identity
    list as the symbol vector makes letter_tensors return the indices themselves."""
    LT = letter_tensors(F, list(range(len(_E))), None, TAB)
    used = set()
    for (_, _, _, T) in LT:
        used.update(T.values())
    return used


def c3(ent, P, cub, res):
    """independent ALGORITHM: Identity 3 (fast_eval_c) vs the compact DP.

    Two guards the first version of this control lacked, both of which made it
    unable to fail: the failure arm perturbed a symbol index the filling never
    reads, and nothing checked that the agreeing values were not both zero."""
    pt = P["points"][0]
    cv = quartic_cv(pt["linear"], cub, pt["cubic_coefficients"])
    ms = syms(cv, P1)
    ok = bad = 0
    vals = []
    for e in [ent[0], ent[50]]:
        F = Filling.from_json(e["native"])
        a = fast_eval_c(F, ms, P1, TAB) % P1
        b = dp_eval_compact(F, ms, P1, TAB) % P1
        vals.append(int(a))
        ok += (a == b)
        bad += (a != b)
    nonvacuous = all(v != 0 for v in vals)

    F = Filling.from_json(ent[0]["native"])
    true_dp = dp_eval_compact(F, ms, P1, TAB) % P1

    # failure arm (a): perturb a symbol the filling DOES read
    used = sorted(referenced_symbols(F))
    ms2 = list(ms)
    ms2[used[len(used) // 2]] = (ms2[used[len(used) // 2]] + 1) % P1
    arm_a = (fast_eval_c(F, ms2, P1, TAB) % P1) != true_dp

    # failure arm (b): a deliberately wrong tensor normalisation -- every symbol
    # doubled, which must scale F_T by 2^delta and so must be rejected
    ms3 = [(2 * x) % P1 for x in ms]
    arm_b = (fast_eval_c(F, ms3, P1, TAB) % P1) != true_dp

    arm_failed = bool(arm_a and arm_b)
    res["C3"] = dict(sample=ok + bad, agree=ok, disagree=bad,
                     true_arm_pass=(bad == 0),
                     values_nonzero=bool(nonvacuous),
                     failure_arm_perturbed_used_symbol=bool(arm_a),
                     failure_arm_wrong_normalisation=bool(arm_b),
                     failure_arm_detected=arm_failed,
                     void=not (arm_failed and nonvacuous),
                     note=("first version was VOID: it perturbed symbol index 7, "
                           "which this filling never reads, so the arm could not "
                           "fail.  Recorded rather than quietly replaced."))
    log(f"C3 independent algorithm: {ok}/{ok+bad} agree (values nonzero={nonvacuous}); "
        f"failure arms a={arm_a} b={arm_b}")


def c5(res):
    """signed CRT round trip, and an integer that must NOT round-trip."""
    P = json.load(open(os.path.join(ROOT, "results", "b14_prep", "points", "P14.json")))
    primes = P["crt_primes"]
    M = 1
    for p in primes:
        M *= p
    half = M // 2
    rng = random.Random(1407)

    def rt(x):
        a = 0
        m = 1
        for p in primes:
            r = x % p
            # CRT accumulate
            g, inv = m % p, None
            t = (r - a) % p
            inv = pow(m % p, p - 2, p)
            a = a + m * ((t * inv) % p)
            m *= p
        a %= M
        return a if a <= half else a - M

    ok = all(rt(x) == x for x in
             [0, 1, -1, H14, -H14, H14 - 1, rng.randrange(-H14, H14)])
    # failure arm: something larger than H_14 must NOT come back (it wraps)
    big = M - 1                     # far above H_14
    arm_failed = (rt(big) != big)
    res["C5"] = dict(true_arm_pass=bool(ok),
                     failure_arm_detected=bool(arm_failed), void=not arm_failed,
                     note="round trip exact on |x| <= H_14; an integer of size M-1 "
                          "wraps, which is what the |x| <= H_14 check in the kernel "
                          "stage exists to catch")
    log(f"C5 signed CRT round trip: pass={ok}; failure arm detected={arm_failed}")


def c6(ent, P, cub, res, n_entries):
    """exact INTEGER evaluator (no modulus) against the CRT-reconstructed entries."""
    kp = os.path.join(OUT, "A14_exact.json.gz")
    if not os.path.exists(kp):
        res["C6"] = dict(status="NOT REACHED -- exact matrix not yet built")
        log("C6 skipped: exact matrix absent")
        return
    import gzip
    ex = json.load(gzip.open(kp, "rt"))
    Mx = ex["matrix"]
    rows = ex["rows"]
    pts = ex["points"]
    checks = []
    rng = random.Random(7)
    picks = [(0, 0), (2, 1), (92, 2)][:n_entries]
    picks += [(rng.randrange(93), rng.randrange(len(pts)))
              for _ in range(max(0, n_entries - 3))]
    for (i, j) in picks[:n_entries]:
        e = ent[i]
        F = Filling.from_json(e["native"])
        pt = P["points"][j]
        cv = quartic_cv(pt["linear"], cub, pt["cubic_coefficients"])
        msx = syms_exact(cv)
        t = time.time()
        nat = exact_eval_identity3(F, msx)
        val = nat * (msx[IU] ** (DEG - F.delta))
        want = int(Mx[i][j])
        checks.append(dict(row=i, point=pts[j]["id"], rung=rows[i]["rung"],
                           exact=str(val), reconstructed=str(want),
                           agree=(val == want), secs=round(time.time() - t, 1)))
        log(f"C6 entry ({i},{j}) rung {rows[i]['rung']}: agree={val==want} "
            f"({time.time()-t:.1f}s)")
    # failure arm: the same comparison against an entry altered by 1
    arm_failed = False
    if checks:
        i, j = picks[0]
        e = ent[i]
        F = Filling.from_json(e["native"])
        pt = P["points"][j]
        msx = syms_exact(quartic_cv(pt["linear"], cub, pt["cubic_coefficients"]))
        val = exact_eval_identity3(F, msx) * (msx[IU] ** (DEG - F.delta))
        arm_failed = (val != int(Mx[i][j]) + 1)
    res["C6"] = dict(entries=checks, true_arm_pass=all(c["agree"] for c in checks),
                     failure_arm_detected=bool(arm_failed), void=not arm_failed)


def c9(ent, res):
    """negative_control_forced: a point of span < l(lambda) = 9 must read zero on
    every row; a generic point must not."""
    rng = random.Random(9)
    lin = [rng.randint(-7, 7) for _ in range(3)] + [0] * 6        # span <= 3
    cub = []
    cexp = json.load(open(os.path.join(ROOT, "results", "b14_prep", "points",
                                       "P14.json")))["cubic_exponents"]
    for b in cexp:
        cub.append(rng.randint(-7, 7) if all(x == 0 for x in b[3:]) else 0)
    cv = quartic_cv(lin, [tuple(b) for b in cexp], cub)
    ms = syms(cv, P1)
    vals = [dp_eval_compact(Filling.from_json(e["native"]), ms, P1, TAB) % P1
            for e in ent]
    forced_zero = all(v == 0 for v in vals)
    # failure arm: a generic full-span point must NOT read all-zero
    lin2 = [rng.randint(1, 7) for _ in range(H)]
    cub2 = [rng.randint(-7, 7) for _ in cexp]
    ms2 = syms(quartic_cv(lin2, [tuple(b) for b in cexp], cub2), P1)
    vals2 = [dp_eval_compact(Filling.from_json(e["native"]), ms2, P1, TAB) % P1
             for e in ent[:12]]
    arm_failed = any(v != 0 for v in vals2)
    res["C9"] = dict(span=3, weight_length=9, rows=len(ent),
                     all_zero_on_low_span=bool(forced_zero),
                     nonzero_count_on_low_span=sum(1 for v in vals if v),
                     true_arm_pass=bool(forced_zero),
                     failure_arm_detected=bool(arm_failed), void=not arm_failed)
    log(f"C9 forced negative control: all-zero at span 3 = {forced_zero}; "
        f"generic point nonzero = {arm_failed}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--controls", default="C1,C2,C3,C5,C6,C9")
    ap.add_argument("--entries", type=int, default=3)
    a = ap.parse_args()
    want = set(a.controls.split(","))
    os.makedirs(OUT, exist_ok=True)
    ent, P, cub = load_common()
    path = os.path.join(OUT, "controls.json")
    res = json.load(open(path)) if os.path.exists(path) else {}
    res["session"] = "B14-07"
    res["_note"] = ("every control has a true arm and a failure arm; void=true "
                    "means the failure arm did NOT fail and the control is "
                    "therefore not a check at all")
    if "C1" in want: c1(ent, res)
    if "C2" in want: c2(ent, P, cub, res)
    if "C3" in want: c3(ent, P, cub, res)
    if "C5" in want: c5(res)
    if "C9" in want: c9(ent, res)
    if "C6" in want: c6(ent, P, cub, res, a.entries)
    json.dump(res, open(path, "w"), indent=1)
    log(f"wrote {path}")
    voids = [k for k, v in res.items() if isinstance(v, dict) and v.get("void")]
    if voids:
        log(f"VOID CONTROLS (failure arm did not fail): {voids}")


if __name__ == "__main__":
    main()
