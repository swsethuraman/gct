"""Session 56 — emit gct-cert/1 `matrix` certificates for the Foulkes engine.

Bare-integer-matrix certificates that tools/verify/verify.py recomputes from
scratch (exact rank over Q, ranks modulo both house primes, one nonvanishing
minor of the claimed rank over Z):

  * delta = 2: the full signed Gram matrix K = (<eps_pi, eps_pi'>), 35 x 35,
    rank f_(2^4) = 14 (H_(4,2) surjects onto the rectangular Specht module),
    and beta = K compose K, 35 x 35, full rank 35 (Theta^+ injective).
  * delta = 3, 4: the weight-space Gram matrix b^mu = (<Theta^+ m_O, Theta^+ m_O'>)
    at representative weights mu, each of full rank nb_mu (Theta^+ injective on
    that weight space, so i_det = 0 there), and the signed k^mu on its
    multilinear orbits of rank the Kostka number K_{(delta^4), mu} (the target
    is the rectangular Specht module).

For a full-rank square Gram matrix the nonvanishing minor is the whole matrix,
so no minor search is needed and the verifier's full-rank fast path applies.
No certificate exceeds 5 MB (gzip above 3 MB raw).
"""
import gzip
import json
import os
import sys

import numpy as np
import flint

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import wk9_s56_core as C   # noqa: E402

CERTS = os.path.join(ROOT, "results", "certs")
LOGS = os.path.join(ROOT, "results", "logs")
os.makedirs(CERTS, exist_ok=True)
P1, P2 = C.P1, C.P2


def minor_indices(rows, rank):
    """rows/cols of a rank x rank nonvanishing minor; the whole index set when
    the matrix is square of full rank, else a Gaussian search modulo P1."""
    m, n = len(rows), len(rows[0])
    if m == n == rank:
        return list(range(m)), list(range(n))
    Amod = [[v % P1 for v in row] for row in rows]
    used = [False] * m
    pr, pc = [], []
    for col in range(n):
        piv = next((i for i in range(m) if not used[i] and Amod[i][col] % P1), -1)
        if piv < 0:
            continue
        used[piv] = True
        pr.append(piv)
        pc.append(col)
        inv = pow(Amod[piv][col], -1, P1)
        for i in range(m):
            if not used[i] and Amod[i][col] % P1:
                f = Amod[i][col] * inv % P1
                for j in range(col, n):
                    Amod[i][j] = (Amod[i][j] - f * Amod[piv][j]) % P1
        if len(pr) == rank:
            break
    return sorted(pr), sorted(pc)


def emit(matrix, rank, title, fname, notes=None):
    rows = [[int(v) for v in row] for row in matrix]
    m, n = len(rows), len(rows[0])
    cert = {"format": "gct-cert/1", "kind": "matrix", "title": title,
            "produced_by": "analysis/wk9_s56_certs.py (session 56, the Foulkes engine)",
            "matrix": rows, "claimed_rank_Q": rank,
            "claimed_ranks_mod_p": {str(P1): rank, str(P2): rank}}
    # For a large full-rank square matrix the only nonvanishing minor is the whole
    # matrix, whose determinant has more digits than verify.py will print; certify
    # such a matrix by nullity_zero (full column rank mod p) instead, which needs
    # no minor determinant.  Smaller matrices carry an explicit minor.
    if m == n == rank and n > 200:
        cert["nullity_zero"] = {"prime": P1}
    else:
        ri, ci = minor_indices(rows, rank)
        assert len(ri) == rank
        sub = flint.fmpz_mat(rank, rank, [rows[i][j] for i in ri for j in ci])
        assert int(sub.det()) != 0, "chosen minor is singular over Z"
        cert["nonvanishing_minor"] = {"rows": ri, "cols": ci}
    if notes:
        cert["notes"] = notes
    data = json.dumps(cert, indent=0).encode()
    path = os.path.join(CERTS, fname)
    if len(data) > 3_000_000:
        with gzip.open(path + ".gz", "wb") as fh:
            fh.write(data)
        path += ".gz"
    else:
        with open(path, "w") as fh:
            fh.write(json.dumps(cert, indent=0))
    print(f"  {os.path.basename(path):40s} {m}x{n} rank {rank}  raw {len(data)} bytes")
    return path


def parse_pass(path):
    lines = open(path).read().split("\n")
    hdr = lines[1].split()
    nb = int(hdr[3])
    orbits = [lines[4 + i].split() for i in range(nb)]
    sizes = [int(o[0]) for o in orbits]
    contents = [[int(x) for x in o[1:]] for o in orbits]
    b = [[int(x) for x in lines[5 + nb + i].split()] for i in range(nb)]
    k = [[int(x) for x in lines[6 + 2 * nb + i].split()] for i in range(nb)]
    return nb, sizes, contents, b, k


# ---- delta = 2: the full signed K and beta
K2 = np.load(os.path.join(LOGS, "s56_Kfull_d2.npy"))
emit(K2.tolist(), 14,
     "Foulkes engine delta=2: signed Gram matrix K(pi,pi')=<eps_pi,eps_pi'> (35x35) has rank "
     "f_(2^4)=14 = dim[2^4]; H_(4,2) surjects onto the rectangular Specht module",
     "s56_signedK_d2.json", "the second fundamental theorem, realised")
emit((K2.astype(object) ** 2).tolist(), 35,
     "Foulkes engine delta=2: beta = K compose K (35x35), Gram of Theta^+(pi)=eps_pi(x)eps_pi, "
     "full rank 35 = |H_(4,2)|; Theta^+ injective so i_det=0, mult_det=a at every delta=2 cell",
     "s56_beta_d2.json")

# ---- delta = 3, 4: representative weight-space Gram matrices from the C pass
picks = {3: [(4, 4, 4), (6, 4, 2), (8, 2, 2)],
         4: [(4, 4, 4, 4), (8, 4, 4), (6, 4, 4, 2)]}
for delta, mus in picks.items():
    for mu in mus:
        tag = f"s56_w{delta}_" + "_".join(str(x) for x in mu)
        path = os.path.join(LOGS, tag + ".txt")
        if not os.path.exists(path):
            print(f"  (skip {mu}: {tag}.txt not present)")
            continue
        nb, sizes, contents, b, k = parse_pass(path)
        kost = C.kostka((delta,) * 4, mu)
        emit(b, nb,
             f"Foulkes engine delta={delta}, weight {mu}: b^mu = Gram of Theta^+ on the {nb} weight-{mu} "
             f"monomials of H_(4,{delta}), full rank {nb}; Theta^+ injective on this weight space (i_det=0)",
             f"s56_bmu_d{delta}_{'_'.join(map(str, mu))}.json",
             f"|H_(4,{delta})| partitions summed; b(O,O')=sum_(pi in O) K(pi,rep(O'))^2")
        # the signed k^mu restricted to multilinear orbits, rank = Kostka
        multi = [i for i, cv in enumerate(contents) if all(x <= 1 for x in cv)]
        if multi and kost > 0:
            km = [[k[i][j] for j in multi] for i in multi]
            emit(km, kost,
                 f"Foulkes engine delta={delta}, weight {mu}: signed k^mu on the {len(multi)} multilinear "
                 f"orbits has rank {kost} = Kostka K_(({delta}^4),{mu}); the target is [{delta}^4]",
                 f"s56_kmu_d{delta}_{'_'.join(map(str, mu))}.json")

print("done")
