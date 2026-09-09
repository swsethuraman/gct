#!/usr/bin/env python3
"""Session 74's checkpoint, re-derived here.

Nothing is taken from s74's decision files except as the thing being tested.
The delivered raw material is the row-by-point value matrices in
results/s74/columns_{det,pad,gen}_<p>.json and the integer points that produced
them.  This script:

  1. rebuilds each matrix from rows_native, in a row order fixed by the source
     file, and computes its rank and nullity by its own Gaussian elimination
     over F_p;
  2. recomputes the transport multiplier msym_u = 4! [s_1^4] f at every point
     from the point's own integer pencil / linear forms, and checks it is
     nonzero -- the transport is column scaling by msym_u^(24-d), so a u-zero
     point silently voids a transported row;
  3. checks the delta = 23 sub-block (the 273 rows of native degree <= 23,
     which are the transported ones) separately, since it is what fixes
     i_det(23) and hence i_det(24) through the birth-quotient proposition;
  4. re-derives an explicit nonzero minor of the claimed size on each side,
     by choosing pivots itself;
  5. checks the claimed kernel vectors really are in the kernel, and reads the
     logical status of every number: a nonzero minor is a rank FLOOR, and a
     nullity read off a finite point sample is a CEILING on the rank and hence
     a FLOOR on nothing at all.
"""
import json, os, sys, itertools, time

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
SRC = os.environ.get('S74_DIR', os.path.join(ROOT, 'results', 's74'))
P1, P2 = 2147483647, 2147483629
out = {'checks': [], 'source': SRC}

def rec(name, ok, **kw):
    out['checks'].append(dict(name=name, ok=bool(ok), **kw))
    print(f'[{"PASS" if ok else "FAIL"}] {name}' + (f'  {kw}' if kw else ''), flush=True)
    return ok

# ---------------------------------------------------------------- rank over F_p
def rank_and_kernel(M, p, want_pivots=False):
    """rank, a basis of the right kernel of M^T ... i.e. of the ROW space's
    annihilator: we treat rows as vectors and eliminate on rows."""
    A = [row[:] for row in M]
    nr, nc = len(A), len(A[0])
    # track the row combination that produced each eliminated row
    T = [[1 if i == j else 0 for j in range(nr)] for i in range(nr)]
    piv_r, piv_c, r = [], [], 0
    for c in range(nc):
        pr = next((i for i in range(r, nr) if A[i][c] % p), None)
        if pr is None: continue
        A[r], A[pr] = A[pr], A[r]; T[r], T[pr] = T[pr], T[r]
        inv = pow(A[r][c], -1, p)
        A[r] = [x * inv % p for x in A[r]]; T[r] = [x * inv % p for x in T[r]]
        for i in range(nr):
            if i != r and A[i][c] % p:
                f = A[i][c]
                A[i] = [(A[i][k] - f * A[r][k]) % p for k in range(nc)]
                T[i] = [(T[i][k] - f * T[r][k]) % p for k in range(nr)]
        piv_r.append(r); piv_c.append(c); r += 1
        if r == nr: break
    ker = [T[i] for i in range(r, nr)]
    return (r, ker, piv_c) if want_pivots else (r, ker)

def det_modp(M, p):
    n = len(M); A = [row[:] for row in M]; d = 1
    for c in range(n):
        pr = next((i for i in range(c, n) if A[i][c] % p), None)
        if pr is None: return 0
        if pr != c: A[c], A[pr] = A[pr], A[c]; d = -d
        d = d * A[c][c] % p
        inv = pow(A[c][c], -1, p)
        for i in range(c + 1, n):
            f = A[i][c] * inv % p
            if f: A[i] = [(A[i][k] - f * A[c][k]) % p for k in range(n)]
    return d % p

def det_int(M):
    from fractions import Fraction
    n = len(M); A = [[Fraction(x) for x in r] for r in M]; sg = 1; d = Fraction(1)
    for c in range(n):
        pr = next((i for i in range(c, n) if A[i][c] != 0), None)
        if pr is None: return 0
        if pr != c: A[c], A[pr] = A[pr], A[c]; sg = -sg
        d *= A[c][c]
        for i in range(c + 1, n):
            f = A[i][c] / A[c][c]
            for k in range(c, n): A[i][k] -= f * A[c][k]
    v = sg * d; assert v.denominator == 1
    return int(v)

# ---------------------------------------------------------------- the source
src = json.load(open(f'{SRC}/source.json'))
ent = src['entries']
LAM24 = tuple(src['cell']['lam']); N, R, DELTA = 4, 9, 24
rec('the source has 274 entries and says it is complete',
    len(ent) == 274 and src['size'] == 274 and src['complete'])
prof = {int(k): v for k, v in src['birth_profile'].items()}
pres = {int(k): v for k, v in src['present'].items()}
rec('the delivered rung histogram is the banked birth profile',
    pres == prof and sum(prof.values()) == 274, profile=[prof[d] for d in sorted(prof)])
from collections import Counter
have = Counter(e['rung'] for e in ent)
rec('the entries themselves realise that histogram',
    all(have[d] == prof[d] for d in prof), counted=dict(sorted(have.items())))

# every literal filling must be a filling of shape lambda_24: n copies of each of
# 24 letters, and its recorded native rung must match its native filling's delta.
def letters(fil):
    c = Counter()
    for x in fil['C1'] + fil['C2'] + fil['one']: c[x] += 1
    for a, b in fil['two']: c[a] += 1; c[b] += 1
    return c
bad_shape, bad_rung, bad_transport = [], [], []
for i, e in enumerate(ent):
    lit, nat = e['literal'], e['native']
    L = letters(lit)
    if tuple(lit['lam']) != LAM24 or len(L) != DELTA or set(L.values()) != {N}:
        bad_shape.append(i)
    if nat['delta'] != e['rung'] or len(letters(nat)) != e['rung']:
        bad_rung.append(i)
    # the literal filling must be the native one with (24 - d) whole u-columns
    # appended: same C1, C2 and pairs, and exactly 4*(24-d) extra singletons.
    if (lit['C1'] != nat['C1'] or lit['C2'] != nat['C2'] or lit['two'] != nat['two']
            or len(lit['one']) - len(nat['one']) != N * (DELTA - e['rung'])):
        bad_transport.append(i)
rec('every literal row is a filling of lambda_24 with n copies of 24 letters',
    not bad_shape, offenders=bad_shape[:5])
rec('every native filling has the rung it is filed under', not bad_rung, offenders=bad_rung[:5])
rec('every literal row is its native filling times u^(24-d), structurally',
    not bad_transport, offenders=bad_transport[:5])
KEYS = [str(e['key']) for e in ent]
rec('the 274 row keys are distinct', len(set(KEYS)) == 274)

# ------------------------------------------------- the transport multiplier
def msym_u_det(pt):
    """4! [s_1^4] det(sum s_i A_i) = 4! det(A_1)."""
    return 24 * det_int(pt['pencil'][0])

def msym_u_pad(pt):
    """4! [s_1^4] ( l(s) . per_3(B(s)) ) = 4! . l_1 . per(B_1)."""
    lf = pt['linear_forms']
    l1 = lf[0][0]
    B1 = [[lf[1 + 3 * i + j][0] for j in range(3)] for i in range(3)]
    per = sum(B1[0][s[0]] * B1[1][s[1]] * B1[2][s[2]]
              for s in itertools.permutations(range(3)))
    return 24 * l1 * per

# ------------------------------------------------------------------ per family
res = {}
for fam, p in [('det', P1), ('det', P2), ('pad', P1), ('pad', P2)]:
    col = json.load(open(f'{SRC}/columns_{fam}_{p}.json'))
    assert col['prime'] == p and col['family'] == fam
    RN = col['rows_native']
    missing = [k for k in KEYS if k not in RN]
    rec(f'{fam} p={p}: every one of the 274 source rows has a value vector',
        not missing, missing=len(missing))
    NAT = [RN[k] for k in KEYS]              # values of the NATIVE fillings
    K = len(NAT[0])
    rec(f'{fam} p={p}: the stored native matrix is 274 x {K}',
        len(NAT) == 274 and all(len(r) == K for r in NAT))

    # the transport multiplier at every delivered point, recomputed here from the
    # point's own integer data, and compared to the value s74 stored.
    pts = col['points']
    mu = [(msym_u_det(q) if fam == 'det' else msym_u_pad(q)) % p for q in pts]
    rec(f'{fam} p={p}: my msym_u = 4! [s_1^4] f agrees with s74\'s u_symbol at all '
        f'{len(pts)} points', mu == [v % p for v in col['u_symbol']],
        first_mismatch=next((j for j in range(len(mu)) if mu[j] != col['u_symbol'][j] % p), None))
    zeros = [j for j, v in enumerate(mu) if v % p == 0]
    rec(f'{fam} p={p}: msym_u is nonzero at all {len(pts)} delivered points '
        f'(a u-zero would void every transported row there)', not zeros, u_zero_columns=zeros)
    out.setdefault('msym_u_zero', {})[f'{fam}_{p}'] = zeros

    # THE TRANSPORT.  row_i(f) = F_{T_i}(f) . msym_u(f)^(24 - d_i): column j of
    # row i is the stored native value scaled by mu_j^(24 - rung_i).  Everything
    # below is computed from this matrix, which this script builds itself.
    pw = {}
    for e in ent: pw.setdefault(DELTA - e['rung'], None)
    POW = {k: [pow(v, k, p) for v in mu] for k in pw}
    M = [[NAT[i][j] * POW[DELTA - ent[i]['rung']][j] % p for j in range(K)]
         for i in range(274)]

    r24, ker24, piv = rank_and_kernel(M, p, want_pivots=True)
    rec(f'{fam} p={p}: rank over the full 274 rows is {r24}', True, rank=r24, nullity=274 - r24)
    res[(fam, p)] = dict(rank=r24, nullity=274 - r24, kernel=ker24, pivots=piv)

    # an explicit nonzero minor of size r24, with rows and columns chosen here.
    # One elimination pass over the pivot columns, tracking which original row
    # supplies each pivot; that set of rows and piv columns is a nonsingular
    # submatrix, and its determinant is recomputed from the untouched matrix.
    Msub = [[M[i][c] for c in piv] for i in range(274)]
    A = [row[:] for row in Msub]; who = list(range(274)); sel = []; rr = 0
    for c in range(len(piv)):
        pr = next((i for i in range(rr, 274) if A[i][c] % p), None)
        if pr is None: continue
        A[rr], A[pr] = A[pr], A[rr]; who[rr], who[pr] = who[pr], who[rr]
        sel.append(who[rr])
        inv = pow(A[rr][c], -1, p)
        A[rr] = [x * inv % p for x in A[rr]]
        for i in range(rr + 1, 274):
            if A[i][c] % p:
                fq = A[i][c]
                A[i] = [(A[i][k] - fq * A[rr][k]) % p for k in range(len(piv))]
        rr += 1
    minor = det_modp([[M[i][c] for c in piv] for i in sel], p)
    rec(f'{fam} p={p}: an independently chosen {r24} x {r24} minor is nonzero',
        minor != 0 and len(sel) == r24, minor=minor, size=len(sel),
        first_row=sel[0], last_row=sel[-1], first_col=piv[0], last_col=piv[-1])
    res[(fam, p)]['minor'] = minor
    res[(fam, p)]['minor_rows'] = sel
    res[(fam, p)]['minor_cols'] = piv

    # the transported sub-block: the rows of native degree <= 23
    idx23 = [i for i, e in enumerate(ent) if e['rung'] <= 23]
    rec(f'{fam} p={p}: exactly 273 rows are transported (native rung <= 23)',
        len(idx23) == 273, count=len(idx23))
    r23, _ = rank_and_kernel([M[i] for i in idx23], p)
    rec(f'{fam} p={p}: rank on the transported delta=23 rows is {r23}', True,
        rank_23=r23, i_at_23=273 - r23)
    res[(fam, p)]['rank_23'] = r23

    # s74's own claimed kernel vectors really annihilate the matrix
    dec = json.load(open(f'{SRC}/decision_{p}.json'))
    kv = dec['columns'][fam].get('kernel_vectors_modp', [])
    badk = []
    for v in kv:
        for c in range(K):
            if sum(v[i] * M[i][c] for i in range(274)) % p:
                badk.append(c); break
    rec(f'{fam} p={p}: s74\'s {len(kv)} claimed kernel vectors annihilate every column',
        not badk, failures=len(badk))
    rec(f'{fam} p={p}: my rank agrees with s74\'s decision file',
        r24 == dec['columns'][fam]['rank_24'] and r23 == dec['columns'][fam]['rank_23'],
        mine=(r24, r23),
        theirs=(dec['columns'][fam]['rank_24'], dec['columns'][fam]['rank_23']))

out['ranks'] = {f'{f}_{p}': {k: v for k, v in d.items() if k not in ('kernel', 'pivots',
                                                                    'minor_rows', 'minor_cols')}
                for (f, p), d in res.items()}
ok = all(c['ok'] for c in out['checks'])
out['status'] = 'OK' if ok else 'FAILURES'
json.dump(out, open(os.path.join(ROOT, 'results', 'wk12_int_s74_verify.json'), 'w'), indent=1)
print('\nRESULT', out['status'], f"({sum(c['ok'] for c in out['checks'])}/{len(out['checks'])})")
