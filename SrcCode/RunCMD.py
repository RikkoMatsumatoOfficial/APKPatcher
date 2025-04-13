import subprocess
from pathlib import Path
import os
def run_command(cmd: list[str | Path]):
    try:
        return subprocess.run(cmd, stderr=subprocess.STDOUT)
    except:
        print("Failed!!!")
        os._exit(334)
