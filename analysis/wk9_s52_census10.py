#!/usr/bin/env python3
"""
Session 52 -- the delta = 10 a=1 census by the Weyl route.

The Frobenius-plethysm route wk8_s30_pleth.amb(10, 4, 6) does NOT fit this
container: it was launched under `ulimit -v 6.3 GB`, reached 3.9 GB resident and
was ended by the kernel with no traceback (results/logs/s52_census10.log is
empty).  The cost is the unbounded memo on the Murnaghan-Nakayama character
chi(lam, rho) over the ~37,000 partitions of 40.

This route is the brief's suggestion -- a better enumeration, not a longer bound.
`a` is the Weyl alternation over 6! terms with non-negativity pruning
(wk9_s42_census.a_weyl), each term a tail DP over the box of lam; the enumeration
is restricted to the obstruction-eligible cells (lam_1 >= delta) up front, which
is 1874 cells rather than every ell=6 partition of 40, and nothing dense is ever
built.  h_pad is the same alternation over the Pieri strips.

The delta = 10 row therefore covers the OBSTRUCTION-ELIGIBLE cells only; the
lam_1 < 10 onset-only cells are not enumerated here and the census table says so.

usage: python3 wk9_s52_census10.py [--delta 10] [--out results/s52_cells_d10.jsonl]
"""
import sys, os, json, time

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from wk9_s42_census import a_weyl, h_pad_weyl, partitions_region
from wk9_s36_census import N_S as N_S_dp, stab_order


def log(*a):
    print(*a, file=sys.stderr, flush=True)


if __name__ == '__main__':
    delta = int(sys.argv[sys.argv.index('--delta') + 1]) if '--delta' in sys.argv else 10
    out = sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv else 'results/s52_cells_d10.jsonl'
    t0 = time.time()
    lams = partitions_region(delta, 6, 6, 4)
    log(f"[d{delta}] {len(lams)} obstruction-eligible ell=6 cells to score")
    cache = {}
    rows = []
    na = n1 = 0
    fh = open(out, 'w')
    for i, lam in enumerate(lams):
        a = a_weyl(lam, delta, 4, cache)
        if a == 0: continue
        na += 1
        rec = dict(lam=list(lam), delta=delta, ell=6, a=a, eligible=True, bal=lam[0] - lam[-1])
        if a == 1:
            n1 += 1
            rec['h_pad'] = h_pad_weyl(lam, delta, cache)
            rec['informative'] = rec['h_pad'] >= 1
            ns = N_S_dp(4, 6, delta, lam); so = stab_order(lam)
            rec.update(N_S=ns, stab=so, nchi_lb=(ns + so - 1) // so)
        rows.append(rec)
        fh.write(json.dumps(rec) + "\n")
        if (i + 1) % 100 == 0:
            fh.flush()
            log(f"[d{delta}] {i+1}/{len(lams)}  a>=1: {na}  a=1: {n1}  "
                f"cache {len(cache)}  [{time.time()-t0:.0f}s]")
            if len(cache) > 3_000_000: cache.clear()
    fh.close()
    inf = [r for r in rows if r['a'] == 1 and r['informative']]
    log(f"[d{delta}] SUMMARY eligible_with_a>=1={na} units={sum(r['a'] for r in rows)} "
        f"a1_eligible={n1} informative(h_pad>=1)={len(inf)}  [{time.time()-t0:.0f}s]")
