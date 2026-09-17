"""Seal MANIFEST.json: hash every input relied on and every output; re-verify the parent packet; record runs."""
import hashlib, json, os, time
from pathlib import Path
HERE = Path(__file__).resolve().parent; ROOT = HERE.parents[2]; PARENT = HERE.parent / 'routeA_signfilter_20260917'
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
pm = json.loads((PARENT / 'MANIFEST.json').read_text())
parent_mism = [p for p, h in pm['outputs_sha256'].items() if sha(PARENT / p) != h]
parent_files = {}
for root, dirs, files in os.walk(PARENT):
    for f in files:
        rel = os.path.relpath(os.path.join(root, f), PARENT).replace(os.sep, '/'); parent_files[rel] = sha(os.path.join(root, f))
unlisted = [r for r in parent_files if r != 'MANIFEST.json' and r not in pm['outputs_sha256']]
inherited_mism = [p for p, h in pm['inherited_sealed_inputs_sha256'].items() if sha(ROOT / p) != h]
inputs = ['work/batch15_workers/B15-01/docs/b19_01_report.md', 'work/batch15_workers/B15-02/docs/b18_02_report.md',
          'work/claude_transverse_structure_20260916_followup/clarification_20260917/SOURCE_HANDOFF.md',
          'work/claude_transverse_structure_20260916_followup/clarification_20260917/STABILIZER.md',
          'work/claude_transverse_structure_20260916_followup/clarification_20260917/CORRIGENDUM.md',
          'work/batch15_workers/B15-02/analysis/b15_bound.py', 'work/batch15_workers/B15-02/.venv/python.exe']
inputs_sha = {p: sha(ROOT / p) for p in inputs}
inputs_sha.update({'work/claude_source_vectors_20260917/routeA_signfilter_20260917/' + k: v for k, v in parent_files.items()})
outputs = {}
for p in sorted(HERE.rglob('*')):
    if p.is_file() and p.name != 'MANIFEST.json' and '__pycache__' not in str(p):
        outputs[str(p.relative_to(HERE)).replace(os.sep, '/')] = sha(p)
runs = []
for name in ('p1_b_L_branching', 'p2_b_L_branching'):
    m = json.loads((HERE / 'results/logs' / (name + '_resources.json')).read_text())
    killed = 'exit_code' not in m   # the wrapper exits via os._exit(124) at the deadline; the receipt then lacks exit/wall fields
    runs.append(dict(name=name, wrapped=True, receipt='results/logs/%s_resources.json' % name, exit_code=(124 if killed else m['exit_code']), wall_seconds=(60.0 if killed else m['wall_seconds']),
                     killed_at_wall_cap=killed, console='results/logs/%s_console.txt' % name, peak_job_memory=(m.get('job_memory') or {}).get('peak_job_memory'), memory_cap_mb=m['memory_cap_mb'], wall_cap_seconds=m['wall_cap_seconds'], workers=m['workers'], blas_threads=m['blas_threads']))
runs.append(dict(name='unwrapped_micro_test_small_controls', wrapped=False, wall_seconds=0.14, note='exec of the module head (small control functions only), disclosed in REPORT.md section 5.3'))
man = dict(session='claude_source_vectors_20260917/arc_target_dimension_followup', created_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
           outcome='Case C: b_L = 74 (70 from skew degree 11, 4 from skew degree 12), proved by two independent formulations; no upper bound below 4; transverse independence from the arc not proved; refined target F'' defined and proved to contain C(M), dimension not computed',
           parent_packet=dict(path='work/claude_source_vectors_20260917/routeA_signfilter_20260917', outputs_listed=len(pm['outputs_sha256']), output_mismatches=parent_mism, unlisted_files=unlisted, inherited_inputs=len(pm['inherited_sealed_inputs_sha256']), inherited_mismatches=inherited_mism, unchanged=(not parent_mism and not unlisted and not inherited_mism)),
           inputs_sha256=inputs_sha, outputs_sha256=outputs, runs=runs,
           numerical_wall_seconds_total=sum(r.get('wall_seconds') or 0 for r in runs), wrapped_pilots_used=2, wrapped_pilots_cap=3,
           source_vectors_evaluated=0, historical_files_modified=[], receipts_overwritten=[],
           note='REPORT.md, CORRIGENDUM.md, code, results and tables finalised before hashing.')
(HERE / 'MANIFEST.json').write_text(json.dumps(man, indent=1) + '\n')
print('parent unchanged:', man['parent_packet']['unchanged'], '| inputs hashed:', len(inputs_sha), '| outputs:', len(outputs), '| wall total:', round(man['numerical_wall_seconds_total'], 2))
