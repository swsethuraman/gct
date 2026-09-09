#!/usr/bin/env python3
"""Session 74's final delivery: all five columns, re-derived here.

Extends analysis/wk12_int_s74_verify.py to the reducible, per_4 and generic
columns of the completed bundle, and tests the two claims the final report adds
that the checkpoint did not have:

  * U_R = U_P at the goal cell -- the padded kernel and the reducible kernel are
    the SAME five-dimensional space, so mult_pad = mult_red and the padded
    permanent inherits no equation in this weight beyond those of the reducible
    locus.  (I found the same coincidence independently at rung 13,
    docs/rung13_reducible.md; this is the rung-24 statement.)
  * i_per4 = 0 and generic nullity 0 -- the unpadded per_4 pencils have no
    equation in this weight, and the 274 transported births are a basis of M_24.

Every rank is computed here, from the delivered native values, with the
transport applied by this script and msym_u recomputed over Z from each point's
own integer data: 4!.det(A_1) for a determinant pencil, 4!.per(A_1) for a per_4
pencil, 4!.l_1.per(B_1) for a padded point, 4!.l_1.c_{s_1^3} for a reducible
point, 4!.c_{(4,0,...,0)} for a generic one.
"""
import gzip, itertools, json, os, sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
SRC = os.environ.get('S74_DIR', os.path.join(ROOT, 'results', 's74'))
P1, P2 = 2147483647, 2147483629
N, R, DELTA = 4, 9, 24
A_LAD = {12: 2, 13: 39, 14: 93, 15: 145, 16: 188, 17: 219, 18: 241, 19: 255,
         20: 264, 21: 269, 22: 272, 23: 273, 24: 274}
out = {'checks': []}


def rec(name, ok, **kw):
    out['checks'].append(dict(name=name, ok=bool(ok), **kw))
    print(f'[{"PASS" if ok else "FAIL"}] {name}' + (f'  {kw}' if kw else ''), flush=True)
    return ok


def det_int(M):
    from fractions import Fraction
    n = len(M); B = [[Fraction(x) for x in r] for r in M]; sg = 1
    d = Fraction(1)
    for c in range(n):
        pr = next((i for i in range(c, n) if B[i][c] != 0), None)
        if pr is None: return 0
        if pr != c: B[c], B[pr] = B[pr], B[c]; sg = -sg
        d *= B[c][c]
        for i in range(c + 1, n):
            f = B[i][c] / B[c][c]
            for k in range(c, n): B[i][k] -= f * B[c][k]
    v = sg * d; assert v.denominator == 1
    return int(v)


def perm_int(M):
    n = len(M)
    return sum(__import__('math').prod(M[i][s[i]] for i in range(n))
               for s in itertools.permutations(range(n)))


def kernel(M, p):
    nr = len(M); nc = len(M[0]); B = [r[:] for r in M]
    T = [[1 if i == j else 0 for j in range(nr)] for i in range(nr)]; r = 0
    for c in range(nc):
        pr = next((i for i in range(r, nr) if B[i][c] % p), None)
        if pr is None: continue
        B[r], B[pr] = B[pr], B[r]; T[r], T[pr] = T[pr], T[r]
        inv = pow(B[r][c], -1, p)
        B[r] = [x * inv % p for x in B[r]]; T[r] = [x * inv % p for x in T[r]]
        for i in range(nr):
            if i != r and B[i][c] % p:
                f = B[i][c]
                B[i] = [(B[i][k] - f * B[r][k]) % p for k in range(nc)]
                T[i] = [(T[i][k] - f * T[r][k]) % p for k in range(nr)]
        r += 1
        if r == nr: break
    return r, [T[i] for i in range(r, nr)]


def span_rank(vecs, p):
    return kernel([list(v) for v in vecs], p)[0] if vecs else 0


def load(fam, p):
    base = f'{SRC}/columns_{fam}_{p}.json'
    if os.path.exists(base):
        return json.load(open(base))
    return json.load(gzip.open(base + '.gz', 'rt'))


def msym_u(fam, q, exps_u_index=None):
    if fam == 'det':
        return 24 * det_int(q['pencil'][0])
    if fam == 'per4':
        return 24 * perm_int(q['pencil'][0])
    if fam == 'pad':
        lf = q['linear_forms']
        B1 = [[lf[1 + 3 * i + j][0] for j in range(3)] for i in range(3)]
        return 24 * lf[0][0] * perm_int(B1)
    if fam == 'red':
        c3 = dict((tuple(e), c) for e, c in q['cubic'])
        return 24 * q['l'][0] * c3.get((3,) + (0,) * (R - 1), 0)
    if fam == 'gen':
        # stored as [exponent, value] pairs; look the letter up by its exponent,
        # never by a positional literal
        for e, c in q['coefficients']:
            if tuple(e) == (N,) + (0,) * (R - 1): return 24 * c
        return 0
    raise ValueError(fam)


def main():
    sys.path.insert(0, os.path.join(ROOT, 'analysis'))
    from wk8_s30_core import exps
    iu = exps(N, R).index(tuple([N] + [0] * (R - 1)))
    rec('u is the last exponent index in the wk8_s30_core ordering, resolved not '
        'assumed', iu == 494, index=iu)

    src = json.load(open(f'{SRC}/source.json')); ent = src['entries']
    KEYS = [str(e['key']) for e in ent]
    kers = {}
    for p in (P1, P2):
        M = {}
        for fam in ('gen', 'det', 'pad', 'red', 'per4'):
            col = load(fam, p)
            mu = [msym_u(fam, q, iu) % p for q in col['points']]
            rec(f'{fam} p={p}: my msym_u agrees with the stored u_symbol at all '
                f'{len(mu)} points', mu == [v % p for v in col['u_symbol']],
                first_mismatch=next((j for j in range(len(mu))
                                     if mu[j] != col['u_symbol'][j] % p), None))
            rec(f'{fam} p={p}: no delivered point is a u-zero',
                all(v % p for v in mu),
                zeros=[j for j, v in enumerate(mu) if v % p == 0])
            NAT = [col['rows_native'][k] for k in KEYS]
            K = col['K']
            POW = {k: [pow(v, k, p) for v in mu]
                   for k in set(DELTA - e['rung'] for e in ent)}
            M[fam] = [[NAT[i][j] * POW[DELTA - ent[i]['rung']][j] % p
                       for j in range(K)] for i in range(274)]
        dec = json.load(open(f'{SRC}/decision_{p}.json'))
        ker = {}
        for fam in ('gen', 'det', 'pad', 'red', 'per4'):
            r, k = kernel(M[fam], p)
            ker[fam] = k
            claimed = dec['columns'].get(fam, {}).get('rank_24')
            rec(f'{fam} p={p}: rank {r}, nullity {274-r}'
                + ('' if claimed is None else f' (s74 says {claimed})'),
                claimed is None or r == claimed, rank=r, nullity=274 - r)
        kers[p] = ker
        rec(f'p={p}: the 274 transported births are a basis of M_24 '
            f'(generic nullity 0)', len(ker['gen']) == 0)
        rec(f'p={p}: i_per4 = 0 -- no equation of the unpadded per_4 pencils in '
            f'this weight', len(ker['per4']) == 0)
        # U_R = U_P ?
        rp, rr = ker['pad'], ker['red']
        same = (len(rp) == len(rr) == span_rank(rp + rr, p) == span_rank(rp, p))
        rec(f'p={p}: U_R = U_P -- the padded and reducible kernels are the same '
            f'{len(rp)}-space, so mult_pad = mult_red', same,
            dim_pad=len(rp), dim_red=len(rr), dim_join=span_rank(rp + rr, p))
        # U_D cap U_P = 0 and neither contains the other
        d_in_p = span_rank(rp + ker['det'], p) == span_rank(rp, p)
        inter = len(rp) + len(ker['det']) - span_rank(rp + ker['det'], p)
        rec(f'p={p}: dim(U_D cap U_P) = 0 and U_D is not inside U_P',
            inter == 0 and not d_in_p, intersection=inter)
        # where the padded kernel lives
        i24 = [i for i, e in enumerate(ent) if e['rung'] == 24][0]
        supp = [max(ent[i]['rung'] for i in range(274) if v[i] % p) for v in rp]
        rec(f'p={p}: every padded kernel vector is supported on rungs <= 14, so '
            f'the candidates are transported from the 39- and 93-dimensional '
            f'cells', all(s <= 14 for s in supp), top_rungs=sorted(supp))
        rec(f'p={p}: no padded kernel vector touches the delta=24 birth row, so '
            f'eps_pad = 0 and i_pad(24) = i_pad(23)',
            all(v[i24] % p == 0 for v in rp))
        # the LMR line's residues
        y = ker['det'][0]
        for fam in ('pad', 'red', 'per4', 'gen'):
            nz = sum(1 for j in range(len(M[fam][0]))
                     if sum(y[i] * M[fam][i][j] for i in range(274)) % p)
            rec(f'p={p}: the LMR line y is nonzero at {nz}/{len(M[fam][0])} '
                f'{fam} points', nz == len(M[fam][0]), nonzero=nz)
        # the ladder, all five columns
        lad = {r_['delta']: r_ for r_ in json.load(
            open(f'{SRC}/ladder_ranks.json'))[str(p)]}
        rows = []
        allok = True
        for d in range(12, 25):
            n = A_LAD[d]; idx = [i for i, e in enumerate(ent) if e['rung'] <= d]
            row = {'delta': d, 'a': n}
            for fam in ('det', 'pad', 'red', 'per4'):
                rr_, _ = kernel([M[fam][i] for i in idx], p)
                row[f'i_{fam}'] = n - rr_
                key = {'det': 'i_det', 'pad': 'i_pad', 'red': 'i_red',
                       'per4': 'i_per4'}[fam]
                if key in lad[d]: allok &= (lad[d][key] == n - rr_)
            row['D'] = row['i_det'] - row['i_pad']
            rows.append(row)
        out.setdefault('ladder', {})[str(p)] = rows
        rec(f'p={p}: the whole five-column ladder agrees with s74', allok)
        print('    delta  ' + ' '.join(f'{r_["delta"]:4d}' for r_ in rows))
        for key in ('i_det', 'i_pad', 'i_red', 'i_per4', 'D'):
            print(f'    {key:6s} ' + ' '.join(f'{r_[key]:4d}' for r_ in rows))

    # the two primes must agree on the kernels' dimensions
    rec('both primes give the same nullities on every column',
        all(len(kers[P1][f]) == len(kers[P2][f])
            for f in ('gen', 'det', 'pad', 'red', 'per4')))
    ok = all(c['ok'] for c in out['checks'])
    out['status'] = 'OK' if ok else 'FAILURES'
    json.dump(out, open(os.path.join(ROOT, 'results', 'wk12_int_s74_final.json'),
                        'w'), indent=1)
    print(f'\nRESULT {out["status"]} '
          f'({sum(c["ok"] for c in out["checks"])}/{len(out["checks"])})')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
