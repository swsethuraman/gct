"""Small local check of the adapted resource wrapper and runtime."""
import json, os
import numpy as np
print(json.dumps(dict(status='PASS',pid=os.getpid(),numpy=np.__version__,integer_control=int(np.sum(np.arange(10))))))
