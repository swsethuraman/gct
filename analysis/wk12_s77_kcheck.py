#!/usr/bin/env python3
"""s77 -- reconcile the two statements about tall-column overlap k:
  (proved, S1 rule 4)  tall columns sharing k letters with h-k > n  =>  F_T = 0.
     at n=4, h=9 this is  k <= 4  =>  F_T = 0.
  (banked)  the delta=24 birth representative F_57 has k = 9.

The claim to test: no contradiction.  "k<5" is a VANISHING region (k<=4 kills
the filling), so nonzero representatives have k >= h-n = 5, and k=9 (the maximal
overlap) is the opposite extreme and expected robustly nonzero.

Method: at the cheapest n=4 h=9 cell (delta=12 seed), force each k in 0..9 and
evaluate random fillings of that k at generic points, both primes.  Report the
first-nonzero rate per k.  Then read k off the banked F_57 and off session 69's
113 saved delta=24 fillings.
"""
import json, os, random, sys, time
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from wk8_s30_core import P1, P2                                          # noqa: E402
from wk11_s69_circuit import (Filling, random_filling, sym_table, symbols_from_coeffs,  # noqa: E402
                              generic_point, dp_eval_c, fast_eval_c)

N, H = 4, 9
_A, _idx, _fact, TAB = sym_table(N, H)


def ev(F, msym, p):
    try:
        return dp_eval_c(F, msym, p, TAB) % p
    except Exception:                                                    # noqa: BLE001
        return fast_eval_c(F, msym, p, TAB) % p


def kcheck(delta=12, trials=40, seed=77):
    n2 = 15
    n1 = N * delta - 2 * H - 2 * n2
    rng = random.Random(seed)
    pts = {p: [symbols_from_coeffs(generic_point(N, H, p, random.Random(seed * 100 + i)), N, H, p)
               for i in range(3)] for p in (P1, P2)}
    out = {}
    for k in range(0, H + 1):
        nz = 0; got = 0; t0 = time.time()
        for _ in range(trials):
            try:
                F = random_filling(H, N, delta, n2, n1, rng, k=k)
            except Exception:                                            # noqa: BLE001
                continue
            got += 1
            hot = False
            for p in (P1, P2):
                if any(ev(F, ms, p) for ms in pts[p]):
                    hot = True
            if hot:
                nz += 1
        out[k] = dict(trials=got, nonzero=nz, secs=round(time.time() - t0, 1))
        print(f"  k={k}: {nz}/{got} nonzero at generic points (both primes)  [{out[k]['secs']}s]", flush=True)
    return out


def banked_k():
    st = json.load(open(os.path.join(ROOT, "results/s69_lmr_state.json")))
    fills = [Filling.from_json(b) for b in st["basis"]]
    ks = [len(set(F.C1) & set(F.C2)) for F in fills]
    from collections import Counter
    dist = dict(sorted(Counter(ks).items()))
    f57 = fills[57]
    return dict(count=len(fills), k_distribution=dist, F57_k=len(set(f57.C1) & set(f57.C2)),
                F57_shared=sorted(set(f57.C1) & set(f57.C2)))


def main():
    res = {"cell": "n=4 h=9 delta=12", "proved_test": "k<=4 => F_T=0 (h-k>n)", "k_scan": kcheck()}
    res["banked_saved_delta24"] = banked_k()
    b = res["banked_saved_delta24"]
    print(f"\nsaved delta=24 fillings: {b['count']};  k-distribution {b['k_distribution']}")
    print(f"F_57 (the birth representative): k = {b['F57_k']}, shared letters {b['F57_shared']}")
    zeros_below5 = all(res["k_scan"][k]["nonzero"] == 0 for k in range(0, 5))
    nz_at9 = res["k_scan"][9]["nonzero"] > 0
    res["verdict"] = dict(all_k_le_4_vanish=zeros_below5, k9_nonzero=nz_at9,
                          reconciled=bool(zeros_below5 and nz_at9))
    print(f"\nverdict: k<=4 all vanish = {zeros_below5}; k=9 nonzero = {nz_at9}; "
          f"RECONCILED = {res['verdict']['reconciled']}")
    json.dump(res, open(os.path.join(ROOT, "results/s77_kcheck.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
