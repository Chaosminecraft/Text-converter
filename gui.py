import ctypes, threading
from tkinter import *

try:
    from converter import parse_input
except ImportError:
    result=ctypes.windll.user32.MessageBoxW(0, "The Converter module is not found, Please download the code again, I can maybe in some time make that it isn't an issue. Do you wanna contiue?", "Woops, Import error!", 1)
    if result==2:
        exit()

try:
    from settings import gui_settings
except ImportError:
    result=ctypes.windll.user32.MessageBoxW(0, "The Settigns module is not found, Please download the code again, I can maybe in some time make that it isn't an issue. Do you wanna contiue?", "Woops, Import error!", 1)
    if result==2:
        exit()

class GuiConfig:
    window=""
    operator=""
    convert=""
    deconvert=""
    