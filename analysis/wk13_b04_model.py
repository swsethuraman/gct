#!/usr/bin/env python3
"""B13-04 -- exact instrument for the cubic-to-quartic transfer criterion on
small models.  Self-contained; shares no code with the rest of analysis/.

Objects (V = C^r, coordinates x_1..x_r, index 0 is x_1 -- the fixed factor):

  Q_delta  = C[Sym^4 V*]_delta = Sym^delta(Sym^4 V)     quartic coordinate ring
  C_delta  = C[Sym^3 V*]_delta = Sym^delta(Sym^3 V)     cubic coordinate ring
  H_lam    = highest-weight vectors of weight lam in Q_delta   (dim a^(4))
  rho(h)(c) = h(x_1 . c)     the fixed-factor restriction, a cubic polynomial of
                              weight lam^- = (lam_1 - delta, lam_2, ..., lam_r)
  W^lam    = rho(H_lam)      (dim = mult_R(lam, delta) -- the fixed-factor lemma)
  J_delta  = I(D)_delta for D = D_r^f = closure{ f(A s) }, f a cubic in N vars
  J_{lam^-} = J_delta cap (weight lam^- space)
  gap(lam, delta) = mult_R - mult_P = dim( W^lam cap J_{lam^-} )   (Theorem A)

Conventions (tools/verify/FORMAT.md): coordinate functional c_alpha(F) = the
coefficient of x^alpha in F; E_ij c_alpha = (alpha_i + 1) c_{alpha + e_i - e_j};
the simple raising operators are E_{i,i+1}, the simple lowering operators
E_{i+1,i}.  Exponent tuples are always looked up by tuple, never by position.

Everything is exact: kernels and ranks over Q by flint fmpz_mat on integer
matrices; the two house primes are used only as cross-checks; cubic-ideal
membership is certified by symbolic substitution c = f(A s) with symbolic A
(flint fmpz_mpoly), never inferred from evaluation.

usage:  python3 wk13_b04_model.py A            (Model A: r=2, f=x^3, delta=2)
        python3 wk13_b04_model.py B <delta>    (Model B: r=3, f=x^3+y^3)
        python3 wk13_b04_model.py C <delta>    (exploratory: r=3, f=x*y*z, N=3)
"""
import sys, os, json, time, itertools, random
from functools import lru_cache
from flint import fmpz_mat, nmod_mat, fmpz_mpoly_ctx

P1, P2 = 2147483647, 2147483629
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))


def log(*a):
    print(*a, flush=True)


# ------------------------------------------------------------ combinatorics
@lru_cache(maxsize=None)
def exps(n, r):
    """all exponent tuples of degree n in r variables (a set; order irrelevant)."""
    if r == 1:
        return ((n,),)
    out = []
    for a in range(n, -1, -1):
        for rest in exps(n - a, r - 1):
            out.append((a,) + rest)
    return tuple(out)


@lru_cache(maxsize=None)
def weight_monomials(n, r, delta, w):
    """multisets (sorted tuples, descending) of delta exponent tuples of degree n
    in r variables whose componentwise sum is w."""
    w = tuple(w)
    if any(x < 0 for x in w) or sum(w) != n * delta:
        return ()
    letters = sorted(exps(n, r), reverse=True)
    out = []

    def rec(start, left, rem, cur):
        if left == 0:
            if not any(rem):
                out.append(tuple(cur))
            return
        for k in range(start, len(letters)):
            al = letters[k]
            if any(al[j] > rem[j] for j in range(r)):
                continue
            rec(k, left - 1, tuple(rem[j] - al[j] for j in range(r)), cur + [al])

    rec(0, delta, w, [])
    return tuple(out)


def dominant(w):
    return all(w[i] >= w[i + 1] for i in range(len(w) - 1)) and w[-1] >= 0


def partitions_with_parts(total, nparts, maxpart=None):
    """all partitions of `total` into at most nparts parts (padded with zeros)."""
    if maxpart is None:
        maxpart = total
    if nparts == 0:
        return [()] if total == 0 else []
    out = []
    for p in range(min(total, maxpart), -1, -1):
        for rest in partitions_with_parts(total - p, nparts - 1, p):
            out.append((p,) + rest)
    return out


def predecessors(lam, k):
    """mu with lam/mu a horizontal k-strip (mu interlaces lam; mu_r may be 0)."""
    r = len(lam)
    out = []

    def rec(i, cur, left):
        if i == r:
            if left == 0:
                out.append(tuple(cur))
            return
        lo = lam[i + 1] if i + 1 < r else 0
        for m in range(lam[i], lo - 1, -1):
            if m <= left:
                rec(i + 1, cur + [m], left - m)

    rec(0, [], sum(lam) - k)
    return out


# ---------------------------------------------------------------- operators
def add_to(d, k, v):
    if v:
        nv = d.get(k, 0) + v
        if nv:
            d[k] = nv
        elif k in d:
            del d[k]


def normalise(vec):
    """divide an integer vector (list or dict) by the gcd of its entries."""
    from math import gcd
    vals = list(vec.values()) if isinstance(vec, dict) else list(vec)
    g = 0
    for v in vals:
        g = gcd(g, abs(int(v)))
    if g <= 1:
        return vec
    if isinstance(vec, dict):
        return {k: v // g for k, v in vec.items()}
    return [v // g for v in vec]


def apply_E(mono, i, j):
    """E_ij on a monomial (multiset of letters): derivation, rule
    E_ij c_alpha = (alpha_i + 1) c_{alpha + e_i - e_j}.  Returns dict."""
    out = {}
    for p, al in enumerate(mono):
        if al[j] == 0:
            continue
        nb = list(al)
        nb[j] -= 1
        nb[i] += 1
        nm = tuple(sorted(mono[:p] + (tuple(nb),) + mono[p + 1:], reverse=True))
        add_to(out, nm, al[i] + 1)
    return out


def apply_E_poly(poly, i, j):
    out = {}
    for mono, c in poly.items():
        for m2, c2 in apply_E(mono, i, j).items():
            add_to(out, m2, c * c2)
    return out


def hwv_space(n, r, delta, w, first=0):
    """integer basis of {v in weight-w space : E_{i,i+1} v = 0 for i >= first}.
    first=0: GL_r highest-weight vectors; first=1: GL_{r-1}-highest (indices
    2..r) with prescribed x_1-weight.  Returns (basis monomials, [vectors as
    dict mono -> int])."""
    basis = weight_monomials(n, r, delta, w)
    if not basis:
        return basis, []
    pos = {m: k for k, m in enumerate(basis)}
    rows = []
    for i in range(first, r - 1):
        j = i + 1
        tgt = list(w)
        tgt[i] += 1
        tgt[j] -= 1
        if tgt[j] < 0:
            continue
        acc = {}
        for m in basis:
            for m2, c in apply_E(m, i, j).items():
                d = acc.setdefault(m2, {})
                add_to(d, pos[m], c)
        rows += list(acc.values())
    nb = len(basis)
    if not rows:
        vecs = [{m: 1} for m in basis]
        return basis, vecs
    M = fmpz_mat(len(rows), nb, [0] * (len(rows) * nb))
    for ri, rw in enumerate(rows):
        for cj, v in rw.items():
            M[ri, cj] = v
    X, nul = M.nullspace()
    vecs = []
    for k in range(nul):
        v = {}
        for cj in range(nb):
            e = int(X[cj, k])
            if e:
                v[basis[cj]] = e
        vecs.append(normalise(v))
    return basis, vecs


# -------------------------------------------------------------------- forms
def poly_mul(f, g):
    out = {}
    for a, ca in f.items():
        for b, cb in g.items():
            add_to(out, tuple(x + y for x, y in zip(a, b)), ca * cb)
    return out


def poly_pow(f, k, r):
    out = {tuple([0] * r): 1}
    for _ in range(k):
        out = poly_mul(out, f)
    return out


def restrict_form(f, N, r, A):
    """f (dict exponent(N) -> coeff) composed with the linear map s -> A s,
    A an N x r integer matrix: the form in r variables."""
    lin = [{tuple(1 if k == i else 0 for k in range(r)): A[t][i] for i in range(r) if A[t][i]}
           for t in range(N)]
    out = {}
    for beta, c in f.items():
        term = {tuple([0] * r): c}
        for t in range(N):
            if beta[t]:
                term = poly_mul(term, poly_pow(lin[t], beta[t], r))
        for k, v in term.items():
            add_to(out, k, v)
    return out


def linear_form(l, r):
    return {tuple(1 if k == i else 0 for k in range(r)): l[i] for i in range(r) if l[i]}


def x1_times(c, r):
    e0 = tuple(1 if k == 0 else 0 for k in range(r))
    return {tuple(x + y for x, y in zip(k, e0)): v for k, v in c.items()}


def eval_poly(poly, F):
    tot = 0
    for mono, c in poly.items():
        v = c
        for al in mono:
            v *= F.get(al, 0)
            if v == 0:
                break
        tot += v
    return tot


def rho(h, r):
    """fixed-factor restriction: h(x_1 . c) as a polynomial in cubic coordinates."""
    out = {}
    for mono, c in h.items():
        if any(al[0] == 0 for al in mono):
            continue
        nm = tuple(sorted((tuple((al[0] - 1,) + al[1:]) for al in mono), reverse=True))
        add_to(out, nm, c)
    return out


# ------------------------------------------------------------- linear algebra
def int_matrix(vecs, cols):
    pos = {m: k for k, m in enumerate(cols)}
    M = fmpz_mat(len(vecs), len(cols), [0] * (len(vecs) * len(cols)))
    for i, v in enumerate(vecs):
        for m, c in v.items():
            M[i, pos[m]] = c
    return M


def rank_Q(vecs, cols):
    if not vecs or not cols:
        return 0
    return int_matrix(vecs, cols).rank()


def rank_p(vecs, cols, p):
    if not vecs or not cols:
        return 0
    pos = {m: k for k, m in enumerate(cols)}
    ent = [0] * (len(vecs) * len(cols))
    for i, v in enumerate(vecs):
        for m, c in v.items():
            ent[i * len(cols) + pos[m]] = c % p
    return nmod_mat(len(vecs), len(cols), ent, p).rank()


def eval_matrix(polys, forms):
    """rows = forms (points), cols = polys; exact integers."""
    M = fmpz_mat(len(forms), len(polys), [0] * (len(forms) * len(polys)))
    for j, F in enumerate(forms):
        for i, h in enumerate(polys):
            M[j, i] = eval_poly(h, F)
    return M


def kernel_combinations(polys, forms):
    """integer vectors kappa with sum_i kappa_i polys_i (F) = 0 at every form."""
    if not polys:
        return []
    M = eval_matrix(polys, forms)
    X, nul = M.nullspace()
    return [normalise([int(X[i, k]) for i in range(len(polys))]) for k in range(nul)]


def combine(polys, kappa):
    out = {}
    for c, h in zip(kappa, polys):
        if c:
            for m, v in h.items():
                add_to(out, m, c * v)
    return out


def rank_eval_Q(polys, forms):
    if not polys:
        return 0
    return eval_matrix(polys, forms).rank()


def rank_eval_p(polys, forms, p):
    if not polys:
        return 0
    ent = []
    for F in forms:
        for h in polys:
            ent.append(eval_poly(h, F) % p)
    return nmod_mat(len(forms), len(polys), ent, p).rank()


# --------------------------------------------------- symbolic certification
class SymbolicCubic:
    """c = f(A s) with A an N x r matrix of indeterminates; c_beta as fmpz_mpoly."""

    def __init__(self, f, N, r):
        names = [f"a{t}_{i}" for t in range(N) for i in range(r)]
        self.ctx = fmpz_mpoly_ctx.get(tuple(names), 'lex')
        gens = self.ctx.gens()
        A = [[gens[t * r + i] for i in range(r)] for t in range(N)]
        zero = self.ctx.from_dict({})
        lin = []
        for t in range(N):
            d = {}
            for i in range(r):
                d[tuple(1 if k == i else 0 for k in range(r))] = A[t][i]
            lin.append(d)
        out = {}
        for beta, c in f.items():
            term = {tuple([0] * r): self.ctx.from_dict({tuple([0] * (N * r)): c})}
            for t in range(N):
                for _ in range(beta[t]):
                    nt = {}
                    for k1, v1 in term.items():
                        for k2, v2 in lin[t].items():
                            kk = tuple(x + y for x, y in zip(k1, k2))
                            nt[kk] = nt.get(kk, zero) + v1 * v2
                    term = nt
            for k, v in term.items():
                out[k] = out.get(k, zero) + v
        self.c = out
        self.zero = zero

    def vanishes(self, g):
        """is g(f(A s)) identically zero as a polynomial in the entries of A?"""
        tot = self.zero
        for mono, coef in g.items():
            v = self.ctx.from_dict({tuple([0] * self.ctx.nvars()): coef})
            for al in mono:
                v = v * self.c.get(al, self.zero)
            tot = tot + v
        return tot.is_zero()


# ------------------------------------------------------- swap certificates
def substitute_x1(form, l, r):
    """form(x_1 - sum_{j>=2} l_j x_j, x_2, ..., x_r) for a form (dict) in r variables;
    this is u_l^{-1} acting on forms when l_1 = 1."""
    lin = {tuple(1 if k == 0 else 0 for k in range(r)): 1}
    for j in range(1, r):
        if l[j]:
            lin[tuple(1 if k == j else 0 for k in range(r))] = -l[j]
    out = {}
    for al, c in form.items():
        term = {tuple([0] * r): c}
        if al[0]:
            term = poly_mul(term, poly_pow(lin, al[0], r))
        rest = tuple((0,) + al[1:])
        term = poly_mul(term, {rest: 1})
        for k, v in term.items():
            add_to(out, k, v)
    return out


def swap_certificate(F, r, rnd, bound=5, tries=40):
    """Lemma: every F in W^lam satisfies F(l.q) = F(u_l^{-1}(x_1 q)) for l with
    l_1 = 1.  Returns an integer point (l, q) violating it for F, or None."""
    for _ in range(tries):
        l = [1] + [rnd.randint(-bound, bound) for _ in range(r - 1)]
        q = {al: rnd.randint(-bound, bound) for al in exps(2, r)}
        lhs = eval_poly(F, poly_mul(linear_form(l, r), q))
        x1q = x1_times(q, r)
        rhs = eval_poly(F, substitute_x1(x1q, l, r))
        if lhs != rhs:
            return dict(l=l, q={str(k): v for k, v in q.items()}, lhs=lhs, rhs=rhs)
    return None


# ------------------------------------------------------------ point families
def random_matrix(rnd, N, r, bound):
    return [[rnd.randint(-bound, bound) for _ in range(r)] for _ in range(N)]


def random_cubic(rnd, r, bound):
    return {al: rnd.randint(-bound, bound) for al in exps(3, r)}


def random_linear(rnd, r, bound, first_nonzero=False):
    l = [rnd.randint(-bound, bound) for _ in range(r)]
    if first_nonzero and l[0] == 0:
        l[0] = 1
    return l


# ---------------------------------------------------------- the model driver
def run_model(tag, f, N, r, delta, seed=20260909, bound=7, out_dir=None):
    t0 = time.time()
    rnd = random.Random(seed)
    res = dict(board_numbering='batch13', session='B13-04', model=tag, f={str(k): v for k, v in f.items()},
               N=N, r=r, delta=delta, seed=seed, bound=bound, primes=[P1, P2],
               conventions="E_ij c_alpha = (alpha_i+1) c_{alpha+e_i-e_j}; fixed factor x_1 = index 0;"
                           " ranks exact over Q (fmpz_mat), primes as cross-checks; all values native"
                           " (values_are: none)")
    sym = SymbolicCubic(f, N, r)

    # ---- cubic side: every dominant nu |- 3 delta with <= r parts
    cubic = {}
    npts_c = 40
    cubic_pts = [restrict_form(f, N, r, random_matrix(rnd, N, r, bound)) for _ in range(npts_c)]
    for nu in partitions_with_parts(3 * delta, r):
        basis, H = hwv_space(3, r, delta, nu)
        a3 = len(H)
        if a3 == 0:
            continue
        rk = rank_eval_Q(H, cubic_pts)
        kap = kernel_combinations(H, cubic_pts)
        certified = []
        for k in kap:
            g = combine(H, k)
            ok = sym.vanishes(g)
            certified.append(ok)
        entry = dict(nu=list(nu), a3=a3, N_S=len(basis), rank_eval_Q=rk,
                     rank_p=[rank_eval_p(H, cubic_pts, P1), rank_eval_p(H, cubic_pts, P2)],
                     kernel_dim_sampled=len(kap), kernel_certified=all(certified) and len(kap) == a3 - rk,
                     i3=(len(kap) if all(certified) else None), hwv=H, kernel=kap)
        cubic[nu] = entry
        log(f"[cubic] nu={nu} a3={a3} N_S={len(basis)} rank_Q={rk} i3={entry['i3']} "
            f"certified={entry['kernel_certified']}")
    res['cubic'] = {str(k): {kk: vv for kk, vv in v.items() if kk not in ('hwv',)}
                    for k, v in cubic.items()}
    for k, v in res['cubic'].items():
        v['kernel'] = [list(x) for x in v['kernel']]

    # ---- quartic side
    npts = 60
    red_pts, pad_pts, pad_x1_pts = [], [], []
    while len(red_pts) < npts:
        l = random_linear(rnd, r, bound, first_nonzero=True)
        c = random_cubic(rnd, r, bound)
        red_pts.append(poly_mul(linear_form(l, r), c))
    while len(pad_pts) < npts:
        l = random_linear(rnd, r, bound, first_nonzero=True)
        c = restrict_form(f, N, r, random_matrix(rnd, N, r, bound))
        pad_pts.append(poly_mul(linear_form(l, r), c))
        pad_x1_pts.append(x1_times(c, r))
    cells = []
    for lam in partitions_with_parts(4 * delta, r):
        basis4, H = hwv_space(4, r, delta, lam)
        a4 = len(H)
        if a4 == 0:
            continue
        lam_minus = (lam[0] - delta,) + tuple(lam[1:])
        cell = dict(lam=list(lam), a4=a4, N_S4=len(basis4), lam_minus=list(lam_minus))
        if lam[0] < delta:
            cell.update(mult_R_fixedfactor=0, note='lam_1 < delta: rho = 0, mult_R = 0 (Cor. of the fixed-factor lemma)')
            cell['mult_R_eval_Q'] = rank_eval_Q(H, red_pts)
            cell['mult_P_eval_Q'] = rank_eval_Q(H, pad_pts)
            cells.append(cell)
            log(f"[quartic] lam={lam} a4={a4} lam_1<delta: mult_R=0 (eval {cell['mult_R_eval_Q']}, pad {cell['mult_P_eval_Q']})")
            continue
        cols = weight_monomials(3, r, delta, lam_minus)
        RH = [rho(h, r) for h in H]
        mR_ff = rank_Q(RH, cols)
        mR_ev = rank_eval_Q(H, red_pts)
        mR_p = [rank_eval_p(H, red_pts, P1), rank_eval_p(H, red_pts, P2)]
        mP_ev = rank_eval_Q(H, pad_pts)
        mP_p = [rank_eval_p(H, pad_pts, P1), rank_eval_p(H, pad_pts, P2)]
        mP_ff = rank_eval_Q(H, pad_x1_pts)
        # the cubic ideal in the weight-lam^- space, exact: kernel of evaluation,
        # every basis vector certified symbolically
        Jbasis = []
        if cols:
            mono_polys = [{m: 1} for m in cols]
            Kc = kernel_combinations(mono_polys, cubic_pts + [restrict_form(f, N, r, random_matrix(rnd, N, r, bound))
                                                              for _ in range(len(cols) + 10)])
            Jcert = True
            for k in Kc:
                g = combine(mono_polys, k)
                if not sym.vanishes(g):
                    Jcert = False
                    break
                Jbasis.append(normalise(g))
        else:
            Jcert = True
        dimW = mR_ff
        dimJ = len(Jbasis)
        dimWJ = rank_Q(RH + Jbasis, cols) if cols else 0
        crit = dimW + dimJ - dimWJ
        # Pieri predecessors and per-constituent contribution
        preds = []
        for nu in predecessors(lam, delta):
            nut = tuple(x for x in nu if x)
            nu_full = tuple(nu)
            e = cubic.get(nu_full)
            if e is None or e['a3'] == 0:
                preds.append(dict(nu=list(nu_full), a3=0, i3=0))
                continue
            pe = dict(nu=list(nu_full), a3=e['a3'], i3=e['i3'], parts=len(nut))
            if e['i3']:
                # branching vectors g^{down lam}: GL_{r-1}-HWVs of weight lam^- in the
                # module generated by the certified cubic-ideal HWVs at nu
                gs = [combine(e['hwv'], k) for k in e['kernel']]
                # words in the simple lowering operators from nu to lam^-
                steps = []
                part = 0
                for i in range(r - 1):
                    part += nu_full[i] - lam_minus[i]
                    steps.append(part)   # number of F_i = E_{i+1,i} applications
                assert all(s >= 0 for s in steps), (nu_full, lam_minus, steps)
                words = set()
                seq = []
                for i, s in enumerate(steps):
                    seq += [i] * s
                for perm in set(itertools.permutations(seq)):
                    words.add(perm)
                lowered = []
                for g in gs:
                    for wd in words:
                        v = g
                        for i in wd:
                            v = apply_E_poly(v, i + 1, i)
                            if not v:
                                break
                        if v:
                            lowered.append(v)
                # intersect span(lowered) with the GL_{r-1}-HWV condition
                Bbasis, Bvecs = hwv_space(3, r, delta, lam_minus, first=1)
                branch = []
                if lowered and Bvecs:
                    # solve: vectors in span(lowered) killed by E_{i,i+1}, i>=1
                    L = int_matrix(lowered, cols)          # rows = lowered vectors
                    # E-images of the lowered vectors, stacked
                    imgs = []
                    tcols = []
                    for i in range(1, r - 1):
                        tw = list(lam_minus)
                        tw[i] += 1
                        tw[i + 1] -= 1
                        tc = weight_monomials(3, r, delta, tuple(tw))
                        tcols.append((i, tc))
                    allcols = []
                    for i, tc in tcols:
                        allcols += [(i, m) for m in tc]
                    if allcols:
                        cpos = {k: j for j, k in enumerate(allcols)}
                        E = fmpz_mat(len(lowered), len(allcols), [0] * (len(lowered) * len(allcols)))
                        for li, v in enumerate(lowered):
                            for i, _ in tcols:
                                for m, c in apply_E_poly(v, i, i + 1).items():
                                    E[li, cpos[(i, m)]] += c
                        X, nul = E.transpose().nullspace()
                        combos = [normalise([int(X[li, k]) for li in range(len(lowered))]) for k in range(nul)]
                    else:
                        combos = [[1 if li == k else 0 for li in range(len(lowered))] for k in range(len(lowered))]
                    cand = [normalise(combine(lowered, k)) for k in combos]
                    cand = [v for v in cand if v]
                    # reduce to an independent set
                    ind = []
                    for v in cand:
                        if rank_Q(ind + [v], cols) > len(ind):
                            ind.append(v)
                    branch = ind
                pe['branch_dim'] = len(branch)
                pe['branch_in_W'] = [rank_Q(RH + [b], cols) == dimW for b in branch]
                pe['branch_span_meets_W'] = (dimW + len(branch) - rank_Q(RH + branch, cols)) if branch else 0
                pe['_branch'] = branch
                pe['swap_certificates'] = [None if inW else swap_certificate(b, r, rnd)
                                           for b, inW in zip(branch, pe['branch_in_W'])]
                pe['swap_detects_all'] = all(sc is not None for sc, inW in zip(pe['swap_certificates'], pe['branch_in_W']) if not inW)
                # sanity: the swap identity must hold for every rho(h)
                for hh in RH:
                    assert swap_certificate(hh, r, rnd, tries=5) is None, "swap identity violated by a rho(h): instrument defect"
                pe['branch_vectors'] = [[[list(map(list, m)), c] for m, c in sorted(b.items())] for b in branch] if sum(len(b) for b in branch) <= 60 else None
            preds.append(pe)
        sum_i3 = sum((p['i3'] or 0) for p in preds)
        sum_a3 = sum(p['a3'] for p in preds)
        all_branch = []
        for p in preds:
            all_branch += p.pop('_branch', [])
        dim_branch = rank_Q(all_branch, cols) if all_branch else 0
        meets_all = (dimW + dim_branch - rank_Q(RH + all_branch, cols)) if all_branch else 0
        # explicit witnesses: quartic HWV combinations h with rho(h) in J (the
        # additional padded equations), as integer combinations of the H basis
        witnesses = []
        if crit > 0 and cols:
            # kappa with sum kappa_i rho(h_i) in span(J): kernel of [RH | -Jbasis] restricted to RH part
            pos = {m: k for k, m in enumerate(cols)}
            nr = len(RH) + len(Jbasis)
            M = fmpz_mat(nr, len(cols), [0] * (nr * len(cols)))
            for i, v in enumerate(RH + Jbasis):
                for m, c in v.items():
                    M[i, pos[m]] = c
            X, nul = M.transpose().nullspace()
            for k in range(nul):
                kap = normalise([int(X[i, k]) for i in range(len(RH))])
                if any(kap):
                    h = normalise(combine(H, kap))
                    rh = rho(h, r)
                    # certify: rho(h) vanishes on D symbolically, and h is nonzero on a reducible point
                    ok = sym.vanishes(rh)
                    nz = any(eval_poly(h, F) != 0 for F in red_pts)
                    witnesses.append(dict(kappa=kap, rho_h_in_J_certified=ok, nonzero_on_reducible=nz,
                                          h_terms=len(h), rho_h_terms=len(rh),
                                          h=[[list(map(list, m)), c] for m, c in sorted(h.items())] if len(h) <= 40 else None,
                                          rho_h=[[list(map(list, m)), c] for m, c in sorted(rh.items())] if len(rh) <= 40 else None))
        cell.update(mult_R_fixedfactor=mR_ff, mult_R_eval_Q=mR_ev, mult_R_eval_p=mR_p,
                    mult_P_eval_Q=mP_ev, mult_P_eval_p=mP_p, mult_P_fixedfactor_eval_Q=mP_ff,
                    dim_J_lam_minus=dimJ, J_certified=Jcert, dim_W_plus_J=dimWJ,
                    criterion_gap=crit, gap_direct=mR_ff - mP_ev,
                    predecessors=preds, sum_i3=sum_i3, sum_a3=sum_a3,
                    N_S_lam_minus=len(cols), dim_branch_total=dim_branch, W_meets_branch_span=meets_all,
                    witnesses=witnesses)
        cells.append(cell)
        log(f"[quartic] lam={lam} a4={a4} mult_R: ff={mR_ff} evQ={mR_ev} p={mR_p} | mult_P: evQ={mP_ev} p={mP_p} ffQ={mP_ff}"
            f" | dimJ={dimJ}({'cert' if Jcert else 'UNCERT'}) crit={crit} direct={mR_ff - mP_ev}"
            f" | sum_i3={sum_i3} sum_a3={sum_a3} | branch_total={dim_branch} W_meets_branch={meets_all} witnesses={len(witnesses)}"
            f"{' cert=' + str([w['rho_h_in_J_certified'] and w['nonzero_on_reducible'] for w in witnesses]) if witnesses else ''}")
        for p in preds:
            if p.get('i3'):
                log(f"      pred nu={tuple(p['nu'])} a3={p['a3']} i3={p['i3']} branch_in_W={p.get('branch_in_W')}"
                    f" meets={p.get('branch_span_meets_W')} swap_detects_all_nondescents={p.get('swap_detects_all')}")
    res['cells'] = cells
    res['seconds'] = round(time.time() - t0, 1)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
        fn = os.path.join(out_dir, f"model_{tag}_d{delta}.json")
        with open(fn, 'w') as fh:
            json.dump(res, fh, indent=1)
        log(f"wrote {fn} ({res['seconds']}s)")
    return res


def main():
    which = sys.argv[1]
    out_dir = os.path.join(ROOT, 'results', 'b13_04')
    if which == 'A':
        run_model('A', {(3,): 1}, 1, 2, 2, out_dir=out_dir)
    elif which == 'B':
        d = int(sys.argv[2])
        run_model('B', {(3, 0): 1, (0, 3): 1}, 2, 3, d, out_dir=out_dir)
    elif which == 'C':
        d = int(sys.argv[2])
        run_model('C', {(1, 1, 1): 1}, 3, 3, d, out_dir=out_dir)
    elif which == 'A2':   # Model A at delta 3 (exploratory)
        run_model('A', {(3,): 1}, 1, 2, 3, out_dir=out_dir)
    else:
        raise SystemExit("usage: A | B <delta> | C <delta> | A2")


if __name__ == '__main__':
    main()
