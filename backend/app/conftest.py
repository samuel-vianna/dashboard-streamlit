import sys
import pathlib

# ensure the backend package root is on sys.path so tests can import 'app' absolutely
ROOT = pathlib.Path(__file__).resolve().parents[0]
BACKEND_ROOT = ROOT
sys.path.insert(0, str(BACKEND_ROOT))
