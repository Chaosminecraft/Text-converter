import locale, json
from logger import log_info, log_system
from random import randint

#these are the values:
#logg is if logging is wanted to all or Only the required to be logged
#language is for the language
#ad is for the advertisement
#prompt is for the prompt at the beginning (Other customisation options may come in the future)

class vars:
    language=""
    ad=""
    prompt=""
    upcheck=""
    logg=""
    autopwgen=""
    excluded_chars=""
    include_uppercase=""
    include_numbers=""
    include_specials=""

def settings_init(**kwargs):
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
    for r in (("{name}", kwargs["name"]), ("{host}", kwargs["host"])):
        prompt=prompt.replace(*r)
    
    autopwgen=False
    
    exclude_chars=""
    
    include_uppercase=True
    
    include_numbers=True
    
    include_specials=True
    
    settings={
        "language":language,
        "advert":ad,
        "prompt":prompt,
        "update":upcheck,
        "logging":logg,
        "autopwgen":autopwgen,
        "excludechars":exclude_chars,
        "includeuppercase":include_uppercase,
        "includenumbers":include_numbers,
        "includespecials":include_specials
        }
    
    with open("settings.json", "w") as save:
        json.dump(settings, save)
    
    return prompt, language, ad, upcheck

def change_settings(**kwargs):
    try:
        try:
            with open("settings.json", "r") as file:
                settings_file=json.load(file)
        except FileNotFoundError:
            settings_init()
            with open("settings.json") as file:
                settings_file=json.load(file)

        vars.language=settings_file.get("language")
        vars.ad=settings_file.get("ad")
        vars.prompt=settings_file.get("prompt")
        vars.upcheck=settings_file.get("update")
        vars.logg=settings_file.get("logging")
        vars.autopwgen=settings_file.get("autopwgen")
        vars.excluded_chars=settings_file.get("excludechars")
        vars.include_uppercase=settings_file.get("includeuppercase")
        vars.include_numbers=settings_file.get("includenumbers")
        vars.include_specials=settings_file.get("includespecials")

        if kwargs['target'] == "language":
            print("language Settings")
            if kwargs["language"] == "de":
                while True:
                    text=input("Welche Sprache? Da ist EN und DE: ").lower()
                    
                    if text=="en" or text=="de":
                        vars.language=text
                        break
                    
                    else:
                        print("Nope, Das ist Invalide!")
            else:
                while True:
                    text=input("What language? There is EN and DE: ").lower()
                    
                    if text=="en" or text=="de":
                        vars.language=text
                        break
                    
                    else:
                        print("Nope, that is not valid!")
        
        elif kwargs['target'] == "ad":
            if kwargs["language"]=="de":
                print(f"Willst du die werbung sehen?? {vars.ad} ist die Aktuelle einstellung.")
                while True:
                    text=input("Ja oder Nein? ").lower()
                    if text=="ja":
                        vars.ad=True
                        break
                    elif text=="nein":
                        vars.ad=False
                        break
                    
                    else:
                        print("Nope, Das ist leider nicht valide.")
            
            else:
                print(f"Do you wanna see the ad? {vars.ad} is the current setting.")
                while True:
                    text=input("Yes or No? ").lower()
                    if text=="yes":
                        vars.ad=True
                        break

                    elif text=="no":
                        vars.ad=False
                        break

                    else:
                        print("Nope, that is sadly invalid!")
        
        elif kwargs['target']=="prompt":            
            if kwargs["language"]=="de":
                print("Was für einen style möchtest du? Du kannst mit {host} den PC namen nehmen, mit {name} kann man den aktuellen nutzernamen nutzen, und mit {system} kann man den namen vom system nehmen.")
                print(f"Da sind auch 3 presets:\n1. linux\n2. windows\n3. macos")
            
            else:
                print("What style do you want? You Can pull the {host} to pull the pc name, you can do {name} to get the name of the user on the PC, with {system} you can pull the System (not always accurate.)")
                print("there are 3 presets:\n1. linux\n2. windows\n3. windows system32\n4. macos\n5. templeos")
            
            if kwargs["language"]=="de":
                vars.prompt=input("Was für ein Prompt? ")
            
            else:
                vars.prompt=input("What prompt look? ")
            
            if vars.prompt.lower()=="linux":
                vars.prompt="{name}@{host}:~$ "
            
            elif vars.prompt.lower()=="windows":
                vars.prompt="C:\\user\\{name}> "
            
            elif vars.prompt.lower()=="windows system32":
                vars.prompt="C:\\Windows\\System32> "
            
            elif vars.prompt.lower()=="macos":
                vars.prompt="{name}@{host} ~ % "
            
            elif vars.prompt.lower()=="templeos":
                vars.prompt="C:/Home"
            
            for r in (("{name}", kwargs['name']), ("{host}", kwargs['host']), ("{system}", kwargs['system'])):
                vars.prompt=vars.prompt.replace(*r)
        
        if kwargs['target']=="logging":
            if kwargs["language"]=="de":
                print("Willst du das nicht kritische sachen geloggt werden? (Kiritische sachen sind wie ein Crash.)")
                text=input("Ja oder Nein? ")
                if text=="ja":
                    vars.logg=True
                
                else:
                    vars.logg=False
            
            else:
                print("Do you want that non critical stuff is not logged anymore? (Critical was meant with if a crash occured.)")
                text=input("Yes or No? ").lower()
                if text=="yes":
                    vars.logg=True
                
                else:
                    vars.logg=False
        
        elif kwargs['target']=="update":
            if kwargs["language"]=="de":
                print("Willst du das das Program beim start nach updates schaut? ")
                while True:
                    text=input("Ja oder Nein? ").lower()
                    if text=="ja":
                        vars.upcheck=True
                        break
                    
                    elif text=="nein":
                        vars.upcheck=False
                        break
                    
                    else:
                        print("Es gibt nur Ja oder Nein.")
            
            else:
                print("Do you want that the program checks for updates at start? ")
                while True:
                    text=input("Yes or No? ").lower()
                    if text=="yes":
                        vars.upcheck=True
                        break
                    
                    elif text=="no":
                        vars.upcheck=False
                        break
                    
                    else:
                        print("There is only Yes or No.")
        
        elif kwargs['target']=="auto password":
            if kwargs["language"]=="de":
                print("Willst du das das Paswort außer länge automatisch generiert wird?")
                while True:
                    text=input("Ja oder Nein? ").lower()
                    if text=="ja":
                        vars.autopwgen=True
                        break
                    
                    elif text=="nein":
                        vars.autopwgen=False
                        break
                    
                    else:
                        print("Da ist nur Ja oder Nein.")
            
            else:
                print("Do you want that the password is automatically generated except the Length?")
                while True:
                    text=input("Yes or No? ").lower()
                    if text=="yes":
                        vars.autopwgen=True
                        break
                    
                    elif text=="no":
                        vars.autopwgen=False
                        break
                    
                    else:
                        print("there is only Yes or No.")
        
        elif kwargs['target']=="excluded chars":
            if kwargs["language"]=="de":
                print("Was für zeichen sollen ausgelassen werden wenn ein passwort generiert wird?")
                text=input("Schreib die hier hin> ")
                vars.excluded_chars=f" {text}"
            
            else:
                print("What characters do you wanna exclude when generating a password?")
                text=input("write them here> ")
                vars.excluded_chars=f" {text}"
        
        elif kwargs["target"]=="include uppercase":
            if kwargs["language"]=="de":
                print("Soll im generierten passowrt Große zeichen sein?")
                while True:
                    text=input("Ja oder Nein? ").lower()
                    if text=="ja":
                        vars.include_uppercase=True
                        break
                    
                    elif text=="nein":
                        vars.include_uppercase=False
                        break
                    
                    else:
                        print("Da ist nur Ja oder Nein.")
            
            else:
                print("Should the generated Password include uppercase?")
                while True:
                    text=input("Yes or No? ").lower()
                    if text=="yes":
                        vars.include_uppercase=True
                        break
                    
                    elif text=="no":
                        vars.include_uppercase=False
                        break
                    
                    else:
                        print("There is only Yes or No.")
        
        elif kwargs["target"]=="include numbers":
            if kwargs["language"]=="de":
                print("Willst du Zahlen im generierten passwort haben?")
                while True:
                    text=input("Ja oder Nein? ").lower()
                    if text=="ja":
                        vars.include_numbers=True
                        break
                    
                    elif text=="nein":
                        vars.include_numbers=False
                        break
                    
                    else:
                        print("Da ist nur Ja oder Nein.")
            
            else:
                print("Do you want to have numbers in the generated Password?")
                while True:
                    text=input("Yes or No? ").lower()
                    if text=="yes":
                        vars.include_numbers=True
                        break
                    
                    elif text=="no":
                        vars.include_numbers=False
                        break
                    
                    else:
                        print("There is only Yes or No.")
        
        elif kwargs["target"]=="include specials":
            if kwargs["language"]=="de":
                print("Willst du Speizalcharactere im passwort haben? (Zum Beispiel: @%!$)")
                while True:
                    text=input("Ja oder Nein? ").lower()
                    if text=="ja":
                        vars.include_specials=True
                        break
                    
                    elif text=="nein":
                        vars.include_specials=False
                        break
                    
                    else:
                        print("Da ist nur Ja oder Nein.")
            
            else:
                print("Do you want Special Characters in your password? (aka: @%!$)")
                while True:
                    text=input("Yes or No? ").lower()
                    if text=="yes":
                        vars.include_specials=True
                        break
                    
                    elif text=="no":
                        vars.include_specials=False
                        break
                    
                    else:
                        print("There is only Yes or No.")

        settings={
            "language":vars.language,
            "advert":vars.ad,
            "prompt":vars.prompt,
            "update":vars.upcheck,
            "logging":vars.logg,
            "autopwgen":vars.autopwgen,
            "excludechars":vars.excluded_chars,
            "includeuppercase":vars.include_uppercase,
            "includenumbers":vars.include_numbers,
            "includespecials":vars.include_specials
        }

        with open("settings.json", "w") as file:
            json.dump(settings, file)
        
        return vars.prompt, vars.language, vars.ad, vars.upcheck, vars.logg, vars.autopwgen, vars.excluded_chars, vars.include_uppercase, vars.include_numbers, vars.include_specials
    
    except KeyboardInterrupt:
        print()
        return

if __name__=="__main__":
    print("Please don't run that file on it's own.")