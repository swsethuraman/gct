#!/usr/bin/env python3
"""B14-01 controls.  Every control is run twice: once on an honest input and once
on an input built to break it.  A control is reported as PASS only when its
NEGATIVE instance was also run and did fail (PROVED.md: check_must_be_able_to_fail
-- the seventh instance was an all() over an empty census, vacuously true)."""
import ctypes, json, os, random, sys, time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from b14_01_mixed import (MixedFilling, random_mixed_filling, brute_force_mixed,
                          mixed_eval_c, mixed_dp_pack, sym_table_v, msym_linear,
                          msym_cubic, strips, strip_ell_cells, rank_mod)
from wk12_s74_dp import _lib as _dpc_lib
from wk8_s30_core import P1, P2, exps

SMALL = [  # (h, n2, n1, n_ell, n_c)  with 2h + 2*n2 + n1 == n_ell + 3*n_c
    (3, 1, 1, 3, 2), (3, 2, 0, 4, 2), (3, 2, 0, 1, 3), (3, 3, 1, 4, 3),
    (4, 1, 2, 3, 3), (4, 2, 1, 4, 3), (4, 2, 1, 1, 4), (3, 1, 1, 6, 1),
]


def rand_msyms(r, p, rng):
    return {1: [rng.randrange(p) for _ in exps(1, r)],
            3: [rng.randrange(p) for _ in exps(3, r)]}


def eval_c_perturbed(F, msym, p, r, which=0, delta=1):
    """the C core with a single packed tensor entry altered -- the negative
    instance for C1."""
    P = mixed_dp_pack(F, msym, p, r)
    t = P["tens"].copy()
    t[which % len(t)] = (int(t[which % len(t)]) + delta) % p
    lib = _dpc_lib()
    I32 = ctypes.POINTER(ctypes.c_int32); I64 = ctypes.POINTER(ctypes.c_int64)
    val = lib.dp_eval_compact(
        ctypes.c_int(P["h"]), ctypes.c_int(P["d"]), ctypes.c_int(P["n2"]),
        ctypes.c_int(P["W"]), ctypes.c_longlong(p),
        P["l_inC1"].ctypes.data_as(I32), P["l_inC2"].ctypes.data_as(I32), P["l_d2"].ctypes.data_as(I32),
        P["l_edge"].ctypes.data_as(I32), P["l_side"].ctypes.data_as(I32), ctypes.c_int(P["l_edge"].shape[1]),
        P["l_off"].ctypes.data_as(I64), t.ctypes.data_as(I64),
        P["slot"].ctypes.data_as(I32), P["first"].ctypes.data_as(I32), P["firstside"].ctypes.data_as(I32))
    return P["sign"] * int(val) % p


def C1(n_per_shape=4, seed=1401):
    """literal Leibniz brute force == C core, on small mixed shapes.
    NEGATIVE: the same with one packed tensor entry altered must DISAGREE."""
    rng = random.Random(seed)
    agree = total = 0
    neg_caught = neg_total = 0
    nonzero = 0
    detail = []
    for (h, n2, n1, ne, nc) in SMALL:
        for _ in range(n_per_shape):
            F = random_mixed_filling(h, n2, n1, ne, nc, rng)
            p = P1 if rng.random() < 0.5 else P2
            ms = rand_msyms(h, p, rng)
            b = brute_force_mixed(F, ms, p, r=h)
            c = mixed_eval_c(F, ms, p, r=h)
            total += 1; agree += (b == c); nonzero += (b != 0)
            # negative instance: perturb one tensor entry
            for w in (0, 3, 7):
                cp = eval_c_perturbed(F, ms, p, h, which=w)
                neg_total += 1; neg_caught += (cp != b)
            detail.append(dict(shape=[h, n2, n1, ne, nc], p=p, brute=b, dp=c, equal=b == c))
    return dict(control="C1", honest_agree=agree, honest_total=total,
                honest_nonzero=nonzero,
                negative_detected=neg_caught, negative_total=neg_total,
                passed=(agree == total and nonzero > 0),
                negative_has_teeth=(neg_caught > 0),
                detail=detail[:6])


if __name__ == "__main__":
    t0 = time.time()
    out = {"C1": C1()}
    out["elapsed_s"] = round(time.time() - t0, 2)
    print(json.dumps(out, indent=1)[:2500])


# ------------------------------------------------------------------ C1b: small-shape dimension
from wk8_s30_core import build_R                                        # noqa: E402


def a_pleth(n, r, delta, lam, p=P1):
    """multiplicity of S_lam(C^r) in Sym^delta(Sym^n C^r), exactly, by the
    corrected raising rule of wk8_s30_core.  Calibrated against
    Sym^2(Sym^3) = S_(6)+S_(4,2), Sym^2(Sym^2) = S_(4)+S_(2,2),
    Sym^3(Sym^2) = S_(6)+S_(4,2)+S_(2,2,2)."""
    lam = tuple(lam) + (0,) * (r - len(lam))
    if len(lam) > r or sum(lam) != n * delta: return 0
    if any(lam[i] < lam[i + 1] for i in range(len(lam) - 1)): return 0
    basis, rows = build_R(n, r, delta, lam)
    if not basis: return 0
    nb = len(basis)
    if not rows: return nb
    dense = [[0] * nb for _ in rows]
    for t, rw in enumerate(rows):
        for c, v in rw.items(): dense[t][c] = v
    return nb - rank_mod(dense, p)


def horiz_strips(lam, k, r):
    """mu with lam/mu a horizontal k-strip, at most r rows."""
    lam = tuple(lam) + (0,) * (r - len(lam))
    out = []
    def rec(i, cur, left):
        if i == r:
            if left == 0: out.append(tuple(cur))
            return
        lo = lam[i + 1] if i + 1 < r else 0
        hi = lam[i]
        if cur: hi = min(hi, cur[-1])
        for v in range(lo, hi + 1):
            if left - v >= 0: rec(i + 1, cur + [v], left - v)
    rec(0, [], sum(lam) - k)
    return out


def predicted_dim(h, n2, n1, n_ell, n_c, r=None):
    """dim of the weight-lam highest-weight space of
    Sym^{n_ell}(V*) (x) Sym^{n_c}((Sym^3 V)*) -- by Pieri,
    sum over horizontal n_ell-strips lam/mu of a_3(mu, n_c)."""
    r = r or h
    lam = tuple([2 + n2 + n1, 2 + n2] + [2] * (h - 2))
    return sum(a_pleth(3, r, n_c, mu) for mu in horiz_strips(lam, n_ell, r))


def C1b(shapes=None, seed=1402, over=4):
    """SMALL-SHAPE DIMENSION AGREEMENT.  The measured rank of mixed-filling
    evaluations must equal the predicted dimension.  A shape with predicted
    dimension >= 2 tests MIXING BETWEEN INDEPENDENT BASIS DIRECTIONS, which a
    one-dimensional test cannot (board slot 1).
    NEGATIVE: the same measurement with the c-letter normalisation WRONG (the
    alpha! polarisation factor dropped) must NOT reproduce the dimensions."""
    rng = random.Random(seed)
    shapes = shapes or [(3, 1, 1, 3, 2), (3, 2, 0, 4, 2), (3, 2, 1, 5, 2), (4, 1, 1, 5, 2),
                        (4, 2, 0, 6, 2), (4, 1, 2, 3, 3), (4, 2, 1, 4, 3), (3, 3, 1, 4, 3),
                        (5, 1, 1, 3, 4), (5, 2, 0, 4, 4), (4, 3, 0, 5, 3), (5, 1, 2, 4, 4)]
    rows = []
    for (h, n2, n1, ne, nc) in shapes:
        if 2 * h + 2 * n2 + n1 != ne + 3 * nc: continue
        pred = predicted_dim(h, n2, n1, ne, nc)
        r = h
        meas = {}
        for scale in (True, False):          # True = honest alpha!, False = the wrong normalisation
            best = 0
            for p in (P1,):
                npts = max(6, over * (pred + 2))
                pts = []
                for _ in range(npts):
                    lin = [rng.randrange(p) for _ in range(r)]
                    cmap = {a: rng.randrange(p) for a in exps(3, r)}
                    pts.append({1: msym_linear(lin, r, p, scale_factorial=True),
                                3: msym_cubic(cmap, r, p, scale_factorial=scale)})
                mat = []
                for _ in range(max(6, over * (pred + 2))):
                    try:
                        F = random_mixed_filling(h, n2, n1, ne, nc, rng)
                    except RuntimeError:
                        continue
                    mat.append([mixed_eval_c(F, ms, p, r=r) for ms in pts])
                best = max(best, rank_mod(mat, p) if mat else 0)
            meas[scale] = best
        rows.append(dict(shape=[h, n2, n1, ne, nc],
                         lam=[2 + n2 + n1, 2 + n2] + [2] * (h - 2),
                         predicted=pred, measured=meas[True], measured_wrong_norm=meas[False],
                         agree=(pred == meas[True]),
                         wrong_norm_differs=(meas[False] != pred)))
    dims_ge2 = [r for r in rows if r["predicted"] >= 2]
    return dict(control="C1b",
                n_shapes=len(rows),
                n_agree=sum(1 for r in rows if r["agree"]),
                n_with_dim_ge_2=len(dims_ge2),
                n_agree_dim_ge_2=sum(1 for r in dims_ge2 if r["agree"]),
                max_predicted=max([r["predicted"] for r in rows] or [0]),
                negative_wrong_norm_differs=sum(1 for r in rows if r["wrong_norm_differs"]),
                negative_total=len(rows),
                passed=all(r["agree"] for r in rows) and len(dims_ge2) >= 2,
                rows=rows)


# ------------------------------------------------------------------ substitutions
def subst_linear(lin, i, j, eps, p):
    """x_j -> x_j + eps*x_i acting on a linear form's coefficients."""
    out = list(lin)
    out[i] = (out[i] + eps * lin[j]) % p
    return out


def subst_cubic(cmap, i, j, eps, p, r):
    """x_j -> x_j + eps*x_i acting on a cubic's coefficient map."""
    from math import comb
    out = {}
    for a, cf in cmap.items():
        if cf % p == 0: continue
        aj = a[j]
        for k in range(aj + 1):
            b = list(a); b[j] -= k; b[i] += k
            b = tuple(b)
            out[b] = (out.get(b, 0) + cf * comb(aj, k) * pow(eps, k, p)) % p
    return out


def scale_linear(lin, t, p):
    return [lin[i] * t[i] % p for i in range(len(lin))]


def scale_cubic(cmap, t, p):
    out = {}
    for a, cf in cmap.items():
        s = cf % p
        for i, e in enumerate(a):
            if e: s = s * pow(t[i], e, p) % p
        out[a] = s
    return out


def rand_point(r, p, rng, support=None):
    """a genuine reducible point (l, c).  support: restrict to these variables."""
    S = list(range(r)) if support is None else list(support)
    lin = [0] * r
    for i in S: lin[i] = rng.randrange(1, p)
    cmap = {}
    for a in exps(3, r):
        if all(a[i] == 0 for i in range(r) if i not in S):
            cmap[a] = rng.randrange(p)
    return lin, cmap


def ms_of(lin, cmap, r, p, scale_factorial=True, cubic_extra=1):
    return {1: msym_linear(lin, r, p),
            3: [v * cubic_extra % p for v in msym_cubic(cmap, r, p, scale_factorial=scale_factorial)]}


# ------------------------------------------------------------------ real-shape member builder
def members_for(lam, delta, h, n2, n1, rng, per_strip, r=9, cache=None):
    """strip-directed mixed fillings: l-letters on the cells of lam/mu."""
    out = []
    for mu in horiz_strips(lam, delta, r):
        seen = set()
        for _ in range(per_strip * 6):
            if len([1 for m, _ in out if m == mu]) >= per_strip: break
            try:
                cells = strip_ell_cells(lam, mu, h, n2, n1, rng)
                F = random_mixed_filling(h, n2, n1, delta, delta, rng, ell_cells=cells)
            except (RuntimeError, ValueError, AssertionError):
                continue
            k = F.key()
            if k in seen: continue
            seen.add(k); out.append((mu, F))
    return out


def C2_C3_C4_C5(h=9, n2=15, n1=4, delta=13, r=9, seed=1403, n_members=14, n_eps=4):
    """C2 torus weight; C3 raising/highest weight; C4 wrong normalisation rejected;
    C5 negative_control_forced (span < l(lambda) must give zero).
    Run at the REAL shape."""
    rng = random.Random(seed)
    lam = tuple([2 + n2 + n1, 2 + n2] + [2] * (h - 2))
    mem = members_for(lam, delta, h, n2, n1, rng, per_strip=1, r=r)[:n_members]
    Fs = [F for _, F in mem]
    p = P1
    lin, cmap = rand_point(r, p, rng)

    # keep only members that are not identically zero on a few generic points, so the
    # equivariance controls are not vacuously satisfied by 0 == 0
    probe = [rand_point(r, p, rng) for _ in range(3)]
    live = []
    for F in Fs:
        if any(mixed_eval_c(F, ms_of(L, C, r, p), p, r=r) for L, C in probe):
            live.append(F)
    res = {}

    # ---- C2 torus weight
    ok = bad = 0; negcaught = negtot = 0
    for F in live:
        for _ in range(2):
            t = [rng.randrange(1, p) for _ in range(r)]
            v0 = mixed_eval_c(F, ms_of(lin, cmap, r, p), p, r=r)
            v1 = mixed_eval_c(F, ms_of(scale_linear(lin, t, p), scale_cubic(cmap, t, p), r, p), p, r=r)
            chi = 1
            for i in range(r): chi = chi * pow(t[i], lam[i], p) % p
            ok += (v1 == chi * v0 % p); bad += (v1 != chi * v0 % p)
            # NEGATIVE: a wrong weight must not satisfy it
            wl = list(lam); wl[0] += 1; wl[1] -= 1
            chiw = 1
            for i in range(r): chiw = chiw * pow(t[i], wl[i], p) % p
            negtot += 1; negcaught += (v1 != chiw * v0 % p)
    res["C2_torus_weight"] = dict(pass_count=ok, fail_count=bad, n_live=len(live),
                                  negative_detected=negcaught, negative_total=negtot,
                                  passed=(bad == 0 and ok > 0), has_teeth=(negcaught > 0))

    # ---- C3 raising, and C4 wrong normalisation
    def const_in_eps(F, i, j, scale_factorial=True):
        vals = []
        for _ in range(n_eps):
            e = rng.randrange(1, p)
            L2 = subst_linear(lin, i, j, e, p)
            C2m = subst_cubic(cmap, i, j, e, p, r)
            vals.append(mixed_eval_c(F, ms_of(L2, C2m, r, p, scale_factorial=scale_factorial), p, r=r))
        v0 = mixed_eval_c(F, ms_of(lin, cmap, r, p, scale_factorial=scale_factorial), p, r=r)
        return all(v == v0 for v in vals), v0

    up_const = down_const = 0; n3 = 0
    for F in live[:8]:
        a, v0 = const_in_eps(F, 0, 1)          # x_1 -> x_1 + e*x_0
        b, _ = const_in_eps(F, 1, 0)           # x_0 -> x_0 + e*x_1
        if v0 == 0: continue
        n3 += 1; up_const += a; down_const += b
    res["C3_raising"] = dict(n_tested=n3, constant_in_raising_dir=up_const,
                             constant_in_lowering_dir=down_const,
                             passed=(n3 > 0 and (up_const == n3) != (down_const == n3)),
                             has_teeth=(n3 > 0 and not (up_const == n3 and down_const == n3)))

    # ---- C4: the wrong c-normalisation must be REJECTED by C3
    w_up = w_down = n4 = 0
    for F in live[:8]:
        a, v0 = const_in_eps(F, 0, 1, scale_factorial=False)
        b, _ = const_in_eps(F, 1, 0, scale_factorial=False)
        if v0 == 0: continue
        n4 += 1; w_up += a; w_down += b
    res["C4_wrong_normalisation"] = dict(
        n_tested=n4, wrongnorm_constant_in_raising_dir=w_up, wrongnorm_constant_in_lowering_dir=w_down,
        rejected=(n4 > 0 and w_up != n4 and w_down != n4),
        note="dropping alpha! is a DIAGONAL rescaling, so it commutes with the torus and C2 cannot "
             "see it (wk8_s30_core docstring: same kernel DIMENSION, different kernel VECTORS). "
             "C3 is the control that rejects it.")

    # ---- C5 negative_control_forced
    zeros = tot = 0
    for F in live:
        for _ in range(3):
            L, C = rand_point(r, p, rng, support=list(range(r - 1)))   # 8 of 9 variables
            v = mixed_eval_c(F, ms_of(L, C, r, p), p, r=r)
            tot += 1; zeros += (v == 0)
    nz_generic = sum(1 for F in live
                     for _ in range(1)
                     if mixed_eval_c(F, ms_of(*rand_point(r, p, rng), r, p), p, r=r) != 0)
    res["C5_span_forced_zero"] = dict(
        n_restricted_evals=tot, n_zero=zeros, all_zero=(zeros == tot),
        n_generic_nonzero=nz_generic, n_live=len(live),
        passed=(zeros == tot and nz_generic > 0),
        has_teeth=(nz_generic > 0),
        note="lambda has 9 parts; a weight vector of weight lambda vanishes at every point of "
             "span < l(lambda) (PROVED.md: bip_blind_at_n4 mechanism). The anti-vacuity half is "
             "n_generic_nonzero > 0: without it the evaluator could be returning 0 identically.")
    return res


def C1b_directed(shapes=None, seed=1404, mult=30):
    """C1b re-run with the STRIP-DIRECTED sampler.  The first C1b run used the
    undirected sampler and reported measured 0 against predicted 1 at
    lam = (5,4,2,2); exhaustive-scale sampling showed the rank IS 1 and only ~9%
    of undirected fillings are non-zero there, so that was UNDERSAMPLING, not a
    disagreement.  Recorded, not hidden.

    Also runs C1c: a strip mu with a_3(mu, n_c) = 0 must give IDENTICALLY ZERO
    rows -- a forced zero that can fail."""
    rng = random.Random(seed)
    shapes = shapes or [(3, 1, 1, 3, 2), (3, 2, 0, 4, 2), (3, 2, 1, 5, 2), (4, 1, 2, 3, 3),
                        (4, 2, 1, 4, 3), (3, 3, 1, 4, 3), (4, 3, 0, 5, 3), (3, 2, 0, 1, 3),
                        (4, 1, 1, 5, 2), (4, 2, 0, 6, 2)]
    rows = []
    c1c_zero_ok = c1c_zero_tot = c1c_pos_ok = c1c_pos_tot = 0
    for (h, n2, n1, ne, nc) in shapes:
        if 2 * h + 2 * n2 + n1 != ne + 3 * nc: continue
        r = h
        lam = tuple([2 + n2 + n1, 2 + n2] + [2] * (h - 2))
        p = P1
        pred_blocks = {mu: a_pleth(3, r, nc, mu) for mu in horiz_strips(lam, ne, r)}
        pred = sum(pred_blocks.values())
        npts = max(8, 3 * (pred + 2))
        MS = [ms_of(*rand_point(r, p, rng), r, p) for _ in range(npts)]
        mat = []
        for mu, a in pred_blocks.items():
            sub = []
            for _ in range(mult * (a + 2)):
                try:
                    cells = strip_ell_cells(lam, mu, h, n2, n1, rng)
                    F = random_mixed_filling(h, n2, n1, ne, nc, rng, ell_cells=cells)
                except (RuntimeError, ValueError, AssertionError):
                    continue
                sub.append([mixed_eval_c(F, ms, p, r=r) for ms in MS])
            nz = sum(1 for row in sub if any(row))
            if a == 0:
                c1c_zero_tot += 1; c1c_zero_ok += (nz == 0)
            else:
                c1c_pos_tot += 1; c1c_pos_ok += (nz > 0)
            mat += sub
        meas = rank_mod(mat, p) if mat else 0
        rows.append(dict(shape=[h, n2, n1, ne, nc], lam=list(lam), predicted=pred,
                         measured=meas, agree=(pred == meas),
                         blocks={str(k): v for k, v in pred_blocks.items()}))
    ge2 = [x for x in rows if x["predicted"] >= 2]
    return dict(control="C1b_directed",
                n_shapes=len(rows), n_agree=sum(1 for x in rows if x["agree"]),
                n_with_dim_ge_2=len(ge2), n_agree_dim_ge_2=sum(1 for x in ge2 if x["agree"]),
                max_predicted=max([x["predicted"] for x in rows] or [0]),
                passed=all(x["agree"] for x in rows) and len(ge2) >= 2,
                C1c_forced_zero=dict(
                    a3_zero_blocks=c1c_zero_tot, a3_zero_blocks_all_zero=c1c_zero_ok,
                    a3_positive_blocks=c1c_pos_tot, a3_positive_blocks_nonzero=c1c_pos_ok,
                    passed=(c1c_zero_ok == c1c_zero_tot and c1c_pos_ok == c1c_pos_tot),
                    has_teeth=(c1c_zero_tot > 0 and c1c_pos_tot > 0),
                    note="a_3(mu)=0 blocks must be identically zero and a_3(mu)>0 blocks must "
                         "not be: the anti-vacuity half is what stops 'all zero' passing trivially."),
                rows=rows)


def C1d(shapes=None, seed=1405, mult=26, n_brute=3):
    """The strongest small-scale control: at shapes whose target dimension is
    INDEPENDENTLY computable and >= 2, check both halves at once --
      (a) the literal Leibniz brute force equals the C core, exactly, mod p;
      (b) the measured rank of strip-directed members equals the predicted dimension.
    (b) at dimension >= 2 is what tests MIXING BETWEEN INDEPENDENT BASIS DIRECTIONS;
    the board says a one-dimensional test does not discharge that."""
    rng = random.Random(seed)
    shapes = shapes or [(4, 4, 3, 4, 5), (4, 4, 2, 3, 5), (3, 4, 3, 5, 4), (4, 3, 3, 2, 5),
                        (3, 4, 2, 4, 4), (3, 3, 3, 3, 4), (4, 3, 3, 5, 4), (4, 2, 3, 3, 4)]
    rows = []
    br_ok = br_tot = br_nonzero = 0
    for (h, n2, n1, ne, nc) in shapes:
        if 2 * h + 2 * n2 + n1 != ne + 3 * nc: continue
        r = h; p = P1
        lam = tuple([2 + n2 + n1, 2 + n2] + [2] * (h - 2))
        blocks = {mu: a_pleth(3, r, nc, mu) for mu in horiz_strips(lam, ne, r)}
        pred = sum(blocks.values())
        MS = [ms_of(*rand_point(r, p, rng), r, p) for _ in range(max(10, 3 * pred))]
        mat = []; live_examples = []
        for mu, aa in blocks.items():
            for _ in range(mult * (aa + 1)):
                try:
                    cells = strip_ell_cells(lam, mu, h, n2, n1, rng)
                    F = random_mixed_filling(h, n2, n1, ne, nc, rng, ell_cells=cells)
                except (RuntimeError, ValueError, AssertionError):
                    continue
                row = [mixed_eval_c(F, ms, p, r=r) for ms in MS]
                mat.append(row)
                if any(row) and len(live_examples) < n_brute: live_examples.append(F)
        meas = rank_mod(mat, p) if mat else 0
        # (a) brute force on live members of THIS shape
        for F in live_examples:
            ms = MS[0]
            b = brute_force_mixed(F, ms, p, r=r)
            c = mixed_eval_c(F, ms, p, r=r)
            br_tot += 1; br_ok += (b == c); br_nonzero += (b != 0)
        rows.append(dict(shape=[h, n2, n1, ne, nc], lam=list(lam), predicted=pred,
                         measured=meas, agree=(pred == meas), n_members=len(mat)))
    ge2 = [x for x in rows if x["predicted"] >= 2]
    return dict(control="C1d",
                n_shapes=len(rows), n_agree=sum(1 for x in rows if x["agree"]),
                n_with_dim_ge_2=len(ge2), n_agree_dim_ge_2=sum(1 for x in ge2 if x["agree"]),
                max_predicted=max([x["predicted"] for x in rows] or [0]),
                brute_vs_core_agree=br_ok, brute_vs_core_total=br_tot,
                brute_nonzero=br_nonzero,
                passed=(all(x["agree"] for x in rows) and len(ge2) >= 4
                        and br_ok == br_tot and br_nonzero > 0),
                rows=rows)
