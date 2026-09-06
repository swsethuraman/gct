#!/usr/bin/env python3
"""
Session 57 -- the nominee list, assembled from the analyses (report section 5).

  T1  room-1 cells: ladders touched by the record whose next cell adds exactly one
      highest-weight vector (Lemma L); a dead verdict at a cell with a = a_inf closes
      the ladder permanently.  Sorted by n_chi~.
  T2  first stable region cells of the open short ladders (|tail| <= 16, a_inf >= 1,
      not permanently dead, not the peaked tail), ell = 6..10, sorted by n_chi~.
  T3  the LMR ladder cells nearest the known kernel (delta = 21..24), with their sizes.
  T4  the balanced corner: the K1 first nominees of the slices delta = 8..12 at ell = 6, with costs.

Output: results/s57_cells/nominees.json and a printed markdown table.
"""
import sys, os, json, glob
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from wk9_s57_lib import ladder_cell, tail_of, negative_record, ROOT, log

CELLS = os.path.join(ROOT, 'results/s57_cells')
def J(name):
    return load_json_any(os.path.join(CELLS, name))

if __name__ == '__main__':
    ladder = J('ladder_status.json'); short = J('short_ladders.json'); fals = J('falsify.json'); pub = J('publish_summary.json')
    rec = negative_record()
    tab = {}
    for p in glob.glob(os.path.join(CELLS, 'bank_d*_l*.jsonl')) + [os.path.join(CELLS, 'bank_below_l6.jsonl')]:
        if not os.path.exists(p): continue
        for ln in open(p):
            r = json.loads(ln); tab[(tuple(r['lam']), r['delta'])] = r
    fam = {(tuple(int(x) for x in r['lam'].strip('()').split(',')), r['delta']): r for r in pub['families']}
    stable = {}
    for ln in open(os.path.join(CELLS, 'stable_a.jsonl')):
        r = json.loads(ln); stable[tuple(r['tail'])] = r['a_inf']
    def info(lam, d):
        r = tab.get((lam, d))
        if r: return dict(a=r['a'], sk=r['sk'], h_pad=r['h_pad'], pad_forced=r['pad_forced'], nchi=r['nchi_est'], ns_status=r['N_S_status'], reach=r['reach'], lemmaA=r['lemmaA_dead'])
        r = fam.get((lam, d))
        if r: return dict(a=r['a'], sk=r['sk'], h_pad=r['h_pad'], pad_forced=r['pad_forced'], nchi=r['nchi_est'], ns_status=r['N_S_status'], reach=r['reach'], lemmaA=(r['h_pad'] == 0 if r['h_pad'] is not None else None))
        return {}
    T1 = []
    for r in ladder['record_ladders']:
        n = r.get('next_room_cell')
        if not n or r['permanently_dead']: continue
        lam = tuple(n['lam']); ci = info(lam, n['delta'])
        ci.pop('a', None)
        T1.append(dict(tail=r['tail'], a_inf=r['a_inf'], top_dead=r['top_dead'], lam=list(lam), delta=n['delta'], a=n['a'], new_room=n['new_room'],
                       stable=(n['a'] == r['a_inf']), **ci))
    T1.sort(key=lambda x: (x['new_room'], x.get('nchi') or 10**12))
    T2 = []
    for r in short:
        if r['a_inf'] < 1 or r['permanently_dead']: continue
        if all(x == 2 for x in r['tail']): continue          # Theorem P
        f = r['first_region_stable']
        if not f['lam']: continue
        lam = tuple(f['lam']); ci = info(lam, f['delta']); ci.pop('a', None)
        T2.append(dict(ell=r['ell'], tail=r['tail'], size=r['size'], a_inf=r['a_inf'], lam=list(lam), delta=f['delta'], a=f['a'],
                       touched=r['any_dead'], K_inf_over_stab=r['K_inf_over_stab'],
                       nchi=f['nchi_est'], ns_status=f['N_S_status'], reach=(f['reach'] or '').rstrip('?'), sk=f['sk'] if f['sk'] is not None else ci.get('sk'),
                       h_pad=ci.get('h_pad'), pad_forced=ci.get('pad_forced'), lemmaA=ci.get('lemmaA')))
    T2.sort(key=lambda x: (x.get('nchi') or 10**12))
    T3 = []
    t = (17,) + (2,) * 7
    for d in range(12, 25):
        lam = ladder_cell(t, d); r = fam.get((lam, d))
        if not r: continue
        T3.append(dict(lam=list(lam), delta=d, a=r['a'], sk=r['sk'], h_pad=r['h_pad'], pad_forced=r['pad_forced'], nchi=r['nchi_est'], ns_status=r['N_S_status']))
    T4 = []
    for key, s in fals['slices'].items():
        d, e = map(int, key.split('|'))
        if e != 6 or d < 8 or d > 12: continue
        for lam in s['K1']['first'][:3]:
            lam = tuple(lam); ci = info(lam, d)
            T4.append(dict(lam=list(lam), delta=d, bal=lam[0] - lam[-1], dead=((lam, d) in rec), a_inf=stable.get(tail_of(lam)), **ci))
    T4.sort(key=lambda x: (x['delta'], x['bal']))
    json.dump(dict(T1=T1, T2=T2, T3=T3, T4=T4), open(os.path.join(CELLS, 'nominees.json'), 'w'))
    print("### T1 room-1 cells (new room = 1), by n_chi~")
    print("| tail | a_∞ | top dead (δ,a) | cell | δ | a | stable? | h_pad | pad-forced | n_χ~ | reach |\n|---|---|---|---|---|---|---|---|---|---|---|")
    for x in T1:
        if x['new_room'] != 1: continue
        print(f"| `{tuple(x['tail'])}` | {x['a_inf']} | ({x['top_dead'][0]},{x['top_dead'][1]}) | `{tuple(x['lam'])}` | {x['delta']} | {x['a']} | {'yes' if x['stable'] else 'no'} | {x.get('h_pad')} | {x.get('pad_forced')} | {x.get('nchi')} | {x.get('reach')} |")
    print("\n### T2 first stable cells of open short ladders, dense frontier only")
    print("| ℓ | tail | |λ̄| | a_∞ | cell | δ | a | sk | h_pad | pad-forced | n_χ~ | K_∞/|Stab'| |\n|---|---|---|---|---|---|---|---|---|---|---|---|")
    for x in T2:
        if (x.get('nchi') or 10**12) > 20000: continue
        print(f"| {x['ell']} | `{tuple(x['tail'])}` | {x['size']} | {x['a_inf']} | `{tuple(x['lam'])}` | {x['delta']} | {x['a']} | {x.get('sk')} | {x.get('h_pad')} | {x.get('pad_forced')} | {x.get('nchi')} | {x['K_inf_over_stab']} |")
    print("\n### T3 the LMR ladder")
    for x in T3: print(x)
    print("\n### T4 balanced corner")
    for x in T4: print(x)
    log(f"T1 {len(T1)} (room 1: {sum(1 for x in T1 if x['new_room']==1)}), T2 {len(T2)} (dense: {sum(1 for x in T2 if (x.get('nchi') or 10**12) <= 20000)}), T3 {len(T3)}, T4 {len(T4)}")
