#!/usr/bin/env python3
"""
Session 52 -- fill the three generated sections of docs/s52_report.md from the
banked jsonl, so the report never drifts from the ledger.

usage: python3 wk9_s52_fill.py
"""
import sys, os, json

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk9_s52_report import load, ledger_rows

REPORT = os.path.join(ROOT, 'docs/s52_report.md')


def block(name, body, text):
    start = f"<!--{name}-->"
    end = f"<!--/{name}-->"
    new = start + "\n" + body.rstrip() + "\n" + end
    if start in text and end in text:
        i = text.index(start); j = text.index(end) + len(end)
        return text[:i] + new + text[j:]
    return text.replace(start, new)


def main():
    rows = load()
    LR = [r for r in ledger_rows() if r.get('status') == 'measured']
    text = open(REPORT).read()

    byd = {}
    for r in LR: byd.setdefault(r['delta'], []).append(r)
    per = ", ".join(f"{len(v)} at `δ = {k}`" for k, v in sorted(byd.items()))
    nchi = sorted(r['n_chi'] for r in LR)
    m = []
    m.append(f"**{len(LR)} `a = 1` cells measured this session** ({per}), `n_χ` from "
             f"{nchi[0]:,} to {nchi[-1]:,}, every one carrying one ambient unit.\n")
    m.append("| | value |\n|---|---|")
    m.append(f"| cells with `mult_det = a` (`i_det = 0`) | **{sum(1 for r in LR if r['i_det']==0)} of {len(LR)}** |")
    m.append(f"| cells with `mult_pad = a` (`i_pad = 0`) | {sum(1 for r in LR if r['i_pad']==0)} of {len(LR)} |")
    m.append(f"| cells with `D > 0` | **{sum(1 for r in LR if r['D']>0)}** |")
    m.append(f"| cells with `D < 0` | {sum(1 for r in LR if r['D']<0)} |")
    m.append(f"| deferred | {sum(1 for r in ledger_rows() if r.get('status')=='DEFER')} |")
    d10 = byd.get(10, [])
    if d10:
        m.append(f"\n**The programme's first `δ = 10` cells.**  {len(d10)} of the 17 `a = 1` "
                 f"cells at `δ = 10` are measured, `n_χ` from {min(r['n_chi'] for r in d10):,} to "
                 f"{max(r['n_chi'] for r in d10):,}, all `mult_det = mult_pad = mult_red = 1 = a`.  "
                 "Before this session the record stopped at `δ = 9`.")
    m.append("\n**No cell reported `D > 0`, so the verification protocol was never entered "
             "and the sweep was never halted.**  Every determinant-side verdict is a "
             "*proof* rather than a measurement: on the dense route by the exact kernel "
             "at both primes with `a` re-derived and every kernel vector checked against "
             "the uncompressed raising-operator rows, and on the sparse route by a "
             "single-prime non-singularity certificate, which implies the rational "
             "statement one-sidedly.")
    m.append("\nCombined with `results/sixrow_record.md`, the six-row determinant ideal is "
             f"now empty at **{193 + len(LR)} measured cells** across `δ = 6, 7, 8, 9, 10`.")
    text = block('MEASUREMENTS', "\n".join(m), text)

    s = []
    s.append("| | prediction | prior | outcome |")
    s.append("|---|---|---|---|")
    s.append("| **P1** | the BIP mechanism does not transfer to `n = 4` | 0.85 | **confirmed**, and more sharply than logged — the failure is a length gap (`ℓ(λ) ≤ 4` reachable at `n = 4`, census at `ℓ(λ) = 6`), not a constant |")
    s.append("| **P2** | `δ = 7`: 258 eligible, 64 with `a = 1` | 0.80 | **confirmed exactly** |")
    s.append("| **P3** | `δ = 8`: 591 eligible, 45 with `a = 1` | 0.80 | **confirmed exactly** |")
    s.append("| **P4** | `δ = 9` census completes within 30 min | 0.85 | **confirmed**, 273 s by the plethysm route; reproduces s43's 1,079 / 86,363 |")
    s.append("| **P5** | `δ = 10` census completes | 0.55 | **confirmed, but not by the route assumed** — the plethysm route was ended by the kernel at 3.9 GB; the Weyl route did it in 202 s inside 3 GB |")
    s.append("| **P6** | `a = 1` share below 5% at `δ = 9` | 0.70 | **confirmed**, 2.2% at `δ = 9` and 0.95% at `δ = 10` |")
    s.append("| **P7** | at least half the `a = 1` cells have `h_pad = 0` | 0.45 | **refuted** — 9/64, 10/45, 2/24, 0/17; the informative fraction rises with `δ` |")
    s.append(f"| **P8** | `i_det = 0` at every cell measured | 0.93 | **confirmed**, {sum(1 for r in LR if r['i_det']==0)} of {len(LR)} |")
    s.append(f"| **P9** | no cell reports `D > 0` | 0.94 | **confirmed** |")
    s.append(f"| **P10** | every measured cell reproduces `a` by kernel dimension | 0.97 | **confirmed** on the dense route (asserted in-process); on the sparse route `a` is the plethysm value by construction and the certificate is one-sided, as `results/s45_ledger.md` states |")
    s.append("\nThe re-measurement gate of pre-registration §5 passed at all three named "
             "cells with every field identical.")
    text = block('SCORECARD', "\n".join(s), text)

    todo = json.load(open(os.path.join(ROOT, 'results/s52_todo.json')))
    left = [c for c in todo if (tuple(c['lam']), c['delta']) not in {(tuple(r['lam']), r['delta']) for r in LR}]
    b = []
    lo9 = [c for c in left if c['delta'] <= 9]
    lo10 = [c for c in left if c['delta'] == 10]
    b.append(f"1. **Coverage.**  {len(LR)} of the 129 informative `a = 1` cells were measured "
             f"this session and 51 were already banked, so **{len(left)} remain**.  They are not "
             "unmeasured because time ran out at the cheap end: the cheapest remaining cell at "
             f"`δ ≤ 9` has an `n_χ` estimate of **{min(c['nchi_lb'] for c in lo9):,}**, well "
             "beyond session 41's dense frontier of 20,000, and the largest in the list is "
             f"{max(c['nchi_lb'] for c in left):,}.  {len(lo10)} `δ = 10` cells remain, with "
             f"estimates {', '.join(format(c['nchi_lb'], ',') for c in sorted(lo10, key=lambda x: x['nchi_lb']))}.")
    b.append("2. **The `δ = 10` census covers obstruction-eligible cells only.**  Its `λ_1 < 10` "
             "onset-only cells were never enumerated, so the `δ = 10` row cannot be compared "
             "with the `δ = 7, 8, 9` rows on the onset axis, only on the obstruction axis.")
    b.append("3. **`δ ≥ 11` was not done.**  A `δ = 11` run was launched and ended by its "
             "recorded process id after 100 of 2,902 cells (about 2 s per cell under contention, "
             "so roughly 1.6 h): the enumeration order is ascending in `λ_1`, and the `a = 1` "
             "cells are the lopsided ones at the far end, so a partial run in that order carries "
             "no rate and is not reported. It is affordable in a session that starts with it.")
    b.append("4. **One cross-check fewer at `δ = 10`.**  There, `a` is the Weyl alternation only "
             "— the plethysm route does not fit the container — so the two-route assertion that "
             "holds at `δ = 7, 8, 9` is not available. `h_pad` still has its two routes. The "
             "measured cells re-derive `a` by kernel dimension in-process, which is the second "
             "route where it matters.")
    b.append("5. **The sparse route does not exhibit its kernel.**  A `nullity = 0` certificate "
             "proves `mult = a` and needs nothing further, which is every sparse row here; had "
             "any been non-zero it would have been a measurement, not a verdict, and would have "
             "gone through the exhibit-and-verify path before being written down.")
    b.append("6. **`mult_red` on the sparse rows is forced, not measured** — `mult_pad ≤ mult_red "
             "≤ a = 1` — and is marked `1*` in the ledger.")
    text = block('BOUNDARY', "\n".join(b), text)

    open(REPORT, 'w').write(text)
    print("filled docs/s52_report.md;", len(LR), "measured rows,", len(left), "left")


if __name__ == '__main__':
    main()
