"""Second character route: geometric border strips, including skew characters."""
import importlib.util
import json
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
from time import perf_counter
ROOT=Path(__file__).resolve().parent
def load(name,path):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
f=load('finite',ROOT/'screen_finite.py');t=f.t
r=load('receiver',ROOT.parent/'work/batch15_workers/B15-02/analysis/b16_02_receive.py')
@lru_cache(None)
def skew(lam,mu,rho):
    if len(lam)<len(mu) or any(a<b for a,b in zip(lam,mu)):return 0
    if not rho:return int(lam==mu)
    return sum(sign*skew(nu,mu,rho[1:]) for nu,sign in r.border_strips(lam,rho[0]))

start=perf_counter();finite=json.loads((ROOT/'finite_screen.json').read_text());checked=0
for row in finite['rows']:
    tail=(row['t'],)+(2,)*8
    delta=0
    for c in row['correction_terms']:
        v=sum((a*skew(tail,tuple(c['hook']),rho) for rho,a in f.G(c['b'],c['m']).items()),Q())
        assert v==c['lr_pairing'],(row,c,v)
        delta+=(-1)**(sum(tail)-c['m']-row['d']+c['b'])*int(v)
        checked+=1
    assert delta==row['correction'] and row['a']==row['stable_a']+delta
    skew.cache_clear();r.border_strips.cache_clear()
print(json.dumps(dict(finite='PASS',correction_terms=checked)),flush=True)
# Recalculate all degree7 screen characters using geometric, not beta-number, hooks.
screen=json.loads((ROOT/'degree7_screen.json').read_text())
t.char=r.character
for row in screen['rows']:
    lam=tuple(row['weight']);a=t.pleth_mult(7,4,lam)
    g,tr,s,_=t.kron(lam,(7,)*4)
    raw=sum(t.pleth_mult(7,3,mu) for mu in t.parts(21) if len(mu)<=7 and t.horizontal(lam,mu))
    assert (a,g,tr,s,raw)==(row['a'],row['g'],row['t'],row['s'],row['source_raw'])
    r.character.cache_clear();r.border_strips.cache_clear()
result=dict(status='PASS',finite_correction_terms=checked,degree7_rows=len(screen['rows']),
            seconds=perf_counter()-start,
            independent='Geometric border-strip characters vs beta numbers; skew MN vs skew Jacobi-Trudi',
            shared='Power-sum plethysm expansion and finite hook formula; inherited stable counts and ideal dimensions')
(ROOT/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result),flush=True)
