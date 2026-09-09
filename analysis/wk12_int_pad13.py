#!/usr/bin/env python3
"""The padded rank at rung 13, on fresh points, with the repository's evaluator.

s74's ladder reports i_pad(13) = 3 on a 39-dimensional source: the sampled
padded rank at rung 13 is 36.  That 3 is a CEILING read off one point family,
and it is the cheapest number in the programme to move, because rung 13 needs
39 rows and no transport at all -- a rung-13 source vector is evaluated at the
same degree-4 padded points as everything else.

Two outcomes, and both matter:

  * the rank reaches 39 on some set of fresh padded points.  Then i_pad(13) = 0
    and the sampled 3 was an artefact of the point family; the whole padded
    ladder, including the 5 at rung 24, has to be redone.
  * the rank stays at 36 over an independent stream.  Then a genuine rung-13
    padded relation is likely, and because i_pad is nondecreasing along the
    ladder, ONE certified rung-13 padded ideal element gives i_pad(23) >= 1 and
    settles the LMR cell against a multiplicity obstruction.

Neither outcome is a proof on its own: a nonzero 39 x 39 minor proves
i_pad(13) = 0; a stalled rank proves nothing and only raises or lowers the
weight of evidence.
"""
import itertools, json, os, random, sys, time

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.normpath(os.path.join(HERE, '..'))
from wk8_s30_core import exps                                        # noqa: E402
import wk11_s69_circuit as C                                         # noqa: E402
from wk12_int_s74_freshpad import pad_cv, msym_u_pad                 # noqa: E402

N, R = 4, 9
P1, P2 = 2147483647, 2147483629
SRC = os.environ.get('S74_DIR', os.path.join(ROOT, 'results', 's74'))


def rank_modp(M, p):
    A = [r[:] for r in M]; nr = len(A); nc = len(A[0]) if A else 0; r = 0
    for c in range(nc):
        pr = next((i for i in range(r, nr) if A[i][c] % p), None)
        if pr is None: continue
        A[r], A[pr] = A[pr], A[r]
        inv = pow(A[r][c], -1, p); A[r] = [x * inv % p for x in A[r]]
        for i in range(nr):
            if i != r and A[i][c] % p:
                f = A[i][c]; A[i] = [(A[i][k] - f * A[r][k]) % p for k in range(nc)]
        r += 1
        if r == nr: break
    return r


def main(argv):
    rung = int(argv[argv.index('--rung') + 1]) if '--rung' in argv else 13
    seed = int(argv[argv.index('--seed') + 1]) if '--seed' in argv else 20260913
    npts = int(argv[argv.index('--points') + 1]) if '--points' in argv else 120
    bound = int(argv[argv.index('--bound') + 1]) if '--bound' in argv else 11
    fam = argv[argv.index('--family') + 1] if '--family' in argv else 'pad'
    t0 = time.time()

    src = json.load(open(f'{SRC}/source.json'))
    ent = [e for e in src['entries'] if e['rung'] <= rung]
    a = {12: 2, 13: 39, 14: 93, 15: 145, 16: 188, 17: 219, 18: 241, 19: 255,
         20: 264, 21: 269, 22: 272, 23: 273, 24: 274}[rung]
    print(f'rung {rung}: {len(ent)} source rows, banked a_{rung} = {a}, '
          f'family {fam}, {npts} fresh points, seed {seed}, bound {bound}')
    assert len(ent) == a, f'{len(ent)} rows for a_{rung} = {a}'
    fills = [C.Filling(e['native']['h'], e['native']['n'], e['native']['delta'],
                       e['native']['C1'], e['native']['C2'],
                       e['native']['two'], e['native']['one']) for e in ent]
    deg = [e['rung'] for e in ent]
    A, idx, fact, tab = C.sym_table(N, R)
    rng = random.Random(seed)
    rows = {P1: [[] for _ in range(a)], P2: [[] for _ in range(a)]}
    best = {P1: 0, P2: 0}
    hist = []
    for j in range(npts):
        tp = time.time()
        if fam == 'pad':
            lf = [[rng.randint(-bound, bound) for _ in range(R)] for _ in range(10)]
            mu = msym_u_pad(lf)
            if mu == 0:
                print(f'  point {j}: msym_u = 0, skipped'); continue
            cv = pad_cv(lf)
        elif fam == 'red':                       # l(s) . generic cubic -- the
            # reducible control.  V_pad is inside V_red, so I(red) is inside
            # I(pad) and i_red <= i_pad.  A relation that is already reducible is
            # a relation satisfied by every l . cubic, which is a far more
            # structured object than a permanent-specific one and much likelier
            # to admit an exact membership proof.
            import itertools as _it
            lf = [rng.randint(-bound, bound) for _ in range(R)]
            cub = {e: rng.randint(-bound, bound)
                   for e in _it.product(range(4), repeat=R) if sum(e) == 3}
            l = {tuple(1 if k == i else 0 for k in range(R)): c
                 for i, c in enumerate(lf) if c}
            f4 = {}
            for e1, c1 in l.items():
                for e2, c2 in cub.items():
                    e = tuple(x + y for x, y in zip(e1, e2))
                    f4[e] = f4.get(e, 0) + c1 * c2
            cv = [int(f4.get(al, 0)) for al in exps(N, R)]
            mu = 24 * lf[0] * cub.get((3,) + (0,) * (R - 1), 0)
            if mu == 0:
                print(f'  point {j}: msym_u = 0, skipped'); continue
        else:                                    # det, as a control
            cv, As = C.det_point(N, R, rng, bound=bound)
            A1 = As[0]
            mu = 24 * round(__import__('numpy').linalg.det(
                [[A1[4 * r + c] for c in range(4)] for r in range(4)]))
            if mu == 0:
                print(f'  point {j}: msym_u = 0, skipped'); continue
        for p in (P1, P2):
            msym = [(cv[k] % p) * fact[k] % p for k in range(len(A))]
            vals = [C.dp_eval_c(F, msym, p, tab) for F in fills]
            # Rows of different native rung must be scaled RELATIVE to each other
            # before their rank means anything: row i enters rung d as
            # F_{T_i} . mu^(d - rung_i).  Using the exponent (24 - rung_i)
            # instead differs by the uniform column factor mu^(24-d), which is a
            # column scaling and changes no rank -- so one convention serves every
            # rung.  Leaving the scaling off altogether does NOT: it mixes weights.
            m = mu % p
            for i in range(a):
                rows[p][i].append(vals[i] * pow(m, 24 - deg[i], p) % p)
        if True:
            for p in (P1, P2): best[p] = rank_modp(rows[p], p)
            hist.append(dict(points=j + 1, rank_P1=best[P1], rank_P2=best[P2]))
            print(f'  after {j+1:4d} points: rank {best[P1]}/{a} at P1, '
                  f'{best[P2]}/{a} at P2   [{time.time()-t0:.0f}s total, '
                  f'{time.time()-tp:.1f}s this point]', flush=True)
            if best[P1] == a and best[P2] == a:
                print('  FULL RANK reached; stopping.')
                break
    for p in (P1, P2): best[p] = rank_modp(rows[p], p)
    res = dict(rung=rung, family=fam, a=a, seed=seed, bound=bound,
               points_used=len(rows[P1][0]),
               rank={str(P1): best[P1], str(P2): best[P2]},
               i_ceiling={str(P1): a - best[P1], str(P2): a - best[P2]},
               history=hist, secs=round(time.time() - t0, 1),
               reading=('a nonzero a x a minor proves i = 0; a stalled rank is '
                        'evidence and not a proof'))
    out = os.path.join(ROOT, 'results',
                       f'wk12_int_{fam}{rung}_seed{seed}_b{bound}.json')
    json.dump(res, open(out, 'w'), indent=1)
    print('RESULT ' + json.dumps({k: v for k, v in res.items() if k != 'history'}))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
