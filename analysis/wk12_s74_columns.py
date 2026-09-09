#!/usr/bin/env python3
"""Session 74 -- the assembled LMR source and its evaluation columns.

Source (results/s74/source.json): the 274 literal transported fillings T_i^up,
in rung order -- the two s69 seeds (rung 12), the per-rung birth bases of
results/s74/births_d13..23.json, and F_57 (rung 24).  Declared row system
(PREREG_s74 section 3b): for every column and both primes

    row_i(f) = F_{T_i^up}(f) = F_{T_i}(f) * msym_u(f)^(24 - d_i),
    msym_u(f) = 4! * [s_1^4] f  (the u-letter symbol),

the native value scaled by the transport factor.  The delta = 23 source is the
same list without F_57 with exponent 23 - d_i (a column scaling of the delta=24
matrix's first 273 rows, so its rank is read off the same native values).

Point families (all integer substitution data; K = a + 8 = 282):
    det   det_4(sum s_i A_i), A_i in Z^{4x4}, entries in [-30,30]     Random(20260974 + j)
    pad   restrict(PAD34): x_0(s).per_3(X(s)), frame V in Z^{9x10}     Random(20261974 + j)
    red   l(s).c(s), l in Z^9, c a generic integer cubic               Random(20262974 + j)
    per4  per_4(sum s_i A_i)                                           Random(20263974 + j)
    gen   a generic integer quartic, coefficients in [-1000,1000]      Random(20264974 + j)
A point whose u-symbol vanishes mod either prime is skipped (recorded).

    --build                       write source.json from the rung files present
    --family det --prime 2147483647   evaluate (resumable, per-row checkpoint)
    --check-rows                  the row-system identity on sampled rows
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

from wk8_s30_core import P1, P2, exps, restrict, det_form, per_form, per_padded   # noqa: E402
from wk11_s69_circuit import (Filling, sym_table, symbols_from_coeffs,          # noqa: E402
                              fast_eval_c, rank_mod)
from wk12_s74_dp import dp_eval_compact                                          # noqa: E402

N, H, N2, TOP = 4, 9, 15, 24
BIRTH = {12: 2, 13: 37, 14: 54, 15: 52, 16: 43, 17: 31, 18: 22,
         19: 14, 20: 9, 21: 5, 22: 3, 23: 1, 24: 1}
_E = exps(N, H)
IU = _E.index(tuple([N] + [0] * (H - 1)))
_A, _idx, _fact, TAB = sym_table(N, H)
OUT = os.environ.get("S74_OUT", os.path.join(ROOT, "results", "s74"))
DET4, N_DET = det_form(4)
PER4, N_PER = per_form(4)
PAD34, N_PAD = per_padded(3, 4)
SEED = dict(det=20260974, pad=20261974, red=20262974, per4=20263974, gen=20264974)
BOUND = 30
K_DEFAULT = 274 + 8
T0 = time.time()


def log(*a):
    print(f"[{time.time()-T0:8.1f}s]", *a, flush=True)


def ev(F, msym, p):
    """the compact-state DP (wk12_s74_dpc.c, validated entry for entry against the
    s69 evaluator); the mixed-discriminant evaluator only if the pathwidth is out
    of range."""
    try:
        return dp_eval_compact(F, msym, p, TAB) % p
    except Exception:                                        # noqa: BLE001
        return fast_eval_c(F, msym, p, TAB) % p


# ------------------------------------------------------------------ the source
def climb(F, top=TOP):
    one = list(F.one)
    nxt = F.delta
    for _ in range(top - F.delta):
        one += [nxt] * N
        nxt += 1
    return Filling(H, N, top, F.C1, F.C2, F.two, one)


def build_source():
    entries = []
    seed = json.load(open(os.path.join(ROOT, "results", "s69_n4_seed.json"), encoding="utf-8"))
    for Fj in seed["basis"]:
        entries.append(dict(rung=12, native=Fj, origin="results/s69_n4_seed.json"))
    present = {12: 2}
    for d in range(13, 24):
        path = os.path.join(OUT, f"births_d{d}.json")
        if not os.path.exists(path):
            continue
        st = json.load(open(path, encoding="utf-8"))
        if not st.get("complete") or st.get("p2_rank") != BIRTH[d]:
            log(f"rung {d}: present but not complete at both primes (rank {st.get('rank_P1')}/{BIRTH[d]}, "
                f"P2 {st.get('p2_rank')}); its {len(st['fillings'])} fillings are included as a partial rung")
        for Fj in st["fillings"]:
            entries.append(dict(rung=d, native=Fj, origin=f"results/s74/births_d{d}.json"))
        present[d] = len(st["fillings"])
    b24 = json.load(open(os.path.join(ROOT, "results", "wk12_int_lmr_birth24.json"), encoding="utf-8"))
    entries.append(dict(rung=24, native=b24["filling"], origin="results/wk12_int_lmr_birth24.json (F_57)"))
    present[24] = 1
    for i, e in enumerate(entries):
        F = Filling.from_json(e["native"])
        assert F.delta == e["rung"]
        Fu = climb(F)
        e["index"] = i
        e["literal"] = Fu.to_json()
        e["exponent"] = TOP - e["rung"]
        e["factorial_scalar"] = 24 ** (TOP - e["rung"])      # (n!)^{D-d}: literal = this * (u^{D-d} F_T)
        e["key"] = list(map(list, F.key()[:2])) + [[list(x) for x in F.key()[2]], list(F.key()[3])]
    src = dict(cell=dict(n=4, r=9, lam=[65, 17] + [2] * 7, delta=24, a=274),
               row_system="row_i(f) = F_{T_i^up}(f) = F_{T_i}(f) * msym_u(f)^(24 - d_i), msym_u = 4! [s_1^4] f; "
                          "literal transported fillings; S1's u-normalised vector = literal / 24^(24-d_i)",
               u_index=IU, birth_profile=BIRTH, present=present, size=len(entries),
               complete=(len(entries) == 274), entries=entries)
    json.dump(src, open(os.path.join(OUT, "source.json"), "w", encoding="utf-8"), indent=1)
    log(f"source: {len(entries)} vectors; rungs present {present}; complete={src['complete']}")
    return src


def load_source():
    return json.load(open(os.path.join(OUT, "source.json"), encoding="utf-8"))


# ------------------------------------------------------------------ points
def _rand_mat(rnd):
    return [[rnd.randint(-BOUND, BOUND) for _ in range(4)] for _ in range(4)]


def make_point(family, j):
    """(record as substitution data, integer coefficient list over exps(4, 9))."""
    rnd = random.Random(SEED[family] + j)
    if family == "det":
        pencil = [_rand_mat(rnd) for _ in range(H)]
        As = [[pencil[i][a][b] for a in range(4) for b in range(4)] for i in range(H)]
        co = restrict(DET4, N_DET, N, H, As)
        rec = {"type": "det_pencil", "pencil": pencil}
    elif family == "per4":
        pencil = [_rand_mat(rnd) for _ in range(H)]
        As = [[pencil[i][a][b] for a in range(4) for b in range(4)] for i in range(H)]
        co = restrict(PER4, N_PER, N, H, As)
        rec = {"type": "permanent_pencil", "pencil": pencil}
    elif family == "pad":
        V = [[rnd.randint(-BOUND, BOUND) for _ in range(N_PAD)] for _ in range(H)]
        co = restrict(PAD34, N_PAD, N, H, V)
        rec = {"type": "padded_permanent",
               "linear_forms": [[int(V[i][c]) for i in range(H)] for c in range(N_PAD)]}
    elif family == "red":
        lin = [rnd.randint(-BOUND, BOUND) for _ in range(H)]
        cub = {al: rnd.randint(-BOUND, BOUND) for al in exps(3, H)}
        co = {}
        for a3, cc in cub.items():
            if cc == 0:
                continue
            for i in range(H):
                if lin[i] == 0:
                    continue
                a4 = list(a3)
                a4[i] += 1
                k = tuple(a4)
                co[k] = co.get(k, 0) + lin[i] * cc
        rec = {"type": "reducible", "l": lin,
               "cubic": [[list(al), int(c)] for al, c in sorted(cub.items()) if c]}
    elif family == "gen":
        co = {al: rnd.randint(-1000, 1000) for al in _E}
        rec = {"type": "form", "coefficients": [[list(al), int(c)] for al, c in sorted(co.items()) if c]}
    else:
        raise ValueError(family)
    cv = [int(co.get(al, 0)) for al in _E]
    return rec, cv


def make_points(family, K):
    """K points whose u-coefficient is nonzero as an integer and mod both primes."""
    pts, skipped, j = [], [], 0
    while len(pts) < K:
        rec, cv = make_point(family, j)
        u = cv[IU]
        if u == 0 or u % P1 == 0 or u % P2 == 0:
            skipped.append(j)
        else:
            pts.append(dict(j=j, record=rec, cv=cv))
        j += 1
    return pts, skipped


# ------------------------------------------------------------------ evaluation
_MS = None
_P = None


def _init(msyms, p):
    global _MS, _P
    _MS, _P = msyms, p


def _row(Fj):
    F = Filling.from_json(Fj)
    return [ev(F, ms, _P) for ms in _MS]


def col_path(family, p):
    return os.path.join(OUT, f"columns_{family}_{p}.json")


def evaluate(family, p, workers, K, block):
    src = load_source()
    path = col_path(family, p)
    if os.path.exists(path):
        st = json.load(open(path, encoding="utf-8"))
        assert st["K"] == K, "point count changed; refusing to mix"
        pts_cv = st["points_cv"]
    else:
        pts, skipped = make_points(family, K)
        st = dict(family=family, prime=p, K=K, seed=SEED[family], bound=BOUND, skipped_points=skipped,
                  points=[q["record"] for q in pts], point_index=[q["j"] for q in pts],
                  points_cv=[q["cv"] for q in pts], rows_native={}, secs=0.0)
        pts_cv = st["points_cv"]
    msyms = [symbols_from_coeffs(cv, N, H, p) for cv in pts_cv]
    st["u_symbol"] = [ms[IU] for ms in msyms]
    todo = [e for e in src["entries"] if json.dumps(e["key"]) not in st["rows_native"]]
    log(f"{family} p={p}: {len(st['rows_native'])} rows banked, {len(todo)} to do, K={K}")
    if not todo:
        return st
    t0 = time.time()
    with Pool(workers, initializer=_init, initargs=(msyms, p)) as pool:
        for s in range(0, len(todo), block):
            chunk = todo[s:s + block]
            rows = pool.map(_row, [e["native"] for e in chunk], chunksize=1)
            for e, r in zip(chunk, rows):
                st["rows_native"][json.dumps(e["key"])] = r
            st["secs"] = round(st["secs"] + time.time() - t0, 1)
            t0 = time.time()
            tmp = path + ".tmp"
            json.dump(st, open(tmp, "w", encoding="utf-8"))
            os.replace(tmp, path)
            log(f"{family} p={p}: {len(st['rows_native'])}/{len(src['entries'])} rows "
                f"(rung {chunk[-1]['rung']}), {st['secs']:.0f}s")
    return st


# ------------------------------------------------------------------ the row-system identity
def check_rows(workers, n_rows=26, n_pts=3):
    src = load_source()
    rng = random.Random(74)
    by_rung = {}
    for e in src["entries"]:
        by_rung.setdefault(e["rung"], []).append(e)
    sample = []
    for d in sorted(by_rung):
        sample += rng.sample(by_rung[d], min(2, len(by_rung[d])))
    sample = sample[:n_rows]
    out = dict(n_rows=len(sample), n_pts=n_pts, checks=[], all_pass=True)
    for p in (P1, P2):
        for fam in ("gen", "det", "pad"):
            pts, _ = make_points(fam, n_pts)
            msyms = [symbols_from_coeffs(q["cv"], N, H, p) for q in pts]
            for e in sample:
                Fn = Filling.from_json(e["native"])
                Fu = Filling.from_json(e["literal"])
                for ms in msyms:
                    lit = ev(Fu, ms, p)
                    nat = ev(Fn, ms, p) * pow(ms[IU], e["exponent"], p) % p
                    ok = lit == nat
                    out["checks"].append(dict(prime=p, family=fam, index=e["index"], rung=e["rung"],
                                              literal=lit, scaled_native=nat, ok=ok))
                    out["all_pass"] &= ok
            log(f"row-system identity p={p} {fam}: {sum(c['ok'] for c in out['checks'])}/{len(out['checks'])} so far")
    json.dump(out, open(os.path.join(OUT, "row_system_check.json"), "w", encoding="utf-8"), indent=1)
    log(f"row-system identity: {'ALL PASS' if out['all_pass'] else 'FAILURES'} over {len(out['checks'])} checks")
    return out


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--build", action="store_true")
    ap.add_argument("--family", default="")
    ap.add_argument("--prime", type=int, default=P1)
    ap.add_argument("--workers", type=int, default=2)
    ap.add_argument("--K", type=int, default=K_DEFAULT)
    ap.add_argument("--block", type=int, default=4)
    ap.add_argument("--check-rows", action="store_true")
    args = ap.parse_args(argv)
    os.makedirs(OUT, exist_ok=True)
    if args.build:
        build_source()
    if args.check_rows:
        check_rows(args.workers)
    if args.family:
        for fam in args.family.split(","):
            evaluate(fam, args.prime, args.workers, args.K, args.block)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
