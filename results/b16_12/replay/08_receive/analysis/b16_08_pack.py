"""Read-only input hashing and B16-08 delivery metadata. Use b15_bound.py."""
from pathlib import Path
import hashlib
import json
import os
import sys
import flint

HERE = Path(__file__).resolve().parents[1]
PROJECT = HERE.parents[2]
DELIVERY = HERE/'delivery/b16_08'
assert 'CI73_DEADLINE' in os.environ


def write(name, obj):
    (DELIVERY/name).write_text(json.dumps(obj, indent=2)+'\n', encoding='utf-8')


def entry(p, role):
    data = p.read_bytes()
    return {'path': str(p), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'role': role, 'hash_convention': 'RAW_BYTES'}


inputs = [
    ('Batch16/BOARD.md', 'frozen research scope and inherited stable bounds'),
    ('Batch16/launch/INPUT_MANIFEST.json', 'per-worktree frozen launch heads and primary inputs'),
    ('Batch16/launch/B16-08.md', 'assigned frozen brief'),
    ('Batch16/launch/runtime_08.json', 'inherited launch runtime receipt'),
    ('Batch15_Launch/native_20260913/INTAKE.json', 'inherited evidence intake and attribution'),
    ('Batch15_Launch/native_20260913/reviews_filesystem/Hessian11_1631/REPORT.md',
     'original shared-block formula and proposed instrument; Astra/xhigh attribution'),
    ('Batch15_Launch/native_20260913/reviews_filesystem/Hessian11_1631/MANIFEST.json', 'original source hashes'),
    ('Batch15_Launch/native_20260913/reviews_filesystem/Hessian11_1631/input_receipt.json', 'original input provenance'),
    ('Batch15_Launch/native_20260913/reviews_filesystem/Hessian11_1631/integrator_review.json', 'inherited review boundaries'),
    ('Batch15_Launch/native_20260913/reviews_filesystem/Hessian11_1631/verify_small.py',
     'source inspected, not imported or executed'),
    ('Batch15_Launch/native_20260913/equation_review/astra/REVIEW.md',
     'original four-space review proof and attribution, inspected excerpts'),
    ('Batch15_Launch/native_20260913/equation_review/astra/hessian_relations.py',
     'original review source inspected, not imported or executed'),
    ('work/batch15_workers/B15-05/docs/b15_05_proved.md', 'original worker proof inspected excerpts'),
    ('work/batch15_workers/B15-05/analysis/b15_05_tail21.py', 'original worker orchestration inspected excerpts'),
    ('work/batch15_workers/B15-08/analysis/b15_bound.py', 'full inspected unchanged Job Object wrapper'),
    ('work/batch15_workers/B15-08/.venv/python.exe', 'required worktree interpreter launcher'),
    ('work/batch15_workers/B15-08/.git', 'read-only worktree location control'),
    ('work/batch15_workers/B15-08/results/logs/b16_08_runtime_resources.json', 'pre-existing inherited runtime process check'),
    ('work/batch15_workers/B15-08/results/logs/b15_08_runtime_native_20260913.pid', 'old process identifier inspected only')]

records = [entry(PROJECT/p, role) for p,role in inputs]
frozen = json.loads((PROJECT/'Batch16/launch/INPUT_MANIFEST.json').read_text())
lookup = {str(Path(r['path'])): r['sha256'] for r in records}
checks = []
for item in frozen['inputs']:
    p = str(Path(item['path']))
    if p in lookup:
        checks.append({'path': p, 'expected': item['sha256'], 'actual': lookup[p],
                       'matches': item['sha256'].lower() == lookup[p]})
assert all(c['matches'] for c in checks)
write('INPUT_HASHES.json', {'status': 'EXACT_READ_INPUT_HASHES', 'files': records,
                           'checked_frozen_primary_hashes': checks,
                           'runtime': {'python': sys.version, 'flint': flint.__version__,
                                       'flint_entry_file': str(Path(flint.__file__))}})

names = ['b16_08_preflight', 'b16_08_elimination', 'b16_08_elimination_pivoted', 'b16_08_receiver']
resources = [json.loads((HERE/f'results/logs/{name}_resources.json').read_text()) for name in names]
write('RESOURCE_SUMMARY.json', {
    'slot': 'B16-08', 'heavy_lease_acquired': False, 'heavy_lease_held': False,
    'legacy_wrapper_labels': 'B15/batch15 retained verbatim; these four named receipts are fresh B16-08 runs',
    'runs': [{'name': name, **r} for name,r in zip(names,resources)],
    'mathematical_run_wall_seconds_total': sum(r['wall_seconds'] for r in resources),
    'failed_run_explanation': 'First-m row selection hit a zero linear coefficient; no relation inferred. Pivot rows among the same ten points give every required nonzero minor.',
    'max_peak_working_set_bytes': max(r['process_memory']['peak_working_set'] for r in resources),
    'max_peak_job_memory_bytes': max(r['job_memory']['peak_job_memory'] for r in resources)})

write('CLAIMS.json', {
    'status': 'COMPLETE_BOUNDED_ELIMINATION_CERTIFICATE', 'slot': '08',
    'frozen_head': '0256ed2561964fe4085ad847518e3fcf85837024',
    'frozen_tree': '2b6f72c485c18f4b8e43c17b0223957c1c6e334a',
    'fresh_readonly_git_head_verified': True, 'common_merged_base_claimed': False,
    'staged_or_committed': False,
    'exact_claim': 'For phi(y_alpha)=[x^alpha]det(diag(0,I3)+sum_(i=1)^3 xi Bi), ker(phi) has zero intersection with ordinary y-degree at most two.',
    'hypotheses': ['Characteristic-zero field', 'Three arbitrary 4x4 direction matrices',
                   'Rank-three normalized base matrix diag(0,I3)', 'Ordinary polynomial coefficients, no factorial rescaling'],
    'fresh_evidence': ['Universal 16-entry block identity, all 49 terms and zero residual',
                       '165 nonzero modular evaluation minors on exactly 630 graded columns',
                       'Ten saved integer points and all coefficient values',
                       'Direct determinant-expansion receiver and two mutation controls'],
    'inherited': ['B15 shared-block formulas and earlier Hessian constructions, attributed in proof',
                  'B16 frozen stable429/418/243..288 facts, not used in fresh proof', 'Original unchanged B15 Job Object wrapper'],
    'limitations': ['No all-degree elimination ideal result', 'No 16-variable coefficient equation',
                    'No new highest weight or finite q/r certificate', 'No padding computation', 'No multiplicity gap'],
    'next_sufficient_witness': 'A nonzero exact eliminant of degree at least three with full substitution-zero witness, followed by basepoint/chart removal, arbitrary 16-matrix substitution proof, and one finite-cell q+r>a certificate.',
    'heavy_lease_status': 'NOT_ACQUIRED_NONE_HELD',
    'receiver': 'delivery/b16_08/RECEIVE.ps1'})

artifacts = [
    'analysis/b16_08_jets.py', 'analysis/b16_08_pack.py',
    'docs/b16_08_proof.md', 'docs/b16_08_report.md',
    'results/b16_08/preflight.json', 'results/b16_08/certificate.json',
    'delivery/b16_08/RECEIVE.ps1', 'delivery/b16_08/README.md',
    'delivery/b16_08/INPUT_HASHES.json', 'delivery/b16_08/RESOURCE_SUMMARY.json', 'delivery/b16_08/CLAIMS.json']
write('ARTIFACT_HASHES.json', {'files': [entry(HERE/p, 'fresh B16-08 immutable delivery evidence') for p in artifacts],
                              'excluded_mutable_outputs': ['results/b16_08/receiver.json', 'results/logs/b16_08*',
                                                           'delivery/b16_08/PROCESS_EXIT.json']})
print(json.dumps({'status': 'PACKAGED', 'input_hashes': len(records), 'artifact_hashes': len(artifacts),
                  'frozen_input_matches': len(checks)}))
