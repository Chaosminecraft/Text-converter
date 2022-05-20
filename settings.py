import locale as loc

def logg_settings(error_nofile, language):
    if error_nofile.lower()=="true":

        setting="true"
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

def get_lang(): #if language file is not there, this is the Function to get the language.
    get_language = loc.getdefaultlocale()[:1]
    system_language = str(get_language)
    if system_language == "('en_EN',)":
        language="en"
        with open("lang.txt", "w") as save:
            save.write(language)
        return
    if system_language == "('de_DE',)":
        language="de"
        with open("lang.txt", "w") as save:
            save.write(language)
        return language, system_language
    else:
        print("An different OS then Windows has been detected. some things may not work.")
        print("The Available Languags are there: de and en")
        lang_answ = input("what language? ")
        lang_answ.lower()
        with open("lang.txt", "w") as save:
            save.write()
        language = lang_answ
        return language
