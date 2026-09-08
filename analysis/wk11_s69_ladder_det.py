#!/usr/bin/env python3
"""Session 69: det-side finisher for the ladder basis.  Reads results/s69_ladder_n<n>.json,
climbs every basis vector to delta_top (an actual bracket filling), evaluates it at K_det det_n
pencils (parallel, both primes), and reports rank = mult_det, i_det = a - rank, and the left
kernel = U_D as a delta_top bracket circuit.

n = 3: also expands U_D into house chi-coordinates and compares with the banked control vector
       results/artefacts/s69_banked_n3_d12.json (must be proportional / equal up to sign).
n = 4: saves U_D as fillings + integer coefficients + committed det/generic values (the handover
       format; the literal chi-expansion is out of range, docs/compact_circuit.md section 6).

    python3 analysis/wk11_s69_ladder_det.py --n 3 [--kdet 20]
    python3 analysis/wk11_s69_ladder_det.py --n 4 [--kdet 290] [--p2]
"""
import argparse, gzip, json, math, os, sys, time
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from wk8_s30_core import P1, P2                                              # noqa: E402
from wk11_s69_circuit import (Filling, sym_table, symbols_from_coeffs, generic_point, det_point,
                              dp_eval_c, fast_eval_c, rank_mod, left_kernel_mod, reconstruct_integer_vector)  # noqa: E402
from wk11_s69_ladder import ladder_params, climb_to_top                     # noqa: E402

T0 = time.time(); _MS = None; _TAB = None; _P = None


def log(*a):
    print(f"[{time.time()-T0:8.1f}s]", *a, flush=True)


def _init(msyms, tab, p):
    global _MS, _TAB, _P
    _MS = msyms; _TAB = tab; _P = p


def _eval_top(Fj):
    F = Filling.from_json(Fj)
    return [dp_eval_c(F, ms, _P, _TAB) for ms in _MS]


def det_points(n, r, K, seed=11, bound=30):
    import random
    rng = random.Random(seed); pts = []; As = []
    for _ in range(K):
        cv, A = det_point(n, r, rng, bound=bound); pts.append(cv); As.append(A)
    return pts, As


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=4)
    ap.add_argument("--kdet", type=int, default=290)
    ap.add_argument("--workers", type=int, default=2)
    ap.add_argument("--p2", action="store_true")
    ap.add_argument("--fresh", type=int, default=24)
    args = ap.parse_args()
    P = ladder_params(args.n); n, r, top = P["n"], P["r"], P["top"]
    A, idx, fact, tab = sym_table(n, r)
    st = json.load(open(os.path.join(ROOT, "results", f"s69_ladder_n{n}.json")))
    basis = st["basis"]
    a = P["a"][top]
    log(f"n={n}: basis {len(basis)} (generic rank {st.get('generic_rank')}), a={a}; climbing to delta={top}")
    top_fillings = [climb_to_top(Filling.from_json(b["filling"]), P).to_json() for b in basis]

    primes = (P1, P2) if args.p2 else (P1,)
    det_pts, det_As = det_points(n, r, args.kdet)
    out = dict(n=n, top=top, a=a, basis_size=len(basis), generic_rank=st.get("generic_rank"),
               kdet=args.kdet, det_seed=11, det_bound=30, primes=list(primes))
    kern_by_p = {}
    for p in primes:
        msyms = [symbols_from_coeffs(cv, n, r, p) for cv in det_pts]
        with Pool(args.workers, initializer=_init, initargs=(msyms, tab, p)) as pool:
            rows = list(pool.map(_eval_top, top_fillings, chunksize=4))
        rk = rank_mod(rows, p); kern = left_kernel_mod(rows, p)
        out[f"det_rank_{p}"] = rk; out[f"i_det_{p}"] = a - rk; out[f"kernel_dim_{p}"] = len(kern)
        kern_by_p[p] = kern
        log(f"  p={p}: det rank {rk} -> mult_det={rk}, i_det={a-rk}, kernel dim {len(kern)}")

    # U_D as a circuit: kernel[0] over the climbed fillings
    if kern_by_p[primes[0]]:
        x = kern_by_p[primes[0]][0]
        # fresh det pencils (must vanish) and fresh generic points (must not) -- both primes
        checks = {}
        for p in primes:
            fdet, _ = det_points(n, r, args.fresh, seed=20260908, bound=40)
            fgen = [generic_point(n, r, p, __import__("random").Random(777000 + i)) for i in range(args.fresh)]
            xp = kern_by_p[p][0] if kern_by_p[p] else x
            vals_d = []
            for cv in fdet:
                ms = symbols_from_coeffs(cv, n, r, p)
                vals_d.append(sum(c * dp_eval_c(Filling.from_json(top_fillings[i]), ms, p, tab)
                                  for i, c in enumerate(xp) if c % p) % p)
            vals_g = []
            for cv in fgen:
                ms = symbols_from_coeffs(cv, n, r, p)
                vals_g.append(sum(c * dp_eval_c(Filling.from_json(top_fillings[i]), ms, p, tab)
                                  for i, c in enumerate(xp) if c % p) % p)
            checks[str(p)] = dict(fresh_det_all_zero=all(v == 0 for v in vals_d), n_fresh_det=len(vals_d),
                                  fresh_generic_nonzero=sum(1 for v in vals_g if v), n_fresh_generic=len(vals_g))
            log(f"  U_D checks p={p}: {checks[str(p)]}")
        out["U_D_checks"] = checks
        out["U_D_kernel_coeffs"] = {str(p): kern_by_p[p] for p in primes}

    # n=3: compare U_D to the banked control vector via the chi-expansion
    if n == 3 and kern_by_p[P1]:
        from wk11_s69_n3 import Expander, get_cell
        B = get_cell(P["lam_top"], top)
        X = Expander(B, n, r)
        # expand each climbed top filling to chi, combine by the kernel coeffs
        x = kern_by_p[P1][0]
        n_chi = B["n_chi"]; u = [0] * n_chi
        for i, c in enumerate(x):
            if c % P1 == 0: continue
            coef, _, _ = X.expand(Filling.from_json(top_fillings[i]))
            v, info = X.to_chi(coef)
            for j in range(n_chi):
                if v[j]: u[j] = (u[j] + c * v[j]) % P1
        bk = json.load(open(os.path.join(ROOT, "results", "artefacts", "s69_banked_n3_d12.json")))["vector_chi_coords"]
        j0 = next(j for j in range(n_chi) if bk[j] % P1)
        lam = u[j0] * pow(bk[j0] % P1, -1, P1) % P1
        mism = sum(1 for j in range(n_chi) if (u[j] - lam * bk[j]) % P1)
        out["banked_comparison"] = dict(proportional=(mism == 0), mismatches=mism, n_chi=n_chi)
        log(f"  n=3 banked comparison: proportional={mism==0}, mismatches={mism}")

    json.dump(out, open(os.path.join(ROOT, "results", f"s69_ladder_det_n{n}.json"), "w"), indent=1)
    # handover artefact
    art = dict(n=n, lam=list(P["lam_top"]), delta=top, a=a, det_rank=out.get(f"det_rank_{primes[0]}"),
               i_det=out.get(f"i_det_{primes[0]}"), basis_native=[b for b in basis],
               basis_climbed_to_top=top_fillings, kernel_coeffs=out.get("U_D_kernel_coeffs"),
               note="basis vectors as native bracket fillings + birth delta; climbed to delta_top by adding e_1^n letters (n one-columns each). U_D = sum kernel_coeffs[i] * climbed_filling[i]. chi-coordinate conversion: docs/compact_circuit.md section 4 (feasible at n=3, out of range at n=4).")
    with gzip.open(os.path.join(ROOT, "results", "artefacts", f"s69_ladder_n{n}_basis.json.gz"), "wt") as fh:
        json.dump(art, fh)
    log("done")


if __name__ == "__main__":
    main()
