#!/usr/bin/env python3
"""Session 74 -- the LMR source by births: per-rung birth bases of the ladder
lambda_d = (4d-31, 17, 2^7), d = 12..24, certified at both house primes.

For each rung d the birth quotient  M_d / u M_{d-1}  (S1's theorem, dimension
b_d = a_d - a_{d-1}) is spanned by fillings that (i) carry no pure-u letter (the
syntactic filter: a letter whose four legs all sit in one-columns gives
F_T = 4! u F_deleted identically) and (ii) raise the rank of the evaluation
rows at generic points with u = 0.  Rank b_d at one prime proves the b_d
restricted polynomials are Q-independent (integer coefficients, integer
points), hence a basis of the birth quotient.  Both primes are run; a nonzero
b_d x b_d minor is recorded at each.

Modes
  --rungs 20,21,22,23          reproduce the integrator's banked streams (same seeds)
  --rungs 13,14,...            discover (same seed rule; the probe's first draws coincide)
  --anchors                    the delta=12 seeds, F_57 at delta=24, S1's ten vectors

The stream.  Draws come from the house sampler (wk11_s69_circuit.random_filling,
k shared tall-column letters) and, once a rung has stalled (--stall consecutive
draws without a new direction, default 60), from a bandit over eight arms --
(house | ones-first sampler of wk12_s74_sampler) x k in {6,7,8,9} -- with
Thompson sampling on each arm's observed new-direction rate.  Before the stall
the stream is exactly the probe's (rng = Random(500+d), k = rng.choice([5..9])
consumed before each draw), so the first draws coincide with the integrator's.
A candidate whose value at the first u=0 point is 0 is discarded without the
other evaluations (a nonzero class vanishing there has probability <= 24/p per
candidate; efficiency only -- a zero row is never kept in any case).
Per-rung state including the random-number states is checkpointed after every
batch, so an interrupted rung resumes where it stopped.

Seeds: u=0 points random.Random(61000+11j) at P1 and random.Random(62000+11j)
at P2; bandit rng Random(1500+d).
"""
import argparse
import json
import os
import random
import sys
import time
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)

from flint import nmod_mat                                               # noqa: E402
from wk8_s30_core import P1, P2, exps                                    # noqa: E402
from wk11_s69_circuit import (Filling, random_filling, sym_table,        # noqa: E402
                              symbols_from_coeffs, generic_point,
                              fast_eval_c, rank_mod)
from wk12_s74_sampler import random_filling_ones_first                   # noqa: E402
from wk12_s74_dp import dp_eval_compact                                  # noqa: E402

N, H, N2 = 4, 9, 15
BIRTH = {12: 2, 13: 37, 14: 54, 15: 52, 16: 43, 17: 31, 18: 22,
         19: 14, 20: 9, 21: 5, 22: 3, 23: 1, 24: 1}
A_LADDER = {12: 2, 13: 39, 14: 93, 15: 145, 16: 188, 17: 219, 18: 241, 19: 255,
            20: 264, 21: 269, 22: 272, 23: 273, 24: 274}
_E = exps(N, H)
IU = _E.index(tuple([N] + [0] * (H - 1)))     # u = c_(4,0,...,0); LAST in this ordering
_A, _idx, _fact, TAB = sym_table(N, H)
KSET = (5, 6, 7, 8, 9)
ARMS = [(s, k) for s in ("house", "ones") for k in (6, 7, 8, 9)]
POINT_SEED = {P1: 61000, P2: 62000}
OUT = os.environ.get("S74_OUT", os.path.join(ROOT, "results", "s74"))
T0 = time.time()


def log(*a):
    print(f"[{time.time()-T0:8.1f}s]", *a, flush=True)


def n1_of(delta):
    return N * delta - 2 * H - 2 * N2


def u0_point(p, seed):
    cv = generic_point(N, H, p, random.Random(seed))
    cv[IU] = 0
    return cv


def u0_points(p, K):
    return [u0_point(p, POINT_SEED[p] + 11 * j) for j in range(K)]


def ev(F, msym, p):
    """the compact-state DP (wk12_s74_dpc.c, validated entry for entry against the
    s69 evaluator); the mixed-discriminant evaluator only if the pathwidth is out
    of range."""
    try:
        return dp_eval_compact(F, msym, p, TAB) % p
    except Exception:                                        # noqa: BLE001
        return fast_eval_c(F, msym, p, TAB) % p


def pure_u_letters(F):
    c = [0] * F.delta
    for l in F.C1:
        c[l] += 1
    for l in F.C2:
        c[l] += 1
    for a, b in F.two:
        c[a] += 1
        c[b] += 1
    return [l for l in range(F.delta) if c[l] == 0]


# ------------------------------------------------------------------ pool workers
_MS = None
_P = None


def _init(msyms, p):
    global _MS, _P
    _MS, _P = msyms, p


def _row(Fj):
    F = Filling.from_json(Fj)
    return [ev(F, ms, _P) for ms in _MS]


def _row_sc(Fj):
    """short-circuit: None if the value at the first point is 0."""
    F = Filling.from_json(Fj)
    v0 = ev(F, _MS[0], _P)
    if v0 == 0:
        return None
    return [v0] + [ev(F, ms, _P) for ms in _MS[1:]]


def eval_rows(fillings_json, cvs, p, workers, short_circuit=False):
    msyms = [symbols_from_coeffs(cv, N, H, p) for cv in cvs]
    fn = _row_sc if short_circuit else _row
    if workers <= 1 or len(fillings_json) == 1:
        _init(msyms, p)
        return [fn(Fj) for Fj in fillings_json]
    with Pool(workers, initializer=_init, initargs=(msyms, p)) as pool:
        return pool.map(fn, fillings_json, chunksize=1)


# ------------------------------------------------------------------ linear algebra
def nonzero_minor(rows, p):
    """a column set of size rank(rows) on which the rows have a nonzero minor, and
    its determinant mod p (greedy column selection, flint ranks)."""
    m = len(rows)
    cols = []
    for j in range(len(rows[0])):
        trial = cols + [j]
        sub = [[r[c] % p for c in trial] for r in rows]
        if rank_mod(sub, p) == len(trial):
            cols = trial
            if len(cols) == m:
                break
    sub = [[r[c] % p for c in cols] for r in rows]
    if len(cols) == m:
        d = int(nmod_mat(m, m, [x for r in sub for x in r], p).det())
        return cols, d
    return cols, None


# ------------------------------------------------------------------ rng state (de)serialisation
def rng_dump(r):
    st = r.getstate()
    return [st[0], list(st[1]), st[2]]


def rng_load(s):
    r = random.Random()
    r.setstate((s[0], tuple(s[1]), s[2]))
    return r


# ------------------------------------------------------------------ one rung
def run_rung(delta, workers, max_draws, cap_secs, batch, stall, s1_candidates=None):
    b = BIRTH[delta]
    n1 = n1_of(delta)
    K = b + 8
    path = os.path.join(OUT, f"births_d{delta}.json")
    st = None
    if os.path.exists(path):
        st = json.load(open(path, encoding="utf-8"))
        if st.get("complete") and st.get("p2_rank") == b:
            log(f"delta={delta}: already complete ({b}/{b} both primes), skipping")
            return st
        if "rng_state" not in st:
            st = None                      # an old-format partial file: restart the rung
    cvs1 = u0_points(P1, K)
    if st is None:
        st = dict(delta=delta, lam=[4 * delta - 31, 17] + [2] * 7, a=A_LADDER[delta], b=b, K=K,
                  stream_seed=500 + delta, kset=list(KSET), point_seed_P1=POINT_SEED[P1],
                  point_seed_P2=POINT_SEED[P2],
                  point_rule="generic_point(4,9,p,Random(seed+11j)); cv[494]=0",
                  filter="reject any filling with a pure-u letter (four legs in one-columns)",
                  keep_rule="value at point 0 nonzero and rank increases; rows = values at the K u=0 points mod P1",
                  fillings=[], rows_P1=[], hits=[], draws=0, past_filter=0, zero_rows=0,
                  draws_to_last_keep=0, past_filter_to_last_keep=0, complete=False, secs=0.0,
                  stall_after=stall, stalled_at=None, consecutive_misses=0,
                  arm_stats={f"{s}:{k}": [0, 0] for s, k in ARMS},      # [draws, new]
                  k_stats={str(k): [0, 0, 0] for k in KSET},           # [draws, zero, new] house phase
                  rng_state=rng_dump(random.Random(500 + delta)),
                  bandit_state=rng_dump(random.Random(1500 + delta)))
        pending = []
        if s1_candidates:
            for i, Fj in enumerate(s1_candidates):
                F = Filling.from_json(Fj)
                assert F.delta == delta
                if pure_u_letters(F):
                    log(f"delta={delta}: S1 candidate {i} carries a pure-u letter, rejected by the filter")
                    continue
                pending.append((f"s1:{i}", "s1:0", "s1", 0, 0, F))
        st["_pending"] = [(t, a, ph, x, y, F.to_json()) for t, a, ph, x, y, F in pending]
    rng = rng_load(st["rng_state"])
    brng = rng_load(st["bandit_state"])
    rows = [r[:] for r in st["rows_P1"]]
    keep = [Filling.from_json(f) for f in st["fillings"]]
    hits = st["hits"]
    tried, filtered = st["draws"], st["past_filter"]
    pending = [(t, a, ph, x, y, Filling.from_json(Fj)) for t, a, ph, x, y, Fj in st.get("_pending", [])]
    t_start = time.time() - st["secs"]

    def flush():
        st.update(fillings=[F.to_json() for F in keep], rows_P1=rows, rank_P1=len(rows), hits=hits,
                  draws=tried, past_filter=filtered, secs=round(time.time() - t_start, 1),
                  rng_state=rng_dump(rng), bandit_state=rng_dump(brng),
                  _pending=[(t, a, ph, x, y, F.to_json()) for t, a, ph, x, y, F in pending])
        tmp = path + ".tmp"
        json.dump(st, open(tmp, "w", encoding="utf-8"), indent=1)
        os.replace(tmp, path)

    def draw_one():
        """returns (arm label, filling) or None; consumes the stream exactly as the probe
        does before the stall, the bandit after."""
        if st["stalled_at"] is None:
            k = rng.choice(list(KSET))
            try:
                F = random_filling(H, N, delta, N2, n1, rng, k=k)
            except Exception:                                # noqa: BLE001
                return None
            return f"house:{k}", "probe", F
        # Thompson sampling over the arms
        best, bestv = None, -1.0
        for s, k in ARMS:
            d_, n_ = st["arm_stats"][f"{s}:{k}"]
            v = brng.betavariate(n_ + 1, d_ - n_ + 1)
            if v > bestv:
                best, bestv = (s, k), v
        s, k = best
        try:
            if s == "house":
                F = random_filling(H, N, delta, N2, n1, brng, k=k)
            else:
                F = random_filling_ones_first(H, N, delta, N2, n1, brng, k=k)
        except Exception:                                    # noqa: BLE001
            return None
        return f"{s}:{k}", "bandit", F

    while len(rows) < b and tried < max_draws and time.time() - t_start < cap_secs:
        cand = list(pending)
        pending = []
        while len(cand) < batch and tried < max_draws:
            r = draw_one()
            if r is None:
                continue
            arm, phase, F = r
            tried += 1
            if pure_u_letters(F):
                continue
            filtered += 1
            cand.append((tried, arm, phase, tried, filtered, F))
        if not cand:
            break
        res = eval_rows([F.to_json() for _, _, _, _, _, F in cand], cvs1, P1, workers, short_circuit=True)
        for (tag, arm, phase, tr, fi, F), row in zip(cand, res):
            if len(rows) >= b:
                continue                                       # drawn past the b-th keep; not consumed
            s_, k_ = arm.split(":")
            if phase == "bandit":
                st["arm_stats"][arm][0] += 1
            elif phase == "probe":
                st["k_stats"][k_][0] += 1
            if row is None:
                st["zero_rows"] += 1
                if phase == "probe":
                    st["k_stats"][k_][1] += 1
                st["consecutive_misses"] += 1
            elif rank_mod(rows + [row], P1) > len(rows):
                rows.append(row)
                keep.append(F)
                hits.append(dict(draw=tag, arm=arm, k_shared=len(F.shared), rank=len(rows),
                                 secs=round(time.time() - t_start, 1)))
                st["consecutive_misses"] = 0
                if phase == "bandit":
                    st["arm_stats"][arm][1] += 1
                elif phase == "probe":
                    st["k_stats"][k_][2] += 1
                if not isinstance(tag, str):
                    st["draws_to_last_keep"] = tr
                    st["past_filter_to_last_keep"] = fi
            else:
                st["consecutive_misses"] += 1
            if st["stalled_at"] is None and st["consecutive_misses"] >= stall and len(rows) < b:
                st["stalled_at"] = dict(draw=tried, rank=len(rows))
                log(f"delta={delta}: stalled at rank {len(rows)}/{b} after {stall} misses (draw {tried}); "
                    f"switching to the bandit stream")
        pending = []
        flush()
        log(f"delta={delta} b={b}: rank {len(rows)}/{b}, draws {tried} ({filtered} past filter, "
            f"{st['zero_rows']} zero rows), {time.time()-t_start:.0f}s")
    st["complete"] = len(rows) == b
    if st["complete"]:
        cols, dmin = nonzero_minor(rows, P1)
        st["minor_P1"] = dict(cols=cols, det=dmin)
        cvs2 = u0_points(P2, K)
        rows2 = eval_rows([F.to_json() for F in keep], cvs2, P2, workers)
        st["rows_P2"] = rows2
        st["p2_rank"] = rank_mod(rows2, P2)
        cols2, dmin2 = nonzero_minor(rows2, P2)
        st["minor_P2"] = dict(cols=cols2, det=dmin2)
        log(f"delta={delta}: COMPLETE {b}/{b} at P1 (minor det {dmin}); P2 rank {st['p2_rank']}/{b} "
            f"(minor det {dmin2}); draws {tried}, past filter {filtered}, {time.time()-t_start:.0f}s")
    else:
        log(f"delta={delta}: NOT FILLED rank {len(rows)}/{b} after {tried} draws ({filtered} past filter), "
            f"{time.time()-t_start:.0f}s -- reported, stream not enlarged")
    flush()
    return st


# ------------------------------------------------------------------ anchors
def run_anchors(workers):
    out = {}
    # (a) the delta=12 seeds: generic rank 2 and u=0 rank 2, both primes
    seed = json.load(open(os.path.join(ROOT, "results", "s69_n4_seed.json"), encoding="utf-8"))
    seeds = seed["basis"]
    assert len(seeds) == 2
    rec = dict(source="results/s69_n4_seed.json basis", fillings=seeds)
    for p in (P1, P2):
        gpts = [generic_point(N, H, p, random.Random(70000 + 7 * j)) for j in range(10)]
        rows = eval_rows(seeds, gpts, p, workers)
        cv0 = u0_points(p, 10)
        rows0 = eval_rows(seeds, cv0, p, workers)
        rec[f"generic_rank_{p}"] = rank_mod(rows, p)
        rec[f"u0_rank_{p}"] = rank_mod(rows0, p)
        rec[f"rows_generic_{p}"] = rows
        rec[f"rows_u0_{p}"] = rows0
    out["seeds_d12"] = rec
    log(f"seeds d=12: generic rank {rec[f'generic_rank_{P1}']},{rec[f'generic_rank_{P2}']}; "
        f"u=0 rank {rec[f'u0_rank_{P1}']},{rec[f'u0_rank_{P2}']}")
    # (b) F_57 at delta=24: nonzero at u=0 points, both primes
    b24 = json.load(open(os.path.join(ROOT, "results", "wk12_int_lmr_birth24.json"), encoding="utf-8"))
    F57 = b24["filling"]
    rec = dict(source="results/wk12_int_lmr_birth24.json", index=b24["index"], filling=F57)
    for p in (P1, P2):
        rows = eval_rows([F57], u0_points(p, 9), p, workers)
        rec[f"rows_u0_{p}"] = rows[0]
        rec[f"u0_rank_{p}"] = rank_mod(rows, p)
        rec[f"nonzero_{p}"] = sum(1 for v in rows[0] if v)
    out["F57_d24"] = rec
    log(f"F57 d=24: u=0 rank {rec[f'u0_rank_{P1}']},{rec[f'u0_rank_{P2}']}; nonzero "
        f"{rec[f'nonzero_{P1}']}/9, {rec[f'nonzero_{P2}']}/9")
    # (c) S1's ten vectors: seeds identical to s69's?  eight delta=13 classes rank 8 at u=0
    s1 = json.load(open(os.path.join(ROOT, "results", "astra", "S1", "partial_source_10.json"), encoding="utf-8"))
    vecs = s1["vectors"]
    keyf = lambda d: Filling.from_json(d).key()                          # noqa: E731
    s1_seed_keys = sorted(keyf(v["native_filling"]) for v in vecs if v["native_degree"] == 12)
    s69_keys = sorted(keyf(d) for d in seeds)
    d13 = [v["native_filling"] for v in vecs if v["native_degree"] == 13]
    rec = dict(source="results/astra/S1/partial_source_10.json", n_vectors=len(vecs),
               seeds_equal_s69=(s1_seed_keys == s69_keys), n_d13=len(d13), d13_fillings=d13,
               d13_pure_u=[pure_u_letters(Filling.from_json(d)) for d in d13])
    K = BIRTH[13] + 8
    for p in (P1, P2):
        rows = eval_rows(d13, u0_points(p, K), p, workers)
        rec[f"rows_u0_{p}"] = rows
        rec[f"u0_rank_{p}"] = rank_mod(rows, p)
    out["S1_partial_source"] = rec
    log(f"S1: seeds equal s69 {rec['seeds_equal_s69']}; eight d=13 classes u=0 rank "
        f"{rec[f'u0_rank_{P1}']},{rec[f'u0_rank_{P2}']} (need 8); pure-u letters {rec['d13_pure_u']}")
    path = os.path.join(OUT, "anchors.json")
    json.dump(out, open(path, "w", encoding="utf-8"), indent=1)
    return out


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--rungs", default="")
    ap.add_argument("--anchors", action="store_true")
    ap.add_argument("--workers", type=int, default=2)
    ap.add_argument("--max-draws", type=int, default=4000)
    ap.add_argument("--cap", type=float, default=7200.0)
    ap.add_argument("--batch", type=int, default=6)
    ap.add_argument("--stall", type=int, default=60)
    ap.add_argument("--with-s1", action="store_true",
                    help="admit S1's eight delta=13 classes as the first rung-13 candidates")
    args = ap.parse_args(argv)
    os.makedirs(OUT, exist_ok=True)
    if args.anchors:
        run_anchors(args.workers)
    if args.rungs:
        s1c = None
        if args.with_s1:
            s1 = json.load(open(os.path.join(ROOT, "results", "astra", "S1", "partial_source_10.json"),
                                encoding="utf-8"))
            s1c = [v["native_filling"] for v in s1["vectors"] if v["native_degree"] == 13]
        for d in [int(x) for x in args.rungs.split(",")]:
            run_rung(d, args.workers, args.max_draws, args.cap, args.batch, args.stall,
                     s1_candidates=(s1c if (d == 13 and s1c) else None))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
