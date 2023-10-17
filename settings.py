import locale as loc
from logger import *
import json, re

#These settings are needed:
#logg settings
#language settings
#ad settings
#migrating old settings

def migrate_settings():
    with open("ad setting.txt", "r") as file:
        ad=file.read()
    
    if ad=="true":
        ad=True
    if ad=="false":
        ad=False

    with open("lang.txt", "r") as file:
        language=file.read()

    with open("logg.txt", "r") as file:
        logg=file.read()
    
    if logg=="true":
        logg=True
    if logg=="false":
        logg=False
    
    upcheck=True

    prompt="W.I.P"

    settings={
        "lang":language,
        "ad":ad,
        "prompt":prompt,
        "update":upcheck,
        "logging":logg
    }
    with open("settings.json", "w") as save:
        json.dump(settings, save)
    return language, ad, logg, prompt, upcheck

def settings_init(name, host):
    get_lang=loc.getdefaultlocale()[:1]
    systemlang=str(get_lang)
    try:
        if systemlang.lower()=="('de_de',)":
            language="de"
        if systemlang.lower()=="('en_en',)":
            language="en"
    except:
        print(f"\nNo compatible language automatically found, Chose English.")
        language="en"
    
    ad=True

    prompt="{name}@{host}:~$ "
    for r in (("{name}", name), ("{host}", host)):
        prompt=prompt.replace(*r)

    upcheck=True

    logg=True

    settings={
        "lang":language,
        "ad":ad,
        "prompt":prompt,
        "update":upcheck,
        "logging":logg
    }

    with open("settings.json", "w") as save:
        json.dump(settings, save)
    return

def change_settings(language, name, host, system, setting):
    #print(language, name, host, system, setting)
    try:
        with open("settings.json", "r") as file:
            settings=json.load(file)
        
        language=settings.get("lang")
        ad=settings.get("ad")
        prompt=settings.get("prompt")
        upcheck=settings.get("update")
        logg=settings.get("logging")


        if setting=="ad":
            if language=="en":
                print("Do you wanna see the ad on every Startup and reboot?")
                answer=input("Yes or No? ")
            
            if language=="de":
                print("Willst du die Werbung sehen wenn fu es startest oder neu startest")
                answer=input("Ja oder Nein? ")

            if answer.lower()=="no" or answer.lower()=="nein":
                ad=False
            if answer.lower()=="yes" or answer.lower()=="ja":
                ad=True

        if setting=="language":
            if language=="en":
                print("There is currently only German and English, What do you choose?")
                answer=input("German or English? ").lower()
            
            if language=="de":
                print("Da ist momentan nur Deutsch und Englisch, was wählst du? ")
                answer=input("Deutsch oder Englisch? ").lower()
            
            if answer.lower()=="german" or answer.lower()=="deutsch":
                language="de"
            if answer.lower()=="english" or answer.lower()=="englisch":
                language="en"
        
        if setting=="promptinput":
            prompt=input("What prompt look? ")
            if prompt.lower()=="linux":
                prompt=f"{name}@{host}:~$ "
            if prompt.lower()=="windows":
                prompt=f"C:\\user\\{name}> "
            
            for r in (("{name}", name), ("{host}", host), ("{system}", system)):
                prompt=prompt.replace(*r)
        
        if setting=="update":
            if language=="en":
                print("Do youn wanna Check for updates?")
                answer=input("Yes or No? ") 
            
            if language=="de":
                print("Willst du nach updates schauen?")
                answer=input("Ja oder Nein? ").lower()

        if setting=="logging":
            if language=="en":
                print("Should the Stuff be logged? If not, only warnings and errors are gonna be logged.")
                answer=input("Yes or No? ")
                
            if language=="de":
                print("Soll logging angeschalten werden? Wenn nicht, dann werden nur warnungen und fehler geloggt.")
                answer=input("Ja oder Nein? ").lower()
        
        settings={
            "lang":language,
            "ad":ad,
            "prompt":prompt,
            "update":upcheck,
            "logging":logg
        }

        with open("settings.json", "w") as file:
            json.dump(settings, file)
        
        return
        
    except KeyboardInterrupt:
        print()
        return

def helper(language, logg):
    with open("settings.json", "r") as file:
        settings=json.load(file)
    
    ad=settings.get("ad")
    text="helpsite printed"
    if language == "en":
        print(f"""\nThere are the Conversion methods:\n
        The command phex Brings you to the Pseudo Hex converter.
        The command pbin Brings you to the Pseudo Binary converter.
        The connamd legacy pbin Brings you to the Legacy version of the Pseudo Binary converter
        The command hex Brings you to the Hex converter.
        The command bin Brings you to the Binary Converter.
        The command ascii Brings you to the ascii converter.
        The command leetcode is permanently removed!
        The command brainfuck Brings you to the Brainfuck converter.
        The command base64 Brings you to the base64 converter.
        \nThere are more General commands:\n
        The command Language Settings changes the language.
        The command Ad Settings Changes if you wanna see the ad. (not getting paid for it.)
        The command Prompt Settings changes the prompt (Not yet known if it fully works on all systems.)
        The command Logg Settings changes if you want the input to appear in the logg file. (System type events will always be logged by default for diagnostics/startup)
        """)
        if ad=="true":
            print("The Command Get Game makes the While True: Learn() game stores where you can buy the game.")
        print()
        log_info(text, logg)
                        
    if language == "de":
        print(f"""\nDa sind die Converter Methoden:\n
        Der Command phex Bringt dich zum Pseudo Hex converter.
        Der Command pbinary Bringt dich zum Pseudo Binary converter.
        Der Command thex Bringt dich zum Hex converter.
        Der Command tbin Bringt dich zum Binary converter
        Der command ascii Bringt you to the ascii converter.
        Der command leetcode ist permanent entfernt!
        Der command brainfuck Bringt you to the Brainfuck converter.
        Der command base64 Bringt you to the base64 converter.
        \nDa sind mehr Generelle Commands:\n
        Der command help Zeigt das hier.
        Der command ad settings fragt ob du die werbung sehen willst.
        Der command clear screen macht das kein text mer von vorhin gezeigt wird.
        Der command language settings ändert die Sprache.
        Der command reset startet das Program neu.
        Der Commend Language zeigt die aktuelle sprache in den einstellungen.""")
        if ad=="true":
            print("Der Command Get Game zeigt dir was für stores für das Spiel while True: learn() kaufen kann.")
        print()
        log_info(text, logg)
    
    return