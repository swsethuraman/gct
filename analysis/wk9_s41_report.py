#!/usr/bin/env python3
"""
Session 41 -- coverage report and the Pieri-transport check.

Reads results/sixrow_census.md (via /root/s41/census.pkl), results/s41_ledger.md,
results/s36_ledger.md + results/s36_aone.md (the ell = 6 cells s36 banked), and
results/s41_per6.md (Phase 0b), and prints:

  1. coverage per degree: cells and ambient units measured (s36 + s41) as
     fractions of what EXISTS (census, lam_1 >= delta), and of what fits;
     the same by a and by balance;
  2. the det-side verdict: every measured ell = 6 cell with mult_det < a (the
     onset in reach), or the bracket if none;
  3. the pad side: cells with mult_pad < mult_red (permanent-specific
     equations) and cells with mult_pad < a (reducibility bites);
  4. the Pieri-transport check (docs/transfer_lemma.md Prop. 8(2)): for every
     measured cell (lam, delta), the length-6 weights mu |- 3 delta with
     mu ⊆ lam and lam/mu a horizontal delta-strip; if every such mu is measured
     empty in Phase 0b, then mult_pad = mult_red at that cell is FORCED
     (a theorem given the measurement), independent of the pad points.

usage: python3 wk9_s41_report.py  -> markdown on stdout
"""
import sys, os, pickle
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, '..')
from collections import Counter, defaultdict

def rows_of(path, prefixes):
    out = []
    if not os.path.exists(path): return out
    for ln in open(path):
        if any(ln.startswith(p) for p in prefixes):
            out.append([x.strip() for x in ln.strip().strip('|').split('|')])
    return out

def load_measured():
    """(lam, delta) -> dict(a, det, pad, red, src)"""
    M = {}
    for c in rows_of(os.path.join(ROOT, 'results', 's36_ledger.md'), ['| B |']):
        lam = eval(c[1].strip('`')); d = int(c[2])
        M[(lam, d)] = dict(a=int(c[4]), det=int(c[10]), pad=int(c[11]), red=None, src='s36')
    for c in rows_of(os.path.join(ROOT, 'results', 's36_aone.md'), ['| 6 |']):
        lam = eval(c[2].strip('`')); d = int(c[1])
        M[(lam, d)] = dict(a=int(c[3]), det=int(c[6]), pad=int(c[7]), red=int(c[8]), src='s36 a=1')   # cols: r, delta, lam, a, N_S, n_chi, det, pad, red, D
    for c in rows_of(os.path.join(ROOT, 'results', 's36_red_table.md'), ['| `(']):
        lam = eval(c[0].strip('`')); d = int(c[1])
        if (lam, d) in M: M[(lam, d)]['red'] = int(c[6])
    for c in rows_of(os.path.join(ROOT, 'results', 's41_ledger.md'), ['| 7 |', '| 8 |']):
        lam = eval(c[1].strip('`')); d = int(c[0])
        M[(lam, d)] = dict(a=int(c[2]), det=int(c[9]), pad=int(c[10]), red=int(c[11]), src='s41',
                           nchi=int(c[6]), secs=int(c[13]), hwm=float(c[14]))
    return M

def load_per6():
    """(mu, delta) -> (a, mult) from Phase 0b; weights with a(mu, delta; n = 3, r = 6) = 0 are
    entered as (0, 0): no S_mu in the ambient, so nothing to transport."""
    sys.path.insert(0, HERE)
    from wk8_s30_pleth import amb
    P = {}
    for d in (6, 7, 8):
        A = amb(d, 3, 6)
        P[('amb', d)] = A
    for c in rows_of(os.path.join(ROOT, 'results', 's41_per6.md'), ['| 7 |', '| 8 |', '| 9 |']):
        d = int(c[0]); mu = eval(c[1].strip('`'))
        P[(mu, d)] = (int(c[2]), int(c[6]))
    # s37: delta = 6, all four cells empty (results/s37_onset_per6_d6.log)
    for mu in [(8, 2, 2, 2, 2, 2), (7, 4, 2, 2, 2, 1), (6, 5, 3, 2, 1, 1), (5, 5, 5, 1, 1, 1)]:
        P[(mu, 6)] = (1, 1)
    return P

def strips(lam, delta):
    """length-6 mu |- 3 delta with mu ⊆ lam, lam/mu a horizontal strip of size delta
    (interlacing: lam_{i+1} <= mu_i <= lam_i), mu_6 >= 1."""
    lam = tuple(lam) + (0,) * (6 - len(lam))
    out = []
    def rec(i, cur, left):
        if i == 6:
            if left == 0 and cur[5] >= 1: out.append(tuple(cur))
            return
        lo = lam[i + 1] if i < 5 else 0
        for m in range(lo, lam[i] + 1):
            take = lam[i] - m
            if take > left: continue
            rec(i + 1, cur + [m], left - take)
    rec(0, [], delta)
    return out

def main():
    census = pickle.load(open('/root/s41/census.pkl', 'rb'))
    M = load_measured(); P = load_per6()
    L = []
    L.append("## Coverage (fractions of what exists; `λ_1 ≥ δ`, `a ≥ 1`, `ℓ = 6`)\n")
    L.append("| δ | cells | units | fit at 20000 | units | measured (s36+s41) | units | measured s41 | units | `mult_det < a` | `mult_pad < a` | `mult_pad < mult_red` |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for d in sorted(census):
        el = [x for x in census[d] if x['eligible']]
        fit = [x for x in el if x['approx'] == '' and x['n_chi'] <= 20000]
        meas = [x for x in el if (x['lam'], d) in M]
        m41 = [x for x in meas if M[(x['lam'], d)]['src'] == 's41']
        detb = [x for x in meas if M[(x['lam'], d)]['det'] < M[(x['lam'], d)]['a']]
        padb = [x for x in meas if M[(x['lam'], d)]['pad'] < M[(x['lam'], d)]['a']]
        perm = [x for x in meas if M[(x['lam'], d)]['red'] is not None and M[(x['lam'], d)]['pad'] < M[(x['lam'], d)]['red']]
        L.append(f"| {d} | {len(el)} | {sum(x['a'] for x in el)} | {len(fit)} | {sum(x['a'] for x in fit)} | "
                 f"{len(meas)} ({100*len(meas)/len(el):.0f}%) | {sum(x['a'] for x in meas)} ({100*sum(x['a'] for x in meas)/sum(x['a'] for x in el):.0f}%) | "
                 f"{len(m41)} | {sum(x['a'] for x in m41)} | {len(detb)} | {len(padb)} | {len(perm)} |")
        byA = defaultdict(lambda: [0, 0]); byB = defaultdict(lambda: [0, 0])
        for x in el:
            byA[x['a']][0] += 1; byB[x['bal']][0] += 1
            if (x['lam'], d) in M: byA[x['a']][1] += 1; byB[x['bal']][1] += 1
        L.append(f"\n`δ = {d}` measured/total by `a`: " + ", ".join(f"`a={k}`: {v[1]}/{v[0]}" for k, v in sorted(byA.items())) + ".")
        L.append(f"\n`δ = {d}` measured/total by balance: " + ", ".join(f"{k}: {v[1]}/{v[0]}" for k, v in sorted(byB.items())) + ".\n")
        big = [x for x in el if (x['lam'], d) in M and M[(x['lam'], d)]['src'] == 's41' and M[(x['lam'], d)].get('nchi', 0) > 15500]
        if big:
            L.append(f"`δ = {d}` cells above s36's frontier (15500) measured this session: " +
                     ", ".join(f"`{x['lam']}` (n_χ {M[(x['lam'], d)]['nchi']}, {M[(x['lam'], d)]['secs']} s, HWM {M[(x['lam'], d)]['hwm']:.2f} GB)" for x in big) + ".\n")
    # det verdict
    L.append("## Det side\n")
    detb = [(k, v) for k, v in M.items() if v['det'] < v['a']]
    if detb:
        L.append("Cells with `mult_det < a` (the six-row onset in reach): " + ", ".join(f"`{k[0]}` δ={k[1]} (a={v['a']}, mult_det={v['det']})" for k, v in sorted(detb, key=lambda t: (t[0][1], t[0][0]))) + "\n")
    else:
        L.append(f"No measured `ℓ = 6` cell has `mult_det < a`: {len(M)} cells, {sum(v['a'] for v in M.values())} ambient units, degrees {sorted(set(k[1] for k in M))}.\n")
    # pad side
    L.append("## Pad side\n")
    padb = [(k, v) for k, v in M.items() if v['pad'] < v['a']]
    L.append("Cells with `mult_pad < a`: " + (", ".join(f"`{k[0]}` δ={k[1]} (a={v['a']}, mult_pad={v['pad']}, mult_red={v['red']})" for k, v in sorted(padb, key=lambda t: (t[0][1], t[0][0]))) if padb else "none") + ".\n")
    perm = [(k, v) for k, v in M.items() if v['red'] is not None and v['pad'] < v['red']]
    L.append("Cells with `mult_pad < mult_red` (permanent-specific equations): " + (", ".join(f"`{k[0]}` δ={k[1]}" for k, v in perm) if perm else "none") + ".\n")
    # Pieri transport
    L.append("## Pieri transport (Prop. 8(2)): is `mult_pad = mult_red` forced at each measured cell?\n")
    L.append("For each measured `(λ, δ)`, the length-6 `μ ⊢ 3δ` with `λ/μ` a horizontal `δ`-strip; `mult_pad < mult_red` needs `S_μ ⊆ I(D_6^{per_3})_δ` for one of them.  "
             "`forced` = every such `μ` measured with `mult = a` in Phase 0b (`results/s41_per6.md`, plus s37's `δ = 6`).\n")
    forced = 0; notforced = []
    unmeasured_mu = Counter()
    for (lam, d), v in sorted(M.items(), key=lambda t: (t[0][1], t[0][0])):
        mus = strips(lam, d)
        st = []
        for mu in mus:
            if (mu, d) in P:
                a, m = P[(mu, d)]
                st.append('empty' if m == a else 'NONZERO')
            elif ('amb', d) in P and P[('amb', d)].get(tuple(x for x in mu if x), 0) == 0:
                st.append('empty')          # a(mu) = 0: no S_mu in Sym^d(Sym^3 C^6) at all
            else:
                st.append('unmeasured'); unmeasured_mu[(mu, d)] += 1
        if all(s == 'empty' for s in st): forced += 1      # vacuous when there is no strip mu
        else: notforced.append((lam, d, mus, st))
    L.append(f"Forced at **{forced} of {len(M)}** measured cells.")
    if notforced:
        L.append("Not forced (some transport weight unmeasured or nonzero): " + "; ".join(
            f"`{lam}` δ={d}: " + ", ".join(f"`{mu}` {s}" for mu, s in zip(mus, st) if s != 'empty') for lam, d, mus, st in notforced) + ".")
    if unmeasured_mu:
        L.append("\nTransport weights not measured in Phase 0b (and the number of measured cells they touch): " +
                 ", ".join(f"`{mu}` δ={d} ({c})" for (mu, d), c in sorted(unmeasured_mu.items(), key=lambda t: -t[1])) + ".")
    print("\n".join(L))

if __name__ == '__main__':
    main()
