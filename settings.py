import locale, json
from tkinter import *

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
    for r in (("{name}", kwargs["name"]), ("{host}", kwargs["host"])):
        prompt=prompt.replace(*r)
    
    gui=False      #starting the project in CLI or GUI
    theme="bright" #the default theme of gui

    settings={
        "language":language,
        "advert":ad,
        "prompt":prompt,
        "update-check":upcheck,
        "logging":logg,
        "gui":gui,
        "theme":theme
    }
    
    with open("settings.json", "w") as save:
        json.dump(settings, save)
    
    return prompt, language, ad, upcheck, logg, gui, theme

def change_settings(config, sysinf, **kwargs):
    try:
        try:
            with open("settings.json", "r") as load:
                settings_file=json.load(load)
        except FileNotFoundError:
            settings_init(name=config.name, host=config.host)
            with open("settings.json", "r") as load:
                settings_file=json.load(load)
        
        language=settings_file.get("language")
        ad=settings_file.get("advert")
        prompt=settings_file.get("prompt")
        upcheck=settings_file.get("update-check")
        logg=settings_file.get("logging")
        gui=settings_file.get("gui")
        theme=settings_file.get("theme")
        
        if kwargs["option"] == "language":
            while True:
                if config.language=="de":
                    text=input("Welche Sprache? (DE/EN) ").lower()
                else:
                    text=input("What language? (DE/EN) ").lower()
            
                if text=="en" or text=="de":
                    language=text
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
        
        elif kwargs["option"]=="logging":
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
        
        elif kwargs["option"]=="theme":
            while True:
                if config.language=="de":
                    text=input("Willst du die Bright theme oder Dark theme benutzen? (bright/dark) ").lower()
                else:
                    text=input("Do you wanna use the Bright theme or Dark theme? (bright/dark) ").lower()

                if text=="bright":
                    theme="bright"
                    break

                elif text=="dark":
                    theme="dark"
                    break

                else:
                    if config.language=="de":
                        print("Ne, es gibt nur bright oder dark im moment, Custom themes werden bald dazu kommen.")
                    else:
                        print("nope, there is only bright or dark in the moment, Custom themes are soon there.")
        
        settings_file={
        "language":language,
        "advert":ad,
        "prompt":prompt,
        "update-check":upcheck,
        "logging":logg,
        "gui":gui,
        "theme":theme
    }
        
        with open("settings.json", "w") as save:
            json.dump(settings_file, save)
        
        return prompt, language, ad, upcheck, logg, gui, theme

    except KeyboardInterrupt:
        print()
        return

class variables:
    log_var=""
    language_var=""
    update_var=""
    gui_var=""
    theme_var=""

def gui_settings(GuiConfig, config, theme):
    if GuiConfig.options_window_count == 0:
        GuiConfig.options_window_count+=1

        settingsgui=Toplevel()
        settingsgui.title("Settings")
        settingsgui.geometry("400x300")
        settingsgui.resizable(width=False, height=False)

        def on_close():
            #print("I'M USEFUL!!!!") #for some goddamn debugging if that shi stops working.
            GuiConfig.options_window_count=0
            settingsgui.destroy()
        
        settingsgui.protocol("WM_DELETE_WINDOW", on_close)

        variables.log_var=IntVar(value=1 if config.logg else 0)
        print(variables.log_var.get())
        log_checkbox=Checkbutton(settingsgui, text="Activate non critical logging?", variable=variables.log_var)
        log_checkbox.pack()

        variables.update_var=IntVar(value=1 if config.upcheck else 0)

        update_checkbox=Checkbutton(settingsgui, text="Check for updates?", variable=variables.update_var)
        update_checkbox.pack()

        variables.gui_var=IntVar(value=1 if config.gui else 0)

        gui_checkbox=Checkbutton(settingsgui, text="Start the GUI on startup", variable=variables.gui_var)
        gui_checkbox.pack()

        language_label=Label(settingsgui, text="Language setting:")
        language_label.pack()

        variables.language_var=StringVar(value=config.language)

        language_radio_de = Radiobutton(settingsgui, text="Deutsch", variable=variables.language_var, value="de")
        language_radio_de.pack()

        language_radio_en = Radiobutton(settingsgui, text="English", variable=variables.language_var, value="en")
        language_radio_en.pack()

        variables.theme_var=StringVar(value=config.theme)
        theme_bright_radio=Radiobutton(settingsgui, text="Bright", variable=variables.theme_var, value="light", command=lambda:change_theme(GuiConfig, theme, variables.theme_var.get()))
        theme_bright_radio.pack()
        theme_dark_radio=Radiobutton(settingsgui, text="Dark", variable=variables.theme_var, value="dark", command=lambda:change_theme(GuiConfig, theme, variables.theme_var.get()))
        theme_dark_radio.pack()

        save_butt=Button(settingsgui, text="Save", command=lambda:save_settings(GuiConfig, config, theme))
        save_butt.pack()
        load_butt=Button(settingsgui, text="reload", command=lambda:load_settings(GuiConfig, config, theme))
        load_butt.pack()
    else:
        return

def change_theme(GuiConfig, theme, theme_var):
    temp=""

def save_settings(GuiConfig, config, theme):
    if variables.update_var.get()==1:
        update_var=True
    else:
        update_var=False
    
    if variables.log_var.get()==1:
        log_var=True
    else:
        log_var=False
    
    if variables.gui_var.get()==1:
        gui_var=True
    else:
        gui_var=False
    
    settings={
        "language":variables.language_var.get(),
        "advert":config.ad,
        "prompt":config.prompt,
        "update-check":update_var,
        "logging":log_var,
        "gui":gui_var,
        "theme":variables.theme_var.get()
    }
    with open("settings.json", "w") as save:
        json.dump(settings, save)

def load_settings(GuiConfig, config, theme):
    temp=""

if __name__=="__main__":
    input("Please don't open that file on it's own. This is a module!")
    exit()