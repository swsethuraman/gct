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

State: results/s74/births_d<d>.json (one file per rung, rewritten as the rung
progresses, complete when "complete": true).  Seeds: stream random.Random(500+d)
with k drawn by rng.choice([5,6,7,8,9]) before each draw (the probe's rule);
u=0 points random.Random(61000+11j) at P1 and random.Random(62000+11j) at P2.
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
                              dp_eval_c, fast_eval_c, rank_mod)

N, H, N2 = 4, 9, 15
BIRTH = {12: 2, 13: 37, 14: 54, 15: 52, 16: 43, 17: 31, 18: 22,
         19: 14, 20: 9, 21: 5, 22: 3, 23: 1, 24: 1}
A_LADDER = {12: 2, 13: 39, 14: 93, 15: 145, 16: 188, 17: 219, 18: 241, 19: 255,
            20: 264, 21: 269, 22: 272, 23: 273, 24: 274}
_E = exps(N, H)
IU = _E.index(tuple([N] + [0] * (H - 1)))     # u = c_(4,0,...,0); LAST in this ordering
_A, _idx, _fact, TAB = sym_table(N, H)
KSET = (5, 6, 7, 8, 9)
POINT_SEED = {P1: 61000, P2: 62000}
OUT = os.path.join(ROOT, "results", "s74")
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
    try:
        return dp_eval_c(F, msym, p, TAB) % p
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


def eval_rows(fillings_json, cvs, p, workers):
    msyms = [symbols_from_coeffs(cv, N, H, p) for cv in cvs]
    if workers <= 1 or len(fillings_json) == 1:
        _init(msyms, p)
        return [_row(Fj) for Fj in fillings_json]
    with Pool(workers, initializer=_init, initargs=(msyms, p)) as pool:
        return pool.map(_row, fillings_json, chunksize=1)


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


# ------------------------------------------------------------------ one rung
def run_rung(delta, workers, max_draws, cap_secs, batch, s1_candidates=None):
    b = BIRTH[delta]
    n1 = n1_of(delta)
    K = b + 8
    path = os.path.join(OUT, f"births_d{delta}.json")
    if os.path.exists(path):
        st = json.load(open(path, encoding="utf-8"))
        if st.get("complete") and st.get("p2_rank") == b:
            log(f"delta={delta}: already complete ({b}/{b} both primes), skipping")
            return st
    cvs1 = u0_points(P1, K)
    rng = random.Random(500 + delta)
    rows, keep, hits = [], [], []
    tried = filtered = 0
    t0 = time.time()
    st = dict(delta=delta, lam=[4 * delta - 31, 17] + [2] * 7, a=A_LADDER[delta], b=b, K=K,
              stream_seed=500 + delta, kset=list(KSET), point_seed_P1=POINT_SEED[P1],
              point_seed_P2=POINT_SEED[P2], point_rule="generic_point(4,9,p,Random(seed+11j)); cv[494]=0",
              filter="reject any filling with a pure-u letter (four legs in one-columns)",
              keep_rule="any(row) and rank increases, rows = values at the K u=0 points mod P1",
              draws_to_last_keep=0, past_filter_to_last_keep=0, complete=False)

    def flush():
        st.update(fillings=[F.to_json() for F in keep], rows_P1=rows, rank_P1=len(rows),
                  hits=hits, draws=tried, past_filter=filtered, secs=round(time.time() - t0, 1))
        tmp = path + ".tmp"
        json.dump(st, open(tmp, "w", encoding="utf-8"), indent=1)
        os.replace(tmp, path)

    # optional externally supplied first candidates (S1's replayed classes); they
    # go through exactly the same filter and rank test as any draw
    pending = []
    if s1_candidates:
        for i, Fj in enumerate(s1_candidates):
            F = Filling.from_json(Fj)
            assert F.delta == delta
            if pure_u_letters(F):
                log(f"delta={delta}: S1 candidate {i} carries a pure-u letter, rejected by the filter")
                continue
            pending.append((f"s1:{i}", 0, 0, F))
    while len(rows) < b and tried < max_draws and time.time() - t0 < cap_secs:
        # draw a batch of filter-survivors (draw order preserved; each candidate
        # carries the draw counters at the moment it was drawn, so the recorded
        # counts are those of the equivalent sequential loop)
        cand = list(pending)
        pending = []
        while len(cand) < batch and tried < max_draws:
            try:
                F = random_filling(H, N, delta, N2, n1, rng, k=rng.choice(list(KSET)))
            except Exception:                                # noqa: BLE001
                continue
            tried += 1
            if pure_u_letters(F):
                continue
            filtered += 1
            cand.append((tried, tried, filtered, F))
        if not cand:
            break
        res = eval_rows([F.to_json() for _, _, _, F in cand], cvs1, P1, workers)
        for (tag, tr, fi, F), row in zip(cand, res):
            if len(rows) >= b:
                break
            if any(row) and rank_mod(rows + [row], P1) > len(rows):
                rows.append(row)
                keep.append(F)
                hits.append(dict(draw=tag, k_shared=len(F.shared), rank=len(rows),
                                 secs=round(time.time() - t0, 1)))
                if not isinstance(tag, str):
                    st["draws_to_last_keep"] = tr
                    st["past_filter_to_last_keep"] = fi
        flush()
        log(f"delta={delta} b={b}: rank {len(rows)}/{b}, draws {tried} ({filtered} past filter), "
            f"{time.time()-t0:.0f}s")
    st["complete"] = len(rows) == b
    if st["complete"]:
        cols, dmin = nonzero_minor(rows, P1)
        st["minor_P1"] = dict(cols=cols, det=dmin)
        # second prime, fresh points
        cvs2 = u0_points(P2, K)
        rows2 = eval_rows([F.to_json() for F in keep], cvs2, P2, workers)
        st["rows_P2"] = rows2
        st["p2_rank"] = rank_mod(rows2, P2)
        cols2, dmin2 = nonzero_minor(rows2, P2)
        st["minor_P2"] = dict(cols=cols2, det=dmin2)
        log(f"delta={delta}: COMPLETE {b}/{b} at P1 (minor det {dmin}); P2 rank {st['p2_rank']}/{b} "
            f"(minor det {dmin2}); draws {tried}, past filter {filtered}, {time.time()-t0:.0f}s")
    else:
        log(f"delta={delta}: NOT FILLED rank {len(rows)}/{b} after {tried} draws ({filtered} past filter), "
            f"{time.time()-t0:.0f}s -- reported, stream not enlarged")
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
    ap.add_argument("--cap", type=float, default=3600.0)
    ap.add_argument("--batch", type=int, default=6)
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
            run_rung(d, args.workers, args.max_draws, args.cap, args.batch,
                     s1_candidates=(s1c if (d == 13 and s1c) else None))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
