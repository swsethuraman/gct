#!/usr/bin/env python3
"""
B13-05 -- the cubic census: every constituent S_mu of Sym^delta(Sym^3 C^r), r <= 9,
delta <= DMAX, with a(mu, delta) >= 1, tabulated by (delta, ell(mu)).

    a      plethysm multiplicity, TWO routes (wk8_s30_pleth.amb: symmetric functions;
           wk9_s42_census.a_weyl: Weyl alternation over the tail DP) -- must agree
    N_S    weight-space dimension of Sym^delta(Sym^3 C^r) at mu, r = ell(mu) (tail DP)
    stab   |Stab_W(mu)|, n_chi_lb = ceil(N_S / stab)

Classification (docs/b13_05_report.md):
    ell <= 5   inherited: excluded at every degree by washout_lemma Thm 2 + restriction lemma
    ell  = 6   inherited: excluded through delta <= 9 by the certified length-6 record
    ell  = 7   genuinely new at r = 7 (shared with r = 8)
    ell  = 8   genuinely new at r = 8
    ell  = 9   the r = 9 problem (exploratory here)

usage: python3 analysis/wk13_b13_05_census.py [--dmax 9] [--out results/b13_05_census.json]
board_numbering: batch13
"""
import sys, os, time, json, argparse, math
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from wk8_s30_pleth import amb
from wk9_s42_census import a_weyl, N_S_tail_n, stab_order


def log(*a):
    print(time.strftime('%H:%M:%S'), *a, flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dmax', type=int, default=9)
    ap.add_argument('--maxrows', type=int, default=9)
    ap.add_argument('--weyl-maxrows', type=int, default=9, help='cross-check a by Weyl alternation up to this length')
    ap.add_argument('--out', default='results/b13_05_census.json')
    args = ap.parse_args()
    rows = []
    summary = {}
    for delta in range(1, args.dmax + 1):
        t0 = time.time()
        A = amb(delta, 3, args.maxrows)              # {mu: a}, mu with <= maxrows rows, a >= 1
        t1 = time.time()
        log(f'delta={delta}: plethysm route done, {len(A)} constituents with a>=1, {t1-t0:.1f}s')
        cache = {}
        bylen = {}
        for mu, a in sorted(A.items(), key=lambda kv: (len(kv[0]), kv[0]), reverse=False):
            ell = len(mu)
            rec = dict(delta=delta, mu=list(mu), ell=ell, a=int(a))
            if ell <= args.weyl_maxrows:
                aw = a_weyl(mu, delta, 3, cache)
                rec['a_weyl'] = int(aw)
                if aw != a:
                    log(f'*** DISAGREEMENT at delta={delta} mu={mu}: amb={a} weyl={aw} -- HALT')
                    json.dump(dict(status='HALT: a-routes disagree', delta=delta, mu=list(mu), amb=int(a), weyl=int(aw)),
                              open(args.out + '.HALT', 'w'))
                    sys.exit(2)
            NS = N_S_tail_n(mu, delta, 3)
            so = stab_order(mu)
            rec.update(N_S=int(NS), stab=int(so), n_chi_lb=int(math.ceil(NS / so)))
            rows.append(rec)
            d = bylen.setdefault(ell, dict(count=0, sum_a=0, max_a=0, max_NS=0))
            d['count'] += 1; d['sum_a'] += int(a); d['max_a'] = max(d['max_a'], int(a)); d['max_NS'] = max(d['max_NS'], int(NS))
        summary[delta] = bylen
        log(f'delta={delta}: by length: ' + ', '.join(f'ell={k}: {v["count"]} weights, sum a={v["sum_a"]}, max a={v["max_a"]}, max N_S={v["max_NS"]}'
                                                       for k, v in sorted(bylen.items())) + f'  [{time.time()-t0:.1f}s]')
    out = dict(board_numbering='batch13', session='B13-05', n=3, dmax=args.dmax, maxrows=args.maxrows,
               a_routes=['wk8_s30_pleth.amb', 'wk9_s42_census.a_weyl'], N_S_route='wk9_s42_census.N_S_tail_n (r = ell(mu))',
               summary=summary, rows=rows)
    with open(args.out, 'w') as f:
        json.dump(out, f, indent=0)
    log(f'wrote {args.out}: {len(rows)} rows')


if __name__ == '__main__':
    main()
