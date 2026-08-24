"""The canonical pattern: 18 distinct epsilon-triples (all C(6,3)=20 minus the
complementary pair {0,1,2},{3,4,5}).  Signed backtracking count of admissible
assignments; incremental epsilon-insertion parities; node budget."""
import itertools, time, sys

DET_MONS = []
for sigma in itertools.permutations((0,1,2)):
    sg = 1
    for i in range(3):
        for j in range(i+1,3):
            if sigma[i] > sigma[j]: sg = -sg
    DET_MONS.append((tuple(3*r + sigma[r] for r in range(3)), sg))

TRIPLES = [t for t in itertools.combinations(range(6), 3)
           if t != (0,1,2) and t != (3,4,5)]
assert len(TRIPLES) == 18
cover = [sum(1 for t in TRIPLES if e in t) for e in range(6)]
assert cover == [9]*6, cover

# order f's to interleave epsilon usage (greedy: sort by triple)
ORDER = sorted(range(18), key=lambda i: TRIPLES[i])

# per f: 36 options: (assignments ((eps, var), (eps, var), (eps, var)), sign)
OPTIONS = []
for i in range(18):
    tri = TRIPLES[i]
    opts = []
    for mon, sg in DET_MONS:
        for perm in itertools.permutations(range(3)):
            asg = tuple((tri[k], mon[perm[k]]) for k in range(3))
            opts.append((asg, sg))
    OPTIONS.append(opts)

NODE_BUDGET = 350_000_000
nodes = 0
start = time.time()
masks = [0]*6          # bitmask of variables already received per epsilon
counts = [0]*6         # number received
total = 0
aborted = False

# feasibility: remaining suppliers per epsilon
REMAIN = [[0]*6 for _ in range(19)]
for pos in range(17, -1, -1):
    f = ORDER[pos]
    for e in range(6):
        REMAIN[pos][e] = REMAIN[pos+1][e] + (1 if e in TRIPLES[f] else 0)

def popcount_gt(mask, v):
    return bin(mask >> (v+1)).count('1')

sys.setrecursionlimit(10000)

def rec(pos, sign):
    global nodes, total, aborted
    if aborted: return
    nodes += 1
    if nodes > NODE_BUDGET:
        aborted = True; return
    if pos == 18:
        total += sign
        return
    # feasibility prune
    for e in range(6):
        if 9 - counts[e] > REMAIN[pos][e]*1:
            return
    f = ORDER[pos]
    for asg, sg in OPTIONS[f]:
        ok = True
        for (e, v) in asg:
            if masks[e] >> v & 1: ok = False; break
        if not ok: continue
        s = sign*sg
        for (e, v) in asg:
            # insertion parity: elements already present and greater than v
            s *= (-1)**popcount_gt(masks[e], v)
            masks[e] |= 1 << v
            counts[e] += 1
        rec(pos+1, s)
        for (e, v) in asg:
            masks[e] &= ~(1 << v)
            counts[e] -= 1

rec(0, 1)
el = time.time()-start
if aborted:
    print(f"ABORTED at {nodes} nodes ({el:.0f}s); partial total (not meaningful) = {total}")
else:
    print(f"complete: nodes {nodes} ({el:.0f}s)")
    print(f"canonical-pattern value at det_3 = {total}")
    if total != 0:
        print("=> THE BIT IS 1: e(det_3) = 18; the unique degree-18 invariant is the")
        print("   fundamental invariant, and its zero set in the closure is the boundary.")
    else:
        print("=> value 0 for this pattern at det_3; need nonzero-witness test on random cubics")
