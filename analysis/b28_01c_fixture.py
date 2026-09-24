#!/usr/bin/env python3
"""B28-01c control inputs: deterministic malformed certificates (copies; the
source directory is never modified).
  missing_minor      SRC DST P   : R28-01's control -- delete evaluation.minor_rows and minor_det_mod_p
  wrong_recipe       SRC DST P   : R28-01's control -- projection base_seed + 1 and attempt 3
                                   (effective pseed, m, extra and nproj unchanged)
  corrupt_candidate  SRC DST P   : deficiency fixture -- replace candidate 1 by K[:,0] and its
                                   combination by e_0, re-hash both files in the certificate
                                   (so the rejection must come from the mathematics, not a hash)
"""
import sys, os, json, glob, shutil, hashlib
import numpy as np


def sha(b):
    return hashlib.sha256(b).hexdigest()


def main():
    kind, src, dst, p = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])
    assert not os.path.exists(dst)
    shutil.copytree(src, dst)
    cf, = glob.glob(os.path.join(dst, f'*_p{p}_cert.json'))
    cert = json.load(open(cf))
    if kind == 'missing_minor':
        del cert['evaluation']['minor_rows']; del cert['evaluation']['minor_det_mod_p']
    elif kind == 'wrong_recipe':
        cert['hybrid']['projection']['base_seed'] += 1
        cert['hybrid']['projection']['attempt'] = 3
    elif kind == 'corrupt_candidate':
        n, a = cert['K']['shape']
        K = np.fromfile(os.path.join(dst, cert['K']['file']), dtype='<u4').reshape(n, a)
        cd = cert['candidates']
        C = np.fromfile(os.path.join(dst, cd['file']), dtype='<u4').reshape(cd['shape'])
        B = np.fromfile(os.path.join(dst, cd['combinations']['file']), dtype='<u4').reshape(cd['combinations']['shape'])
        assert C.shape[0] >= 2
        C[1] = K[:, 0]
        B[1] = 0; B[1, 0] = 1
        C.astype('<u4').tofile(os.path.join(dst, cd['file'])); B.astype('<u4').tofile(os.path.join(dst, cd['combinations']['file']))
        cd['sha256'] = sha(C.astype('<u4').tobytes()); cd['combinations']['sha256'] = sha(B.astype('<u4').tobytes())
    else:
        raise SystemExit('unknown kind')
    with open(cf, 'w') as f: json.dump(cert, f, indent=1, sort_keys=True)
    print(json.dumps(dict(kind=kind, cert=os.path.basename(cf), cert_sha256=sha(open(cf, 'rb').read()))))


if __name__ == '__main__':
    main()
