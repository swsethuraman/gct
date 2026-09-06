#!/usr/bin/env python3
"""
Session 57 -- Lemma L (first-row transport) applied to the record and the region.

For every cell (lam, delta) the ladder is {(4 d - |tail|, tail) : d}, tail = lam[1:].
Along a ladder a, mult_det and i_det are non-decreasing (Lemma L), with
i_det(upper) <= i_det(lower) + [a(upper) - a(lower)].  Hence, given the
negative record (i_det = 0 at every measured cell):

  dead_by_transport : some measured dead cell lies below on the ladder with the
                      same a                       -> i_det = 0, proved
  bounded           : a dead cell lies below       -> i_det <= a - a(highest dead cell below)
  unconstrained     : no dead cell below           -> i_det <= a

and, given the one cell with i_det >= 1 (LMR, (65,17,2^7) at delta 24):

  forced below      : i_det(d) >= 1 - [a(24) - a(d)]  -> >= 1 wherever a(d) = a(24).

Inputs: the negative record (ledgers), the region banks (delta 10-12), the
a-profile bank (ell = 6, delta 6-12 below the eligibility line), the family
bank, and the s39 table (delta 8-12).  Output: results/s57_cells/ladder_status.json
and results/s57_cells/ladder_profiles_l6.json, plus a printed summary.

usage: python3 wk9_s57_ladder.py
"""
import sys, os, json, glob
from collections import defaultdict, Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from wk9_s57_lib import negative_record, load_s39, tail_of, ladder_cell, gzip_copy, ROOT, log

CELLS = os.path.join(ROOT, 'results/s57_cells')

def load_all_a():
    """(lam, delta) -> a from every banked source; sources recorded."""
    A, src = {}, {}
    s39, zeros = load_s39()
    for k, (a, sk) in s39.items(): A[k] = a; src[k] = 's39'
    for k in zeros: A[k] = 0; src[k] = 's39'
    for p in glob.glob(os.path.join(CELLS, 'bank_d*_l*.jsonl')):
        for ln in open(p):
            r = json.loads(ln); k = (tuple(r['lam']), r['delta'])
            if k in A: assert A[k] == r['a'], ("a disagreement", k, A[k], r['a'])
            A[k] = r['a']; src[k] = 'table'
    p = os.path.join(CELLS, 'bank_aprofile.jsonl')
    if os.path.exists(p):
        for ln in open(p):
            r = json.loads(ln); k = (tuple(r['lam']), r['delta'])
            if k in A: assert A[k] == r['a'], ("a disagreement", k, A[k], r['a'])
            A[k] = r['a']; src[k] = 'aprofile'
    p = os.path.join(CELLS, 'bank_families.jsonl')
    if os.path.exists(p):
        for ln in open(p):
            r = json.loads(ln)
            if r['col'] not in ('a_engine', 'a_weyl') or r['value'] is None: continue
            k = (tuple(r['lam']), r['delta'])
            if k in A: assert A[k] == r['value'], ("a disagreement", k, A[k], r['value'], r['col'])
            A[k] = r['value']; src.setdefault(k, 'families')
    rec = negative_record()
    for k, (a, md, s) in rec.items():
        if k in A: assert A[k] == a, ("a disagreement record vs table", k, A[k], a)
        A[k] = a; src.setdefault(k, 'record')
    return A, src, rec

def ladder_status(lam, delta, A, dead_by_tail):
    """-> dict(status, room, dead_below=[(delta', a')], implied_by)"""
    t = tail_of(lam); a = A[(lam, delta)]
    below = sorted((d2, a2) for (d2, a2) in dead_by_tail.get(t, []) if d2 < delta)
    if not below:
        return dict(status='unconstrained', room=a, dead_below=[], implied_by=None)
    d_hi, a_hi = below[-1]
    for d2, a2 in below:
        assert a2 <= a, ("a not monotone along the ladder", lam, delta, (d2, a2))
    if a_hi == a:
        return dict(status='dead_by_transport', room=0, dead_below=below, implied_by=[d_hi, ladder_cell(t, d_hi)])
    return dict(status='bounded', room=a - a_hi, dead_below=below, implied_by=None)

if __name__ == '__main__':
    A, src, rec = load_all_a()
    dead_by_tail = defaultdict(list)
    for (lam, d), (a, md, s) in rec.items():
        dead_by_tail[tail_of(lam)].append((d, a))
    log(f"a known at {len(A)} cells; negative record {len(rec)} cells on {len(dead_by_tail)} ladders")

    # ---- 1. the record against itself (P5)
    implied = []
    for (lam, d), (a, md, s) in sorted(rec.items()):
        st = ladder_status(lam, d, A, dead_by_tail)
        if st['status'] == 'dead_by_transport':
            implied.append(dict(lam=list(lam), delta=d, a=a, implied_by=st['implied_by'], source=s))
    by_len = Counter(len(x['lam']) for x in implied)
    log(f"record cells implied by a lower dead cell with equal a: {len(implied)} "
        f"(six-row {by_len.get(6,0)} of 210, length-5 {by_len.get(5,0)} of {sum(1 for k in rec if len(k[0])==5)})")

    # ---- 2. the region at delta 10-12 (every cell with a >= 1), and the family cells
    status = {}
    counts = defaultdict(Counter)
    region_keys = [k for k, s in src.items() if s == 'table' and A[k] >= 1]
    fam_keys = [k for k, s in src.items() if s == 'families' and A[k] >= 1]
    for k in region_keys + fam_keys:
        lam, d = k
        st = ladder_status(lam, d, A, dead_by_tail)
        status[f"{d}|{','.join(map(str, lam))}"] = dict(lam=list(lam), delta=d, ell=len(lam), a=A[k], **st)
        counts[(d, len(lam))][st['status']] += 1
    for (d, ell) in sorted(counts):
        c = counts[(d, ell)]
        log(f"  delta {d} ell {ell}: dead_by_transport {c['dead_by_transport']}, bounded {c['bounded']}, unconstrained {c['unconstrained']}")

    # ---- 3. the ell = 6 ladder profiles from the bottom to the top banked degree
    profiles = {}
    tails6 = {tail_of(lam) for (lam, d) in A if len(lam) == 6}
    for t in sorted(tails6):
        prof = []
        for d in range(6, 25):
            c = ladder_cell(t, d)
            if c is None or (c, d) not in A: continue
            dead = (c, d) in rec
            prof.append(dict(delta=d, lam=list(c), a=A[(c, d)], dead=dead, eligible=c[0] >= d))
        if prof: profiles[','.join(map(str, t))] = prof

    # ---- 4. the LMR ladder: forcing from delta = 24 downward
    lmr = {}
    t = (17,) + (2,) * 7
    prof = [(d, A[(ladder_cell(t, d), d)]) for d in range(12, 25) if (ladder_cell(t, d), d) in A]
    if prof:
        top_d, top_a = prof[-1]
        lmr = dict(profile=prof, top=[top_d, top_a],
                   forced=[(d, max(0, 1 - (top_a - a))) for d, a in prof] if top_d == 24 else None)
        log("LMR ladder a-profile: " + ", ".join(f"{d}:{a}" for d, a in prof))
        if top_d == 24:
            forced = [d for d, f in lmr['forced'] if f >= 1]
            log(f"  i_det >= 1 forced at delta in {forced} (a equal to a(24) = {top_a})")

    # ---- 5. the record's ladders against their stable values (Proposition S): permanently dead,
    #         and for the others the first cell above the top dead cell where a grows (the 'next room' cell)
    stable = {}
    sp = os.path.join(CELLS, 'stable_a.jsonl')
    if os.path.exists(sp):
        for ln in open(sp):
            r = json.loads(ln); stable[tuple(r['tail'])] = r['a_inf']
    table = {}
    for p in glob.glob(os.path.join(CELLS, 'bank_d*_l*.jsonl')):
        for ln in open(p):
            r = json.loads(ln); table[(tuple(r['lam']), r['delta'])] = r
    ladders = []
    for t, cells in dead_by_tail.items():
        if t not in stable: continue
        top_d, top_a = max(cells)
        ai = stable[t]
        row = dict(tail=list(t), ell=len(t) + 1, a_inf=ai, top_dead=[top_d, top_a], permanently_dead=(top_a == ai),
                   n_dead=len(cells), room_above=ai - top_a)
        if top_a < ai:
            nxt = None
            for d in range(top_d + 1, 25):
                c = ladder_cell(t, d)
                if c is None or (c, d) not in A: continue
                if A[(c, d)] > top_a:
                    tr = table.get((c, d), {})
                    nxt = dict(delta=d, lam=list(c), a=A[(c, d)], new_room=A[(c, d)] - top_a, eligible=c[0] >= d,
                               nchi_est=tr.get('nchi_est'), N_S_status=tr.get('N_S_status'), reach=tr.get('reach'),
                               h_pad=tr.get('h_pad'), sk=tr.get('sk'))
                    break
            row['next_room_cell'] = nxt
        ladders.append(row)
    n_perm = sum(1 for r in ladders if r['permanently_dead'])
    log(f"record ladders with a stable value: {len(ladders)}; permanently dead (a(top dead) = a_inf): {n_perm}; "
        f"with room above: {len(ladders) - n_perm}")
    json.dump(dict(implied=implied, status=status, counts={f"{d}|{e}": dict(c) for (d, e), c in counts.items()}, lmr=lmr,
                   record_ladders=ladders),
              open(os.path.join(CELLS, 'ladder_status.json'), 'w'))
    json.dump(profiles, open(os.path.join(CELLS, 'ladder_profiles_l6.json'), 'w'))
    for name in ('ladder_status.json', 'ladder_profiles_l6.json'): gzip_copy(os.path.join(CELLS, name))
    log("written ladder_status.json, ladder_profiles_l6.json (and .gz copies for the repository)")
