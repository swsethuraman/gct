#!/usr/bin/env python3
"""
Session 57 -- Task 1, coverage C1 + C2: the selector table over delta = 10, 11, 12
(every cell of the brief's region there) and the census counts for every (delta, ell).

Per cell (see results/PREREG_s57.md section 2):
  a, sk        from the s39 C-engine table results/longweight_screen.csv
               (a re-verified by the Weyl route in wk9_s57_verify.py);
  h_pad        s42 definition, cubic plethysm by the C engine (PlethEngine, d = 3);
  bal          lam_1 - lam_ell;  stab = |Stab_W(lam)|;
  N_S          weight-space dimension by the modular tail DP (two primes, CRT)
               when the DP cost is within the cap, else the 5-variable merged
               lower bound (status 'lb');
  nchi_est     ceil(N_S / stab) -- an ESTIMATE (s46), for cost only;
  pad_forced   max(0, a - h_pad) <= i_pad (Corollary B2 + Lemma A of s52);
  lemmaA_dead  h_pad == 0 (mult_pad = 0, so D <= 0: excluded from the ranking).

Banked per (delta, ell) chunk to results/s57_cells/bank_d{delta}_l{ell}.jsonl
(append-only; a rerun skips banked cells) and published as csv.gz by
wk9_s57_publish.py.

usage: python3 wk9_s57_table.py --deltas 10,11,12 [--ells 6,7,8,9,10] [--cost-cap 5e8] [--cost-cheap 2e7]
       python3 wk9_s57_table.py --census          (the (delta, ell) counts only)
"""
import sys, os, json, time, math
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from wk9_s57_lib import (region_cells, count_region, stab_order, balance, tail_of, tails,
                         K_mod, crt2, merged_lower_bound, pieri_strips, load_s39, log,
                         P1, P2, ROOT)

DENSE, SPARSE = 20000, 120000

def reach_class(nchi, status):
    if nchi <= DENSE: c = 'dense'
    elif nchi <= SPARSE: c = 'sparse'
    else: c = 'beyond'
    return c if status == 'exact' else c + '?'

def ns_cost(lam, delta, n=4):
    r = len(lam); tl = lam[1:]
    nb = sum(1 for b in tails(r, n) if all(b[i] <= tl[i] for i in range(r - 1)))
    box = 1
    for x in tl: box *= (x + 1)          # slab size per (beta, d) step; the array is (delta+1) x box
    return nb * delta * box, box * (delta + 1)

def census_table():
    lines = ["| delta | ell=6 | ell=7 | ell=8 | ell=9 | ell=10 | total |", "|---|---|---|---|---|---|---|"]
    grand = 0
    per = {}
    for delta in range(10, 25):
        row = [count_region(delta, ell) for ell in range(6, 11)]
        per[delta] = row
        grand += sum(row)
        lines.append(f"| {delta} | " + " | ".join(f"{x:,}" for x in row) + f" | {sum(row):,} |")
    lines.append(f"| **all** | | | | | | **{grand:,}** |")
    return "\n".join(lines), per, grand

if __name__ == '__main__':
    args = sys.argv[1:]
    if '--census' in args:
        txt, per, grand = census_table()
        print(txt); print("grand total", grand)
        json.dump(dict(per={str(k): v for k, v in per.items()}, grand=grand),
                  open(os.path.join(ROOT, 'results/s57_cells/census_counts.json'), 'w'))
        sys.exit(0)
    deltas = [int(x) for x in args[args.index('--deltas') + 1].split(',')]
    ells = [int(x) for x in args[args.index('--ells') + 1].split(',')] if '--ells' in args else [6, 7, 8, 9, 10]
    cost_cap = float(args[args.index('--cost-cap') + 1]) if '--cost-cap' in args else 5e8
    cost_cheap = float(args[args.index('--cost-cheap') + 1]) if '--cost-cheap' in args else 2e7
    outdir = os.path.join(ROOT, 'results/s57_cells'); os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(ROOT, 'results/s57_config.jsonl'), 'a') as cf:
        cf.write(json.dumps(dict(run='table', deltas=deltas, ells=ells, cost_cap=cost_cap, cost_cheap=cost_cheap,
                                 t=time.strftime('%Y-%m-%dT%H:%M:%S'))) + "\n")

    s39, zeros = load_s39()
    log(f"s39 table: {len(s39)} cells with a >= 1, {len(zeros)} with a = 0")

    from wk9_s39_chars import PlethEngine, LIB
    LIB.memo_set_cap(1 << 24)          # 16M entries ~ 512 MB

    for delta in deltas:
        t0 = time.time()
        PE3 = PlethEngine(delta, d=3)
        log(f"[d{delta}] cubic plethysm engine built ({PE3.rl.n} classes) [{time.time()-t0:.0f}s]")
        cubic = {}
        def c3(nu):
            key = tuple(x for x in nu if x)
            if len(key) > delta or len(key) > 10: return 0
            if key not in cubic: cubic[key] = PE3.a(key)
            return cubic[key]
        for ell in ells:
            path = os.path.join(outdir, f'bank_d{delta}_l{ell}.jsonl')
            done = set()
            if os.path.exists(path):
                for ln in open(path):
                    try: done.add(tuple(json.loads(ln)['lam']))
                    except Exception: pass
            cells = region_cells(delta, ell)
            assert len(cells) == count_region(delta, ell)
            fh = open(path, 'a')
            n_new = 0; t1 = time.time()
            for lam in cells:
                if lam in done: continue
                key = (lam, delta)
                if key in s39:
                    a, sk = s39[key]
                elif key in zeros:
                    a, sk = 0, None
                else:
                    raise KeyError(f"cell {key} absent from the s39 table")
                rec = dict(lam=list(lam), delta=delta, ell=ell, tail=list(tail_of(lam)),
                           a=a, a_src='s39', sk=sk, sk_src='s39' if sk is not None else 'none',
                           bal=balance(lam), stab=stab_order(lam))
                if a >= 1:
                    hp = sum(c3(nu) for nu in pieri_strips(lam, delta))
                    rec.update(h_pad=hp, h_pad_src='engine_d3', pad_forced=max(0, a - hp),
                               lemmaA_dead=(hp == 0))
                    cost, box = ns_cost(lam, delta)
                    lb = merged_lower_bound(lam, delta)
                    # exact N_S where it is cheap, or where the lower bound leaves the cell
                    # inside the sparse frontier and the cost is within the cap; else the bound
                    if cost <= cost_cheap or (-(-lb // rec['stab']) <= SPARSE and cost <= cost_cap):
                        ns = crt2(K_mod(lam, delta, 4, P1), K_mod(lam, delta, 4, P2))
                        st = 'exact'
                        assert ns >= lb, ("merged lower bound above the exact value", lam, delta, ns, lb)
                    else:
                        ns = lb; st = 'lb'
                    nchi = -(-ns // rec['stab'])
                    rec.update(N_S=ns, N_S_status=st, nchi_est=nchi, reach=reach_class(nchi, st),
                               ns_cost=cost)
                else:
                    rec.update(h_pad=None, pad_forced=None, lemmaA_dead=None, N_S=None,
                               N_S_status='n/a', nchi_est=None, reach='n/a')
                fh.write(json.dumps(rec) + "\n"); n_new += 1
                if n_new % 500 == 0:
                    fh.flush()
                    log(f"[d{delta} l{ell}] {n_new} new cells ({len(done)} banked before) "
                        f"cubic table {len(cubic)} [{time.time()-t1:.0f}s]")
            fh.close()
            log(f"[d{delta} l{ell}] chunk complete: {len(cells)} cells, {n_new} new [{time.time()-t1:.0f}s]")
        log(f"[d{delta}] done; cubic coefficients tabulated: {len(cubic)} [{time.time()-t0:.0f}s]")
