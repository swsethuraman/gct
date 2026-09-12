"""Intentionally exceed a tiny resource budget to test the supervisor."""
import sys
import time

if sys.argv[1] == "memory":
    allocation = bytearray(128 * 1024 * 1024)
    raise RuntimeError("128 MiB allocation incorrectly passed a 64 MiB process cap")
elif sys.argv[1] == "wall":
    time.sleep(3)
    raise RuntimeError("three-second wait incorrectly passed a subsecond wall cap")
else:
    raise ValueError("unknown resource probe")
