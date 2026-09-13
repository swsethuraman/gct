"""Bounded exact source-independence pilot from integral flagged tensors."""
from collections import defaultdict
from itertools import product
import json
from pathlib import Path
import random
import time

from b15_10_witness import pencil_coefficients, tensor, require, sizing, skew_pencil


def hyperdet_series(t, v, r, degree=2):
    """Coefficients through degree of H(t+z*v), without interpolation."""
    sizing(r)
    require(degree in (1,2) and r <= 6, 'series bounds')
    states = {(0,0,0): (1,)+(0,)*degree}
    choices = {mask: [(j, 1<<j, -1 if (mask>>(j+1)).bit_count()%2 else 1)
                      for j in range(r) if not mask & (1<<j)] for mask in range(1<<r)}
    for i in range(r):
        nxt = {}
        for (a,b,c), values in states.items():
            for j,jb,js in choices[a]:
                for k,kb,ks in choices[b]:
                    for l,lb,ls in choices[c]:
                        x,y = t[i,j,k,l], v[i,j,k,l]
                        if not x and not y:
                            continue
                        key = (a|jb,b|kb,c|lb)
                        if key not in nxt:
                            nxt[key] = [0]*(degree+1)
                        s = js*ks*ls
                        for d in range(degree+1):
                            nxt[key][d] += s*(x*values[d]+(y*values[d-1] if d else 0))
        states = {key: val for key,val in nxt.items() if any(val)}
    return states.get(((1<<r)-1,)*3, [0]*(degree+1))


def covariant_tensors(t, r):
    v = [t[i,0,0,0] for i in range(r)]
    m = [[t[i,j,0,0] for j in range(r)] for i in range(r)]
    vv, w = {}, {}
    for i,j,k,l in product(range(r), repeat=4):
        vv[i,j,k,l] = m[i][j]*m[k][l]+m[i][k]*m[j][l]+m[i][l]*m[j][k]
        w[i,j,k,l] = (m[i][j]*v[k]*v[l]+m[i][k]*v[j]*v[l]+m[i][l]*v[j]*v[k]
                        +m[j][k]*v[i]*v[l]+m[j][l]*v[i]*v[k]+m[k][l]*v[i]*v[j])
    return vv,w


def values(coeffs, r=6):
    t = tensor(coeffs,r)
    v,w = covariant_tensors(t,r)
    a = hyperdet_series(t,v,r,2)
    b = hyperdet_series(t,w,r,1)
    c0 = coeffs.get((4,)+(0,)*(r-1),0)
    require(a[0] == b[0], 'series constant control')
    return [c0*c0*a[0], c0*a[1], a[2], b[1]]


def det_bareiss(a):
    a = [row[:] for row in a]
    n = len(a)
    s, divisor = 1,1
    for k in range(n-1):
        pivot = next((j for j in range(k,n) if a[j][k]),None)
        if pivot is None:
            return 0
        if pivot != k:
            a[pivot],a[k] = a[k],a[pivot]
            s = -s
        p = a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num = a[i][j]*p-a[i][k]*a[k][j]
                require(num % divisor == 0, 'Bareiss exact division')
                a[i][j] = num//divisor
            a[i][k] = 0
        divisor = p
    return s*a[-1][-1]


def main():
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    require(not a.output.exists(), 'preserve pilot output')
    rnd = random.Random(1510)
    points = [skew_pencil()]+[[[[rnd.randint(-2,2) for _ in range(4)]
                               for _ in range(4)] for _ in range(6)] for _ in range(3)]
    rows=[]
    start=time.perf_counter()
    for i,point in enumerate(points):
        row=values(pencil_coefficients(point))
        rows.append(row)
        print(json.dumps(dict(point=i,values=row,elapsed=time.perf_counter()-start)),flush=True)
    result=dict(status='CANDIDATE',points=points,matrix=rows,minor_Z=str(det_bareiss(rows)),
                source_names=['c0^2 H(T)','c0 [z]H(T+z V)','[z^2]H(T+z V)','[z]H(T+z W)'],
                wall_seconds=time.perf_counter()-start)
    a.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('points','matrix')}))


if __name__=='__main__':
    main()
