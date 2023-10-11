#the Links for the download of older/newer versions.
dl_link="https://github.com/Chaosminecraft/Text-converter/releases/"
old_link="https://drive.google.com/open?id=16AcLcgRRLlM7chKUi4eHgT-NOfBCnArM"
old_repo="https://github.com/Chaosminecraft/Custom-Encoder"

#importing all the stock modules and getting the start time
from datetime import datetime
from time import sleep
start=datetime.now()
import getpass, os, platform, socket, json
from threading import Thread, Event

#importing the rest of the modules that might not be installed.
try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests

#determins if release or not and determins the version.
release=True
rversion="2.4"
bversion="2.3"

#Variables for the project
logg=True
init="false"
check_init_time=True
updatethread=""
mail="chaosminecraftmail@gmail.com"
stop_event=Event()

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

text=f"The platform uses: {sys} {ver} {arc[0]} {cpu} {arc[1]}
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

#loading settings
def settingsload():
    while True:
        try:
            with open("settings.json", "r") as file:
                settings=json.load(file)

            language=settings.get("langauge")
            ad=settings.get("ad")
            prompt=settings.get("prompt")
            upcheck=settings.get("update")
            logg=settings.get("logging")
            break
        except FileNotFoundError:
            try:
                print("Would you like to keep your current configuration?")
                answer=input("Yes or No? ").lower()

                if answer=="yes" or answer=="ja":
                    migrate_settings()
                    try:
                        os.remove("ad settings.txt")
                        os.remove("lang.txt")
                        os.remove("logg.txt")
                        os.remove("platform.txt")
                        os.remove("system.txt")
                    except FileNotFoundError:
                        pass

                if answer=="no" or answer=="nein":
                    try:
                        os.remove("ad settings.txt")
                        os.remove("lang.txt")
                        os.remove("logg.txt")
                        os.remove("platform.txt")
                        os.remove("system.txt")
                    except FileNotFoundError:
                        pass
                    settings_init()
            except:
                print("I'm sorry, but something went wrong while trying to get the settings... The old settings are still there.")
                settings_init
    return language, ad, prompt, upcheck, logg

#init function for startup
def main():
    global updatethread
    global stop_event
    while True:
        stop_event=Event()
        language, ad, prompt, upcheck, logg=settingsload()
        if release==True:
            version=rversion
        elif release==False:
            version=bversion
        if upcheck==True:
            updatethread=Thread(target=update, args=(release, language, version))
            updatethread.start()
        if ad==True:
            free_ad(language, logg)
        timethread=Thread(target=title_time, args=(stop_event, language, sys))
        timethread.start()

        if sys=="'Linux'":
            print(f"It is known that the title has an update issue in Linux.")
        
        if language == "de":
            print(f"\nWilkommen beim Text converter, wenn es das erste mal ist das du benutzt, es gibt den befehl: help")
        if language == "en":
            print(f"\nWelcome at the text converter, if that is the first time that you use it, there is the command: help")
        
        TextConverter(language, prompt, upcheck, logg)

def TextConverter(language, prompt, upcheck, logg):
    global init
    global check_init_time
    global stop_event
    try:
        try:
            text="The program started successfully"
            log_system(text)
            while True:
                name=getpass.getuser()
                host=socket.gethostname()
                init="true"
                if upcheck==True:
                    updatethread.join()
                if check_init_time==True:
                    end=datetime.now()
                    computed=end-start
                    print(f"Startup needed that long to start: {computed}")
                    check_init_time=False


                comand=input(prompt).lower()

                text=f"the user used: {comand}"
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
                    ad=change_settings(language, setting="ad")
                
                if comand=="logg settings":
                    logg=change_settings(language, setting="logging")
                
                if comand=="prompt settings":
                    print("Warning: That feauture is experimental! Continue with caution.")
                    logg=change_settings(language, setting="prompt")
                
                if comand=="language settings":
                    language=change_settings(language, settings="language")

                if comand=="update settings":
                    upcheck=change_settings(language, setting="update")
                
                if comand=="reset settings" or comand=="new settingsfile":
                    if language=="en":
                        print(f"\nAre you sure you want to wipe the Settings to the default?")
                        answer=input("Yes/No ").lower()
                        if answer=="yes" or answer=="ja":
                            settings_init()

                    if language=="de":
                        print(f"\nBist du dir sicher das du die einstellungen zurücksetzen willst?")
                        answer=input("Ja/Nein").lower()
                        if answer=="yes" or answer=="ja":
                            settings_init()

                if comand=="clear screen":
                    if sys=="Windows":
                        os.system("cls")
                    if sys=="Linux":
                        os.system("clear")
                
                if comand=="exit":
                    close(language)
        except TypeError:
            if language=="en":
                print(f"\nThere has been an unexpected Error. That is gonna get fixed soon.\n")
            if language=="de":
                print(f"\nDas war ein unerwarteter Fehler. Dieser ist bald repariert.\n")
            sleep(5)
            stop_event.set()
            exit()
    except KeyboardInterrupt:
        close(language)

def close(language):
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