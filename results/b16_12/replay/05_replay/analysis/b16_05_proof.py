"""Exact small arithmetic for the universal split-Hessian remainder identities.

Formal reductions use integer coefficient dictionaries, not sampled zeros.
One genuine ambient quartic jet provides an integer nonzero for E3.
Run with b15_bound.py, -B,60s/512MiB from this worktree.
"""
from collections import defaultdict
from fractions import Fraction as Q
import itertools
import json
import random
import time
from b16_05_receiver import (HERE, OUT, P, POINTS, inputs, read, save, modules,
                            cubic_terms, family_jets, hessian_control)


def symbolic_remainders():
    # Monomials in (s2,s3,s4), ascending t-coefficients.
    powers=[]
    for k in range(8):
        row=[{} for _ in range(4)]
        if k<4:
            row[k][(0,0,0)]=1
        else:
            for decrement,index in [(2,0),(3,1),(4,2)]:
                for j in range(4):
                    for exp,c in powers[k-decrement][j].items():
                        new=list(exp);new[index]+=1;new=tuple(new)
                        row[j][new]=row[j].get(new,0)-c
            row=[{e:c for e,c in d.items() if c} for d in row]
        powers.append(row)
    expected=[
        [(0,(0,0,0),1),(4,(0,0,1),-1),(6,(1,0,1),1),(7,(0,1,1),1)],
        [(1,(0,0,0),1),(4,(0,1,0),-1),(5,(0,0,1),-1),(6,(1,1,0),1),(7,(1,0,1),1),(7,(0,2,0),1)],
        [(2,(0,0,0),1),(4,(1,0,0),-1),(5,(0,1,0),-1),(6,(2,0,0),1),(6,(0,0,1),-1),(7,(1,1,0),2)],
        [(3,(0,0,0),1),(5,(1,0,0),-1),(6,(0,1,0),-1),(7,(2,0,0),1),(7,(0,0,1),-1)]]
    found=[]
    for j in range(4):
        row=[(k,e,c) for k in range(8) for e,c in powers[k][j].items()]
        assert sorted(row)==sorted(expected[j])
        assert all(2*e[0]+3*e[1]+4*e[2]+38-k==38-j for k,e,c in row)
        found.append(row)
    # Equalities E=0 cut precisely the multiples of the monic p in degree<8:
    # leading coefficient1 on S0,S1,S2,S3 gives an identity4x4 block.
    # No claim that these four functions have independent images in one weight.
    return {'variable_order':['s2','s3','s4'],
            'term_format':['S_index','scalar_exponents','integer_coefficient'],
            'relations':found,'formal_rank_over_Q_s2_s3_s4':4,
            'formal_kernel_dimension':4,'slice_weights':[38,37,36,35]}


def interpolate(values):
    values=list(map(Q,values)); out=[Q(0)]*len(values); basis=[Q(1)]
    for k in range(len(values)):
        for j,x in enumerate(basis):out[j]+=values[0]*x
        values=[values[i+1]-values[i] for i in range(len(values)-1)]
        nxt=[Q(0)]*(len(basis)+1)
        for j,x in enumerate(basis):
            nxt[j]-=k*x/(k+1);nxt[j+1]+=x/(k+1)
        basis=nxt
    return out


def rem(a,p):
    a=list(map(Q,a))
    for k in range(len(a)-1,len(p)-2,-1):
        v=a[k]/p[-1]
        for j,x in enumerate(p):a[k-len(p)+1+j]-=v*x
    return a[:len(p)-1]


def exact_nonzero(flint):
    rng=random.Random(160505)
    N={}
    for d in [2,3,4]:
        M=[[0]*9 for _ in range(9)]
        for i in range(9):
            for j in range(i,9):M[i][j]=M[j][i]=rng.randint(-3,3)
        N[d]=M
    s={d:N[d][0][0] for d in N}
    u={d:[row[0] for row in N[d]] for d in N}
    Dvalues=[]
    for t in range(21):
        B=[[2*t*t*N[2][i][j]+6*t*N[3][i][j]+12*N[4][i][j] for j in range(9)] for i in range(9)]
        v=[4*t*u[2][i]+3*u[3][i] for i in range(9)]
        H=[[12*t*t+2*s[2]]+v]+[[v[i]]+B[i] for i in range(9)]
        Dvalues.append(int(flint.fmpz_mat(H).det()))
    D=interpolate(Dvalues)
    assert all(x.denominator==1 for x in D)
    assert all(sum(x*t**j for j,x in enumerate(D))==v for t,v in enumerate(Dvalues))
    p=[s[4],s[3],s[2],0,1]
    square=[sum(p[j]*p[k-j] for j in range(5) if 0<=k-j<5) for k in range(9)]
    S=rem(D,square)
    E3=S[3]-s[2]*S[5]-s[3]*S[6]+(s[2]**2-s[4])*S[7]
    assert E3==rem(D,p)[3]!=0
    # Every symmetric N_d is realized by a symmetric tensor with
    # T_(i,j,0,...,0)=N_d[i,j], with unused entries set zero. Euler ties agree.
    return {'seed':160505,'N':N,'s':s,'D_values':Dvalues,
            'D_coefficients':list(map(int,D)),'S_coefficients':list(map(int,S)),
            'E3':int(E3),'coefficient_c':1,
            'finite_lift_degree':27,'finite_weight':[73,19]+[2]*8,
            'realization':'For each d, symmetric tensor T[i,j,0^(d-2)]=N_d[i,j]; other entries0. F=t^4+f2*t^2+f3*t+f4.'}


def support_pricing():
    # A direct generic source image uses100 L entries and165 cubic coefficients.
    # Stable bracket safe c^35 lift pulls back to bidegree(35,35) in(l,C).
    # With C precomposed by9 forms, its coefficient pullback has total L-degree140.
    # Stars and bars is only a dense ceiling: no allocation follows from it.
    from math import comb
    # Normalize cubic jets in a two-dimensional source plane:4 binary cubic
    # coefficients,3*7 first transverse and2*28 second transverse coefficients.
    two_jet=4+3*7+2*comb(8,2)
    return {'generic_cubic_coefficients':165,'linear_substitution_entries':100,
            'line_cubic_2jet_coefficients_before_coordinate_relations':two_jet,
            'formal_quotient_relations_to_certify':186,
            'extra_dimension_loss_beyond_source_ceiling':288-243,
            'naive_expanded_pullback_L_degree':140,'naive_expanded_pullback_C_degree':35,
            'dense_monomial_ceiling_L':comb(239,99),'dense_monomial_ceiling_C':comb(199,164),
            'dense_joint_ceiling':comb(239,99)*comb(199,164),
            'authorization':'No dense carrier allocated or priced as feasible; sparse symbolic image requires a separate support preflight and lease if above60s/512MiB.'}


def essential_rank(terms,flint):
    derivatives=[defaultdict(int) for _ in range(10)]
    for c,mon in terms:
        padded=(0,)+tuple(i+1 for i in mon)
        for k,i in enumerate(padded):
            derivatives[i][padded[:k]+padded[k+1:]]+=c
    columns=sorted(set().union(*(set(d) for d in derivatives)))
    matrix=[[d.get(col,0) for col in columns] for d in derivatives]
    rank=int(flint.fmpz_mat(matrix).rank())
    assert rank==10
    return {'rank':rank,'matrix_shape':[10,len(columns)],
            'method':'Exact integer rank of complete first-partial coefficient matrix of native z*C; invertible L preserves rank.'}


def restriction_minors(np,flint,geo,br,pts):
    saved=read('control.json')
    L=np.array(saved['L'],dtype=np.int64)
    out={}
    for family in ['SPLIT','PAD']:
        ts=[cubic_terms(family,saved['split_coefficients'][k]) for k in range(POINTS)]
        essential=[essential_rank(t,flint) for t in ts]
        reds,cs,shifts=family_jets(L,ts,np,geo,br,pts)
        hs=[hessian_control(reds[k],L[:,:,k].tolist(),cs[k],shifts[k],ts[k],br) for k in range(POINTS)]
        assert hs==saved['families'][family]['hessian']
        values=[h['S_weight35'] for h in hs]
        # Points by the five functions E=(S3,s2*S5,s3*S6,s4*S7,s2^2*S7).
        minor=geo.minor_certificate(values,P)
        assert minor['rank_lb']==4
        assert all(row[0]-row[1]-row[2]-row[3]+row[4] == 0 or
                   (row[0]-row[1]-row[2]-row[3]+row[4])%P==0 for row in values)
        finite=[[v*pow(cs[k],27,P)%P for v in row] for k,row in enumerate(values)]
        finite_minor=br.det_mod([[finite[i][j] for j in minor['columns']] for i in minor['rows']],P)
        assert finite_minor!=0
        assert finite_minor == minor['determinant_mod_p']*math_product(pow(cs[i],27,P) for i in minor['rows'])%P
        out[family]={'prime':P,'function_order':['S3','s2*S5','s3*S6','s4*S7','s2^2*S7'],
                     'points_by_functions':values,'minor':minor,'finite_degree27_minor':finite_minor,
                     'global_restriction_upper':4,'exact_restriction_rank':4,
                     'kernel_vector':[1,-1,-1,-1,1],
                     'essential_variable_checks':essential,
                     'ambient_dimension5':'Inherited accepted Hessian11 source and independence proof',
                     'fresh_native_Hessian_replay':True}
    return out


def math_product(seq):
    value=1
    for x in seq:value*=x
    return value


def main():
    np,flint,geo,br,pts=modules()
    before=inputs()
    assert before==read('preflight.json')['input_hashes']
    result={'status':'EXACT_FORMAL_REDUCTION_AND_AMBIENT_NONZERO',
            'formal':symbolic_remainders(),'ambient_nonzero':exact_nonzero(flint),
            'five_space_restriction':restriction_minors(np,flint,geo,br,pts),
            'source_pricing':support_pricing(),'input_hashes':before,
            'proof_source':'docs/b16_05_proof.md'}
    assert inputs()==before
    save('proof_arithmetic.json',result)
    print(json.dumps({'status':result['status'],'E3':result['ambient_nonzero']['E3'],
                      'line_cubic_2jet_coefficients':result['source_pricing']['line_cubic_2jet_coefficients_before_coordinate_relations']}))


if __name__=='__main__':main()
