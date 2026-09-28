#!/usr/bin/env python3
"""
B28-01c -- the refreshed gate rate file and Cell A repriced with R28-01 P3/P4.

Rates: B28-01a's calibration receipts (cal1 = (24,6,5,3,2)_10, cal2 =
(13,9,9,3,1,1)_9, both at 2147483647), mapped onto the phase model exactly as
analysis/b28_01_reprice.py does (maximum coefficient over the two cells; cD
floored at the preregistered 5e-10; evaluation charged to both cV and cR).  The
producer and verifier coefficient sets are both kept, with
rho_up = max_X cX_v / cX_p rounded up to 4 decimals (P3), in the gate rate file
the driver reads (schema b28-01c-gate-rates/1).

Cell A (n = N_S = 813,314, k = 8, a = 109) at z = 10n, 32n and f = 0.10%, 0.48%,
1.30% (U = a + ceil(f n)):
  time    producer B + S + 2 (H + V + R + D) + verifier max(direct, rho_up x producer model)
  memory  max(producer envelope, verifier estimate) (b28_01c_model.py), with the
          unknown row data bounded: rows = ceil(0.30 z) (calibration rows/z <= 0.277),
          z_R1 = z_Fo = z, ro = rows, nS = n - U.  At the gate the driver uses the
          actual values instead.

usage: b28_01c_reprice.py CALROOT OUTDIR
   CALROOT holds cal1/ and cal2/ (B28-01a's committed calibration receipts);
   writes OUTDIR/gate_rates_c.json, OUTDIR/host_rates_c.json, OUTDIR/cellA_price_c.json
"""
import sys, os, json, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import b28_01c_model as MODEL

BASE = dict(cB=2.1e-6, cS=5e-7, cH=8e-8, cV=2.7e-8, cR=1e-9, cD=5e-10)
CELLS = [('cal1', '24_6_5_3_2_d10', 2147483647), ('cal2', '13_9_9_3_1_1_d9', 2147483647)]
A = dict(n=813314, N_S=813314, k=8, a=109)
CAP_S = 86400; CAP_B = 24_000_000_000
ROWS_PER_NNZ = 0.30


def phases(lst):
    return {d['phase']: d for d in lst}


def main():
    root, out = sys.argv[1], sys.argv[2]
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
        per[name] = dict(tag=tag, n=n, k=k, a=a, z=z, U=U, rates_producer=prod, rates_verifier=ver,
                         verifier_peak_bytes={q: V[q]['peak_rss_bytes'] for q in V}, producer_peak_bytes={q: P[q]['peak_rss_bytes'] for q in P})
    producer = {c: max(per[x]['rates_producer'][c] for x in per) for c in BASE}
    verifier = {c: max(per[x]['rates_verifier'][c] for x in per) for c in BASE}
    rho = MODEL.ratio_up(producer, verifier)
    gate_rates = dict(schema='b28-01c-gate-rates/1', producer=producer, verifier=verifier, verifier_ratio_up=rho,
                      ratios={c: verifier[c] / producer[c] for c in BASE},
                      rule='coefficients: max over the two B28-01a calibration cells (cD floored at 5e-10; evaluation charged to both cV and cR); '
                           'verifier gate time = max(direct verifier model, verifier_ratio_up x producer model); verifier_ratio_up = max ratio rounded up to 4 decimals')
    n, N_S, k, a = A['n'], A['N_S'], A['k'], A['a']
    rows_out = []
    for zf in (10, 32):
        for f in (0.0010, 0.0048, 0.0130):
            z = zf * n; U = a + math.ceil(f * n)
            prod_rem, ver, det = MODEL.remaining_secs(n, k, a, z, U, 2, gate_rates)
            pm = det['producer_phase_secs']
            prod = pm['B'] + pm['S'] + prod_rem
            env = MODEL.mem_envelope(n, a, z, U)
            rows = math.ceil(ROWS_PER_NNZ * z)
            vmem, vterms = MODEL.verifier_mem(n, N_S, k, a, z, rows, U, n - U, rows, z, z)
            need = max(env, vmem)
            rows_out.append(dict(z_over_n=zf, f=f, z=z, U=U, producer_secs=round(prod, 1),
                                 verifier_direct_secs=round(det['verifier_direct_secs'], 1), verifier_ratio_secs=round(det['verifier_ratio_secs'], 1),
                                 verifier_gate_secs=round(ver, 1), total_secs=round(prod + ver, 1), total_hours=round((prod + ver) / 3600, 3),
                                 producer_phase_secs={q: round(v, 1) for q, v in pm.items()},
                                 mem_envelope_bytes=int(env), verifier_mem_estimate_bytes=int(vmem), verifier_mem_terms=vterms,
                                 mem_needed_bytes=int(need), fits_24h=bool(prod + ver <= CAP_S), fits_24GB=bool(need <= CAP_B),
                                 passes_gate_75pct_mem=bool(need <= 0.75 * CAP_B)))
    os.makedirs(out, exist_ok=True)
    json.dump(gate_rates, open(os.path.join(out, 'gate_rates_c.json'), 'w'), indent=1, sort_keys=True)
    json.dump(dict(schema='b28-01c-host-rates/1', baseline=BASE, per_cell=per, producer=producer, verifier=verifier, verifier_ratio_up=rho),
              open(os.path.join(out, 'host_rates_c.json'), 'w'), indent=1, sort_keys=True)
    json.dump(dict(schema='b28-01c-cellA-price/1', cell=dict(lam=[12, 8, 6, 4, 2], delta=8, a=109, n_chi=813314),
                   caps=dict(wall_secs=CAP_S, mem_bytes=CAP_B), scenario_assumptions=dict(rows_per_nnz=ROWS_PER_NNZ, z_R1='z', z_Fo='z', ro='rows', nS='n - U'),
                   scenarios=rows_out), open(os.path.join(out, 'cellA_price_c.json'), 'w'), indent=1, sort_keys=True)
    for r in rows_out:
        print(f"z={r['z_over_n']}n f={r['f']*100:.2f}% U={r['U']}: producer {r['producer_secs']/3600:.3f} h + verifier {r['verifier_gate_secs']/3600:.3f} h "
              f"(direct {r['verifier_direct_secs']:.1f} s, ratio {r['verifier_ratio_secs']:.1f} s) = {r['total_hours']:.3f} h; "
              f"envelope {r['mem_envelope_bytes']/1e9:.3f} GB, verifier est {r['verifier_mem_estimate_bytes']/1e9:.3f} GB; "
              f"fits24h={r['fits_24h']} fits24GB={r['fits_24GB']} gate75={r['passes_gate_75pct_mem']}")
    print('rho_up', rho)


if __name__ == '__main__':
    main()
