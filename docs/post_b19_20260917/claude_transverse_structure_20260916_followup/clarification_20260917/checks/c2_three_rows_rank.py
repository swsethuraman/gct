"""Arithmetic only: rank mod P of the rows (q3, q7, e) at the five sealed P6 points (q3, q7 from
p6_basis.json 'basis_matrix_pair_by_point'; e from c1_e_arc_kernel.json reduced mod P). A rank of
three is a second, numerical certificate of the independence proved in CORRIGENDUM item K3."""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent; ROOT = HERE.parents[3]; P = 524287
p6 = json.loads((ROOT / 'work/descent_followup_claude_20260916/pilots/p6_basis.json').read_text())
c1 = json.loads((HERE / 'c1_e_arc_kernel.json').read_text())
rows = [p6['basis_matrix_pair_by_point'][0], p6['basis_matrix_pair_by_point'][1], [v % P for v in c1['e_at_P6_points_0_to_4']]]
def rank_mod(M):
    M = [[x % P for x in r] for r in M]; r = 0
    for c in range(len(M[0])):
        piv = next((i for i in range(r, len(M)) if M[i][c]), None)
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]; inv = pow(M[r][c], P - 2, P); M[r] = [(x * inv) % P for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c]: f = M[i][c]; M[i] = [(x - f * y) % P for x, y in zip(M[i], M[r])]
        r += 1
    return r
def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1]) - A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0]) + A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0])) % P
out = dict(rows_q3_q7_e_mod_P_at_P6_points=rows, rank_mod_P=rank_mod(rows), minor_cols_0_1_2=det3([r[:3] for r in rows]))
(HERE / 'c2_three_rows_rank.json').write_text(json.dumps(out, indent=1) + '\n'); print(json.dumps(out, indent=1))
