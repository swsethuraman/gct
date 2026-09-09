#!/usr/bin/env python3
"""
Session 79 -- certificate manifest and the shipping cut.

Every cell and weight of this session wrote gct-cert/1 files (hybrid_kernel
recorded certificates with the kernel in chi-coordinates, and full_rank
certificates with the basis expanded to canonical terms).  Together they are
~780 MB, far beyond the bundle transfer limit, so the tree ships only the files
at or below the size cut (default 150 KB) plus every calibration certificate;
the manifest lists ALL files with size and md5 so that a regenerated set can be
checked byte for byte.  Regeneration: the recorded commands in
results/s79_cells.jsonl / results/s79_per6.jsonl (seeds, primes, hybrid seed)
through analysis/wk12_s79_cell6.py and wk12_s79_per6.py.

usage: python3 analysis/wk12_s79_certs_manifest.py [--cut 150000] [--prune]
  --prune moves the files above the cut to /home/claude/s79_certs_big/ (outside the tree)
"""
import hashlib, json, os, shutil, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
DIRS = ('results/certs/s79_calib6', 'results/certs/s79_cells', 'results/certs/s79_per6')


def md5(path):
    h = hashlib.md5()
    with open(path, 'rb') as f:
        for blk in iter(lambda: f.read(1 << 20), b''): h.update(blk)
    return h.hexdigest()


def main(argv):
    cut = int(argv[argv.index('--cut') + 1]) if '--cut' in argv else 150000
    prune = '--prune' in argv
    keep_calib = '--cut-calib' not in argv
    big_dir = '/home/claude/s79_certs_big'
    man = dict(size_cut_bytes=cut, keep_all_in=(['results/certs/s79_calib6'] if keep_calib else []), files=[], shipped=0, shipped_bytes=0, total=0, total_bytes=0)
    for d in DIRS:
        dd = os.path.join(ROOT, d)
        if not os.path.isdir(dd): continue
        for fn in sorted(os.listdir(dd)):
            p = os.path.join(dd, fn); sz = os.path.getsize(p)
            ship = (keep_calib and d == 'results/certs/s79_calib6') or sz <= cut
            man['files'].append(dict(path=f'{d}/{fn}', bytes=sz, md5=md5(p), shipped=ship))
            man['total'] += 1; man['total_bytes'] += sz
            if ship: man['shipped'] += 1; man['shipped_bytes'] += sz
            elif prune:
                os.makedirs(os.path.join(big_dir, d), exist_ok=True)
                shutil.move(p, os.path.join(big_dir, d, fn))
    # files pruned on an earlier pass are listed from the big directory so the manifest stays complete
    for d in DIRS:
        dd = os.path.join(big_dir, d)
        if not os.path.isdir(dd): continue
        listed = {f['path'] for f in man['files']}
        for fn in sorted(os.listdir(dd)):
            if f'{d}/{fn}' in listed: continue
            p = os.path.join(dd, fn); sz = os.path.getsize(p)
            man['files'].append(dict(path=f'{d}/{fn}', bytes=sz, md5=md5(p), shipped=False))
            man['total'] += 1; man['total_bytes'] += sz
    man['files'].sort(key=lambda f: f['path'])
    with open(os.path.join(ROOT, 'results', 's79_cert_manifest.json'), 'w') as f:
        json.dump(man, f, indent=0)
    print(f"certificates: {man['total']} files, {man['total_bytes']/1e6:.1f} MB; shipped in the tree: {man['shipped']} files, {man['shipped_bytes']/1e6:.1f} MB (cut {cut} bytes; calib6 kept whole)")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
