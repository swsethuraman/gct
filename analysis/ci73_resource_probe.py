"""Intentional resource failures; a successful probe has a nonzero exit."""
import json,sys,time
from pathlib import Path

mode=sys.argv[1]
if mode=='memory':
    try:value=bytearray(128*1024**2)
    except MemoryError:
        print(json.dumps(dict(status='EXPECTED_MEMORY_REJECTION')),flush=True)
        raise SystemExit(77)
    raise RuntimeError('memory cap did not reject 128 MiB allocation')
elif mode=='backend_timeout':
    sys.path.insert(0,str(Path('tools/verify').resolve()))
    import ci73_eval as ev,ci73_io as io
    s=io.load(Path('results/ci73/inputs/source.json'));pts=io.load(Path('results/ci73/inputs/points.json'))
    symbols=[{4:ev.quartic_symbols(pts['points'][0],pts['cubic_exponents'])}]
    try:ev.evaluate(ev.native_source(s['entries'][15]),symbols,name='ci73_timeout_probe',seconds=0.000001)
    except RuntimeError as exc:
        if 'backend deadline, recorded pid' not in str(exc):raise
        print(json.dumps(dict(status='EXPECTED_BACKEND_TIMEOUT',detail=str(exc))),flush=True)
        raise SystemExit(78)
    raise RuntimeError('backend deadline did not fire')
elif mode=='wall':
    time.sleep(4)
    raise RuntimeError('one-second wall cap did not fire')
else:raise RuntimeError('unknown probe')
