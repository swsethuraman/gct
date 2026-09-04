# s48 raw ranks -- target C, the washout Jacobians

Session 48, `analysis/wk9_s48_washout.py` (m = 2..12) and
`analysis/wk9_s48_washout_hi.py` (m = 13..18, r = 3, 4).  Full Jacobian rank
at ONE integer point PROVES density (Lemma 1, `docs/washout_lemma.md`).
`sharp` = `m^2 r - orbit(m)`, `orbit` = 2m-2 for m >= 3 and 6 for m = 2.

```
# s48 target C -- washout threshold.  Jacobian rank of Phi_{m,r}: (M_m)^r -> Sym^m C^r at a random point, both house primes.
#   naive  bound: m^2 r            >= C(r+m-1, m)
#   sharp  bound: m^2 r - orbit(m) >= C(r+m-1, m),  orbit = 2m-2 (m>=3), 6 (m=2)
  m   r   m^2 r  orbit   sharp   dimSym  count?  rank p1  rank p2  dense?  codim  time
  2   2       8      6       2        3   False        3        3    True      0  0.0s
  2   3      12      6       6        6    True        6        6    True      0  0.0s
  2   4      16      6      10       10    True       10       10    True      0  0.0s
  2   5      20      6      14       15   False       14       14   False      1  0.0s
  3   2      18      4      14        4    True        4        4    True      0  0.0s
  3   3      27      4      23       10    True       10       10    True      0  0.0s
  3   4      36      4      32       20    True       20       20    True      0  0.0s
  3   5      45      4      41       35    True       35       35    True      0  0.0s
  3   6      54      4      50       56   False       50       50   False      6  0.0s
  4   2      32      6      26        5    True        5        5    True      0  0.0s
  4   3      48      6      42       15    True       15       15    True      0  0.0s
  4   4      64      6      58       35    True       35       35    True      0  0.0s
  4   5      80      6      74       70    True       70       70    True      0  0.0s
  4   6      96      6      90      126   False       90       90   False     36  0.0s
  5   2      50      8      42        6    True        6        6    True      0  0.0s
  5   3      75      8      67       21    True       21       21    True      0  0.0s
  5   4     100      8      92       56    True       56       56    True      0  0.0s
  5   5     125      8     117      126   False      117      117   False      9  0.1s
  6   2      72     10      62        7    True        7        7    True      0  0.0s
  6   3     108     10      98       28    True       28       28    True      0  0.1s
  6   4     144     10     134       84    True       84       84    True      0  0.1s
  6   5     180     10     170      210   False      170      170   False     40  0.2s
  7   2      98     12      86        8    True        8        8    True      0  0.0s
  7   3     147     12     135       36    True       36       36    True      0  0.1s
  7   4     196     12     184      120    True      120      120    True      0  0.2s
  7   5     245     12     233      330   False      233      233   False     97  0.3s
  8   2     128     14     114        9    True        9        9    True      0  0.2s
  8   3     192     14     178       45    True       45       45    True      0  0.2s
  8   4     256     14     242      165    True      165      165    True      0  0.4s
  8   5     320     14     306      495   False      306      306   False    189  0.8s
  9   2     162     16     146       10    True       10       10    True      0  0.5s
  9   3     243     16     227       55    True       55       55    True      0  0.6s
  9   4     324     16     308      220    True      220      220    True      0  1.0s
  9   5     405     16     389      715   False      389      389   False    326  1.7s
 10   2     200     18     182       11    True       11       11    True      0  0.9s
 10   3     300     18     282       66    True       66       66    True      0  1.3s
 10   4     400     18     382      286    True      286      286    True      0  2.6s
 10   5     500     18     482     1001   False      482      482   False    519  4.9s
 11   2     242     20     222       12    True       12       12    True      0  1.9s
 11   3     363     20     343       78    True       78       78    True      0  2.8s
 11   4     484     20     464      364    True      364      364    True      0  5.6s
 11   5     605     20     585     1365   False      585      585   False    780  11.0s
 12   2     288     22     266       13    True       13       13    True      0  5.5s
 12   3     432     22     410       91    True       91       91    True      0  8.4s
 12   4     576     22     554      455    True      455      455    True      0  12.5s
 12   5     720     22     698     1820   False      698      698   False   1122  23.4s
```

```
  m   r   m^2 r  orbit   sharp   dimSym  count?  rank p1  rank p2  dense?  codim  time
 13   3     507     24     483      105    True      105      105    True      0  10.0s
 13   4     676     24     652      560    True      560      560    True      0  17.5s
 14   3     588     26     562      120    True      120      120    True      0  24.0s
 14   4     784     26     758      680    True      680      680    True      0  44.4s
 15   3     675     28     647      136    True      136      136    True      0  63.0s
 15   4     900     28     872      816    True      816      816    True      0  117.1s
 16   3     768     30     738      153    True      153      153    True      0  144.0s
 16   4    1024     30     994      969    True      969      969    True      0  279.4s
```
