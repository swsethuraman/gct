"""Degree-13 CI acceptance: fresh polynomial values, not stored rank receipts.

No analysis/ or producer imports. A Session may memoize values computed in the
same process for adversarial tests; no disk value cache is ever accepted.
"""
from fractions import Fraction
import json
import math
from pathlib import Path
import time

import ci73_dimension as dim
import ci73_eval as ev
import ci73_io as io
import ci73_linear as la

PROFILE='quartic_lmr_degree13_ci73'
PRIMES=[2147483647,2147483629,2147483587,2147483579,2147483563,2147483549,2147483543]
LAM=[21,17]+[2]*7
CONVENTIONS={'coefficient':'ordinary c_alpha; symbol alpha! c_alpha',
 'bracket':'initial-column Leibniz sum; no orbit averaging',
 'orientation':'source rows; point columns; A^T K=0',
 'transport':'u=24*c_(4,0^8); native to degree13, then u^11 to degree24'}


def need(ok,why):
    if not ok:raise ValueError(why)


def keys(d,names):
    need(type(d) is dict and set(d)==set(names.split()),'missing or unknown keys: '+names)


def integer(x):
    need(type(x) is int or (type(x) is str and len(x)<10000 and x.lstrip('-').isdigit()),'integer expected')
    return int(x)


def rational(x):
    need(type(x) in (str,int) and len(str(x))<10000,'rational expected')
    return Fraction(x)


def indices(v,n,k):
    need(type(v) is list and len(v)==k and all(type(x) is int and 0<=x<n for x in v)
         and len(set(v))==k,'minor or point indices invalid')


def matrix(v,r,c,convert=integer):
    need(type(v) is list and len(v)==r and all(type(row) is list and len(row)==c for row in v),'matrix shape')
    return [[convert(x) for x in row] for row in v]


def prime(p):
    return type(p) is int and 2<=p<=2147483647 and all(p%d for d in range(2,math.isqrt(p)+1))


def schema(c):
    keys(c,'format kind profile title produced_by field cell conventions dependencies source_rows point_indices point_ids target_members target_values target_minor source_values source_minor kernel arithmetic claim transport_claim')
    need(c['format']=='gct-cert/1' and c['kind']=='complete_interpolation' and c['profile']==PROFILE,'unsupported CI profile')
    need(c['field']=='Q' and c['cell']==dict(n=4,r=9,delta=13,**{'lambda':LAM}),'wrong field or cell')
    need(c['conventions']==CONVENTIONS,'unsupported coefficient, bracket, orientation or transport convention')
    need(all(type(c[x]) is str and c[x] for x in ('title','produced_by')),'missing authorship/title')
    keys(c['dependencies'],'source points source_matrix generic target_dimension target_power ambient_power inherited_s74 '+' '.join('residues_'+str(p) for p in PRIMES))
    keys(c['target_values'],'values_are rows_by_prime');keys(c['source_values'],'values_are entries')
    keys(c['target_minor'],'rows columns determinants');keys(c['source_minor'],'rows columns determinant')
    keys(c['kernel'],'values_are entries rank');keys(c['arithmetic'],'method integer_modulus height_bound primes crt_modulus')
    need(c['source_values']['values_are']=='unscaled integral F_native*u^(13-native_degree); source rows; selected points','source value normalization')
    need(c['target_values']['values_are']=='raw integral member evaluations mod indicated prime; target rows; selected points','target value normalization')
    need(c['kernel']['values_are']=='columns in the explicitly scaled rational source basis; integer representatives by default','kernel orientation/normalization')
    need(c['arithmetic']['method']=='fresh integer256 contraction plus seven-prime signed CRT cross-check','unsupported arithmetic proof')
    need(c['claim']==dict(source_dimension=39,target_dimension=73,source_rank_Q=36,i_red13=3),'unsupported claim')
    need(c['transport_claim']==dict(u_power=11,target_degree=24,target_weight=[65,17]+[2]*7,
        source_coordinates='same first39 kernel coefficients after source scaling; 235 zeros',
        i_pad24_interval=[3,5],D_LMR_interval=[-4,-2]),'transport claim mismatch')


class Session:
    """Cache only values independently computed by this live verification process."""
    def __init__(self):
        self.values={};self.dimensions=set();self.calls=0;self.entries=0;self.hits=0
        self.max_array_bytes=0;self.backend_seconds=0

    def row(self,f,symbols,p,name):
        # Include every coefficient, its exponent, filling and modulus in identity.
        serial=[f,p,[{str(n):sorted((list(a),v) for a,v in table.items()) for n,table in point.items()} for point in symbols]]
        key=io.digest(serial)
        if key in self.values:
            self.hits+=1;return self.values[key][:]
        spec=ev.plan(json.dumps(ev.filling(f),sort_keys=True))
        batch=min(16,max(1,450_000_000//(spec['peak_states_pair']*(8 if p else 32))))
        out=[]
        for offset in range(0,len(symbols),batch):
            values,receipt=ev.evaluate(f,symbols[offset:offset+batch],p,
                                      name='ci73_'+name+'_'+key[:10]+'_'+str(offset),seconds=120)
            self.calls+=1;self.entries+=len(values);out.extend(values)
            self.max_array_bytes=max(self.max_array_bytes,receipt['peak_array_bytes'])
            self.backend_seconds+=receipt['wall_seconds']
        self.values[key]=out[:]
        return out


def dimensions(d,session):
    proof=[d[x] for x in ('target_dimension','target_power','ambient_power')]
    identity=io.digest(proof)
    if identity in session.dimensions:return
    t,p,a=proof
    need(t['method']=='Pieri interlacing; banked power-sum plethysm and MN characters','unsupported target dimension method')
    need(a['method']=='exact Newton power expansion and outer-rim MN','unsupported ambient dimension method')
    dim.selfcheck_rim()
    cubic=dim.cubic_exact(13)[13]
    mods={p:dim.modular_newton(13,p,cubic_outer=True)[13] for p in dim.PRIMES}
    need(dim.check_hpad(13,cubic,mods,t,p)==73,'target dimension is not 73')
    ambient,power=dim.ambient13()
    need(a['n']==4 and a['degree']==13 and a['lambda']==LAM and a['dimension']==ambient==39,'ambient dimension mismatch')
    need(a['values_are']=='exact power-sum coefficients of h_13[h_4]','ambient power convention')
    saved={tuple(rho):Fraction(x,y) for rho,x,y in a['rows']}
    need(len(saved)==len(a['rows']) and saved==power,'ambient complete expansion mismatch')
    session.dimensions.add(identity)


def run(c,root,session,log):
    gate='schema'
    def report(name,**detail):
        log.append({'check':name,'ok':True,'detail':detail})
        print(json.dumps({'ci73_gate':name,**detail}),flush=True)
    try:
        schema(c)
        gate='dependencies'
        d={name:io.read_reference(ref,root) for name,ref in c['dependencies'].items()}
        gate='source definitions and degree13 transport'
        s=d['source'];entries=s['entries']
        need(s['complete'] is True and s['size']==274 and len(entries)==274,'incomplete inherited source')
        need(s['cell']==dict(n=4,r=9,lam=[65,17]+[2]*7,delta=24,a=274),'inherited source cell')
        need(len(c['source_rows'])==39,'source row count')
        F=[];scales=[]
        for i,(row,e) in enumerate(zip(c['source_rows'],entries)):
            keys(row,'index native_degree transport_exponent representation scale')
            need(row['index']==e['index']==i and row['native_degree']==e['rung']==(12 if i<2 else 13),'source identifier/native degree')
            need(row['representation']=='native' and row['transport_exponent']==13-e['rung'],'wrong native transport or literal representation')
            f=ev.native_source(e)
            need(f['h']==9 and len(f['two'])==15 and len(f['one'])==4 and f['val']==[4]*13,'source degree13 column shape')
            need(e['native']['lam']==[4*e['rung']-31,17]+[2]*7,'native highest weight')
            need(e['key']==[e['native'][k] for k in ('C1','C2','two','one')],'source key disagrees with polynomial')
            literal=ev.native_source(e,24)
            need(e['literal']==dict(h=9,n=4,delta=24,C1=literal['C1'],C2=literal['C2'],two=literal['two'],one=literal['one'],lam=[65,17]+[2]*7),'literal24 transport polynomial mismatch')
            need(e['exponent']==24-e['rung'] and e['factorial_scalar']==24**e['exponent'],'source factorial transport scalar')
            scale=rational(row['scale']);need(scale and all(scale.numerator%p and scale.denominator%p for p in PRIMES),'noninvertible source scale')
            scales.append(scale);F.append(f)
        report(gate,rows=39,native12=2,native13=37,degree24_polynomial_identity=True)
        gate='points and ordinary/factorial symbols'
        pts=d['points'];ce=pts['cubic_exponents'];points=pts['points']
        need(pts['degree']==13 and pts['r']==9 and pts['lambda']==LAM and pts['integer_bound']==7,'point contract')
        need(pts['coefficient_convention']=='plain coefficients; cubic_exponents give the exact order','point coefficient convention')
        need(len(ce)==165 and set(map(tuple,ce))==set(ev.exps(3,9)),'cubic exponent coverage')
        need(len(points)==116 and len({x['id'] for x in points})==116,'point IDs/count')
        need([x['role'] for x in points]==['primary']*96+['holdout']*20,'point roles/order')
        need(pts['primary_point_count']==96 and pts['holdout_point_count']==20,'point counts')
        symbols=[]
        for p in points:
            need(len(p['linear'])==9 and len(p['cubic_coefficients'])==165,'point shape')
            need(all(type(v) is int and abs(v)<=7 for v in p['linear']+p['cubic_coefficients']),'point integer bound')
            table={4:ev.quartic_symbols(p,ce)}
            need(table[4][(4,)+(0,)*8]==p['u_symbol']!=0,'point u-symbol')
            need(max(map(abs,table[4].values()))==p['max_abs_quartic_symbol']<=1176,'quartic symbol bound')
            symbols.append(table)
        sm=d['source_matrix'];cols=c['point_indices'];indices(cols,96,73)
        need(c['point_ids']==[points[x]['id'] for x in cols],'selected point order')
        need(sm['col_id']==[p['id'] for p in points[:96]],'source matrix point order')
        need(sm['transform']=='none' and sm['degree']==13 and sm['n_rows']==39 and sm['n_cols']==96,'stored source model')
        need(sm['row_index']==list(range(39)) and sm['row_rung']==[12]*2+[13]*37 and sm['row_transport_exponent']==[1]*2+[0]*37,'stored source order/transport')
        need(sm['col_u_symbol']==[p['u_symbol'] for p in points[:96]] and sm['col_max_abs_quartic_symbol']==[p['max_abs_quartic_symbol'] for p in points[:96]],'source point tags')
        selected=[symbols[j] for j in cols]
        report(gate,primary=96,selected=cols,holdouts=20)
        gate='dimension proofs'
        dimensions(d,session);report(gate,source=39,target=73,Pieri_channels=15)
        gate='exact arithmetic bound'
        symbol_bound=max(math.prod(math.factorial(x) for x in alpha)*sum(x>0 for x in alpha)*7**2 for alpha in ev.exps(4,9))
        H=math.factorial(9)**2*2**15*symbol_bound**13;M=math.prod(PRIMES);a=c['arithmetic']
        need(symbol_bound==1176 and integer(a['height_bound'])==H and H<2**255,'height bound')
        need(a['primes']==PRIMES and len(set(PRIMES))==7 and all(prime(p) for p in PRIMES),'CRT primes')
        need(integer(a['integer_modulus'])==2**256 and integer(a['crt_modulus'])==M>2*H,'insufficient/wrong CRT modulus')
        need(sm['primes']==PRIMES and integer(sm['modulus'])==M and integer(sm['height_bound'])==H,'stored CRT contract')
        residue=[]
        for p in PRIMES:
            block=d['residues_'+str(p)]
            need(block['prime']==p and block['role']=='primary' and block['n_rows']==39 and block['n_cols']==96,'residue model')
            need(set(block['rows'])==set(map(str,range(39))),'residue source IDs')
            R=matrix([block['rows'][str(i)] for i in range(39)],39,96)
            need(all(0<=v<p for row in R for v in row),'noncanonical residue')
            need(block['u_mod_p']==[x['u_symbol']%p for x in points[:96]],'residue point tags')
            residue.append(R)
        report(gate,height_bound=str(H),integer_ring_bits=256,CRT_modulus=str(M))
        gate='fresh exact source values and signed CRT'
        A=matrix(c['source_values']['entries'],39,73);stored=matrix(sm['A'],39,96)
        crtweights=[(M//p)*pow(M//p,-1,p) for p in PRIMES]
        for i,f in enumerate(F):
            fresh=session.row(f,selected,0,'source_'+str(i))
            for j,x in enumerate(fresh):
                need(abs(x)<=H and x==A[i][j]==stored[i][cols[j]],f'fresh source mismatch at row {i}, point {cols[j]}')
                rs=[R[i][cols[j]] for R in residue]
                need(all(x%p==v for p,v in zip(PRIMES,rs)),f'fresh residue mismatch row {i}, point {cols[j]}')
                z=sum(v*w for v,w in zip(rs,crtweights))%M;z=z-M if z>M//2 else z
                need(z==x,'signed CRT disagrees with fresh exact evaluation')
            if i%8==7:print(json.dumps({'ci73_progress':'source','rows':i+1}),flush=True)
        # Additional columns are only an arithmetic replay, and are not used in CI.
        for i in range(39):
            for j in range(96):
                need(abs(stored[i][j])<=H and all(stored[i][j]%p==R[i][j] for p,R in zip(PRIMES,residue)),'unused-column arithmetic mismatch')
        report(gate,exact_entries=39*73,residue_comparisons=39*73*7,unused_primary_columns_arithmetic_only=23)
        gate='source independence on fresh generic quartics'
        g=d['generic'];p=g['prime'];need(p==PRIMES[0],'generic prime')
        ge=g['coefficient_exponents'];need(list(map(tuple,ge))==list(ev.exps(4,9)),'generic exponent order')
        need(len(g['points'])==39 and len({x['id'] for x in g['points']})==39,'generic point IDs')
        generic=[]
        for point in g['points']:
            need(len(point['coefficients'])==495 and all(type(v) is int and 0<=v<p for v in point['coefficients']),'generic coefficient integer lifts')
            generic.append({4:{tuple(alpha):v*math.prod(math.factorial(x) for x in alpha)%p for alpha,v in zip(ge,point['coefficients'])}})
        G=matrix(g['entries'],39,39)
        need(g['values_are']=='unscaled native source climbed to degree 13; rows; generic points as integer lifts','generic normalization')
        for i,f in enumerate(F):
            need(session.row(f,generic,p,'generic_'+str(i))==G[i],f'fresh generic mismatch row {i}')
        gd=la.determinant(G,p);need(gd!=0 and gd==g['minor_determinant'],'source independence minor')
        report(gate,entries=39*39,prime=p,determinant=gd)
        gate='target membership and fresh evaluations'
        members=c['target_members'];need(len(members)==73,'target member count')
        mixed=[ev.mixed_symbols(points[j],ce) for j in cols];target={}
        need(set(c['target_values']['rows_by_prime'])==set(map(str,PRIMES[:2])),'target value primes')
        for p in PRIMES[:2]:
            B=matrix(c['target_values']['rows_by_prime'][str(p)],73,73)
            need(all(0<=v<p for row in B for v in row),'target canonical residues')
            for i,member in enumerate(members):
                if member['kind']=='mixed_bracket':
                    keys(member,'kind filling');keys(member['filling'],'h val C1 C2 two one')
                    f=ev.filling(member['filling'])
                    need(f['h']==9 and len(f['two'])==15 and len(f['one'])==4 and sorted(f['val'])==[1]*13+[3]*13,'mixed bidegree or highest weight')
                    values=session.row(f,mixed,p,'target_'+str(p)+'_'+str(i))
                elif member['kind']=='quartic_source_pullback':
                    keys(member,'kind source_index basis');index=member['source_index']
                    need(type(index) is int and 0<=index<39 and member['basis']=='native_unscaled','pullback source identity/basis')
                    values=[v%p for v in A[index]]
                else:raise ValueError('unsupported target membership proof')
                need(values==B[i],f'fresh target mismatch member {i}, prime {p}')
                if i%12==11:print(json.dumps({'ci73_progress':'target','prime':p,'rows':i+1}),flush=True)
            target[p]=B
        report(gate,members=73,entries=73*73*2,mixed_entries=72*73*2,completing_entry_reuses_fresh_source=True)
        gate='full target minor'
        w=c['target_minor'];indices(w['rows'],73,73);indices(w['columns'],73,73)
        need(set(w['determinants'])==set(map(str,PRIMES[:2])),'target minor primes')
        determinants={}
        for p,B in target.items():
            z=la.determinant(la.minor(B,w['rows'],w['columns']),p)
            need(z!=0 and z==integer(w['determinants'][str(p)]),'target full-rank minor is zero or disagrees')
            determinants[str(p)]=z
        report(gate,dimension=73,determinants=determinants)
        gate='exact source rank and kernel'
        w=c['source_minor'];indices(w['rows'],39,36);indices(w['columns'],73,36)
        z=la.determinant(la.minor(A,w['rows'],w['columns']))
        need(z!=0 and z==integer(w['determinant']),'source rank36 exact minor')
        K=matrix(c['kernel']['entries'],39,3,rational)
        need(c['kernel']['rank']==3 and la.rank_q(K)==3,'kernel column rank')
        # Coordinates are in scale_i*F_i, while saved integer values are raw F_i.
        effective=[[scales[i]*x for x in row] for i,row in enumerate(K)]
        need(all(sum(A[i][j]*effective[i][k] for i in range(39))==0 for j in range(73) for k in range(3)),'A^T K relation fails')
        report(gate,rank_Q=36,kernel_rank=3,exact_identities=219,minor_determinant=str(z))
        gate='fresh holdout relation controls'
        hold=[session.row(f,symbols[96:],0,'holdout_'+str(i)) for i,f in enumerate(F)]
        need(all(abs(x)<=H for row in hold for x in row),'holdout height')
        need(all(sum(hold[i][j]*effective[i][k] for i in range(39))==0 for j in range(20) for k in range(3)),'holdout relation fails')
        report(gate,exact_entries=780,identities=60,used_for_target_minor=False)
        gate='inherited LMR dependency identification'
        inherited=d['inherited_s74']
        need(inherited['cell']==s['cell'] and inherited['row_system']==s['row_system'],'inherited cell/source mismatch')
        need(set(inherited['primes'])==set(map(str,PRIMES[:2])),'inherited prime records')
        for p in PRIMES[:2]:
            record=inherited['primes'][str(p)]
            for name,rank in [('det_minor_delta23',273),('pad_minor',269)]:
                witness=record[name]
                need(witness['rank']==rank and 0<witness['det_mod_p']<p,'inherited rank witness record')
                indices(witness['row_set'],witness['rows'],rank);indices(witness['col_set'],witness['cols'],rank)
        report(gate,status='INHERITED; degree24 polynomial matrices not freshly evaluated here',
               a24=274,det_rank=273,pad_rank_floor=269,
               dependency='frozen S74 certified.json; separate inherited-minor arithmetic replay in delivery')
        report('complete interpolation',source_dimension=39,target_dimension=73,rank_Q=36,i_red13=3,
               i_pad24_lower_bound=3,transport='u^11, same effective coefficients then 235 zeros',
               D_interval_with_inherited_S74=[-4,-2],D_equals_minus4='OPEN')
        return {'status':'PASS','checks':log,'code':'OK','detail':'Degree13 polynomial CI proof complete; LMR consequence uses identified inherited S74 facts.'}
    except (ValueError,KeyError,TypeError,IndexError,ZeroDivisionError) as exc:
        return {'status':'FAIL','checks':log,'code':gate,'detail':str(exc)}


def verify(c,root,session=None):
    started=time.monotonic();session=session or Session()
    before=(session.calls,session.entries,session.hits)
    result=run(c,Path(root),session,[])
    result.update(seconds=time.monotonic()-started,backend_calls=session.calls-before[0],
                  fresh_backend_entries=session.entries-before[1],live_session_cache_hits=session.hits-before[2],
                  max_backend_array_bytes=session.max_array_bytes)
    return result
