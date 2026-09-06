#!/usr/bin/env python3
"""
Session 60 -- the ladder (tail) census for length 5, and the closing cells.

Ladder theorem (integrator notes 1-3 of session 60; proof checked in
docs/s60_report.md sec. 4).  For a tail rho = (lam_2, lam_3, lam_4, lam_5),
t = |rho|, the cells lam_delta = (4 delta - t, rho) form a ladder on which
multiplication by u = c_(4,0,0,0,0) is an injective map of highest-weight
spaces that descends injectively to C[D_5] and C[R_5]; so a, mult_det,
mult_red, i_det, i_red are non-decreasing in delta, and u is surjective for
delta >= t, so all are constant there: a_inf(rho) = a_t(rho), PROVED.  If
a_delta = a_inf then every step from delta on is an isomorphism and every
quantity is constant from delta on; the first such delta is delta_close(rho).
A determinant-side full-rank result at (lam_close, delta_close) therefore gives
i_det = 0 at EVERY rung of the ladder -- downward by monotonicity, upward by
stability -- hence D = i_det - i_red <= 0 at every rung, in every degree: the
tail is dead for D > 0 permanently.

Caution (integrator note 3): a_inf is taken from the PROVED value a_t, never
from an observed plateau (a_delta can plateau and rise again, e.g. rho = (4):
1, 1, 2, 2 at delta = 2..5).

For every tail that occurs in the length-5 census (delta 6..10, plus s54's
measured cells) this script records delta_min, the sequence a_delta from
delta_min to t, a_inf = a_t, delta_close, lam_close, and the size of the
closing cell (N_S, |Stab|, n_chi exact when affordable, h_pad there), plus the
census rungs the closing cell would settle.

usage: python3 analysis/wk9_s60_tails.py [--exact-cap 1500000]
writes results/s60_tail_census.json, results/s60_tail_census.md and
/home/claude/s60/closing_cells.json (the driver's cell list, ordered by cost).
"""
import sys, os, json, time, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
from wk9_s42_census import N_S_tail, stab_order, a_weyl, h_pad_weyl
from wk9_s45_build import orbit_setup_arr
from math import comb

N = 4; R = 5
CODE_SAFE_DELTA = 18      # the multiset combinadic of the s45 build is int64: comb(70 + delta - 1, delta) < 2^63


def log(*a): print(*a, file=sys.stderr, flush=True)


def ladder(rho, wc):
    t = sum(rho)
    dmin = max((t + rho[0] + 3) // 4, 1)          # 4 delta - t >= rho[0]
    while 4 * dmin - t < rho[0]: dmin += 1
    seq = []
    for d in range(dmin, t + 1):
        lam = (4 * d - t,) + tuple(rho)
        seq.append(a_weyl(lam, d, N, wc))
    a_inf = seq[-1]
    for k, v in enumerate(seq):
        assert v <= a_inf, ("a_delta exceeds a_t: monotonicity violated", rho, seq)
        if k and v < seq[k - 1]: raise AssertionError(("a_delta decreases", rho, seq))
    dclose = next(dmin + k for k, v in enumerate(seq) if v == a_inf) if a_inf > 0 else None
    return dict(t=t, delta_min=dmin, a_seq=seq, a_inf=a_inf, delta_close=dclose)


if __name__ == '__main__':
    args = sys.argv[1:]
    exact_cap = int(args[args.index('--exact-cap') + 1]) if '--exact-cap' in args else 1_500_000
    C = json.load(open(os.path.join(ROOT, 'results/s60_census.json')))
    C.update(json.load(open(os.path.join(ROOT, 'results/s60_census_d10.json'))))
    tails = collections.defaultdict(list)
    for d, o in C.items():
        for c in o['cells']:
            tails[tuple(c['lam'][1:])].append(dict(delta=c['delta'], lam=c['lam'], a=c['a'], red=c['red'], n_chi=c['n_chi'], src='census'))
    for d in (6, 7, 8, 9):
        for ln in open(os.path.join(ROOT, f'results/s54_cells_d{d}.jsonl')):
            r = json.loads(ln)
            if 'mult_det' in r:
                tails[tuple(r['lam'][1:])].append(dict(delta=d, lam=r['lam'], a=r['a'], red='s54', n_chi=None, src='s54'))
    log(f"{len(tails)} tails")
    wc = {}
    out = []
    t0 = time.time()
    for i, (rho, mem) in enumerate(sorted(tails.items(), key=lambda kv: (sum(kv[0]), kv[0]))):
        L = ladder(rho, wc)
        rec = dict(tail=list(rho), **L, rungs=sorted(mem, key=lambda m: m['delta']))
        # consistency with the census a at every rung
        for m in mem:
            k = m['delta'] - L['delta_min']
            expect = L['a_seq'][k] if k < len(L['a_seq']) else L['a_inf']      # rungs above t sit in the stable range
            assert k >= 0 and expect == m['a'], ("census a disagrees with the ladder sequence", rho, m, L['a_seq'])
        if L['a_inf'] > 0:
            dc = L['delta_close']; lam = (4 * dc - L['t'],) + tuple(rho)
            ns = N_S_tail(lam, dc, N); so = stab_order(lam)
            hp = h_pad_weyl(lam, dc, wc)
            if so == 1: nchi, ex = ns, True
            elif ns <= exact_cap and dc <= CODE_SAFE_DELTA:
                arr = orbit_setup_arr(N, R, dc, lam, verbose=False); nchi, ex = int(arr['n_chi']), True; del arr
            else: nchi, ex = (ns + so - 1) // so, False
            rec.update(lam_close=list(lam), close_N_S=ns, close_stab=so, close_n_chi=nchi, close_n_chi_exact=ex,
                       close_h_pad=hp, close_key=nchi ** 2 * (L['a_inf'] + 30), close_buildable=(dc <= CODE_SAFE_DELTA),
                       lam1_ge_3delta=(lam[0] >= 3 * dc))
        out.append(rec)
        if (i + 1) % 100 == 0: log(f"  {i+1} tails [{time.time()-t0:.0f}s]")
        if len(wc) > 3_000_000: wc.clear()
    json.dump(out, open(os.path.join(ROOT, 'results/s60_tail_census.json'), 'w'))
    live = [r for r in out if r['a_inf'] > 0]
    dead = [r for r in out if r['a_inf'] == 0]
    # closing cells for the driver, cheapest first
    cells = []
    for r in live:
        if not r['close_buildable']: continue
        cells.append(dict(lam=r['lam_close'], delta=r['delta_close'], a=r['a_inf'], h_pad=r['close_h_pad'], N_S=r['close_N_S'],
                          stab=r['close_stab'], n_chi=r['close_n_chi'], n_chi_exact=r['close_n_chi_exact'], key=r['close_key'],
                          red=('informative' if r['close_h_pad'] >= 1 else 'dead'), tail=r['tail'], t=r['t'],
                          rungs_settled=[m['delta'] for m in r['rungs']], closing=True))
    cells.sort(key=lambda c: (c['key'], c['N_S']))
    os.makedirs('/home/claude/s60', exist_ok=True)
    json.dump(cells, open('/home/claude/s60/closing_cells.json', 'w'))
    # markdown
    M = ["# Session 60 -- the length-5 ladder census and the closing cells", "",
         "For each tail `rho` occurring in the length-5 census (delta 6..10) or in s54's measured cells: `t = |rho|`, `delta_min`,",
         "the ambient sequence `a_delta` from `delta_min` to `t`, `a_inf = a_t` (proved stable value), `delta_close` = first delta with",
         "`a_delta = a_inf`, the closing cell `lam_close = (4 delta_close - t, rho)` and its size.  A determinant-side full-rank result at",
         "the closing cell settles the whole tail for `D > 0` in every degree.  `buildable`: `delta_close <= 18` (the int64 multiset code",
         "of the session-45 build); beyond that the build needs a different monomial code.", "",
         f"tails: {len(out)}; live (`a_inf > 0`): {len(live)}; dead at every degree (`a_inf = 0`): {len(dead)}; ",
         f"closing cells with `lam_1 >= 3 delta`: {sum(1 for r in live if r.get('lam1_ge_3delta'))}; ",
         f"buildable closing cells: {sum(1 for r in live if r['close_buildable'])}", ""]
    for cap in (3000, 10000, 30000, 100000, 300000, 1000000):
        sel = [c for c in cells if c['n_chi'] <= cap]
        M.append(f"- closing cells with `n_chi <= {cap}`: {len(sel)} tails, settling {sum(len(c['rungs_settled']) for c in sel)} census rungs")
    M += ["", "| tail | t | delta_min | a_delta (delta_min..t) | a_inf | delta_close | lam_close | close N_S | Stab | close n_chi | close h_pad | rungs in census |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in sorted(live, key=lambda r: r['close_key']):
        seq = ','.join(map(str, r['a_seq'][:12])) + (',…' if len(r['a_seq']) > 12 else '')
        M.append(f"| `{tuple(r['tail'])}` | {r['t']} | {r['delta_min']} | {seq} | {r['a_inf']} | {r['delta_close']} | `{tuple(r['lam_close'])}` | {r['close_N_S']} | {r['close_stab']} | {r['close_n_chi']}{'' if r['close_n_chi_exact'] else '~'} | {r['close_h_pad']} | {[m['delta'] for m in r['rungs']]} |")
    if dead:
        M += ["", "## Tails dead at every degree (`a_inf = 0`)", "", ', '.join(f"`{tuple(r['tail'])}`" for r in dead)]
    open(os.path.join(ROOT, 'results/s60_tail_census.md'), 'w').write("\n".join(M) + "\n")
    log(f"wrote results/s60_tail_census.{{json,md}} and /home/claude/s60/closing_cells.json: {len(cells)} closing cells [{time.time()-t0:.0f}s]")
    for c in cells[:8]: log('  ', c['lam'], 'd', c['delta'], 'a', c['a'], 'n_chi', c['n_chi'], 'tail', c['tail'], 'rungs', c['rungs_settled'])
