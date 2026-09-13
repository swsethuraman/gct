"""Slot-local command for the independent degree14 verifier."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"tools/verify"))
from b15_01_ci159 import main
if __name__ == "__main__":
    main()
