"""Seal MANIFEST.json: read-only inputs (programme documents, wrapper), literature hashes (scratchpad, not copied), outputs."""
import hashlib, json, os, time
from pathlib import Path, PurePosixPath
root = Path('C:/users/swami/projects/gct-gpt')
orig = Path('C:/users/swami/projects/gct')
def h(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
inputs_recent = [
 'work/batch15_workers/B15-02/analysis/b15_bound.py',
 'work/batch15_workers/B15-01/docs/b18_01_report.md',
 'work/batch15_workers/B15-05/docs/b18_05_report.md',
 'work/batch15_workers/B15-10/docs/b18_10_review.md',
 'work/batch15_workers/B15-01/docs/equation_census.md',
 'work/batch15_workers/B15-01/docs/excess_singularity.md',
 'work/batch15_workers/B15-01/docs/s49_s55_batch_review.md',
 'work/batch15_workers/B15-04/docs/b17_04_report.md',
 'work/claude_image_ceiling_20260916/REPORT.md',
 'work/claude_singular_locus_audit_20260916/REPORT.md',
 'work/claude_transverse_structure_20260916_followup/clarification_20260917/SOURCE_HANDOFF.md',
 'work/claude_source_vectors_20260917/routeA_signfilter_20260917/REPORT.md',
 'work/claude_source_vectors_20260917/arc_target_dimension_followup/REPORT.md',
]
inputs_orig = [
 'work/docs/onset_conjecture.md',
 'work/docs/paper1_delta0_patch.md',
 'work/docs/PROVED.md',
 'work/paper/det4-onset.tex',
 'work/paper/det3-conductor.tex',
]
lit_dir = Path(os.environ['GKZ_LIT_DIR'])
literature = {
 'segal_gkz_2412.14748.pdf': {'source': 'https://arxiv.org/pdf/2412.14748', 'version': 'arXiv:2412.14748v1 (19 Dec 2024)'},
 'dimca_1210.1795.pdf': {'source': 'https://arxiv.org/pdf/1210.1795', 'version': 'arXiv:1210.1795v4 (24 Dec 2012)'},
}
for name, d in literature.items():
    p = lit_dir / name
    d['sha256'] = h(p); d['bytes'] = p.stat().st_size; d['kept_in'] = 'session scratchpad (not in the delivery tree)'
here = Path(__file__).resolve().parent
outputs = sorted(PurePosixPath(p.relative_to(here)).as_posix() for p in here.rglob('*') if p.is_file() and p.name != 'MANIFEST.json')
man = {
 'session': 'claude_gkz_incidence_20260917',
 'created_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
 'outcome': 'C: rigorous negative. GKZ Cayley-complex route = Macaulay/Koszul Fitting ideals; Theorem A (16 vars, all k) and Theorem B (5 vars, all k) proved with exact certificates; second differential D_7 exact ranks 1904 (det4) vs 1650 (z per3). No gap claimed.',
 'interpreter': 'work/batch15_workers/B15-02/.venv/python.exe (Python 3.12.10, numpy 2.4.6, sympy 1.14.0, python-flint 0.9.0)',
 'wrapper': 'work/batch15_workers/B15-02/analysis/b15_bound.py, 60 s / 512 MiB, one process, one BLAS thread; receipts in results/logs/',
 'read_only_inputs_sha256_gct_gpt': {p: h(root / p) for p in inputs_recent},
 'read_only_inputs_sha256_gct_original': {p: h(orig / p) for p in inputs_orig},
 'literature': literature,
 'outputs_sha256': {p: h(here / p) for p in outputs},
 'pilots': [
  {'name': 'p1_ambient_macaulay', 'script': 'pilots/p1_ambient_macaulay.py', 'result': 'pilots/p1_ambient_macaulay.json', 'receipt': 'results/logs/p1_ambient_macaulay_resources.json'},
  {'name': 'p2_quinary_macaulay', 'script': 'pilots/p2_quinary_macaulay.py', 'result': 'pilots/p2_quinary_macaulay.json', 'receipt': 'results/logs/p2_quinary_macaulay_resources.json'},
  {'name': 'p3_koszul2_exact', 'script': 'pilots/p3_koszul2_exact.py', 'result': 'pilots/p3_koszul2_exact.json', 'receipt': 'results/logs/p3_koszul2_exact_resources.json'},
 ],
 'historical_files_modified': [],
 'note': 'REPORT.md finalised (status line replaced) before hashing. Unwrapped work: file reads, pdftotext, one 2x2 python-flint API syntax check, this hashing script. P1 all_checks_pass=false reflects only its exploratory hypothesis check (D_7 full row rank at det4), which was false and was settled exactly by P3; all P1 certificate checks passed.',
}
for c in man['pilots']:
    r = json.loads((here / c['receipt']).read_text())
    c.update(exit_code=r.get('exit_code'), wall_seconds=r.get('wall_seconds'), peak_job_memory=r.get('job_memory', {}).get('peak_job_memory'), job_object_enforced=r.get('job_object_enforced'))
    j = json.loads((here / c['result']).read_text()); c['all_checks_pass'] = j.get('all_checks_pass')
(here / 'MANIFEST.json').write_text(json.dumps(man, indent=1) + '\n')
print(json.dumps(man['pilots'], indent=1)); print(len(outputs), 'outputs hashed'); print('total wall', sum(c['wall_seconds'] for c in man['pilots']))
