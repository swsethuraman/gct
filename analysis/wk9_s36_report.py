#!/usr/bin/env python3
"""Session 36 -- coverage per stratum from the ledger and the census (cells and ambient units)."""
import sys, os, pickle
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.join(HERE, '..')

def read_ledger():
    rows = []
    for ln in open(os.path.join(ROOT, 'results', 's36_ledger.md')):
        if ln.startswith('| A') or ln.startswith('| B'):
            c = [x.strip() for x in ln.strip().strip('|').split('|')]
            rows.append(dict(strat=c[0], lam=eval(c[1].strip('`')), delta=int(c[2]), ell=int(c[3]),
                             a=int(c[4]), N_S=int(c[5]), stab=int(c[6]), n_chi=int(c[7]),
                             mult_det=int(c[10]), mult_pad=int(c[11]), D=int(c[12]), secs=int(c[13])))
    return rows

if __name__ == '__main__':
    r6, r7 = pickle.load(open('/root/s36/census.pkl', 'rb'))
    led = read_ledger()
    done = {(x['lam'], x['delta']): x for x in led}
    s30 = set()
    for ln in open(os.path.join(ROOT, 'results', 'sweep62_ledger.md')):
        if ln.startswith("| ("): s30.add(eval(ln.split('|')[1].strip()))
    strata = {
        'A  (delta 6, ell 5; the 33 s30 left unmeasured)': [x for x in r6 if x['ell'] == 5 and x['lam'] not in s30],
        'A  (delta 6, ell 5; all 67 incl. s27/s30)': [x for x in r6 if x['ell'] == 5],
        'B6 (delta 6, ell 6)': [x for x in r6 if x['ell'] == 6],
        'B7 (delta 7, ell 6)': [x for x in r7 if x['ell'] == 6],
        'A7 (delta 7, ell 5, outside s34 domain)': [x for x in r7 if x['ell'] == 5 and not x['s34']],
    }
    print("| stratum | cells | measured (this session) | ambient units | measured units | fit budget | D<0 cells | D>0 cells |")
    print("|---|---|---|---|---|---|---|---|")
    for name, cells in strata.items():
        delta = 6 if 'delta 6' in name else 7
        meas = [x for x in cells if (x['lam'], delta) in done]
        ns30 = 0
        if 'incl. s27/s30' in name:
            meas_units = sum(x['a'] for x in meas) + sum(x['a'] for x in cells if x['lam'] in s30)
            ns30 = sum(1 for x in cells if x['lam'] in s30)
            nmeas = f"{len(meas)} + {ns30} (s27/s30) = {len(meas)+ns30}"
        else:
            meas_units = sum(x['a'] for x in meas); nmeas = str(len(meas))
        neg = sum(1 for x in meas if done[(x['lam'], delta)]['D'] < 0)
        pos = sum(1 for x in meas if done[(x['lam'], delta)]['D'] > 0)
        print(f"| {name} | {len(cells)} | {nmeas} ({100*(len(meas)+(ns30 if 'incl' in name else 0))/len(cells):.0f}%) | "
              f"{sum(x['a'] for x in cells)} | {meas_units} ({100*meas_units/sum(x['a'] for x in cells):.0f}%) | "
              f"{sum(1 for x in cells if x['fits'])} | {neg} | {pos} |")
    print()
    print("per-stratum axes reached (measured this session):")
    for name, cells in strata.items():
        delta = 6 if 'delta 6' in name else 7
        meas = [done[(x['lam'], delta)] for x in cells if (x['lam'], delta) in done]
        if not meas: continue
        bal = [x['lam'][0] - x['lam'][-1] for x in meas]
        print(f"  {name}: n_chi {min(x['n_chi'] for x in meas)}–{max(x['n_chi'] for x in meas)}, "
              f"N_S up to {max(x['N_S'] for x in meas)}, a {min(x['a'] for x in meas)}–{max(x['a'] for x in meas)}, "
              f"balance {min(bal)}–{max(bal)}, total {sum(x['secs'] for x in meas)/60:.0f} min")
