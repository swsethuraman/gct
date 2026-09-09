#!/usr/bin/env python3
"""Session 79's Part 1, re-derived here from its artefacts.

The claim is a theorem, so it gets the theorem treatment: nothing is taken from
s79's engine, its checker, or the repository's own stable instrument.  This
script rebuilds, for each block,

  1. the raw weight space -- multisets of the 120 generators y_(d,alpha),
     d in {2,3,4}, alpha a degree-d exponent in five variables, with exponent
     sum rho -- and compares it as a SET with the delivered monomial list;
  2. a_inf(rho) by its own Weyl alternation over S_5 on the weight-space
     dimensions of Sym(Sym^2 U + Sym^3 U + Sym^4 U), each computed by an
     unbounded-knapsack numpy DP -- no repository census is called;
  3. the raising operators E_{i,i+1} from the stated derivation rule, and
     checks E.v = 0 for every delivered kernel vector at both primes;
  4. the point map by its own Leibniz expansion of det(t I - A(s)) over the 24
     permutations of four rows -- not power sums -- and rebuilds G = ev.K entry
     by entry;
  5. rank G, by its own elimination.

A full rank at one prime, with the kernel dimension equal to the
characteristic-zero a_inf, proves i_det^inf(rho) = 0 over Q.
"""
import itertools, json, math, os, sys
import numpy as np

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
SRC = os.environ.get('S79_DIR', os.path.join(ROOT, 'results', 's79_stable'))
P1, P2 = 2147483647, 2147483629
NV = 5                                       # five variables
DEGS = (2, 3, 4)
out = {'checks': [], 'blocks': {}}


def rec(name, ok, **kw):
    out['checks'].append(dict(name=name, ok=bool(ok), **kw))
    print(f'[{"PASS" if ok else "FAIL"}] {name}' + (f'  {kw}' if kw else ''), flush=True)
    return ok


def exps_deg(d, r=NV):
    if r == 1: return [(d,)]
    o = []
    for a in range(d, -1, -1):
        for rest in exps_deg(d - a, r - 1): o.append((a,) + rest)
    return o


def _gens(order):
    """the 120 generators, in one of the two exponent orderings the programme
    uses.  wk8_s30_core.exps runs the FIRST exponent up from 0; exps_deg here
    runs it down from d.  They are opposite, the preamble warns about it, and
    this is the third time it has bitten -- so the ordering is DETECTED from the
    delivered monomials, never assumed."""
    return [(d, a) for d in DEGS
            for a in (exps_deg(d) if order == 'desc' else list(reversed(exps_deg(d))))]


GENS = _gens('desc')                                      # 15 + 35 + 70 = 120
GIDX = {g: i for i, g in enumerate(GENS)}


def detect_order(monomials, rho):
    """pick the ordering under which every delivered monomial has exponent sum
    rho.  Fails loudly if neither works."""
    global GENS, GIDX
    for o in ('desc', 'asc'):
        G = _gens(o)
        if all([sum(G[i][1][k] for i in m) for k in range(NV)] == list(rho)
               for m in monomials):
            GENS, GIDX = G, {g: i for i, g in enumerate(G)}
            return o
    return None


def weight_dim(mu):
    """dim of the weight-mu part of Sym(Sym^2 U + Sym^3 U + Sym^4 U): the number
    of multisets of the 120 generators with exponent sum mu.  Unbounded knapsack,
    one in-place prefix sum per generator."""
    if any(x < 0 for x in mu): return 0
    shape = tuple(x + 1 for x in mu)
    F = np.zeros(shape, dtype=object)
    F[(0,) * NV] = 1
    for _d, a in GENS:
        if any(a[i] > mu[i] for i in range(NV)): continue
        # F[v] += F[v - a] for v increasing
        it = [range(a[i], mu[i] + 1) for i in range(NV)]
        # do it as a loop over the first axis order that respects the shift
        src = tuple(slice(0, mu[i] + 1 - a[i]) for i in range(NV))
        dst = tuple(slice(a[i], mu[i] + 1) for i in range(NV))
        # F_new = sum_k shift^k(F).  Repeated in-place F[dst] += F[src] does NOT
        # compute this -- numpy evaluates the whole right-hand side first, so the
        # second pass double counts.  Accumulate into a separate array.
        steps = min(mu[i] // a[i] for i in range(NV) if a[i])
        acc = F.copy(); cur = F
        for _ in range(steps):
            nxt = np.zeros(shape, dtype=object)
            nxt[dst] = cur[src]
            acc += nxt
            cur = nxt
        F = acc
        del it
    return int(F[tuple(mu)])


def a_inf(rho):
    """Weyl alternation over S_5 on weight_dim."""
    rho = tuple(rho) + (0,) * (NV - len(rho))
    d = tuple(range(NV - 1, -1, -1))                     # (4,3,2,1,0)
    tot = 0
    for w in itertools.permutations(range(NV)):
        sg = 1
        for i in range(NV):
            for j in range(i + 1, NV):
                if w[i] > w[j]: sg = -sg
        mu = tuple(rho[i] + d[i] - d[w[i]] for i in range(NV))
        if any(x < 0 for x in mu): continue
        tot += sg * weight_dim(mu)
    return tot


def monomials_of(rho):
    """multisets of generator indices with exponent sum rho, as sorted tuples."""
    rho = tuple(rho) + (0,) * (NV - len(rho))
    out_ = []
    G = [(i, GENS[i][1]) for i in range(len(GENS))]

    def rec_(start, rem, cur):
        if all(x == 0 for x in rem):
            out_.append(tuple(cur)); return
        if start >= len(G): return
        # prune: the smallest remaining degree is 2, so |rem| must be reachable
        for k in range(start, len(G)):
            i, a = G[k]
            nr = tuple(rem[j] - a[j] for j in range(NV))
            if any(x < 0 for x in nr): continue
            rec_(k, nr, cur + [i])
    rec_(0, rho, [])
    return set(out_)


def raise_gen(i, gi):
    """E_{i,i+1} y_(d,alpha) = (alpha_i + 1) y_(d, alpha + e_i - e_{i+1}); 0 if
    alpha_{i+1} = 0.  Returns (coefficient, generator index) or None."""
    d, a = GENS[gi]
    if a[i + 1] == 0: return None
    b = list(a); b[i] += 1; b[i + 1] -= 1
    return (a[i] + 1, GIDX[(d, tuple(b))])


def apply_E(i, vec, mons):
    """E_{i,i+1} as a derivation on monomials (multisets of generators).

    The image lives at weight rho + e_i - e_{i+1}, which is NOT the delivered
    basis, so targets are collected by their multiset and never looked up in it.
    An earlier version indexed into the delivered basis and skipped anything it
    did not find -- which made E.v = 0 pass vacuously under a wrong generator
    ordering.  Nothing is skipped here.
    """
    out_ = {}
    for mi, c in vec.items():
        if not c: continue
        m = mons[mi]
        for pos in range(len(m)):
            r = raise_gen(i, m[pos])
            if r is None: continue
            co, gj = r
            nm = tuple(sorted(m[:pos] + (gj,) + m[pos + 1:]))
            out_[nm] = out_.get(nm, 0) + c * co
    return out_


def _pmul(a, b):
    o = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            e = tuple(x + y for x, y in zip(e1, e2)); o[e] = o.get(e, 0) + c1 * c2
    return {e: c for e, c in o.items() if c}


def char_poly_coeffs(As, deg):
    """e_deg of A(s) = sum_k s_k A_k, as a dict alpha -> integer.

    e_d is the sum of the principal d x d minors, each expanded by Leibniz over
    S_d with entries the linear forms sum_k s_k (A_k)_{ij}.  No power sums, no
    char-poly sign bookkeeping -- the definition itself.
    """
    def lin(i, j):
        return {tuple(1 if q == k else 0 for q in range(NV)): As[k][i][j]
                for k in range(NV) if As[k][i][j]}
    acc = {}
    for S in itertools.combinations(range(4), deg):
        for perm in itertools.permutations(range(deg)):
            sg = 1
            for i in range(deg):
                for j in range(i + 1, deg):
                    if perm[i] > perm[j]: sg = -sg
            term = {(0,) * NV: sg}
            for i in range(deg):
                term = _pmul(term, lin(S[i], S[perm[i]]))
                if not term: break
            for e, c in term.items(): acc[e] = acc.get(e, 0) + c
    return {e: c for e, c in acc.items() if c}


def main(argv):
    output = os.path.join(ROOT, 'results', 'wk12_int_s79_stable_verify.json')
    if '--out' in argv:
        argv = list(argv)
        i = argv.index('--out'); output = argv[i + 1]; del argv[i:i + 2]
    blocks = argv or ['6_3_3_1', '4_4_3_2', '6_2_2_2_1', '5_3_2_2_1', '5_2_2_2_2']
    for b in blocks:
        path = os.path.join(SRC, f'stable_{b}.json')
        d = json.load(open(path))
        rho = tuple(d['rho'])
        print(f'\n===== rho = {rho}, a_inf claimed {d["a_inf"]}, raw {d["raw_weight_space"]}')
        theirs = set(tuple(m) for m in d['monomials'])
        o = detect_order(theirs, tuple(rho))
        rec(f'{rho}: the generator ordering is identified from the delivered '
            f'monomials ({o})', o is not None, ordering=o)
        if o is None: continue
        mine = monomials_of(rho)
        rec(f'{rho}: my weight space equals the delivered one as a set',
            mine == theirs, mine=len(mine), theirs=len(theirs))
        ai = a_inf(rho)
        rec(f'{rho}: my Weyl alternation gives a_inf = {ai}', ai == d['a_inf'],
            mine=ai, theirs=d['a_inf'])
        mons = sorted(theirs)
        index = {m: k for k, m in enumerate(mons)}
        order = [index[tuple(m)] for m in d['monomials']]     # delivered -> my order
        pts = d['points']
        for p in (P1, P2):
            pp = d['per_prime'][str(p)]
            K = pp['kernel']
            rec(f'{rho} p={p}: kernel dimension is a_inf', len(K) == ai)
            bad = 0
            for v in K:
                vec = {order[j]: v[j] % p for j in range(len(v)) if v[j] % p}
                for i in range(NV - 1):
                    im = apply_E(i, vec, mons)
                    if any(c % p for c in im.values()): bad += 1
            rec(f'{rho} p={p}: E.v = 0 for every kernel vector on my raising rows',
                bad == 0, failures=bad)
            # rebuild G myself
            ev = []
            for A in pts:
                As = A if isinstance(A[0][0], list) else A
                row = [0] * len(mons)
                val = {}
                for dg in DEGS:
                    cs = char_poly_coeffs(As, dg)
                    for gi, (gd, ga) in enumerate(GENS):
                        if gd == dg: val[gi] = cs.get(ga, 0) % p
                for k, m in enumerate(mons):
                    x = 1
                    for gi in m:
                        x = x * val[gi] % p
                        if x == 0: break
                    row[k] = x
                ev.append(row)
            G = [[sum(ev[j][order[t]] * K[c][t] for t in range(len(mons))) % p
                  for c in range(len(K))] for j in range(len(pts))]
            # Convention: s79's y_(d,.) are the char-poly coefficients
            # (-1)^d e_d; mine are e_d.  Every monomial of an ODD weight |rho|
            # carries an odd number of degree-3 generators (2 and 4 are even),
            # so the two differ by a GLOBAL sign on this weight space -- which
            # cannot change a kernel or a rank.  Checked as such, not assumed.
            neg = [[(-x) % p for x in r] for r in G]
            same = (G == pp['G'])
            flip = (neg == pp['G'])
            rec(f'{rho} p={p}: my G equals the delivered G entry by entry'
                + ('' if same else ' up to the global char-poly sign'),
                same or flip, sign=1 if same else (-1 if flip else None))
            # rank
            Aq = [r[:] for r in G]; nr, nc = len(Aq), len(Aq[0]); r_ = 0
            for c in range(nc):
                pr = next((i for i in range(r_, nr) if Aq[i][c] % p), None)
                if pr is None: continue
                Aq[r_], Aq[pr] = Aq[pr], Aq[r_]
                inv = pow(Aq[r_][c], -1, p); Aq[r_] = [x * inv % p for x in Aq[r_]]
                for i in range(nr):
                    if i != r_ and Aq[i][c] % p:
                        f = Aq[i][c]
                        Aq[i] = [(Aq[i][k] - f * Aq[r_][k]) % p for k in range(nc)]
                r_ += 1
            rec(f'{rho} p={p}: rank of MY OWN G is {r_} = a_inf, so '
                f'i_det^inf = 0 over Q', r_ == ai, rank=r_)
        # the points must be traceless
        tl = all(sum(A[k][i][i] for i in range(4)) == 0 for A in pts for k in range(NV))
        rec(f'{rho}: every pencil matrix is traceless', tl)
        out['blocks'][str(rho)] = dict(a_inf=ai, raw=len(mine), i_det_inf=0)
    ok = all(c['ok'] for c in out['checks'])
    out['status'] = 'OK' if ok else 'FAILURES'
    with open(output, 'w', encoding='utf-8') as f:
        json.dump(out, f, indent=1)
    print(f'\nRESULT {out["status"]} '
          f'({sum(c["ok"] for c in out["checks"])}/{len(out["checks"])})')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
