import subprocess
from pathlib import Path
import os
def run_command_and_check(cmd: list[str | Path]):
    try:
        return subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode()
    except:
        print("Failed!!!")
        os._exit(334)