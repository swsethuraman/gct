"""Seal MANIFEST.json: hash inputs relied on and outputs delivered; confirm both parent packets unchanged."""
import hashlib, json, os, time
from pathlib import Path
HERE = Path(__file__).resolve().parent; ROOT = HERE.parents[2]; PAR = HERE.parent
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
parents = {}
for name in ('routeA_signfilter_20260917', 'arc_target_dimension_followup'):
    D = PAR / name; pm = json.loads((D / 'MANIFEST.json').read_text())
    mism = [p for p, h in pm['outputs_sha256'].items() if sha(D / p) != h]
    files = {}
    for root, dirs, fs in os.walk(D):
        for f in fs:
            rel = os.path.relpath(os.path.join(root, f), D).replace(os.sep, '/'); files[rel] = sha(os.path.join(root, f))
    unl = [r for r in files if r != 'MANIFEST.json' and r not in pm['outputs_sha256']]
    parents[name] = dict(outputs=len(pm['outputs_sha256']), mismatches=mism, unlisted=unl, unchanged=(not mism and not unl), files_sha256=files)
rm = json.loads((PAR / 'routeA_signfilter_20260917/MANIFEST.json').read_text())
inh = [p for p, h in rm['inherited_sealed_inputs_sha256'].items() if sha(ROOT / p) != h]
inputs = {p: sha(ROOT / p) for p in ['work/descent_followup_claude_20260916/pilots/p6_basis.json', 'work/descent_followup_claude_20260916/pilots/paired_runner.py',
          'work/batch15_workers/B15-02/analysis/b18_02_carrier.py', 'work/batch15_workers/B15-02/analysis/b15_bound.py', 'work/batch15_workers/B15-02/.venv/python.exe',
          'work/batch15_workers/B15-01/docs/b19_01_report.md', 'work/batch15_workers/B15-02/docs/b18_02_report.md',
          'work/claude_transverse_structure_20260916_followup/clarification_20260917/SOURCE_HANDOFF.md']}
outputs = {}
for p in sorted(HERE.rglob('*')):
    if p.is_file() and p.name != 'MANIFEST.json' and '__pycache__' not in str(p):
        outputs[str(p.relative_to(HERE)).replace(os.sep, '/')] = sha(p)
runs = []
for name in ('p1_covariant_counts', 'p2_isotypic_top_vanishing', 'p3_covariant_relation'):
    m = json.loads((HERE / 'results/logs' / (name + '_resources.json')).read_text())
    killed = 'exit_code' not in m
    runs.append(dict(name=name, wrapped=True, receipt='results/logs/%s_resources.json' % name, exit_code=(124 if killed else m['exit_code']), wall_seconds=(60.0 if killed else m['wall_seconds']), killed_at_wall_cap=killed, peak_job_memory=(m.get('job_memory') or {}).get('peak_job_memory'), memory_cap_mb=m['memory_cap_mb'], wall_cap_seconds=m['wall_cap_seconds'], workers=m['workers'], blas_threads=m['blas_threads']))
runs.append(dict(name='unwrapped_micro_computations', wrapped=False, wall_seconds=8.0, note='N_22 count (0.02 s), slice-geometry searches (~2 s), two smoke tests of pilot 3 (~5 s); disclosed in REPORT.md'))
man = dict(session='claude_source_vectors_20260917/direct_arc_relation_followup', created_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
           outcome='C (unresolved): rank_Q(C|U) neither proved 2 nor 3; proportional-tops mechanism refuted exactly (r_top = 3); factorization q3 = 2B(F1,F2), q7 = 2B(F3,F2), n02 = 2B(F1,F1) exact at the general point; degree-12 rows exact rank 1; no explicit rational survivor',
           parent_packets={k: {kk: vv for kk, vv in v.items() if kk != 'files_sha256'} for k, v in parents.items()}, parent_files_sha256={k: v['files_sha256'] for k, v in parents.items()},
           inherited_sealed_inputs_mismatches=inh, inputs_sha256=inputs, outputs_sha256=outputs, runs=runs,
           numerical_wall_seconds_total=sum(r['wall_seconds'] for r in runs), wrapped_pilots_used=3, wrapped_pilots_cap=3, source_vectors_evaluated_by_runner=0,
           historical_files_modified=[], receipts_overwritten=[], note='REPORT.md, CORRIGENDUM.md, code, results, verify_records.py finalised before hashing.')
(HERE / 'MANIFEST.json').write_text(json.dumps(man, indent=1) + '\n')
print('parents unchanged:', {k: v['unchanged'] for k, v in parents.items()}, '| inherited mismatches:', inh, '| outputs:', len(outputs), '| wall total:', round(man['numerical_wall_seconds_total'], 2))
