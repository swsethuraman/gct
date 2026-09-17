"""P5: label-only planning diagnostic (no tensors). Greedy planner cost vs a hand order for
paired-columns partitions; also the cost of a 'column-sequential' order used by a custom runner."""
import importlib.util, json, time
from pathlib import Path
HERE = Path(__file__).resolve().parent
SRC = HERE.parents[2] / 'work/batch15_workers/B15-02/analysis/b18_02_carrier.py'
spec = importlib.util.spec_from_file_location('carrier', SRC); c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
np = c.np
HEIGHTS = (5, 5, 5, 5)


def labels_for(pi, rho):
    ll = []
    for j, h in enumerate(HEIGHTS):
        lab = []
        for k in range(h): lab += [('a', (j, k)), ('b', (j, k))]
        ll.append(lab)
    ll += [[('a', s) for s in b] for b in pi]; ll += [[('b', s) for s in b] for b in rho]
    return ll


def paired_partition(rng, pairing):
    blocks = []; left = []
    for (X, Y) in pairing:
        px = list(rng.permutation(5)); py = list(rng.permutation(5))
        blocks.append(tuple([(X, px[0]), (X, px[1]), (Y, py[0]), (Y, py[1])]))
        blocks.append(tuple([(X, px[2]), (X, px[3]), (Y, py[2]), (Y, py[3])]))
        left += [(X, px[4]), (Y, py[4])]
    blocks.append(tuple(left))
    return blocks


def hand_order_cost(pi, rho, order):
    """Contract in a fixed sequence: for each column j in `order`, absorb all epsilon tensors
    that touch column j and are not yet absorbed, then (if a previous accumulated tensor shares
    legs) contract with it. Label-only simulation; returns (maxint, flops)."""
    ll = labels_for(pi, rho)
    cols = [list(l) for l in ll[:4]]; eps = [list(l) for l in ll[4:]]
    acc = None; maxint = 1; flops = 0
    absorbed = [False] * len(eps)
    for j in order:
        cur = cols[j]
        for e_i, e in enumerate(eps):
            if absorbed[e_i]: continue
            if any(lab[1][0] == j for lab in e):
                shared = set(cur) & set(e)
                out = [x for x in cur if x not in shared] + [x for x in e if x not in shared]
                flops += 4 ** len(set(cur) | set(e)); maxint = max(maxint, 4 ** len(out)); cur = out; absorbed[e_i] = True
        if acc is None:
            acc = cur
        else:
            shared = set(acc) & set(cur)
            out = [x for x in acc if x not in shared] + [x for x in cur if x not in shared]
            flops += 4 ** len(set(acc) | set(cur)); maxint = max(maxint, 4 ** len(out)); acc = out
    assert acc == [], acc
    return maxint, flops


rng = np.random.default_rng(1)
PAIRINGS = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]
out = []
t0 = time.perf_counter()
for n in range(6):
    pi = paired_partition(rng, PAIRINGS[n % 3]); rho = paired_partition(rng, PAIRINGS[(n + 1) % 3])
    _, gm, gf = c.Net.plan(labels_for(pi, rho))
    hand = {}
    for order in [(0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2), (1, 0, 3, 2)]:
        try:
            hand[str(order)] = hand_order_cost(pi, rho, order)
        except AssertionError as exc:
            hand[str(order)] = 'incomplete'
    out.append(dict(n=n, greedy=(gm, gf), hand=hand))
# also: same pairing for pi and rho
for n in range(3):
    pi = paired_partition(rng, PAIRINGS[n]); rho = paired_partition(rng, PAIRINGS[n])
    _, gm, gf = c.Net.plan(labels_for(pi, rho))
    hand = {str(o): hand_order_cost(pi, rho, o) for o in [(0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2)]}
    out.append(dict(n='same-pairing-%d' % n, greedy=(gm, gf), hand=hand))
res = dict(results=out, elapsed_s=time.perf_counter() - t0)
Path(HERE / 'p5_plan_diag.json').write_text(json.dumps(res, indent=1) + '\n')
print(json.dumps(res, indent=1))
