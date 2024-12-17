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

def log_info(**kwargs):
    if kwargs["logg"]==True:
        text=f"[INFO] {kwargs["text"]}"
        logging.info(text)
        return
    if kwargs["logg"]==False:
        return

def log_warn(**kwargs):
    if kwargs["logg"]==True:
        text=f"[WARNING] {kwargs["text"]}"
        logging.info(text)
        return
    if kwargs["logg"]==False:
        return

def log_error(text):
    text=f"[ERROR] {text}"
    logging.info(text)
    return
