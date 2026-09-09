"""One-process Windows runner: hard Job Object memory cap and wall watchdog."""
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
    info.basic.flags = 0x100  # JOB_OBJECT_LIMIT_PROCESS_MEMORY
    info.process_memory = megabytes * 1024**2
    if not kernel.SetInformationJobObject(job, 9, C.byref(info), C.sizeof(info)):
        raise C.WinError(C.get_last_error())
    if not kernel.AssignProcessToJobObject(job, kernel.GetCurrentProcess()):
        raise C.WinError(C.get_last_error())
    return job  # keep handle alive for this process


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds", type=int, default=600)
    parser.add_argument("--memory-mb", type=int, default=768)
    parser.add_argument("--name", required=True)
    parser.add_argument("script")
    parser.add_argument("args", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
                "NUMEXPR_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
        os.environ[key] = "1"
    before = memory()
    if before["available_physical"] < 2 * args.memory_mb * 1024**2:
        raise RuntimeError("Insufficient available RAM for conservative cap")
    job = cap_memory(args.memory_mb)
    logs = Path("results/logs")
    logs.mkdir(parents=True, exist_ok=True)
    (logs / (args.name + ".pid")).write_text(str(os.getpid()) + "\n")
    meta = {"board_numbering": "batch13", "session_id": "B13-03",
            "pid": os.getpid(), "memory_before": before,
            "memory_cap_mb": args.memory_mb, "wall_cap_seconds": args.seconds,
            "workers": 1, "blas_threads": 1, "job_object_enforced": bool(job),
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
    sys.path[:0] = [str(Path(".b13_03_deps").resolve()), str(Path("analysis").resolve())]
    sys.argv = [args.script] + args.args
    try:
        runpy.run_path(args.script, run_name="__main__")
    finally:
        timer.cancel()
        meta["wall_seconds"] = time.perf_counter() - start
        meta["memory_after"] = memory()
        meta_path.write_text(json.dumps(meta, indent=2) + "\n")
        print(json.dumps({"wall_seconds": meta["wall_seconds"]}), flush=True)


if __name__ == "__main__":
    main()
