"""Factored HWV evaluation: fix the short-column (eps3) variable assignments
(36 subproblems), drop those legs, fold their parity into a global sign.
Also: factored version of the S(4,2) anchor for validation."""
import itertools, os, sys
import sympy as sp

X = sp.symbols('x0:9')
det3 = sp.expand(sp.Matrix(3, 3, lambda i, j: X[3*i+j]).det())

def cubic_mons(f, nv):
    Xs = X[:nv]
    out = []
    for mono, cf in sp.Poly(sp.expand(f), *Xs).terms():
        if cf == 0: continue
        vs = tuple(i for i in range(nv) for _ in range(mono[i]))
        out.append((int(cf), vs))
    return out

def arrangements(vs):
    return sorted(set(itertools.permutations(vs)))

def sgn(perm):
    s = 1
    for i in range(len(perm)):
        for j in range(i+1, len(perm)):
            if perm[i] > perm[j]: s = -s
    return s

def write_factored(fn, tris, mons, shortsyms, widths_keep, ne_keep, assign, groups=()):
    """tris: ordered copy triples (may contain short symbols).
    shortsyms: dict shortsym -> list of (copy_index_in_order) suppliers.
    assign: dict shortsym -> tuple of vars for its suppliers in copy order.
    Emits evalopts file over the kept eps only. Returns False if some copy has 0 options."""
    sign = 1
    for ssym, vars_ in assign.items():
        sign *= sgn(vars_)
    lines = []
    ok = True
    for i, t in enumerate(tris):
        opts = []
        spos = [k for k, e in enumerate(t) if e in shortsyms]
        assert len(spos) <= 1
        if spos:
            p = spos[0]; ssym = t[p]
            v_forced = assign[ssym][shortsyms[ssym].index(i)]
        for c, vs in mons:
            arrs = arrangements(vs)
            w = c * (6 // len(arrs))
            for a in arrs:
                if spos:
                    if a[p] != v_forced: continue
                    legs = [(t[k], a[k]) for k in range(3) if k != p]
                else:
                    legs = [(t[k], a[k]) for k in range(3)]
                if any(v >= widths_keep[e] for e, v in legs): continue   # width filter
                opts.append((w, legs))
        if not opts: ok = False
        lines.append(opts)
    with open(fn, 'w') as f:
        f.write(f"{ne_keep} {len(tris)}\n")
        f.write(" ".join(map(str, widths_keep)) + "\n")
        f.write(f"{len(groups)}\n")
        for tot, vs in groups:
            f.write(f"{tot} {len(vs)} " + " ".join(map(str, vs)) + "\n")
        for opts in lines:
            f.write(f"{len(opts)}\n")
            for w, legs in opts:
                f.write(f"{w} {len(legs)} " + " ".join(f"{e} {v}" for e, v in legs) + "\n")
        f.write(f"{sign}\n")
    return ok

# ---------- anchor validation: factored S(4,2) ----------
def anchor_factored():
    import random
    random.seed(23)
    allm = [(i, j, 3-i-j) for i in range(4) for j in range(4-i)]
    tests = {'cusp': {(2,1,0):1,(0,0,3):1}, 'rand0': {m: random.randint(-3,3) for m in allm}}
    for name, fdict in tests.items():
        mons = []
        for (i,j,k), cf in fdict.items():
            if cf == 0: continue
            mons.append((cf, tuple([0]*i + [1]*j + [2]*k)))
        tris = [(0,1,2),(0,1,3)]
        shortsyms = {2: [0], 3: [1]}
        assign = {2: (0,), 3: (0,)}   # width-1 columns: forced x0
        write_factored(f'evalin/af_{name}.txt', tris, mons, shortsyms, (2,2), 2, assign)
    print("anchor-factored files written (expect cusp -8, rand0 -24)")

# ---------- the 36 subproblems for scheme s at point C ----------
SUBS_C = {X[5]: X[5] + X[1], X[7]: X[7] + X[2]}
ALL20 = [t for t in itertools.combinations(range(6), 3)]
SCHEMES = {
 1: ([(0,1,6),(2,3,6),(4,5,6),(0,2,7),(1,4,7),(3,5,7)],
     {(0,1,2),(3,4,5),(0,1,3),(2,4,5),(0,2,4),(1,3,5)}),
 2: ([(0,3,6),(1,4,6),(2,5,6),(0,4,7),(1,5,7),(2,3,7)],
     {(0,1,2),(3,4,5),(0,1,4),(2,3,5),(0,2,5),(1,3,4)}),
 3: ([(0,1,6),(2,3,6),(4,5,6),(0,2,7),(1,4,7),(3,5,7)],
     {(0,1,3),(2,4,5),(0,1,4),(2,3,5),(0,1,5),(2,3,4)}),
}
def ordered_tris(shorts, removed):
    pure = [t for t in ALL20 if t not in removed]
    tris = shorts + pure
    ordered, used = [], set()
    for sym in range(8):
        batch = [t for t in tris if t not in used and sym in t]
        batch.sort(key=lambda t: (0 if (6 in t or 7 in t) else 1, t))
        for t in batch: ordered.append(t); used.add(t)
    return ordered

def gen_subproblems(snum, pointname='C'):
    shorts, removed = SCHEMES[snum]
    tris = ordered_tris(shorts, removed)
    mons = cubic_mons(det3.subs(SUBS_C, simultaneous=True), 9)
    shortsyms = {6: [i for i, t in enumerate(tris) if 6 in t],
                 7: [i for i, t in enumerate(tris) if 7 in t]}
    n = 0
    for p6 in itertools.permutations((0,1,2)):
        for p7 in itertools.permutations((0,1,2)):
            fn = f'evalin/f{snum}{pointname}_{n:02d}.txt'
            G = [(18,(0,1,2)),(18,(3,4,5)),(18,(6,7,8)),(18,(0,3,6)),(18,(1,4,7)),(18,(2,5,8))]
            write_factored(fn, tris, mons, shortsyms, (9,)*6, 6, {6: p6, 7: p7}, groups=G)
            n += 1
    print(f"scheme {snum} point {pointname}: {n} subproblem files")

if __name__ == '__main__':
    os.makedirs('evalin', exist_ok=True)
    anchor_factored()
    gen_subproblems(1)
