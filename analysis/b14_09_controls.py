#!/usr/bin/env python3
"""
B14-09 controls C1-C4 for the `n_chi` character-sum instrument, and the two
deliberately wrong inputs that must make it fail.

`PROVED.md: check_must_be_able_to_fail` -- and the seventh instance of it, which
is the integrator's own batch-14 reachability script reporting both controls
PASS on an EMPTY census because `all()` and `not any()` over nothing are true.
So every control here reports the size of the input it ran on, and a control
that ran on nothing is a FAIL, not a PASS.

  C1  the g = 1 term of the character sum reproduces every banked N_S
  C2  the character sum reproduces every banked MEASURED n_chi
  C3a NEGATIVE: chi dropped (plain orbit count) must DISAGREE with the bank
  C3b NEGATIVE: group widened to the full S_r must DISAGREE with the bank
  C3c NEGATIVE: a weight perturbed off n*delta must be refused, not answered
  C4  the character sum agrees with the repository's own independent
      enumerate-and-canonicalise implementations, wk9_s45_build.orbit_setup_arr
      and wk9_s36_stabred.orbit_setup, on cells small enough to run them

usage: python3 analysis/b14_09_controls.py [--out results/b14_09/controls.json]
"""
import sys, os, json, time, itertools
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
import b14_09_sizing as S


def _fail_if_empty(n, what):
    if n == 0:
        raise AssertionError(f"CONTROL RAN ON NOTHING: {what} -- a check that cannot fail is not a check")


def c1_c2(H):
    _fail_if_empty(len(H), "banked n_chi corpus")
    t0 = time.time()
    bad_ns, bad_nc, bad_st = [], [], []
    for k, v in sorted(H.items()):
        n, r, mu, de = k
        res = S.n_chi_exact(mu, de, n=n)
        if res['N_S'] != v['N_S']:
            bad_ns.append([list(k[2]), k[3], res['N_S'], v['N_S'], v['src']])
        if res['n_chi'] != v['n_chi']:
            bad_nc.append([list(k[2]), k[3], res['n_chi'], v['n_chi'], v['src']])
        if v['stab'] is not None and res['stab'] != v['stab']:
            bad_st.append([list(k[2]), k[3], res['stab'], v['stab'], v['src']])
    return dict(records=len(H), secs=round(time.time() - t0, 1),
                sources=sorted({v['src'] for v in H.values()}),
                by_nr={f"n={k[0]},r={k[1]}": sum(1 for q in H if q[0] == k[0] and q[1] == k[1])
                       for k in {(q[0], q[1]) for q in H}},
                C1_N_S_mismatches=bad_ns, C2_n_chi_mismatches=bad_nc,
                stab_mismatches=bad_st,
                C1=("PASS" if not bad_ns else "FAIL"),
                C2=("PASS" if not bad_nc else "FAIL"))


def c3a(H):
    """chi dropped: n_chi becomes the plain orbit count.  It must DISAGREE."""
    tested = agree = 0; examples = []
    for k, v in sorted(H.items()):
        n, r, mu, de = k
        if len(set(mu)) == len(mu):          # |Stab| = 1: chi cannot matter, skip
            continue
        tested += 1
        wrong = S.n_chi_exact(mu, de, n=n, chi_on=False)['n_chi']
        if wrong == v['n_chi']:
            agree += 1
        elif len(examples) < 5:
            examples.append([list(mu), de, dict(wrong=wrong, banked=v['n_chi'])])
    _fail_if_empty(tested, "cells with |Stab| > 1")
    return dict(tested=tested, still_agreeing=agree, disagreeing=tested - agree,
                examples=examples,
                note="the sign twist is what chi is; dropping it must change the answer",
                C3a=("PASS" if tested - agree > 0 else "FAIL: insensitive to chi, so C2 has no teeth"))


def c3b(H):
    """the group widened to the full S_r.  It must DISAGREE."""
    tested = agree = 0; examples = []
    for k, v in sorted(H.items()):
        n, r, mu, de = k
        if len(set(mu)) == 1 or r != 6:      # Stab already S_r, or r! too large to widen to
            continue
        tested += 1
        # the full S_r with the same chi rule applied to the whole of it
        full = []
        for p in itertools.permutations(range(r)):
            rel = list(p)
            full.append((tuple(p), S.perm_sign(rel) if mu[0] % 2 else 1))
        try:
            wrong = S.n_chi_exact(mu, de, n=n, group=full)['n_chi']
        except AssertionError:
            wrong = None                     # character sum not divisible: also a disagreement
        if wrong == v['n_chi']:
            agree += 1
        elif len(examples) < 5:
            examples.append([list(mu), de, dict(wrong=wrong, banked=v['n_chi'])])
        if tested >= 24:                     # r! DPs per cell; 24 cells is plenty
            break
    _fail_if_empty(tested, "cells whose stabiliser is not already S_r")
    return dict(tested=tested, still_agreeing=agree, disagreeing=tested - agree,
                examples=examples,
                C3b=("PASS" if tested - agree > 0 else "FAIL: insensitive to the group"))


def c3c():
    """a weight off n*delta must be refused, not answered."""
    cases, refused = [], 0
    for mu, de, n in [((9, 9, 4, 3, 3, 2), 10, 3), ((10, 6, 5, 4, 3, 2), 10, 3),
                      ((5, 5, 5, 5, 5, 5), 10, 3)]:
        pert = list(mu); pert[0] += 1
        try:
            got = S.n_chi_exact(tuple(pert), de, n=n)['n_chi']
            cases.append([pert, de, dict(answered=got)])
        except ValueError as e:
            refused += 1
            cases.append([pert, de, dict(refused=str(e))])
    _fail_if_empty(len(cases), "perturbed weights")
    return dict(tested=len(cases), refused=refused, cases=cases,
                C3c=("PASS" if refused == len(cases) else "FAIL: a wrong weight got a number"))


def c4(cells):
    """the repository's own enumerate-and-canonicalise routes, which share no
    code with the character sum: wk9_s45_build.orbit_setup_arr (arrays) and
    wk9_s36_stabred.orbit_setup (dicts of multisets)."""
    from wk9_s45_build import orbit_setup_arr
    from wk9_s36_stabred import orbit_setup
    rows = []
    for mu, de, n, r in cells:
        t = time.time()
        arr = orbit_setup_arr(n, r, de, mu, verbose=False)
        t45 = time.time() - t
        mine = S.n_chi_exact(mu, de, n=n)
        row = dict(mu=list(mu), delta=de, n=n, r=r,
                   s45=dict(N_S=int(arr['N_S']), stab=int(arr['stab']), n_chi=int(arr['n_chi']), secs=round(t45, 2)),
                   char_sum=dict(N_S=mine['N_S'], stab=mine['stab'], n_chi=mine['n_chi']))
        if arr['N_S'] <= 60000:
            t = time.time()
            basis, vecs, group = orbit_setup(n, r, de, mu, verbose=False)
            row['s36'] = dict(N_S=len(basis), stab=len(group), n_chi=len(vecs), secs=round(time.time() - t, 2))
        row['agree'] = all(row['char_sum'][f] == row[k][f]
                           for k in ('s45', 's36') if k in row
                           for f in ('N_S', 'stab', 'n_chi'))
        rows.append(row)
    _fail_if_empty(len(rows), "independent-implementation cells")
    return dict(tested=len(rows), rows=rows,
                C4=("PASS" if all(r['agree'] for r in rows) else "FAIL"))


CELLS_C4 = [                      # small enough that BOTH enumerating routes run
    ((4, 3, 3, 2), 4, 3, 4),
    ((5, 4, 3, 3, 3), 6, 3, 5),
    ((6, 4, 4, 2, 2), 6, 3, 5),
    ((4, 4, 4, 4, 2, 0), 6, 3, 6),
    ((5, 5, 4, 2, 2, 0), 6, 3, 6),
    ((6, 5, 3, 3, 2, 2), 7, 3, 6),
    ((5, 5, 5, 3, 3, 3), 8, 3, 6),
    ((7, 4, 4, 4, 3, 2), 8, 3, 6),
    ((6, 6, 4, 4, 4, 3), 9, 3, 6),
    ((4, 4, 4, 4, 4, 4), 8, 3, 6),           # |Stab| = 720, the largest in the batch, at a size both routes can run
]


def main():
    out = {}
    out['instrument'] = 'analysis/b14_09_sizing.py  n_chi = (1/|G|) sum_g chi(g) |Fix_X(g)|'
    out['group_and_character_check'] = []
    for mu, de, n, r in CELLS_C4:
        out['group_and_character_check'].append([list(mu), S._check_group(mu)])
    S._check_perm_tables(3, 6, (9, 9, 4, 3, 3, 2))
    S._check_perm_tables(3, 6, (5, 5, 5, 5, 5, 5))
    out['perm_action_matches_engine'] = True
    H = S.harvest(verbose=True)
    out['c1_c2'] = c1_c2(H)
    out['c3a_chi_dropped'] = c3a(H)
    out['c3b_group_widened'] = c3b(H)
    out['c3c_weight_perturbed'] = c3c()
    out['c4_independent_implementations'] = c4(CELLS_C4)
    out['verdict'] = {k: out[s][k] for s, k in
                      [('c1_c2', 'C1'), ('c1_c2', 'C2'), ('c3a_chi_dropped', 'C3a'),
                       ('c3b_group_widened', 'C3b'), ('c3c_weight_perturbed', 'C3c'),
                       ('c4_independent_implementations', 'C4')]}
    dest = sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv else 'results/b14_09/controls.json'
    dest = os.path.join(ROOT, dest)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    json.dump(out, open(dest, 'w'), indent=1)
    print(json.dumps(out['verdict'], indent=1))
    print(f"written {os.path.relpath(dest, ROOT)}")
    return 0 if all(v.startswith('PASS') for v in out['verdict'].values()) else 1


if __name__ == '__main__':
    sys.exit(main())
