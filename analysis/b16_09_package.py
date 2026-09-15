"""Snapshot the actual B16-09 inputs, preserving B15 provenance byte for byte."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from hashlib import sha256
import json
from fractions import Fraction
import shutil

ROOT=Path(__file__).resolve().parents[1]
PROJECT=ROOT.parents[2]
SOURCE=ROOT.parent/'B15-08'
DELIVERY=ROOT/'delivery/b16_09'
SNAP=DELIVERY/'inputs'


def main():
    review=PROJECT/'Batch15_Launch/native_20260913/reviews_filesystem/B15-08_0256ed256196'
    intake_path=PROJECT/'Batch15_Launch/native_20260913/INTAKE.json'
    intake=json.loads(intake_path.read_text(encoding='utf-8-sig'))
    entry=next(x for x in intake['entries'] if x['slot']=='08')
    expected={x['path']:x['sha256'] for x in entry['input_hashes']}
    specs=[]
    for rel in ('analysis/b15_08_bracket.py','analysis/b15_08_points.py','analysis/b15_08_witness.py',
                'analysis/b14_04/recount.py','analysis/wk8_s30_pleth.py'):
        specs.append((SOURCE/rel,rel,expected.get(rel)))
    for rel in ('docs/b15_08_report.md','docs/b15_08_proved.md','results/PREREG_b15_08.md'):
        specs.append((SOURCE/rel,'b15_08/'+rel,expected.get(rel)))
    for rel in ('Batch16/BOARD.md','Batch16/launch/INPUT_MANIFEST.json','Batch16/launch/B16-09.md',
                'Batch16/launch/runtime_09.json','Batch16/launch/dispatch_09.json',
                'Batch15_Launch/native_20260913/INTAKE.json'):
        specs.append((PROJECT/rel,'project/'+rel,None))
    specs.append((review/'integrator_review.json','intake_b15_08/integrator_review.json',None))
    for rel in ('analysis/b15_bound.py','docs/s57_report.md','.venv/python.exe'):
        specs.append((ROOT/rel,'b15_09/'+rel,None))
    checks=[]
    for original,rel,wanted in specs:
        raw=original.read_bytes();digest=sha256(raw).hexdigest()
        if wanted: assert digest==wanted, str(original)
        target=SNAP/rel;target.parent.mkdir(parents=True,exist_ok=True)
        target.write_bytes(raw)
        checks.append(dict(original=str(original),snapshot='inputs/'+rel,sha256=digest,
            bytes=len(raw),intake_expected_sha256=wanted,intake_match=(digest==wanted) if wanted else None))
    source_snapshot_checks=[]
    for rel in ('analysis/b15_08_bracket.py','analysis/b15_08_witness.py','analysis/b14_04/recount.py',
                'analysis/wk8_s30_pleth.py','docs/b15_08_report.md','docs/b15_08_proved.md'):
        saved=review/'source'/rel
        assert saved.read_bytes()==(SOURCE/rel).read_bytes()
        source_snapshot_checks.append(dict(snapshot=str(saved),sha256=sha256(saved.read_bytes()).hexdigest(),
            byte_identical_to_original=True))
    # These snapshot bytes were also actual verification inputs, so preserve them.
    for item in source_snapshot_checks:
        path=Path(item['snapshot']);rel=path.relative_to(review/'source').as_posix()
        target=SNAP/'review_source'/rel;target.parent.mkdir(parents=True,exist_ok=True)
        target.write_bytes(path.read_bytes())
        checks.append(dict(original=str(path),snapshot='inputs/review_source/'+rel,
            sha256=item['sha256'],bytes=path.stat().st_size,intake_match=True))
    manifest=dict(status='FROZEN_ACTUAL_INPUTS',hash_convention='SHA256 exact bytes, CRLF retained',
        frozen_worktree_head='5e555cbe23725a247b572dde9b0ac9338f5dc797',
        frozen_worktree_tree='25ca726a9ff15b3e11fb2ef8254b2524e15fb4c2',
        source_worktree_head=entry['head'],source_worktree_tree=entry['tree'],
        source_snapshot_checks=source_snapshot_checks,inputs=checks,
        attribution='B15-08 GPT-6 Astra sources; B14-06 bordered-det input retains Claude Opus 5 attribution; B14-04/S30 character engines inherited.',
        packaging='Filesystem snapshots. No commit or merged base asserted. Python runtime snapshot records provenance; execute the assigned live .venv/python.exe.')
    DELIVERY.mkdir(parents=True,exist_ok=True)
    (DELIVERY/'input_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    cert=json.loads((ROOT/'results/b16_09/certificate.json').read_text())
    scales=cert['row_scaling']
    print(json.dumps(dict(input_files=len(checks),
        actual_matrix=[[str(Fraction(v,s)) for v in row] for row,s in zip(cert['integer_scaled_matrix'],scales)],
        integer_scaled_minor=cert['integer_scaled_minor'],
        frame_determinants=[p['full_frame']['integer_determinant'] for p in cert['points']],
        coefficient_pair_visits=[p['coefficient_pair_visits'] for p in cert['points']],
        character_terms=len(cert['character_terms']))))


if __name__=='__main__':main()
