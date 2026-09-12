"""Nonvacuous audit, typed-rule controls, and trace-form exact validation."""
import collections, copy, hashlib, importlib.util, json, pathlib, sys
HERE=pathlib.Path(__file__).resolve().parent;ROOT=HERE.parents[1]
sys.path.insert(0,str(HERE));sys.path.insert(0,str(ROOT/'tools/integrate'))
from inventory import BASE, OUT, OLD, MANIFESTS, read, frozen, jsonl, write, certificate_key
from recover import det_bareiss, CELLS, verify
from exclusion_predicates import conclusions_for, matches, stable_full_rank_closure

def load_register(name):
    if (OUT/name).is_file(): data=(OUT/name).read_bytes()
    else:
        manifest=json.loads((OUT/(name+'.parts.json')).read_text())
        assert manifest['parts'], 'no parts'
        data=b''
        for i,p in enumerate(manifest['parts']):
            assert f'.part{i:02d}.' in p['path']
            block=(OUT/p['path']).read_bytes()
            assert len(block)==p['bytes'] and hashlib.sha256(block).hexdigest()==p['sha256']
            assert hashlib.md5(block).hexdigest()==p['md5'];data+=block
        assert len(data)==manifest['bytes'] and hashlib.sha256(data).hexdigest()==manifest['sha256']
        assert hashlib.md5(data).hexdigest()==manifest['md5']
    return [json.loads(s) for s in data.splitlines() if s.strip()]

def validate_files(rows,expected):
    assert expected and rows, 'nonempty inventory required'
    actual=[r['path'] for r in rows if r['historical_unparsed']]
    assert len(actual)==len(set(actual)) and set(actual)==set(expected), 'source coverage mismatch'
    for r in rows:
        assert r['classification'] in ('result','metadata','superseded') and r['classification_reason']
        assert r['cell_key_status'] and 'cell_keys' in r
        assert not r['independent_replay'], 'inventory cannot claim replay'
        assert (ROOT/r['path']).is_file(), 'required file missing'
        if r['superseded_by']:
            assert r.get('supersession_evidence') and (ROOT/r['superseded_by']).is_file(), 'unsupported supersession'
    return True

def validate_certificates(rows,expected):
    assert rows and expected
    actual=[(r['manifest'],r['path']) for r in rows]
    assert len(actual)==len(set(actual)) and set(actual)==set(expected)
    for r in rows:
        e=expected[r['manifest'],r['path']]
        assert r['expected_bytes']==e['bytes'] and r['expected_md5']==e['md5']
        assert r['present']==(ROOT/r['path']).is_file()
        if r['present']:
            data=(ROOT/r['path']).read_bytes()
            assert hashlib.md5(data).hexdigest()==r['actual_md5'] and hashlib.sha256(data).hexdigest()==r['sha256']
            assert r['md5_match']==(r['actual_md5']==r['expected_md5'])
        else:
            assert r['historical_reason'] in ('never_written','size_guard','superseded','unknown')
            assert r['replay_status']=='MISSING'
        assert not r['independent_replay'], 'historical cert not replayed here'
    return True

def trace_validation():
    basis=[]
    for i in range(4):
        for j in range(i+1,4):
            for sign in (1,-1):
                m=[[0]*4 for _ in range(4)];m[i][j]=1;m[j][i]=sign;basis.append(m)
    for i in range(3):
        m=[[0]*4 for _ in range(4)];m[i][i]=1;m[i+1][i+1]=-1;basis.append(m)
    assert len(basis)==15 and all(sum(b[i][i] for i in range(4))==0 for b in basis)
    gram=[[sum(a[i][j]*b[j][i] for i in range(4) for j in range(4)) for b in basis] for a in basis]
    minors=[]
    for k in range(1,16):
        d=det_bareiss([r[:k] for r in gram[:k]])
        assert d!=0
        minors.append(dict(k=k,ell=k+1,determinant_Z=d,determinants_mod_p={str(p):d%p for p in (2147483647,2147483629)}))
        assert all(x!=0 for x in minors[-1]['determinants_mod_p'].values())
    bad=copy.deepcopy(gram);bad[0]=bad[1][:]
    assert det_bareiss(bad)==0, 'duplicated-row control did not fail'
    write('trace_form_validation.json',dict(status='CERTIFIED exact trace pairing arithmetic',
          basis=basis,matrix=dict(values_are='tr(A_i A_j) over Z',orientation='rows and columns: listed sl4 basis',values=gram),
          leading_minors=minors,denominators=[1],quadric_scaling='-1/2; denominator a unit at both house primes',
          controls=[dict(name='duplicated_Gram_row',rejected=True)]))

def rule_tests(index):
    def c(n,ell,d,lam=None):return dict(n=n,ell=ell,delta=d,**{'lambda':lam or [n*d-(ell-1)]+[1]*(ell-1)})
    cases=[
        ('washout_thm2',c(3,5,9),'cubic_per3_ideal',c(3,6,9)),
        ('length6_record',c(3,6,9),'cubic_per3_ideal',c(3,6,10)),
        ('degree8_global',c(3,8,8),'cubic_per3_ideal',c(3,8,9)),
        ('n4_gate_containment',c(4,4,8),'quartic_padded_gap',c(4,5,8)),
        ('cartan_ladder_invariance',c(4,9,24,[65,17]+[2]*7),'quartic_ladder_identity',c(4,9,24,[66,16]+[2]*7)),
        ('eleven_row_padded_zero',c(4,11,12),'quartic_padded_gap',c(4,10,12)),
        ('n3_padded_seven_row',c(3,7,9),'padded_gap_at_l_per2',c(3,5,9)),
        ('peaked_quartic_ladders',c(4,6,6,[14]+[2]*5),'quartic_padded_gap',c(4,6,6,[15,2,2,2,2,1])),
        ('b14_10_four_cubic_top_replacements',c(3,8,8,list(CELLS[0])),'cubic_per3_ideal',c(3,8,9))]
    logs=[]
    for ident,good,context,bad in cases:
        assert ident in {x['id'] for x in conclusions_for(index,good,context)}
        assert ident not in {x['id'] for x in conclusions_for(index,bad,context)}
        assert not conclusions_for(index,good,'wrong_context')
        logs.append(dict(rule=ident,positive=True,deliberate_bad_cell_rejected=True,wrong_context_rejected=True))
    peak=next(x for x in index['exclusions'] if x['id']=='peaked_quartic_ladders')['predicate']
    assert matches(peak,c(4,16,16,[34]+[2]*15),'quartic_padded_gap')
    assert not matches(peak,c(4,17,17,[36]+[2]*16),'quartic_padded_gap')
    assert not matches(peak,c(4,6,5,[10]+[2]*5),'quartic_padded_gap')
    assert stable_full_rank_closure(ambient_at_witness=4,stable_ambient=4,rank_lower_bound=4,dimension_verified=True,witness_verified=True)
    for kwargs in [dict(rank_lower_bound=3),dict(dimension_verified=False),dict(witness_verified=False),dict(stable_ambient=5)]:
        args=dict(ambient_at_witness=4,stable_ambient=4,rank_lower_bound=4,dimension_verified=True,witness_verified=True);args.update(kwargs)
        assert not stable_full_rank_closure(**args)
    return logs

def main():
    frozen();files=load_register('file_register.jsonl');certs=load_register('certificate_register.jsonl')
    old=read(OLD+'unparsed_sources.json');expected={}
    for p in MANIFESTS:
        m=read(p)
        for x in m.get('files',m.get('cert_files')):expected[p,x['path']]=x
    assert validate_files(files,old) and validate_certificates(certs,expected)
    controls=[]
    def reject(name,fn):
        try:fn()
        except (AssertionError,ValueError,FileNotFoundError):controls.append(dict(name=name,rejected=True))
        else:raise AssertionError(name+' accepted a bad input')
    reject('empty_inventory',lambda:validate_files([],old))
    reject('removed_source_row',lambda:validate_files([r for r in files if r['path']!=old[0]],old))
    bad=copy.deepcopy(files);bad[0]['path']='results/b14_10/missing_required_source.json'
    reject('missing_required_source',lambda:validate_files(bad,old))
    bad=copy.deepcopy(files);bad[0]['superseded_by']=old[1]
    reject('unsupported_supersession',lambda:validate_files(bad,old))
    bad=copy.deepcopy(certs);present=next(r for r in bad if r['present']);present['actual_md5']='0'*32
    reject('altered_digest',lambda:validate_certificates(bad,expected))
    reject('empty_certificate_list',lambda:validate_certificates([],expected))
    index=json.loads((ROOT/'results/integrate/inherited_exclusions.json').read_text())
    rulelog=rule_tests(index)
    good=dict(n=3,ell=6,delta=6,**{'lambda':[13,1,1,1,1,1]})
    reject('empty_predicate',lambda:matches({},good,'cubic_per3_ideal'))
    reject('unknown_predicate',lambda:matches({'a_equals':1},good,'cubic_per3_ideal'))
    reject('missing_application_contract',lambda:conclusions_for({},good,'cubic_per3_ideal'))
    trace_validation()
    replacements=[]
    for p in sorted((OUT/'recovered').glob('*.json')):
        if p.name.endswith('.validation.json'):continue
        cert=json.loads(p.read_text());assert verify(cert)
        hits=[r for r in certs if not r['present'] and r['cell_key']==cert['cell']]
        assert len(hits)==2 and {r['prime'] for r in hits}=={2147483647,2147483629}
        for r in hits:
            r['recovery_status']='EXACT_REPLACEMENT_CERTIFIED'
            r['replacement_certificate']=p.relative_to(ROOT).as_posix()
            r['original_bytes_recovered']=False
            replacements.append(dict(original_path=r['path'],replacement_certificate=r['replacement_certificate'],
                                     status='CERTIFIED replacement; original MISSING',cell=r['cell_key']))
    assert len(replacements)==8
    jsonl('certificate_register.jsonl',certs);write('replacement_map.json',replacements)
    resources=[json.loads(p.read_text()) for p in (ROOT/'results/logs').glob('b14_10_recover*.resource.json')]
    assert len(resources)==4 and sum(r['elapsed_seconds'] for r in resources)<=360
    summary=dict(status='PASS',meaning='inventory accounting, exact replacement proofs and typed predicate controls; not historical rank replay',
                 file_rows=len(files),historical_rows=len(old),certificate_rows=len(certs),replacements=len(replacements),
                 mutation_controls=controls,rule_controls=rulelog,trace_form_nonzero_minors=15,
                 exact_recovery_process_seconds=sum(r['elapsed_seconds'] for r in resources),
                 unchanged_lmr=dict(a=274,mult_det=273,mult_pad_lower_bound=269,D_interval=[-4,1]))
    write('validation.json',summary);print(json.dumps(summary,indent=2))

if __name__=='__main__':main()
