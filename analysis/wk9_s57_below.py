#!/usr/bin/env python3
"""
Session 57 -- the six-row slices BELOW the region (delta = 6..9, ell = 6, eligible,
a >= 1): the same columns as the region table (h_pad, N_S, n_chi estimate, sk where
the s39 table has it, else by the C engine at delta = 6, 7), so that the criteria
can be scored and the unmeasured cheap cells below the region can be listed next
to the region's own.

a comes from the a-profile bank (delta 6, 7, engine) and the s39 table (delta 8, 9).
Banked to results/s57_cells/bank_below_l6.jsonl (append-only).
"""
import sys, os, json, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from wk9_s57_lib import (load_s39, stab_order, balance, tail_of, pieri_strips, K_mod, crt2,
                         merged_lower_bound, negative_record, P1, P2, ROOT, log)
from wk9_s57_table import ns_cost, reach_class, SPARSE

BANK = os.path.join(ROOT, 'results/s57_cells/bank_below_l6.jsonl')

if __name__ == '__main__':
    with open(os.path.join(ROOT, 'results/s57_config.jsonl'), 'a') as cf:
        cf.write(json.dumps(dict(run='below_l6', deltas=[6, 7, 8, 9], t=time.strftime('%Y-%m-%dT%H:%M:%S'))) + "\n")
    s39, zeros = load_s39()
    ap = {}
    for ln in open(os.path.join(ROOT, 'results/s57_cells/bank_aprofile.jsonl')):
        r = json.loads(ln); ap[(tuple(r['lam']), r['delta'])] = r['a']
    rec = negative_record()
    done = set()
    if os.path.exists(BANK):
        for ln in open(BANK):
            r = json.loads(ln); done.add((tuple(r['lam']), r['delta']))
    fh = open(BANK, 'a')
    from wk9_s39_chars import PlethEngine, MdetEngine, LIB
    LIB.memo_set_cap(1 << 23)
    for delta in (6, 7, 8, 9):
        t0 = time.time()
        if delta <= 7:
            cells = sorted((lam, a) for (lam, d), a in ap.items() if d == delta and a >= 1 and lam[0] >= delta)
            ME = MdetEngine(delta, n=4)
        else:
            cells = sorted((lam, a) for (lam, d), (a, sk) in s39.items() if d == delta and len(lam) == 6)
            ME = None
        PE3 = PlethEngine(delta, d=3); cubic = {}
        def c3(nu):
            key = tuple(x for x in nu if x)
            if len(key) > delta or len(key) > 10: return 0
            if key not in cubic: cubic[key] = PE3.a(key)
            return cubic[key]
        n_new = 0
        for lam, a in cells:
            if (lam, delta) in done: continue
            sk = s39[(lam, delta)][1] if (lam, delta) in s39 else ME.m_det(lam)
            hp = sum(c3(nu) for nu in pieri_strips(lam, delta))
            so = stab_order(lam)
            cost, box = ns_cost(lam, delta)
            lb = merged_lower_bound(lam, delta)
            if cost <= 5e8:
                ns = crt2(K_mod(lam, delta, 4, P1), K_mod(lam, delta, 4, P2)); st = 'exact'
            else:
                ns = lb; st = 'lb'
            nchi = -(-ns // so)
            rec_ = dict(lam=list(lam), delta=delta, ell=6, tail=list(tail_of(lam)), a=a,
                        a_src=('aprofile' if delta <= 7 else 's39'), sk=sk, sk_src=('engine' if delta <= 7 else 's39'),
                        h_pad=hp, h_pad_src='engine_d3', pad_forced=max(0, a - hp), lemmaA_dead=(hp == 0),
                        bal=balance(lam), stab=so, N_S=ns, N_S_status=st, nchi_est=nchi, reach=reach_class(nchi, st),
                        dead=((lam, delta) in rec))
            fh.write(json.dumps(rec_) + "\n"); n_new += 1
        fh.flush()
        log(f"[d{delta}] {len(cells)} eligible six-row cells, {n_new} new [{time.time()-t0:.0f}s]")
    fh.close()
