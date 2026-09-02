# Session 39 — P1 reduction validation (reproduce s36 ledger cells + witness)

- witness `l^3 m` (4,4) d2, p=2147483647: a=1 kernel (12,-3,1) ok
- witness `l^3 m` (4,4) d2, p=2147483629: a=1 kernel (12,-3,1) ok

- `(8, 4, 4, 4, 4)` d6: got {'a': 2, 'N_S': 94675, 'stab': 24, 'n_chi': 4562, 'mult_det': 2, 'mult_pad': 1} vs ledger {'a': 2, 'N_S': 94675, 'stab': 24, 'n_chi': 4562, 'mult_det': 2, 'mult_pad': 1} — ok [96s]
- `(11, 4, 4, 4, 1)` d6: got {'a': 2, 'N_S': 11574, 'stab': 6, 'n_chi': 2113, 'mult_det': 2, 'mult_pad': 2} vs ledger {'a': 2, 'N_S': 11574, 'stab': 6, 'n_chi': 2113, 'mult_det': 2, 'mult_pad': 2} — ok [135s]
- `(13, 8, 4, 1, 1, 1)` d7: got {'a': 2, 'N_S': 27213, 'stab': 6, 'n_chi': 1844, 'mult_det': 2, 'mult_pad': 2} vs ledger {'a': 2, 'N_S': 27213, 'stab': 6, 'n_chi': 1844, 'mult_det': 2, 'mult_pad': 2} — ok [21s]

**P1: PASS**
