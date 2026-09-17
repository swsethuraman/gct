"""Label-only: regenerate P6 candidates (seed 20260916, same rng call order as p6_basis.py) and
apply the sign-vanishing criterion: two slots of the same column sharing a pi block AND a rho block
=> P_{pi,rho} = 0 identically (swap the two summation slots: D flips, both epsilons flip => P=-P).
Also test the symmetrised pair (pi,rho) and (rho,pi): the criterion is symmetric in pi,rho."""
import json, sys, itertools
sys.path.insert(0, 'work/descent_followup_claude_20260916/pilots')
import paired_runner as pr
np = pr.np
def crit1(pi, rho):
    """returns list of offending (slot,slot') pairs"""
    bad = []
    for B in pi:
        for s, t in itertools.combinations(B, 2):
            if s[0] == t[0]:
                for R in rho:
                    if s in R and t in R: bad.append((s, t))
    return bad
rng = np.random.default_rng(20260916)
PAIRINGS = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]
cands = []
for n in range(30):
    prg = PAIRINGS[n % 3]
    cands.append(dict(index=n, pairing=prg, pi=pr.paired_partition(rng, prg), rho=pr.paired_partition(rng, prg)))
p6 = json.load(open('work/descent_followup_claude_20260916/pilots/p6_basis.json'))
# check regeneration matches stored q3,q7
for b in p6['basis']:
    c = cands[b['index']]
    ok = [[list(s) for s in blk] for blk in c['pi']] == b['pi'] and [[list(s) for s in blk] for blk in c['rho']] == b['rho']
    print('regen match index', b['index'], ok)
vals = {a['index']: a['values'] for a in p6['basis_attempts']}
for c in cands[:16]:
    bad = crit1(c['pi'], c['rho'])
    print(c['index'], 'pairing', c['pairing'], 'crit1_zero' if bad else 'crit1_pass', 'nonzero' if any(vals[c['index']]) else 'ZERO', len(bad))
print('--- P8 ---')
p8 = json.load(open('work/descent_followup_claude_20260916/pilots/p8_basis_v2.json'))
a0 = p8['basis_attempts'][0]
print('kind', a0['kind'], 'tried', str(a0['tried'])[:300])
for a in p8['basis_attempts']:
    t = a['tried']
    if isinstance(t, dict) and 'pi' in t:
        pi = [tuple(tuple(s) for s in blk) for blk in t['pi']]; rho = [tuple(tuple(s) for s in blk) for blk in t['rho']]
        print(a['kind'], 'crit1_zero' if crit1(pi, rho) else 'crit1_pass', 'nonzero' if any(a['values']) else 'ZERO', a['maxint'])
    else:
        print(a['kind'], 'no pi/rho stored', 'nonzero' if any(a['values']) else 'ZERO')
print('cost keys', p8.get('candidate_costs_first20', [None])[0])
