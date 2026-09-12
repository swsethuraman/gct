"""Export the committed B14-05 named branch, checks and exact artifacts.

Run only after committing intentional changes. No pushes or integration writes.
The output directory is the explicitly authorized delivery location.
"""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys

BASE = '9898e56941a7665f231873481dae956f08509995'
TREE = 'cb688cd3fe454d638f3202e759e2eaa0c629739f'
BRANCH = 'b14-05-astra'
OUT = Path('C:/Users/swami/Projects/gct-gpt/Batch14_Results/B14-05')
MAX_BYTES = 5_000_000


def run(argv, log=None):
    result = subprocess.run(argv, capture_output=True, text=True, timeout=120)
    if log:
        (OUT/log).write_text('COMMAND: '+json.dumps(argv)+'\nEXIT: '+str(result.returncode)
                             +'\nSTDOUT:\n'+result.stdout+'\nSTDERR:\n'+result.stderr, encoding='utf-8')
    if result.returncode:
        raise RuntimeError(f'Command failed ({result.returncode}): {argv}\n{result.stderr}\n{result.stdout}')
    return result.stdout.strip()


def digest(path, algorithm):
    h = hashlib.new(algorithm)
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024*1024), b''):
            h.update(chunk)
    return h.hexdigest()


def describe(path):
    return {'filename': path.name, 'bytes': path.stat().st_size,
            'md5': digest(path, 'md5'), 'sha256': digest(path, 'sha256')}


def main():
    if run(['git', 'branch', '--show-current']) != BRANCH:
        raise ValueError('Incorrect branch')
    if run(['git', 'status', '--porcelain']):
        raise ValueError('Commit intentional session changes before packaging')
    if run(['git', 'log', '-1', '--format=%H', 'batch14-base']) != BASE:
        raise ValueError('Frozen tag commit mismatch')
    if run(['git', 'log', '-1', '--format=%T', 'batch14-base']) != TREE:
        raise ValueError('Frozen tag tree mismatch')
    OUT.mkdir(parents=True, exist_ok=True)
    head = run(['git', 'rev-parse', BRANCH])
    tree = run(['git', 'log', '-1', '--format=%T', BRANCH])
    check = [sys.executable, 'tools/delivery/check_delivery.py', '--branch', BRANCH, '--base', BASE]
    run(check, 'delivery_pre_bundle.log')
    bundle = OUT/'b14_05_astra.bundle'
    run(['git', 'bundle', 'create', str(bundle), BASE+'..'+BRANCH, BRANCH], 'bundle_create.log')
    heads = run(['git', 'bundle', 'list-heads', str(bundle)], 'bundle_list_heads.log')
    if head+' refs/heads/'+BRANCH not in heads:
        raise ValueError('Named branch not exported')
    run(['git', 'bundle', 'verify', str(bundle)], 'bundle_verify.log')
    run(check+['--bundle', str(bundle)], 'delivery_post_bundle.log')
    data = bundle.read_bytes()
    parts = []
    for i, start in enumerate(range(0, len(data), MAX_BYTES)):
        part = OUT/(bundle.name+f'.part{i:02d}')
        part.write_bytes(data[start:start+MAX_BYTES]); parts.append(part)
    if len(parts) != 1:
        raise ValueError('Report declares one part; update it and recommit before delivery')
    if b''.join(p.read_bytes() for p in parts) != data:
        raise ValueError('Parts do not reconstruct the bundle')
    # Parse the prerequisite lines from the bundle header, which precedes PACK bytes.
    header = data.split(b'\n\n', 1)[0].decode('utf-8')
    prerequisites = [line[1:] for line in header.splitlines() if line.startswith('-')]
    if not any(line.split()[0] == BASE for line in prerequisites):
        raise ValueError('Frozen base missing from bundle prerequisites')
    sources = [Path('docs/b14_05_report.md'), Path('docs/b14_05_transport.md'),
               Path('results/PREREG_b14_05.md')]
    sources += sorted(Path('results/b14_05').glob('*'))
    sources += sorted(Path('results/logs').glob('b14_05_*'))
    sources += sorted(Path('analysis').glob('b14_05_*.py'))
    copied = []
    for source in sources:
        if source.is_file():
            if source.stat().st_size > MAX_BYTES:
                raise ValueError('Oversized artifact: '+str(source))
            destination = OUT/source.name
            shutil.copyfile(source, destination)
            copied.append({'repository_path': source.as_posix(), 'delivery_filename': destination.name})
    external = []
    for path in (Path('C:/Users/swami/Projects/gct-gpt/Batch14_Launch/B14-05_astra_prompt.md'),
                 Path('C:/Users/swami/Projects/gct-gpt/Batch14_Launch/packets/B14-05_packet.md')):
        external.append({'path': str(path), **describe(path)})
    packet = Path(external[1]['path']).read_bytes().replace(b'\r\n', b'\n')
    if packet != Path('docs/dispatch/B14-05_packet.md').read_bytes().replace(b'\r\n', b'\n'):
        raise ValueError('External and frozen tracked assignment packets disagree')
    changed = run(['git', 'diff', '--name-only', BASE, BRANCH]).splitlines()
    # The final branch may only contain intentional B14-05 files and the append-only index edit.
    if any(not (p.startswith(('analysis/b14_05_', 'results/b14_05/', 'results/logs/b14_05_',
                              'docs/b14_05_')) or p in ('results/PREREG_b14_05.md', 'docs/PROVED.md')) for p in changed):
        raise ValueError('Out-of-scope changed file')
    before = run(['git', 'show', BASE+':docs/PROVED.md'])
    after = Path('docs/PROVED.md').read_text(encoding='utf-8').strip()
    if not after.startswith(before):
        raise ValueError('PROVED.md was not append-only')
    # Remove no files. A clean output directory or repeat of this same package is expected.
    exclusions = {'delivery_manifest.json', 'MD5SUMS.txt', 'SHA256SUMS.txt',
                  bundle.name+'.md5', bundle.name+'.sha256', 'package_verification.json'}
    artifacts = [describe(p) for p in sorted(OUT.iterdir()) if p.is_file() and p.name not in exclusions]
    manifest = {'board_numbering': 'batch14', 'session_id': 'B14-05', 'actual_model': 'gpt-6-astra',
                'requested_reasoning_effort': 'xhigh; not independently introspected',
                'packaged_utc': datetime.now(timezone.utc).isoformat(),
                'branch': BRANCH, 'base_commit': BASE, 'base_tree': TREE,
                'head_commit': head, 'head_tree': tree, 'bundle_heads': heads.splitlines(),
                'bundle_prerequisites': prerequisites, 'part_count': len(parts),
                'part_size_ceiling_bytes': MAX_BYTES, 'bundle_and_parts': [describe(bundle)]+[describe(p) for p in parts],
                'verification': {'delivery_pre': 'CLEAN', 'delivery_post': 'CLEAN', 'git_bundle_verify': 'PASS',
                                 'named_ref': 'PASS', 'part_reconstruction': 'PASS', 'index_append_only': 'PASS',
                                 'external_packet_matches_frozen_packet': True, 'delivery_check_failures': []},
                'research_status': 'Substantive fallback complete: T/CI and mixed conventions proved; raw adjunction refuted; qualified operators proved and validated',
                'evidence_boundary': 'a24=274; determinant rank 273; padded rank >=269; D in [-4,+1]',
                'source_copy_map': copied, 'external_launch_inputs': external,
                'changed_repository_files': changed, 'artifacts': artifacts}
    (OUT/'delivery_manifest.json').write_text(json.dumps(manifest, indent=2)+'\n', encoding='utf-8')
    for algorithm, suffix in (('md5', '.md5'), ('sha256', '.sha256')):
        (OUT/(bundle.name+suffix)).write_text(''.join(digest(p, algorithm)+'  '+p.name+'\n' for p in [bundle]+parts), encoding='ascii')
    verification = {'status': 'PASS', 'head': head, 'artifact_hashes_checked': len(artifacts),
                    'source_worktree_clean': not bool(run(['git', 'status', '--porcelain'])),
                    'max_payload_bytes': max(a['bytes'] for a in artifacts),
                    'research_rejected_mutations': 36, 'full_target_interpolation_13_14': 'NOT PRODUCED'}
    for a in artifacts:
        p = OUT/a['filename']
        if any(digest(p, h) != a[h] for h in ('md5', 'sha256')):
            raise ValueError('Artifact checksum mismatch')
    if not verification['source_worktree_clean']:
        raise ValueError('Packaging modified source worktree')
    (OUT/'package_verification.json').write_text(json.dumps(verification, indent=2)+'\n', encoding='utf-8')
    checksum_sources = [p for p in sorted(OUT.iterdir()) if p.is_file() and p.name not in ('MD5SUMS.txt', 'SHA256SUMS.txt')]
    for algorithm, filename in (('md5', 'MD5SUMS.txt'), ('sha256', 'SHA256SUMS.txt')):
        (OUT/filename).write_text(''.join(digest(p, algorithm)+'  '+p.name+'\n' for p in checksum_sources), encoding='ascii')
        for line in (OUT/filename).read_text().splitlines():
            expected, name = line.split('  ', 1)
            if Path(name).name != name or digest(OUT/name, algorithm) != expected:
                raise ValueError('Sidecar verification failed')
    print(json.dumps({'status': 'PASS', 'output_directory': str(OUT), 'head': head,
                      'bundle_bytes': len(data), 'parts': len(parts), 'files_checksummed': len(checksum_sources)}, indent=2))


if __name__ == '__main__':
    main()
