#!/usr/bin/env python3
"""
B13-05 -- collect every banked verdict, re-run the closure to a fixed point with the new blocks,
and emit the final residual set with a fitted cost model.

usage: python3 analysis/wk13_b13_05_collect.py
board_numbering: batch13
"""
import sys, os, json, glob, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)


def is_partition(v):
    return all(v[i] >= v[i + 1] for i in range(len(v) - 1)) and (len(v) == 0 or v[-1] >= 0)


def trim(v):
    v = list(v)
    while v and v[-1] == 0: v.pop()
    return tuple(v)


def main():
    cen = json.load(open('results/b13_05_census.json'))
    A, bydeg, REC = {}, {}, {}
    for r in cen['rows']:
        mu = tuple(r['mu']); d = r['delta']
        A[(d, mu)] = r['a']; REC[(d, mu)] = r
        bydeg.setdefault(d, []).append(mu)

    # ---- banked verdicts from this session's own instrument
    measured = {}
    for fn in ['results/b13_05_validate.json'] + sorted(glob.glob('results/b13_05_deg8_w*.json')):
        if not os.path.exists(fn): continue
        for c in json.load(open(fn))['cells']:
            if c.get('status', '').startswith('CERTIFIED'):
                measured[(c['delta'], tuple(c['mu']))] = dict(source=os.path.basename(fn), secs=c.get('secs'),
                                                              n_chi=c.get('n_chi'), N_S=c.get('N_S'),
                                                              route=c.get('route', 'dense'), nnz=c.get('nnz'),
                                                              build_secs=c.get('build_secs'))
            elif 'CANDIDATE' in c.get('status', ''):
                measured[(c['delta'], tuple(c['mu']))] = dict(candidate=True, source=os.path.basename(fn))
    cands = {k: v for k, v in measured.items() if v.get('candidate')}
    print(f'banked CERTIFIED verdicts on this session\'s instrument: {len([k for k,v in measured.items() if not v.get("candidate")])}'
          f'   CANDIDATE drops: {len(cands)}')
    if cands:
        print('  *** CANDIDATES (not promoted, verification protocol):', list(cands))

    # ---- seeds
    known = {}
    for (d, mu), a in A.items():
        if len(mu) <= 5: known[(d, mu)] = 'inherited ell<=5 (Thm 2 + restriction lemma)'
        elif len(mu) == 6 and d <= 9: known[(d, mu)] = 'inherited ell=6 (certified length-6 record)'
        elif len(mu) == d: known[(d, mu)] = 'top cell (catalecticant minor, CERTIFIED here)'
    for k, v in measured.items():
        if not v.get('candidate'): known[k] = 'measured here on the s45 build (CERTIFIED)'

    # ---- Theorems F and D to a fixed point
    it = 0
    while True:
        it += 1; new = 0
        for d in range(2, 10):
            for mu in bydeg.get(d, []):
                if (d, mu) in known or A[(d, mu)] != 1: continue
                found = None
                for p in range(1, d):
                    q = d - p
                    for kap in bydeg.get(p, []):
                        if (p, kap) not in known or len(kap) > len(mu): continue
                        nu = trim(tuple(mu[i] - (kap[i] if i < len(kap) else 0) for i in range(len(mu))))
                        if any(x < 0 for x in nu) or not is_partition(nu): continue
                        if (q, nu) in known: found = (p, kap, q, nu); break
                    if found: break
                if found:
                    known[(d, mu)] = f'Theorem F: ({found[0]},{list(found[1])}) x ({found[2]},{list(found[3])})'; new += 1
        for d in range(1, 9):
            for mu in bydeg.get(d, []):
                if (d, mu) in known: continue
                found = None
                for q in range(1, 10 - d):
                    for nu in bydeg.get(q, []):
                        L = max(len(mu), len(nu))
                        M = trim(tuple((mu[i] if i < len(mu) else 0) + (nu[i] if i < len(nu) else 0) for i in range(L)))
                        if is_partition(M) and (d + q, M) in known: found = (d + q, M); break
                    if found: break
                if found:
                    known[(d, mu)] = f'Theorem D (ladder) from ({found[0]},{list(found[1])})'; new += 1
        print(f'  closure iteration {it}: +{new}')
        if new == 0: break

    # ---- the picture
    print()
    tot_open = []
    for d in range(7, 10):
        for ell in (7, 8, 9):
            cells = [mu for mu in bydeg.get(d, []) if len(mu) == ell]
            if not cells: continue
            op = [mu for mu in cells if (d, mu) not in known]
            print(f'delta={d} ell={ell}: {len(cells):4d} cells   closed {len(cells)-len(op):4d}   OPEN {len(op):4d}')
            tot_open += [(d, mu) for mu in op]
    allopen = [(d, mu) for d in range(1, 10) for mu in bydeg.get(d, []) if (d, mu) not in known]
    print(f'\nTOTAL OPEN over the whole census (delta <= 9, ell <= 9): {len(allopen)}')
    for d in range(1, 10):
        n = sum(1 for (dd, _) in allopen if dd == d)
        if n: print(f'   delta={d}: {n}')

    # ---- cost model from the measured builds
    pts = [(v['N_S'], v['build_secs']) for v in measured.values() if v.get('N_S') and v.get('build_secs') is not None]
    rate = sum(s for _, s in pts) / max(1, sum(n for n, _ in pts))
    print(f'\ncost model: {len(pts)} measured builds, N_S from {min(n for n,_ in pts)} to {max(n for n,_ in pts)}; '
          f'build ~ {rate*1e6:.1f} s per 10^6 monomials')
    dec = [(d, mu) for (d, mu) in allopen if d == 9]
    sN = sum(REC[(d, mu)]['N_S'] for d, mu in dec)
    print(f'residual (delta = 9): {len(dec)} cells, sum N_S = {sN:.3e}, fitted build cost = {sN*rate/3600:.1f} CPU-hours')
    wied = [(v['n_chi'], v['secs']) for v in measured.values() if v.get('route', '').startswith('inject') and v.get('n_chi')]
    if wied:
        wrate = sum(s for _, s in wied) / sum(n for n, _ in wied)
        print(f'inject/Wiedemann: {len(wied)} cells, n_chi {min(n for n,_ in wied)}..{max(n for n,_ in wied)}; '
              f'~{wrate*1000:.1f} s per 10^3 of n_chi (both primes)')
        est = sum(REC[(d, mu)]['n_chi_lb'] for d, mu in dec) * wrate / 3600
        print(f'   fitted decision cost over the residual (using n_chi lower bounds): {est:.1f} CPU-hours -- a LOWER bound, '
              f'and Wiedemann is superlinear in n_chi, so treat it as such')

    out = dict(board_numbering='batch13', session='B13-05',
               certified_here=[dict(delta=d, mu=list(mu), **{k: v for k, v in val.items() if k != 'candidate'})
                               for (d, mu), val in sorted(measured.items()) if not val.get('candidate')],
               candidates=[dict(delta=d, mu=list(mu)) for (d, mu) in sorted(cands)],
               closed_total=len(known), census_cells=len(A),
               open=[dict(delta=d, mu=list(mu), ell=len(mu), a=A[(d, mu)], N_S=REC[(d, mu)]['N_S'],
                          stab=REC[(d, mu)]['stab'], n_chi_lb=REC[(d, mu)]['n_chi_lb']) for (d, mu) in allopen],
               cost_model=dict(build_secs_per_monomial=rate, measured_builds=len(pts)))
    json.dump(out, open('results/b13_05_final.json', 'w'), indent=0)
    print('\nwrote results/b13_05_final.json')


if __name__ == '__main__':
    main()
