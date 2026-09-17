"""Label-only pricing of structurally different contraction families (no arrays touched).
F_trace: 10-cycle trace word tr(W1 adj(W2) W3 adj(W4) ... W9 adj(W10)): adjugate k has 3 slots (in 3 distinct
  columns, forced by symmetry), pi_k = adj_k + following Y-slot, rho_k = adj_k + preceding Y-slot; column
  assignment random subject to column loads 5.
F_asym: paired columns (X,Y),(Z,W) with block types (3,1)+(2,2) or (3,1)+(1,3)... i.e. random split of the
  10 slots of a column pair into two blocks of 4 plus 2 leftovers, no (2,2) constraint.
F_tri: blocks touching three columns: random partition of the 20 slots into 5 blocks subject to each block
  meeting at most 3 columns and at least one block meeting 3 columns.
Each sample: automorphism-sign filter, then hand_plan over all 24 column orders and the greedy planner."""
import itertools, json, sys, time
sys.path.insert(0, 'pilots'); sys.path.insert(0, 'C:/users/swami/projects/gct-gpt/work/descent_followup_claude_20260916/pilots')
import paired_runner as pr, autfilter as af
np = pr.np; c = pr.c
ALL = tuple(itertools.permutations(range(4)))
SLOTS = pr.SLOTS
rng = np.random.default_rng(20260917 + 1)

def price(pi, rho):
    hp = pr.hand_plan(pi, rho, orders=ALL); hr = pr.hand_plan(rho, pi, orders=ALL)
    ll = [pr.column_labels(j) for j in range(4)] + [[('a', s) for s in b] for b in pi] + [[('b', s) for s in b] for b in rho]
    _, gm, gf = c.Net.plan(ll)
    hand = (max(hp[1], hr[1]), hp[2] + hr[2], hp[0], hr[0]) if hp and hr else None
    return hand, (gm, gf)

def random_assignment_trace():
    # 5 adjugates need 3 distinct columns each; Y-slots fill the rest so that each column has 5 slots
    while True:
        miss = [int(x) for x in rng.integers(0, 4, size=5)]  # column missed by adjugate k
        loads = [5 - miss.count(j) for j in range(4)]       # adj slots per column
        need = [5 - loads[j] for j in range(4)]              # Y-slots per column = miss.count(j)
        if any(v < 0 for v in need): continue
        cols_pool = [j for j in range(4) for _ in range(need[j])]
        rng.shuffle(cols_pool)
        # positions: assign slots per column sequentially
        nxt = [0] * 4
        def take(j):
            s = (j, nxt[j]); nxt[j] += 1; return s
        adj = [[take(j) for j in range(4) if j != miss[k]] for k in range(5)]
        ys = [take(cols_pool[k]) for k in range(5)]
        # randomise positions within columns
        perm = {j: [int(x) for x in rng.permutation(5)] for j in range(4)}
        f = lambda s: (s[0], perm[s[0]][s[1]])
        adj = [[f(s) for s in blk] for blk in adj]; ys = [f(s) for s in ys]
        pi = [tuple(adj[k] + [ys[(k + 1) % 5]]) for k in range(5)]
        rho = [tuple(adj[k] + [ys[k]]) for k in range(5)]
        return pi, rho

def random_asym(pairing):
    blocks = []; left = []
    for (X, Y) in pairing:
        s = [(X, k) for k in range(5)] + [(Y, k) for k in range(5)]
        s = [s[int(i)] for i in rng.permutation(10)]
        blocks.append(tuple(s[0:4])); blocks.append(tuple(s[4:8])); left += s[8:10]
    blocks.append(tuple(left))
    return blocks

def random_tri():
    while True:
        s = [SLOTS[int(i)] for i in rng.permutation(20)]
        blocks = [tuple(s[4 * i:4 * i + 4]) for i in range(5)]
        ncols = [len(set(x[0] for x in b)) for b in blocks]
        if max(ncols) <= 3 and 3 in ncols: return blocks

PAIRINGS = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]
fams = {}
t0 = time.time()
fams['trace'] = [random_assignment_trace() for _ in range(300)]
fams['asym_same'] = [(random_asym(PAIRINGS[i % 3]), random_asym(PAIRINGS[i % 3])) for i in range(300)]
fams['asym_paired_pi_22_rho_asym'] = [(pr.paired_partition(rng, PAIRINGS[i % 3]), random_asym(PAIRINGS[i % 3])) for i in range(300)]
fams['tri'] = [(random_tri(), random_tri()) for _ in range(300)]
fams['tri_vs_paired'] = [(pr.paired_partition(rng, PAIRINGS[i % 3]), random_tri()) for i in range(300)]
summary = {}; kept = {}
for name, samples in fams.items():
    from collections import Counter
    cnt = Counter(); kk = []
    for pi, rho in samples:
        pi = [tuple(b) for b in pi]; rho = [tuple(b) for b in rho]
        if af.vanishing_reason(pi, rho) is not None: cnt['obstructed'] += 1; continue
        hand, greedy = price(pi, rho)
        mi = min(hand[0] if hand else 10 ** 12, greedy[0])
        cnt['maxint_%d' % mi] += 1
        if mi <= 4 ** 11:
            kk.append(dict(family=name, pi=[[list(s) for s in b] for b in pi], rho=[[list(s) for s in b] for b in rho], hand=None if hand is None else dict(maxint=int(hand[0]), flops=int(hand[1]), order=list(hand[2]), order_rev=list(hand[3])), greedy=dict(maxint=int(greedy[0]), flops=int(greedy[1])), aut=af.aut_count(pi, rho)))
    summary[name] = dict(cnt); kept[name] = kk
    print(name, dict(cnt), 'kept<=4^11:', len(kk), 'elapsed', round(time.time() - t0, 1), flush=True)
json.dump(dict(summary=summary, kept=kept), open('pilots/price_families.json', 'w'), indent=1)
for name, kk in kept.items():
    for k in kk[:3]: print(name, 'hand', k['hand'] and (k['hand']['maxint'], k['hand']['flops']), 'greedy', k['greedy'], 'aut', k['aut'])
