#!/usr/bin/env python3
"""
B13-08 -- the independent re-check of the session's own records.

  1. a(mu, 10) for every queued weight recomputed by tools/verify/pleth.py
     (the verifier's Weyl-alternation knapsack, which imports nothing from
     analysis/) and compared with the queue's plethysm value.
  2. every merged record (results/b13_08/per6_d10.jsonl) audited: delta, n, r,
     the pre-registered seeds and bound, both house primes present, the
     hybrid's attempt verified with projected nullity = rank = a at each prime,
     cover excess >= 0, mult == a at both primes iff status says proved,
     units = a - mult, primes_agree consistent, N_S and n_chi consistent with
     |Stab| (n_chi <= N_S), and no weight outside the frozen queue.
  3. tools/verify/verify.py on every gct-cert/1 full_rank certificate the sweep
     wrote (results/certs/b13_08_per6/*.json.gz): the verifier's own kernel
     and evaluation, independent of analysis/.

usage: python3 analysis/wk13_b08_verify.py [--skip-certs]
writes results/b13_08/verify.json and prints a summary; exit 0 iff everything checked passes.
"""
import os, sys, json, glob, subprocess, time, collections, math

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..'))
RES = os.path.join(ROOT, 'results', 'b13_08'); CERTS = os.path.join(ROOT, 'results', 'certs', 'b13_08_per6')
sys.path.insert(0, os.path.join(ROOT, 'tools', 'verify'))
from pleth import ambient_multiplicity                                   # noqa: E402

P1, P2 = 2147483647, 2147483629
SEEDS = dict(per3=41, recheck=907); BOUND = 40


def stab_order(mu):
    s = 1
    for v in collections.Counter(mu).values(): s *= math.factorial(v)
    return s


def main(argv):
    Q = json.load(open(os.path.join(RES, 'queue.json')))
    queue = {tuple(w['mu']): w for w in Q['queue']}
    out = dict(board_numbering='batch13', session='B13-08')
    # 1. a by the verifier's independent plethysm
    t = time.time(); mism = []
    for mu, w in queue.items():
        a_ind = ambient_multiplicity(mu, 10, n=3)
        if a_ind != w['a']: mism.append(dict(mu=list(mu), queue_a=w['a'], independent_a=a_ind))
    out['a_independent'] = dict(checked=len(queue), mismatches=mism, secs=round(time.time() - t, 1))
    print(f"1. a(mu,10) by tools/verify/pleth.py on {len(queue)} weights: {len(mism)} mismatches ({out['a_independent']['secs']}s)")
    # 2. the records
    recs = [json.loads(l) for l in open(os.path.join(RES, 'per6_d10.jsonl')) if l.strip()] if os.path.exists(os.path.join(RES, 'per6_d10.jsonl')) else []
    problems = []; seen = collections.Counter()
    for r in recs:
        mu = tuple(r['mu']); seen[mu] += 1
        def bad(msg): problems.append(dict(mu=list(mu), problem=msg))
        if mu not in queue: bad('not in the frozen queue'); continue
        w = queue[mu]
        if r.get('delta') != 10 or r.get('n') != 3 or r.get('r') != 6: bad('delta/n/r')
        if r.get('a') != w['a']: bad(f"a {r.get('a')} != queue {w['a']}")
        if r.get('seeds') != SEEDS or r.get('bound') != BOUND: bad(f"seeds/bound {r.get('seeds')} {r.get('bound')}")
        if sorted(r.get('primes', [])) != sorted([P1, P2]): bad('primes')
        if r.get('N_S') != w['N_S']: bad(f"N_S {r.get('N_S')} != queue {w['N_S']}")
        if r.get('stab') != stab_order(mu): bad('stab order')
        if not (0 < r.get('n_chi', 0) <= r['N_S']): bad('n_chi range')
        if r.get('cover_E', {}).get('excess', -1) < 0: bad('cover excess < 0')
        pp = r.get('per_prime', {})
        if set(pp) != {str(P1), str(P2)}: bad('per_prime keys')
        for p, rec in pp.items():
            att = rec.get('hybrid', {}).get('attempts', [])
            if not att: bad(f'no hybrid attempt at {p}'); continue
            last = att[-1]
            if not (last.get('verified') and last.get('projected_nullity') == r['a'] == last.get('rank')):
                bad(f"hybrid attempt at {p}: verified {last.get('verified')} nullity {last.get('projected_nullity')} rank {last.get('rank')} a {r['a']}")
            if rec.get('units') != r['a'] - rec.get('mult', -1): bad(f'units at {p}')
            if rec.get('mult', -1) > r['a']: bad(f'mult > a at {p}')
        ms = {rec.get('mult') for rec in pp.values()}
        if r.get('primes_agree') != (len(ms) == 1): bad('primes_agree flag')
        if r.get('primes_agree'):
            if r.get('mult') != list(ms)[0] or r.get('units') != r['a'] - r['mult']: bad('mult/units summary')
            if (r['mult'] == r['a']) != r.get('status', '').startswith('proved'): bad('status vs mult')
            if r.get('halt') != (r['mult'] != r['a']): bad('halt flag')
        else:
            if not r.get('halt'): bad('primes disagree but no halt')
    dup = [list(m) for m, c in seen.items() if c > 1]
    if dup: problems.append(dict(mu=dup, problem='duplicate records'))
    out['records'] = dict(count=len(recs), distinct=len(seen), problems=problems,
                          full_rank_both_primes=sum(1 for r in recs if r.get('primes_agree') and r.get('mult') == r.get('a')),
                          sum_a=sum(r['a'] for r in recs))
    print(f"2. records: {len(recs)} ({len(seen)} distinct), {out['records']['full_rank_both_primes']} full rank at both primes, {len(problems)} problems")
    for pr in problems: print('   ', pr)
    # 3. the certificates through tools/verify
    if '--skip-certs' not in argv:
        files = sorted(glob.glob(os.path.join(CERTS, '*_fullrank_p*.json.gz')))
        res = []
        for fn in files:
            t = time.time()
            pr = subprocess.run(['python3', os.path.join(ROOT, 'tools', 'verify', 'verify.py'), fn, '--quiet'], capture_output=True, text=True, cwd=ROOT)
            res.append(dict(file=os.path.relpath(fn, ROOT), rc=pr.returncode, secs=round(time.time() - t, 1),
                            tail=(pr.stdout + pr.stderr).strip().splitlines()[-3:]))
            print(f"3. verify {os.path.basename(fn)}: {'PASS' if pr.returncode == 0 else 'FAIL rc ' + str(pr.returncode)} ({res[-1]['secs']}s)")
        out['certificates'] = dict(count=len(files), passed=sum(1 for x in res if x['rc'] == 0), results=res)
    ok = not mism and not problems and (('certificates' not in out) or out['certificates']['passed'] == out['certificates']['count'])
    out['all_pass'] = ok
    json.dump(out, open(os.path.join(RES, 'verify.json'), 'w'), indent=1)
    print('ALL PASS' if ok else 'FAILURES -- see results/b13_08/verify.json')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
