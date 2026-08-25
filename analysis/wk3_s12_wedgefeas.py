"""Wedge-structural feasibility: does the scheme-1 HWV contraction at a point
admit ANY completing assignment of (monomial, arrangement) choices?
Finer than the content DFS (wk3_s8_feas): respects per-column wedge masks.

Modes:
  point-level: exists a completion with each wide column receiving 0..8
    exactly once and each short column receiving {0,1,2} bijectively.
  subproblem-level: short-column values forced by (sigma6, sigma7).

DFS over copies in engine order with per-column bitmasks, failure memo,
and a remaining-supplier propagation cut.
"""
import itertools, sys
sys.setrecursionlimit(100000)

def scheme1_tris():
    SHORTS = [(0,1,6),(2,3,6),(4,5,6),(0,2,7),(1,4,7),(3,5,7)]
    REMOVED = {(0,1,2),(3,4,5),(0,1,3),(2,4,5),(0,2,4),(1,3,5)}
    ALL20 = [t for t in itertools.combinations(range(6),3)]
    pure = [t for t in ALL20 if t not in REMOVED]
    tris = SHORTS + pure
    ordered, used = [], set()
    for sym in range(8):
        batch = [t for t in tris if t not in used and sym in t]
        batch.sort(key=lambda t: (0 if (6 in t or 7 in t) else 1, t))
        for t in batch: ordered.append(t); used.add(t)
    return ordered

def options_for(tris, mons, sigma=None):
    """Per copy: list of leg-tuples ((e,v),...). sigma: dict col->tuple forcing
    short-column values by supplier order; None = any distinct values allowed
    (handled by masks)."""
    sup = {6: [i for i,t in enumerate(tris) if 6 in t],
           7: [i for i,t in enumerate(tris) if 7 in t]}
    opts = []
    for i, t in enumerate(tris):
        oi = []
        for c, vs in mons:
            for a in sorted(set(itertools.permutations(vs))):
                legs = tuple((t[k], a[k]) for k in range(3))
                ok = True
                for e, v in legs:
                    if e >= 6 and v >= 3: ok = False; break
                    if e >= 6 and sigma is not None and v != sigma[e][sup[e].index(i)]: ok = False; break
                if ok: oi.append(legs)
        opts.append(sorted(set(oi)))
    return opts

def feasible(tris, opts):
    NCOL = 8
    FULL = [0x1FF]*6 + [0x7, 0x7]
    # supplier table: for each (e,v), which copies can place v in e
    supp = [[set() for _ in range(9)] for _ in range(NCOL)]
    for i, oi in enumerate(opts):
        for legs in oi:
            for e, v in legs: supp[e][v].add(i)
    fail = set()
    def dfs(i, masks):
        if i == len(tris):
            return all(masks[e] == FULL[e] for e in range(NCOL))
        key = (i,) + masks
        if key in fail: return False
        # propagation: every still-needed (e,v) must have a supplier >= i
        for e in range(NCOL):
            need = FULL[e] & ~masks[e]
            v = 0
            while need:
                if need & 1:
                    if not any(j >= i for j in supp[e][v]):
                        fail.add(key); return False
                need >>= 1; v += 1
        for legs in opts[i]:
            nm = list(masks); ok = True
            for e, v in legs:
                b = 1 << v
                if nm[e] & b: ok = False; break
                nm[e] |= b
            if ok and dfs(i+1, tuple(nm)):
                return True
        fail.add(key)
        return False
    return dfs(0, (0,)*NCOL)

def mons_of_subs(subs_pairs):
    import sympy as sp
    X = sp.symbols('x0:9')
    det3 = sp.expand(sp.Matrix(3,3, lambda i,j: X[3*i+j]).det())
    f = sp.expand(det3.subs({X[a]: X[a]+X[b] for a,b in subs_pairs}, simultaneous=True))
    out = []
    for mono, cf in sp.Poly(f, *X).terms():
        vs = tuple(i for i in range(9) for _ in range(mono[i]))
        out.append((int(cf), vs))
    return out

if __name__ == '__main__':
    import time
    tris = scheme1_tris()
    perms = list(itertools.permutations((0,1,2)))
    CASES = {'C': [(5,1),(7,2)], 'P': [(3,0),(6,0)], 'G': [(5,1),(7,2),(3,0)]}
    for name, subs in CASES.items():
        mons = mons_of_subs(subs)
        t0 = time.time()
        f_any = feasible(tris, options_for(tris, mons))
        print(f"point {name}: exists-completion {'FEASIBLE' if f_any else 'INFEASIBLE'} ({time.time()-t0:.1f}s)")
        if name in ('C','P'):
            for rep, (i6, i7) in [('00',(0,0)), ('01',(0,1)), ('02',(0,2)), ('03',(0,3)),
                                   ('04',(0,4)), ('05',(0,5)), ('14',(2,2)), ('16',(2,4))]:
                sg = {6: perms[i6], 7: perms[i7]}
                t0 = time.time()
                f = feasible(tris, options_for(tris, mons, sg))
                print(f"   sub {rep}: {'feasible' if f else 'STRUCTURAL ZERO'} ({time.time()-t0:.1f}s)")
