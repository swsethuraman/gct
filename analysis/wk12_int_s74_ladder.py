#!/usr/bin/env python3
"""The whole D-ladder re-derived from session 74's delivered values.

No evaluation and no session code: the rung-d matrix is the leading a_d rows of
the delivered native matrix, scaled.  Two facts make this cheap and exact.

  * A rung-d source vector is evaluated at the same degree-4 points as
    everything else, so no new points are needed for any rung.
  * Rows of different native rung must be scaled RELATIVE to each other by
    mu^(d - rung_i) before their rank means anything.  Using the exponent
    (24 - rung_i) instead differs by the uniform column factor mu^(24-d), a
    column scaling, which changes no rank -- so ONE scaled matrix serves every
    rung.  Leaving the scaling off does not work: it mixes weights, and it is
    the trap that first gave me determinant rank 274, contradicting LMR.

It also locates where each padded kernel direction is born, by checking that the
rung-d kernel, zero-extended, lies in the rung-24 kernel.
"""
import json, os, sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
SRC = os.environ.get('S74_DIR', os.path.join(ROOT, 'results', 's74'))
P1, P2 = 2147483647, 2147483629
A = {12: 2, 13: 39, 14: 93, 15: 145, 16: 188, 17: 219, 18: 241, 19: 255,
     20: 264, 21: 269, 22: 272, 23: 273, 24: 274}


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


def main():
    src = json.load(open(f'{SRC}/source.json')); ent = src['entries']
    KEYS = [str(e['key']) for e in ent]
    lad = json.load(open(f'{SRC}/ladder_ranks.json'))
    out = {'agrees_with_s74': True, 'per_prime': {}, 'births': {}}
    for p in (P1, P2):
        cols = {}
        for fam in ('det', 'pad'):
            col = json.load(open(f'{SRC}/columns_{fam}_{p}.json'))
            mu = [v % p for v in col['u_symbol']]; K = col['K']
            POW = {k: [pow(v, k, p) for v in mu]
                   for k in set(24 - e['rung'] for e in ent)}
            NAT = [col['rows_native'][k] for k in KEYS]
            cols[fam] = [[NAT[i][j] * POW[24 - ent[i]['rung']][j] % p
                          for j in range(K)] for i in range(274)]
        theirs = {r['delta']: r for r in lad[str(p)]}
        rows = []
        kers = {}
        print(f'--- p = {p}')
        print(f'{"d":>3} {"a":>4} | {"rk_det":>6} {"i_det":>5} | {"rk_pad":>6} '
              f'{"i_pad":>5} |   D  | s74')
        for d in range(12, 25):
            n = A[d]
            rd, _ = kernel(cols['det'][:n], p)
            rp, kp = kernel(cols['pad'][:n], p)
            kers[d] = kp
            t = theirs[d]
            ok = (rd == t['rank_det'] and rp == t['rank_pad'])
            out['agrees_with_s74'] &= ok
            rows.append(dict(delta=d, a=n, rank_det=rd, i_det=n - rd,
                             rank_pad=rp, i_pad=n - rp, D=(n - rd) - (n - rp),
                             agrees=ok))
            print(f'{d:3d} {n:4d} | {rd:6d} {n-rd:5d} | {rp:6d} {n-rp:5d} | '
                  f'{(n-rd)-(n-rp):+4d} | {"agrees" if ok else "DIFFERS"}')
        out['per_prime'][str(p)] = rows
        # where the padded kernel directions are born
        K = len(cols['pad'][0])
        born = {}
        for d in (13, 14, 15, 23):
            allin = all(
                all(sum((list(v) + [0] * (274 - A[d]))[i] * cols['pad'][i][j]
                        for i in range(274)) % p == 0 for j in range(K))
                for v in kers[d])
            born[d] = dict(dim=len(kers[d]), extends_into_rung_24=allin)
            print(f'  rung {d:2d} padded kernel: dim {len(kers[d])}, '
                  f'zero-extends into the rung-24 kernel: {allin}')
        out['births'][str(p)] = born
    out['reading'] = ('every i in this table is a CEILING read off one point '
                      'family, except i_det(23) = 0, which is a nonzero '
                      '273-minor on a 273-dimensional space and therefore exact')
    json.dump(out, open(os.path.join(ROOT, 'results', 'wk12_int_s74_ladder.json'),
                        'w'), indent=1)
    print(f'\nRESULT the whole ladder agrees with s74 at both primes: '
          f'{out["agrees_with_s74"]}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
