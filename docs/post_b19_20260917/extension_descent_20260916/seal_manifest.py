import hashlib
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent.parent
inputs=[
 'work/batch15_workers/B15-02/docs/b17_02_report.md',
 'work/batch15_workers/B15-02/docs/b18_02_report.md',
 'work/batch15_workers/B15-01/docs/b19_01_report.md',
 'work/batch15_workers/B15-01/docs/b19_01_review.md',
 'work/batch15_workers/B15-10/docs/b15_10_proved.md',
 'work/batch15_workers/B15-02/docs/b19_02_report.md',
 'work/batch15_workers/B15-02/docs/b19_02_review.md',
 'work/batch15_workers/B15-06/analysis/b18_06_sweep.py',
 'work/batch15_workers/B15-02/analysis/b15_bound.py',
 'Batch17_Planning/symmetry_dream/astra/toy_character_screen_d5_d6.json',
]
def record(p):
    return {'path':str(p.relative_to(ROOT)).replace('\\','/'),'bytes':p.stat().st_size,
            'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
result={'scope':'One proved six-row false survivor; one negative five-row pilot; no five-row equation or gap.',
        'inputs':[record(ROOT/p) for p in inputs],
        'outputs':[record(p) for p in sorted(HERE.rglob('*')) if p.is_file()
                   and p.name!='MANIFEST.json' and p.suffix in ('.md','.py','.json')],
        'claims':{'six_row_old_arc_rank':0,'six_row_new_scalar_rank':1,
                  'six_row_combined_rank':1,'six_row_descent_witness':6884352000,
                  'five_row_pilot':'no determinant equation in (d=6,lambda=(12,8,2,1,1))',
                  'new_five_row_equation':False,'positive_gap':False}}
HERE.joinpath('MANIFEST.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'inputs':len(result['inputs']),'outputs':len(result['outputs']),'sealed':True}))
