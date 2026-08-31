"""Session 23(a), step 1: dim of the bidegree-(m,m) simultaneous-conjugation
invariants of a pencil of 3x3 matrices, by an SL_3 character computation.
Weights of gl_3 are e_i - e_j; the torus is coordinatised by (x,y) with
t_1 = x, t_2 = y, t_3 = 1/(xy).  Exact integer arithmetic (Laurent polynomials
as dicts).  m = 2 must return 9 (session 22)."""
from fractions import Fraction

W3 = [(1,0), (0,1), (-1,-1)]
def sub(u, v): return (u[0]-v[0], u[1]-v[1])
GL3 = [sub(u, v) for u in W3 for v in W3]           # 9 weights of gl_3
ROOTS = [sub(u, v) for u in W3 for v in W3 if u != v]

def mul(p, q):
    r = {}
    for k1, v1 in p.items():
        for k2, v2 in q.items():
            k = (k1[0]+k2[0], k1[1]+k2[1]); r[k] = r.get(k, 0) + v1*v2
    return {k: v for k, v in r.items() if v}

def sym_power_char(weights, m):
    """character of Sym^m of a rep with the given multiset of weights."""
    cur = {(0,0): 1}
    for w in weights:
        nxt = {}
        # allow multiplicity 0..m of this weight
        powers = [{(0,0): 1}]
        for k in range(1, m+1):
            powers.append({(w[0]*k, w[1]*k): 1})
        for k in range(m+1):
            for kk, vv in mul(cur, powers[k]).items():
                nxt[kk] = nxt.get(kk, 0) + vv
        # truncate by total Sym-degree: track degree separately instead
        cur = nxt
    return cur

def sym_char(weights, m):
    """Sym^m character, tracked with an explicit degree variable."""
    # state: dict (deg, wx, wy) -> coeff
    cur = {(0,0,0): 1}
    for w in weights:
        nxt = {}
        for (d, a, b), c in cur.items():
            for k in range(0, m-d+1):
                key = (d+k, a+w[0]*k, b+w[1]*k)
                nxt[key] = nxt.get(key, 0) + c
        cur = nxt
    return {(a,b): c for (d,a,b), c in cur.items() if d == m}

def trivial_mult(ch):
    weyl = {(0,0): 1}
    for a in ROOTS:
        weyl = mul(weyl, {(0,0): 1, a: -1})
    v = mul(ch, weyl).get((0,0), 0)
    assert v % 6 == 0, v
    return v // 6

if __name__ == '__main__':
    print(" m   dim Sym^m(gl3)   dim of bidegree-(m,m) conjugation invariants")
    for m in range(1, 8):
        ch = sym_char(GL3, m)
        d = sum(ch.values())
        U = mul(ch, ch)
        print(f" {m}   {d:>8}        {trivial_mult(U)}")
