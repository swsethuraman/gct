"""One bounded source-binding/arithmetic audit; never imports research producers.

Run only with the existing interpreter, -B and the inspected b15_bound wrapper.
This verifies saved numbers and provenance, not historical character/geometry proofs.
"""
import hashlib
import json
import os
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'results/b17_12'
started = time.perf_counter()
checks = []
bindings = []


def check(label, truth, detail=None):
    checks.append({'check': label, 'pass': bool(truth), 'detail': detail})


def digest(path):
    value = hashlib.sha256()
    with path.open('rb') as handle:
        for block in iter(lambda: handle.read(65536), b''):
            value.update(block)
    return value.hexdigest()


def read(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))


def write(name, value):
    (OUT / name).write_text(json.dumps(value, indent=2) + '\n', encoding='utf-8')


inventory = read(OUT / 'input_inventory.json')
records = {row['path'].replace('\\', '/'): row for row in inventory['files']}
project = inventory['project_root'].replace('\\', '/').rstrip('/')
check('existing interpreter', Path(sys.executable).resolve() == (ROOT / '.venv/python.exe').resolve())
check('bytecode disabled', sys.dont_write_bytecode)
check('BLAS configuration', all(os.environ.get(k) == '1' for k in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS')))
check('wrapper deadline present', 'CI73_DEADLINE' in os.environ)
check('bounded input inventory', len(records) <= 300 and sum(r.get('bytes', 0) for r in records.values()) <= 16 * 1024**2)
if not all(c['pass'] for c in checks):
    write('verification.json', {'status': 'FAILED_PREFLIGHT', 'checks': checks})
    raise SystemExit(1)

for key, row in records.items():
    check('input present: ' + key, row['status'] == 'PINNED')
    if row['status'] != 'PINNED':
        continue
    path = ROOT / row['snapshot']
    actual = digest(path)
    check('snapshot SHA256: ' + key, actual == row['sha256'])
    check('snapshot length: ' + key, path.stat().st_size == row['bytes'])
    if row.get('expected_sha256'):
        check('declared source hash: ' + key, actual == row['expected_sha256'])


def snap(key):
    return ROOT / records[key]['snapshot']


def src(key):
    return read(snap(key))


def bind(key, expected, authority):
    if key in records:
        matches = records[key]['sha256'] == expected
        bindings.append({'input': key, 'authority': authority, 'expected_sha256': expected, 'matches': matches})
        check('binding: ' + authority + ' -> ' + key, matches)
        return True
    return False


launch = src('Batch17/launch/INPUT_MANIFEST.json')
for entry in launch['inputs']:
    key = entry['path'].replace('\\', '/')[len(project) + 1:]
    bind(key, entry['sha256'], 'Batch17/launch/INPUT_MANIFEST.json')
for task in launch['tasks']:
    bind('Batch17/launch/B17-' + task['slot'] + '.md', task['sha256'], 'Batch17/launch/INPUT_MANIFEST.json')

screen_manifest = src('Batch17_Planning/SCREEN_MANIFEST.json')
for entry in screen_manifest['artifacts']:
    bind('Batch17_Planning/' + entry['path'], entry['sha256'], 'Batch17_Planning/SCREEN_MANIFEST.json')
for entry in screen_manifest['inherited_sources']:
    bind(entry['path'], entry['sha256'], 'Batch17_Planning/SCREEN_MANIFEST.json')

manifest_names = {'08': 'ARTIFACT_HASHES.json', '09': 'delivery_manifest.json', '10': 'SHA256_MANIFEST.json', '11': 'DELIVERY_MANIFEST.json'}
intake = src('Batch16/INTAKE.json')
inherited = []
for entry in intake['entries']:
    slot = entry['slot']
    prefix = 'work/batch15_workers/B15-' + slot
    manifest_key = prefix + '/delivery/b16_' + slot + '/' + manifest_names.get(slot, 'MANIFEST.json')
    manifest = src(manifest_key)
    entries = manifest.get('files', []) + manifest.get('artifacts', []) + manifest.get('outputs', [])
    bound = []
    for item in entries:
        if not item.get('path') or not item.get('sha256'):
            continue
        key = item['path'].replace('\\', '/')
        if key.lower().startswith(project.lower() + '/'):
            candidates = [key[len(project) + 1:]]
        else:
            key = key.removeprefix('./')
            candidates = [prefix + '/' + key, prefix + '/delivery/b16_' + slot + '/' + key]
        for candidate in candidates:
            if bind(candidate, item['sha256'], manifest_key):
                bound.append(candidate)
    receipt_key = 'Batch16/reviews/' + slot + '/integrator_review.json'
    receipt = src(receipt_key)
    check('intake/receipt status slot ' + slot, receipt['status'] == entry['status'])
    check('original selected evidence bound slot ' + slot, len(bound) > 0)
    inherited.append({'slot': slot, 'status_in_this_ledger': 'INHERITED_ACCEPTED_SCOPED', 'intake_status': entry['status'], 'claim': entry.get('claim', entry.get('consequence')), 'acceptance_receipt': receipt_key, 'acceptance_receipt_sha256': records[receipt_key]['sha256'], 'original_report': prefix + '/docs/b16_' + slot + '_report.md', 'original_manifest': manifest_key, 'original_manifest_sha256': records[manifest_key]['sha256'], 'selected_bound_artifacts': sorted(set(bound)), 'original_acceptance_record': entry, 'new_mathematical_review_or_replay_by_b17_12': False})

sealed = src('Batch16/reviews/12_final/ORIGINAL_DELIVERY_MANIFEST.json')
for entry in sealed['files']:
    if entry['path'].startswith('docs/'):
        key = 'Batch16/reviews/12_final/' + entry['path']
        bind(key, entry['sha256'], 'Batch16/reviews/12_final/ORIGINAL_DELIVERY_MANIFEST.json')
        original = 'work/batch15_workers/B15-12/' + entry['path']
        bind(original, entry['sha256'], 'Batch16/reviews/12_final/ORIGINAL_DELIVERY_MANIFEST.json')

declared_data = [(23,15,189,1,158),(25,17,294,4,218),(26,17,294,4,218),(27,19,429,11,288)]
cells = []
for d, t, a, ideal, ceiling in declared_data:
    cells.append({'d': d, 't': t, 'weight': [4*d-t-16, t] + [2]*8, 'a': a, 'exact_i_det': ideal, 'm_det': a-ideal, 'padding_ceiling_U': ceiling, 'D_upper': ideal+ceiling-a, 'minimum_positive_padding_rank': a-ideal+1, 'status': 'INHERITED_CLOSED_CELL', 'sources': ['B16-01', 'B16-02', 'B16-04', 'Batch16/STOCKTAKE.md']})
m04 = src('work/batch15_workers/B15-04/delivery/b16_04/MANIFEST.json')
check('declared exact ideals match original manifest', [c['exact_i_det'] for c in cells] == m04['declared_ideal_dimensions'])
check('declared gap bounds match original manifest', [c['D_upper'] for c in cells] == m04['declared_gap_upper'])
check('declared ambient matches accepted02', [c['a'] for c in cells] == next(e for e in intake['entries'] if e['slot'] == '02')['counts'])

finite = src('Batch17_Planning/finite_screen.json')
check('finite screen complete', finite['status'] == 'COMPLETE' and len(finite['rows']) == 6)
for row in finite['rows']:
    d, t, a, ideal, ceiling = (row[k] for k in ('d','t','a','exact_i_det','padding_ceiling'))
    check('finite correction ' + str((d,t)), row['stable_a'] + row['correction'] == a)
    check('finite determinant arithmetic ' + str((d,t)), a-ideal == row['determinant_multiplicity'])
    check('finite gap arithmetic ' + str((d,t)), ideal+ceiling-a == row['D_upper'] <= 0)
    cells.append({'d': d, 't': t, 'weight': row['weight'], 'a': a, 'exact_i_det': ideal, 'm_det': a-ideal, 'padding_ceiling_U': ceiling, 'D_upper': ideal+ceiling-a, 'minimum_positive_padding_rank': a-ideal+1, 'status': 'INHERITED_CLOSED_CELL', 'sources': ['Batch17_Planning/finite_screen.json', 'B16-04']})
for row in cells:
    check('same finite cell ' + str((row['d'],row['t'])), sum(row['weight']) == 4*row['d'] and row['weight'] == sorted(row['weight'], reverse=True))
    check('excluded witness exceeds ceiling ' + str((row['d'],row['t'])), row['minimum_positive_padding_rank'] > row['padding_ceiling_U'])

degree7 = src('Batch17_Planning/degree7_screen.json')
check('degree7 saved scope', degree7['considered'] == 114 and degree7['eligible'] == len(degree7['rows']) == 31)
for row in degree7['rows']:
    check('degree7 saved row ' + str(row['weight']), sum(row['weight']) == 28 and row['a'] >= 2 and row['g'] + row['t'] == 2*row['s'] and row['B'] == min(row['a'], row['s']) and row['headroom'] == row['U']-row['B'] and row['required_minor'] == row['B']+1 and not (1 <= row['B'] < row['U']))
verification = src('Batch17_Planning/verification.json')
check('historical independent-route receipt', verification['status'] == 'PASS' and verification['finite_correction_terms'] == 57 and verification['degree7_rows'] == 31)
leases = src('Batch17/LEASES.json')
check('launch leases are empty', leases['active'] == [] and leases['eligible'] == ['01','02'] and leases['max_heavy'] == 2)
check('stable interval arithmetic', (243-418, 288-418) == (-175,-130))
template = read(OUT / 'review_template.json')
check('new claim template unaccepted', template['status'] == 'NOT_RECEIVED' and template['review']['acceptance_receipt'] is None and template['bounds']['actual_padding_coordinate_lower_r'] is None)

dispatch = src('Batch17/DISPATCHED.json')
coordination = src('Batch17/COORDINATION.json')
pending = [{'slot': task['slot'], 'assignment': task['title'], 'launch_status': task['status'], 'mathematical_result_status': 'NOT_RECEIVED_OR_REVIEWED_BY_B17_12', 'required_release': coordination.get('held', {}).get(task['slot']), 'heavy_lease_issued': False} for task in launch['tasks'] if task['slot'] != '12']
ledger = {'schema': 'b17_12_source_ledger_v1', 'scope': 'INITIAL_LAUNCH_SOURCE_LEDGER', 'final_closeout': 'PENDING_LATER_CONTINUATION', 'new_b17_mathematical_acceptances': [], 'provenance_limit': 'Selected input bindings and inherited scoped acceptance; no recursive historical replay.', 'launch_snapshot': dispatch, 'coordination_snapshot': coordination, 'leases_snapshot': leases, 'inherited_b16': inherited, 'finite_cells': cells, 'degree7': {'status': 'CERTIFICATE_METHOD_RETIRED_NOT_CELL_EXCLUSION', 'scope': degree7['scope'], 'considered': 114, 'eligible': 31, 'boundary_losses_excluded': False}, 'pending_b17': pending, 'next_sufficient_test': 'In one new reviewed finite cell, U>B then exact actual-padding (B+1)-minor, after integrator resource release.', 'next_input': 'Later continuation with original reviewed Stage A claims, B17-08 family proposal, B17-11 acceptance and applicable B17-09 certificate.', 'bound_directions': {'positive': 'r>B, or q+r>a with q<=i_det', 'negative': 'Q+U<=a with i_det<=Q, or U<=L with L<=m_det', 'failed_method_only': 'q+U<=a with q merely a floor; U<=B with B merely an upper'}, 'superseded': [{'source': 'COMMON_CONTEXT.md', 'statement': 'six counts not yet computed', 'by': 'SCREEN_REPORT.md and finite_screen.json'}, {'source': 'SCREEN_REPORT.md', 'statement': 'batch not launched', 'by': 'pinned Batch17 dispatch (operational only)'}, {'source': 'early B16-02/03/10 bounds', 'statement': '-20,-65,-65,-130', 'by': 'accepted B16-04 exact ideals: -30,-72,-72,-130'}], 'binding_checks': bindings}
write('source_ledger.json', ledger)
failures = [c for c in checks if not c['pass']]
receipt = {'schema': 'b17_12_verification_v1', 'status': 'PASS' if not failures else 'FAIL', 'computation_index': 1, 'scope': 'Snapshot and selected-original hash binding plus saved scalar arithmetic; no historical mathematical recomputation.', 'input_count': len(records), 'input_bytes': sum(r.get('bytes',0) for r in records.values()), 'original_manifest_bindings': len(bindings), 'checks_count': len(checks), 'failures': failures, 'checks': checks, 'wall_seconds_internal': time.perf_counter()-started, 'interpreter': sys.executable, 'interpreter_sha256': digest(Path(sys.executable)), 'script_sha256': digest(Path(__file__)), 'wrapper_sha256': digest(ROOT / 'analysis/b15_bound.py'), 'new_b17_claims_accepted': 0, 'mathematical_producers_executed': 0}
write('verification.json', receipt)
print(json.dumps({k: receipt[k] for k in ('status','input_count','input_bytes','original_manifest_bindings','checks_count','failures','wall_seconds_internal')}))
raise SystemExit(0 if not failures else 1)
