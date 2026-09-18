"""B22-01: typed eps_3-contraction patterns, an explicit spanning set of F^L_{-1} and F^L_{-2}.

Adapted coordinates (B18-02 par. 1): a = Y[0,0]; r_j = Y[0,1+j] (a B'-leg); c_i = Y[1+i,0] (an A'-leg);
block E_{ij} = Y[1+i,1+j] (A'-leg i, B'-leg j), E = S + K with S symmetric, K skew.  Under
L = {(diag(alpha,g), diag(beta, c g^T))} acting by Y -> A Y B every leg is a copy of std = C^3 under g.

A pattern types the 20 slots (4 columns x 5 positions) of D = Y_1 ^ ... ^ Y_5 by {a, r, c, S, K}
(legs 0, 1, 1, 2, 2) and partitions the 30 legs into ten triples contracted with eps_{ijk}.  Within a
column the K slots come first, then the non-K slots, in the order stored.  h(Y) = T_h(D, D, D, D), each
column the full antisymmetrisation of its typed slots (`typed_wedge`).

F_1^h(Z_1, Z_2, Z) := [u^11] h(Z_1, Z_2, Z + u nu_1, u nu_2, u nu_3)  (degree-11 patterns, K-counts 2,3,3,3)
top^h(Z_1, Z_2)     := [u^12] h(same tuple)                          (degree-12 patterns, K-counts 3,3,3,3)
Structured form (Claim S(iii), docs/b22_01_report.md sec. 2):
  column with K-count 3 at D_3  = Z_1^Z_2^nu_1^nu_2^nu_3  is  Omega  (x) beta_{t,t'}(Z_1, Z_2)
  column with K-count 2 at D_2' = Z_1^Z_2^Z^nu_2^nu_3     is  Omega' (x) gamma_{t1,t2,t3}(Z_1, Z_2, Z)
so F_1^h(p) = < Xi_h , gamma(p) (x) beta(p) (x) beta(p) (x) beta(p) >, Xi_h the ten eps contracted with the
constant Omega', Omega, Omega, Omega over the 22 K-legs (8 open legs); tops likewise with 6 open legs.
All arithmetic mod P = 524287 in int64 with a reduction after every product (overflow asserted)."""
import itertools, string
import numpy as np

P = 524287
INV2 = pow(2, P - 2, P)
LEGS = {'a': 0, 'r': 1, 'c': 1, 'S': 2, 'K': 2}
LET = string.ascii_letters
BATCH = 'Z'
assert LET.index(BATCH) >= 30

EPS = np.zeros((3, 3, 3), dtype=np.int64)
for (i, j, k), s in {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1, (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}.items():
    EPS[i, j, k] = s


def nu_matrices():
    """nu_k := A(e_k), (nu_k)_{1+i,1+j} = -eps_{ijk}; identical to analysis/b20_01_flag.nu_matrices."""
    out = []
    for k in range(3):
        m = np.zeros((4, 4), dtype=np.int64)
        m[1:, 1:] = -EPS[:, :, k]
        out.append(m % P)
    return out


NU = nu_matrices()


def comp(t, Y):
    """Typed component of a batch Y (N,4,4): a (N,), r (N,3) [B-leg], c (N,3) [A-leg], S/K (N,3,3) [A,B]."""
    Y = np.asarray(Y, dtype=np.int64) % P
    if t == 'a': return Y[:, 0, 0].copy()
    if t == 'r': return Y[:, 0, 1:].copy()
    if t == 'c': return Y[:, 1:, 0].copy()
    E = Y[:, 1:, 1:]; Et = np.swapaxes(E, 1, 2)
    if t == 'S': return ((E + Et) % P) * INV2 % P
    if t == 'K': return ((E - Et) % P) * INV2 % P
    raise ValueError(t)


def perm_sign(p):
    p = list(p); s = 1
    for i in range(len(p)):
        while p[i] != i:
            j = p[i]; p[i], p[j] = p[j], p[i]; s = -s
    return s


def outer(x, y):
    N = x.shape[0]
    r = (x.reshape(N, -1, 1) * y.reshape(N, 1, -1)) % P
    return r.reshape((N,) + x.shape[1:] + y.shape[1:])


def typed_wedge(types, vecs):
    """sum_{perm} sgn(perm) (x)_s comp_{types[s]}(vecs[perm[s]]) for batches vecs[i] (N,4,4); legs in slot order."""
    n = len(types); assert len(vecs) == n
    N = np.asarray(vecs[0]).shape[0]
    cache = {}
    for t in set(types):
        for i in range(n):
            cc = comp(t, vecs[i]); cache[(t, i)] = (cc, bool(cc.any()))
    shape = (N,) + tuple(3 for t in types for _ in range(LEGS[t]))
    out = np.zeros(shape, dtype=np.int64)
    for perm in itertools.permutations(range(n)):
        if not all(cache[(t, perm[s])][1] for s, t in enumerate(types)): continue
        term = np.ones((N,), dtype=np.int64)
        for s, t in enumerate(types): term = outer(term, cache[(t, perm[s])][0])
        out = (out + perm_sign(perm) * term) % P
    return out % P


LIMIT = (2 ** 63 - 1) // ((P - 1) ** 2)
MAXSIZE = 2 ** 23          # elements of one intermediate (64 MiB in int64): a guard for the 512 MiB cap


def mod_einsum(subs, *ops):
    """einsum mod P along numpy's greedy path; every pairwise step is exact in int64 (asserted)."""
    ins, out = subs.split('->'); ins = ins.split(',')
    assert len(ins) == len(ops)
    dummies = [np.broadcast_to(np.float64(1.0), np.shape(o)) for o in ops]
    path = np.einsum_path(subs, *dummies, optimize='greedy')[0][1:]
    cur = [(np.asarray(o, dtype=np.int64) % P, s) for o, s in zip(ops, ins)]
    for step in path:
        taken = [cur.pop(i) for i in sorted(step, reverse=True)]
        assert len(taken) <= 2, 'path step with more than two operands'
        rest = ''.join(s for _, s in cur) + out
        letters = ''.join(dict.fromkeys(''.join(s for _, s in taken)))
        keep = ''.join(ch for ch in letters if ch in rest)
        dims = {}
        for a, s in taken:
            for ch, d in zip(s, a.shape): dims[ch] = d
        summed = 1
        for ch in letters:
            if ch not in keep: summed *= dims[ch]
        assert summed <= LIMIT, ('int64 overflow risk', summed)
        size = 1
        for ch in keep: size *= dims[ch]
        assert size <= MAXSIZE, ('intermediate too large', size)
        r = np.einsum(','.join(s for _, s in taken) + '->' + keep, *[a for a, _ in taken])
        cur.append((r % P, keep))
    assert len(cur) == 1
    a, s = cur[0]
    if s != out: a = np.einsum(s + '->' + out, a)
    return a % P


# ------------------------------------------------------------------ patterns
BLOCKS11 = {(1, 4, 4, 0): 7, (2, 3, 3, 1): 31, (3, 2, 2, 2): 28, (4, 1, 1, 3): 4}   # arc_target sec. 5.1, #v = 11
BLOCKS12 = {(2, 3, 3, 0): 1, (3, 2, 2, 1): 2, (4, 1, 1, 2): 1}                    # arc_target sec. 5.1, #v = 12


def pattern_legs(kcounts, cols):
    """Leg list [(col, slot, type, side)], columns in order, K slots first, then cols[j] in order."""
    legs = []
    for j in range(4):
        slot = 0
        for _ in range(kcounts[j]):
            legs += [(j, slot, 'K', 'A'), (j, slot, 'K', 'B')]; slot += 1
        for t in cols[j]:
            if t in ('S', 'K'): legs += [(j, slot, t, 'A'), (j, slot, t, 'B')]
            elif t == 'r': legs.append((j, slot, 'r', 'B'))
            elif t == 'c': legs.append((j, slot, 'c', 'A'))
            slot += 1
    return legs


def random_pattern(rng, md, deg):
    na, nr, nc, nS = md
    items = ['a'] * na + ['r'] * nr + ['c'] * nc + ['S'] * nS
    rng.shuffle(items)
    if deg == 11:
        kc = [2, 3, 3, 3]; cols = [tuple(items[0:3]), tuple(items[3:5]), tuple(items[5:7]), tuple(items[7:9])]
    else:
        kc = [3, 3, 3, 3]; cols = [tuple(items[2 * j:2 * j + 2]) for j in range(4)]
    if any(col.count('a') > 1 for col in cols): return None
    legs = pattern_legs(kc, cols); assert len(legs) == 30
    perm = [int(x) for x in rng.permutation(30)]
    triples = [tuple(sorted(perm[3 * i:3 * i + 3])) for i in range(10)]
    for tr in triples:
        seen = set()
        for li in tr:
            col, slot, t, _ = legs[li]
            if t == 'S':
                if (col, slot) in seen: return None      # eps against a symmetric pair: zero
                seen.add((col, slot))
    return dict(deg=deg, md=list(md), kcounts=kc, cols=[list(c) for c in cols], triples=[list(t) for t in triples])


def split_letters(pat):
    legs = pattern_legs(pat['kcounts'], [tuple(c) for c in pat['cols']])
    kl, nl = [], []
    for j in range(4):
        kl.append(''.join(LET[i] for i, L in enumerate(legs) if L[0] == j and L[2] == 'K' and L[1] < pat['kcounts'][j]))
        nl.append(''.join(LET[i] for i, L in enumerate(legs) if L[0] == j and not (L[2] == 'K' and L[1] < pat['kcounts'][j])))
    return legs, kl, nl


_CONST = {}
def const_K_parts():
    """Omega (nu_1,nu_2,nu_3 into three K slots) and Omega' (nu_2,nu_3 into two K slots), antisymmetrised."""
    if not _CONST:
        nu = [n.reshape(1, 4, 4) for n in NU]
        _CONST[3] = typed_wedge(('K', 'K', 'K'), nu)[0]
        _CONST[2] = typed_wedge(('K', 'K'), nu[1:])[0]
    return _CONST


def xi_tensor(pat):
    """Xi_h: the ten eps contracted with the constant K parts; open legs = the non-K legs, column order."""
    legs, kl, nl = split_letters(pat)
    C = const_K_parts()
    ops, subs = [], []
    for j in range(4):
        ops.append(C[pat['kcounts'][j]]); subs.append(kl[j])
    for tr in pat['triples']:
        ops.append(EPS); subs.append(''.join(LET[i] for i in tr))
    return mod_einsum(','.join(subs) + '->' + ''.join(nl), *ops)


class PointSet:
    """Typed wedges of a batch of flag points (Z_1, Z_2, Z), cached by type tuple."""
    def __init__(self, Z1, Z2, Z):
        self.Z1, self.Z2, self.Z = [np.asarray(x, dtype=np.int64) % P for x in (Z1, Z2, Z)]
        self.N = self.Z1.shape[0]; self.cache = {}

    def beta(self, types):
        key = ('b',) + tuple(types)
        if key not in self.cache: self.cache[key] = typed_wedge(tuple(types), [self.Z1, self.Z2])
        return self.cache[key]

    def gamma(self, types):
        key = ('g',) + tuple(types)
        if key not in self.cache: self.cache[key] = typed_wedge(tuple(types), [self.Z1, self.Z2, self.Z])
        return self.cache[key]


def evaluate(pat, ps, xi=None):
    """F_1^h (degree 11) or top^h (degree 12) at every point of ps, structured route."""
    legs, kl, nl = split_letters(pat)
    if xi is None: xi = xi_tensor(pat)
    ops, subs = [xi], [''.join(nl)]
    for j in range(4):
        cols = pat['cols'][j]
        t = ps.gamma(cols) if (pat['deg'] == 11 and j == 0) else ps.beta(cols)
        ops.append(t); subs.append(BATCH + nl[j])
    return mod_einsum(','.join(subs) + '->' + BATCH, *ops)


def brute_value(pat, Y):
    """h(Y) at one full 5-tuple Y (5,4,4): full typed columns (all 120 permutations), full eps network."""
    legs, kl, nl = split_letters(pat)
    vecs = [np.asarray(Y[m], dtype=np.int64).reshape(1, 4, 4) % P for m in range(5)]
    ops, subs = [], []
    for j in range(4):
        types = ('K',) * pat['kcounts'][j] + tuple(pat['cols'][j])
        ops.append(typed_wedge(types, vecs)); subs.append(BATCH + kl[j] + nl[j])
    for tr in pat['triples']:
        ops.append(EPS); subs.append(''.join(LET[i] for i in tr))
    return int(mod_einsum(','.join(subs) + '->' + BATCH, *ops)[0])


def flag_tuple(Z1, Z2, Z, u):
    T = np.zeros((5, 4, 4), dtype=np.int64)
    T[0] = Z1 % P; T[1] = Z2 % P
    T[2] = (Z + u * NU[0]) % P; T[3] = (u * NU[1]) % P; T[4] = (u * NU[2]) % P
    return T


# ------------------------------------------------------------------ modular linear algebra (own code)
def inv_mod(x): return pow(int(x) % P, P - 2, P)


class Echelon:
    """Incremental reduced row space over F_P of vectors of fixed length."""
    def __init__(self, n):
        self.n = n; self.rows = []; self.piv = []

    def reduce(self, v):
        v = np.asarray(v, dtype=np.int64) % P
        for row, p in zip(self.rows, self.piv):
            if v[p]: v = (v - v[p] * row) % P
        return v

    def add(self, v):
        v = self.reduce(v)
        nz = np.nonzero(v)[0]
        if len(nz) == 0: return False
        p = int(nz[0]); v = (v * inv_mod(v[p])) % P
        for i in range(len(self.rows)):
            if self.rows[i][p]: self.rows[i] = (self.rows[i] - self.rows[i][p] * v) % P
        self.rows.append(v); self.piv.append(p)
        return True


def det_rows(M):
    """Determinant mod P by row elimination on Python ints (method 1)."""
    A = [[int(x) % P for x in r] for r in M]; n = len(A); det = 1
    for k in range(n):
        p = next((i for i in range(k, n) if A[i][k]), None)
        if p is None: return 0
        if p != k: A[k], A[p] = A[p], A[k]; det = -det
        det = det * A[k][k] % P; iv = inv_mod(A[k][k])
        for i in range(k + 1, n):
            if A[i][k]:
                f = A[i][k] * iv % P; A[i] = [(x - f * y) % P for x, y in zip(A[i], A[k])]
    return det % P


def solve_mod(M, B):
    """X with M X = B mod P, M square invertible (numpy Gauss-Jordan)."""
    M = np.asarray(M, dtype=np.int64) % P; B = np.asarray(B, dtype=np.int64) % P
    n = M.shape[0]; A = np.concatenate([M, B.reshape(n, -1)], axis=1)
    for k in range(n):
        p = k + int(np.nonzero(A[k:, k])[0][0]); A[[k, p]] = A[[p, k]]
        A[k] = (A[k] * inv_mod(A[k, k])) % P
        f = A[:, k].copy(); f[k] = 0
        A = (A - np.outer(f, A[k]) % P) % P
    return A[:, n:]
