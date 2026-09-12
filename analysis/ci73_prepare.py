"""Prepare a portable certificate from pinned definitions, not fresh-value claims."""
import gzip,json,math,shutil,sys
from pathlib import Path
sys.path.insert(0,str(Path('tools/verify').resolve()))
import ci73_io as io
import ci73_eval as ev
import ci73_linear as la

OUT=Path('results/ci73')

def write(p,d):p.write_text(json.dumps(d,indent=1)+'\n',encoding='utf-8')

def main():
    for source,name in [('results/s74/source.json','source.json'),('results/b14_prep/points/P13.json','points.json'),
                        ('results/s74/certified.json','inherited_s74.json')]:
        shutil.copyfile(source,OUT/'inputs'/name)
    s=io.load(OUT/'inputs/source.json');pts=io.load(OUT/'inputs/points.json')
    m=io.load(OUT/'inputs/mixed.json');a=io.load(OUT/'inputs/source_matrix.json');k=io.load(OUT/'inputs/kernel.json')
    j=io.load(OUT/'inputs/joint.json');cols=j['minor_columns'];primary=[p for p in pts['points'] if p['role']=='primary']
    A=[[int(row[c]) for c in cols] for row in a['A']]
    rows,cminor=la.pivot_minor(A,2147483647)
    w={'rows':rows,'columns':cminor,'determinant':str(la.determinant(la.minor(A,rows,cminor)))}
    g=io.load(Path('results/s74/columns_gen_2147483647.json.gz'))
    lookup={json.dumps(json.loads(key),separators=(',',':')):row for key,row in g['rows_native'].items()}
    ge=ev.exps(4,9);us=[24*cv[ge.index((4,)+(0,)*8)]%g['prime'] for cv in g['points_cv'][:39]]
    G=[]
    for e in s['entries'][:39]:
        values=lookup[json.dumps(e['key'],separators=(',',':'))]
        G.append([int(value)*pow(u,13-e['rung'],g['prime'])%g['prime'] for value,u in zip(values,us)])
    generic={'prime':g['prime'],'coefficient_exponents':[list(a) for a in ge],
             'points':[{'id':f'S74-generic-{g["prime"]}-{i:03d}','coefficients':cv} for i,cv in enumerate(g['points_cv'][:39])],
             'values_are':'unscaled native source climbed to degree 13; rows; generic points as integer lifts',
             'entries':G,'minor_determinant':la.determinant(G,g['prime'])}
    write(OUT/'inputs/generic39.json',generic)
    cert={'format':'gct-cert/1','kind':'complete_interpolation','profile':'quartic_lmr_degree13_ci73',
          'title':'Degree-13 complete interpolation and three reducible equations',
          'produced_by':'B14-03-ci73, gpt-6-astra xhigh; original inputs B14-01/02/04/05',
          'field':'Q','cell':{'n':4,'r':9,'delta':13,'lambda':[21,17]+[2]*7},
          'conventions':{'coefficient':'ordinary c_alpha; symbol alpha! c_alpha',
                         'bracket':'initial-column Leibniz sum; no orbit averaging',
                         'orientation':'source rows; point columns; A^T K=0',
                         'transport':'u=24*c_(4,0^8); native to degree13, then u^11 to degree24'},
          'dependencies':{},'source_rows':[{'index':e['index'],'native_degree':e['rung'],
                       'transport_exponent':13-e['rung'],'representation':'native','scale':'1'} for e in s['entries'][:39]],
          'point_indices':cols,'point_ids':[primary[i]['id'] for i in cols],
          'target_members':[{'kind':'mixed_bracket','filling':ev.filling(row['filling'])} for row in m['members']]+
                           [{'kind':'quartic_source_pullback','source_index':15,'basis':'native_unscaled'}],
          'target_values':{'values_are':'raw integral member evaluations mod indicated prime; target rows; selected points',
              'rows_by_prime':{str(p):[[int(row[c])%p for c in cols] for row in m[key]]+[[int(a['A'][15][c])%p for c in cols]]
                               for p,key in [(2147483647,'rows_P1'),(2147483629,'rows_P2')]}},
          'target_minor':{'rows':list(range(73)),'columns':list(range(73)),
               'determinants':{str(x['prime']):x['determinant'] for x in j['joint_minor_by_prime']}},
          'source_values':{'values_are':'unscaled integral F_native*u^(13-native_degree); source rows; selected points',
                           'entries':[[str(v) for v in row] for row in A]},
          'source_minor':w,'kernel':{'values_are':'columns in the explicitly scaled rational source basis; integer representatives by default',
                                   'entries':k['left_kernel_K'],'rank':3},
          'arithmetic':{'method':'fresh integer256 contraction plus seven-prime signed CRT cross-check',
                        'integer_modulus':str(2**256),'height_bound':a['height_bound'],'primes':a['primes'],'crt_modulus':a['modulus']},
          'claim':{'source_dimension':39,'target_dimension':73,'source_rank_Q':36,'i_red13':3},
          'transport_claim':{'u_power':11,'target_degree':24,'target_weight':[65,17]+[2]*7,
                             'source_coordinates':'same first39 kernel coefficients after source scaling; 235 zeros',
                             'i_pad24_interval':[3,5],'D_LMR_interval':[-4,-2]}}
    refs={'source':'inputs/source.json','points':'inputs/points.json','source_matrix':'inputs/source_matrix.json',
          'generic':'inputs/generic39.json','target_dimension':'inputs/dimension73.json',
          'target_power':'inputs/dimension73_power.json.gz','ambient_power':'ambient13_power.json.gz',
          'inherited_s74':'inputs/inherited_s74.json'}
    refs.update({f'residues_{p}':f'inputs/residues_{p}.json' for p in a['primes']})
    cert['dependencies']={name:io.reference(OUT/path,OUT) for name,path in refs.items()}
    write(OUT/'certificate.json',cert)
    print(json.dumps({'source_minor_shape':len(rows),'source_minor_bits':abs(int(w['determinant'])).bit_length(),
                      'generic_minor':generic['minor_determinant'],'selected_columns':cols}))

if __name__=='__main__':main()
