"""Literal mixed-bracket comparisons in multiple independent directions."""
import json,math,random,sys
from pathlib import Path
sys.path.insert(0,str(Path('tools/verify').resolve()))
import ci73_eval as ev
import ci73_linear as la

def main():
    rng=random.Random(731303);ce=ev.exps(3,3)
    pts=[dict(linear=[rng.randint(-4,4) for _ in range(3)],
              cubic_coefficients=[rng.randint(-4,4) for _ in ce]) for _ in range(8)]
    symbols=[ev.mixed_symbols(pt,ce) for pt in pts]
    rows=[];records=[];attempts=0
    while len(rows)<8 and attempts<5000:
        attempts+=1;letters=[0,1,2]+[x for x in range(3,6) for _ in range(3)];rng.shuffle(letters)
        f=dict(h=3,val=[1]*3+[3]*3,C1=letters[:3],C2=letters[3:6],two=[letters[6:8],letters[8:10]],one=letters[10:])
        try:ev.filling(f)
        except ValueError:continue
        values=[ev.literal(f,s) for s in symbols]
        if not any(values):continue
        for p in [0,2147483647,2147483629]:
            result,receipt=ev.evaluate(f,symbols,p,name=f'ci73_literal_mixed_{len(rows)}_{p}')
            ev.need(result==[v%p if p else v for v in values],'literal mixed disagreement')
        rows.append(values);records.append(dict(filling=f,exact_values=values))
    rank=la.rank_q(rows)
    ev.need(len(rows)==8 and rank>=2,'literal fixtures do not span two independent directions')
    Path('results/ci73/literal_controls.json').write_text(json.dumps(dict(status='PASS',
        comparisons=8*8*3,independent_directions=rank,attempts=attempts,points=pts,records=records),indent=2)+'\n')
    print(json.dumps(dict(status='PASS',comparisons=192,independent_directions=rank)))

if __name__=='__main__':main()
