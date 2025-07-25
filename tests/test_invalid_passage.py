import subprocess
import sys
import os
from pathlib import Path


def test_invalid_passage_exits_gracefully():
    repo_root = Path(__file__).resolve().parents[1]
    env = os.environ.copy()
    stub_path = str(Path(__file__).resolve().parent / "stubs")
    env["PYTHONPATH"] = stub_path + os.pathsep + env.get("PYTHONPATH", "")
    result = subprocess.run([sys.executable, str(repo_root / "bible"), "invalid"], capture_output=True, text=True, env=env)
    assert result.returncode == 0
    assert result.stdout.strip() == ""
