#v2.1

#importing the Needed modules
import time as t
from datetime import datetime
import getpass, os, ctypes, socket
import random as ran
import webbrowser as web
#import locale as loc


logg="true" #if the errors should appear on an log file.
logg_makefile="true" #if an log file is wanted.

dl_link="https://github.com/Chaosminecraft/Text-converter/releases/"
ad="true"
upcheck="true"
conv="true"
prob="true"
time_read="true"
settingngs_ok="true"

def errors(reason, file):
    if reason=="recommended":
        print(f"THe file '{file}' is missing, it is recommended to download the source code if needed from:\n{dl_link}\n")
        return

    if reason=="critical":
        print(f"The file '{file}' is missing, Please download the whole source Code at:\n{dl_link}")
        return

#loading Custom modules
try:
    from logger import *
except:
    reason="critical"
    print(f"The file 'logger.py' is missing. Please download the whole source Code at: {dl_link}")
    input("press enter to exit.")
    exit()

log_init()

try:
    import requests
except:
    text="requests module is missing."
    log_error(text, logg)
    print(f"The module 'requests' is missing. Please install the module with:\npip install requests")
    input("press enter to exit.")
    exit()

try:
    from learn import *
except:
    text="learn.py is missing."
    log_error(text, logg)
    reason="recomended"
    file="learn.py"
    errors(reason, file)
    t.sleep(1)
    print(f"Great...\n")
    input("press enter to continue.")
    ad="false"
try:
    from updater import *
except:
    text="updater.py is missing."
    log_error(text, logg)
    reason="recommended"
    file="updater"
    errors(reason, file)
    input("press enter to continue.")
    upcheck="false"
try:
    from converter import *
except:
    text="converter.py is missing."
    log_error(text, logg)
    reason="recommended"
    file="converter.py"
    errors(reason, file)
    t.sleep(1)
    print("well, the project without the file is now just an Glorified time viewer :/")
    input("press enter to continue.")
    conv="false"
try:
    from problems import *
except:
    text="problems.py is missing"
    log_error(text, logg)
    reason="critical"
    file="problems.py"
    errors(reason, file)
    input("press enter to exit")
    exit()
try:
    from timeread import timereader
except:
    text="timeread.py is mising."
    log_error(text, logg)
    reason="recomended"
    file="timeread.py"
    errors(reason, file)
    input("press enter to continue")
    time_read="false"
try:
    from settings import *
except:
    text="settings.py is missing"
    log_error(text, logg)
    reason="recommended"
    file="settings.py"
    errors(reason, file)
    settings_ok="false"
    input("press enter to continue")

release="true"
error_nofile="false"
startup="false"
confirm="NULL"
language="en"
content="notext"
answer="notext"
system_language="notext"

mail="chaosminecraftmail@gmail.com"

old_link="https://drive.google.com/open?id=16AcLcgRRLlM7chKUi4eHgT-NOfBCnArM"
old_repo="https://github.com/Chaosminecraft/Custom-Encoder"

#the Main startpoint.
def start():
    while True:
        main()

def main():
    global error_nofile
    global language
    global logg
    while True:
        try:
            error_nofile = "logger"
            logg_file = open("logger.txt", "r")
            logg = logg_file.read()
            error_nofile = "false"

            language_file = open("lang.txt", "r")
            language = language_file.read()
            language_file.close()
            
            if language=="":
                print(f"There is an Problem with the language file: lang.txt")
                language="en"
                with open("lang.txt", "w") as save:
                    save.write(language)
            if startup=="false":
                if language.lower() == "de":

                    print(f"\nWillkommen zum Text Converter. Um die Hilfe seite zu sehen, Schreib 'help'\nEs gibt jetzt Mehrere wege Text zu convertieren.\n")

                    if ad=="true":
                        while_true_learn_ad(language, logg)
                    main_thread()
                    return

                if language.lower() == "en":

                    print(f"\nWelcome to my Text Converter. To get the helpsite, write 'help'\nThere are now multiple ways to convert text.\n")

                    if ad=="true":
                        while_true_learn_ad(language, logg)
                    main_thread()
                    return

        except FileNotFoundError:
            if error_nofile=="logger":
                logg_settings(error_nofile, language)
            else:
                text="Language file not found."
                log_warn(text, logg)
                get_lang()

def main_thread():
    global answer
    global language
    global startup
    startup="ok"
    if upcheck=="true":
        update(release)
    if upcheck=="false":
        print("Updade Checking failed, retry later again with: update")
    month="4"
    day="1"
    lol = datetime.now()
    if lol.day == day and now.month == month:
        if language=="en":
            print(f"An critical error happened, write 'Hello' to\n{mail}")
            input("press enter to continue.")
            web.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        if language=="de":
            print(f"Ein Kritischer fehler passierte, schreib 'Hallo' zu\n{mail}")
            input("Drück enter um weiterzukommen.")
            web.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    text="Startup Successful"
    log_info(text, logg)
    while True:
        try:
            try:
                try:
                    name = getpass.getuser()
                    host = socket.gethostname()
                    answer = input(f"{name}@{host}:~$ ")
                    text = answer
                    log_info(text, logg)

                    if answer.lower()=="phex" or answer.lower()=="thex" or answer.lower()=="pbin" or answer.lower()=="tbin":
                        if conv=="true":
                            converter(answer. language)
                        if conv=="false":
                            print(f"\nThe converter file can't yet be dynamically loaded yet :(")

                    if answer.lower()=="get game":
                        try:
                            get_game(language, logg)
                        except FileNotFoundError:
                            if language=="en":
                                print(f"\nlearn.py is missing. :(\n")
                            if language=="de":
                                print(f"\nlearn.py Wurde nicht gefunden.\n")
                            text="learn.py is missing."
                            log_error(text, logg)

                    if answer.lower()=="ad setting" or answer.lower()=="ad settings":
                        set_ad_setting(error_nofile, language)

                    if answer.lower()=="update":
                        if language=="en":
                            print(f"Here. ↓\n{dl_link}\nOlder releases: ↓\n\n{old_repo}\n{old_link}")
                        if language=="de":
                            print(f"Hier: ↓\n{dl_link}\nÄltere releases: ↓\n\n{old_repo}\n{old_link}")

                    if answer.lower()=="test":
                        if language=="en":
                            text="test success"
                            print(f"\nTest Successful\n")
                            log_info(text, logg)
                        if language=="de":
                            print(f"\nTest erfolgreich\n")
                            log_info(text, logg)

                    if answer.lower()=="reset":
                        startup="false"
                        os.system("cls")
                        return

                    if answer.lower()=="clear language":
                        os.remove("lang.txt")
                        text="Clearing language successfully done"
                        if system_language=="('en_EN',)":
                            print(f"\nLangeage file Deleted.\n")
                            log_info(text, logg)
                        if system_language=="('de_DE',)":
                            print(f"\nSprachdatei Gelöscht.")
                            log_info(text, logg)

                    if answer.lower()=="set language":
                        if language=="en":
                            get_lang()
                            print("\nHello, and welcome to my Custom Text converter.")
                            print("To get the ''helpsite'' you can write help.")
                            print(f"There are now multiple ways to Convert text.\n")
                        if language=="de":
                            get_lang()
                            print("\nWillkommen zu meinem Selbstgemachten text Converter.")
                            print("Um die ''Hilfeseite'' zu bekommen kann man Help schreiben.")
                            print("Jetzt gibt es Mehrere wege text zu convertieren.")

                    if answer.lower()=="check language":
                        try:
                            content=open("lang.txt", "r")
                            result=content.read()
                            if language != result:
                                if language == "en":
                                    print("something is weird with the 'lang.txt' file that had to be redone.")
                                if language == "de":
                                    print("etwas ist komisch mit der datei 'lang.txt', die musste neu gemacht werden.")
                                content.close()
                                get_lang()
                                content=open("lang.txt", "r")
                                result = content.read()
                                language = result
                                content.close()
                                
                            
                            content.close()
                            text=f"Current language: {result}"
                            log_info(text, logg)
                            print(result)
                        except FileNotFoundError:
                            if language=="en":
                                print("Try again.")
                                get_lang()
                            if language=="de":
                                print("Versuch es nochmal.")
                                get_lang()

                    if answer.lower()=="close test":
                        close()

                    if answer.lower() == 'help':#just a Boring o'l help command.
                        text="helpsite printed"
                        if language == "en":
                            print(f"\nHere is the Help site:\n")
                            print("The command phex Brings you to the Pseudo Hex converter.")
                            print("The command pbinary Brings you to the Pseudo Binary converter.")
                            print("The command thex Brings you to the Hex converter.")
                            print("The command tbin Brings you to the Binary Converter")
                            print("The command Clear Language deletes the file lang.txt")
                            print(f"The command Set Language Creates the lang.txt file and resetting the code to the system language if possible.")
                            print("The Command Check Language shows the current language in the lang.txt file.")
                            if ad=="true":
                                print("The Command Get Game makes the While True: Learn() game stores where you can buy the game.")
                            log_info(text, logg)
                        
                        if language == "de":
                            print(f"\nHier sind die komandos:\n")

                            print("Der Command phex Bringt dich zum Pseudo Hex converter.")
                            print("Der Command pbinary Bringt dich zum Pseudo Binary converter.")
                            print("Der Command thex Bringt dich zum Hex converter.")
                            print("Der Command tbin Bringt dich zum Binary converter")
                            print("Der Command Clear Language Löscht die Datei lang.txt")
                            print(f"Der Command Set Language Macht die Datei lang.txt und startet das Program neu in der Systemsprache wenn möglich.")
                            print("Der Commend Check Language zeigt die aktuelle sprache in der lang.txt datei.")
                            if ad=="true":
                                print(" Der Command Get Game zeigt dir was für stores für das Spiel while True: learn() kaufen kann.")
                            log_info(text, logg)

                    if answer.lower()=="email":
                        if language=="en":
                            print(f"\nHere: {mail}")
                        if language=="de":
                            print(f"\nHier: {mail}")

                    if answer.lower()=="time":
                        if time_read=="true":
                            timereader(language, logg)
                        if time_read=="false":
                            print("timeread.py is missing.")

                    if answer.lower()=="halt":
                        print("you're fast.")
                        t.sleep(0.8)
                        exit()

                    if answer.lower()=="exit":
                        close()

                    if answer=="":
                        notext(language)

                except FileNotFoundError:
                    print("An file is not found, that might be fixed in the future.")
            except KeyboardInterrupt:
                close()
        except ValueError:
            return

start()
