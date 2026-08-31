"""Session 26's reduction, applied to the PADDED permanent -- the GCT-relevant case.

A weight of length r sees a form f on C^N only through f restricted to an
r-dimensional subspace.  So D_r^f = closure{ f|_L } and the ideal at length r is
empty iff that map is dominant.  For per_3^pad = x_0 * per_3 inside Sym^4 C^16,
the form uses only 10 of the 16 coordinates, so the source is (C^10)^r.
"""
import random, itertools
from math import comb
P = (1 << 61) - 1

def pmul(a, b, r):
    o = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            e = tuple(e1[k]+e2[k] for k in range(r))
            o[e] = (o.get(e,0) + c1*c2) % P
    return {e:c for e,c in o.items() if c}
def padd(a,b):
    o = dict(a)
    for e,c in b.items(): o[e] = (o.get(e,0)+c) % P
    return {e:c for e,c in o.items() if c}
def pscal(a,s): return {e:(c*s)%P for e,c in a.items() if (c*s)%P}

def per3(M, r):
    """permanent of a 3x3 matrix of polynomials"""
    acc = {}
    for s in itertools.permutations(range(3)):
        t = pmul(pmul(M[0][s[0]], M[1][s[1]], r), M[2][s[2]], r)
        acc = padd(acc, t)
    return acc

def rank_mod(rows, ncols):
    rk = 0
    for col in range(ncols):
        piv = next((i for i in range(rk, len(rows)) if rows[i][col]), None)
        if piv is None: continue
        rows[rk], rows[piv] = rows[piv], rows[rk]
        inv = pow(rows[rk][col], P-2, P)
        rows[rk] = [(x*inv) % P for x in rows[rk]]
        for i in range(len(rows)):
            if i != rk and rows[i][col]:
                f = rows[i][col]
                rows[i] = [(rows[i][c]-f*rows[rk][c]) % P for c in range(ncols)]
        rk += 1
    return rk

def perpad_rank(r, seed=0):
    """rank of d[(v_1..v_r) -> per_3^pad(sum s_i v_i)], v_i in C^10."""
    rnd = random.Random(seed)
    V = [[rnd.randint(-6,6) for _ in range(10)] for _ in range(r)]   # v_i coords: 0 = x_0, 1..9 = y
    def lin(c):        # coordinate c of sum s_i v_i, as a poly in s
        d = {}
        for i in range(r):
            v = V[i][c] % P
            if v:
                e = [0]*r; e[i] = 1; d[tuple(e)] = v
        return d
    X0 = lin(0)
    Y  = [[lin(1+3*a+b) for b in range(3)] for a in range(3)]
    monos = [e for e in itertools.product(range(5), repeat=r) if sum(e) == 4]
    assert len(monos) == comb(r+3, 4)
    idx = {e:k for k,e in enumerate(monos)}
    rows = []
    for i in range(r):
        e_i = [0]*r; e_i[i] = 1; e_i = tuple(e_i)
        for c in range(10):
            if c == 0:                       # d/dv_i[x_0] = s_i * per_3(Y)
                der = pmul({e_i:1}, per3(Y, r), r)
            else:                            # d/dv_i[y_ab] = s_i * X0 * per(minor)
                a, b = divmod(c-1, 3)
                sub = [[Y[p][q] for q in range(3) if q != b] for p in range(3) if p != a]
                pm = padd(pmul(sub[0][0], sub[1][1], r), pmul(sub[0][1], sub[1][0], r))
                der = pmul({e_i:1}, pmul(X0, pm, r), r)
            row = [0]*len(monos)
            for e,cc in der.items(): row[idx[e]] = (row[idx[e]]+cc) % P
            rows.append(row)
    return rank_mod(rows, len(monos))

if __name__ == "__main__":
    import jac
    print("n = 4 (ambient Sym^4 C^16).  Ideal at length r is EMPTY iff rank = target.")
    print("%3s %8s %10s %10s   %s" % ("r","target","det_4","per_3^pad","reading"))
    for r in (2,3,4,5):
        tgt = comb(r+3,4)
        d = max(jac.jac_rank(4, r, True, s) for s in (0,1)) if r <= 4 else None
        p = max(perpad_rank(r, s) for s in (0,1))
        ds = "%d"%d if d is not None else "  -"
        note = ""
        if d is not None:
            if d < tgt and p == tgt: note = "*** det ideal LIVE, per^pad ideal EMPTY ***"
            elif d == tgt and p == tgt: note = "both empty"
            else: note = "both live" if p < tgt else ""
        else:
            note = ("per^pad empty" if p == tgt else "per^pad live")
        print("%3d %8d %10s %10d   %s" % (r, tgt, ds, p, note))
