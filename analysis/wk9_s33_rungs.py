#!/usr/bin/env python3
"""
Session 33 -- Phase 2: witness gate, reduction validation, and the rungs.

Reuses analysis/wk8_s30_core.py verbatim for: the corrected raising rule
(build_R), the unreduced measure(), restrict/eval_row/det_form, and every
rank/nullspace (flint nmod_mat; no hand-rolled elimination anywhere).

The registered rectangular-weight reduction (PREREG_s33.md section 2): for
lam = (delta^4), S_lam = det^delta is one-dimensional, so the highest-weight
space IS the invariant space and lies in the sign^delta-isotypic part V_chi of
the S_4 variable-permutation action; on V_chi, ker(E_12) is the whole
highest-weight space (E_23 = Ad P_(123) E_12, E_34 = Ad P_(13)(24) E_12, both
conjugators even).  Rows of E_12 are deduplicated by the (34)-swap of the
target weight (delta+1, delta-1, delta, delta): column values satisfy
v_swap(t) = (-1)^delta v_t, so non-canonical rows are scalar multiples of
canonical ones and (delta odd) swap-fixed rows vanish identically -- the
latter is asserted exactly, as a free correctness check.

Stages (argv): gate | v45 | rung <delta> [--p2-only|--both] [--seed N] [--npts N]
"""
import sys, time, itertools, random
sys.path.insert(0, 'analysis')
from wk8_s30_core import (exps, monomials, build_R, restrict, eval_row,
                          det_form, measure, nullspace, rank_of, _mat, P1, P2)
from flint import nmod_mat

E4 = exps(4, 4)
IDX4 = {a: k for k, a in enumerate(E4)}
PERMS4 = list(itertools.permutations(range(4)))
def _sgn(p):
    s = 1
    for i in range(4):
        for j in range(i + 1, 4):
            if p[i] > p[j]: s = -s
    return s
SGN4 = {p: _sgn(p) for p in PERMS4}
# monomial-index permutation tables: (sigma.alpha)[sigma(i)] = alpha[i]
PTAB = {}
for p in PERMS4:
    tab = [0] * 35
    for k, al in enumerate(E4):
        nx = [0] * 4
        for i in range(4): nx[p[i]] = al[i]
        tab[k] = IDX4[tuple(nx)]
    PTAB[p] = tab

# ladder anchors (results/e4_ledger.md, three independent routes)
A_LADDER = {4: 1, 5: 0, 6: 1, 7: 1, 8: 3}
NS_LADDER = {4: 465, 5: 2505, 6: 12652, 7: 57232, 8: 240481}
NCHI_LADDER = {4: 43, 5: 95, 6: 661, 7: 2310, 8: 10738}
NP_LADDER = {4: 404, 5: 2293, 6: 11624, 7: 53506, 8: 226348}

SWAP34 = (0, 1, 3, 2)

def log(*a):
    print(*a, file=sys.stderr); sys.stderr.flush()

# ------------------------------------------------------------------ the gate
def gate():
    """K1: binary quartics, closure{l^3 m}, lam = (4,4), delta = 2."""
    f = {(3, 1): 1}                      # x0^3 x1 as a binary quartic
    res = measure(f, 2, 4, 2, 2, (4, 4), a_expect=1)
    basis, R = build_R(4, 2, 2, (4, 4))
    E2 = exps(4, 2)
    want = (((0, 4), (4, 0)), ((1, 3), (3, 1)), ((2, 2), (2, 2)))
    got = tuple(tuple(E2[i] for i in m) for m in basis)
    assert got == want, ("witness basis order changed", got)
    ok = {}
    for p in (P1, P2):
        (v,) = nullspace(R, 3, p)
        inv = pow(v[2], p - 2, p)
        vn = tuple(x * inv % p for x in v)
        ok[p] = vn
        assert vn == (12 % p, (-3) % p, 1), ("K1 kernel wrong", p, vn)
        assert vn != (1, (-4) % p, 3 % p), "K1 wrong-rule signature"
    assert res['a'] == 1 and res['mult'] == 0, ("K1 mult wrong", res)
    print(f"GATE PASS: witness a=1 mult=0, kernel = (12,-3,1) at both primes "
          f"({ok[P1]}, {ok[P2]})")

# --------------------------------------------------- reduced pipeline pieces
def orbit_setup(delta):
    """basis, and the chi-valid S_4-orbit vectors (dict multiset -> +-1)."""
    lam = (delta,) * 4
    basis = monomials(4, 4, delta, lam)
    assert len(basis) == NS_LADDER[delta], (len(basis), NS_LADDER[delta])
    odd = delta % 2 == 1
    seen, vecs = set(), []
    for m in basis:
        if m in seen: continue
        acc = {}
        for p in PERMS4:
            t = PTAB[p]
            im = tuple(sorted(t[i] for i in m))
            ch = SGN4[p] if odd else 1
            acc[im] = acc.get(im, 0) + ch
        for im in acc: seen.add(im)
        if acc[m] == 0: continue           # chi nontrivial on stabiliser
        stab = 24 // len(acc)
        assert all(abs(v) == stab for v in acc.values()), (m, acc)
        vecs.append({im: (1 if v > 0 else -1) for im, v in acc.items()})
    assert len(vecs) == NCHI_LADDER[delta], (len(vecs), NCHI_LADDER[delta])
    return basis, vecs

def target_setup(delta):
    """canonical rows of the (34)-deduplicated E_12 target space."""
    tlam = (delta + 1, delta - 1, delta, delta)
    tbasis = monomials(4, 4, delta, tlam)
    assert len(tbasis) == NP_LADDER[delta], (len(tbasis), NP_LADDER[delta])
    tab = PTAB[SWAP34]
    tpos, fixed = {}, set()
    for t in tbasis:
        tw = tuple(sorted(tab[i] for i in t))
        if tw == t: fixed.add(t)
        if t <= tw and t not in tpos: tpos[t] = len(tpos)
    return tpos, fixed

def reduced_triples(delta, vecs, tpos, fixed):
    """(row, col, value) of E_12 on the chi-basis, canonical rows only.
    delta odd: contributions on swap-fixed rows must cancel exactly (asserted).
    """
    odd = delta % 2 == 1
    fx = {}
    tri = []
    for j, vec in enumerate(vecs):
        col = {}
        for m, s in vec.items():
            k = 0
            while k < len(m):
                i = m[k]; c = 1
                while k + c < len(m) and m[k + c] == i: c += 1
                al = E4[i]
                if al[1] > 0:
                    ni = IDX4[(al[0] + 1, al[1] - 1, al[2], al[3])]
                    nm = tuple(sorted(m[:k] + m[k + 1:k + c] + (ni,) + m[k + c:]))
                    val = s * c * (al[0] + 1)
                    if odd and nm in fixed:
                        fx[(nm, j)] = fx.get((nm, j), 0) + val
                    elif nm in tpos:
                        col[tpos[nm]] = col.get(tpos[nm], 0) + val
                k += c
        for r, v in col.items():
            if v: tri.append((r, j, v))
    if odd:
        bad = {k: v for k, v in fx.items() if v != 0}
        assert not bad, ("odd-fixed rows failed to cancel", list(bad)[:3])
    return tri

def kernel_reduced(delta, vecs, tpos, fixed, prime, block=6000):
    """a and the invariant kernel (in chi-coordinates) over F_prime, by
    flint rref on row blocks of the deduplicated E_12 matrix."""
    nchi = len(vecs)
    tri = reduced_triples(delta, vecs, tpos, fixed)
    nrows = len(tpos)
    log(f"  delta={delta} p={prime}: {nrows} dedup rows x {nchi} cols, "
        f"{len(tri)} nonzeros")
    tri.sort()
    ech = None      # accumulated echelon rows, list of row-lists
    ti, t0 = 0, time.time()
    for lo in range(0, nrows, block):
        hi = min(lo + block, nrows)
        rows = {}
        while ti < len(tri) and tri[ti][0] < hi:
            r, c, v = tri[ti]
            rows.setdefault(r, {})[c] = (rows.get(r, {}).get(c, 0) + v) % prime
            ti += 1
        blk = [rw for rw in rows.values() if any(rw.values())]
        prev = ech if ech else []
        ent = [0] * ((len(prev) + len(blk)) * nchi)
        for i, rw in enumerate(prev):
            ent[i * nchi:(i + 1) * nchi] = rw
        for i, rw in enumerate(blk):
            base = (len(prev) + i) * nchi
            for c, v in rw.items(): ent[base + c] = v % prime
        M = nmod_mat(len(prev) + len(blk), nchi, ent, prime)
        del ent
        Rm, rk = M.rref()   # python-flint 0.9: returns (rref matrix, rank)
        ech = [[int(Rm[i, c]) for c in range(nchi)] for i in range(rk)]
        del M, Rm
        log(f"    rows {lo}..{hi}: rank {rk}  ({time.time()-t0:.0f}s)")
    rk = len(ech)
    a = nchi - rk
    ent = [v for rw in ech for v in rw]
    Me = nmod_mat(rk, nchi, ent, prime)
    X, nul = Me.nullspace()
    assert nul == a
    kern = [[int(X[i, j]) for i in range(nchi)] for j in range(nul)]
    return a, rk, kern

def expand(vecs, kvec, prime):
    """chi-coordinates -> dict multiset -> value mod prime."""
    out = {}
    for j, coef in enumerate(kvec):
        if coef == 0: continue
        for m, s in vecs[j].items():
            out[m] = (out.get(m, 0) + s * coef) % prime
    return {m: v for m, v in out.items() if v}

DET4, NVAR = det_form(4)

def det_point_coeffs(rnd, bound=40):
    As = [[rnd.randint(-bound, bound) for _ in range(16)] for _ in range(4)]
    return restrict(DET4, 16, 4, 4, As), As

def eval_invariant(full, coeffs, prime):
    tot = 0
    for m, cf in full.items():
        v = cf
        for k in m:
            v = v * (coeffs.get(E4[k], 0) % prime) % prime
            if v == 0: break
        tot = (tot + v) % prime
    return tot

def rung(delta, primes=(P1, P2), seed=11, npts=None, bound=40):
    t0 = time.time()
    basis, vecs = orbit_setup(delta)
    tpos, fixed = target_setup(delta)
    a_exp = A_LADDER[delta]
    out = {}
    for prime in primes:
        a, rk, kern = kernel_reduced(delta, vecs, tpos, fixed, prime)
        assert a == a_exp, ("a mismatch vs plethysm", delta, prime, a, a_exp)
        assert rk == len(vecs) - a, ("rank(R) != n_chi - a", delta, prime)
        if a == 0:
            out[prime] = dict(a=0, mult=0); continue
        fulls = [expand(vecs, kv, prime) for kv in kern]
        K = npts if npts else a + 8
        rnd = random.Random(seed)
        rows = []
        for _ in range(K):
            coeffs, _As = det_point_coeffs(rnd, bound)
            rows.append([eval_invariant(f, coeffs, prime) for f in fulls])
        E = nmod_mat(K, a, [v for rw in rows for v in rw], prime)
        mult = E.rank()
        out[prime] = dict(a=a, mult=mult, kern=kern, fulls=fulls)
        log(f"  delta={delta} p={prime}: a={a} rank(R)={rk} mult={mult} "
            f"npts={K}  ({time.time()-t0:.0f}s)")
    ms = {p: out[p]['mult'] for p in primes}
    assert len(set(ms.values())) == 1, ("primes disagree", delta, ms)
    print(f"RUNG {delta}: a = {a_exp}, mult = {ms[primes[0]]}  "
          f"[n_chi = {len(vecs)}, dedup rows = {len(tpos)}, "
          f"primes = {primes}, seed = {seed}, {time.time()-t0:.0f}s]")
    return out

# ---------------------------------------------------------------- validation
def v45():
    """V2 (delta=4, both pipelines incl. kernel vector) and V4 (delta=5)."""
    # unreduced, s30 measure(); also its explicit kernel vector
    res = measure(det_form(4)[0], 16, 4, 4, 4, (4, 4, 4, 4), a_expect=1)
    assert res['a'] == 1 and res['mult'] == 1, ("V2 unreduced", res)
    basis, R = build_R(4, 4, 4, (4, 4, 4, 4))
    out = rung(4)
    for p in (P1, P2):
        (w,) = nullspace(R, len(basis), p)
        full = out[p]['fulls'][0]
        wv = [full.get(m, 0) for m in basis]
        i0 = next(i for i, x in enumerate(w) if x % p)
        assert wv[i0] % p, "V2: support mismatch"
        lam1, lam2 = w[i0] % p, wv[i0] % p
        assert all((x * lam2 - y * lam1) % p == 0 for x, y in zip(w, wv)), \
            ("V2 kernel vectors differ", p)
    print("V2 PASS: delta=4 reduced == unreduced (a=1, mult=1, same kernel "
          "vector at both primes)")
    out5 = rung(5)      # V4: odd branch, a must be 0
    assert all(out5[p]['a'] == 0 for p in (P1, P2))
    print("V4 PASS: delta=5 reduced kernel dimension 0 = a(5) (odd/sign branch, "
          "odd-fixed rows cancelled exactly)")

if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'gate': gate()
    elif cmd == 'v45': v45()
    elif cmd == 'rung':
        delta = int(sys.argv[2])
        kw = {}
        if '--seed' in sys.argv: kw['seed'] = int(sys.argv[sys.argv.index('--seed') + 1])
        if '--npts' in sys.argv: kw['npts'] = int(sys.argv[sys.argv.index('--npts') + 1])
        if '--p1-only' in sys.argv: kw['primes'] = (P1,)
        if '--p2-only' in sys.argv: kw['primes'] = (P2,)
        rung(delta, **kw)
