#!/usr/bin/env python3
"""Session 69, beyond the brief's tasks: the LMR cell itself by the compact circuit.

lambda = (65, 17, 2^7), delta = 24, det_4, r = 9, a = 274; fillings of lambda' = (9, 9, 2^15, 1^48).
No coordinates anywhere: the Grassmann DP evaluator (wk11_s69_dp.c) costs ~0.1 s per
(filling, point) here, so the 274-dimensional space is reachable by evaluation alone.

Phase A (spanning): sample fillings (k shared letters drawn from --kset), keep a greedy
  independent set by generic-point rank at P1, growing the point set as the rank grows
  (a candidate is tested at rank + margin points; accepted fillings are evaluated at every
  new point).  Stops at rank a = 274 (a from a_weyl).
Phase B (det side): evaluate the basis at K_det det_4 pencils at P1 (and at P2 when asked):
  rank = mult_det (a rigorous lower bound over Q), left kernel = the ideal part U_D as a circuit.
Phase C (checks): U_D at fresh det pencils (must vanish) and at fresh generic points (must not),
  both primes.

Everything is checkpointed to results/s69_lmr_state.json (resumable) and the final record is
results/s69_lmr.json.  Points are reproducible from the seeds recorded there.

    python3 analysis/wk11_s69_lmr.py [--phase A|B|C|all] [--kdet 290] [--margin 16] [--p2]
"""
import argparse, json, os, random, sys, time
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from wk8_s30_core import P1, P2                                              # noqa: E402
from wk11_s69_circuit import (Filling, random_filling, sym_table, symbols_from_coeffs, generic_point,
                              det_point, dp_eval_c, letter_order, rank_mod, left_kernel_mod, PRIMES)   # noqa: E402

N_DEG, R, H = 4, 9, 9
DELTA, N2, N1 = 24, 15, 48
LAM = (65, 17, 2, 2, 2, 2, 2, 2, 2)
A_LMR = 274          # a((65,17,2^7),24), lmr_cell section 2, reproduced by s63 by three routes
STATE = os.path.join(ROOT, "results", "s69_lmr_state.json")
T0 = time.time()


def log(*a):
    print(f"[{time.time()-T0:8.1f}s]", *a, flush=True)


def gen_point(i, p):
    return generic_point(N_DEG, R, p, random.Random(69 * 1000 + i))


def det_points(K, seed=11, bound=30):
    rng = random.Random(seed)
    pts, As = [], []
    for _ in range(K):
        cv, A = det_point(N_DEG, R, rng, bound=bound); pts.append(cv); As.append(A)
    return pts, As


def save(st):
    tmp = STATE + ".tmp"
    json.dump(st, open(tmp, "w")); os.replace(tmp, STATE)


def load():
    if os.path.exists(STATE):
        return json.load(open(STATE))
    return dict(basis=[], rows=[], npts=0, samples=0, hist=[], eval_secs=[], phase="A")


def phase_A(st, args, tab):
    rng = random.Random(args.seed + st["samples"])      # continue the stream after a resume
    kset = [int(x) for x in args.kset.split(",")]
    msym_cache = {}

    def ms(i):
        if i not in msym_cache:
            msym_cache[i] = symbols_from_coeffs(gen_point(i, P1), N_DEG, R, P1)
        return msym_cache[i]

    basis = [Filling.from_json(F) for F in st["basis"]]
    rows = st["rows"]; npts = st["npts"]
    t_eval, n_eval = 0.0, 0
    while len(basis) < A_LMR and st["samples"] < args.maxsamples:
        need = min(len(basis) + args.margin, args.kgen)
        if need > npts:
            # extend every accepted filling to the new points
            for F, row in zip(basis, rows):
                for i in range(npts, need):
                    t = time.time(); row.append(dp_eval_c(F, ms(i), P1, tab)); t_eval += time.time() - t; n_eval += 1
            npts = need; st["npts"] = npts; st["rows"] = rows; save(st)
        kk = rng.choice(kset)
        F = random_filling(H, N_DEG, DELTA, N2, N1, rng, k=kk)
        st["samples"] += 1
        t = time.time(); v0 = dp_eval_c(F, ms(0), P1, tab); t_eval += time.time() - t; n_eval += 1
        if v0 == 0:
            st["hist"].append([st["samples"], "zero", len(F.shared)]); continue
        row = [v0]
        for i in range(1, npts):
            t = time.time(); row.append(dp_eval_c(F, ms(i), P1, tab)); t_eval += time.time() - t; n_eval += 1
        r_new = rank_mod(rows + [row], P1)
        if r_new > len(basis):
            basis.append(F); rows.append(row)
            st["basis"].append(F.to_json()); st["rows"] = rows
            st["hist"].append([st["samples"], "new", len(F.shared), letter_order(F)[1]])
            log(f"  sample {st['samples']}: k={len(F.shared)} rank -> {r_new} at {npts} points ({t_eval/max(n_eval,1):.3f}s/eval, {n_eval} evals)")
            if len(basis) % 5 == 0: save(st)
        else:
            st["hist"].append([st["samples"], "dep", len(F.shared)])
    st["eval_secs"].append(round(t_eval / max(n_eval, 1), 4))
    st["generic_rank_P1"] = rank_mod(rows, P1) if rows else 0
    st["npts"] = npts
    save(st)
    log(f"phase A: rank {st['generic_rank_P1']} of {A_LMR} after {st['samples']} samples, {npts} generic points")
    return st


def phase_B(st, args, tab, p):
    basis = [Filling.from_json(F) for F in st["basis"]]
    key = f"det_rows_{p}"
    rows = st.get(key, [])
    pts, As = det_points(args.kdet)
    st["det_seed"] = 11; st["det_bound"] = 30; st["kdet"] = args.kdet
    msyms = [symbols_from_coeffs(cv, N_DEG, R, p) for cv in pts]
    t_eval, n_eval = 0.0, 0
    for i in range(len(rows), len(basis)):
        F = basis[i]; row = []
        for msy in msyms:
            t = time.time(); row.append(dp_eval_c(F, msy, p, tab)); t_eval += time.time() - t; n_eval += 1
        rows.append(row); st[key] = rows
        if i % 10 == 9:
            save(st); log(f"  det rows p={p}: {i+1}/{len(basis)} ({t_eval/max(n_eval,1):.3f}s/eval)")
    st[key] = rows
    st[f"det_rank_{p}"] = rank_mod(rows, p)
    st[f"kernel_{p}"] = left_kernel_mod(rows, p)
    st[f"i_det_{p}"] = A_LMR - st[f"det_rank_{p}"]
    save(st)
    log(f"phase B p={p}: det rank {st[f'det_rank_{p}']} -> i_det = {st[f'i_det_{p}']}, kernel dim {len(st[f'kernel_{p}'])}")
    return st


def phase_C(st, args, tab):
    basis = [Filling.from_json(F) for F in st["basis"]]
    out = {}
    for p in PRIMES:
        kern = st.get(f"kernel_{p}") or st.get(f"kernel_{P1}")
        if not kern: continue
        x = kern[0]
        # fresh det pencils (different seed) and fresh generic points
        pts, As = det_points(args.kfresh, seed=20260908, bound=40)
        vals_det = []
        for cv in pts:
            msy = symbols_from_coeffs(cv, N_DEG, R, p)
            vals_det.append(sum(c * dp_eval_c(F, msy, p, tab) for c, F in zip(x, basis) if c % p) % p)
        vals_gen = []
        for i in range(args.kfresh):
            msy = symbols_from_coeffs(generic_point(N_DEG, R, p, random.Random(777000 + i)), N_DEG, R, p)
            vals_gen.append(sum(c * dp_eval_c(F, msy, p, tab) for c, F in zip(x, basis) if c % p) % p)
        out[str(p)] = dict(fresh_det_all_zero=all(v == 0 for v in vals_det), n_fresh_det=len(vals_det),
                           fresh_generic_nonzero=sum(1 for v in vals_gen if v), n_fresh_generic=len(vals_gen),
                           kernel_used_from=str(p) if st.get(f"kernel_{p}") else str(P1))
        log(f"phase C p={p}: {out[str(p)]}")
    st["phase_C"] = out
    save(st)
    return st


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--phase", default="all")
    ap.add_argument("--kgen", type=int, default=300)
    ap.add_argument("--kdet", type=int, default=290)
    ap.add_argument("--kfresh", type=int, default=24)
    ap.add_argument("--margin", type=int, default=16)
    ap.add_argument("--maxsamples", type=int, default=3000)
    ap.add_argument("--kset", default="5,6,7,8,9")
    ap.add_argument("--seed", type=int, default=69)
    ap.add_argument("--p2", action="store_true", help="phase B at P2 as well")
    args = ap.parse_args()
    A, idx, fact, tab = sym_table(N_DEG, R)
    st = load()
    st.setdefault("lam", list(LAM)); st.setdefault("delta", DELTA); st.setdefault("a", A_LMR)
    st.setdefault("kset", args.kset); st.setdefault("seed", args.seed)
    st.setdefault("generic_seed_rule", "random.Random(69*1000+i), uniform mod p, point i")
    if args.phase in ("A", "all"):
        st = phase_A(st, args, tab)
        if st["generic_rank_P1"] < A_LMR:
            log("spanning not reached; stopping"); return
    if args.phase in ("B", "all"):
        st = phase_B(st, args, tab, P1)
        if args.p2: st = phase_B(st, args, tab, P2)
    if args.phase == "B2":
        st = phase_B(st, args, tab, P2)
    if args.phase in ("C", "all"):
        st = phase_C(st, args, tab)
    json.dump({k: v for k, v in st.items() if k not in ("rows",) and not k.startswith("det_rows_")},
              open(os.path.join(ROOT, "results", "s69_lmr.json"), "w"), indent=1)
    log("done")


if __name__ == "__main__":
    main()
