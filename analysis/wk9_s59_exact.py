#!/usr/bin/env python3
"""
Session 59 -- section 2A : the exact reducible-determinantal locus, as the
lower-bound anchor (KC2). M = s_5 A_5 + M_0(s'), M_0(s') = sum_{i=1}^4 s_i A_i
with A_i in a bounded-rank-<=3 space E (so det M_0(s') == 0), A_5 free. Then
det M is divisible by s_5, c = det M / s_5 in Sym^3 C^5, and dim{[c]} is the
exact interior of D_5 cap W (fixing l = s_5). s32 certified the maximum at 31
(over the c21/c32 compression strata). This must reproduce, or the higher-order
numbers are not trusted.
"""
import sys, random, argparse, json
sys.path.insert(0, 'analysis')
from wk9_s59_core import (R, n, NQ, NC, QIDX, Q2C, det_arc, pencils_to_entry,
                          rank_mod, quartic_vec, stratum_E_basis, STRATA)

P1, P2 = 2147483647, 2147483629

def c_vector(Ai, A5, p, dual=None):
    """A_i (i=1..4) list of 4x4 int mats ; A5 4x4 int. M(s)=s5 A5 + sum s_i A_i.
    return c = det M / s_5 as length-35 cubic vector (part = value or dual).
    dual = ('Ai', i, a, b) or ('A5', a, b) sets that entry's eps-part to 1."""
    # build pencil B_k[a][b], k=0..4 (s_1..s_5), and dual pencil
    B = [[[0]*n for _ in range(n)] for _ in range(R)]
    D = [[[0]*n for _ in range(n)] for _ in range(R)]
    for i in range(4):
        for a in range(n):
            for b in range(n):
                B[i][a][b] = Ai[i][a][b] % p
    for a in range(n):
        for b in range(n):
            B[4][a][b] = A5[a][b] % p
    if dual:
        if dual[0] == 'Ai':
            _, i, a, b = dual; D[i][a][b] = 1
        else:
            _, a, b = dual; D[4][a][b] = 1
    entry = pencils_to_entry([B], p, duals=[D])
    det = det_arc(entry, p, 0)
    sp = det.get(0, {})
    # divide by s_5 : each quartic exp with s5>=1 -> cubic; s5=0 part must vanish
    cval = [0]*NC; cdv = [0]*NC
    for e, cc in sp.items():
        i = QIDX[e]
        if e[4] == 0:
            # divisibility check : must be zero
            if cc[0] % p or cc[1] % p:
                return None, None
            continue
        j = Q2C[i]
        cval[j] = cc[0] % p; cdv[j] = cc[1] % p
    return cval, cdv

def A_in_E(Ebasis, coords, p):
    """A = sum_j coords[j] E_j."""
    A = [[0]*n for _ in range(n)]
    for j, Eb in enumerate(Ebasis):
        c = coords[j] % p
        for a in range(n):
            for b in range(n):
                if Eb[a][b]:
                    A[a][b] = (A[a][b] + c*Eb[a][b]) % p
    return A

def exact_dim(name, p, seed=3, lo=1, hi=None):
    rng = random.Random(seed)
    if hi is None: hi = p-1
    Eb = stratum_E_basis(name, rng, p); m = len(Eb)
    # A_1..A_4 : each a generic element of E (coords u[i][j])
    u = [[rng.randint(lo, hi) for _ in range(m)] for _ in range(4)]
    A5 = [[rng.randint(lo, hi) for _ in range(n)] for _ in range(n)]
    Ai = [A_in_E(Eb, u[i], p) for i in range(4)]
    # sanity : c well-defined (det divisible by s_5)
    v0, _ = c_vector(Ai, A5, p)
    if v0 is None:
        return dict(name=name, dimE=m, exact_dim=None, note="det not div by s5")
    # Jacobian columns : d c / d(param), param = A_i coords and A_5 entries.
    cols = []
    # A_i coords : perturb coord j of A_i -> perturbs A_i by E_j
    for i in range(4):
        for j in range(m):
            # dual on A_i in direction E_j : realise by perturbing entries of A_i
            # by E_j. Build a one-off dual pencil.
            Ai2 = [row[:] for row in [r[:] for r in []]]  # placeholder
            # simplest: set dual entries = E_j pattern on slot i
            val, dv = c_vector_dirEi(Eb, Ai, A5, i, j, p)
            cols.append(dv)
    for a in range(n):
        for b in range(n):
            _, dv = c_vector(Ai, A5, p, dual=('A5', a, b))
            cols.append(dv)
    rk = rank_mod(cols, NC, p)
    return dict(name=name, dimE=m, exact_dim=rk)

def c_vector_dirEi(Ebasis, Ai, A5, i, j, p):
    """directional derivative of c wrt moving A_i along E_j (a full matrix dir)."""
    B = [[[0]*n for _ in range(n)] for _ in range(R)]
    D = [[[0]*n for _ in range(n)] for _ in range(R)]
    for ii in range(4):
        for a in range(n):
            for b in range(n):
                B[ii][a][b] = Ai[ii][a][b] % p
    for a in range(n):
        for b in range(n):
            B[4][a][b] = A5[a][b] % p
    Eb = Ebasis[j]
    for a in range(n):
        for b in range(n):
            if Eb[a][b]:
                D[i][a][b] = Eb[a][b] % p
    from wk9_s59_core import det_arc as _d
    entry = pencils_to_entry([B], p, duals=[D])
    det = _d(entry, p, 0)
    sp = det.get(0, {})
    cdv = [0]*NC
    for e, cc in sp.items():
        if e[4] == 0: continue
        cdv[Q2C[QIDX[e]]] = cc[1] % p
    return None, cdv

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--primes', default='both')
    ap.add_argument('--out', default='results/s59_exact.json')
    a = ap.parse_args()
    primes = [P1, P2] if a.primes == 'both' else [int(a.primes)]
    res = {}
    for p in primes:
        res[str(p)] = {}
        for name in STRATA:
            r = exact_dim(name, p)
            res[str(p)][name] = r
            print(f"[p={p}] {name:5s} dimE={r['dimE']:2d} exact_dim(c)={r['exact_dim']} "
                  f"(s32: ker/coker 29, c21/c32 31, prim<=27)", flush=True)
    json.dump(res, open(a.out, 'w'), indent=1)
    print("wrote", a.out)
