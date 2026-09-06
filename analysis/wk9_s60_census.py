#!/usr/bin/env python3
"""
Session 60 -- census of the balanced length-5 complement.

Session 54 swept the length-5 cells (n = 4, r = 5) at delta = 6, 7, 8, 9 with
the dense flint route and reached only the cells with nb <= 2500 (17/15/12/12
cells); the rest (88/224/423/696) were skipped as "over_maxnb".  This script
takes the complement of what s54 measured, from s54's own census
(results/s54_length5_census.json) and its own ledgers
(results/s54_cells_d{6,7,8,9}.jsonl), and scores every unmeasured cell with

    a       plethysm multiplicity (s54's value, re-derived here by the Weyl
            alternation of wk9_s42_census.a_weyl and asserted equal),
    h_pad   the normalisation bound of docs/reducible_engine.md sec. B
            (mult_red <= h_pad, proved); h_pad = 0 forces mult_red = 0,
    N_S     the weight-space dimension (nb of s54), exact, by the tail DP,
    stab    |Stab_W(lam)|,
    n_chi   the chi_lam-isotypic dimension: exact when the parts of lam are
            distinct (then n_chi = N_S) or when the orbit setup is cheap
            (N_S <= --exact-cap); otherwise the estimate ceil(N_S/|Stab|),
            flagged n_chi_exact = false,
    red     classification for the R_5 vs D_5 question:
              'informative'  h_pad >= 1  (a refutation mult_red > mult_det is
                             not excluded by a theorem),
              'dead'         h_pad = 0   (mult_red = 0 by Corollary B/B2 of
                             docs/reducible_ideal.md; only the determinant
                             side is a measurement there),
    key     the cost-order key n_chi^2 * (a + 30) (see PREREG_s60.md sec. 4).

delta = 10 (never touched at length 5 at any balance) is enumerated the same
way, with a by the Weyl alternation only (no s54 census exists there).

usage: python3 analysis/wk9_s60_census.py [--deltas 6,7,8,9,10] [--exact-cap 3000000]
writes results/s60_census.json and results/s60_census.md
"""
import sys, os, json, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
from wk9_s42_census import N_S_tail, stab_order, a_weyl, h_pad_weyl
from wk9_s42_hpad import h_pad as h_pad_frob
from wk9_s45_build import orbit_setup_arr

N = 4
R = 5


def log(*a):
    print(*a, file=sys.stderr, flush=True)


def length5_partitions(delta):
    """all partitions of 4*delta with exactly 5 (nonzero) parts."""
    tot = N * delta
    out = []
    def rec(rem, mx, cur):
        k = len(cur)
        if k == R:
            if rem == 0: out.append(tuple(cur))
            return
        left = R - k
        for v in range(min(rem - (left - 1), mx), 0, -1):
            if rem - v < (left - 1): break
            rec(rem - v, v, cur + [v])
    rec(tot, tot, [])
    return out


def s54_measured():
    """(lam, delta) -> record for every cell s54 actually measured."""
    out = {}
    for d in (6, 7, 8, 9):
        fn = os.path.join(ROOT, f'results/s54_cells_d{d}.jsonl')
        for ln in open(fn):
            rec = json.loads(ln)
            if 'mult_det' in rec:
                out[(tuple(rec['lam']), rec['delta'])] = rec
    return out


def score(lam, delta, a, exact_cap, wcache):
    ns = N_S_tail(lam, delta, N)
    so = stab_order(lam)
    # h_pad by the Frobenius cubic plethysm at delta <= 9 (as s42/s47 did) and by the Weyl
    # alternation over the Pieri strips at delta = 10 (as s52 did; the Frobenius memo is too large there)
    hp = h_pad_frob(lam, delta) if delta <= 9 else h_pad_weyl(lam, delta, wcache)
    aw = a_weyl(lam, delta, N, wcache)
    if a is None: a = aw
    assert aw == a, ("a: Weyl alternation disagrees with the census", lam, delta, aw, a)
    rec = dict(lam=list(lam), delta=delta, a=a, h_pad=hp, N_S=ns, stab=so,
               bal=lam[0] - lam[-1], lam1_ge_delta=lam[0] >= delta,
               red=('informative' if hp >= 1 else 'dead'))
    if so == 1:
        rec.update(n_chi=ns, n_chi_exact=True)
    elif ns <= exact_cap:
        arr = orbit_setup_arr(N, R, delta, lam, verbose=False)
        rec.update(n_chi=int(arr['n_chi']), n_chi_exact=True)
        del arr
    else:
        rec.update(n_chi=(ns + so - 1) // so, n_chi_exact=False)
    rec['key'] = rec['n_chi'] ** 2 * (a + 30)
    return rec


if __name__ == '__main__':
    args = sys.argv[1:]
    deltas = [int(x) for x in (args[args.index('--deltas') + 1].split(',') if '--deltas' in args else ['6', '7', '8', '9', '10'])]
    exact_cap = int(args[args.index('--exact-cap') + 1]) if '--exact-cap' in args else 3_000_000
    census54 = json.load(open(os.path.join(ROOT, 'results/s54_length5_census.json')))
    measured = s54_measured()
    out = {}
    wcache = {}
    t_all = time.time()
    for d in deltas:
        t0 = time.time()
        if str(d) in census54:
            cells = [(tuple(l), int(av)) for l, av in census54[str(d)]]
            allparts = set(length5_partitions(d))
            assert all(tuple(l) in allparts for l, _ in cells), "census cell is not a length-5 partition"
            src = 's54 census'
        else:
            cells = [(lam, None) for lam in length5_partitions(d)]
            src = 'Weyl alternation (new)'
        rows = []
        n_meas = 0
        for lam, a in cells:
            if (lam, d) in measured:
                n_meas += 1
                continue
            if a is None:
                a = a_weyl(lam, d, N, wcache)
                if a == 0: continue
            rows.append(score(lam, d, a, exact_cap, wcache))
        rows.sort(key=lambda r: (r['key'], r['N_S']))
        inf = [r for r in rows if r['red'] == 'informative']
        dead = [r for r in rows if r['red'] == 'dead']
        out[str(d)] = dict(source=src, n_cells_a_pos=len(cells) if src == 's54 census' else len(rows) + n_meas,
                           measured_by_s54=n_meas, unmeasured=len(rows),
                           informative=len(inf), dead=len(dead),
                           sum_a_unmeasured=sum(r['a'] for r in rows),
                           cells=rows)
        log(f"delta={d}: {len(cells) if src=='s54 census' else len(rows)} cells with a>0 ({src}); "
            f"measured by s54 {n_meas}; unmeasured {len(rows)} = informative {len(inf)} + dead {len(dead)}; "
            f"sum a (unmeasured) {sum(r['a'] for r in rows)}  [{time.time()-t0:.0f}s]")
        if len(wcache) > 2_000_000: wcache.clear()
    outfile = args[args.index('--outfile') + 1] if '--outfile' in args else 'results/s60_census.json'
    with open(os.path.join(ROOT, outfile), 'w') as f:
        json.dump(out, f)
    # markdown summary
    L = ["# Session 60 -- census of the balanced length-5 complement", "",
         "`n = 4`, `r = 5`.  Complement of the cells session 54 measured (its dense route reached `nb <= 2500`).",
         "`a` = plethysm (s54's census value, re-derived by the Weyl alternation and asserted equal);",
         "`h_pad` = normalisation bound (`mult_red <= h_pad`, proved); `h_pad = 0` forces `mult_red = 0`, so",
         "such a cell cannot refute `R_5 ⊆ D_5` and only its determinant side is a measurement ('dead').",
         "`n_chi` is exact unless marked `~` (estimate `ceil(N_S/|Stab|)`).", "",
         "| delta | cells `a>0` | measured by s54 | unmeasured | informative (`h_pad>=1`) | dead (`h_pad=0`) | sum `a` unmeasured | smallest `n_chi` unmeasured | largest `n_chi` |",
         "|---|---|---|---|---|---|---|---|---|"]
    for d in deltas:
        o = out[str(d)]; cs = o['cells']
        if cs:
            mn = min(cs, key=lambda r: r['n_chi']); mx = max(cs, key=lambda r: r['n_chi'])
            smn = f"{mn['n_chi']} at `{tuple(mn['lam'])}`"; smx = f"{mx['n_chi']}{'' if mx['n_chi_exact'] else '~'} at `{tuple(mx['lam'])}`"
        else:
            smn = smx = '-'
        L.append(f"| {d} | {o['n_cells_a_pos']} | {o['measured_by_s54']} | {o['unmeasured']} | {o['informative']} | {o['dead']} | {o['sum_a_unmeasured']} | {smn} | {smx} |")
    L += ["", "## Per-degree cost bands (unmeasured cells, by `n_chi`)", "",
          "| delta | `n_chi <= 3000` | `3000 < n_chi <= 20000` | `20000 < n_chi <= 100000` | `n_chi > 100000` |",
          "|---|---|---|---|---|"]
    for d in deltas:
        cs = out[str(d)]['cells']
        b = [sum(1 for r in cs if lo < r['n_chi'] <= hi) for lo, hi in ((0, 3000), (3000, 20000), (20000, 100000), (100000, 10**12))]
        L.append(f"| {d} | {b[0]} | {b[1]} | {b[2]} | {b[3]} |")
    L += ["", "## The twenty cheapest unmeasured informative cells overall (order key `n_chi^2 (a+30)`)", "",
          "| delta | lam | a | h_pad | N_S | Stab | n_chi | key |", "|---|---|---|---|---|---|---|---|"]
    allinf = sorted((r for d in deltas for r in out[str(d)]['cells'] if r['red'] == 'informative'), key=lambda r: r['key'])
    for r in allinf[:20]:
        L.append(f"| {r['delta']} | `{tuple(r['lam'])}` | {r['a']} | {r['h_pad']} | {r['N_S']} | {r['stab']} | {r['n_chi']}{'' if r['n_chi_exact'] else '~'} | {r['key']:.3g} |")
    with open(os.path.join(ROOT, outfile.replace('.json', '.md')), 'w') as f:
        f.write("\n".join(L) + "\n")
    log(f"wrote {outfile} and its .md [{time.time()-t_all:.0f}s]")
