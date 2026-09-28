#!/usr/bin/env python3
"""
B28-01 -- host rates from the calibration receipts, and Cell A repriced.

Phase model (B27-06 PREREGISTRATION.md), seconds:
  B = cB n k   S = cS z   H = cH z U   V = cV (a+8) n k   R = cR (a+8) n a   D = cD U^3
Measured phases are mapped onto it as follows (per calibration cell, then the
MAXIMUM coefficient over the two cells is kept):
  cB <- build / (n k)                     cS <- cover / z
  cH <- (schur - nullspace + lift_check) / (z U)
  cD <- max(baseline 5e-10, nullspace / U^3)   (U is small at calibration)
  cV <- evaluation / ((a+8) n k)  and  cR <- evaluation / ((a+8) n a)
        (the whole evaluation phase is charged to BOTH terms: a deliberate
        double count, because rows and contraction were not timed apart)
and likewise for the verifier's phases (its schur phase includes its own
rank of G, and its build includes E).
Cell A total = producer (B + S + 2 (H + V + R + D), two sequential primes)
             + verifier (Bv + Sv + Hv + Vv + Rv + Dv, one independent rebuild/replay).
Memory = the preregistered envelope 16na + 100z + 400n + 5 max(2.5e8, 128n) + 80U^2 + 5e8,
reported with the measured calibration peaks.

usage: b28_01_reprice.py OUTROOT  -> writes OUTROOT/host_rates.json, OUTROOT/cellA_price.json
"""
import sys, os, json, math

BASE = dict(cB=2.1e-6, cS=5e-7, cH=8e-8, cV=2.7e-8, cR=1e-9, cD=5e-10)
CELLS = [('cal1', '24_6_5_3_2_d10', 2147483647), ('cal2', '13_9_9_3_1_1_d9', 2147483647)]
A = dict(n=813314, k=8, a=109)
CAP_S = 24 * 3600; CAP_B = 24_000_000_000


def phases(lst):
    return {d['phase']: d for d in lst}


def main():
    root = sys.argv[1]
    per = {}
    for name, tag, p in CELLS:
        d = os.path.join(root, name)
        cell = json.load(open(os.path.join(d, f'{tag}_cell.json')))
        rc = json.load(open(os.path.join(d, f'{tag}_receipt.json')))
        vr = json.load(open(os.path.join(d, f'{tag}_p{p}_verify_receipt.json')))
        P = phases(rc['phases']); V = phases(vr['phases'])
        n, k, a = cell['n_chi'], cell['delta'], cell['a']
        z, U = cell['nnz_E'], cell['cover']['nU']
        nul = P['schur']['nullspace_secs']
        prod = dict(cB=P['build']['secs'] / (n * k), cS=P['cover']['secs'] / z,
                    cH=(P['schur']['secs'] - nul + P['lift_check']['secs']) / (z * U),
                    cD=max(BASE['cD'], nul / U ** 3),
                    cV=P['evaluation']['secs'] / ((a + 8) * n * k), cR=P['evaluation']['secs'] / ((a + 8) * n * a))
        ver = dict(cB=V['build']['secs'] / (n * k), cS=V['cover']['secs'] / z,
                   cH=(V['schur']['secs'] + V['lift_check']['secs']) / (z * U), cD=BASE['cD'],
                   cV=V['evaluation']['secs'] / ((a + 8) * n * k), cR=V['evaluation']['secs'] / ((a + 8) * n * a))
        per[name] = dict(tag=tag, n=n, k=k, a=a, z=z, U=U, z_over_n=round(z / n, 3), f=round((U - a) / n, 6),
                         producer_phases={q: P[q]['secs'] for q in ('build', 'cover', 'schur', 'lift_check', 'evaluation')},
                         producer_peak_bytes={q: P[q]['peak_rss_bytes'] for q in P},
                         verifier_phases={q: V[q]['secs'] for q in V}, verifier_peak_bytes={q: V[q]['peak_rss_bytes'] for q in V},
                         producer_total_secs=rc.get('total_secs'), verifier_total_secs=vr.get('total_secs'),
                         rates_producer=prod, rates_verifier=ver)
    host = dict(producer={c: max(per[x]['rates_producer'][c] for x in per) for c in BASE},
                verifier={c: max(per[x]['rates_verifier'][c] for x in per) for c in BASE})
    # the driver's gate reads one coefficient set plus a verifier factor (verifier seconds / producer one-prime seconds)
    def model(r, n, k, a, z, U):
        return dict(B=r['cB'] * n * k, S=r['cS'] * z, H=r['cH'] * z * U, V=r['cV'] * (a + 8) * n * k,
                    R=r['cR'] * (a + 8) * n * a, D=r['cD'] * U ** 3)
    n, k, a = A['n'], A['k'], A['a']
    rows = []
    for zf in (10, 32):
        for f in (0.0010, 0.0048, 0.0130):
            z = zf * n; U = a + math.ceil(f * n)
            pm = model(host['producer'], n, k, a, z, U); vm = model(host['verifier'], n, k, a, z, U)
            pass_ = pm['H'] + pm['V'] + pm['R'] + pm['D']
            prod = pm['B'] + pm['S'] + 2 * pass_
            ver = sum(vm.values())
            env = 16 * n * a + 100 * z + 400 * n + 5 * max(250_000_000, 128 * n) + 80 * U * U + 500_000_000
            rows.append(dict(z_over_n=zf, f=f, z=z, U=U, producer_secs=round(prod, 1), verifier_secs=round(ver, 1),
                             total_secs=round(prod + ver, 1), total_hours=round((prod + ver) / 3600, 3),
                             producer_phase_secs={q: round(v, 1) for q, v in pm.items()},
                             verifier_phase_secs={q: round(v, 1) for q, v in vm.items()},
                             mem_envelope_bytes=int(env), fits_24h=bool(prod + ver <= CAP_S), fits_24GB=bool(env <= CAP_B),
                             passes_gate_75pct_mem=bool(env <= 0.75 * CAP_B)))
    vf = max((sum(model(host['verifier'], c['n'], c['k'], c['a'], c['z'], c['U']).values()) /
              sum(model(host['producer'], c['n'], c['k'], c['a'], c['z'], c['U']).values())) for c in per.values())
    gate_rates = dict(host['producer']); gate_rates['verifier_factor'] = round(vf, 4)
    json.dump(dict(schema='b28-01-host-rates/1', rule='max over the two calibration cells; cD floored at the preregistered 5e-10; evaluation charged to both cV and cR',
                   baseline=BASE, producer=host['producer'], verifier=host['verifier'], gate_rates=gate_rates, per_cell=per),
              open(os.path.join(root, 'host_rates.json'), 'w'), indent=1, sort_keys=True)
    json.dump(gate_rates, open(os.path.join(root, 'gate_rates.json'), 'w'), indent=1, sort_keys=True)
    json.dump(dict(schema='b28-01-cellA-price/1', cell=dict(lam=[12, 8, 6, 4, 2], delta=8, a=109, n_chi=813314),
                   caps=dict(wall_secs=CAP_S, mem_bytes=CAP_B), scenarios=rows),
              open(os.path.join(root, 'cellA_price.json'), 'w'), indent=1, sort_keys=True)
    for r in rows:
        print(f"z={r['z_over_n']}n f={r['f']*100:.2f}% U={r['U']}: producer {r['producer_secs']/3600:.2f} h + verifier {r['verifier_secs']/3600:.2f} h "
              f"= {r['total_hours']:.2f} h; envelope {r['mem_envelope_bytes']/1e9:.1f} GB; fits24h={r['fits_24h']} fits24GB={r['fits_24GB']} gate75={r['passes_gate_75pct_mem']}")
    print('gate_rates', gate_rates)


if __name__ == '__main__':
    main()
