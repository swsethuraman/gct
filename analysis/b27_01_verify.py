"""One fixed B17 smoothness-certificate replay, exact over F_65521 and Z.

No random generator, pivot-minor search, sampled nullspace, or equation search.
The 210 row indices are frozen in the committed input certificate.  Only
installed Python standard-library integer arithmetic is used.
"""
import ctypes as C
from ctypes import wintypes as W
import hashlib
import itertools as it
import json
import os
from pathlib import Path
import sys
import threading
import time

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'results/b27_01'
P = 65521
EXPECTED_INPUT = '03585015180e0724bb7d8f1a6264a64e9a6fc877d191dc13cab0187c49f58e9c'

def sha(data):
    return hashlib.sha256(data).hexdigest()

def dump(path, data):
    path.write_bytes((json.dumps(data, indent=2) + '\n').encode('utf-8'))

def cap_memory():
    class Basic(C.Structure):
        _fields_ = [('process_time', C.c_longlong), ('job_time', C.c_longlong),
                    ('flags', W.DWORD), ('minimum', C.c_size_t),
                    ('maximum', C.c_size_t), ('active', W.DWORD),
                    ('affinity', C.c_size_t), ('priority', W.DWORD),
                    ('scheduling', W.DWORD)]
    class IO(C.Structure):
        _fields_ = [(name, C.c_ulonglong) for name in
                    ('read_ops', 'write_ops', 'other_ops', 'read_bytes',
                     'write_bytes', 'other_bytes')]
    class Extended(C.Structure):
        _fields_ = [('basic', Basic), ('io', IO),
                    ('process_memory', C.c_size_t), ('job_memory', C.c_size_t),
                    ('peak_process', C.c_size_t), ('peak_job', C.c_size_t)]
    kernel = C.WinDLL('kernel32', use_last_error=True)
    kernel.CreateJobObjectW.restype = W.HANDLE
    kernel.CreateJobObjectW.argtypes = [C.c_void_p, W.LPCWSTR]
    kernel.SetInformationJobObject.argtypes = [W.HANDLE, C.c_int, C.c_void_p, W.DWORD]
    kernel.GetCurrentProcess.restype = W.HANDLE
    kernel.AssignProcessToJobObject.argtypes = [W.HANDLE, W.HANDLE]
    job = kernel.CreateJobObjectW(None, None)
    if not job:
        raise C.WinError(C.get_last_error())
    info = Extended()
    info.basic.flags = 0x100 | 0x200 | 0x2000
    # 512 decimal MB is stricter than the historic 512 MiB allowance.
    info.process_memory = info.job_memory = 512_000_000
    if not kernel.SetInformationJobObject(job, 9, C.byref(info), C.sizeof(info)):
        raise C.WinError(C.get_last_error())
    if not kernel.AssignProcessToJobObject(job, kernel.GetCurrentProcess()):
        raise C.WinError(C.get_last_error())
    def stats():
        final = Extended()
        kernel.QueryInformationJobObject.argtypes = [W.HANDLE, C.c_int, C.c_void_p, W.DWORD, C.c_void_p]
        if not kernel.QueryInformationJobObject(job, 9, C.byref(final), C.sizeof(final), None):
            raise C.WinError(C.get_last_error())
        return {'peak_job_memory_bytes': final.peak_job, 'peak_process_memory_bytes': final.peak_process}
    return job, stats

def exponents(degree):
    return sorted((tuple(c.count(i) for i in range(5))
                   for c in it.combinations_with_replacement(range(5), degree)), reverse=True)

def cubic_coefficients(matrices):
    result = dict.fromkeys(exponents(3), 0)
    for perm in it.permutations(range(3)):
        for variables in it.product(range(5), repeat=3):
            product = 1
            for row in range(3):
                product *= matrices[variables[row]][row][perm[row]]
            result[tuple(variables.count(i) for i in range(5))] += product
    return result

def modular_determinant(matrix):
    a = [[x % P for x in row] for row in matrix]
    n, answer = len(a), 1
    assert all(len(row) == n for row in a)
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j]), None)
        if pivot is None:
            return 0
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            answer = -answer
        value = a[j][j]
        answer = answer * value % P
        inverse = pow(value, -1, P)
        for i in range(j + 1, n):
            factor = a[i][j] * inverse % P
            if factor:
                a[i][j + 1:] = [(u - factor*v) % P for u, v in zip(a[i][j+1:], a[j][j+1:])]
                a[i][j] = 0
    return answer % P

def integer_determinant(matrix):
    a = [row[:] for row in matrix]
    n, previous, sign = len(a), 1, 1
    for j in range(n - 1):
        pivot = next((i for i in range(j, n) if a[i][j]), None)
        if pivot is None:
            return 0
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            sign = -sign
        value, pivot_tail = a[j][j], a[j][j+1:]
        for i in range(j + 1, n):
            scale = a[i][j]
            tail = []
            for u, v in zip(a[i][j+1:], pivot_tail):
                quotient, remainder = divmod(value*u - scale*v, previous)
                assert remainder == 0
                tail.append(quotient)
            a[i][j+1:] = tail
            a[i][j] = 0
        previous = value
    return sign*a[-1][-1]

def verify():
    source = OUT / 'inputs/b17_certificate.json'
    raw = source.read_bytes()
    assert sha(raw) == EXPECTED_INPUT
    old = json.loads(raw)
    assert P == old['prime'] and all(P % d for d in range(2, 256))
    matrices = old['matrices_A0_to_A4']
    c = cubic_coefficients(matrices)
    assert [list(a) for a in c] == old['cubic_exponents']
    assert list(c.values()) == old['cubic_coefficients']
    partials = []
    for i in range(5):
        partials.append({tuple(a[j]-int(i == j) for j in range(5)): a[i]*v
                         for a, v in c.items() if a[i]})
    quartic, sextic = exponents(4), exponents(6)
    index = {a:i for i,a in enumerate(sextic)}
    macaulay, labels = [], []
    for i in range(5):
        for beta in quartic:
            row = [0]*len(sextic)
            for gamma, v in partials[i].items():
                row[index[tuple(a+b for a,b in zip(beta,gamma))]] += v
            macaulay.append(row)
            labels.append([i, list(beta)])
    selected = old['smoothness']['selected_rows']
    assert len(selected) == len(set(selected)) == 210
    assert [labels[i] for i in selected] == old['smoothness']['selected_row_labels']
    assert [list(a) for a in sextic] == old['smoothness']['column_exponents']
    minor = [macaulay[i] for i in selected]
    residue = modular_determinant(minor)
    assert residue == old['smoothness']['minor_mod_prime'] == 61614
    exact = integer_determinant(minor)
    assert exact != 0 and exact % P == residue
    frame = [[matrices[k][i][j] for k in range(5)] for i,j in it.product(range(3), repeat=2)]
    frame_minor = integer_determinant(frame[:5])
    assert frame_minor == 2562 == int(old['source_frame']['minor_integer'])
    linear_form = old['padding_linear_form']
    assert linear_form == [1,0,0,0,0]
    tstar = dict(row_order=['l','A11','A12','A13','A21','A22','A23','A31','A32','A33'],
                 variables=['x0','x1','x2','x3','x4'], T=[linear_form]+frame,
                 matrices_A0_to_A4=matrices, cubic_exponents=[list(a) for a in c],
                 cubic_coefficients=list(c.values()), field='Q',
                 source_commit='01c49022c2a222254884c8c96611dd0e9f302892',
                 source_certificate_sha256=EXPECTED_INPUT,
                 method='READ fixed witness, COMPUTED coefficient and rank replay')
    dump(OUT / 'T_STAR.json', tstar)
    result = dict(status='PASS', label='COMPUTED', prime=P,
                  certificate_kind='Exact Jacobian-ideal degree-six spanning certificate',
                  input_sha256=EXPECTED_INPUT,
                  matrix_shape=[350,210], selected_rows=selected,
                  row_order='partial index 0..4, then descending-lex degree-four exponent',
                  column_order='descending-lex degree-six exponent',
                  integer_minor_determinant=str(exact), minor_mod_prime=residue,
                  exact_Bareiss_divisions_checked=True,
                  rank_over_Fp=210, rank_over_Q=210, frame_minor_integer=frame_minor,
                  conclusion='S_6 is contained in the gradient ideal over Q and F_65521; the projective cubic is geometrically smooth in both characteristics.',
                  witness_output_sha256=sha((OUT / 'T_STAR.json').read_bytes()))
    dump(OUT / 'SMOOTHNESS_CERTIFICATE.json', result)
    print(json.dumps({'status':'PASS', 'minor_mod_prime':residue,
                      'integer_determinant_digits':len(str(abs(exact))), 'frame_minor':frame_minor}), flush=True)

def main():
    if os.name != 'nt':
        raise RuntimeError('This bound implementation requires Windows Job Objects')
    started = time.perf_counter()
    job, stats = cap_memory()
    receipt = dict(run_number=1, started_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),
                   command=[sys.executable, '-B', 'analysis/b27_01_verify.py'],
                   script_sha256=sha(Path(__file__).read_bytes()),
                   interpreter_sha256=sha(Path(sys.executable).read_bytes()),
                   input_sha256=EXPECTED_INPUT, seconds_limit=60,
                   memory_limit_bytes=512_000_000, job_object_enforced=bool(job),
                   workers=1, installs=0, arithmetic='Python standard-library exact int and finite-field arithmetic',
                   historical_random_generator_executed=False, outcome='RUNNING')
    dump(OUT / 'RUN_01_RECEIPT.json', receipt)
    def timeout():
        receipt.update(outcome='TIMEOUT', wall_seconds=time.perf_counter()-started)
        dump(OUT / 'RUN_01_RECEIPT.json', receipt)
        os._exit(124)
    timer = threading.Timer(max(0.01, 60-(time.perf_counter()-started)), timeout)
    timer.daemon = True
    timer.start()
    try:
        verify()
        receipt['outcome'] = 'PASS'
    except BaseException:
        receipt['outcome'] = 'FAIL'
        raise
    finally:
        timer.cancel()
        receipt['wall_seconds'] = time.perf_counter()-started
        receipt.update(stats())
        receipt['outputs'] = [{ 'path':p.relative_to(ROOT).as_posix(), 'sha256':sha(p.read_bytes()), 'bytes':p.stat().st_size}
                              for p in [OUT/'T_STAR.json',OUT/'SMOOTHNESS_CERTIFICATE.json'] if p.exists()]
        if receipt['wall_seconds'] > 60:
            receipt['outcome'] = 'OVERRUN'
        dump(OUT / 'RUN_01_RECEIPT.json', receipt)
        print(json.dumps({'outcome':receipt['outcome'], 'wall_seconds':receipt['wall_seconds'], **stats()}), flush=True)
    assert receipt['outcome'] == 'PASS'

if __name__ == '__main__':
    main()
