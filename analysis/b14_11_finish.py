"""Read-only mathematical validation and deterministic session artifact assembly."""
import argparse, copy, hashlib, json, math, re, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'results/b14_11'
BASE='9898e56941a7665f231873481dae956f08509995'

def read(name):return json.loads((OUT/name).read_text(encoding='utf-8'))
def save(name,obj): (OUT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def require(b,m):
    if not b:raise ValueError(m)

def audit():
    files=subprocess.check_output(['git','ls-tree','-r','--name-only',BASE],text=True).splitlines()
    files=[p for p in files if Path(p).suffix.lower() in {'.md','.tex','.html'}]
    regex=re.compile(r'\bBIP\b|Panova|occurrence\s+obstruction|closed by.*occurrence|excluded by convention',re.I)
    changed={x['path'] for x in read('prose_changes.json')};hits=[];matched_files=[]
    for path in files:
        text=(ROOT/path).read_text(encoding='utf-8',errors='replace')
        lines=text.splitlines();local=[]
        for i,line in enumerate(lines):
            if not regex.search(line):continue
            context='\n'.join(lines[max(0,i-2):i+4])
            disposition=('PROTECTED_REVIEW_SEE_B14_11_PROTECTED_ERRATA' if path in ['PROJECT_NOTES.md','paper/det3-conductor.tex','paper/det4-onset.tex','docs/boundary_deficit.html'] else 'CORRECTED_AND_REVIEWED' if path in changed else
                         'HISTORICAL_QUOTATION_OR_REGIME_WARNING' if any(x in path for x in ['batch14','dip_transfer','s37_review','s52_prompt','ambient_audit','s25_review','session_25']) else
                         'CONTEXT_REVIEWED_NO_A1_EXCLUSION')
            local.append(dict(path=path,line=i+1,text=line,context=context,disposition=disposition))
        if local:matched_files.append(path);hits.extend(local)
    require(hits,'empty prose audit')
    rules=json.loads((ROOT/'results/integrate/inherited_exclusions.json').read_text())
    old=json.loads(subprocess.check_output(['git','show',BASE+':results/integrate/inherited_exclusions.json'],text=True))
    require(rules['exclusions'][:len(old['exclusions'])]==old['exclusions'],'original predicates changed')
    save('prose_audit.json',dict(status='AUDIT_COMPLETE_WITH_PROTECTED_ERRATA',base=BASE,extensions=['.md','.tex','.html'],
         scanned_files=len(files),matching_files=len(matched_files),hits=len(hits),patterns=regex.pattern,
         matched_files=matched_files,entries=hits,protected_files_modified=False,
         interpretation='Every matched context reviewed; search is a reproducible lexical scope, not a proof about arbitrary unrecognised paraphrases. Historical quotes retain explicit corrections.'))
    print('prose coverage',len(files),'files;',len(hits),'hits in',len(matched_files),'files')

def assemble():
    rows=read('inventory.json');sizes=[read(f'shortlist_size_{i:02d}.json') for i in range(10)]
    require(len({tuple(s['lam'][1:]) for s in sizes})==10,'duplicate tails')
    save('shortlist.json',dict(board_numbering='batch14',model='gpt-6-astra',n=4,
         selection='ten distinct tails in recorded N_S order; funding choice only; no A1 suppression',
         mathematical_status='OPEN',ranks_measured_this_session=False,candidates=sizes))
    excluded=[dict(n=4,delta=r['delta'],lam=r['lam'],a=r['a'],h_pad=0,
                   conclusion='mult_pad=0; D<=0',certificate=f"results/b14_11/hpad_d{r['delta']}.json",
                   status='CERTIFIED_EXACT_COMBINATORICS') for r in rows if r['h_pad']==0]
    save('exact_exclusions.json',dict(schema='b14_11_explicit_keys_v1',count=len(excluded),cells=excluded))
    require(len(excluded)==153,'exclusion census mismatch')
    print('assembled',len(sizes),'shortlist entries and',len(excluded),'exact exclusion keys')

def session_exclusions(row,catalog):
    """Apply only the two new typed predicates; fail on incomplete certificates."""
    require(catalog.get('schema')=='b14_11_explicit_keys_v1','unsupported catalog')
    cells=catalog.get('cells');require(isinstance(cells,list) and len(cells)==catalog.get('count')==153,'missing key catalog')
    keys={(x['n'],x['delta'],tuple(x['lam'])) for x in cells}
    require(len(keys)==len(cells),'duplicate exclusion key')
    require(all(x['h_pad']==0 and x['a']>0 for x in cells),'invalid exclusion evidence')
    if row['n']!=4:return []
    d=row['delta'];lam=row['lam'];answer=[]
    require(isinstance(d,int) and d>0 and all(isinstance(x,int) and x>0 for x in lam),'invalid cell')
    require(sum(lam)==4*d and lam==sorted(lam,reverse=True),'invalid partition')
    if len(lam)>d or lam[0]<d:answer.append('quartic_length_and_eligibility')
    if (4,d,tuple(lam)) in keys:answer.append('quartic_pullback_zero')
    return answer

def verify(limit=True):
    # Memory-limit before numerical imports, matching every other calculation.
    from b14_11_run import memory_limit,peak_memory
    if limit:memory_limit()
    from b14_11_work import all_census,exact_a,strips,eligible,validate_rows,validate_rules
    from wk9_s42_hpad import pieri_strips
    from b14_11_sizes import burnside
    rows=all_census();require(len(rows)==2734,'census count')
    sizes=read('shortlist.json')['candidates'];require(len(sizes)==10,'shortlist missing')
    queue=read('cost_queue.json');expected=[];tails=set()
    for r in queue:
        t=tuple(r['lam'][1:])
        if t in tails:continue
        tails.add(t);expected.append((r['delta'],r['lam']))
        if len(expected)==10:break
    require(expected==[(s['delta'],s['lam']) for s in sizes],'selection rule')
    verified=[]
    for s in sizes:
        require(eligible(s),'shortlist eligibility')
        a=exact_a(s['lam'],s['delta']);require(a==s['a'],'shortlist a')
        fresh=burnside(s['lam'],s['delta'])
        for field in ['N_S','n_chi','stabilizer_order','signed_trace_sum','classes']:
            # json turns tuples into lists
            require(json.dumps(fresh[field])==json.dumps(s[field]),'size '+field)
        hp=sum(exact_a(nu,s['delta'],3) for nu in strips(s['lam'],s['delta']))
        require(hp==s['h_pad'],'shortlist hpad')
        verified.append(dict(delta=s['delta'],lam=s['lam'],a=a,h_pad=hp,N_S=s['N_S'],n_chi=s['n_chi']))
    # Cross-check every fresh horizontal-strip list against the banked enumerator,
    # and re-evaluate the complete set of distinct cubic coefficients exactly.
    cache={}; hpkeys={};cubic_den=[]
    from wk8_s30_pleth import pleth_p,chi
    for d in range(5,9):
        for r in read(f'hpad_d{d}.json'):
            lam=r['lam'];new=set(strips(lam,d));old={tuple(x for x in nu if x) for nu in pieri_strips(lam,d)}
            stored={tuple(c['nu']) for c in r['channels']}
            require(new==old==stored,'horizontal strips differ')
            require(len(stored)==len(r['channels']),'duplicate channel')
            total=0
            for c in r['channels']:
                k=(d,tuple(c['nu']))
                if k not in cache:
                    cache[k]=exact_a(c['nu'],d,3)
                    if len(cache)%32==0:chi.cache_clear()
                require(cache[k]==c['a3'],'channel coefficient');total+=cache[k]
            require(total==r['h_pad'],'pullback sum');hpkeys[(d,tuple(lam))]=total
        den=math.lcm(*(v.denominator for v in pleth_p(d,3).values()))
        require(all(math.gcd(den,q)==1 for q in [2147483647,2147483629]),'bad denominator')
        cubic_den.append(dict(delta=d,denominator=str(den),prime_unit=True))
    ex=read('exact_exclusions.json')['cells'];require(len(ex)==153,'empty/wrong exclusions')
    require({(e['delta'],tuple(e['lam'])) for e in ex}=={k for k,v in hpkeys.items() if v==0},'exclusion equality')
    validate_rules(json.loads((ROOT/'results/integrate/inherited_exclusions.json').read_text())['exclusions'])
    catalog=read('exact_exclusions.json')
    require(sum(bool(session_exclusions(r,catalog)) for r in rows)==153,'typed matcher census')
    require(not any(session_exclusions(s,catalog) for s in sizes),'shortlist accidentally excluded')
    require(session_exclusions(dict(n=4,delta=6,lam=[12,2,2,2,2,2,2]),catalog)==['quartic_length_and_eligibility'],'length predicate')
    require(session_exclusions(dict(n=4,delta=6,lam=[4,4,4,4,4,4]),catalog)==['quartic_length_and_eligibility'],'first-row predicate')
    require(session_exclusions({**ex[0],'n':3},catalog)==[],'cross-model exclusion')
    # Exercise artifact controls with explicit wrong values, including absent inputs.
    rejected=[]
    tests=[('wrong_shortlist_a',lambda:require(sizes[0]['a']+1==exact_a(sizes[0]['lam'],sizes[0]['delta']),'bad a')),
           ('wrong_size',lambda:require(sizes[0]['n_chi']+1==verified[0]['n_chi'],'bad size')),
           ('wrong_hpad',lambda:require(hpkeys[(sizes[0]['delta'],tuple(sizes[0]['lam']))]+1==sizes[0]['h_pad'],'bad hp')),
           ('empty_artifact',lambda:validate_rows([])),
           ('missing_artifact',lambda:read('deliberately_absent_required_input.json')),
           ('empty_key_catalog',lambda:session_exclusions(sizes[0],{**catalog,'cells':[]}))]
    for name,fn in tests:
        try:fn()
        except (ValueError,FileNotFoundError):rejected.append(name)
        else:raise AssertionError(name+' was accepted')
    save('validation.json',dict(status='PASS',verified_shortlist=verified,census_positive_labels=len(rows),
         complete_strip_lists_checked=len(hpkeys),distinct_cubic_counts_rechecked=len(cache),
         exact_exclusions=len(ex),cubic_denominators=cubic_den,mutations_rejected=rejected,
         peak_working_set_bytes=peak_memory(),rank_or_equation_certificate_claimed=False))
    print('validation PASS: 10 sizes, 2734 strip lists,',len(cache),'cubic coefficients, 153 exact exclusions; 6 mutations rejected')

def inputs():
    names=set(read('inventory_summary.json')['consumed_historical_files'])
    names.update(read('prose_audit.json')['matched_files'])
    names.update(['docs/batch14_board.md','docs/PROVED.md','docs/brief_wording.md','docs/batch14_reconciliation.md',
         'docs/b14_claude_scratch_code.md','docs/bip_transfer.md','docs/dip_transfer.md','docs/n4_gate.md',
         'docs/dispatch/B14-11_packet.md','results/integrate/inherited_exclusions.json',
         'analysis/wk8_s30_pleth.py','analysis/wk9_s42_census.py','analysis/wk9_s42_hpad.py',
         'analysis/wk9_int_record.py','tools/integrate/reconcile_cells.py','tools/delivery/check_delivery.py'])
    out=[]
    for n in sorted(names):
        raw=subprocess.check_output(['git','show',BASE+':'+n]);blob=subprocess.check_output(['git','rev-parse',BASE+':'+n],text=True).strip()
        out.append(dict(path=n,base_blob=blob,base_bytes=len(raw),base_sha256=hashlib.sha256(raw).hexdigest()))
    save('input_manifest.json',dict(base_commit=BASE,base_tree='cb688cd3fe454d638f3202e759e2eaa0c629739f',inputs=out,
         external_sources=[dict(url='https://arxiv.org/pdf/1604.06431',version='v3, 2018-09-17',
          accessed_utc='2026-09-12',locations='pages 2-5; definition (1.2), Theorems 1.4/2.1, Proposition 2.3 and sharp notation')]))
    print('input manifest',len(out),'frozen blobs')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['audit','assemble','verify','inputs']);args=p.parse_args();globals()[args.mode]()
