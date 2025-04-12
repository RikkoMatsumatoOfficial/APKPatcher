import tkinter.filedialog as fd
import dearpygui.dearpygui as dpg
import os
from os import _exit as exitfunc
from typing import Optional
import PatchAPK as patchapk
def GetValue(value_tag):
    return dpg.get_value(value_tag)
def DPG_Createcontext():
    return dpg.create_context()
def DPG_CreateViewport(titlename : str, width_int : int, height_int : int, windowname: Optional[str]):
    dpg.create_viewport(title=titlename, width=width_int, height=height_int)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window(windowname, True)
    dpg.start_dearpygui()
    dpg.destroy_context()
class GUI():
    def Main_GraphicalUserInterf():
        patchapk.CheckIfFGI_IsInstalled()
        DPG_Createcontext()
        with dpg.window(label="APKPatcher by RikkoMatsumato", tag="windows_apkpatcher", width=600, height=600):
            dpg.add_text("This is My Program for Patching .apk Games(Only works IL2Cpp Games)... \nSo Enjoy to use!!!")
            dpg.add_input_text(label="Write You're File Directory for Patching APK File", tag="fd_apkpatcher_val")
            dpg.add_button(label="Patching!!!", callback=lambda:print("Coming Soon!!!"))
        DPG_CreateViewport("APKPatcher by RikkoMatsumato", 600, 600, "windows_apkpatcher")
