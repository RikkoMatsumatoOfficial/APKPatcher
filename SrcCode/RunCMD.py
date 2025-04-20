import subprocess
from pathlib import Path
import os
def run_command(cmd: list[str | Path]):
    try:
        print(f"running {cmd}")
        return subprocess.run(cmd, stderr=subprocess.STDOUT, stdin=subprocess.STDOUT, stdout=subprocess.STDOUT)
    except:
        print(f"Failed to Run {cmd}!!!")
        os._exit(334)
