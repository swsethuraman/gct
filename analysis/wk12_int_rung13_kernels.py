#!/usr/bin/env python3
"""Are the three rung-13 padded relations reducible relations?

At rung 13 the source is 39-dimensional and s74's padded rank is 36, so
i_pad(13) <= 3.  V_pad = {l . per_3(B)} sits inside V_red = {l . C, C any
cubic}, so I(red) is inside I(pad) and i_red <= i_pad.  If the three relations
are already REDUCIBLE -- if they vanish on every l . cubic and not only on
l . per_3 -- then settling them is a question about the classical variety of
reducible quartics, with no permanent in it, and a single proved one gives
i_pad(13) >= 1, hence i_pad(23) >= 1 by monotonicity, hence D <= 0.

This script takes s74's rung-13 padded kernel from the delivered data and
evaluates it at reducible points generated here, and separately computes the
reducible kernel from scratch and compares the two spaces.  A generic control
comes last: a nonzero polynomial cannot vanish on all quartics, so the rung-13
generic rank must be 39, and if it is not the reading is an evaluator fault and
not a relation.
"""
import itertools, json, os, random, sys, time

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.normpath(os.path.join(HERE, '..'))
from wk8_s30_core import exps                                        # noqa: E402
import wk11_s69_circuit as C                                         # noqa: E402

N, R = 4, 9
P1, P2 = 2147483647, 2147483629
SRC = os.environ.get('S74_DIR', os.path.join(ROOT, 'results', 's74'))


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


def rank_of(M, p):
    return kernel(M, p)[0]


def red_point(rng, bound):
    lf = [rng.randint(-bound, bound) for _ in range(R)]
    cub = {e: rng.randint(-bound, bound)
           for e in itertools.product(range(4), repeat=R) if sum(e) == 3}
    f4 = {}
    for i, c1 in enumerate(lf):
        if not c1: continue
        e1 = tuple(1 if k == i else 0 for k in range(R))
        for e2, c2 in cub.items():
            e = tuple(x + y for x, y in zip(e1, e2))
            f4[e] = f4.get(e, 0) + c1 * c2
    mu = 24 * lf[0] * cub.get((3,) + (0,) * (R - 1), 0)
    return [int(f4.get(al, 0)) for al in exps(N, R)], mu


def gen_point(rng, p):
    return [rng.randrange(p) for _ in exps(N, R)]


def main(argv):
    npts = int(argv[argv.index('--points') + 1]) if '--points' in argv else 45
    bound = int(argv[argv.index('--bound') + 1]) if '--bound' in argv else 11
    seed = int(argv[argv.index('--seed') + 1]) if '--seed' in argv else 20260915
    t0 = time.time()
    src = json.load(open(f'{SRC}/source.json'))
    ent = [e for e in src['entries'] if e['rung'] <= 13]
    assert len(ent) == 39
    KEYS = [str(e['key']) for e in ent]
    deg = [e['rung'] for e in ent]
    fills = [C.Filling(e['native']['h'], e['native']['n'], e['native']['delta'],
                       e['native']['C1'], e['native']['C2'],
                       e['native']['two'], e['native']['one']) for e in ent]
    A, idx, fact, tab = C.sym_table(N, R)

    # s74's rung-13 padded kernel, from the delivered data
    padker = {}
    for p in (P1, P2):
        col = json.load(open(f'{SRC}/columns_pad_{p}.json'))
        mu = [v % p for v in col['u_symbol']]; K = col['K']
        M = [[col['rows_native'][KEYS[i]][j] * pow(mu[j], 24 - deg[i], p) % p
              for j in range(K)] for i in range(39)]
        r, ker = kernel(M, p)
        padker[p] = ker
        print(f'p={p}: s74 padded rung-13 rank {r}/39, kernel dim {len(ker)}')

    rng = random.Random(seed)
    rows = {p: [[] for _ in range(39)] for p in (P1, P2)}
    grows = {p: [[] for _ in range(39)] for p in (P1, P2)}
    escaped = {p: [False] * len(padker[p]) for p in (P1, P2)}
    for j in range(npts):
        cv, mu = red_point(rng, bound)
        if mu == 0:
            print(f'  reducible point {j}: msym_u = 0, skipped'); continue
        for p in (P1, P2):
            msym = [(cv[k] % p) * fact[k] % p for k in range(len(A))]
            vals = [C.dp_eval_c(F, msym, p, tab) for F in fills]
            m = mu % p
            row = [vals[i] * pow(m, 24 - deg[i], p) % p for i in range(39)]
            for i in range(39): rows[p][i].append(row[i])
            for t, v in enumerate(padker[p]):
                if sum(v[i] * row[i] for i in range(39)) % p: escaped[p][t] = True
            gcv = gen_point(rng, p)
            gmsym = [gcv[k] * fact[k] % p for k in range(len(A))]
            gvals = [C.dp_eval_c(F, gmsym, p, tab) for F in fills]
            gm = gcv[[tuple(al) for al in A].index(tuple([N] + [0] * (R - 1)))] * 24 % p
            for i in range(39):
                grows[p][i].append(gvals[i] * pow(gm, 24 - deg[i], p) % p)
        if (j + 1) % 5 == 0 or j < 2:
            rr = {p: rank_of(rows[p], p) for p in (P1, P2)}
            gg = {p: rank_of(grows[p], p) for p in (P1, P2)}
            print(f'  after {j+1:3d} reducible points: rank {rr[P1]}/39 (P1), '
                  f'{rr[P2]}/39 (P2);  generic control {gg[P1]}/39, {gg[P2]}/39;  '
                  f'padded relations still vanishing: '
                  f'{len(padker[P1])-sum(escaped[P1])}/{len(padker[P1])}   '
                  f'[{time.time()-t0:.0f}s]', flush=True)

    out = {'seed': seed, 'bound': bound, 'points': npts, 'per_prime': {}}
    for p in (P1, P2):
        rr, rker = kernel(rows[p], p)
        gg = rank_of(grows[p], p)
        # do the two 3-spaces coincide?
        same = None
        if rker and padker[p]:
            base = [list(v) for v in rker]
            joint = rank_of(base + [list(v) for v in padker[p]], p)
            same = (joint == len(rker) == len(padker[p]))
        out['per_prime'][str(p)] = dict(
            reducible_rank=rr, reducible_kernel_dim=len(rker),
            generic_rank=gg, padded_kernel_dim=len(padker[p]),
            padded_relations_escaping_on_reducible=sum(escaped[p]),
            kernels_coincide=same)
        print(f'\np={p}: reducible rank {rr}/39 (i_red(13) <= {39-rr}), '
              f'generic control {gg}/39')
        print(f'   the {len(padker[p])} padded relations vanish at every reducible '
              f'point: {sum(escaped[p]) == 0}')
        print(f'   the reducible kernel and the padded kernel are the same space: '
              f'{same}')
    out['reading'] = ('i_red <= i_pad because V_pad is inside V_red. If the two '
                      'rung-13 kernels coincide, the relations are reducible and '
                      'settling them is a question about reducible quartics with '
                      'no permanent in it. None of this is a proof: a stalled '
                      'sampled rank is a ceiling.')
    json.dump(out, open(os.path.join(ROOT, 'results',
                                     f'wk12_int_rung13_kernels_seed{seed}.json'),
                        'w'), indent=1)
    print('\nRESULT ' + json.dumps(out['per_prime']))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
