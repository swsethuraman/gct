#!/usr/bin/env python3
"""
Session 46 -- the reach table, rebuilt on EXACT n_chi.

Session 45's reach table (analysis/wk9_s45_reach.py) read n_chi from
results/sixrow_census.md, where every large cell carries the bound N_S/|Stab|
marked `~`.  That bound is wrong in both directions at the balanced cells this
session sweeps (it is a lower bound on the orbit count, an upper bound on
nothing, and says nothing about dropped orbits): at (8,8,5,5,1,1)_7 it reads
75,474 against a true 62,613, at (8,8,6,2,2,2)_7 it reads 98,744 against a true
114,875, and at the named target (8,4,4,4,4,4)_7 it reads 83,836 against a true
92,031.  Here n_chi is exact, by the character count of wk9_s46_census (no
monomial enumerated).

The cost model, fitted to measured cells (session 45's ledger plus this
session's) and printed with its residuals:

    nnz(E)    = C_NNZ  * N_S                      (measured 2.66-4.39)
    nrows(E)  = C_ROW  * N_S
    level (12,2): ns = min(nrows, 12 n_chi + 64) rows sampled, grouped in 2s, so
    nnz_c     ~ (ns / nrows) * nnz + K * n_chi,   K = a + 8 pinned dense ev rows
    one sequence = 4 * n_chi * nnz_c element-ops at NS_PER_OP(n_chi) ns each,
    the two house primes run concurrently, so
    wall      ~ build + sequence.
    build     = mono + orbits + rows, each fitted linear in N_S (the generator
                reduction removed the |Stab| factor from `orbits`).

It is an EXPECTATION, not a measurement: it assumes the fitted constants hold at
cells nobody has built.  Cells whose exact n_chi is known from a measurement use
that value; the rest use the exact character count, which is not an
extrapolation at all -- only the *cost* columns are.

usage: python3 wk9_s46_reach.py [--delta 7] [--out results/s46_reach.md]
"""
import sys, os, json, re, math
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
R = os.path.join(HERE, '..', 'results')
from wk9_s46_census import census_cell

def partitions(nn, k, mx):
    if k == 1:
        if 1 <= nn <= mx: yield (nn,)
        return
    for a in range(min(mx, nn - (k - 1)), 0, -1):
        for rest in partitions(nn - a, k - 1, a): yield (a,) + rest

def census_a():
    """a and m_det from results/sixrow_census.md (a asserted there by two
    independent routes -- plethysm and a Kostant alternation)."""
    txt = open(os.path.join(R, 'sixrow_census.md')).read()
    secs = re.split(r'\n## `δ = (\d)`', txt)
    out = {}
    for i in range(1, len(secs), 2):
        d = int(secs[i])
        for line in secs[i + 1].splitlines():
            if not line.startswith('| `('): continue
            p = [x.strip() for x in line.strip('|').split('|')]
            lam = tuple(int(x) for x in re.findall(r'\d+', p[0]))
            try: out[(lam, d)] = (int(p[1]), int(p[2]))
            except (ValueError, IndexError): pass
    return out

def measured_cells():
    """every measured determinant-side cell available to this session, for the fit."""
    out = {}
    for fn in ('s45_cells.jsonl', 's46_cells.jsonl'):
        p = os.path.join(R, fn)
        if not os.path.exists(p): continue
        for l in open(p):
            try: d = json.loads(l)
            except Exception: continue
            if 'n_chi' not in d or 'nnz' not in d: continue
            out[(tuple(d['lam']), d['delta'])] = d
    return out

def fit(ms):
    """(C_NNZ, C_ROW, ns_per_op coefficients, build coefficients, residuals)."""
    vals = list(ms.values())
    c_nnz = sum(d['nnz'] / d['N_S'] for d in vals) / len(vals)
    c_row = sum(d['nrows'] / d['N_S'] for d in vals) / len(vals)
    # ns per element-op, from the diagnostic of the run that carried the verdict:
    # the C helper reports the sequence length and its own wall time.
    pts = []
    for d in vals:
        for sd in d.get('sides', {}).values():
            for pp in sd.get('per_prime', {}).values():
                for dg in pp.get('diag', []):
                    if dg.get('status') != 'NONSINGULAR': continue
                    m = re.search(r'SEQ n=(\d+) nrows=\d+ nnz=(\d+) k=\d+ len=\d+ secs=([\d.]+)', dg.get('note', ''))
                    if m:
                        nc = int(m.group(1)); nz = int(m.group(2)); sec = float(m.group(3))
                        pts.append((nc, sec * 1e9 / (4.0 * nc * nz), nz))
    if len(pts) >= 2:
        xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
        mx = sum(xs) / len(xs); my = sum(ys) / len(ys)
        den = sum((x - mx) ** 2 for x in xs)
        b = (sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / den) if den else 0.0
        a0 = my - b * mx
    else:
        a0, b = 2.3, 0.0
    bt = [(d['N_S'], d['build_secs']) for d in vals if 'build_secs' in d]
    c_build = (sum(t for _, t in bt) / sum(n for n, _ in bt)) if bt else 3.0e-5
    return c_nnz, c_row, (a0, b), c_build, pts

def rows_for(delta, a_tab, ms, C_NNZ, C_ROW, nsop, C_BUILD, n=4):
    out = []
    for lam in partitions(n * delta, 6, n * delta):
        key = (lam, delta)
        if key not in a_tab: continue           # a = 0 cells are not in the census
        a, m_det = a_tab[key]
        if a < 1: continue
        N_S, n_chi, stab, _a = census_cell(lam, delta)
        meas = ms.get(key)
        nnz = meas['nnz'] if meas else C_NNZ * N_S
        nrows = meas['nrows'] if meas else C_ROW * N_S
        K = a + 8
        ns = min(nrows, 12 * n_chi + 64)
        nnz_c = (ns / nrows) * nnz + K * n_chi
        ns_op = max(1.5, nsop[0] + nsop[1] * n_chi)
        seq = 4.0 * n_chi * nnz_c * ns_op * 1e-9
        build = C_BUILD * N_S
        out.append(dict(lam=lam, delta=delta, a=a, m_det=m_det, N_S=N_S, stab=stab,
                        n_chi=n_chi, bal=lam[0] - lam[-1], elig=lam[0] >= delta,
                        nnz=int(nnz), nrows=int(nrows), nnz_c=int(nnz_c),
                        secs=seq + build, build_secs=build,
                        measured=bool(meas), exact_nchi=True))
    out.sort(key=lambda r: r['secs'])
    return out

if __name__ == '__main__':
    delta = 7
    outp = None
    args = sys.argv[1:]; i = 0
    while i < len(args):
        if args[i] == '--delta': delta = int(args[i + 1]); i += 2
        elif args[i] == '--out': outp = args[i + 1]; i += 2
        else: i += 1
    a_tab = census_a(); ms = measured_cells()
    C_NNZ, C_ROW, nsop, C_BUILD, pts = fit(ms)
    rows = rows_for(delta, a_tab, ms, C_NNZ, C_ROW, nsop, C_BUILD)
    print(json.dumps(dict(delta=delta, C_NNZ=C_NNZ, C_ROW=C_ROW, ns_per_op=nsop,
                          C_BUILD=C_BUILD, npts=len(pts), nfit=len(ms), rows=rows),
                     default=str))
