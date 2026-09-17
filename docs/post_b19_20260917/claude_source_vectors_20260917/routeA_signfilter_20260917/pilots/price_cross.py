import json, sys, itertools
sys.path.insert(0, sys.argv[1]); sys.path.insert(0, 'work/descent_followup_claude_20260916/pilots')
import paired_runner as pr, autfilter as af
np = pr.np; c = pr.c
PAIRINGS = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]
rng = np.random.default_rng(20260917)
ALL = tuple(itertools.permutations(range(4)))
from collections import Counter
res = Counter()
kept = []
for A in range(3):
    for B in range(3):
        if A == B: continue
        for n in range(40):
            pi = pr.paired_partition(rng, PAIRINGS[A]); rho = pr.paired_partition(rng, PAIRINGS[B])
            if af.vanishing_reason(pi, rho) is not None: res['obstructed'] += 1; continue
            hp = pr.hand_plan(pi, rho, orders=ALL); hr = pr.hand_plan(rho, pi, orders=ALL)
            # greedy planner of the carrier as alternative
            ll = [pr.column_labels(j) for j in range(4)] + [[('a', s) for s in b] for b in pi] + [[('b', s) for s in b] for b in rho]
            _, gm, gf = c.Net.plan(ll)
            mi = max(hp[1], hr[1]) if hp and hr else None
            res[('hand24', mi, 'greedy', gm)] += 1
            if mi is not None and mi <= 4 ** 10:
                kept.append(dict(pi_pairing=PAIRINGS[A], rho_pairing=PAIRINGS[B], seq=n, pi=[[list(s) for s in blk] for blk in pi], rho=[[list(s) for s in blk] for blk in rho], order=list(hp[0]), order_rev=list(hr[0]), maxint=int(mi), flops=int(hp[2] + hr[2]), aut=af.aut_count(pi, rho)))
for k, v in res.items(): print(k, v)
print('cross kept at <=4^10:', len(kept))
json.dump(kept, open(sys.argv[2], 'w'), indent=1)
