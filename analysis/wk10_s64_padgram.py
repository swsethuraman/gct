#!/usr/bin/env python3
"""Independent reproduction of S3's padded Gram at delta = 2 (integrator note 1).

    K_pad(G) = sum_{M_0 in PM(G)}  E_3(G - M_0)^2
    E_3(H)   = sum_{M_1 in PM(H)}  2^{c(H - M_1)}

over the degree-4 bipartite overlap multigraph G of two Foulkes block partitions.
At delta = 2 each partition is [8] into two blocks of size 4; G is the 2+2
bipartite multigraph whose edge (i,j) has multiplicity |P_i cap Q_j|, so the
overlap type is the 2x2 table [[a,4-a],[4-a,a]] with a = 0,1,2 up to symmetry:
(0,4), (1,3), (2,2).  Edges are the 8 elements (labelled), so perfect matchings
and edge removals are on labelled edges.  c(.) is the number of connected
components of the 2+2 bipartite multigraph.

Expected (integrator, reproduced from the formula, sharing no code):
    (0,4): 20736    (1,3): 2592    (2,2): 1152
"""
import itertools


def components(edges, verts=('P0', 'P1', 'Q0', 'Q1')):
    """connected components of the multigraph with vertex set verts and the given
    (u,v) edges."""
    parent = {v: v for v in verts}
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    for u, v, _lab in edges:
        parent[find(u)] = find(v)
    return len({find(v) for v in verts})


def perfect_matchings(edges):
    """all perfect matchings of the 2+2 bipartite multigraph given as labelled
    edges (u='P0'/'P1', v='Q0'/'Q1', label).  A PM = 2 edges covering all 4
    vertices."""
    out = []
    for e1, e2 in itertools.combinations(edges, 2):
        us = {e1[0], e2[0]}; vs = {e1[1], e2[1]}
        if us == {'P0', 'P1'} and vs == {'Q0', 'Q1'}:
            out.append((e1, e2))
    return out


def E3(H):
    tot = 0
    for M1 in perfect_matchings(H):
        rem = [e for e in H if e not in M1]
        tot += 2 ** components(rem)
    return tot


def K_pad(edges):
    tot = 0
    for M0 in perfect_matchings(edges):
        H = [e for e in edges if e not in M0]
        tot += E3(H) ** 2
    return tot


def edges_for_type(a):
    """8 labelled edges realising overlap table [[a,4-a],[4-a,a]]:
    P0∩Q0 = a, P0∩Q1 = 4-a, P1∩Q0 = 4-a, P1∩Q1 = a."""
    mults = {('P0', 'Q0'): a, ('P0', 'Q1'): 4 - a, ('P1', 'Q0'): 4 - a, ('P1', 'Q1'): a}
    edges = []; lab = 0
    for (u, v), m in mults.items():
        for _ in range(m):
            edges.append((u, v, lab)); lab += 1
    assert len(edges) == 8
    return edges


def main():
    expected = {0: 20736, 1: 2592, 2: 1152}
    print("overlap type   K_pad   expected   match")
    ok = True
    for a in (0, 1, 2):
        k = K_pad(edges_for_type(a))
        typ = f"({a},{4-a})"
        m = (k == expected[a]); ok = ok and m
        print(f"  {typ:8s}   {k:6d}   {expected[a]:6d}   {'YES' if m else 'NO'}")
    print("padded Gram delta=2:", "PASS -- all three orbital values reproduced" if ok else "FAIL")
    return ok


if __name__ == '__main__':
    import sys
    sys.exit(0 if main() else 1)
