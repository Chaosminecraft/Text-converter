#importing required "libraries" adn getting the beginning of the startup time
import getpass, os, platform, socket, json, traceback, webbrowser
from threading import Thread, Event
from time import sleep

class setting:
    #if the version is a release or Dev version
    release=True
    version="2.7"
    beta_version="2.7"

    #variables needed for propper execution
    language=""
    upcheck=True
    prompt=""
    ad=""
    logg=True
    init=False
    check_init_time=True
    start=""
    start_time=""

    #Email adress if GitHub is not a option
    mail="chaosminecraftmail@gmail.com"

    #the user name and system name
    name=getpass.getuser()
    host=socket.gethostname()

    #the links to all the versions from the project
    dl_link="https://github.com/Chaosminecraft/Text-converter/releases/"
    beta_channel="https://github.com/Chaosminecraft/Text-Converter-Beta/"
    old_link="https://drive.google.com/open?id=16AcLcgRRLlM7chKUi4eHgT-NOfBCnArM"
    old_repo="https://github.com/Chaosminecraft/Custom-Encoder"

class converterdata:
    out=""
    
from datetime import datetime
setting.start=datetime.now()

try:
    import requests
except ImportError:
    print("Please install requests for update checking")
    setting.upcheck=False

#importing custom "modules" that may need the setting class
from logger import log_init, log_system, log_info, log_warn, log_error
log_init(setting.logg)
from settings import settings_init, change_settings
from timeread import timereader, title_time
from converter import convert
from helpfunctions import mainhelp
from advert import free_ad, get_game

#The update checking function
def updatecheck():
    #print("FUNCTION START") #For checking if the function starts at all
    if setting.release==True:
        #print("RELEASE VERSION") #says if it is a Release version.
        link_ver="https://github.com/Chaosminecraft/Text-converter/raw/main/version.txt"
        checked_version=requests.get(link_ver, allow_redirects=True)
        checked_version=str(checked_version.content)[2:5]
        #print(checked_version) #If the version from the internet doesn't give good results.
        
        if checked_version>setting.version:
            if setting.language=="en":
                print(f"There is a new version: {checked_version}\nThere is the download link:↓{setting.dl_link}\n")
            elif setting.language=="de":
                print(f"Da ist eine neue version: {checked_version}\nDa ist der download link:↓{setting.dl_link}\n")
            else:
                print(f"There is a new version: {checked_version}\nThere is the download link:↓{setting.dl_link}\n")
            return
        
        elif checked_version==setting.version:
            if setting.language == "en":
                print(f"\nThe version {setting.version} is the latest version at the moment.\n")
            elif setting.language == "de":
                    print(f"\nDie version {setting.version} ist die neuste im moment.\n")
            else:
                print(f"\nThe version {setting.version} is the latest version at the moment.\n")
            return
        
        elif checked_version<setting.version:
            if setting.language=="en":
                print(f"No need to be ashamed to be a dev \n")
            elif setting.language=="de":
                print(f"Man muss sich nicht schämen, ein Entwickler zu sein \n")
            else:
                print(f"No need to be ashamed to be a dev \n")
            return
        
        else:
            if setting.language=="en":
                print(f"An unknown version was found. :(\n")
            elif setting.language=="de":
                print(f"Eine unbekannte version wurde gefunden. :(\n")
            else:
                print(f"An unknown version was found. :(\n")
            return
    
    elif setting.release==False:
        #print("BETA RELEASE") Says if it is a Beta version.
        link_ver="https://github.com/Chaosminecraft/Text-converter/raw/Beta/betaversion.txt"
        checked_version=requests.get(link_ver, allow_redirects=True, timeout=10)
        checked_version=str(checked_version.content)[2:5]
        #print(checked_version) #If the version from the internet doesn't give good results.

        if checked_version>setting.beta_version:
            if setting.language=="en":
                print(f"There is a new beta version, Download it here: {checked_version}\nThere is the download link: {setting.beta_channel}\n")
            elif setting.language=="de":
                print(f"Da ist eine neue beta version: {checked_version}\nDa ist der Download link: {setting.beta_channel}\n")
            else:
                print(f"There is a new beta version, Download it here: {checked_version}\nThere is the download link: {setting.beta_channel}\n")
            return
        
        elif checked_version==setting.beta_version:
            if setting.language=="en":
                print(f"The beta verision {setting.beta_version} is the latest version right now.\n")
            elif setting.language=="de":
                print(f"Die version {setting.beta_version} ist die neuste Beta version.\n")
            else:
                print(f"The beta verision {setting.beta_version} is the latest version right now.\n")
            return
        
        elif checked_version<setting.beta_version:
            if setting.language=="en":
                print(f"Hello fellow coder :)\n")
            elif setting.language=="de":
                print(f"Hallo Mitprogrammierer :)")
            else:
                print(f"Hello fellow coder :)\n")
            return
        
        else:
            if setting.language=="en":
                print(f"An unknown beta version was found :(\n")
            elif setting.language=="de":
                print(f"Eine unbekannte beta version wurde gefunden :(\n")
            else:
                print(f"An unknown beta version was found :(\n")
            return

class SysInf:
    system=platform.system()
    version=platform.release()
    detail_version=platform.version()
    cpu_architecture=platform.machine()
    complete_system=f"{system} {version}"

class threads:
    updatethread=Thread(target=updatecheck)
    stop_event=Event()
    titletime=Thread(target=title_time, args=(setting.language, SysInf.system, stop_event, ))

text=f"The platform uses: \n                {SysInf.complete_system} build {SysInf.detail_version}\n                With the architecture: {SysInf.cpu_architecture}\n"
log_system(text)

if SysInf.system=="'Linux'":
    print("[WARNING] Linux may not work on all versions...")

if SysInf.system=="'Darwin'":
    print(f"[WARNING] MacOS and other Darwin based systems can't be tested, it may not work!\n")

def init():
    while True:
        try:
            while True:
                try:
                    with open("settings.json", "r") as file:
                        settings=json.load(file)

                    setting.language=settings.get("language")
                    setting.ad=settings.get("ad")
                    setting.prompt=settings.get("prompt")
                    setting.upcheck=settings.get("update")
                    setting.logg=settings.get("logging")
                    break
                except FileNotFoundError:
                    settings_init(setting.name, setting.host)
        except:
            traced=traceback.format_exc()
            text=f"There has been a settings Specific settings error that is currently unable to be fixed. Please manually repair the settings file if possible. THere is more information about the crash:\n{traced}"
            print(text)
            log_system(text)
            print(f"\nThere is the option to report it to the GitHub page as an problem, Do you wanna open the site?")
            if input("Yes or No? ").lower() == "yes":
                webbrowser.open(setting.dl_link)

            setting.language="en"
            setting.ad=False
            setting.prompt="PC@NAME:~$ "
            setting.upcheck=False
            setting.logg=True

            print(f"A temporare workaround has been put in until the solution is there.\n")

            if setting.ad==True:
                free_ad(setting.language, setting.logg, setting.ad)

        if setting.init==False:
            threads.titletime.start()

        if setting.init==False:
            if setting.upcheck==True:
                threads.updatethread.start()
        
        if SysInf.system=="Linux":
            print("I'm aware that the title doesn't update on Linux...")
            threads.stop_event.set()
        
        if setting.language=="en":
            print(f"Welcome to the currently Beta version of Text Converter. Please complain on the Beta GitHub Site about issues. it is at {setting.beta_channel}")

        main()

def main():
    try:
        try:
            try:
                if setting.upcheck==True:
                    if setting.init==False:
                        threads.updatethread.join()
                
                if setting.check_init_time==True:
                    setting.start_time=datetime.now()-setting.start
                    if setting.init==False:
                        if setting.language=="en":
                            print(f"Startup needed {setting.start_time} seconds.")
                        elif setting.language=="de":
                            print(f"Start brauchte {setting.start_time} Sekunden.")
                    text=f"The program started in {setting.start_time} seconds."
                    log_system(text)
                
                while True:
                    setting.init=True
                    command=input(setting.prompt).lower()
                    if command=="":
                        text="No input detected."
                    else:
                        text=f"The user used: {command}"
                    log_info(text, setting.logg)

                    if command=="test":
                        print("SUCCESS :P")

                    elif command=="leetspeak" or command=="leetcode":
                        if setting.language=="en":
                            print(f"\nThat feature is permanently Removed.\n")
                    
                    elif command=="phex" or command=="pbin" or command=="legacy pbin" or command=="hex" or command=="bin" or command=="ascii" or command=="brainfuck" or command=="base64" or command=="symbenc":
                        converterdata.out=convert(command, setting.language, setting.logg, setting.name)
                    
                    elif command=="last conversion":
                        print(converterdata.out)
                    
                    elif command=="help" or command=="helpsite":
                        mainhelp(command, setting.language)
                    
                    elif command=="language":
                        change_settings(settings="lang", prom=setting.prompt, language=setting.language, logging=setting.logg)
                        return
                    
                    elif command=="prompt":
                        change_settings(settings="prompt", prom=setting.prompt, language=setting.language, logging=setting.logg, pc=setting.host, name=setting.name, version=SysInf.version, system=SysInf.system)
                        return
                    
                    elif command=="ad":
                        change_settings(settings="ad", prom=setting.prompt, language=setting.language, logging=setting.logg)
                        return
                    
                    elif command=="check update":
                        updatecheck()
                    
                    elif command=="reset":
                        setting.init=False
                        setting.start_time=""
                        threads.stop_event.set()
                        return

                    elif command=="exit" or command=="close" or command=="stop":
                        close()
                    
                    elif command=="halt" or command=="stop, you violated the law":
                        threads.stop_event.set()
                        exit()
                    
                    elif command=="titletimestop":
                        threads.stop_event.set()
                    
                    elif command=="titletimestart":
                        threads.stop_event=Event()
                        threads.titletime=Thread(target=title_time, args=(setting.language, SysInf.system, threads.stop_event, ))
                        threads.titletime.start()
                    
                    elif command=="":
                        if setting.language=="en":
                            print(f"I'm sorry, i can't parse nothing :(")
                        
                        elif setting.language=="de":
                            print(f"Es tut mir leid, ich kann nicht nicths parsen. :(")
                        
                        else:
                            print(f"I'm sorry, i can't parse nothing :(")
                    
                    else:
                        text=f"The user used an unknown command: {command}"
                        if setting.language=="en":
                            print(f"The command '{command}' was not found :(")
                        elif setting.language=="de":
                            print(f"Der command '{command}' wurde nicht gefunden :(")
                        else:
                            print(f"The command '{command}' was not found :(")

            except AttributeError:
                pass
        
        except TypeError:
            traced=traceback.format_exc()
            if setting.language=="en":
                print("\nAn unexpected error occured...\n")
            
            text=f"There was an type error somehow. that is the traceback:\n{traced}"
            log_system(text)
            threads.titletime.terminate()
            sleep(5)
            exit()
    except KeyboardInterrupt:
        close()

def close():
    if setting.language=="en":
        os.system("cls")
        print(f"\nDo you wanna clsoe the PRogram?\n")
        if input("Yes/No: ").lower()=="yes":
            threads.stop_event.set()
            exit()
        else:
            return
    if setting.language=="de":
        os.system("cls")
        print(f"Willst du das Program beenden?\n")
        if input("Ja/Nein: ").lower()=="ja":
            threads.stop_event.set()
            exit()
        else:
            return
    return

if __name__=="__main__":
    init()