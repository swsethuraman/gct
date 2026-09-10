"""Single-process Windows hard memory bound and wall watchdog for B13-06."""
import argparse
import ctypes as C
from ctypes import wintypes as W
import datetime as dt
import json
import os
from pathlib import Path
import runpy
import sys
import threading
import time


class Basic(C.Structure):
    _fields_ = [('PerProcessUserTimeLimit', C.c_int64), ('PerJobUserTimeLimit', C.c_int64),
                ('LimitFlags', W.DWORD), ('MinimumWorkingSetSize', C.c_size_t),
                ('MaximumWorkingSetSize', C.c_size_t), ('ActiveProcessLimit', W.DWORD),
                ('Affinity', C.c_size_t), ('PriorityClass', W.DWORD),
                ('SchedulingClass', W.DWORD)]


class IO(C.Structure):
    _fields_ = [(x, C.c_uint64) for x in ('ReadOperationCount', 'WriteOperationCount',
                'OtherOperationCount', 'ReadTransferCount', 'WriteTransferCount',
                'OtherTransferCount')]


class Extended(C.Structure):
    _fields_ = [('BasicLimitInformation', Basic), ('IoInfo', IO),
                ('ProcessMemoryLimit', C.c_size_t), ('JobMemoryLimit', C.c_size_t),
                ('PeakProcessMemoryUsed', C.c_size_t), ('PeakJobMemoryUsed', C.c_size_t)]


class Memory(C.Structure):
    _fields_ = [('length', W.DWORD), ('load', W.DWORD)] + [
        (n, C.c_uint64) for n in ('total_phys', 'avail_phys', 'total_page', 'avail_page',
                               'total_virtual', 'avail_virtual', 'avail_extended')]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--name', required=True)
    ap.add_argument('--seconds', type=int, required=True)
    ap.add_argument('--mib', type=int, default=768)
    ap.add_argument('command', nargs=argparse.REMAINDER)
    args = ap.parse_args()
    assert 0 < args.seconds <= 1200 and 0 < args.mib <= 768
    command = args.command[1:] if args.command[0] == '--' else args.command
    for var in ('OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS', 'OMP_NUM_THREADS',
                'NUMEXPR_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS'):
        os.environ[var] = '1'
    assert os.name == 'nt', 'Use an equivalent native bound on other platforms.'
    k = C.WinDLL('kernel32', use_last_error=True)
    k.CreateJobObjectW.argtypes = [C.c_void_p, W.LPCWSTR]
    k.CreateJobObjectW.restype = W.HANDLE
    k.GetCurrentProcess.restype = W.HANDLE
    k.SetInformationJobObject.argtypes = [W.HANDLE, C.c_int, C.c_void_p, W.DWORD]
    k.AssignProcessToJobObject.argtypes = [W.HANDLE, W.HANDLE]
    k.QueryInformationJobObject.argtypes = [W.HANDLE, C.c_int, C.c_void_p, W.DWORD, C.c_void_p]
    job = k.CreateJobObjectW(None, None)
    info = Extended()
    info.BasicLimitInformation.LimitFlags = 0x100 | 0x2000  # process memory, close cleanup
    info.ProcessMemoryLimit = args.mib * 2**20
    if not job or not k.SetInformationJobObject(job, 9, C.byref(info), C.sizeof(info)):
        raise C.WinError(C.get_last_error())
    if not k.AssignProcessToJobObject(job, k.GetCurrentProcess()):
        raise C.WinError(C.get_last_error())
    mem = Memory(); mem.length = C.sizeof(mem)
    if not k.GlobalMemoryStatusEx(C.byref(mem)):
        raise C.WinError(C.get_last_error())
    log = Path('results/logs') / ('b13_06_' + args.name)
    log.parent.mkdir(parents=True, exist_ok=True)
    log.with_suffix('.pid').write_text(str(os.getpid()) + '\n')
    record = dict(board_numbering='batch13', session_id='B13-06', pid=os.getpid(),
                  start_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
                  wall_limit_seconds=args.seconds, memory_limit_bytes=info.ProcessMemoryLimit,
                  available_physical_bytes=mem.avail_phys, total_physical_bytes=mem.total_phys,
                  worker_count=1, blas_threads=1, command=command)
    start = time.monotonic()
    def save(status):
        k.QueryInformationJobObject(job, 9, C.byref(info), C.sizeof(info), None)
        record.update(status=status, wall_seconds=time.monotonic() - start,
                      peak_process_memory_bytes=info.PeakProcessMemoryUsed)
        log.with_suffix('.resources.json').write_text(json.dumps(record, indent=2) + '\n')
    def expired():
        save('wall_limit_reached')
        os._exit(124)
    timer = threading.Timer(args.seconds, expired); timer.daemon = True; timer.start()
    save('running')
    print(json.dumps(record), flush=True)
    sys.argv = command
    sys.path.insert(0, str(Path(command[0]).resolve().parent))
    dep = Path('.b13_06_deps')
    if dep.exists(): sys.path.insert(0, str(dep.resolve()))
    try:
        runpy.run_path(command[0], run_name='__main__')
    except BaseException:
        save('exception'); raise
    else:
        save('completed')
    finally:
        timer.cancel()
    print(json.dumps(record), flush=True)


if __name__ == '__main__':
    main()
