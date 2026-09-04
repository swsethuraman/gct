#!/usr/bin/env python3
"""
Session 47, Phase C2 -- close I(D_6^{per_3})_8 = 0.

Session 43 measured 81 of the 91 length-6 weights mu |- 24 with a(mu,8) >= 1 in
Sym^8(Sym^3 C^6) and found every one empty (mult = a).  This driver identifies
the 10 that are left and measures them by session 43's injectivity certificate
(analysis/wk9_s43_inject.py), unchanged.

If all ten are empty then I(D_6^{per_3})_8 = 0 outright and, by Prop. 8(1) of
docs/transfer_lemma.md, mult_pad = mult_red at EVERY weight of degree 8 -- the
degree at which every pad-side bite in the six-row record lives.

If one is NOT empty it is the first permanent-specific equation the programme has
seen: the driver halts the phase, re-checks it independently, and reports.

usage: python3 wk9_s47_per6.py --list
       python3 wk9_s47_per6.py --run [--cap N]
"""
import sys, os, re, json, time

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
from wk8_s30_pleth import a_of
from wk9_s36_stabred import orbit_setup, monomials


def partitions_len(total, length, maxpart=None):
    """partitions of `total` into exactly `length` positive parts, weakly decreasing."""
    if maxpart is None: maxpart = total
    if length == 1:
        if 1 <= total <= maxpart: yield (total,)
        return
    for first in range(min(maxpart, total - length + 1), 0, -1):
        for rest in partitions_len(total - first, length - 1, first):
            yield (first,) + rest


def all_weights(delta):
    """length-6 mu |- 3*delta with a(mu, delta) >= 1 for Sym^delta(Sym^3 C^6).

    I(D_6^{per_3}) is concentrated at weights of length exactly 6 (restriction
    lemma, docs/transfer_lemma.md sec 4)."""
    out = []
    for mu in partitions_len(3 * delta, 6):
        a = a_of(mu, delta, 3, 6)
        if a >= 1: out.append((mu, a))
    return out


MEAS_RE = re.compile(r"^\|\s*(\d+)\s*\|\s*`\(([^)]*)\)`\s*\|\s*(\d+)\s*\|")


def measured(delta):
    """(mu, a, mult) rows already banked, from sessions 41 and 43.  The two
    ledgers have different column counts -- s43 inserted a `route` column -- so
    the mult column is located by header, not by a fixed index."""
    seen = {}
    for fn in ('s41_per6.md', 's43_per6.md'):
        p = os.path.join(ROOT, 'results', fn)
        if not os.path.exists(p): continue
        cols_idx = None
        for line in open(p):
            line = line.strip()
            if line.startswith('| delta |'):
                hdr = [c.strip() for c in line.strip('|').split('|')]
                cols_idx = hdr.index('mult')
                continue
            m = MEAS_RE.match(line)
            if not m or cols_idx is None: continue
            cols = [c.strip() for c in line.strip('|').split('|')]
            if int(cols[0]) != delta: continue
            mu = tuple(int(v) for v in cols[1].strip('`()').split(','))
            seen[mu] = (int(cols[2]), int(cols[cols_idx]))
    return seen


def outstanding(delta):
    seen = measured(delta)
    return [(mu, a) for mu, a in all_weights(delta) if mu not in seen], seen


# --------------------------------------------------------------------- runner
OUTSTANDING_D8 = [((7,5,4,4,2,2),1), ((6,6,5,4,2,1),1), ((8,6,4,3,2,1),3),
                  ((8,5,4,3,2,2),1), ((6,5,5,3,3,2),1), ((7,5,4,4,3,1),1),
                  ((7,6,5,3,2,1),2), ((7,6,4,3,2,2),1), ((6,5,5,4,3,1),1)]
# ascending in n_chi (76792 .. 127182), measured by orbit_setup before the run

LEDGER = os.path.join(ROOT, 'results', 's47_per6_d8.md')
JSONL  = os.path.join(ROOT, 'results', 's47_per6.jsonl')

HEADER = """# `I(D_6^{per_3})_8` — the last nine weights — session 47, Phase C2

Session 41 measured 28 of the 91 length-6 weights `μ ⊢ 24` with `a(μ,8) ≥ 1` in
`Sym^8(Sym^3 C^6)`; session 43 measured 54 more.  All 82 are **empty**
(`mult = a`).  This table measures the **nine** that were left.

*(The brief says "81 of the 91 ... the 10 remaining".  Re-enumerating the
weights here and re-parsing `results/s41_per6.md` and `results/s43_per6.md`
gives 91 total, **82** measured — 28 + 54, disjoint, every `a` agreeing with an
independent plethysm recomputation — and **9** outstanding.  The count is off by
one; the list below is the true remainder.)*

Route: the sparse injectivity certificate `analysis/wk9_s43_inject.py`
(`inject_one`), unchanged, both house primes, `a + 8` points
`per_3(Σ s_i A_i)`.  `[M; Ev]` nonsingular at one prime proves `mult = a` at
that prime; the two primes are asserted to agree.  A kernel vector would prove
`mult < a` and would be the **first permanent-specific equation the programme
has seen** — the run halts there.

If all nine are empty then `I(D_6^{per_3})_8 = 0` outright, and by Prop. 8(1)
of `docs/transfer_lemma.md`, **`mult_pad = mult_red` at every weight of degree
8** — the degree at which every pad-side bite in the six-row record lives.

| `μ` | `a` | `N_S` | Stab | `n_χ` | route | `mult` | units | secs |
|---|---|---|---|---|---|---|---|---|
"""


def run():
    from wk9_s43_inject import inject_one
    if not os.path.exists(LEDGER):
        open(LEDGER, 'w').write(HEADER)
    done = set()
    if os.path.exists(JSONL):
        for L in open(JSONL):
            L = L.strip()
            if L: done.add(tuple(json.loads(L)['lam']))
    for mu, a in OUTSTANDING_D8:
        if mu in done: continue
        print(f"=== per6 d=8 {mu} a={a} ===", flush=True)
        t0 = time.time()
        res = inject_one(8, mu, a, verbose=True)
        res['units'] = None if res['mult'] is None else a - res['mult']
        with open(JSONL, 'a') as f: f.write(json.dumps(res) + "\n")
        mult = res['mult'] if res['mult'] is not None else '**< a**'
        units = res['units'] if res['units'] is not None else '**≥ 1**'
        with open(LEDGER, 'a') as f:
            f.write(f"| `{mu}` | {a} | {res['N_S']} | {res['stab']} | {res['n_chi']} | "
                    f"inject | {mult} | {units} | {round(res['secs'])} |\n")
        print(json.dumps({k: res[k] for k in ('lam','a','n_chi','mult','units','secs')}), flush=True)
        if res['mult'] is None:
            print(f"!!! STOP: NON-EMPTY permanent weight {mu} at delta=8 — "
                  f"the first permanent-specific equation on record.", flush=True)
            sys.exit(4)
    print("all nine empty: I(D_6^{per_3})_8 = 0", flush=True)


if __name__ == '__main__':
    delta = 8
    out, seen = outstanding(delta)
    tot = all_weights(delta)
    print(f"delta={delta}: {len(tot)} length-6 weights with a >= 1; "
          f"{len(seen)} measured, {len(out)} outstanding")
    bad = [(mu, v) for mu, v in seen.items() if v[1] is not None and v[1] != v[0]]
    print(f"measured non-empty (mult < a): {len(bad)}  {bad if bad else ''}")
    if '--run' in sys.argv:
        run(); sys.exit(0)
    if True:
        rows = []
        for mu, a in out:
            basis, vecs, group = None, None, None
            rows.append((mu, a))
        for mu, a in sorted(rows, key=lambda z: z[0]):
            print(f"   {mu}  a={a}")


