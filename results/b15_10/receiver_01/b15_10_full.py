"""Full four-source geometric certificate and stdlib receiver, B15-10."""
import argparse
import copy
from itertools import permutations, product
import json
from math import factorial, prod
from pathlib import Path
import random
import sys
import time

# Resolve only these portable companion modules even when a runner prepends
# another analysis directory. A receiver needs this file and its two companions.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from b15_10_witness import (PRIMES, require, pencil_coefficients, polynomial_product,
                            tensor, hyperdet, brute_hyperdet, sign, sizing)
from b15_10_extend import values, det_bareiss, hyperdet_series, covariant_tensors

CELL = dict(n=4, delta=8, ell=6, ambient_variables=16, partition=[12,4,4,4,4,4])
SOURCES = dict(tensor='T_ijkl = product(alpha_j!) * ordinary_c_alpha; alpha counts i,j,k,l',
               flag_index=0, vector='v_i = T_i000', matrix='M_ij = T_ij00',
               V='V_ijkl = M_ij M_kl + M_ik M_jl + M_il M_jk',
               W='W_ijkl = M_ij v_k v_l + M_ik v_j v_l + M_il v_j v_k + M_jk v_i v_l + M_jl v_i v_k + M_kl v_i v_j',
               H='H(S) = sum_(sigma,tau,upsilon in S6) sgn(sigma)sgn(tau)sgn(upsilon) product_(i=0..5) S_i,sigma(i),tau(i),upsilon(i)',
               H_epsilon_divisor=720,
               polynomials=['c400000^2 H(T)', 'c400000 [z]H(T+z V)',
                            '[z^2]H(T+z V)', '[z]H(T+z W)'],
               weight_convention='Sym^8(Sym^4 V), positive coefficient-functional weights',
               row_orientation='points', column_orientation='polynomials in listed order',
               label_indexing='zero-based', arithmetic='integer coefficients; no modular source')


def padded_coefficients(frame):
    require(len(frame) == 6 and all(len(row) == 10 and all(type(x) is int and
            abs(x) <= 10**6 for x in row) for row in frame), 'six by ten integer pad frame')
    c = pencil_coefficients([[row[1+3*j:1+3*(j+1)] for j in range(3)]
                            for row in frame], permanent=True)
    ell = {tuple(int(i == j) for i in range(6)): frame[j][0]
           for j in range(6) if frame[j][0]}
    return polynomial_product(ell,c)


def coeff_record(c):
    return [[list(a),v] for a,v in sorted(c.items())]


def make_certificate(pilot):
    rnd=random.Random(151037)
    frame=[[rnd.randint(-2,2) for _ in range(10)] for _ in range(6)]
    pad=values(padded_coefficients(frame))
    require(any(pad), 'padded pilot is zero; retain and report before changing point')
    matrix=[values(pencil_coefficients(point)) for point in pilot['points']]
    require(matrix==pilot['matrix'], 'pilot replay')
    d=det_bareiss(matrix)
    cert=dict(format='b15-10-full-integral/1', actual_model='gpt-6-astra',
              cell=CELL, sources=SOURCES,
              determinant_points=[dict(family='det4_integer_pencil', pencil=point,
                                        ordinary_coefficients=coeff_record(pencil_coefficients(point)))
                                  for point in pilot['points']],
              determinant_matrix_Z=matrix, determinant_minor_Z=str(d),
              determinant_minor_mod_p={str(p):d%p for p in PRIMES},
              padded_point=dict(family='z_times_per3', source_ambient_variables=10,
                                frame_orientation='six variable rows; columns z,a11,a12,a13,a21,a22,a23,a31,a32,a33',
                                frame=frame, ordinary_coefficients=coeff_record(padded_coefficients(frame))),
              padded_values_Z=pad, padded_minor_column=next(i for i,v in enumerate(pad) if v),
              inherited_bounds=dict(a_ub=4,h_pad_ub=1),
              inherited_bound_source='results/b15_prep/Q1_combined_bound.json',
              conclusion=dict(r_det_lb=4,r_pad_lb=1,m_det_lb=4,m_det_ub=4,
                              m_pad_lb=1,m_pad_ub=1,i_det_lb=0,i_det_ub=0,
                              i_pad_lb=3,i_pad_ub=3,D_lb=-3,D_ub=-3))
    return cert


def verify(cert):
    require(cert['format']=='b15-10-full-integral/1','format')
    require(cert['cell']==CELL,'cell')
    require(cert['sources']==SOURCES,'source construction or normalization')
    require(cert['inherited_bounds']==dict(a_ub=4,h_pad_ub=1),'inherited bounds')
    require(cert['inherited_bound_source']=='results/b15_prep/Q1_combined_bound.json','bound provenance')
    require(len(cert['determinant_points'])==4,'four explicit determinant points')
    matrix=[]
    for point in cert['determinant_points']:
        require(point['family']=='det4_integer_pencil','determinant family')
        require(len(point['pencil'])==6 and len(point['pencil'][0])==4,'det4 pencil dimensions')
        c=pencil_coefficients(point['pencil'])
        require(coeff_record(c)==point['ordinary_coefficients'],'determinant coefficients')
        matrix.append(values(c))
    require(matrix==cert['determinant_matrix_Z'],'fresh determinant evaluations')
    d=det_bareiss(matrix)
    require(d and str(d)==cert['determinant_minor_Z'],'nonzero determinant minor')
    independent=sum(sign(p)*prod(matrix[i][p[i]] for i in range(4)) for p in permutations(range(4)))
    require(d==independent,'Bareiss and Leibniz agreement')
    require(cert['determinant_minor_mod_p']=={str(p):d%p for p in PRIMES},'minor residues')
    point=cert['padded_point']
    require(point['family']=='z_times_per3' and point['source_ambient_variables']==10,'true pad family')
    require(point['frame_orientation']=='six variable rows; columns z,a11,a12,a13,a21,a22,a23,a31,a32,a33','pad orientation')
    c=padded_coefficients(point['frame'])
    require(coeff_record(c)==point['ordinary_coefficients'],'padded coefficients')
    pad=values(c)
    require(pad==cert['padded_values_Z'],'fresh padded evaluations')
    j=cert['padded_minor_column']
    require(type(j) is int and 0<=j<4 and pad[j]!=0,'padded nonzero minor')
    conclusion=dict(r_det_lb=4,r_pad_lb=1,m_det_lb=4,m_det_ub=4,
                    m_pad_lb=1,m_pad_ub=1,i_det_lb=0,i_det_ub=0,
                    i_pad_lb=3,i_pad_ub=3,D_lb=-3,D_ub=-3)
    require(cert['conclusion']==conclusion,'conclusion mismatch')
    return dict(status='EXACT', geometric_replay=True, determinant_minor_Z=str(d),
                determinant_minor_mod_p={str(p):d%p for p in PRIMES},
                padded_minor_Z=str(pad[j]), padded_minor_column=j,
                conclusion=conclusion, inherited_premises=cert['inherited_bounds'],
                source_lifting='not needed: all four polynomials are integral before evaluation',
                verifier_modules=[str(Path(__file__).resolve()),
                                  str(Path(sys.modules['b15_10_witness'].__file__).resolve()),
                                  str(Path(sys.modules['b15_10_extend'].__file__).resolve())],
                resource_sizing=dict(**sizing(6), series_degree_max=2,
                                     integer_entries_per_live_state_max=3,
                                     symbolic_permutation_expansion_allocated=False))


def controls(cert):
    checks=[]
    # Independent direct permutation evaluation and polynomial-series expansion,
    # with r=3 but the same normalization, tensor construction and recurrences.
    rnd=random.Random(151099)
    c={a:rnd.randint(-3,3) for a in product(range(5),repeat=3) if sum(a)==4}
    t=tensor(c,3);v,w=covariant_tensors(t,3)
    require(hyperdet(t,3)[0]==brute_hyperdet(t,3),'direct permutation control')
    for direction,degree in ((v,2),(w,1)):
        direct=[0]*(degree+1)
        for p,q,s in product(list(permutations(range(3))),repeat=3):
            terms=[1]+[0]*degree
            for i in range(3):
                x,y=t[i,p[i],q[i],s[i]],direction[i,p[i],q[i],s[i]]
                terms=[x*terms[d]+(y*terms[d-1] if d else 0) for d in range(degree+1)]
            for d in range(degree+1):
                direct[d]+=sign(p)*sign(q)*sign(s)*terms[d]
        require(direct==hyperdet_series(t,direction,3,degree),'direct truncated series control')
    checks.append(dict(name='independent_small_permutation_and_series',status='EXACT'))
    require(brute_hyperdet(t,3,signed=False)!=hyperdet(t,3)[0],'altered signs must be detected')
    require(hyperdet(tensor(c,3,normalized=False),3)[0]!=hyperdet(t,3)[0],
            'altered normalization must be detected')
    checks.append(dict(name='altered_sign_and_tensor_factorials',rejected=True))
    # Separate liveness: diagonal quartic sum_i x_i^4 has H(T)=24^r.
    diagonal={tuple(4*int(i==j) for i in range(6)):1 for j in range(6)}
    require(hyperdet(tensor(diagonal,6),6)[0]==24**6,'separate quartic liveness')
    checks.append(dict(name='sum_of_six_fourth_powers_liveness',value_Z=24**6,status='EXACT'))
    # Weight and simple-root invariance on a full generic determinant pencil.
    base=cert['determinant_points'][1]['pencil'];base_values=values(pencil_coefficients(base))
    for i in range(5):
        point=copy.deepcopy(base)
        point[i+1]=[[point[i+1][j][k]+2*point[i][j][k] for k in range(4)] for j in range(4)]
        require(values(pencil_coefficients(point))==base_values,'simple-root shear control')
    for i in (0,1,5):
        point=copy.deepcopy(base)
        point[i]=[[2*x for x in row] for row in point[i]]
        require(values(pencil_coefficients(point))==[2**CELL['partition'][i]*x for x in base_values],
                'torus weight control')
    checks.append(dict(name='five_raising_shears_and_three_weight_scalings',status='EXACT',
                       scope='point controls; global highest-weight identity proved from epsilon tensors'))
    zero=[[[0]*4 for _ in range(4)] for _ in range(6)]
    diagonal_point=[[[base[a][i][j] if i==j else 0 for j in range(4)] for i in range(4)] for a in range(6)]
    require(values(pencil_coefficients(zero))==[0]*4,'zero family')
    require(values(pencil_coefficients(diagonal_point))==[0]*4,'four-factor family forced zero')
    checks.append(dict(name='zero_and_four_factor_determinant_families',values=[0]*4,status='EXACT'))
    # Honest mutations, running the geometric verifier each time.
    mutations=[('altered_source',lambda b:b['sources'].__setitem__('H_epsilon_divisor',1)),
               ('altered_normalization',lambda b:b['sources'].__setitem__('tensor','ordinary coefficients')),
               ('altered_point',lambda b:b['determinant_points'][0]['pencil'][0][0].__setitem__(1,7)),
               ('altered_matrix',lambda b:b['determinant_matrix_Z'][0].__setitem__(0,1)),
               ('altered_minor',lambda b:b.__setitem__('determinant_minor_Z','1')),
               ('false_padded_minor',lambda b:b.__setitem__('padded_minor_column',0)),
               ('wrong_cell',lambda b:b['cell'].__setitem__('delta',9)),
               ('missing_native_point',lambda b:b['determinant_points'][0].pop('pencil'))]
    for name,mutate in mutations:
        bad=copy.deepcopy(cert);mutate(bad)
        try:
            verify(bad)
        except (ValueError,KeyError,TypeError,IndexError):
            checks.append(dict(name=name,rejected=True))
        else:
            raise ValueError('mutation was not rejected: '+name)
    return dict(status='EXACT',checks=checks)


def main():
    p=argparse.ArgumentParser()
    p.add_argument('mode',choices=('produce','verify','controls'))
    p.add_argument('--certificate',type=Path,required=True)
    p.add_argument('--pilot',type=Path)
    p.add_argument('--receipt',type=Path)
    a=p.parse_args();start=time.perf_counter()
    if a.mode=='produce':
        require(not a.certificate.exists(),'preserve existing certificate')
        cert=make_certificate(json.loads(a.pilot.read_text(encoding='utf-8')))
        result=verify(cert)
        a.certificate.write_text(json.dumps(cert,indent=2)+'\n',encoding='utf-8')
    else:
        cert=json.loads(a.certificate.read_text(encoding='utf-8'))
        result=verify(cert) if a.mode=='verify' else controls(cert)
    result['wall_seconds']=time.perf_counter()-start
    if a.receipt:
        require(not a.receipt.exists(),'preserve receipt')
        a.receipt.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__':
    main()
