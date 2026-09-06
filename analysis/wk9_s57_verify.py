#!/usr/bin/env python3
"""
Session 57 -- the independent re-checks (pre-registration P1 and the consistency
consequences of Lemma L and Proposition S), run after the banks are complete.

  V1  a at every delta = 10, ell = 6 cell of the s39 table recomputed by the
      modular Weyl route (a route that shares no character code with the C engine),
      plus a random sample of cells from the other (delta, ell) chunks of delta 10-12.
  V2  sk at a few delta = 10 cells recomputed by the house Python route
      scripts/ambient_screen.m_det (Murnaghan-Nakayama in Python, s24b lineage).
  V3  Lemma L on the data: a is non-decreasing up every ladder across all banked
      cells (s39 delta 8-12, the region, the a-profile, the families); h_pad likewise.
  V4  Proposition S on the data: a <= a_inf at every cell whose tail has a stable
      value, and a = a_inf at every such cell with delta >= |tail|.
  V5  the family bank: engine and Weyl values of a agree wherever both exist.
  V6  the (delta, ell) census counts equal the s39 candidate counts at delta 10-12.

usage: python3 wk9_s57_verify.py [--sample 60] [--skip-v1]
"""
import sys, os, json, glob, random, time
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'scripts'))
from wk9_s57_lib import (load_s39, region_cells, count_region, a_weyl_mod, tail_of, ladder_cell, ROOT, log)

CELLS = os.path.join(ROOT, 'results/s57_cells')

def all_a():
    A = {}
    s39, zeros = load_s39()
    for k, (a, sk) in s39.items(): A[k] = a
    for k in zeros: A[k] = 0
    for p in glob.glob(os.path.join(CELLS, 'bank_d*_l*.jsonl')) + [os.path.join(CELLS, 'bank_aprofile.jsonl'), os.path.join(CELLS, 'bank_below_l6.jsonl')]:
        if not os.path.exists(p): continue
        for ln in open(p):
            r = json.loads(ln); A[(tuple(r['lam']), r['delta'])] = r['a']
    fam = defaultdict(dict)
    p = os.path.join(CELLS, 'bank_families.jsonl')
    if os.path.exists(p):
        for ln in open(p):
            r = json.loads(ln)
            if r['value'] is not None: fam[(tuple(r['lam']), r['delta'])][r['col']] = r['value']
    for k, cols in fam.items():
        for c in ('a_engine', 'a_weyl'):
            if c in cols: A[k] = cols[c]
    return A, fam

if __name__ == '__main__':
    args = sys.argv[1:]
    nsample = int(args[args.index('--sample') + 1]) if '--sample' in args else 60
    out = {}
    s39, zeros = load_s39()
    rnd = random.Random(5757)
    # ---- V1
    box_cap = float(args[args.index('--box-cap') + 1]) if '--box-cap' in args else 2e6
    cache = {}
    if '--skip-v1' not in args and '--skip-v1a' not in args:
        t0 = time.time(); bad = []; n = 0
        for lam in region_cells(10, 6):
            a39 = s39[(lam, 10)][0] if (lam, 10) in s39 else 0
            aw, _, _ = a_weyl_mod(lam, 10, 4, cache)
            n += 1
            if aw != a39: bad.append((lam, a39, aw))
        log(f"V1a: delta 10 ell 6: {n} cells, Weyl route disagreements {len(bad)} [{time.time()-t0:.0f}s]")
        out['V1a'] = dict(cells=n, disagreements=bad)
    elif '--skip-v1a' in args:
        out['V1a'] = dict(cells=1874, disagreements=[], note='from the first run, results/logs/s57_verify_v1a.log')
    if '--skip-v1' not in args:
        # sample across the other chunks, restricted to cells whose tail box is within box_cap
        # (the Weyl route on balanced eight- and nine-row cells runs for hours; the restriction is stated in the report)
        from wk9_s57_lib import box_size
        pool = []
        for d in (10, 11, 12):
            for ell in (6, 7, 8, 9, 10):
                if (d, ell) == (10, 6): continue
                cells = [l for l in region_cells(d, ell) if box_size(l, d) <= box_cap]
                k = min(len(cells), max(1, nsample // 14) if ell < 10 else 2)
                pool += [(lam, d) for lam in rnd.sample(cells, k)]
        t0 = time.time(); bad = []; done_n = 0; skipped = []
        for lam, d in pool:
            a39 = s39[(lam, d)][0] if (lam, d) in s39 else 0
            try:
                aw, _, _ = a_weyl_mod(lam, d, 4, cache, box_cap=box_cap, terms_cap=20000)
            except MemoryError as e:
                skipped.append((list(lam), d, str(e))); continue
            done_n += 1
            if aw != a39: bad.append((lam, d, a39, aw))
            log(f"V1b: {lam} delta {d}: s39 {a39} weyl {aw} [{time.time()-t0:.0f}s]")
        log(f"V1b: sample of {len(pool)} cells across delta 10-12, ell 7-10 (tail box <= {box_cap:.0e}): {done_n} computed, disagreements {len(bad)}, skipped {len(skipped)} [{time.time()-t0:.0f}s]")
        out['V1b'] = dict(cells=done_n, disagreements=bad, skipped=skipped, box_cap=box_cap, sample=[[list(l), d] for l, d in pool])
    # ---- V2
    try:
        from ambient_screen import m_det as mdet_house, chi as chi_house
        picks = [((30, 2, 2, 2, 2, 2), 10), ((22, 12, 3, 1, 1, 1), 10), ((26, 6, 2, 2, 2, 2), 10)]
        res = []
        for lam, d in picks:
            t0 = time.time(); v = mdet_house(lam, 4, d); chi_house.cache_clear()
            res.append((lam, d, s39[(lam, d)][1], v, round(time.time() - t0, 1)))
            log(f"V2: house m_det {lam} delta {d}: {v} vs s39 {s39[(lam, d)][1]} [{time.time()-t0:.0f}s]")
        out['V2'] = dict(rows=[[list(l), d, s, v, t] for l, d, s, v, t in res], all_agree=all(s == v for _, _, s, v, _ in res))
    except Exception as e:
        log(f"V2: house route unavailable: {e}"); out['V2'] = dict(error=str(e))
    # ---- V3
    A, fam = all_a()
    by_tail = defaultdict(list)
    for (lam, d), a in A.items(): by_tail[tail_of(lam)].append((d, a))
    viol = []; steps = 0
    for t, cells in by_tail.items():
        cells.sort()
        for (d1, a1), (d2, a2) in zip(cells, cells[1:]):
            steps += 1
            if a2 < a1: viol.append((list(t), d1, a1, d2, a2))
    log(f"V3a: a non-decreasing up ladders: {steps} consecutive pairs over {len(by_tail)} ladders, violations {len(viol)}")
    out['V3a'] = dict(pairs=steps, ladders=len(by_tail), violations=viol)
    H = {}
    for p in glob.glob(os.path.join(CELLS, 'bank_d*_l*.jsonl')) + [os.path.join(CELLS, 'bank_below_l6.jsonl')]:
        if not os.path.exists(p): continue
        for ln in open(p):
            r = json.loads(ln)
            if r.get('h_pad') is not None: H[(tuple(r['lam']), r['delta'])] = r['h_pad']
    for k, cols in fam.items():
        if 'h_pad' in cols: H[k] = cols['h_pad']
    by_tail_h = defaultdict(list)
    for (lam, d), h in H.items(): by_tail_h[tail_of(lam)].append((d, h))
    violh = []; stepsh = 0
    for t, cells in by_tail_h.items():
        cells.sort()
        for (d1, h1), (d2, h2) in zip(cells, cells[1:]):
            stepsh += 1
            if h2 < h1: violh.append((list(t), d1, h1, d2, h2))
    log(f"V3b: h_pad non-decreasing up ladders: {stepsh} pairs, violations {len(violh)}")
    out['V3b'] = dict(pairs=stepsh, violations=violh)
    # ---- V4
    stable = {}
    p = os.path.join(CELLS, 'stable_a.jsonl')
    if os.path.exists(p):
        for ln in open(p):
            r = json.loads(ln); stable[tuple(r['tail'])] = r['a_inf']
    n_le = n_eq = 0; bad_le = []; bad_eq = []
    for (lam, d), a in A.items():
        t = tail_of(lam)
        if t not in stable: continue
        n_le += 1
        if a > stable[t]: bad_le.append((list(lam), d, a, stable[t]))
        if d >= sum(t):
            n_eq += 1
            if a != stable[t]: bad_eq.append((list(lam), d, a, stable[t]))
    log(f"V4: a <= a_inf at {n_le} cells (violations {len(bad_le)}); a = a_inf at the {n_eq} cells with delta >= |tail| (violations {len(bad_eq)})")
    out['V4'] = dict(cells=n_le, violations_le=bad_le, stable_cells=n_eq, violations_eq=bad_eq)
    # ---- V5
    both = [(k, c['a_engine'], c['a_weyl']) for k, c in fam.items() if 'a_engine' in c and 'a_weyl' in c]
    dis = [(list(k[0]), k[1], e, w) for k, e, w in both if e != w]
    log(f"V5: family cells with both a routes: {len(both)}, disagreements {len(dis)}")
    out['V5'] = dict(both=len(both), disagreements=dis)
    # ---- V6
    import csv
    cnt = defaultdict(int)
    with open(os.path.join(ROOT, 'results/longweight_screen.csv')) as fh:
        for r in csv.DictReader(fh): cnt[(int(r['delta']), int(r['ell']))] += 1
    mism = [(d, ell, cnt[(d, ell)], count_region(d, ell)) for d in (10, 11, 12) for ell in range(6, 11) if cnt[(d, ell)] != count_region(d, ell)]
    log(f"V6: census counts vs s39 candidate counts at delta 10-12: mismatches {len(mism)}")
    out['V6'] = dict(mismatches=mism)
    json.dump(out, open(os.path.join(CELLS, 'verify.json'), 'w'))
    log("written verify.json")
