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
    """Fitted constants, with the residuals the caller prints.

    The useful ratio is nnz/nrows, not nnz/N_S: across every measured cell it
    sits in 2.9-4.6 (mean ~3.8) while nnz/N_S ranges 2.1-4.4 and nrows/N_S
    0.62-1.20.  And nnz/nrows is exactly the quantity the compression needs,
    because at level (s, 2) the sampled stack has

        nnz_c = min(nnz, s * n_chi * (nnz/nrows)) + K * n_chi,   K = a + 8,

    the second term being the K pinned dense evaluation rows.  Checked against
    the four measured cells that sample (predicted 4.598 M / 5.587 M / 6.483 M /
    5.275 M against measured 4.596 M / 5.592 M / 6.477 M / 5.269 M) and against
    the cells that do not (1.432 M against 1.432 M at (8,8,5,5,1,1)_7).
    """
    vals = list(ms.values())
    rho = sum(d['nnz'] / d['nrows'] for d in vals) / len(vals)
    c_row = sum(d['nrows'] / d['N_S'] for d in vals) / len(vals)
    c_nnz = sum(d['nnz'] / d['N_S'] for d in vals) / len(vals)
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
        xs = [q[0] for q in pts]; ys = [q[1] for q in pts]
        mx = sum(xs) / len(xs); my = sum(ys) / len(ys)
        den = sum((x - mx) ** 2 for x in xs)
        b = (sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / den) if den else 0.0
        a0 = my - b * mx
    else:
        a0, b = 2.3, 0.0
    bt = [(d['N_S'], d['build_secs']) for d in vals if 'build_secs' in d]
    c_build = (sum(t for _, t in bt) / sum(n for n, _ in bt)) if bt else 3.0e-5
    return dict(rho=rho, c_row=c_row, c_nnz=c_nnz, nsop=(a0, b), c_build=c_build,
                pts=pts, n=len(vals))

def rows_for(delta, a_tab, ms, F, hpad=None, n=4):
    rho = F['rho']; c_row = F['c_row']; nsop = F['nsop']; c_build = F['c_build']
    out = []
    for lam in partitions(n * delta, 6, n * delta):
        key = (lam, delta)
        if key not in a_tab: continue
        a, m_det = a_tab[key]
        if a < 1: continue
        N_S, n_chi, stab, _a = census_cell(lam, delta)
        meas = ms.get(key)
        nrows = meas['nrows'] if meas else c_row * N_S
        nnz = meas['nnz'] if meas else rho * nrows
        K = a + 8
        # level policy: (12,2) when nrows/n_chi > 10, else (3,2)
        s = 12 if nrows / n_chi > 10 else 3
        nnz_c = min(nnz, s * n_chi * (nnz / nrows)) + K * n_chi
        ns_op = max(1.5, nsop[0] + nsop[1] * n_chi)
        seq = 4.0 * n_chi * nnz_c * ns_op * 1e-9
        build = c_build * N_S
        out.append(dict(lam=lam, delta=delta, a=a, m_det=m_det, N_S=N_S, stab=stab,
                        n_chi=n_chi, bal=lam[0] - lam[-1], elig=lam[0] >= delta,
                        h_pad=(hpad or {}).get(key), nnz=int(nnz), nrows=int(nrows),
                        nnz_c=int(nnz_c), level='(12,2)' if s == 12 else '(3,2)',
                        rows_over_nchi=round(nrows / n_chi, 1),
                        secs=seq + build, seq_secs=seq, build_secs=build,
                        measured=bool(meas)))
    out.sort(key=lambda r: (r['secs'], r['bal']))
    return out

def hpad_table():
    out = {}
    for fn in ('s46_census7_hpad.json', 's46_census8_hpad.json'):
        p = os.path.join(R, fn)
        if not os.path.exists(p): continue
        for r in json.load(open(p)):
            out[(tuple(r['lam']), r['delta'])] = r['h_pad']
    return out

if __name__ == '__main__':
    delta = 7
    outp = None
    args = sys.argv[1:]; i = 0
    while i < len(args):
        if args[i] == '--delta': delta = int(args[i + 1]); i += 2
        elif args[i] == '--out': outp = args[i + 1]; i += 2
        else: i += 1
    a_tab = census_a(); ms = measured_cells(); F = fit(ms)
    rows = rows_for(delta, a_tab, ms, F, hpad_table())
    res = dict(delta=delta, fit={k: v for k, v in F.items() if k != 'pts'},
               residuals=F['pts'], rows=rows)
    if outp:
        json.dump(res, open(outp, 'w'), default=str)
    print(json.dumps(res, default=str))
