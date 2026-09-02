#!/usr/bin/env python3
"""
Session 36 -- the validation battery (results/PREREG_s36.md P1).  Nothing new
is measured until every part passes.  Each part is written so that the WRONG
lemma fails it; the discriminating counts are printed, not the pass counts.

  part 1  isotypic containment of the UNREDUCED HWV kernel, per candidate
          character psi of Stab(lam): dim(ker ∩ V_psi) for every psi.
  part 2  reduced pipeline reproduces results/sweep62_ledger.md exactly
          (a, mult_det, mult_pad; both primes); compressed == exact route at
          three cells (a, mult, kernel span; both primes).
  part 3  the l^3 m witness through the reduced pipeline; wk8_s30_calib.py as-is.
  part 4  the s35 cell (10,10,10,6) at delta 9: size line, a by plethysm.

usage: python3 wk9_s36_validate.py [1|2|3|4|all]  -> appends to results/stabred_validation.md
"""
import sys, os, time, itertools, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from wk9_s36_stabred import *
from wk8_s30_pleth import a_of

OUT = os.path.join(HERE, '..', 'results', 'stabred_validation.md')
LEDGER = {  # results/sweep62_ledger.md rows used here: lam -> (a, N_S, mult_det, mult_pad)
    (13, 5, 2, 2, 2): (2, 3672, 2, 2), (14, 4, 2, 2, 2): (2, 2337, 2, 2),
    (12, 6, 2, 2, 2): (4, 5194, 4, 4), (13, 5, 4, 1, 1): (2, 1824, 2, 2),
    (12, 5, 5, 1, 1): (2, 2795, 2, 2), (9, 8, 5, 1, 1): (2, 5159, 2, 2),
}
EVEN = [(13, 5, 2, 2, 2), (14, 4, 2, 2, 2), (12, 6, 2, 2, 2)]
ODD = [(13, 5, 4, 1, 1), (12, 5, 5, 1, 1), (9, 8, 5, 1, 1)]
EXTRA = [((7, 7, 4, 1, 1), 5, 1)]     # two odd blocks, a = 1: four candidate characters

def emit(s):
    print(s); sys.stdout.flush()
    with open(OUT, 'a') as fh: fh.write(s + "\n")

def characters(lam):
    """all linear characters of Stab(lam) as dict perm -> +-1, labelled by the
    per-block choice (t = trivial, s = sign on blocks of size >= 2)."""
    blks = [B for B in blocks_of(lam) if len(B) >= 2]
    group = [g for g, _ in stab_group(lam)]
    out = {}
    for choice in itertools.product('ts', repeat=len(blks)):
        ch = {}
        for g in group:
            v = 1
            for B, c in zip(blks, choice):
                if c == 's': v *= perm_sign([g[b] for b in B])
            ch[g] = v
        label = ",".join(f"{lam[B[0]]}^{len(B)}:{c}" for B, c in zip(blks, choice))
        out[label] = ch
    return out, blks

def part1():
    emit("\n## Part 1 — isotypic containment of the unreduced kernel, per candidate character\n")
    emit("`dim(ker R ∩ V_psi)` for every linear character `psi` of `Stab(lam)` "
         "(`m^k:t` = trivial on the block of value `m`, size `k`; `:s` = sign).  "
         "Lemma predicts `a` at `psi = chi_lam` (sign iff `m` odd) and `0` elsewhere.\n")
    emit("| lam | delta | a | Stab | character | dim(ker ∩ V_psi) | predicted | verdict |")
    emit("|---|---|---|---|---|---|---|---|")
    n = 4
    ndisc, ncells, fails = 0, 0, []
    cells = [(l, 6, LEDGER[l][0]) for l in EVEN + ODD] + EXTRA
    for lam, delta, a_exp in cells:
        r = len(lam)
        basis, R = build_R(n, r, delta, lam)
        nb = len(basis); pos = {m: c for c, m in enumerate(basis)}
        chars, blks = characters(lam)
        group = [g for g, _ in stab_group(lam)]
        tabs = dict(zip(group, [t for t, _ in perm_tables(n, r, [(g, 1) for g in group])]))
        pred = {}
        for label in chars:
            pred[label] = all((c == 's') == (lam[B[0]] % 2 == 1)
                              for B, c in zip(blks, [x.split(':')[1] for x in label.split(',')]))
        ncells += 1
        cell_ok = True
        for p in (P1, P2):
            K = nullspace(R, nb, p)
            a = len(K)
            assert a == a_exp == a_of(lam, delta, n, r), (lam, a, a_exp)
            for label, ch in chars.items():
                # constraint rows: v_{g m} - psi(g) v_m = 0 for all g, m; dim = a - rank
                rows = []
                for g in group:
                    if all(g[i] == i for i in range(r)): continue
                    tab = tabs[g]
                    for m in basis:
                        gm = tuple(sorted(tab[i] for i in m))
                        rows.append([(kv[pos[gm]] - ch[g] * kv[pos[m]]) % p for kv in K])
                d = a - rank_of(rows, a, p)
                want = a if pred[label] else 0
                ok = d == want
                cell_ok &= ok
                if p == P1:
                    emit(f"| `{lam}` | {delta} | {a} | {len(group)} | `{label}` | {d} | {want} | "
                         f"{'ok' if ok else '**FAIL**'} |")
                elif not ok:
                    emit(f"| `{lam}` | {delta} | {a} | {len(group)} | `{label}` | {d} | {want} | **FAIL at p2** |")
        if len(chars) >= 2: ndisc += 1
        if not cell_ok: fails.append(lam)
    emit(f"\n**Part 1: {ncells} cells, {ndisc} discriminating** (each has >= 2 candidate characters; "
         f"the three even-block cells kill a 'sign always' rule, the three odd-block cells kill a "
         f"'trivial always' rule, the two-block cells `(12,5,5,1,1)` and `(7,7,4,1,1)` (four candidate characters each) "
         f"kill every mixed rule).  Failures: {fails if fails else 'none'}.")
    return not fails

def part2():
    emit("\n## Part 2 — reduced pipeline vs the s30 ledger, and compressed vs exact\n")
    emit("| lam | a (pleth) | N_S | Stab | n_chi | rows | route | a (kernel) | rank(R) | mult_det | mult_pad | ledger (det, pad) | verdict |")
    emit("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    fails = []
    kept = {}
    for lam in EVEN + ODD:
        a_exp, ns, md, mp = LEDGER[lam]
        out = measure_reduced(4, len(lam), 6, lam, a_exp, route='exact', verbose=False)
        kept[lam] = out
        ok = (out['N_S'] == ns and out['mult_det'] == md and out['mult_pad'] == mp
              and all(v['a'] == a_exp and v['rank'] == out['n_chi'] - a_exp
                      for v in out['per_prime'].values()))
        if not ok: fails.append(lam)
        emit(f"| `{lam}` | {a_exp} | {out['N_S']} | {out['stab']} | {out['n_chi']} | {out['nrows']} | exact | "
             f"{out['per_prime'][P1]['a']} | {out['per_prime'][P1]['rank']} | {out['mult_det']} | {out['mult_pad']} | "
             f"({md}, {mp}) | {'ok' if ok else '**FAIL**'} |")
    emit("\nCompressed route (`Agg = P·M`, certified) against the exact route, three cells:\n")
    emit("| lam | prime | a | mult_det | mult_pad | kernel span identical | verdict |")
    emit("|---|---|---|---|---|---|---|")
    for lam in [(13, 5, 2, 2, 2), (12, 5, 5, 1, 1), (12, 6, 2, 2, 2)]:
        a_exp = LEDGER[lam][0]
        oc = measure_reduced(4, len(lam), 6, lam, a_exp, route='compressed', verbose=False)
        oe = kept[lam]
        for p in (P1, P2):
            ke, kc = oe['per_prime'][p]['kern'], oc['per_prime'][p]['kern']
            both = ke + kc
            rk = nmod_mat(len(both), len(both[0]), [v % p for rw in both for v in rw], p).rank()
            same = rk == a_exp
            ok = same and oc['per_prime'][p]['mult'] == oe['per_prime'][p]['mult']
            if not ok: fails.append((lam, p, 'compressed'))
            emit(f"| `{lam}` | {p} | {oc['per_prime'][p]['a']} | {oc['per_prime'][p]['mult']['det']} | "
                 f"{oc['per_prime'][p]['mult']['pad']} | {'yes' if same else 'NO'} | {'ok' if ok else '**FAIL**'} |")
    emit(f"\n**Part 2 failures: {fails if fails else 'none'}.**")
    return not fails

def part3():
    emit("\n## Part 3 — the gate: the `l^3 m` witness (reduced and unreduced) and `wk8_s30_calib.py` as-is\n")
    f1, N1 = per_padded(1, 4)
    ok = True
    basis, vecs, group = orbit_setup(4, 2, 2, (4, 4), verbose=False)
    rows, _ = reduced_rows(4, 2, 2, (4, 4), vecs, verbose=False)
    for p in (P1, P2):
        a, rk, kern = kernel_exact(rows, len(vecs), p)
        full = expand(vecs, kern[0], p)
        v = [full.get(m, 0) for m in basis]
        inv = pow(v[2], p - 2, p); vn = tuple(x * inv % p for x in v)
        ev = point_rows(f1, N1, 4, 2, basis, vecs, 9, 11, 40, p)
        mult = mult_from(kern, ev, a, p)
        good = (a == 1 and vn == (12 % p, (-3) % p, 1) and mult == 0)
        ok &= good
        emit(f"- reduced witness, p = {p}: a = {a}, kernel ∝ `{(12, -3, 1) if good else vn}`, "
             f"mult = {mult} — {'ok' if good else '**FAIL**'} (wrong rule would give `(1,-4,3)`, mult 1)")
    res = measure(f1, N1, 4, 2, 2, (4, 4), a_expect=1)
    good = res['mult'] == 0; ok &= good
    emit(f"- unreduced witness (`wk8_s30_core.measure`): mult = {res['mult']} — {'ok' if good else '**FAIL**'}")
    pr = subprocess.run([sys.executable, os.path.join(HERE, 'wk8_s30_calib.py')],
                        capture_output=True, text=True)
    txt = pr.stdout
    emit("- `analysis/wk8_s30_calib.py` as-is:\n")
    emit("```\n" + txt.strip() + "\n```")
    good = 'CALIBRATION PASSED' in txt; ok &= good
    emit(f"\n**Part 3: {'PASS' if ok else 'FAIL'}** — discriminating ratio quoted from the battery line above "
         f"(World A cells with `mult < a` / cells).")
    return ok

def part4():
    emit("\n## Part 4 — the s35 cell `mult_det((10,10,10,6), 9)` at `r = 4`\n")
    t = time.time()
    a = a_of((10, 10, 10, 6), 9, 4, 4)
    ns, nchi, so = n_chi_of(4, 4, 9, (10, 10, 10, 6))
    emit(f"- `a = {a}` by plethysm; `N_S = {ns}`, `|Stab| = {so}` (block `10^3`, even → trivial character; "
         f"singleton 6), `n_chi = {nchi}` ({time.time()-t:.0f}s of orbit enumeration).")
    emit(f"- Resident model for the compressed route: `8 · n_chi^2 = {8*nchi*nchi/1e9:.0f} GB`; "
         f"measured constant `2.5e-8 · n_chi^2 = {2.5e-8*nchi*nchi:.0f} GB` — against 6.5 GB usable.  "
         f"**The direct measurement is out of reach on this container by a factor of ~{2.5e-8*nchi*nchi/6.5:.0f}.**")
    emit("- What stands: s35's T1w exhibits one weight-`(10,10,10,6)` HWV (the extremal catalecticant 9-minor) "
         "nonzero at a det pencil, so `mult_det >= 1`; `mult_det = a = 10` follows from "
         "`docs/s35_review.md` §2 (principality of `I(D_4^det)` + no rectangular equation below degree 10, s33).  "
         "Not banked as a measurement.  See the PREREG P1.4 feasibility line, written before this part ran.")
    return True

if __name__ == '__main__':
    which = sys.argv[1] if len(sys.argv) > 1 else 'all'
    if which == 'all' or not os.path.exists(OUT):
        with open(OUT, 'w') as fh:
            fh.write("# Stabiliser-reduction validation battery — session 36\n\n"
                     "Run before any new cell (PREREG_s36.md P1).  Both house primes at every rank.  "
                     "Pad points everywhere are true padded-permanent restrictions "
                     "`x_0 · per_3(x_1..x_9)` with random linear-form substitutions.\n")
    parts = {'1': part1, '2': part2, '3': part3, '4': part4}
    results = {}
    for k in (['1', '2', '3', '4'] if which == 'all' else [which]):
        t0 = time.time()
        results[k] = parts[k]()
        emit(f"\n_(part {k}: {time.time()-t0:.0f}s)_")
    emit("\n---\n**BATTERY " + ("PASSED" if all(results.values()) else "FAILED — STOP") +
         f"** (parts run: {sorted(results)})")
