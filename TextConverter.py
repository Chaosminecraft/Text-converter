import getpass, os, platform, socket, json, traceback, locale, time, datetime, threading, logging, subprocess, sys

#The version variables in a class
class version:
    release=False        #if that version is a release or beta version
    version="3.1.0"      #The release version
    beta_version="3.1.9" #The Beta version

#The settings variables in a class (Some name clashing was making me name the settings class to config)
class config:
    config={}                 #The variable that loads the settings file
    language="en"             #The Language Variable
    upcheck=True              #If the code checks for updates
    prompt="Input> "          #This is the prompt look if loading the settings fails somehow (Heck that all that is pre-configured is a failsafe)
    ad=True                   #This is if the ad for the game while true: learn(), But I'm not getting any ad money to show that, so feel free to just set it to false if you wanna.
    logg=True                 #This is a optional thing, But I'm redoing the logging part. So that is to be seen what happens to it.
    gui=False                 #The default setting of the CLI/GUI setting is False
    theme="bright"            #The default theme setting
    log_name=""               #The log name in case of a error
    name=getpass.getuser()    #The Username
    host=socket.gethostname() #The PC name

#The Startup variables in a class
class startup:
    init=False                    #That is a variable that is soon to be used for logging if the code at least got to the prompt part
    Startup_time_check=True       #That is if the Startup time should be checked
    start=datetime.datetime.now() #that is taking the time when the code got started
    stop=""                       #that is the time needed that the code got to the prompt part (including update checking)

#Some exit variables
class stopvars:
    exit_code=1   #The exit code get's changed on what failed and code is maybe gonna be added to look what went wrong.
    is_exit=False #That is somewhat of a Band aid fix for the exit situation.

#the variables in here is if the module loading went ok or if something went south and to not use the funcionality of that module (module checking might be getting added in the future)
class modules:
    settings_module=True
    convert_module=True
    helpsite_module=True
    advert_module=True
    splitit_module=True
    logg_module=True
    gui_module=True
    ping_module=True

#Other General variables or links or E-Mail (For the project)
class info:
    mail="chaosminecraftmail@gmail.com"                                                     #The Email adress that is a direct contact to me for Feature suggestions (if youd're not comfortable with GitHub) or if there is an issue on the project
    release_site="https://github.com/Chaosminecraft/Text-converter/releases/"               #The main version that also has releases with EXE files
    issues_site="https://github.com/Chaosminecraft/Text-converter/issues"
    beta_site="https://github.com/Chaosminecraft/Text-converter/tree/Beta"                  #The Beta branch that may have the latest fixes (no releases, only Source Code!!!)
    public_archive="https://github.com/Chaosminecraft/Custom-Encoder"                       #The old versions of my converter
    old_public_archive="https://drive.google.com/open?id=16AcLcgRRLlM7chKUi4eHgT-NOfBCnArM" #Yeah... I still host the first few versions in here... But at least I still keep them there if anyone wants to see.
    ingenarel="https://github.com/ingenarel"                                                #A real chad that made something neat (Yeah, Path n stuff is wonky right now on his version)

class VariableData:
    converted_text="No text was converted." #The last converted string
    command=""                              #The command variable

#Basic system info for the log
class sysinf:
    system=platform.system()
    release=platform.release()
    build=platform.version()
    cpu=platform.machine()
    system_desc=f"{system} {release}"

class PingDataModule:
    host=""
    maxpings=100
    last_ping="No ping done."

#backup functions (Experimental)
class backupfunc:
    def backup_logg(**kwargs):
        if kwargs["mode"]=="init":
            if not os.path.exists('meinOrdner'):
                os.mkdir('meinOrdner')
            loggfile=datetime.datetime.now().strftime("%d.%m.%Y %H.%M.%S")
            config.logg_path=f"logs/{loggfile} logg.txt"
            logging.basicConfig(filename=config.logg_path, filemode="w", level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%d/%m/%Y %H:%M:%S")
            return

        elif kwargs["mode"]=="logg":
            text=f'[SYSTEM] {kwargs["text"]}'
            logging.info(text)
            return
    
    def backup_setting_init(**kwargs):
        system_language=locale.getdefaultlocale()[:1]
        system_language=str(system_language).lower()[2:7]
    
        if system_language=="de_de":
            language="de"
    
        else:
            language="en"
    
        ad=True
    
        logg=True
    
        upcheck=True
    
        prompt="{name}@{host}:~$ "
        for r in (("{name}", config.name), ("{host}", config.host)):
            prompt=prompt.replace(*r)
    
        gui=False
        
        theme="bright"
    
        settings_file={
            "language":language,
            "advert":ad,
            "prompt":prompt,
            "update":upcheck,
            "logging":logg,
            "gui":gui,
            "theme":theme
            }
    
        with open("settings.json", "w") as save:
            json.dump(settings_file, save)
    
        return prompt, language, ad, upcheck, theme
    
    def backuphelp():
        if config.language=="de":
            print(f"""
Allgemeine commands:
    Help gibt den Hilfetext aus
    Hex konvertiert zwischen Hex und Text
    phex konvertiert zwischen Pseudo-Hex und Text
    bin konvertiert zwischen Binär und Text
    pbin konvertiert zwischen Pseudobinärdatei und Text
    lpbin konvertiert zwischen einer älteren Version von Pseudo Binary und Text
    ASCII konvertiert zwischen ASCII und Text
    Brainfuck konvertiert zwischen Brainfuck und Text
    base64 konvertiert zwischen base64 und Text (vorerst nur normaler Text)\n
Zusätzliche Informationen:
    language Gibt dir eine auswahl zwischen Deutsch(de) und Englisch(en)
    prompt ändert den prompt look (direkt nach start den prompt)
    ad gibt dir die option ob du die Werbung sehen willst oder nicht
    update gibt dir die option nach updates zu schauen am start.
    logging gibt dir die option ob du Nicht essenzielle sachen loggen möchtest.
    ping ist ein simpler ping command\n""")
        
            return
    
        else:
            print(f"""
Common commands:
    Help gives the Help text
    Hex converts between hex and text
    phex converts between pseudo hex and text
    bin converts between Binary and text
    pbin converts between pseudo binary and text
    lpbin converts between an older version of Pseudo Binary and text
    ascii converts between ascii and text
    brainfuck converts between brainfuck and text
    base64 converts between base64 and text (only normal text for now)\n
Additional info:
    language let's you change between English(en) or German(de).
    prompt let's you change the prompt look. (After startup the prompt)
    ad let's you change if you wanna see the ad (currently broken)
    update let's you change the setting if you want to check for updates.
    logging let's you change if you wanna log non critical things. (critical things are like: Mid runtime there was a Recoverable or non recoverable error)
    ping is a simple ping command\n""")
        
            return

try:
    import requests #Trying to import requests
except ImportError: #If the module isn't installed.
    try:
        if input("The 'requests' Module is missign, do you wanna install it? (Yes/No) ").lower() == "yes": #asking if installing the module is wanted.
            if sysinf.system=="Windows":
                subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
            elif sysinf.system=="Linux":
                subprocess.check_call([sys.executable, "-m", "pip", "install", "--user","requests", "--break-system-packages"])
            import requests
        
        else:
            print("The requests module isn't installed, that simply means that no Update checking is available.")
            config.upcheck=False

    except subprocess.CalledProcessError:
        print("The requests module isn't installed, that simply means that no Update checking is available.")
        config.upcheck=False

try:
    from logger import *
    log_init(config)
except ImportError:
    backupfunc.backup_logg(mode="init")
    if version.release==True:
        print(f"The logging module is missing/broken, A bare basic built in logging version for errors and system calls is used now. Please get the missing module at: {info.release_site}")
    else:
        print(f"The logging module is missing/broken, A bare basic built in logging version for errors and system calls is used now. Please get the missing module at: {info.beta_site}")
    modules.logg_module=False

try:
    from settings import settings_init, change_settings
except ImportError:
    if version.release==True:
        print(f"The module that is responsible for changing settings is unable to be loaded, please download the version of converter.py of V{version.version}")
    else:
        print(f"The module that is responsible for changing settings is unable to be loaded, please download the version of converter.py of V{info.beta_site}")
    print("INFO: Only manual settings changes are possible at the moment. You can load the changes via 'reload settings'")
    modules.settings_module=False

try:
    from converter import parse_input
except ImportError:
    if version.release==True:
        print(f"The module that is responsible for converting text is unable to be loaded, please download the version of converter.py of V{version.version}")
    else:
        print(f"The module that is responsible for converting text is unable to be loaded, please download the version of converter.py of V{info.beta_site}")
    modules.convert_module=False

try:
    from helpfunctions import mainhelp
except ImportError:
    print("The help page module can't be loaded, that is currently then not available. I might move the Help site to the relevant modules.")
    modules.helpsite_module=False

try:
    from advert import free_ad, get_game
except ImportError:
    modules.advert_module=False

try:
    from gui import cli_to_gui
except ImportError:
    modules.gui_module=False
    print("The GUI module is unable to be loaded. If you want teh GUI too, please download the beta again. (and if you downloaded it before, re-extract it maybe.)")

try:
    from SplitIt.backend import split
except ImportError:
    print("The project SplitIt is unable to be imported. That means it can't be ran.")
    modules.splitit_module=False

try:
    from pinger import init_ping
except ImportError:
    print("The ping module is unable to be imported. That means there is no pinging :(")
    modules.ping_module=False

#The update checking function
def updatecheck():
    #print("FUNCTION START") #For checking if the function starts at all
    if version.release==True:
        #print("RELEASE VERSION") #says if it is a Release version.
        link_ver="https://raw.githubusercontent.com/Chaosminecraft/Text-converter/refs/heads/Beta/version.txt"
        checked_version=requests.get(link_ver, allow_redirects=True)
        checked_version=str(checked_version.content)[2:7]
        #print(checked_version) #If the version from the internet doesn't give good results.
        
        if checked_version>version.version:
            if config.language=="de":
                print(f"Da ist eine neue version: {checked_version}\nDa ist der download link:↓{info.release_site}\n")
            else:
                print(f"There is a new version: {checked_version}\nThere is the download link:↓{info.release_site}\n")
            return
        
        elif checked_version==version.version:
            if config.language == "de":
                print(f"\nDie version {version.version} ist die neuste im moment.\n")
            else:
                print(f"\nThe version {version.version} is the latest version at the moment.\n")
            return
        
        elif checked_version<version.version:
            if config.language=="de":
                print(f"Yay, Dev gefunden :D\n")
            else:
                print(f"Yay, found a Dev :D\n")
            return
        
        else:
            if config.language=="de":
                print(f"Eine unbekannte version wurde gefunden. :(\n")
            else:
                print(f"An unknown version was found. :(\n")
            return
    
    elif version.release==False:
        #print("BETA RELEASE") Says if it is a Beta version.
        link_ver="https://raw.githubusercontent.com/Chaosminecraft/Text-converter/refs/heads/Beta/betaversion.txt"
        checked_version=requests.get(link_ver, allow_redirects=True, timeout=10)
        checked_version=str(checked_version.content)[2:7]
        #print(checked_version) #If the version from the internet doesn't give good results.

        if checked_version>version.beta_version:
            if config.language=="de":
                print(f"Da ist eine neue beta version: {checked_version}\nDa ist der Download link: {info.beta_site}\n")
            else:
                print(f"There is a new beta version, Download it here: {checked_version}\nThere is the download link: {info.beta_site}\n")
            return
        
        elif checked_version==version.beta_version:
            if config.language=="de":
                print(f"Die version {version.beta_version} ist die neuste Beta version.\n")
            else:
                print(f"The beta verision {version.beta_version} is the latest version right now.\n")
            return
        
        elif checked_version<version.beta_version:
            if config.language=="de":
                print(f"Yay, Dev gefunden :D\n")
            else:
                print(f"Yay, found a Dev :D\n")
            return
        
        else:
            if config.language=="de":
                print(f"Eine unbekannte beta version wurde gefunden :(\n")
            else:
                print(f"An unknown beta version was found :(\n")
            return

def title_time(stop_event):
    try:
        if sysinf.system=="Windows":
            while not stop_event.is_set():
                start=time.time()
                now=datetime.datetime.now()
                if config.language=="de":
                    now=now.strftime("%d/%m/%Y, %H:%M:%S") #%H:%M:%S.%f
                if config.language=="en":
                    now=now.strftime("%m/%d/%Y, %r")
                
                if version.release==True:
                    os.system(f"title Text Converter V{version.version} {now}")
                else:
                    os.system(f"title Text Converter Beta V{version.beta_version} {now}")
                elapsed_time=time.time()-start
                wait_time=max(0.5, elapsed_time * 2)
                time.sleep(wait_time)
            return   


        if sysinf.system=="Linux":
            sys.stdout.write(f"\x1b]2;Text Converter V2.3\x07")
            return
        
        else:
            print("I sadly don't know how to handle the title of that System. :( )")
            return
                
    except:
        traced=traceback.format_exc()
        print(f"There has been an exception:\n{traced}")
        text=f"There has been an exception:\n{traced}"
        log_system(text)
        if sysinf.system=="Linux":
            sys.stdout.write(f"\x1b]2;Text Converter V2.3\x07")
        if sysinf.system=="Windows":
            if version.release==True:
                os.system(f"title Text Converter V{version.version}")
            elif version.release==False:
                os.system(f"title Text Converter V{version.beta_version}")
        return

class threads:
    updatethread=threading.Thread(target=updatecheck)
    stop_event=threading.Event()
    time_thread=threading.Thread(target=title_time, args=(stop_event, ))

text=f"The platform uses: \n                {sysinf.system_desc} build {sysinf.build}\n                With the architecture: {sysinf.cpu}\n"
if modules.logg_module==True:
    log_system(text)
else:
    backupfunc.backup_logg(mode="logg", text=text)

if  sysinf.system=="Linux":
    print("INFO: I know that my project might be not too great for linux, but I might in the future test it more often after the big refactoring and merge.")

if sysinf.system=="Darwin":
    print("WARNING: You're on your own. I (the creator) do not test the code if it runs on MacOS/Darwin. Good luck.")

def init():
    while True:
        try:
            with open("settings.json", "r") as load:
                config.config=json.load(load)
        except FileNotFoundError:
            if modules.settings_module==True:
                settings_init(name=config.name, host=config.host)
            else:
                backupfunc.backup_setting_init()
            with open("settings.json", "r") as load:
                config.config=json.load(load)

        try:
            config.language=config.config.get("language")
            #print(config.language) #Debugging purposes
            if config.language not in ("de", "en"):
                config.language="en"
            config.ad=config.config.get("advert")
            if config.ad not in (True, False):
                config.ad=True
            config.prompt=config.config.get("prompt")
            if config.prompt==None:
                config.prompt=f"{config.name}@{config.host}:~$ "
            config.upcheck=config.config.get("update-check")
            if config.upcheck not in (True, False):
                config.upcheck=True
            config.logg=config.config.get("logging")
            if config.logg not in (True, False):
                config.logg=True
            config.gui=config.config.get("gui")
            if config.gui not in (True, False):
                config.gui=False
            config.theme=config.config.get("theme")
            if config.theme not in ("bright", "dark"):
                config.theme="bright"
            break

        except:
            exception=traceback.format_exc()
            text=f"There has been a edge case that has not been found yet, There is the traceback:\n{exception}"
            if modules.logg_module==True:
                log_error(text)
            if input("Press enter to retry, to close this programm, write exit").lower()=="exit":
                break
    
    if stopvars.is_exit==False:
        if config.ad==True:
            if startup.init==False:
                if modules.advert_module==True:
                    free_ad(config)

        if startup.init==False:
            threads.time_thread.start()
        
        if startup.init==False:
            if config.upcheck==True:
                threads.updatethread.start()
        
        if version.release==True:
            if config.language=="de":
                print(f"\nWillkommen zur Beta version vom Text converter. Bitte beschwer dich bei der Beta seite bei problemen. Sie ist bei {info.release_site}")
            else:
                print(f"\nWelcome to the currently Beta version of Text Converter. Please complain on the Beta GitHub Site about issues. it is at {info.release_site}")
        
        elif version.release==False:
            if config.language=="de":
                print(f"""\n[WARNUNG] Dies ist eine BETA version, Die könnte unstabil sein.
Bitte meldet dies bei:
{info.issues_site}

Info: GUI ist bis jetzt nur bei Windows 10 getestet

Willkommen zur Beta version vom Text converter.\n""")

            else:
                print(f"""\n[WARNING] This is a BETA version, There might be errors in the code.
So please report it to:

{info.issues_site}

Info: GUI is for now only tested on Windows 10.

Welcome to the Beta version of the Text Converter.\n""")
        while stopvars.is_exit is not True:
            if stopvars.is_exit==False:
                main()


def main():
    try:
        while stopvars.exit_code is not True:
            try:
                if config.upcheck==True:
                    if startup.init==False:
                        threads.updatethread.join()

                if startup.init==False:
                    if startup.Startup_time_check==True:
                        startup.start= datetime.datetime.now()-startup.start
                        if config.language=="de":
                            print(f"Das programm hat so viel zeit gebraucht: {startup.start}")
                        else:
                            print(f"The programm needed that much to start: {startup.start}")

                        text=f"The programm needed that much to start: {startup.start}"
                        if modules.logg_module==True:
                            log_system(text)
                        else:
                            backupfunc.backup_logg(mode="logg", text=text)

                startup.init=True
                if config.gui==True:
                    if modules.gui_module==True:
                        cli_to_gui(config, sysinf, version)
                        return
                    else:
                        config.gui=False
                else:
                    VariableData.command=input(config.prompt).lower()

                if VariableData.command=="":
                    if modules.logg_module==True:
                        log_info(config, text=f"The user didn't use a command")
                    else:
                        backupfunc.backup_logg(mode="logg", text=f"The user didn't use a command")
                else:
                    if modules.logg_module==True:
                        log_info(config, text=f"The user used the command: {VariableData.command}")
                    else:
                        backupfunc.backup_logg(mode="logg", text=f"The user used the command: {VariableData.command}")
                if VariableData.command=="":
                    if config.language=="de":
                        print("Kein command gefunden.")
                    else:
                        print("No command found.")

                elif VariableData.command=="test":
                    print(f"\nTestOK!!\n")
                    if modules.logg_module==True:
                        log_system(text="The test went ok.")

                elif VariableData.command in ("phex", "pbin", "lpbin", "hex", "bin", "ascii", "brainfuck", "base64", "symbenc"):
                    if modules.convert_module==True:
                        VariableData.converted_text=parse_input(config, mode=VariableData.command)
                    else:
                        if config.language=="de":
                            print("Das convert modul ist nicht verfügbar.")
                        else:
                            print("The convert module is unavailable.")

                elif VariableData.command=="last conversion":
                    print(VariableData.converted_text)
                
                elif VariableData.command in ("help", "hilfe"):
                    if modules.helpsite_module==True:
                        mainhelp(config.language)
                    else:
                        backupfunc.backuphelp()
                
                elif VariableData.command in ("language", "prompt", "ad", "update", "logging", "gui", "theme"):
                    config.prompt, config.language, config.ad, config.upcheck, config.logg, config.gui, config.theme = change_settings(config, sysinf, option=VariableData.command)

                elif VariableData.command=="reset settings":
                    config.prompt, config.language, config.ad, config.upcheck, config.logg, config.gui, config.theme = settings_init(name=config.name, host=config.host)
                
                elif VariableData.command=="reload settings":
                    while True:
                        try:
                            with open("settings.json", "r") as load:
                                config.config=json.load(load)
                        except FileNotFoundError:
                            if modules.settings_module==True:
                                settings_init(name=config.name, host=config.host)
                            else:
                                backupfunc.backup_setting_init()
                            with open("settings.json", "r") as load:
                                config.config=json.load(load)

                        try:
                            config.language=config.config.get("language")
                            #print(config.language) #Debugging purposes
                            if config.language not in ("de", "en"):
                                config.language="en"
                            config.ad=config.config.get("advert")
                            if config.ad not in (True, False):
                                config.ad=True
                            config.prompt=config.config.get("prompt")
                            if config.prompt==None:
                                config.prompt=f"{config.name}@{config.host}:~$ "
                            config.upcheck=config.config.get("update-check")
                            if config.upcheck not in (True, False):
                                config.upcheck=True
                            config.logg=config.config.get("logging")
                            if config.logg not in (True, False):
                                config.logg=True
                            config.gui=config.config.get("gui")
                            if config.gui not in (True, False):
                                config.gui=False
                            config.theme=config.config.get("theme")
                            if config.theme!="bright" or config.theme!="dark":
                                config.theme="bright"
                            break

                        except:
                            exception=traceback.format_exc()
                            text=f"There has been a edge case that has not been found yet, There is the traceback:\n{exception}"
                            if modules.logg_module==True:
                                log_error(text)
                            if input("Press enter to retry, to close this programm, write exit").lower()=="exit":
                                return

                elif VariableData.command=="check update":
                    if config.upcheck==True:
                        updatecheck()
                    else:
                        if config.language=="de":
                            print("requests ist nicht installiert.")
                        else:
                            print("requests is not installed.")

                elif VariableData.command=="split it":
                    print("Command comming up ;)")
                
                elif VariableData.command=="start gui" or VariableData.command=="sg":
                    if modules.gui_module==True:
                        backup=config.gui
                        config.gui=True
                        cli_to_gui(config, sysinf, version)
                        config.gui=backup
                    else:
                        print("The gui module is missing.")
                
                elif VariableData.command=="time":
                    timereader()
                
                elif VariableData.command=="ping":
                    PingDataModule.host=input(f"\nWhat host? ")
                    while True:
                        try:
                            PingDataModule.last_ping=PingDataModule.maxpings=int(input("How many?(don't do too many if slow internet) "))
                            break
                        except ValueError:
                            print(f"Nope, that ain't a number.\n")
                    init_ping(PingDataModule)
                
                elif VariableData.command=="last ping" or VariableData.command=="lp":
                    print(f"\n{PingDataModule.last_ping}\n")

                elif VariableData.command=="exit":
                    close()
                    if stopvars.is_exit==True:
                        break
                
                else:
                    if config.language=="de":
                        print(f"Upsi, der 'command' {VariableData.command} ist nicht ein command.")
                    else:
                        print(f"Oops, the 'command' {VariableData.command} isn't a command.")

            except KeyboardInterrupt:
                print()
                close()
                if stopvars.is_exit==True:
                    break
    except:
        error=traceback.format_exc()
        if version.release==False:
            print(f"An error happened, there it is:\n{error}")
        else:
            print(f"An error occured, Please send the log shown to the github issues tab with an explenation of what was done for it to happen.\nThe log file: {config.log_name}\nThe github issues link: {info.issues_site}")
            text=f"There was an error, This is the traceback:\n{error}"
            if modules.logg_module==True:
                log_error(text)
            else:
                backupfunc.backup_logg(mode="logg", text=text)

def close():
    if sysinf.system=="Linux":
        os.system("clear")
    elif sysinf.system=="Windows":
        os.system("cls")

    while True:
        if config.language=="de":
            text=input("Willst du das Programm beenden? (Ja/Nein) ").lower()
        else:
            text=input("Do you wanna close the Programm? (Yes/No) ").lower()
        
        if text in ("ja", "j", "yes", "y"):
            threads.stop_event.set()

            if config.language=="de":
                print("Programm schließt...")
            else:
                print("Closing program...")
            
            time.sleep(1)
            stopvars.exit_code=0
            stopvars.is_exit=True
            text=f"The programm successfully closed with the exit code: {stopvars.exit_code}"
            if modules.logg_module==True:
                log_system(text)
            else:
                backupfunc.backup_logg(mode="logg", text=text)
            return
        
        else:
            
            if sysinf.system=="Linux":
                os.system("clear")
            elif sysinf.system=="Windows":
                os.system("cls")

            if config.language=="de":
                print("Schließen gestopt.")
            else:
                print("Stopped closing.")
            return

def timereader():
    current_time=datetime.datetime.now()
    if config.language == "de":
        print(f"\nDie zeit ist:", current_time.strftime("%d/%m/%Y, %H:%M:%S"), "\n")

    else:
        print(f"\nThe time is:", current_time.strftime("%m/%d/%Y, %r"), "\n")

    return

if __name__=="__main__":
    init()