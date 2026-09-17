"""Integrator cross-seam test of B19-11's packet, per its own section 9.
Reads results/b19_11/vectors/S19.json ONLY. Imports no project code.
Rebuilds the four raising operators from MONS + basis tuples and the stated rule."""
import json, itertools
from collections import defaultdict

P = json.load(open('/mnt/user-data/uploads/Projects/gct-gpt/work/batch15_workers/'
                   'B15-11/results/b19_11/vectors/S19.json'))
MONS  = [tuple(m) for m in P['monomial_ordering']['MONS_degree4_exponent_vectors_in_order']]
BASIS = [tuple(b) for b in P['monomial_ordering']['basis_as_MONS_index_tuples_in_order']]
W     = P['vector_W']
LAM   = tuple(P['lambda'])
NV    = P['n_variables']
MIDX  = {m: i for i, m in enumerate(MONS)}
print(f"read packet: |MONS| = {len(MONS)}, K = {len(BASIS)}, |W| = {len(W)}, lambda = {LAM}")

# --- sanity on the ordering the packet claims
assert len(MONS) == 70 and all(sum(m) == 4 for m in MONS)
first_exp = [list(MONS[i]) for i in BASIS[0]]
assert first_exp == P['monomial_ordering']['first_basis_element_expanded'], "first element mismatch"
last_exp  = [list(MONS[i]) for i in BASIS[-1]]
assert last_exp == P['monomial_ordering']['last_basis_element_expanded'], "last element mismatch"
def wt(b):
    v = [0]*NV
    for i in b:
        for k in range(NV): v[k] += MONS[i][k]
    return tuple(v)
assert all(wt(b) == LAM for b in BASIS), "a basis element has the wrong weight"
print("ordering self-consistent: first/last expansions match, every basis element has weight lambda")

# --- independent target-basis dimension: multisets of 5 degree-4 monomials of a given weight
def multiset_weight_counts(deg=4, size=5, nv=5):
    base = [m for m in itertools.product(range(deg+1), repeat=nv) if sum(m) == deg]
    dp = [dict() for _ in range(size+1)]
    dp[0][(0,)*nv] = 1
    for m in base:
        for c in range(size):
            for vec, cnt in list(dp[c].items()):
                nvv = tuple(a+b for a, b in zip(vec, m))
                dp[c+1][nvv] = dp[c+1].get(nvv, 0) + cnt
    return dp[size]
M = multiset_weight_counts()
print(f"independent weight-multiplicity table built: {len(M)} weights; M[lambda] = {M[LAM]}")

# --- rebuild each operator from the stated convention
def raise_op(i):
    "E_{i,i+1}: c_alpha -> (alpha_i + 1) c_(alpha + e_i - e_{i+1}) when alpha_{i+1} > 0, as a derivation"
    j = i + 1
    ent = defaultdict(int)                 # (src_index, target_multiset) -> coefficient
    for si, b in enumerate(BASIS):
        for pos in range(5):
            a = MONS[b[pos]]
            if a[j] == 0: continue
            na = list(a); na[i] += 1; na[j] -= 1; na = tuple(na)
            ti = MIDX[na]
            tgt = tuple(sorted(b[:pos] + (ti,) + b[pos+1:]))
            ent[(si, tgt)] += (a[i] + 1)
    return {k: v for k, v in ent.items() if v != 0}

print(f"\n{'op':>6} {'target weight':>16} {'target dim':>11} {'claimed':>8} "
      f"{'nonzeros':>9} {'claimed':>8} {'E(W)=0':>7} {'E(e0) nz':>9} {'claimed':>8}")
ok_all = True
for i in range(4):
    op = raise_op(i)
    tw = list(LAM); tw[i] += 1; tw[i+1] -= 1; tw = tuple(tw)
    tdim = M.get(tw, 0)
    nz   = len(op)
    # E(W)
    res = defaultdict(int)
    for (si, tgt), c in op.items(): res[tgt] += c * W[si]
    resnz = sum(1 for v in res.values() if v != 0)
    # E(e_0): e_0 is the indicator of source basis element 0
    a0 = defaultdict(int)
    for (si, tgt), c in op.items():
        if si == 0: a0[tgt] += c
    a0nz = sum(1 for v in a0.values() if v != 0)
    cl = P['verification']['operators'][i]
    good = (tdim == cl['target_dim'] and nz == cl['operator_nonzero_entries']
            and resnz == 0 and a0nz == cl['action_on_e0_nonzero_count']
            and list(tw) == cl['target_weight'])
    ok_all &= good
    print(f"{'E_%d,%d'%(i+1,i+2):>6} {str(tw):>16} {tdim:>11} {cl['target_dim']:>8} "
          f"{nz:>9} {cl['operator_nonzero_entries']:>8} {str(resnz==0):>7} {a0nz:>9} "
          f"{cl['action_on_e0_nonzero_count']:>8}  {'OK' if good else 'MISMATCH'}")

print(f"\nvector primitive, first nonzero positive: "
      f"{__import__('math').gcd(*[abs(x) for x in W if x]) == 1 and next(x for x in W if x) > 0}")
print(f"max |coefficient| = {max(abs(x) for x in W)}   (packet says {P['verification']['max_abs_coefficient']})")
print(f"nonzero coordinates = {sum(1 for x in W if x)}   (packet says {P['verification']['nonzero_coordinates']})")
print(f"\nALL FOUR OPERATORS REBUILT AND MATCHED: {ok_all}")
