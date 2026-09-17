"""Label-only automorphism-sign filter for epsilon contraction pairs (pi,rho) on 4 columns x 5 positions.
g in S_5 wr S_4 (column map sigma, position bijections phi_j) acting on slots. If g maps the pi set-partition
to itself and the rho set-partition to itself, then P_{pi,rho} = sign(g) P_{pi,rho} where
sign(g) = prod_j sgn(phi_j) * prod_{pi blocks} sgn(reorder) * prod_{rho blocks} sgn(reorder). sign=-1 => P=0.
If g maps pi->rho and rho->pi with sign -1 then q = P_{pi,rho}+P_{rho,pi} = 0 (tau-antisymmetric)."""
import itertools, sys
sys.path.insert(0, 'work/descent_followup_claude_20260916/pilots')
import paired_runner as pr
np = pr.np
SLOTS = pr.SLOTS

def perm_sign(seq):
    s = 1; seq = list(seq)
    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            if seq[i] > seq[j]: s = -s
    return s

def block_of(part):
    d = {}
    for bi, B in enumerate(part):
        for s in B: d[s] = bi
    return d

def automorphisms(pi, rho, target_pi, target_rho):
    """Backtracking over column maps sigma and slot bijections g with g(block of pi) = block of target_pi etc.
    Yields (sigma, gmap dict)."""
    bpi, brho = block_of(pi), block_of(rho)
    tbpi, tbrho = block_of(target_pi), block_of(target_rho)
    tpi_sets = [frozenset(B) for B in target_pi]; trho_sets = [frozenset(B) for B in target_rho]
    for sigma in itertools.permutations(range(4)):
        # assign g on slots column by column; g(j,k) = (sigma[j], phi_j[k])
        g = {}
        used = set()
        # block image maps must be consistent: pi block index -> target pi block index (a bijection)
        pimap = {}; rhomap = {}
        order = SLOTS
        def rec(idx):
            if idx == len(order):
                yield dict(g); return
            s = order[idx]
            for k in range(5):
                t = (sigma[s[0]], k)
                if t in used: continue
                # pi consistency
                pb = bpi[s]; tpb = tbpi[t]
                if pb in pimap:
                    if pimap[pb] != tpb: continue
                    newp = False
                else:
                    if tpb in pimap.values(): continue
                    newp = True
                rb = brho[s]; trb = tbrho[t]
                if rb in rhomap:
                    if rhomap[rb] != trb: continue
                    newr = False
                else:
                    if trb in rhomap.values(): continue
                    newr = True
                if newp: pimap[pb] = tpb
                if newr: rhomap[rb] = trb
                g[s] = t; used.add(t)
                yield from rec(idx + 1)
                del g[s]; used.discard(t)
                if newp: del pimap[pb]
                if newr: del rhomap[rb]
        for gm in rec(0):
            yield sigma, gm

def sign_of(g, pi, rho, target_pi, target_rho):
    # positions: for each column j, phi_j(k) = g[(j,k)][1]
    s = 1
    for j in range(4):
        s *= perm_sign([g[(j, k)][1] for k in range(5)])
    for part, tpart in ((pi, target_pi), (rho, target_rho)):
        tindex = {}
        for B in tpart:
            for pos, sl in enumerate(B): tindex[sl] = (B, pos)
        for B in part:
            imgs = [g[sl] for sl in B]
            tB = tindex[imgs[0]][0]
            assert all(tindex[x][0] == tB for x in imgs)
            s *= perm_sign([tindex[x][1] for x in imgs])
    return s

def vanishing_reason(pi, rho, max_aut=200000):
    """Returns None if no sign obstruction found, else a description."""
    n = 0
    for sigma, g in automorphisms(pi, rho, pi, rho):
        n += 1
        if sign_of(g, pi, rho, pi, rho) == -1:
            return dict(kind='P_zero', sigma=list(sigma), g={str(k): list(v) for k, v in g.items()})
        if n > max_aut: break
    for sigma, g in automorphisms(pi, rho, rho, pi):
        if sign_of(g, pi, rho, rho, pi) == -1:
            return dict(kind='q_zero_tau_antisym', sigma=list(sigma), g={str(k): list(v) for k, v in g.items()})
    return None

def aut_count(pi, rho):
    return sum(1 for _ in automorphisms(pi, rho, pi, rho))

if __name__ == '__main__':
    import json
    rng = np.random.default_rng(20260916)
    PAIRINGS = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]
    cands = []
    for n in range(30):
        prg = PAIRINGS[n % 3]
        cands.append(dict(index=n, pairing=prg, pi=pr.paired_partition(rng, prg), rho=pr.paired_partition(rng, prg)))
    p6 = json.load(open('work/descent_followup_claude_20260916/pilots/p6_basis.json'))
    vals = {a['index']: a['values'] for a in p6['basis_attempts']}
    for c in cands[:16]:
        r = vanishing_reason(c['pi'], c['rho'])
        print(c['index'], 'nonzero' if any(vals[c['index']]) else 'ZERO', 'aut', aut_count(c['pi'], c['rho']), 'obstruction:', None if r is None else (r['kind'], r['sigma']))
