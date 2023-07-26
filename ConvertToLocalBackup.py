#importing the Needed modules
import base64

data =  open("converter.py", "rb").read()

string=base64.b64encode(data)

with open("connverter.txt", "wb") as save:
    save.write(string)

data =  open("learn.py", "rb").read()

string=base64.b64encode(data)

with open("learn.txt", "wb") as save:
    save.write(string)

data =  open("logger.py", "rb").read()

string=base64.b64encode(data)

with open("logger.txt", "wb") as save:
    save.write(string)

data =  open("settings.py", "rb").read()

bestringtwee=base64.b64encode(data)

with open("settings.txt", "wb") as save:
    save.write(string)

data =  open("timeread.py", "rb").read()

string=base64.b64encode(data)

with open("timeread.txt", "wb") as save:
    save.write(string)

data =  open("updater.py", "rb").read()

string=base64.b64encode(data)

with open("updater.txt", "wb") as save:
    save.write(string)