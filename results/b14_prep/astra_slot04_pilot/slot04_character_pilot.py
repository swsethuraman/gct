"""Bounded planning pilot, not a pre-registered Batch 14 result.

Uses the banked session-30 power-sum / Murnaghan-Nakayama route, not a_weyl
or the Claude scratch counters. Independently enumerates interlacing strips.
Arguments: accepted checkout, degree (13 or 14), output JSON.
"""
import itertools
import json
from pathlib import Path
import sys
import time

root = Path(sys.argv[1]).resolve()
degree = int(sys.argv[2])
output = Path(sys.argv[3]).resolve()
sys.path.insert(0, str(root / 'analysis'))
from wk8_s30_pleth import pleth_p, chi

started = time.monotonic()
lam = (4 * degree - 31, 17, 2, 2, 2, 2, 2, 2, 2)
limits = list(zip(lam[1:] + (0,), lam))
shapes = sorted({tuple(x for x in mu if x) for mu in
                 itertools.product(*(range(lo, hi + 1) for lo, hi in limits))
                 if sum(mu) == 3 * degree}, reverse=True)
print('interlacing_shapes', len(shapes), flush=True)
power = pleth_p(degree, 3)
print('power_terms', len(power), 'seconds', time.monotonic()-started, flush=True)
rows = []
complete = True
for mu in shapes:
    value = 0
    for index, (rho, coeff) in enumerate(power.items()):
        value += coeff * chi(mu, rho)
        if index % 256 == 0 and time.monotonic()-started > 75:
            complete = False
            break
    if not complete:
        break
    assert value.denominator == 1
    assert value >= 0
    rows.append({'mu': list(mu), 'a3': int(value)})
    print('channel', len(rows), '/', len(shapes), int(value), flush=True)
    if chi.cache_info().currsize > 250000:
        chi.cache_clear()
elapsed = time.monotonic() - started
result = {'status': 'PLANNING PILOT, NOT PREREGISTERED', 'degree': degree,
          'lambda': list(lam), 'method': 'power-sum cycle index and Murnaghan-Nakayama',
          'implementation': 'banked wk8_s30_pleth.pleth_p and chi; new interlacing enumeration',
          'complete': complete, 'shapes': len(shapes), 'power_terms': len(power),
          'rows': rows, 'h': sum(x['a3'] for x in rows) if complete else None,
          'seconds': elapsed, 'chi_cache': chi.cache_info()._asdict()}
output.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print(json.dumps({k: result[k] for k in ('degree', 'complete', 'h', 'seconds')}), flush=True)
