# eval/eval.py
import argparse, os, re, sys, tempfile, subprocess, ast
from pathlib import Path
import pandas as pd

# Optional colors
GREEN = "\033[92m"; RED = "\033[91m"; YELLOW = "\033[93m"; CYAN = "\033[96m"; RESET = "\033[0m"
try:
    from colorama import init as _colorama_init
    _colorama_init()
except Exception:
    GREEN = RED = YELLOW = CYAN = RESET = ""

# ------------------------- Dataset --------------------------------------------
def load_hevplus_index():
    """
    Load HumanEval+ ('evalplus/humanevalplus') → dict[task_id] = {entry_point, test}
    """
    from datasets import load_dataset
    ds = load_dataset("evalplus/humanevalplus")["test"]
    return {
        row["task_id"]: {"entry_point": row["entry_point"], "test": row["test"]}
        for row in ds
    }

# ------------------------- Sanitizers -----------------------------------------
FENCE_BLOCK_RE = re.compile(r"```(?:python)?\s*(.*?)```", re.DOTALL)
FENCE_LINE_RE  = re.compile(r"^\s*```(?:python)?\s*$|^\s*```\s*$")

def extract_code_from_text(s: str) -> str:
    """
    If file contains markdown fences/prose, extract the largest fenced code block;
    else strip leading/trailing fence lines. Otherwise return as-is.
    """
    mblocks = FENCE_BLOCK_RE.findall(s)
    if mblocks:
        return max(mblocks, key=len)
    lines = s.splitlines()
    while lines and FENCE_LINE_RE.match(lines[0]): lines.pop(0)
    while lines and FENCE_LINE_RE.match(lines[-1]): lines.pop()
    return "\n".join(lines)

def maybe_autofix_entrypoint(py_code: str, expected_name: str) -> str:
    """
    If expected entry point is missing but there's exactly one top-level def,
    rename it to expected_name (simple line replacement).
    """
    try:
        tree = ast.parse(py_code)
    except SyntaxError:
        return py_code  # let pytest report it

    defs = [n for n in tree.body if isinstance(n, ast.FunctionDef)]
    if any(d.name == expected_name for d in defs):
        return py_code
    if len(defs) == 1:
        old = defs[0].name
        pattern = re.compile(rf"^(\s*)def\s+{re.escape(old)}\s*\(", re.MULTILINE)
        fixed, n = pattern.subn(r"\1def " + expected_name + "(", py_code, count=1)
        return fixed if n == 1 else py_code
    return py_code

# ------------------------- Harness patch --------------------------------------
def build_pytest_harness(entry_point: str) -> str:
    """
    Always append a real pytest test so PyTest never exits with 'no tests collected'.
    Assumes the original test code defines `check`.
    """
    return f"""
# --- Appended by evaluator to ensure pytest runs at least one test ---
import importlib
_mod = importlib.import_module('candidate')
try:
    _fn = getattr(_mod, '{entry_point}')
except AttributeError as e:
    raise AssertionError("Entry point '{entry_point}' not found in candidate") from e

def test_eval():
    # Call the dataset-provided 'check' function with our candidate entry point
    check(_fn)
"""

# ------------------------- Runner ---------------------------------------------
def run_pytest_on_candidate(py_code: str, test_code: str, entry_point: str, timeout_sec: int = 20):
    """
    Execute candidate code against provided tests in an isolated temp directory.
    Returns (passed: bool, logs: str).
    """
    # Clean & normalize candidate code
    py_code = extract_code_from_text(py_code)
    py_code = maybe_autofix_entrypoint(py_code, entry_point)

    # Ensure PyTest collects a test by appending our own test
    test_fixed = test_code.rstrip() + "\n" + build_pytest_harness(entry_point)

    with tempfile.TemporaryDirectory() as td:
        cand_path = os.path.join(td, "candidate.py")
        test_path = os.path.join(td, "test_candidate.py")

        with open(cand_path, "w", encoding="utf-8") as f: f.write(py_code)
        with open(test_path, "w", encoding="utf-8") as f: f.write(test_fixed)

        proc = subprocess.run(
            [sys.executable, "-m", "pytest", "-q", test_path],
            capture_output=True, text=True, timeout=timeout_sec
        )
        passed = (proc.returncode == 0)
        logs = (proc.stdout or "") + ("\n" + (proc.stderr or ""))
        return passed, logs

# ------------------------- Filename → task_id ---------------------------------
def map_filename_to_taskid(pyfile: Path) -> str:
    """
    Accept names like '103.py' → HumanEval/103
    Also tolerates 'HumanEval_103.py' or 'task103.py'.
    """
    stem = pyfile.stem
    if stem.lower().startswith("humaneval_"):
        stem = stem.split("_", 1)[1]
    elif stem.lower().startswith("task"):
        stem = stem[4:]
    return f"HumanEval/{stem}"

# ------------------------- Main ----------------------------------------------
def main():
    ap = argparse.ArgumentParser(description="Evaluate model outputs on HumanEval+ tests.")
    ap.add_argument("--outputs-root", default="outputs", help="Root with <Model>/<Strategy>/*.py")
    ap.add_argument("--out-csv", default="reports/eval_results.csv", help="CSV path for detailed results")
    ap.add_argument("--per-task", default="reports/per_task.csv", help="Optional per-task pass matrix CSV")
    ap.add_argument("--timeout", type=int, default=20, help="Per-test timeout seconds")
    args = ap.parse_args()

    out_root = Path(args.outputs_root)
    if not out_root.exists():
        print(f"{RED}ERROR:{RESET} outputs root not found: {out_root}")
        sys.exit(1)

    Path(args.out_csv).parent.mkdir(parents=True, exist_ok=True)
    if args.per_task: Path(args.per_task).parent.mkdir(parents=True, exist_ok=True)

    print(f"{CYAN}Loading HumanEval+ index...{RESET}")
    index = load_hevplus_index()

    rows = []
    for model_dir in sorted(out_root.iterdir()):
        if not model_dir.is_dir(): continue
        model = model_dir.name  # e.g., GPT5, Gemini2.5
        for strat_dir in sorted(model_dir.iterdir()):
            if not strat_dir.is_dir(): continue
            strategy = strat_dir.name  # e.g., CoT, SelfDebug
            for pyfile in sorted(strat_dir.glob("*.py")):
                task_id = map_filename_to_taskid(pyfile)
                spec = index.get(task_id)
                if not spec:
                    print(f"{YELLOW}[WARN]{RESET} {pyfile} -> {task_id} not in HumanEval+; skipping")
                    continue

                candidate = pyfile.read_text(encoding="utf-8")
                passed, log = run_pytest_on_candidate(
                    candidate, spec["test"], spec["entry_point"], args.timeout
                )
                status = f"{GREEN}PASS{RESET}" if passed else f"{RED}FAIL{RESET}"
                print(f"[{status}] {model}/{strategy}/{pyfile.name}")
                rows.append(dict(
                    task_id=task_id, model=model, strategy=strategy,
                    filename=str(pyfile), passed=bool(passed), log=log[:4000]
                ))

    if not rows:
        print(f"{YELLOW}No .py files found under {out_root}{RESET}")
        return

    df = pd.DataFrame(rows)
    df.to_csv(args.out_csv, index=False)
    print(f"\nSaved detailed results → {args.out_csv}")

    # Summary pass@1
    summary = df.groupby(["model","strategy"])["passed"].mean().reset_index()
    summary = summary.rename(columns={"passed":"pass@1"})
    print("\n=== Summary pass@1 ===")
    try:
        from tabulate import tabulate
        print(tabulate(summary, headers="keys", tablefmt="github", showindex=False))
    except Exception:
        print(summary.to_string(index=False))

    # Optional per-task matrix
    if args.per_task:
        per_task = df.pivot_table(index="task_id",
                                  columns=["model","strategy"],
                                  values="passed",
                                  aggfunc="max").fillna(False).astype(bool)
        per_task.to_csv(args.per_task)
        print(f"Saved per-task matrix → {args.per_task}")

if __name__ == "__main__":
    main()


