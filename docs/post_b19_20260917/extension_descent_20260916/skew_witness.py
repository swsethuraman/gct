"""Exact sparse contraction at the six standard skew 4x4 matrices."""
import itertools as it
import json
import random
import time
from collections import defaultdict
from pathlib import Path

START = time.monotonic()
EDGES = list(it.combinations(range(4), 2))
PAIRS = ((0, 1), (2, 3), (4, 5))

def sign(p):
    return (-1) ** sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1, len(p)))

ASSIGNMENTS = []
for perm in it.permutations(range(6)):
    for flips in it.product((0, 1), repeat=6):
        pairs = [EDGES[e][::(-1 if f else 1)] for e, f in zip(perm, flips)]
        ASSIGNMENTS.append((tuple(a for a,b in pairs), tuple(b for a,b in pairs), sign(perm)*(-1)**sum(flips)))

def aggregate(colpairs):
    out = defaultdict(int)
    for aa, bb, ss in ASSIGNMENTS:
        key = []
        ok = True
        for indices, pairs in ((aa, PAIRS), (bb, colpairs)):
            for i, j in pairs:
                a, b = indices[i], indices[j]
                if a == b:
                    ok = False
                    break
                key.append((1 << a) | (1 << b))
                if a > b:
                    ss = -ss
            if not ok:
                break
        if ok:
            out[tuple(key)] += ss
    return {k:v for k,v in out.items() if v}

def join(left, right):
    total = 0
    matched = 0
    for key, coeff in left.items():
        comp = tuple(15 ^ m for m in key)
        rr = right.get(comp, 0)
        if rr:
            ss = 1
            for mask in key:
                aa = [i for i in range(4) if mask & (1 << i)]
                bb = [i for i in range(4) if not mask & (1 << i)]
                ss *= sign(aa+bb)
            total += ss * coeff * rr
            matched += 1
    return total, matched

def main():
    rng = random.Random(16092026)
    records = []
    for attempt in range(24):
        if time.monotonic()-START > 55:
            break
        lp, rp = list(range(6)), list(range(6))
        rng.shuffle(lp)
        rng.shuffle(rp)
        cp = tuple(tuple(lp[2*i:2*i+2]) for i in range(3))
        cq = tuple(tuple(rp[2*i:2*i+2]) for i in range(3))
        left, right = aggregate(cp), aggregate(cq)
        value, matched = join(left, right)
        rec = dict(attempt=attempt, pi=[list(p)+[i+6 for i in p] for p in PAIRS],
                   rho=[list(p)+[i+6 for i in q] for p,q in zip(cp,cq)],
                   P_value=value, full_H_symmetric_value=2*value,
                   left_support=len(left), right_support=len(right), matched=matched)
        records.append(rec)
        if value:
            # Independent symmetry check: swapping the two six-slot columns
            # reverses two-index blocks in every epsilon (even parity).
            reverse, _ = join(right, left)
            assert reverse == value
            # Swapping one pair in rho reverses precisely one epsilon.
            bad = list(cp)
            bad[0] = bad[0][::-1]
            opposite, _ = join(aggregate(tuple(bad)), right)
            assert opposite == -value
            rec['column_swap_check'] = reverse
            rec['epsilon_sign_control'] = opposite
            break
    result = dict(cell=dict(d=3, weight=[2]*6, ambient=0, source=1, arc_rank=0),
                  point_edges=[list(e) for e in EDGES], assignments=len(ASSIGNMENTS),
                  records=records, found=bool(records and records[-1]['P_value']),
                  elapsed_seconds=time.monotonic()-START)
    dest = Path(__file__).with_name('skew_witness.json')
    dest.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()
