from os import _exit as exitfunc
import importlib.util as ut
import os
def CheckIfFGI_IsInstalled():
    try:
        return ut.find_spec("fgi")
        
    except:
        os.system("pip install git+https://github.com/commonuserlol/fgi")
        print("Installed Successfully!!! Please Make Sure what Android NDK or Android Build Tools is Set as System Environment(Console Commands!!!)")
        exitfunc(3221)
