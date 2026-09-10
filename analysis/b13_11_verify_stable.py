"""Replay all sixteen frozen s79 stable blocks on the independent checker."""
import json
from pathlib import Path
import sys
import wk12_int_s79_stable_verify as checker

root=Path(__file__).resolve().parents[1]
dest=root/'results/b13_11'; dest.mkdir(exist_ok=True)
paths=sorted((root/'results/s79_stable').glob('**/*_summary.json'))
if len(paths)!=16: raise ValueError('incomplete frozen stable block list')
for path in paths:
    checker.SRC=str(path.parent)
    block=path.name.removeprefix('stable_').removesuffix('_summary.json')
    checker.main([block,'--out',str(dest/'stable_replay.json')])
checker.out.update(board_numbering='batch13',session_id='B13-11',
                   expected_blocks=16,expected_checks=16*12)
with (dest/'stable_replay.json').open('w') as f: json.dump(checker.out,f,indent=1)
if len(checker.out['checks'])!=192 or any(not c['ok'] for c in checker.out['checks']):
    sys.exit(1)
