from os import _exit as exitfunc
import importlib.util as ut
foundedfgi = True
def CheckIfFGI_IsInstalled():
    try:
        return ut.find_spec("fgi")
        
    except:
        print("Please Install FGI via Github Link!!! Thanks!!!")
        exitfunc(3221)
