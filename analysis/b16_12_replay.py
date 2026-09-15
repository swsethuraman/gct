"""Run reviewed delivered receivers in owned replay directories, under b15_bound.py."""
from pathlib import Path
import hashlib
import json
import runpy
import sys

WORK=Path(__file__).resolve().parents[1]
OUT=WORK/'results/b16_12'

def main():
    slot=sys.argv[1]
    assert slot in ('03','07')
    intake=OUT/'intake'/slot
    ledger=json.loads((OUT/f'intake_{slot}.json').read_bytes())
    for row in ledger['files']:
        assert hashlib.sha256(Path(row['snapshot']).read_bytes()).hexdigest()==row['sha256']
    for row in ledger['original_inputs']:
        assert hashlib.sha256(Path(row['path']).read_bytes()).hexdigest()==row['sha256']
    if slot=='03':
        replay=OUT/'replay'/slot
        assert not replay.exists(), 'Preserve prior replay'
        for row in ledger['files']:
            dest=replay/row['relative']
            dest.parent.mkdir(parents=True,exist_ok=True)
            dest.write_bytes(Path(row['snapshot']).read_bytes())
        script=replay/'analysis/b16_03_receiver.py'
        sys.path.insert(0,str(script.parent))
        sys.argv=[str(script),'verify']
    else:
        script=intake/'analysis/b16_07_receive.py'
        sys.argv=[str(script),'--certificate',str(intake/'results/b16_07/pilot.json'),
                  '--inputs',str(intake/'results/b16_07/input_hashes.json'),
                  '--out',str(OUT/'receiver07.json')]
    runpy.run_path(str(script),run_name='__main__')
    # Check immutable intake and original upstream inputs again after replay.
    for row in ledger['files']:
        assert hashlib.sha256(Path(row['snapshot']).read_bytes()).hexdigest()==row['sha256']
    for row in ledger['original_inputs']:
        assert hashlib.sha256(Path(row['path']).read_bytes()).hexdigest()==row['sha256']
    runtime=[]
    for name,module in sorted(sys.modules.items()):
        if name.startswith(('flint','sympy')):
            path=getattr(module,'__file__',None)
            if path and Path(path).is_file():
                raw=Path(path).read_bytes()
                runtime.append({'module':name,'path':path,'bytes':len(raw),
                                'sha256':hashlib.sha256(raw).hexdigest()})
    (OUT/f'replay_{slot}_integrity.json').write_text(json.dumps({
        'status':'PASS','immutable_delivery_files':len(ledger['files']),
        'original_inputs_rechecked':len(ledger['original_inputs']),
        'runtime_modules':runtime,'frozen_inputs_unchanged_after_replay':True},indent=2)+'\n')

if __name__=='__main__':
    main()
