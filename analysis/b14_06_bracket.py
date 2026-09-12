#!/usr/bin/env python3
"""
B14-06 -- stable BRACKET evaluator (slot 6), new code.

Shares no code with s69/s74/s79.  Those realise the highest-weight space as the
common kernel of the raising operators on an explicitly enumerated weight space;
at the LMR tail that space has 7.21e9 dimensions (docs/b14_claude_scratch_code.md)
and the route is not runnable at all.  This module writes down an explicit
SPANNING SET of the highest-weight space directly from the shape, and never
touches the weight space.  No raising operator, no u-tower, no transport
exponent, no weight-space enumeration appears anywhere below.

Setting (Proposition S, docs/s57_report.md sec.1), ell = 9:

    V' = C^8 with coordinates s_1..s_8            (the ambient s_2..s_9)
    Z  = Sym^2 V'^* + Sym^3 V'^* + Sym^4 V'^*
    C[Z] = Sym(Sym^2 V' + Sym^3 V' + Sym^4 V'),  letters Q_2,Q_3,Q_4 of valence 2,3,4

A tail lam_bar with conjugate (8,8,1^k) gives HWVs built from two height-8
eps-columns and k singletons -- no 2-column, no u-tower.  Because every letter is
symmetric it may place at most one slot in each eps, so a bracket depends on the
point only through, for d in {2,3,4},

    s_d    = f_d(e_1)                         (scalar)
    u_d[i] = d(f_d)(e_1)_i / d                (gradient / d)
    N_d[i][j] = dd(f_d)(e_1)_ij / (d(d-1))    (Hessian / d(d-1))

and a bracket is fixed by twelve integers (a_d,b_d,c_d,z_d): copies of Q_d in
eps_1 only / eps_2 only / both / neither, with a_d,b_d in {0,1}.

Evaluation is one determinant per (a,b) pattern:

    BigM(y) = [[ y_2 N_2 + y_3 N_3 + y_4 N_4 , W^T ],
               [ U                          , 0   ]]
    value   = c_2! c_3! c_4! * [y_2^c2 y_3^c3 y_4^c4] det BigM(y) * prod_d s_d^{z_d}

det BigM is homogeneous of degree m = col - |A| in y, so all coefficients for one
(a,b) pattern come from one interpolation.  The formula is DERIVED, and control
C2 checks it against a direct brute-force eps-eps contraction in a reduced
dimension, including inputs that must make the comparison fail.

Conventions banked with every stored matrix (values_are, beside the numbers).

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
"""
import itertools
import numpy as np
from flint import nmod_mat

P1, P2 = 2147483647, 2147483629
PRIMES = (P1, P2)
DEGS = (2, 3, 4)

CONVENTIONS = {
    "picture": "Proposition S stable picture; Z = Sym^2+Sym^3+Sym^4 of V'^*, V' = C^col",
    "letters": "Q_d in Sym^d V', T_d symmetric with f_d(s) = sum T_d[i_1..i_d] s_{i_1}..s_{i_d}",
    "reduced": "s_d = f_d(e_1); u_d[i] = T_d[i,1^(d-1)]; N_d[i][j] = T_d[i,j,1^(d-2)]",
    "bracket": "(a_d,b_d,c_d,z_d): copies of Q_d in eps1 only / eps2 only / both / neither",
    "shape": "lam_bar' = (col,col,1^k); two height-col eps columns and k singletons",
    "value": "c!.[y^c] det BigM(y) . prod s_d^{z_d}; see module docstring",
    "values_are": "exact residues mod p of the bracket values at the stored integer points; "
                  "no transform, no normalisation, no scaling applied",
    "independence": "no code, data structure or mechanism shared with s69/s74/s79",
}


# --------------------------------------------------------------- bracket index set
def enumerate_brackets(W, col=8, degs=DEGS, dedupe=True):
    """All (a,b,c,z) for a tail of size W with conjugate shape (col,col,1^{W-2col}).

    a_d,b_d in {0,1}: two copies of one letter in one eps repeat a row of an
    antisymmetric contraction, so the bracket is zero.  N_d is symmetric, so the
    eps1<->eps2 swap gives the same value up to sign; dedupe under (a,b)->(b,a).
    """
    nd = len(degs)
    out = []
    for a in itertools.product((0, 1), repeat=nd):
        for b in itertools.product((0, 1), repeat=nd):
            if sum(a) != sum(b):
                continue
            need = col - sum(a)
            if need < 0:
                continue
            for c in itertools.product(range(need + 1), repeat=nd):
                if sum(c) != need:
                    continue
                base = sum(d * (a[k] + b[k] + c[k]) for k, d in enumerate(degs))
                R = W - base
                if R < 0:
                    continue
                for z in itertools.product(range(R // min(degs) + 1), repeat=nd):
                    if sum(d * z[k] for k, d in enumerate(degs)) == R:
                        out.append((a, b, c, z))
    if not dedupe:
        return out
    seen, ded = set(), []
    for (a, b, c, z) in out:
        key = (min(a, b), max(a, b), c, z)
        if key in seen:
            continue
        seen.add(key)
        ded.append((a, b, c, z))
    return ded


# --------------------------------------------------------------- modular helpers
def inv_mod(x, p):
    return pow(int(x) % p, p - 2, p)


def _fl(mat, p):
    r = len(mat); c = len(mat[0]) if r else 0
    return nmod_mat(r, c, [int(v) % p for row in mat for v in row], p)


def det_mod(mat, p):
    return int(_fl(mat, p).det())


def rank_mod(mat, p):
    return int(_fl(mat, p).rank())


def _interp_setup(m, p, rng):
    """Nodes and inverse Vandermonde for a homogeneous degree-m form in 3 vars."""
    mons = [(i, j, m - i - j) for i in range(m + 1) for j in range(m + 1 - i)]
    K = len(mons)
    while True:
        nodes = [tuple(int(v) for v in rng.integers(1, p - 1, 3)) for _ in range(K)]
        V = [[pow(nd[0], e[0], p) * pow(nd[1], e[1], p) % p * pow(nd[2], e[2], p) % p
              for e in mons] for nd in nodes]
        M = _fl(V, p)
        if int(M.det()) % p:
            return mons, nodes, M.inv()


# --------------------------------------------------------------- the evaluator
class BracketEvaluator:
    """Evaluates a fixed bracket list at points given by reduced data (s,u,N)."""

    def __init__(self, brackets, col, p, seed=20260912):
        self.brackets = list(brackets)
        self.col = col
        self.p = p
        rng = np.random.default_rng(seed)
        self.patterns = {}          # (a,b) -> dict
        for (a, b, c, z) in self.brackets:
            self.patterns.setdefault((a, b), None)
        self._interp = {}
        for (a, b) in self.patterns:
            m = col - sum(a)
            if m not in self._interp:
                self._interp[m] = _interp_setup(m, p, rng)
            self.patterns[(a, b)] = {"m": m, "A": [k for k in range(len(DEGS)) if a[k]],
                                     "B": [k for k in range(len(DEGS)) if b[k]]}
        self.fact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320]

    def values(self, red):
        """red = {d: (s_d, u_d(list), N_d(list of lists))} as ints mod p."""
        p, col = self.p, self.col
        N = {d: red[d][2] for d in DEGS}
        u = {d: red[d][1] for d in DEGS}
        s = {d: red[d][0] % p for d in DEGS}
        coef = {}                                   # (a,b) -> {(c2,c3,c4): coefficient}
        for (a, b), info in self.patterns.items():
            m = info["m"]
            mons, nodes, Vinv = self._interp[m]
            nA = len(info["A"])
            size = col + nA
            vals = []
            for nd in nodes:
                M = [[0] * size for _ in range(size)]
                for i in range(col):
                    for j in range(col):
                        M[i][j] = (nd[0] * N[2][i][j] + nd[1] * N[3][i][j]
                                   + nd[2] * N[4][i][j]) % p
                for t, k in enumerate(info["B"]):    # W^T : right columns
                    for i in range(col):
                        M[i][col + t] = u[DEGS[k]][i] % p
                for t, k in enumerate(info["A"]):    # U : bottom rows
                    for j in range(col):
                        M[col + t][j] = u[DEGS[k]][j] % p
                vals.append(det_mod(M, p))
            hv = _fl([[v] for v in vals], p)
            hcoef = Vinv * hv
            coef[(a, b)] = {mons[t]: int(hcoef[t, 0]) for t in range(len(mons))}
        out = []
        for (a, b, c, z) in self.brackets:
            v = coef[(a, b)].get(tuple(c), 0)
            v = v * self.fact[c[0]] % p * self.fact[c[1]] % p * self.fact[c[2]] % p
            if sum(a) % 2:                      # Laplace sign, fixed per bracket;
                v = (-v) % p                    # control C2 pins it to (-1)^|A|
            for k, d in enumerate(DEGS):
                if z[k]:
                    v = v * pow(s[d], z[k], p) % p
            out.append(v % p)
        return out


def consistency_defect(red, col, p):
    """Euler's relations, which every genuine point of Z satisfies:

        u_d[0] = s_d,   N_d[i][0] = N_d[0][i] = u_d[i],   N_d[0][0] = s_d

    because the free slots of a bracket are contracted with e^1, so u_d and s_d
    are the 0-column and (0,0)-entry of N_d.  Applying Euler's identity to f_d and
    to d(f_d) gives exactly these.  Returns the number of violated relations --
    random independent (s,u,N) is NOT a point of Z, and reporting a rank on such
    data inflates it.  Found by control C4."""
    bad = 0
    for d in DEGS:
        s, u, N = red[d]
        if u[0] % p != s % p:
            bad += 1
        if N[0][0] % p != s % p:
            bad += 1
        for i in range(col):
            if N[i][0] % p != u[i] % p or N[0][i] % p != u[i] % p:
                bad += 1
    return bad


def random_point(col, p, rng):
    """A legitimate generic point of Z in reduced form: three free symmetric
    matrices N_d, with u_d and s_d read off as Euler requires.  The map
    Z -> (N_2,N_3,N_4) is surjective, so this is a generic point of Z."""
    red = {}
    for d in DEGS:
        N = rng.integers(0, p, (col, col))
        N = (N + N.T) % p
        Nl = [[int(N[i][j]) for j in range(col)] for i in range(col)]
        red[d] = (Nl[0][0], [Nl[i][0] for i in range(col)], Nl)
    return red


# --------------------------------------------------------------- brute force (control C2)
def brute_value(bracket, red, col, p):
    """Direct eps (x) eps contraction, straight from the definition.  Exponential
    in col: for the control only."""
    a, b, c, z = bracket
    eps1, eps2, pairs = [], [], []
    for k, d in enumerate(DEGS):
        if a[k]:
            eps1.append(("u", d))
    for k, d in enumerate(DEGS):
        if b[k]:
            eps2.append(("u", d))
    for k, d in enumerate(DEGS):
        for _ in range(c[k]):
            pairs.append(d)
    for d in pairs:
        eps1.append(("N", d)); eps2.append(("N", d))
    assert len(eps1) == col and len(eps2) == col, (len(eps1), len(eps2), col)
    nC = len(pairs)
    s = {d: red[d][0] % p for d in DEGS}
    u = {d: red[d][1] for d in DEGS}
    N = {d: red[d][2] for d in DEGS}

    def lc(perm):
        seen = set(); sign = 1
        arr = list(perm)
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] > arr[j]:
                    sign = -sign
        return sign

    total = 0
    for pi in itertools.permutations(range(col)):
        s1 = lc(pi)
        for pj in itertools.permutations(range(col)):
            s2 = lc(pj)
            t = s1 * s2
            term = 1
            for slot in range(col):
                kind, d = eps1[slot]
                if kind == "u":
                    term = term * u[d][pi[slot]] % p
            for slot in range(col):
                kind, d = eps2[slot]
                if kind == "u":
                    term = term * u[d][pj[slot]] % p
            base1 = col - nC
            for q in range(nC):
                d = pairs[q]
                term = term * N[d][pi[base1 + q]][pj[base1 + q]] % p
            total = (total + t * term) % p
    for k, d in enumerate(DEGS):
        if z[k]:
            total = total * pow(s[d], z[k], p) % p
    return total % p


# --------------------------------------------------------------- 2-jets in F_p[eta]/(deg 3)
class Jet:
    """Truncated arithmetic in F_p[eta_0..eta_{n-1}] / (eta-degree >= 3), vectorised
    over a batch of points with numpy int64 (p < 2^31 so a*b < 2^62)."""

    def __init__(self, n, p, npts):
        self.n = n; self.p = p; self.npts = npts
        self.pairs = [(i, j) for i in range(n) for j in range(i, n)]
        self.pix = {ij: k for k, ij in enumerate(self.pairs)}
        self.dim = 1 + n + len(self.pairs)

    def zero(self):
        return np.zeros((self.dim, self.npts), dtype=np.int64)

    def const(self, v):
        z = self.zero(); z[0] = np.asarray(v, dtype=np.int64) % self.p; return z

    def mul(self, x, y):
        p, n = self.p, self.n
        out = self.zero()
        out[0] = x[0] * y[0] % p
        for i in range(n):
            out[1 + i] = (x[0] * y[1 + i] + x[1 + i] * y[0]) % p
        for k, (i, j) in enumerate(self.pairs):
            t = x[0] * y[1 + n + k] % p + x[1 + n + k] * y[0] % p
            if i == j:
                t += x[1 + i] * y[1 + i] % p
            else:
                t += x[1 + i] * y[1 + j] % p + x[1 + j] * y[1 + i] % p
            out[1 + n + k] = t % p
        return out

    def add(self, x, y):
        return (x + y) % self.p

    def scal(self, x, k):
        return x * (int(k) % self.p) % self.p

    def reduced(self, jet, d):
        """(s_d, u_d, N_d) from the 2-jet of a degree-d form at e_1, per point."""
        p, n = self.p, self.n
        s = jet[0] % p
        gi = jet[1:1 + n] % p
        H = np.zeros((n, n, self.npts), dtype=np.int64)
        for k, (i, j) in enumerate(self.pairs):
            v = jet[1 + n + k] % p
            if i == j:
                H[i, i] = 2 * v % p
            else:
                H[i, j] = v; H[j, i] = v
        iu = inv_mod(d, p); iN = inv_mod(d * (d - 1), p)
        return s, gi * iu % p, H * iN % p


def jet_point_list(jetalg, jets_by_d):
    """Turn batched jets into a list of per-point reduced dicts."""
    npts = jetalg.npts
    red = [dict() for _ in range(npts)]
    for d, jet in jets_by_d.items():
        s, u, N = jetalg.reduced(jet, d)
        for t in range(npts):
            red[t][d] = (int(s[t]), [int(v) for v in u[:, t]],
                         [[int(N[i, j, t]) for j in range(jetalg.n)] for i in range(jetalg.n)])
    return red
