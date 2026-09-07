"""Session 62 — the block Gram matrix on highest-weight vectors, for general n.

    G_lambda = V^T B_lambda V,      mult_det(lambda, delta) = rank_Q G_lambda,

with V the (n_lambda x a) matrix of highest-weight coordinates in the orbit-sum
basis of H^{S_lambda} and B_lambda the Gram matrix of beta = K∘K on the
S_lambda-orbit sums,

    B_lambda(O, O') = beta(m_O, m_O') = |O'| * sum_{pi in O} beta(pi, pi'_0)
                    = |O'| * sum_d N_d(O, O') * K_d^2,

N_d(O, O') = #{pi in O : rel(pi, pi'_0) = d} the block-intersection counts
(the pair-orbital data), K_d the signed kernel on the orbital d.

Provenance.  The orbital constancy of K and beta, the sign formula and
beta = K∘K = Gram of Theta^+ are session 56's (analysis/wk9_s56_hecke.py,
analysis/wk9_s56_core.py).  What is new here is the lift to the a x a block on
the highest-weight vectors and the room-one Schur complement, plus a general-n
enumeration of the Foulkes module and of the orbitals.

Conventions.  Highest-weight vectors are computed on the GL side in the
programme's coordinates (wk8_s30_core.build_R: c_alpha = e^alpha / alpha!,
E_ij c_alpha = (alpha_i + 1) c_{alpha + e_i - e_j}) and carried to the
orbit-sum basis of H^{S_lambda} by the equivariant identification

    prod_j c_{alpha_j}  <->  (prod_k mult_k! / |W|) * M_O,   M_O = sum_{x in O} e_x,

so that v_O = h_O * prod_k mult_k(O)!, mult_k the multiplicities of the repeated
exponent vectors in the monomial O (derivation in docs/s62_report.md §1).  The
global 1/|W| is dropped.  Everything is exact: Python ints, flint fmpz/fmpq.
"""
import itertools
import os
import sys
import time
from fractions import Fraction
from functools import lru_cache
from math import factorial, comb

import numpy as np
import flint

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "tools", "verify"))
from wk8_s30_core import exps, monomials, build_R, P1, P2      # noqa: E402
import wk9_s56_core as C56                                      # noqa: E402

T0 = time.time()


def log(*a):
    print(f"[{time.time()-T0:8.1f}s]", *a, flush=True)


# ------------------------------------------------------------- the Foulkes module
def enum_H(n, delta):
    """All decompositions of range(N), N = n*delta, into delta blocks of size n.
    Returns labels (|H| x N, int8): labels[i, p] = index of the block of position p,
    blocks numbered in order of their smallest element (the canonical order of
    wk9_s56_core.canonical_partition)."""
    N = n * delta
    lab = np.full((1, N), -1, dtype=np.int8)
    for k in range(delta):
        rows = lab.shape[0]
        # unassigned positions, ascending, per row (nonzero is row-major)
        unassigned = np.nonzero(lab == -1)[1].reshape(rows, N - n * k)
        first = unassigned[:, 0]
        rest = unassigned[:, 1:]                       # rows x (N - n k - 1)
        combos = np.array(list(itertools.combinations(range(rest.shape[1]), n - 1)), dtype=np.int64)
        if combos.size == 0:
            combos = np.zeros((1, 0), dtype=np.int64)
        nc = combos.shape[0]
        new = np.repeat(lab, nc, axis=0)
        first_r = np.repeat(first, nc)
        chosen = rest[:, combos]                       # rows x nc x (n-1)
        chosen = chosen.reshape(rows * nc, n - 1)
        ar = np.arange(rows * nc)
        new[ar, first_r] = k
        for t in range(n - 1):
            new[ar, chosen[:, t]] = k
        lab = new
    assert not (lab == -1).any()
    expected = factorial(N) // (factorial(n) ** delta * factorial(delta))
    assert lab.shape[0] == expected, (lab.shape[0], expected)
    return lab


def standard_labels(n, delta):
    return np.repeat(np.arange(delta, dtype=np.int8), n)


# ------------------------------------------------------------------- orbitals
def margin_matrices(n, delta):
    """All delta x delta nonnegative integer matrices with every row and column sum n."""
    rows = [c for c in itertools.product(range(n + 1), repeat=delta) if sum(c) == n]
    out = []

    def rec(i, colsum, acc):
        if i == delta:
            if all(c == n for c in colsum):
                out.append(tuple(acc))
            return
        remaining = delta - i
        for r in rows:
            nc = tuple(colsum[j] + r[j] for j in range(delta))
            if any(x > n for x in nc):
                continue
            if sum(n - x for x in nc) != n * (remaining - 1):
                continue
            acc.append(r)
            rec(i + 1, nc, acc)
            acc.pop()

    rec(0, (0,) * delta, [])
    return out


def canonical_matrix(M):
    """canonical form under independent row and column permutations."""
    delta = len(M)
    best = None
    for cp in itertools.permutations(range(delta)):
        key = tuple(sorted(tuple(row[c] for c in cp) for row in M))
        if best is None or key < best:
            best = key
    return best


class Orbitals:
    """The double cosets W\\S_N/W (pair-orbitals of S_N on H x H) for (n, delta), with a
    lookup from the labelled intersection-matrix code to the orbital index and the
    signed kernel value K_d on each orbital."""

    def __init__(self, n, delta, verbose=True):
        self.n, self.delta = n, delta
        N = n * delta
        self.N = N
        t = time.time()
        labelled = margin_matrices(n, delta)
        canon = {}
        for M in labelled:
            canon[M] = canonical_matrix(M)
        keys = sorted(set(canon.values()))
        self.keys = keys
        self.index = {k: i for i, k in enumerate(keys)}
        self.n_orb = len(keys)
        base = n + 1
        assert base ** (delta * delta) < 2 ** 62, "code base too large for int64"
        self.pw = np.array([base ** (delta * j + b) for j in range(delta) for b in range(delta)], dtype=np.int64)
        codes = np.array([sum(M[j][b] * base ** (delta * j + b) for j in range(delta) for b in range(delta))
                          for M in labelled], dtype=np.int64)
        ids = np.array([self.index[canon[M]] for M in labelled], dtype=np.int64)
        order = np.argsort(codes)
        self.codes_sorted = codes[order]
        self.ids_sorted = ids[order]
        self.n_labelled = len(labelled)
        if verbose:
            log(f"orbitals n={n} delta={delta}: {self.n_labelled} labelled margin-{n} matrices, {self.n_orb} orbitals ({time.time()-t:.1f}s)")
        # representatives and K_d
        self.K = [None] * self.n_orb
        self.rep_labels = [None] * self.n_orb
        std = standard_labels(n, delta)
        for d, key in enumerate(keys):
            lab = self.partition_from_matrix(key)
            self.rep_labels[d] = lab
            # check the orbital of (standard, lab) is d
            code = self.codes_of(lab[None, :], std)
            dd = self.lookup(code)[0]
            assert dd == d, (d, dd)
            self.K[d] = kernel_general(std, lab, n)
        self.beta = [k * k for k in self.K]
        if verbose:
            log(f"K_d computed for {self.n_orb} orbitals; |K_d| values {sorted(set(abs(k) for k in self.K))}")

    def partition_from_matrix(self, M):
        """a decomposition pi (labels) with intersection matrix M against the standard
        decomposition: M[j][b] elements of standard block b go to block j."""
        n, delta = self.n, self.delta
        lab = np.full(self.N, -1, dtype=np.int8)
        for b in range(delta):
            pos = list(range(n * b, n * b + n))
            k = 0
            for j in range(delta):
                for _ in range(M[j][b]):
                    lab[pos[k]] = j
                    k += 1
            assert k == n
        # renumber blocks by smallest element
        order = {}
        new = np.zeros_like(lab)
        for p in range(self.N):
            j = int(lab[p])
            if j not in order:
                order[j] = len(order)
            new[p] = order[j]
        return new

    def codes_of(self, labels, ref_labels):
        """intersection-matrix codes of every row of `labels` (rows x N) against the fixed
        decomposition ref_labels (N,): M[j][b] = #{p : labels[p] = j, ref[p] = b}."""
        n, delta = self.n, self.delta
        rows = labels.shape[0]
        code = np.zeros(rows, dtype=np.int64)
        for b in range(delta):
            pos = np.nonzero(ref_labels == b)[0]
            sub = labels[:, pos]                           # rows x n
            for j in range(delta):
                cnt = (sub == j).sum(axis=1).astype(np.int64)
                code += cnt * self.pw[delta * j + b]
        return code

    def lookup(self, code):
        pos = np.searchsorted(self.codes_sorted, code)
        assert pos.max(initial=0) < len(self.codes_sorted)
        assert np.all(self.codes_sorted[pos] == code), "intersection matrix not a margin matrix"
        return self.ids_sorted[pos]


def kernel_general(lab1, lab2, n):
    """K(pi1, pi2) = sum_x eps_pi1(x) eps_pi2(x) over x in [n]^N, x running over the
    (n!)^delta support of eps_pi1 (transparent tensor sum, vectorised)."""
    N = len(lab1)
    delta = N // n
    perms = list(itertools.permutations(range(n)))
    sg = np.array([C56_sign(p) for p in perms], dtype=np.int64)
    P = np.array(perms, dtype=np.int8)
    X = P
    S = sg.copy()
    for _ in range(delta - 1):
        X = np.concatenate([np.repeat(X, len(perms), axis=0), np.tile(P, (X.shape[0], 1))], axis=1)
        S = np.repeat(S, len(perms)) * np.tile(sg, S.shape[0])
    # X columns are ordered block by block of pi1: block j occupies columns n*j .. n*j+n-1;
    # map them to positions
    blocks1 = [np.nonzero(lab1 == j)[0] for j in range(delta)]
    Xpos = np.zeros((X.shape[0], N), dtype=np.int8)
    for j in range(delta):
        Xpos[:, blocks1[j]] = X[:, n * j: n * j + n]
    tot = S.copy()
    # sign table for n-tuples with values 0..n-1
    base = n
    table = np.zeros(base ** n, dtype=np.int64)
    for p in perms:
        c = 0
        for v in p:
            c = c * base + int(v)
        table[c] = C56_sign(p)
    for j in range(delta):
        pos = np.nonzero(lab2 == j)[0]
        c = np.zeros(X.shape[0], dtype=np.int64)
        for p in pos:
            c = c * base + Xpos[:, p].astype(np.int64)
        tot *= table[c]
    return int(tot.sum())


def C56_sign(vals):
    if len(set(vals)) < len(vals):
        return 0
    s = 1
    v = list(vals)
    for i in range(len(v)):
        for j in range(i + 1, len(v)):
            if v[i] > v[j]:
                s = -s
    return s


# --------------------------------------------------------------- weight orbits
def colouring(lam, N):
    col = np.zeros(N, dtype=np.int64)
    p = 0
    for c, m in enumerate(lam):
        col[p:p + m] = c
        p += m
    assert p == N
    return col


def weight_orbits(labels, lam, n, r):
    """S_lambda-orbits of H under the standard colouring by lam (r colours).
    Returns dict(orbit_id (|H|,), monos: list of monomials as sorted tuples of exps-indices,
    size (n_lam,), rep (n_lam,) index of a representative decomposition)."""
    N = labels.shape[1]
    delta = N // n
    lam = tuple(lam) + (0,) * (r - len(lam))
    col = colouring(lam, N)
    A = exps(n, r)
    aidx = {a: k for k, a in enumerate(A)}
    L = len(A)
    nH = labels.shape[0]
    # content code of each block: for block j, count colours
    onehot = np.zeros((nH, delta, r), dtype=np.int16)
    for c in range(r):
        pos = np.nonzero(col == c)[0]
        sub = labels[:, pos]                              # nH x lam_c
        for j in range(delta):
            onehot[:, j, c] = (sub == j).sum(axis=1)
    # encode content vector -> exps index
    pw = np.array([(n + 1) ** c for c in range(r)], dtype=np.int64)
    ccode = (onehot.astype(np.int64) * pw[None, None, :]).sum(axis=2)     # nH x delta
    code_to_idx = {sum(a[c] * (n + 1) ** c for c in range(r)): k for a, k in aidx.items()}
    lut_keys = np.array(sorted(code_to_idx), dtype=np.int64)
    lut_vals = np.array([code_to_idx[k] for k in lut_keys], dtype=np.int64)
    pos = np.searchsorted(lut_keys, ccode)
    assert np.all(lut_keys[pos] == ccode)
    eidx = lut_vals[pos]                                                    # nH x delta, exps indices
    eidx.sort(axis=1)
    # multiset code
    mpw = np.array([L ** k for k in range(delta)], dtype=np.int64)
    assert L ** delta < 2 ** 62
    mcode = (eidx.astype(np.int64) * mpw[None, :]).sum(axis=1)
    uniq, inv, counts = np.unique(mcode, return_inverse=True, return_counts=True)
    # canonical monomial list from the GL side, matched to the orbit codes
    monos = list(monomials(n, r, delta, lam))
    mono_codes = np.array([sum(m[k] * L ** k for k in range(delta)) for m in monos], dtype=np.int64)
    order = np.argsort(mono_codes)
    assert np.array_equal(mono_codes[order], uniq), "S_lambda-orbits do not match the weight-lambda monomials"
    # orbit id in the order of `monos`: inv[i] is the position of pi_i's code in the
    # sorted list `uniq`, and order[k] is the mono index whose code sits at position k
    orbit_id = order[inv]
    size = np.zeros(len(monos), dtype=np.int64)
    size[order] = counts
    rep = np.full(len(monos), -1, dtype=np.int64)
    first = np.unique(inv, return_index=True)[1]     # first occurrence of every sorted code
    rep[order] = first
    # consistency: the representative of orbit m has monomial m
    chk = np.random.default_rng(1).choice(len(monos), size=min(20, len(monos)), replace=False)
    for m in chk:
        assert int(orbit_id[rep[m]]) == int(m)
        assert tuple(sorted(eidx[rep[m]].tolist())) == tuple(monos[m])
    assert (rep >= 0).all()
    return dict(orbit_id=orbit_id, monos=monos, size=size, rep=rep, n_lam=len(monos), lam=lam)


def orbit_multiplicity_factor(mono):
    """prod over distinct exponent vectors of (multiplicity)!"""
    f = 1
    for k in set(mono):
        f *= factorial(mono.count(k))
    return f


# ------------------------------------------------------ pair-orbital counts
def pair_counts(labels, orb, orbitals, verbose=True, tag=""):
    """N[O, O', d] = #{pi in O : rel(pi, rep(O')) = d}  as an int32 array
    (n_lam x n_lam x n_orb), by one pass over H per orbit representative."""
    n_lam = orb["n_lam"]
    n_orb = orbitals.n_orb
    Ncount = np.zeros((n_lam, n_lam, n_orb), dtype=np.int32)
    oid = orb["orbit_id"].astype(np.int64)
    t = time.time()
    per = []
    for c in range(n_lam):
        t1 = time.time()
        ref = labels[orb["rep"][c]]
        code = orbitals.codes_of(labels, ref)
        d = orbitals.lookup(code)
        h = np.bincount(oid * n_orb + d, minlength=n_lam * n_orb)
        Ncount[:, c, :] = h.reshape(n_lam, n_orb)
        per.append(time.time() - t1)
        if verbose and (c % 50 == 0 or c == n_lam - 1):
            log(f"  {tag} pass {c+1}/{n_lam} ({per[-1]:.2f}s per rep)")
    # every pi of O appears exactly once per column
    assert np.array_equal(Ncount.sum(axis=2), np.repeat(orb["size"][:, None], n_lam, axis=1))
    return Ncount, dict(total_s=time.time() - t, per_rep_s=float(np.mean(per)), n_pass=n_lam, H=int(labels.shape[0]))


def B_from_counts(Ncount, size, beta):
    """B(O,O') = |O'| * sum_d N[O,O',d] beta_d, exact Python ints; asserts symmetry."""
    n_lam = Ncount.shape[0]
    n_orb = Ncount.shape[2]
    beta = [int(b) for b in beta]
    B = [[0] * n_lam for _ in range(n_lam)]
    for i in range(n_lam):
        for j in range(n_lam):
            row = Ncount[i, j]
            s = 0
            for d in range(n_orb):
                v = int(row[d])
                if v:
                    s += v * beta[d]
            B[i][j] = s * int(size[j])
    for i in range(n_lam):
        for j in range(i + 1, n_lam):
            assert B[i][j] == B[j][i], ("B not symmetric", i, j)
    return B


def n_touched(Ncount):
    """how many orbitals carry a nonzero count, per (O, O') pair: distribution stats."""
    nz = (Ncount > 0).sum(axis=2)
    return dict(mean=float(nz.mean()), max=int(nz.max()), min=int(nz.min()))


# ------------------------------------------------------ highest-weight vectors
def hwv_basis_Q(n, r, delta, lam):
    """Exact integer basis of the highest-weight space of weight lam in
    Sym^delta(Sym^n C^r) in the programme's c-monomial coordinates
    (rows of the returned list are vectors over the monomials of
    wk8_s30_core.monomials(n, r, delta, lam)); a = len(basis)."""
    lam = tuple(lam) + (0,) * (r - len(lam))
    basis, rows = build_R(n, r, delta, lam)
    nb = len(basis)
    if nb == 0:
        return basis, []
    if not rows:
        # no raising operator applies: everything is a highest-weight vector
        return basis, [[1 if i == j else 0 for i in range(nb)] for j in range(nb)]
    ent = [0] * (len(rows) * nb)
    for i, rw in enumerate(rows):
        for c, v in rw.items():
            ent[i * nb + c] = int(v)
    M = flint.fmpz_mat(len(rows), nb, ent)
    X, nul = M.nullspace()
    vecs = []
    for j in range(nul):
        v = [int(X[i, j]) for i in range(nb)]
        g = 0
        for x in v:
            g = gcd(g, abs(x))
        if g > 1:
            v = [x // g for x in v]
        vecs.append(v)
    # check E v = 0 exactly
    for v in vecs:
        for rw in rows:
            assert sum(int(c) * v[k] for k, c in rw.items()) == 0
    return basis, vecs


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def to_orbit_coords(monos, vecs):
    """v_O = h_O * prod mult_k(O)!  (the equivariant identification, global 1/|W| dropped)."""
    fac = [orbit_multiplicity_factor(m) for m in monos]
    return [[h * f for h, f in zip(v, fac)] for v in vecs]


def gram_block(V, B):
    """G = V^T B V with V a list of a integer vectors (length n_lam) and B an
    n_lam x n_lam list of Python ints.  Returns a list of lists (Python ints)."""
    a = len(V)
    n_lam = len(B)
    BV = []
    for v in V:
        BV.append([sum(B[i][k] * v[k] for k in range(n_lam) if v[k]) for i in range(n_lam)])
    G = [[sum(V[p][i] * BV[q][i] for i in range(n_lam) if V[p][i]) for q in range(a)] for p in range(a)]
    for p in range(a):
        for q in range(p + 1, a):
            assert G[p][q] == G[q][p]
    return G


def rank_Q(G):
    if not G:
        return 0
    m = len(G)
    k = len(G[0])
    return flint.fmpz_mat(m, k, [int(x) for row in G for x in row]).rank()


def rank_mod(G, p):
    if not G:
        return 0
    m = len(G)
    k = len(G[0])
    return flint.nmod_mat(m, k, [int(x) % p for row in G for x in row], p).rank()


def snf_diagonal(G):
    if not G:
        return []
    m = len(G)
    k = len(G[0])
    S = flint.fmpz_mat(m, k, [int(x) for row in G for x in row]).snf()
    return [int(S[i, i]) for i in range(min(m, k))]


# -------------------------------------------------------- ladder / transport
def transported_and_new(n, r, delta, lam, pred_basis, pred_vecs, basis, vecs):
    """Given the predecessor cell's HWVs (weight lam - n e_1, degree delta-1) and the
    cell's own HWV basis, return (T, new) with T the transported vectors u.h_i in the
    cell's monomial coordinates (u = c_{(n,0,..,0)}: append the exponent vector) and
    new = one vector of the cell's basis completing T to a basis (or None if a == a_pred).
    Exact over Q; asserts the transported vectors are independent and lie in the
    highest-weight space."""
    A = exps(n, r)
    u_idx = A.index((n,) + (0,) * (r - 1))
    pos = {m: i for i, m in enumerate(basis)}
    T = []
    for v in pred_vecs:
        w = [0] * len(basis)
        for k, m in enumerate(pred_basis):
            if v[k]:
                mm = tuple(sorted(m + (u_idx,)))
                w[pos[mm]] += v[k]
        T.append(w)
    nb = len(basis)
    # T subset of span(vecs): rank check
    a = len(vecs)
    if T:
        rT = rank_Q(T)
        assert rT == len(T), "transported vectors dependent"
        rTV = rank_Q(T + vecs)
        assert rTV == a, ("transported vectors not in the highest-weight space", rTV, a)
    if a == len(T):
        return T, None
    # pick a vector of vecs completing T
    for v in vecs:
        if rank_Q(T + [v]) == len(T) + 1:
            return T, v
    raise AssertionError("no completing vector")


def schur_complement(G_full_basis):
    """G given in a basis whose LAST vector is the new one: returns (det A, s, det G)
    as Fractions, with A the leading (a-1) x (a-1) block = B_{lambda,delta}|_{J(M_{delta-1})}
    (the CURRENT-degree Gram on the transported predecessor, NOT the predecessor's own
    Gram -- integrator note 1); s = c - b^T A^{-1} b = det G / det A, and s >= 0 with
    equality iff the new line's image lies in the transported image (integrator's
    distance form s = ||(I-P) T(v)||^2, cross-checked in schur_all_forms)."""
    a = len(G_full_basis)
    if a == 1:
        return Fraction(1), Fraction(G_full_basis[0][0]), Fraction(G_full_basis[0][0])
    A = flint.fmpq_mat(a - 1, a - 1, [int(G_full_basis[i][j]) for i in range(a - 1) for j in range(a - 1)])
    detA = A.det()
    assert detA != 0, "A singular: predecessor not full rank in this Gram"
    b = flint.fmpq_mat(a - 1, 1, [int(G_full_basis[i][a - 1]) for i in range(a - 1)])
    x = A.solve(b)
    bt_x = sum(Fraction(int(G_full_basis[i][a - 1])) * _to_frac(x[i, 0]) for i in range(a - 1))
    s = Fraction(int(G_full_basis[a - 1][a - 1])) - bt_x
    detG = flint.fmpz_mat(a, a, [int(x_) for row in G_full_basis for x_ in row]).det()
    assert _to_frac(detA) * s == Fraction(int(detG)), "det G != det A * s"
    return _to_frac(detA), s, Fraction(int(detG))


def schur_all_forms(G_full_basis):
    """Return s in the three coincident forms (integrator note 1) and assert they agree:
      s1 = c - b^T A^{-1} b        (the Schur complement)
      s2 = det B / det A           (B = full Gram, A = transported block)
      s3 = ||(I - P) T(v)||^2      (squared distance of the new image from the transported
                                    image, P the B-orthogonal projector onto J(M_{delta-1}))
    All exact rationals; s3 >= 0 makes s >= 0 manifest, = 0 iff dependence."""
    detA, s1, detG = schur_complement(G_full_basis)
    s2 = detG / detA
    a = len(G_full_basis)
    if a == 1:
        return {"s_schur": s1, "s_detB_over_detA": s2, "s_distance": s1,
                "agree": s1 == s2}
    A = flint.fmpq_mat(a - 1, a - 1, [int(G_full_basis[i][j]) for i in range(a - 1) for j in range(a - 1)])
    b = flint.fmpq_mat(a - 1, 1, [int(G_full_basis[i][a - 1]) for i in range(a - 1)])
    x = A.solve(b)                    # coordinates of the B-orthogonal projection of T(v) onto J(M)
    # ||(I-P)T(v)||^2 = <v,v>_B - x^T A x  (= c - b^T A^{-1} b since A x = b)
    xt_A_x = Fraction(0)
    Ax = A * x
    for i in range(a - 1):
        xt_A_x += _to_frac(x[i, 0]) * _to_frac(Ax[i, 0])
    s3 = Fraction(int(G_full_basis[a - 1][a - 1])) - xt_A_x
    agree = (s1 == s2 == s3)
    return {"s_schur": s1, "s_detB_over_detA": s2, "s_distance": s3, "agree": agree}


def detA_mod_p(G_full_basis, p):
    """det of the transported block A mod p -- the LOWER-BOUND (predecessor-full-rank)
    step is valid in every characteristic: det A != 0 mod p already proves det A != 0
    over Z, hence rank_Q A = a-1, hence rank_Q of the map on M_{delta-1} is a-1 = full
    (rank(M^T M) <= rank M in every characteristic; integrator note 2).  A claimed
    s = 0 (a rank drop) is NOT provable mod p and stays characteristic zero."""
    a = len(G_full_basis)
    if a == 1:
        return None
    Am = flint.nmod_mat(a - 1, a - 1, [int(G_full_basis[i][j]) % p for i in range(a - 1) for j in range(a - 1)], p)
    return int(Am.det())


def foulkes_support(size, support_orbit_indices):
    """|S| = the support of the highest-weight vectors in the FOULKES basis (block
    decompositions), = sum of orbit sizes over the monomials O the HWVs touch
    (integrator note 3: this is the number that decides the Gram-entry cost, not the
    weight-space support n_lam).  `size` the orbit sizes, `support_orbit_indices` the
    set of monomial indices with a nonzero HWV coordinate."""
    return int(sum(int(size[o]) for o in support_orbit_indices))


def gram_H(V, size):
    """N_lambda = V^T diag(size) V, the Gram of the HWV basis under the standard
    S_N-invariant inner product on H (<m_O, m_O'> = |O| delta_{OO'}); used for the
    centrality check (beta central on M_lambda iff G_lambda proportional to N_lambda)."""
    a = len(V)
    n_lam = len(size)
    N = [[0] * a for _ in range(a)]
    for p in range(a):
        for q in range(p, a):
            s = 0
            vp, vq = V[p], V[q]
            for i in range(n_lam):
                if vp[i] and vq[i]:
                    s += vp[i] * vq[i] * int(size[i])
            N[p][q] = N[q][p] = s
    return N


def proportional(G, Nmat):
    """are the two a x a integer symmetric matrices proportional over Q?  Returns
    (bool, ratio-or-None).  Used to test whether beta is scalar (central) on M_lambda:
    G_lambda = c * N_lambda for a scalar c iff beta acts as the scalar c there."""
    a = len(G)
    # find a nonzero entry of N to fix the ratio
    c = None
    for i in range(a):
        for j in range(a):
            if Nmat[i][j] != 0:
                c = Fraction(G[i][j], Nmat[i][j])
                break
        if c is not None:
            break
    if c is None:
        return False, None
    for i in range(a):
        for j in range(a):
            if Fraction(G[i][j]) != c * Nmat[i][j]:
                return False, c
    return True, c


def _to_frac(q):
    return Fraction(int(q.p), int(q.q))


def u_free_count(n, r, delta, lam):
    """dimension of the u-free part of the weight space: N_S(lam, delta) - N_S(lam - n e_1, delta - 1)."""
    lam = tuple(lam) + (0,) * (r - len(lam))
    NS = len(monomials(n, r, delta, lam))
    pred = (lam[0] - n,) + lam[1:]
    if pred[0] < pred[1] if r > 1 else pred[0] < 0:
        return NS, NS, 0
    NSp = len(monomials(n, r, delta - 1, pred)) if pred[0] >= 0 else 0
    return NS, NS - NSp, NSp
