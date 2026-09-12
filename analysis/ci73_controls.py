"""Standard dispatcher positive/rejection tests, using a fresh live session."""
import copy,gzip,json,sys,time
from fractions import Fraction
from pathlib import Path
sys.path.insert(0,str(Path('tools/verify').resolve()))
import ci73,ci73_io as io,ci73_linear as la
from verify import verify_file

OUT=Path('results/ci73')

def write(path,data):path.write_text(json.dumps(data,indent=1)+'\n',encoding='utf-8')

def main():
    base=io.load(OUT/'certificate.json');session=ci73.Session();results=[]
    active=OUT/'control_active.json'
    def check(name,c,expected='FAIL',gate=None):
        write(active,c);before=(session.calls,session.entries,session.hits);start=time.monotonic()
        status,log=verify_file(str(active),ci73_session=session)
        passed=status==expected and (gate is None or log[-1][0]==gate)
        item=dict(name=name,status=status,expected=expected,passed=passed,seconds=time.monotonic()-start,
            fresh_calls=session.calls-before[0],fresh_entries=session.entries-before[1],
            live_session_cache_hits=session.hits-before[2],checks=log)
        results.append(item);write(OUT/'controls.json',results)
        print(json.dumps({k:v for k,v in item.items() if k!='checks'}),flush=True)
        if not passed:raise RuntimeError('control failed: '+name+' '+str(log[-1]))
    def dep(c,name,mutator):
        value=io.read_reference(c['dependencies'][name],OUT);mutator(value)
        path=OUT/'cache'/('control_'+name+'.json');write(path,value)
        c['dependencies'][name]=io.reference(path,OUT)
    def mutant(name,fn,gate=None):
        c=copy.deepcopy(base);fn(c);check(name,c,gate=gate)
    check('fresh standard-dispatcher positive',base,'PASS')
    write(OUT/'dispatcher_positive.json',results[-1])
    def duplicate(c):
        c['target_members'][72]=copy.deepcopy(c['target_members'][0])
        for B in c['target_values']['rows_by_prime'].values():B[72]=B[0][:]
    mutant('duplicate completing member with consistent duplicate values',duplicate,'full target minor')
    mutant('completing source15 changed to source14, incompatible values',lambda c:c['target_members'][72].update(source_index=14),'target membership and fresh evaluations')
    mutant('source identifier changed',lambda c:c['source_rows'][0].update(index=1),'source definitions and degree13 transport')
    def source_polynomial(c):
        def change(s):
            e=s['entries'][0]
            for field in ['native','literal']:e[field]['C1'][0],e[field]['C1'][1]=e[field]['C1'][1],e[field]['C1'][0]
            e['key']=[copy.deepcopy(e['native'][k]) for k in ('C1','C2','two','one')]
        dep(c,'source',change)
    mutant('consistent source definition change, incompatible matrix',source_polynomial,'fresh exact source values and signed CRT')
    def point_change(c):
        def change(p):p['points'][0]['linear'][2]+=1
        dep(c,'points',change)
    mutant('changed linear coefficient',point_change)
    def reorder(c):
        def change(p):p['points'][0],p['points'][1]=p['points'][1],p['points'][0]
        dep(c,'points',change)
    mutant('point reorder without matrices',reorder,'points and ordinary/factorial symbols')
    mutant('degree24 literal representation',lambda c:c['source_rows'][0].update(representation='literal'),'source definitions and degree13 transport')
    mutant('wrong degree13 transport exponent',lambda c:c['source_rows'][0].update(transport_exponent=12),'source definitions and degree13 transport')
    mutant('wrong factorial convention',lambda c:c['conventions'].update(coefficient='ordinary symbols without factorials'),'schema')
    def factorial(c):dep(c,'source',lambda s:s['entries'][0].update(factorial_scalar=1))
    mutant('wrong actual transport factorial scalar',factorial,'source definitions and degree13 transport')
    mutant('altered exact source entry',lambda c:c['source_values']['entries'][0].__setitem__(0,str(int(c['source_values']['entries'][0][0])+1)),'fresh exact source values and signed CRT')
    def residue(c):
        dep(c,'residues_2147483543',lambda d:d['rows']['0'].__setitem__(0,(d['rows']['0'][0]+1)%2147483543))
    mutant('altered seventh-prime residue',residue,'fresh exact source values and signed CRT')
    mutant('altered kernel coefficient',lambda c:c['kernel']['entries'][0].__setitem__(0,str(Fraction(c['kernel']['entries'][0][0])+1)),'exact source rank and kernel')
    mutant('altered exact rank witness',lambda c:c['source_minor'].update(determinant=str(int(c['source_minor']['determinant'])+1)),'exact source rank and kernel')
    mutant('altered target witness determinant',lambda c:c['target_minor']['determinants'].__setitem__('2147483647',1),'full target minor')
    mutant('duplicate source-minor row',lambda c:c['source_minor']['rows'].__setitem__(0,c['source_minor']['rows'][1]),'exact source rank and kernel')
    mutant('insufficient CRT modulus',lambda c:c['arithmetic'].update(crt_modulus='17'),'exact arithmetic bound')
    mutant('incompatible source denominator',lambda c:c['source_rows'][0].update(scale='1/2147483647'),'source definitions and degree13 transport')
    mutant('incorrect height bound',lambda c:c['arithmetic'].update(height_bound='1'),'exact arithmetic bound')
    mutant('unsupported target dimension proof',lambda c:dep(c,'target_dimension',lambda d:d.update(method='stored rank')),'dimension proofs')
    mutant('unsupported ambient dimension proof',lambda c:dep(c,'ambient_power',lambda d:d.update(method='trusted total')),'dimension proofs')
    mutant('wrong Pieri channel',lambda c:dep(c,'target_dimension',lambda d:d['rows'][0].update(a3=d['rows'][0]['a3']+1)),'dimension proofs')
    def bad_power(c):dep(c,'target_power',lambda d:d['rows'][0].__setitem__(1,d['rows'][0][1]+1))
    mutant('altered complete power expansion',bad_power,'dimension proofs')
    mutant('unknown target membership proof',lambda c:c['target_members'][72].update(kind='rank_receipt'),'target membership and fresh evaluations')
    mutant('altered generic independence entry',lambda c:dep(c,'generic',lambda d:d['entries'][0].__setitem__(0,(d['entries'][0][0]+1)%d['prime'])),'source independence on fresh generic quartics')
    for name in base['dependencies']:
        mutant('missing dependency '+name,lambda c,name=name:c['dependencies'].pop(name),'schema')
    # Invertible rescaling is a positive, including nonintegral coordinates.
    c=copy.deepcopy(base)
    for i,row in enumerate(c['source_rows']):
        scale=[Fraction(2,3),Fraction(-7,11),Fraction(5)][i%3];row['scale']=str(scale)
        c['kernel']['entries'][i]=[str(Fraction(x)/scale) for x in c['kernel']['entries'][i]]
    check('consistent invertible rational source rescaling',c,'PASS');write(OUT/'rational_certificate.json',c)
    # A different valid completing source is allowed when all data agree.
    A=[[int(x) for x in row] for row in base['source_values']['entries']]
    alternate=None
    for index in range(39):
        if index==15:continue
        ds={}
        for p in ci73.PRIMES[:2]:
            B=copy.deepcopy(base['target_values']['rows_by_prime'][str(p)]);B[72]=[x%p for x in A[index]]
            ds[str(p)]=la.determinant(B,p)
        if all(ds.values()):alternate=index;break
    if alternate is None:raise RuntimeError('no second completing source for positive control')
    c=copy.deepcopy(base);c['target_members'][72]['source_index']=alternate
    c['target_minor']['determinants']=ds
    for p in ci73.PRIMES[:2]:c['target_values']['rows_by_prime'][str(p)][72]=[x%p for x in A[alternate]]
    check('consistent alternative completing source '+str(alternate),c,'PASS')
    # Normal dispatcher entrance must reject malformed bytes before any parse.
    fixtures=[('duplicate JSON key',b'{"kind":"complete_interpolation","kind":"matrix"}',False),
              ('nonfinite JSON',b'{"x":NaN}',False),
              ('expanded gzip limit',gzip.compress(b' '*16_000_001,mtime=0),True),
              ('input byte limit',b' '*5_000_001,False),
              ('unknown profile',json.dumps(dict(base,profile='unknown')).encode(),False)]
    for name,raw,zipped in fixtures:
        path=OUT/'cache'/('malformed.json.gz' if zipped else 'malformed.json');path.write_bytes(raw)
        status,log=verify_file(str(path));passed=status=='UNPARSEABLE'
        results.append(dict(name=name,status=status,expected='UNPARSEABLE',passed=passed,checks=log))
        if not passed:raise RuntimeError('loader control failed: '+name)
        path.unlink()
    active.unlink();write(OUT/'controls.json',results)
    summary=dict(status='PASS',cases=len(results),positives=sum(x['expected']=='PASS' for x in results),
        rejections=sum(x['expected']!='PASS' for x in results),fresh_backend_calls=session.calls,
        fresh_backend_entries=session.entries,live_session_cache_hits=session.hits,
        max_array_bytes=session.max_array_bytes,alternate_completing_source=alternate)
    write(OUT/'controls_summary.json',summary);print(json.dumps(summary),flush=True)

if __name__=='__main__':main()
