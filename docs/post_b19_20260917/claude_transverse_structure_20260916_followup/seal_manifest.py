"""Seal MANIFEST.json for the follow-up: inputs (read-only), preserved sealed packet, outputs."""
import hashlib, json, time
from pathlib import Path, PurePosixPath
root = Path('C:/users/swami/projects/gct-gpt')
def h(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
inputs = [
 'work/descent_followup_claude_20260916/pilots/p6_basis.json',
 'work/descent_followup_claude_20260916/pilots/p7_arc_S0.json',
 'work/descent_followup_claude_20260916/pilots/paired_runner.py',
 'work/descent_followup_claude_20260916/pilots/p7_arc_S0.py',
 'work/batch15_workers/B15-02/analysis/b18_02_carrier.py',
 'work/batch15_workers/B15-02/analysis/b15_bound.py',
 'work/descent_followup_claude_20260916_addendum/FEASIBILITY.md',
 'work/descent_followup_claude_20260916_addendum/MANIFEST.json',
]
sealed = sorted(PurePosixPath(p.relative_to(root)).as_posix() for p in (root / 'work/claude_transverse_structure_20260916').rglob('*') if p.is_file())
here = Path('.')
outputs = sorted(PurePosixPath(p.relative_to(here)).as_posix() for p in here.rglob('*') if p.is_file() and p.name != 'MANIFEST.json')
man = {
 'session': 'claude_transverse_structure_20260916_followup',
 'created_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
 'interpreter': 'work/batch15_workers/B15-02/.venv/python.exe (Python 3.12.10)',
 'wrapper': 'work/batch15_workers/B15-02/analysis/b15_bound.py, 60 s / 512 MiB, one process, one BLAS thread; receipts in results/logs/',
 'read_only_inputs_sha256': {p: h(root / p) for p in inputs},
 'preserved_sealed_packet_sha256': {p: h(root / p) for p in sealed},
 'outputs_sha256': {p: h(here / p) for p in outputs},
 'numerical_pilots': [
  {'name': 'f1_c4_vs_c2', 'script': 'pilots/f1_c4_vs_c2.py', 'result': 'pilots/f1_c4_vs_c2.json', 'receipt': 'results/logs/f1_c4_vs_c2_resources.json', 'note': 'stopped by its own corruption control (the corruption was a stabilizer conjugate); reproduction passed for each vector'},
  {'name': 'f2_c4_vs_c2', 'script': 'pilots/f2_c4_vs_c2.py', 'result': 'pilots/f2_c4_vs_c2.json', 'receipt': 'results/logs/f2_c4_vs_c2_resources.json', 'note': 'complete; all controls passed; minors 247396, 197933, 281079 mod 524287'},
 ],
 'arithmetic_only': {'script': 'pilots/f3_derived_rows.py', 'result': 'pilots/f3_derived_rows.json', 'note': 'no evaluations; E-using rows from stored values; ambient ratios adopted from Check 2'},
 'outcome': '2: fourth-order compatibility certified independent of C2 on span(q3,q7); arc independence open',
 'historical_files_modified': [],
 'note': 'REPORT.md and CORRIGENDUM.md finalised before hashing.',
}
for c in man['numerical_pilots']:
    r = json.loads((here / c['receipt']).read_text()); c.update(exit_code=r.get('exit_code'), wall_seconds=r.get('wall_seconds'), peak_job_memory=r.get('job_memory', {}).get('peak_job_memory'))
(here / 'MANIFEST.json').write_text(json.dumps(man, indent=1) + '\n')
print(json.dumps(man['numerical_pilots'], indent=1)); print(len(outputs), 'outputs;', len(sealed), 'sealed files re-hashed')
print('sealed REPORT', man['preserved_sealed_packet_sha256']['work/claude_transverse_structure_20260916/REPORT.md'][:16], 'sealed MANIFEST', man['preserved_sealed_packet_sha256']['work/claude_transverse_structure_20260916/MANIFEST.json'][:16])
