#!/usr/bin/env python3
"""
INDEPENDENT adversarial verification of session 77's bridge claims.

Writes its OWN SSYT generator (does NOT import wk12_s77_bridge for generation)
and its OWN drivers.  Relies only on the already-verified s69 circuit primitives
(wk11_s69_circuit: Filling, sym_table, symbols_from_coeffs, generic_point,
det_point, fast_eval_c, dp_eval_c, rank_mod) and wk8_s30_core (P1, P2, exps,
restrict).

Run:  python3 analysis/wk12_s77_verify.py [item1|item2|item3|all]
"""
import os, sys, json, math, random, itertools, time
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from wk8_s30_core import P1, P2, exps, restrict
from wk11_s69_circuit import (Filling, sym_table, symbols_from_coeffs, generic_point,
                              det_point, fast_eval_c, dp_eval_c, rank_mod)

PRIMES = (P1, P2)
T0 = time.time()
def log(*a): print(f"[{time.time()-T0:7.1f}s]", *a, flush=True)


# =====================================================================================
# MY OWN SSYT generator (tall/two/one layout of lambda' = (h,h,2^n2,1^n1)).
# An SSYT of shape lambda=(2+n2+n1, 2+n2, 2^{h-2}) with content (n^delta):
#   values 0..delta-1 each used exactly n times, strictly increasing DOWN every
#   column, weakly increasing ALONG every row.
# Layout -> Filling:  C1 = column 0 (rows 0..h-1); C2 = column 1; two[e] = (row0,row1)
# of two-column e; one = row-0 tail (one-columns).
# =====================================================================================
def my_is_ssyt(F):
    """Independent SSYT check on a Filling in the tall/two/one layout."""
    h = F.h
    if any(F.C1[r] >= F.C1[r+1] for r in range(h-1)): return False   # C1 strict down
    if any(F.C2[r] >= F.C2[r+1] for r in range(h-1)): return False   # C2 strict down
    if any(a >= b for a, b in F.two): return False                   # two-col strict down
    row0 = [F.C1[0], F.C2[0]] + [a for a, _ in F.two] + list(F.one)  # row 0 weak
    if any(row0[i] > row0[i+1] for i in range(len(row0)-1)): return False
    row1 = [F.C1[1], F.C2[1]] + [b for _, b in F.two]                # row 1 weak
    if any(row1[i] > row1[i+1] for i in range(len(row1)-1)): return False
    if any(F.C1[r] > F.C2[r] for r in range(2, h)): return False     # rows 2..h-1 weak
    return True


def complete_tall(h, n, delta, n2, n1, C1, C2, limit=None):
    """Given tall columns C1, C2 (strictly-increasing h-tuples with C1[r] <= C2[r]),
    DETERMINISTICALLY enumerate the SSYT completions: the n2 two-columns (weakly
    increasing tops from C2[0], weakly increasing bottoms from C2[1], strict down)
    and the forced one-columns (sorted leftover, row-0 junction checked).  Increasing
    value order + count pruning => well-behaved (never explodes)."""
    cnt = [0]*delta
    for l in C1: cnt[l] += 1
    for l in C2: cnt[l] += 1
    if max(cnt, default=0) > n:
        return
    two = []; emitted = [0]

    def cand(lo):
        return [v for v in range(lo, delta) if cnt[v] < n]

    def finish_ones():
        remaining = []
        for l in range(delta):
            remaining += [l]*(n - cnt[l])
        if len(remaining) != n1:
            return None
        remaining.sort()
        last_row0 = two[-1][0] if n2 >= 1 else C2[0]
        if n1 and remaining[0] < last_row0:
            return None
        return remaining

    def rec_two(e):
        if e == n2:
            one = finish_ones()
            if one is not None:
                yield Filling(h, n, delta, list(C1), list(C2), list(two), one)
            return
        lo_top = two[-1][0] if e > 0 else C2[0]
        lo_bot_base = two[-1][1] if e > 0 else C2[1]
        for a in cand(lo_top):
            cnt[a] += 1
            for b in cand(max(lo_bot_base, a+1)):
                cnt[b] += 1; two.append((a, b))
                yield from rec_two(e+1)
                two.pop(); cnt[b] -= 1
            cnt[a] -= 1

    for F in rec_two(0):
        yield F; emitted[0] += 1
        if limit is not None and emitted[0] >= limit:
            return


def tall_pairs(h, delta, kset=None, order=None):
    """Enumerate tall-column pairs (C1, C2): strictly-increasing h-subsets of 0..delta-1
    with C1[r] <= C2[r] for all r (the SSYT row-weak constraint on the two tall columns).
    kset (if given) restricts |C1 cap C2|.  order = optional Random to shuffle the pair
    order (safe: only reorders which pair is tried first; each pair is genuine)."""
    cols = list(itertools.combinations(range(delta), h))
    pairs = []
    for C1 in cols:
        s1 = set(C1)
        for C2 in cols:
            if any(C1[r] > C2[r] for r in range(h)):
                continue
            if kset is not None and len(s1 & set(C2)) not in kset:
                continue
            pairs.append((C1, C2))
    if order is not None:
        order.shuffle(pairs)
    return pairs


def gen_ssyt(h, n, delta, n2, n1, rng=None, limit=None, kset=None):
    """Stream genuine SSYT (Filling objects).  rng=None: deterministic lex order over
    (C1,C2) then completions.  rng given: the (C1,C2) ORDER is shuffled for diversity,
    completions stay deterministic.  kset restricts tall-column overlap."""
    assert 2*h + 2*n2 + n1 == n*delta
    emitted = 0
    for C1, C2 in tall_pairs(h, delta, kset=kset, order=rng):
        for F in complete_tall(h, n, delta, n2, n1, C1, C2):
            yield F
            emitted += 1
            if limit is not None and emitted >= limit:
                return


# =====================================================================================
# ITEM 1 : n=3 LMR control, independently
# =====================================================================================
N3 = dict(n=3, r=7, h=7, delta=12, n2=5, n1=12, lam=(19, 7, 2, 2, 2, 2, 2), a=6)


def ev(F, ms, p, tab):
    """evaluate F_T(point) via the s69 circuit (dp if pathwidth ok, else fast)."""
    try:
        return dp_eval_c(F, ms, p, tab) % p
    except Exception:
        return fast_eval_c(F, ms, p, tab) % p


def item1():
    C = N3; n, r, h, delta, n2, n1, a = C["n"], C["r"], C["h"], C["delta"], C["n2"], C["n1"], C["a"]
    A, idx, fact, tab = sym_table(n, r)
    log(f"ITEM 1  cell lam={C['lam']} delta={delta} n={n} r={r} h={h} n2={n2} n1={n1} a={a}")
    log(f"        content = ({n}^{delta})  (n=3 => each letter used 3 times; task's '(4^12)' is the n=4 statement)")

    # precompute all valid tall-column pairs (C1,C2) grouped by overlap k
    allpairs = tall_pairs(h, delta)
    pairs_by_k = {}
    for C1, C2 in allpairs:
        k = len(set(C1) & set(C2)); pairs_by_k.setdefault(k, []).append((C1, C2))
    log(f"  tall pairs by k = { {kk: len(v) for kk, v in sorted(pairs_by_k.items())} }")

    # ---- 1a+1c. Deterministic lex SSYT stream: first-nonzero, and greedy generic-rank
    # basis built directly from it (my own generator, my own generic points/seeds).  A
    # cheap 1-point zero-filter (gp[0]) skips the many zero fillings before the full
    # multi-point rank test.  This mirrors the session's deterministic-stream method with
    # an INDEPENDENT generator, generator order, and evaluation points. ------------------
    gp = [symbols_from_coeffs(generic_point(n, r, P1, random.Random(2000003*i + 111)), n, r, P1)
          for i in range(a+2)]
    first_nz = None; scanned = 0; nz = 0; kdist = {}
    basis, rows = [], []
    for F in gen_ssyt(h, n, delta, n2, n1, rng=None, limit=12000):
        assert my_is_ssyt(F)
        scanned += 1
        k = len(set(F.C1) & set(F.C2)); kdist[k] = kdist.get(k, 0) + 1
        if ev(F, gp[0], P1, tab) == 0:
            continue
        nz += 1
        if first_nz is None:
            first_nz = scanned
        if len(basis) < a:
            row = [ev(F, ms, P1, tab) for ms in gp]
            if rank_mod(rows + [row], P1) > len(rows):
                rows.append(row); basis.append(F)
                log(f"     +basis {len(basis)} (SSYT #{scanned}, k={k}, C1={F.C1}, C2={F.C2})")
                if len(basis) == a:
                    log(f"     reached generic rank {a} at SSYT #{scanned}")
                    break
    log(f"  1a lex stream: scanned {scanned} SSYT, {nz} nonzero, first nonzero at #{first_nz}")
    log(f"     k-distribution over lex-scanned SSYT: {dict(sorted(kdist.items()))}")
    log(f"  1c greedy: reached generic rank {len(basis)}/{a} from deterministic SSYT stream")
    if len(basis) < a:
        log("  !!! DISCREPANCY: could not reach generic rank a=6 from SSYT")
        return dict(item1="DISCREPANCY_span", basis_size=len(basis))

    # ---- 1b. n=3 k-vanishing spot check (adversarial): all k<=3 must be zero --------
    # h-k>n  <=>  7-k>3  <=>  k<4  =>  F_T=0.  Nonzero requires k>=4.
    bad_kle3 = []; nz_by_k = {}; seen_by_k = {}
    checkpts = [symbols_from_coeffs(generic_point(n, r, P1, random.Random(700000+i)), n, r, P1) for i in range(3)]
    for k in range(0, h+1):
        prs = list(pairs_by_k.get(k, []))
        random.Random(4000+k).shuffle(prs)
        seen = 0
        for C1, C2 in prs[:40]:
            for F in complete_tall(h, n, delta, n2, n1, C1, C2, limit=2):
                seen += 1
                vals = [ev(F, cp, P1, tab) for cp in checkpts]
                if any(vals):
                    nz_by_k[k] = nz_by_k.get(k, 0) + 1
                    if k <= 3:
                        bad_kle3.append((F.key(), k, vals))
        seen_by_k[k] = seen
    log(f"  1b k-vanishing (n=3): sampled-by-k = {dict(sorted(seen_by_k.items()))}")
    log(f"     nonzero-by-k        = {dict(sorted(nz_by_k.items()))}  (must be 0 for k<=3)")
    log(f"     SSYT with k<=3 that are NONzero: {len(bad_kle3)}  (must be 0)")

    # ---- confirm generic rank 6 at BOTH primes, fresh points ------------------------
    grank = {}
    for p in PRIMES:
        gpp = [symbols_from_coeffs(generic_point(n, r, p, random.Random(3000017*i + 991)), n, r, p)
               for i in range(a+6)]
        M = [[ev(F, ms, p, tab) for ms in gpp] for F in basis]
        grank[p] = rank_mod(M, p)
    log(f"  1c generic rank both primes (fresh pts): { {str(p): grank[p] for p in PRIMES} }  (expect 6,6)")

    # ---- 1d. det_3 pencils: rank should be 5, i_det = a - rank = 1 ------------------
    det_rng = random.Random(9090909)
    det_cv = [det_point(n, r, det_rng, bound=30)[0] for _ in range(a+10)]
    det_rank = {}
    for p in PRIMES:
        msd = [symbols_from_coeffs(cv, n, r, p) for cv in det_cv]
        M = [[ev(F, ms, p, tab) for ms in msd] for F in basis]
        det_rank[p] = rank_mod(M, p)
    idet = {p: a - det_rank[p] for p in PRIMES}
    log(f"  1d det rank both primes: { {str(p): det_rank[p] for p in PRIMES} }  (expect 5,5)")
    log(f"     i_det = a - rank    : { {str(p): idet[p] for p in PRIMES} }  (expect 1,1)")

    # ---- 1e. HWV check by explicit upper-unitriangular substitution ------------------
    hwv = hwv_check(basis[:3], n, r, tab)

    return dict(item1_first_nonzero_lex=first_nz, item1_lex_kdist=kdist,
                item1_bad_kle3=len(bad_kle3), item1_nz_by_k=nz_by_k,
                item1_generic_rank={str(p): grank[p] for p in PRIMES},
                item1_det_rank={str(p): det_rank[p] for p in PRIMES},
                item1_i_det={str(p): idet[p] for p in PRIMES},
                item1_hwv=hwv)


def transform_coeffs(cv, g, n, r, p):
    """coefficients of the form  f(g.s)  (= f composed with g),  where cv are the
    coefficients of f over exps(n,r) and g is an r x r matrix (mod p).
    restrict substitutes old-var t -> sum_i As[i][t] s_i ; taking As = g^T gives
    old-var t -> sum_i g[t][i] s_i = (g s)_t, i.e. the form f(g s)."""
    A = exps(n, r)
    fdict = {A[i]: int(cv[i]) % p for i in range(len(A)) if cv[i] % p}
    AsT = [[g[t][i] % p for t in range(r)] for i in range(r)]     # As[i][t] = g[t][i]
    out = restrict(fdict, r, n, r, AsT)
    return [int(out.get(al, 0)) % p for al in A]


def rand_unitri(r, rng, p, upper=True):
    g = [[0]*r for _ in range(r)]
    for i in range(r):
        g[i][i] = 1
        for j in range(r):
            if (upper and j > i) or (not upper and j < i):
                g[i][j] = rng.randrange(p)
    return g


def hwv_check(basis, n, r, tab):
    """For each filling F and random g: F_T(f o g) should EQUAL F_T(f) for g upper-
    unitriangular (Identity 1), and generically DIFFER for lower-unitriangular g
    (negative control confirming F_T is a *highest* (not lowest) weight vector)."""
    out = []
    for bi, F in enumerate(basis):
        for p in PRIMES:
            crng = random.Random(4242 + 17*bi + p % 1000)
            cv = generic_point(n, r, p, crng)
            ms = symbols_from_coeffs(cv, n, r, p)
            base = ev(F, ms, p, tab)
            for gi in range(3):
                grng = random.Random(88 + 31*gi + 7*bi)
                gu = rand_unitri(r, grng, p, upper=True)
                cvU = transform_coeffs(cv, gu, n, r, p)
                valU = ev(F, symbols_from_coeffs(cvU, n, r, p), p, tab)
                gl = rand_unitri(r, grng, p, upper=False)
                cvL = transform_coeffs(cv, gl, n, r, p)
                valL = ev(F, symbols_from_coeffs(cvL, n, r, p), p, tab)
                out.append(dict(filling=bi, p=p, g=gi, base=base,
                                upper_equal=(valU == base), lower_equal=(valL == base)))
    n_up_ok = sum(1 for o in out if o["upper_equal"])
    n_low_diff = sum(1 for o in out if not o["lower_equal"])
    log(f"  1e HWV: upper-unitriangular invariance holds {n_up_ok}/{len(out)} (expect all); "
        f"lower-unitriangular differs {n_low_diff}/{len(out)} (negative control)")
    fails = [o for o in out if not o["upper_equal"]]
    if fails:
        log(f"  !!! DISCREPANCY: {len(fails)} upper-unitriangular HWV checks FAILED: {fails[:3]}")
    return dict(n_checks=len(out), upper_invariant=n_up_ok, lower_differs=n_low_diff,
                all_upper_ok=(n_up_ok == len(out)))


# =====================================================================================
# ITEM 2 : k-reconciliation at n=4  (proved vanishing  h-k>n => F_T=0)
# =====================================================================================
def item2():
    from wk11_s69_circuit import random_filling
    n, r, h = 4, 9, 9
    # 2h + 2 n2 + n1 = n*delta = 72.  n2=6,n1=42 keeps k=0..9 instantiable but makes the
    # 2^{n2} evaluation cheap; the vanishing test h-k>n depends only on h,k,n (not n2,n1).
    delta, n2, n1 = 18, 6, 42
    assert 2*h + 2*n2 + n1 == n*delta
    A, idx, fact, tab = sym_table(n, h)
    log(f"ITEM 2  n={n} h={h} r={r} delta={delta} n2={n2} n1={n1};  vanishing test h-k>n <=> k<={h-n-1} => 0")
    # generic points, both primes, my own seeds
    ms = {p: [symbols_from_coeffs(generic_point(n, r, p, random.Random(80808*i + 5)), n, r, p)
              for i in range(2)] for p in PRIMES}
    per_k = 8
    nz_by_k = {}; tested_by_k = {}; bad = []
    examples = {}
    for k in range(0, h+1):
        rng = random.Random(50000 + k)
        made = 0; nzc = 0
        for _try in range(per_k*20):
            if made >= per_k:
                break
            try:
                F = random_filling(h, n, delta, n2, n1, rng, k=k)
            except RuntimeError:
                continue
            if len(set(F.C1) & set(F.C2)) != k:
                continue
            made += 1
            vals = {}
            nonzero = False
            for p in PRIMES:
                vv = [fast_eval_c(F, m, p, tab) % p for m in ms[p]]
                vals[p] = vv
                if any(vv):
                    nonzero = True
            if nonzero:
                nzc += 1
                examples.setdefault(k, F)
            if k <= (h - n - 1) and nonzero:          # k<=4 must be zero
                bad.append((k, F.key(), vals))
        tested_by_k[k] = made; nz_by_k[k] = nzc
        log(f"   k={k}: tested {made}, nonzero {nzc}  {'<-- MUST be 0' if k<=h-n-1 else ''}")
    ok = (len(bad) == 0)
    log(f"  vanishing k<= {h-n-1}: {'CONFIRMED (all zero)' if ok else f'DISCREPANCY: {len(bad)} nonzero!'}")
    log(f"  nonzero-by-k = {nz_by_k}  (nonzero expected for high k incl k={h})")
    if bad:
        for b in bad[:3]:
            log(f"    !!! k={b[0]} NONZERO: {b[2]}")
    return dict(item2_tested_by_k=tested_by_k, item2_nz_by_k=nz_by_k,
                item2_kle4_all_zero=ok, item2_kmax_nonzero=(nz_by_k.get(h, 0) > 0))


# =====================================================================================
# ITEM 3 : internal consistency of the session's banked-comparison JSON
# =====================================================================================
def item3():
    log("ITEM 3  internal consistency of results/s77_control_n3.json vs banked artefact")
    bpath = os.path.join(ROOT, "results", "artefacts", "s69_banked_n3_d12.json")
    bk = json.load(open(bpath))
    vec = bk["vector_chi_coords"]
    b_support = sum(1 for x in vec if x)
    b_maxabs = max(abs(x) for x in vec)
    log(f"  banked artefact: n_chi={len(vec)}  support={b_support} (claim 3900)  max|c|={b_maxabs} (claim 544)")
    log(f"  banked header fields: support={bk.get('support')}  max_abs_coeff={bk.get('max_abs_coeff')}")
    sc = json.load(open(os.path.join(ROOT, "results", "s77_control_n3.json")))
    a = sc["a"]
    det_rank = {p: sc["det_rank"][p] for p in sc["det_rank"]}
    idet = {p: sc["i_det"][p] for p in sc["i_det"]}
    kdim = {p: sc["kernel_dim"][p] for p in sc["kernel_dim"]}
    checks = []
    checks.append(("banked support == 3900", b_support == 3900))
    checks.append(("banked max_abs == 544", b_maxabs == 544))
    checks.append(("banked header support == 3900", bk.get("support") == 3900))
    checks.append(("banked header max_abs_coeff == 544", bk.get("max_abs_coeff") == 544))
    for p in sc["det_rank"]:
        checks.append((f"i_det[{p}] == a - det_rank  ({a}-{det_rank[p]})", idet[p] == a - det_rank[p]))
        checks.append((f"i_det[{p}] == 1", idet[p] == 1))
        checks.append((f"det_rank[{p}] == 5", det_rank[p] == 5))
        checks.append((f"kernel_dim[{p}] == i_det[{p}] (1-dim det kernel)", kdim[p] == idet[p]))
    bmod = sc["banked"]["mod_p"]
    for p in bmod:
        checks.append((f"mod_p[{p}].support_u == 3900", bmod[p].get("support_u") == 3900))
        checks.append((f"mod_p[{p}].support_banked == 3900", bmod[p].get("support_banked") == 3900))
        checks.append((f"mod_p[{p}].proportional == True", bmod[p].get("proportional") is True))
        checks.append((f"mod_p[{p}].mismatches == 0", bmod[p].get("mismatches") == 0))
    oz = sc["banked"]["over_Z"]
    checks.append(("over_Z.support == 3900 == banked support", oz.get("support") == 3900 == b_support))
    checks.append(("over_Z.max_abs == 544 == banked max|c|", oz.get("max_abs") == 544 == b_maxabs))
    checks.append(("over_Z.equal_up_to_sign == True", oz.get("equal_up_to_sign") is True))
    checks.append(("over_Z.E_u_nonzero_rows == 0 (U_D is a HWV)", oz.get("E_u_nonzero_rows") == 0))
    checks.append(("banked.semantics_ok == True", sc["banked"].get("semantics_ok") is True))
    allok = True
    for name, ok in checks:
        log(f"    [{'OK' if ok else 'FAIL'}] {name}")
        allok = allok and ok
    log(f"  ITEM 3: session JSON internally consistent = {allok}")
    return dict(item3_banked_support=b_support, item3_banked_maxabs=b_maxabs,
                item3_all_consistent=allok,
                item3_failed=[name for name, ok in checks if not ok])


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    res = {}
    if which in ("item1", "all"):
        res.update(item1())
    if which in ("item2", "all"):
        res.update(item2())
    if which in ("item3", "all"):
        res.update(item3())
    print("\n=== RESULT JSON ===")
    print(json.dumps(res, indent=1, default=str))
