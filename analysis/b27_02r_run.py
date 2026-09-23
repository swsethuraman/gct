"""R27-02 administrative runner: one sequential run of b27_02r_check.py with a 60 s wall cap and a
512 MiB Windows Job Object memory cap (argv: tag [script, default b27_02r_check.py]); records wall time, peak job memory and output hash."""
import ctypes as C
from ctypes import wintypes as W
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'results/b27_02r'
tag = sys.argv[1]
out_path = OUT / (tag + '_output.json')
assert not out_path.exists(), 'refuse to overwrite'

class Basic(C.Structure):
    _fields_ = [('a', C.c_longlong), ('b', C.c_longlong), ('flags', W.DWORD), ('mn', C.c_size_t),
                ('mx', C.c_size_t), ('act', W.DWORD), ('aff', C.c_size_t), ('pri', W.DWORD), ('sch', W.DWORD)]
class IO(C.Structure):
    _fields_ = [(n, C.c_ulonglong) for n in 'abcdef']
class Ext(C.Structure):
    _fields_ = [('basic', Basic), ('io', IO), ('proc_mem', C.c_size_t), ('job_mem', C.c_size_t),
                ('peak_proc', C.c_size_t), ('peak_job', C.c_size_t)]
k = C.WinDLL('kernel32', use_last_error=True)
k.CreateJobObjectW.restype = W.HANDLE
k.OpenProcess.restype = W.HANDLE
job = k.CreateJobObjectW(None, None)
info = Ext()
info.basic.flags = 0x100 | 0x200 | 0x2000  # process memory, job memory, kill on close
info.proc_mem = info.job_mem = 512 * 1024 ** 2
assert k.SetInformationJobObject(W.HANDLE(job), 9, C.byref(info), C.sizeof(info))

script = ROOT / 'analysis' / (sys.argv[2] if len(sys.argv) > 2 else 'b27_02r_check.py')
cmd = [sys.executable, str(script)]
started = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
t0 = time.perf_counter()
p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
h = k.OpenProcess(0x1F0FFF, False, p.pid)
assert k.AssignProcessToJobObject(W.HANDLE(job), W.HANDLE(h))
try:
    so, se = p.communicate(timeout=60)
except subprocess.TimeoutExpired:
    p.kill()
    so, se = p.communicate()
wall = time.perf_counter() - t0
q = Ext()
k.QueryInformationJobObject(W.HANDLE(job), 9, C.byref(q), C.sizeof(q), None)
out_path.write_bytes(so)
receipt = {'tag': tag, 'command': cmd, 'started_utc': started, 'wall_seconds': round(wall, 3),
           'exit_code': p.returncode, 'peak_job_bytes': q.peak_job, 'memory_cap_bytes': 512 * 1024 ** 2,
           'input_sha256': {script.relative_to(ROOT).as_posix(): hashlib.sha256(script.read_bytes()).hexdigest()},
           'output': {'path': out_path.relative_to(ROOT).as_posix(), 'bytes': len(so),
                      'sha256': hashlib.sha256(so).hexdigest()},
           'stderr': se.decode(errors='replace')}
(OUT / (tag + '_resources.json')).write_bytes((json.dumps(receipt, indent=2) + '\n').encode())
print(json.dumps(receipt, indent=2))
