import tkinter.filedialog as fd
import dearpygui.dearpygui as dpg
import os
from os import _exit as exitfunc
from typing import Optional
import PatchAPK as patchapk
import fgi
import webbrowser as web_brow
import win32gui, win32con
def GetValue(value_tag):
    return dpg.get_value(value_tag)
def Patching():
    return patchapk.PatchAPK(GetValue("apkpatch_val"), GetValue("fd_apkpatcher_val"))
def DPG_Createcontext():
    return dpg.create_context()
def DPG_CreateViewport(titlename : str, width_int : int, height_int : int, windowname: Optional[str]):
    dpg.create_viewport(title=titlename, width=width_int, height=height_int)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window(windowname, True)
    dpg.start_dearpygui()
    dpg.destroy_context()
def Main_GraphicalUserInterf():
        DPG_Createcontext()
        with dpg.font_registry():
            intelonemono = dpg.add_font("{}".format(os.getcwd() + "\\INTELONEMONOITAL.ttf"), 16)
        with dpg.window(label="APKPatcher by RikkoMatsumato", tag="windows_apkpatcher", width=600, height=600):
            dpg.add_text("This is My Program for Patching .apk Games(Only works IL2Cpp Games... Maybe, I Don't Testing this!!!)... \nSo Enjoy to use!!!")
            dpg.add_input_text(label="Write You're File Directory for Patching APK File", tag="fd_apkpatcher_val")
            dpg.add_input_text(label="Write APK File(Also Remember you're directory)!!!", tag="apkpatch_val")
            dpg.add_button(label="Patching!!!", callback=Patching)
            with dpg.menu(label="Donations"):
                dpg.add_button(label="DonationAlerts", callback=lambda: web_brow.open("https://www.donationalerts.com/r/rikkomatsumato"))
                dpg.add_text("BTC Wallet: \nbc1qz987mqatjrhuurme49sleq75a80atysgyska9e")
        dpg.bind_font(intelonemono)
        DPG_CreateViewport("APKPatcher by RikkoMatsumato", 600, 600, "windows_apkpatcher")
        hwnd = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
