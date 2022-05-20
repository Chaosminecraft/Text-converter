from datetime import datetime
from logger import log_info
language="de"
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
