import locale
from logger import log_info, log_error, log_warn, log_system
import json

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

        if kwargs['settings'] == "lang":
            print("I RAN")
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
                        print("Nope, that is sadly invalid!")
            
            else:
                while True:
                    text=input("What language? There is EN and DE: ").lower()
                    
                    if text=="en" or text=="de":
                        variables.language=text
                        break
                    
                    else:
                        print("Nope, that is sadly invalid!")
            
        
        if kwargs['settings'] == "prompt":
            if kwargs["language"] == "en":
                variables.prompt=input("What prompt look? ")
                if variables.prompt.lower()=="linux":
                    variables.prompt=f"{kwargs["name"]}@{kwargs["pc"]}:~$ "
                if variables.prompt.lower()=="windows":
                    variables.prompt=f"C:\\user\\{kwargs["name"]}> "
                
                for r in (("{name}", kwargs["name"]), ("{host}", kwargs["pc"]), ("{system}", kwargs["system"])):
                    variables.prompt=variables.prompt.replace(*r)

            elif kwargs["language"] == "de":
                variables.prompt=input("What prompt look? ")
                if variables.prompt.lower()=="linux":
                    variables.prompt=f"{kwargs["name"]}@{kwargs["pc"]}:~$ "
                if variables.prompt.lower()=="windows":
                    variables.prompt=f"C:\\user\\{kwargs["name"]}> "
                
                for r in (("{name}", kwargs["name"]), ("{host}", kwargs["pc"]), ("{system}", kwargs["system"])):
                    variables.prompt=variables.prompt.replace(*r)
        
        elif kwargs["settings"] == "ad":
            if kwargs["language"] == "en":
                print("AYO language time!")
            elif kwargs["language"] == "de":
                print("HALLOOOOOOOOOOOOOOO")
        
        print(variables.language)

        settings={
            "language":variables.language,
            "ad":variables.ad,
            "prompt":variables.prompt,
            "update":variables.upcheck,
            "logging":variables.logg
        }

        with open("settings.json", "w") as file:
            json.dump(settings, file)
        
        return
    
    except KeyboardInterrupt:
        print()
        return