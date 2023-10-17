import logging
from datetime import *
import os

def log_init(logg):
    try:
        now=datetime.now()
        time=now.strftime("%d.%m.%Y %H.%M.%S")
        logging.basicConfig(filename=f"logs/{time} logg.txt", filemode="w", level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%d/%m/%Y %H:%M:%S")
        return
    except FileNotFoundError:
        os.mkdir("logs")
        log_init(logg)

def log_system(text):
    text=f"[SYSTEM] {text}"
    logging.info(text)
    return

def log_info(text, logg):
    if text!="the user entered: ":
        if logg==True:
            text=f"[INFO] {text}"
            logging.info(text)
            return
        if logg==False:
            return

def log_warn(text, logg):
    if logg==True:
        text=f"[WARNING] {text}"
        logging.info(text)
        return
    if logg==False:
        return

def log_error(text, logg):
    if logg==True:
        text=f"[ERROR] {text}"
        logging.info(text)
        return
    if logg==False:
        return
