"""B21-01 isotropic-type utilities for the pairing B on Lambda^2 A (x) Lambda^2 B.

Setting (B20-01 section 4.5(c), C7 PROVED).  W = A (x) B = Mat_4, A = C e_0 (+) A', B = C f_0 (+) B'
with A' = <e_1, e_2, e_3>.  A half-tensor X_H is a 256-vector X[a1, a2, b1, b2]; only its
Lambda^2 A (x) Lambda^2 B part survives the pairing

    B(X, X') = sum eps_A[a1 a2 a3 a4] eps_B[b1 b2 b3 b4] X[a1,a2,b1,b2] X'[a3,a4,b3,b4].

Lambda^2 A = (e_0 ^ A') (+) Lambda^2 A'; write type 1 for the first summand, type 2 for the second.
The three A-pairs of type 1 are (0,1), (0,2), (0,3) and TYPE2[i] is the complement of TYPE1[i], so
every partition of {0,1,2,3} into two pairs has exactly one pair of each type: the wedge
Lambda^2 A x Lambda^2 A -> Lambda^4 A kills type1 x type1 and type2 x type2 and is nondegenerate
between them.  Hence the four-term type formula

    B(X, X') = <X_11, X'_22> + <X_12, X'_21> + <X_21, X'_12> + <X_22, X'_11>,

with X_{ta,tb} the 3x3 block of the Lambda-projection L(X) at A-type ta, B-type tb, and <,> the
sign-weighted Frobenius pairing built in `pair_blocks`.  `B_direct` evaluates the definition by
einsum; `B_types` evaluates the four-term formula; the pilot asserts they agree (the C7 replay).

All arithmetic mod P = 524287.  Producer-only (G18): nothing here is certified by a second lineage.
"""
import numpy as np

P = 524287
TYPE1 = [(0, 1), (0, 2), (0, 3)]
TYPE2 = [tuple(sorted(set(range(4)) - set(p))) for p in TYPE1]      # (2,3), (1,3), (1,2)


def eps4_signed():
    """Levi-Civita on four indices with entries in {-1, 0, +1}."""
    E = np.zeros((4, 4, 4, 4), dtype=np.int64)
    import itertools
    for perm in itertools.permutations(range(4)):
        s = 1
        q = list(perm)
        for i in range(4):
            for j in range(i + 1, 4):
                if q[i] > q[j]: s = -s
        E[perm] = s
    return E
EPS = eps4_signed()

# sign of the partition {TYPE1[i], TYPE2[i]}: eps[p0, p1, pbar0, pbar1]; independent of which half
# is written first, because moving a block of two indices past another block of two is even.
SGN = np.array([int(EPS[TYPE1[i] + TYPE2[i]]) for i in range(3)], dtype=np.int64)


def lam(X):
    """Lambda-projection of a 256-vector: L[ta, i, tb, j] for A-type ta+1, A-pair index i, likewise B.

    L[(p0,p1),(q0,q1)] = X[p0,p1,q0,q1] - X[p1,p0,q0,q1] - X[p0,p1,q1,q0] + X[p1,p0,q1,q0].
    """
    x = (np.asarray(X, dtype=np.int64) % P).reshape(4, 4, 4, 4)
    pairsA = [TYPE1, TYPE2]
    L = np.zeros((2, 3, 2, 3), dtype=np.int64)
    for ta in range(2):
        for i, (p0, p1) in enumerate(pairsA[ta]):
            for tb in range(2):
                for j, (q0, q1) in enumerate([TYPE1, TYPE2][tb]):
                    L[ta, i, tb, j] = (int(x[p0, p1, q0, q1]) - int(x[p1, p0, q0, q1])
                                       - int(x[p0, p1, q1, q0]) + int(x[p1, p0, q1, q0])) % P
    return L


def pair_blocks(Lblk, Mblk):
    """<Lblk, Mblk> = sum_{i,j} SGN[i] SGN[j] Lblk[i,j] Mblk[i,j] mod P, on 3x3 type blocks."""
    s = 0
    for i in range(3):
        for j in range(3):
            s += int(SGN[i]) * int(SGN[j]) * int(Lblk[i, j]) * int(Mblk[i, j])
    return s % P


def B_types(LX, LY):
    """The four type contributions of B(X, Y) and their sum, from the Lambda-projections.

    Returns (total, {'11x22': ..., '12x21': ..., '21x12': ..., '22x11': ...}); the key `ta tb x ta' tb'`
    pairs X's (ta, tb) block against Y's (ta', tb') block.
    """
    parts = {}
    for (ta, tb) in ((0, 0), (0, 1), (1, 0), (1, 1)):
        ua, ub = 1 - ta, 1 - tb
        key = '%d%dx%d%d' % (ta + 1, tb + 1, ua + 1, ub + 1)
        parts[key] = pair_blocks(LX[ta, :, tb, :], LY[ua, :, ub, :])
    return sum(parts.values()) % P, parts


def B_direct(X, Y):
    """The definition, by einsum; |terms| <= 576 P^2 < 2^63 so int64 is exact before reduction."""
    x = (np.asarray(X, dtype=np.int64) % P).reshape(4, 4, 4, 4)
    y = (np.asarray(Y, dtype=np.int64) % P).reshape(4, 4, 4, 4)
    return int(np.einsum('ijkl,mnop,ijmn,klop->', EPS, EPS, x, y, optimize=True)) % P


def balanced_float(T):
    """Balanced residues of a mod-P tensor as float64: |x| <= P/2 < 2.7e5."""
    r = np.mod(np.asarray(T, dtype=np.int64), P)
    r = np.where(r > P // 2, r - P, r)
    return r.astype(np.float64)


def col_arr(T):
    """A column tensor D of shape (16,)*5 as a balanced float64 array of shape (4,4)*5.

    The 16-index of each wedge slot splits as (a-leg, b-leg), which is the layout `column_labels`
    names; without this reshape the ten labels do not match the five axes.
    """
    return balanced_float(T).reshape((4, 4) * 5)


def column_labels(j):
    lab = []
    for k in range(5): lab += [('a', (j, k)), ('b', (j, k))]
    return lab


def half_tensor(arrF, EPSF, H):
    """X_H[a_x5, a_y5, b_x5', b_y5'] as a 256-vector mod P, from the balanced-float column tensor.

    H = dict(pi=[blkA, blkB], rho=[blkA, blkB], pi_free=(x5, y5), rho_free=(x5p, y5p)), slots (col, pos).
    Every tensordot sums at most 4^8 products of magnitude < (P/2)^2, and 4^8 (P/2)^2 < 2^53, so the
    float64 partial sums are exact; residues are re-balanced after each step.
    """
    cols = sorted({s[0] for blk in H['pi'] + H['rho'] for s in blk}
                  | {s[0] for s in H['pi_free']} | {s[0] for s in H['rho_free']})
    assert len(cols) == 2, cols
    X, Y = cols
    peak = [0]

    def contract(t1, l1, t2, l2):
        shared = [x for x in l1 if x in set(l2)]
        assert len(shared) <= 8, shared
        ax1 = [l1.index(x) for x in shared]; ax2 = [l2.index(x) for x in shared]
        res = np.tensordot(t1, t2, axes=(ax1, ax2))
        r = np.mod(res, P); res = np.where(r > P // 2, r - P, r)
        peak[0] = max(peak[0], res.size)
        return res, [x for x in l1 if x not in shared] + [x for x in l2 if x not in shared]

    cur = (arrF, column_labels(X))
    for blk in H['pi']: cur = contract(cur[0], cur[1], EPSF, [('a', s) for s in blk])
    for blk in H['rho']: cur = contract(cur[0], cur[1], EPSF, [('b', s) for s in blk])
    cur = contract(cur[0], cur[1], arrF, column_labels(Y))
    val, lab = cur
    val = np.mod(np.rint(val), P).astype(np.int64)
    want = [('a', H['pi_free'][0]), ('a', H['pi_free'][1]), ('b', H['rho_free'][0]), ('b', H['rho_free'][1])]
    assert sorted(lab) == sorted(want), (lab, want)
    return np.transpose(val, [lab.index(w) for w in want]).reshape(256) % P, peak[0]


def halves(pi, rho, pairing):
    """The four two-column half structures h1, h1t, h2, h2t of a paired pattern (direct_arc B.1)."""
    out = {}
    for h, (X, Y) in enumerate(pairing):
        for blk in pi[2 * h:2 * h + 2] + rho[2 * h:2 * h + 2]:
            assert {s[0] for s in blk} == {X, Y}, (blk, X, Y)
        pf = (pi[4][2 * h], pi[4][2 * h + 1]); rf = (rho[4][2 * h], rho[4][2 * h + 1])
        assert {pf[0][0], pf[1][0]} == {X, Y} and {rf[0][0], rf[1][0]} == {X, Y}
        out['h%d' % (h + 1)] = dict(pi=pi[2 * h:2 * h + 2], rho=rho[2 * h:2 * h + 2], pi_free=pf, rho_free=rf)
        out['h%dt' % (h + 1)] = dict(pi=rho[2 * h:2 * h + 2], rho=pi[2 * h:2 * h + 2], pi_free=rf, rho_free=pf)
    return out


def inv_mod(x): return pow(int(x) % P, P - 2, P)


def vander_solve_vec(nodes, degrees, vecs):
    """c_d with vecs[i] = sum_d nodes[i]^d c_d mod P, for integer vectors; Gauss-Jordan mod P."""
    n = len(nodes); assert n == len(degrees) == len(vecs)
    A = [[pow(int(t), d, P) for d in degrees] for t in nodes]
    R = [np.asarray(v, dtype=np.int64) % P for v in vecs]
    for col in range(n):
        p = next((i for i in range(col, n) if A[i][col]), None); assert p is not None, (nodes, degrees)
        A[col], A[p] = A[p], A[col]; R[col], R[p] = R[p], R[col]
        iv = inv_mod(A[col][col])
        A[col] = [(x * iv) % P for x in A[col]]; R[col] = (R[col] * iv) % P
        for i in range(n):
            if i != col and A[i][col]:
                f = A[i][col]
                A[i] = [(x - f * y) % P for x, y in zip(A[i], A[col])]
                R[i] = (R[i] - f * R[col]) % P
    return {d: R[i] for i, d in enumerate(degrees)}
