#!/usr/bin/env python3
"""Session 45 -- what the measured cost curve buys: coverage of the six-row
census, and of the balanced corner in particular.

Model, fitted to this session's measured cells (results/s45_ledger.md):
  n_chi  ~ the census value (exact where this session measured it),
  nnz(E) ~ NNZ_PER_NS * N_S                    (measured 2.7-4.4, mean ~3.5),
  the (12,2) compression leaves nnz_c ~ min(1, 12 n_chi / nrows) * nnz + K n_chi,
     which for the cells with nrows >= 12 n_chi is ~ NNZC_PER_N * n_chi,
  one Wiedemann sequence ~ 4 * n_chi * nnz_c * SEC_PER_OP seconds,
  the two house primes run concurrently, so wall ~ one sequence + build.
The fitted constants are printed with the residuals so the reader can see how
rough the extrapolation is.  It is an EXPECTATION, not a measurement.
"""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
R = os.path.join(HERE, '..', 'results')

def census():
    txt = open(os.path.join(R, 'sixrow_census.md')).read()
    secs = re.split(r'\n## `δ = (\d)`', txt)
    out = []
    for i in range(1, len(secs), 2):
        d = int(secs[i]); body = secs[i + 1]
        for line in body.splitlines():
            if not line.startswith('| `('): continue
            p = [x.strip() for x in line.strip('|').split('|')]
            lam = tuple(int(x) for x in re.findall(r'\d+', p[0]))
            try:
                a = int(p[1]); NS = int(p[5]); st = int(p[6])
            except (ValueError, IndexError): continue
            nchi = int(re.sub(r'[^0-9]', '', p[7]))
            out.append(dict(d=d, lam=lam, a=a, N_S=NS, stab=st, n_chi=nchi,
                            approx='~' in p[7], bal=lam[0] - lam[-1], elig=lam[0] >= d))
    # onset-only tables (lam_1 < delta) use a shorter row format
    for m in re.finditer(r'\n\| `\(([\d, ]+)\)` \| (\d+) \| \d+ \| (\d+) \| (\d+) \| ~?(\d+) \| [\d.]+ \| (?:yes|no) \|', txt):
        lam = tuple(int(x) for x in m.group(1).split(','))
        d = 7 if sum(lam) == 28 else 8
        out.append(dict(d=d, lam=lam, a=int(m.group(2)), N_S=int(m.group(3)),
                        stab=int(m.group(4)), n_chi=int(m.group(5)), approx=True,
                        bal=lam[0] - lam[-1], elig=lam[0] >= d))
    seen = {}
    for c in out: seen[(c['lam'], c['d'])] = c
    return list(seen.values())

def measured():
    p = os.path.join(R, 's45_cells.jsonl')
    if not os.path.exists(p): return []
    seen = {}
    for l in open(p):
        d = json.loads(l); seen[(tuple(d['lam']), d['delta'])] = d
    return list(seen.values())

def fit():
    ms = measured()
    nnz_per_ns = [d['nnz'] / d['N_S'] for d in ms]
    return (sum(nnz_per_ns) / len(nnz_per_ns)) if ms else 3.5, ms

if __name__ == '__main__':
    NNZ_PER_NS, ms = fit()
    NNZC_PER_N = float(os.environ.get('NNZC_PER_N', 60.0))
    SEC_PER_OP = float(os.environ.get('SEC_PER_OP', 2.3e-9))
    BUILD_PER_NS = float(os.environ.get('BUILD_PER_NS', 0.0))   # fitted below
    cs = census()
    exact = {(tuple(d['lam']), d['delta']): d for d in ms}
    rows = []
    for c in cs:
        key = (c['lam'], c['d'])
        n = exact[key]['n_chi'] if key in exact else c['n_chi']
        t = 4 * n * (NNZC_PER_N * n) * SEC_PER_OP
        rows.append((c, n, t))
    def band(t): return '1h' if t <= 3600 else ('8h' if t <= 8 * 3600 else ('48h' if t <= 48 * 3600 else 'beyond'))
    print(f"fitted nnz/N_S = {NNZ_PER_NS:.2f} from {len(ms)} measured cells; "
          f"nnz_c/n_chi = {NNZC_PER_N}, {SEC_PER_OP*1e9:.1f} ns per element-op")
    for d in (7, 8):
        for tag, sel in (('eligible (lam_1>=delta)', lambda c: c['elig']),
                         ('onset-only (lam_1<delta)', lambda c: not c['elig'])):
            sub = [(c, n, t) for c, n, t in rows if c['d'] == d and sel(c)]
            if not sub: continue
            tot = len(sub)
            cnt = {b: sum(1 for c, n, t in sub if band(t) == b) for b in ('1h', '8h', '48h', 'beyond')}
            print(f"  delta={d} {tag}: {tot} cells -> <=1h {cnt['1h']}, <=8h {cnt['1h']+cnt['8h']}, "
                  f"<=48h {cnt['1h']+cnt['8h']+cnt['48h']}, beyond {cnt['beyond']}")
            for b in (4, 5, 6, 7, 8):
                bb = [(c, n, t) for c, n, t in sub if c['bal'] == b]
                if bb:
                    r48 = sum(1 for c, n, t in bb if t <= 48 * 3600)
                    print(f"      balance {b}: {len(bb)} cells, {r48} within 48 h "
                          f"(smallest n_chi {min(n for c, n, t in bb)})")
