"""F3: arithmetic only (no evaluations, no wrapper). E-using order-four rows on the columns (q3, q7)
from the preserved P7 values and the F2 values; ratios [t^4]/[t^0] on the ambient generator taken from
Check 2 of the sealed transverse-structure report (13/21 for S1, 2/7 for S2, 0 for S4): these are
ambient-image data (adopted from the H5 evaluation), so these rows are NOT E-free."""
import json
from fractions import Fraction
from pathlib import Path
HERE = Path(__file__).resolve().parent; ROOT = HERE.parents[2]
P = 524287
p7 = json.loads((ROOT / 'work/descent_followup_claude_20260916/pilots/p7_arc_S0.json').read_text())
f2 = json.loads((HERE / 'f2_c4_vs_c2.json').read_text())
c2j = json.loads((ROOT / 'work/claude_transverse_structure_20260916/checks/c2_fivevar_order4.json').read_text())['five_variables']['ambient_line']
pres = p7['C2_values_at_K5_K5S_K52S']; new = f2['new_values']
inv12 = pow(12, P - 2, P)
def J4(z0, z1, z2): return [((z2[i] - 4 * z1[i] + 3 * z0[i]) * inv12) % P for i in range(2)]
def J2(z0, z1, z2): return [((16 * z1[i] - z2[i] - 15 * z0[i]) * inv12) % P for i in range(2)]
def modfrac(fr):
    fr = Fraction(fr); return fr.numerator * pow(fr.denominator, P - 2, P) % P
pts = {'S1': (pres[0], pres[1], pres[2]), 'S2': (pres[0], new['S2_t1'], new['S2_t2']), 'S4': (pres[0], new['S4_t1'], new['S4_t2'])}
ratio4 = {'S1': c2j['S1=x1*I']['t4_over_t0'], 'S2': c2j['S2=x2*I']['t4_over_t0'], 'S4': c2j['S4=x1*diag(1,1,0,0)']['t4_over_t0']}
ratio2 = {'S1': c2j['S1=x1*I']['t2_over_t0'], 'S2': c2j['S2=x2*I']['t2_over_t0'], 'S4': c2j['S4=x1*diag(1,1,0,0)']['t2_over_t0']}
out = {'ambient_ratios_adopted': dict(t4_over_t0=ratio4, t2_over_t0=ratio2)}
rows = {}
for S, (z0, z1, z2) in pts.items():
    j4 = J4(z0, z1, z2); j2 = J2(z0, z1, z2)
    rows[f'Eusing_order4_{S}'] = [(j4[i] - modfrac(ratio4[S]) * z0[i]) % P for i in range(2)]
    rows[f'order2_{S}'] = [(j2[i] - modfrac(ratio2[S]) * z0[i]) % P for i in range(2)]
out['rows_on_q3_q7'] = rows
def det2(a, b): return (a[0] * b[1] - a[1] * b[0]) % P
inv84 = pow(84, P - 2, P)
out['check_order2_S1_equals_C2_over_84'] = (rows['order2_S1'] == [(x * inv84) % P for x in p7['C2_row']])  # C2 = 84*(J2 - (6/7) z0)
# Theorem 6.2 prediction: every order-two row is proportional to C2 on M; on two vectors check proportionality
out['order2_rows_proportional_to_C2'] = {S: det2(rows[f'order2_{S}'], p7['C2_row']) for S in ('S2', 'S4')}
out['minors_Eusing_vs_C2'] = {S: det2(rows[f'Eusing_order4_{S}'], p7['C2_row']) for S in ('S1', 'S2', 'S4')}
out['minors_Eusing_pairs'] = {f'{a},{b}': det2(rows[f'Eusing_order4_{a}'], rows[f'Eusing_order4_{b}']) for a, b in (('S1', 'S2'), ('S1', 'S4'), ('S2', 'S4'))}
# torus argument for the degenerate control: z(K_deg) = s^8 z(K_deg) for all s, hence 0
out['degenerate_control_forced_zero'] = dict(argument='A=diag(s,s,1/s,1/s) in SL4 with (A,A^T) in H0 maps K_deg to diag(s^2,1,1,1,1).K_deg; GL5 weight det^4 gives z = s^8 z, so z(K_deg)=0 for every z in M', observed=f2['corrupted_input_controls']['degenerate_pencil']['values'])
(HERE / 'f3_derived_rows.json').write_text(json.dumps(out, indent=1) + '\n'); print(json.dumps(out, indent=1))
