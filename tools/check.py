# check_one.py — run exactly one file against the dataset test
from datasets import load_dataset
from pathlib import Path
import importlib.util, sys, tempfile, os, subprocess, textwrap

TASK_NUM = "59"  # <-- change to match the file you're testing
FILE = Path(f"outputs/GPT5/CoT_fail/{TASK_NUM}.py")  # <-- adjust path if needed

ds = load_dataset("evalplus/humanevalplus")["test"]
spec = {r["task_id"]: r for r in ds}[f"HumanEval/{TASK_NUM}"]

candidate = FILE.read_text(encoding="utf-8")
test_code = spec["test"]
entry = spec["entry_point"]

# Append an explicit pytest test so collection always runs
test_fixed = test_code.rstrip() + f"""
import importlib
_mod = importlib.import_module('candidate')
_fn = getattr(_mod, '{entry}')
def test_eval():
    check(_fn)
"""

with tempfile.TemporaryDirectory() as td:
    open(os.path.join(td,"candidate.py"),"w").write(candidate)
    open(os.path.join(td,"test_candidate.py"),"w").write(test_fixed)
    print("Entry point expected:", entry)
    print("Running pytest...")
    p = subprocess.run([sys.executable,"-m","pytest","-q","test_candidate.py"],
                       cwd=td, capture_output=True, text=True)
    print("RC:", p.returncode)
    print(p.stdout)
    print(p.stderr)

