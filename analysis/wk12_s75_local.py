#!/usr/bin/env python3
"""s75 -- local block-swap recoupling in the branching (path) basis, mod p.

The block swap of the last two 4-blocks A,B on Hom(W_rho, W_nu (x) A (x) B)
depends only on the skew shape rho/nu, so COLLAPSE empty rows and full columns to
a tiny shape (rho_c, nu_c) [|rho_c|<=16, N<=4 on the LMR ladder].  Realize

    W_{nu_c} (x) Sym^4 (x) Sym^4   inside   V^{|nu_c|} (x) Sym^4 (x) Sym^4,  V=C^N,

with the coefficient-free diagonal gl_N action (E_{ab}: e_b->e_a per tensor slot;
E_{ab} y^alpha = alpha_b y^{alpha-e_b+e_a} on a monomial).  Extract the weight-
rho_c highest-weight space (dim = #paths), split it into the intermediate-mu
branching basis by the quadratic (and, when it degenerates, cubic) Casimir of the
(W_nu,A) subsystem, and read off sigma = swap(A,B) in that basis.

All arithmetic is mod a house prime p (>96); the tower re-verifies a(rho) against
the char-0 engine a_weyl at every node, and both house primes agree.
"""
import sys, os
from itertools import permutations, product as iproduct
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from wk12_s75_recoup import horiz_strips_below, cells_of_skew, is_h4_below


def norm(t):
    t = tuple(t)
    while t and t[-1] == 0:
        t = t[:-1]
    return t


def perm_sign(p):
    p = list(p); s = 1; seen = [False] * len(p)
    for i in range(len(p)):
        if seen[i]:
            continue
        j = i; l = 0
        while not seen[j]:
            seen[j] = True; j = p[j]; l += 1
        if l % 2 == 0:
            s = -s
    return s


def collapse(rho, nu):
    """remove SPECTATOR ROWS (rho_i == nu_i) only -- a valid reduction of the
       recoupling (those rows are inert); keep all columns / full row lengths.
       Removing full columns is NOT valid (it shifts the strips relative to nu)."""
    r = len(rho); nuv = list(nu) + [0] * (r - len(nu))
    active_rows = [i for i in range(r) if rho[i] > nuv[i]]
    rho_c = norm([rho[i] for i in active_rows])
    nu_c = norm([nuv[i] for i in active_rows])
    return rho_c, nu_c, active_rows, None


def collapse_shape(mu, active_rows, active_cols, nu):
    muv = list(mu) + [0] * (max(active_rows) + 1 - len(mu))
    return norm([muv[i] for i in active_rows])


def comps(tot, N):
    if N == 1:
        yield (tot,); return
    for first in range(tot + 1):
        for rest in comps(tot - first, N - 1):
            yield (first,) + rest


def nullspace_modp(M, ncols, p):
    """right kernel of M (rows x ncols) over F_p; list of vectors length ncols."""
    A = [row[:] for row in M]; rows = len(A); piv = 0; pc = []
    for col in range(ncols):
        sel = None
        for rr in range(piv, rows):
            if A[rr][col] % p:
                sel = rr; break
        if sel is None:
            continue
        A[piv], A[sel] = A[sel], A[piv]
        inv = pow(A[piv][col] % p, p - 2, p)
        A[piv] = [(x * inv) % p for x in A[piv]]
        for rr in range(rows):
            if rr != piv and A[rr][col] % p:
                f = A[rr][col] % p
                A[rr] = [(A[rr][t] - f * A[piv][t]) % p for t in range(ncols)]
        pc.append(col); piv += 1
    free = [c for c in range(ncols) if c not in pc]
    out = []
    for fc in free:
        v = [0] * ncols; v[fc] = 1
        for ri, pcol in enumerate(pc):
            v[pcol] = (-A[ri][fc]) % p
        out.append(v)
    return out


class Coupler:
    def __init__(self, nu_c, N, p):
        self.nu_c = tuple(nu_c); self.N = N; self.k = sum(nu_c); self.p = p
        self.whw = self._hw_tensor()
        self._build_module()
        self.mon = list(comps(4, N))

    def _hw_tensor(self):
        cells = [(i, j) for i in range(len(self.nu_c)) for j in range(self.nu_c[i])]
        cs = sorted(cells, key=lambda c: (c[1], c[0]))
        pos = {c: q for q, c in enumerate(cs)}
        cols = {}
        for (i, j) in cells:
            cols.setdefault(j, []).append(i)
        vec = {tuple([0] * self.k): 1}
        for j in sorted(cols):
            rows = sorted(cols[j]); h = len(rows)
            slots = [pos[(i, j)] for i in rows]
            new = {}
            for key, co in vec.items():
                for perm in permutations(range(h)):
                    s = perm_sign(perm)
                    kk = list(key)
                    for a, sl in enumerate(slots):
                        kk[sl] = perm[a]
                    kk = tuple(kk)
                    new[kk] = (new.get(kk, 0) + co * s) % self.p
            vec = {k2: c % self.p for k2, c in new.items() if c % self.p}
        return vec

    def _E_tensor(self, vec, a, b):
        out = {}
        for key, co in vec.items():
            for q in range(self.k):
                if key[q] == b:
                    kk = list(key); kk[q] = a; kk = tuple(kk)
                    out[kk] = (out.get(kk, 0) + co) % self.p
        return {k2: c for k2, c in out.items() if c}

    def _reduce(self, v, basis, leads):
        v = dict(v); coeffs = {}
        while True:
            v = {k: c % self.p for k, c in v.items() if c % self.p}
            if not v:
                break
            lead = min(v)
            hit = leads.get(lead)
            if hit is None:
                break
            bv = basis[hit]
            f = (v[lead] * pow(bv[lead], self.p - 2, self.p)) % self.p
            coeffs[hit] = (coeffs.get(hit, 0) + f) % self.p
            for k2, c2 in bv.items():
                v[k2] = (v.get(k2, 0) - f * c2) % self.p
        return v, coeffs

    def _build_module(self):
        basis = []; leads = {}
        def add(v):
            r, _ = self._reduce(v, basis, leads)
            if r:
                basis.append(r); leads[min(r)] = len(basis) - 1
                return True
            return False
        add(self.whw)
        frontier = [self.whw]
        while frontier:
            nxt = []
            for v in frontier:
                for a in range(self.N - 1):
                    w = self._E_tensor(v, a + 1, a)
                    if w and add(w):
                        nxt.append(basis[-1])
            frontier = nxt
        self.wbasis = basis; self.wleads = leads; self.wdim = len(basis)
        # Emat: columns[i] = coords of E_ab wbasis[i]
        self.Emat = {}
        for a in range(self.N):
            for b in range(self.N):
                if a == b:
                    continue
                cols = []
                for i in range(self.wdim):
                    w = self._E_tensor(self.wbasis[i], a, b)
                    if w:
                        r, co = self._reduce(w, basis, leads)
                        assert not r, "E_ab left module"
                        vec = [0] * self.wdim
                        for idx, c in co.items():
                            vec[idx] = c % self.p
                    else:
                        vec = [0] * self.wdim
                    cols.append(vec)
                self.Emat[(a, b)] = cols
        self.wwt = []
        for w in self.wbasis:
            k0 = next(iter(w)); cnt = [0] * self.N
            for x in k0:
                cnt[x] += 1
            self.wwt.append(tuple(cnt))

    def E_full(self, state, a, b, on_w=True, on_a=True, on_b=True):
        p = self.p; out = {}
        if a == b:
            for (wi, am, bm), co in state.items():
                d = 0
                if on_w: d += self.wwt[wi][a]
                if on_a: d += am[a]
                if on_b: d += bm[a]
                if d % p:
                    out[(wi, am, bm)] = (out.get((wi, am, bm), 0) + co * d) % p
            return {k: c for k, c in out.items() if c}
        for (wi, am, bm), co in state.items():
            if on_w:
                col = self.Emat[(a, b)][wi]
                for j in range(self.wdim):
                    if col[j]:
                        out[(j, am, bm)] = (out.get((j, am, bm), 0) + co * col[j]) % p
            if on_a and am[b] > 0:
                am2 = list(am); am2[b] -= 1; am2[a] += 1; am2 = tuple(am2)
                out[(wi, am2, bm)] = (out.get((wi, am2, bm), 0) + co * am[b]) % p
            if on_b and bm[b] > 0:
                bm2 = list(bm); bm2[b] -= 1; bm2[a] += 1; bm2 = tuple(bm2)
                out[(wi, am, bm2)] = (out.get((wi, am, bm2), 0) + co * bm[b]) % p
        return {k: c for k, c in out.items() if c}

    def casimir_eig(self, order):
        """C_order eigenvalue on W_{nu_c} via the hw vector, mod p."""
        p = self.p; hw = {0: 1}
        def Ew(vec, a, b):
            out = {}
            if a == b:
                for i, c in vec.items():
                    d = self.wwt[i][a]
                    if d % p:
                        out[i] = (out.get(i, 0) + c * d) % p
                return {i: c for i, c in out.items() if c}
            for i, c in vec.items():
                col = self.Emat[(a, b)][i]
                for j in range(self.wdim):
                    if col[j]:
                        out[j] = (out.get(j, 0) + c * col[j]) % p
            return {i: c for i, c in out.items() if c}
        total = 0
        for word in iproduct(range(self.N), repeat=order):
            seq = [(word[i], word[(i + 1) % order]) for i in range(order)]
            v = dict(hw)
            for (a, b) in reversed(seq):
                v = Ew(v, a, b)
                if not v:
                    break
            total = (total + v.get(0, 0)) % p
        return total

    def hw_space(self, rho_c):
        p = self.p
        target = tuple(list(rho_c) + [0] * (self.N - len(rho_c)))
        states = []
        for wi in range(self.wdim):
            ww = self.wwt[wi]
            for am in self.mon:
                s0 = tuple(ww[i] + am[i] for i in range(self.N))
                if any(s0[i] > target[i] for i in range(self.N)):
                    continue
                bm = tuple(target[i] - s0[i] for i in range(self.N))
                if sum(bm) == 4 and all(x >= 0 for x in bm):
                    states.append((wi, am, bm))
        n = len(states)
        if n == 0:
            return [], []
        spos = {s: i for i, s in enumerate(states)}
        Mcols = [dict() for _ in range(n)]
        for a in range(self.N - 1):
            for si, s in enumerate(states):
                img = self.E_full({s: 1}, a, a + 1)
                for st, c in img.items():
                    rk = (a, st)
                    Mcols[si][rk] = (Mcols[si].get(rk, 0) + c) % p
        allkeys = sorted({rk for col in Mcols for rk in col}, key=lambda x: (x[0], str(x[1])))
        kpos = {rk: i for i, rk in enumerate(allkeys)}
        M = [[0] * n for _ in range(len(allkeys))]
        for si in range(n):
            for rk, c in Mcols[si].items():
                M[kpos[rk]][si] = c
        ker = nullspace_modp(M, n, p)
        hwstates = []
        for kv in ker:
            st = {}
            for si in range(n):
                if kv[si]:
                    st[states[si]] = kv[si]
            hwstates.append(st)
        return hwstates, states


def casimir_value(kappa, N):
    k = list(kappa) + [0] * (N - len(kappa))
    return sum(k[i] * (k[i] + N + 1 - 2 * (i + 1)) for i in range(N))


def solve_coords(U, b, H, p):
    ns = len(U)
    aug = [U[i][:] + [b[i]] for i in range(ns)]
    piv = 0; pc = []
    for col in range(H):
        sel = None
        for rr in range(piv, ns):
            if aug[rr][col] % p:
                sel = rr; break
        if sel is None:
            continue
        aug[piv], aug[sel] = aug[sel], aug[piv]
        inv = pow(aug[piv][col] % p, p - 2, p)
        aug[piv] = [(x * inv) % p for x in aug[piv]]
        for rr in range(ns):
            if rr != piv and aug[rr][col] % p:
                f = aug[rr][col] % p
                aug[rr] = [(aug[rr][t] - f * aug[piv][t]) % p for t in range(H + 1)]
        pc.append((col, piv)); piv += 1
    x = [0] * H
    for col, pr in pc:
        x[col] = aug[pr][H] % p
    return x


def matmul(A, B, p):
    m = len(A); n = len(B); q = len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(n)) % p for j in range(q)] for i in range(m)]


def invmat(P, p):
    n = len(P)
    A = [P[i][:] + [1 if i == j else 0 for j in range(n)] for i in range(n)]
    for col in range(n):
        sel = next(r for r in range(col, n) if A[r][col] % p)
        A[col], A[sel] = A[sel], A[col]
        inv = pow(A[col][col] % p, p - 2, p)
        A[col] = [(x * inv) % p for x in A[col]]
        for r in range(n):
            if r != col and A[r][col] % p:
                f = A[r][col] % p
                A[r] = [(A[r][k] - f * A[col][k]) % p for k in range(2 * n)]
    return [row[n:] for row in A]


_LOCAL_CACHE = {}
_COUPLER_CACHE = {}


def get_coupler(shape, N, p):
    key = (tuple(shape), N, p)
    if key not in _COUPLER_CACHE:
        _COUPLER_CACHE[key] = Coupler(shape, N, p)
    return _COUPLER_CACHE[key]


def build_local_correct(rho, nu, p):
    rho_c, nu_c, ar, ac = collapse(rho, nu)
    orig = [mu for mu in horiz_strips_below(rho, 4) if is_h4_below(mu, nu)]
    c2o = {collapse_shape(mu, ar, ac, nu): mu for mu in orig}
    mus_c, S = _build_local_collapsed(rho_c, nu_c, p)
    return [c2o[mc] for mc in mus_c], S


def _build_local_collapsed(rho_c, nu_c, p):
    key = (tuple(rho_c), tuple(nu_c), p)
    if key in _LOCAL_CACHE:
        return _LOCAL_CACHE[key]
    N = len(rho_c)
    cp = get_coupler(nu_c, N, p)
    hw, states = cp.hw_space(rho_c)
    H = len(hw)
    inter = [mc for mc in horiz_strips_below(rho_c, 4) if is_h4_below(mc, nu_c)]
    assert H == len(inter), f"hw {H} != #interm {len(inter)} at {rho_c}/{nu_c}"
    if H == 0:
        _LOCAL_CACHE[key] = ([], []); return [], []
    spos = {s: i for i, s in enumerate(states)}; ns = len(states)
    U = [[0] * H for _ in range(ns)]
    for t, v in enumerate(hw):
        for s, c in v.items():
            U[spos[s]][t] = c

    def Cp_op(order):
        Op = [[0] * H for _ in range(H)]
        for t in range(H):
            acc = {}
            for word in iproduct(range(N), repeat=order):
                seq = [(word[i], word[(i + 1) % order]) for i in range(order)]
                v = hw[t]
                for (a, b) in reversed(seq):
                    v = cp.E_full(v, a, b, on_w=True, on_a=True, on_b=False)
                    if not v:
                        break
                for st, c in v.items():
                    acc[st] = (acc.get(st, 0) + c) % p
            bvec = [0] * ns
            for st, c in acc.items():
                bvec[spos[st]] = c
            co = solve_coords(U, bvec, H, p)
            for i in range(H):
                Op[i][t] = co[i]
        return Op

    c2val = {mc: casimir_value(mc, N) % p for mc in inter}
    C2 = Cp_op(2)
    use_c3 = len(set(c2val.values())) < len(inter)
    if use_c3:
        C3 = Cp_op(3)
        sig = {mc: (c2val[mc], get_coupler(mc, N, p).casimir_eig(3)) for mc in inter}
    else:
        sig = {mc: (c2val[mc],) for mc in inter}
    assert len(set(sig.values())) == len(inter), f"Casimirs fail to separate at {rho_c}/{nu_c}"
    pathvec = {}
    for mc in inter:
        A = [[(C2[i][j] - (sig[mc][0] if i == j else 0)) % p for j in range(H)] for i in range(H)]
        if use_c3:
            A = A + [[(C3[i][j] - (sig[mc][1] if i == j else 0)) % p for j in range(H)] for i in range(H)]
        ker = nullspace_modp(A, H, p)
        assert len(ker) == 1, f"Casimir degenerate at {rho_c}/{nu_c} {mc}: {len(ker)}"
        pathvec[mc] = ker[0]
    P = [[pathvec[inter[j]][i] for j in range(H)] for i in range(H)]
    Pinv = invmat(P, p)
    Sig = [[0] * H for _ in range(H)]
    for t in range(H):
        sw = {}
        for (wi, am, bm), c in hw[t].items():
            sw[(wi, bm, am)] = (sw.get((wi, bm, am), 0) + c) % p
        bvec = [0] * ns
        for st, c in sw.items():
            bvec[spos[st]] = c
        co = solve_coords(U, bvec, H, p)
        for i in range(H):
            Sig[i][t] = co[i]
    S_path = matmul(matmul(Pinv, Sig, p), P, p)
    _LOCAL_CACHE[key] = (inter, S_path)
    return inter, S_path


if __name__ == "__main__":
    P = 2147483647
    from wk9_s42_census import a_weyl

    def a_from_local(rho, nu):
        mus, S = build_local_correct(rho, nu, P)
        n = len(S)
        good = [i for i, mu in enumerate(mus) if a_weyl(mu, 2, 4, {}) > 0]
        M = [[(S[i][good[j]] - (1 if i == good[j] else 0)) % P for j in range(len(good))]
             for i in range(n)]
        return len(good) - (len(good) - len(nullspace_modp(M, len(good), P)))
    print("(8,4)/(4) a =", a_from_local((8, 4), (4,)), "(expect 1)")
