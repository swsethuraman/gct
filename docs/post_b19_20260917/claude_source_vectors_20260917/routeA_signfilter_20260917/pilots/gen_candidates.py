"""Label-only candidate generation: paired partitions (2+2 slots from a column pair per block, leftover block
of the four fifth slots), pi pairing A and rho pairing B over all 9 combinations, seed 20260917.
Filters: (i) automorphism-sign obstruction (autfilter.vanishing_reason) must be None;
(ii) hand_plan price for both orientations with max intermediate <= 4^10 entries.
No arrays are touched."""
import json, sys, time
sys.path.insert(0, sys.argv[1])  # scratchpad with autfilter.py
sys.path.insert(0, 'work/descent_followup_claude_20260916/pilots')
import paired_runner as pr
import autfilter as af
np = pr.np
PAIRINGS = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]
rng = np.random.default_rng(20260917)
t0 = time.time()
out = []
stats = dict(generated=0, obstructed=0, too_expensive=0, kept=0)
N_PER_COMBO = 40
for A in range(3):
    for B in range(3):
        for n in range(N_PER_COMBO):
            pi = pr.paired_partition(rng, PAIRINGS[A]); rho = pr.paired_partition(rng, PAIRINGS[B])
            stats['generated'] += 1
            r = af.vanishing_reason(pi, rho)
            if r is not None:
                stats['obstructed'] += 1; continue
            hp = pr.hand_plan(pi, rho); hr = pr.hand_plan(rho, pi)
            if hp is None or hr is None or max(hp[1], hr[1]) > 4 ** 10:
                stats['too_expensive'] += 1; continue
            stats['kept'] += 1
            out.append(dict(pi_pairing=PAIRINGS[A], rho_pairing=PAIRINGS[B], seq=n, pi=[[list(s) for s in blk] for blk in pi], rho=[[list(s) for s in blk] for blk in rho],
                            order=list(hp[0]), order_rev=list(hr[0]), maxint=int(max(hp[1], hr[1])), flops=int(hp[2] + hr[2]), aut=af.aut_count(pi, rho)))
print(json.dumps(stats), 'elapsed', round(time.time() - t0, 1))
json.dump(out, open(sys.argv[2], 'w'), indent=1)
from collections import Counter
print('kept per (A,B):', Counter((tuple(c['pi_pairing']), tuple(c['rho_pairing'])) for c in out))
print('flops range', min(c['flops'] for c in out), max(c['flops'] for c in out), 'maxint set', Counter(c['maxint'] for c in out))
