from os import _exit as exitfunc
import importlib.util as ut
import os
from RunCMD import run_command
from time import sleep
def CheckIfFGI_IsInstalled():
    try:
        return ut.find_spec("fgi")
        
    except:
        os.system("pip install git+https://github.com/commonuserlol/fgi")
        print("Installed Successfully!!! Please Make Sure what Android NDK or Android Build Tools is Set as System Environment(Console Commands!!!)")
        exitfunc(3221)

def PatchAPK(apk_path: str, path_indexjs : str):
    try:
        CheckIfFGI_IsInstalled()
        cmd_line = ["fgi", "-i", "{}.apk".format(apk_path), "-t script", "-l {}".format(path_indexjs),]
        delimiter_space = " "
        print(delimiter_space.join(cmd_line))
        run_command(delimiter_space.join(cmd_line))

    except:
        print(f"Failed to Execute {cmd_line}")
        sleep(14)
        exitfunc(221)
