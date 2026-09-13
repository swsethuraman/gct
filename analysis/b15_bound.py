"""Batch 15 Windows runner: aggregate Job Object memory and recorded deadlines."""
import argparse
import ctypes as C
from ctypes import wintypes as W
import json
import os
from pathlib import Path
import runpy
import sys
import threading
import time


class MemoryStatus(C.Structure):
    _fields_ = [("length", W.DWORD), ("load", W.DWORD)] + [
        (name, C.c_ulonglong) for name in
        ("total_physical", "available_physical", "total_page", "available_page",
         "total_virtual", "available_virtual", "available_extended")]


def memory():
    m = MemoryStatus()
    m.length = C.sizeof(m)
    if not C.windll.kernel32.GlobalMemoryStatusEx(C.byref(m)):
        raise C.WinError()
    return {key: getattr(m, key) for key in
            ("total_physical", "available_physical", "load")}


def cap_memory(megabytes):
    class Basic(C.Structure):
        _fields_ = [("process_time", C.c_longlong), ("job_time", C.c_longlong),
                    ("flags", W.DWORD), ("minimum", C.c_size_t),
                    ("maximum", C.c_size_t), ("active", W.DWORD),
                    ("affinity", C.c_size_t), ("priority", W.DWORD),
                    ("scheduling", W.DWORD)]
    class IO(C.Structure):
        _fields_ = [(name, C.c_ulonglong) for name in
                    ("read_ops", "write_ops", "other_ops", "read_bytes",
                     "write_bytes", "other_bytes")]
    class Extended(C.Structure):
        _fields_ = [("basic", Basic), ("io", IO),
                    ("process_memory", C.c_size_t), ("job_memory", C.c_size_t),
                    ("peak_process", C.c_size_t), ("peak_job", C.c_size_t)]
    kernel = C.WinDLL("kernel32", use_last_error=True)
    kernel.CreateJobObjectW.restype = W.HANDLE
    kernel.CreateJobObjectW.argtypes = [C.c_void_p, W.LPCWSTR]
    kernel.SetInformationJobObject.argtypes = [W.HANDLE, C.c_int, C.c_void_p, W.DWORD]
    kernel.GetCurrentProcess.restype = W.HANDLE
    kernel.AssignProcessToJobObject.argtypes = [W.HANDLE, W.HANDLE]
    job = kernel.CreateJobObjectW(None, None)
    if not job:
        raise C.WinError(C.get_last_error())
    info = Extended()
    info.basic.flags = 0x100 | 0x200 | 0x2000  # process/job memory and kill on close
    info.process_memory = megabytes * 1024**2
    info.job_memory = megabytes * 1024**2
    if not kernel.SetInformationJobObject(job, 9, C.byref(info), C.sizeof(info)):
        raise C.WinError(C.get_last_error())
    if not kernel.AssignProcessToJobObject(job, kernel.GetCurrentProcess()):
        raise C.WinError(C.get_last_error())
    def statistics():
        final=Extended()
        kernel.QueryInformationJobObject.argtypes=[W.HANDLE,C.c_int,C.c_void_p,W.DWORD,C.c_void_p]
        if not kernel.QueryInformationJobObject(job,9,C.byref(final),C.sizeof(final),None):
            raise C.WinError(C.get_last_error())
        return dict(peak_job_memory=final.peak_job,peak_process_memory=final.peak_process)
    return job,statistics  # keep handle alive for this process


def process_memory():
    class Counters(C.Structure):
        _fields_ = [("cb", W.DWORD), ("faults", W.DWORD)] + [
            (name, C.c_size_t) for name in
            ("peak_working_set", "working_set", "peak_paged_pool", "paged_pool",
             "peak_nonpaged_pool", "nonpaged_pool", "pagefile", "peak_pagefile")]
    value = Counters()
    value.cb = C.sizeof(value)
    kernel = C.windll.kernel32
    kernel.GetCurrentProcess.restype = W.HANDLE
    psapi = C.windll.psapi
    psapi.GetProcessMemoryInfo.argtypes = [W.HANDLE, C.c_void_p, W.DWORD]
    if not psapi.GetProcessMemoryInfo(kernel.GetCurrentProcess(), C.byref(value), value.cb):
        raise C.WinError()
    return {key: getattr(value, key) for key in
            ("peak_working_set", "working_set", "peak_pagefile")}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds", type=int, default=600)
    parser.add_argument("--memory-mb", type=int, default=768)
    parser.add_argument("--name", required=True)
    parser.add_argument("--slot", required=True)
    parser.add_argument("script")
    parser.add_argument("args", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
                "NUMEXPR_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
        os.environ[key] = "1"
    before = memory()
    if before["available_physical"] < 2 * args.memory_mb * 1024**2:
        raise RuntimeError("Insufficient available RAM for conservative cap")
    job,job_statistics = cap_memory(args.memory_mb)
    # Hold an idle-sleep request only while this bounded calculation is active.
    # Manual sleep is still possible; deadline checks reject an overrun on wake.
    awake=C.windll.kernel32.SetThreadExecutionState(0x80000001)
    if not awake:raise C.WinError()
    logs = Path("results/logs")
    logs.mkdir(parents=True, exist_ok=True)
    (logs / (args.name + ".pid")).write_text(str(os.getpid()) + "\n")
    meta = {"board_numbering": "batch15", "session_id": "B15-" + args.slot,
            "pid": os.getpid(), "memory_before": before,
            "memory_cap_mb": args.memory_mb, "wall_cap_seconds": args.seconds,
            "workers": 1, "blas_threads": 1, "job_object_enforced": bool(job),
            "idle_sleep_inhibited_during_run":True,
            "started_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    meta_path = logs / (args.name + "_resources.json")
    meta_path.write_text(json.dumps(meta, indent=2) + "\n")
    print(json.dumps(meta), flush=True)
    def deadline():
        print("WALL LIMIT REACHED", flush=True)
        os._exit(124)
    timer = threading.Timer(args.seconds, deadline)
    timer.daemon = True
    timer.start()
    start = time.perf_counter()
    os.environ['CI73_DEADLINE']=str(time.monotonic()+args.seconds)
    sys.path[:0] = [str(Path("analysis").resolve())]
    sys.argv = [args.script] + args.args
    meta['exit_code']=0
    try:
        runpy.run_path(args.script, run_name="__main__")
    except SystemExit as exc:
        meta['exit_code']=exc.code if isinstance(exc.code,int) else (0 if exc.code is None else 1)
        raise
    except BaseException:
        meta['exit_code']=1
        raise
    finally:
        timer.cancel()
        meta["wall_seconds"] = time.perf_counter() - start
        overrun=meta['wall_seconds']>args.seconds
        if overrun:meta['exit_code']=124
        meta["memory_after"] = memory()
        meta["process_memory"] = process_memory()
        meta['job_memory']=job_statistics()
        meta_path.write_text(json.dumps(meta, indent=2) + "\n")
        print(json.dumps({"wall_seconds": meta["wall_seconds"]}), flush=True)
        C.windll.kernel32.SetThreadExecutionState(0x80000000)
        if overrun:raise SystemExit(124)


if __name__ == "__main__":
    main()
