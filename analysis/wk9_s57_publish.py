#!/usr/bin/env python3
"""
Session 57 -- publish the banks as csv.gz (one file per (delta, ell) chunk, plus
the families, the below-region slices and the short ladders) and write
results/s57_selector.md from the analyses (ladder_status.json, short_ladders.json,
falsify.json, stable_a.jsonl, the family bank).

Columns of a chunk file: delta, ell, lam, tail, a, sk, h_pad, bal, stab, N_S,
N_S_status, nchi_est, reach, pad_forced, lemmaA_dead, transport, room, a_inf,
stable_bound, perm_dead_ladder.  Missing = pending.  A later session fills a
pending sk by keying on (delta, lam); nothing else needs recomputing.

usage: python3 wk9_s57_publish.py
"""
import sys, os, json, glob, csv, gzip, io, statistics
from collections import defaultdict, Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from wk9_s57_lib import (load_json_any, gzip_copy, tail_of, ladder_cell, negative_record, lmr_weight, count_region, ROOT, log)

CELLS = os.path.join(ROOT, 'results/s57_cells')
FIELDS = ['delta', 'ell', 'lam', 'tail', 'a', 'sk', 'h_pad', 'bal', 'stab', 'N_S', 'N_S_status', 'nchi_est', 'reach',
          'pad_forced', 'lemmaA_dead', 'transport', 'room', 'a_inf', 'stable_bound', 'perm_dead_ladder']

def fmt_lam(l): return '(' + ','.join(str(x) for x in l) + ')'

def write_csv_gz(path, rows, fields):
    buf = io.StringIO(); w = csv.DictWriter(buf, fieldnames=fields, extrasaction='ignore'); w.writeheader()
    for r in rows: w.writerow({k: ('' if r.get(k) is None else r.get(k)) for k in fields})
    with gzip.open(path, 'wt') as fh: fh.write(buf.getvalue())
    return os.path.getsize(path)

def load_json(name, default):
    return load_json_any(os.path.join(CELLS, name), default)

if __name__ == '__main__':
    ladder = load_json('ladder_status.json', {})
    status = ladder.get('status', {})
    stable = {}
    p = os.path.join(CELLS, 'stable_a.jsonl')
    if os.path.exists(p):
        for ln in open(p):
            r = json.loads(ln); stable[tuple(r['tail'])] = r['a_inf']
    perm_tails = {tuple(r['tail']) for r in ladder.get('record_ladders', []) if r['permanently_dead']}
    rec = negative_record()
    sizes = {}
    summary = {}
    # ---- chunk files
    for path in sorted(glob.glob(os.path.join(CELLS, 'bank_d*_l*.jsonl'))):
        rows = [json.loads(ln) for ln in open(path)]
        d, ell = rows[0]['delta'], rows[0]['ell']
        out = []
        c = Counter(); units = 0
        for r in rows:
            k = f"{d}|{','.join(map(str, r['lam']))}"
            st = status.get(k, {})
            t = tuple(r['tail'])
            row = dict(r, lam=fmt_lam(r['lam']), tail=fmt_lam(r['tail']), transport=st.get('status'), room=st.get('room'),
                       a_inf=stable.get(t), stable_bound=(d >= sum(t)), perm_dead_ladder=(t in perm_tails))
            out.append(row)
            if r['a'] >= 1:
                c['a>=1'] += 1; units += r['a']
                c['lemmaA_dead'] += bool(r['lemmaA_dead']); c['pad_forced'] += (r['pad_forced'] > 0)
                c[st.get('status', 'n/a')] += 1
                c[r['reach']] += 1
                c['N_S_exact'] += (r['N_S_status'] == 'exact')
        name = f"table_d{d}_l{ell}.csv.gz"
        sizes[name] = write_csv_gz(os.path.join(CELLS, name), out, FIELDS)
        summary[(d, ell)] = dict(cells=len(rows), a1=c['a>=1'], units=units, lemmaA=c['lemmaA_dead'], padf=c['pad_forced'],
                                 dbt=c['dead_by_transport'], bounded=c['bounded'], unc=c['unconstrained'],
                                 dense=c['dense'] + c['dense?'], sparse=c['sparse'] + c['sparse?'],
                                 beyond=c['beyond'] + c['beyond?'], exact=c['N_S_exact'])
        log(f"{name}: {len(rows)} rows, {sizes[name]/1024:.0f} KB")
    # ---- below-region slices
    p = os.path.join(CELLS, 'bank_below_l6.jsonl')
    below = []
    if os.path.exists(p):
        for ln in open(p):
            r = json.loads(ln); t = tuple(r['tail'])
            k = f"{r['delta']}|{','.join(map(str, r['lam']))}"
            below.append(dict(r, lam=fmt_lam(r['lam']), tail=fmt_lam(r['tail']), a_inf=stable.get(t),
                              stable_bound=(r['delta'] >= sum(t)), perm_dead_ladder=(t in perm_tails)))
        sizes['below_l6.csv.gz'] = write_csv_gz(os.path.join(CELLS, 'below_l6.csv.gz'), below, FIELDS + ['dead'])
    # ---- families, pivoted per cell
    fam = defaultdict(dict)
    p = os.path.join(CELLS, 'bank_families.jsonl')
    if os.path.exists(p):
        for ln in open(p):
            r = json.loads(ln); key = (tuple(r['lam']), r['delta'])
            fam[key].setdefault('family', r.get('family')); fam[key][r['col']] = r['value']
            fam[key][r['col'] + '_route'] = r['route']
            for x in ('nchi_est', 'status', 'reach', 'terms', 'g', 'T'):
                if x in r: fam[key][r['col'] + '_' + x] = r[x]
    frows = []
    for (lam, d), c in sorted(fam.items(), key=lambda kv: (kv[1].get('family') or '', kv[0][1], kv[0][0])):
        t = tail_of(lam)
        a = c.get('a_engine') if c.get('a_engine') is not None else c.get('a_weyl')
        frows.append(dict(family=c.get('family'), delta=d, ell=len(lam), lam=fmt_lam(lam), tail=fmt_lam(t), a=a,
                          a_engine=c.get('a_engine'), a_weyl=c.get('a_weyl'), sk=c.get('sk'), sk_note=(c.get('sk_route') if c.get('sk') is None else ''),
                          h_pad=c.get('h_pad'), pad_forced=(max(0, a - c['h_pad']) if (a is not None and c.get('h_pad') is not None) else None),
                          N_S=c.get('N_S'), N_S_status=c.get('N_S_status'), nchi_est=c.get('N_S_nchi_est'), reach=c.get('N_S_reach'),
                          a_inf=stable.get(t), stable_bound=(d >= sum(t)), bal=lam[0] - lam[-1]))
    sizes['families.csv.gz'] = write_csv_gz(os.path.join(CELLS, 'families.csv.gz'), frows,
                                            ['family', 'delta', 'ell', 'lam', 'tail', 'a', 'a_engine', 'a_weyl', 'sk', 'sk_note', 'h_pad', 'pad_forced',
                                             'N_S', 'N_S_status', 'nchi_est', 'reach', 'a_inf', 'stable_bound', 'bal'])
    json.dump(dict(sizes=sizes, summary={f"{d}|{e}": v for (d, e), v in summary.items()}, families=frows, below=below),
              open(os.path.join(CELLS, 'publish_summary.json'), 'w'))
    log("published; sizes: " + ", ".join(f"{k} {v/1024:.0f}KB" for k, v in sizes.items()))
    big = [k for k, v in sizes.items() if v > 5 * 1024 * 1024]
    assert not big, ("file over 5 MB", big)
