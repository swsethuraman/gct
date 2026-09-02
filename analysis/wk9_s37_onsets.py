#!/usr/bin/env python3
"""
Session 37, check 2 -- two cheap ideal onsets with the house pipeline
(analysis/wk8_s30_core.py, corrected raising rule, two primes).

(a) I(D_6^{per_3}) inside C[Sym^3 C^6]: the ideal of the 6-variable
    restrictions of the 3x3 permanent (dim 50 in 56).  By the restriction
    lemma it is concentrated at weights of length exactly 6 (D_5^{per_3} is
    everything).  docs/dip_transfer.md: the permanent can enter I(P_6) only
    at degrees where this ideal is nonzero.
(b) I(R_3) = I(D_3^pad) inside C[Sym^4 C^3] (and, mode R4, I(R_4) at r = 4): the reducible ternary quartics
    with a linear factor (dim 12 in 15).  At ell = 3 the determinant side is
    everything (D_3^det = Sym^4 C^3), so every pad bite here is a strict
    D < 0 cell of the blindness slab (docs/blindness_slab.md).

Scans every weight of the given length and degree; reports cells with
mult < a (ideal nonzero) and the per-degree totals.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk8_s30_core import measure, per_form, per_padded, monomials
from wk8_s30_pleth import a_of
NS_CAP = int(os.environ.get("NS_CAP", "7000"))   # memory wall of this container (~3.5 GB cgroup)

def partitions(total, parts, maxpart=None):
    if maxpart is None: maxpart = total
    if parts == 0:
        if total == 0: yield ()
        return
    for first in range(min(total, maxpart), 0, -1):
        for rest in partitions(total - first, parts - 1, first):
            yield (first,) + rest

def scan(label, f, N, n, r, deltas, length):
    print(f"== {label}: n={n}, r={r}, weights of length exactly {length}", flush=True)
    for delta in deltas:
        tot_a = tot_units = 0; bites = []; skipped = []
        for lam in partitions(n * delta, length):
            a = a_of(lam, delta, n, r)          # plethysm route first: skip a = 0 cells
            if a == 0: continue
            NS = len(monomials(n, r, delta, lam))
            if NS > NS_CAP:
                skipped.append((lam, a, NS)); continue
            res = measure(f, N, n, r, delta, lam, seed=37 + delta, bound=10**5, a_expect=a)
            tot_a += a
            units = a - res['mult']
            tot_units += units
            print(f"     lam={lam}  a={a}  mult={res['mult']}  units={units}  N_S={NS}", flush=True)
            if units > 0: bites.append((lam, a, res['mult'], NS))
        print(f"  delta={delta}: measured sum a = {tot_a}, ideal units = {tot_units}; "
              f"{len(skipped)} cells above N_S cap {NS_CAP} unmeasured: "
              + ", ".join(f"{l} a={a} N_S={ns}" for l, a, ns in skipped), flush=True)
        for lam, a, m, nb in bites:
            print(f"     BITE lam={lam}  a={a}  mult={m}  units={a-m}  N_S={nb}", flush=True)

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "both"
    lo = int(sys.argv[2]) if len(sys.argv) > 2 else 2
    hi = int(sys.argv[3]) if len(sys.argv) > 3 else 7
    if which in ("both", "per6"):
        f, N = per_form(3)
        scan("I(D_6^{per_3})", f, N, 3, 6, range(lo, hi + 1), 6)
    if which in ("both", "R3"):
        f, N = per_padded(3, 4)
        scan("I(R_3) = I(D_3^pad)", f, N, 4, 3, range(lo, hi + 1), 3)
    if which == "R4":   # (c) length-4 weights at r = 4: closes the a = 1 gap at delta = 5
        f, N = per_padded(3, 4)
        scan("I(R_4) = I(D_4^pad)", f, N, 4, 4, range(lo, hi + 1), 4)
    if which == "R5":   # (d) length-5 weights at r = 5: the pad onset at ell = 5
        f, N = per_padded(3, 4)
        scan("I(R_5) = I(D_5^pad)", f, N, 4, 5, range(lo, hi + 1), 5)
