#importing the needed modules
import requests
import os

#Variables for the code
link="https://github.com/Chaosminecraft/Text-converter/releases/"
rversion="2.3"
bversion="2.3"

#the main function of that code
def update(release, language):
    try: #Trying to Check for updates
        if release=="true":
                url = "https://www.dropbox.com/s/a5wc7oon68nz9io/version-beta.txt?dl=1"
                new_version = requests.get(url, allow_redirects=True)
                open("release-version.txt", "wb").write(new_version.content)
                
                if new_version>rversion:
                    if language.lower() == "en":
                        print(f"\nThere is an new version: {new_version}\nThere is download the link:↓\n{link}\n")

                    if language.lower() == "de":
                        print(f"\nDa ist eine neue Version: {new_version}\nDa ist der link zum herunterladen:↓\n{link}\n")

                    else:
                        print(f"\nThere is an new version: {new_version}\nThere is the download link:↓\n{link}\n")

                if new_version==rversion:
                    if language.lower() == "en":
                        print(f"\nThe version is the latest version at the moment.\n")

                    if language.lower() == "de":
                        print(f"\nDas ist die neuste version im moment.\n")

                    else:
                        print(f"\nThe version is the latest version at the moment.\n")

                else:
                    if language.lower() == "en":
                        print(f"\nUNKNOWN VERSION.\n")

                    if language.lower() == "de":
                        print(f"\nUNBEKANNTE VERSION\n")
                    
                    else:
                        print(f"\nUNKNOWN VERSION.\n")
                
                return
        
        if release=="false":
            url="https://www.dropbox.com/s/a5wc7oon68nz9io/version-beta.txt?dl=1"
            new_version=requests.get(url, allow_redirects=True)
            open("beta-version.txt", "wb").write(new_version.content)
            
            if new_version>bversion:
                if language.lower() == "en":
                        print(f"\nThere is an new beta version: {new_version}\nThere is download the link:↓\n{link}\n")

                if language.lower() == "de":
                    print(f"\nDa ist eine neue beta version: {new_version}\nDa ist der link zum herunterladen:↓\n{link}\n")

                else:
                    print(f"\nThere is an new beta version: {new_version}\nThere is the download link:↓\n{link}\n")
            
            if new_version==bversion:
                if language.lower() == "en":
                        print(f"\nThe version is the latest beta version at the moment.\n")

                if language.lower() == "de":
                    print(f"\nDas ist die neuste beta version im moment.\n")

                else:
                    print(f"\nThe version is the latest version at the moment.\n")
            
            else:
                if language.lower() == "en":
                    print(f"\nUNKNOWN BETA VERSION\n")

                if language.lower() == "de":
                    print(f"\nUNBEKANNTE BETA VERSION\n")
                    
                else:
                    print(f"\nUNKNOWN BETA VERSION\n")
            return

    #No internet Connection found, update Checking can't be done.
    except requests.exceptions.ConnectionError: #thanks TizzySaurus for helping me getting that catch. :)
        
        if language=="en":
            print(f"\nCurrently there is no internet, Try checking for updates later when a internet connection exists/is stable.\n")
            
        if language=="de":
            print(f"\nMomentan ist da kein internet, Versuch es später nochmal wenn die Internetverbindung da ist/Stabil ist.\n")
            
        else:
            print(f"\nCurrently there is no internet, Try checking for updates later when a internet connection exists/is stable.\n")
            
        return

def Test():
    while True:
        language=input("DE/EN").lower()
        release=input("TRUE/FALSE").lower()
        update(release, language)

#Test()