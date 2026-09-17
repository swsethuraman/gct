"""Read the stored polynomial and pencil; verify without importing its producer."""
import itertools
import json
import math
from collections import defaultdict
from pathlib import Path

HERE=Path(__file__).resolve().parent
data=json.loads(HERE.joinpath('five_row_pilot.json').read_text())
terms=data['coefficient_polynomial']
lam=tuple(data['lambda'])
derivative_sizes=[]
for i in range(4):
    residue=defaultdict(int)
    for term in terms:
        factors=[tuple(a) for a in term['factors']]
        assert len(factors)==6 and all(sum(a)==4 for a in factors)
        assert tuple(map(sum,zip(*factors)))==lam
        for k,a in enumerate(factors):
            if a[i+1]:
                aa=list(a)
                aa[i]+=1
                aa[i+1]-=1
                ff=factors[:k]+[tuple(aa)]+factors[k+1:]
                residue[tuple(sorted(ff))]+=term['coefficient']*(a[i]+1)
    derivative_sizes.append(len(residue))
    assert not any(residue.values())

pencil=data['determinant_point']['A']
f=defaultdict(int)
for perm in itertools.permutations(range(4)):
    s=(-1)**sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
    for labels in itertools.product(range(5),repeat=4):
        coeff=s*math.prod(pencil[i][perm[i]][labels[i]] for i in range(4))
        exponent=tuple(labels.count(i) for i in range(5))
        f[exponent]+=coeff
value=sum(term['coefficient']*math.prod(f[tuple(a)] for a in term['factors']) for term in terms)
assert value==data['determinant_value'] and value!=0
result={'all_passed':True,'polynomial_terms':len(terms),'raising_residues_zero':True,
        'populated_derivative_monomials':derivative_sizes,'determinant_value':value,
        'ambient_multiplicity_one':'inherited from pinned exact character table; not recomputed'}
HERE.joinpath('five_row_verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
