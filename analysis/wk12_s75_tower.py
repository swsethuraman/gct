#!/usr/bin/env python3
"""s75 -- the S5 one-block recursion, built as an explicit operator tower.

For each shape rho (level m = |rho|/4) the recursion gives
    W(rho) = (+)_{mu <. rho}  M(mu)                          dim B(rho)
    P(rho) = (+)_{mu <. rho}  W(mu) = (+)_{nu <.. rho} X_{nu,rho} (x) M(nu)
                                                            dim C(rho)
    iota : W(rho) --> P(rho)     (embed each M(mu) in W(mu), stored recursively)
    sigma_rho : P(rho) --> P(rho) block-diagonal over (nu,e), acting on the
               intermediate mu-index by the local block swap S_{nu,rho}
               (analysis/wk12_s75_recoup, verified against LR).
    R_rho = (sigma_rho - I) . iota : W(rho) --> P(rho)
    M(rho) = ker R_rho,   dim a(rho).

`<.` is a horizontal 4-strip step.  M(rho) is stored as a basis in W(rho)-
coordinates (the predecessor coordinates the brief asks for).

All tower linear algebra is done mod the two house primes with python-flint;
a(rho) is checked against the char-0 plethysm engine a_weyl at *every* node.
No prime below 97 is used (both house primes exceed |lambda_24| = 96).
"""
import sys, os, time, json, pickle
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.normpath(os.path.join(HERE, '..'))
from flint import nmod_mat
from wk12_s75_recoup import horiz_strips_below
from wk12_s75_local import build_local_correct
from wk9_s42_census import a_weyl

P1 = 2147483647
P2 = 2147483629


def lam_of(delta):
    return (4 * delta - 31, 17) + (2,) * 7


def norm(p):
    p = tuple(p)
    while p and p[-1] == 0:
        p = p[:-1]
    return p


def build_dag(top):
    """all shapes reachable from `top` by repeated h4-strip removal, grouped by level."""
    from collections import defaultdict
    levels = defaultdict(set)
    seen = set()
    frontier = {norm(top)}
    while frontier:
        nxt = set()
        for rho in frontier:
            m = sum(rho) // 4
            levels[m].add(rho)
            if rho in seen:
                continue
            seen.add(rho)
            if sum(rho) >= 4:
                for mu in horiz_strips_below(rho, 4):
                    nxt.add(norm(mu))
        frontier = nxt - seen
    return levels


def fr_to_mod(x, p):
    return (int(x.numerator) % p) * pow(int(x.denominator) % p, p - 2, p) % p


def build_tower(top, primes=(P1, P2), verbose=True, checkpoint=None):
    levels = build_dag(top)
    maxlev = max(levels)
    # data[p][rho] = dict(index_list=[(mu,e)...], basis=nmod_mat (a x B))
    data = {p: {} for p in primes}
    a_of = {}
    local_cache = {}    # (rho, nu) -> (mus, S_mod[p])
    dag_nodes = sum(len(v) for v in levels.values())
    if verbose:
        print(f"DAG: {dag_nodes} nodes, levels 1..{maxlev}", flush=True)

    # seed level 1: M((4)) = Hom(W_(4), Sym^1 Sym^4) = C (1-dim); every other
    # mu |- 4 has a_1(mu) = 0 (Sym^1 Sym^4 = W_(4) only).
    for mu in levels.get(1, []):
        if mu == (4,):
            for p in primes:
                data[p][(4,)] = dict(index_list=[((), 0)], basis=nmod_mat(1, 1, [1], p))
            a_of[(4,)] = 1
        else:
            for p in primes:
                data[p][mu] = dict(index_list=[], basis=nmod_mat(0, 0, [], p))
            a_of[mu] = 0

    for m in range(2, maxlev + 1):
        t0 = time.time()
        for rho in sorted(levels[m], reverse=True):
            mus = horiz_strips_below(rho, 4)                     # predecessors
            # W(rho) index list: (mu, e) for e in range(a(mu))
            Windex = []
            for mu in mus:
                for e in range(a_of[mu]):
                    Windex.append((mu, e))
            Wpos = {me: i for i, me in enumerate(Windex)}
            B = len(Windex)
            # P(rho) index list: (mu, nu, e) with nu <. mu, e in range(a(nu))
            Pindex = []
            for mu in mus:
                for (nu, e) in data[primes[0]][mu]['index_list']:
                    Pindex.append((mu, nu, e))
            Ppos = {mne: i for i, mne in enumerate(Pindex)}
            C = len(Pindex)
            # group P by (nu,e): intermediates mu
            from collections import defaultdict
            groups = defaultdict(dict)      # (nu,e) -> {mu: Prow}
            for (mu, nu, e) in Pindex:
                groups[(nu, e)][mu] = Ppos[(mu, nu, e)]

            akept = None
            for p in primes:
                # iota : W(rho)->P(rho) as C x B matrix (columns = W basis vectors)
                iota = [[0] * B for _ in range(C)]
                for wj, (mu, e) in enumerate(Windex):
                    Mmu = data[p][mu]                       # basis a(mu) x B(mu)
                    idxmu = Mmu['index_list']               # (nu,e') list = W(mu) coords
                    row = [int(Mmu['basis'][e, k]) for k in range(len(idxmu))]
                    for k, (nu, ee) in enumerate(idxmu):
                        c = row[k]
                        if c:
                            iota[Ppos[(mu, nu, ee)]][wj] = (iota[Ppos[(mu, nu, ee)]][wj] + c) % p
                # sigma_rho on P: block-diagonal over (nu,e)
                # build as C x C then R = (sigma - I) * iota
                # local matrices S_{nu,rho}
                Smats = {}
                for (nu, e), mudict in groups.items():
                    key = (rho, nu, p)
                    if key not in local_cache:
                        lm, S = build_local_correct(rho, nu, p)
                        local_cache[key] = (lm, S)
                    lm, S = local_cache[key]
                    Smats[(nu, e)] = (lm, S, mudict)
                # R = (sigma - I) iota  (C x B)
                R = [[0] * B for _ in range(C)]
                # first copy -iota then add sigma*iota
                for i in range(C):
                    for j in range(B):
                        if iota[i][j]:
                            R[i][j] = (-iota[i][j]) % p
                # sigma * iota : for each column j, sigma acts on iota[:,j]
                for j in range(B):
                    # collect iota column
                    for (nu, e), (lm, Sp, mudict) in Smats.items():
                        # gather the mu-components of this (nu,e) group from iota col
                        vec = [iota[mudict[mu]][j] if mu in mudict else 0 for mu in lm]
                        if not any(vec):
                            continue
                        for a_i, mu_i in enumerate(lm):
                            s = 0
                            Srow = Sp[a_i]
                            for b_i in range(len(lm)):
                                if vec[b_i]:
                                    s += Srow[b_i] * vec[b_i]
                            s %= p
                            if s:
                                r = mudict[mu_i]
                                R[r][j] = (R[r][j] + s) % p
                # kernel of R (B columns): a(rho) = B - rank
                Rmat = nmod_mat(C, B, [R[i][j] for i in range(C) for j in range(B)], p)
                rank = Rmat.rank()
                a_here = B - rank
                if akept is None:
                    akept = a_here
                elif akept != a_here:
                    raise RuntimeError(f"prime disagreement at {rho}: {akept} vs {a_here}")
                # kernel basis (B x a) -> store as a x B
                ker = kernel_basis(Rmat, p)   # list of columns (each length B)
                assert len(ker) == a_here
                basis = nmod_mat(a_here, B, [ker[t][k] for t in range(a_here) for k in range(B)], p) \
                    if a_here > 0 else nmod_mat(0, B, [], p)
                data[p][rho] = dict(index_list=Windex, basis=basis)
            # verify against a_weyl (char 0)
            aw = a_weyl(rho, m, 4, {})
            a_of[rho] = akept
            status = "ok" if akept == aw else "MISMATCH"
            if akept != aw:
                print(f"  !!! {rho} level {m}: tower a={akept}  a_weyl={aw}  {status}", flush=True)
                raise RuntimeError("tower disagrees with a_weyl")
        if verbose:
            print(f"level {m:2d}: {len(levels[m])} shapes  [{time.time()-t0:.1f}s]", flush=True)
        if checkpoint:
            pickle.dump({'a_of': a_of, 'level': m}, open(checkpoint, 'wb'))
    return data, a_of, levels


def kernel_basis(Rmat, p):
    """right kernel of Rmat (C x B) over F_p, as a list of column vectors length B."""
    C, B = Rmat.nrows(), Rmat.ncols()
    # use flint nullspace
    ns, nul = Rmat.nullspace()   # ns is B x k with columns spanning kernel
    cols = []
    k = ns.ncols()
    for t in range(k):
        cols.append([int(ns[i, t]) for i in range(B)])
    # nullspace() may return k columns with nul the dimension
    return cols[:nul] if nul <= k else cols


if __name__ == "__main__":
    delta = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    top = lam_of(delta)
    print(f"lambda_{delta} = {top}")
    t0 = time.time()
    data, a_of, levels = build_tower(top, checkpoint=os.path.join(ROOT, 'results', f's75_tower{delta}.pkl'))
    print(f"\nTOP a({top}) = {a_of[top]}   [{time.time()-t0:.1f}s total]")
    # report B and C at the top
    mus = horiz_strips_below(top, 4)
    B = sum(a_of[mu] for mu in mus)
    print(f"B_{delta} = {B}")
