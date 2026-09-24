"""Exact rational audit of recorded timing models. NEVER builds a target matrix.
One bounded pricing-arithmetic run; no rank experiment or new calibration run.
"""
import ctypes, datetime, hashlib, json, math, os, pathlib, sys, threading, time
from ctypes import wintypes
from decimal import Decimal, localcontext
from fractions import Fraction as F

OUT=pathlib.Path(__file__).resolve().parent
START=time.perf_counter()
JOB=None

def cap():
    global JOB
    class Basic(ctypes.Structure):
        _fields_=[('PerProcessUserTimeLimit',ctypes.c_int64),('PerJobUserTimeLimit',ctypes.c_int64),
            ('LimitFlags',wintypes.DWORD),('MinimumWorkingSetSize',ctypes.c_size_t),('MaximumWorkingSetSize',ctypes.c_size_t),
            ('ActiveProcessLimit',wintypes.DWORD),('Affinity',ctypes.c_size_t),('PriorityClass',wintypes.DWORD),('SchedulingClass',wintypes.DWORD)]
    class IO(ctypes.Structure):
        _fields_=[(n,ctypes.c_uint64) for n in ['ReadOperationCount','WriteOperationCount','OtherOperationCount','ReadTransferCount','WriteTransferCount','OtherTransferCount']]
    class Extended(ctypes.Structure):
        _fields_=[('BasicLimitInformation',Basic),('IoInfo',IO),('ProcessMemoryLimit',ctypes.c_size_t),
            ('JobMemoryLimit',ctypes.c_size_t),('PeakProcessMemoryUsed',ctypes.c_size_t),('PeakJobMemoryUsed',ctypes.c_size_t)]
    k=ctypes.WinDLL('kernel32',use_last_error=True)
    k.CreateJobObjectW.restype=wintypes.HANDLE
    k.SetInformationJobObject.argtypes=[wintypes.HANDLE,ctypes.c_int,ctypes.c_void_p,wintypes.DWORD]
    k.AssignProcessToJobObject.argtypes=[wintypes.HANDLE,wintypes.HANDLE]
    k.GetCurrentProcess.restype=wintypes.HANDLE
    JOB=k.CreateJobObjectW(None,None)
    e=Extended(); e.BasicLimitInformation.LimitFlags=0x100; e.ProcessMemoryLimit=512*1024*1024
    if not JOB or not k.SetInformationJobObject(JOB,9,ctypes.byref(e),ctypes.sizeof(e)) or not k.AssignProcessToJobObject(JOB,k.GetCurrentProcess()):
        raise ctypes.WinError(ctypes.get_last_error())
    timer=threading.Timer(60,lambda:os._exit(124)); timer.daemon=True; timer.start()

def raw(p): return (OUT/p).read_bytes()
def load(p): return json.loads(raw(p),parse_float=Decimal)
def lines(p): return [json.loads(s,parse_float=Decimal) for s in raw(p).splitlines() if s.strip()]
def frac(x): return F(x)
def render(x):
    if isinstance(x,F):
        with localcontext() as c:
            c.prec=9; d=str(Decimal(x.numerator)/Decimal(x.denominator))
        return dict(exact=str(x),decimal=d)
    if isinstance(x,Decimal): return str(x)
    if isinstance(x,dict): return {k:render(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)): return [render(v) for v in x]
    return x
def save(p,x): (OUT/p).write_text(json.dumps(render(x),indent=2)+'\n',encoding='utf-8')
def quant(v):
    v=sorted(v)
    return dict(count=len(v),min=v[0],p10=v[max(0,math.ceil(len(v)/10)-1)],median=v[(len(v)-1)//2],p90=v[math.ceil(9*len(v)/10)-1],max=v[-1])

cap()
files=['inputs/results__s60_scan_dense.jsonl','inputs/results__s60_scan_sparse.jsonl',
       'inputs/results__s71_sweep.jsonl','inputs/results__s71_calibration.jsonl','inputs/results__s71_cost_refit.json',
       'inputs/results__s79_cells.jsonl','inputs/results__s36_ledger.md','inputs/results__s60_census.json',
       'inputs/results__s62_cost.json','inputs/results__occurrence_screen.csv']
bindings=[dict(path=p,bytes=len(raw(p)),sha256=hashlib.sha256(raw(p)).hexdigest()) for p in files]
save('RUN_02_INPUTS.json',bindings)

dense=[]
for r in lines(files[0]):
    if r['n_chi']<3000: continue
    for p,v in r['per_prime'].items():
        dense.append(dict(lam=r['lam'],delta=r['delta'],n=r['n_chi'],p=p,seconds=v['kernel_secs'],
                          coefficient=F(v['kernel_secs'])/r['n_chi']**3))
s36=[]
for line in raw(files[6]).decode().splitlines():
    if not line.startswith('| A'): continue
    v=[t.strip().strip('`') for t in line.strip('|').split('|')]
    if len(v)<14 or not v[7].isdigit(): continue
    n=int(v[7]); secs=int(v[13])
    if n>=8000: s36.append(dict(lam=v[1],n=n,seconds_two_primes=secs,coefficient=F(secs,2*n**3)))

hybrid=[]
for file in files[2:4]+[files[5]]:
    for r in lines(file):
        if 'per_prime' not in r or 'cover_E' not in r: continue
        n=r['n_chi']; a=r['a']; u=n-r['cover_E']['size']; nz=r['nnz']
        if n<20000: continue
        for p,v in r['per_prime'].items():
            if 'hybrid' not in v: continue
            hybrid.append(dict(source=file,lam=r['lam'],delta=r['delta'],a=a,n=n,N_S=r['N_S'],u=u,nnz=nz,prime=p,
                seconds=v['hybrid']['secs'],c_h=F(v['hybrid']['secs'])/(nz*u),rho=F(nz,n),f=F(u-a,n),
                hwm_gb=v['hwm_gb']))
stats=dict(dense_c_seconds_per_n_cubed=quant([r['coefficient'] for r in dense]),
           s36_c_seconds_per_n_cubed_per_prime=quant([r['coefficient'] for r in s36]),
           hybrid_c_seconds_per_nnz_u=quant([r['c_h'] for r in hybrid]),
           hybrid_excess_fraction=quant([r['f'] for r in hybrid]),
           hybrid_nnz_per_n=quant([r['rho'] for r in hybrid]))
save('TIMING_DATA.json',dict(dense=dense,s36=s36,hybrid=hybrid,summary=stats))

targets=[dict(k=8,lam=[12,8,6,4,2],a=109,n=813314,m_det=27257),
         dict(k=9,lam=[14,10,6,4,2],a=437,n=2085864,m_det=104544)]
census=load(files[7]); found=[]
def walk(x):
    if isinstance(x,dict):
        if x.get('lam') in [t['lam'] for t in targets]: found.append(x)
        for v in x.values(): walk(v)
    elif isinstance(x,list):
        for v in x: walk(v)
walk(census)
for t in targets:
    assert any(r['lam']==t['lam'] and r['delta']==t['k'] and r['a']==t['a'] and r['N_S']==t['n'] and r['n_chi']==t['n'] for r in found)
    assert sum(t['lam'])==4*t['k'] and len(set(t['lam']))==5

result=[]
for t in targets:
    n,a,k=t['n'],t['a'],t['k']; K=a+8
    H=math.factorial(4*k)//(math.factorial(4)**k*math.factorial(k))
    d=dict(**t,K=K,NS_delta=n*k,H=H,
        dense_three_arrays_TB=F(24*n*n,10**12),dense_historical_range_TB=[F(24*n*n,10**12),F(75*n*n,10**12)],
        dense_s60_days_per_prime=[F(c*n**3,86400) for c in [F(3,10**10),F(12,10**10)]],
        dense_s36_days_two_primes=[F(2*c*n**3,86400) for c in [F(1,10**10),F(5,10**10)]],
        sparse_days_one_sequence=F(n*n*(2*a+29),2*10**8*86400),
        sparse_days_op_range=[F(4*n*n*(2*a+29),2)*v/86400 for v in [F(17,10**10),F(53,10**10)]],
        sparse_C_arrays_GB=F(16*n*(2*a+29),2*10**9),
        sparse_pipeline_memory_estimate_GB=[F(60*n*(2*a+29),2*10**9),F(100*n*(2*a+29),2*10**9)],
        sparse_dense_EV_GB=F(8*n*K,10**9),kernel_u32_GB=F(4*n*a,10**9),kernel_u32_and_i64_GB=F(12*n*a,10**9),
        gram_s62_one_pass_days=F(1737*H,10**10*86400),gram_s62_cell_days=F(1737*H*n,10**10*86400),
        gram_s56_one_weight_days=F(62*H*n,10**9*86400),gram_labels_min_bytes=4*k*H,
        gram_dense_B_words_bytes=8*n*n,gram_count_min_bytes=4*n*n,
        gram_reduced_ops_if_full_support=a*n*n+a*a*n,
        matmul_exact_inner_bound_pass=n<2**21,
        hybrid=[])
    for f in [F(1,1000),F(25,10000),F(48,10000),F(13,1000)]:
        u=a+math.ceil(f*n); nz=10*n
        build=F(21,10**7)*n*k
        sieve=F(5,10**7)*nz
        h=F(8,10**8)*nz*u
        ev=F(27,10**9)*K*n*k
        contraction=F(K*n*a,10**9)
        # Added conservative cubic residual term, not claimed as a new fitted theorem.
        residual=F(5,10**10)*u**3
        # Memory envelope: code-read live kernel arrays, row copies, minimum block,
        # source verification/lift temporaries, and Python list + flint residual copies.
        block=max(250000000,128*n)
        memory=12*n*a+100*nz+400*n+5*block+80*u*u+500000000
        one=build+sieve+h+ev+contraction+residual
        two=build+sieve+2*(h+ev+contraction+residual)
        audited=build+sieve+3*(h+ev+contraction+residual)
        d['hybrid'].append(dict(excess_fraction=f,u=u,nnz_assumed=nz,build_s=build,sieve_s=sieve,
             hybrid_s_per_prime=h,residual_cubic_allowance_s=residual,ev_s_per_prime=ev,
             contraction_s_per_prime=contraction,one_prime_minutes=one/60,two_primes_hours=two/3600,
             two_primes_plus_replay_hours=audited/3600,memory_envelope_GB=F(memory,10**9)))
    result.append(d)

save('PRICE_CALCULATIONS.json',dict(label='COMPUTED: exact rational verification of conditional pricing formulae; not measured rank or target runtime',
     statistics=stats,targets=result,model='Published s71 refit; one determinant family; sequential primes; separate cubic residual allowance and memory envelope'))
outfiles=['RUN_02_INPUTS.json','TIMING_DATA.json','PRICE_CALCULATIONS.json']
save('RUN_02_RECEIPT.json',dict(label='COMPUTED pricing arithmetic only',finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
     command=[sys.executable,str(pathlib.Path(__file__).resolve())],script_sha256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
     inputs_sha256=hashlib.sha256(raw('RUN_02_INPUTS.json')).hexdigest(),outputs=[dict(path=p,bytes=len(raw(p)),sha256=hashlib.sha256(raw(p)).hexdigest()) for p in outfiles],
     wall_seconds=time.perf_counter()-START,limits=dict(wall_seconds=60,memory_bytes=512*1024*1024,memory_enforcement='Windows process memory Job Object',wall_enforcement='daemon wall timer exits 124'),
     mathematical_rank_runs=0,target_builds=0,arithmetic='Python int/Fraction; Decimal only for display; no binary floating-point fits'))
print(json.dumps(render(dict(stats=stats,targets=result)),indent=2))
