"""Read-only B15-12 receiver check; recomputes characters, not geometric ranks."""
import argparse
import copy
from fractions import Fraction
import json
from math import factorial
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'analysis'))
from wk8_s30_pleth import parts, zr, chi
from b15_12_orbit_bounds import square_type, padding_controls, character_controls, digest


def verify_rows(data):
    """Use the original banked character engine, with caches cleared per lambda."""
    degree = data['delta']
    n = 4 * degree
    rect = tuple(data['rectangle'])
    assert rect == (degree,) * 4
    records = data['rows']
    assert [tuple(r['rho']) for r in records] == list(parts(n))
    order = factorial(n)
    for r in records:
        rho = tuple(r['rho'])
        assert r['z'] == zr(rho)
        assert r['class_size'] == order // zr(rho)
        assert r['rectangle_character'] == chi(rect, rho)
        assert r['rectangle_squared_cycle_character'] == chi(rect, square_type(rho))
    assert sum(r['class_size'] for r in records) == order
    chi.cache_clear()
    results = []
    for k, lam in enumerate(data['lambdas']):
        g, t, norm = 0, 0, 0
        for r in records:
            value = chi(tuple(lam), tuple(r['rho']))
            assert value == r['lambda_characters'][k]
            norm += r['class_size'] * value * value
            g += r['class_size'] * value * r['rectangle_character']**2
            t += r['class_size'] * value * r['rectangle_squared_cycle_character']
        assert norm == order
        assert g % order == t % order == 0
        g, t = g // order, t // order
        assert (g+t) % 2 == 0 and (g-t) % 2 == 0 and g >= abs(t)
        results.append(dict(lam=lam, rectangular_orbit_ub=g, symmetric_orbit_ub=(g+t)//2))
        chi.cache_clear()
    return results


def fixture():
    rect = (1, 1, 1, 1)
    ps = parts(4)
    data = dict(delta=1, rectangle=list(rect), lambdas=[list(p) for p in ps], rows=[])
    for rho in ps:
        data['rows'].append(dict(rho=list(rho), z=zr(rho), class_size=24//zr(rho),
                                 rectangle_character=chi(rect,rho),
                                 rectangle_squared_cycle_character=chi(rect,square_type(rho)),
                                 lambda_characters=[chi(lam,rho) for lam in ps]))
    assert verify_rows(data)[0]['symmetric_orbit_ub'] == 1
    broken = copy.deepcopy(data)
    broken['rows'][0]['rectangle_character'] += 1
    try:
        verify_rows(broken)
    except AssertionError:
        rejected = True
    else:
        rejected = False
    assert rejected
    return dict(status='EXACT', S4_certificate_checked=True, altered_character_rejected=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--controls-only', action='store_true')
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    start = time.perf_counter()
    stored = json.loads((ROOT/'results/b15_12/controls.json').read_text())
    assert padding_controls() == stored['padding']
    assert character_controls() == stored['character']
    report = dict(status='EXACT', model='gpt-6-astra', fixture=fixture(),
                  padding_certificate_reconstructed=True,
                  independent_character_controls_reconstructed=True,
                  geometric_determinant_rank_replayed=False,
                  full_character_pilot_replayed=False)
    if not args.controls_only:
        pilot = json.loads((ROOT/'results/b15_12/pilot.json').read_text())
        groups = {}
        for f in pilot['class_files']:
            p = ROOT/'results/b15_12'/f['path']
            assert digest(p) == f['sha256']
            d = json.loads(p.read_text())
            if d['delta'] not in groups:
                groups[d['delta']] = d
            else:
                g = groups[d['delta']]
                assert g['rectangle'] == d['rectangle'] and g['lambdas'] == d['lambdas']
                g['rows'].extend(d['rows'])
        results = []
        for degree, d in sorted(groups.items()):
            rows = verify_rows(d)
            for r in rows:
                c = next(c for c in pilot['cells'] if c['delta']==degree and c['lam']==r['lam'])
                assert c['rectangular_orbit_ub']==r['rectangular_orbit_ub']
                assert c['symmetric_orbit_ub']==r['symmetric_orbit_ub']
                assert c['U_det_ub']==min(c['ambient_multiplicity'],r['symmetric_orbit_ub'])
                assert c['determinant_rank_lb']<=c['U_det_ub']
            results.extend(rows)
        assert len(results) == 7
        report.update(full_character_pilot_replayed=True, cells=results)
    report['wall_seconds'] = time.perf_counter()-start
    p = Path(args.output).resolve()
    assert p.is_relative_to(ROOT)
    p.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report), flush=True)


if __name__ == '__main__':
    main()
