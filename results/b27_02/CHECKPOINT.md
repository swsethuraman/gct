# B27-02 early checkpoint

2026-09-23T03:53Z (before the 45-minute checkpoint).

**HAND — escape paragraph.** Over C, use the symmetric quartic tensor
q(x)=sum q_ijkl x_i x_j x_k x_l, with no column or label factorials.
There are ten labels, each occurring four times, and shape (24,4,4,4,4).
T1 has four columns (1,2,3,4,5) and four singleton columns (j) for each
j=6,...,10. T2 has two columns (1,2,3,4,5), two columns (6,7,8,9,10),
and two singleton columns (j) for every j=1,...,10. All columns use the
displayed order and the top coordinates. The sole candidate is
f = f_T1 - 567 f_T2. Its effective signs are mixed, so it satisfies the
accepted reopening condition despite both individual tableaux being paired.

**HAND — anticipated exact values, to be replayed.** With A=x1^2+x2^2,
B=x3^2+x4^2+x5^2 and Q=A+B, f(Q^2)=f((A+B/2)^2)=0, whereas
f(p4)=-175/9 for p4=A(A+B). Thus q=p4 and t=0,1/4 certify visibility
of B^2. At the start of rung 2d, b27-01 still had its setup tip
6dea55ec926c1618cc60ad71209795528705bf61 and no committed b27_01 paths;
the brief's fallback p4 is therefore used.

**HAND — determinant-side obstruction.** The normalized pencil with top-left
block x1 I3, last column/row (x3,x4,x5), and last entry x1+x2 has determinant
E=x1^2(x1^2+x1*x2-B). The candidate evaluates to -175/256 on E.
Consequently it is rejected even though both prescribed determinant tests pass.
The complete report will give a hand proof and exact replay. One candidate only.

No five-row determinant equation is known to be nonzero on padding.
