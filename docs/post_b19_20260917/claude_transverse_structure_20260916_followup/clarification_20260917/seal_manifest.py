"""Seal MANIFEST.json for clarification_20260917: read-only inputs, the two preserved packets, outputs."""
import hashlib, json, time
from pathlib import Path, PurePosixPath
root = Path('C:/users/swami/projects/gct-gpt'); here = Path('.')
def h(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
inputs = ['work/descent_followup_claude_20260916/pilots/p6_basis.json', 'work/descent_followup_claude_20260916/pilots/p6_basis.py',
 'work/descent_followup_claude_20260916/pilots/p7_arc_S0.json', 'work/descent_followup_claude_20260916/pilots/p7_arc_S0.py',
 'work/descent_followup_claude_20260916/pilots/paired_runner.py', 'work/descent_followup_claude_20260916/pilots/p3_c2_derivation.py',
 'work/descent_followup_claude_20260916/pilots/p3_c2_derivation.json', 'work/descent_followup_claude_20260916/pilots/p2_carrier_arc.json',
 'work/descent_followup_claude_20260916/pilots/p4_paired_basis.json', 'work/descent_followup_claude_20260916/pilots/p8_basis_v2.json',
 'work/descent_followup_claude_20260916_addendum/pilots/q1_price.json', 'work/descent_followup_claude_20260916_addendum/CORRIGENDUM.md',
 'work/descent_followup_claude_20260916_addendum/FEASIBILITY.md', 'work/batch15_workers/B15-02/analysis/b18_02_carrier.py',
 'work/batch15_workers/B15-02/analysis/b15_bound.py', 'work/batch15_workers/B15-02/results/b19_02/rect_4_4_4_4_4.json',
 'work/batch15_workers/B15-02/analysis/b19_02_rect.py', 'work/batch15_workers/B15-01/docs/b19_01_report.md',
 'work/batch15_workers/B15-02/docs/b18_02_report.md', 'work/batch15_workers/B15-02/docs/b19_02_report.md']
packets = {}
for d in ('work/claude_transverse_structure_20260916', 'work/claude_transverse_structure_20260916_followup'):
    for p in sorted((root / d).rglob('*')):
        if p.is_file() and 'clarification_20260917' not in p.as_posix(): packets[PurePosixPath(p.relative_to(root)).as_posix()] = h(p)
outputs = sorted(PurePosixPath(p.relative_to(here)).as_posix() for p in here.rglob('*') if p.is_file() and p.name != 'MANIFEST.json')
man = {'session': 'claude_transverse_structure_20260916_followup/clarification_20260917', 'created_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
 'read_only_inputs_sha256': {p: h(root / p) for p in inputs}, 'preserved_packets_sha256': packets, 'outputs_sha256': {p: h(here / p) for p in outputs},
 'checks': [{'name': 'c1_e_arc_kernel', 'wrapped': True, 'receipt': 'results/logs/c1_e_arc_kernel_resources.json'}, {'name': 'c2_three_rows_rank', 'wrapped': False, 'note': 'arithmetic on stored values only'}],
 'no_source_contraction_evaluated': True, 'historical_files_modified': [], 'note': 'CORRIGENDUM.md, STABILIZER.md, SOURCE_HANDOFF.md finalised before hashing.'}
r = json.loads((here / 'results/logs/c1_e_arc_kernel_resources.json').read_text()); man['checks'][0].update(exit_code=r['exit_code'], wall_seconds=r['wall_seconds'], peak_job_memory=r['job_memory']['peak_job_memory'])
(here / 'MANIFEST.json').write_text(json.dumps(man, indent=1) + '\n')
print(len(outputs), 'outputs;', len(packets), 'preserved files')
for k in ('work/claude_transverse_structure_20260916/REPORT.md', 'work/claude_transverse_structure_20260916/MANIFEST.json', 'work/claude_transverse_structure_20260916_followup/REPORT.md', 'work/claude_transverse_structure_20260916_followup/CORRIGENDUM.md', 'work/claude_transverse_structure_20260916_followup/MANIFEST.json'):
    print(packets[k][:16], k)
