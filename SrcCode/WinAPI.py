import ctypes
import sys
def ImportKernel32():
    return ctypes.cdll.LoadLibrary("Kernel32.dll")

def freopen(filename, mode):
    if mode == "r":
        sys.stdin = open(filename, mode)

    elif mode == "w":
        sys.stdout = open(filename, mode)

def AllocateConsole():
    ImportKernel32().AllocConsole()
    freopen("CONOUT$", "w")