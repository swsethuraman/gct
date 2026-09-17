"""Seal MANIFEST.json for this session: hash every input actually relied on (read-only) and every
output delivered; confirm the inherited sealed inputs are byte-identical to the clarification's
MANIFEST.json. Run last, after REPORT.md and all outputs are final. MANIFEST.json itself is excluded."""
import hashlib, json, os, time
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CLAR = ROOT / 'work/claude_transverse_structure_20260916_followup/clarification_20260917'
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
clar = json.loads((CLAR / 'MANIFEST.json').read_text())
inherited = {}
mism = []
for sec in ('read_only_inputs_sha256', 'preserved_packets_sha256'):
    for rel, h in clar[sec].items():
        hh = sha(ROOT / rel); inherited[rel] = hh
        if hh != h: mism.append(rel)
clar_outputs = {}
for rel, h in clar['outputs_sha256'].items():
    hh = sha(CLAR / rel); clar_outputs['work/claude_transverse_structure_20260916_followup/clarification_20260917/' + rel] = hh
    if hh != h: mism.append(rel)
extra_inputs = ['work/batch15_workers/B15-02/.venv/python.exe']
extra = {rel: sha(ROOT / rel) for rel in extra_inputs}
outputs = {}
for p in sorted(HERE.rglob('*')):
    if p.is_file() and p.name != 'MANIFEST.json':
        outputs[str(p.relative_to(HERE)).replace(os.sep, '/')] = sha(p)
receipts = []
for name in ('s1_screen_arc', 's2_certify_n02_and_new', 's3_full_forbidden_rows'):
    m = json.loads((HERE / 'results/logs' / (name + '_resources.json')).read_text())
    receipts.append(dict(name=name, wrapped=True, receipt='results/logs/%s_resources.json' % name, exit_code=m['exit_code'], wall_seconds=m['wall_seconds'], peak_job_memory=m['job_memory']['peak_job_memory'], memory_cap_mb=m['memory_cap_mb'], wall_cap_seconds=m['wall_cap_seconds'], workers=m['workers'], blas_threads=m['blas_threads']))
man = dict(session='claude_source_vectors_20260917/routeA_signfilter_20260917', created_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
           outcome='C (source progress only): fourth independent source direction n02 certified; transverse triple rank 3 on M proved; arc rank on all tested forbidden rows stays 2; sampled kernel candidate not promoted; b_L uncomputed',
           inherited_sealed_inputs_sha256=inherited, clarification_outputs_sha256=clar_outputs, inherited_inputs_byte_identical=(not mism), mismatches=mism,
           other_inputs_sha256=extra, outputs_sha256=outputs, wrapped_runs=receipts,
           numerical_wall_seconds_total=sum(r['wall_seconds'] for r in receipts), new_contraction_candidates_evaluated=12, evaluations_total=194,
           historical_files_modified=[], receipts_overwritten=[], note='REPORT.md and all certificate/result files finalised before hashing; verify_certificates.py passed 42/42.')
(HERE / 'MANIFEST.json').write_text(json.dumps(man, indent=1) + '\n')
print('inherited inputs checked:', len(inherited) + len(clar_outputs), 'mismatches:', mism)
print('outputs hashed:', len(outputs), 'numerical wall total:', round(man['numerical_wall_seconds_total'], 2))
