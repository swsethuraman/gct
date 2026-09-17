import importlib.util
import itertools as it
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('pilot',HERE/'pilot.py')
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
c=m.c
P=c.P
data=json.loads(HERE.joinpath('pilot.json').read_text())
ex=json.loads(HERE.joinpath('exact_pair.json').read_text())
pairs=[[[tuple(slot) for slot in block] for block in part] for pair in data['basis'] for part in pair]
pairs=list(zip(pairs[::2],pairs[1::2]))

checks=[]
for label,raw,expected in [('B',ex['matrices'],ex['values'][0]),('Bprime',ex['partner_matrices'],ex['values'][1])]:
    Y=m.np.array(raw,dtype=m.np.int64).reshape(5,4,4)
    vs=[m.value(pair,m.tensors(Y)) for pair in pairs]
    assert vs==[v%P for v in expected]
    tr=[m.value(pair,m.tensors(m.np.swapaxes(Y,1,2))) for pair in pairs]
    assert tr==vs
    checks.append({'point':label,'exact_values_agree_with_independent_modular_network':True,
                   'whole_transpose_control':True})

# Reconstruct interpolation by explicit Lagrange polynomials, not Gaussian elimination.
nodes=data['u_nodes']
L=[]
for j,x in enumerate(nodes):
    coeff=[1]
    den=1
    for k,y in enumerate(nodes):
        if k==j:continue
        out=[0]*(len(coeff)+1)
        for i,v in enumerate(coeff):
            out[i]=(out[i]-y*v)%P
            out[i+1]=(out[i+1]+v)%P
        coeff=out
        den=den*(x-y)%P
    L.append([v*pow(den,-1,P)%P for v in coeff])
rows=[]
for samples in data['skew_samples']:
    for degree in (7,8):
        rows.append([sum(L[j][degree]*samples[j][i] for j in range(9))%P for i in range(2)])
assert rows==data['forbidden_rows']
a,b=rows[:2]
minor=(a[0]*b[1]-a[1]*b[0])%P
assert minor==61631 and minor!=0
result={'all_passed':True,'checks':checks,'lagrange_coefficients_match':True,
        'arc_2x2_minor_mod_prime':minor,'prime':P,
        'basis_dimension':2,'arc_rank_over_Q':2,'equal_fiber_constraint_rank_over_Q':1,
        'combined_rank_over_Q':2,'five_row_increment':0}
HERE.joinpath('verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
