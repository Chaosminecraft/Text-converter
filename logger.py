import logging
from datetime import *
import os

def log_init():
    try:
        now=datetime.now()
        time=now.strftime("%d.%m.%Y %H.%M.%S")
        logging.basicConfig(filename=f"logs/{time} logg.txt", filemode="w", level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%d/%m/%Y %H:%M:%S")
        return
    except FileNotFoundError:
        os.mkdir("logs")
        log_init()

def log_info(text, logg):
    if logg=="yes":
        logging.info(text)
        return
    if logg=="no":
        return

def log_warn(text, logg):
    if logg=="yes":
        logging.warn(text)
        return
    if logg=="no":
        return

def log_error(text, logg):
    if logg=="yes":
        logging.error(text)
        return
    if logg=="no":
        return
