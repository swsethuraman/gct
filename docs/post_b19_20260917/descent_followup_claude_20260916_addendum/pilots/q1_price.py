"""Q1 (Stage A): price a sparse evaluator for full-H epsilon contractions in cell (4^5), d=5.
No contraction is evaluated here. For each point and each block pattern this script counts
  * nonzero column-tensor entries: 5-subsets of nonzero positions with nonzero 5x5 minor
    (ordered entries = 120 x that count);
  * per column, the number of distinct aggregate keys (for each block touched by the column,
    the set of values inserted) among the ordered entries;
  * a bound on reachable DP states at each column boundary: product over partially filled
    blocks of C(4, filled);
  * the transition bound sum_j states(j-1) * keys(j), and estimated time/memory (labelled).
Points: K5, K5+S, K5+2S with S = x1 I4 (transverse); two proposed sparse symmetric-part-zero
arc points at nodes t=0..3 (scaling a); the recorded P7 S0 points for comparison.
Patterns: the two certified vectors q3, q7 (p6_basis.json) and one cross-pairing partition.
"""
import itertools, json, math, sys, time
from pathlib import Path
HERE = Path(__file__).resolve().parent
SEALED = HERE.parents[1] / 'descent_followup_claude_20260916' / 'pilots'
t0 = time.perf_counter()
P = 524287
b6 = json.loads((SEALED / 'p6_basis.json').read_text())
d7 = json.loads((SEALED / 'p7_arc_S0.json').read_text())
patterns = {}
for b in b6['basis']:
    patterns['q%d' % b['index']] = (tuple(tuple(tuple(s) for s in blk) for blk in b['pi']), tuple(tuple(tuple(s) for s in blk) for blk in b['rho']))
# additional pattern: cross pairing, rows on (0,1),(2,3), columns on (0,2),(1,3), fixed explicit splits
pi_x = (((0, 0), (0, 1), (1, 0), (1, 1)), ((0, 2), (0, 3), (1, 2), (1, 3)), ((2, 0), (2, 1), (3, 0), (3, 1)), ((2, 2), (2, 3), (3, 2), (3, 3)), ((0, 4), (1, 4), (2, 4), (3, 4)))
rho_x = (((0, 0), (0, 2), (2, 1), (2, 3)), ((0, 1), (0, 3), (2, 0), (2, 2)), ((1, 0), (1, 2), (3, 1), (3, 3)), ((1, 1), (1, 3), (3, 0), (3, 2)), ((0, 4), (1, 4), (2, 4), (3, 4)))
patterns['cross_x'] = (pi_x, rho_x)


def K5_tuple(t):
    Y = [[[0] * 4 for _ in range(4)] for _ in range(5)]
    for i, (r, cc) in enumerate([(0, 1), (0, 2), (0, 3), (1, 2), (1, 3)]):
        Y[i][r][cc] = 1; Y[i][cc][r] = -1
    Y[0][2][3] += 1; Y[0][3][2] += -1
    for d in range(4): Y[0][d][d] += t
    return Y


def sparse_S0_point(seed):
    """Each matrix: one entry among a, r_i, c_i (value in {1,2,3}) and one skew pair (v, -v)."""
    import random
    rng = random.Random(seed)
    Y = [[[0] * 4 for _ in range(4)] for _ in range(5)]
    for i in range(5):
        choice = rng.choice([(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (2, 0), (3, 0)])
        Y[i][choice[0]][choice[1]] = rng.choice([1, 2, 3, -1, -2])
        r, cc = rng.choice([(1, 2), (1, 3), (2, 3)]); v = rng.choice([1, 2, -1, 3])
        Y[i][r][cc] += v; Y[i][cc][r] -= v
    return Y


def scale_a(Y, t):
    Z = [[row[:] for row in M] for M in Y]
    for i in range(5): Z[i][0][0] *= t
    return Z


def det5(M):
    tot = 0
    for perm in itertools.permutations(range(5)):
        s = 1
        for i in range(5):
            for j in range(i + 1, 5):
                if perm[i] > perm[j]: s = -s
        prod = s
        for i in range(5):
            prod *= M[i][perm[i]]
            if prod == 0: break
        tot += prod
    return tot


def column_support(Y):
    """dict sorted-position-5-tuple -> det (nonzero only)."""
    flat = [[M[r][cc] for r in range(4) for cc in range(4)] for M in Y]
    positions = sorted({p for M in flat for p, v in enumerate(M) if v})
    supp = {}
    for sub in itertools.combinations(positions, 5):
        d = det5([[flat[i][p] for p in sub] for i in range(5)])
        if d: supp[sub] = d
    return positions, supp


SUPP_CACHE = {}


def price(Y, pi, rho, exact_keys):
    key = json.dumps(Y)
    if key not in SUPP_CACHE: SUPP_CACHE[key] = column_support(Y)
    positions, supp = SUPP_CACHE[key]
    n_sub = len(supp); n_ordered = 120 * n_sub
    blocks = [('a', blk) for blk in pi] + [('b', blk) for blk in rho]
    slot_blocks = {}  # slot -> list of (block_id, kind)
    for bid, (kind, blk) in enumerate(blocks):
        for s in blk: slot_blocks.setdefault(s, []).append((bid, kind))
    keys_per_col = []; key_bounds = []; filled = [0] * len(blocks); state_bounds = []; trans = 0; prev_states = 1
    for j in range(4):
        # bound on keys: product over blocks touched of C(4, slots of the block in this column)
        touched = {}
        for k in range(5):
            for bid, kind in slot_blocks[(j, k)]: touched[bid] = touched.get(bid, 0) + 1
        kb = 1
        for n in touched.values(): kb *= math.comb(4, n)
        key_bounds.append(kb)
        nkeys = None
        if exact_keys:
            keys = set()
            for sub in supp:
                for perm in itertools.permutations(range(5)):
                    agg = {}; ok = True
                    for k in range(5):
                        a, b = divmod(sub[perm[k]], 4)
                        for bid, kind in slot_blocks[(j, k)]:
                            v = a if kind == 'a' else b; m = agg.get(bid, 0)
                            if m & (1 << v): ok = False; break
                            agg[bid] = m | (1 << v)
                        if not ok: break
                    if ok: keys.add(tuple(sorted(agg.items())))
            nkeys = len(keys)
        keys_per_col.append(nkeys)
        for bid in touched: filled[bid] += touched[bid]
        sb = 1
        for f in filled:
            if 0 < f < 4: sb *= math.comb(4, f)
        state_bounds.append(sb)
        kk = nkeys if nkeys is not None else kb
        trans += prev_states * kk
        # reachable states after this column are also bounded by prev_states * keys
        prev_states = min(sb, prev_states * kk)
    return dict(nonzero_positions=len(positions), nonzero_subsets=n_sub, ordered_entries=n_ordered,
                keys_per_column_exact=keys_per_col, keys_per_column_bound=key_bounds,
                state_bounds_after_column=state_bounds, transition_bound=trans)


out = dict(prime=P, patterns={k: dict(pi=[[list(s) for s in blk] for blk in v[0]], rho=[[list(s) for s in blk] for blk in v[1]]) for k, v in patterns.items()}, points={})
pts = {('K5', t): K5_tuple(t) for t in (0, 1, 2)}
S0a = sparse_S0_point(101); S0b = sparse_S0_point(202)
out['proposed_sparse_S0_points'] = dict(A=S0a, B=S0b)
for name, Y in (('S0A', S0a), ('S0B', S0b)):
    for t in (0, 1, 2, 3): pts[(name, t)] = scale_a(Y, t)
for p in d7['points'][:1]:
    pts[('P7_S0_point0', 1)] = p['entries']
# exact key counts only where affordable in one 60 s pilot: K5 (t=0,1) all patterns/orientations,
# K5+2S for q3 only, S0A node t=1 for q3 only; everything else gets the product bounds.
EXACT = {('K5', 0): None, ('K5', 1): None, ('K5', 2): {('q3', 'pi_rho'), ('q3', 'rho_pi')}, ('S0A', 1): {('q3', 'pi_rho')}}
order = [('K5', 0), ('K5', 1), ('K5', 2), ('S0A', 0), ('S0A', 1), ('S0A', 2), ('S0A', 3), ('S0B', 0), ('S0B', 1), ('S0B', 2), ('S0B', 3), ('P7_S0_point0', 1)]
for (name, t) in order:
    Y = pts[(name, t)]
    entry = dict(nonzeros_per_matrix=[sum(1 for r in M for v in r if v) for M in Y])
    for pname, (pi, rho) in patterns.items():
        for orient, (pp, rr) in (('pi_rho', (pi, rho)), ('rho_pi', (rho, pi))):
            if time.perf_counter() - t0 > 52: entry['STOP'] = 'deadline'; break
            ex = (name, t) in EXACT and (EXACT[(name, t)] is None or (pname, orient) in EXACT[(name, t)])
            entry['%s_%s' % (pname, orient)] = price(Y, pp, rr, exact_keys=ex)
    out['points']['%s_t%d' % (name, t)] = entry
    (HERE / 'q1_price.json').write_text(json.dumps(out, indent=1) + '\n')
# totals for the full check: q3,q7 at 3 transverse points + S0A,S0B at 4 nodes, both orientations
tot = 0
for key, entry in out['points'].items():
    if key.startswith('P7'): continue
    for pname in ('q3', 'q7'):
        for orient in ('pi_rho', 'rho_pi'):
            e = entry.get('%s_%s' % (pname, orient))
            if e: tot += e['transition_bound']
out['total_transition_bound_two_vectors_all_points'] = tot
out['estimate_note'] = ('ESTIMATE: Python dict transitions at ~2-5 microseconds each; memory ~200 bytes per live state '
                        '(tuple of 10 small ints + big int), states bounded by the listed products; ordered column entries '
                        'need not be materialised (keys are aggregated per column); two orientations double the work; '
                        'the 4 identical columns share one support dict.')
out['elapsed_s'] = time.perf_counter() - t0
(HERE / 'q1_price.json').write_text(json.dumps(out, indent=1) + '\n')
print(json.dumps({k: v for k, v in out.items() if k not in ('patterns', 'proposed_sparse_S0_points')}, indent=1))
