"""Seal MANIFEST.json: SHA-256 of every input read and every output written by this session.
Run AFTER REPORT.md is final. Paths relative to the gct-gpt workspace root unless absolute."""
import hashlib, json, os, sys, time
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()
inputs = [
    'Claude_Handover_B15_B18/CLAUDE_DESCENT_FOLLOWUP_20260916.md',
    'work/extension_descent_20260916/REPORT.md', 'work/extension_descent_20260916/MANIFEST.json',
    'work/extension_descent_20260916/sixrow_witness.py', 'work/extension_descent_20260916/skew_witness.py',
    'work/extension_descent_20260916/sixrow_witness.json', 'work/extension_descent_20260916/skew_witness.json',
    'work/extension_descent_20260916/verify_witness.py', 'work/extension_descent_20260916/verification.json',
    'work/extension_descent_20260916/five_row_pilot.py', 'work/extension_descent_20260916/five_row_pilot.json',
    'work/extension_descent_20260916/verify_five_row.py', 'work/extension_descent_20260916/five_row_verification.json',
    'work/extension_descent_20260916/results/logs/five_row_pilot_resources.json',
    'work/fiber_compatibility_20260916/REPORT.md', 'work/fiber_compatibility_20260916/MANIFEST.json',
    'work/fiber_compatibility_20260916/pilot.py', 'work/fiber_compatibility_20260916/pilot.json',
    'work/fiber_compatibility_20260916/exact_pair.py', 'work/fiber_compatibility_20260916/exact_pair.json',
    'work/fiber_compatibility_20260916/verify.py', 'work/fiber_compatibility_20260916/verification.json',
    'work/fiber_compatibility_20260916/rectangular_factor_check.py', 'work/fiber_compatibility_20260916/rectangular_factor_check.json',
    'work/fiber_compatibility_20260916/results/logs/fiber_pilot_resources.json',
    'work/batch15_workers/B15-12/docs/b18_12_coefficient_algebra.md',
    'work/batch15_workers/B15-12/analysis/b18_12_fibre_check.py', 'work/batch15_workers/B15-12/analysis/b18_12_ambient_table.py',
    'work/batch15_workers/B15-12/results/b18_12/fibre_check.out', 'work/batch15_workers/B15-12/results/b18_12/ambient_table.out',
    'work/batch15_workers/B15-02/analysis/b18_02_carrier.py', 'work/batch15_workers/B15-02/analysis/b15_bound.py',
    'work/batch15_workers/B15-02/analysis/b19_02_rect.py', 'work/batch15_workers/B15-02/results/b19_02/rect_4_4_4_4_4.json',
    'work/batch15_workers/B15-02/docs/b18_02_report.md', 'work/batch15_workers/B15-02/docs/b19_02_report.md', 'work/batch15_workers/B15-02/docs/b19_02_review.md',
    'work/batch15_workers/B15-01/docs/b19_01_report.md', 'work/batch15_workers/B15-01/docs/b18_01_report.md',
    'work/batch15_workers/B15-06/analysis/b18_06_sweep.py',
    'Claude_Handover_B15_B18/batch19_launch/B19_PREAMBLE.md',
    'Batch17_Planning/symmetry_dream/astra/toy_character_screen_d5_d6.json',
]
attachments = {
    'e95184a7': 'C:/Users/swami/.codex/attachments/e95184a7-abfe-47c2-890d-33657b1ef45e/pasted-text.txt',
    'ccc1abb3': 'C:/Users/swami/.codex/attachments/ccc1abb3-7107-4b7d-8026-ba0c85252064/pasted-text.txt',
    '43761221': 'C:/Users/swami/.codex/attachments/43761221-fb51-456c-be76-a0579371b0c0/pasted-text.txt',
    '515d31fd': 'C:/Users/swami/.codex/attachments/515d31fd-e196-4d2b-9ba3-a164462b5672/pasted-text.txt',
    'd4a38184': 'C:/Users/swami/.codex/attachments/d4a38184-669a-4ea3-a5a3-dae2e39a915a/pasted-text.txt',
}
outputs = ["REPORT.md"] + sorted(str(p.relative_to(HERE)).replace(os.sep, "/") for p in list(HERE.glob("pilots/*")) + list(HERE.glob("results/logs/*")) + [HERE / "seal_manifest.py"] if p.is_file())
man = dict(
    session='descent_followup_claude_20260916', sealed_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
    workspace_root=str(ROOT),
    inputs={p: dict(sha256=sha(ROOT / p), bytes=(ROOT / p).stat().st_size) for p in inputs if (ROOT / p).exists()},
    inputs_missing=[p for p in inputs if not (ROOT / p).exists()],
    attachments={k: dict(path=v, sha256=sha(v), bytes=Path(v).stat().st_size) for k, v in attachments.items()},
    literature=dict(eisenbud_harris_1988=dict(url='https://eisenbud.github.io/papers/pdfs/1988-004.pdf', sha256_prefix='6b10d8fea80396a7', note='fetched copy kept outside the delivery tree; not readable in this environment'),
                    huang_landsberg=dict(arxiv='2306.14428'), css_cayley=dict(arxiv='1105.6270'), hmsv=dict(url='https://ems.press/content/serial-article-files/31806')),
    outputs={p: dict(sha256=sha(HERE / p), bytes=(HERE / p).stat().st_size) for p in outputs},
    note='REPORT.md was finalised before this manifest was written; the manifest is not self-hashing.',
)
(HERE / 'MANIFEST.json').write_text(json.dumps(man, indent=1) + '\n')
print(json.dumps(dict(inputs=len(man['inputs']), missing=man['inputs_missing'], outputs=len(man['outputs']), report_sha256=man['outputs']['REPORT.md']['sha256']), indent=1))
