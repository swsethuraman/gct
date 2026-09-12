#!/usr/bin/env python3
"""wk13_b10_lean.raising_rows_lean must not remove a scratch directory it was handed.

    python3 tools/verify/scratch_not_removed.py

B14-12 lost a completed 47-minute build to the old behaviour: a blocks='disk' run
ended with shutil.rmtree(scratch) on the directory the CALLER passed, so anything
else the caller kept there went with it.  This test runs a small cell both ways and
requires all four things:

  1  a caller-owned scratch directory still exists after the run
  2  a caller's own file in it is untouched
  3  the builder's own block_*.npz files ARE gone (it still cleans up after itself)
  4  scratch=None still removes the temporary directory the builder created

It must be able to fail: run with --show-old to apply the old one-line behaviour to
a copy of the module and watch checks 1-3 fail.
"""
import os, sys, glob, shutil, tempfile, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'analysis'))

LAM, DELTA, N = (13, 5, 2, 2, 2), 6, 4          # B13-10's A1: 0.3 s, 61 MB


def load(old=False):
    src = open(os.path.join(ROOT, 'analysis', 'wk13_b10_lean.py')).read()
    if old:
        src = src.replace("    if blocks == 'disk':\n        for _b in out_blocks:\n"
                          "            try: os.remove(_b[0])\n            except OSError: pass\n",
                          "")
        src = src.replace("if blocks == 'disk' and scratch_is_ours:",
                          "if blocks == 'disk':")
    path = os.path.join(tempfile.mkdtemp(), 'lean_under_test.py')
    open(path, 'w').write(src)
    spec = importlib.util.spec_from_file_location('lean_under_test', path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


def run(old=False):
    lean = load(old)
    fails = []
    scratch = tempfile.mkdtemp(prefix='caller_owned_')
    keep = os.path.join(scratch, 'the_callers_own_file.txt')
    open(keep, 'w').write('47 minutes of build\n')
    E, nfixed, phases = lean.build_cell_lean(LAM, DELTA, n=N, verbose=False,
                                             blocks='disk', scratch=scratch)['E'], None, None
    if not os.path.isdir(scratch):
        fails.append('1  the caller-owned scratch directory was removed')
    elif not os.path.exists(keep):
        fails.append("2  the caller's own file in it was removed")
    elif open(keep).read() != '47 minutes of build\n':
        fails.append("2  the caller's own file was altered")
    left = glob.glob(os.path.join(scratch, 'block_*.npz')) if os.path.isdir(scratch) else []
    if left:
        fails.append(f'3  the builder left its own blocks behind: {len(left)}')
    shutil.rmtree(scratch, ignore_errors=True)

    before = set(glob.glob(os.path.join(tempfile.gettempdir(), 'b13_10_rows_*')))
    lean.build_cell_lean(LAM, DELTA, n=N, verbose=False, blocks='disk', scratch=None)
    after = set(glob.glob(os.path.join(tempfile.gettempdir(), 'b13_10_rows_*')))
    if after - before:
        fails.append('4  scratch=None left its own temporary directory behind')
    return fails


def main(argv):
    if '--show-old' in argv:
        fails = run(old=True)
        print('OLD behaviour, applied to a copy of the module:')
        for f in fails: print('  fails ' + f)
        print('  the old line fails %d of the four checks -- the test can fail' % len(fails))
        if not fails:
            print('THE TEST CANNOT FAIL -- fix the test'); return 1
        return 0
    fails = run()
    for f in fails: print('  FAIL ' + f)
    print('SCRATCH TEST ' + ('PASS' if not fails else 'FAIL'))
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
