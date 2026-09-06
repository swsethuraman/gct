#!/usr/bin/env python3
"""
Session 57 -- Task 3: the criteria of the pre-registration scored against the
negative record, and the nominee lists of each criterion in the region.

Criteria (results/PREREG_s57.md section 4), each an ordering of a (delta, ell)
slice of eligible cells with a >= 1:
  K1 balance      ascending lam_1 - lam_ell
  K2 closeness    ascending sk / a
  K3 LMR shape    ascending |lam_2 - (2k+5)| + sum_{i>=3} |lam_i - 2|, k = ell - 3; ties by lam_1
  K4 frontier     ascending delta, then n_chi~, among cells not dead by transport
  K5 new room     descending a - a(highest dead cell below on the ladder), dead-by-transport removed
A cell's percentile in a slice is (#cells strictly ahead of it) / (slice size).

Slice populations: ell = 5 from s38's tables (results/occurrence_screen.csv,
results/screen_d10.csv); ell = 6 at delta = 6, 7 from the a-profile bank plus
sk by the C engine here; ell = 6..10 at delta = 8, 9 from the s39 table; the
region (delta 10-12) from the table banks.

Output: results/s57_cells/falsify.json and a printed summary.
"""
import sys, os, json, csv, glob, statistics
from collections import defaultdict, Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from wk9_s57_lib import (load_json_any, gzip_copy, negative_record, load_s39, region_cells, count_region, tail_of, balance,
                         stab_order, ladder_cell, lmr_weight, ROOT, log)

CELLS = os.path.join(ROOT, 'results/s57_cells')

def k3_dist(lam):
    ell = len(lam); k = ell - 3
    return abs(lam[1] - (2 * k + 5)) + sum(abs(x - 2) for x in lam[2:])

def load_slices():
    """(delta, ell) -> {lam: dict(a, sk, ...)} for eligible cells with a >= 1."""
    S = defaultdict(dict)
    # ell = 5, s38
    for p in ('results/occurrence_screen.csv', 'results/screen_d10.csv'):
        fp = os.path.join(ROOT, p)
        if not os.path.exists(fp): continue
        with open(fp) as fh:
            for r in csv.DictReader(fh):
                lam = tuple(int(x) for x in r['lam'].split('|')); d = int(r['delta'])
                a = int(r['a']); sk = int(r['m_det']) if r.get('m_det') not in (None, '', '-1') else None
                if a >= 1 and lam[0] >= d and len(lam) == 5:
                    S[(d, 5)][lam] = dict(a=a, sk=sk)
    # ell = 6..10, s39 (delta 8-12) -- the region banks override at 10-12
    s39, zeros = load_s39()
    for (lam, d), (a, sk) in s39.items():
        if lam[0] >= d: S[(d, len(lam))][lam] = dict(a=a, sk=sk)
    for p in glob.glob(os.path.join(CELLS, 'bank_d*_l*.jsonl')):
        for ln in open(p):
            r = json.loads(ln)
            if r['a'] >= 1:
                lam = tuple(r['lam'])
                S[(r['delta'], r['ell'])][lam] = dict(a=r['a'], sk=r['sk'], h_pad=r['h_pad'], N_S=r['N_S'],
                                                     N_S_status=r['N_S_status'], nchi_est=r['nchi_est'],
                                                     lemmaA_dead=r['lemmaA_dead'], pad_forced=r['pad_forced'])
    # ell = 6 at delta 6, 7: a from the a-profile bank; sk by the engine
    ap = os.path.join(CELLS, 'bank_aprofile.jsonl')
    need_sk = []
    if os.path.exists(ap):
        for ln in open(ap):
            r = json.loads(ln)
            if r['delta'] in (6, 7) and r['a'] >= 1 and r['lam'][0] >= r['delta']:
                lam = tuple(r['lam']); S[(r['delta'], 6)][lam] = dict(a=r['a'], sk=None); need_sk.append((lam, r['delta']))
    if need_sk:
        from wk9_s39_chars import MdetEngine, LIB
        LIB.memo_set_cap(1 << 22)
        for d in (6, 7):
            ME = MdetEngine(d, n=4)
            for lam, dd in need_sk:
                if dd == d: S[(d, 6)][lam]['sk'] = ME.m_det(lam)
    return S

def percentiles(slice_cells, key, ascending=True):
    """lam -> percentile under the ordering by key (ties share the best rank)."""
    items = [(key(lam, v), lam) for lam, v in slice_cells.items() if key(lam, v) is not None]
    items.sort(key=lambda x: x[0], reverse=not ascending)
    n = len(items); out = {}
    i = 0
    while i < n:
        j = i
        while j < n and items[j][0] == items[i][0]: j += 1
        for _, lam in items[i:j]: out[lam] = i / n
        i = j
    return out, n

if __name__ == '__main__':
    rec = negative_record()
    S = load_slices()
    ladder = load_json_any(os.path.join(CELLS, 'ladder_status.json'))
    st_by_key = {k: v for k, v in ladder['status'].items()}
    def lstatus(lam, d): return st_by_key.get(f"{d}|{','.join(map(str, lam))}")

    keys = {
        'K1': (lambda lam, v: balance(lam), True),
        'K2': (lambda lam, v: (v['sk'] / v['a']) if v.get('sk') is not None else None, True),
        'K3': (lambda lam, v: (k3_dist(lam), lam[0]), True),
    }
    report = dict(dead_percentiles={}, slices={}, nominees={})
    dead_pct = {k: [] for k in keys}
    dead_rows = []
    onset_only = []
    for (lam, d), (a, md, s) in sorted(rec.items()):
        sl = S.get((d, len(lam)))
        if sl is None or lam not in sl:
            if lam[0] < d: onset_only.append((lam, d)); continue
            log(f"WARNING dead cell {lam} delta {d} not in its slice population"); continue
        row = dict(lam=list(lam), delta=d, ell=len(lam), a=a, sk=sl[lam].get('sk'), bal=balance(lam), k3=k3_dist(lam))
        for kname, (kf, asc) in keys.items():
            pct, n = percentiles(sl, kf, asc)
            if lam in pct:
                row[kname] = pct[lam]; row[kname + '_n'] = n; dead_pct[kname].append(pct[lam])
        dead_rows.append(row)
    for kname in keys:
        v = dead_pct[kname]
        if not v: continue
        q = statistics.quantiles(v, n=4) if len(v) > 3 else v
        report['dead_percentiles'][kname] = dict(n=len(v), min=min(v), q1=q[0], median=q[1], q3=q[2], max=max(v),
                                                 frac_first_quartile=sum(1 for x in v if x <= 0.25) / len(v),
                                                 frac_first_decile=sum(1 for x in v if x <= 0.10) / len(v),
                                                 frac_top_cell=sum(1 for x in v if x == 0.0) / len(v))
        log(f"{kname}: dead cells n={len(v)} min={min(v):.3f} q1={q[0]:.3f} median={q[1]:.3f} q3={q[2]:.3f} max={max(v):.3f} "
            f"in first quartile {report['dead_percentiles'][kname]['frac_first_quartile']:.2f}, first decile "
            f"{report['dead_percentiles'][kname]['frac_first_decile']:.2f}, ranked first {report['dead_percentiles'][kname]['frac_top_cell']:.2f}")
    # per-slice: the first nominee of each criterion and whether it is dead
    for (d, ell), sl in sorted(S.items()):
        if not sl: continue
        entry = dict(size=len(sl))
        for kname, (kf, asc) in keys.items():
            pct, n = percentiles(sl, kf, asc)
            firsts = sorted([lam for lam, p in pct.items() if p == 0.0])
            entry[kname] = dict(first=[list(l) for l in firsts[:3]], n_first=len(firsts),
                                first_dead=[((l, d) in rec) for l in firsts[:3]],
                                first_value=[kf(l, sl[l]) for l in firsts[:3]])
        # the balanced corner: how many of the 5 most balanced are measured
        bal_sorted = sorted(sl, key=lambda l: (balance(l), l[0], l))
        entry['balanced5_dead'] = sum(1 for l in bal_sorted[:5] if (l, d) in rec)
        entry['dead'] = sum(1 for l in sl if (l, d) in rec)
        report['slices'][f"{d}|{ell}"] = entry
    # the LMR cell in its slice (delta 24, ell 9): K1 and K3 percentiles by enumeration
    lam_lmr, d_lmr = lmr_weight(6)
    cells = region_cells(24, 9)
    n = len(cells); assert n == count_region(24, 9)
    b = balance(lam_lmr)
    ahead = sum(1 for l in cells if balance(l) < b)
    report['lmr'] = dict(lam=list(lam_lmr), delta=24, ell=9, slice_size=n, bal=b, K1_percentile=ahead / n,
                         K1_rank=ahead + 1, K3_percentile=0.0,
                         max_balance=max(balance(l) for l in cells), min_balance=min(balance(l) for l in cells),
                         n_more_skewed=sum(1 for l in cells if balance(l) > b))
    log(f"LMR cell {lam_lmr} at delta 24: balance {b}, K1 percentile {ahead/n:.4f} (rank {ahead+1} of {n}); "
        f"{report['lmr']['n_more_skewed']} cells are more skewed; slice balance range [{report['lmr']['min_balance']}, {report['lmr']['max_balance']}]")
    # nominee lists in the region (delta 10-12 and the families), K1/K2/K3 first 10 per (delta, ell), with status
    for (d, ell), sl in sorted(S.items()):
        if d < 10: continue
        noms = {}
        for kname, (kf, asc) in keys.items():
            pct, nn = percentiles(sl, kf, asc)
            order = sorted(pct, key=lambda l: (pct[l], l))[:10]
            noms[kname] = [dict(lam=list(l), a=sl[l]['a'], sk=sl[l].get('sk'), h_pad=sl[l].get('h_pad'),
                                nchi_est=sl[l].get('nchi_est'), N_S_status=sl[l].get('N_S_status'),
                                lemmaA_dead=sl[l].get('lemmaA_dead'), pad_forced=sl[l].get('pad_forced'),
                                transport=(lstatus(l, d) or {}).get('status'), room=(lstatus(l, d) or {}).get('room'),
                                value=kf(l, sl[l]) if kname != 'K3' else k3_dist(l)) for l in order]
        report['nominees'][f"{d}|{ell}"] = noms
    report['dead_rows'] = dead_rows
    report['onset_only_dead'] = [[list(l), d] for l, d in onset_only]
    json.dump(report, open(os.path.join(CELLS, 'falsify.json'), 'w'))
    log("written falsify.json")
