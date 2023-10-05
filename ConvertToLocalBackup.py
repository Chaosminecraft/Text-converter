#importing the Needed modules
import base64

data =  open("converter.py", "rb").read()

string=base64.b64encode(data)

with open("text/connverter.txt", "wb") as save:
    save.write(string)

data =  open("learn.py", "rb").read()

string=base64.b64encode(data)

with open("text/learn.txt", "wb") as save:
    save.write(string)

data =  open("logger.py", "rb").read()

string=base64.b64encode(data)

with open("text/logger.txt", "wb") as save:
    save.write(string)

data =  open("settings.py", "rb").read()

bestringtwee=base64.b64encode(data)

with open("text/settings.txt", "wb") as save:
    save.write(string)

data =  open("timeread.py", "rb").read()

string=base64.b64encode(data)

with open("text/timeread.txt", "wb") as save:
    save.write(string)

data =  open("updater.py", "rb").read()

string=base64.b64encode(data)

with open("text/updater.txt", "wb") as save:
    save.write(string)