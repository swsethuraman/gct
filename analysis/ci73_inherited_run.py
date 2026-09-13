import json,sys
from pathlib import Path
sys.path.insert(0,str(Path('tools/verify').resolve()))
import ci73_inherited
result=ci73_inherited.verify(Path('.'))
Path('results/ci73/inherited_replay.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result),flush=True)
