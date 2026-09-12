#!/usr/bin/env python3
"""B14-02 control C3 -- an independent EXACT-INTEGER bracket evaluator.

Shares no algorithm and no code with the fast modular path
(`wk12_s74_dpc.c` / `dp_eval_compact`, a transfer-matrix DP over letters with
slot states, in Z/p).  This module goes back to the Leibniz definition and
computes in exact Z.

Definition (docs/compact_circuit.md; the same sum brute_force_eval writes out):

    F_T(f) = sum_{sigma_1,sigma_2 in S_h} sum_{s in {0,1}^{n2}}
                sgn(sigma_1) sgn(sigma_2) (-1)^{|s|} prod_{l} m_{alpha_l(sigma,s)}

Derivation used here, from that definition and nothing else.  Each letter sits
in at most one cell of C1 and at most one cell of C2 (column-strict), so with

  * pi  : any bijection C1-rows -> C2-rows sending a shared letter's C1 row to
          its C2 row, and pairing the C1-only letters with the C2-only letters
          (this module uses the plain order-preserving pairing, not the
          2-edge-maximising heuristic the house evaluator uses -- the identity
          below holds for ANY such bijection);
  * M_k(s)[i][j] = m_alpha for the shared letter of C1-row k, or
                   m_alpha(l;i) * m_alpha(m;j) for a paired (C1-only, C2-only);
  * N(s)         = product of the letters in neither tall column,

the double permutation sum collapses:

    sum_{sigma,rho} sgn(sigma) sgn(rho) prod_k M_k(sigma(k), rho(k))
        = sum_{S subset [h]} (-1)^{h-|S|} det( sum_{k in S} M_k )

because expanding det(sum_{k in S} M_k) multilinearly in rows and applying
inclusion-exclusion over S retains exactly the bijective row->matrix
assignments.  Hence

    F_T(f) = sgn(pi) * sum_s (-1)^{|s|} N(s)
                       * sum_{S subset [h]} (-1)^{h-|S|} det(sum_{k in S} M_k(s))

with every quantity an exact integer.  `validate_small()` checks this module
against the literal Leibniz sum (`brute_force_eval`) on small shapes where the
definition is directly computable.

Symbols are keyed by the exponent tuple alpha, never by a position in an
`exps()` list, so the house's two opposite orderings cannot reach this file.
"""
import argparse, itertools, json, math, os, sys, time
import numpy as np
from flint import fmpz_mat

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

DEG, NLEG, HH = 13, 4, 9
T0 = time.time()


def log(*a):
    print(f"[{time.time()-T0:8.1f}s]", *a, flush=True)


# ------------------------------------------------------------------ symbols
def quartic_dict_from_point(pt, cubic_exponents):
    """{alpha : c_alpha}  for f = l * c, keyed by exponent tuple."""
    lin, cub = pt["linear"], pt["cubic_coefficients"]
    q = {}
    for al, cc in zip(cubic_exponents, cub):
        if cc == 0:
            continue
        for i, li in enumerate(lin):
            if li == 0:
                continue
            a = list(al)
            a[i] += 1
            k = tuple(a)
            q[k] = q.get(k, 0) + li * cc
    return {k: v for k, v in q.items() if v}


def symbol_fn(qdict, r):
    """m_alpha = alpha! * c_alpha, from a multiset of leg indices."""
    def m(ids):
        a = [0] * r
        for i in ids:
            a[i] += 1
        t = tuple(a)
        c = qdict.get(t, 0)
        if c == 0:
            return 0
        f = 1
        for x in t:
            if x > 1:
                f *= math.factorial(x)
        return f * c
    return m


# ------------------------------------------------------------------ structure
def letter_cells(C1, C2, two, one, delta):
    """letter -> ('C1',row) / ('C2',row) / ('two',edge,row) / ('one',)"""
    cells = [[] for _ in range(delta)]
    for k, l in enumerate(C1):
        cells[l].append(("C1", k))
    for k, l in enumerate(C2):
        cells[l].append(("C2", k))
    for e, (a, b) in enumerate(two):
        cells[a].append(("two", e, 0))
        cells[b].append(("two", e, 1))
    for l in one:
        cells[l].append(("one",))
    return cells


def build_units(C1, C2, delta):
    """my own pairing: order-preserving between C1-only and C2-only letters."""
    h = len(C1)
    posC2 = {l: k for k, l in enumerate(C2)}
    setC1, setC2 = set(C1), set(C2)
    U1 = [l for l in C1 if l not in setC2]              # C1 order
    U2 = [l for l in C2 if l not in setC1]              # C2 order
    assert len(U1) == len(U2)
    pair = dict(zip(U1, U2))
    units, pi = [], []
    for k, l in enumerate(C1):
        if l in setC2:
            units.append(("shared", l))
            pi.append(posC2[l])
        else:
            m = pair[l]
            units.append(("pair", l, m))
            pi.append(posC2[m])
    assert sorted(pi) == list(range(h))
    sgn = 1
    for i in range(h):
        for j in range(i + 1, h):
            if pi[i] > pi[j]:
                sgn = -sgn
    neither = [l for l in range(delta) if l not in setC1 and l not in setC2]
    return units, neither, sgn


def leg_tables(cells, msym, delta, h, r):
    """per letter: bits-indexed table over (i, j) of the C1/C2 legs."""
    tabs = []
    for l in range(delta):
        cl = cells[l]
        inC1 = any(c[0] == "C1" for c in cl)
        inC2 = any(c[0] == "C2" for c in cl)
        edges = [(c[1], c[2]) for c in cl if c[0] == "two"]
        nones = sum(1 for c in cl if c[0] == "one")
        d2 = len(edges)
        T = {}
        for i in (range(h) if inC1 else [None]):
            for j in (range(h) if inC2 else [None]):
                for bits in range(1 << d2):
                    ids = [0] * nones
                    if i is not None:
                        ids.append(i)
                    if j is not None:
                        ids.append(j)
                    for q in range(d2):
                        ids.append((bits >> q) & 1)
                    T[(i, j, bits)] = msym(ids)
        tabs.append((inC1, inC2, edges, T))
    return tabs


def bits_for(edges, s, sabotage=None):
    b = 0
    for q, (e, side) in enumerate(edges):
        se = (s >> e) & 1
        if sabotage == 'flipbits':
            se = 1 - se
        elif sabotage == 'flipone' and e == 0:
            se = 1 - se
        b |= (se if side == 0 else 1 - se) << q
    return b


# ------------------------------------------------------------------ evaluator
def exact_eval(C1, C2, two, one, delta, h, r, msym, progress=None, sabotage=None):
    cells = letter_cells(C1, C2, two, one, delta)
    units, neither, pisgn = build_units(C1, C2, delta)
    if sabotage == 'nosign':
        pisgn = 1
    tabs = leg_tables(cells, msym, delta, h, r)
    n2 = len(two)
    total = 0
    grey = [0] * (1 << h)
    for S in range(1, 1 << h):
        grey[S] = (S ^ (S >> 1))
    order = [(S ^ (S >> 1)) for S in range(1 << h)]        # Gray code over subsets
    flip = [None] * (1 << h)
    for t in range(1, 1 << h):
        flip[t] = (order[t] ^ order[t - 1]).bit_length() - 1
    par = [(-1) ** ((h - bin(order[t]).count("1")) % 2) for t in range(1 << h)]
    if sabotage == 'noincl':
        par = [1] * (1 << h)
    for s in range(1 << n2):
        N = 1
        for l in neither:
            inC1, inC2, edges, T = tabs[l]
            N *= T[(None, None, bits_for(edges, s, sabotage))]
            if N == 0:
                break
        if N == 0:
            continue
        Ms = []
        for u in units:
            if u[0] == "shared":
                inC1, inC2, edges, T = tabs[u[1]]
                b = bits_for(edges, s, sabotage)
                Ms.append(np.array([[T[(i, j, b)] for j in range(h)] for i in range(h)], dtype=object))
            else:
                _, _, e1, T1 = tabs[u[1]]
                _, _, e2, T2 = tabs[u[2]]
                b1, b2 = bits_for(e1, s, sabotage), bits_for(e2, s, sabotage)
                v = np.array([T1[(i, None, b1)] for i in range(h)], dtype=object)
                w = np.array([T2[(None, j, b2)] for j in range(h)], dtype=object)
                Ms.append(np.outer(v, w))
        acc = np.zeros((h, h), dtype=object)
        inner = 0
        for t in range(1 << h):
            if t:
                acc = acc + Ms[flip[t]] if (order[t] & (1 << flip[t])) else acc - Ms[flip[t]]
            if order[t] == 0:
                continue
            d = fmpz_mat(h, h, [int(x) for x in acc.ravel()]).det()
            inner += par[t] * int(d)
        sp = 1 if sabotage == 'noparity' else (-1 if bin(s).count("1") & 1 else 1)
        total += sp * N * inner
        if progress and (s & 4095) == 4095:
            log(f"    {progress}: s={s+1}/{1<<n2}")
    return pisgn * total


# ------------------------------------------------------------------ validation
def validate_small(trials=4, seed=1402, need_nonzero=12):
    """this module vs the LITERAL Leibniz sum (brute_force_eval) on small shapes.

    A control that only ever compares zeros cannot fail, so this requires a
    stated number of NONZERO agreements, and finishes with a deliberately
    corrupted input that the comparison must reject."""
    import random
    from wk11_s69_circuit import random_filling, brute_force_eval, sym_table
    from wk8_s30_core import exps
    rng = random.Random(seed)
    P = 2 ** 61 - 1                       # large enough to read values as integers
    # (h, n, delta, n2, n1) with 2h + 2*n2 + n1 == n*delta
    shapes = [(3, 3, 3, 1, 1), (3, 3, 3, 0, 3), (3, 4, 3, 3, 0), (3, 4, 3, 2, 2),
              (4, 3, 4, 2, 0), (4, 4, 4, 4, 0), (4, 4, 4, 3, 2), (5, 4, 5, 5, 0),
              (2, 4, 2, 2, 0)]
    out, nz, bad = [], 0, 0
    for (h, n, delta, n2, n1) in shapes:
        assert 2 * h + 2 * n2 + n1 == n * delta, (h, n, delta, n2, n1)
        A = exps(n, h)
        _, _, _, tab = sym_table(n, h)
        for t in range(trials):
            F = random_filling(h, n, delta, n2, n1, rng)
            msl = [rng.randrange(1, 40) for _ in A]
            bf = brute_force_eval(F, [x % P for x in msl], P, tab)
            qd = {al: msl[k] for k, al in enumerate(A)}
            def msym(ids, qd=qd, r=h):
                a = [0] * r
                for i in ids:
                    a[i] += 1
                return qd.get(tuple(a), 0)
            mine = exact_eval(F.C1, F.C2, F.two, F.one, delta, h, h, msym)
            ok = (mine % P) == bf
            nz += (mine != 0)
            bad += (not ok)
            out.append(dict(shape=[h, n, delta, n2, n1], trial=t, mine=str(mine),
                            brute_mod=bf, nonzero=mine != 0, ok=ok))
        agree = sum(1 for o in out if o["shape"] == [h, n, delta, n2, n1] and o["ok"])
        nzs = sum(1 for o in out if o["shape"] == [h, n, delta, n2, n1] and o["nonzero"])
        log(f"  h={h} n={n} d={delta} n2={n2} n1={n1}: {agree}/{trials} agree, {nzs} nonzero")
    log(f"  TOTAL {len(out)} cases, {len(out)-bad} agree, {nz} nonzero "
        f"(need >= {need_nonzero})")
    # ---- deliberate failures.  The first attempt at this control was VACUOUS:
    # it shifted msl[0], the symbol at exponent (0,..,0,n), which the sampled
    # fillings never use, so the comparison accepted the corrupted input.  That
    # is check_must_be_able_to_fail in miniature and it is reported as such.
    h, n, delta, n2, n1 = 4, 4, 4, 4, 0
    A = exps(n, h); _, _, _, tab = sym_table(n, h)
    F = random_filling(h, n, delta, n2, n1, rng)
    msl = [rng.randrange(1, 40) for _ in A]
    while brute_force_eval(F, [x % P for x in msl], P, tab) == 0:
        F = random_filling(h, n, delta, n2, n1, rng)
        msl = [rng.randrange(1, 40) for _ in A]
    bf = brute_force_eval(F, [x % P for x in msl], P, tab)

    def mk(vals):
        qd = {al: vals[k] for k, al in enumerate(A)}
        def f(ids, qd=qd, r=h):
            a = [0] * r
            for i in ids:
                a[i] += 1
            return qd.get(tuple(a), 0)
        return f

    # (a) corrupt a symbol the filling ACTUALLY uses -- chosen by requiring the
    #     definition's own value to move, so the input provably must be rejected
    used = None
    for kk in range(len(A)):
        c = list(msl); c[kk] += 1
        if brute_force_eval(F, [x % P for x in c], P, tab) != bf:
            used = kk
            break
    assert used is not None, "no symbol moves the definition: shape is degenerate"
    mine_bad = exact_eval(F.C1, F.C2, F.two, F.one, delta, h, h, mk(
        [v + (1 if i == used else 0) for i, v in enumerate(msl)]))
    a_rejected = (mine_bad % P) != bf
    log(f"  MUST-FAIL (a) symbol at exps index {used} shifted +1 (definition moves): "
        f"{'REJECTED, control can fail' if a_rejected else 'ACCEPTED -- VACUOUS'}")

    # (b) the control that matters: sabotage THIS EVALUATOR and confirm the
    #     comparison against the definition rejects it.  Run over several
    #     nonzero cases, including odd n2, because one mode is a genuine
    #     SYMMETRY at even n2 (see below) and a single even-n2 case would have
    #     reported it as a passing check.
    battery = [(3, 4, 3, 2, 2), (4, 4, 4, 4, 0), (2, 4, 2, 2, 0),     # even n2
               (2, 3, 3, 1, 3), (2, 3, 5, 3, 5), (2, 3, 6, 3, 8)]     # odd  n2
    # the odd-n2 shapes were SEARCHED FOR: the first three tried had identically
    # zero bracket spaces, which would have left the flipbits mode untested.
    cases = []
    for (hh, nn, dd, e2, e1) in battery:
        assert 2 * hh + 2 * e2 + e1 == nn * dd, (hh, nn, dd, e2, e1)
        AA = exps(nn, hh); _, _, _, tt = sym_table(nn, hh)
        for _try in range(60):
            FF = random_filling(hh, nn, dd, e2, e1, rng)
            vv = [rng.randrange(1, 40) for _ in AA]
            b = brute_force_eval(FF, [x % P for x in vv], P, tt)
            if b:
                cases.append((hh, nn, dd, e2, e1, FF, AA, vv, b))
                break
    log(f"  sabotage battery: {len(cases)} nonzero cases "
        f"({sum(1 for c in cases if c[3] % 2) } with odd n2)")
    sab = {}
    for mode in ("nosign", "noparity", "noincl", "flipone", "flipbits"):
        rej_odd = rej_even = tot_odd = tot_even = 0
        for (hh, nn, dd, e2, e1, FF, AA, vv, b) in cases:
            qd = {al: vv[k] for k, al in enumerate(AA)}
            def f(ids, qd=qd, r=hh):
                a = [0] * r
                for i in ids:
                    a[i] += 1
                return qd.get(tuple(a), 0)
            v = exact_eval(FF.C1, FF.C2, FF.two, FF.one, dd, hh, hh, f, sabotage=mode)
            r_ = (v % P) != b
            if e2 % 2:
                tot_odd += 1; rej_odd += r_
            else:
                tot_even += 1; rej_even += r_
        sab[mode] = dict(rejected_odd_n2=f"{rej_odd}/{tot_odd}",
                         rejected_even_n2=f"{rej_even}/{tot_even}",
                         detected=bool(rej_odd + rej_even))
        log(f"  MUST-FAIL (b) [{mode}]: rejected on {rej_odd}/{tot_odd} odd-n2 and "
            f"{rej_even}/{tot_even} even-n2 nonzero cases")
    sab["flipbits"]["note"] = (
        "flipping EVERY 2-column bit is the relabelling s -> ~s of the summation "
        "variable, so it multiplies the sum by (-1)^n2: it is a genuine symmetry at "
        "even n2 and undetectable there, and is detected at odd n2. The 39 rows of "
        "this session all have n2 = 15, odd, so this mode is live on the real data.")
    b_all = all(x["detected"] for x in sab.values())
    rejected = a_rejected and b_all
    return dict(cases=out, n_cases=len(out), n_agree=len(out) - bad, n_nonzero=nz,
                need_nonzero=need_nonzero,
                all_agree=(bad == 0), enough_nonzero=(nz >= need_nonzero),
                must_fail_corrupted_symbol_rejected=a_rejected,
                must_fail_sabotaged_evaluator=sab,
                first_attempt_at_this_control_was_vacuous=True,
                verdict=("PASS" if (bad == 0 and nz >= need_nonzero and rejected) else "FAIL"))


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--validate", action="store_true")
    ap.add_argument("--entries", default="")      # "row:col,row:col"
    ap.add_argument("--out", default=os.path.join(ROOT, "results", "b14_02", "exact_entries.json"))
    a = ap.parse_args(argv)
    res = {}
    if a.validate:
        res["small_shape_validation"] = validate_small()
    if a.entries:
        src = json.load(open(os.path.join(ROOT, "results", "s74", "source.json"), encoding="utf-8"))
        rows = [e for e in src["entries"] if e["rung"] <= DEG][:39]
        P13 = json.load(open(os.path.join(ROOT, "results", "b14_prep", "points", "P13.json"), encoding="utf-8"))
        ce = [tuple(x) for x in P13["cubic_exponents"]]
        pts = [q for q in P13["points"] if q["role"] == "primary"]
        got = []
        for spec in a.entries.split(","):
            i, j = (int(x) for x in spec.split(":"))
            e = rows[i]
            nat = e["native"]
            one = list(nat["one"]); nxt = nat["delta"]
            for _ in range(DEG - nat["delta"]):
                one += [nxt] * NLEG; nxt += 1
            qd = quartic_dict_from_point(pts[j], ce)
            t = time.time()
            v = exact_eval(nat["C1"], nat["C2"], [tuple(x) for x in nat["two"]], one,
                           DEG, HH, HH, symbol_fn(qd, HH), progress=f"({i},{j})")
            log(f"  A[{i}][{j}] = {v}   ({time.time()-t:.0f}s, {abs(v).bit_length()} bits)")
            got.append(dict(row=i, col=j, col_id=pts[j]["id"], value=str(v),
                            bits=abs(v).bit_length(), secs=round(time.time() - t, 1)))
        res["entries"] = got
    res["values_are"] = ("exact integers F_{T_i^up13}(f_j) over Z, computed by the "
                         "independent Identity-3 evaluator in this file; no transform")
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    json.dump(res, open(a.out, "w"), indent=1)
    log("wrote " + a.out)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
