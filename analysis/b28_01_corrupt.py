#!/usr/bin/env python3
"""B28-01 control inputs: deterministic single-entry corruptions.
  kernel  SRC DST P   : copy the uint32 kernel file, entry [0,0] -> (entry + 1) mod P
  pencil  SRC DST     : copy the pencils JSON, pencils[0][0][0][0] -> value + 1
"""
import sys, json
import numpy as np

kind, src, dst = sys.argv[1:4]
if kind == 'kernel':
    p = int(sys.argv[4])
    K = np.fromfile(src, dtype='<u4')
    K[0] = (int(K[0]) + 1) % p
    K.tofile(dst)
elif kind == 'pencil':
    d = json.load(open(src))
    d['pencils'][0][0][0][0] += 1
    json.dump(d, open(dst, 'w'), separators=(',', ':'))
else:
    raise SystemExit('unknown kind')
