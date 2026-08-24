"""Generate evalfile inputs: quad check, det3 calibration, P1, P2, ternary tests."""
import itertools, os

os.makedirs('evalin', exist_ok=True)

# --- det-world triples, early-completion order (must match dp.c exactly) ---
raw = [t for t in itertools.combinations(range(6), 3) if t not in ((0,1,2),(3,4,5))]
TRI = []
for cls in range(3):
    for t in raw:
        k = 0 if 0 in t else (1 if 1 in t else 2)
        if k == cls: TRI.append(t)
assert len(TRI) == 18 and TRI[0] == (0,1,3)

def write_file(name, NV, NE, NF, NLEG, tri, mons, fixroot=-1, mult=1):
    with open(f'evalin/{name}', 'w') as f:
        f.write(f"{NV} {NE} {NF} {NLEG}\n")
        for t in tri: f.write(" ".join(map(str, t)) + "\n")
        f.write(f"{len(mons)}\n")
        for c, vs in mons:
            f.write(f"{c} " + " ".join(map(str, vs)) + "\n")
        f.write(f"{fixroot} {mult}\n")

# quad: det2 = x0 x3 - x1 x2, expect 24
write_file('quad.txt', 4, 2, 4, 2, [(0,1)]*4, [(1,(0,3)), (-1,(1,2))])

# det3 calibration: fixroot 0 (identity monomial listed first, arrangement (0,4,8)), x36
DET = [(1,(0,4,8)), (-1,(0,5,7)), (-1,(1,3,8)), (1,(1,5,6)), (1,(2,3,7)), (-1,(2,4,6))]
write_file('det3cal.txt', 9, 6, 18, 3, TRI, DET, fixroot=0, mult=36)

# P1: det of traceless (x8 -> -x0-x4): 8 monomials
P1 = [(-1,(0,0,4)), (-1,(0,4,4)),          # from +x0 x4 x8
      (-1,(0,5,7)),
      (1,(0,1,3)), (1,(1,3,4)),            # from -x1 x3 x8
      (1,(1,5,6)), (1,(2,3,7)), (-1,(2,4,6))]
write_file('p1.txt', 9, 6, 18, 3, TRI, P1)

# P2: universal quadric (session-1 representative, cone-dim 64 validated)
P2 = [(1,(3,0,0)), (1,(4,1,1)), (1,(5,2,2)), (1,(6,0,1)), (1,(7,1,2)), (1,(8,0,2))]
write_file('p2.txt', 9, 6, 18, 3, TRI, P2)

# ternary degree-4 pattern world: 4 copies, 4 eps_3, all C(4,3) triples
T4 = [(0,1,2),(0,1,3),(0,2,3),(1,2,3)]
def tern(name, monos):
    """monos: dict (i,j,k) exponents -> coeff; vars x,y,z -> 0,1,2"""
    ms = []
    for (i,j,k), c in monos.items():
        vs = tuple([0]*i + [1]*j + [2]*k)
        ms.append((c, vs))
    write_file(name, 3, 4, 4, 3, T4, ms)

tern('t_fermat.txt', {(3,0,0):1, (0,3,0):1, (0,0,3):1})
tern('t_cusp.txt',   {(2,1,0):1, (0,0,3):1})
tern('t_xyz.txt',    {(1,1,1):1})
import random
random.seed(7)
allm = [(i, j, 3-i-j) for i in range(4) for j in range(4-i)]
for r in range(3):
    tern(f't_rand{r}.txt', {m: random.randint(-3,3) for m in allm})
print("inputs written:", sorted(os.listdir('evalin')))
