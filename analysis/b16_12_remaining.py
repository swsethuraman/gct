"""Immutable intake and path-only receiver replay for delivered B16 slots04/05/06/08.

Run through the unchanged B15-12 b15_bound.py with -B, 60s and 512MiB.
Never execute delivery packagers or write outside owned results/b16_12.
"""
from pathlib import Path
import hashlib
import json
import runpy
import sys

WORK = Path(__file__).resolve().parents[1]
PROJECT = WORK.parents[2]
OUT = WORK/'results/b16_12'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def records(obj):
    if isinstance(obj, dict):
        if 'path' in obj and 'sha256' in obj:
            yield obj
        for value in obj.values():
            yield from records(value)
    elif isinstance(obj, list):
        for value in obj:
            yield from records(value)


def save(path, obj):
    path.write_text(json.dumps(obj, indent=2)+'\n', encoding='utf8')


def snapshot(slot):
    worker = PROJECT/f'work/batch15_workers/B15-{slot}'
    delivery = worker/f'delivery/b16_{slot}'
    target = OUT/'intake'/slot
    assert not target.exists(), 'Preserve previous intake'
    manifest_path = delivery/('ARTIFACT_HASHES.json' if slot == '08' else 'MANIFEST.json')
    raw = manifest_path.read_bytes()
    manifest = json.loads(raw)
    declared = manifest[{'04':'files','05':'outputs','06':'artifacts','08':'files'}[slot]]
    copies = {}
    for row in declared:
        source = Path(row['path'])
        if not source.is_absolute():
            source = worker/source
        source = source.resolve()
        rel = source.relative_to(worker)
        data = source.read_bytes()
        assert sha(data) == row['sha256'], str(source)
        assert len(data) == row['bytes'], str(source)
        copies[rel] = (source, data, 'declared_artifact')
    if slot == '05':
        inputs = list(records(manifest['input_hashes'])) + list(records(manifest['frozen_manifest_checks']))
    else:
        ip = (delivery/'INPUT_HASHES.json' if slot == '08' else worker/f'results/b16_{slot}/input_hashes.json')
        inputs = list(records(json.loads(ip.read_bytes())))
    input_rows = []
    for row in inputs:
        source = Path(row['path'])
        if not source.is_absolute():
            source = worker/source
        data = source.read_bytes()
        assert sha(data) == row['sha256'], str(source)
        assert len(data) == row.get('bytes', len(data)), str(source)
        input_rows.append({'path':str(source), 'sha256':sha(data), 'bytes':len(data)})
    # Also bind the delivery envelope without claiming it was self-hashed.
    for source in delivery.iterdir():
        if source.is_file() and source.relative_to(worker) not in copies:
            copies[source.relative_to(worker)] = (source, source.read_bytes(), 'delivery_envelope_current_bytes')
    assert manifest_path.read_bytes() == raw
    target.mkdir(parents=True)
    rows = []
    for rel, (source, data, role) in sorted(copies.items()):
        dest = target/rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
        assert source.read_bytes() == dest.read_bytes() == data
        rows.append({'source':str(source), 'snapshot':str(dest), 'relative':str(rel),
                     'bytes':len(data), 'sha256':sha(data), 'role':role})
    receipt = {'slot':slot, 'status':'PASS_IMMUTABLE_INTAKE_AND_INPUT_HASHES',
               'manifest_source':str(manifest_path), 'manifest_sha256':sha(raw),
               'declared_artifacts':len(declared), 'files':rows, 'original_inputs':input_rows}
    save(OUT/f'intake_{slot}.json', receipt)
    print(json.dumps({'slot':slot,'status':receipt['status'],'files':len(rows),'declared_artifacts':len(declared),'inputs':len(input_rows)}))


def verify(ledger):
    for row in ledger['files']:
        assert sha(Path(row['source']).read_bytes()) == row['sha256'], row['source']
        assert sha(Path(row['snapshot']).read_bytes()) == row['sha256'], row['snapshot']
    for row in ledger['original_inputs']:
        assert sha(Path(row['path']).read_bytes()) == row['sha256'], row['path']


def replay(slot, mode):
    ledger = json.loads((OUT/f'intake_{slot}.json').read_bytes())
    verify(ledger)
    worker = PROJECT/f'work/batch15_workers/B15-{slot}'
    target = OUT/'replay'/f'{slot}_{mode}'
    assert not target.exists(), 'Preserve prior replay'
    for row in ledger['files']:
        dest = target/row['relative']
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(Path(row['snapshot']).read_bytes())
    result_dir = target/f'results/b16_{slot}'
    result_dir.mkdir(parents=True, exist_ok=True)
    adapted = []

    def adapt(name, replacements):
        path = target/'analysis'/name
        before = path.read_bytes()
        code = before.decode('utf8')
        for old, new in replacements:
            assert code.count(old) == 1, (name, old)
            code = code.replace(old, new)
        path.write_text(code, encoding='utf8', newline='')
        adapted.append({'path':str(path), 'original_sha256':sha(before),
                        'adapted_sha256':sha(path.read_bytes()), 'path_only_replacements':replacements})

    literal = lambda p: 'Path('+repr(p.as_posix())+')'
    if slot == '04':
        assert mode == 'verify'
        adapt('b16_04_filtration.py', [('ROOT=HERE.parents[2]', 'ROOT='+literal(PROJECT))])
        script = target/'analysis/b16_04_verify.py'
        args = []
    elif slot == '05':
        assert mode in ('replay','proof')
        adapt('b16_05_receiver.py', [
            ('HERE = Path(__file__).resolve().parents[1]', 'HERE = '+literal(worker)),
            ("OUT = HERE / 'results/b16_05'", 'OUT = '+literal(result_dir))])
        script = target/('analysis/b16_05_proof.py' if mode == 'proof' else 'analysis/b16_05_receiver.py')
        args = [] if mode == 'proof' else ['replay']
    elif slot == '06':
        assert mode == 'verify'
        adapt('b16_06_receiver.py', [
            ('ROOT=Path(__file__).resolve().parents[1]', 'ROOT='+literal(worker)),
            ("OUT=ROOT/'results/b16_06'", 'OUT='+literal(result_dir))])
        sys.path.insert(0, str(worker/'analysis'))
        script = target/'analysis/b16_06_receiver.py'
        args = ['--verify']
    else:
        assert slot == '08' and mode == 'receive'
        adapt('b16_08_jets.py', [
            ('HERE = Path(__file__).resolve().parents[1]', 'HERE = '+literal(worker)),
            ("OUT = HERE / 'results/b16_08'", 'OUT = '+literal(result_dir))])
        script = target/'analysis/b16_08_jets.py'
        args = ['receive']
    save(OUT/f'replay_{slot}_{mode}_adaptations.json', adapted)
    sys.path.insert(0, str(script.parent))
    sys.argv = [str(script)] + args
    runpy.run_path(str(script), run_name='__main__')
    if slot == '05' and mode == 'proof':
        original = OUT/'intake/05/results/b16_05/proof_arithmetic.json'
        assert json.loads(original.read_bytes()) == json.loads((result_dir/'proof_arithmetic.json').read_bytes())
    verify(ledger)
    runtime = []
    for name, module in sorted(sys.modules.items()):
        filename = getattr(module, '__file__', None)
        if filename and Path(filename).is_file() and (name.startswith(('flint','sympy','numpy','b1')) or name == 'hessian11'):
            path = Path(filename)
            data = path.read_bytes()
            runtime.append({'module':name,'path':str(path),'sha256':sha(data),'bytes':len(data)})
    save(OUT/f'replay_{slot}_{mode}_integrity.json', {
        'status':'PASS', 'original_inputs_rechecked':len(ledger['original_inputs']),
        'immutable_delivery_files':len(ledger['files']), 'path_only_adaptations':adapted,
        'worker_and_intake_bytes_unchanged':True, 'runtime_modules':runtime})
    print(json.dumps({'slot':slot,'mode':mode,'integrity':'PASS'}))


if __name__ == '__main__':
    assert sys.dont_write_bytecode
    action, slot = sys.argv[1:3]
    assert slot in ('04','05','06','08')
    if action == 'snapshot':
        snapshot(slot)
    else:
        assert action == 'replay'
        replay(slot, sys.argv[3])
