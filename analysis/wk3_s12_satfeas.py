"""SAT-based wedge-structural feasibility for scheme-1 HWV evaluation.
Encoding: x_{i,o} = copy i uses option o (a (monomial, arrangement) with legs).
  - exactly-one option per copy
  - for each wide column e in 0..5, each variable v in 0..8: exactly one
    chosen leg supplies (e, v)
  - for each short column e in 6,7, each v in 0..2: exactly one chosen leg
    supplies (e, v)   [point-level; subproblem-level forces values instead]
UNSAT  <=> structural zero (no completing contraction path).
"""
import itertools, sys
from pysat.solvers import Minisat22
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool

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
    sup = {6: [i for i,t in enumerate(tris) if 6 in t],
           7: [i for i,t in enumerate(tris) if 7 in t]}
    opts = []
    for i, t in enumerate(tris):
        oi = set()
        for c, vs in mons:
            for a in set(itertools.permutations(vs)):
                legs = tuple((t[k], a[k]) for k in range(3))
                ok = True
                for e, v in legs:
                    if e >= 6 and v >= 3: ok = False; break
                    if e >= 6 and sigma is not None and v != sigma[e][sup[e].index(i)]: ok = False; break
                if ok: oi.add(legs)
        opts.append(sorted(oi))
    return opts

def sat_feasible(tris, opts):
    pool = IDPool()
    cls = []
    xvar = {}
    for i, oi in enumerate(opts):
        if not oi: return False
        vs = []
        for o, legs in enumerate(oi):
            xvar[(i,o)] = pool.id(('x', i, o)); vs.append(xvar[(i,o)])
        cls.append(vs)                                    # at least one
        cls += CardEnc.atmost(vs, 1, vpool=pool, encoding=EncType.pairwise).clauses
    covers = {}
    for i, oi in enumerate(opts):
        for o, legs in enumerate(oi):
            for e, v in legs:
                covers.setdefault((e, v), []).append(xvar[(i,o)])
    targets = [(e, v) for e in range(6) for v in range(9)] + [(e, v) for e in (6,7) for v in range(3)]
    for t in targets:
        lst = covers.get(t, [])
        if not lst: return False
        cls.append(lst)
        cls += CardEnc.atmost(lst, 1, vpool=pool, encoding=EncType.pairwise).clauses
    with Minisat22(bootstrap_with=cls) as m:
        return m.solve()

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
    REPS = [('00',(0,0)), ('01',(0,1)), ('02',(0,2)), ('03',(0,3)),
            ('04',(0,4)), ('05',(0,5)), ('14',(2,2)), ('16',(2,4))]
    # validation cases first, then P orbit adjudication
    for name, subs in [('C', [(5,1),(7,2)]), ('P', [(3,0),(6,0)])]:
        mons = mons_of_subs(subs)
        t0 = time.time()
        pt = sat_feasible(tris, options_for(tris, mons))
        print(f"point {name}: exists-completion {'SAT-live' if pt else 'UNSAT (structural zero)'} ({time.time()-t0:.1f}s)")
        for rep, (i6, i7) in REPS:
            sg = {6: perms[i6], 7: perms[i7]}
            t0 = time.time()
            f = sat_feasible(tris, options_for(tris, mons, sg))
            print(f"   sub {rep}: {'SAT-live' if f else 'UNSAT'} ({time.time()-t0:.1f}s)")
