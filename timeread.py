import os
import sys as syst
from time import  sleep
from datetime import datetime

from logger import log_info

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

def title_time(stop_event, language):
    sys=open("system.txt", "r").read()
    while not stop_event.is_set():
        if sys=="Windows":
            now=datetime.now()
            if language=="de":
                now=now.strftime("%d/%m/%Y, %H:%M:%S")
            if language=="en":
                now=now.strftime("%m/%d/%Y, %r")

            os.system(f"title Text Converter V2.3 {now}")
            sleep(1)

        if sys=="Linux":
            now=datetime.now()
            now=now.strftime("%d/%m/%Y, %H:%M:%S")
            syst.stdout.write(f"\x1b]2;Text Converter V2.3 {now}\x07")
            #print("Time Updated") somehow that fixes the title...
            sleep(1)
    #exit()
