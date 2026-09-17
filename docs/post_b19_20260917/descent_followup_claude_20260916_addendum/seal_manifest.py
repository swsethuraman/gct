"""Seal MANIFEST.json for the addendum: pins of the sealed packet files read, the historical
evaluator, and every output here. Run after CORRIGENDUM.md and FEASIBILITY.md are final."""
import hashlib, json, os, time
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SEALED = ROOT / 'work/descent_followup_claude_20260916'
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
inputs = [SEALED / 'REPORT.md', SEALED / 'MANIFEST.json', SEALED / 'pilots/p6_basis.json', SEALED / 'pilots/p7_arc_S0.json',
          SEALED / 'pilots/p2_carrier_arc.json', SEALED / 'pilots/p4_paired_basis.json', SEALED / 'pilots/p8_basis_v2.json',
          SEALED / 'pilots/paired_runner.py', ROOT / 'work/batch15_workers/B15-02/analysis/b18_02_carrier.py',
          ROOT / 'work/batch15_workers/B15-02/analysis/b15_bound.py']
outputs = sorted(p for p in HERE.rglob('*') if p.is_file() and p.name != 'MANIFEST.json')
man = dict(session='descent_followup_claude_20260916_addendum', sealed_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
           sealed_packet_unchanged=dict(REPORT_sha256=sha(SEALED / 'REPORT.md'), MANIFEST_sha256=sha(SEALED / 'MANIFEST.json')),
           inputs={str(p.relative_to(ROOT)).replace(os.sep, '/'): dict(sha256=sha(p), bytes=p.stat().st_size) for p in inputs},
           outputs={str(p.relative_to(HERE)).replace(os.sep, '/'): dict(sha256=sha(p), bytes=p.stat().st_size) for p in outputs},
           pilots_run=dict(count=1, wall_seconds_total=1.6889614, cap_seconds=60, cap_mib=512, wrapper='analysis/b15_bound.py (Job Object)'),
           note='reports finalised before sealing; manifest not self-hashing')
(HERE / 'MANIFEST.json').write_text(json.dumps(man, indent=1) + '\n')
print(json.dumps(dict(outputs=len(man['outputs']), sealed_packet=man['sealed_packet_unchanged']), indent=1))
