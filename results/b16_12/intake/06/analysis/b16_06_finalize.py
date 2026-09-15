"""Record actual inputs, resources and local delivery; no Git or subprocesses."""
from pathlib import Path
import ctypes
import hashlib
import json
import sys
import sympy
import flint

ROOT=Path(__file__).resolve().parents[1]
PROJECT=ROOT.parents[2]
OUT=ROOT/'results/b16_06';DEL=ROOT/'delivery/b16_06'

def record(p):
    b=p.read_bytes()
    return dict(path=str(p.resolve()),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())

def main():
    OUT.mkdir(exist_ok=True);DEL.mkdir(exist_ok=True)
    paths=[PROJECT/p for p in ['Batch16/BOARD.md','Batch16/launch/INPUT_MANIFEST.json',
        'Batch16/launch/B16-06.md','Batch16/launch/runtime_06.json',
        'Batch15_Launch/native_20260913/INTAKE.json']]
    h=PROJECT/'Batch15_Launch/native_20260913/reviews_filesystem/Hessian11_1631'
    paths += [h/p for p in ['REPORT.md','input_receipt.json','integrator_review.json','verify_small.py']]
    ast=PROJECT/'Batch15_Launch/native_20260913/equation_review/astra'
    paths += [ast/p for p in ['REVIEW.md','hessian_relations.py']]
    paths += [ROOT/p for p in ['analysis/b15_bound.py','analysis/b15_06_census.py',
        'analysis/b13_06_decompose.py','docs/b13_06_report.md','docs/b14_06_report.md',
        'docs/b14_06_review.md','docs/b15_06_proved.md','.venv/python.exe']]
    paths += [ROOT.parent/'B15-07'/p for p in ['docs/b15_07_report.md','analysis/b15_07_next.py']]
    # Hash the imported package entry points; record versions rather than claiming
    # every transitive third-party library file is included in a standalone bundle.
    paths += [Path(sympy.__file__),Path(flint.__file__)]
    hashes=[record(p) for p in paths]
    launch=json.loads((PROJECT/'Batch16/launch/INPUT_MANIFEST.json').read_text())
    expected={str(Path(x['path']).resolve()).lower():x['sha256'] for x in launch['inputs']}
    for item in hashes:
        if item['path'].lower() in expected:assert item['sha256']==expected[item['path'].lower()]
    (OUT/'input_hashes.json').write_text(json.dumps(dict(status='EXACT_LOCAL_FILE_HASHES',inputs=hashes,
        runtime=dict(python=sys.executable,python_version=sys.version,sympy=sympy.__version__,flint=flint.__version__),
        external_reference=dict(url='https://arxiv.org/pdf/1004.4802',version='v1',
            sections='2.2-2.3',retrieval='web tool; no local byte hash claimed'),
        frozen_head_inherited='41e03e172e32a8efc1803c7207a244ca95966b04',
        git_binding='NOT_FRESHLY_CHECKED_NO_GIT_OPERATION'),indent=2)+'\n')
    resources=[]
    kernel=ctypes.WinDLL('kernel32',use_last_error=True)
    kernel.OpenProcess.restype=ctypes.c_void_p
    kernel.OpenProcess.argtypes=[ctypes.c_ulong,ctypes.c_int,ctypes.c_ulong]
    kernel.GetExitCodeProcess.argtypes=[ctypes.c_void_p,ctypes.POINTER(ctypes.c_ulong)]
    kernel.CloseHandle.argtypes=[ctypes.c_void_p]
    for p in sorted((ROOT/'results/logs').glob('b16_06_*_resources.json')):
        if 'runtime' in p.name or 'finalize' in p.name:continue
        d=json.loads(p.read_text());assert d.get('exit_code')==0
        assert d['wall_cap_seconds']<=60 and d['memory_cap_mb']<=512
        assert d['job_object_enforced'] and d['workers']==d['blas_threads']==1
        handle=kernel.OpenProcess(0x1000,False,d['pid'])
        if handle:
            code=ctypes.c_ulong();ok=kernel.GetExitCodeProcess(handle,ctypes.byref(code));kernel.CloseHandle(handle)
            assert ok and code.value!=259
            state=dict(state='EXITED',code=code.value)
        else:
            err=ctypes.get_last_error();assert err==87,(d['pid'],err)
            state=dict(state='PID_ABSENT',winerror=err)
        resources.append(dict(receipt=record(p),pid=d['pid'],process=state,
            seconds=d['wall_seconds'],peak_job_memory=d['job_memory']['peak_job_memory'],exit_code=0))
    (OUT/'resource_summary.json').write_text(json.dumps(dict(status='ALL_SMALL_RUNS_EXITED',runs=resources,
        heavy_lease='NEVER_REQUESTED_OR_HELD; NONE TO RELEASE',processes_remaining=0,
        cap='60 seconds / 512 MiB, one process and BLAS thread',
        maximum_seconds=max(x['seconds'] for x in resources),
        maximum_peak_job_memory=max(x['peak_job_memory'] for x in resources)),indent=2)+'\n')
    (OUT/'coordination.json').write_text(json.dumps(dict(action='interim message to source integrator task',
        status='AUTO_REVIEW_REJECTED_NOT_RETRIED',reason='Potential internal research disclosure under no-publication constraint; authorization to disclose was not recognized.',
        research_files_unaffected=True),indent=2)+'\n')
    files=list((ROOT/'analysis').glob('b16_06*.py'))+list((ROOT/'docs').glob('b16_06*.md'))+list(OUT.glob('*.json'))
    files += [Path(x['receipt']['path']) for x in resources]
    manifest=dict(status='LOCAL_FILESYSTEM_DELIVERY_NOT_GIT_BOUND',slot='06',
        owned_worktree=str(ROOT),artifacts=[record(p) for p in sorted(files)],
        receiver='analysis/b16_06_receiver.py --verify',bounded_command='.venv/python.exe -B analysis/b15_bound.py --slot 06 --name b16_06_receive --seconds 60 --memory-mb 512 analysis/b16_06_receiver.py --verify',
        claims=dict(image_ranks_tail17_d25_d26=[1,2],finite_determinant_floors_d25_d26_d27=[3,4,7],
                    full_J24_image=False,positive_gap=False),
        preserved='All B15 evidence and shared files; writes only owned B16 paths.')
    (DEL/'MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',input_hashes=len(hashes),artifacts=len(files),
                         runs=len(resources),processes_remaining=0,heavy_lease='NONE')))

if __name__=='__main__':main()
