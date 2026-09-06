#!/usr/bin/env python3
"""
Session 57 -- Task 1, coverage C3 + C4: the targeted families above delta = 12.

Families (results/PREREG_s57.md section 3):
  F1  the LMR ladder, tail (17, 2^7), ell = 9, delta = 12..24
  F2  the peaked ladders, tail (2^{ell-1}), ell = 6..10
  F3  the LMR shapes at the other lengths: tails (11,2^4) k=3, (13,2^5) k=4,
      (15,2^6) k=5, (19,2^8) k=7, as ladders
  F4  the five most balanced eligible cells of each (delta, ell), delta = 13..16
  F5  the ladders through the six-row negative record, continued to delta = 16

Routes.  a: the C plethysm engine (PlethEngine, N = 4 delta <= 64) and the
modular Weyl route (a_weyl_mod) wherever the tail box allows; both are banked
and asserted equal when both exist.  sk: MdetEngine, N <= 64 only (delta <= 16);
above that 'pending'.  h_pad: PlethEngine at d = 3 (3 delta <= 48, i.e.
delta <= 16), else the modular Weyl route at d = 3.  N_S: modular tail DP when
the cost is within the cap, else the merged lower bound.  Every CRT-reconstructed
engine value is accepted only if f^lam < P1 P2 / 2 (all of a, g, |T| are <= f^lam).

Each cell is banked as it completes to results/s57_cells/bank_families.jsonl
(append-only; reruns skip banked (lam, delta, col) triples).

usage: python3 wk9_s57_families.py --families F1,F2,F3 --deltas 13,14,15,16 [--terms-cap 20000] [--box-cap 3e7]
       python3 wk9_s57_families.py --families F1,F2,F3 --deltas 17,18,...,24   (Weyl only)
"""
import sys, os, json, time
from math import factorial
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from wk9_s57_lib import (region_cells, ladder_cell, tail_of, balance, stab_order, a_weyl_mod,
                         h_pad_weyl_mod, K_mod, crt2, merged_lower_bound, pieri_strips,
                         most_balanced_eligible, negative_record, lmr_weight, log, P1, P2, ROOT)
from wk9_s57_table import ns_cost, reach_class, SPARSE

BANK = os.path.join(ROOT, 'results/s57_cells/bank_families.jsonl')
NMAX_ENGINE = 64
CRT_BOUND = P1 * P2 // 2

def f_lam(lam):
    """number of standard Young tableaux (hook length formula)."""
    lam = [x for x in lam if x]; N = sum(lam)
    conj = [sum(1 for x in lam if x > j) for j in range(lam[0])] if lam else []
    h = 1
    for i, li in enumerate(lam):
        for j in range(li):
            h *= (li - j) + (conj[j] - i) - 1
    return factorial(N) // h

def family_cells(fams, deltas):
    """-> {delta: [(lam, family_tag)]}"""
    out = {d: [] for d in deltas}
    def add(d, lam, tag):
        if lam is None: return
        if len(lam) < 6 or len(lam) > 10 or lam[0] < d: return
        if (lam, tag) not in out[d]: out[d].append((lam, tag))
    for d in deltas:
        if 'F1' in fams:
            add(d, ladder_cell((17,) + (2,) * 7, d), 'F1')
        if 'F2' in fams:
            for ell in range(6, 11): add(d, ladder_cell((2,) * (ell - 1), d), f'F2_l{ell}')
        if 'F3' in fams:
            for k in (3, 4, 5, 7):
                lam_k, d_k = lmr_weight(k)
                add(d, ladder_cell(tail_of(lam_k), d), f'F3_k{k}')
        if 'F4' in fams:
            for ell in range(6, 11):
                for lam in most_balanced_eligible(d, ell, k=5): add(d, lam, f'F4_l{ell}')
        if 'F5' in fams:
            rec = negative_record()
            tails = sorted({tail_of(lam) for (lam, dd) in rec if len(lam) == 6})
            for t in tails: add(d, ladder_cell(t, d), 'F5')
    return out

def banked():
    keys = {}
    if os.path.exists(BANK):
        for ln in open(BANK):
            try: r = json.loads(ln)
            except json.JSONDecodeError: continue
            keys[(tuple(r['lam']), r['delta'], r['col'])] = r
    return keys

if __name__ == '__main__':
    args = sys.argv[1:]
    fams = args[args.index('--families') + 1].split(',')
    deltas = [int(x) for x in args[args.index('--deltas') + 1].split(',')]
    box_cap = float(args[args.index('--box-cap') + 1]) if '--box-cap' in args else 3e7
    terms_cap = int(args[args.index('--terms-cap') + 1]) if '--terms-cap' in args else 20000
    ns_cap = float(args[args.index('--ns-cap') + 1]) if '--ns-cap' in args else 2e9
    no_sk = '--no-sk' in args
    no_hpad = '--no-hpad' in args
    only_hpad = '--only-hpad' in args
    with open(os.path.join(ROOT, 'results/s57_config.jsonl'), 'a') as cf:
        cf.write(json.dumps(dict(run='families', families=fams, deltas=deltas, box_cap=box_cap, terms_cap=terms_cap,
                                 ns_cap=ns_cap, no_sk=no_sk, no_hpad=no_hpad, only_hpad=only_hpad, t=time.strftime('%Y-%m-%dT%H:%M:%S'))) + "\n")
    cells = family_cells(fams, deltas)
    done = banked()
    fh = open(BANK, 'a')
    def bank(lam, delta, col, value, route, extra=None):
        rec = dict(lam=list(lam), delta=delta, ell=len(lam), col=col, value=value, route=route,
                   t=time.strftime('%H:%M:%S'))
        if extra: rec.update(extra)
        fh.write(json.dumps(rec) + "\n"); fh.flush()
        done[(tuple(lam), delta, col)] = rec

    from wk9_s39_chars import PlethEngine, MdetEngine, LIB
    LIB.memo_set_cap(1 << 24)
    cache = {}
    for delta in deltas:
        todo = cells[delta]
        if not todo: continue
        log(f"[d{delta}] {len(todo)} family cells: " + ", ".join(f"{t}:{l}" for l, t in todo[:6]) + (" ..." if len(todo) > 6 else ""))
        N = 4 * delta
        use_engine = N <= NMAX_ENGINE
        PE4 = PE3 = ME = None
        t0 = time.time()
        if use_engine:
            PE4 = PlethEngine(delta, d=4); log(f"[d{delta}] PlethEngine d=4 built, support {PE4.rl.n} [{time.time()-t0:.0f}s]")
            PE3 = PlethEngine(delta, d=3); log(f"[d{delta}] PlethEngine d=3 built, support {PE3.rl.n} [{time.time()-t0:.0f}s]")
            if not no_sk:
                ME = MdetEngine(delta, n=4, verbose=True); log(f"[d{delta}] MdetEngine built [{time.time()-t0:.0f}s]")
        for lam, tag in todo:
            key = (lam, delta)
            bal = balance(lam); so = stab_order(lam); fl = f_lam(lam)
            crt_ok = fl < CRT_BOUND
            # ---- a
            a_e = a_w = None
            if only_hpad:
                # a is taken from the bank; nothing else is computed
                for col in ('a_engine', 'a_weyl'):
                    if (lam, delta, col) in done and done[(lam, delta, col)]['value'] is not None:
                        a_e = done[(lam, delta, col)]['value']
            if not only_hpad and use_engine and (lam, delta, 'a_engine') not in done:
                if crt_ok:
                    t1 = time.time(); a_e = PE4.a(lam)
                    bank(lam, delta, 'a_engine', a_e, 'PlethEngine d=4 (MN, two moduli, CRT)', dict(secs=round(time.time()-t1, 2), family=tag, f_lam=str(fl)))
                else:
                    bank(lam, delta, 'a_engine', None, 'skipped: f^lam >= P1 P2 / 2', dict(family=tag, f_lam=str(fl)))
            elif (lam, delta, 'a_engine') in done:
                a_e = done[(lam, delta, 'a_engine')]['value']
            if not only_hpad and (lam, delta, 'a_weyl') not in done:
                try:
                    t1 = time.time(); a_w, nt, nd = a_weyl_mod(lam, delta, 4, cache, box_cap=box_cap, terms_cap=terms_cap)
                    bank(lam, delta, 'a_weyl', a_w, 'Weyl alternation, modular tail DP (two primes, CRT)', dict(secs=round(time.time()-t1, 2), terms=nt, distinct=nd, family=tag))
                except MemoryError as e:
                    bank(lam, delta, 'a_weyl', None, f'skipped: {e}', dict(family=tag))
            elif (lam, delta, 'a_weyl') in done:
                a_w = done[(lam, delta, 'a_weyl')]['value']
            if a_e is not None and a_w is not None:
                assert a_e == a_w, ("ROUTE DISAGREEMENT on a", lam, delta, a_e, a_w)
            a = a_e if a_e is not None else a_w
            log(f"[d{delta}] {tag} {lam}: a={a} (engine {a_e}, weyl {a_w}) bal={bal} stab={so}")
            if a is None or a == 0:
                continue
            # ---- sk
            if only_hpad: ME = None
            if ME is not None and (lam, delta, 'sk') not in done:
                if crt_ok:
                    t1 = time.time(); g, T = ME.gT(lam); sk = (g + T) // 2
                    bank(lam, delta, 'sk', sk, 'MdetEngine (MN, two moduli, CRT)', dict(g=g, T=T, secs=round(time.time()-t1, 2), family=tag, f_lam=str(fl)))
                    log(f"[d{delta}] {tag} {lam}: sk={sk} (g={g}, T={T}) [{time.time()-t1:.1f}s]")
                else:
                    bank(lam, delta, 'sk', None, 'skipped: f^lam >= P1 P2 / 2', dict(family=tag))
            elif ME is None and (lam, delta, 'sk') not in done and not no_sk:
                bank(lam, delta, 'sk', None, 'pending: N > 64 (session 58)', dict(family=tag))
            # ---- h_pad
            if no_hpad and (lam, delta, 'h_pad') not in done:
                bank(lam, delta, 'h_pad', None, 'pending: skipped by --no-hpad (Weyl d=3 route too slow here)', dict(family=tag))
            if (lam, delta, 'h_pad') not in done or (only_hpad and done[(lam, delta, 'h_pad')]['value'] is None):
                if PE3 is not None:
                    t1 = time.time()
                    hp = 0
                    for nu in pieri_strips(lam, delta):
                        k3 = tuple(x for x in nu if x)
                        if len(k3) > delta or len(k3) > 10: continue
                        hp += PE3.a(k3)
                    bank(lam, delta, 'h_pad', hp, 'PlethEngine d=3 over the Pieri strips', dict(secs=round(time.time()-t1, 2), family=tag))
                else:
                    try:
                        t1 = time.time(); hp = h_pad_weyl_mod(lam, delta, cache, box_cap=box_cap, terms_cap=terms_cap)
                        bank(lam, delta, 'h_pad', hp, 'Weyl d=3 over the Pieri strips (modular DP)', dict(secs=round(time.time()-t1, 2), family=tag))
                    except MemoryError as e:
                        hp = None
                        bank(lam, delta, 'h_pad', None, f'skipped: {e}', dict(family=tag))
                log(f"[d{delta}] {tag} {lam}: h_pad={hp}")
            # ---- N_S
            if (lam, delta, 'N_S') not in done and not only_hpad:
                cost, box = ns_cost(lam, delta)
                lb = merged_lower_bound(lam, delta)
                if cost <= ns_cap:
                    t1 = time.time(); ns = crt2(K_mod(lam, delta, 4, P1), K_mod(lam, delta, 4, P2)); st = 'exact'
                    assert ns >= lb
                    bank(lam, delta, 'N_S', ns, 'modular tail DP (two primes, CRT)', dict(status=st, stab=so, nchi_est=-(-ns // so), reach=reach_class(-(-ns // so), st), secs=round(time.time()-t1, 2), family=tag))
                else:
                    ns = lb; st = 'lb'
                    bank(lam, delta, 'N_S', ns, 'merged 5-part lower bound (dominance)', dict(status=st, stab=so, nchi_est=-(-ns // so), reach=reach_class(-(-ns // so), st), family=tag))
                log(f"[d{delta}] {tag} {lam}: N_S={ns} ({st}) n_chi~={-(-ns // so)}")
        log(f"[d{delta}] family cells done [{time.time()-t0:.0f}s]")
        del PE4, PE3, ME
    fh.close()
