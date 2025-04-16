import logging, datetime, os

def log_init(config):
    if not os.path.exists('logs'):
        os.mkdir('logs')
    loggfile=datetime.datetime.now().strftime("%d.%m.%Y %H.%M.%S")
    logg_path=f"logs/{loggfile} logg.txt"
    logging.basicConfig(filename=logg_path, filemode="w", level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%d/%m/%Y %H:%M:%S")
    config.log_name=logg_path
    return

def log_system(text):
    logging.info(f'[SYSTEM] {text}')
    return

def log_info(config, text):
    if config.logg==True:
        logging.info(f'[INFO] {text}')
    
    return

def log_warn(text):
    logging.warning(f'[WARNING] {text}')
    return

def log_error(text):
    logging.error(f'[ERROR] {text}')
    return

if __name__=="__main__":
    input("Please don't open that file on it's own. This is a module!")
    exit()