"""Run 03: exact verification/correction of recorded pricing formulae, no rank or build."""
import ctypes, datetime, hashlib, json, math, os, pathlib, sys, threading, time
from ctypes import wintypes
from decimal import Decimal, localcontext
from fractions import Fraction as Q
OUT=pathlib.Path(__file__).resolve().parent
START=time.perf_counter()
class Basic(ctypes.Structure):
    _fields_=[('PerProcessUserTimeLimit',ctypes.c_int64),('PerJobUserTimeLimit',ctypes.c_int64),('LimitFlags',wintypes.DWORD),('MinimumWorkingSetSize',ctypes.c_size_t),('MaximumWorkingSetSize',ctypes.c_size_t),('ActiveProcessLimit',wintypes.DWORD),('Affinity',ctypes.c_size_t),('PriorityClass',wintypes.DWORD),('SchedulingClass',wintypes.DWORD)]
class IO(ctypes.Structure):
    _fields_=[(n,ctypes.c_uint64) for n in ['ReadOperationCount','WriteOperationCount','OtherOperationCount','ReadTransferCount','WriteTransferCount','OtherTransferCount']]
class Extended(ctypes.Structure):
    _fields_=[('BasicLimitInformation',Basic),('IoInfo',IO),('ProcessMemoryLimit',ctypes.c_size_t),('JobMemoryLimit',ctypes.c_size_t),('PeakProcessMemoryUsed',ctypes.c_size_t),('PeakJobMemoryUsed',ctypes.c_size_t)]
class Memory(ctypes.Structure):
    _fields_=[('cb',wintypes.DWORD),('PageFaultCount',wintypes.DWORD)]+[(n,ctypes.c_size_t) for n in ['PeakWorkingSetSize','WorkingSetSize','QuotaPeakPagedPoolUsage','QuotaPagedPoolUsage','QuotaPeakNonPagedPoolUsage','QuotaNonPagedPoolUsage','PagefileUsage','PeakPagefileUsage','PrivateUsage']]
win=ctypes.WinDLL('kernel32',use_last_error=True)
win.CreateJobObjectW.restype=wintypes.HANDLE
win.GetCurrentProcess.restype=wintypes.HANDLE
win.SetInformationJobObject.argtypes=[wintypes.HANDLE,ctypes.c_int,ctypes.c_void_p,wintypes.DWORD]
win.AssignProcessToJobObject.argtypes=[wintypes.HANDLE,wintypes.HANDLE]
win.K32GetProcessMemoryInfo.argtypes=[wintypes.HANDLE,ctypes.c_void_p,wintypes.DWORD]
job=win.CreateJobObjectW(None,None)
lim=Extended(); lim.BasicLimitInformation.LimitFlags=0x100; lim.ProcessMemoryLimit=500000000
assert job and win.SetInformationJobObject(job,9,ctypes.byref(lim),ctypes.sizeof(lim)) and win.AssignProcessToJobObject(job,win.GetCurrentProcess()),ctypes.get_last_error()
timer=threading.Timer(50,lambda:os._exit(124)); timer.daemon=True; timer.start()
def sha(b): return hashlib.sha256(b).hexdigest()
def read(p): return json.loads((OUT/p).read_bytes(),parse_float=Decimal)
def binding(p):
    b=(OUT/p).read_bytes(); return dict(path=p,bytes=len(b),sha256=sha(b))
def render(x):
    if isinstance(x,Q):
        with localcontext() as c:
            c.prec=10; val=str(Decimal(x.numerator)/Decimal(x.denominator))
        return dict(exact=str(x),decimal=val)
    if isinstance(x,dict): return {k:render(v) for k,v in x.items()}
    if isinstance(x,list): return [render(v) for v in x]
    return x
def save(p,x): (OUT/p).write_text(json.dumps(render(x),indent=2)+'\n',encoding='utf-8')
files=['PRICE_CALCULATIONS.json','TIMING_DATA.json','inputs/results__s71_cost_refit.json','inputs/results__s62_cost.json','inputs/analysis__wk11_s71_hybrid.py','inputs/analysis__wk12_s79_cell6.py']
save('RUN_03_INPUTS.json',[binding(p) for p in files])
old=read(files[0]); rates=read(files[2])['constants']; gram_raw=Q(read(files[3])['measured_sec_per_H_pass'])
assert Q(rates['c_b'])==Q(21,10**7)
assert Q(rates['c_h'])==Q(8,10**8)
assert Q(rates['c_e'])==Q(27,10**9)
assert Q(rates['c_r'])==Q(1,10**9)
assert gram_raw<=Q(1737,10**10)<gram_raw*Q(1001,1000)
checks=[]; finals=[]
def eq(actual,node,label):
    assert actual==Q(node['exact']),label
    checks.append(label)
for t in old['targets']:
    n,a,k=t['n'],t['a'],t['k']; K=a+8
    assert sum(t['lam'])==4*k and len(t['lam'])==5 and len(set(t['lam']))==5
    H=math.factorial(4*k)//(math.factorial(4)**k*math.factorial(k)); assert H==t['H']
    eq(Q(24*n*n,10**12),t['dense_three_arrays_TB'],f'k{k} dense memory')
    eq(Q(n*n,10**8)*Q(2*a+29,2)/86400,t['sparse_days_one_sequence'],f'k{k} sparse time')
    eq(Q(1737*H*n,10**10*86400),t['gram_s62_cell_days'],f'k{k} Gram enumeration')
    eq(Q(4*n*a,10**9),t['kernel_u32_GB'],f'k{k} source array')
    assert n*(2**16-1)**2<2**53 and n<2**21
    assert n*(2**16-1)**2<2**63
    scenarios=[]
    for h in t['hybrid']:
        f=Q(h['excess_fraction']['exact']); U=a+math.ceil(f*n); z=10*n
        assert U==h['u']
        B=Q(rates['c_b'])*n*k; S=5*Q(rates['c_c'])*z
        Ht=Q(rates['c_h'])*z*U; V=Q(rates['c_e'])*K*n*k; R=Q(rates['c_r'])*K*n*a; D=Q(5,10**10)*U**3
        pass_time=Ht+V+R+D
        eq((B+S+2*pass_time)/3600,h['two_primes_hours'],f'k{k} f{f} two-prime hours')
        eq((B+S+3*pass_time)/3600,h['two_primes_plus_replay_hours'],f'k{k} f{f} old replay formula')
        old_mem=12*n*a+100*z+400*n+5*max(250000000,128*n)+80*U*U+500000000
        eq(Q(old_mem,10**9),h['memory_envelope_GB'],f'k{k} f{f} old memory formula')
        # Additional uint32 temporary during K % p -> int64 conversion.
        mem=old_mem+4*n*a
        # The independent pass rebuilds E and selects its cover too.
        audited=2*(B+S)+3*pass_time
        # Crude nnz <= 4*k*n for distinct-part five-row targets.
        zmax=4*k*n
        worst_rho_audit=2*(B+5*Q(rates['c_c'])*zmax)+3*(Q(rates['c_h'])*zmax*U+V+R+D)
        scenarios.append(dict(f=f,U=U,nnz_model=z,two_primes_hours=(B+S+2*pass_time)/3600,
            two_primes_plus_independent_rebuild_hours=audited/3600,
            memory_envelope_GB=Q(mem,10**9),
            structural_nnz_bound=zmax,structural_nnz_audit_hours=worst_rho_audit/3600,
            structural_nnz_memory_GB=Q(mem+100*(zmax-z),10**9)))
    finals.append(dict(k=k,lam=t['lam'],a=a,n=n,scenarios=scenarios))
save('FINAL_PRICE_AUDIT.json',dict(label='COMPUTED: exact arithmetic checks and two disclosed pricing corrections; no rank experiment',
    passed_checks=len(checks),checks=checks,gram_rate_raw_seconds=gram_raw,gram_rate_used_rounded_seconds=Q(1737,10**10),
    corrections=['Count an additional uint32 kernel temporary: 16*n*a in the memory envelope instead of 12*n*a.',
                 'Include a second build and cover for the independent replay.'],targets=finals,
    uncertainties='Rates and support fractions are extrapolations, not measured target properties. Scenario bounds are not confidence intervals.'))
mem=Memory(); mem.cb=ctypes.sizeof(mem)
assert win.K32GetProcessMemoryInfo(win.GetCurrentProcess(),ctypes.byref(mem),ctypes.sizeof(mem))
assert mem.PeakWorkingSetSize<500000000
save('RUN_03_RECEIPT.json',dict(label='COMPUTED pricing verification only',command=[sys.executable,str(pathlib.Path(__file__).resolve())],
    finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),script=binding('b27_06_audit.py'),
    inputs=binding('RUN_03_INPUTS.json'),outputs=[binding('FINAL_PRICE_AUDIT.json')],
    wall_seconds=time.perf_counter()-START,peak_working_set_bytes=mem.PeakWorkingSetSize,
    peak_pagefile_bytes=mem.PeakPagefileUsage,memory_cap_bytes=500000000,wall_cap_seconds=50,
    enforcement='Windows process-memory Job Object and daemon wall watchdog',target_builds=0,rank_measurements=0,
    arithmetic='Python int/Fraction; Decimal for reading recorded decimal rates and displaying results'))
print(json.dumps(render(dict(passed_checks=len(checks),peak_working_set_bytes=mem.PeakWorkingSetSize,targets=finals)),indent=2))
