import logging
from datetime import *
import os

def log_init(logg_makefile):
    try:
        if logg_makefile=="true":
            now=datetime.now()
            time=now.strftime("%d.%m.%Y %H.%M.%S")
            logging.basicConfig(filename=f"logs/{time} logg.txt", filemode="w", level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%d/%m/%Y %H:%M:%S")
            return
        if logg_makefile=="false":
            return
    except FileNotFoundError:
        os.mkdir("logs")
        log_init(logg_makefile)

def log_system(text, logg):
    if logg=="true":
        text=f"[SYSTEM] {text}"
        logging.info(text)
        return
    if logg=="false":
        return

def log_info(text, logg):
    if logg=="true":
        text=f"[INFO] {text}"
        logging.info(text)
        return
    if logg=="false":
        return

def log_warn(text, logg):
    if logg=="true":
        text=f"[WARNING] {text}"
        logging.warn(text)
        return
    if logg=="false":
        return

def log_error(text, logg):
    if logg=="true":
        text=f"[ERROR] {text}"
        logging.error(text)
        return
    if logg=="false":
        return
