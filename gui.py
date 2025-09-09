import ctypes, threading, datetime, time, traceback
from tkinter import *

class modules:
    logg_module=True

try:
    from converter import parse_input
except ImportError:
    result=ctypes.windll.user32.MessageBoxW(0, "The Converter module is not found, Please download the code again, I can maybe in some time make that it isn't an issue. Do you wanna contiue?", "Woops, Import error!", 1)
    if result==2:
        exit()

try:
    from settings import gui_settings
except ImportError:
    result=ctypes.windll.user32.MessageBoxW(0, "The Settigns module is not found, Please download the code again, I can maybe in some time make that it isn't an issue. Do you wanna contiue?", "Woops, Import error!", 1)
    if result==2:
        exit()

try:
    from logger import log_error
except ImportError:
    print("The module is missing. Logging on GUI without the module is not possible right now.")
    modules.logg_module=False

class GuiConfig:
    window=""
    operator=""
    convert=""
    deconvert=""
    optionsvar=""
    options_window_count=0
    converted="Something went wrong, Fix it Chaosminecraft!!"
    isexit=False
    stop_event=""

class theme:
    deconvert_msg=""
    convert_msg=""
    convert_var=""
    deconvert_var=""
    convert_check=""
    deconvert_check=""
    convert_butt=""
    settings_butt=""
    exit_butt=""
    options=""
    show_last_convert_butt=""


def cli_to_gui(config, sysinf, version, backupfunc):
    try:
        GuiConfig.window=Tk()
        GuiConfig.window.config(bg="#EFEFEF")
        GuiConfig.window.title("Text Converter V3.0 UI Preview [W.I.P]")
        GuiConfig.window.geometry("600x500")
        GuiConfig.window.resizable(width=False, height=False)
        GuiConfig.window.attributes("-topmost", True)

        def on_close():
            #print("I'M USEFUL!!!!") #for some goddamn debugging if that shi stops working.
            ui_exit(config)

        GuiConfig.window.protocol("WM_DELETE_WINDOW", on_close)

        if config.language=="en":
            theme.deconvert_msg=Label(GuiConfig.window, text="Text to deconvert:", padx=5, pady=5)
            theme.deconvert_msg.place(x=160, y=0)

            theme.convert_msg=Label(GuiConfig.window, text="Text to convert:", padx=5, pady=5)
            theme.convert_msg.place(x=160, y=35)

            theme.deconvert_var=Entry(GuiConfig.window, width=50)
            theme.deconvert_var.place(x=160, y=20)

            theme.convert_var=Entry(GuiConfig.window, width=50)
            theme.convert_var.place(x=160, y=60)
        
            GuiConfig.convert=IntVar()
        
            theme.convert_check=Checkbutton(GuiConfig.window, text="Convert", relief="raised", onvalue=1, offvalue=0, variable=GuiConfig.convert)
            theme.convert_check.place(x=70, y=57)
        
            GuiConfig.deconvert=IntVar()
        
            theme.deconvert_check=Checkbutton(GuiConfig.window, text="Deconvert", relief="raised", onvalue=1, offvalue=0, variable=GuiConfig.deconvert)
            theme.deconvert_check.place(x=70, y=17)

            theme.convert_butt=Button(GuiConfig.window, text="Go.", padx=5, pady=5, command=lambda:prep_convert(config, theme.convert_var, theme.deconvert_var, version, backupfunc))
            theme.convert_butt.place(x=70, y=120)

            theme.settings_butt=Button(GuiConfig.window, text="Settings", padx=5, pady=5, command=lambda:gui_settings(GuiConfig, config, theme, ))
            theme.settings_butt.place(x=115, y=120) 

            theme.exit_butt=Button(GuiConfig.window, text="Exit", pady=5, padx=5, command=lambda:ui_exit(config))
            theme.exit_butt.place(x=185, y=120)

            theme.show_last_convert_butt=Button(GuiConfig.window, text="Last Conversion", pady=5, padx=5, command=lambda:display_conversion)
            theme.show_last_convert_butt.place(x=235, y=120)

            GuiConfig.optionsvar=StringVar(GuiConfig.window)
            GuiConfig.optionsvar.set("Hex")
            theme.options=OptionMenu(GuiConfig.window, GuiConfig.optionsvar, "Hex", "Pseudo Hex", "Binary", "Pseudo Binary", "Legacy Pseudo Binary", "ascii", "brainfuck", "base64", "symbenc")
            theme.options.place(x=220, y=160)
        
        elif config.language=="de":
            theme.deconvert_msg=Label(GuiConfig.window, text="Text zum deconvertieren:", padx=5, pady=5)
            theme.deconvert_msg.place(x=160, y=0)

            theme.convert_msg=Label(GuiConfig.window, text="Text zu konvertieren:", padx=5, pady=5)
            theme.convert_msg.place(x=160, y=35)

            theme.deconvert_var=Entry(GuiConfig.window, width=50)
            theme.deconvert_var.place(x=160, y=20)

            theme.convert_var=Entry(GuiConfig.window, width=50)
            theme.convert_var.place(x=160, y=60)
        
            GuiConfig.convert=IntVar()
        
            theme.convert_check=Checkbutton(GuiConfig.window, text="Konvert", relief="raised", onvalue=1, offvalue=0, variable=GuiConfig.convert)
            theme.convert_check.place(x=80, y=57)
        
            GuiConfig.deconvert=IntVar()
        
            theme.deconvert_check=Checkbutton(GuiConfig.window, text="Dekonvertieren", relief="raised", onvalue=1, offvalue=0, variable=GuiConfig.deconvert)
            theme.deconvert_check.place(x=40, y=17)

            theme.convert_butt=Button(GuiConfig.window, text="Start", padx=5, pady=5, command=lambda:prep_convert(config, theme.convert_var, theme.deconvert_var, version, backupfunc))
            theme.convert_butt.place(x=70, y=120)

            theme.settings_butt=Button(GuiConfig.window, text="Einstellungen", padx=5, pady=5, command=lambda:gui_settings(GuiConfig, config, theme, ))
            theme.settings_butt.place(x=120, y=120) 

            theme.exit_butt=Button(GuiConfig.window, text="Exit", pady=5, padx=5, command=lambda:ui_exit(config))
            theme.exit_butt.place(x=217, y=120)

            theme.show_last_convert_butt=Button(GuiConfig.window, text="Letzte Konvertierung", pady=5, padx=5, command=lambda:display_conversion)
            theme.show_last_convert_butt.place(x=262, y=120)

            GuiConfig.optionsvar=StringVar(GuiConfig.window)
            GuiConfig.optionsvar.set("Hex")
            theme.options=OptionMenu(GuiConfig.window, GuiConfig.optionsvar, "Hex", "Pseudo Hex", "Binary", "Pseudo Binary", "Legacy Pseudo Binary", "ascii", "brainfuck", "base64", "symbenc")
            theme.options.place(x=220, y=160)

        GuiConfig.window.after(5, lambda:set_theme(config))
        GuiConfig.window.after(5, lambda:start_thread(config, sysinf, version, backupfunc))
        GuiConfig.window.after(25, lambda:GuiConfig.window.attributes("-topmost", False))

        GuiConfig.window.mainloop()
    except AttributeError:
        return

def set_theme(config):
    if config.theme.lower()=="bright":
        GuiConfig.window.config(bg="#EFEFEF")
        theme.deconvert_msg.config(bg="#EFEFEF")
        theme.convert_msg.config(bg="#EFEFEF")
        theme.deconvert_var.config(bg="#EFEFEF")
        theme.convert_var.config(bg="#EFEFEF")
        theme.convert_check.config(bg="#EFEFEF", selectcolor="#EFEFEF")
        theme.deconvert_check.config(bg="#EFEFEF", selectcolor="#EFEFEF")
        theme.convert_butt.config(bg="#EFEFEF")
        theme.settings_butt.config(bg="#EFEFEF")
        theme.exit_butt.config(bg="#EFEFEF")
        theme.options.config(bg="#EFEFEF")
        theme.show_last_convert_butt.config(bg="#EFEFEF")
    elif config.theme.lower()=="dark":
        GuiConfig.window.config(bg="#1F1F1F")
        theme.deconvert_msg.config(bg="#1F1F1F", fg="#FFFFFF")
        theme.convert_msg.config(bg="#1F1F1F", fg="#FFFFFF")
        theme.deconvert_var.config(bg="#1F1F1F", fg="#FFFFFF")
        theme.convert_var.config(bg="#1F1F1F", fg="#FFFFFF")
        theme.convert_check.config(bg="#1F1F1F", fg="#FFFFFF", selectcolor="#333333")
        theme.deconvert_check.config(bg="#1F1F1F", fg="#FFFFFF", selectcolor="#333333")
        theme.convert_butt.config(bg="#1F1F1F", fg="#FFFFFF")
        theme.settings_butt.config(bg="#1F1F1F", fg="#FFFFFF")
        theme.exit_butt.config(bg="#1F1F1F", fg="#FFFFFF")
        theme.options.config(bg="#1F1F1F", fg="#FFFFFF")
        theme.options["menu"].config(bg="#1F1F1F", fg="#FFFFFF")
        theme.show_last_convert_butt.config(bg="#1F1F1F", fg="#FFFFFF")
    elif config.theme.lower()=="violet":
        GuiConfig.window.config(bg="#7F00FF")
        theme.deconvert_msg.config(bg="#7F00FF", fg="#00FF00")
        theme.convert_msg.config(bg="#7F00FF", fg="#00FF00")
        theme.deconvert_var.config(bg="#7F00FF", fg="#00FF00")
        theme.convert_var.config(bg="#7F00FF", fg="#00FF00")
        theme.convert_check.config(bg="#7F00FF", fg="#00FF00", selectcolor="#7F00FF")
        theme.deconvert_check.config(bg="#7F00FF", fg="#00FF00", selectcolor="#7F00FF")
        theme.convert_butt.config(bg="#7F00FF", fg="#00FF00")
        theme.settings_butt.config(bg="#7F00FF", fg="#00FF00")
        theme.exit_butt.config(bg="#7F00FF", fg="#00FF00")
        theme.options.config(bg="#7F00FF", fg="#00FF00")
        theme.options["menu"].config(bg="#7F00FF", fg="#00FF00")
        theme.show_last_convert_butt.config(bg="#7F00FF", fg="#00FF00")

    return

def display_conversion():
    ctypes.windll.user32.MessageBoxW(0, GuiConfig.converted, "Converted data", 0)

def prep_convert(config, convert_var, deconvert_var, version, backupfunc):
    try:
        if GuiConfig.convert.get()==1:
            convert_mode="convert"
            GuiConfig.converted=parse_input(config, guimode=convert_mode, mode=GuiConfig.optionsvar.get().lower(), convdata=convert_var.get())
    
        if GuiConfig.deconvert.get()==1:
            convert_mode="deconvert"
            GuiConfig.converted=parse_input(config, guimode=convert_mode, mode=GuiConfig.optionsvar.get().lower(), convdata=deconvert_var.get())
    
        ctypes.windll.user32.MessageBoxW(0, GuiConfig.converted, "Converted data", 0)
    except:
        error=traceback.format_exc()
        if version.release==False:
            print(f"An error happened, there is a traceback:\n{error}")
            text=f"An error happened, there is a traceback:\n{error}"
        if version.release==True:
            text=f"An error happened, there is a traceback:\n{error}"
            ctypes.windll.user32.MessageBoxW(0, error, "Error", 0)
        if modules.logg_module==True:
            log_error(text=text)
        else:
            backupfunc.backup_logg(mode="logg", text=text)

def start_thread(config, sysinf, version, backupfunc):
    GuiConfig.stop_event=threading.Event()
    title_thread=threading.Thread(target=title_time, args=(config, sysinf, version, backupfunc, ))
    title_thread.start()
    return

def title_time(config, sysinf, version, backupfunc):
    try:
        while not GuiConfig.stop_event.set():
            now=datetime.datetime.now()
            start=time.time()
            if config.language=="de":
                if version.release==True:
                    GuiConfig.window.title(f"Text Converter GUI V{version.version} {now.strftime("%d/%m/%Y, %H:%M:%S")}")
                else:
                    GuiConfig.window.title(f"Text Converter GUI Beta V{version.beta_version} {now.strftime("%d/%m/%Y, %H:%M:%S")}")

            else:
                if version.release==True:
                    GuiConfig.window.title(f"Text Converter GUI V{version.version} {now.strftime("%m/%d/%Y, %r")}")
                else:
                    GuiConfig.window.title(f"Text Converter GUI Beta V{version.beta_version} {now.strftime("%m/%d/%Y, %r")}")

            elapsed_time=time.time()-start
            wait_time=max(0.5, elapsed_time * 2)
            time.sleep(wait_time)
    
    except:
        error=traceback.format_exc()
        if version.release==False:
            print(f"An error happened, there is a traceback:\n{error}")
            text=f"An error happened, there is a traceback:\n{error}"
        if version.release==True:
            text=f"An error happened, there is a traceback:\n{error}"
            ctypes.windll.user32.MessageBoxW(0, error, "Error", 0)

        if modules.logg_module==True:
            log_error(text=text)
        else:
            backupfunc.backup_logg(mode="logg", text=text)

def ui_exit(config):
    result=ctypes.windll.user32.MessageBoxW(0, "If you press Ok, the Program will close, but if you press Cancel it stays open.", "Do you wanna close that?", 1)
    if result == 1:
        #stop_event.set()
        GuiConfig.stop_event.set()
        GuiConfig.window.destroy()
        config.gui=False
        return
    else:
        return

if __name__=="__main__":
    input("This is a module, Please don't run it on it's own!")
    exit()