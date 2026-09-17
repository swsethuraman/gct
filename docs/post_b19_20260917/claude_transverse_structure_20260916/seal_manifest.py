"""Seal MANIFEST.json: SHA-256 of read-only inputs, attachments, and every output of this session.
Run from the session directory after REPORT.md is final."""
import hashlib, json, time
from pathlib import Path, PurePosixPath
root = Path('C:/users/swami/projects/gct-gpt')
def h(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
inputs = [
 'Claude_Handover_B15_B18/CLAUDE_DESCENT_FOLLOWUP_20260916.md',
 'work/descent_followup_claude_20260916/REPORT.md',
 'work/descent_followup_claude_20260916/MANIFEST.json',
 'work/descent_followup_claude_20260916/pilots/p3_c2_derivation.json',
 'work/descent_followup_claude_20260916/pilots/p3_c2_derivation.py',
 'work/descent_followup_claude_20260916/pilots/p9_sixrow_replay.json',
 'work/descent_followup_claude_20260916/pilots/p9_sixrow_replay.py',
 'work/descent_followup_claude_20260916_addendum/CORRIGENDUM.md',
 'work/descent_followup_claude_20260916_addendum/FEASIBILITY.md',
 'work/extension_descent_20260916/REPORT.md',
 'work/fiber_compatibility_20260916/REPORT.md',
 'work/batch15_workers/B15-01/docs/b19_01_report.md',
 'work/batch15_workers/B15-02/analysis/b15_bound.py',
 'work/batch15_workers/B15-12/docs/b18_12_coefficient_algebra.md',
]
attachments = {
 'attachment_515d31fd_sixrow_order4': 'C:/Users/swami/.codex/attachments/515d31fd-e196-4d2b-9ba3-a164462b5672/pasted-text.txt',
 'attachment_43761221_quadratic_square': 'C:/Users/swami/.codex/attachments/43761221-fb51-456c-be76-a0579371b0c0/pasted-text.txt',
}
here = Path('.')
outputs = sorted(PurePosixPath(p.relative_to(here)).as_posix() for p in here.rglob('*') if p.is_file() and p.name != 'MANIFEST.json')
man = {
 'session': 'claude_transverse_structure_20260916',
 'created_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
 'interpreter': 'work/batch15_workers/B15-02/.venv/python.exe (Python 3.12.10, sympy 1.14.0)',
 'wrapper': 'work/batch15_workers/B15-02/analysis/b15_bound.py, 60 s / 512 MiB, one process, one BLAS thread; receipts in results/logs/',
 'read_only_inputs_sha256': {p: h(root / p) for p in inputs},
 'attachments_sha256': {k: h(v) for k, v in attachments.items()},
 'outputs_sha256': {p: h(here / p) for p in outputs},
 'numerical_checks': [
  {'name': 'c1_normal_space_counts', 'script': 'checks/c1_normal_space_counts.py', 'result': 'checks/c1_normal_space_counts.json', 'receipt': 'results/logs/c1_normal_space_counts_resources.json'},
  {'name': 'c2_fivevar_order4', 'script': 'checks/c2_fivevar_order4.py', 'result': 'checks/c2_fivevar_order4.json', 'receipt': 'results/logs/c2_fivevar_order4_resources.json'},
 ],
 'not_run': 'the section 9.2 three-way test (source-carrier evaluations); overlaps the active sparse-evaluator session',
 'historical_files_modified': [],
 'note': 'REPORT.md finalised before hashing; drafts/REPORT_body_draft.md is the superseded first draft of sections 4-12.',
}
for c in man['numerical_checks']:
    r = json.loads((here / c['receipt']).read_text())
    c.update(exit_code=r.get('exit_code'), wall_seconds=r.get('wall_seconds'), peak_job_memory=r.get('job_memory', {}).get('peak_job_memory'))
(here / 'MANIFEST.json').write_text(json.dumps(man, indent=1) + '\n')
print(json.dumps(man['numerical_checks'], indent=1))
print(len(outputs), 'outputs hashed; REPORT.md', man['outputs_sha256']['REPORT.md'])
