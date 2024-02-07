#importing the needed modules
import requests
import logger

#Variables for the code
link="https://github.com/Chaosminecraft/Text-converter/releases/"

#the main function of that code
def update(release, language, version):
    #print(version) #also debugging, can be optionally removed.
    try: #Trying to Check for updates
        if release==True:
            url = "https://www.dropbox.com/s/h9cwtlx43bkbro2/version.txt?dl=1"
            new_version = requests.get(url, allow_redirects=True)
            new_version=str(new_version.content)[2:5]
            #print(new_version) #debug purpose

                
            if new_version>version:
                if language == "en":
                    print(f"\nThere is an new version: {new_version}\nThere is download the link:↓\n{link}\n")

                elif language == "de":
                    print(f"\nDa ist eine neue Version: {new_version}\nDa ist der link zum herunterladen:↓\n{link}\n")

                elif language!="de" or language !="en":
                    print(f"\nThere is an new version: {new_version}\nThere is the download link:↓\n{link}\n")
                return

            elif new_version==version:
                if language == "en":
                    print(f"\nThe version is the latest version at the moment.\n")

                elif language == "de":
                    print(f"\nDas ist die neuste version im moment.\n")

                elif language!="de" and language !="en":
                    print(f"\nThe version is the latest version at the moment.\n")
                return
                
            elif new_version<version:
                if language == "en":
                    print(f"\nAre you a Dev?\n")

                elif language == "de":
                    print(f"\nBist du ein dev?\n")

                elif language !="de" and language !="en":
                    print(f"\nAre you a Dev?\n")
                return

            else:
                if language == "en":
                    print(f"\nUNKNOWN VERSION.\n")

                if language == "de":
                    print(f"\nUNBEKANNTE VERSION\n")
                    
                if language !="de" or language !="en":
                    print(f"\nUNKNOWN VERSION.\n")
                return
        
        if release==False:
            url="https://www.dropbox.com/s/a5wc7oon68nz9io/version-beta.txt?dl=1"
            new_version = requests.get(url, allow_redirects=True)
            new_version=str(new_version.content)[2:5]
            #print(new_version)#for debugging
            
            if new_version>version:
                if language == "en":
                        print(f"\nThere is an new beta version: {new_version}\nThere is download the link:↓\n{link}\n")

                elif language == "de":
                    print(f"\nDa ist eine neue beta version: {new_version}\nDa ist der link zum herunterladen:↓\n{link}\n")

                elif language !="de" or language !="en":
                    print(f"\nThere is an new beta version: {new_version}\nThere is the download link:↓\n{link}\n")
                return
            
            elif new_version==version:
                if language == "en":
                        print(f"\nThe version is the latest beta version at the moment.\n")

                elif language == "de":
                    print(f"\nDas ist die neuste beta version im moment.\n")

                elif language !="de" or language !="en":
                    print(language)
                    print(f"\nThe version is the latest beta version at the moment.\n")
                return
            
            else:
                if language == "en":
                    print(f"\nUNKNOWN BETA VERSION\n")

                elif language == "de":
                    print(f"\nUNBEKANNTE BETA VERSION\n")
                    
                elif language !="de" or language !="en":
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

def test():
    while True:
        language=input("DE/EN ").lower()
        release=input("TRUE/FALSE ").lower()
        if release=="true":
            release=True
        if release=="false":
            release=False
        version=input("VER: ")
        update(release, language, version)
#test()
