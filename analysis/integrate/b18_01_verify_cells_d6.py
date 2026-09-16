import itertools
exec(open('verify_b18_01_deg5.py').read().split('for d in (2,3,4,5):')[0])

# --- d = 6 claim: 105 five-row cells, 38 with a = 1, largest a = 7
M6 = plethysm_monomial_coeffs(6)
lams6 = [l for l in partitions_into_at_most(24, NVAR) if l[4] > 0]
live6 = [(l, schur_coeff(M6,l)) for l in lams6]
live6 = [(l,a) for l,a in live6 if a > 0]
print(f"d=6  five-row cells with a>0: {len(live6)}   with a==1: {sum(1 for _,a in live6 if a==1)}   max a: {max(a for _,a in live6)}")

# --- K(lambda) = weight multiplicity, spot-checked against the report's table
M5 = plethysm_monomial_coeffs(5)
claimed = {(12,2,2,2,2):553,(9,7,2,1,1):621,(11,4,2,2,1):705,(10,5,3,1,1):774,
           (10,5,2,2,1):1008,(8,7,3,1,1):1091,(9,5,4,1,1):1215,(9,6,2,2,1):1275,
           (7,7,4,1,1):1564,(8,5,5,1,1):1610,(10,4,2,2,2):1761,(9,5,3,2,1):1860,
           (9,4,4,2,1):2123,(8,6,3,2,1):2261,(8,5,4,2,1):2825,(8,6,2,2,2):2972,
           (7,6,4,2,1):3260,(7,5,4,3,1):4807,(8,4,4,2,2):4988,(7,4,4,4,1):5490,
           (6,6,4,2,2):6869,(6,4,4,4,2):11640,(4,4,4,4,4):19834}
bad=[(l,c,M5.get(l,0)) for l,c in claimed.items() if M5.get(l,0)!=c]
print(f"K(lambda) table: {len(claimed)-len(bad)}/{len(claimed)} agree" + (f"  MISMATCH {bad}" if bad else ""))

# --- the slot's own control: sum_lambda a * dim S_lambda(C^5) = C(69+d, d)
from math import comb
def dim_schur(lam):
    num=den=1
    for i in range(5):
        for j in range(i+1,5):
            num*= (lam[i]-lam[j]+j-i); den*= (j-i)
    return num//den
for d in (2,3,4,5,6):
    Md = M5 if d==5 else (M6 if d==6 else plethysm_monomial_coeffs(d))
    tot=sum(schur_coeff(Md,l)*dim_schur(l) for l in partitions_into_at_most(4*d,NVAR))
    print(f"  control d={d}: sum a*dim = {tot:>12}   C(69+d,d) = {comb(69+d,d):>12}   {'OK' if tot==comb(69+d,d) else 'FAIL'}")

# --- Prop 8.4 arithmetic
r=(4,-1,-1,-1,-1); mu=(4,4,4,4,4)
print("\nProp 8.4:  <mu,r> =", sum(m*x for m,x in zip(mu,r)), "(must be 0)")
worst=min(4*(1+b0)-(3-b0) for b0 in range(4))
print("           min over cubics C of <e_0+beta, r> =", worst, "(must be > 0)")
