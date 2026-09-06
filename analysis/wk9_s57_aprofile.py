#!/usr/bin/env python3
"""
Session 57 -- the a-profiles below the region at ell = 6.

The s39 table carries a(lam, delta) only for lam_1 >= delta at delta = 8..12.
Lemma L reads the ladder {(4 delta - |tail|, tail)} from its bottom, which is
below the eligibility line for most tails, so this script computes a for every
six-row partition of 4 delta with lam_1 < delta at delta = 8..12, and for every
six-row partition of 4 delta at delta = 6, 7 (both eligible and onset-only), by
the C plethysm engine (Murnaghan-Nakayama, two moduli, CRT), with an
independent Weyl-route check on a 5 per cent sample.

Banked to results/s57_cells/bank_aprofile.jsonl (append-only).

usage: python3 wk9_s57_aprofile.py [--deltas 6,7,8,9,10,11,12]
"""
import sys, os, json, time, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from wk9_s57_lib import partitions_exact, a_weyl_mod, log, ROOT

BANK = os.path.join(ROOT, 'results/s57_cells/bank_aprofile.jsonl')

if __name__ == '__main__':
    args = sys.argv[1:]
    deltas = [int(x) for x in args[args.index('--deltas') + 1].split(',')] if '--deltas' in args else [6, 7, 8, 9, 10, 11, 12]
    with open(os.path.join(ROOT, 'results/s57_config.jsonl'), 'a') as cf:
        cf.write(json.dumps(dict(run='aprofile', deltas=deltas, t=time.strftime('%Y-%m-%dT%H:%M:%S'))) + "\n")
    done = set()
    if os.path.exists(BANK):
        for ln in open(BANK):
            try: r = json.loads(ln); done.add((tuple(r['lam']), r['delta']))
            except Exception: pass
    fh = open(BANK, 'a')
    from wk9_s39_chars import PlethEngine, LIB
    LIB.memo_set_cap(1 << 24)
    rnd = random.Random(57)
    cache = {}
    for delta in deltas:
        t0 = time.time()
        cells = [l for l in partitions_exact(4 * delta, 6) if delta <= 7 or l[0] < delta]
        todo = [l for l in cells if (l, delta) not in done]
        log(f"[d{delta}] {len(cells)} six-row cells ({'all' if delta <= 7 else 'onset-only'}), {len(todo)} to do")
        if not todo: continue
        PE4 = PlethEngine(delta, d=4)
        n_chk = n_bad = 0
        for i, lam in enumerate(todo):
            a = PE4.a(lam)
            rec = dict(lam=list(lam), delta=delta, ell=6, a=a, route='PlethEngine d=4', eligible=lam[0] >= delta)
            if a >= 1 and rnd.random() < 0.05:
                aw, nt, nd = a_weyl_mod(lam, delta, 4, cache, box_cap=3e7)
                rec.update(a_weyl=aw, weyl_agree=(aw == a)); n_chk += 1; n_bad += (aw != a)
            fh.write(json.dumps(rec) + "\n")
            if (i + 1) % 200 == 0:
                fh.flush(); log(f"[d{delta}] {i+1}/{len(todo)} [{time.time()-t0:.0f}s] weyl checks {n_chk} disagreements {n_bad}")
        fh.flush()
        log(f"[d{delta}] done [{time.time()-t0:.0f}s]; weyl checks {n_chk}, disagreements {n_bad}")
        assert n_bad == 0, "ROUTE DISAGREEMENT on a"
    fh.close()
