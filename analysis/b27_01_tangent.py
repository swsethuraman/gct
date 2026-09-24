"""Run 3: one fixed tangent-section certificate, after the zero-entry obstruction.

The input is a specified rational smooth point of the ambient permanent and
four specified tangent vectors. No iteration over candidates is performed.
"""
import itertools as it
import json
import os
from pathlib import Path
import sys
import threading
import time
from b27_01_verify import (cap_memory, cubic_coefficients, dump, exponents,
                          integer_determinant, modular_determinant, P, ROOT, OUT, sha)
from b27_01_boundary import independent_rows

def verify():
    q = [[1,2,3],[4,5,6],[91,104,-333]]
    gradient = [-1041,-786,871,-354,-60,286,27,18,13]
    # V_r has first eight entries 13*r^i and ninth -sum gradient_i*r^i.
    # Thus gradient dot V_r = 0 exactly; q itself is on per=0.
    matrices = [q]
    for r in (1,2,3,4):
        values = [13*r**i for i in range(8)] + [-sum(gradient[i]*r**i for i in range(8))]
        assert sum(a*b for a,b in zip(gradient,values)) == 0
        matrices.append([values[3*i:3*i+3] for i in range(3)])
    cubic = cubic_coefficients(matrices)
    assert cubic[(3,0,0,0,0)] == 0
    for i in range(1,5):
        alpha = [2,0,0,0,0]; alpha[i] = 1
        assert cubic[tuple(alpha)] == 0
    hessian = []
    for i in range(1,5):
        row = []
        for j in range(1,5):
            alpha = [1,0,0,0,0]; alpha[i]+=1; alpha[j]+=1
            row.append(cubic[tuple(alpha)]*(2 if i==j else 1))
        hessian.append(row)
    hdet = integer_determinant(hessian)
    partials = [{tuple(a[j]-int(i==j) for j in range(5)):a[i]*v for a,v in cubic.items() if a[i]}
                for i in range(5)]
    sextic = exponents(6); index = {a:i for i,a in enumerate(sextic)}
    macaulay = []
    for i,beta in it.product(range(5),exponents(4)):
        row = [0]*210
        for gamma,v in partials[i].items():
            row[index[tuple(a+b for a,b in zip(beta,gamma))]] += v
        assert row[0] == 0
        macaulay.append(row[1:])
    selected = independent_rows(macaulay)
    result = dict(label='COMPUTED', prime=P, matrices_A0_to_A4=matrices,
                  construction='q plus four fixed tangent Vandermonde directions r=1,2,3,4',
                  tangent_point=q, permanent_gradient_at_q=gradient,
                  cubic_exponents=[list(a) for a in cubic], cubic_coefficients=list(cubic.values()),
                  singular_point=[1,0,0,0,0], hessian_at_point=hessian, hessian_determinant=str(hdet),
                  jacobian_ideal_degree=6, jacobian_ideal_rank_mod_p=len(selected), selected_rows=selected,
                  column_order='Descending-lex degree-six monomials, omitting x0^6',
                  row_order='partial index, then descending-lex degree-four monomial',
                  outcome='NEGATIVE')
    if len(selected) == 209 and hdet != 0:
        square = [macaulay[i] for i in selected]
        mod = modular_determinant(square)
        exact = integer_determinant(square)
        assert exact % P == mod != 0
        result.update(jacobian_ideal_rank_Q=209, integer_minor_determinant=str(exact),minor_mod_prime=mod)
        index3 = {a:i for i,a in enumerate(cubic)}
        differential = []
        for k,i,j in it.product(range(5),range(3),range(3)):
            rr=[r for r in range(3) if r!=i]; cc=[c for c in range(3) if c!=j]
            row=[0]*35
            for a,b in it.product(range(5),repeat=2):
                alpha=tuple(int(v==k)+int(v==a)+int(v==b) for v in range(5))
                row[index3[alpha]] += matrices[a][rr[0]][cc[0]]*matrices[b][rr[1]][cc[1]] + matrices[a][rr[0]][cc[1]]*matrices[b][rr[1]][cc[0]]
            differential.append(row)
        chosen=independent_rows(differential)
        result['parameter_differential']=dict(rank_mod_p=len(chosen),selected_rows=chosen,
                                              row_order='(k,i,j)',column_order='Descending-lex cubic monomials')
        if len(chosen)==35:
            square=[differential[i] for i in chosen]
            exact,mod=integer_determinant(square),modular_determinant(square)
            assert exact % P == mod != 0
            result['parameter_differential'].update(rank_Q=35,integer_minor_determinant=str(exact),minor_mod_prime=mod)
            result['outcome']='PASS'
    dump(OUT/'TANGENT_CERTIFICATE.json',result)
    print(json.dumps({'outcome':result['outcome'],'jacobian_ideal_rank':len(selected),
                      'hessian_nondegenerate':bool(hdet),'parameter_differential':result.get('parameter_differential',{}).get('rank_mod_p')}),flush=True)

def main():
    start=time.perf_counter(); job,stats=cap_memory()
    receipt=dict(run_number=3,started_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),
                 command=[sys.executable,'-B','analysis/b27_01_tangent.py'],
                 inputs=[dict(path=p.relative_to(ROOT).as_posix(),sha256=sha(p.read_bytes())) for p in
                         [Path(__file__),ROOT/'analysis/b27_01_verify.py',ROOT/'analysis/b27_01_boundary.py']],
                 seconds_limit=60,memory_limit_bytes=512_000_000,job_object_enforced=bool(job),
                 workers=1,random_generation=False,outcome='RUNNING')
    dump(OUT/'RUN_03_RECEIPT.json',receipt)
    def timeout():
        receipt.update(outcome='TIMEOUT',wall_seconds=time.perf_counter()-start)
        dump(OUT/'RUN_03_RECEIPT.json',receipt); os._exit(124)
    timer=threading.Timer(max(.01,60-(time.perf_counter()-start)),timeout); timer.daemon=True; timer.start()
    try:
        verify(); receipt['outcome']='COMPLETED'
    except BaseException:
        receipt['outcome']='FAIL'; raise
    finally:
        timer.cancel(); receipt['wall_seconds']=time.perf_counter()-start; receipt.update(stats())
        p=OUT/'TANGENT_CERTIFICATE.json'
        if p.exists():
            receipt['output']=dict(path=p.relative_to(ROOT).as_posix(),sha256=sha(p.read_bytes()),bytes=p.stat().st_size)
            receipt['mathematical_outcome']=json.loads(p.read_bytes())['outcome']
        dump(OUT/'RUN_03_RECEIPT.json',receipt)
        print(json.dumps({'wall_seconds':receipt['wall_seconds'],**stats()}),flush=True)
    assert receipt['wall_seconds']<60

if __name__=='__main__':
    main()
