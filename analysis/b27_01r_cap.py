"""R27-01 run harness: Windows Job Object memory cap (512,000,000 bytes), 60 s wall
watchdog, and a JSON run receipt with input and output hashes.  No mathematics here."""
import ctypes as C
from ctypes import wintypes as W
import hashlib
import json
import os
import subprocess
from pathlib import Path
import sys
import threading
import time

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'results/b27_01r'
LIMIT = 512_000_000
TIP = '01f78eb2a585599378727253e1906b8314f2adb2'


def blob(path):
    """Committed bytes of the producer tip; 'TIP:' prefixed inputs are read this way."""
    return subprocess.run(['git', '-C', str(ROOT), 'show', TIP + ':' + path],
                          capture_output=True, check=True).stdout


def sha(data):
    return hashlib.sha256(data).hexdigest()


def _job():
    class Basic(C.Structure):
        _fields_ = [('a', C.c_longlong), ('b', C.c_longlong), ('flags', W.DWORD),
                    ('mn', C.c_size_t), ('mx', C.c_size_t), ('act', W.DWORD),
                    ('aff', C.c_size_t), ('pri', W.DWORD), ('sch', W.DWORD)]

    class IO(C.Structure):
        _fields_ = [(n, C.c_ulonglong) for n in ('r', 'w', 'o', 'rb', 'wb', 'ob')]

    class Ext(C.Structure):
        _fields_ = [('basic', Basic), ('io', IO), ('pm', C.c_size_t), ('jm', C.c_size_t),
                    ('peak_process', C.c_size_t), ('peak_job', C.c_size_t)]
    k = C.WinDLL('kernel32', use_last_error=True)
    k.CreateJobObjectW.restype = W.HANDLE
    k.CreateJobObjectW.argtypes = [C.c_void_p, W.LPCWSTR]
    k.SetInformationJobObject.argtypes = [W.HANDLE, C.c_int, C.c_void_p, W.DWORD]
    k.QueryInformationJobObject.argtypes = [W.HANDLE, C.c_int, C.c_void_p, W.DWORD, C.c_void_p]
    k.GetCurrentProcess.restype = W.HANDLE
    k.AssignProcessToJobObject.argtypes = [W.HANDLE, W.HANDLE]
    job = k.CreateJobObjectW(None, None)
    info = Ext()
    info.basic.flags = 0x100 | 0x200 | 0x2000
    info.pm = info.jm = LIMIT
    assert k.SetInformationJobObject(job, 9, C.byref(info), C.sizeof(info))
    assert k.AssignProcessToJobObject(job, k.GetCurrentProcess())

    def stats():
        f = Ext()
        assert k.QueryInformationJobObject(job, 9, C.byref(f), C.sizeof(f), None)
        return {'peak_job_memory_bytes': f.peak_job}
    return stats


def run(number, script, body, inputs, outputs):
    """body() returns a JSON-able result dict; it is written to outputs[0]."""
    OUT.mkdir(parents=True, exist_ok=True)
    stats = _job()
    t0 = time.perf_counter()
    rec = dict(run=number, started_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
               command=['python', '-B', 'analysis/' + Path(script).name],
               interpreter_sha256=sha(Path(sys.executable).read_bytes()),
               inputs=[dict(path=p, sha256=sha(blob(p[4:]) if p.startswith('TIP:') else (ROOT / p).read_bytes()))
                       for p in inputs],
               seconds_limit=60, memory_limit_bytes=LIMIT, outcome='RUNNING')
    rpath = OUT / f'RUN_{number:02d}_RECEIPT.json'

    def dump(p, d):
        p.write_bytes((json.dumps(d, indent=2) + '\n').encode())

    def timeout():
        rec.update(outcome='TIMEOUT', wall_seconds=time.perf_counter() - t0)
        dump(rpath, rec)
        os._exit(124)
    timer = threading.Timer(60, timeout)
    timer.daemon = True
    timer.start()
    try:
        result = body()
        dump(OUT / outputs[0], result)
        rec['outcome'] = result.get('status', 'DONE')
    except BaseException as e:
        rec['outcome'] = 'FAIL: ' + repr(e)
        raise
    finally:
        timer.cancel()
        rec['wall_seconds'] = round(time.perf_counter() - t0, 3)
        rec.update(stats())
        rec['outputs'] = [dict(path='results/b27_01r/' + o, sha256=sha((OUT / o).read_bytes()))
                          for o in outputs if (OUT / o).exists()]
        dump(rpath, rec)
        print(json.dumps({k: rec[k] for k in ('outcome', 'wall_seconds', 'peak_job_memory_bytes')}))
