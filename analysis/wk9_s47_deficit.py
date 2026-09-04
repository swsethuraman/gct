#!/usr/bin/env python3
"""
Session 47, Phase B direction 3 -- the rank deficit across the whole record.

mult_red(lam,delta) = rank of the Foulkes-Howe map mu*_delta on the lambda
multiplicity space, a map C^a -> C^{h_pad} (results/PREREG_s47.md sec 1).  So

    d(lam,delta) := min(a, h_pad) - mult_red   >= 0

is the RANK DEFICIT: d = 0 says mu_lambda has maximal rank.  The exactness
conjecture is 'd = 0 whenever h_pad < a'.  This script tabulates d at every cell
of the record where a, h_pad and mult_red are all known, taken from the banked
tables (session 36 via results/s42_hpad_banked.md, session 42 via its cells
jsonl, sessions 43/45 via results/sixrow_record.md), and stratifies the deficit
rate by h_pad - a.

usage: python3 wk9_s47_deficit.py
"""
import json, os, re, glob, sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
R = lambda *p: os.path.join(ROOT, *p)


def from_s36_banked():
    """results/s42_hpad_banked.md: lam | delta | a | mult_det | mult_pad | mult_red | h_pad | ..."""
    out = []
    p = R('results', 's42_hpad_banked.md')
    if not os.path.exists(p): return out
    for line in open(p):
        line = line.strip()
        if not line.startswith('| `('): continue
        c = [x.strip() for x in line.strip('|').split('|')]
        lam = tuple(int(v) for v in c[0].strip('`()').split(','))
        out.append(dict(lam=lam, delta=int(c[1]), a=int(c[2]), mult_red=int(c[5]),
                        h_pad=int(c[6]), src='s36'))
    return out


def from_s42_cells():
    out = []
    for f in glob.glob(R('results', 's42_cells_*.jsonl')):
        for L in open(f):
            L = L.strip()
            if not L: continue
            r = json.loads(L)
            if r.get('h_pad') is None or r.get('mult_red') is None: continue
            out.append(dict(lam=tuple(r['lam']), delta=r['delta'], a=r['a'],
                            mult_red=r['mult_red'], h_pad=r['h_pad'], src='s42'))
    return out


def from_sixrow_record():
    """results/sixrow_record.md pad-side table: delta | lam | a | mult_pad | D | h_pad | ...
    mult_pad = mult_red at every cell of that table (stated there)."""
    out = []
    p = R('results', 'sixrow_record.md')
    if not os.path.exists(p): return out
    for line in open(p):
        line = line.strip()
        if not re.match(r'^\|\s*\d+\s*\|\s*`\(', line): continue
        c = [x.strip() for x in line.strip('|').split('|')]
        try:
            delta = int(c[0]); lam = tuple(int(v) for v in c[1].strip('`()').split(','))
            a = int(c[2]); mr = int(c[3]); h = int(c[5].strip('*'))
        except Exception:
            continue
        out.append(dict(lam=lam, delta=delta, a=a, mult_red=mr, h_pad=h, src='sixrow'))
    return out


def record():
    seen, out = {}, []
    for src in (from_sixrow_record(), from_s36_banked(), from_s42_cells()):
        for r in src:
            k = (r['lam'], r['delta'])
            if k in seen:
                old = seen[k]
                assert (old['a'], old['h_pad'], old['mult_red']) == (r['a'], r['h_pad'], r['mult_red']), \
                    ('record disagrees with itself at', k, old, r)
                continue
            seen[k] = r; out.append(r)
    for r in out:
        r['d'] = min(r['a'], r['h_pad']) - r['mult_red']
        r['e'] = r['h_pad'] - r['a']
        assert r['d'] >= 0, ('mult_red > min(a,h_pad) -- impossible', r)
    return out


if __name__ == '__main__':
    rec = record()
    print(f"cells with a, h_pad and mult_red all known: {len(rec)}")
    print(f"  sources: {dict(Counter(r['src'] for r in rec))}")
    bad = [r for r in rec if r['d'] > 0]
    print(f"  rank deficit d > 0 at {len(bad)} of {len(rec)}")
    print()
    print("  every cell with d > 0:")
    print("  %-28s %2s %4s %6s %8s %4s %4s" % ('lam', 'd', 'a', 'h_pad', 'mult_red', 'def', 'e'))
    for r in sorted(bad, key=lambda z: (z['e'], z['delta'])):
        print("  %-28s %2d %4d %6d %8d %4d %4d" % (str(r['lam']), r['delta'], r['a'],
                                                   r['h_pad'], r['mult_red'], r['d'], r['e']))
    print()
    print("  deficit rate stratified by e = h_pad - a:")
    tot = Counter(r['e'] for r in rec); dd = Counter(r['e'] for r in bad)
    print("   %6s %7s %7s %8s" % ('e', 'cells', 'd>0', 'rate'))
    for e in sorted(tot):
        if tot[e] >= 1:
            print("   %6d %7d %7d %8s" % (e, tot[e], dd[e], f"{dd[e]/tot[e]:.0%}"))
    print()
    fire = [r for r in rec if r['e'] < 0]
    print(f"  FIRING cells (h_pad < a) in the record: {len(fire)}; d > 0 at {sum(1 for r in fire if r['d']>0)}")
    nt = [r for r in fire if r['h_pad'] > 0]
    print(f"    of which nontrivial (h_pad > 0): {len(nt)}; d > 0 at {sum(1 for r in nt if r['d']>0)}")
    print()
    print("  parity of e at deficit cells:", dict(Counter(r['e'] % 2 for r in bad)),
          " over the record:", dict(Counter(r['e'] % 2 for r in rec)))
