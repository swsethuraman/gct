#!/usr/bin/env python3
"""Session 79's Part 2, re-derived where it is a theorem.

The load-bearing claim is I(D_6^{per_3})_9 = 0 -- because Prop. 8(1) of
docs/transfer_lemma.md turns it into mult_pad = mult_red at EVERY six-row weight
of degree 9, with no points in it.  A scan proves that only if the scan is
COMPLETE: one missing weight with a >= 1 and the theorem does not follow.  So the
first and most important check here is the census, recomputed by my own Weyl
alternation, independently of s79's queue.

Also checked: every delivered record actually says what the report says (mult = a
at both primes on the cubic side; i_det = 0, mult_pad = mult_red, i_per4 = 0 at
every quartic cell), the a-values, and the counts.
"""
import json, os, sys, time
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.normpath(os.path.join(HERE, '..'))
SRC = os.environ.get('S79_DIR', os.path.join(ROOT, 'results'))
from wk9_s42_census import a_weyl                                    # noqa: E402
P1, P2 = 2147483647, 2147483629
out = {'checks': []}


def rec(name, ok, **kw):
    out['checks'].append(dict(name=name, ok=bool(ok), **kw))
    print(f'[{"PASS" if ok else "FAIL"}] {name}' + (f'  {kw}' if kw else ''), flush=True)
    return ok


def parts(n, maxlen, maxpart=None):
    """partitions of n into at most maxlen parts."""
    if maxpart is None: maxpart = n
    if n == 0: return [()]
    if maxlen == 0: return []
    o = []
    for k in range(min(n, maxpart), 0, -1):
        for rest in parts(n - k, maxlen - 1, k):
            o.append((k,) + rest)
    return o


def main(argv):
    # ---------------------------------------------------------------- cubic side
    per6 = [json.loads(l) for l in open(f'{SRC}/s79_per6.jsonl')]
    d9 = [r for r in per6 if r['delta'] == 9]
    d10 = [r for r in per6 if r['delta'] == 10]
    seen9 = {tuple(r['mu']): r for r in d9}
    rec(f'the degree-9 cubic scan has {len(seen9)} distinct weights',
        len(seen9) == 210, count=len(seen9))
    badm = [tuple(r['mu']) for r in d9
            if not (r['mult'] == r['a'] and r.get('primes_agree')
                    and all(v['mult'] == r['a'] for v in r['per_prime'].values()))]
    rec('every degree-9 cubic record reports mult = a at BOTH primes',
        not badm, offenders=badm[:4])
    badm10 = [tuple(r['mu']) for r in d10
              if not (r['mult'] == r['a'] and r.get('primes_agree'))]
    rec('every degree-10 cubic record reports mult = a at both primes',
        not badm10, offenders=badm10[:4])
    # the a-values, recomputed
    t0 = time.time(); cache = {}
    bad_a = []
    for mu, r in seen9.items():
        av = a_weyl(mu + (0,) * (6 - len(mu)), 9, 3, cache)
        if av != r['a']: bad_a.append((mu, av, r['a']))
    rec(f'my Weyl alternation reproduces a(mu,9) at all {len(seen9)} scanned '
        f'weights [{time.time()-t0:.0f}s]', not bad_a, offenders=bad_a[:4])
    rec(f'sum of a over the degree-9 scan is 592',
        sum(r['a'] for r in d9) == 592, total=sum(r['a'] for r in d9))
    rec('max a on the degree-9 scan is 9',
        max(r['a'] for r in d9) == 9, mx=max(r['a'] for r in d9))

    # THE COMPLETENESS CHECK.  I(D_6^{per_3})_9 = 0 is a statement about EVERY
    # weight of the degree-9 part, and Prop. 8(2) pairs a six-row lambda with a
    # mu such that lambda/mu is a horizontal 9-strip -- mu interlaces lambda, so
    # mu_6 may be 0 and mu of length 5 pairs with lambda of length 6.  Weights
    # shorter than 6 therefore matter, and a weight of length k < 6 sees only
    # Sym^3 C^k, so its multiplicity is the length-k one.
    t0 = time.time()
    allp = list(parts(27, 6))
    long6 = [p for p in allp if len(p) == 6]
    short = [p for p in allp if len(p) < 6]
    miss6 = [(p, a_weyl(p, 9, 3, cache)) for p in long6
             if p not in seen9 and a_weyl(p, 9, 3, cache) >= 1]
    rec(f'the scan covers EVERY length-exactly-6 partition of 27 with a >= 1 '
        f'({len(long6)} candidates) [{time.time()-t0:.0f}s]',
        not miss6, missing=miss6[:6])
    shortpos = [(p, a_weyl(p + (0,) * (6 - len(p)), 9, 3, cache)) for p in short]
    shortpos = [(p, a) for p, a in shortpos if a >= 1]
    rec(f'GAP: {len(shortpos)} partitions of 27 of length <= 5 have a >= 1 '
        f'(sum a = {sum(a for _, a in shortpos)}) and NONE is in the scan, so '
        f'I(D_6^per3)_9 = 0 is established only on the length-exactly-6 part',
        False, count=len(shortpos), sum_a=sum(a for _, a in shortpos),
        by_length={L: sum(1 for p, _ in shortpos if len(p) == L) for L in range(1, 6)},
        largest=sorted(shortpos, key=lambda t: -t[1])[:4])
    out['degree9'] = dict(scanned=len(seen9), sum_a_scanned=sum(r['a'] for r in d9),
                          length6_candidates=len(long6), length6_missing=len(miss6),
                          shorter_with_a_positive=len(shortpos),
                          shorter_sum_a=sum(a for _, a in shortpos))
    rec(f'the degree-10 scan covers {len(d10)} weights (296 reported)',
        len(d10) == 296, count=len(d10))

    # ---------------------------------------------------------------- quartic side
    cells = [json.loads(l) for l in open(f'{SRC}/s79_cells.jsonl')]
    rec(f'{len(cells)} six-row cells delivered (682 reported)', len(cells) == 682,
        count=len(cells))
    keys = set()
    bad = {'det': [], 'padred': [], 'per4': [], 'primes': []}
    for r in cells:
        lam, dl, a = tuple(r['lam']), r['delta'], r['a']
        keys.add((lam, dl))
        s = r['sides']
        if s['det']['mult'] != a: bad['det'].append((lam, dl))
        if s['pad']['mult'] != s['red_star']['mult']: bad['padred'].append((lam, dl))
        if s['per4']['mult'] != a: bad['per4'].append((lam, dl))
    rec('i_det = 0 at every delivered six-row cell', not bad['det'],
        offenders=bad['det'][:4])
    rec('mult_pad = mult_red at every delivered six-row cell', not bad['padred'],
        offenders=bad['padred'][:4])
    rec('i_per4 = 0 at every delivered six-row cell', not bad['per4'],
        offenders=bad['per4'][:4])
    rec('the 682 cells are distinct', len(keys) == len(cells), distinct=len(keys))
    drops = [r for r in cells if r['sides']['red_star']['mult'] < r['a']]
    rec(f'{len(drops)} reducible drops (59 reported)', len(drops) == 59,
        count=len(drops))
    trailing = Counter(sum(1 for x in r['lam'] if x == 1) for r in drops)
    rec('58 of the 59 drops have at least two trailing 1s',
        sum(v for k, v in trailing.items() if k >= 2) == 58,
        histogram=dict(sorted(trailing.items())))
    worst = min(drops, key=lambda r: r['sides']['red_star']['mult'] - r['a'])
    rec('the largest reducible bite is -25 at (13,9,9,3,1,1)_9',
        worst['sides']['red_star']['mult'] - worst['a'] == -25
        and tuple(worst['lam']) == (13, 9, 9, 3, 1, 1),
        cell=(worst['lam'], worst['delta']),
        bite=worst['sides']['red_star']['mult'] - worst['a'])
    # a-values on a stratified sample of the quartic cells
    t0 = time.time(); samp = cells[::40]; bada = []
    for r in samp:
        av = a_weyl(tuple(r['lam']), r['delta'], 4, cache)
        if av != r['a']: bada.append((r['lam'], r['delta'], av, r['a']))
    rec(f'my Weyl alternation reproduces a at {len(samp)} sampled quartic cells '
        f'[{time.time()-t0:.0f}s]', not bada, offenders=bada[:4])
    out['quartic'] = dict(cells=len(cells), drops=len(drops))

    ok = all(c['ok'] for c in out['checks'])
    out['status'] = 'OK' if ok else 'FAILURES'
    json.dump(out, open(os.path.join(ROOT, 'results',
                                     'wk12_int_s79_part2_verify.json'), 'w'), indent=1)
    print(f'\nRESULT {out["status"]} '
          f'({sum(c["ok"] for c in out["checks"])}/{len(out["checks"])})')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
