"""Shared runner for epsilon contractions of four height-5 columns (cell (4^5)), with a
column-sequential hand order: process columns in a fixed order; at column j absorb every
not-yet-absorbed epsilon block that has >= 2 legs in column j or whose legs all lie in
columns processed so far; then join with the accumulated tensor. A label-only simulation
(`hand_plan`) prices a partition pair before any array is touched; `hand_run` executes the
same steps with the historical Net.contract_pair (mod P, int64)."""
import importlib.util
from pathlib import Path
HERE = Path(__file__).resolve().parent
SRC = HERE.parents[2] / 'work/batch15_workers/B15-02/analysis/b18_02_carrier.py'
spec = importlib.util.spec_from_file_location('carrier', SRC); c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
np = c.np; P = c.P
HEIGHTS = (5, 5, 5, 5)
SLOTS = [(j, k) for j in range(4) for k in range(5)]


def column_labels(j):
    lab = []
    for k in range(5): lab += [('a', (j, k)), ('b', (j, k))]
    return lab


def paired_partition(rng, pairing):
    blocks = []; left = []
    for (X, Y) in pairing:
        px = [int(v) for v in rng.permutation(5)]; py = [int(v) for v in rng.permutation(5)]
        blocks.append(tuple([(X, px[0]), (X, px[1]), (Y, py[0]), (Y, py[1])]))
        blocks.append(tuple([(X, px[2]), (X, px[3]), (Y, py[2]), (Y, py[3])]))
        left += [(X, px[4]), (Y, py[4])]
    blocks.append(tuple(left))
    return blocks


def random_partition(rng):
    s = [SLOTS[int(i)] for i in rng.permutation(20)]
    return [tuple(s[4 * i:4 * i + 4]) for i in range(5)]


def _plan(pi, rho, order):
    """Returns (steps, maxint, flops). steps: ('col', j) | ('eps', i) | ('join',)."""
    eps = [('a', blk) for blk in pi] + [('b', blk) for blk in rho]
    absorbed = [False] * len(eps)
    steps = []; maxint = 1; flops = 0
    R = None; done = set()

    def absorb_into(cur, pred):
        nonlocal flops, maxint
        changed = True
        while changed:
            changed = False
            for i, (kind, blk) in enumerate(eps):
                if absorbed[i]: continue
                if pred([s[0] for s in blk]):
                    lab = [(kind, s) for s in blk]
                    shared = set(cur) & set(lab)
                    out = [x for x in cur if x not in shared] + [x for x in lab if x not in shared]
                    flops += 4 ** len(set(cur) | set(lab)); maxint = max(maxint, 4 ** len(out))
                    cur = out; absorbed[i] = True; steps.append(('eps', i)); changed = True
        return cur

    for j in order:
        cur = list(column_labels(j)); steps.append(('col', j))
        # (1) blocks with at least two legs in this column
        cur = absorb_into(cur, lambda cols: cols.count(j) >= 2)
        # (2) join with the accumulated tensor
        if R is None:
            R = cur
        else:
            shared = set(R) & set(cur)
            out = [x for x in R if x not in shared] + [x for x in cur if x not in shared]
            flops += 4 ** len(set(R) | set(cur)); maxint = max(maxint, 4 ** len(out)); R = out; steps.append(('join',))
        done.add(j)
        # (3) blocks with at least two legs inside the processed columns
        R = absorb_into(R, lambda cols: sum(1 for cc in cols if cc in done) >= 2)
    assert all(absorbed) and R == [], (absorbed, R)
    return steps, maxint, flops


def hand_plan(pi, rho, orders=((0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2), (1, 2, 0, 3), (2, 3, 0, 1))):
    best = None
    for order in orders:
        try:
            steps, mi, fl = _plan(pi, rho, order)
        except AssertionError:
            continue
        if best is None or (fl, mi) < (best[2], best[1]):
            best = (order, mi, fl)
    return best  # (order, maxint, flops) or None


def evaluate_P(pi, rho, T, order):
    """Executes exactly the control flow of _plan with arrays."""
    net = c.Net(); arr = T.reshape((4, 4) * 5)
    eps = [('a', blk) for blk in pi] + [('b', blk) for blk in rho]
    absorbed = [False] * len(eps)
    R = None; done = set()

    def absorb_into(cur, pred):
        changed = True
        while changed:
            changed = False
            for i, (kind, blk) in enumerate(eps):
                if absorbed[i]: continue
                if pred([s[0] for s in blk]):
                    cur = net.contract_pair(cur, (c.EPS4, [(kind, s) for s in blk]))
                    absorbed[i] = True; changed = True
        return cur

    for j in order:
        cur = (arr, column_labels(j))
        cur = absorb_into(cur, lambda cols: cols.count(j) >= 2)
        R = cur if R is None else net.contract_pair(R, cur)
        done.add(j)
        R = absorb_into(R, lambda cols: sum(1 for cc in cols if cc in done) >= 2)
    val, labels = R
    assert all(absorbed) and labels == [], labels
    return int(val) % P, net.max_intermediate, net.flops


def qval(pi, rho, T, order):
    a, m1, f1 = evaluate_P(pi, rho, T, order); b, m2, f2 = evaluate_P(rho, pi, T, order)
    return (a + b) % P, max(m1, m2), f1 + f2
