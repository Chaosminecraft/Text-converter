#the Links for the download of older/newer versions.
dl_link="https://github.com/Chaosminecraft/Text-converter/releases/"
old_link="https://drive.google.com/open?id=16AcLcgRRLlM7chKUi4eHgT-NOfBCnArM"
old_repo="https://github.com/Chaosminecraft/Custom-Encoder"

#importing all the stock modules and getting the start time
from datetime import datetime
from time import sleep
start=datetime.now()
import getpass, os, platform, socket, json, sys, traceback
from threading import Thread, Event

#importing the rest of the modules that might not be installed.
try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests

#determins if release or not and determins the version.
release=True
version="2.4"

#Variables for the project
logg=True
init="false"
check_init_time=True
updatethread=""
mail="chaosminecraftmail@gmail.com"
stop_event=Event()
name=getpass.getuser()
host=socket.gethostname()

#for some reason that logging function is needed...
def log_module_load(module):
    text=f"The module {module} has been loaded."
    log_system(text)
    return

def log_module_error(module):
    text=f"The module {module} couldn't be loaded, please check the file for corruptions."
    log_error(text, logg)
    return

while True:
    try:
        module="logger"
        from logger import log_init, log_system, log_info, log_warn, log_error
        log_init(logg)
        log_module_load(module)
        module="settings"
        from settings import migrate_settings, settings_init, change_settings, helper
        log_module_load(module)
        module="learn"
        from learn import free_ad, get_game
        log_module_load(module)
        module="updater"
        from updater import update
        log_module_load(module)
        module="converter"
        from converter import convert
        log_module_load(module)
        module="timeread"
        from timeread import timereader, title_time
        log_module_load(module)
        break
    except ImportError:
        input("There is no solution for missing Modules at the moment...")

sys=platform.system()
ver=platform.release()
cpu=platform.machine()
arc=platform.architecture()
system=f"{sys} {ver}"

text=f"The platform uses: {sys} {ver} {arc[0]} {cpu} {arc[1]}"
log_system(text)

if sys=="'Linux'":
    print("[WARNING] Linux Might not get Checked anymore. It might not run. Continue?")
    answer=input("Yes/No ").lower()
    if answer=="no":
        exit()
    else:
        pass

if sys=="Darwin":
    print("That platform is not getting tested and from my variation is not designed to run there.")
    input("press enter to exit")
    exit()

#init function for startup
def main():
    global updatethread
    global stop_event
    global init
    while True:
        stop_event=Event()
        while True:
            try:
                with open("settings.json", "r") as file:
                    settings=json.load(file)

                language=settings.get("lang")
                ad=settings.get("ad")
                prompt=settings.get("prompt")
                upcheck=settings.get("update")
                logg=settings.get("logging")
                break
            except FileNotFoundError:
                settings_init(name, host)
        if upcheck==True:
            updatethread=Thread(target=update, args=(release, language, version))
            updatethread.start()
        if ad==True:
            free_ad(language, logg, ad)
        timethread=Thread(target=title_time, args=(stop_event, language, sys))
        timethread.start()

        if sys=="'Linux'":
            print(f"It is known that the title has an update issue in Linux.")

        if language == "de":
            print(f"\nWilkommen beim Text converter, wenn es das erste mal ist das du benutzt, es gibt den befehl: help")
        if language == "en":
            print(f"\nWelcome at the text converter, if that is the first time that you use it, there is the command: help")
        while True:
            if init=="true":
                while True:
                    try:
                        with open("settings.json", "r") as file: 
                            settings=json.load(file)

                        language=settings.get("lang")
                        ad=settings.get("ad")
                        prompt=settings.get("prompt")
                        upcheck=settings.get("update")
                        logg=settings.get("logging")
                        break
                    except FileNotFoundError:
                        settings_init(name, host)
            TextConverter(language, prompt, upcheck, logg, ad)

def TextConverter(language, prompt, upcheck, logg, ad):
    global init
    global check_init_time
    global stop_event
    try:
        try:
            
            if upcheck==True:
                if init=="false":
                    updatethread.join()

            if check_init_time==True:
                end=datetime.now()
                computed=end-start
                print(f"Startup needed that long to start: {computed}\n")
                check_init_time=False

            if init=="false":
                text=f"The program started successfully in {computed} seconds."
                log_system(text)

            while True:

                init="true"
                comand=input(prompt).lower()

                text=f"the user entered: {comand}"
                log_info(text, logg)

                if comand=="test":
                    print(f"\nOK")

                if comand=="leetspeak" or comand=="leetcode":
                    if language=="en":
                        print(f"\nThat feature is Permanently removed.\n")
                    if language=="de":
                        print(f"Dieses feature ist Permanent entfenrt.\n")
                    return

                if comand=="phex" or comand.lower()=="pbin" or comand.lower()=="legacy pbin" or comand.lower()=="hex" or comand.lower()=="bin" or comand.lower()=="ascii" or comand.lower()=="brainfuck" or comand.lower()=="base64":
                    convert(comand, language, logg, name)

                if comand=="help":
                    helper(language, logg)
                
                if comand=="get game":
                    get_game(language, logg)
                
                if comand=="ad settings":
                    change_settings(language, name, host, system, setting="ad")#
                
                if comand=="ad":
                    print(f"the advertisement is set to: {ad}")
                
                if comand=="logg settings":
                    logg=change_settings(language, name, host, system, setting="logging")
                
                if comand=="logg":
                    print(f"The logging is set to: {logg}")
                
                if comand=="prompt settings":
                    if language=="en":
                        print("""Warning: That feauture is experimental! Continue with caution.
    The options are {system} and {name} and {host}, The rest can be however you want. IF the program crashes, Please tell me on GiHub or Email! The email adress can be found in the "Contact if crash.txt".
                    """)
                    if language=="de":
                        print("""Warnung: Dieses feature ist expertimental! Fahre fort mit vorsicht.
    Die optionen sind {system} und {name} und {host}, Der rest kann alles sein. Wenn das programm crasht, Bitte sag es mir bei GitHub oder Email! Die email adresse kann im "Contact if crash.txt" gefunden werden.
                    """)
                    prompt=change_settings(language, name, host, system, setting="promptinput")
                    return

                if comand=="prompt":
                    print(f"\n{prompt}\n")
                
                if comand=="language settings":
                    language=change_settings(language, name, host, system, setting="language")
                
                if comand=="language":
                    print(language)

                if comand=="update settings":
                    upcheck=change_settings(language, name, host, system, setting="update")
                
                if comand=="update":
                    update(release, language, version)
                
                if comand=="reset settings" or comand=="new settingsfile":
                    if language=="en":
                        print(f"\nAre you sure you want to wipe the Settings to the default?")
                        answer=input("Yes/No ").lower()
                        if answer=="yes" or answer=="ja":
                            settings_init(name, host)

                    if language=="de":
                        print(f"\nBist du dir sicher das du die einstellungen zurücksetzen willst?")
                        answer=input("Ja/Nein").lower()
                        if answer=="yes" or answer=="ja":
                            settings_init(name, host)

                if comand=="delete settings":
                    try:
                        os.remove("settings.json")

                    except FileNotFoundError:
                        print(f"\nNo settings file there... i'd advice that you make one.\n")

                if comand=="clear screen":
                    if sys=="Windows":
                        os.system("cls")
                    if sys=="Linux":
                        os.system("clear")
                
                if comand=="reset":
                    return
                
                if comand=="exit":
                    close(language)
        except TypeError:
            traced=traceback.format_exc()
            if language=="en":
                print(f"\nThere has been an unexpected Error. That is gonna get fixed soon.\n")
            if language=="de":
                print(f"\nDas war ein unerwarteter Fehler. Dieser ist bald repariert.\n")
            text=f"There has been an unexpected error, there is an traceback:\n{traced}"
            log_system(text)
            sleep(5)
            stop_event.set()
            exit()
    except KeyboardInterrupt:
        close(language, sys)

def close(language, sys):
    global count
    
    if sys.lower()=="windows":
        os.system("cls")

    if sys.lower()=="linux":
        os.system("clear")
    while True:
        if language=="en":
            answer=input("Do you wanna close that program? ")
            if answer.lower()=="no" or answer.lower()=="false":
                return

        if language=="de":
            answer=input("Willst du das Program schliesen? ")
            if answer.lower()=="nein" or answer.lower()=="false":
                return
        
        stop_event.set()
        sleep(4)
        if sys.lower()=="windows":
            os.system("cls")

        elif sys.lower()=="linux":
            os.system("clear")
        exit()

main()