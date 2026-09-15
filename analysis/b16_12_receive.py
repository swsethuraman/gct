"""B16-12 bounded adversarial receiver. New code; no producer imports/count production.

Run through the inspected analysis/b15_bound.py with -B, 60 s, 512 MiB.
Proofs live in docs/b16_12_proof.md. Saved characters are inherited, not regenerated.
"""
import argparse
from fractions import Fraction as Q
from itertools import permutations
from pathlib import Path
import gzip
import hashlib
import json
import os
import time

ROOT = Path(__file__).resolve().parents[4]
WORK = Path(__file__).resolve().parents[1]
OUT = WORK / 'results/b16_12'
DREAM = ROOT / 'Batch15_Launch/native_20260913/reviews_filesystem/Dream_Upper288'
N = 7
ZERO = (0,) * N
READS = {}


def read(path, parse=True):
    path = Path(path).resolve()
    raw = path.read_bytes()
    READS[str(path)] = {'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}
    return json.loads(raw) if parse else raw


def check_time():
    if time.monotonic() + 2 > float(os.environ['CI73_DEADLINE']):
        raise RuntimeError('Incomplete: nearing enforced deadline')


class P(dict):
    """Tiny exact polynomial ring, seven indeterminates, rational coefficients."""
    def __add__(self, other):
        if not isinstance(other, dict):
            other = {ZERO: Q(other)}
        out = P(self)
        for e, c in other.items():
            out[e] = out.get(e, 0) + c
            if not out[e]:
                del out[e]
        return out

    __radd__ = __add__

    def __neg__(self):
        return P({e: -c for e, c in self.items()})

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        if not isinstance(other, dict):
            other = {ZERO: Q(other)}
        out = P()
        for a, b in self.items():
            for c, d in other.items():
                e = tuple(x+y for x, y in zip(a, c))
                out[e] = out.get(e, 0) + b*d
        return P({e: c for e, c in out.items() if c})

    __rmul__ = __mul__

    def __pow__(self, n):
        out = P({ZERO: Q(1)})
        for _ in range(n):
            out = out*self
        return out

    def diff(self, i):
        out = P()
        for e, c in self.items():
            if e[i]:
                f = list(e)
                f[i] -= 1
                out[tuple(f)] = c*e[i]
        return out


def variables():
    return [P({tuple(int(i==j) for j in range(N)): Q(1)}) for i in range(N)]


def det(a):
    out = P()
    for perm in permutations(range(len(a))):
        sign = (-1)**sum(perm[i] > perm[j] for i in range(len(a)) for j in range(i+1, len(a)))
        term = P({ZERO: Q(sign)})
        for i, j in enumerate(perm):
            term = term*a[i][j]
        out = out + term
    return out


def terms(p):
    return [[list(e), c.numerator, c.denominator] for e, c in sorted(p.items())]


def controls():
    c, l, q, r, h, _, _ = variables()
    # Binary restriction of the universal multivariate depression formulas.
    lp = l+3*c*h
    qp = q+2*l*h+3*c*h**2
    rp = r+q*h+l*h**2+c*h**3
    A = 3*c*q-l**2
    B = 27*c**2*r-9*c*l*q+2*l**3
    assert 3*c*qp-lp**2 == A
    assert 27*c**2*rp-9*c*lp*qp+2*lp**3 == B
    assert 27*c**2*rp-9*c*lp*qp-2*lp**3 != B
    # Exact tiny Hessian control; arbitrary-nine-variable proof is in the memo.
    z, x, y, *_ = variables()
    C = x**3+x*y**2+y**3
    F = z*C
    HC = [[C.diff(i).diff(j) for j in (1, 2)] for i in (1, 2)]
    HF = [[F.diff(i).diff(j) for j in (0, 1, 2)] for i in (0, 1, 2)]
    lhs, rhs = 2*det(HF), -3*z*C*det(HC)
    assert lhs == rhs and lhs
    assert lhs != -rhs
    s2, s3, s4, t0, t1, t2, t3 = variables()
    # Coefficients of p*T for arbitrary T=t0+t1*t+t2*t^2+t3*t^3.
    S7, S6, S5 = t3, t2, t1+s2*t3
    S3 = s2*t1+s3*t2+s4*t3
    rel = S3-s2*S5-s3*S6-(s4-s2**2)*S7
    assert not rel
    assert S3-s2*S5-s3*S6-(s4+s2**2)*S7
    return {'chart': {'A_3cQ_minus_L2': terms(A), 'B_27c2R_minus_9cLQ_plus_2L3': terms(B),
                      'shear_invariance': True, 'wrong_cubic_sign_rejected': True},
            'tiny_hessian': {'variables': ['z', 'x', 'y'], 'C': terms(C),
                             'two_det_H_zC': terms(lhs), 'negative_sign_checked': True,
                             'scope': 'Instrument control in three variables; general proof separate'},
            'shared_remainder': {'five_expression_relation': [1, -1, -1, -1, 1],
                                 'expression_order': ['S3', 's2*S5', 's3*S6', 's4*S7', 's2^2*S7'],
                                 'identity': True, 'wrong_sign_rejected': True}}


def inherited_arithmetic():
    saved = read(DREAM / 'cubic_bound.json')
    rows = []
    for row in saved['rows']:
        check_time()
        b = row['b']
        raw = read(DREAM / f'cubic_tail_{b}.json.gz', False)
        cert = json.loads(gzip.decompress(raw))
        assert cert['row'] == row
        total = Q(0)
        records = cert['power_sum_numerator_denominator_character_rows']
        assert len(records) == row['terms']
        assert row['tail'] == [b]+[2]*7
        for rho, num, den, character in records:
            assert rho == sorted(rho, reverse=True) and sum(rho) == b+14
            assert den > 0 and isinstance(character, int)
            total += Q(num, den)*character
        assert total == row['stable_cubic_upper']
        rows.append({'b': b, 'sum': int(total), 'terms': len(records)})
    assert [r['b'] for r in rows] == list(range(2, 20))
    channels = []
    for d, t in ((23, 15), (25, 17), (26, 17), (27, 19), (35, 19)):
        lam = [4*d-t-16, t]+[2]*8
        mus = [[3*d-14-b, b]+[2]*7 for b in range(2, t+1)]
        for mu in mus:
            assert sum(mu) == 3*d
            ext = mu+[0]
            assert all(lam[i] >= ext[i] >= (lam+[0])[i+1] for i in range(10))
            assert sum(lam)-sum(mu) == d
        upper = sum(r['sum'] for r in rows if r['b'] <= t)
        assert upper == saved['sum_b_2_through_t'][str(t)]
        channels.append({'degree': d, 'lambda': lam, 'cubic_channels': mus, 'padding_upper': upper})
    return {'rows': rows, 'cells': channels, 'saved_terms_checked': sum(r['terms'] for r in rows),
            'fresh': 'Exact rational sums of saved complete terms; degree/strip checks',
            'inherited': 'Completeness and correctness of power sums and characters; no regenerated census',
            'stable': {'a': 429, 'm_det': 418, 'm_pad_lower': 243, 'm_pad_upper': 288,
                       'D_interval': [243-418, 288-418], 'i_pad_interval': [429-288, 429-243]}}


def arithmetic_gate(a, q, r, q_cell, r_cell, a_cell, rank_kind='actual_padding_floor', global_proof=True):
    if None in (a, q, r) or not q_cell == r_cell == a_cell:
        return 'MISSING_OR_DIFFERENT_FINITE_CELL'
    if rank_kind != 'actual_padding_floor' or not global_proof:
        return 'MISSING_GEOMETRIC_PREMISE'
    if not all(isinstance(v, int) and 0 <= v <= a for v in (q, r)):
        return 'INCONSISTENT_BOUND'
    return 'POSITIVE_IF_PREMISES_PROVED' if q+r > a else 'INSUFFICIENT_NOT_EXCLUDED'


def gate_controls():
    cell = [23, [61, 15]+[2]*8]
    assert arithmetic_gate(158, 1, 158, cell, cell, cell) == 'POSITIVE_IF_PREMISES_PROVED'
    assert arithmetic_gate(159, 1, 158, cell, cell, cell) == 'INSUFFICIENT_NOT_EXCLUDED'
    assert arithmetic_gate(None, 1, 158, cell, cell, cell) == 'MISSING_OR_DIFFERENT_FINITE_CELL'
    assert arithmetic_gate(158, 1, 158, cell, cell, [35, [105, 19]+[2]*8]) == 'MISSING_OR_DIFFERENT_FINITE_CELL'
    assert arithmetic_gate(158, 1, 158, cell, cell, cell, 'source_ceiling') == 'MISSING_GEOMETRIC_PREMISE'
    assert arithmetic_gate(158, 1, 158, cell, cell, cell, global_proof=False) == 'MISSING_GEOMETRIC_PREMISE'
    return {'status': 'PASS', 'examples_are_synthetic': True,
            'mathematical_premises_are_not_machine_certified_by_this_gate': True}


def receive02():
    """Receive delivered math and distinguish integrator reruns from original bytes."""
    base = ROOT/'Batch16/reviews/02'
    manifest = read(base/'INPUT_DELIVERY_MANIFEST.json')
    acceptance = read(base/'integrator_review.json')
    bindings = []
    refreshable = {'results/b16_02/receiver.json', 'results/logs/b16_02_receiver_resources.json'}
    for artifact in manifest['artifacts']:
        path = base/artifact['path']
        read(path, False)
        actual = READS[str(path.resolve())]
        match = actual['sha256'] == artifact['sha256'] and actual['bytes'] == artifact['bytes']
        binding = {'path': artifact['path'], 'expected_sha256': artifact['sha256'],
                   'actual_sha256': actual['sha256'], 'matches_original_delivery': match}
        if not match:
            assert artifact['path'] in refreshable, 'Unexpected delivered content change'
            original = ROOT/'work/batch15_workers/B15-02'/artifact['path']
            original_data = read(original)
            assert READS[str(original.resolve())]['sha256'] == artifact['sha256']
            fresh = read(path)
            if artifact['path'].endswith('/receiver.json'):
                old_math = {k:v for k,v in original_data.items() if k != 'elapsed_seconds'}
                new_math = {k:v for k,v in fresh.items() if k != 'elapsed_seconds'}
                assert old_math == new_math
            else:
                assert fresh['session_id'] == 'B15-integrator' and fresh['exit_code'] == 0
                assert fresh['job_object_enforced'] and fresh['wall_cap_seconds'] <= 60
                assert fresh['memory_cap_mb'] <= 512 and fresh['workers'] == fresh['blas_threads'] == 1
            binding['classification'] = 'Integrator replay output; original worker bytes separately matched'
        bindings.append(binding)
    census = read(base/'results/b16_02/census.json')
    expected = [(23,15,189,158,-20),(25,17,294,218,-65),
                (26,17,294,218,-65),(27,19,429,288,-130)]
    assert acceptance['counts'] == [c[2] for c in expected]
    checked = []
    for row, (d,t,a,h,upper) in zip(census['rows'], expected):
        n = t+16
        assert row['degree'] == d and row['lambda'] == [4*d-n,t]+[2]*8
        assert row['a'] == a and row['source_ceiling'] == h
        assert row['inherited_full_det_ideal_upper'] == 11
        assert row['D_upper'] == 11+h-a == upper < 0
        assert 2*d-n+2 > t and row['finite_equals_stable']
        corrections = []
        for b in range(n//2+1):
            for m in range(2*b,min(4*b,n)+1):
                L, D = n-m, d-b
                assert D >= 0
                if L>D:
                    assert D+1 >= 2*d-n+2 > t
                    corrections.append([b,m,L,D,D+1,L-D])
        checked.append({'degree':d,'tail':t,'ambient':a,'padding_upper':h,
                        'D_upper':upper,'correction_carriers_b_m_L_D_hookfirst_hookheight':corrections})
    assert len(census['rows']) == len(checked) == 4
    return {'status':'PASS_PROOF_REVIEW_AND_FINITE_EXCLUSION_ARITHMETIC',
            'binding_checks':bindings,'finite_cells':checked,
            'counts_and_geometric_premises':'Inherited from delivered, independently accepted slot02; no census regenerated',
            'fresh':'Reviewed first-row hook argument; enumerated finite correction carriers; checked all four exclusions',
            'degree27':'Full ambient/stable equality plus inherited chart/ideal compatibility transfers i_det11, m_det418, m_pad243..288'}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', default='results/b16_12/receiver.json')
    args = ap.parse_args()
    output = (WORK/args.output).resolve()
    if not output.is_relative_to(OUT.resolve()):
        raise ValueError('Output must remain inside owned results/b16_12')
    start = time.monotonic()
    registry = read(OUT/'input_paths.json')
    for name in registry['paths']:
        read(ROOT/name, False)
    manifest = read(ROOT/'Batch16/launch/INPUT_MANIFEST.json')
    for row in manifest['inputs']:
        read(row['path'], False)
        assert READS[str(Path(row['path']).resolve())]['sha256'] == row['sha256']
    sources = read(WORK/'results/b15_12/source_manifest.json')
    source = next(s for s in sources['sources'] if s['file'] == 'kl_1204.4693v1.pdf')
    pdf = WORK/'results/b15_12/sources'/source['file']
    read(pdf, False)
    assert READS[str(pdf.resolve())]['sha256'] == source['sha256']
    self_hash = read(Path(__file__), False)
    evidence = {'status': 'PASS_PROOF_CONTROLS_AND_INHERITED_ARITHMETIC',
                'controls': controls(), 'arithmetic': inherited_arithmetic(),
                'acceptance_gate': gate_controls(),
                'received_02': receive02(),
                'received_03_through_08': read(OUT/'received.json'),
                'heavy_lease': 'Never acquired; no heavy job launched',
                'wall_seconds': time.monotonic()-start,
                'input_hashes': READS,
                'source_sha256': hashlib.sha256(self_hash).hexdigest()}
    # Detect any source changes during this execution.
    for name, record in READS.items():
        assert hashlib.sha256(Path(name).read_bytes()).hexdigest() == record['sha256'], name
    output.write_text(json.dumps(evidence, indent=2)+'\n')
    print(json.dumps({'status': evidence['status'], 'seconds': evidence['wall_seconds'],
                      'hashed_inputs': len(READS), 'positive_claim': False}))


if __name__ == '__main__':
    main()
