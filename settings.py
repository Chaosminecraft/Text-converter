import locale as loc
from logger import *


def logg_settings(init, language):
    if init=="true":
        setting="true"
        with open("logg.txt", "w") as save:
            save.write(setting)
        return
    
    if language=="de":
        while True:
            print(f"\nWillst du die sachen loggen?\n")
            setting=input("Ja oder Nein? ")
            if setting.lower()=="ja":
                choice="true"
                with open("logg.txt", "w") as save:
                    save.write(choice)
                return
            if setting.lower()=="nein":
                choice="false"
                with open("logg.txt", "w") as save:
                    save.write(choice)
                return
            else:
                print(f"\nVersuch nochmal!\n")
    
    if language=="en":
        while True:
            print(f"\nDo you want to log the Stuff? \n")
            setting=input("Yes or No? ")
            if setting.lower()=="yes":
                choice="true"
                with open("logg.txt", "w") as save:
                    save.write(choice)
                return
            if setting.lower()=="no":
                choice="false"
                with open("logg.txt", "w") as save:
                    save.write(choice)
                return
            else:
                print(f"\nTry again!\n")

def get_lang(language, change, init):
    get_language = loc.getdefaultlocale()[:1]
    system_language = str(get_language)
    if init=="false":
        if system_language=="('en_EN',)" or system_language=="('de_DE',)":
            if system_language=="('de_DE',)":
                language="en"
                with open("lang.txt", "w") as  save:
                    save.write(language)
            if system_language=="('de_DE',)":
                language="de"
                with open("lang.txt", "w") as save:
                    save.write(language)
            return

        else:
            language="en"
            with open("lang.txt", "w") as save:
                save.write(language)
            return
    
    if change=="true":
        if language == "en":
            print(f"\nThere are English and German and are the official languages.\n")
            language=input("What do you take? English or German: ")
            if language.lower()=="german" or language.lower()=="deutsch":
                language="de"
            if language.lower()=="englisch" or language.lower()=="english":
                language="en"
            language.lower()
            with open("lang.txt", "w") as save:
                save.write(language)
            return language
        
        if language=="de":
            print(f"\nDa ist Deutsch und Englisch die offiziellen sprachen.")
            language=input("Was nimmst du? Deutsch oder Englisch: ")
            if language.lower()=="deutsch" or language.lower() == "german":
                language="de"
            if language.lower()=="englisch" or language.lower() == "english":
                language="en"
            language.lower()
            with open("lang.txt", "w") as save:
                save.write(language)
            return language

def ad_makefile(logg):
    ad="true"
    with open("ad setting.txt", "w") as save:
        save.write(ad)
    text="settings file made."
    log_info(text, logg)
    
    return

def ad_settings(language, logg):
    while True:
        if language=="de":
            ad=input("Willst du die Werbung sehen? ")
            if ad=="ja":
                ad_var="true"
                text="Werbung Aktiviert"

            if ad=="nein":
                ad_var="false"
                text="Werbung deaktiviert"
            
            log_info(text, logg)
            
            with open("ad setting.txt", "w") as save:
                save.write(ad_var)
            return

        if language=="en":
            ad=input("Do you wanna see the advertisement? ")
            if ad=="yes":
                ad_var="true"

            if ad=="no":
                ad_var="false"

            with open("ad setting.txt", "w") as save:
                save.write(ad_var)
            return

def helper(language, logg):
    try:
        ad=open("ad setting.txt", ).read()
    except FileNotFoundError:
        ad_makefile(logg)
        ad=open("ad setting.txt", ).read()
    text="helpsite printed"
    if language == "en":
        print(f"\nThere are the Conversion methods:\n")
        print("The command phex Brings you to the Pseudo Hex converter.")
        print("The command pbin Brings you to the Pseudo Binary converter.")
        print("The connamd legacy pbin Brings you to the Legacy version of the Pseudo Binary converter")
        print("The command hex Brings you to the Hex converter.")
        print("The command bin Brings you to the Binary Converter.")
        print("The command ascii Brings you to the ascii converter.")
        print("The command leetcode brings you to the leetcode converter.")
        print("The command brainfuck Brings you to the Brainfuck converter.")
        print("The command base64 Brings you to the base64 converter.")
        print(f"\nThere are more General commands:\n")
        print("The command ad setting asks if you want to see the ad.")
        print("The command clear screen means that no text from earlier is shown.")
        print("The command Clear Language deletes the file lang.txt")
        print("The command Set Language Creates the lang.txt file and resetting the code to the system language if possible.")
        print("The command reset restarts the program.")
        print("The Command Check Language shows the current language in the lang.txt file.")
        if ad=="true":
            print("The Command Get Game makes the While True: Learn() game stores where you can buy the game.")
        print()
        log_info(text, logg)
                        
    if language == "de":
        print(f"\nDa sind die Converter Methoden:\n")
        print("Der Command phex Bringt dich zum Pseudo Hex converter.")
        print("Der Command pbinary Bringt dich zum Pseudo Binary converter.")
        print("Der Command thex Bringt dich zum Hex converter.")
        print("Der Command tbin Bringt dich zum Binary converter")
        print("Der command ascii Bringt you to the ascii converter.")
        print("Der command leetcode bringt you to the leetcode converter.")
        print("Der command brainfuck Bringt you to the Brainfuck converter.")
        print("Der command base64 Bringt you to the base64 converter.")
        print(f"\nDa sind mehr Generelle Commands:\n")
        print("Der command help Zeigt das hier.")
        print("Der command ad setting fragt ob du die werbung sehen willst.")
        print("Der command clear screen macht das kein text mer von vorhin gezeigt wird.")
        print("Der Command Clear Language Löscht die Datei lang.txt")
        print("Der Command Set Language Macht die Datei lang.txt und startet das Program neu in der Systemsprache wenn möglich.")
        print("Der command reset startet das Program neu.")
        print("Der Commend Check Language zeigt die aktuelle sprache in der lang.txt datei.")
        if ad=="true":
            print("Der Command Get Game zeigt dir was für stores für das Spiel while True: learn() kaufen kann.")
        print()
        log_info(text, logg)
    
    return
