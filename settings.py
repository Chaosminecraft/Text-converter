import locale, json

#The function that makes the Settings file
def settings_init(**kwargs):
    system_language=str(locale.getlocale()[:1]).lower()[2:7] #That is to fetch the language of the system to set the language in the settings file.
    
    if system_language=="de_de":
        language="de" #If the language ended up being de_de
    
    else:
        language="en" #Anything else, and it's English.
    
    ad=True      #the advert setting (defaulting to true)
    logg=True    #the logg setting (defaulting to true)
    upcheck=True #the update check setting (Defaulting to true)

    prompt="{name}@{host}:~$ "
    for r in (("{name}", kwargs.get("name")), ("{host}", kwargs.get("host"))):
        prompt=prompt.replace(*r)
    
    gui=False #starting the project in CLI or GUI

    settings={
        "language":language,
        "advert":ad,
        "prompt":prompt,
        "update-check":upcheck,
        "logging":logg,
        "gui":gui
    }
    
    with open("settings.json", "w") as save:
        json.dump(settings, save)
    
    return prompt, language, ad, upcheck

def change_settings(config, sysinf, **kwargs):
    try:
        try:
            with open("settings.json", "r") as load:
                settings_file=json.load(load)
        except FileNotFoundError:
            settings_init(name=kwargs["name"], host=kwargs["host"])
            with open("settings.json", "r") as load:
                settings_file=json.load(load)
        
        language=settings_file.get("language")
        ad=settings_file.get("advert")
        prompt=settings_file.get("prompt")
        upcheck=settings_file.get("update-check")
        logg=settings_file.get("logging")
        gui=settings_file.get("gui")
        
        if kwargs["option"] == "language":
            while True:
                if config.language=="de":
                    text=input("Welche Sprache? (DE/EN) ").lower()
                else:
                    text=input("What language? (DE/EN) ").lower()
            
                if text=="en" or text=="de":
                    config.language=text
                    break

                else:
                    if config.language=="de":
                        print("Nope, nur DE oder EN.")
                    else:
                        print("Nope, Only DE or EN")
        
        elif kwargs["option"]=="ad":
            while True:
                if config.language=="de":
                    text=input("Willst du die Werbung sehen? (J/N) ").lower()
                else:
                    text=input("Do you wanna see the ad? (Y/N) ").lower()
                
                if text=="y" or text=="yes" or text=="j" or text=="ja":
                    ad=True
                    break
                
                elif text=="n" or text=="no" or text=="nein":
                    ad=False
                    break
                
                else:
                    if config.language=="de":
                        print("Nur j oder n.")
                    else:
                        print("Only y or n.")
        
        elif kwargs["option"]=="prompt":
            if config.language=="de":
                print("Was für ein prompt style möchtest du? {host} ist der PC name, {name} istder nutzername, {system} ist der name vom betriebssystem.")
                print("Es gibt 3 prompt presets:\n1. Linux\n2. Windows\n3. macos\n4. templeos")
                text=input("Was für ein prompt? ")
            else:
                print("What prompt style do you want? {host} is the PC name, {name} is the username, {system} is the name of the Operating System.")
                print("There are 3 prompt presets:\n1. Linux\n2. Windows\n3. macos\n4. templeos")
                text=input("What prompt look? ")
            
            if text=="Linux" or text=="1":
                prompt="{name}@{host}:~$ "

            elif text=="Windows" or text=="2":
                prompt="C:\\Users\\{name}> "

            elif text=="macos" or text=="3":
                prompt="{name}@{host} ~ % "

            elif text=="templeos" or text=="4":
                prompt="C:/Home "
            
            for r in (("{name}", config.name), ("{host}", config.host), ("{system}", sysinf.system_desc)):
                prompt=prompt.replace(*r)
        
        elif kwargs["option"]=="logg":
            while True:
                if config.language=="de":
                    text=input("Willst du nicht kritische sachen loggen? (J/N) ").lower()
                else:
                    text=input("Do you wanna log non critical stuff? (Y/N) ").lower()
            
                if text=="y" or text=="yes" or text=="j" or text=="ja":
                    logg=True
                    break

                elif text=="n" or text=="no" or text=="nein":
                    logg=False
                    break

                else:
                    if config.language=="de":
                        print("Nur j oder n")
                    else:
                        print("only y or n")
        
        elif kwargs["option"]=="update":
            while True:
                if config.language=="de":
                    text=input("Willst du nach updates checken? (J/N) ").lower()
                else:
                    text=input("Do you wanna check for updates? (Y/N) ").lower()
                
                if text=="j" or text=="ja" or text=="y" or text=="yes":
                    upcheck=True
                    break

                elif text=="n" or text=="no" or text=="nein":
                    upcheck=False
                    break

                else:
                    if config.language=="de":
                        print("Nur j oder n")
                    else:
                        print("only y or n")

        elif kwargs["option"]=="gui":
            if config.language=="de":
                text=input("Willst du beim start die CLI version oder GUI version verwenden? (CLI/GUI) ").lower()
            else:
                text=input("Do you wanna use the CLI version or GUI Version at the start? (CLI/GUI) ").lower()
            
            if text=="gui":
                gui=True

            elif text=="cli":
                gui=False
            
            else:
                if config.language=="de":
                    print("Nur CLI oder GUI")
                else:
                    print("Only CLI or GUI")
        
        settings_file={
        "language":language,
        "advert":ad,
        "prompt":prompt,
        "update-check":upcheck,
        "logging":logg,
        "gui":gui
    }

    except KeyboardInterrupt:
        print()
        return

def gui_settings():
    tmp="" #pls add the GUI settings functionality while adding the GUI code.

if __name__=="__main__":
    input("Please don't open that file on it's own. This is a module!")
    exit()