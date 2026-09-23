"""Verify the fixed one-node example and coefficient-map submersion.

This is run 2. A negative check is recorded as a negative, not retried on new
examples. No determinant equation is sought.
"""
import hashlib
import itertools as it
import json
import os
from pathlib import Path
import sys
import threading
import time
from b27_01_verify import (cap_memory, cubic_coefficients, dump, exponents,
                          integer_determinant, modular_determinant, P, ROOT, OUT, sha)

def independent_rows(rows):
    basis, chosen = {}, []
    for i, raw in enumerate(rows):
        row = [v % P for v in raw]
        for col in sorted(basis):
            factor = row[col]
            if factor:
                row = [(a-factor*b) % P for a,b in zip(row, basis[col])]
        pivot = next((j for j,v in enumerate(row) if v), None)
        if pivot is not None:
            inverse = pow(row[pivot],-1,P)
            basis[pivot] = [v*inverse % P for v in row]
            chosen.append(i)
    return chosen

def verify():
    spec = json.loads((OUT/'NODAL_INPUT.json').read_bytes())
    rows = spec['matrix_rows_of_linear_forms']
    matrices = [[[rows[i][j][k] for j in range(3)] for i in range(3)] for k in range(5)]
    cubic = cubic_coefficients(matrices)
    assert cubic[(3,0,0,0,0)] == 0
    assert all(cubic[tuple(2 if j==0 else int(j==i) for j in range(5))] == 0 for i in range(1,5))
    quadratic = {alpha[1:]:v for alpha,v in cubic.items() if alpha[0] == 1 and v}
    assert quadratic == {(1,1,0,0):1, (0,0,1,1):1}, quadratic
    partials = []
    for i in range(5):
        partials.append({tuple(alpha[j]-int(i==j) for j in range(5)): alpha[i]*v
                         for alpha,v in cubic.items() if alpha[i]})
    sextic = exponents(6)
    index = {a:i for i,a in enumerate(sextic)}
    macaulay = []
    for i,beta in it.product(range(5), exponents(4)):
        row = [0]*210
        for gamma,v in partials[i].items():
            row[index[tuple(a+b for a,b in zip(beta,gamma))]] += v
        assert row[0] == 0
        macaulay.append(row)
    chosen = independent_rows([r[1:] for r in macaulay])
    result = dict(label='COMPUTED', prime=P, jacobian_ideal_degree=6,
                  jacobian_ideal_rank_mod_p=len(chosen), expected_rank=209,
                  selected_rows=chosen, omitted_column=[6,0,0,0,0],
                  row_order='partial 0..4, then descending-lex degree-four exponent',
                  column_order='descending-lex degree-six exponent, omit x0^6',
                  point=[1,0,0,0,0], quadratic_term='x1*x2+x3*x4',
                  cubic_exponents=[list(a) for a in cubic], cubic_coefficients=list(cubic.values()))
    if len(chosen) != 209:
        result['outcome'] = 'NEGATIVE: fixed candidate did not certify a unique singular point'
        dump(OUT/'BOUNDARY_CERTIFICATE.json', result)
        return
    minor = [macaulay[i][1:] for i in chosen]
    residue, exact = modular_determinant(minor), integer_determinant(minor)
    assert residue and exact % P == residue
    result.update(integer_minor_determinant=str(exact), minor_mod_prime=residue,
                  jacobian_ideal_rank_Q=209)
    cubic_index = {a:i for i,a in enumerate(cubic)}
    differential = []
    for k,i,j in it.product(range(5), range(3), range(3)):
        rr = [r for r in range(3) if r != i]
        cc = [c for c in range(3) if c != j]
        row = [0]*35
        for a,b in it.product(range(5), repeat=2):
            alpha = tuple(int(v==k)+int(v==a)+int(v==b) for v in range(5))
            row[cubic_index[alpha]] += (matrices[a][rr[0]][cc[0]]*matrices[b][rr[1]][cc[1]]
                                       +matrices[a][rr[0]][cc[1]]*matrices[b][rr[1]][cc[0]])
        differential.append(row)
    selected = independent_rows(differential)
    result['parameter_differential'] = dict(rank_mod_p=len(selected), selected_rows=selected,
                                           row_order='(variable k, matrix row i, matrix column j)',
                                           column_order='descending-lex cubic monomials')
    if len(selected) == 35:
        square = [differential[i] for i in selected]
        value, mod = integer_determinant(square), modular_determinant(square)
        assert value and value % P == mod
        result['parameter_differential'].update(rank_Q=35, integer_minor_determinant=str(value), minor_mod_prime=mod)
        result['outcome'] = 'PASS'
    else:
        result['outcome'] = 'NEGATIVE: unique node certified but coefficient-map submersion not certified'
    dump(OUT/'BOUNDARY_CERTIFICATE.json', result)
    print(json.dumps({'outcome':result['outcome'], 'singular_ideal_rank':209, 'parameter_rank':len(selected),
                      'minor_mod_prime':residue}), flush=True)

def main():
    started = time.perf_counter()
    job, stats = cap_memory()
    receipt = dict(run_number=2, started_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),
                   command=[sys.executable,'-B','analysis/b27_01_boundary.py'],
                   inputs=[dict(path=p.relative_to(ROOT).as_posix(),sha256=sha(p.read_bytes()))
                           for p in [Path(__file__),ROOT/'analysis/b27_01_verify.py',OUT/'NODAL_INPUT.json']],
                   seconds_limit=60, memory_limit_bytes=512_000_000, job_object_enforced=bool(job),
                   workers=1, random_generation=False, outcome='RUNNING')
    dump(OUT/'RUN_02_RECEIPT.json',receipt)
    def timeout():
        receipt.update(outcome='TIMEOUT',wall_seconds=time.perf_counter()-started)
        dump(OUT/'RUN_02_RECEIPT.json',receipt)
        os._exit(124)
    timer = threading.Timer(max(.01,60-(time.perf_counter()-started)),timeout)
    timer.daemon = True
    timer.start()
    try:
        verify()
        receipt['outcome'] = 'COMPLETED'
    except BaseException:
        receipt['outcome'] = 'FAIL'
        raise
    finally:
        timer.cancel()
        receipt['wall_seconds'] = time.perf_counter()-started
        receipt.update(stats())
        p = OUT/'BOUNDARY_CERTIFICATE.json'
        if p.exists():
            receipt['output'] = dict(path=p.relative_to(ROOT).as_posix(),sha256=sha(p.read_bytes()),bytes=p.stat().st_size)
            receipt['mathematical_outcome'] = json.loads(p.read_bytes())['outcome']
        dump(OUT/'RUN_02_RECEIPT.json',receipt)
        print(json.dumps({'wall_seconds':receipt['wall_seconds'],**stats()}),flush=True)
    assert receipt['wall_seconds'] < 60

if __name__ == '__main__':
    main()
