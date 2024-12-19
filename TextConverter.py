#That is the portion that get's the Normal modules
import getpass, os, platform, socket, json, traceback, webbrowser
from threading import Thread, Event
from time import sleep
from datetime import datetime

#the settings class
class settings:
    #If the version is a release
    release=False

    #What version it is
    version="2.8"
    beta_version="2.81"

    #variables for runtime
    config={}
    language="en"
    upcheck=True
    prompt="Input> "
    ad=True
    logg=True
    log_module_ok=True
    init=False
    start_time_check=True
    start=datetime.now() #The startup time needed for initial Startup
    start_time=""
    settings_module_ok=True
    timeread_module_ok=True
    convert_module_ok=True
    helpfunctions_module_ok=True
    advert_module_ok=True
    password_module_ok=True
    split_module_ok=True

    #the username and system name
    name=getpass.getuser()
    host=socket.gethostname()

class pwgen:
    password="" #the generated password
    e="" #if something went wrong from passwordgen
    autopwgen="null" #if the password should have the same settings except length
    excluded_chars="" #Excluded characters stored within the settings file
    include_uppercase="" #if uppercase should be used defined from the settings file
    include_numbers="" #if the password should have numbers defined by the settings file
    include_specials="" #if there are Special characters needed according to the Settings file.
    



#The class for the variables that are just variables.
class variables:
    #The email adress to directly complain to me
    mail="chaosminecraftmail@gmail.com"
    
    #There are the links that are for the people that snoop in my code to see something
    release_site="https://github.com/Chaosminecraft/Text-converter/releases/"
    beta_site="https://github.com/Chaosminecraft/Text-Converter-Beta/"
    public_archive="https://github.com/Chaosminecraft/Custom-Encoder"
    old_public_archive="https://drive.google.com/open?id=16AcLcgRRLlM7chKUi4eHgT-NOfBCnArM"
    
    #The converted text is here too
    converted_text="" #a basic version of what was last time converted
    detailed_converted_text="" #A more detailed version of from what to what

#Basic System infos
class SysInf:
    system=platform.system()
    version=platform.release()
    detail_version=platform.version()
    cpu_architecture=platform.machine()
    complete_system=f"{system} {version}"

#the other .py files are getting loaded.
try:
    import requests
except ImportError:
    print("Please install the module requests for update checking, for further information, write help requests")
    settings.upcheck=False

try:
    from logger import log_init, log_system, log_info, log_warn, log_error
    log_init(settings.logg)
except ImportError:
    print(f"The logging module is missing/broken, IF that is unexpected, then try getting the latest version of {variables.release_site}")
    settings.log_module_ok=False

try:
    from settings import settings_init, change_settings
except ImportError:
    print(f'Warning: Settings cannot be Initialised/Changed for the moment (External Changing is still possible by makign a settings.json file with the right format or editing the existing one)\nThe format mentioned needed is: {"language": "en", "ad": false, "prompt": "Volks@PC-Patrick ~ % ", "update": false, "logging": true}')
    settings.settings_module_ok=False

try:
    from timeread import timereader, title_time 
except ImportError:
    print("Warning: Time can't be read or title time can't be set.")
    settings.timeread_module_ok=False

try:
    from converter import convert
except ImportError:
    print("The main funcionality of the project is currently not available.")
    settings.convert_module_ok=False

try:
    from helpfunctions import mainhelp, converterhelp
except ImportError:
    print("The main help page is unavailabel, A basic one is available as a backup.")
    settings.helpfunctions_module_ok=False

try:
    from advert import free_ad, get_game
except ImportError:
    print("The advert cannot be shown (shrugs)")
    settings.advert_module_ok=False

try:
    from passwdgen import password_generator
except ImportError:
    print("The Password Generator part is unavailable due to the file probably having a corruption.")
    settings.password_module_ok=False

try:
    from SplitIt.backend import split
except ImportError:
    print("The Split It project is not available at the moment.")
    settings.split_module_ok=False

#The update checking function
def updatecheck():
    #print("FUNCTION START") #For checking if the function starts at all
    if settings.release==True:
        #print("RELEASE VERSION") #says if it is a Release version.
        link_ver="https://github.com/Chaosminecraft/Text-converter/raw/main/version.txt"
        checked_version=requests.get(link_ver, allow_redirects=True)
        checked_version=str(checked_version.content)[2:5]
        #print(checked_version) #If the version from the internet doesn't give good results.
        
        if checked_version>settings.version:
            if settings.language=="de":
                print(f"Da ist eine neue version: {checked_version}\nDa ist der download link:↓{settings.dl_link}\n")
            else:
                print(f"There is a new version: {checked_version}\nThere is the download link:↓{settings.dl_link}\n")
            return
        
        elif checked_version==settings.version:
            if settings.language == "de":
                print(f"\nDie version {settings.version} ist die neuste im moment.\n")
            else:
                print(f"\nThe version {settings.version} is the latest version at the moment.\n")
            return
        
        elif checked_version<settings.version:
            if settings.language=="de":
                print(f"Man muss sich nicht schämen, ein Entwickler zu sein \n")
            else:
                print(f"No need to be ashamed to be a dev \n")
            return
        
        else:
            if settings.language=="de":
                print(f"Eine unbekannte version wurde gefunden. :(\n")
            else:
                print(f"An unknown version was found. :(\n")
            return
    
    elif settings.release==False:
        #print("BETA RELEASE") Says if it is a Beta version.
        link_ver="https://github.com/Chaosminecraft/Text-converter/raw/Beta/betaversion.txt"
        checked_version=requests.get(link_ver, allow_redirects=True, timeout=10)
        checked_version=str(checked_version.content)[2:5]
        #print(checked_version) #If the version from the internet doesn't give good results.

        if checked_version>settings.beta_version:
            if settings.language=="de":
                print(f"Da ist eine neue beta version: {checked_version}\nDa ist der Download link: {settings.beta_channel}\n")
            else:
                print(f"There is a new beta version, Download it here: {checked_version}\nThere is the download link: {settings.beta_channel}\n")
            return
        
        elif checked_version==settings.beta_version:
            if settings.language=="de":
                print(f"Die version {settings.beta_version} ist die neuste Beta version.\n")
            else:
                print(f"The beta verision {settings.beta_version} is the latest version right now.\n")
            return
        
        elif checked_version<settings.beta_version:
            if settings.language=="de":
                print(f"Hallo Mitprogrammierer :)")
            else:
                print(f"Hello fellow coder :)\n")
            return
        
        else:
            if settings.language=="de":
                print(f"Eine unbekannte beta version wurde gefunden :(\n")
            else:
                print(f"An unknown beta version was found :(\n")
            return

class threads:
    updatethread=Thread(target=updatecheck)
    stop_event=Event()
    if settings.timeread_module_ok==True:
        titletime=""

text=f"The platform uses: \n                {SysInf.complete_system} build {SysInf.detail_version}\n                With the architecture: {SysInf.cpu_architecture}\n"
if settings.log_module_ok==True:
    log_system(text)

elif SysInf.system=="'Linux'":
    print("[WARNING] Linux may not work on all versions...")

elif SysInf.system=="'Darwin'":
    print(f"[WARNING] MacOS and other Darwin based systems can't be tested, it may not work!\n")

else:
    print("I can't gauge how good the code runs, I don't know what system that is. ")

def init():
    while True:
        try: #If there is a invalid string in the settings and the Default settings are required
            while True:
                try: #Trying to load the settings file.
                    with open("settings.json", "r") as file:
                        settings.config=json.load(file)
                    
                    settings.language=settings.config.get("language")
                    settings.ad=settings.config.get("advert")
                    settings.prompt=settings.config.get("prompt")
                    settings.upcheck=settings.config.get("update")
                    settings.logg=settings.config.get("logging")
                    pwgen.autopwgen=settings.config.get("autopwgen")
                    pwgen.excluded_chars=settings.config.get("excludechars")
                    #if pwgen.excluded_chars==None:
                    #    pwgen.excluded_chars=""
                    pwgen.include_uppercase=settings.config.get("includeuppercase")
                    pwgen.include_numbers=settings.config.get("includenumbers")
                    pwgen.include_specials=settings.config.get("includespecials")
                    break
                
                except FileNotFoundError: #If the File didn't exist
                    settings_init(name=settings.name, host=settings.host)
        
        except: #if the Default settings are required
            error=traceback.format_exc()
            formatted_error=f"There has been a settings Specific settings error that is currently unable to be fixed. Please manually repair the settings file if possible. THere is more information about the crash:\n{error}"
            print(formatted_error)
            if settings.log_module_ok==True:
                log_system(formatted_error)
            
            print(f"\nThere is the option to report it to the GitHub page as an problem, Do you wanna open the site?")
            while True:
                if input("Yes or No? ").lower()=="yes":
                    if settings.release==True:
                        webbrowser.open(variables.release_site)
                        break

                    elif settings.release==False:
                        webbrowser.open(variables.beta_site)
                        break

                    else:
                        print("I'm sorry, there is only Yes or No... :( )")

            print(f"Due to a Settings error the Default settings are used.\n")

            settings.language="en"
            settings.ad=False
            settings.prompt="Input: "
            settings.upcheck=True
            settings.logg=True

        if settings.ad==True:
            if settings.init==True:
                free_ad(settings.language, settings.logg)

        if settings.init==False:
            if settings.timeread_module_ok==True:
                threads.titletime=Thread(target=title_time, args=(settings, SysInf.system, threads.stop_event, ))
                threads.titletime.start()

        if settings.init==False:
            if settings.upcheck==True:
                threads.updatethread.start()

        if SysInf.system=="Linux":
            print("I'M aware that some issues may come at a few versions on that Project...")
        
        if settings.release==False:
            if settings.language=="de":
                print(f"Willkommen zur Beta version vom Text converter. Bitte beschwer dich bei der Beta seite bei problemen. Sie ist bei {variables.beta_site}")
            
            else:
                print(f"Welcome to the currently Beta version of Text Converter. Please complain on the Beta GitHub Site about issues. it is at {variables.beta_site}")
        
        elif settings.release==True:
            if settings.language=="de":
                print(f"Willkommen zur Beta version vom Text converter. Bitte beschwer dich bei der Beta seite bei problemen. Sie ist bei {variables.release_site}")
    
            else:
                print(f"Welcome to the currently Beta version of Text Converter. Please complain on the Beta GitHub Site about issues. it is at {variables.release_site}")
        
        else:
            print("There are some settings issues, Please delete the settings.json and restart the program.")
        
        main()

# Hauptprogramm anpassen, um den neuen Befehl zu integrieren
def main():
    try:
        try:
            try:
                if settings.upcheck == True:
                    if settings.init == False:
                        threads.updatethread.join()

                if settings.start_time_check == True:
                    settings.start_time = datetime.now() - settings.start
                    if settings.language == "de":
                        print(f"Der Start brauchte {settings.start_time} Sekunden.\n")
                    else:
                        print(f"The startup needed {settings.start_time} seconds.\n")

                    text = f"The program needed {settings.start_time} seconds to start up."
                    log_system(text)

                while True:
                    settings.init = True
                    command = input(settings.prompt).lower()
                    if command == "":
                        if settings.language == "de":
                            print("Nope, da ist nicht ein command wo nichts als input ist.")
                        else:
                            print("Nope, there is not a command that has 0 Characters.")
                    else:
                        text = f"Command used was: {command}"
                        log_info(text=text, logg=settings.logg)

                    if command == "test":
                        print(f"\nTest OK\n")
                        text = "Test Successful"
                        log_info(text=text, logg=settings.logg)

                    elif command == "leetspeak" or command == "leetcode":
                        if settings.language == "de":
                            print(f"\nDieses Feature wurde permanent entfernt!\n")
                        else:
                            print(f"\nThis feature is permanently removed!\n")

                    elif command == "phex" or command == "pbin" or command == "legacy pbin" or command == "hex" or command == "bin" or command == "ascii" or command == "brainfuck" or command == "base64" or command == "symbenc":
                        variables.converted_text = convert(command, settings.language, settings.logg)

                    elif command == "last conversion":
                        print(variables.converted_text)

                    elif command == "help" or command == "helpsite":
                        mainhelp(command, settings.language)

                    elif command == "language" or command == "prompt" or command == "ad" or command == "update" or command == "logging" or command=="auto password" or command=="excluded chars" or command=="include uppercase" or command=="include numbers" or command=="include specials":
                        settings.prompt, settings.language, settings.ad, settings.upcheck, settings.logg, pwgen.autopwgen, pwgen.excluded_chars, pwgen.include_uppercase, pwgen.include_numbers, pwgen.include_specials = change_settings(
                            target=command, prom=settings.prompt, language=settings.language, logging=settings.logg,
                            host=settings.host, name=settings.name, version=SysInf.version, system=SysInf.complete_system
                        )

                    elif command == "reset settings":
                        settings_init(name=settings.name, host=settings.host)

                    elif command == "check update":
                        updatecheck()
                    
                    elif command == "password generator" or command == "passwort generator" or command == "passwordgen" or command == "pwgen":
                        pwgen.e, pwgen.password=password_generator(settings, pwgen, variables)  # Neuer Passwort-Generator-Befehl
                    
                    elif command == "manualtraceback":
                        text = f"There as an unexpected error, There is a traceback:\n{traceback.format_exc()}"
                        log_system(text)
                    
                    elif command == "split it test module":
                        print(f"This is a hidden Module test! Use with caution!!!\nThere is only Yes, No and Skip")
                        while True:
                            standalone=input("Test Standalone or Module?").lower()
                            if standalone=="yes" or standalone=="ja":
                                standalone=True
                                break
                            elif standalone=="no" or standalone=="nein":
                                standalone=False
                                break
                            elif standalone=="skip":
                                break
                            else:
                                if settings.language=="de":
                                    print("Nope, Da gibt es nur Ja oder Nein oder Skip.")
                                else:
                                    print("Nope, There is only Yes or No or Skip.")
                        
                        if standalone==True or standalone==False:
                            split(standalone=standalone)
                        else:
                            split(standalone=False)
                    
                    elif command == "split it":
                        split(standalone=False)
                        
            except AttributeError:
                pass
        except KeyboardInterrupt:
            temp="" #Put closing function here
    except:
            traced = traceback.format_exc()
            if settings.language == "de":
                print(f"\n Ein unerwarteter Fehler erschien, Hier ist was passierte:\n{traced}\n")
            else:
                print(f"\nAn unexpected error occurred... there is a trace:\n{traced}\n")

            text = f"There as an unexpected error, There is a traceback:\n{traced}"
            log_system(text)

if __name__ == "__main__":
    init()