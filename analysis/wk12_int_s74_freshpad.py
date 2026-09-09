#!/usr/bin/env python3
"""Fresh padded points against session 74's five padded kernel vectors.

s74's padded column has rank 269 on 282 points of one family, so its kernel is
five-dimensional there.  A nonzero minor makes 269 a FLOOR; the five kernel
vectors are a CEILING read off one finite sample, and a ceiling read off a
sample is not a theorem.  The cheapest way to move it is more padded points from
a different stream: any point at which one of the five is nonzero raises the
floor, and 274 independent padded points would settle D = +1 outright.

Everything here is the repository's own instrument (the s69 circuit evaluator
and exponent ordering), not s74's compact DP.  The padded points are generated
by this script, from its own seed, at a different coefficient bound.
"""
import itertools, json, os, random, sys, time

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.normpath(os.path.join(HERE, '..'))
from wk8_s30_core import exps                                        # noqa: E402
import wk11_s69_circuit as C                                         # noqa: E402

N, R, DELTA = 4, 9, 24
P1, P2 = 2147483647, 2147483629
SRC = os.environ.get('S74_DIR', os.path.join(ROOT, 'results', 's74'))


def _mul(a, b):
    o = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            e = tuple(x + y for x, y in zip(e1, e2)); o[e] = o.get(e, 0) + c1 * c2
    return {e: c for e, c in o.items() if c}


def _form(coeffs):
    return {tuple(1 if k == i else 0 for k in range(R)): c
            for i, c in enumerate(coeffs) if c}


def pad_cv(linear_forms):
    """coefficient vector over exps(4,9) of l(s) . per_3(B(s)) from ten linear
    forms: the first is l, the next nine are B row by row."""
    l = _form(linear_forms[0])
    B = [[_form(linear_forms[1 + 3 * i + j]) for j in range(3)] for i in range(3)]
    per = {}
    for s in itertools.permutations(range(3)):
        t = _mul(_mul(B[0][s[0]], B[1][s[1]]), B[2][s[2]])
        for e, c in t.items(): per[e] = per.get(e, 0) + c
    f = _mul(l, {e: c for e, c in per.items() if c})
    return [int(f.get(al, 0)) for al in exps(N, R)]


def msym_u_pad(linear_forms):
    lf = linear_forms
    B1 = [[lf[1 + 3 * i + j][0] for j in range(3)] for i in range(3)]
    per = sum(B1[0][s[0]] * B1[1][s[1]] * B1[2][s[2]]
              for s in itertools.permutations(range(3)))
    return 24 * lf[0][0] * per


def main(argv):
    seed = int(argv[argv.index('--seed') + 1]) if '--seed' in argv else 20260909
    npts = int(argv[argv.index('--points') + 1]) if '--points' in argv else 40
    bound = int(argv[argv.index('--bound') + 1]) if '--bound' in argv else 17
    t0 = time.time()

    src = json.load(open(f'{SRC}/source.json'))
    ent = src['entries']
    fills = [C.Filling(e['native']['h'], e['native']['n'], e['native']['delta'],
                       e['native']['C1'], e['native']['C2'],
                       e['native']['two'], e['native']['one']) for e in ent]
    rung = [e['rung'] for e in ent]
    A, idx, fact, tab = C.sym_table(N, R)

    # ---- coordinate compatibility: my expansion must reproduce s74's own point
    col0 = json.load(open(f'{SRC}/columns_pad_{P1}.json'))
    mine = pad_cv(col0['points'][0]['linear_forms'])
    same = mine == list(col0['points_cv'][0])
    print(f'coordinate check: my expansion of s74 padded point 0 equals its '
          f'points_cv -- {"PASS" if same else "FAIL"}')
    if not same:
        for k in range(len(mine)):
            if mine[k] != col0['points_cv'][0][k]:
                print(f'  first mismatch at exponent {A[k]}: mine {mine[k]} '
                      f'theirs {col0["points_cv"][0][k]}')
                break
        return 1

    ker = {p: json.load(open(f'{SRC}/decision_{p}.json'))['columns']['pad']
           ['kernel_vectors_modp'] for p in (P1, P2)}
    print(f'five padded kernel vectors at each prime; {npts} fresh padded points, '
          f'seed {seed}, bound {bound}')

    rng = random.Random(seed)
    res = {'seed': seed, 'points': npts, 'bound': bound, 'per_prime': {}}
    escaped = {p: [False] * 5 for p in (P1, P2)}
    rows_new = {p: [] for p in (P1, P2)}
    for j in range(npts):
        lf = [[rng.randint(-bound, bound) for _ in range(R)] for _ in range(10)]
        mu = msym_u_pad(lf)
        if mu == 0:
            print(f'  point {j}: msym_u = 0, skipped'); continue
        cv = pad_cv(lf)
        for p in (P1, P2):
            msym = [(cv[a] % p) * fact[a] % p for a in range(len(A))]
            vals = [C.dp_eval_c(F, msym, p, tab) for F in fills]
            m = mu % p
            row = [vals[i] * pow(m, DELTA - rung[i], p) % p for i in range(274)]
            rows_new[p].append(row)
            for t, v in enumerate(ker[p]):
                s = sum(v[i] * row[i] for i in range(274)) % p
                if s: escaped[p][t] = True
        print(f'  point {j:3d}: done  [{time.time()-t0:.0f}s]  '
              f'escaped so far P1 {sum(escaped[P1])}/5  P2 {sum(escaped[P2])}/5', flush=True)

    for p in (P1, P2):
        E = sum(escaped[p])
        newrank = 269 + E
        res['per_prime'][str(p)] = dict(escaped=escaped[p], escaped_count=E,
                                        floor_before=269, floor_after=newrank)
        print(f'p={p}: {E} of the five kernel directions are nonzero at a fresh '
              f'point -> rank T_pad >= {newrank}')
    res['secs'] = round(time.time() - t0, 1)
    res['reading'] = ('Any escape raises the certified floor on rank T_pad and lowers '
                      'the ceiling on i_pad by the same amount; zero escapes over a '
                      'fresh independent stream is evidence for i_pad = 5 and is not '
                      'a proof of it.')
    out = os.path.join(ROOT, 'results',
                       f'wk12_int_s74_freshpad_seed{seed}_b{bound}.json')
    json.dump(res, open(out, 'w'), indent=1)
    print('RESULT ' + json.dumps({k: v for k, v in res.items() if k != 'per_prime'}))
    print(json.dumps(res['per_prime'], indent=1))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
