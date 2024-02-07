#the Links for the download of older/newer versions.


from datetime import datetime
import getpass, os, platform, socket, json, sys, traceback, webbrowser
from threading import Thread, Event

class setting:
    stop_event=Event()
    #determins if release or not and determins the version.
    release=True
    version="2.4"

    #Variables for the project
    language=""
    logg=True
    init=False
    check_init_time=True
    mail="chaosminecraftmail@gmail.com"
    name=getpass.getuser()
    host=socket.gethostname()
    upcheck=""
    prompt=""
    ad=""
    updatethread=""
    start=""
    end=""
    computed=""
    dl_link="https://github.com/Chaosminecraft/Text-converter/releases/"
    old_link="https://drive.google.com/open?id=16AcLcgRRLlM7chKUi4eHgT-NOfBCnArM"
    old_repo="https://github.com/Chaosminecraft/Custom-Encoder"

#importing all the stock modules and getting the start time
from time import sleep
setting.start=datetime.now()

#stop_event=Event()

#importing the rest of the modules that might not be installed.
try:
    import requests
except ImportError:
    os.system("pip install requests")
    try:
        import requests
    except ImportError:
        print("No update checking there :(")

#for some reason that logging function is needed...
def log_module_load(module):
    text=f"The module {module} has been loaded."
    log_system(text)
    return

def log_module_error(module):
    text=f"The module {module} couldn't be loaded, please check the file for corruptions."
    log_error(text, setting.logg)
    return

while True:
    try:
        module="logger"
        from logger import log_init, log_system, log_info, log_warn, log_error
        log_init(setting.logg)
        log_module_load(module)
        module="settings"
        from settings import settings_init, change_settings, helper
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

sys_=platform.system()
ver=platform.release()
cpu=platform.machine()
arc=platform.architecture()
system=f"{sys_} {ver}"

text=f"The platform uses: {sys_} {ver} {arc[0]} {cpu} {arc[1]}"
log_system(text)

if sys=="'Linux'":
    print("[WARNING] Linux Might not get Checked anymore. It might not run. Continue?")
    answer=input("Yes/No ").lower()
    if answer=="no":
        exit()
    else:
        pass

if sys_=="Darwin":
    print("That platform is not getting tested and from my variation is not designed to run there.")
    input("press enter to exit")
    exit()

#init function for startup
def main():
    while True:
        stop_event=Event()
        while True:
            try:
                try:
                    with open("settings.json", "r") as file:
                        settings=json.load(file)

                    setting.language=settings.get("lang")
                    setting.ad=settings.get("ad")
                    setting.prompt=settings.get("prompt")
                    setting.upcheck=settings.get("update")
                    setting.logg=settings.get("logging")
                    break
                except FileNotFoundError:
                    settings_init(setting.name, setting.host)
            except:
                traced=traceback.format_exc()
                text=f"There has been an Settings corruption. Please delete them and start the code again. Please send the traceback if you think there is more going on:\n{traced}"
                log_system(text)
                print(f"Please delete the settings file or restore it to the correct way. a fix is probably comming in some versions...\ni'd appreciate the log if you can send it to the GitHub page as a issue.\n should the site open?")
                openbrowser=input("Yes or No? ").lower()
                if openbrowser=="yes" or openbrowser=="ja":
                    webbrowser.open(setting.dl_link)
                exit()

        if setting.upcheck==True:
            setting.updatethread=Thread(target=update, args=(setting.release, setting.language, setting.version))
            setting.updatethread.start()
        if setting.ad==True:
            free_ad(setting.language, setting.logg, setting.ad)
        timethread=Thread(target=title_time, args=(stop_event, setting.language, sys_))
        timethread.start()

        if sys_=="'Linux'":
            print(f"It is known that the title has an update issue in Linux.")

        if setting.language == "de":
            print(f"\nWilkommen beim Text converter, wenn es das erste mal ist das du benutzt, es gibt den befehl: help")
        if setting.language == "en":
            print(f"\nWelcome at the text converter, if that is the first time that you use it, there is the command: help")
        while True:
            if setting.init=="true":
                while True:
                    try:
                        with open("settings.json", "r") as file: 
                            settings=json.load(file)

                        setting.language=settings.get("lang")
                        setting.ad=settings.get("ad")
                        setting.prompt=settings.get("prompt")
                        setting.upcheck=settings.get("update")
                        setting.logg=settings.get("logging")
                        break
                    except FileNotFoundError:
                        settings_init(setting.name, setting.host)
            textconverter(setting.language, setting.prompt, setting.upcheck, setting.logg, setting.ad)

def textconverter(language, prompt, upcheck, logg, ad):
    try:
        try:
            
            if upcheck==True:
                if setting.init==False:
                    setting.updatethread.join()

            if setting.check_init_time==True:
                setting.end=datetime.now()
                setting.computed=setting.end-setting.start
                print(setting.computed)
                if setting.init==False:
                    print(f"Startup needed that long to start: {setting.computed}\n")
                text=f"The program started successfully in {setting.computed} seconds."
                log_system(text)
                setting.check_init_time=False

            while True:

                setting.init=True
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
                    convert(comand, language, logg, setting.name)

                if comand=="help":
                    helper(language, logg)
                
                if comand=="get game":
                    get_game(language, logg)
                
                if comand=="ad settings":
                    change_settings(language, setting.name, setting.host, system, setting="ad")#
                
                if comand=="ad":
                    print(f"the advertisement is set to: {ad}")
                
                if comand=="logg settings":
                    logg=change_settings(language, setting.name, setting.host, system, setting="logging")
                
                if comand=="logg":
                    print(f"The logging is set to: {logg}")
                
                if comand=="prompt settings":
                    if language=="en":
                        print("""Warning: That feauture is experimental! Continue with caution.
    The options are {system} and {name} and {host}, The rest can be however you want.
    
    IF the program crashes, Please tell me on GitHub or Email! The email adress can be found in the "Contact if crash.txt".
                    """)
                    if language=="de":
                        print("""Warnung: Dieses feature ist expertimental! Fahre fort mit vorsicht.
    Die optionen sind {system} und {name} und {host}, Der rest kann alles sein. 
    
    Wenn das programm crasht, Bitte sag es mir bei GitHub oder Email! Die email adresse kann im "Contact if crash.txt" gefunden werden.
                    """)
                    prompt=change_settings(language, setting.name, setting.host, system, setting="promptinput")
                    return

                if comand=="prompt":
                    print(f"\n{prompt}\n")
                
                if comand=="language settings":
                    language=change_settings(language, setting.name, setting.host, system, setting="language")
                    return
                
                if comand=="language":
                    print(language)

                if comand=="update settings":
                    upcheck=change_settings(language, setting.name, setting.host, system, setting="update")
                
                if comand=="update":
                    update(setting.release, language, setting.version)
                
                if comand=="reset settings" or comand=="new settingsfile":
                    if language=="en":
                        print(f"\nAre you sure you want to wipe the Settings to the default?")
                        answer=input("Yes/No ").lower()
                        if answer=="yes" or answer=="ja":
                            settings_init(vars.name, vars.host)

                    if language=="de":
                        print(f"\nBist du dir sicher das du die einstellungen zurücksetzen willst?")
                        answer=input("Ja/Nein").lower()
                        if answer=="yes" or answer=="ja":
                            settings_init(vars.name, vars.host)

                if comand=="delete settings":
                    try:
                        os.remove("settings.json")

                    except FileNotFoundError:
                        print(f"\nNo settings file there... i'd advice that you make one.\n")

                if comand=="clear screen":
                    if sys_=="Windows":
                        os.system("cls")
                    if sys_=="Linux":
                        os.system("clear")
                
                if comand=="reset":
                    return
                
                if comand=="halt" or comand=="scrum":
                    setting.stop_event.set()
                    exit()
                
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
            setting.stop_event.set()
            exit()
    except KeyboardInterrupt:
        close(language, sys_)

def close(language, sys_):
    
    if sys_.lower()=="windows":
        os.system("cls")

    if sys_.lower()=="linux":
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
        
        setting.stop_event.set()
        sleep(4)
        if sys_.lower()=="windows":
            os.system("cls")

        elif sys_.lower()=="linux":
            os.system("clear")
        exit()

main()