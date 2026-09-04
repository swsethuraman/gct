# s48 raw output -- target A, the six non-Koszul syzygies

Session 48.  `analysis/wk9_s48_syz.py` (identity (I) and the antisymmetric
family), `analysis/wk9_s48_syzfam.py` (all one-adjugate equivariant words),
`analysis/wk9_s48_syzprobe.py` (the true six, and the vacuity of the next
shape up).  Two pencils, both house primes throughout.

## identity (I): the antisymmetric family
```
(inline run; see s48_syzfam.log fam1 row -- 216 words, 6 syzygies, 0 new)
```

## every one-adjugate equivariant word
```

=== pencil 0, p = 2147483647 ===
  fam1 l*A_a adj(M) A_b             216 words ->   6 syzygies, NEW mod Koszul = 0   [9.4s]
  fam2 M P_B(M) M                    16 words ->   0 syzygies, NEW mod Koszul = 0   [1.6s]
  fam3 F*B                           16 words ->   0 syzygies, NEW mod Koszul = 0   [0.1s]
  fam4 phi_X * M                     16 words ->   0 syzygies, NEW mod Koszul = 0   [1.5s]
  fam5 l*A P_A(M) M / l*M P_A(M) A  432 words -> 222 syzygies, NEW mod Koszul = 0   [18.9s]
  fam6 l*M ADJ(A,A,M) M             126 words ->   0 syzygies, NEW mod Koszul = 0   [5.3s]
  ALL FAMILIES TOGETHER             822 words -> 432 syzygies, NEW mod Koszul = 0   [38.1s]
  (dim Koszul = 90; the true answer is 6 new)

=== pencil 0, p = 2147483629 ===
  fam1 l*A_a adj(M) A_b             216 words ->   6 syzygies, NEW mod Koszul = 0   [7.5s]
  fam2 M P_B(M) M                    16 words ->   0 syzygies, NEW mod Koszul = 0   [1.2s]
  fam3 F*B                           16 words ->   0 syzygies, NEW mod Koszul = 0   [0.1s]
  fam4 phi_X * M                     16 words ->   0 syzygies, NEW mod Koszul = 0   [1.2s]
  fam5 l*A P_A(M) M / l*M P_A(M) A  432 words -> 222 syzygies, NEW mod Koszul = 0   [15.3s]
  fam6 l*M ADJ(A,A,M) M             126 words ->   0 syzygies, NEW mod Koszul = 0   [4.6s]
  ALL FAMILIES TOGETHER             822 words -> 432 syzygies, NEW mod Koszul = 0   [40.7s]
  (dim Koszul = 90; the true answer is 6 new)

=== pencil 1, p = 2147483647 ===
  fam1 l*A_a adj(M) A_b             216 words ->   6 syzygies, NEW mod Koszul = 0   [7.5s]
  fam2 M P_B(M) M                    16 words ->   0 syzygies, NEW mod Koszul = 0   [1.2s]
  fam3 F*B                           16 words ->   0 syzygies, NEW mod Koszul = 0   [0.1s]
  fam4 phi_X * M                     16 words ->   0 syzygies, NEW mod Koszul = 0   [1.3s]
  fam5 l*A P_A(M) M / l*M P_A(M) A  432 words -> 222 syzygies, NEW mod Koszul = 0   [15.7s]
  fam6 l*M ADJ(A,A,M) M             126 words ->   0 syzygies, NEW mod Koszul = 0   [4.3s]
  ALL FAMILIES TOGETHER             822 words -> 432 syzygies, NEW mod Koszul = 0   [47.9s]
  (dim Koszul = 90; the true answer is 6 new)

=== pencil 1, p = 2147483629 ===
  fam1 l*A_a adj(M) A_b             216 words ->   6 syzygies, NEW mod Koszul = 0   [9.2s]
  fam2 M P_B(M) M                    16 words ->   0 syzygies, NEW mod Koszul = 0   [1.5s]
  fam3 F*B                           16 words ->   0 syzygies, NEW mod Koszul = 0   [0.1s]
  fam4 phi_X * M                     16 words ->   0 syzygies, NEW mod Koszul = 0   [1.2s]
  fam5 l*A P_A(M) M / l*M P_A(M) A  432 words -> 222 syzygies, NEW mod Koszul = 0   [17.8s]
  fam6 l*M ADJ(A,A,M) M             126 words ->   0 syzygies, NEW mod Koszul = 0   [5.4s]
  ALL FAMILIES TOGETHER             822 words -> 432 syzygies, NEW mod Koszul = 0   [35.3s]
  (dim Koszul = 90; the true answer is 6 new)
```

## the six themselves, and the vacuous next shape
```

=== pencil seed 20260904, p = 2147483647 ===
(a) dim Syz_7 = 96   dim Koszul = 90   non-Koszul = 6
    extracted 6 representatives of Syz/Koszul
(b) dim J(M)_4 = 66 (of 126);  coefficient forms G_k lying in J(M)_4: 0 of 36
(c) rank W(s) at a random s, over the six: [4, 4, 4, 4, 4, 4]
(d) fam7 q(s)*A_a ADJ(A_b,M,M) A_c : 4536 words, span dim 2016 of 2016  -- VACUOUS (spans everything)

=== pencil seed 20260904, p = 2147483629 ===
(a) dim Syz_7 = 96   dim Koszul = 90   non-Koszul = 6
    extracted 6 representatives of Syz/Koszul
(b) dim J(M)_4 = 66 (of 126);  coefficient forms G_k lying in J(M)_4: 0 of 36
(c) rank W(s) at a random s, over the six: [4, 4, 4, 4, 4, 4]
(d) fam7 q(s)*A_a ADJ(A_b,M,M) A_c : 4536 words, span dim 2016 of 2016  -- VACUOUS (spans everything)
```
