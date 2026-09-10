#!/usr/bin/env python3
"""
B13-09 -- the costed census of the cubic side at lengths 7 and 8 through degree 9.

Objects: the weights mu |- 3*delta of length EXACTLY r, r in {7, 8}, delta <= 9,
with a(mu, delta) >= 1 in Sym^delta(Sym^3 C^r) -- the constituents at which
I(D_r^{per_3})_delta can live and that no inherited result covers:

  * length <= 5: excluded at every degree by docs/washout_lemma.md Theorem 2
    (D_k^{per_3} = Sym^3 C^k for k <= 5) plus the restriction lemma (Thm 3(1)),
    which gives mult_mu C[D_r^{per_3}]_delta = mult_mu C[D_k^{per_3}]_delta
    for k = ell(mu) < r;
  * length 6: the same restriction lemma carries the length-6 value, and
    I(D_6^{per_3})_delta = 0 for delta <= 9 (s41+s43 at delta = 7, s41+s43+s47
    at delta = 8, s79 at delta = 9; delta <= 6 by Pieri + s37);
  * length 7 at r = 8: the length-7 value, i.e. THIS session's length-7 result
    where it is complete (and open where it is not).

Every constituent of Sym^delta(Sym^3) has at most delta rows (Pieri), so
length 7 needs delta >= 7 and length 8 needs delta >= 8:  (r, delta) in
{(7,7), (7,8), (7,9), (8,8), (8,9)}.

Per weight: a by Weyl alternation (wk9_s42_census.a_weyl, tail DP) and,
independently, by the symmetric-function plethysm (wk8_s30_pleth.a_of); N_S by
the tail DP (N_S_tail_n); |Stab_W(mu)|; the lower bound n_chi >= N_S/|Stab|;
the cost N_S*delta and the s71/s79 hybrid model's build time 2.1e-6 s * N_S*delta.

The shorter weights are COUNTED here (not run), by length, with their Sum a, so
the report can say exactly what the inherited theorems cover.

usage: python3 analysis/b13_09_census.py [--out results/b13_09_census.json] [--no-pleth]
The (8, 9) plethysm cross-check is a separate run (analysis/b13_09_pleth89.py) merged by
analysis/b13_09_census_merge.py; the queue's `a` is asserted against the Weyl alternation
again inside the evaluator, and the hybrid kernel's nullity must equal it at both primes.
"""
import sys, os, json, time
from math import ceil
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
from wk9_s42_census import N_S_tail_n, stab_order, perm_sign
from wk8_s30_pleth import a_of


def a_weyl_sym(mu, delta, n, cache):
    """wk9_s42_census.a_weyl with one change in HOW, none in WHAT: the weight
    multiplicity m(nu) of Sym^delta(Sym^n C^r) is S_r-symmetric, so the tail DP is
    looked up at the SORTED composition (a partition), which keeps every DP array
    small (the largest part is the excluded head) and makes the cache hit across
    the whole Weyl orbit.  Asserted equal to a_weyl on every weight of the r = 7
    census in the log (the two share the DP and differ only in the cache key)."""
    mu = tuple(mu); r = len(mu)
    rho = tuple(range(r - 1, -1, -1))
    lr = [mu[i] + rho[i] for i in range(r)]
    tot = 0
    order = sorted(range(r), key=lambda i: lr[i])
    used = [False] * r
    w = [0] * r
    def rec(k):
        nonlocal tot
        if k == r:
            nu = tuple(sorted((lr[i] - rho[w[i]] for i in range(r)), reverse=True))
            key = (nu, delta, n)
            v = cache.get(key)
            if v is None:
                v = N_S_tail_n(nu, delta, n) if nu[-1] >= 0 else 0
                cache[key] = v
            tot += perm_sign(w) * v
            return
        i = order[k]
        for j in range(r):
            if not used[j] and rho[j] <= lr[i]:
                used[j] = True; w[i] = j
                rec(k + 1)
                used[j] = False
    rec(0)
    return tot


a_weyl = a_weyl_sym

N3 = 3
BUILD_RATE = 2.1e-6          # s per unit of N_S*delta (s71 hybrid model, re-fit at length 6 by s79: median 0.99x)
WALL = 1.5e8                 # N_S*delta at which s79's box (7 GB) failed in the raising-row build


def partitions_exact(total, parts, maxpart=None):
    """partitions of `total` into exactly `parts` positive parts, nonincreasing."""
    if maxpart is None: maxpart = total
    out = []
    def rec(remaining, k, mx, cur):
        if k == 0:
            if remaining == 0: out.append(tuple(cur))
            return
        # k parts left, each <= mx and >= 1
        for v in range(min(remaining - (k - 1), mx), 0, -1):
            if v * k < remaining: break
            rec(remaining - v, k - 1, v, cur + [v])
    rec(total, parts, maxpart, [])
    return out


def census_rd(r, delta, cache, do_pleth=True, verbose=True):
    t0 = time.time()
    rows = []
    n_all = 0
    for mu in partitions_exact(3 * delta, r):
        n_all += 1
        a = a_weyl(mu, delta, N3, cache)
        assert a >= 0, (mu, delta, a)
        if a == 0: continue
        ns = N_S_tail_n(mu, delta, N3)
        st = stab_order(mu)
        rec = dict(mu=list(mu), delta=delta, r=r, a=int(a), N_S=int(ns), stab=int(st),
                   n_chi_lb=int(ceil(ns / st)), NS_delta=int(ns) * delta,
                   build_model_s=round(BUILD_RATE * ns * delta, 1),
                   above_wall=bool(ns * delta > WALL))
        if do_pleth and not (r == 8 and delta == 9):     # amb(9, 3, 8) is run separately (analysis/b13_09_pleth89.py): too slow inline
            ap = a_of(mu, delta, N3, r)
            assert ap == a, ('plethysm routes disagree', mu, delta, a, ap)
            rec['a_pleth'] = int(ap)
        rows.append(rec)
    rows.sort(key=lambda x: (x['N_S'], x['mu']))
    if verbose:
        print(f"r={r} delta={delta}: {n_all} partitions of {3*delta} with exactly {r} parts, "
              f"{len(rows)} with a>=1, sum a = {sum(x['a'] for x in rows)}, max a = {max((x['a'] for x in rows), default=0)}, "
              f"N_S from {rows[0]['N_S'] if rows else None} to {rows[-1]['N_S'] if rows else None} [{time.time()-t0:.0f}s]",
              file=sys.stderr, flush=True)
    return rows


def shorter_counts(delta, rmax, cache, verbose=True):
    """the weights of length < rmax with a >= 1 at this degree: counted, not run."""
    out = {}
    for k in range(1, rmax):
        cnt = 0; sa = 0; amax = 0
        for mu in partitions_exact(3 * delta, k):
            a = a_weyl(mu, delta, N3, cache)
            if a >= 1:
                cnt += 1; sa += a; amax = max(amax, a)
        out[str(k)] = dict(weights=cnt, sum_a=sa, max_a=amax)
    if verbose:
        print(f"delta={delta}: shorter weights (length < {rmax}) with a>=1: " +
              ', '.join(f"ell={k}: {v['weights']} (sum a {v['sum_a']})" for k, v in out.items()), file=sys.stderr, flush=True)
    return out


def main(argv):
    out = argv[argv.index('--out') + 1] if '--out' in argv else os.path.join(ROOT, 'results', 'b13_09_census.json')
    do_pleth = '--no-pleth' not in argv
    cache = {}
    res = dict(board_numbering='batch13', session='B13-09', n=N3,
               build_rate_s_per_NS_delta=BUILD_RATE, wall_NS_delta=WALL,
               inherited=dict(
                   length_le_5='docs/washout_lemma.md Thm 2 + Thm 3(1) (restriction lemma): I(D_k^{per_3}) = 0 for k <= 5, every degree',
                   length_6='I(D_6^{per_3})_delta = 0 for delta <= 9: delta <= 6 Pieri + s37 (docs/transfer_lemma.md sec. 4); '
                            'delta = 7 results/s41_per6.md + results/s43_per6.md (27 weights); delta = 8 s41 + s43 + results/s47_per6_d8.md (91 weights); '
                            'delta = 9 results/s79_per6_d9.md (210 weights); carried to length r >= 7 by the restriction lemma',
                   length_7_at_r_8='this session\'s length-7 results, where complete'),
               cells={}, shorter={})
    for (r, delta) in [(7, 7), (7, 8), (7, 9), (8, 8), (8, 9)]:
        res['cells'][f"r{r}_d{delta}"] = census_rd(r, delta, cache, do_pleth=do_pleth)
    for delta in (7, 8, 9):
        res['shorter'][f"d{delta}"] = shorter_counts(delta, 9, cache)
    with open(out, 'w') as f:
        json.dump(res, f, indent=1)
    print(f"wrote {out}", file=sys.stderr)


if __name__ == '__main__':
    main(sys.argv[1:])
