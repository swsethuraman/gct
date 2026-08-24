"""HWV schemes evaluated at exact sparse orbit points g.det3, g = integer transvections.
Substitutions create monomials with >= 2 row-0 variables, defeating the 20 < 24
counting obstruction that kills all values at det3 itself."""
import itertools, os
from collections import defaultdict
import sympy as sp

X = sp.symbols('x0:9')
det3 = sp.expand(sp.Matrix(3, 3, lambda i, j: X[3*i+j]).det())

SUBS = {
    'A': {X[5]: X[5] + X[1]},                       # x5 -> x5 + x1
    'B': {X[7]: X[7] + X[2]},                       # x7 -> x7 + x2
    'C': {X[5]: X[5] + X[1], X[7]: X[7] + X[2]},    # compose
    'D': {X[3]: X[3] + X[0], X[8]: X[8] + X[1]},
}

def cubic_mons(f):
    out = []
    for mono, cf in sp.Poly(sp.expand(f), *X).terms():
        if cf == 0: continue
        assert sum(mono) == 3
        vs = tuple(i for i in range(9) for _ in range(mono[i]))
        out.append((int(cf), vs))
    return out

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
        for t in batch:
            ordered.append(t); used.add(t)
    assert len(ordered) == 20
    return ordered

os.makedirs('evalin', exist_ok=True)
for sname, sub in SUBS.items():
    mons = cubic_mons(det3.subs(sub, simultaneous=True))
    # row-0 supply check: max legs of vars {0,1,2} available
    rich = sum(1 for c, vs in mons if sum(1 for v in vs if v < 3) >= 2)
    print(f"point {sname}: {len(mons)} monomials, {rich} with >=2 row-0 vars")
    for snum, (shorts, removed) in SCHEMES.items():
        tris = ordered_tris(shorts, removed)
        fn = f'evalin/h{snum}{sname}.txt'
        with open(fn, 'w') as f:
            f.write("9 8 20 3\n9 9 9 9 9 9 3 3\n")
            for t in tris: f.write(" ".join(map(str, t)) + "\n")
            f.write(f"{len(mons)}\n")
            for c, vs in mons:
                f.write(f"{c} " + " ".join(map(str, vs)) + "\n")
            f.write("-1 1\n")
print("files written")
