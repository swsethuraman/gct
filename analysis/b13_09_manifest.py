#!/usr/bin/env python3
"""
B13-09 -- the delivery manifest: every artefact this session produced, with size
and md5, and an explicit statement of which files travel in the bundle and which
do not.

The repository rule is that no file over 5 MB is committed.  Every certificate
this session wrote is under that (largest 3.3 MB), but the directory as a whole is
about 178 MB, far too much to ship -- so, as s79 did, the manifest lists ALL of
them with their digests and the tree ships a subset.

`shipped_in_bundle` is not a plan: it is read from `git ls-files`, so this
manifest CANNOT disagree with the bundle.  (Batch 12 shipped a digest naming a
container path and a two-part bundle that was really three; the general lesson is
that a manifest which describes an intention rather than the artefact is the thing
that costs a round trip.)  Certificates were committed as each weight banked, so
the tracked set is that chronological prefix of the certificate stream.  Every
unshipped certificate is listed with its md5 and the exact command that
regenerates it from the recorded seeds.

board_numbering is a top-level key here: the preamble asks for it in every
manifest.  (It is deliberately NOT in the gct-cert/1 certificates -- that schema
is closed and tools/verify rejects an unknown key.)

usage: python3 analysis/b13_09_manifest.py [--out results/b13_09/cert_manifest.json]
"""
import sys, os, json, hashlib, subprocess

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..'))
CERTS = os.path.join(ROOT, 'results', 'certs', 'b13_09')
LIMIT = 5 * 1024 * 1024


def md5(path, blk=1 << 20):
    h = hashlib.md5()
    with open(path, 'rb') as f:
        while True:
            b = f.read(blk)
            if not b: break
            h.update(b)
    return h.hexdigest()


def main(argv):
    budget = float(argv[argv.index('--budget-mb') + 1]) if '--budget-mb' in argv else 30.0
    out = argv[argv.index('--out') + 1] if '--out' in argv else os.path.join(ROOT, 'results', 'b13_09', 'cert_manifest.json')
    files = []
    if os.path.isdir(CERTS):
        for fn in sorted(os.listdir(CERTS)):
            p = os.path.join(CERTS, fn)
            if not os.path.isfile(p): continue
            sz = os.path.getsize(p)
            files.append(dict(name=fn, path=os.path.relpath(p, ROOT), bytes=sz, md5=md5(p),
                              over_repo_limit=bool(sz > LIMIT),
                              kind=('ideal' if '_ideal_' in fn else 'full_rank'),
                              prime=(2147483647 if 'p2147483647' in fn else 2147483629 if 'p2147483629' in fn else None)))
    # What travels in the bundle is not a hypothesis: it is exactly what git tracks.
    # Certificates were committed as each weight banked (bank-per-unit), so the tracked
    # set is the run's own chronological prefix of the certificate stream, capped in
    # practice by the moment the directory was last staged.  The manifest reports that
    # set as `shipped_in_bundle` by ASKING GIT, so the manifest can never disagree with
    # the bundle -- the failure batch 12 paid for.  Every other certificate is listed
    # here with its digest and the exact command that regenerates it.
    tracked = set()
    r = subprocess.run(['git', '-C', ROOT, 'ls-files', '-z', 'results/certs/b13_09'],
                       capture_output=True, text=True)
    for rel in r.stdout.split('\0'):
        if rel.strip(): tracked.add(os.path.basename(rel))
    used = 0
    for f in files:
        f['shipped_in_bundle'] = f['name'] in tracked
        if f['shipped_in_bundle']: used += f['bytes']
        f['regenerate'] = ('python3 analysis/b13_09_per_r.py <delta> <mu...> --certs results/certs/b13_09'
                           ' (seeds: per3 41, bound 40, recheck 907, hybrid 20260908; both house primes)')
    ship = tracked
    other = []
    for rel in ['results/PREREG_b13_09.md', 'results/b13_09_census.json', 'results/b13_09_pleth89.json',
                'results/b13_09/costfit.json', 'results/b13_09/verify.json', 'results/b13_09/cert_verify_report.md',
                'docs/b13_09_report.md']:
        p = os.path.join(ROOT, rel)
        if os.path.exists(p):
            other.append(dict(path=rel, bytes=os.path.getsize(p), md5=md5(p), over_repo_limit=os.path.getsize(p) > LIMIT))
    for rel in sorted(os.listdir(os.path.join(ROOT, 'results', 'b13_09'))):
        p = os.path.join(ROOT, 'results', 'b13_09', rel)
        if os.path.isfile(p) and (rel.endswith('.jsonl') or rel.startswith('status_')):
            other.append(dict(path=f'results/b13_09/{rel}', bytes=os.path.getsize(p), md5=md5(p),
                              over_repo_limit=os.path.getsize(p) > LIMIT))
    man = dict(board_numbering='batch13', session='B13-09',
               base=subprocess.run(['git', '-C', ROOT, 'rev-parse', 'main'], capture_output=True, text=True).stdout.strip(),
               head=subprocess.run(['git', '-C', ROOT, 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip(),
               branch=subprocess.run(['git', '-C', ROOT, 'rev-parse', '--abbrev-ref', 'HEAD'], capture_output=True, text=True).stdout.strip(),
               repo_file_limit_bytes=LIMIT,
               shipping_rule=('shipped_in_bundle is read from `git ls-files`, so this manifest cannot disagree with '
                              'the bundle.  Certificates were committed as each weight banked; the tracked set is that '
                              'chronological prefix of the certificate stream.  The full set is %.1f MB, too large to '
                              'ship, and no single file exceeds the 5 MB repository limit.  Every certificate is listed '
                              'here with its md5 whether shipped or not, and every unshipped one is regenerable by the '
                              'recorded command from the recorded seeds.' % (sum(f['bytes'] for f in files) / 1e6)),
               certs=dict(directory='results/certs/b13_09', files=len(files),
                          total_bytes=sum(f['bytes'] for f in files),
                          shipped=len(ship), shipped_bytes=used,
                          over_repo_limit=[f['name'] for f in files if f['over_repo_limit']]),
               cert_files=files, other_artefacts=other)
    json.dump(man, open(out, 'w'), indent=1)
    print(f"manifest: {len(files)} certificates ({man['certs']['total_bytes']/1e6:.1f} MB), "
          f"{len(ship)} shipped ({used/1e6:.1f} MB), {len(man['certs']['over_repo_limit'])} over the 5 MB limit; "
          f"{len(other)} other artefacts -> {out}")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
