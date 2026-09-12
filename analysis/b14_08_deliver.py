"""Package the committed B14-08 named branch and verify an actual named fetch.

Writes only to the authorized delivery directory and a checked temporary
receiver under this session worktree. All subprocesses have a 120-second bound.
"""
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
DEST = Path('C:/Users/swami/Projects/gct-gpt/Batch14_Results/B14-08')
BASE = '9898e56941a7665f231873481dae956f08509995'
TREE = 'cb688cd3fe454d638f3202e759e2eaa0c629739f'
BRANCH = 'b14-08-astra'
CEILING = 5_000_000  # also below the repository checker's 5 MiB threshold


def run(arguments, cwd=ROOT, log=None):
    result = subprocess.run(arguments, cwd=cwd, capture_output=True, text=True, timeout=120)
    transcript = '$ '+subprocess.list2cmdline(list(map(str, arguments)))+'\n'
    transcript += result.stdout + result.stderr + '\nexit_code='+str(result.returncode)+'\n'
    if log:
        (DEST/log).write_text(transcript, encoding='utf-8')
    if result.returncode:
        raise RuntimeError(transcript)
    return result.stdout.strip()


def digests(path):
    data = path.read_bytes()
    return {'bytes': len(data), 'md5': hashlib.md5(data).hexdigest(),
            'sha256': hashlib.sha256(data).hexdigest()}


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    if run(['git', 'branch', '--show-current']) != BRANCH:
        raise RuntimeError('Wrong branch')
    if run(['git', 'status', '--porcelain']):
        raise RuntimeError('Commit intentional session changes before packaging')
    if run(['git', 'log', '-1', '--format=%H', 'batch14-base']) != BASE:
        raise RuntimeError('Frozen tag commit mismatch')
    if run(['git', 'log', '-1', '--format=%T', 'batch14-base']) != TREE:
        raise RuntimeError('Frozen tag tree mismatch')
    head = run(['git', 'rev-parse', BRANCH])
    head_tree = run(['git', 'log', '-1', '--format=%T', BRANCH])
    checker = [sys.executable, 'tools/delivery/check_delivery.py', '--branch', BRANCH, '--base', BASE]
    run(checker, log='delivery_precheck.log')
    bundle = DEST/'b14_08_astra.bundle'
    run(['git', 'bundle', 'create', str(bundle), BASE+'..'+BRANCH, BRANCH], log='bundle_creation.log')
    run(checker+['--bundle', str(bundle)], log='delivery_postcheck.log')
    heads = run(['git', 'bundle', 'list-heads', str(bundle)], log='bundle_list_heads.log')
    if head+' refs/heads/'+BRANCH not in heads.splitlines():
        raise RuntimeError('Named ref absent from actual bundle')
    run(['git', 'bundle', 'verify', str(bundle)], log='bundle_verify.log')
    header = bundle.read_bytes().split(b'\n\n', 1)[0].decode('utf-8')
    prerequisites = [line[1:].split(' ', 1)[0] for line in header.splitlines() if line.startswith('-')]
    if prerequisites != [BASE]:
        raise RuntimeError('Unexpected bundle prerequisites: '+repr(prerequisites))

    # Share source objects read-only to avoid copying this large research repo.
    # The operation still must resolve the requested branch name from the bundle.
    receiver = Path(tempfile.mkdtemp(prefix='.b14_08_receive_', dir=ROOT))
    if not receiver.resolve().is_relative_to(ROOT.resolve()):
        raise RuntimeError('Temporary receiver escaped the session')
    try:
        run(['git', 'init', '--bare', str(receiver)])
        objects = Path(run(['git', 'rev-parse', '--git-path', 'objects']))
        if not objects.is_absolute():
            objects = (ROOT/objects).resolve()
        (receiver/'objects/info/alternates').write_text(objects.as_posix()+'\n', encoding='utf-8')
        run(['git', '--git-dir='+str(receiver), 'update-ref', 'refs/heads/frozen-prerequisite', BASE])
        run(['git', '--git-dir='+str(receiver), 'fetch', '--no-tags', str(bundle),
             BRANCH+':refs/heads/'+BRANCH], log='named_branch_fetch.log')
        received_head = run(['git', '--git-dir='+str(receiver), 'rev-parse', 'refs/heads/'+BRANCH])
        received_tree = run(['git', '--git-dir='+str(receiver), 'log', '-1', '--format=%T', BRANCH])
        if (received_head, received_tree) != (head, head_tree):
            raise RuntimeError('Received head/tree mismatch')
        with (DEST/'named_branch_fetch.log').open('a', encoding='utf-8') as f:
            f.write('receiver_used_read_only_source_object_alternates=true\n')
            f.write('received_head='+received_head+'\nreceived_tree='+received_tree+'\nPASS\n')
    finally:
        resolved = receiver.resolve()
        if resolved.is_relative_to(ROOT.resolve()) and resolved.name.startswith('.b14_08_receive_'):
            shutil.rmtree(resolved)  # only this newly created, checked receiver

    data = bundle.read_bytes()
    parts = []
    for index, offset in enumerate(range(0, len(data), CEILING)):
        part = DEST/(bundle.name+'.part%02d' % index)
        part.write_bytes(data[offset:offset+CEILING]); parts.append(part)
    if len(parts) != 1:
        raise RuntimeError('Report says one part; revise it and commit before packaging')
    for algorithm in ('md5', 'sha256'):
        (DEST/(bundle.name+'.'+algorithm)).write_text(''.join(
            digests(path)[algorithm]+'  '+path.name+'\n' for path in [bundle, *parts]), encoding='ascii')

    sources = {'b14_08_report.md': ROOT/'docs/b14_08_report.md',
               'replay.md': ROOT/'results/b14_08/replay.md',
               'PREREG_b14_08.md': ROOT/'results/PREREG_b14_08.md'}
    for name in ('census.json', 'census.csv', 'witnesses.json', 'verification.json',
                 'summary.json', 'input_manifest.json'):
        sources[name] = ROOT/'results/b14_08'/name
    for name in ('b14_08_audit.py', 'b14_08_verify.py', 'b14_08_bound.py', 'b14_08_deliver.py'):
        sources[name] = ROOT/'analysis'/name
    for name, source in sources.items():
        shutil.copyfile(source, DEST/name)
    log_dir = DEST/'resource_logs'; log_dir.mkdir(exist_ok=True)
    for source in (ROOT/'results/logs').glob('b14_08_*'):
        if source.is_file():
            shutil.copyfile(source, log_dir/source.name)
    for name in sources:
        for algorithm in ('md5', 'sha256'):
            (DEST/(name+'.'+algorithm)).write_text(digests(DEST/name)[algorithm]+'  '+name+'\n', encoding='ascii')
    status = run(['git', 'status', '--porcelain'], log='worktree_status.log')
    if status:
        raise RuntimeError('Unexpected worktree changes after packaging')
    artifact_hashes = {str(path.relative_to(DEST)).replace('\\', '/'): digests(path)
                       for path in sorted(DEST.rglob('*')) if path.is_file() and
                       not path.name.startswith('delivery_manifest.json')}
    oversized = {name: record['bytes'] for name, record in artifact_hashes.items() if record['bytes'] > CEILING}
    if oversized:
        raise RuntimeError('Unexpected oversized artifacts: '+repr(oversized))
    manifest = {'board_numbering': 'batch14', 'session_id': 'B14-08', 'actual_model': 'gpt-6-astra',
                'reasoning_effort': 'xhigh', 'model_evidence': 'executing automation.toml',
                'completed_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
                'branch': BRANCH, 'base': BASE, 'base_tree': TREE, 'head': head, 'head_tree': head_tree,
                'prerequisites': prerequisites, 'bundle_refs': heads.splitlines(),
                'bundle': bundle.name, 'part_count': len(parts), 'parts': [p.name for p in parts],
                'preregistration_commit': run(['git', 'rev-parse', 'c58063e5']),
                'commit_attribution': run(['git', 'log', '--format=%H%n%B', BASE+'..'+BRANCH]),
                'repository_precheck': 'CLEAN', 'repository_postcheck': 'CLEAN',
                'bundle_verify': 'PASS', 'named_branch_fetch': 'PASS, source object alternates used read-only',
                'working_tree': 'clean', 'delivery_failures': [],
                'result': {'targets': 239, 'tests': 717, 'positive_pairs': 66, 'factor_witnesses': 61,
                           'local_controls': 29, 'historical_checks': 8, 'new_exclusions': 0,
                           'LMR_D_interval_unchanged': [-4, 1], 'exact_birth_increments_still_open': 235},
                'artifacts': artifact_hashes}
    manifest_path = DEST/'delivery_manifest.json'
    manifest_path.write_text(json.dumps(manifest, indent=2)+'\n', encoding='utf-8')
    for algorithm in ('md5', 'sha256'):
        (DEST/(manifest_path.name+'.'+algorithm)).write_text(
            digests(manifest_path)[algorithm]+'  '+manifest_path.name+'\n', encoding='ascii')
    print(json.dumps({'head': head, 'tree': head_tree, 'bundle_bytes': len(data),
                      'part_count': len(parts), 'delivery': str(DEST), 'status': 'CLEAN; named fetch PASS'}))


if __name__ == '__main__':
    main()
