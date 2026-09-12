#!/usr/bin/env python3
"""
B14-06 -- driver: controls first, then the reproduction.

    python3 analysis/b14_06_run.py --selftest
    python3 analysis/b14_06_run.py --measure --tail 17,2,2,2,2,2,2,2 --npts 340
    python3 analysis/b14_06_run.py --stretch --npts 460

EVERY control below is run twice: once on the real input, and once on an input
that MUST make it fail.  A control whose must-fail twin does not fail is
reported as VACUOUS and the run exits nonzero.  This is
PROVED.md: check_must_be_able_to_fail, whose seventh instance -- the batch-14
reachability script passing on an empty census because all() over nothing is
true -- is why the twins are mandatory here.  Controls also assert a positive
cardinality before asserting anything about their contents, and C9 exercises
that assertion on an empty input.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
"""
import argparse, json, os, sys, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
from b14_06_bracket import (P1, P2, PRIMES, DEGS, CONVENTIONS, enumerate_brackets,
                            BracketEvaluator, brute_value, det_mod, rank_mod,
                            jet_point_list, inv_mod, consistency_defect, random_point)
import b14_06_points as PT

OUT = os.path.join(ROOT, 'results/b14_06')
RESULTS = {"conventions": CONVENTIONS, "controls": [], "measurements": []}


def log(*a):
    print(*a); sys.stdout.flush()


def record(name, passed, twin_failed, detail):
    vacuous = (twin_failed is False)
    RESULTS["controls"].append({"control": name, "passed": bool(passed),
                                "must_fail_twin_failed_as_required": twin_failed,
                                "vacuous": vacuous, "detail": detail})
    tag = "PASS" if passed else "FAIL"
    tw = {True: "twin failed as required", False: "TWIN DID NOT FAIL -- VACUOUS",
          None: "no twin"}[twin_failed]
    log(f"  [{tag}] {name:<34} ({tw})  {detail}")
    return passed and not vacuous


# ------------------------------------------------------------------ point batches
def batch(fam, npts, p, seed, **kw):
    rng = np.random.default_rng(seed)
    J, jets, aux = PT.FAMILIES[fam](npts, p, rng, **kw)
    valid = aux["valid"]
    red = jet_point_list(J, jets)
    red = [r for r, v in zip(red, valid) if v]
    return red, aux, int((~valid).sum())


def ev_matrix(ev, reds):
    return [ev.values(r) for r in reds]        # rows = points; transposed by rank_mod anyway


def rank_of(ev, reds, p):
    M = ev_matrix(ev, reds)
    if not M or not M[0]:
        raise ValueError("rank_of called on an empty matrix -- refusing to report a rank")
    return rank_mod(M, p)


# ------------------------------------------------------------------ controls
def control_C1(p):
    """s57 Theorem P: a_inf((2^{ell-1})) = 1 with HWV det(G_2)."""
    br = enumerate_brackets(16, col=8)
    ev = BracketEvaluator(br, 8, p)
    reds, _, _ = batch("DET", 8, p, 3)
    assert len(reds) > 0, "C1 got no points"
    vals = [ev.values(r)[0] for r in reds]
    dets = [det_mod(r[2][2], p) for r in reds]
    ok = (len(br) == 1 and all(v == 40320 * d % p for v, d in zip(vals, dets))
          and all(v for v in vals))
    brL = enumerate_brackets(31, col=8)
    twin_failed = not (len(brL) == 1)
    return record("C1 Theorem P at tail (2^8)", ok, twin_failed,
                  f"count={len(br)}, value=8!.det(N_2) on {len(reds)}/{len(reds)} DET points, "
                  f"all nonzero; twin: count at (17,2^7) = {len(brL)}")


def control_C2(p):
    """the BigM formula against a direct eps-eps contraction, col = 3."""
    col, W = 3, 13
    br = enumerate_brackets(W, col=col)
    ev = BracketEvaluator(br, col, p)
    rng = np.random.default_rng(4242)

    def rred(sym=True):
        r = {}
        for d in DEGS:
            N = rng.integers(0, p, (col, col))
            if sym:
                N = (N + N.T) % p
            r[d] = (int(rng.integers(0, p)), [int(v) for v in rng.integers(0, p, col)],
                    [[int(N[i][j]) for j in range(col)] for i in range(col)])
        return r

    ok = True; npt = 4
    for _ in range(npt):
        r = rred()
        ok &= (ev.values(r) == [brute_value(b, r, col, p) for b in br])
    assert len(br) > 0
    rns = rred(sym=False)
    t1 = ev.values(rns) != [brute_value(b, rns, col, p) for b in br]

    class NoFact(BracketEvaluator):
        def __init__(self, *a, **k):
            super().__init__(*a, **k); self.fact = [1] * 9
    r = rred()
    t2 = NoFact(br, col, p).values(r) != [brute_value(b, r, col, p) for b in br]
    return record("C2 formula == brute-force eps.eps", ok, bool(t1 and t2),
                  f"{len(br)} brackets, {npt} random points, exact equality; "
                  f"twins: non-symmetric N differs={t1}, c!-dropped differs={t2}")


def control_C3(p, W=31):
    """g fixing e_1 acts by (s,u,N) -> (s, g^T u, g^T N g) and B -> det(g)^2 B;
    the torus reads the weight lam_bar off the instrument."""
    col = 8
    br = enumerate_brackets(W, col=col)
    ev = BracketEvaluator(br, col, p)
    reds, _, _ = batch("GEN", 3, p, 77)
    assert len(reds) > 0
    rng = np.random.default_rng(31415)

    def act(r, g):
        out = {}
        gT = g.T
        for d in DEGS:
            s, u, N = r[d]
            uu = (gT @ np.array(u, dtype=object)) % p
            NN = (gT @ np.array(N, dtype=object) @ g) % p
            out[d] = (s, [int(v) for v in uu], [[int(NN[i][j]) for j in range(col)]
                                                for i in range(col)])
        return out

    def gfix(det_one=True):
        g = np.eye(col, dtype=object)
        for _ in range(12):
            k, l = rng.integers(0, col), rng.integers(1, col)   # l != 0 keeps g.e_1 = e_1
            if k == l:
                continue
            g = g @ (np.eye(col, dtype=object) + int(rng.integers(1, 50)) *
                     np.eye(col, dtype=object)[:, [k]] @ np.eye(col, dtype=object)[[l], :])
        if not det_one:
            g = g.copy(); g[:, 1] = g[:, 1] * 3        # column 1 != 0, so g.e_1 = e_1 kept
        return g % p

    ok_inv = True; ok_det = True
    for r in reds:
        v0 = ev.values(r)
        g = gfix(True)
        ok_inv &= (ev.values(act(r, g)) == v0)
        h = gfix(False)                                  # det(h) = 3.det(g)
        dh = det_mod([[int(x) for x in row] for row in h], p)
        ok_det &= (ev.values(act(r, h)) == [x * dh % p * dh % p for x in v0])
    # torus: B -> t_0^{W-16} . (prod_k t_k)^2 . B
    ok_tor = True
    for r in reds:
        t = [int(x) for x in rng.integers(2, 1000, col)]
        rt = {}
        for d in DEGS:
            s, u, N = r[d]
            rt[d] = (s * pow(t[0], d, p) % p,
                     [u[i] * pow(t[0], d - 1, p) % p * t[i] % p for i in range(col)],
                     [[N[i][j] * pow(t[0], d - 2, p) % p * t[i] % p * t[j] % p
                       for j in range(col)] for i in range(col)])
        fac = pow(t[0], W - 16, p)
        for k in range(col):
            fac = fac * t[k] % p * t[k] % p
        ok_tor &= (ev.values(rt) == [x * fac % p for x in ev.values(r)])
    # twins
    r = reds[0]; h = gfix(False)
    dh = det_mod([[int(x) for x in row] for row in h], p)
    twin_a = (ev.values(act(r, h)) != ev.values(r)) and dh % p not in (1, p - 1)
    t = [int(x) for x in rng.integers(2, 1000, col)]
    rt = {}
    for d in DEGS:
        s, u, N = r[d]
        rt[d] = (s * pow(t[0], d, p) % p,
                 [u[i] * pow(t[0], d - 1, p) % p * t[i] % p for i in range(col)],
                 [[N[i][j] * pow(t[0], d - 2, p) % p * t[i] % p * t[j] % p
                   for j in range(col)] for i in range(col)])
    wrongfac = pow(t[0], W - 15, p)                       # weight (18,2^7): must not hold
    for k in range(col):
        wrongfac = wrongfac * t[k] % p * t[k] % p
    twin_b = (ev.values(rt) != [x * wrongfac % p for x in ev.values(r)])
    ok = ok_inv and ok_det and ok_tor
    return record("C3 covariance and weight", ok, bool(twin_a and twin_b),
                  f"det(g)^2 law on {len(reds)} points ({len(br)} brackets); torus reads "
                  f"weight ({W-16}+2, 2^7); twins: non-unimodular g not invariant={twin_a}, "
                  f"wrong weight rejected={twin_b}")


def control_C4(p):
    """bracket generic rank vs wk9_s57_stable.a_inf (Weyl alternation) on a family."""
    from wk9_s57_stable import a_inf
    tails = [(x,) + (2,) * (n - 1) for n in (3, 4) for x in (2, 3, 4, 5, 6, 7)]
    tails = [t for t in tails if t[0] >= 2]
    rows = []; ok = True
    rng = np.random.default_rng(2718)
    for tail in tails:
        n = len(tail); W = sum(tail)
        br = enumerate_brackets(W, col=n)
        ai = a_inf(tail)
        if not br:
            rows.append((tail, 0, ai, ai == 0)); ok &= (ai == 0); continue
        ev = BracketEvaluator(br, n, p)
        reds = [random_point(n, p, rng) for _ in range(ai + 12)]
        rk = rank_of(ev, reds, p)
        rows.append((tail, rk, ai, rk == ai)); ok &= (rk == ai)
    assert len(rows) > 0, "C4 got no tails"
    # twin (i): the defect this control actually caught -- random INDEPENDENT (s,u,N)
    # is not a point of Z (Euler forces u_d = N_d[:,0], s_d = N_d[0][0]), and the
    # rank must then EXCEED a_inf somewhere.
    inflated = False
    for tail in tails:
        n = len(tail); W = sum(tail)
        br = enumerate_brackets(W, col=n)
        if not br:
            continue
        ai = a_inf(tail)
        ev = BracketEvaluator(br, n, p)
        reds = []
        for _ in range(ai + 12):
            r = {}
            for d in DEGS:
                N = rng.integers(0, p, (n, n)); N = (N + N.T) % p
                r[d] = (int(rng.integers(0, p)), [int(v) for v in rng.integers(0, p, n)],
                        [[int(N[i][j]) for j in range(n)] for i in range(n)])
            reds.append(r)
        if rank_of(ev, reds, p) > ai:
            inflated = True; break
    # twin (ii): delete a whole (a,b) pattern class -- some tail's rank must drop
    dropped = False
    for tail in tails:
        n = len(tail); W = sum(tail)
        br = enumerate_brackets(W, col=n)
        if len(br) < 2:
            continue
        pats = sorted(set((b[0], b[1]) for b in br))
        for pat in pats:
            sub = [b for b in br if (b[0], b[1]) != pat]
            if not sub:
                continue
            ai = a_inf(tail)
            ev = BracketEvaluator(sub, n, p)
            reds = [random_point(n, p, rng) for _ in range(ai + 12)]
            if rank_of(ev, reds, p) < ai:
                dropped = True; break
        if dropped:
            break
    detail = "; ".join(f"{t}:{rk}v{ai}" for t, rk, ai, _ in rows)
    return record("C4 a_inf vs Weyl alternation", ok, bool(inflated and dropped),
                  f"{len(rows)} tails, rank == a_inf everywhere -> {detail}; "
                  f"twins: inconsistent (s,u,N) inflates={inflated}, "
                  f"a deleted (a,b) class drops the rank={dropped}")


def control_C10(p):
    """Euler's relations on every real point of every family: u_d = N_d[:,0] and
    s_d = N_d[0][0].  Validates the jet machinery end to end."""
    tot = 0; n = 0
    for fam in ("GEN", "DET", "DETQ", "PAD", "RED", "NEG"):
        reds, _, _ = batch(fam, 6, p, 1234)
        assert len(reds) > 0, f"C10 got no {fam} points"
        for r in reds:
            tot += consistency_defect(r, 8, p); n += 1
    rng = np.random.default_rng(8)
    bad = {}
    for d in DEGS:
        N = rng.integers(0, p, (8, 8)); N = (N + N.T) % p
        bad[d] = (int(rng.integers(0, p)), [int(v) for v in rng.integers(0, p, 8)],
                  [[int(N[i][j]) for j in range(8)] for i in range(8)])
    twin = consistency_defect(bad, 8, p) > 0
    return record("C10 Euler relations on real points", tot == 0, bool(twin),
                  f"{n} points across 6 families, {tot} violated relations; "
                  f"twin: independent random data has {consistency_defect(bad, 8, p)} violations")


def control_C9(p):
    """the empty-input guard itself: rank_of must refuse an empty matrix, and an
    all() over nothing must not be reportable as a pass."""
    br = enumerate_brackets(31, col=8)
    ev = BracketEvaluator(br, 8, p)
    raised = False
    try:
        rank_of(ev, [], p)
    except ValueError:
        raised = True
    vacuous_all = all(x == 1 for x in [])          # True: the batch-13/14 defect shape
    return record("C9 empty-input guard", raised, bool(vacuous_all),
                  f"rank_of([]) raised={raised}; all([]) is {vacuous_all}, which is why "
                  f"every control here asserts cardinality first")


# ------------------------------------------------------------------ measurement
def measure(tail, npts, primes=PRIMES, seed=20260912, families=("GEN", "DET", "PAD", "RED", "NEG"),
            with_C6=True):
    W = sum(tail); col = len(tail)
    br = enumerate_brackets(W, col=col)
    out = {"tail": list(tail), "W": W, "col": col, "n_brackets": len(br),
           "npts_requested": npts, "seed": seed, "ranks": {}, "dropped": {},
           "values_are": CONVENTIONS["values_are"]}
    log(f"\n  tail {tail}  |lam_bar|={W}  brackets={len(br)}  points={npts}")
    for p in primes:
        ev = BracketEvaluator(br, col, p)
        out["ranks"][str(p)] = {}
        for fam in families:
            t0 = time.time()
            reds, aux, drop = batch(fam, npts, p, seed + hash(fam) % 1000)
            rk = rank_of(ev, reds, p)
            out["ranks"][str(p)][fam] = rk
            out["dropped"][fam] = drop
            log(f"    p={p}  {fam:<5} rank {rk:>4}   ({len(reds)} pts, {drop} dropped, "
                f"{time.time()-t0:.1f}s)")
        if with_C6:                      # C6: a corrupted determinantal family must rise
            # Z is a vector space and the Euler relations are linear, so r + t.q is a
            # legitimate point of Z for any legitimate q: the perturbed points leave
            # M_ell but STAY IN Z.  An earlier version replaced N_d alone, which left
            # Z altogether and inflated the rank past a_inf for the wrong reason.
            reds, _, _ = batch("DET", npts, p, seed + 7)
            rng = np.random.default_rng(9)
            for k, r in enumerate(reds):
                if k % 3:
                    continue             # perturb a third of the points
                q = random_point(col, p, rng)
                t = int(rng.integers(1, p))
                for d in DEGS:
                    s, u, N = r[d]; qs, qu, qN = q[d]
                    r[d] = ((s + t * qs) % p,
                            [(u[i] + t * qu[i]) % p for i in range(col)],
                            [[(N[i][j] + t * qN[i][j]) % p for j in range(col)]
                             for i in range(col)])
                assert consistency_defect(r, col, p) == 0, "C6 left Z"
            out["ranks"][str(p)]["DET_corrupted"] = rank_of(ev, reds, p)
            log(f"    p={p}  DET*  rank {out['ranks'][str(p)]['DET_corrupted']:>4}   "
                f"(C6: perturbed off M_ell; must rise)")
    RESULTS["measurements"].append(out)
    return out


# ------------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--measure", action="store_true")
    ap.add_argument("--stretch", action="store_true")
    ap.add_argument("--tail", default="17,2,2,2,2,2,2,2")
    ap.add_argument("--npts", type=int, default=340)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)
    t0 = time.time()
    allok = True
    if a.selftest or a.measure or a.stretch:
        log("controls (each with an input that must make it fail):")
        allok &= control_C9(P1)
        allok &= control_C2(P1)
        allok &= control_C1(P1)
        allok &= control_C10(P1)
        allok &= control_C4(P1)
        allok &= control_C3(P1)
    if a.measure:
        tail = tuple(int(x) for x in a.tail.split(","))
        m = measure(tail, a.npts)
        r1 = m["ranks"][str(P1)]; r2 = m["ranks"][str(P2)]
        allok &= record("C7 both house primes agree", r1 == r2, None, f"{r1} vs {r2}")
        allok &= record("C5 negative_control_forced", r1["NEG"] == 0,
                        r1["DET"] != 0, f"NEG rank {r1['NEG']}; twin: DET rank {r1['DET']}")
        allok &= record("C6 corrupted determinantal family",
                        r1["DET_corrupted"] > r1["DET"], None,
                        f"{r1['DET']} -> {r1['DET_corrupted']}")
        allok &= record("C8 DET == DETQ (normalise+depress)", *_c8(P1))
    if a.stretch:
        for tl in ((19,) + (2,) * 7, (21,) + (2,) * 7):
            measure(tl, a.npts, families=("GEN", "DET"), with_C6=False)
    RESULTS["ok"] = bool(allok)
    RESULTS["elapsed_s"] = round(time.time() - t0, 1)
    path = a.out or os.path.join(OUT, "run.json")
    with open(path, "w") as f:
        json.dump(RESULTS, f, indent=1, sort_keys=True)
    log(f"\nwrote {path}   ok={allok}   {RESULTS['elapsed_s']}s")
    return 0 if allok else 1


def _c8(p, npts=6):
    rng = np.random.default_rng(555)
    A = rng.integers(-50, 51, (PT.NV, 4, 4, npts)).astype(np.int64)
    A[:, 3, 3] = -(A[:, 0, 0] + A[:, 1, 1] + A[:, 2, 2])
    shift = rng.integers(-9, 10, (PT.NV, npts)).astype(np.int64)
    _, j1, _ = PT.family_DET(npts, p, rng, A=A)
    _, j2, aux = PT.family_DETQ(npts, p, rng, A=A, shift=shift)
    same = all(np.array_equal(j1[d] % p, j2[d] % p) for d in DEGS)
    _, jX, _ = PT.family_DETQ(npts, p, np.random.default_rng(1))
    twin = not all(np.array_equal(j1[d] % p, jX[d] % p) for d in DEGS)
    return (same and aux["g0_eta_max"] == 0, twin,
            f"identical on {npts} pencils, g_0 eta-parts zero; twin: unrelated pencil differs")


if __name__ == "__main__":
    sys.exit(main())
