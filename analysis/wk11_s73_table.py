#!/usr/bin/env python3
"""Session 73 -- render the D-ladder table results/s73_dladder.md from
results/s73_dladder.jsonl (one record per rung and seed family, latest wins)
and results/s73_transport.jsonl.

Columns: delta, lambda, a, n_chi, i_det, mult_det, i_per, mult_per, D, the
three-outcome decision, dim(U_D ∩ U_P), the orientation, the transport status
of the rung's kernels, and the status labels (proved / measured).
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def load_jsonl(path):
    out = []
    if os.path.exists(path):
        with open(path) as fh:
            for ln in fh:
                ln = ln.strip()
                if ln:
                    out.append(json.loads(ln))
    return out


def outcome(iD, iP):
    if iD is None or iP is None:
        return "—"
    if iD > iP:
        return f"D = +{iD - iP} > 0: multiplicity obstruction (i_per < i_det)"
    if iD == iP:
        return "D = 0: orientation test"
    return f"D = {iD - iP} < 0"


def main():
    recs = load_jsonl(os.path.join(ROOT, 'results', 's73_dladder.jsonl'))
    trs = load_jsonl(os.path.join(ROOT, 'results', 's73_transport.jsonl'))
    latest = {}
    for r in recs:
        if 'sides' in r:
            latest[(r['delta'], r.get('seedtag', 'primary'))] = r
    tr_by = {t['delta_lo']: t for t in trs}
    lines = ["# The `n = 3` `D`-ladder on `λ_δ = (3δ − 17, 7, 2^5)`, `r = 7` — session 73", "",
             "`D = i_det − i_per = mult_per − mult_det`; `i_X = a − mult_X`.  `i_X = 0` rows are **proved** "
             "(nullity 0 at one prime proves `mult_X = a` over `Q`); positive nullities are **measured** at both "
             "primes and carried to `Q` by an exhibited integer kernel vector (see the certificates).  "
             "`a` by two independent plethysm engines.  Seed family `primary` = the pre-registered seeds; "
             "`second` = the verification-protocol family (`K = a + 20`).", ""]
    hdr = ("| δ | λ | seeds | a | n_χ | i_det | mult_det | i_per | mult_per | D | outcome | dim(U_D ∩ U_P) | "
           "U_D ⊆ U_P / U_P ⊆ U_D | kernel origin (transport) | primes agree | wall s |")
    lines += [hdr, "|" + "---|" * (hdr.count("|") - 1)]
    for (d, tag) in sorted(latest):
        r = latest[(d, tag)]
        sd, sp = r['sides'].get('det', {}), r['sides'].get('per', {})
        iD, iP = sd.get('i'), sp.get('i')
        inter = r.get('intersection', {}).get(str(r['primes'][0]), {})
        t = tr_by.get(d - 1, {}).get('sides', {}).get('det', {}).get(f"mod_{r['primes'][0]}", {})
        origin = "—"
        if iD is not None and iD > 0:
            if t:
                origin = ("= J(U_D(δ−1)) (transported, nothing born)" if t.get('U_hi_equals_J_U_lo')
                          else f"born at this rung: {t.get('born_at_hi')} new")
            elif d - 1 in tr_by or d == 12:
                prev = latest.get((d - 1, 'primary'))
                if prev and prev['sides'].get('det', {}).get('i') == 0:
                    origin = "born at this rung (U_D(δ−1) = 0)"
        agree = all(r['sides'][s].get('primes_agree') for s in r['sides'])
        lines.append(f"| {d} | `{tuple(r['lam'])}` | {tag} | {r['a']} | {r['n_chi']} | "
                     f"{iD if iD is not None else '—'} | {sd.get('mult', '—')} | {iP if iP is not None else '—'} | {sp.get('mult', '—')} | "
                     f"{('+' if r.get('D', 0) > 0 else '') + str(r['D']) if 'D' in r else '—'} | {outcome(iD, iP)} | "
                     f"{inter.get('dim_intersection', '—')} | {inter.get('UD_subset_UP', '—')} / {inter.get('UP_subset_UD', '—')} | "
                     f"{origin} | {agree} | {r.get('secs', '—')} |")
    lines += ["", "## Transport records (`J = ·c_{(3,0,…,0)}`)", "",
              "| δ → δ+1 | a → a | J(M_δ) HWV at δ+1 | rank J(M_δ) | J(M_δ) ⊆ M_{δ+1} | birth dim | u-free rank of M_{δ+1} | "
              "E·J(v) = 0 over Z (det) | J(U_D) ⊆ U_D' / equal (P1) | lines equal over Z |",
              "|---|---|---|---|---|---|---|---|---|---|"]
    for t in sorted(trs, key=lambda x: x['delta_lo']):
        jm = t.get('J_M_lo', {})
        sd = t.get('sides', {}).get('det', {})
        m = sd.get(f"mod_{2147483647}", {})
        lines.append(f"| {t['delta_lo']} → {t['delta_hi']} | {t['a_lo']} → {t['a_hi']} | {jm.get('all_highest_weight_mod_P1', '—')} | "
                     f"{jm.get('rank_mod_P1', '—')} | {jm.get('contained_in_M_hi', '—')} | {jm.get('birth_dim', '—')} | "
                     f"{jm.get('ufree_rank_M_hi', '—')} | {sd.get('E_hi_J_v_zero_over_Z', '—')} | "
                     f"{m.get('J_U_lo_subset_U_hi', '—')} / {m.get('U_hi_equals_J_U_lo', '—')} | {sd.get('over_Z_lines_equal', '—')} |")
    with open(os.path.join(ROOT, 'results', 's73_dladder.md'), 'w') as fh:
        fh.write("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == '__main__':
    main()
