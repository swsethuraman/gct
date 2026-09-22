"""Administrative A25-10 seal only: owned text, read-only Git, hashes; no mathematics."""
import datetime
import hashlib
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path('C:/Users/swami/Projects/gct-gpt/work/batch15')
OUT = ROOT / 'results/a25_10'
HEAD = 'eb53b97cf0904e2d54fdb7d101d83b024822811b'
NAMES = [
    'INTAKE.md', 'REVIEW_PLAN.md', 'CLAIM_LEDGER.md', 'REVIEW.md',
    'RELEASE_DECISIONS.md', 'NEXT_ACTION.md', 'RESOURCE_RECEIPTS.md',
    'LIMITATIONS.md', 'SOURCE_READS.md', 'DELIVERY_NOTE.md',
    'INPUT_BINDINGS.json', 'audit_inputs.py', 'seal_packet.py',
    'PROPOSED_ADD_LIST.txt', 'ADMIN_VERIFICATION.json',
]
PAYLOAD = ['docs/a25_10_report.md'] + ['results/a25_10/' + n for n in NAMES]
MANIFEST = 'results/a25_10/MANIFEST.json'
RECEIPT = 'results/a25_10/SEAL_RECEIPT.json'
PROPOSED = PAYLOAD + [MANIFEST, RECEIPT]
WARNINGS = []

def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat().replace('+00:00', 'Z')

def sha(data):
    return hashlib.sha256(data).hexdigest()

def write_json(path, value):
    (ROOT / path).write_bytes((json.dumps(value, indent=2, ensure_ascii=False) + '\n').encode('utf-8'))

def git(*args, input_bytes=None, allowed=(0,)):
    r = subprocess.run(['git', *args], cwd=ROOT, input=input_bytes, capture_output=True)
    if r.stderr:
        WARNINGS.append(r.stderr.decode('utf-8', 'replace').strip())
    if r.returncode not in allowed:
        raise RuntimeError((args, r.returncode, r.stderr.decode('utf-8', 'replace')))
    return r.stdout.decode('utf-8').strip()

def binding(path):
    data = (ROOT / path).read_bytes()
    return {'path': path, 'bytes': len(data), 'sha256': sha(data)}

def filter_check(path):
    data = (ROOT / path).read_bytes()
    raw = hashlib.sha1(b'blob ' + str(len(data)).encode('ascii') + b'\0' + data).hexdigest()
    filtered = git('hash-object', '--path=' + path, path)  # deliberately no -w
    if raw != filtered:
        raise RuntimeError('Prospective Git filter changes bytes: ' + path)
    return {'path': path, 'raw_blob': raw, 'filtered_blob': filtered, 'equal': True}

assert pathlib.Path.cwd().resolve() == ROOT.resolve(), 'Wrong workdir'
assert git('rev-parse', 'HEAD') == HEAD, 'Unexpected HEAD'
assert git('branch', '--show-current') == 'batch15-launch', 'Unexpected branch'
assert not git('diff', '--name-only'), 'Unexpected tracked working changes'
assert not git('diff', '--cached', '--name-only'), 'Unexpected staged changes'

# Explicit allowlist; exclude literature input cache and unrelated integrator outputs.
(OUT / 'PROPOSED_ADD_LIST.txt').write_bytes(('\n'.join(PROPOSED) + '\n').encode('utf-8'))
for path in PAYLOAD:
    if path.endswith('/ADMIN_VERIFICATION.json'):
        continue
    p = ROOT / path
    assert p.resolve().is_relative_to(ROOT.resolve())
    data = p.read_bytes().decode('utf-8-sig').replace('\r\n', '\n')
    p.write_bytes(data.encode('utf-8'))

inputs = json.loads((OUT / 'INPUT_BINDINGS.json').read_text(encoding='utf-8'))
assert not inputs['failures']
assert sum(p['manifest_entries'] for p in inputs['packets']) == 89
direct_pins = {p['commit'] for p in inputs['packets']}
direct = [r for r in inputs['bindings'] if r['commit'] in direct_pins]
assert len(direct) == 95
assert all(r.get('working_bytes_equal') is True for r in direct)
assert all(p['starting_head_is_ancestor'] for p in inputs['packets'])

checks = [filter_check(p) for p in PAYLOAD if not p.endswith('/ADMIN_VERIFICATION.json')]
attributes = git('check-attr', 'text', 'eol', 'filter', '--', *PROPOSED)
ignored = git('check-ignore', '--stdin', input_bytes=('\n'.join(PROPOSED)+'\n').encode(), allowed=(0, 1))
assert not ignored, 'Proposed file ignored: ' + ignored
admin = {
    'utc': utc(), 'method': 'Administrative only; no staging, object writes or mathematics',
    'repository': str(ROOT), 'branch': 'batch15-launch', 'head': HEAD,
    'python_executable': sys.executable, 'python_version': sys.version,
    'status_before_seal': git('status', '--short'),
    'tracked_working_changes': [], 'staged_changes': [],
    'core_autocrlf': git('config', '--get', 'core.autocrlf', allowed=(0, 1)),
    'core_safecrlf': git('config', '--get', 'core.safecrlf', allowed=(0, 1)),
    'proposed_attributes': attributes, 'ignored_proposed_paths': [],
    'raw_vs_filtered_checks_excluding_this_file': checks,
    'direct_manifest_and_payload_observations': len(direct),
    'direct_working_bytes_equal_committed': True,
    'input_binding_observations': len(inputs['bindings']),
    'input_declared_hash_size_failures': [],
    'warnings': sorted(set(WARNINGS)),
}
write_json('results/a25_10/ADMIN_VERIFICATION.json', admin)
filter_check('results/a25_10/ADMIN_VERIFICATION.json')

manifest = {
    'schema': 'a25-10-review-seal-v1', 'slot': 'A25-10', 'sealed_utc': utc(),
    'status': 'UNCOMMITTED / NOT RELEASED', 'delivery_commit': None,
    'repository': str(ROOT), 'branch': 'batch15-launch', 'research_head': HEAD,
    'outcome': 'no construction ready',
    'packet_verdicts': {'A25-01':'REPAIR','A25-02':'PROCEED','A25-03':'PROCEED',
                       'A25-04':'PROCEED','A25-05':'STOP at construction gate','B25-04':'REPAIR'},
    'method': 'READ plus explicitly labelled independent hand derivations; no computational REPLAY',
    'intake_utc': '2026-09-22T14:34:06Z',
    'substantive_assessment_start_utc': '2026-09-22T14:42:53Z',
    'initial_assessment_completed_utc': '2026-09-22T14:49:45Z',
    'mathematical_pilots': 0, 'mathematical_computational_seconds': 0,
    'mathematical_environment': 'Not used; administrative Python/Git environment in ADMIN_VERIFICATION.json',
    'compute_lease_acquired': False, 'tool_memory_created': False,
    'additional_agents_or_tasks': 0,
    'source_bindings': inputs['packets'],
    'source_binding_detail': 'results/a25_10/INPUT_BINDINGS.json',
    'source_read_levels': 'results/a25_10/SOURCE_READS.md',
    'primary_source_inputs': inputs['primary_source_files'],
    'administrative_inputs': inputs['administrative_inputs'],
    'claim_status_detail': 'results/a25_10/CLAIM_LEDGER.md',
    'files': [binding(p) for p in PAYLOAD],
    'manifest_self_hashed': False,
    'external_manifest_digest_receipt': RECEIPT,
    'exclusions': [
        'MANIFEST.json itself (no self-hash)',
        'SEAL_RECEIPT.json (post-seal external receipt; no circular hash graph)',
        'literature/*.pdf (downloaded third-party input cache; not proposed for Git)',
        'producer packets, papers, shared ledgers and pre-existing results/b15_integrator/',
    ],
    'proposed_add_list': 'results/a25_10/PROPOSED_ADD_LIST.txt',
    'gates_open': ['G29 for this review: separate authorized delivery and committed-byte verification'],
}
write_json(MANIFEST, manifest)
verified = []
for item in json.loads((ROOT / MANIFEST).read_text(encoding='utf-8'))['files']:
    assert binding(item['path']) == item
    verified.append(item['path'])
final_checks = [filter_check(p) for p in PAYLOAD + [MANIFEST]]
receipt = {
    'utc': utc(), 'status': 'LOCAL SEALED / UNCOMMITTED / NOT RELEASED',
    'manifest': binding(MANIFEST), 'verified_payload_count': len(verified),
    'payload_hash_failures': [], 'head_after_seal': git('rev-parse', 'HEAD'),
    'branch_after_seal': git('branch', '--show-current'),
    'tracked_working_changes': git('diff', '--name-only'),
    'staged_changes': git('diff', '--cached', '--name-only'),
    'raw_vs_filtered_checks': final_checks,
    'receipt_self_hash': None,
    'receipt_filter_check': 'Performed by sealing process after this final write; raw UTF-8/LF bytes',
    'warnings': sorted(set(WARNINGS)),
}
write_json(RECEIPT, receipt)
filter_check(RECEIPT)
assert receipt['head_after_seal'] == HEAD
assert not receipt['tracked_working_changes'] and not receipt['staged_changes']
print(json.dumps({'manifest': binding(MANIFEST), 'payload_count': len(verified),
                  'proposed_add_count': len(PROPOSED), 'all_filters_preserve_bytes': True,
                  'git_unchanged': True, 'pilots': 0, 'mathematical_seconds': 0,
                  'sealed_utc': manifest['sealed_utc']}, indent=2))
