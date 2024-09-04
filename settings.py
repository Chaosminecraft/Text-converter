import locale
from logger import log_info, log_error, log_warn, log_system
import json
from random import randint

#These settings are needed:
#logg settings
#language settings
#ad settings
#migrating old settings

class variables:
    language=""
    ad=""
    prompt=""
    logg=""
    upcheck=""

def settings_init(name, host):
    system_language=locale.getdefaultlocale()[:1]
    system_language=str(system_language).lower()[2:7]
    print(system_language)

    try:
        if system_language=="de_de":
            language="de"
        elif system_language=="en_en" or system_language=="en_us":
            language="en"
    except:
        print(f"\nNo compatible language found, Defaulted to English.")
        language="en"
    
    ad=True

    prompt="{name}@{host}:~$ "
    for r in (("{name}", name), ("{host}", host)):
        prompt=prompt.replace(*r)
    
    upcheck=True

    logg=True

    settings={
        "languane":language,
        "ad":ad,
        "prompt":prompt,
        "update":upcheck,
        "logging":logg
    }

    with open("settings.json", "w") as save:
        json.dump(settings, save)
    return

def change_settings(**kwargs):
    try:
        try:
            with open("settings.json", "r") as file:
                settings_file=json.load(file)
        except FileNotFoundError:
            settings_init()
            with open("settings.json") as file:
                settings_file=json.load(file)

        variables.language=settings_file.get("language")
        variables.ad=settings_file.get("ad")
        variables.prompt=settings_file.get("prompt")
        variables.upcheck=settings_file.get("update")
        variables.logg=settings_file.get("logging")

        if kwargs['target'] == "language":
            print("language Settings")
            if kwargs["language"] == "de":
                while True:
                    text=input("Welche Sprache? Da ist EN und DE: ").lower()
                    
                    if text=="en" or text=="de":
                        variables.language=text
                        break
                    
                    else:
                        print("Nope, Das ist Invalide!")
                    
            elif kwargs["language"] == "en":
                while True:
                    text=input("What language? There is EN and DE: ").lower()
                    
                    if text=="en" or text=="de":
                        variables.language=text
                        break
                    
                    else:
                        if variables.language=="en":
                            print("Nope, that is sadly invalid!")
                        
                        elif variables.language=="de":
                            print("Nope, Das ist nicht Valide!")

                        else:
                            print("Nope, that is sadly invalid!")
            else:
                while True:
                    text=input("What language? There is EN and DE: ").lower()
                    
                    if text=="en" or text=="de":
                        variables.language=text
                        break
                    
                    else:
                        print("Nope, that is sadly invalid!")
        
        elif kwargs['target'] == "ad":
            print("Ad Settings")
            if kwargs["language"]=="en":
                while True:
                    print(f"Do you wanna see the ad? {variables.ad} is the current setting.")
                    text=input("Yes or No? ").lower()
                    if text=="yes":
                        variables.ad=True
                        break
                    
                    elif text=="no":
                        variables.ad=False
                    
                    else:
                        print("Nope, that is sadly invalid!")
                
            elif kwargs["language"]=="de":
                while True:
                    print(f"Willst du die werbung sehen?? {variables.ad} ist die Aktuelle einstellung.")
                    text=input("Yes or No? ").lower()
                    if text=="ja":
                        variables.ad=True
                        break
                    elif text=="nein":
                        variables.ad=False
                        break
                    
                    else:
                        print("Nope, Das ist leider nicht valide.")
            
            else:
                while True:
                    print(f"Do you wanna see the ad? {variables.ad} is the current setting.")
                    text=input("Yes or No? ").lower()
                    if text=="yes":
                        variables.ad=True
                        break

                    elif text=="no":
                        variables.ad=False
                        break

                    else:
                        print("Nope, that is sadly invalid!")
        
        elif kwargs['target']=="prompt":
            print("Prompt Settings")
            if kwargs["language"]=="en":
                print("What style do you want? You Can pull the {host} to pull the pc name, you can do {name} to get the name of the user on the PC, with {system} you can pull the System (not always accurate.)")
                print("there are 3 presets:\n1. linux\n2. windows\n3. macos")
            
            elif kwargs["language"]=="de":
                print("Was für einen style möchtest du? Du kannst mit {host} den PC namen nehmen, mit {name} kann man den aktuellen nutzernamen nutzen, und mit {system} kann man den namen vom system nehmen.")
                print(f"Da sind auch 3 presets:\n1. linux\n2. windows\n3. macos")
            
            if kwargs["language"]=="en":
                variables.prompt=input("What prompt look? ")
            
            elif kwargs["language"]=="de":
                variables.prompt=input("Was für ein Prompt? ")
            
            else:
                variables.prompt=input("What prompt look? ")
            
            if variables.prompt.lower()=="linux":
                variables.prompt="{name}@{host}:~$ "
            
            elif variables.prompt.lower()=="windows":
                variables.prompt="C:\\user\\{name}> "
            
            elif variables.prompt.lower()=="macos":
                variables.prompt="{name}@{host} ~ % "
            
            for r in (("{name}", kwargs['name']), ("{host}", kwargs['pc']), ("{system}", kwargs['system'])):
                variables.prompt=variables.prompt.replace(*r)
        
        if kwargs['target']=="logging":
            print("Logg Settings")
            if variables.language=="en":
                print("Do you want that non critical stuff is not logged anymore? (Critical was meant with if a crash occured.)")
                text=input("Yes or No? ").lower()
                if text=="yes":
                    variables.logg=True
                
                else:
                    variables.logg=False
            
            elif variables.language=="de":
                print("Willst du das nicht kritische sachen geloggt werden? (Kiritische sachen sind wie ein Crash.)")
                text=input("Ja oder Nein? ")
                if text=="ja":
                    variables.logg=True
                
                else:
                    variables.logg=False
            
            else:
                print("Do you want that non critical stuff is not logged anymore? (Critical was meant with if a crash occured.)")
                text=input("Yes or No? ").lower()
                if text=="yes":
                    variables.logg=True
                
                else:
                    variables.logg=False
        
        elif kwargs['target']=="update":
            print("update settings")

        settings={
            "language":variables.language,
            "ad":variables.ad,
            "prompt":variables.prompt,
            "update":variables.upcheck,
            "logging":variables.logg
        }

        with open("settings.json", "w") as file:
            json.dump(settings, file)
        
        return variables.prompt, variables.language, variables.ad, variables.upcheck
    
    except KeyboardInterrupt:
        print()
        return

if __name__=="__main__":
    print("Please don't run that file.")