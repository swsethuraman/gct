#!/usr/bin/env python3
"""B13-10 -- the report's tables, generated from the banked records so that no
number in docs/b13_10_report.md is typed by hand."""
import json, os, sys, glob
import numpy as np
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
SC = '/home/claude/b13_10_scratch'


def last_per_id(fn):
    out = {}
    for l in open(fn):
        if not l.strip(): continue
        r = json.loads(l); out[r['id']] = r
    return out


def main():
    S = last_per_id(os.path.join(ROOT, 'results', 'b13_10', 'suite.jsonl'))
    order = ['A1', 'A2', 'A3', 'A4', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'D1', 'X1', 'X2']
    print("### SUITE")
    print("| id | n | cell | a | N_S·δ | \\|Stab\\| | n_χ | nnz(E) | identical | kernel on E_old | banked ranks | old peak | lean peak | ×mem | old s | lean s | ×time |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    ratios = []
    for i in order:
        r = S.get(i)
        if not r: continue
        b = r.get('build_old', {}).get('rec'); l = r.get('build_lean', {}).get('rec')
        if not b or not l: 
            print(f"| {i} | | | | | | | | BUILD FAILED | | | | | | | | |"); continue
        cmp = r.get('rank_compare', {})
        ranks = 'n/a (a = 0)' if r['a'] == 0 else ('all ' + str(len(cmp)) + ' reproduce' if cmp and all(v['match'] for v in cmp.values()) else 'MISMATCH')
        rm = b['hwm_above_baseline_gb'] / l['hwm_above_baseline_gb']; rt = l['secs']['total'] / b['secs']['total']
        ratios.append((b['NS_delta'], rm, rt, i))
        cell = '(' + ','.join(map(str, r['lam'])) + ')_' + str(r['delta'])
        print(f"| {i} | {r['n']} | `{cell}` | {r['a']} | {b['NS_delta']:,} | {b['stab']} | {b['n_chi']:,} | {b['nnz']:,} | "
              f"**{'yes' if r['agreement']['identical'] else 'NO'}** | {'yes' if r.get('kernel_ok') else ('n/a' if r['a']==0 else 'NO')} | {ranks} | "
              f"{b['hwm_above_baseline_gb']:.3f} | {l['hwm_above_baseline_gb']:.3f} | {rm:.2f}× | {b['secs']['total']:.1f} | {l['secs']['total']:.1f} | {rt:.2f}× |")
    ok = [i for i in order if i in S and S[i]['status'] == 'PASS']
    print(f"\n{len(ok)} of {len([i for i in order if i in S])} cells PASS: " + ', '.join(ok))
    bad = [i for i in order if i in S and S[i]['status'] != 'PASS']
    if bad: print("NOT PASS: " + ', '.join(f"{i} ({S[i]['status']})" for i in bad))
    # the banked drops
    print("\ndrops reproduced:")
    for i in order:
        r = S.get(i)
        if not r or not r.get('rank_compare'): continue
        for name, v in r['rank_compare'].items():
            if v['banked'] != r['a']:
                print(f"  {i} {name}: banked {v['banked']} vs a = {r['a']}, here {v['here']} ({'match' if v['match'] else 'MISMATCH'})")
    print("\n### VARIANTS")
    for i in order:
        r = S.get(i)
        if not r or 'build_lean_variants' not in r: continue
        base = r['build_lean']['rec']
        print(f"  {i} baseline lean: peak {base['hwm_above_baseline_gb']:.3f} GB, {base['secs']['total']:.1f}s "
              f"(old {r['build_old']['rec']['hwm_above_baseline_gb']:.3f} GB, {r['build_old']['rec']['secs']['total']:.1f}s)")
        for v in r['build_lean_variants']:
            if not v.get('rec'): print(f"    {v['name']}: FAILED rc={v['rc']}"); continue
            rr = v['rec']
            print(f"    {str(rr['knobs']):66} peak {rr['hwm_above_baseline_gb']:.3f} GB ({rr['hwm_above_baseline_gb']/base['hwm_above_baseline_gb']:.2f}×)  "
                  f"{rr['secs']['total']:.1f}s ({rr['secs']['total']/base['secs']['total']:.2f}×)  identical={v.get('agreement_with_old')}")
    print("\n### FIT")
    rows = []
    for fn in sorted(glob.glob(os.path.join(SC, '*.json'))):
        try: r = json.load(open(fn))
        except Exception: continue
        if 'builder' not in r or 'N_S' not in r: continue
        rows.append(r)
    pj = os.path.join(ROOT, 'results', 'b13_10', 'pilot.json')
    if os.path.exists(pj):
        p = json.load(open(pj)); b = p['build']
        rows.append(dict(tag='PILOT', builder='lean', knobs=p['knobs'], NS_delta=b['N_S'] * p['delta'], nnz=b['nnz'], nrows=b['nrows'],
                         hwm_above_baseline_gb=b['hwm_above_baseline_gb'], secs=dict(total=b['secs'])))
    for bl in ('old', 'lean'):
        Sx = [r for r in rows if r['builder'] == bl and (bl == 'old' or r.get('knobs') == dict(chunk=400000, triples='store', blocks='memory'))]
        if len(Sx) < 4: continue
        A = np.array([[r['NS_delta'], r['nnz'], 1.0] for r in Sx], float)
        y = np.array([r['hwm_above_baseline_gb'] for r in Sx], float)
        c, *_ = np.linalg.lstsq(A, y, rcond=None)
        res = np.abs(A @ c - y)
        print(f"{bl}:  peak_GB = {c[0]:.3e}·(N_S·δ) + {c[1]:.3e}·nnz + {c[2]:.3f}   "
              f"(n = {len(Sx)}, max |residual| {res.max():.3f} GB, median {np.median(res):.3f} GB, largest point N_S·δ = {max(r['NS_delta'] for r in Sx):,})")
        if bl == 'lean':
            print(f"        7.0 GB is reached at N_S·δ ≈ {(7.0 - c[2]) / c[0]:.3g}" if c[0] > 0 else "")
    print("\n### PILOT")
    if os.path.exists(pj):
        p = json.load(open(pj)); b = p['build']
        print(f"build {b['secs']}s (mono {b['mono_secs']}s, orbits {b['orbit_secs']}s, rows {b['rows_secs']}s), peak {b['hwm_gb']} GB "
              f"({b['hwm_above_baseline_gb']} above baseline); N_S {b['N_S']:,} n_chi {b['n_chi']:,} rows {b['nrows']:,} nnz {b['nnz']:,} E.data {b['dtypes']['E_data']}")
        s79rows = {'E_01': (3423455, 18038214), 'E_12': (8688185, 35847528), 'E_23': (8688185, 35847528), 'E_34': (3911695, 16114190)}
        print("| block | \\|H\\| | targets | rows | nnz | s79's rows/nnz | agree | tables s | rows s | HWM GB |")
        print("|---|---|---|---|---|---|---|---|---|---|")
        for ph in b['phases']:
            if ph['op'] == 'assemble':
                print(f"| assemble | | | {ph['rows']:,} | {ph['nnz']:,} | — | — | | {ph['secs']} | {ph['hwm_gb']} |"); continue
            s = s79rows.get(ph['op'])
            ag = ('**yes**' if s == (ph['rows'], ph['nnz']) else 'NO') if s else 'not reached by s79'
            print(f"| `{ph['op']}` | {ph['H']} | {ph['targets']:,} | {ph['rows']:,} | {ph['nnz']:,} | "
                  f"{(str(s[0])+' / '+str(s[1])) if s else '— (ended here)'} | {ag} | {ph['secs_tables']} | {ph['secs_rows']} | {ph['hwm_gb']} |")
        print(f"cover: {p['cover']['size']:,}/{p['cover']['n_chi']:,} by {p['cover']['order']}, |U| = {p['cover']['nU']}, excess {p['cover']['excess']}, {p['cover']['secs']}s, HWM {p['cover']['hwm_gb']} GB")
        for pp, v in p['per_prime'].items():
            print(f"p = {pp}: nullity {v['nullity']} (= a = {p['a']}), verified on E {v['verified_on_E']}, kernel rank {v['kernel_rank']}, "
                  f"mult_det {v['mult_det']}, i_det {v['i_det']}; kernel {v['kernel_secs']}s, ev+rank {v['ev_rank_secs']}s, HWM {v['hwm_gb']} GB")
        print("status:", p['status'])


if __name__ == '__main__':
    main()
