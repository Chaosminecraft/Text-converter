import os, traceback
import sys as syst
from time import  sleep
from datetime import datetime

from logger import log_info, log_system

class timesetting:
    delay=0.125

def timereader(language, logg):
    if language == "en":
        now=datetime.now()
        print(f"\nThe time is:", now.strftime("%m/%d/%Y, %r"), "\n")

        text=datetime.now()
        text=text.strftime("%m/%d/%Y, %r")
        log_info(text, logg)

        return

    if language == "de":
        now=datetime.now()
        print(f"\nDie zeit ist:", now.strftime("%d/%m/%Y, %H:%M:%S"), "\n")

        
        text=datetime.now()
        text=text.strftime("%d/%m/%Y, %H:%M:%S")
        log_info(text, logg)

        return

def title_time(settings, system, stop_event):
    try:
        if system=="Windows":
            while not stop_event.is_set():
                now=datetime.now()
                if settings.language=="de":
                    now=now.strftime("%d/%m/%Y, %H:%M:%S") #%H:%M:%S.%f
                if settings.language=="en":
                    now=now.strftime("%m/%d/%Y, %r")

                os.system(f"title Text Converter V2.3 {now}")
                sleep(timesetting.delay)
                


        if system=="Linux":
            syst.stdout.write(f"\x1b]2;Text Converter V2.3\x07")
            return
                
    except:
        traced=traceback.format_exc()
        print(f"There has been an exception:\n{traced}")
        text=f"There has been an exception:\n{traced}"
        log_system(text)
        if system=="Linux":
            syst.stdout.write(f"\x1b]2;Text Converter V2.3\x07")
        if system=="Windows":
            os.system(f"title Text Converter V2.3")
        return

if __name__=="__main__":
    print("That file isn't designed to run on it's own. It is supposed to be a module.")