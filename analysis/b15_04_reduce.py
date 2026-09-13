"""Portable block Schur projection, with full-kernel and lifting rank checks.

New B15-04 implementation by gpt-6-astra. Uses banked triangular cover and
ordinary-coefficient source construction, without the banked native C helper.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import time
import numpy as np
from scipy import sparse
from flint import nmod_mat
import b15_04_panel as panel
from wk11_s71_hybrid import nullspace_mod_p, rank_mod_p

ROOT, OUT = panel.ROOT, panel.OUT


def projected_kernel(E, cov, p, a, block=32):
    S, U = cov['S'], cov['U']
    nc, nS, nU = E.shape[1], len(S), len(U)
    m = nU+64
    # Conservative pricing includes G, its dense modular copy, FLINT, list
    # conversion, and another dense nullspace allocation, plus sparse storage.
    sparse_bytes = E.data.nbytes+E.indices.nbytes+E.indptr.nbytes
    estimated_bytes = 72*m*nU+6*sparse_bytes+8*nc*block+256*1024**2
    if estimated_bytes > 1200*1024**2 or nU > 3000:
        raise MemoryError('projected-reduction gate: estimated peak '+str(estimated_bytes)+' bytes; nU='+str(nU))
    t = time.perf_counter()
    cs = np.full(nc, -1, np.int32); cs[S] = np.arange(nS)
    cu = np.full(nc, -1, np.int32); cu[U] = np.arange(nU)
    T, dinv, TU = panel.lean._split_rows_safe(E, cov['rows'], cs, cu, p)
    row_bound = int(np.diff(E.indptr).max(initial=0))*int(np.abs(E.data.astype(np.int64)).max(initial=0))
    assert row_bound*(p-1) < 2**63
    G = np.zeros((m, nU), dtype=np.int64)
    for b0 in range(0, nU, block):
        b1 = min(nU, b0+block)
        width = b1-b0
        X = panel.triangular_solve(T, dinv, TU[:, b0:b1].toarray(), p)
        V = np.zeros((nc, width), dtype=np.int64)
        V[S] = (-X) % p
        V[U[b0:b1]] = np.eye(width, dtype=np.int64)
        assert not np.any((E[cov['rows']] @ V) % p)
        rng = np.random.default_rng(1504001)
        g = np.zeros((m, width), dtype=np.int64)
        for r0 in range(0, E.shape[0], 10000):
            r1 = min(E.shape[0], r0+10000)
            residual = (E[r0:r1] @ V) % p
            choices = rng.integers(0, m, size=(r1-r0, 4))
            signs = rng.integers(0, 2, size=(r1-r0, 4))*2-1
            for j in range(4):
                np.add.at(g, choices[:, j], residual*signs[:, j, None])
                g %= p
        G[:, b0:b1] = g
        print('PROJECTED BLOCK', b1, '/', nU, 'elapsed', round(time.perf_counter()-t, 3), flush=True)
    projected_seconds = time.perf_counter()-t
    digest = hashlib.sha256(G.astype('<i8').tobytes()).hexdigest()
    tnull = time.perf_counter()
    Y = nullspace_mod_p(G, p).T
    nullspace_seconds = time.perf_counter()-tnull
    assert Y.shape == (nU, a), ('projected nullity', Y.shape, 'expected', a)
    assert rank_mod_p(Y, p) == a
    del G
    K = np.zeros((nc, a), dtype=np.int64)
    K[U] = Y
    tu_bound = int(np.diff(TU.indptr).max(initial=0))*int(np.abs(TU.data.astype(np.int64)).max(initial=0))
    assert tu_bound*(p-1) < 2**63
    K[S] = panel.triangular_solve(T, dinv, (-TU @ Y) % p, p)
    for r0 in range(0, E.shape[0], 10000):
        assert not np.any((E[r0:r0+10000] @ K) % p)
    return K, dict(status='EXACT', nS=nS, nU=nU, projected_rows=m, projection_seed=1504001,
                   projection_nonzeros_per_row=4, projected_rank_lb=nU-a, raising_rank_lb=nc-a,
                   kernel_dimension=a, full_raising_verified=True, lifting_gate=True,
                   projected_sha256_little_endian_int64=digest, projected_seconds=projected_seconds,
                   nullspace_seconds=nullspace_seconds, estimated_peak_bytes=estimated_bytes,
                   estimate_method='72*m*nU + 6*CSR bytes + 8*ncols*block + 256 MiB reserve')


def control():
    # A nontrivial residual in this synthetic matrix exercises projection/lifting.
    E = sparse.csr_matrix([[2, 3, 5, 7], [0, 11, 13, 17], [0, 0, 19, 23],
                           [2, 14, 18, 24], [0, 11, 32, 40]], dtype=np.int64)
    cov = dict(S=np.array([0, 1]), U=np.array([2, 3]), rows=np.array([0, 1]))
    records = []
    for p in panel.PRIMES:
        K, info = projected_kernel(E, cov, p, 1, block=1)
        expected, nullity = nmod_mat(E.toarray().tolist(), p).nullspace()
        assert nullity == 1 and nmod_mat(K.tolist(), p).rank() == 1
        assert not np.any((E @ K) % p)
        bad = K.copy(); bad[0, 0] = (bad[0, 0]+1) % p
        assert np.any((E @ bad) % p)
        records.append(dict(prime=p, info=info, altered_source_rejected=True))
    # Reuse the integral (6,2) control to exercise an actual source matrix.
    b = panel.lean.build_cell_lean((6, 2), 2, verbose=False)
    cov = panel.lean.best_cover_lean(b['E'], b['n_chi'])
    K, info = projected_kernel(b['E'], cov, panel.PRIMES[0], 1)
    vals = panel.eval_orbits(b['arr'], panel.det_coefficients(panel.pencil(1504, 2)), panel.PRIMES[0], 2)
    assert int(vals @ K[:, 0] % panel.PRIMES[0]) != 0
    panel.save('reduction_controls.json', dict(status='EXACT', model='gpt-6-astra', cases=records,
                                              actual_source_control=info, actual_source_liveness=True))
    print('PROJECTED REDUCTION CONTROLS PASS', flush=True)


def run(cell):
    tag = 'cell'+str(cell)
    data = np.load(OUT/(tag+'_native.npz'))
    E = sparse.csr_matrix((data['E_data'], data['E_indices'], data['E_indptr']), shape=tuple(data['E_shape']))
    arr = dict(M=data['M'], col_of=data['col_of'], sgn=data['sgn'], n_chi=E.shape[1])
    z = np.load(OUT/(tag+'_cover.npz'))
    cov = {k: z[k] for k in z.files}
    a = [4, 3][cell-1]
    p = panel.PRIMES[0]
    rec = dict(status='RESOURCE_STOP', lam=panel.CELLS[cell-1], n=4, delta=8, a=a,
               stage='reduction', prime=p, m_det_lb=0, U_pad_ub=3)
    panel.save(tag+'_rank.json', rec)
    t = time.perf_counter()
    K, info = projected_kernel(E, cov, p, a)
    rec['reduction'] = info
    rec['stage'] = 'evaluation'
    np.savez_compressed(OUT/(tag+'_kernel.npz'), K=K.astype(np.uint32), prime=p)
    panel.save(tag+'_rank.json', rec)
    values, points = [], []
    from wk11_s71_hybrid import matmul_mod
    for j in range(a+8):
        point = panel.pencil(1504100+j, 7)
        co = panel.det_coefficients(point)
        # Independent integer determinant spot checks at explicit restrictions.
        for s in ([1, 0, 0, 0, 0, 0, 0], [1, 1, -1, 2, -2, 3, 1]):
            assert panel.poly_at(co, s) == panel.direct_det_at(point, s)
        ev = panel.eval_orbits(arr, co, p, 7).reshape(1, -1)
        values.append(matmul_mod(ev, K, p)[0].tolist())
        points.append(point)
        rank = rank_mod_p(np.asarray(values), p)
        rec.update(m_det_lb=rank, i_det_ub=a-rank, D_ub=3-rank,
                   points=points, values=values, status='REPLAYED_RANK_FLOOR',
                   wall_seconds=time.perf_counter()-t,
                   source_construction='b15_04_panel.py pilot and modular kernel with rank-certified rational lift')
        panel.save(tag+'_rank.json', rec)
        print('DET RANK', rank, 'after', j+1, 'points', flush=True)
        if rank >= 3:
            break
    rec['stage'] = 'completed'
    rec['positive_excluded'] = rec['m_det_lb'] >= 3
    panel.save(tag+'_rank.json', rec)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['control', 'run'])
    parser.add_argument('--cell', type=int, choices=[1, 2], default=1)
    args = parser.parse_args()
    control() if args.mode == 'control' else run(args.cell)
