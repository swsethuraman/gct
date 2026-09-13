"""Exact certificate checks and adversarial controls for B14-08.

Witness differentiation, monomial enumeration, and birth-bound summation below
do not call the producer's arithmetic. Historical replay is explicitly separate.
"""
import argparse
from collections import Counter
from contextlib import redirect_stdout, redirect_stderr
import copy
from functools import lru_cache
import hashlib
import importlib.util
import io
import json
from math import comb, gcd, lcm, prod
from pathlib import Path
import subprocess
import sys
from types import SimpleNamespace
from unittest.mock import patch

import b14_08_audit as audit

ROOT = audit.ROOT
PRIMES = (2147483647, 2147483629)


def check(condition, message):
    if not condition:
        raise ValueError(message)


def compositions(n, r):
    if r == 1:
        yield (n,)
    else:
        for first in range(n+1):
            for rest in compositions(n-first, r-1):
                yield (first,)+rest


@lru_cache(None)
def independently_count_monomials(degree, weight):
    """Enumerate multisets by their next factor, rather than a coin recurrence."""
    weight = tuple(x for x in weight if x)
    if not weight:
        return int(degree == 0)
    # The distinguished u is filled last. Every other factor has positive tail.
    letters = [a for a in compositions(4, len(weight)) if sum(a[1:]) and
               all(x <= y for x, y in zip(a, weight))]

    @lru_cache(None)
    def visit(first, left, target):
        if not any(target[1:]):
            return int(target[0] == 4*left)
        if not left:
            return 0
        return sum(visit(i, left-1, tuple(b-a for a, b in zip(letter, target)))
                   for i, letter in enumerate(letters[first:], start=first)
                   if all(a <= b for a, b in zip(letter, target)))
    return visit(0, degree, weight)


def witness_polynomial(w):
    check(w['coefficient_convention'] == 'c_alpha(F)=[s^alpha]F', 'wrong normalization convention')
    check(w['values_are'] == 'primitive integer coefficients in ordinary c_alpha monomials',
          'wrong polynomial values_are')
    d, mu = w['degree'], w['weight']
    polynomial = Counter()
    for term in w['terms']:
        coefficient = term['coefficient']
        check(type(coefficient) is int and coefficient != 0, 'noninteger/zero coefficient')
        mon = []
        for factor in term['factors']:
            alpha, power = tuple(factor['alpha']), factor['power']
            check(len(alpha) == len(mu) and sum(alpha) == 4 and min(alpha) >= 0,
                  'invalid coefficient letter')
            check(type(power) is int and power > 0, 'invalid factor power')
            mon.extend([alpha]*power)
        check(len(mon) == d, 'wrong coefficient degree')
        check([sum(a[i] for a in mon) for i in range(len(mu))] == mu, 'wrong witness weight')
        polynomial[tuple(sorted(mon))] += coefficient
    check(polynomial and all(polynomial.values()), 'zero witness or cancelling duplicate terms')
    check(gcd(*polynomial.values()) == 1, 'nonprimitive normalization')
    check(polynomial[min(polynomial)] > 0, 'wrong normalization sign')
    norm = w['normalization']
    check(norm['cleared_lcm'] == lcm(*norm['rational_denominators']), 'wrong clearing denominator')
    check(all(gcd(norm['cleared_lcm'], p) == 1 for p in PRIMES), 'house-prime denominator')
    check(norm['denominators_coprime_to_house_primes'] is True, 'denominator declaration')
    return polynomial


def verify_witness(w):
    polynomial = witness_polynomial(w)
    roots = []
    # Differentiate one occurrence at a time, independently of the producer's
    # grouped-power formula. Include the boundary root into an unused variable.
    for root in range(len(w['weight'])):
        derivative = Counter()
        for mon, coefficient in polynomial.items():
            extended = [a+(0,) for a in mon]
            for occurrence, alpha in enumerate(extended):
                if alpha[root+1] == 0:
                    continue
                beta = list(alpha); beta[root] += 1; beta[root+1] -= 1
                changed = list(extended); changed[occurrence] = tuple(beta)
                derivative[tuple(sorted(changed))] += coefficient*(alpha[root]+1)
        derivative = {mon: c for mon, c in derivative.items() if c}
        check(not derivative, 'nonzero simple raising derivative')
        roots.append({'root': [root+1, root+2], 'integer_nonzero_terms': len(derivative)})
    # Beyond support all raising derivatives vanish because every alpha_j=0.
    modular = []
    for p in PRIMES:
        nonzero = sum(c % p != 0 for c in polynomial.values())
        check(nonzero > 0, 'zero witness modulo house prime')
        modular.append({'prime': p, 'nonzero_coefficients': nonzero, 'raising_zero': True})
    return {'id': w['id'], 'status': 'CERTIFIED factor HWV over Z; not ideal membership',
            'terms': len(polynomial), 'root_checks': roots, 'house_primes': modular,
            'verified_exactly_over_Z': True}


def verify_pair_witness(test, by_id):
    check(test['witness_id'] in by_id, 'missing required positive witness')
    w = by_id[test['witness_id']]
    check(w['degree'] == test['degree_difference'] and
          w['weight'] == [x for x in test['difference'] if x], 'wrong-source witness')


@lru_cache(None)
def birth_bound_closed_sum(r, d, s):
    populations = [comb(r+j-2, j) for j in range(1, 5)]
    total = 0
    for m3 in range(d+1):
        for m4 in range(d-m3+1):
            m2 = s-d-2*m3-3*m4
            m1 = d-m2-m3-m4
            if min(m1, m2) >= 0:
                total += prod(comb(n+m-1, m) for n, m in zip(populations, (m1, m2, m3, m4)))
    return total


def exclusion_policy(padded_floor, determinant_upper, upper_kind='determinant_ideal'):
    # Arithmetic policy only; this is deliberately not a source-certificate verifier.
    if padded_floor is None or determinant_upper is None or upper_kind != 'determinant_ideal':
        return 'OPEN'
    return 'EXCLUDED' if determinant_upper <= padded_floor else 'OPEN'


def expect_rejection(name, function, controls):
    try:
        function()
    except (ValueError, KeyError) as exc:
        controls.append({'name': name, 'status': 'PASS: rejected', 'reason': str(exc)})
    else:
        raise ValueError('control incorrectly accepted: '+name)


def local_controls(census_document, reference, rows, witnesses):
    controls = []
    expect_rejection('empty census', lambda: audit.read_targets({'rows': []}), controls)
    for control in sorted(audit.CONTROLS):
        bad = copy.deepcopy(census_document)
        target = next(r for r in bad['rows'] if audit.key(r) == control)
        # Preserve number, weight and length so the named-control check itself fires.
        target['partition'][0] += 20; target['partition'][1] -= 15
        target['partition'][2] = 1
        target['partition'][0] -= 4  # sum change = 20-15-1-4 = 0
        target['partition'] = sorted(target['partition'], reverse=True)
        expect_rejection('missing named control '+str(control), lambda: audit.read_targets(bad), controls)
    bad = copy.deepcopy(census_document); bad['rows'].append(copy.deepcopy(bad['rows'][0]))
    expect_rejection('duplicate census key', lambda: audit.read_targets(bad), controls)
    bad = copy.deepcopy(census_document); bad['rows'][0]['partition'][0] += 1
    expect_rejection('wrong total weight', lambda: audit.read_targets(bad), controls)
    for name in ('missing reference source', 'missing reference target', 'wrong reference source'):
        bad = copy.deepcopy(reference)
        if name == 'missing reference source': del bad['sources']['lmr']
        elif name == 'missing reference target': bad['targets'].pop()
        else: bad['sources']['lmr']['delta'] = 23
        expect_rejection(name, lambda: audit.validate_reference(bad, rows), controls)
    bad = copy.deepcopy(rows)
    control = next(r for r in bad if audit.key(r) in audit.CONTROLS)
    control['reached_by']['lmr'] = False
    check(control['reached_by']['rung13'], 'wrong-source mutation must retain another positive source')
    expect_rejection('wrong LMR source masked by rung13', lambda: audit.validate_flags(bad), controls)
    bad = copy.deepcopy(rows); next(r for r in bad if r['length'] == 10)['reached_by']['rung13'] = True
    expect_rejection('forced ten-row positive', lambda: audit.validate_flags(bad), controls)
    q = next(w for w in witnesses if w['degree'] == 2 and w['weight'] == [6, 2])
    bad = copy.deepcopy(q); bad['terms'][0]['coefficient'] += 1
    expect_rejection('altered HWV coefficient', lambda: verify_witness(bad), controls)
    bad = copy.deepcopy(q); bad['coefficient_convention'] = 'divided-power coefficients'
    expect_rejection('wrong tensor normalization', lambda: verify_witness(bad), controls)
    positive = next(t for r in rows for t in r['tests'] if t['witness_id'] == q['id'])
    expect_rejection('missing positive witness artifact', lambda: verify_pair_witness(positive, {}), controls)
    other = next(w for w in witnesses if w['degree'] == 2 and w['weight'] == [4, 4])
    expect_rejection('wrong source attached to witness ID',
                     lambda: verify_pair_witness(positive, {q['id']: other}), controls)
    bad = copy.deepcopy(q)
    bad['normalization']['rational_denominators'] = [PRIMES[0]]
    bad['normalization']['cleared_lcm'] = PRIMES[0]
    expect_rejection('normalization denominator hits house prime', lambda: verify_witness(bad), controls)
    for name, low, upper, kind, wanted in [
        ('missing padded certificate', None, 0, 'determinant_ideal', 'OPEN'),
        ('missing determinant certificate', 5, None, 'determinant_ideal', 'OPEN'),
        ('insufficient upper bound', 1, 2, 'determinant_ideal', 'OPEN'),
        ('tensor image bound mislabelled', 5, 2, 'product_image', 'OPEN'),
        ('sufficient synthetic bounds', 1, 1, 'determinant_ideal', 'EXCLUDED')]:
        actual = exclusion_policy(low, upper, kind)
        check(actual == wanted, 'exclusion policy: '+name)
        controls.append({'name': name, 'status': 'PASS', 'scope': 'synthetic arithmetic policy only', 'result': actual})
    # Two tiny exact character controls. No sampled evaluation or modular rank.
    for d, mu, wanted in [(1, (4,), 1), (1, (3, 1), 0), (2, (8,), 1),
                           (2, (7, 1), 0), (2, (6, 2), 1), (2, (5, 3), 0), (2, (4, 4), 1)]:
        actual, _ = audit.multiplicity(d, mu)
        check(actual == wanted, 'small exact character control')
        controls.append({'name': 'small character '+str((d, mu)), 'status': 'PASS', 'multiplicity': actual})
    return controls


def historical_controls(census_document, output_dir):
    spec = importlib.util.spec_from_file_location('historical_reach', ROOT/'analysis/b14_claude_reach.py')
    old = importlib.util.module_from_spec(spec); spec.loader.exec_module(old)
    original_reaches = old.reaches
    controls = []
    cases = [('valid replay', census_document, None, 0), ('empty census', {'rows': []}, None, 1)]
    for control in sorted(audit.CONTROLS):
        bad = copy.deepcopy(census_document)
        bad['rows'] = [r for r in bad['rows'] if audit.key(r) != control]
        cases.append(('missing control '+str(control), bad, None, 1))
    cases += [('wrong-source control', census_document, 'wrong-source', 1),
              ('forced ten-row positive', census_document, 'ten-row', 1)]
    for index, (name, document, mutation, expected) in enumerate(cases):
        transcript, errors = io.StringIO(), io.StringIO()
        path = output_dir/('historical_%02d.json' % index)
        def reaches(nu, lam, dl, dn, width):
            if mutation == 'wrong-source' and tuple(lam) == audit.SOURCES['lmr'][1] and (dn, tuple(nu)) in audit.CONTROLS:
                return False
            if mutation == 'ten-row' and len(nu) == 10:
                return True
            return original_reaches(nu, lam, dl, dn, width)
        with patch.object(old, 'json', SimpleNamespace(load=lambda stream: document, dump=json.dump)), \
             patch.object(old, 'reaches', reaches), \
             patch.object(sys, 'argv', ['b14_claude_reach.py', '--out', str(path)]), \
             redirect_stdout(transcript), redirect_stderr(errors):
            code = old.main()
        check(code == expected, 'historical control accepted: '+name)
        controls.append({'name': name, 'actual_exit': code, 'expected_exit': expected,
                         'status': 'PASS', 'stdout': transcript.getvalue(), 'stderr': errors.getvalue(),
                         'output': str(path.relative_to(ROOT)) if path.exists() else None})
    return controls


def verify_input_blobs():
    manifest = json.loads((ROOT/'results/b14_08/input_manifest.json').read_text())
    required = {'docs/dispatch/B14-08_packet.md', 'docs/batch14_board.md', 'docs/PROVED.md',
                'docs/brief_wording.md', 'docs/batch14_reconciliation.md',
                'docs/b14_claude_scratch_code.md', 'docs/b14_strategy_memo.md',
                'docs/s57_report.md', 'docs/b13_06_report.md', 'results/b13_06/components.json',
                'analysis/b14_claude_reach.py', 'results/b14_claude_reach.json',
                'results/b14_prep/ladder_recount.json', 'results/b13_06/run_summary.json',
                'analysis/b13_06_bound.py', 'tools/delivery/check_delivery.py'}
    check({e['path'] for e in manifest['files'] if e['git_blob']} == required,
          'missing or unexpected required input-manifest entry')
    check(manifest['base'] == audit.BASE and manifest['base_tree'] ==
          'cb688cd3fe454d638f3202e759e2eaa0c629739f', 'wrong input base')
    results = []
    for entry in manifest['files']:
        if entry['git_blob'] is None:
            # Dispatch files are provenance, not portable replay prerequisites.
            p = Path(entry['path'])
            status = 'RECORDED external provenance absent on receiver'
            if p.exists():
                check(hashlib.sha256(p.read_bytes()).hexdigest() == entry['sha256'], 'external provenance changed')
                status = 'external dispatch hash verified'
        else:
            p = ROOT/entry['path']
            check(p.is_file(), 'missing required input: '+entry['path'])
            # PROVED.md is append-only for this session; bind its inherited
            # assertions to the immutable base object, not our appended index.
            if entry['path'] == 'docs/PROVED.md':
                blob = subprocess.check_output(['git', 'rev-parse', audit.BASE+':'+entry['path']],
                                               cwd=ROOT, text=True).strip()
                frozen = subprocess.check_output(['git', 'show', audit.BASE+':'+entry['path']], cwd=ROOT)
                normalized = p.read_text(encoding='utf-8').replace('\r\n', '\n')
                check(normalized.startswith(frozen.decode().replace('\r\n', '\n')),
                      'inherited PROVED content changed')
            else:
                blob = subprocess.check_output(['git', 'hash-object', '--path='+entry['path'], entry['path']],
                                               cwd=ROOT, text=True).strip()
            check(blob == entry['git_blob'], 'required frozen input blob mismatch: '+entry['path'])
            status = 'frozen Git blob verified'
        results.append({'path': entry['path'], 'status': status})
    return results


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', type=Path, default=ROOT/'results/b14_08/verification.json')
    ap.add_argument('--data', type=Path, default=ROOT/'results/b14_08')
    args = ap.parse_args()
    args.data = args.data.resolve()
    args.out = args.out.resolve()
    input_checks = verify_input_blobs()
    document = json.loads((ROOT/'results/b13_06/components.json').read_text())
    reference = json.loads((ROOT/'results/b14_claude_reach.json').read_text())
    data = json.loads((args.data/'census.json').read_text())
    witness_data = json.loads((args.data/'witnesses.json').read_text())
    check(witness_data['status'] == 'complete', 'incomplete witness artifact')
    witnesses = witness_data['witnesses']
    check(len(witnesses) == len({w['id'] for w in witnesses}), 'duplicate witness id')
    rows = data['targets']
    check(data['sources'] == {s: {'degree': d, 'weight': list(w)}
                             for s, (d, w) in audit.SOURCES.items()}, 'wrong/missing census source metadata')
    source_rows = audit.read_targets(document)
    check({audit.key(r) for r in rows} == {audit.key(r) for r in source_rows}, 'complete key equality')
    audit.validate_reference(reference, source_rows)
    audit.validate_flags(rows)
    verified = [verify_witness(w) for w in witnesses]
    by_id = {w['id']: w for w in witnesses}
    tests, character_terms, inversions, positives = 0, 0, 0, 0
    for row in rows:
        d, nu = audit.key(row)
        check(len(row['tests']) == 3 and {t['source'] for t in row['tests']} == set(audit.SOURCES),
              'missing or duplicate source test')
        for test in row['tests']:
            tests += 1
            source_degree, source_weight = audit.SOURCES[test['source']]
            delta = d-source_degree
            diff = tuple((nu[i] if i < len(nu) else 0) -
                         (source_weight[i] if i < len(source_weight) else 0) for i in range(max(len(nu), len(source_weight))))
            check(list(diff) == test['difference'] and delta == test['degree_difference'], 'difference identity')
            expected_flag = next(r for r in reference['targets'] if audit.key(r) == (d, nu))['reached_by'][test['source']]
            check(test['reached'] is expected_flag and row['reached_by'][test['source']] is expected_flag, 'flag mismatch')
            if test['reason'] == 'not_dominant':
                i, j = test['failure_rows']
                check(j == i+1 and diff[i-1] < diff[j-1], 'false inversion certificate')
                check(not test['reached'], 'inversion marked reachable')
                inversions += 1
            else:
                check(min(diff) >= 0 and all(a >= b for a, b in zip(diff, diff[1:])), 'uncertified nondominance')
                mu = tuple(x for x in diff if x)
                value = 0
                for term in test['character_terms']:
                    actual = independently_count_monomials(delta, tuple(term['weight']))
                    check(actual == term['weight_monomials'], 'independent monomial count')
                    value += actual*term['alternant_coefficient']
                    character_terms += 1
                # Reconstruct the full alternant, not only the supplied sum.
                mult, expected_terms = audit.multiplicity(delta, mu)
                check(expected_terms == test['character_terms'] and value == mult == test['multiplicity'], 'character certificate')
                check(bool(value) == test['reached'], 'character flag')
            if test['reached']:
                positives += 1
                verify_pair_witness(test, by_id)
        b, t = row['lemma_B'], row['lemma_T']
        check(b['predecessor_degree'] == d-1 and b['predecessor_weight'] == [nu[0]-4, *nu[1:]], 'birth predecessor')
        check(b['scalar_tail_birth_upper_bound'] == birth_bound_closed_sum(len(nu), d, sum(nu[1:])), 'birth coefficient sum')
        if b['ambient_increment'] is not None:
            check(b['ambient_increment'] == b['ambient_target']-b['ambient_predecessor'] >= 0 and
                  b['birth_upper_bound'] == b['ambient_increment'], 'inherited numeric birth arithmetic')
        else:
            check(b['birth_upper_bound'] == b['scalar_tail_birth_upper_bound'], 'coarse bound not recorded')
        reached = [name for name in audit.SOURCES if row['reached_by'][name]]
        names = {'rung13': 'p13', 'rung14': 'p14', 'lmr': 'p24'}
        check(t['reached_sources'] == reached and t['conditional_padded_ideal_floor'] ==
              'max(0'+''.join(', '+names[s] for s in reached)+')', 'conditional transport floor')
        check(t['determinant_ideal_upper_bound'] == (1 if nu[1:] == (17,)+(2,)*7 else None),
              'unsupported determinant ideal upper bound')
        if len(nu) == 10:
            check(nu[8] == 2 and nu[9] > 0, 'ten-row proof scope')
        check(t['certified_padded_ideal_floor'] == 0 and t['source_floor_certificates'] is None and
              t['exclusion_status'] == 'OPEN', 'uncertified exclusion')
        check(exclusion_policy(0, t['determinant_ideal_upper_bound']) == 'OPEN', 'unexpected certified exclusion')
    controls = local_controls(document, reference, rows, witnesses)
    historical = historical_controls(document, args.data)
    check(tests == 717 and positives == 66 and len(verified) == 61, 'incomplete core certificate')
    results = {'board_numbering': 'batch14', 'session_id': 'B14-08',
               'status': 'PASS: complete finite transport audit; no ideal-membership or D-exclusion claim',
               'tests': tests, 'positive_pairs': positives, 'certified_factor_witnesses': len(verified),
               'dominance_inversion_certificates': inversions, 'independent_monomial_count_checks': character_terms,
               'input_checks': input_checks, 'witness_checks': verified,
               'controls': controls, 'historical_script_checks': historical,
               'birth_bounds_checked': len(rows), 'certified_exclusions': 0}
    audit.dump(args.out, results)
    print(json.dumps({k: v for k, v in results.items() if k not in
                     ('witness_checks', 'controls', 'historical_script_checks', 'input_checks')}))
    print('Local controls:', len(controls), '; historical replay/failure controls:', len(historical))


if __name__ == '__main__':
    main()
