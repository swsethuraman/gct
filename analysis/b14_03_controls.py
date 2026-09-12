"""Adversarial replay: mutations, exact rescaling, and an extra symbolic oracle."""
import copy
from fractions import Fraction as Q
import json
import gzip
from pathlib import Path
import sys
import time

sys.path.insert(0,str(Path('tools/verify').resolve()))
import complete_interpolation as ci
import b13_03_exact as producer_oracle

OUT = Path('results/b14_03')


def change(cert,path,value=None,delete=False):
    p = cert
    for key in path[:-1]:
        p = p[key]
    if delete:
        del p[path[-1]]
    else:
        p[path[-1]] = value


def dict_paths(obj,path=()):
    if type(obj) is dict:
        for k,v in obj.items():
            yield path+(k,)
            yield from dict_paths(v,path+(k,))
    elif type(obj) is list:
        for i,v in enumerate(obj):
            yield from dict_paths(v,path+(i,))


def main():
    start = time.perf_counter()
    base = ci.load(OUT/'control.json')
    cases = []
    records = []
    def run(name, edits, expected='FAIL', code=None):
        cert = copy.deepcopy(base)
        for edit in edits:
            change(cert,edit['path'],edit.get('value'),edit.get('delete',False))
        r = ci.verify(cert)
        good = r['status'] == expected and (code is None or r.get('code') == code)
        cases.append({'name':name,'edits':edits,'expected_status':expected,'expected_code':code})
        records.append({'name':name,'test_passed':good,'result':r})
        if not good:
            raise RuntimeError(f'{name}: expected {expected}/{code}, got {r}')
        return cert
    def e(path,value):
        return {'path':path.split('.'),'value':value}
    run('complete_control',[],'PASS')
    run('wrong_points',[{'path':['points',0,'l'],'value':[2,0,0]}],code='target_entries')
    run('wrong_source_scaling',[e('source_arithmetic.row_denominators',[2,1])],code='source_scaling')
    cols = copy.deepcopy(base['target']['members'][0]['columns'])
    cols[0][2] = 6
    run('invalid_target_membership',[{'path':['target','members',0,'columns'],'value':cols}],code='target_membership')
    cols[5][2] = 7  # preserve every valence; repeated letter forces zero polynomial
    run('rank_deficient_target',[
        {'path':['target','members',0,'columns'],'value':cols},
        e('target.evaluation.entries',[[0,0]]),e('target.minor.determinant',0)],code='target_rank')
    p = ci.PRIMES[0]
    run('insufficient_CRT_modulus',[
        e('source_arithmetic.crt.primes',[p]),e('source_arithmetic.crt.modulus',p),
        e('source_arithmetic.crt.residues',{str(p):base['source_arithmetic']['entries']})],code='crt_insufficient')
    run('one_altered_integer_entry',[
        {'path':['source_arithmetic','entries',0,0],'value':730}],code='source_entries')
    run('congruent_wrong_integer_lift',[
        {'path':['source_arithmetic','entries',0,0],'value':729+base['source_arithmetic']['crt']['modulus']}],code='source_entries')
    run('bad_CRT_residue',[
        {'path':['source_arithmetic','crt','residues',str(p),0,0],'value':730}],code='crt_residues')
    run('wrong_target_dimension',[e('target.dimension_proof.dimension',2)],code='target_dimension')
    run('wrong_source_dimension',[e('source.dimension_proof.dimension',3)],code='source_dimension')
    run('empty_points',[e('points',[])],'UNPARSEABLE','points')
    run('empty_target_members',[e('target.members',[])],'UNPARSEABLE','members')
    run('empty_source_basis',[e('source.basis',[])],'UNPARSEABLE','source_basis')
    run('missing_cubic_coordinate',[{'path':['points',0,'cubic',0],'delete':True}],'UNPARSEABLE','points')
    run('duplicate_cubic_coordinate',[{'path':['points',0,'cubic',0],'value':base['points'][0]['cubic'][1]}],'UNPARSEABLE','points')
    run('wrong_values_are',[e('source_arithmetic.values_are','normalized values')],'UNPARSEABLE','values_are')
    run('wrong_orientation',[e('conventions.orientation','A K=0')],'UNPARSEABLE','conventions')
    run('unknown_member_key',[{'path':['target','members',0,'untrusted_proof'],'value':'proved'}],'UNPARSEABLE','schema')
    run('unsupported_large_profile',[e('profile','degree13')],'UNPARSEABLE','unsupported_profile')
    run('wrong_source_polynomial',[{'path':['source','basis',0,0,1],'value':'289'}],code='source_membership')
    run('source_rank_loss',[e('source.change_of_basis',[[1,1],[1,1]])],code='source_scaling')
    run('wrong_left_kernel',[e('kernel.entries',[[1],[1]])],code='left_kernel')
    # The actual right kernel of A is (49,-9); it must not pass as a source relation.
    run('right_kernel_in_source_coordinates',[e('kernel.entries',[[49],[-9]])],code='left_kernel')
    rational = run('consistent_rational_rescaling',[
        e('source.change_of_basis',[['1/2','1/2'],[0,'1/3']]),
        e('source_arithmetic.row_denominators',[2,3]),e('kernel.entries',[[2],[-3]])],'PASS')
    (OUT/'rational_control.json').write_text(json.dumps(rational,indent=2)+'\n')
    compressed = OUT/'control.json.gz'
    compressed.write_bytes(gzip.compress((OUT/'control.json').read_bytes(),mtime=0))
    if ci.load(compressed) != base:
        raise RuntimeError('gzip certificate roundtrip failed')
    run('prime_divides_denominator',[
        e('source.change_of_basis',[[f'1/{p}',f'1/{p}'],[0,1]]),
        e('source_arithmetic.row_denominators',[p,1]),e('kernel.entries',[[p],[-1]])],code='denominator_prime')
    # Every dictionary key is mandatory in this profile; delete each independently.
    required_paths = list(dict_paths(base))
    for path in required_paths:
        run('missing:'+'.'.join(map(str,path)),[{'path':list(path),'delete':True}],'UNPARSEABLE')
    # Exact coefficient comparison with the OLD universal-pullback instrument.
    # This is an additional oracle, not used by CI's acceptance path.
    _,E,source = producer_oracle.load_source('results/b13_03/primary_source.json')
    images,counts = producer_oracle.full_pullback(source,E,4,3,6,(8,8,8))
    target,TE = ci.bracket_polynomial(json.dumps(base['target']['members'][0],sort_keys=True))
    C = producer_oracle.exps(3,3)
    converted = {}
    for (eta,word),v in images[1].items():
        factors = [TE.index(tuple(int(i==j) for i in range(3))) for j in range(3) for _ in range(eta[j])]
        factors += [TE.index(C[j]) for j in word]
        converted[tuple(sorted(factors))] = int(v)*288
    if images[0] or converted != target:
        raise RuntimeError('independent universal identity G = 288 mu*(F1) failed')
    extra = {'mu_star_F0_zero':not images[0],'G_equals_288_mu_star_F1':converted==target,
             'all_coefficients_compared':len(target),'producer_expansion_counts':counts}
    # Strict JSON loader must also reject duplicate object keys.
    dup = OUT/'duplicate_key_control.json'
    dup.write_text('{"kind":"complete_interpolation","kind":"complete_interpolation"}\n')
    try:
        ci.load(dup)
    except ci.Rejected as exc:
        if exc.code != 'duplicate_key':
            raise
    else:
        raise RuntimeError('duplicate JSON key accepted')
    bad = copy.deepcopy(base)
    bad['source_arithmetic']['entries'][0][0] += 1
    (OUT/'corrupted_entry_control.json').write_text(json.dumps(bad,indent=2)+'\n')
    (OUT/'missing_input_control.json').write_text(json.dumps({k:v for k,v in base.items() if k!='points'},indent=2)+'\n')
    result = {'status':'PASS','test_count':len(records),'negative_count':sum(r['result']['status']!='PASS' for r in records),
              'required_key_deletions':len(required_paths),'cases':records,'extra_symbolic_oracle':extra,
              'duplicate_json_key_rejected':True,'wall_seconds':time.perf_counter()-start}
    (OUT/'control_mutations.json').write_text(json.dumps(cases,indent=2)+'\n')
    (OUT/'control_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='cases'}),flush=True)


if __name__ == '__main__':
    main()
