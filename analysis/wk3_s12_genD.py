"""Factored HWV evaluation inputs for point D (second balanced substitution),
generalizing wk3_s8_gen3.py: parameterized substitution + output dir.
Validation mode: regenerate the point-C set and diff against the banked
inputs/evalin/f1C_*.txt (must be byte-identical).

Point D: x3 -> x3 + x0 (row0 col0 into row1 col0),
         x8 -> x8 + x1 (row0 col1 into row2 col2).
"""
import itertools, os, sys
import sympy as sp

X = sp.symbols('x0:9')
det3 = sp.expand(sp.Matrix(3, 3, lambda i, j: X[3*i+j]).det())

SUBS = {
    'C': {X[5]: X[5] + X[1], X[7]: X[7] + X[2]},
    'D': {X[3]: X[3] + X[0], X[8]: X[8] + X[1]},
}

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
                if any(v >= widths_keep[e] for e, v in legs): continue
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

ALL20 = [t for t in itertools.combinations(range(6), 3)]
SCHEMES = {
 1: ([(0,1,6),(2,3,6),(4,5,6),(0,2,7),(1,4,7),(3,5,7)],
     {(0,1,2),(3,4,5),(0,1,3),(2,4,5),(0,2,4),(1,3,5)}),
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

def gen_subproblems(snum, pointname, outdir):
    shorts, removed = SCHEMES[snum]
    tris = ordered_tris(shorts, removed)
    mons = cubic_mons(det3.subs(SUBS[pointname], simultaneous=True), 9)
    shortsyms = {6: [i for i, t in enumerate(tris) if 6 in t],
                 7: [i for i, t in enumerate(tris) if 7 in t]}
    n = 0
    allok = True
    for p6 in itertools.permutations((0,1,2)):
        for p7 in itertools.permutations((0,1,2)):
            fn = f'{outdir}/f{snum}{pointname}_{n:02d}.txt'
            G = [(18,(0,1,2)),(18,(3,4,5)),(18,(6,7,8)),(18,(0,3,6)),(18,(1,4,7)),(18,(2,5,8))]
            ok = write_factored(fn, tris, mons, shortsyms, (9,)*6, 6, {6: p6, 7: p7}, groups=G)
            allok = allok and ok
            n += 1
    print(f"scheme {snum} point {pointname}: {n} subproblem files -> {outdir} (all copies have options: {allok})")

if __name__ == '__main__':
    point = sys.argv[1] if len(sys.argv) > 1 else 'D'
    outdir = sys.argv[2] if len(sys.argv) > 2 else 'evalin'
    os.makedirs(outdir, exist_ok=True)
    gen_subproblems(1, point, outdir)
