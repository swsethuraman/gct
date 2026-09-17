"""Seal MANIFEST.json: hash inputs relied on and outputs delivered; confirm every inherited sealed packet unchanged."""
import hashlib, json, os, time
from pathlib import Path
HERE = Path(__file__).resolve().parent; ROOT = HERE.parents[2]; PAR = HERE.parent
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def packet(D, key='outputs_sha256'):
    pm = json.loads((D / 'MANIFEST.json').read_text()); listed = pm.get(key, {})
    files = {}
    for root, dirs, fs in os.walk(D):
        for f in fs:
            rel = os.path.relpath(os.path.join(root, f), D).replace(os.sep, '/')
            if '__pycache__' in rel: continue
            files[rel] = sha(os.path.join(root, f))
    mism = [p for p, h in listed.items() if files.get(p) != h]
    unl = [r for r in files if r != 'MANIFEST.json' and r not in listed]
    return dict(listed=len(listed), mismatches=mism, unlisted=unl, unchanged=(not mism and not unl), files_sha256=files)
parents = {n: packet(PAR / n) for n in ('routeA_signfilter_20260917', 'arc_target_dimension_followup', 'direct_arc_relation_followup')}
astraD = ROOT / 'work/astra_gkz_degenerations_20260917'; am = json.loads((astraD / 'MANIFEST.json').read_text())
astra_files = {}
for root, dirs, fs in os.walk(astraD):
    for f in fs:
        rel = os.path.relpath(os.path.join(root, f), astraD).replace(os.sep, '/'); astra_files[rel] = sha(os.path.join(root, f))
astra_hash_sections = {k: v for k, v in am.items() if isinstance(v, dict) and v and all(isinstance(x, str) and len(x) == 64 for x in v.values())}
astra_mism = [p for sec in astra_hash_sections.values() for p, h in sec.items() if (astra_files.get(p) or (sha(ROOT / p) if (ROOT / p).exists() else None)) != h]
rm = json.loads((PAR / 'routeA_signfilter_20260917/MANIFEST.json').read_text())
inh = [p for p, h in rm['inherited_sealed_inputs_sha256'].items() if sha(ROOT / p) != h]
inputs = {p: sha(ROOT / p) for p in ['work/descent_followup_claude_20260916/pilots/p6_basis.json', 'work/descent_followup_claude_20260916/pilots/paired_runner.py',
          'work/batch15_workers/B15-02/analysis/b18_02_carrier.py', 'work/batch15_workers/B15-02/analysis/b15_bound.py', 'work/batch15_workers/B15-02/.venv/python.exe',
          'work/claude_transverse_structure_20260916_followup/clarification_20260917/SOURCE_HANDOFF.md', 'work/astra_gkz_degenerations_20260917/REPORT.md', 'work/astra_gkz_degenerations_20260917/MANIFEST.json']}
outputs = {}
for p in sorted(HERE.rglob('*')):
    if p.is_file() and p.name != 'MANIFEST.json' and '__pycache__' not in str(p):
        outputs[str(p.relative_to(HERE)).replace(os.sep, '/')] = sha(p)
m = json.loads((HERE / 'results/logs/f1_new_point_minor_resources.json').read_text()); killed = 'exit_code' not in m
run = dict(name='f1_new_point_minor', wrapped=True, receipt='results/logs/f1_new_point_minor_resources.json', exit_code=(124 if killed else m['exit_code']), wall_seconds=(60.0 if killed else m['wall_seconds']), killed_at_wall_cap=killed, peak_job_memory=(m.get('job_memory') or {}).get('peak_job_memory'), memory_cap_mb=m['memory_cap_mb'], wall_cap_seconds=m['wall_cap_seconds'], workers=m['workers'], blas_threads=m['blas_threads'], evaluations=68)
man = dict(session='claude_source_vectors_20260917/final_arc_diagnostic', created_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
           outcome='B: no nonzero 3x3 full-forbidden minor on (q3,q7,n02); four new rows at P6 points 2,3 satisfy the recorded relation; combined 14-row rank 2; rank(C|U) in {2,3} unresolved; diagnostic paused',
           parent_packets={k: {kk: vv for kk, vv in v.items() if kk != 'files_sha256'} for k, v in parents.items()}, parent_files_sha256={k: v['files_sha256'] for k, v in parents.items()},
           astra_packet=dict(files=len(astra_files), hash_sections=list(astra_hash_sections), mismatches=astra_mism, files_sha256=astra_files),
           inherited_sealed_inputs_mismatches=inh, inputs_sha256=inputs, outputs_sha256=outputs, runs=[run],
           numerical_wall_seconds_total=run['wall_seconds'], wrapped_pilots_used=1, wrapped_pilots_cap=1, unwrapped_computations=0, source_vectors_searched=0,
           historical_files_modified=[], receipts_overwritten=[], shared_memory_or_ledgers_modified=False,
           note='REPORT.md, CURRENT_DIAGNOSTIC_STATE.md, code, results, verify_minors.py finalised before hashing.')
(HERE / 'MANIFEST.json').write_text(json.dumps(man, indent=1) + '\n')
print('parents unchanged:', {k: v['unchanged'] for k, v in parents.items()}, '| astra mismatches:', astra_mism, '| inherited mismatches:', inh, '| outputs:', len(outputs), '| wall:', round(run['wall_seconds'], 2))
