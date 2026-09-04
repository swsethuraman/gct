#!/usr/bin/env python3
"""
Session 47 -- regenerate the Phase A table of results/s47_ledger.md from
results/s47_cells.jsonl.  Everything above the marker is kept verbatim.

usage: python3 wk9_s47_report.py
"""
import json, os, sys
from collections import Counter

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
LED = os.path.join(ROOT, 'results', 's47_ledger.md')
MARK = "<!-- PHASE A TABLE -->"


def cells():
    out = []
    p = os.path.join(ROOT, 'results', 's47_cells.jsonl')
    if not os.path.exists(p): return out
    for L in open(p):
        L = L.strip()
        if L: out.append(json.loads(L))
    return out


def table(rs):
    L = []
    L.append("| # | `λ` | `δ` | `ℓ` | `a` | `h_pad` | gap `a−h_pad` | `n_red` | `nnz_red` | nullity | `mult_red` | `d` | units | verdict | secs |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for i, r in enumerate(rs, 1):
        a, h, m = r['a'], r['h_pad'], r['mult_red']
        d = min(a, h) - m
        v = '**REFUTED**' if r['verdict'] == 'REFUTED' else 'exact'
        L.append("| %d | `%s` | %d | %d | %d | %d | %d | %d | %d | %d | **%d** | %d | %d | %s | %d |" % (
            i, str(tuple(r['lam'])).replace(' ', ''), r['delta'], r['ell'], a, h, a - h,
            r['n_red'], r['nnz_red'], r['nullity'], m, d, a - m, v, round(r['wall'])))
    return "\n".join(L)


def summary(rs):
    ex = [r for r in rs if r['verdict'] == 'EXACT']
    rf = [r for r in rs if r['verdict'] == 'REFUTED']
    L = ["", f"**{len(rs)} firing cells measured this session: the bound is exact at {len(ex)} "
             f"and missed at {len(rf)}.**", ""]
    byg = {}
    for r in rs:
        g = r['a'] - r['h_pad']
        byg.setdefault(g, [0, 0])
        byg[g][0] += 1
        byg[g][1] += r['verdict'] == 'REFUTED'
    L.append("| gap `a − h_pad` | parity | cells | missed |")
    L.append("|---|---|---|---|")
    for g in sorted(byg):
        L.append("| %d | %s | %d | %d |" % (g, 'odd' if g % 2 else 'even', byg[g][0], byg[g][1]))
    L.append("")
    L.append("")
    L.append("Stratified by where the cell sits:")
    L.append("")
    L.append("| stratum | cells | exact | missed |")
    L.append("|---|---|---|---|")
    def strat(r):
        fam = r['ell'] == 6 and tuple(r['lam'])[3:] == (1, 1, 1)
        if fam and r['delta'] == 9: return "`ell = 6`, `delta = 9`, in family"
        if fam: return f"`ell = 6`, `delta = {r['delta']}`, in family"
        if r['ell'] == 6: return f"`ell = 6`, `delta = {r['delta']}`, outside the family"
        return f"`ell = {r['ell']}`, `delta = {r['delta']}`"
    st = {}
    for r in rs:
        k = strat(r); st.setdefault(k, [0, 0])
        st[k][0] += 1; st[k][1] += r['verdict'] == 'REFUTED'
    for k in sorted(st):
        L.append("| %s | %d | %d | %d |" % (k, st[k][0], st[k][0] - st[k][1], st[k][1]))
    L.append("")
    L.append("Stratified by the **target** dimension `h_pad` — exactness is surjectivity of")
    L.append("`mu_lambda : C^a -> C^{h_pad}`, so this is the dimension the demand is made on:")
    L.append("")
    L.append("| `h_pad` | cells | exact | missed |")
    L.append("|---|---|---|---|")
    hb = {}
    for r in rs:
        k = r['h_pad']; hb.setdefault(k, [0, 0])
        hb[k][0] += 1; hb[k][1] += r['verdict'] == 'REFUTED'
    for k in sorted(hb):
        L.append("| %d | %d | %d | %d |" % (k, hb[k][0], hb[k][0] - hb[k][1], hb[k][1]))
    lo = [r for r in rs if r['h_pad'] <= 8]; hi = [r for r in rs if r['h_pad'] >= 9]
    L.append("")
    L.append("`h_pad <= 8`: %d cells, %d exact, %d missed.  `h_pad >= 9`: %d cells, %d exact, %d missed."
             % (len(lo), sum(1 for r in lo if r['verdict'] == 'EXACT'), sum(1 for r in lo if r['verdict'] == 'REFUTED'),
                len(hi), sum(1 for r in hi if r['verdict'] == 'EXACT'), sum(1 for r in hi if r['verdict'] == 'REFUTED')))
    L.append("")
    ds = Counter(min(r['a'], r['h_pad']) - r['mult_red'] for r in rs)
    L.append(f"Rank deficits `d = min(a, h_pad) − mult_red` seen: {dict(sorted(ds.items()))}.")
    L.append("")
    return "\n".join(L)


if __name__ == '__main__':
    rs = cells()
    head = open(LED).read().split(MARK)[0].rstrip() if os.path.exists(LED) else ''
    open(LED, 'w').write(head + "\n\n" + MARK + "\n\n" + table(rs) + "\n" + summary(rs))
    print(f"{len(rs)} cells; exact {sum(1 for r in rs if r['verdict']=='EXACT')}, "
          f"refuted {sum(1 for r in rs if r['verdict']=='REFUTED')}")
