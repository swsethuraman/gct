"""Export explicit equations only after a recorded full standard-verifier PASS."""
import json,sys
from fractions import Fraction
from pathlib import Path
sys.path.insert(0,str(Path('tools/verify').resolve()))
import ci73_io as io,ci73_eval as ev

OUT=Path('results/ci73')

def main():
    receipt=io.load(OUT/'dispatcher_positive.json')
    if receipt['status']!='PASS' or not receipt['passed']:raise RuntimeError('full polynomial verification absent')
    c=io.load(OUT/'certificate.json');s=io.read_reference(c['dependencies']['source'],OUT)
    K=[[str(Fraction(c['source_rows'][i]['scale'])*Fraction(x)) for x in row] for i,row in enumerate(c['kernel']['entries'])]
    equations={'format':'ci73-explicit-equations/1','field':'Q','lambda':[21,17]+[2]*7,'degree':13,
        'coefficient_convention':c['conventions'],'indexing':'zero-based source rows; equation columns j=1,2,3',
        'definition':'Q_j = sum_i K[i,j] F_i^native u^(13-native_degree_i); u=24*c_(4,0^8)',
        'certificate_canonical_sha256':io.digest(c),'K':K,'source_definitions':[],
        'transport':{'degree':24,'lambda':[65,17]+[2]*7,'multiplier':'u^11',
                     'literal_source_coefficients':K+[['0','0','0'] for _ in range(235)]},
        'scope':'integer representatives of a rational kernel basis; no saturated Z-lattice claim'}
    for i,e in enumerate(s['entries'][:39]):
        equations['source_definitions'].append(dict(index=i,native=e['native'],degree13=ev.native_source(e),
            u_exponent=13-e['rung'],literal24=e['literal'],coefficients=K[i]))
    if len(equations['transport']['literal_source_coefficients'])!=274:raise RuntimeError('export shape')
    (OUT/'equations.json').write_text(json.dumps(equations,indent=1)+'\n',encoding='utf-8')
    lines=['# Three explicit degree-13 equations','',
        'All source indices below are zero-based. Let u=24 c_(4,0^8). Each F_i is',
        'the literal bracket sum defined in ci73_proof.md, using the native filling',
        'listed below and factorial symbols alpha! c_alpha. Then', '',
        '    Q_j = sum_(i=0)^38 K[i,j] u^(13-d_i) F_i^native,  j=1,2,3.', '',
        'The complete standard-verifier replay proves that these are three independent',
        'equations of the reducible quartic locus. They are integer representatives',
        'of a rational kernel basis; integral lattice saturation is not asserted.', '',
        '| i | d_i | u exponent | K[i,1] | K[i,2] | K[i,3] |',
        '|---|---|---|---|---|---|']
    for i,e in enumerate(s['entries'][:39]):lines.append('| '+' | '.join(map(str,[i,e['rung'],13-e['rung'],*K[i]]))+' |')
    lines+=['','## Every native source filling','',
        'All fillings have n=4, h=9. C1 and C2 are ordered height-nine columns;',
        'each pair in `two` is an ordered height-two column and `one` lists singleton',
        'letters. Each native letter occurs four times. No implicit source lookup',
        'is required: all 39 definitions follow.','']
    for i,e in enumerate(s['entries'][:39]):
        lines+=['### Source '+str(i),'','```json',json.dumps(e['native'],separators=(',',':')),'```','']
    lines+=['## Degree-24 transport','',
        'Multiply each Q_j by u^11. Appending four singleton occurrences for each',
        'new letter gives exactly the S74 literal degree-24 filling, as checked by',
        'the verifier. The coefficient table above is unchanged on rows 0–38;',
        'rows 39–273 have coefficients (0,0,0). `equations.json` contains all 274',
        'rows explicitly, plus native, degree-13 and degree-24 definitions.','',
        'The three transported equations establish i_pad(24)>=3. With the separately',
        'inherited S74 bounds, i_pad(24) lies in [3,5] and D_LMR lies in [-4,-2].',
        'D=-4 remains open.','']
    Path('docs/ci73_equations.md').write_text('\n'.join(lines),encoding='utf-8')
    # Read back and verify every exported coefficient and transport row.
    read=io.load(OUT/'equations.json')
    if read['K']!=K or read['source_definitions']!=equations['source_definitions'] or read['transport']!=equations['transport']:
        raise RuntimeError('equation export mismatch')
    print(json.dumps(dict(status='PASS',equations=3,source_definitions=39,transport_rows=274)))

if __name__=='__main__':main()
