#importing time from time to look about the Time needed to do the initialisation part
from datetime import datetime
start=datetime.now()

#importing the Needed modules
import getpass
import os as ost
import platform
import socket
from threading import Thread, Event

#the Variables for the Logger module
logg="true"
logg_makefile="true"

#the Links for the download of older/newer versions.
dl_link="https://github.com/Chaosminecraft/Text-converter/releases/"
old_link="https://drive.google.com/open?id=16AcLcgRRLlM7chKUi4eHgT-NOfBCnArM"
old_repo="https://github.com/Chaosminecraft/Custom-Encoder"

#initial variable for ad and other stuff
ad="true"
upcheck="true"
module=""

temp=1

#for some reason that logging function is needed...
def log_module_load(module):
    global temp
    #print(f"{temp}times started the function.")
    temp+=1
    text=f"The module {module} has been loaded."
    log_system(text, logg)
    return

def log_module_error(module):
    text=f"The module {module} couldn't be loaded, please check the file for corruptions."
    log_error(text, logg)
    return

done = False



#custom modules are being imported now.
while True:
    try:
        module="logger"
        from logger import log_init, log_system, log_info, log_error
        log_init(logg_makefile) #making the log file
        log_module_load(module)
        module="settings"
        from settings import ad_settings, get_lang, helper, logg_settings
        log_module_load(module)
        module="learn"
        from learn import free_ad, get_game
        log_module_load(module)
        module="updater"
        from updater import *
        log_module_load(module)
        module="converter"
        from converter import *
        log_module_load(module)
        module="timeread"
        from timeread import *
        log_module_load(module)
        done = True
        if done == True:
            break
    except ModuleNotFoundError:
        log_module_error(module)
        input(f"\nThere has been a import error, please check the logs in the logs folder.\nPress enter to Exit")
        exit()

sys=platform.system()
ver=platform.release()
cpu=platform.machine()
#print(cpu)
arc=platform.architecture()[1]
system=f"{sys} {ver}"
with open("platform.txt", "w") as save:
    save.write(system)

with open("system.txt", "w") as save:
    save.write(sys)

if sys=="Windows":
    if ver>="10":
        print("The Recommend OS is used.")
    if ver=="8.1":
        print("That operating system should work.")
    if ver=="7":
        print("That is my Favourite OS, but problems may occure.")
    
if sys=="'Linux'":
    print("WARNING: that is not the operating system of that it's designed to run on! there might be some problems.")

if sys=="Darwin":
    print("This platform is not supported!")
    input("press enter to exit")
    exit()

stop_event = Event()

#email adress for project
mail="chaosminecraftmail@gmail.com"

#determins if release or not and determins the version.
release="true"
version="2.3"

#variables for the rest of startup
init="false"
check_init_time=True
change="false"
language="en"
error_reason=""
noinp="false"
content=""
condecon=""

#the initialising phase of the code
def startup():
    global logg
    global language
    global error_reason
    while True:
        try:
            language_file=open("lang.txt", "r")
            language=language_file.read()
            language_file.close()
        except FileNotFoundError:
            get_lang(language, change, init)
            language_file=open("lang.txt", "r")
            language=language_file.read()
            language_file.close()

        try:
            logg_file=open("logg.txt", "r")
            logg=logg_file.read()
            logg_file.close()
        except FileNotFoundError:
            logg_settings(init, language)
            logg_file=open("logg.txt", "r")
            logg=logg_file.read()
            logg_file.close()
    
        free_ad(language, logg)
        if init=="false":
            #the thread that updates the time in the title
            timethread=Thread(target=title_time, args=(stop_event, language))
            timethread.start()

        if sys=="'Linux'":
            print("Warning: it is a Known issue that the time is not updating until the Next line is written. that may be fixed in newer versions!")

        if language == "de":
            print(f"\nWilkommen beim Text converter, wenn es das erste mal ist das du benutzt, es gibt den befehl: help")
        if language == "en":
            print(f"\nWelcome at the text converter, if that is the first time that you use it, there is the command: help")

        main_thread()

#the main part of the code
def main_thread():
    global init
    global stop_event
    global check_init_time
    try:
        try:
            while True:
                name=getpass.getuser()
                host=socket.gethostname()
                init="true"
                if check_init_time==True:
                    end=datetime.now()
                    computed=end-start
                    print(f"\nThe project needed {computed} Seconds to start.\n")
                    check_init_time=False
                comand=input(f"{name}@{host}:~$ ")
                
                text=comand
                log_info(text, logg)
                
                if comand.lower()=="phex" or comand.lower()=="pbin" or comand.lower()=="legacy pbin" or comand.lower()=="hex" or comand.lower()=="bin" or comand.lower()=="ascii" or comand.lower()=="leetcode" or comand.lower()=="brainfuck" or comand.lower()=="base64":
                    convert(comand, language, logg, name)

                if comand.lower()=="help":
                    helper(language, logg)

                if comand.lower()=="get game":
                    get_game(language, logg)
                
                if comand.lower()=="ad setting":
                    ad_settings(language, logg)
                
                if comand.lower()=="set language":
                    change="true"
                    stop_event.set()
                    get_lang(language, change, init)
                    change="false" 
                    init="false"
                    stop_event = ""
                    stop_event = Event()
                    return
                
                if comand.lower()=="clear screen":
                    if sys.lower()=="windows":
                        os.system("cls")

                    if sys.lower()=="linux":
                        os.system("clear")
                
                if comand.lower()=="reset":
                    stop_event.set()
                    if sys.lower()=="windows":
                        os.system("cls")
                    
                    if sys.lower()=="linux":
                        os.system("cleear")
                    init="false"
                    stop_event = ""
                    stop_event = Event()
                    return
                
                if comand.lower()=="exit":
                    close(language, sys)
                
                if comand.lower()=="halt":
                    stop_event.set()
                    exit()
        except TypeError:
            if language=="en":
                print(f"\nThere has been an unexpected Error on Startup time check.\n")
            if language=="de":
                print(f"\nDas war ein unerwarteter Fehler beim startzeit Check.\n")
            sleep(5)
            stop_event.set()
            exit()

    except KeyboardInterrupt:
        close(language, sys)

count=0

def close(language, sys):
    global count
    try:
        if sys.lower()=="windows":
            os.system("cls")

        if sys.lower()=="linux":
            os.system("clear")

        if language=="en":
            answer=input("Do you wanna close that program? ")
            if answer.lower()=="no" or answer.lower()=="false":
                return

        if language=="de":
            answer=input("Willst du das Program schliesen? ")
            if answer.lower()=="nein" or answer.lower()=="false":
                return
        
        #t.sleep(4)
        if sys.lower()=="windows":
            os.system("cls")

        if sys.lower()=="linux":
            os.system("clear")
            timethread=False
        stop_event.set()
        exit()

    except KeyboardInterrupt:
        close_2(language)
        close(language)

def close_2(language):
    global count
    if count==0:
        print(f"\n\nyou're already on the Exit.\n")
        count+=1
        return
    if count==1:
        print(f"\n\nAre you seroius?\n")
        count+=1
        return
    if count==2:
        print(f"\n\nJust stop!\n")
        count+=1
        return
    if count==3:
        print(f"\n\nSTOP IT!!!\n")
        count+=1
        return
    if count==4:
        print(f"\n\nI'M SERIOUS, THIS IS PAINFUL!!!!\n")
        count+=1
        return
    if count<4 or count<10:
        print(f"\n\nThat is all i'm gonna say!\n")
        count+=1
        return
    if count<10 or count<20:
        print(f"\n\nSTOP IT!!! IT IS PAINFULL!!! I DON'T EVEN LIVE. I'M JUST SENTIENT!!!\n")
        count+=1
        return
    if count==20:
        print(f"\n\nLOOK WHAT YOU DONE!")
        message="YOU DONE THAT!"
        with open("OPEN_ME.txt", "w") as save:
            save.write(message)
        command="notepad.exe OPEN_ME.txt"
        os.system(command)
        os.remove("OPEN_ME.txt")
        stop_event.set()
        exit()

def ModuleRecovery(module):
    if module == "converter":
        data="I2ltcG9ydGluZyB0aGUgbmVlZGVkIG1vZHVsZXMNCmltcG9ydCByZXF1ZXN0cw0KaW1wb3J0IG9zDQoNCiNWYXJpYWJsZXMgZm9yIHRoZSBjb2RlDQpsaW5rPSJodHRwczovL2dpdGh1Yi5jb20vQ2hhb3NtaW5lY3JhZnQvVGV4dC1jb252ZXJ0ZXIvcmVsZWFzZXMvIg0KcnZlcnNpb249IjIuMyINCmJ2ZXJzaW9uPSIyLjMiDQoNCiN0aGUgbWFpbiBmdW5jdGlvbiBvZiB0aGF0IGNvZGUNCmRlZiB1cGRhdGUocmVsZWFzZSwgbGFuZ3VhZ2UpOg0KICAgIHRyeTogI1RyeWluZyB0byBDaGVjayBmb3IgdXBkYXRlcw0KICAgICAgICBpZiByZWxlYXNlPT0idHJ1ZSI6DQogICAgICAgICAgICAgICAgdXJsID0gImh0dHBzOi8vd3d3LmRyb3Bib3guY29tL3MvYTV3Yzdvb242OG56OWlvL3ZlcnNpb24tYmV0YS50eHQ/ZGw9MSINCiAgICAgICAgICAgICAgICBuZXdfdmVyc2lvbiA9IHJlcXVlc3RzLmdldCh1cmwsIGFsbG93X3JlZGlyZWN0cz1UcnVlKQ0KICAgICAgICAgICAgICAgIG9wZW4oInJlbGVhc2UtdmVyc2lvbi50eHQiLCAid2IiKS53cml0ZShuZXdfdmVyc2lvbi5jb250ZW50KQ0KICAgICAgICAgICAgICAgIA0KICAgICAgICAgICAgICAgIGlmIG5ld192ZXJzaW9uPnJ2ZXJzaW9uOg0KICAgICAgICAgICAgICAgICAgICBpZiBsYW5ndWFnZS5sb3dlcigpID09ICJlbiI6DQogICAgICAgICAgICAgICAgICAgICAgICBwcmludChmIlxuVGhlcmUgaXMgYW4gbmV3IHZlcnNpb246IHtuZXdfdmVyc2lvbn1cblRoZXJlIGlzIGRvd25sb2FkIHRoZSBsaW5rOuKGk1xue2xpbmt9XG4iKQ0KDQogICAgICAgICAgICAgICAgICAgIGlmIGxhbmd1YWdlLmxvd2VyKCkgPT0gImRlIjoNCiAgICAgICAgICAgICAgICAgICAgICAgIHByaW50KGYiXG5EYSBpc3QgZWluZSBuZXVlIFZlcnNpb246IHtuZXdfdmVyc2lvbn1cbkRhIGlzdCBkZXIgbGluayB6dW0gaGVydW50ZXJsYWRlbjrihpNcbntsaW5rfVxuIikNCg0KICAgICAgICAgICAgICAgICAgICBlbHNlOg0KICAgICAgICAgICAgICAgICAgICAgICAgcHJpbnQoZiJcblRoZXJlIGlzIGFuIG5ldyB2ZXJzaW9uOiB7bmV3X3ZlcnNpb259XG5UaGVyZSBpcyB0aGUgZG93bmxvYWQgbGluazrihpNcbntsaW5rfVxuIikNCg0KICAgICAgICAgICAgICAgIGlmIG5ld192ZXJzaW9uPT1ydmVyc2lvbjoNCiAgICAgICAgICAgICAgICAgICAgaWYgbGFuZ3VhZ2UubG93ZXIoKSA9PSAiZW4iOg0KICAgICAgICAgICAgICAgICAgICAgICAgcHJpbnQoZiJcblRoZSB2ZXJzaW9uIGlzIHRoZSBsYXRlc3QgdmVyc2lvbiBhdCB0aGUgbW9tZW50LlxuIikNCg0KICAgICAgICAgICAgICAgICAgICBpZiBsYW5ndWFnZS5sb3dlcigpID09ICJkZSI6DQogICAgICAgICAgICAgICAgICAgICAgICBwcmludChmIlxuRGFzIGlzdCBkaWUgbmV1c3RlIHZlcnNpb24gaW0gbW9tZW50LlxuIikNCg0KICAgICAgICAgICAgICAgICAgICBlbHNlOg0KICAgICAgICAgICAgICAgICAgICAgICAgcHJpbnQoZiJcblRoZSB2ZXJzaW9uIGlzIHRoZSBsYXRlc3QgdmVyc2lvbiBhdCB0aGUgbW9tZW50LlxuIikNCg0KICAgICAgICAgICAgICAgIGVsc2U6DQogICAgICAgICAgICAgICAgICAgIGlmIGxhbmd1YWdlLmxvd2VyKCkgPT0gImVuIjoNCiAgICAgICAgICAgICAgICAgICAgICAgIHByaW50KGYiXG5VTktOT1dOIFZFUlNJT04uXG4iKQ0KDQogICAgICAgICAgICAgICAgICAgIGlmIGxhbmd1YWdlLmxvd2VyKCkgPT0gImRlIjoNCiAgICAgICAgICAgICAgICAgICAgICAgIHByaW50KGYiXG5VTkJFS0FOTlRFIFZFUlNJT05cbiIpDQogICAgICAgICAgICAgICAgICAgIA0KICAgICAgICAgICAgICAgICAgICBlbHNlOg0KICAgICAgICAgICAgICAgICAgICAgICAgcHJpbnQoZiJcblVOS05PV04gVkVSU0lPTi5cbiIpDQogICAgICAgICAgICAgICAgDQogICAgICAgICAgICAgICAgcmV0dXJuDQogICAgICAgIA0KICAgICAgICBpZiByZWxlYXNlPT0iZmFsc2UiOg0KICAgICAgICAgICAgdXJsPSJodHRwczovL3d3dy5kcm9wYm94LmNvbS9zL2E1d2M3b29uNjhuejlpby92ZXJzaW9uLWJldGEudHh0P2RsPTEiDQogICAgICAgICAgICBuZXdfdmVyc2lvbj1yZXF1ZXN0cy5nZXQodXJsLCBhbGxvd19yZWRpcmVjdHM9VHJ1ZSkNCiAgICAgICAgICAgIG9wZW4oImJldGEtdmVyc2lvbi50eHQiLCAid2IiKS53cml0ZShuZXdfdmVyc2lvbi5jb250ZW50KQ0KICAgICAgICAgICAgDQogICAgICAgICAgICBpZiBuZXdfdmVyc2lvbj5idmVyc2lvbjoNCiAgICAgICAgICAgICAgICBpZiBsYW5ndWFnZS5sb3dlcigpID09ICJlbiI6DQogICAgICAgICAgICAgICAgICAgICAgICBwcmludChmIlxuVGhlcmUgaXMgYW4gbmV3IGJldGEgdmVyc2lvbjoge25ld192ZXJzaW9ufVxuVGhlcmUgaXMgZG93bmxvYWQgdGhlIGxpbms64oaTXG57bGlua31cbiIpDQoNCiAgICAgICAgICAgICAgICBpZiBsYW5ndWFnZS5sb3dlcigpID09ICJkZSI6DQogICAgICAgICAgICAgICAgICAgIHByaW50KGYiXG5EYSBpc3QgZWluZSBuZXVlIGJldGEgdmVyc2lvbjoge25ld192ZXJzaW9ufVxuRGEgaXN0IGRlciBsaW5rIHp1bSBoZXJ1bnRlcmxhZGVuOuKGk1xue2xpbmt9XG4iKQ0KDQogICAgICAgICAgICAgICAgZWxzZToNCiAgICAgICAgICAgICAgICAgICAgcHJpbnQoZiJcblRoZXJlIGlzIGFuIG5ldyBiZXRhIHZlcnNpb246IHtuZXdfdmVyc2lvbn1cblRoZXJlIGlzIHRoZSBkb3dubG9hZCBsaW5rOuKGk1xue2xpbmt9XG4iKQ0KICAgICAgICAgICAgDQogICAgICAgICAgICBpZiBuZXdfdmVyc2lvbj09YnZlcnNpb246DQogICAgICAgICAgICAgICAgaWYgbGFuZ3VhZ2UubG93ZXIoKSA9PSAiZW4iOg0KICAgICAgICAgICAgICAgICAgICAgICAgcHJpbnQoZiJcblRoZSB2ZXJzaW9uIGlzIHRoZSBsYXRlc3QgYmV0YSB2ZXJzaW9uIGF0IHRoZSBtb21lbnQuXG4iKQ0KDQogICAgICAgICAgICAgICAgaWYgbGFuZ3VhZ2UubG93ZXIoKSA9PSAiZGUiOg0KICAgICAgICAgICAgICAgICAgICBwcmludChmIlxuRGFzIGlzdCBkaWUgbmV1c3RlIGJldGEgdmVyc2lvbiBpbSBtb21lbnQuXG4iKQ0KDQogICAgICAgICAgICAgICAgZWxzZToNCiAgICAgICAgICAgICAgICAgICAgcHJpbnQoZiJcblRoZSB2ZXJzaW9uIGlzIHRoZSBsYXRlc3QgdmVyc2lvbiBhdCB0aGUgbW9tZW50LlxuIikNCiAgICAgICAgICAgIA0KICAgICAgICAgICAgZWxzZToNCiAgICAgICAgICAgICAgICBpZiBsYW5ndWFnZS5sb3dlcigpID09ICJlbiI6DQogICAgICAgICAgICAgICAgICAgIHByaW50KGYiXG5VTktOT1dOIEJFVEEgVkVSU0lPTlxuIikNCg0KICAgICAgICAgICAgICAgIGlmIGxhbmd1YWdlLmxvd2VyKCkgPT0gImRlIjoNCiAgICAgICAgICAgICAgICAgICAgcHJpbnQoZiJcblVOQkVLQU5OVEUgQkVUQSBWRVJTSU9OXG4iKQ0KICAgICAgICAgICAgICAgICAgICANCiAgICAgICAgICAgICAgICBlbHNlOg0KICAgICAgICAgICAgICAgICAgICBwcmludChmIlxuVU5LTk9XTiBCRVRBIFZFUlNJT05cbiIpDQogICAgICAgICAgICByZXR1cm4NCg0KICAgICNObyBpbnRlcm5ldCBDb25uZWN0aW9uIGZvdW5kLCB1cGRhdGUgQ2hlY2tpbmcgY2FuJ3QgYmUgZG9uZS4NCiAgICBleGNlcHQgcmVxdWVzdHMuZXhjZXB0aW9ucy5Db25uZWN0aW9uRXJyb3I6ICN0aGFua3MgVGl6enlTYXVydXMgZm9yIGhlbHBpbmcgbWUgZ2V0dGluZyB0aGF0IGNhdGNoLiA6KQ0KICAgICAgICANCiAgICAgICAgaWYgbGFuZ3VhZ2U9PSJlbiI6DQogICAgICAgICAgICBwcmludChmIlxuQ3VycmVudGx5IHRoZXJlIGlzIG5vIGludGVybmV0LCBUcnkgY2hlY2tpbmcgZm9yIHVwZGF0ZXMgbGF0ZXIgd2hlbiBhIGludGVybmV0IGNvbm5lY3Rpb24gZXhpc3RzL2lzIHN0YWJsZS5cbiIpDQogICAgICAgICAgICANCiAgICAgICAgaWYgbGFuZ3VhZ2U9PSJkZSI6DQogICAgICAgICAgICBwcmludChmIlxuTW9tZW50YW4gaXN0IGRhIGtlaW4gaW50ZXJuZXQsIFZlcnN1Y2ggZXMgc3DDpHRlciBub2NobWFsIHdlbm4gZGllIEludGVybmV0dmVyYmluZHVuZyBkYSBpc3QvU3RhYmlsIGlzdC5cbiIpDQogICAgICAgICAgICANCiAgICAgICAgZWxzZToNCiAgICAgICAgICAgIHByaW50KGYiXG5DdXJyZW50bHkgdGhlcmUgaXMgbm8gaW50ZXJuZXQsIFRyeSBjaGVja2luZyBmb3IgdXBkYXRlcyBsYXRlciB3aGVuIGEgaW50ZXJuZXQgY29ubmVjdGlvbiBleGlzdHMvaXMgc3RhYmxlLlxuIikNCiAgICAgICAgICAgIA0KICAgICAgICByZXR1cm4NCg0KZGVmIFRlc3QoKToNCiAgICB3aGlsZSBUcnVlOg0KICAgICAgICBsYW5ndWFnZT1pbnB1dCgiREUvRU4iKS5sb3dlcigpDQogICAgICAgIHJlbGVhc2U9aW5wdXQoIlRSVUUvRkFMU0UiKS5sb3dlcigpDQogICAgICAgIHVwZGF0ZShyZWxlYXNlLCBsYW5ndWFnZSkNCg0KI1Rlc3QoKQ=="
        out=base64.b64decode(data)
        with open("converter.py", "w") as save:
            save.write(out)

startup()