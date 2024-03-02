import os
import locale as loc
from tkinter import *

def logg_settings(error_nofile, language):
    if error_nofile.lower()=="logger":

        setting="yes"
        with open("logger.txt", "w")as f:
            f.write(setting)
        error_nofile = "false"
        return error_nofile

    if language=="en":
        print(f"\nDo you want to log the stuff?\n")
        setting=input("Yes or no? ")
        setting.lower()
        logg=setting
        with open("logger.txt", "w") as f:
            f.write(setting)
        return logg

    if language=="de":
        print(f"\nWillst du die sachen loggen?\n")
        setting=input("Ja oder Nein? ")
        setting.lower()
        logg=setting
        with open("logger.txt", "w") as save:
            save.write()
        return logg


def set_ad_setting(error_nofile, language):
    if error_nofile.lower()=="true":

        setting="yes"
        with open("ad setting.txt", "w")as f:
            f.write(setting)
        error_nofile = "false"
        return

    if language=="en":
        print(f"\nDo you want to see the ad?\n")
        setting=input("Yes or no? ")
        setting.lower()
        with open("ad setting.txt", "w") as f:
            f.write(setting)
        return

    if language=="de":
        print(f"\nWillst du die Werbung sehen?\n")
        setting=input("Ja oder Nein? ")
        setting.lower()
        with open("ad setting.txt", "w") as save:
            save.write()

def get_lang(language, change): #if language file is not there, this is the Function to get the language.
    get_language = loc.getdefaultlocale()[:1]
    system_language = str(get_language)
    if change=="true":
        if language=="en":
            language=input("What language of DE and EN? ")
            language.lower()
            with open("lang.txt", "w") as save:
                save.write(language)
            return language

        if language=="de":
            language=input("Was für eine sprache von DE und EN? ")
            language.lower()
            with open("lang.txt", "w") as save:
                save.write(language)
            return language

    else:

        if system_language == "('en_EN',)":
            language="en"
            with open("lang.txt", "w") as save:
                save.write(language)
            return language

        if system_language == "('de_DE',)":
            language="de"
            with open("lang.txt", "w") as save:
                save.write(language)
            return language

        if system_language == "('en_US',)":
            language="en"
            with open("lang.txt", "w") as save:
                save.write(language)
            return language

        else:
            print("An different language than yet supported language has been found. the Standard language is English.")
            language="en"
            with open("lang.txt", "w") as save:
                save.write(language)

            return language

def ad_makefile():
    ad="yes"
    open("ad settings.txt", "w")
    return

def settings_gui():
    #main function
    settings_window=Tk()
    settings_window.config(bg="#EFEFEF") 
    settings_window.title("Settings [W.I.P]")
    settings_window.geometry("400x200")
    settings_window.resizable(width=False, height=False)

    settings_window.mainloop()